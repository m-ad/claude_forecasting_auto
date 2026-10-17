#!/usr/bin/env python3
"""Fetch and cache Metaculus aggregations for one or more questions, in one browser.

Each Metaculus post is fetched once (group subquestions share their post), and
the result is cached in every matching question folder under the name that says
what it holds:

- ``raw/metaculus-<date>.json``: the full fetch (cohorts, criteria, comments);
- ``raw/metaculus-api-<date>.json``: a pool block left only the API-key
  metadata. The cohorts were *not* fetched, which is not the same as "no data".

Examples
--------
    uv run scripts/fetch_metaculus.py mc45262 mc45617 2026-09-20-mc45219-us-national-debt...
    uv run scripts/fetch_metaculus.py mc45262 --comments 10 --no-history

Exit status: 0 when every post was fetched, 3 when at least one was blocked and
none failed (re-fetch once in ~90 min), 1 when any post failed or did not resolve.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import QUESTIONS, REPO, find_slug, load_meta, make_stdio_lenient, today

SKILL_SCRIPTS = REPO / ".claude" / "skills" / "metaculus-aggregations" / "scripts"


def snapshot_name(result: Any, day: str) -> str:
    """The ``raw/`` file name for one fetch result, by what it actually holds."""
    return f"metaculus-api-{day}.json" if result.blocked else f"metaculus-{day}.json"


def resolve(needles: list[str]) -> tuple[dict[int, list[str]], list[str]]:
    """Map each needle to its slug, and group the slugs by Metaculus post id.

    Returns
    -------
    (dict, list)
        Post id -> slugs (in argument order, without duplicates), and one error
        line per needle that did not resolve to a Metaculus question.
    """
    by_post: dict[int, list[str]] = {}
    errors: list[str] = []
    for needle in needles:
        slug = find_slug(needle)
        if slug is None:
            errors.append(f"{needle} | FAILED | no unique question matches")
            continue
        meta = load_meta(slug)
        pid = meta.get("post_id")
        if meta.get("source") != "metaculus" or not pid:
            errors.append(f"{slug} | FAILED | not a Metaculus question")
            continue
        slugs = by_post.setdefault(int(pid), [])
        if slug not in slugs:
            slugs.append(slug)
    return by_post, errors


def cache_results(
    by_post: dict[int, list[str]],
    results: dict[int, Any],
    day: str,
    root: Path = QUESTIONS,
) -> tuple[list[str], int]:
    """Write every result into its slugs' ``raw/`` folders.

    A failed post writes nothing: an empty or error-shaped file under a dated
    name would read as a snapshot.

    Returns
    -------
    (list of str, int)
        One report line per slug, and the exit status (see the module docstring).
    """
    lines: list[str] = []
    failed = blocked = False
    for pid, slugs in by_post.items():
        res = results.get(pid)
        for slug in slugs:
            if res is None or isinstance(res, Exception):
                failed = True
                lines.append(f"{slug} | FAILED | {res or 'not fetched'}")
                continue
            raw = root / slug / "raw"
            raw.mkdir(parents=True, exist_ok=True)
            path = raw / snapshot_name(res, day)
            path.write_text(
                json.dumps(asdict(res), indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            blocked = blocked or res.blocked
            state = "BLOCKED (metadata only)" if res.blocked else "fetched"
            lines.append(f"{slug} | {state} | {path.relative_to(root.parent)}")
    return lines, 1 if failed else (3 if blocked else 0)


def main() -> None:
    make_stdio_lenient()
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("questions", nargs="+", help="slug, post id, URL or title fragment")
    ap.add_argument(
        "--comments", type=int, default=8, help="recent comments (default 8)"
    )
    ap.add_argument(
        "--no-history",
        dest="history",
        action="store_false",
        help="skip the CP-vs-time series",
    )
    ap.add_argument("--date", default=today(), help="retrieval date for file names")
    args = ap.parse_args()

    by_post, errors = resolve(args.questions)
    results: dict[int, Any] = {}
    if by_post:
        sys.path.insert(0, str(SKILL_SCRIPTS))
        from metaculus_aggregations import fetch_many  # type: ignore

        results = fetch_many(
            list(by_post), include_history=args.history, n_comments=args.comments
        )
    lines, code = cache_results(by_post, results, args.date)
    for line in errors + lines:
        print(line)
    if code == 3:
        blocked = [line.split(" | ")[0] for line in lines if "BLOCKED" in line]
        print(
            "\nPool block: re-fetch these once in ~90 min, not before:\n"
            f"  uv run scripts/fetch_metaculus.py {' '.join(blocked)}",
            file=sys.stderr,
        )
    sys.exit(1 if errors else code)


if __name__ == "__main__":
    main()
