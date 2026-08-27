#!/usr/bin/env python3
"""
Metaculus question scraper using Playwright.

Extracts community prediction and comments from a Metaculus question page.
Works in sandboxed/containerised environments by routing through the egress proxy.

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
import sys
import time
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class MetaculusComment:
    author: str
    text: str
    author_prediction: Optional[str] = None
    date: Optional[str] = None
    votes: Optional[int] = None


@dataclass
class MetaculusQuestion:
    post_id: int
    title: str
    url: str
    question_type: str  # "binary", "date", "numeric", "multiple_choice", "unknown"
    community_prediction: Optional[str] = None
    num_forecasters: Optional[str] = None
    num_comments: Optional[str] = None
    resolution_criteria: Optional[str] = None
    fine_print: Optional[str] = None
    comments: list = field(default_factory=list)


def _parse_proxy() -> dict:
    """Parse the container egress proxy from environment."""
    proxy_url = os.environ.get("https_proxy", os.environ.get("HTTPS_PROXY", ""))
    m = re.match(r"http://([^:]+):([^@]+)@([^:]+):(\d+)", proxy_url)
    if not m:
        # Outside the Claude.ai sandbox there is no authenticated egress proxy;
        # a direct connection is correct there, so return no proxy config
        # instead of aborting.
        return {}
    return {
        "server": f"http://{m.group(3)}:{m.group(4)}",
        "username": m.group(1),
        "password": m.group(2),
    }


def _detect_question_type(lines: list[str]) -> tuple[str, Optional[str]]:
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
        if not line or line in (
            "Log in", "Recent", "Load more comments", "Oldest",
            "Changed my mind", "IMPACT", "STRENGTH", "Increases Likelihood",
            "Decreases Likelihood", "Earlier", "later",
        ) or line.startswith("Changed my mind") or line.startswith("hide "):
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
    from playwright.sync_api import sync_playwright

    proxy = _parse_proxy() or None
    url = f"https://www.metaculus.com/questions/{post_id}/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, proxy=proxy)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        )
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        time.sleep(wait_seconds)

        title = page.title()
        body = page.inner_text("body")
        browser.close()

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
        num_forecasters=num_forecasters_match.group(1) if num_forecasters_match else None,
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
        "--wait", type=int, default=10, help="Seconds to wait for JS render (default: 10)"
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
            print(f"\n--- Resolution Criteria ---")
            print(result.resolution_criteria[:500])
        if result.comments:
            print(f"\n--- Top {len(result.comments)} Comments ---")
            for c in result.comments:
                pred = f" [{c['author_prediction']}]" if c.get("author_prediction") else ""
                print(f"\n  @{c['author']}{pred}:")
                print(f"  {c['text'][:300]}")


if __name__ == "__main__":
    main()
