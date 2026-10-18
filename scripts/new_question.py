#!/usr/bin/env python3
"""Scaffold a question folder under ``questions/``.

Metaculus metadata comes from the official API (``scripts/metaculus_api.py``) with
the bot token. For a Metaculus question the forecaster-facing part of the post --
title, type, resolution criteria, fine print, background, bounds, options, window
-- is cached to ``raw/metaculus-question-<date>.json``, so the forecaster reads the
criteria from disk and never calls Metaculus itself.

Examples
--------
    uv run scripts/new_question.py --url https://www.metaculus.com/questions/43505/...
    uv run scripts/new_question.py --title "Will X happen by 2027?" --type binary --source other
    uv run scripts/new_question.py --post-id 46044 --tournament minibench --reuse
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (
    QUESTIONS,
    REPO,
    SRC_ABBREV,
    TEMPLATES,
    all_questions,
    slugify,
    today,
)

TOURNAMENT_MODES = ("one_shot", "updatable")

# The template's `tournament: null` plus the commented example block that follows
# it, up to the `current:` key that ends the region.
TOURNAMENT_PLACEHOLDER_RE = re.compile(
    r"^tournament: null.*?\n\ncurrent:", re.MULTILINE | re.DOTALL
)


def _group_subquestions(post: dict[str, Any]) -> list[dict[str, Any]]:
    """``{label, id, type}`` per subquestion of a group post; empty for any other.

    A group-of-questions post (one subquestion per year, say) carries no
    top-level ``question``: type, id and label live on each subquestion under
    ``group_of_questions``.
    """
    group = post.get("group_of_questions") or {}
    return [
        {"label": q.get("label"), "id": q.get("id"), "type": q.get("type")}
        for q in group.get("questions") or []
    ]


def _shared_type(subqs: list[dict[str, Any]]) -> str | None:
    """The one type every subquestion shares, or None when they differ or none exist."""
    types = {q.get("type") for q in subqs}
    return types.pop() if len(types) == 1 else None


def _day(ts: str | None) -> str | None:
    """The ``YYYY-MM-DD`` part of an ISO timestamp, or None."""
    return (ts or "")[:10] or None


def fetch_metaculus(post_id: int) -> dict[str, Any]:
    """Pull title/type/window/ids for a Metaculus post, tolerating failure.

    Returns an empty dict when the fetch fails, so scaffolding never blocks on
    network trouble -- the fields can be filled in by hand. For a group post,
    ``type`` is the subquestions' shared type (None if they differ) and
    ``subquestions`` lists them; it is empty for a single-question post.
    ``snapshot`` is what goes to ``raw/`` (single-question posts only).
    """
    try:
        import metaculus_api as mapi

        post = mapi.get_post(post_id, stage="scaffold")
    except Exception as exc:  # noqa: BLE001 - any failure degrades to manual entry
        print(f"! Metaculus fetch failed ({exc}); scaffolding with blanks.", file=sys.stderr)
        return {}
    q = post.get("question") or {}
    subqs = _group_subquestions(post)
    return {
        "title": post.get("title"),
        # Without this a group came back typeless and was silently scaffolded as
        # the --type default, "binary".
        "type": q.get("type") or _shared_type(subqs),
        "question_id": q.get("id"),
        "opens": _day(post.get("open_time") or q.get("open_time")),
        "closes": _day(post.get("scheduled_close_time")),
        "resolves": _day(post.get("scheduled_resolve_time")),
        "open_time": q.get("open_time") or post.get("open_time"),
        "close_time": q.get("scheduled_close_time") or post.get("scheduled_close_time"),
        # The post reads "approved" before opening; only the question says
        # "upcoming", which is what the pre-open warning keys on.
        "status": q.get("status") or post.get("status"),
        "unit": q.get("unit"),
        "subquestions": subqs,
        "snapshot": mapi.question_snapshot(post, q) if q else None,
    }


def _yaml_str(value: str | None) -> str:
    """Render an optional scalar as a quoted YAML string or ``null``."""
    return f'"{value}"' if value else "null"


def tournament_block(
    tslug: str, mode: str, opened: str | None, closes: str | None, registered: str
) -> str:
    """Render the ``tournament:`` mapping for a bot-tournament question.

    Emitted as text rather than dumped with PyYAML so the rest of the scaffold --
    hand-written YAML that carries the schema's documentation in its comments --
    survives intact. The submission fields start empty: ``submit_metaculus.py``
    writes them once the API has actually accepted a forecast, so a
    scaffolded-but-unsubmitted question is never mistaken for a sent one.
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


def existing_slug(post_id: int, tournament: str | None = None) -> str | None:
    """The folder already scaffolded for this post (in this tournament), if any.

    The sweep re-enters a question whose earlier job died after scaffolding; it
    must reuse that folder, not make a second one for the same question.
    """
    for slug, meta in all_questions():
        if meta.get("post_id") != post_id:
            continue
        if tournament and (meta.get("tournament") or {}).get("slug") != tournament:
            continue
        return slug
    return None


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
    ap.add_argument(
        "--reuse",
        action="store_true",
        help="if this post already has a folder, print its slug and stop",
    )
    args = ap.parse_args()

    post_id: int | None = args.post_id
    if args.url and not post_id:
        m = re.search(r"/questions/(\d+)", args.url)
        if m:
            post_id = int(m.group(1))

    if args.reuse and post_id:
        found = existing_slug(post_id, args.tournament)
        if found:
            print(found)
            print(f"reusing questions/{found}")
            return

    source = args.source or ("metaculus" if post_id else "other")
    title, qtype = args.title, args.type
    question_id: int | None = args.question_id
    dates: dict[str, str | None] = {}
    meta_remote: dict[str, Any] = {}

    if source == "metaculus" and post_id:
        meta_remote = fetch_metaculus(post_id)
        title = title or meta_remote.get("title")
        qtype = meta_remote.get("type") or qtype
        question_id = question_id or meta_remote.get("question_id")
        dates = {
            "opened": meta_remote.get("opens"),
            "closes": meta_remote.get("closes"),
            "resolves": meta_remote.get("resolves"),
        }
        if meta_remote.get("status") == "upcoming":
            print(
                f"note: post {post_id} is not open yet (opens "
                f"{meta_remote.get('opens') or '?'}). Bot tokens see null question "
                "text before a question opens; scaffold again once it is open.",
                file=sys.stderr,
            )
        # Diagnostics go to stderr so stdout keeps its shape: slug, then path.
        subqs = meta_remote.get("subquestions") or []
        if subqs:
            print(
                f"note: post {post_id} is a group of {len(subqs)} subquestions; "
                "each is forecast separately:",
                file=sys.stderr,
            )
            for sq in subqs:
                print(
                    f"  {sq['label']}: question {sq['id']} ({sq['type']})",
                    file=sys.stderr,
                )
            pinned = re.search(r"[?&]sub-question=(\d+)", args.url or "")
            if pinned:
                question_id = int(pinned.group(1))
            else:
                # The URL's sub-question id is the only slug-to-subquestion
                # mapping the repo keeps; submission refuses a group slug without it.
                print(
                    "! pin this slug's subquestion: end meta.yaml's url with "
                    "?sub-question=<id> (or pass --url with it), and set question_id",
                    file=sys.stderr,
                )
            if not meta_remote.get("type"):
                print(
                    f"! the subquestions differ in type; scaffolding as --type {qtype}",
                    file=sys.stderr,
                )

    if not title:
        ap.error("--title is required when the title cannot be fetched")

    frag = args.slug or slugify(title)
    ident = f"{SRC_ABBREV[source]}{post_id}" if post_id else SRC_ABBREV[source]
    slug = f"{today()}-{ident}-{frag}"

    folder = QUESTIONS / slug
    if folder.exists():
        sys.exit(f"! {folder} already exists")
    (folder / "raw").mkdir(parents=True)

    clean_title = title.replace('"', "'")
    url = args.url or (
        f"https://www.metaculus.com/questions/{post_id}/" if post_id else ""
    )
    # Free-text questions have no URL: meta.yaml gets null and the link line
    # degrades to the plain title, never an empty ``[title]()`` link.
    link_title = clean_title.replace("[", "\\[").replace("]", "\\]")
    one_shot = bool(args.tournament) and args.tournament_mode == "one_shot"
    window = (
        f"{meta_remote.get('open_time') or '?'} -> {meta_remote.get('close_time') or '?'}"
    )
    mapping = {
        "SLUG": slug,
        "TITLE": clean_title,
        "SOURCE": source,
        "URL": url,
        "URL_YAML": f'"{url}"' if url else "null",
        "QUESTION_LINK": f"[{link_title}]({url})" if url else clean_title,
        "SOURCE_LINE": f"{source} — {url}"
        if url
        else f"{source} — no URL (free-text question)",
        "POST_ID": str(post_id) if post_id else "null",
        "QUESTION_ID": str(question_id) if question_id else "null",
        "TYPE": qtype,
        "TODAY": today(),
        "TOURNAMENT": args.tournament or "",
        "WINDOW": window,
        "DATES": " / ".join(
            str(dates.get(k) or "—") for k in ("opened", "closes", "resolves")
        ),
    }
    # A one-shot tournament question is forecast once inside a 3-hour window and
    # never revisited: a working log has no second reader, so its sources go
    # straight into the short-form forecast.md and research.md is not scaffolded.
    files = {"meta.yaml": "meta.yaml"}
    if one_shot:
        files["forecast.md"] = "forecast-tournament.md"
    else:
        files.update({"forecast.md": "forecast.md", "research.md": "research.md"})
    for name, template in files.items():
        (folder / name).write_text(
            render(TEMPLATES / template, mapping), encoding="utf-8"
        )

    text = (folder / "meta.yaml").read_text(encoding="utf-8")
    for key, day in dates.items():
        if day:
            text = text.replace(f"  {key}: null", f'  {key}: "{day}"', 1)
    if meta_remote.get("unit") and qtype not in ("binary", "multiple_choice"):
        unit = str(meta_remote["unit"]).replace('"', "'")
        text = text.replace("unit: null ", f'unit: "{unit}" ', 1)
    if args.tournament:
        # Swallow the commented-out example block along with the `null`: it
        # documents exactly the keys about to be written, and leaving it behind
        # would put the schema's own docs after the real values.
        block = tournament_block(
            args.tournament,
            args.tournament_mode,
            meta_remote.get("open_time"),
            meta_remote.get("close_time"),
            today(),
        )
        text = TOURNAMENT_PLACEHOLDER_RE.sub(
            lambda _: block + "\n\ncurrent:", text, count=1
        )
    (folder / "meta.yaml").write_text(text, encoding="utf-8")

    snapshot = meta_remote.get("snapshot")
    if snapshot:
        (folder / "raw" / f"metaculus-question-{today()}.json").write_text(
            json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    print(slug)
    print(f"created {folder.relative_to(REPO)}")
    if args.tournament:
        print(f"tournament {args.tournament} ({args.tournament_mode})")


if __name__ == "__main__":
    main()
