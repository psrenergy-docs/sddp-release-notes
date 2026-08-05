#!/usr/bin/env python3
"""Check the links in the SDDP release-notes docs, report on them, and
optionally hide broken ones / restore revived ones.

Usage
-----
    python tools/check_links.py                     # check + print report
    python tools/check_links.py --report FILE.md    # also write a markdown report
    python tools/check_links.py --json FILE.json    # also write machine-readable results
    python tools/check_links.py --fix               # hide broken links, restore revived ones
    python tools/check_links.py --offline           # only check internal links (no network)
    python tools/check_links.py --only-internal / --only-external

Exit codes: 0 = nothing broken, 1 = broken links found, 2 = usage/IO error.

How hiding works
----------------
A broken link is wrapped in an HTML comment carrying a machine-readable marker,
so Jekyll stops rendering it but nothing is lost:

    <!--broken-link status=404 checked=2026-08-04
    [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.1-setup-linux.bin)
    -->

On a later run, every link inside such a marker is re-checked. Once it answers
OK the marker is removed and the original text is restored verbatim. Links are
only hidden on a definitive "does not exist" answer -- a timeout, a DNS failure
or an auth wall never hides anything.

Auth-gated download links
-------------------------
Every `psr-inc.com/app/link/?t=d&f=...` URL is a URL builder that redirects to
the PSR login page whether or not the file exists, so anonymously it cannot be
verified and is reported as AUTH (never hidden). To verify them, supply a session
cookie -- easiest via `python tools/psr_login.py`, which opens Chrome, waits for
you to sign in and writes the cookie to `.psr-cookie` (git-ignored).

The cookie is looked up in this order:
    1. the PSR_COOKIE environment variable
    2. the `.psr-cookie` file at the repo root

With a cookie the script follows the redirect chain and treats a real file
download (binary content-type / attachment) as OK, and an error page as BROKEN.
"""

from __future__ import annotations

import argparse
import codecs
import concurrent.futures
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
COOKIE_FILE = os.path.join(REPO_ROOT, ".psr-cookie")

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0 Safari/537.36 sddp-link-checker/1.0"
)

# --------------------------------------------------------------------------
# statuses
# --------------------------------------------------------------------------
OK = "OK"            # link resolves -> restore it if it is currently hidden
BROKEN = "BROKEN"     # link definitively does not exist -> hide it
AUTH = "AUTH"        # behind a login wall, existence not observable -> leave alone
ERROR = "ERROR"      # network/transport problem, inconclusive -> leave alone
SKIPPED = "SKIPPED"   # not checkable by design (mailto:, pure anchor, ...)

# Only these two statuses ever cause an edit.
HIDE_ON = {BROKEN}
RESTORE_ON = {OK}

# --------------------------------------------------------------------------
# link extraction
# --------------------------------------------------------------------------
MD_LINK_RE = re.compile(r"\[(?P<text>[^\[\]]*)\]\((?P<url>[^()\s]+)\)")
HTML_HREF_RE = re.compile(r"""href\s*=\s*['"](?P<url>[^'"]+)['"]""")
JS_REDIRECT_RE = re.compile(r"""location\.href\s*=\s*['"](?P<url>[^'"]+)['"]""")
YAML_URL_RE = re.compile(r"^\s*url:\s*['\"]?(?P<url>[^'\"\s#]+)")

# `\|` is how the docs escape a pipe used as a visual separator between links.
SEPARATOR_LINES = {r"\|", "|", "&#124;", r"\\|"}
SEP_AFTER_RE = re.compile(r"^\s*\\?\|")
SEP_BEFORE_RE = re.compile(r"\\?\|\s*$")
# Punctuation and list markers do not count as content when deciding whether a
# line holds anything besides links.
PLUMBING_RE = re.compile(r"[\s*\-+()\[\]|\\]")

# --------------------------------------------------------------------------
# hidden-link markers
# --------------------------------------------------------------------------
MARKER = "broken-link"
# Whole-line form. `[^\n>]*` keeps the meta from swallowing a `-->`.
BLOCK_MARKER_RE = re.compile(
    r"^[ \t]*<!--" + MARKER + r"(?P<meta>[^\n>]*)\n(?P<body>.*?)\n[ \t]*-->[ \t]*$",
    re.DOTALL | re.MULTILINE,
)
# Partial-line form: <!--broken-link status=404 checked=... :: [Eng](url)-->
INLINE_MARKER_RE = re.compile(
    r"<!--" + MARKER + r"(?P<meta>[^\n>]*?):: (?P<body>[^\n]*?)-->"
)


class Link:
    """One link occurrence in one file."""

    __slots__ = ("file", "line", "url", "text", "kind", "hidden", "status", "detail")

    def __init__(self, file, line, url, text, kind, hidden=False):
        self.file = file      # repo-relative path, forward slashes
        self.line = line      # 1-based line number
        self.url = url
        self.text = text
        self.kind = kind      # "internal" | "external" | "gated" | "config"
        self.hidden = hidden  # currently inside a broken-link marker?
        self.status = None
        self.detail = ""

    def __repr__(self):
        return f"<Link {self.status} {self.file}:{self.line} {self.url}>"


# --------------------------------------------------------------------------
# file IO that preserves CRLF and BOM (the docs are CRLF)
# --------------------------------------------------------------------------
def read_text(path):
    raw = open(path, "rb").read()
    bom = raw.startswith(codecs.BOM_UTF8)
    if bom:
        raw = raw[len(codecs.BOM_UTF8):]
    text = raw.decode("utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    return text.replace("\r\n", "\n"), newline, bom


def write_text(path, text, newline, bom):
    data = text.replace("\n", newline).encode("utf-8")
    if bom:
        data = codecs.BOM_UTF8 + data
    with open(path, "wb") as fh:
        fh.write(data)


def rel(path):
    return os.path.relpath(path, REPO_ROOT).replace("\\", "/")


# --------------------------------------------------------------------------
# discovery
# --------------------------------------------------------------------------
def doc_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(DOCS_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith((".", "_site"))]
        for name in sorted(filenames):
            if name.endswith((".md", ".markdown", ".html", ".yml", ".yaml")):
                out.append(os.path.join(dirpath, name))
    return sorted(out)


def front_matter_permalink(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    for line in text[3:end].splitlines():
        m = re.match(r"\s*permalink:\s*['\"]?(?P<v>[^'\"\s]+)", line)
        if m:
            return m.group("v")
    return None


def build_site_index():
    """Map every URL path the site can serve -> the file that serves it."""
    index = {}

    def add(key, path):
        index.setdefault(key.rstrip("/") or "/", path)

    for path in doc_files():
        if not path.endswith((".md", ".markdown", ".html")):
            continue
        stem = os.path.splitext(os.path.basename(path))[0]
        sub = os.path.dirname(rel(path))[len("docs"):].strip("/")
        prefix = "/" + sub + "/" if sub else "/"
        add(prefix + stem, path)
        add(prefix + stem + ".html", path)
        add(prefix + os.path.basename(path), path)
        try:
            text, _, _ = read_text(path)
        except OSError:
            continue
        permalink = front_matter_permalink(text)
        if permalink:
            add(permalink if permalink.startswith("/") else "/" + permalink, path)
    return index


# --------------------------------------------------------------------------
# classification
# --------------------------------------------------------------------------
GATED_RE = re.compile(r"^https?://(www\.)?psr-inc\.com/app/link/", re.I)


def classify(url, in_config):
    low = url.strip().lower()
    if low.startswith(("mailto:", "tel:", "javascript:", "data:", "#")):
        return None                    # nothing to verify
    if in_config:
        return "config" if not low.startswith(("http://", "https://")) else "external"
    if GATED_RE.match(url):
        return "gated"
    if low.startswith(("http://", "https://")):
        return "external"
    if low.startswith("//"):
        return "external"
    return "internal"


def extract_links(path):
    """All links in one file, tagging the ones already inside a broken-link marker."""
    text, _, _ = read_text(path)
    is_config = os.path.basename(path) in ("_config.yml", "_config.yaml")

    # Character offsets covered by our markers, so we can flag hidden links.
    hidden_spans = []
    for rx in (BLOCK_MARKER_RE, INLINE_MARKER_RE):
        for m in rx.finditer(text):
            hidden_spans.append(m.span())

    def is_hidden(pos):
        return any(a <= pos < b for a, b in hidden_spans)

    # offset -> line number
    line_starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            line_starts.append(i + 1)

    def line_of(pos):
        lo, hi = 0, len(line_starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if line_starts[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    found = []
    seen = set()

    def collect(rx, text_group=None):
        for m in rx.finditer(text):
            url = m.group("url").strip()
            key = (m.start("url"), url)
            if key in seen:
                continue
            seen.add(key)
            kind = classify(url, is_config)
            if kind is None:
                continue
            label = m.group(text_group) if text_group else ""
            found.append(
                Link(rel(path), line_of(m.start()), url, label, kind, is_hidden(m.start()))
            )

    if is_config:
        for i, line in enumerate(text.split("\n"), 1):
            for rx in (YAML_URL_RE, HTML_HREF_RE):
                m = rx.search(line)
                if m:
                    kind = classify(m.group("url"), True)
                    if kind:
                        found.append(Link(rel(path), i, m.group("url").strip(), "", kind))
    else:
        collect(MD_LINK_RE, "text")
        collect(JS_REDIRECT_RE)
        collect(HTML_HREF_RE)

    return found


# --------------------------------------------------------------------------
# checking
# --------------------------------------------------------------------------
def check_internal(link, site_index):
    target = link.url.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return SKIPPED, "fragment only"
    target = urllib.parse.unquote(target)

    if target.startswith("/"):
        key = target.rstrip("/") or "/"
        if key in site_index:
            return OK, "serves " + rel(site_index[key])
        return BROKEN, "no page serves " + target

    base = os.path.dirname(os.path.join(REPO_ROOT, link.file))
    candidate = os.path.normpath(os.path.join(base, target))
    for probe in (candidate, candidate + ".md", candidate + ".html"):
        if os.path.exists(probe):
            return OK, rel(probe)
    return BROKEN, "file not found: " + target


def _request(url, method, cookie, timeout, follow):
    req = urllib.request.Request(url, method=method)
    req.add_header("User-Agent", USER_AGENT)
    req.add_header("Accept", "*/*")
    if cookie:
        req.add_header("Cookie", cookie)

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **kw):
            return None

    handlers = [] if follow else [NoRedirect()]
    opener = urllib.request.build_opener(*handlers)
    try:
        with opener.open(req, timeout=timeout) as resp:
            return resp.status, resp.headers, resp.geturl()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.headers, exc.url or url


def check_external(link, cookie, timeout, retries):
    """A plain external URL: HEAD, fall back to GET, follow redirects."""
    last = ""
    for attempt in range(retries + 1):
        for method in ("HEAD", "GET"):
            try:
                status, headers, final = _request(link.url, method, cookie, timeout, True)
            except (urllib.error.URLError, OSError, ValueError) as exc:
                last = f"{type(exc).__name__}: {exc}"
                continue
            if status in (401, 403) and method == "HEAD":
                continue                      # some hosts refuse HEAD
            if status == 405 and method == "HEAD":
                continue
            if 200 <= status < 400:
                return OK, f"HTTP {status}"
            if status in (401, 403):
                return AUTH, f"HTTP {status} (access restricted)"
            if status in (404, 410):
                return BROKEN, f"HTTP {status}"
            last = f"HTTP {status}"
        if attempt < retries:
            continue
    return (ERROR, last or "no response")


def check_gated(link, cookie, timeout, retries):
    """psr-inc.com/app/link/?t=d&f=... -- only observable with a session cookie.

    HEAD is enough and, unlike GET, does not start transferring a 400 MB installer
    (the site actually answers 502 to a GET whose body is never read). Signed in,
    the redirect chain ends either on download.aspx with an attachment header, or
    on download/acessonegado.htm when the file cannot be served.
    """
    if not cookie:
        return AUTH, "login-gated download link (run tools/psr_login.py to verify)"

    filename = urllib.parse.parse_qs(urllib.parse.urlparse(link.url).query).get("f", [""])[0]
    last = ""
    for attempt in range(retries + 1):
        for method in ("HEAD", "GET"):
            try:
                status, headers, final = _request(link.url, method, cookie, timeout, True)
            except (urllib.error.URLError, OSError, ValueError) as exc:
                last = f"{type(exc).__name__}: {exc}"
                continue
            ctype = (headers.get("Content-Type") or "").lower()
            disp = (headers.get("Content-Disposition") or "").lower()
            length = headers.get("Content-Length", "?")
            low_final = (final or "").lower()

            if "acessonegado" in low_final:
                return BROKEN, f"not downloadable: {filename} (site answered acesso-negado)"
            if status in (404, 410) or "error404" in low_final:
                return BROKEN, f"HTTP {status} for {filename}"
            if "/login" in low_final or "login.asp" in low_final:
                return AUTH, "session cookie rejected or expired (run tools/psr_login.py)"
            if "attachment" in disp or filename.lower() in disp:
                return OK, f"download served ({length} bytes)"
            if ctype.startswith(("application/octet-stream", "application/zip",
                                 "application/x-zip", "binary/")):
                return OK, f"download served ({ctype}, {length} bytes)"
            # Signed in but the site answered with some other page: inconclusive,
            # so report ERROR rather than risk hiding a working link.
            last = f"HTTP {status} {ctype} -> {final}"
        if attempt < retries:
            time.sleep(1.0)
    return ERROR, last or "no response"


def load_cookie():
    """PSR session cookie from $PSR_COOKIE, else from the .psr-cookie file."""
    value = os.environ.get("PSR_COOKIE", "").strip()
    if not value and os.path.exists(COOKIE_FILE):
        try:
            with open(COOKIE_FILE, encoding="utf-8-sig") as fh:
                value = fh.read().strip()
        except OSError:
            return None
    # tolerate a whole header line being pasted in
    if value.lower().startswith("cookie:"):
        value = value.split(":", 1)[1].strip()
    return value or None


def check_all(links, args, site_index):
    """Resolve every distinct (kind, url) once, then fan the result back out."""
    cookie = load_cookie()
    results = {}

    internal = [l for l in links if l.kind in ("internal", "config")]
    remote = [l for l in links if l.kind in ("external", "gated")]

    if args.only_external:
        internal = []
    if args.only_internal or args.offline:
        remote = []

    for link in internal:
        results[(link.kind, link.url)] = check_internal(link, site_index)

    ext_todo, gated_todo = {}, {}
    for link in remote:
        bucket = gated_todo if link.kind == "gated" else ext_todo
        bucket.setdefault((link.kind, link.url), link)

    if args.no_downloads:
        for key in gated_todo:
            results[key] = (SKIPPED, "download link skipped (--no-downloads)")
        gated_todo = {}

    def run(item):
        (kind, url), sample = item
        if kind == "gated":
            return (kind, url), check_gated(sample, cookie, args.timeout, args.retries)
        return (kind, url), check_external(sample, cookie, args.timeout, args.retries)

    def sweep(todo, workers, label):
        if not todo:
            return
        done = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
            for key, res in pool.map(run, todo.items()):
                results[key] = res
                done += 1
                if not args.quiet and (done % 25 == 0 or done == len(todo)):
                    print(f"  {label}: {done}/{len(todo)}", file=sys.stderr)

    sweep(ext_todo, args.jobs, "external links")
    # The download endpoint starts answering "acessonegado" when it is hit hard,
    # and that is the very same answer it gives for a file that does not exist.
    # Keep the pressure low here.
    sweep(gated_todo, max(1, min(args.jobs, args.download_jobs)), "download links")

    # ...and never trust a single failure: re-test each one on its own, spaced
    # out. A genuinely missing file fails again; a throttled request does not.
    suspects = [k for k, (st, _) in results.items()
                if k[0] == "gated" and st == BROKEN]
    if suspects and not args.no_confirm:
        if not args.quiet:
            print(f"  confirming {len(suspects)} download failure(s), one at a time",
                  file=sys.stderr)
        for i, key in enumerate(suspects, 1):
            time.sleep(args.confirm_delay)
            status, detail = check_gated(gated_todo[key], cookie, args.timeout, 1)
            if status != BROKEN:
                detail += " [the bulk pass called this broken; not reproducible]"
            results[key] = (status, detail)
            if not args.quiet and (i % 10 == 0 or i == len(suspects)):
                print(f"    confirmed {i}/{len(suspects)}", file=sys.stderr)

    for link in links:
        status, detail = results.get((link.kind, link.url), (SKIPPED, "not checked"))
        link.status, link.detail = status, detail
    return links


# --------------------------------------------------------------------------
# hide / restore
# --------------------------------------------------------------------------
def urls_in(fragment):
    out = [m.group("url").strip() for m in MD_LINK_RE.finditer(fragment)]
    out += [m.group("url").strip() for m in JS_REDIRECT_RE.finditer(fragment)]
    out += [m.group("url").strip() for m in HTML_HREF_RE.finditer(fragment)]
    return out


def status_of(url, links):
    """Worst-case status for a URL across the whole run."""
    seen = {l.status for l in links if l.url == url}
    for s in (ERROR, AUTH, BROKEN, OK, SKIPPED):
        if s in seen:
            return s
    return None


def restore_pass(text, links, actions, path):
    """Remove markers whose links now all answer OK."""

    def handle(m, inline):
        body = m.group("body")
        urls = urls_in(body)
        if not urls:
            return m.group(0)
        statuses = [status_of(u, links) for u in urls]
        if all(s in RESTORE_ON for s in statuses):
            for u in urls:
                actions.append(("restored", path, u))
            return body
        return m.group(0)

    text = INLINE_MARKER_RE.sub(lambda m: handle(m, True), text)
    text = BLOCK_MARKER_RE.sub(lambda m: handle(m, False), text)
    return text


def hide_pass(text, links, actions, path, today):
    """Wrap still-broken, still-visible links in markers."""
    broken_urls = {l.url for l in links if l.file == path and l.status in HIDE_ON}
    if not broken_urls:
        return text

    reason = {}
    for l in links:
        if l.url in broken_urls and l.detail:
            reason.setdefault(l.url, l.detail)

    lines = text.split("\n")

    # Character ranges already wrapped in a marker -- those links stay put.
    marker_spans = [mm.span()
                    for rx in (BLOCK_MARKER_RE, INLINE_MARKER_RE)
                    for mm in rx.finditer(text)]

    def in_marker(pos):
        return any(a <= pos < b for a, b in marker_spans)

    # Collect, per line, the visible link spans and which of them are broken.
    per_line = {}
    offset = 0
    for idx, line in enumerate(lines):
        spans = [(m.start(), m.end(), m.group("url").strip())
                 for m in MD_LINK_RE.finditer(line)]
        spans += [(m.start(), m.end(), m.group("url").strip())
                  for m in JS_REDIRECT_RE.finditer(line)]
        spans = [s for s in spans if not in_marker(offset + s[0])]
        if spans:
            bad = [s for s in spans if s[2] in broken_urls]
            if bad:
                per_line[idx] = (spans, bad)
        offset += len(line) + 1

    consumed = set()
    out = list(lines)

    for idx in sorted(per_line, reverse=True):
        spans, bad = per_line[idx]
        line = out[idx]
        meta = f" status={_slug(reason.get(bad[0][2], 'broken'))} checked={today}"

        if line_is_only_links(line, bad, spans):
            # Nothing on this line but links and punctuation, so the whole line
            # can go -- together with the adjacent `\|` separator, which would
            # otherwise render as a stray pipe.
            start = end = idx
            nxt, prv = idx + 1, idx - 1
            if nxt < len(out) and nxt not in consumed and out[nxt].strip() in SEPARATOR_LINES:
                end = nxt
            elif prv >= 0 and prv not in consumed and out[prv].strip() in SEPARATOR_LINES:
                start = prv
            region = "\n".join(out[start:end + 1])
            if _marker_unsafe(region):
                actions.append(("skipped", path, bad[0][2]))
                continue
            indent = re.match(r"[ \t]*", out[start]).group(0)
            replacement = f"{indent}<!--{MARKER}{meta}\n{region}\n{indent}-->"
            out[start:end + 1] = [replacement]
            consumed.update(range(start, end + 1))
            for s in bad:
                actions.append(("hidden", path, s[2]))
        else:
            # There is real text on this line -- a fix, a feature, a date -- so
            # only the links themselves come out, never the prose around them.
            new_line = line
            for s_start, s_end, urls in sorted(removal_intervals(line, bad),
                                               key=lambda iv: iv[0], reverse=True):
                original = line[s_start:s_end]
                if _marker_unsafe(original):
                    for url in urls:
                        actions.append(("skipped", path, url))
                    continue
                m2 = (f" status={_slug(reason.get(urls[0], 'broken'))}"
                      f" checked={today}")
                new_line = (new_line[:s_start]
                            + f"<!--{MARKER}{m2} :: {original}-->"
                            + new_line[s_end:])
                for url in urls:
                    actions.append(("hidden-inline", path, url))
            out[idx] = new_line
            consumed.add(idx)

    return "\n".join(out)


def line_is_only_links(line, bad, spans):
    """True when the line carries nothing but links and punctuation.

    Only then may the whole line be hidden. If any prose survives -- a bug fix,
    a feature, a release date -- the line stays and just the links come out.
    """
    if len(bad) != len(spans):
        return False
    residue = line
    for s_start, s_end, _ in sorted(spans, key=lambda s: s[0], reverse=True):
        residue = residue[:s_start] + residue[s_end:]
    return not PLUMBING_RE.sub("", residue)


def removal_intervals(line, bad):
    """Slices to hide, as (start, end, [urls]).

    Each broken link takes with it the `\\|` that binds it to a neighbour, so
    hiding one of several links leaves no dangling separator. And when the links
    sat inside a `(...)` group that is now empty, the brackets go too -- otherwise
    the page renders a bare `( )`.
    """
    ordered = sorted(bad, key=lambda s: s[0])
    intervals = []
    cursor = 0
    for s_start, s_end, url in ordered:
        start, end = s_start, s_end
        after = SEP_AFTER_RE.match(line[end:])
        if after:
            end += after.end()
        else:
            before = SEP_BEFORE_RE.search(line[cursor:start])
            if before:
                start = cursor + before.start()
        intervals.append((max(start, cursor), end, [url]))
        cursor = end
    return absorb_empty_group(line, intervals)


def absorb_empty_group(line, intervals):
    """Merge the intervals and take the enclosing brackets when nothing is left
    between them -- `Release notes ([Eng] \\| [Esp])` must not become
    `Release notes ( )`."""
    if not intervals:
        return intervals
    start = min(s for s, _, _ in intervals)
    end = max(e for _, e, _ in intervals)

    covered = set()
    for s, e, _ in intervals:
        covered.update(range(s, e))
    between = "".join(ch for i, ch in enumerate(line[start:end], start)
                      if i not in covered)
    if between.strip():
        return intervals            # something visible survives between them

    opener = re.search(r"\s*\(\s*$", line[:start])
    closer = re.match(r"^\s*\)", line[end:])
    if not (opener and closer):
        return intervals

    urls = [u for _, _, group in intervals for u in group]
    return [(opener.start(), end + closer.end(), urls)]


def _slug(detail):
    m = re.search(r"HTTP\s+(\d{3})", detail)
    if m:
        return m.group(1)
    return re.sub(r"[^a-z0-9]+", "-", detail.lower()).strip("-")[:40] or "broken"


def _marker_unsafe(fragment):
    return "<!--" in fragment or "-->" in fragment


def apply_fixes(links, today):
    actions = []
    for path in doc_files():
        relpath = rel(path)
        if os.path.basename(path) in ("_config.yml", "_config.yaml"):
            continue                      # never rewrite the nav config automatically
        if not any(l.file == relpath for l in links):
            continue
        text, newline, bom = read_text(path)
        updated = restore_pass(text, links, actions, relpath)
        updated = hide_pass(updated, links, actions, relpath, today)
        if updated != text:
            write_text(path, updated, newline, bom)
    return actions


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------
ORDER = [BROKEN, ERROR, AUTH, OK, SKIPPED]


def summarize(links):
    counts = {s: 0 for s in ORDER}
    for l in links:
        counts[l.status] = counts.get(l.status, 0) + 1
    return counts


def print_report(links, counts, actions, today, fixed):
    total_urls = len({(l.kind, l.url) for l in links})
    print()
    print("=" * 72)
    print(f"SDDP release-notes link check -- {today}")
    print("=" * 72)
    print(f"{len(links)} link occurrences / {total_urls} distinct URLs "
          f"in {len({l.file for l in links})} files")
    print()
    for s in ORDER:
        if counts.get(s):
            print(f"  {s:<8} {counts[s]:>5}")
    print()

    broken = [l for l in links if l.status == BROKEN]
    if broken:
        print("-" * 72)
        print("BROKEN LINKS")
        print("-" * 72)
        for l in sorted(broken, key=lambda l: (l.file, l.line)):
            flag = " [currently hidden]" if l.hidden else ""
            print(f"  {l.file}:{l.line}{flag}")
            print(f"      {l.url}")
            print(f"      -> {l.detail}")
        print()

    revived = [l for l in links if l.hidden and l.status == OK]
    if revived:
        print("-" * 72)
        print("HIDDEN LINKS THAT NOW WORK")
        print("-" * 72)
        for l in sorted(revived, key=lambda l: (l.file, l.line)):
            print(f"  {l.file}:{l.line}  {l.url}  -> {l.detail}")
        print()

    inconclusive = [l for l in links if l.status in (ERROR, AUTH)]
    if inconclusive:
        by_detail = {}
        for l in inconclusive:
            by_detail.setdefault(l.detail, []).append(l)
        print("-" * 72)
        print("NOT VERIFIABLE (left untouched)")
        print("-" * 72)
        for detail, group in sorted(by_detail.items(), key=lambda kv: -len(kv[1])):
            print(f"  {len(group):>5} links  {detail}")
            for l in sorted(group, key=lambda l: (l.file, l.line))[:3]:
                print(f"           e.g. {l.file}:{l.line} {l.url}")
            if len(group) > 3:
                print(f"           ... and {len(group) - 3} more")
        print()

    if fixed:
        print("-" * 72)
        print("CHANGES APPLIED")
        print("-" * 72)
        if actions:
            for kind, path, url in actions:
                print(f"  {kind:<14} {path}  {url}")
        else:
            print("  none")
        print()
    elif broken or revived:
        print("Re-run with --fix to hide the broken links and restore the revived ones.")
        print()


def markdown_report(links, counts, actions, today, fixed):
    out = [f"# Link check report -- {today}", ""]
    out.append("| Status | Count |")
    out.append("| --- | --- |")
    for s in ORDER:
        if counts.get(s):
            out.append(f"| {s} | {counts[s]} |")
    out.append("")

    def table(title, rows, note=None):
        if not rows:
            return
        out.append(f"## {title}")
        out.append("")
        if note:
            out.append(note)
            out.append("")
        out.append("| File | Line | URL | Detail |")
        out.append("| --- | --- | --- | --- |")
        for l in sorted(rows, key=lambda l: (l.file, l.line)):
            url = l.url.replace("|", "\\|")
            out.append(f"| `{l.file}` | {l.line} | `{url}` | {l.detail} |")
        out.append("")

    table("Broken links", [l for l in links if l.status == BROKEN])
    table("Hidden links that now work", [l for l in links if l.hidden and l.status == OK])
    table("Transport errors", [l for l in links if l.status == ERROR])

    auth = [l for l in links if l.status == AUTH]
    if auth:
        out.append("## Not verifiable without credentials")
        out.append("")
        out.append(f"{len(auth)} links are behind a login wall and were left untouched. "
                   "Set `PSR_COOKIE` to an authenticated session cookie to check them.")
        out.append("")

    if fixed:
        out.append("## Changes applied")
        out.append("")
        if actions:
            out.append("| Action | File | URL |")
            out.append("| --- | --- | --- |")
            for kind, path, url in actions:
                safe = url.replace("|", "\\|")
                out.append(f"| {kind} | `{path}` | `{safe}` |")
        else:
            out.append("None.")
        out.append("")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
def main(argv=None):
    p = argparse.ArgumentParser(
        description="Check links in the SDDP release-notes docs; "
                    "hide broken ones and restore revived ones.")
    p.add_argument("--fix", action="store_true",
                   help="comment out broken links and uncomment revived ones")
    p.add_argument("--offline", action="store_true",
                   help="skip all network checks (internal links only)")
    p.add_argument("--only-internal", action="store_true",
                   help="check only internal/relative links")
    p.add_argument("--only-external", action="store_true",
                   help="check only http(s) links")
    p.add_argument("--report", metavar="FILE",
                   help="write a markdown report to FILE")
    p.add_argument("--json", metavar="FILE", dest="json_out",
                   help="write machine-readable results to FILE")
    p.add_argument("--timeout", type=float, default=20.0,
                   help="per-request timeout in seconds (default 20)")
    p.add_argument("--retries", type=int, default=1,
                   help="retries per URL before reporting ERROR (default 1)")
    p.add_argument("--jobs", type=int, default=8,
                   help="parallel HTTP requests (default 8)")
    p.add_argument("--download-jobs", type=int, default=3,
                   help="parallel requests for psr-inc.com download links "
                        "(default 3; the endpoint throttles into false failures)")
    p.add_argument("--confirm-delay", type=float, default=2.0,
                   help="seconds between the serial re-tests of failed downloads")
    p.add_argument("--no-confirm", action="store_true",
                   help="skip the serial re-test of failed downloads (faster, "
                        "but a throttled request can then look like a dead link)")
    p.add_argument("--no-downloads", action="store_true",
                   help="do not check the psr-inc.com download links at all")
    p.add_argument("-q", "--quiet", action="store_true", help="less progress output")
    args = p.parse_args(argv)

    if not os.path.isdir(DOCS_DIR):
        print(f"error: docs directory not found at {DOCS_DIR}", file=sys.stderr)
        return 2

    today = datetime.date.today().isoformat()
    site_index = build_site_index()

    links = []
    for path in doc_files():
        links.extend(extract_links(path))
    if not links:
        print("no links found", file=sys.stderr)
        return 0

    if not args.quiet:
        print(f"found {len(links)} link occurrences in {len({l.file for l in links})} files",
              file=sys.stderr)

    check_all(links, args, site_index)

    actions = []
    if args.fix:
        actions = apply_fixes(links, today)

    counts = summarize(links)
    print_report(links, counts, actions, today, args.fix)

    if args.report:
        with open(args.report, "w", encoding="utf-8", newline="") as fh:
            fh.write(markdown_report(links, counts, actions, today, args.fix))
        print(f"markdown report written to {args.report}", file=sys.stderr)

    if args.json_out:
        payload = {
            "checked": today,
            "counts": counts,
            "actions": [{"action": a, "file": f, "url": u} for a, f, u in actions],
            "links": [
                {"file": l.file, "line": l.line, "url": l.url, "kind": l.kind,
                 "hidden": l.hidden, "status": l.status, "detail": l.detail}
                for l in links
            ],
        }
        with open(args.json_out, "w", encoding="utf-8", newline="") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)
        print(f"json results written to {args.json_out}", file=sys.stderr)

    return 1 if counts.get(BROKEN) else 0


if __name__ == "__main__":
    sys.exit(main())
