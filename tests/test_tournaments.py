"""Schema of ``tournaments/registry.yaml`` and the behaviour of its writer.

The registry is small but load-bearing: the sweep gate decides what to spend a
run's budget on by reading it, before any model is invoked. A wrong ``priority``
or a stale ``active`` flag does not raise anything — it quietly forecasts the
wrong tournament, or none — so the invariants live here.
"""

from __future__ import annotations

import datetime as dt
import subprocess
import sys

import pytest
import tournament_registry as tr
import yaml
from conftest import (
    REGISTRY,
    REGISTRY_ENTRY_KEYS,
    REPO,
    SCRIPTS,
    TOURNAMENT_MODES,
    as_date,
    registry_entries,
)

ENTRIES = registry_entries()
IDS = [slug for slug, _ in ENTRIES]


# ------------------------------------------------------------------ the file
def test_registry_exists_and_parses():
    assert REGISTRY.is_file(), (
        f"{REGISTRY} is missing - the sweep gate has nothing to iterate"
    )
    doc = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    assert isinstance(doc, dict) and isinstance(doc.get("tournaments"), list), (
        "registry.yaml must be a mapping with a `tournaments` list"
    )


def test_slugs_are_unique():
    """``get()`` returns the first match, so a duplicate silently shadows."""
    slugs = [s for s, _ in ENTRIES]
    dupes = sorted({s for s in slugs if slugs.count(s) > 1})
    assert not dupes, f"duplicate tournament slugs: {dupes}"


@pytest.mark.parametrize("slug,entry", ENTRIES, ids=IDS)
def test_entry_keys_are_exactly_the_schema(slug, entry):
    assert set(entry) == REGISTRY_ENTRY_KEYS, (
        f"{slug}: missing={sorted(REGISTRY_ENTRY_KEYS - set(entry))} "
        f"extra={sorted(set(entry) - REGISTRY_ENTRY_KEYS)}"
    )


@pytest.mark.parametrize("slug,entry", ENTRIES, ids=IDS)
def test_identity_fields(slug, entry):
    assert tr.SLUG_RE.match(slug), f"{slug} is not a lowercase kebab-case slug"
    url = entry.get("url")
    assert isinstance(url, str) and url.startswith("https://"), (
        f"{slug}: url {url!r} is not an absolute https URL"
    )
    assert tr.slug_from_url(url) == slug, (
        f"{slug}: url points at tournament {tr.slug_from_url(url)!r}"
    )
    assert isinstance(entry.get("name"), str) and entry["name"].strip(), (
        f"{slug}: name is empty"
    )
    added = as_date(entry.get("added"))
    assert added is not None, f"{slug}: added {entry.get('added')!r} is not a date"
    assert added <= dt.date.today(), f"{slug}: added {added} is in the future"


@pytest.mark.parametrize("slug,entry", ENTRIES, ids=IDS)
def test_policy_fields(slug, entry):
    """``mode``, ``scored``, ``active`` and ``priority`` are the spending policy."""
    assert entry.get("mode") in TOURNAMENT_MODES, (
        f"{slug}: mode {entry.get('mode')!r} not in {sorted(TOURNAMENT_MODES)}"
    )
    for key in ("active", "scored"):
        assert isinstance(entry.get(key), bool), (
            f"{slug}: {key} must be a bool, got {entry.get(key)!r}"
        )
    priority = entry.get("priority")
    assert isinstance(priority, int) and not isinstance(priority, bool), (
        f"{slug}: priority must be an int, got {priority!r}"
    )
    assert priority >= 1, f"{slug}: priority is 1-based, got {priority}"



def test_a_scored_tournament_outranks_an_unscored_one():
    """Priority is the whole point of the field: ranking-affecting work goes first.

    Not a style rule - when the per-run budget cannot cover every open question,
    this ordering decides which ones are never forecast at all.
    """
    scored = [e.get("priority") for _, e in ENTRIES if e.get("scored")]
    unscored = [e.get("priority") for _, e in ENTRIES if not e.get("scored")]
    if not scored or not unscored:
        pytest.skip("registry does not hold both kinds")
    assert max(scored) < min(unscored), (
        f"a smoke-test tournament outranks a scored one: scored={scored} "
        f"unscored={unscored}"
    )


# -------------------------------------------------------------- the module API
def test_active_tournaments_is_sorted_and_filtered():
    active = tr.active_tournaments()
    assert all(e["active"] for e in active)
    keys = [(e["priority"], e["slug"]) for e in active]
    assert keys == sorted(keys), f"active_tournaments is not in sweep order: {keys}"


def test_get_raises_for_an_unknown_slug():
    with pytest.raises(tr.RegistryError):
        tr.get("definitely-not-a-tournament")


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://www.metaculus.com/tournament/minibench/", "minibench"),
        ("https://www.metaculus.com/tournament/bot-testing-area/", "bot-testing-area"),
        ("https://www.metaculus.com/project/aibq4/", "aibq4"),
        ("https://www.metaculus.com/questions/45501/", None),
        ("minibench", None),
    ],
)
def test_slug_from_url(url, expected):
    assert tr.slug_from_url(url) == expected


def _isolate(tmp_path, monkeypatch):
    """Point the module at a throwaway registry file."""
    path = tmp_path / "registry.yaml"
    monkeypatch.setattr(tr, "REGISTRY", path)
    return path


def test_add_then_read_back_round_trips(tmp_path, monkeypatch):
    _isolate(tmp_path, monkeypatch)
    entry = tr.add(
        "https://www.metaculus.com/tournament/minibench/", name="MiniBench", priority=1
    )
    assert entry["slug"] == "minibench" and entry["scored"] is True
    assert tr.get("minibench")["url"].endswith("/minibench/")
    assert set(tr.load_registry()[0]) == REGISTRY_ENTRY_KEYS


def test_add_derives_a_url_from_a_bare_slug(tmp_path, monkeypatch):
    _isolate(tmp_path, monkeypatch)
    entry = tr.add("bot-testing-area")
    assert entry["url"] == "https://www.metaculus.com/tournament/bot-testing-area/"
    assert entry["name"] == "Bot Testing Area"


@pytest.mark.parametrize(
    "bad", ["Not A Slug", "https://example.org/nothing-here/", "", "under_score"]
)
def test_add_rejects_an_unusable_slug(tmp_path, monkeypatch, bad):
    _isolate(tmp_path, monkeypatch)
    with pytest.raises(tr.RegistryError):
        tr.add(bad)


def test_add_refuses_a_duplicate(tmp_path, monkeypatch):
    _isolate(tmp_path, monkeypatch)
    tr.add("minibench")
    with pytest.raises(tr.RegistryError):
        tr.add("minibench")


def test_save_orders_entries_by_priority(tmp_path, monkeypatch):
    _isolate(tmp_path, monkeypatch)
    tr.add("bot-testing-area", priority=3)
    tr.add("minibench", priority=1)
    assert [e["slug"] for e in tr.load_registry()] == ["minibench", "bot-testing-area"]


def test_update_rejects_an_unknown_field(tmp_path, monkeypatch):
    _isolate(tmp_path, monkeypatch)
    tr.add("minibench")
    with pytest.raises(tr.RegistryError):
        tr.update("minibench", tournament_mode="one_shot")



def test_writing_preserves_the_header_comments(tmp_path, monkeypatch):
    """The comments are the only documentation at the point of use."""
    path = _isolate(tmp_path, monkeypatch)
    path.write_text("# keep me\n# and me\ntournaments: []\n", encoding="utf-8")
    tr.add("minibench")
    assert path.read_text(encoding="utf-8").startswith("# keep me\n# and me\n")


def test_load_registry_on_a_missing_file_is_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(tr, "REGISTRY", tmp_path / "nope.yaml")
    assert tr.load_registry() == []


# ---------------------------------------------------------------- the real CLI
@pytest.mark.parametrize(
    "argv",
    [["list"], ["list", "--active"], ["list", "--json"], ["get", "minibench"]],
    ids=lambda a: " ".join(a),
)
def test_cli_runs_clean_against_the_real_registry(argv):
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "tournament_registry.py"), *argv],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, f"{' '.join(argv)} failed:\n{proc.stderr}"
    assert "Traceback" not in proc.stderr
