"""Unit tests for ``scripts/changed_forecasts.py`` -- the CI picker for what to submit."""

from __future__ import annotations

import json

import changed_forecasts as cf


def _line(slug: str, event: str = "forecast", source: str = "metaculus", v: int = 1) -> str:
    return json.dumps({"event": event, "slug": slug, "source": source, "version": v})


def test_only_lines_added_since_base_count():
    base = [_line("a"), _line("b")]
    head = [*base, _line("c"), _line("a", v=2)]
    assert cf.added_metaculus_slugs(base, head) == ["c", "a"]


def test_resolutions_and_other_sources_are_not_submitted():
    head = [
        _line("resolved", event="resolution"),
        _line("kalshi-q", source="kalshi"),
        _line("free-text", source="other"),
        _line("mc"),
    ]
    assert cf.added_metaculus_slugs([], head) == ["mc"]


def test_slugs_are_unique_and_keep_ledger_order():
    head = [_line("x"), _line("y"), _line("x", v=2)]
    assert cf.added_metaculus_slugs([], head) == ["x", "y"]


def test_no_change_means_no_slugs():
    lines = [_line("a"), ""]
    assert cf.added_metaculus_slugs(lines, lines) == []


def test_current_ledger_parses():
    """The real ledger at HEAD must be readable by the picker (it runs in CI)."""
    assert cf.added_metaculus_slugs([], cf.ledger_at("HEAD"))
