#!/usr/bin/env python3
"""List the Metaculus slugs whose forecast was added to the ledger between two git refs.

Used by CI after a pull request merges into ``main``: the slugs printed here are
the questions whose forecast changed in that merge, and nothing else. The ledger
is append-only (rule 8), so "added" is simply the lines present at ``HEAD`` that
were not present at ``BASE`` -- no diff parsing, no dependence on merge strategy.

Examples
--------
    uv run scripts/changed_forecasts.py origin/main~1 origin/main
    uv run scripts/changed_forecasts.py <base-sha> <merge-sha>
"""

from __future__ import annotations

import argparse
import json
import subprocess

LEDGER_PATH = "ledger/forecasts.jsonl"


def ledger_at(ref: str) -> list[str]:
    """Return the ledger's lines at ``ref`` (empty if the file did not exist yet)."""
    proc = subprocess.run(
        ["git", "show", f"{ref}:{LEDGER_PATH}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        # A ref before the ledger existed has no forecasts; any other git failure
        # (unknown ref, shallow clone) must not silently mean "nothing changed".
        if "does not exist" in proc.stderr or "exists on disk, but not in" in proc.stderr:
            return []
        raise SystemExit(f"git show {ref}:{LEDGER_PATH} failed: {proc.stderr.strip()}")
    return proc.stdout.splitlines()


def added_metaculus_slugs(base: list[str], head: list[str]) -> list[str]:
    """Slugs of Metaculus ``forecast`` records in ``head`` but not in ``base``.

    Parameters
    ----------
    base, head
        Raw ledger lines (JSON objects) at the two refs.

    Returns
    -------
    list[str]
        Unique slugs in first-seen ledger order. Resolutions and non-Metaculus
        questions are excluded: there is nothing to submit for them.
    """
    seen = set(base)
    slugs: list[str] = []
    for line in head:
        if not line.strip() or line in seen:
            continue
        rec = json.loads(line)
        if rec.get("event") != "forecast" or rec.get("source") != "metaculus":
            continue
        if rec["slug"] not in slugs:
            slugs.append(rec["slug"])
    return slugs


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("base", help="git ref before the change (e.g. the PR's base sha)")
    ap.add_argument("head", help="git ref after the change (e.g. the merge commit)")
    args = ap.parse_args()
    for slug in added_metaculus_slugs(ledger_at(args.base), ledger_at(args.head)):
        print(slug)


if __name__ == "__main__":
    main()
