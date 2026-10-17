#!/usr/bin/env python3
"""Undo anything the forecaster session changed outside its own question.

The CI forecaster may run Python (a Monte Carlo model, a distribution fit), and a
Python process is not bound by the Edit/Write permission rules in
``.claude/settings.ci.json``. The steps after the session run with the Metaculus
token and a push credential, so before them this restores the repository to what
the session was allowed to change:

- every tracked file outside ``questions/<slug>/`` and the ledger goes back to
  ``HEAD`` (modified or deleted alike);
- every untracked file outside ``questions/<slug>/`` is deleted;
- the ledger keeps its committed lines and only the new lines the session may
  legitimately add: ``forecast`` records for its own slug (``log_forecast.py add``).

Standard library only, and the workflow runs the copy committed at ``HEAD``
(``git show HEAD:scripts/ci_guard.py | python3 -I - <slug>``), so a session that
edited this file, ``pyproject.toml`` or the virtualenv cannot change what runs.

Examples
--------
    git show HEAD:scripts/ci_guard.py | python3 -I - 2026-10-19-mc46101-some-question
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

LEDGER = "ledger/forecasts.jsonl"


def _git(repo: Path, *args: str) -> str:
    # .git is not tracked, so a session could plant hooks or an fsmonitor command
    # there; neither may run from here.
    return subprocess.run(
        ["git", "-c", "core.fsmonitor=false", "-c", "core.hooksPath=/dev/null", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def changed_paths(repo: Path) -> list[tuple[str, str]]:
    """``(status, path)`` for every change against ``HEAD``, untracked files included.

    Ignored files (``.venv``, ``uv.lock``, caches) are not listed: the workflow
    rebuilds the virtualenv after this guard instead.
    """
    raw = _git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    out = []
    for entry in raw.split("\0"):
        if len(entry) > 3:
            out.append((entry[:2], entry[3:]))
    return out


def allowed_ledger_line(line: str, slug: str) -> bool:
    """True for a record the session may add: a forecast for its own question."""
    try:
        rec = json.loads(line)
    except json.JSONDecodeError:
        return False
    return isinstance(rec, dict) and rec.get("event") == "forecast" and rec.get(
        "slug"
    ) == slug


def repair_ledger(repo: Path, slug: str) -> list[str]:
    """Keep the committed ledger as a prefix plus only this slug's new forecasts."""
    path = repo / LEDGER
    try:
        committed = _git(repo, "show", f"HEAD:{LEDGER}").splitlines()
    except subprocess.CalledProcessError:
        committed = []
    current = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    prefix_kept = current[: len(committed)] == committed
    tail = current[len(committed) :] if prefix_kept else current
    if not prefix_kept:
        # Lines the session removed or rewrote: rebuild from HEAD, then keep any
        # line that is new and legitimate wherever it sits.
        tail = [line for line in current if line not in set(committed)]
    kept = [line for line in tail if line.strip() and allowed_ledger_line(line, slug)]
    dropped = len([line for line in tail if line.strip()]) - len(kept)
    if prefix_kept and not dropped:
        return []
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"{line}\n" for line in committed + kept), encoding="utf-8")
    notes = []
    if not prefix_kept:
        notes.append("ledger: restored committed lines the session had changed")
    if dropped:
        notes.append(f"ledger: dropped {dropped} line(s) that were not {slug} forecasts")
    return notes


def guard(slug: str, repo: Path) -> list[str]:
    """Restore everything the session may not change; returns what was undone."""
    if not slug or "/" in slug or slug.startswith("."):
        raise ValueError(f"bad slug {slug!r}")
    own = f"questions/{slug}/"
    actions: list[str] = []
    for status, path in changed_paths(repo):
        if path.startswith(own) or path == LEDGER:
            continue
        if status == "??":
            (repo / path).unlink(missing_ok=True)
            actions.append(f"deleted untracked {path}")
        else:
            _git(repo, "checkout", "HEAD", "--", path)
            actions.append(f"restored {path}")
    actions += repair_ledger(repo, slug)
    return actions


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: ci_guard.py <slug>")
    repo = Path(_git(Path.cwd(), "rev-parse", "--show-toplevel").strip())
    actions = guard(sys.argv[1], repo)
    for line in actions:
        print(f"::warning::guard {line} (changed by the forecaster session)")
    print(f"guard: {len(actions)} change(s) undone outside questions/{sys.argv[1]}/")


if __name__ == "__main__":
    main()
