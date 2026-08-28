#!/usr/bin/env python3
"""Scaffold a question folder under ``questions/``.

Examples
--------
    uv run scripts/new_question.py --url https://www.metaculus.com/questions/43505/...
    uv run scripts/new_question.py --title "Will X happen by 2027?" --type binary --source other
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import QUESTIONS, REPO, SRC_ABBREV, TEMPLATES, slugify, today

SKILL_SCRIPTS = REPO / ".claude" / "skills" / "metaculus-aggregations" / "scripts"


def fetch_metaculus(post_id: int) -> dict[str, Any]:
    """Pull title/type/close-time for a Metaculus post, tolerating failure.

    Returns an empty dict when the fetch fails, so scaffolding never blocks on
    network trouble — the agent can fill the fields in by hand.
    """
    sys.path.insert(0, str(SKILL_SCRIPTS))
    try:
        from metaculus_aggregations import fetch_aggregations  # type: ignore

        res = fetch_aggregations(post_id, methods=["recency_weighted"])
    except Exception as exc:  # noqa: BLE001 - any failure degrades to manual entry
        print(f"! Metaculus fetch failed ({exc}); scaffolding with blanks.")
        return {}
    return {
        "title": res.title,
        "type": res.question_type,
        "closes": (res.scheduled_close_time or "")[:10] or None,
        "status": res.status,
        "nr_forecasters": res.nr_forecasters,
    }


def render(template: Path, mapping: dict[str, str]) -> str:
    """Substitute ``{{KEY}}`` placeholders in a template file."""
    text = template.read_text(encoding="utf-8")
    for key, val in mapping.items():
        text = text.replace("{{" + key + "}}", val)
    return text


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--url", help="question URL (Metaculus URLs are parsed for the post id)"
    )
    ap.add_argument("--post-id", type=int, help="Metaculus post id")
    ap.add_argument("--title", help="question title (required for non-Metaculus)")
    ap.add_argument(
        "--type",
        default="binary",
        choices=["binary", "numeric", "date", "multiple_choice", "discrete"],
    )
    ap.add_argument(
        "--source",
        default=None,
        choices=list(SRC_ABBREV),
        help="defaults to metaculus when an id is known",
    )
    ap.add_argument("--slug", help="override the derived slug fragment")
    args = ap.parse_args()

    post_id: int | None = args.post_id
    if args.url and not post_id:
        m = re.search(r"/questions/(\d+)", args.url)
        if m:
            post_id = int(m.group(1))

    source = args.source or ("metaculus" if post_id else "other")
    title, qtype, closes = args.title, args.type, None

    if source == "metaculus" and post_id:
        meta_remote = fetch_metaculus(post_id)
        title = title or meta_remote.get("title")
        qtype = meta_remote.get("type") or qtype
        closes = meta_remote.get("closes")

    if not title:
        ap.error("--title is required when the title cannot be fetched")

    frag = args.slug or slugify(title)
    ident = f"{SRC_ABBREV[source]}{post_id}" if post_id else SRC_ABBREV[source]
    slug = f"{today()}-{ident}-{frag}"

    folder = QUESTIONS / slug
    if folder.exists():
        sys.exit(f"! {folder} already exists")
    (folder / "raw").mkdir(parents=True)
    (folder / "charts").mkdir()

    mapping = {
        "SLUG": slug,
        "TITLE": title.replace('"', "'"),
        "SOURCE": source,
        "URL": args.url
        or (f"https://www.metaculus.com/questions/{post_id}/" if post_id else ""),
        "POST_ID": str(post_id) if post_id else "null",
        "TYPE": qtype,
        "TODAY": today(),
    }
    for name in ("meta.yaml", "forecast.md", "research.md"):
        (folder / name).write_text(render(TEMPLATES / name, mapping), encoding="utf-8")

    if closes:
        text = (folder / "meta.yaml").read_text(encoding="utf-8")
        (folder / "meta.yaml").write_text(
            text.replace("  closes: null", f'  closes: "{closes}"'), encoding="utf-8"
        )

    print(slug)
    print(f"created {folder.relative_to(REPO)}")


if __name__ == "__main__":
    main()
