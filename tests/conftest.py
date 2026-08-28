"""Shared fixtures and loaders for the workbench test suite.

The tests are *data* tests as much as unit tests: they assert that the invariants
the scripts silently rely on actually hold for the real ledger and the real
question folders. Loaders therefore run at collection time so that each ledger
line and each question folder becomes its own parametrised test case with a
readable id.
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
QUESTIONS = REPO / "questions"
LEDGER = REPO / "ledger" / "forecasts.jsonl"
TEMPLATES = REPO / "templates"
SCRIPTS = REPO / "scripts"

# Importing the scripts under test needs their own directory on the path: they
# use flat `from _common import ...` imports, not a package.
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# ---------------------------------------------------------------- vocabularies
# Kept here rather than imported so that a typo in a script's own constant is a
# test failure instead of a tautology.
SOURCES = {"metaculus", "kalshi", "polymarket", "manifold", "other"}
SRC_ABBREV = {
    "metaculus": "mc",
    "kalshi": "ks",
    "polymarket": "pm",
    "manifold": "mf",
    "other": "x",
}
QUESTION_TYPES = {"binary", "numeric", "date", "multiple_choice", "discrete"}
STATUSES = {"open", "closed", "resolved", "dropped"}
MODES = {"initial", "update", "reanalysis"}
DIRECTIONS = {"up", "down", "either"}
EVENTS = {"forecast", "resolution"}

META_KEYS = {
    "slug",
    "title",
    "source",
    "url",
    "post_id",
    "type",
    "unit",
    "tags",
    "dates",
    "status",
    "current",
    "next_review",
    "tripwires",
    "resolution",
}
DATE_KEYS = {"created", "opened", "closes", "resolves"}
CURRENT_KEYS = {"version", "date", "median", "iqr", "community"}
COMMUNITY_KEYS = {"cp", "pro", "gold", "n_forecasters", "as_of"}
RESOLUTION_KEYS = {"outcome", "date", "source"}
TRIPWIRE_KEYS = {"signal", "by", "direction", "magnitude_pp", "fired"}

SLUG_RE = r"^\d{4}-\d{2}-\d{2}-(?:mc|ks|pm|mf|x)\d*-[a-z0-9]+(?:-[a-z0-9]+)*$"


# -------------------------------------------------------------------- loaders
def ledger_lines() -> list[tuple[int, str]]:
    """Return ``(1-based line number, raw text)`` for every line in the ledger."""
    if not LEDGER.exists():
        return []
    text = LEDGER.read_text(encoding="utf-8")
    if not text:
        return []
    return list(
        enumerate(
            text.split("\n")[:-1] if text.endswith("\n") else text.split("\n"), start=1
        )
    )


def ledger_records() -> list[tuple[int, dict[str, Any]]]:
    """Parsed ledger records as ``(line number, record)``, skipping blank lines.

    Malformed lines are skipped here so that a single bad line fails exactly one
    test (``test_every_line_is_a_json_object``) instead of erroring out the whole
    collection.
    """
    out: list[tuple[int, dict[str, Any]]] = []
    for lineno, raw in ledger_lines():
        if not raw.strip():
            continue
        try:
            rec = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(rec, dict):
            out.append((lineno, rec))
    return out


def forecast_records() -> list[tuple[int, dict[str, Any]]]:
    return [(n, r) for n, r in ledger_records() if r.get("event") == "forecast"]


def resolution_records() -> list[tuple[int, dict[str, Any]]]:
    return [(n, r) for n, r in ledger_records() if r.get("event") == "resolution"]


def question_dirs() -> list[Path]:
    """Every scaffolded question folder, sorted (folder names sort as dates)."""
    if not QUESTIONS.exists():
        return []
    return sorted(
        d for d in QUESTIONS.iterdir() if d.is_dir() and (d / "meta.yaml").is_file()
    )


def metas() -> list[tuple[str, dict[str, Any]]]:
    """``(slug, parsed meta.yaml)`` for every question; unparseable ones skipped."""
    out = []
    for d in question_dirs():
        try:
            data = yaml.safe_load((d / "meta.yaml").read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        if isinstance(data, dict):
            out.append((d.name, data))
    return out


def meta_of(slug: str) -> dict[str, Any]:
    return dict(metas()).get(slug, {})


# -------------------------------------------------------------------- helpers
def as_date(value: Any) -> dt.date | None:
    """Coerce a YAML/JSON date-ish value to ``datetime.date``, or ``None``.

    PyYAML turns an unquoted ``2026-08-27`` into a ``date`` and a quoted one into
    a ``str``; both are accepted everywhere in this repo, so every date check
    goes through here.
    """
    if value is None:
        return None
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value.strip()[:10])
        except ValueError:
            return None
    return None


def require_date(value: Any, what: str) -> dt.date:
    """Like ``as_date``, but fail the calling test instead of returning ``None``.

    Comparing two dates is the common case, and ``as_date`` returning an optional
    forces a guard at every call site that a type checker cannot see through.
    """
    parsed = as_date(value)
    if parsed is None:
        pytest.fail(f"{what}: {value!r} is not an ISO YYYY-MM-DD date")
    return parsed


def is_number(value: Any) -> bool:
    """True for ints/floats but not bools (``isinstance(True, int)`` is True)."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def is_probability(value: Any) -> bool:
    return is_number(value) and 0.0 <= float(value) <= 1.0


def ids_for(pairs) -> list[str]:
    return [str(p[0]) for p in pairs]


# ------------------------------------------------------------ pytest plumbing
def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "git: needs a working git checkout")


@pytest.fixture(scope="session")
def repo() -> Path:
    return REPO


@pytest.fixture(scope="session")
def all_metas() -> dict[str, dict[str, Any]]:
    return dict(metas())


@pytest.fixture(scope="session")
def all_records() -> list[dict[str, Any]]:
    return [r for _, r in ledger_records()]
