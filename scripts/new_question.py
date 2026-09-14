#!/usr/bin/env python3
"""Scaffold a question folder under ``questions/``.

Examples
--------
    uv run scripts/new_question.py --url https://www.metaculus.com/questions/43505/...
    uv run scripts/new_question.py --title "Will X happen by 2027?" --type binary --source other
    uv run scripts/new_question.py --url <url> --tournament minibench \
        --opened 2026-09-14T11:03:00Z --closes 2026-09-14T12:33:00Z
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
        "close_time": res.scheduled_close_time,
        "question_id": res.question_id,
        "status": res.status,
        "nr_forecasters": res.nr_forecasters,
    }


TOURNAMENT_MODES = ("one_shot", "updatable")

# The template's `tournament: null` plus the commented example block that follows
# it, up to the `current:` key that ends the region.
TOURNAMENT_PLACEHOLDER_RE = re.compile(
    r"^tournament: null.*?\n\ncurrent:", re.MULTILINE | re.DOTALL
)


def _yaml_str(value: str | None) -> str:
    """Render an optional scalar as a quoted YAML string or ``null``."""
    return f'"{value}"' if value else "null"


def tournament_block(
    tslug: str, mode: str, opened: str | None, closes: str | None, registered: str
) -> str:
    """Render the ``tournament:`` mapping for a bot-tournament question.

    Emitted as text rather than dumped with PyYAML so the rest of the scaffold -
    hand-written YAML that carries the schema's documentation in its comments -
    survives intact. The submission fields start empty: they are written by
    ``log_forecast.py submit`` once the API has actually accepted a forecast, so
    that a scaffolded-but-unsubmitted question is never mistaken for a sent one.
    """
    return "\n".join(
        [
            "tournament:",
            f'  slug: "{tslug}"',
            f'  mode: "{mode}"',
            f'  registered: "{registered}"',
            f"  opened: {_yaml_str(opened)}",
            f"  closes: {_yaml_str(closes)}",
            "  submitted: null",
            "  submitted_forecast: null",
            "  comment_posted: false",
            "  official_score: null",
            "  missed_window: false",
        ]
    )


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
    ap.add_argument(
        "--question-id",
        type=int,
        help="Metaculus question id; fetched automatically when it can be",
    )
    ap.add_argument(
        "--tournament",
        help="tournament slug from tournaments/registry.yaml; makes this a bot question",
    )
    ap.add_argument(
        "--tournament-mode",
        default="one_shot",
        choices=list(TOURNAMENT_MODES),
        help="one_shot (bot tournaments) forecasts once and never revisits",
    )
    ap.add_argument("--opened", help="ISO-8601 UTC instant the tournament window opened")
    ap.add_argument("--closes", help="ISO-8601 UTC instant the tournament window closes")
    args = ap.parse_args()

    if not args.tournament and (args.opened or args.closes):
        ap.error("--opened/--closes describe a tournament window; pass --tournament too")

    post_id: int | None = args.post_id
    if args.url and not post_id:
        m = re.search(r"/questions/(\d+)", args.url)
        if m:
            post_id = int(m.group(1))

    source = args.source or ("metaculus" if post_id else "other")
    title, qtype, closes = args.title, args.type, None
    question_id: int | None = args.question_id

    if source == "metaculus" and post_id:
        meta_remote = fetch_metaculus(post_id)
        title = title or meta_remote.get("title")
        qtype = meta_remote.get("type") or qtype
        closes = meta_remote.get("closes")
        question_id = question_id or meta_remote.get("question_id")

    if not title:
        ap.error("--title is required when the title cannot be fetched")

    frag = args.slug or slugify(title)
    ident = f"{SRC_ABBREV[source]}{post_id}" if post_id else SRC_ABBREV[source]
    slug = f"{today()}-{ident}-{frag}"

    folder = QUESTIONS / slug
    if folder.exists():
        sys.exit(f"! {folder} already exists")
    (folder / "raw").mkdir(parents=True)

    mapping = {
        "SLUG": slug,
        "TITLE": title.replace('"', "'"),
        "SOURCE": source,
        "URL": args.url
        or (f"https://www.metaculus.com/questions/{post_id}/" if post_id else ""),
        "POST_ID": str(post_id) if post_id else "null",
        "QUESTION_ID": str(question_id) if question_id else "null",
        "TYPE": qtype,
        "TODAY": today(),
    }
    # A one-shot tournament question is forecast inside a ~90-minute window and
    # never revisited, so a working log has no second reader: its sources go
    # straight into forecast.md and research.md is not scaffolded at all.
    one_shot = args.tournament and args.tournament_mode == "one_shot"
    files = ["meta.yaml", "forecast.md"] + ([] if one_shot else ["research.md"])
    for name in files:
        (folder / name).write_text(render(TEMPLATES / name, mapping), encoding="utf-8")

    text = (folder / "meta.yaml").read_text(encoding="utf-8")
    # `dates.closes` is a calendar day; the tournament window is an instant. When
    # only the window is known, the day it falls on is the right answer for triage.
    closes = closes or (args.closes or "")[:10] or None
    if closes:
        text = text.replace("  closes: null", f'  closes: "{closes}"')
    if args.tournament:
        # Swallow the commented-out example block along with the `null`: it
        # documents exactly the keys we are about to write, and leaving it behind
        # would put the schema's own docs after the real values.
        text = TOURNAMENT_PLACEHOLDER_RE.sub(
            lambda _: tournament_block(
                args.tournament,
                args.tournament_mode,
                args.opened,
                args.closes,
                today(),
            )
            + "\n\ncurrent:",
            text,
            count=1,
        )
    (folder / "meta.yaml").write_text(text, encoding="utf-8")

    print(slug)
    print(f"created {folder.relative_to(REPO)}")
    if args.tournament:
        print(f"tournament {args.tournament} ({args.tournament_mode})")


if __name__ == "__main__":
    main()
