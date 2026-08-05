#!/usr/bin/env python3
"""Open Chrome, wait for you to sign in to psr-inc.com, save the session cookie.

The cookie is written to `.psr-cookie` at the repo root (git-ignored), which
`check_links.py` picks up automatically -- no copy/paste from DevTools needed.

    python tools/psr_login.py            # open Chrome, wait for login, save
    python tools/psr_login.py --print    # also print the cookie header
    python tools/psr_login.py --check    # only test the cookie already saved
    python tools/psr_login.py --reset    # forget the saved browser profile

The browser runs on a dedicated profile under `.psr-profile/`, separate from your
day-to-day Chrome, so nothing interferes with your normal session -- and the
login usually survives to the next run.

Success is not guessed from the page: the cookie is proven by asking for a file
that is known to exist and checking that a real download comes back.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
COOKIE_FILE = os.path.join(REPO_ROOT, ".psr-cookie")
PROFILE_DIR = os.path.join(REPO_ROOT, ".psr-profile")

LOGIN_URL = "https://www.psr-inc.com/en/login/"
COOKIE_DOMAIN = "psr-inc.com"

# A file that certainly exists, used to prove the cookie really works.
PROBE_URL = "https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.10-setup.zip"


def load_checker():
    spec = importlib.util.spec_from_file_location(
        "check_links", os.path.join(HERE, "check_links.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CL = load_checker()


def probe(cookie, timeout=25):
    """(status, detail) for the probe URL with this cookie -- OK means logged in."""
    link = CL.Link("(probe)", 0, PROBE_URL, "", "gated")
    return CL.check_gated(link, cookie, timeout, 0)


def header_from(driver):
    """Build a `name=value; ...` header from the browser's psr-inc.com cookies."""
    pairs = []
    for c in driver.get_cookies():
        domain = (c.get("domain") or "").lstrip(".")
        if domain.endswith(COOKIE_DOMAIN):
            pairs.append(f"{c['name']}={c['value']}")
    return "; ".join(pairs)


def save(cookie):
    with open(COOKIE_FILE, "w", encoding="utf-8", newline="") as fh:
        fh.write(cookie + "\n")
    print(f"\nsaved to {os.path.relpath(COOKIE_FILE, REPO_ROOT)} "
          f"({len(cookie)} chars, {cookie.count(';') + 1} cookies)")
    print("check_links.py will pick it up automatically.")


def do_check():
    cookie = CL.load_cookie()
    if not cookie:
        print("no cookie found (neither $PSR_COOKIE nor .psr-cookie)")
        return 1
    status, detail = probe(cookie)
    print(f"saved cookie -> {status}: {detail}")
    return 0 if status == CL.OK else 1


def do_login(args):
    try:
        from selenium import webdriver
        from selenium.common.exceptions import WebDriverException
    except ImportError:
        print("Selenium is not installed. Run:\n\n    python -m pip install selenium\n")
        return 2

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=" + PROFILE_DIR)
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    # never actually pull a file down while probing from the browser
    options.add_experimental_option("prefs", {"download_restrictions": 3})

    print("opening Chrome (a separate profile, not your everyday one)...")
    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as exc:
        print(f"could not start Chrome: {exc}")
        print("Is Chrome installed? Selenium downloads its driver on first run, "
              "so this step needs internet access.")
        return 2

    try:
        driver.get(LOGIN_URL)
        print()
        print("=" * 68)
        print(" Sign in to psr-inc.com in the window that just opened.")
        print(" Leave the browser open -- I detect the login on my own and")
        print(" close it for you. Ctrl+C here to give up.")
        print("=" * 68)
        print()

        deadline = time.time() + args.timeout
        last_note = ""
        while time.time() < deadline:
            try:
                cookie = header_from(driver)
                url = driver.current_url
            except WebDriverException:
                print("\nbrowser was closed before the login completed.")
                return 1

            if cookie:
                status, detail = probe(cookie, timeout=20)
                if status == CL.OK:
                    print("login confirmed -- a real download came back.")
                    save(cookie)
                    if args.print_cookie:
                        print("\n" + cookie)
                    return 0
                note = f"waiting for login... ({detail})"
            else:
                note = f"waiting for login... (no psr-inc.com cookie yet, at {url})"

            if note != last_note:
                print("  " + note)
                last_note = note
            time.sleep(3)

        print(f"\ngave up after {args.timeout}s without a working session.")
        return 1
    except KeyboardInterrupt:
        print("\ncancelled.")
        return 1
    finally:
        try:
            driver.quit()
        except Exception:
            pass


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Sign in to psr-inc.com in a browser and save the session "
                    "cookie for the link checker.")
    p.add_argument("--print", dest="print_cookie", action="store_true",
                   help="also print the cookie header to stdout")
    p.add_argument("--check", action="store_true",
                   help="only test the cookie that is already saved")
    p.add_argument("--reset", action="store_true",
                   help="delete the saved browser profile and cookie, then exit")
    p.add_argument("--timeout", type=int, default=300,
                   help="seconds to wait for the login (default 300)")
    args = p.parse_args(argv)

    if args.reset:
        for path in (PROFILE_DIR, COOKIE_FILE):
            if os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
                print(f"removed {os.path.relpath(path, REPO_ROOT)}/")
            elif os.path.exists(path):
                os.remove(path)
                print(f"removed {os.path.relpath(path, REPO_ROOT)}")
        return 0

    if args.check:
        return do_check()

    # already signed in from a previous run?
    existing = CL.load_cookie()
    if existing:
        status, detail = probe(existing)
        if status == CL.OK:
            print(f"the saved cookie still works ({detail}) -- nothing to do.")
            print("Use --reset to start over.")
            return 0
        print(f"saved cookie is no longer usable ({detail}); signing in again.")

    return do_login(args)


if __name__ == "__main__":
    sys.exit(main())
