#!/usr/bin/env python3
"""Compare this changelog repo (the source) with the knowledge_hub copy and
generate the missing entries in the knowledge_hub's MkDocs Material format.

    python tools/sync_knowledge_hub.py                    # drift report
    python tools/sync_knowledge_hub.py --snippets s.md    # + blocks ready to paste
    python tools/sync_knowledge_hub.py --apply            # insert what is safe to insert
    python tools/sync_knowledge_hub.py --target PATH       # other knowledge_hub location

Why this is not a file copy
---------------------------
The knowledge_hub copy is a hand-curated rewrite, not a mechanical rendering of
this repo. Where the source says `## Fixed Bugs`, the copy splits the very same
bullets across `Operation Planning - Bug fixes`, `Graphical interface - Bug
fixes` and so on: someone read each item and assigned it a module. Overwriting
the copy would throw that work away, so this tool never rewrites existing
entries. It only reports drift and adds versions that are missing.

What can be generated reliably
------------------------------
Recent source files carry module headings (`## Operation Planning Module
(SDDP)`, `#### OptGen 1`), so new versions can be rendered into the copy's
format faithfully. That covers exactly where the drift is -- the top of each
file. The flat historical format (a bare `## Fixed Bugs` with no module) cannot
be re-categorised automatically; such entries are rendered without a module and
flagged for review.

What --apply will and will not do
---------------------------------
It inserts:
  * new release candidates into an existing `??? abstract "Release candidates
    for X"` block, newest first;
  * a whole new version block at the top of an existing file.
It never:
  * edits or reorders an entry that already exists in the copy;
  * removes the `!!! note "Upcoming release"` admonition when a version stops
    being upcoming -- that deletes curated text, so it is reported with a ready
    snippet for you to apply;
  * touches `index.md` or `zensical.toml` -- a new file needs a nav entry, which
    is reported instead.
"""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
SOURCE_DIR = os.path.join(REPO_ROOT, "docs")
DEFAULT_TARGET = os.path.normpath(
    os.path.join(REPO_ROOT, "..", "knowledge_hub", "docs", "changelog", "sddp"))


def load_checker():
    spec = importlib.util.spec_from_file_location(
        "check_links", os.path.join(HERE, "check_links.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CL = load_checker()

# --------------------------------------------------------------------------
# source -> copy vocabulary
# --------------------------------------------------------------------------
MODULE_MAP = {
    "operation planning module (sddp)": "Operation Planning",
    "expansion planning module (optgen)": "Expansion Planning",
    "maintenance planning module (optmain)": "Maintenance Planning (OptMain)",
    "post processing tool (psrio)": "Post-processing (PSRIO)",
    "post-processing tool (psrio)": "Post-processing (PSRIO)",
    "graphical user interface": "Graphical interface",
    "graphical interface and user experience": "Graphical interface",
    "post-contingency analysis": "Post-contingency analysis",
    "reliability analysis model (coral)": "Reliability analysis model (Coral)",
    "setup": "Setup",
}
CATEGORY_MAP = {
    "new features and improvements": "New features",
    "new features and improvement": "New features",
    "new features": "New features",
    "fixed issues": "Bug fixes",
    "fixed bugs": "Bug fixes",
    "fixed issue": "Bug fixes",
    "bug fixes": "Bug fixes",
}
CATEGORY_ORDER = ["New features", "Bug fixes"]

OPTGEN_SUB_RE = re.compile(r"^optgen\s*([12])$", re.I)

ICONS = [
    (re.compile(r"linux", re.I), ":fontawesome-brands-linux:"),
    (re.compile(r"mac|darwin|osx", re.I), ":fontawesome-brands-apple:"),
    (re.compile(r"win", re.I), ":fontawesome-brands-windows:"),
]
BTN_ATTRS = '{ .os-btn target="_blank" rel="noopener" }'

# source file stem -> copy file name
FILE_MAP = {
    "sddp14.0": "sddp14.0-changelog.md",
    "sddp15.0": "sddp15.0-changelog.md",
    "sddp15.1": "sddp15.1-changelog.md",
    "sddp16.0": "sddp16.0-changelog.md",
    "sddp17.0": "sddp17.0-changelog.md",
    "sddp17.1": "sddp17.1-changelog.md",
    "sddp17.2": "sddp17.2-changelog.md",
    "sddp17.3-changelog": "sddp17.3-changelog.md",
    "sddp18.0-changelog": "sddp18.0-changelog.md",
    "sddp19.0-changelog": "sddp19.0-changelog.md",
}

VERSION_RE = re.compile(r"^#\s+SDDP\s+(?P<ver>[0-9][0-9A-Za-z.\-]*)\s*$")
DATE_RE = re.compile(r"Date:\s*(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})")
RC_RE = re.compile(r"^(?P<base>[0-9]+(?:\.[0-9]+)*)rc(?P<rc>[0-9]+)$", re.I)
BULLET_RE = re.compile(r"^(?P<indent>\s*)\*\s+(?P<text>.*\S)\s*$")


# --------------------------------------------------------------------------
# parsing the source
# --------------------------------------------------------------------------
class Section:
    def __init__(self, module, category):
        self.module = module        # already mapped, or None
        self.category = category    # already mapped, or None
        self.bullets = []          # list of (raw_indent, text); nesting is
                                   # derived per section, since the source uses
                                   # "  * " as its base level, not as nesting

    @property
    def label(self):
        if self.module and self.category:
            return f"{self.module} — {self.category}"
        return self.module or self.category or "Notes"


class Version:
    def __init__(self, ver, source_file, line):
        self.ver = ver
        self.source_file = source_file
        self.line = line
        self.date = None
        self.links = []            # (label, url)
        self.sections = []
        self.free_text = []
        self.unmapped = []          # source headings we could not map

    @property
    def is_rc(self):
        return bool(RC_RE.match(self.ver))

    @property
    def base(self):
        m = RC_RE.match(self.ver)
        return m.group("base") if m else self.ver

    @property
    def bullet_count(self):
        return sum(len(s.bullets) for s in self.sections)


def strip_hidden_markers(text):
    """Unwrap check_links' broken-link comments so hidden links still parse."""
    text = CL.INLINE_MARKER_RE.sub(lambda m: m.group("body"), text)
    text = CL.BLOCK_MARKER_RE.sub(lambda m: m.group("body"), text)
    return text


def parse_source_file(path):
    text, _, _ = CL.read_text(path)
    text = strip_hidden_markers(text)
    lines = text.split("\n")

    versions = []
    current = None
    module = None
    category = None
    submodule = None
    section = None
    in_links = False

    def new_section():
        nonlocal section
        mod = module
        if submodule:
            mod = submodule
        section = Section(mod, category)
        current.sections.append(section)

    for idx, raw in enumerate(lines, 1):
        line = raw.rstrip()
        m = VERSION_RE.match(line)
        if m:
            current = Version(m.group("ver"), os.path.basename(path), idx)
            versions.append(current)
            module = category = submodule = section = None
            in_links = False
            continue
        if current is None:
            continue

        if DATE_RE.search(line):
            current.date = DATE_RE.search(line).group("date")
            continue
        if line.strip().startswith("\U0001f517"):        # link emoji
            in_links = True
            continue

        if in_links:
            found = list(CL.MD_LINK_RE.finditer(line))
            if found:
                for lm in found:
                    current.links.append((lm.group("text").strip(),
                                          lm.group("url").strip()))
                continue
            if line.strip() in ("\\|", "|", ""):
                continue
            in_links = False

        h = re.match(r"^(?P<hashes>#{2,6})\s+(?P<title>.*\S)\s*$", line)
        if h:
            level = len(h.group("hashes"))
            title = h.group("title").strip()
            key = title.lower().strip()
            sub = OPTGEN_SUB_RE.match(key)
            if sub:
                submodule = f"Expansion Planning (OptGen {sub.group(1)})"
                new_section()
                continue
            if key in CATEGORY_MAP:
                category = CATEGORY_MAP[key]
                submodule = None
                new_section()
                continue
            if key in MODULE_MAP:
                module = MODULE_MAP[key]
                submodule = None
                category = None
                section = None
                continue
            # unknown heading: keep the text so nothing is silently dropped
            current.unmapped.append((level, title))
            module = title
            submodule = None
            category = None
            section = None
            continue

        b = BULLET_RE.match(line)
        if b:
            if section is None:
                new_section()
            section.bullets.append((len(b.group("indent")), b.group("text")))
            continue

        if line.strip() and section is not None and section.bullets:
            # continuation of the previous bullet
            indent, prev = section.bullets[-1]
            section.bullets[-1] = (indent, prev + " " + line.strip())
        elif line.strip() and section is None:
            current.free_text.append(line.strip())

    return versions


def parse_source():
    by_file = {}
    for stem, target_name in FILE_MAP.items():
        path = os.path.join(SOURCE_DIR, stem + ".md")
        if os.path.exists(path):
            by_file[target_name] = parse_source_file(path)
    return by_file


# --------------------------------------------------------------------------
# parsing the copy
# --------------------------------------------------------------------------
# The copy is mostly `## 18.0.10`, but a couple of 14.0 headings carry a
# decoration (`## 14.0.11rev1 · April 2017`), so anything after the version token
# is tolerated. Safe because a version token has to start with a digit, which
# rules out `#### Bug fixes` and friends.
COPY_VER_RE = re.compile(
    r"^(?P<indent>\s*)#{2,4}\s+(?P<ver>[0-9][0-9A-Za-z.]*)(?:\s+.*)?$")
ABSTRACT_RE = re.compile(r'^\s*\?\?\?\s*\+?\s*abstract\s+"Release candidates for '
                         r'(?P<base>[0-9][0-9A-Za-z.]*)"')
UPCOMING_RE = re.compile(r'^\s*!!!\s*note\s+"Upcoming release"')


def parse_copy_file(path):
    text, _, _ = CL.read_text(path)
    lines = text.split("\n")
    found = {}
    top = {}
    abstracts = {}
    upcoming = {}        # version -> line of its "!!! note" admonition
    last_top = None

    for idx, raw in enumerate(lines, 1):
        a = ABSTRACT_RE.match(raw)
        if a:
            abstracts[a.group("base")] = idx
            continue
        if UPCOMING_RE.match(raw) and last_top:
            upcoming[last_top] = idx
            continue
        m = COPY_VER_RE.match(raw)
        if m:
            ver = m.group("ver")
            found.setdefault(ver, idx)
            if not m.group("indent"):
                top.setdefault(ver, idx)
                last_top = ver
    return {"versions": found, "top": top, "abstracts": abstracts,
            "upcoming": upcoming, "lines": lines, "text": text}


# --------------------------------------------------------------------------
# rendering into the copy's format
# --------------------------------------------------------------------------
def icon_for(label):
    for rx, icon in ICONS:
        if rx.search(label):
            return icon
    return ":fontawesome-solid-download:"


def links_row(version):
    parts = []
    for label, url in version.links:
        parts.append(f"[{icon_for(label)} {label}]({url}){BTN_ATTRS}")
    return " ".join(parts)


def render_bullets(section):
    """Bullets rebased so the shallowest one in this section sits at level 0."""
    if not section.bullets:
        return []
    base = min(indent for indent, _ in section.bullets)
    out = []
    for indent, text in section.bullets:
        level = max(0, (indent - base) // 2)
        out.append("    " * level + f"- {text}")
    return out


def ordered_sections(version):
    """Merge sections with the same label, keeping New features before Bug fixes."""
    merged = {}
    order = []
    for s in version.sections:
        if not s.bullets:
            continue
        key = (s.category or "", s.module or "")
        if key not in merged:
            merged[key] = Section(s.module, s.category)
            order.append(key)
        merged[key].bullets.extend(s.bullets)

    def sort_key(key):
        cat = key[0]
        rank = CATEGORY_ORDER.index(cat) if cat in CATEGORY_ORDER else len(CATEGORY_ORDER)
        return (rank, order.index(key))

    return [merged[k] for k in sorted(order, key=sort_key)]


def month_year(date):
    if not date:
        return "?"
    d = datetime.date.fromisoformat(date)
    return d.strftime("%B %Y")


def render_rc(version, indent="    "):
    """A release-candidate block as it appears inside the ??? abstract block."""
    out = [f"{indent}### {version.ver}",
           f"{indent}\U0001f4c5 *{version.date or '?'}*",
           ""]
    row = links_row(version)
    if row:
        out += [indent + row, ""]
    for s in ordered_sections(version):
        out.append(f"{indent}##### {s.label}")
        out.append("")
        for line in render_bullets(s):
            out.append(indent + line)
        out.append("")
    for line in version.free_text:
        out += [indent + line, ""]
    return [l.rstrip() for l in out]


def render_release_body(version):
    """Everything a released version needs below its `## x.y.z` heading."""
    out = [f"\U0001f4c5 *{month_year(version.date)}*", ""]
    row = links_row(version)
    if row:
        out += [row, ""]

    sections = ordered_sections(version)
    by_cat = {}
    cat_order = []
    for s in sections:
        cat = s.category or "Notes"
        if cat not in by_cat:
            by_cat[cat] = []
            cat_order.append(cat)
        by_cat[cat].append(s)

    for cat in cat_order:
        out += [f"#### {cat}", ""]
        for s in by_cat[cat]:
            if s.module:
                out += [f"##### {s.module}", ""]
            out += render_bullets(s)
            out.append("")
    for line in version.free_text:
        out += [line, ""]
    return [l.rstrip() for l in out]


def render_release(version):
    """A released version block at top level: category as H4, module as H5."""
    return [f"## {version.ver}", ""] + render_release_body(version)


FRONT_MATTER = """---
title: "Changelog"
parent: "SDDP {major}"
nav_order: 2
hide:
  - feedback
search:
  exclude: true
---

# SDDP {major} Changelog

---
"""


def render_new_file(major, versions):
    out = [FRONT_MATTER.format(major=major).rstrip(), ""]
    rcs = [v for v in versions if v.is_rc]
    finals = [v for v in versions if not v.is_rc]
    for v in finals:
        out += render_release(v)
        if rcs:
            out += [f'??? abstract "Release candidates for {v.ver}"', ""]
            for i, rc in enumerate(rcs):
                out += render_rc(rc)
                if i < len(rcs) - 1:
                    out += ["    ---", ""]
        out += ["---", ""]
    if not finals:
        for rc in rcs:
            out += render_rc(rc, indent="")
            out += ["---", ""]
    return "\n".join(out).rstrip() + "\n"


# --------------------------------------------------------------------------
# diffing
# --------------------------------------------------------------------------
class Drift:
    def __init__(self):
        self.missing = []        # (target_name, Version)
        self.extra = []          # (target_name, version string)
        self.date_diff = []     # (target_name, ver, src_date, note)
        self.link_diff = []     # (target_name, ver, note)
        self.promote = []       # (target_name, base) upcoming -> released
        self.new_files = []     # (target_name, major, [Version])
        self.duplicates = []    # (source_file, ver, count) repeated in the source
        self.notes = []


def compare(source_by_file, target_dir):
    drift = Drift()
    for target_name, versions in sorted(source_by_file.items()):
        target_path = os.path.join(target_dir, target_name)
        major = re.sub(r"^sddp|-changelog$", "", target_name.replace(".md", ""))

        if not os.path.exists(target_path):
            drift.new_files.append((target_name, major, versions))
            continue

        copy = parse_copy_file(target_path)
        present = copy["versions"]

        # A version heading repeated in the source makes any per-version
        # comparison ambiguous, so record it and skip those checks.
        counts = {}
        for v in versions:
            counts[v.ver] = counts.get(v.ver, 0) + 1
        repeated = {ver for ver, n in counts.items() if n > 1}
        for ver in sorted(repeated):
            drift.duplicates.append((versions[0].source_file, ver, counts[ver]))

        for v in versions:
            if v.ver not in present:
                drift.missing.append((target_name, v))
                continue
            if v.ver in repeated:
                continue
            # the upcoming->released case is reported on its own
            if v.ver in copy["upcoming"]:
                continue
            # present on both sides -- compare the facts we can compare
            line = copy["lines"][present[v.ver] - 1:present[v.ver] + 6]
            chunk = "\n".join(line)
            if v.date:
                iso = v.date
                pretty = month_year(v.date)
                if iso not in chunk and pretty not in chunk:
                    shown = re.search(r"\U0001f4c5\s*\*?([^*\n]+)", chunk)
                    drift.date_diff.append(
                        (target_name, v.ver, iso,
                         f"copy shows {shown.group(1).strip() if shown else 'no date'}"))
            src_urls = {u for _, u in v.links}
            copy_urls = set(CL.MD_LINK_RE.findall(chunk))
            copy_urls = {u for _, u in CL.MD_LINK_RE.findall(chunk)} if False else \
                {m.group("url") for m in CL.MD_LINK_RE.finditer(chunk)}
            if src_urls and copy_urls and src_urls != copy_urls:
                only_src = src_urls - copy_urls
                if only_src:
                    drift.link_diff.append(
                        (target_name, v.ver,
                         f"{len(only_src)} download link(s) differ, e.g. "
                         f"{sorted(only_src)[0]}"))

        src_vers = {v.ver for v in versions}
        for ver in present:
            if ver not in src_vers:
                drift.extra.append((target_name, ver))

        # a version that is upcoming in the copy but already final in the source
        for base in copy["upcoming"]:
            if any(v.ver == base and not v.is_rc for v in versions):
                drift.promote.append((target_name, base))

    # copy files with no source counterpart at all
    if os.path.isdir(target_dir):
        known = set(FILE_MAP.values()) | {"index.md"}
        for name in sorted(os.listdir(target_dir)):
            if name.endswith(".md") and name not in known:
                drift.notes.append(
                    f"{name} exists only in the knowledge_hub (no source file maps to it)")
    return drift


# --------------------------------------------------------------------------
# applying
# --------------------------------------------------------------------------
def placement_for(version, src_versions, copy_top, line_count):
    """Where a new top-level version block goes.

    The source is ordered newest-first, so the right anchor is the nearest older
    version that the copy already has: the new block goes immediately before it.
    Falls back to the end of the file when there is no older sibling.
    """
    idx = next((i for i, v in enumerate(src_versions) if v.ver == version.ver), None)
    if idx is not None:
        for older in src_versions[idx + 1:]:
            if older.ver in copy_top:
                return copy_top[older.ver] - 1
    return line_count


def admonition_span(lines, start):
    """Line range (0-based, end-exclusive) of the `!!! note` block at `start`.

    An MkDocs admonition is its `!!!` line plus everything indented under it;
    trailing blank lines are swallowed so the replacement does not leave a gap.
    """
    end = start + 1
    while end < len(lines):
        line = lines[end]
        if not line.strip():
            end += 1
            continue
        if line.startswith(("    ", "\t")):
            end += 1
            continue
        break
    # give back any blank lines we ran past, except one separator
    while end - 1 > start and not lines[end - 1].strip():
        end -= 1
    return start, end


def apply_drift(drift, target_dir, source_by_file, create_files=False, promote=False):
    actions = []
    by_target = {}
    for target_name, v in drift.missing:
        by_target.setdefault(target_name, []).append(v)
    if promote:
        for target_name, base in drift.promote:
            by_target.setdefault(target_name, [])

    for target_name, missing in sorted(by_target.items()):
        target_path = os.path.join(target_dir, target_name)
        text, newline, bom = CL.read_text(target_path)
        lines = text.split("\n")
        copy = parse_copy_file(target_path)
        src_versions = source_by_file[target_name]
        order = {v.ver: i for i, v in enumerate(src_versions)}
        missing = sorted(missing, key=lambda v: order.get(v.ver, 10 ** 6))

        rc_groups = {}
        finals = []
        for v in missing:
            if v.is_rc:
                if v.base in copy["abstracts"]:
                    rc_groups.setdefault(v.base, []).append(v)
                else:
                    actions.append(
                        ("skipped: no rc block", target_name,
                         f"{v.ver} (no '??? abstract ... for {v.base}' in the copy)"))
            elif v.ver in copy["upcoming"]:
                actions.append(
                    ("skipped: needs promotion", target_name,
                     f"{v.ver} (copy still marks it upcoming)"))
            else:
                finals.append(v)

        # Build every edit as (start, end, block) first, then apply bottom-up so
        # the line numbers stay valid. end == start means "insert here".
        edits = []
        for base, rcs in rc_groups.items():
            at = copy["abstracts"][base]        # 0-based index just past "??? abstract"
            while at < len(lines) and not lines[at].strip():
                at += 1
            block = []
            for rc in rcs:                      # already newest-first
                block += render_rc(rc) + ["    ---", ""]
            edits.append((at, at, block))
            for rc in rcs:
                actions.append(("rc inserted", target_name, rc.ver))

        for v in finals:
            at = placement_for(v, src_versions, copy["top"], len(lines))
            edits.append((at, at, render_release(v) + ["---", ""]))
            actions.append(("version inserted", target_name, v.ver))

        if promote:
            for tname, base in drift.promote:
                if tname != target_name or base not in copy["upcoming"]:
                    continue
                v = next((s for s in src_versions
                          if s.ver == base and not s.is_rc), None)
                if v is None:
                    continue
                start, end = admonition_span(lines, copy["upcoming"][base] - 1)
                edits.append((start, end, render_release_body(v)))
                actions.append(("promoted to released", target_name,
                                f"{base} ({month_year(v.date)})"))

        for start, end, block in sorted(edits, key=lambda e: e[0], reverse=True):
            lines[start:end] = block

        if edits:
            CL.write_text(target_path, "\n".join(lines), newline, bom)

    for target_name, major, versions in drift.new_files:
        if not create_files:
            actions.append(
                ("skipped: new file", target_name,
                 "pass --create-files once you know it should exist "
                 "(it also needs a nav entry)"))
            continue
        target_path = os.path.join(target_dir, target_name)
        with open(target_path, "w", encoding="utf-8", newline="") as fh:
            fh.write(render_new_file(major, versions))
        actions.append(("file created", target_name, f"{len(versions)} version(s)"))
    return actions


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------
def print_report(drift, source_by_file, target_dir, actions, applied):
    print()
    print("=" * 72)
    print("changelog (source)  ->  knowledge_hub (copy)")
    print("=" * 72)
    print(f"source: {SOURCE_DIR}")
    print(f"copy:   {target_dir}")
    print()

    total_src = sum(len(v) for v in source_by_file.values())
    print(f"{total_src} source versions across {len(source_by_file)} files")
    print(f"  missing from the copy : {len(drift.missing)}")
    print(f"  only in the copy      : {len(drift.extra)}")
    print(f"  date mismatches       : {len(drift.date_diff)}")
    print(f"  download link diffs   : {len(drift.link_diff)}")
    print(f"  files to create       : {len(drift.new_files)}")
    print()

    if drift.missing:
        print("-" * 72)
        print("MISSING FROM THE COPY")
        print("-" * 72)
        by_target = {}
        for target_name, v in drift.missing:
            by_target.setdefault(target_name, []).append(v)
        for target_name, versions in sorted(by_target.items()):
            print(f"  {target_name}")
            for v in versions:
                kind = "rc " if v.is_rc else "REL"
                flag = "  [no module headings -- review]" if any(
                    s.module is None for s in v.sections if s.bullets) else ""
                print(f"      {kind} {v.ver:<18} {v.date or '?':<12} "
                      f"{v.bullet_count} item(s){flag}")
        print()

    if drift.promote:
        print("-" * 72)
        print("UPCOMING -> RELEASED (needs your hand: removes curated text)")
        print("-" * 72)
        for target_name, base in drift.promote:
            print(f"  {target_name}: {base} is final in the source but the copy still")
            print(f"      carries the '!!! note \"Upcoming release\"' admonition.")
            print(f"      Replace that note with the date + download row + entries.")
        print()

    if drift.extra:
        print("-" * 72)
        print("ONLY IN THE COPY")
        print("-" * 72)
        for target_name, ver in drift.extra:
            print(f"  {target_name}: {ver}")
        print()

    if drift.date_diff:
        print("-" * 72)
        print("DATE MISMATCHES")
        print("-" * 72)
        for target_name, ver, iso, note in drift.date_diff:
            print(f"  {target_name}: {ver} source={iso}, {note}")
        print()

    if drift.link_diff:
        print("-" * 72)
        print("DOWNLOAD LINK MISMATCHES")
        print("-" * 72)
        for target_name, ver, note in drift.link_diff:
            print(f"  {target_name}: {ver} {note}")
        print()

    if drift.new_files:
        print("-" * 72)
        print("FILES TO CREATE IN THE COPY")
        print("-" * 72)
        for target_name, major, versions in drift.new_files:
            print(f"  {target_name} ({len(versions)} version(s))")
            print(f"      also needs a nav entry in zensical.toml and a row in index.md")
        print()

    if drift.duplicates:
        print("-" * 72)
        print("REPEATED VERSION HEADINGS IN THE SOURCE (not a drift; worth fixing)")
        print("-" * 72)
        for source_file, ver, count in drift.duplicates:
            print(f"  {source_file}: '# SDDP {ver}' appears {count}x")
        print()

    if drift.notes:
        print("-" * 72)
        print("NOTES")
        print("-" * 72)
        for note in drift.notes:
            print(f"  {note}")
        print()

    if applied:
        print("-" * 72)
        print("CHANGES APPLIED")
        print("-" * 72)
        for kind, target_name, what in actions:
            print(f"  {kind:<22} {target_name}  {what}")
        print()
    elif drift.missing or drift.new_files:
        print("Run with --apply to insert what can be inserted safely,")
        print("or --snippets FILE to get the blocks without touching the copy.")
        print()


def write_snippets(drift, path):
    out = ["# Generated blocks for the knowledge_hub copy", "",
           "Paste these into the matching file. Nothing here has been applied.", ""]
    by_target = {}
    for target_name, v in drift.missing:
        by_target.setdefault(target_name, []).append(v)

    for target_name, versions in sorted(by_target.items()):
        out += [f"## {target_name}", ""]
        for v in versions:
            where = (f"inside `??? abstract \"Release candidates for {v.base}\"`, "
                     f"as the first entry" if v.is_rc else "at the top, before the newest version")
            out += [f"### {v.ver} -- insert {where}", "", "```markdown"]
            out += render_rc(v) if v.is_rc else render_release(v)
            out += ["```", ""]

    for target_name, major, versions in drift.new_files:
        out += [f"## {target_name} -- new file", "", "```markdown",
                render_new_file(major, versions), "```", "",
                "Then add to `zensical.toml` nav and to `index.md`.", ""]

    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(out).rstrip() + "\n")


# --------------------------------------------------------------------------
def main(argv=None):
    p = argparse.ArgumentParser(
        description="Report and close the drift between this changelog repo "
                    "(source) and the knowledge_hub copy.")
    p.add_argument("--target", default=DEFAULT_TARGET,
                   help="knowledge_hub sddp changelog directory")
    p.add_argument("--apply", action="store_true",
                   help="insert missing versions into the copy (never rewrites "
                        "existing entries)")
    p.add_argument("--snippets", metavar="FILE",
                   help="write the generated blocks to FILE instead of applying")
    p.add_argument("--promote", action="store_true",
                   help="with --apply, replace the '!!! note \"Upcoming release\"' "
                        "admonition with the real date, download row and entries "
                        "for versions that are final in the source")
    p.add_argument("--create-files", action="store_true",
                   help="with --apply, also create changelog files the copy lacks "
                        "(off by default: the copy may already carry that release "
                        "under a different version number)")
    args = p.parse_args(argv)

    target_dir = os.path.abspath(args.target)
    if not os.path.isdir(target_dir):
        print(f"error: copy directory not found: {target_dir}", file=sys.stderr)
        return 2

    source_by_file = parse_source()
    drift = compare(source_by_file, target_dir)

    actions = []
    if args.apply:
        actions = apply_drift(drift, target_dir, source_by_file,
                              args.create_files, args.promote)

    print_report(drift, source_by_file, target_dir, actions, args.apply)

    if args.snippets:
        write_snippets(drift, args.snippets)
        print(f"snippets written to {args.snippets}", file=sys.stderr)

    return 1 if (drift.missing or drift.new_files or drift.promote) else 0


if __name__ == "__main__":
    sys.exit(main())
