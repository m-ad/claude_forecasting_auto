#!/usr/bin/env python3
"""Read and write ``tournaments/registry.yaml`` — the list of tournaments the bot competes in.

The registry is the single place that answers "which tournaments are live, and in
what order do they get the budget?". The sweep gate reads it before spending a
token; the operator writes it, through this script. The bot never does: the gate is
stateless (it asks Metaculus which questions the bot has already forecast), so the
registry only changes when a human changes policy -- and a file only humans write
cannot conflict when ``main`` is merged into ``live-bot``.

Multi-tournament is the default rather than a later generalisation because
MiniBench and a FutureEval season can burst at the same time, and the resolution
of that collision — ``priority`` first, then the soonest close — has to exist
before the first collision, not after it.

Examples
--------
    uv run scripts/tournament_registry.py list
    uv run scripts/tournament_registry.py add https://www.metaculus.com/tournament/minibench/ \
        --name MiniBench --priority 1 --scored
    uv run scripts/tournament_registry.py set minibench --active
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import REPO, today

REGISTRY = REPO / "tournaments" / "registry.yaml"

MODES = ("one_shot", "updatable")
ENTRY_KEYS = (
    "slug",
    "url",
    "name",
    "added",
    "active",
    "mode",
    "scored",
    "priority",
)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class RegistryError(RuntimeError):
    """A registry operation that cannot be completed as asked."""


# ------------------------------------------------------------------ load/save
def load_registry() -> list[dict[str, Any]]:
    """Return every tournament entry, in file order.

    Returns
    -------
    list of dict
        One mapping per tournament. An absent registry file is an empty list, not
        an error: a fresh checkout has no tournaments and the gate must simply
        find nothing to do.
    """
    if not REGISTRY.exists():
        return []
    doc = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    entries = doc.get("tournaments") or []
    if not isinstance(entries, list):
        raise RegistryError("tournaments/registry.yaml: `tournaments` is not a list")
    return [e for e in entries if isinstance(e, dict)]


def save_registry(entries: list[dict[str, Any]]) -> None:
    """Write the registry back, entries ordered by ``(priority, slug)``.

    Sorting on write rather than on read means a human opening the file sees the
    order the sweep will actually use.
    """
    ordered = sorted(entries, key=lambda e: (e.get("priority", 99), e.get("slug", "")))
    normalised = [{k: e.get(k) for k in ENTRY_KEYS} for e in ordered]
    header = _preserved_header()
    body = yaml.safe_dump(
        {"tournaments": normalised}, sort_keys=False, allow_unicode=True, width=100
    )
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY.write_text(header + body, encoding="utf-8")


def _preserved_header() -> str:
    """The leading comment block of the registry, which ``safe_dump`` would drop.

    The comments document what ``priority``, ``mode`` and ``scored`` mean, and the
    file is read by humans deciding whether to activate a tournament — losing them
    on the first write would be a slow leak of the only documentation at the point
    of use.
    """
    if not REGISTRY.exists():
        return ""
    lines = []
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            lines.append(line)
            continue
        break
    return "\n".join(lines) + "\n" if lines else ""


# --------------------------------------------------------------------- lookup
def get(slug: str) -> dict[str, Any]:
    """Return one entry by slug, or raise ``RegistryError``."""
    for entry in load_registry():
        if entry.get("slug") == slug:
            return entry
    known = [e.get("slug") for e in load_registry()]
    raise RegistryError(f"no tournament {slug!r} in the registry (known: {known})")


def active_tournaments() -> list[dict[str, Any]]:
    """Active entries in sweep order: ``priority`` ascending, then slug.

    The sweep gate walks this list and stops when the per-run forecast budget runs
    out, so the order *is* the spending policy — a scored tournament ahead of a
    smoke-test one.
    """
    return sorted(
        (e for e in load_registry() if e.get("active")),
        key=lambda e: (e.get("priority", 99), e.get("slug", "")),
    )


def slug_from_url(url: str) -> str | None:
    """Pull the tournament slug out of a Metaculus tournament URL."""
    m = re.search(r"/(?:tournament|project)/([^/?#]+)", url)
    return m.group(1).lower() if m else None


# --------------------------------------------------------------------- writes
def add(
    url_or_slug: str,
    *,
    name: str | None = None,
    mode: str = "one_shot",
    priority: int = 5,
    scored: bool = True,
    active: bool = True,
) -> dict[str, Any]:
    """Add a tournament, returning the new entry.

    Parameters
    ----------
    url_or_slug : str
        A Metaculus tournament URL, or the bare slug.
    name : str, optional
        Human-readable name; defaults to the slug title-cased.
    mode : {'one_shot', 'updatable'}
        ``one_shot`` for bot tournaments — one forecast per question, no updates.
    priority : int
        Lower wins when the per-run budget cannot cover every open question.
    scored : bool
        Whether results affect a public ranking.
    active : bool
        Whether the sweep should pick it up at all.

    Raises
    ------
    RegistryError
        If the slug is unusable or already registered.
    """
    slug = slug_from_url(url_or_slug) or url_or_slug.strip().lower()
    if not SLUG_RE.match(slug):
        raise RegistryError(f"{slug!r} is not a lowercase kebab-case tournament slug")
    if mode not in MODES:
        raise RegistryError(f"mode {mode!r} not in {list(MODES)}")
    if priority < 1:
        raise RegistryError("priority is 1-based; lower numbers are forecast first")
    entries = load_registry()
    if any(e.get("slug") == slug for e in entries):
        raise RegistryError(f"{slug!r} is already registered")
    entry = {
        "slug": slug,
        "url": url_or_slug
        if url_or_slug.startswith("http")
        else f"https://www.metaculus.com/tournament/{slug}/",
        "name": name or slug.replace("-", " ").title(),
        "added": today(),
        "active": bool(active),
        "mode": mode,
        "scored": bool(scored),
        "priority": int(priority),
    }
    entries.append(entry)
    save_registry(entries)
    return entry


def update(slug: str, **fields: Any) -> dict[str, Any]:
    """Set fields on one entry. Unknown keys raise rather than being ignored."""
    unknown = sorted(set(fields) - set(ENTRY_KEYS))
    if unknown:
        raise RegistryError(f"unknown registry field(s): {unknown}")
    entries = load_registry()
    for entry in entries:
        if entry.get("slug") != slug:
            continue
        entry.update({k: v for k, v in fields.items() if v is not None})
        save_registry(entries)
        return entry
    raise RegistryError(f"no tournament {slug!r} in the registry")


# ------------------------------------------------------------------------ CLI
def _print_table(entries: list[dict[str, Any]]) -> None:
    if not entries:
        print("(no tournaments registered)")
        return
    head = f"{'slug':<22} {'pri':>3} {'mode':<10} {'scored':<6} active"
    print(head)
    print("-" * len(head))
    for e in entries:
        print(
            f"{e.get('slug')!s:<22} {e.get('priority', ''):>3} "
            f"{e.get('mode')!s:<10} {e.get('scored')!s:<6} {e.get('active')!s}"
        )


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    ls = sub.add_parser("list", help="show the registry in sweep order")
    ls.add_argument("--active", action="store_true", help="active tournaments only")
    ls.add_argument("--json", action="store_true")

    g = sub.add_parser("get", help="show one tournament")
    g.add_argument("slug")
    g.add_argument("--json", action="store_true")

    a = sub.add_parser("add", help="register a tournament")
    a.add_argument("url", help="tournament URL or bare slug")
    a.add_argument("--name")
    a.add_argument("--mode", default="one_shot", choices=list(MODES))
    a.add_argument(
        "--priority", type=int, default=5, help="lower is forecast first (default 5)"
    )
    a.add_argument("--unscored", action="store_true", help="does not affect a ranking")
    a.add_argument("--inactive", action="store_true", help="register but do not sweep")

    s = sub.add_parser("set", help="change fields on a registered tournament")
    s.add_argument("slug")
    s.add_argument("--name")
    s.add_argument("--mode", choices=list(MODES))
    s.add_argument("--priority", type=int)
    activity = s.add_mutually_exclusive_group()
    activity.add_argument("--active", dest="active", action="store_true", default=None)
    activity.add_argument("--inactive", dest="active", action="store_false")
    scoring = s.add_mutually_exclusive_group()
    scoring.add_argument("--scored", dest="scored", action="store_true", default=None)
    scoring.add_argument("--unscored", dest="scored", action="store_false")


    args = ap.parse_args()
    try:
        if args.cmd == "list":
            entries = active_tournaments() if args.active else load_registry()
            entries = sorted(
                entries, key=lambda e: (e.get("priority", 99), e.get("slug", ""))
            )
            print(json.dumps(entries, indent=2)) if args.json else _print_table(entries)
        elif args.cmd == "get":
            entry = get(args.slug)
            print(json.dumps(entry, indent=2)) if args.json else _print_table([entry])
        elif args.cmd == "add":
            entry = add(
                args.url,
                name=args.name,
                mode=args.mode,
                priority=args.priority,
                scored=not args.unscored,
                active=not args.inactive,
            )
            print(f"registered {entry['slug']} (priority {entry['priority']})")
        elif args.cmd == "set":
            entry = update(
                args.slug,
                name=args.name,
                mode=args.mode,
                priority=args.priority,
                active=args.active,
                scored=args.scored,
            )
            _print_table([entry])
    except RegistryError as exc:
        sys.exit(f"! {exc}")


if __name__ == "__main__":
    main()
