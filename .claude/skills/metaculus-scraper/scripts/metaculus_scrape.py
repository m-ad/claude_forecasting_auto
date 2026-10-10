#!/usr/bin/env python3
"""
Metaculus question scraper using Playwright (HTML fallback).

Extracts the community prediction and resolution criteria by rendering the
public question page -- no comments (see ``scrape_metaculus_question``). This
is the **fallback** path: prefer the ``metaculus-aggregations`` skill, which
returns structured numbers for all three cohorts and comment text. This script only ever
sees the single headline figure the page renders.

Works in sandboxed/containerised environments by routing through the egress
proxy.

--------------------------------------------------------------------------
WHY THIS WAS BROKEN (fixed September 2026)
--------------------------------------------------------------------------
Three independent faults, each fatal on its own:

1. **Playwright could not find a browser.** The script never set
   ``PLAYWRIGHT_BROWSERS_PATH``, so in a sandbox that ships Chromium at
   ``/opt/pw-browsers`` it died with "Looks like Playwright was just installed
   or updated. Please run playwright install" before issuing any request. Even
   with the path set, Playwright looks for the exact Chromium build *its own
   version* expects (1.62 wants ``chromium_headless_shell-1234``) while the
   image ships an older build (1194) behind a stable ``chromium`` symlink. Since
   ``playwright`` is pinned only as ``>=1.44``, a routine dependency resolution
   was enough to break the launch. The binary is therefore resolved explicitly
   and by symlink, never by build number.
2. **The proxy was silently dropped.** ``_parse_proxy`` matched only an
   *authenticated* proxy URL (``http://user:pass@host:port``). The agent proxy
   is a bare ``http://127.0.0.1:<port>`` with no credentials, so the regex
   failed, the function returned ``{}``, and Chromium was launched with no
   proxy at all -- which means no egress.
3. **Chromium's TLS 1.3 handshake is reset by the egress proxy.** Even with the
   proxy wired up correctly, every navigation died with
   ``net::ERR_CONNECTION_RESET`` -- for *any* host, example.com included. The
   MITM proxy cannot complete Chromium's TLS 1.3 ClientHello (~1.8 kB sent,
   39 B back, tunnel closed), most likely the post-quantum key share splitting
   it across records. ``--ssl-version-max=tls1.2`` fixes it; that fallback is
   applied automatically on a reset-class error, and can be forced up front
   with ``METACULUS_FORCE_TLS12=1``.

Metaculus itself also rate-limits by IP and answers over-quota clients with a
Cloudflare managed challenge ("Just a moment..."). A shared sandbox egress IP
trips this easily, so a challenged page is reported as such instead of being
parsed into a confidently wrong answer.

With ``METACULUS_API_KEY`` set, title, forecaster count, resolution criteria and
fine print are taken from the token-authed ``/api/posts/<id>/`` endpoint (plain
HTTPS, exact source text) instead of being parsed out of the rendered page. The
headline prediction still comes from the page: Metaculus returns null
aggregations to bot-account keys. See the ``metaculus-aggregations`` docstring.

Usage:
    python metaculus_scrape.py <post_id> [--wait SECONDS] [--json]

Examples:
    python metaculus_scrape.py 578
    python metaculus_scrape.py 578 --json
    python metaculus_scrape.py 3479 --json
"""

import argparse
import json
import os
import re
import time
import urllib.request
from dataclasses import asdict, dataclass
from typing import Any
from urllib.parse import unquote, urlparse

# The sandbox ships Chromium here; setting this lets Playwright find it without
# a separate `playwright install` step. Only set it when the store really
# exists -- on a normal workstation Playwright must keep its own location.
if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")

# Must NOT contain "HeadlessChrome": Cloudflare challenges that token outright.
_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
)

# Chromium flag that makes the handshake survive a TLS-1.3-intolerant MITM proxy.
_TLS12_ARG = "--ssl-version-max=tls1.2"

# Seconds to wait between retries of a challenged page load. Metaculus' IP-level
# rate limit was measured to clear in ~2 min, so short retries are wasted
# requests that only re-arm it.
_BACKOFF = (5, 30, 60, 75)

_API = "https://www.metaculus.com/api"
# Cloudflare bans the stdlib default "Python-urllib/x.y" outright (error 1010).
_API_UA = "claude-forecasting/0.1 (metaculus-scraper)"

# Substrings meaning the handshake or tunnel died rather than an HTTP error.
_RESET_MARKERS = (
    "ERR_CONNECTION_RESET",
    "ERR_CONNECTION_CLOSED",
    "ERR_SSL_PROTOCOL_ERROR",
    "ERR_EMPTY_RESPONSE",
    "ERR_QUIC_PROTOCOL_ERROR",
    "ERR_TUNNEL_CONNECTION_FAILED",
)


@dataclass
class MetaculusQuestion:
    post_id: int
    title: str
    url: str
    question_type: str  # "binary", "date", "numeric", "multiple_choice", "unknown"
    community_prediction: str | None = None
    num_forecasters: str | None = None
    num_comments: str | None = None
    resolution_criteria: str | None = None
    fine_print: str | None = None


def _parse_proxy() -> dict:
    """Playwright ``proxy=`` config from the environment, or ``{}``.

    Chromium does not read ``HTTPS_PROXY`` from the shell environment, so the
    value has to be parsed and passed explicitly. Credentials are *optional*:
    a sandbox egress proxy may be ``http://user:pass@host:port`` or a bare
    ``http://127.0.0.1:<port>``. Requiring them is what silently disabled the
    proxy in this environment -- see the module docstring.
    """
    raw = os.environ.get("https_proxy") or os.environ.get("HTTPS_PROXY") or ""
    if not raw:
        # Outside a sandbox there is no egress proxy; a direct connection is
        # correct there, so return no proxy config instead of aborting.
        return {}
    parsed = urlparse(raw)
    if not parsed.hostname:
        return {}
    server = f"{parsed.scheme or 'http'}://{parsed.hostname}"
    if parsed.port:
        server += f":{parsed.port}"
    cfg = {"server": server}
    if parsed.username:
        cfg["username"] = unquote(parsed.username)
    if parsed.password:
        cfg["password"] = unquote(parsed.password)
    return cfg


def _api_post(post_id: int, timeout: float = 30.0) -> dict | None:
    """``/api/posts/<id>/`` JSON via ``METACULUS_API_KEY``; None if unset or failed."""
    key = os.environ.get("METACULUS_API_KEY")
    if not key:
        return None
    req = urllib.request.Request(
        f"{_API}/posts/{post_id}/",
        headers={
            "Authorization": f"Token {key}",
            "Accept": "application/json",
            "User-Agent": _API_UA,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
    # URLError/HTTPError/timeouts are OSErrors, bad JSON is a ValueError; either
    # way the page-parsed values stand.
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def _is_transport_reset(exc: Exception) -> bool:
    """True when an exception is a dead handshake/tunnel, not an HTTP error."""
    return any(m in str(exc) for m in _RESET_MARKERS)


def _open_question_info(page: Any) -> None:
    """Reveal the resolution criteria by clicking the "Question Info" tab.

    Metaculus moved the resolution criteria, fine print and background behind a
    tab, so they are no longer in the initially rendered text at all. That is
    what silently emptied ``resolution_criteria`` here: the section markers the
    parser looks for are real headings, they were just never on the page. One
    click brings them back. Best-effort -- the headline community prediction,
    which is this script's actual contract, does not depend on it.
    """
    try:
        page.get_by_text("Question Info", exact=False).first.click(timeout=8000)
    except Exception:  # noqa: BLE001 - tab absent or renamed; not fatal
        return
    # The panel mounts client-side; the text is not there on the next tick.
    time.sleep(3)


def _render_page(post_id: int, wait_seconds: int) -> tuple[str, str]:
    """Load a question page in Chromium and return ``(title, body_text)``.

    Retries once pinned to TLS 1.2 when the first attempt dies with a
    reset-class error, which is what a TLS-1.3-intolerant egress proxy does to
    Chromium, and rides out a Cloudflare rate-limit block per :data:`_BACKOFF`.
    See the module docstring.

    Raises
    ------
    RuntimeError
        If the page cannot be loaded, or Cloudflare was still challenging after
        the whole backoff schedule. Both are reported rather than parsed, so a
        blocked fetch can never masquerade as a missing community prediction.
    """
    from playwright.sync_api import sync_playwright

    url = f"https://www.metaculus.com/questions/{post_id}/"
    proxy = _parse_proxy() or None
    force_tls12 = os.environ.get("METACULUS_FORCE_TLS12") == "1"
    # Pin the binary: Playwright otherwise demands the exact build its own
    # version expects, which the sandbox image does not ship. See the docstring.
    exe = os.environ.get(
        "PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH", "/opt/pw-browsers/chromium"
    )

    with sync_playwright() as p:
        for attempt in range(2):
            args = [_TLS12_ARG] if (force_tls12 or attempt) else []
            kwargs = {"headless": True, "proxy": proxy, "args": args}
            if os.path.exists(exe):
                kwargs["executable_path"] = exe
            browser = p.chromium.launch(**kwargs)
            try:
                page = browser.new_page(user_agent=_UA)
                for wait in (0, *_BACKOFF):
                    if wait:
                        time.sleep(wait)
                    try:
                        page.goto(url, wait_until="domcontentloaded", timeout=60000)
                    except Exception as exc:
                        if (
                            attempt == 0
                            and not force_tls12
                            and _is_transport_reset(exc)
                        ):
                            break  # relaunch pinned to TLS 1.2
                        raise RuntimeError(
                            f"Could not load {url}: {str(exc).splitlines()[0]}"
                        ) from exc
                    time.sleep(wait_seconds)
                    title = page.title()
                    if "just a moment" not in (title or "").lower():
                        _open_question_info(page)
                        return title, page.inner_text("body")
                else:
                    raise RuntimeError(
                        f"Cloudflare was still challenging post {post_id} after "
                        f"{sum(_BACKOFF)}s of backoff. Metaculus rate-limits by IP "
                        "and a shared sandbox egress IP trips it easily; wait a few "
                        "minutes and retry."
                    )
            finally:
                browser.close()
    raise RuntimeError(f"Could not load {url} (transport reset on both attempts)")


def _detect_question_type(lines: list[str]) -> tuple[str, str | None]:
    """
    Detect question type and extract community prediction from the first ~20 lines.

    Returns
    -------
    (question_type, prediction)
        question_type: "binary", "date", "numeric", "multiple_choice", or "unknown"
        prediction: the community prediction value as a string, or None
    """
    # Find the relevant section after the question title (skip nav lines)
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Binary open: "<number>%\nCHANCE"
        if stripped == "CHANCE" and i > 0:
            pct_match = re.match(r"^(\d{1,3}(?:\.\d+)?)\s*%$", lines[i - 1].strip())
            if pct_match:
                return "binary", f"{pct_match.group(1)}%"

        # Binary resolved: "Resolved YES" / "Resolved NO"
        if re.match(r"^Resolved\s+(YES|NO)$", stripped, re.IGNORECASE):
            return "binary", stripped

        # Date/numeric: "Current estimate\n<value>"
        if stripped == "Current estimate" and i + 1 < len(lines):
            estimate = lines[i + 1].strip()
            if re.match(r"\d{1,2}\s+\w{3}\s+\d{4}", estimate):
                return "date", estimate
            if re.match(r"[\d,\.]+", estimate):
                return "numeric", estimate
            return "date", estimate

        # Multiple choice: option followed by "Result: Yes/No" or a percentage
        if stripped.startswith("Result:") and i > 0:
            # Collect all MC options by scanning nearby lines
            options = {}
            j = i - 1
            while j >= 0 and j >= i - 30:
                opt_name = lines[j].strip()
                if opt_name in ("Share", "Sign Up", "Log In", "More", ""):
                    break
                if j + 1 < len(lines):
                    result_line = lines[j + 1].strip()
                    if result_line.startswith("Result:"):
                        options[opt_name] = result_line
                j -= 1
            # Also scan forward
            j = i - 1
            while j < len(lines) - 1 and j < i + 60:
                opt_name = lines[j].strip()
                if opt_name in ("Share", "Timeline", ""):
                    break
                if j + 1 < len(lines):
                    result_line = lines[j + 1].strip()
                    if result_line.startswith("Result:"):
                        options[opt_name] = result_line
                        j += 2
                        continue
                j += 1
            if options:
                summary = "; ".join(f"{k}: {v}" for k, v in options.items())
                return "multiple_choice", summary

    return "unknown", None


def scrape_metaculus_question(
    post_id: int,
    wait_seconds: int = 10,
) -> MetaculusQuestion:
    """
    Scrape a Metaculus question page for its community prediction and criteria.

    Comment text is not extractable from the rendered page (it sits behind a
    lazy-loaded tab that does not survive a scripted click); use the
    ``metaculus-aggregations`` skill for comments.

    Parameters
    ----------
    post_id : int
        The numeric post ID from the Metaculus question URL.
    wait_seconds : int
        Seconds to wait for JS rendering (default 10).

    Returns
    -------
    MetaculusQuestion
        Parsed question data.
    """
    url = f"https://www.metaculus.com/questions/{post_id}/"
    title, body = _render_page(post_id, wait_seconds)

    lines = body.split("\n")

    # Extract metadata from early lines
    num_comments_match = re.search(r"(\d[\d,.]*k?)\s*comments?", body[:500])
    num_forecasters_match = re.search(r"([\d,.]+k?)\s*forecasters?", body[:500])

    # Detect type and prediction
    q_type, prediction = _detect_question_type(lines[:30])

    # Extract resolution criteria
    res_criteria = None
    fine_print = None
    rc_start = None
    fp_start = None
    for i, line in enumerate(lines):
        if line.strip() == "Resolution Criteria":
            rc_start = i + 1
        if line.strip() == "Fine Print":
            fp_start = i + 1
            if rc_start is not None:
                res_criteria = "\n".join(lines[rc_start:i]).strip()

    if rc_start is not None and res_criteria is None:
        # No fine print section — take until "Comments" or end
        end = len(lines)
        for i in range(rc_start, len(lines)):
            if lines[i].strip() in ("Comments", "Timeline", "Key Factors"):
                end = i
                break
        res_criteria = "\n".join(lines[rc_start:end]).strip()

    if fp_start is not None:
        end = len(lines)
        for i in range(fp_start, len(lines)):
            if lines[i].strip() in ("Comments",):
                end = i
                break
        fine_print = "\n".join(lines[fp_start:end]).strip()

    num_forecasters = num_forecasters_match.group(1) if num_forecasters_match else None

    # The text parse above depends on section headings in the rendered page and
    # has silently come back empty before; the API returns the exact source text.
    post = _api_post(post_id)
    if post:
        q = post.get("question") or {}
        title = post.get("title") or title
        res_criteria = q.get("resolution_criteria") or res_criteria
        fine_print = q.get("fine_print") or fine_print
        if post.get("nr_forecasters") is not None:
            num_forecasters = str(post["nr_forecasters"])

    return MetaculusQuestion(
        post_id=post_id,
        title=title,
        url=url,
        question_type=q_type,
        community_prediction=prediction,
        num_forecasters=num_forecasters,
        num_comments=num_comments_match.group(1) if num_comments_match else None,
        resolution_criteria=res_criteria,
        fine_print=fine_print,
    )


def main():
    parser = argparse.ArgumentParser(description="Scrape a Metaculus question")
    parser.add_argument("post_id", type=int, help="Metaculus post/question ID")
    parser.add_argument(
        "--json", action="store_true", help="Output as JSON instead of human-readable"
    )
    parser.add_argument(
        "--wait",
        type=int,
        default=10,
        help="Seconds to wait for JS render (default: 10)",
    )
    args = parser.parse_args()

    result = scrape_metaculus_question(
        post_id=args.post_id,
        wait_seconds=args.wait,
    )

    if args.json:
        print(json.dumps(asdict(result), indent=2, ensure_ascii=False))
    else:
        print(f"Title: {result.title}")
        print(f"URL:   {result.url}")
        print(f"Type:  {result.question_type}")
        print(f"Community Prediction: {result.community_prediction}")
        print(f"Forecasters: {result.num_forecasters}")
        print(f"Comments: {result.num_comments}")
        if result.resolution_criteria:
            print("\n--- Resolution Criteria ---")
            print(result.resolution_criteria[:500])
        # Say so explicitly, rather than letting silence read as "no discussion".
        print(
            f"\n(note: {result.num_comments or '?'} comments exist but are not "
            "extractable from the rendered page; use the metaculus-aggregations "
            "skill with --comments N for comment text)"
        )


if __name__ == "__main__":
    main()
