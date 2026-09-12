#!/usr/bin/env python3
"""
Metaculus question scraper using Playwright (HTML fallback).

Extracts community prediction and comments by rendering the public question
page. This is the **fallback** path: prefer the ``metaculus-aggregations`` skill,
which returns structured numbers for all three cohorts. This script only ever
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

Usage:
    python metaculus_scrape.py <post_id> [--comments N] [--json]

Examples:
    python metaculus_scrape.py 578
    python metaculus_scrape.py 578 --comments 10 --json
    python metaculus_scrape.py 3479 --json
"""

import argparse
import json
import os
import re
import time
from dataclasses import asdict, dataclass, field
from typing import Any
from urllib.parse import unquote, urlparse

# The sandbox ships Chromium here; setting this lets Playwright find it without
# a separate `playwright install` step. Only set it when the store really
# exists -- on a normal workstation Playwright must keep its own location.
if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")

# Chromium flag that makes the handshake survive a TLS-1.3-intolerant MITM proxy.
_TLS12_ARG = "--ssl-version-max=tls1.2"

# Seconds to wait between retries of a challenged page load. Metaculus' IP-level
# rate limit was measured to clear in ~2 min, so short retries are wasted
# requests that only re-arm it.
_BACKOFF = (5, 30, 60, 75)

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
class MetaculusComment:
    author: str
    text: str
    author_prediction: str | None = None
    date: str | None = None
    votes: int | None = None


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
    comments: list = field(default_factory=list)


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
                page = browser.new_page(
                    user_agent=(
                        # Must NOT say "HeadlessChrome": Cloudflare challenges
                        # that token outright.
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                        "Chrome/122.0.0.0 Safari/537.36"
                    )
                )
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


def _parse_comments(lines: list[str], max_comments: int) -> list[MetaculusComment]:
    """
    Parse comments from the body text lines.

    Comment blocks follow this pattern:
        username
        ·
        [username's Prediction]  (optional)
        [prediction value]       (optional)
        [date]                   (optional)
        <blank line>
        comment text (one or more lines)
        <blank line>
        [number]                 (votes, optional)
        Reply
    """
    comments = []
    # Find the "Comments" section
    comments_start = None
    for i, line in enumerate(lines):
        if line.strip() == "Comments":
            comments_start = i
            break

    if comments_start is None:
        return comments

    # Walk through lines after "Comments"
    i = comments_start + 1
    while i < len(lines) and len(comments) < max_comments:
        line = lines[i].strip()

        # Skip empty lines and navigation elements
        if (
            not line
            or line
            in (
                "Log in",
                "Recent",
                "Load more comments",
                "Oldest",
                "Changed my mind",
                "IMPACT",
                "STRENGTH",
                "Increases Likelihood",
                "Decreases Likelihood",
                "Earlier",
                "later",
            )
            or line.startswith(("Changed my mind", "hide "))
        ):
            i += 1
            continue

        # A comment block starts with "username\n·"
        if i + 1 < len(lines) and lines[i + 1].strip() == "·":
            author = line
            i += 2  # skip past "·"

            # Check for optional prediction line: "username's Prediction"
            author_pred = None
            date = None
            if i < len(lines) and "'s Prediction" in lines[i]:
                i += 1
                # Next line is the prediction value
                if i < len(lines):
                    pred_line = lines[i].strip()
                    if pred_line and pred_line not in ("Reply",):
                        author_pred = pred_line
                        i += 1
                # Next might be the date
                if i < len(lines):
                    date_candidate = lines[i].strip()
                    if re.match(
                        r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}",
                        date_candidate,
                    ):
                        date = date_candidate
                        i += 1

            # Now collect the comment text until we hit "Reply" or a vote count
            text_lines = []
            while i < len(lines):
                cl = lines[i].strip()
                if cl == "Reply":
                    i += 1
                    break
                # Vote count is a lone number before "Reply"
                if (
                    cl.isdigit()
                    and i + 1 < len(lines)
                    and lines[i + 1].strip() == "Reply"
                ):
                    i += 1  # skip the vote count
                    continue
                if cl.startswith("Changed my mind"):
                    i += 1
                    continue
                # Another comment starting (username\n·)
                if (
                    i + 1 < len(lines)
                    and lines[i + 1].strip() == "·"
                    and cl
                    and not cl.startswith("@")
                ):
                    break
                text_lines.append(lines[i])
                i += 1

            text = "\n".join(text_lines).strip()
            if text:
                comments.append(
                    MetaculusComment(
                        author=author,
                        text=text,
                        author_prediction=author_pred,
                        date=date,
                    )
                )
        else:
            i += 1

    return comments


def scrape_metaculus_question(
    post_id: int,
    max_comments: int = 5,
    wait_seconds: int = 10,
) -> MetaculusQuestion:
    """
    Scrape a Metaculus question page for community prediction and comments.

    Parameters
    ----------
    post_id : int
        The numeric post ID from the Metaculus question URL.
    max_comments : int
        Maximum number of comments to extract (default 5).
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

    # Parse comments
    comments = _parse_comments(lines, max_comments)

    return MetaculusQuestion(
        post_id=post_id,
        title=title,
        url=url,
        question_type=q_type,
        community_prediction=prediction,
        num_forecasters=num_forecasters_match.group(1)
        if num_forecasters_match
        else None,
        num_comments=num_comments_match.group(1) if num_comments_match else None,
        resolution_criteria=res_criteria,
        fine_print=fine_print,
        comments=[asdict(c) for c in comments],
    )


def main():
    parser = argparse.ArgumentParser(description="Scrape a Metaculus question")
    parser.add_argument("post_id", type=int, help="Metaculus post/question ID")
    parser.add_argument(
        "--comments", type=int, default=5, help="Max comments to extract (default: 5)"
    )
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
        max_comments=args.comments,
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
        if args.comments and not result.comments:
            # Comments now live behind a lazy-loaded tab that does not survive a
            # scripted click, so the HTML path cannot see them at all. Say so,
            # rather than letting an empty list read as "no discussion".
            print(
                f"\n(note: {result.num_comments or '?'} comments exist but are not "
                "extractable from the rendered page; use the metaculus-aggregations "
                "skill with --comments N for comment text)"
            )
        if result.comments:
            print(f"\n--- Top {len(result.comments)} Comments ---")
            for c in result.comments:
                pred = (
                    f" [{c['author_prediction']}]" if c.get("author_prediction") else ""
                )
                print(f"\n  @{c['author']}{pred}:")
                print(f"  {c['text'][:300]}")


if __name__ == "__main__":
    main()
