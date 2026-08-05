# SDDP release notes
Repository for SDDP release notes

https://psrenergy-docs.github.io/sddp-release-notes/

## Maintenance scripts

Double-click either `.bat` in the repo root; both end on a pause so the window
stays open.

| Script | What it does |
| --- | --- |
| `check-links.bat` | Menu: check links, apply fixes, sign in, or run offline |
| `login-psr.bat` | Opens Chrome, waits for your psr-inc.com login, saves the cookie |

From a terminal the flags are passed straight through, e.g.
`check-links.bat --fix`.

## Link checker

`tools/check_links.py` (Python 3.8+, standard library only) checks every link in
`docs/`, reports on them, and can hide the broken ones / bring back the ones that
started working.

```
python tools/check_links.py                   # check and print a report
python tools/check_links.py --fix             # hide broken links, restore revived ones
python tools/check_links.py --offline         # internal links only, no network
python tools/check_links.py --report r.md     # also write a markdown report
python tools/check_links.py --json r.json     # also write machine-readable results
```

Exit code is `1` when something is broken, so it can gate a CI job.

### How a link is hidden

A broken link is wrapped in an HTML comment that carries a machine-readable
marker, so Jekyll stops rendering it but nothing is lost:

```
<!--broken-link status=404 checked=2026-08-04
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-19.0-setup-linux.bin)
-->
```

When the link sits alone on its line the whole line is hidden, together with the
adjacent `\|` separator, so the rendered download row stays clean. When it shares
a line with working links, only that link is wrapped (inline `:: … -->` form).

Every run re-checks the links inside those markers. As soon as a link answers OK
the marker is removed and the original text is restored **byte for byte** — that
is the "the installer has been published, publish the link" path. Only the
script's own `broken-link` markers are touched; hand-written comments are left
alone and merely reported.

A link is hidden only on a definitive "does not exist" answer (HTTP 404/410, or a
missing file for relative links). A timeout, a DNS failure or a login wall is
reported as `ERROR`/`AUTH` and never edits anything, so a flaky network cannot
silently delete links. `docs/_config.yml` is checked but never rewritten, since
its `url:` entries are navigation structure.

### Download links need a session cookie

`https://www.psr-inc.com/app/link/?t=d&f=…` is only a URL builder: it redirects to
the PSR login page whether or not the file exists, so anonymously these ~1400
links cannot be verified and are reported as `AUTH`. Sign in once with

```
login-psr.bat            # or: python tools/psr_login.py
```

which opens Chrome on a throwaway profile, waits for you to sign in, proves the
session by asking for a file known to exist, and writes the cookie to
`.psr-cookie` (git-ignored). `check_links.py` reads `$PSR_COOKIE` first and falls
back to that file. `login-psr.bat --check` re-tests the saved cookie;
`--reset` forgets it.

Signed in, the checker uses `HEAD` — enough to read the headers without pulling a
400 MB installer, and the site answers `502` to a `GET` whose body is never read.
A real file comes back as an attachment; an unavailable one lands on
`download/acessonegado.htm`.

**That page is not proof of anything on its own.** It means "cannot be served",
which covers "not published yet", "your account has no access", *and* "you are
asking too fast" — the endpoint starts returning it under concurrency. A run at
eight parallel requests produced hundreds of failures that a slow re-probe could
not reproduce. So downloads are checked gently and every failure is re-tested on
its own before it is believed:

```
--download-jobs 3     # parallel requests for download links (default 3)
--confirm-delay 2     # seconds between the serial re-tests of failures
--no-confirm          # skip the re-test (fast, but throttling looks like a dead link)
--no-downloads        # do not check download links at all
```

Keep the confirmation pass on for anything that writes. It is what stops a busy
server from quietly commenting out working links.

Do not paste the cookie into a `.bat`: it contains `%` characters and `cmd`
would expand them, silently corrupting the value. Use `.psr-cookie`.

## Syncing the knowledge_hub copy

`../knowledge_hub/docs/changelog/sddp` holds a second copy of this changelog for
the Zensical/MkDocs site. It is a **hand-curated rewrite**, not a rendering of
this repo: where the source has a flat `## Fixed Bugs`, the copy splits the same
bullets across `Operation Planning — Bug fixes`, `Graphical interface — Bug
fixes` and so on. So the sync never overwrites existing entries.

```
python tools/sync_knowledge_hub.py                  # drift report
python tools/sync_knowledge_hub.py --snippets s.md  # blocks ready to paste
python tools/sync_knowledge_hub.py --apply          # insert what is safe
python tools/sync_knowledge_hub.py --apply --promote # + turn "upcoming" into released
python tools/sync_knowledge_hub.py --target PATH    # other copy location
```

`--apply` only ever *adds*: new release candidates go into the existing
`??? abstract "Release candidates for X"` block (newest first), and a new version
block goes in at its chronological position. Existing entries are never rewritten.

Two things need an explicit opt-in:

- `--promote` replaces the `!!! note "Upcoming release"` admonition with the real
  date, download row and entries, once the source shows the version as final.
  It is off by default because it *deletes* curated text.
- `--create-files` creates a changelog file the copy lacks. Off by default,
  because the copy may already carry that release under a different version
  number — and a new file also needs a nav entry in `zensical.toml` and a row in
  `index.md`, neither of which this tool touches.

It also flags things worth fixing on the source side: repeated `# SDDP x.y.z`
headings, and dates that disagree between the two copies.
