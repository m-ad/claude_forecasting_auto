"""Invariants of ``ledger/forecasts.jsonl``.

The ledger is append-only JSON Lines and is the only machine-readable record of
what was forecast when. ``scripts/calibration.py`` reads it with ``json.loads``
per line and assumes, without checking, that every line parses, that timestamps
run forward, that versions per slug are 1..N with no gaps, and that a slug has at
most one resolution. These tests make those assumptions explicit.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
from collections import Counter, defaultdict

import pytest
from conftest import (
    EVENTS,
    LEDGER,
    MODES,
    QUESTION_TYPES,
    REPO,
    SOURCES,
    SRC_ABBREV,
    forecast_records,
    ids_for,
    is_number,
    is_probability,
    ledger_lines,
    ledger_records,
    question_dirs,
    resolution_records,
)

RECORDS = ledger_records()
FORECASTS = forecast_records()
RESOLUTIONS = resolution_records()
LINES = ledger_lines()

FORECAST_KEYS = {
    "ts",
    "event",
    "slug",
    "version",
    "source",
    "post_id",
    "type",
    "median",
    "iqr",
    "community",
    "thesis",
    "mode",
}
RESOLUTION_KEYS = {"ts", "event", "slug", "type", "outcome", "resolution_source"}


# ------------------------------------------------------------- file structure
def test_ledger_file_exists():
    assert LEDGER.is_file(), f"{LEDGER} is missing - the scoreable record is the repo"


def test_ledger_ends_with_a_newline():
    """Without it the next ``_append`` glues two records onto one line."""
    text = LEDGER.read_text(encoding="utf-8")
    if not text:
        pytest.skip("empty ledger")
    assert text.endswith("\n"), "ledger must end with a newline"


def test_ledger_has_no_carriage_returns():
    """CRLF survives ``splitlines`` but breaks byte-level append tooling."""
    assert b"\r" not in LEDGER.read_bytes(), "ledger must use LF line endings"


@pytest.mark.parametrize("lineno,raw", LINES, ids=ids_for(LINES))
def test_every_line_is_a_json_object(lineno, raw):
    assert raw.strip(), f"line {lineno} is blank - the ledger has no blank lines"
    rec = json.loads(raw)
    assert isinstance(rec, dict), f"line {lineno} is not a JSON object"


@pytest.mark.parametrize("lineno,raw", LINES, ids=ids_for(LINES))
def test_each_record_is_compact_single_line_json(lineno, raw):
    """``log_forecast._append`` writes ``json.dumps(rec, ensure_ascii=False)``."""
    if not raw.strip():
        pytest.skip("blank line reported elsewhere")
    rec = json.loads(raw)
    assert json.dumps(rec, ensure_ascii=False) == raw, (
        f"line {lineno} is not the canonical compact encoding of its record"
    )


# ----------------------------------------------------------------- timestamps
@pytest.mark.parametrize("lineno,rec", RECORDS, ids=ids_for(RECORDS))
def test_timestamp_is_timezone_aware_utc_iso8601(lineno, rec):
    ts = rec.get("ts")
    assert isinstance(ts, str) and ts, f"line {lineno}: missing ts"
    parsed = dt.datetime.fromisoformat(ts)
    assert parsed.tzinfo is not None, f"line {lineno}: ts {ts!r} has no timezone"
    assert parsed.utcoffset() == dt.timedelta(0), f"line {lineno}: ts {ts!r} is not UTC"
    assert parsed.microsecond == 0, (
        f"line {lineno}: ts {ts!r} should be written with timespec='seconds'"
    )


def test_timestamps_are_non_decreasing_in_file_order():
    """The headline assumption: file order == chronological order.

    Append-only writing guarantees it; a hand-edit, a bad ledger merge, or a
    machine with a wrong clock breaks it, and every downstream "latest version"
    read then silently returns the wrong record.
    """
    stamps = [
        (n, dt.datetime.fromisoformat(r["ts"]))
        for n, r in RECORDS
        if isinstance(r.get("ts"), str)
    ]
    offenders = [
        (stamps[i - 1][0], stamps[i][0])
        for i in range(1, len(stamps))
        if stamps[i][1] < stamps[i - 1][1]
    ]
    assert not offenders, f"ledger timestamps go backwards at line pairs {offenders}"


def test_no_timestamp_is_in_the_future():
    now = dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=5)  # clock slack
    future = [
        n
        for n, r in RECORDS
        if isinstance(r.get("ts"), str) and dt.datetime.fromisoformat(r["ts"]) > now
    ]
    assert not future, f"lines {future} carry a future timestamp"


# --------------------------------------------------------------- record shape
@pytest.mark.parametrize("lineno,rec", RECORDS, ids=ids_for(RECORDS))
def test_event_is_a_known_kind(lineno, rec):
    assert rec.get("event") in EVENTS, (
        f"line {lineno}: unknown event {rec.get('event')!r}, expected {sorted(EVENTS)}"
    )


@pytest.mark.parametrize("lineno,rec", RECORDS, ids=ids_for(RECORDS))
def test_slug_points_at_an_existing_question_folder(lineno, rec):
    slug = rec.get("slug")
    assert isinstance(slug, str) and slug, f"line {lineno}: missing slug"
    known = {d.name for d in question_dirs()}
    assert slug in known, (
        f"line {lineno}: slug {slug!r} has no questions/<slug>/meta.yaml - "
        "calibration.py would score a question nobody can audit"
    )


@pytest.mark.parametrize("lineno,rec", RECORDS, ids=ids_for(RECORDS))
def test_type_is_known(lineno, rec):
    assert rec.get("type") in QUESTION_TYPES, (
        f"line {lineno}: unknown question type {rec.get('type')!r}"
    )


@pytest.mark.parametrize("lineno,rec", FORECASTS, ids=ids_for(FORECASTS))
def test_forecast_record_has_exactly_the_expected_keys(lineno, rec):
    assert set(rec) == FORECAST_KEYS, (
        f"line {lineno}: key mismatch, missing={sorted(FORECAST_KEYS - set(rec))} "
        f"extra={sorted(set(rec) - FORECAST_KEYS)}"
    )


@pytest.mark.parametrize("lineno,rec", RESOLUTIONS, ids=ids_for(RESOLUTIONS))
def test_resolution_record_has_exactly_the_expected_keys(lineno, rec):
    assert set(rec) == RESOLUTION_KEYS, (
        f"line {lineno}: key mismatch, missing={sorted(RESOLUTION_KEYS - set(rec))} "
        f"extra={sorted(set(rec) - RESOLUTION_KEYS)}"
    )


@pytest.mark.parametrize("lineno,rec", FORECASTS, ids=ids_for(FORECASTS))
def test_forecast_source_and_post_id_agree_with_the_slug(lineno, rec):
    src, pid, slug = rec.get("source"), rec.get("post_id"), rec.get("slug", "")
    assert src in SOURCES, f"line {lineno}: unknown source {src!r}"
    assert pid is None or (isinstance(pid, int) and pid > 0), (
        f"line {lineno}: post_id must be a positive int or null, got {pid!r}"
    )
    m = re.match(r"^\d{4}-\d{2}-\d{2}-([a-z]{1,2})(\d*)-", slug)
    assert m, f"line {lineno}: slug {slug!r} does not carry a <src><id> fragment"
    assert m.group(1) == SRC_ABBREV[src], (
        f"line {lineno}: slug says {m.group(1)!r} but source is {src!r}"
    )
    if m.group(2):
        assert pid == int(m.group(2)), (
            f"line {lineno}: slug post id {m.group(2)} != record post_id {pid}"
        )


@pytest.mark.parametrize("lineno,rec", FORECASTS, ids=ids_for(FORECASTS))
def test_forecast_mode_is_known_and_matches_version(lineno, rec):
    mode, version = rec.get("mode"), rec.get("version")
    assert mode in MODES, f"line {lineno}: unknown mode {mode!r}"
    if version == 1:
        assert mode == "initial", (
            f"line {lineno}: v1 must be mode 'initial', got {mode!r}"
        )
    else:
        assert mode != "initial", (
            f"line {lineno}: v{version} must be 'update' or 'reanalysis', not 'initial'"
        )


@pytest.mark.parametrize("lineno,rec", FORECASTS, ids=ids_for(FORECASTS))
def test_forecast_thesis_is_a_real_sentence(lineno, rec):
    thesis = rec.get("thesis")
    assert isinstance(thesis, str), f"line {lineno}: thesis must be a string"
    assert len(thesis.strip()) >= 40, (
        f"line {lineno}: thesis is {len(thesis.strip())} chars - the ledger thesis is "
        "the only human-readable summary a scorer sees"
    )


# ------------------------------------------------------------- numeric sanity
@pytest.mark.parametrize("lineno,rec", FORECASTS, ids=ids_for(FORECASTS))
def test_median_sits_inside_the_iqr(lineno, rec):
    med, iqr = rec.get("median"), rec.get("iqr")
    assert is_number(med), f"line {lineno}: median must be numeric, got {med!r}"
    assert isinstance(iqr, list) and len(iqr) == 2, (
        f"line {lineno}: iqr must be a 2-element list, got {iqr!r}"
    )
    lo, hi = iqr
    assert is_number(lo) and is_number(hi), f"line {lineno}: iqr bounds must be numeric"
    assert lo <= med <= hi, f"line {lineno}: median {med} outside IQR [{lo}, {hi}]"
    assert lo < hi, (
        f"line {lineno}: degenerate IQR [{lo}, {hi}] claims zero uncertainty"
    )


@pytest.mark.parametrize("lineno,rec", FORECASTS, ids=ids_for(FORECASTS))
def test_binary_forecasts_are_probabilities_not_percentages(lineno, rec):
    """A 45 that should have been 0.45 scores as a Brier of ~1936. Catch it here."""
    if rec.get("type") != "binary":
        pytest.skip("not a binary question")
    for name, val in [
        ("median", rec.get("median")),
        ("iqr lower", rec["iqr"][0]),
        ("iqr upper", rec["iqr"][1]),
    ]:
        assert is_probability(val), (
            f"line {lineno}: binary {name} {val!r} is not in [0, 1] - "
            "probabilities are stored as fractions, not percent"
        )


@pytest.mark.parametrize("lineno,rec", FORECASTS, ids=ids_for(FORECASTS))
def test_community_snapshot_shape(lineno, rec):
    com = rec.get("community")
    assert isinstance(com, dict), f"line {lineno}: community must be an object"
    assert set(com) == {"cp", "pro", "gold", "n_forecasters"}, (
        f"line {lineno}: community keys {sorted(com)} != cp/pro/gold/n_forecasters"
    )
    for key in ("cp", "pro", "gold"):
        val = com[key]
        if val is None:
            continue
        assert is_number(val), f"line {lineno}: community.{key} must be numeric or null"
        if rec.get("type") == "binary":
            assert is_probability(val), (
                f"line {lineno}: community.{key}={val} is not a probability in [0, 1]"
            )
    n = com["n_forecasters"]
    assert n is None or (isinstance(n, int) and n > 0), (
        f"line {lineno}: n_forecasters must be a positive int or null, got {n!r}"
    )


@pytest.mark.parametrize("lineno,rec", RESOLUTIONS, ids=ids_for(RESOLUTIONS))
def test_resolution_outcome_is_usable_by_the_scorer(lineno, rec):
    outcome = rec.get("outcome")
    assert outcome is not None, (
        f"line {lineno}: a resolution with a null outcome scores nothing"
    )
    if rec.get("type") == "binary":
        assert is_number(outcome) and float(outcome) in (0.0, 1.0), (
            f"line {lineno}: binary outcome must be 1.0 or 0.0, got {outcome!r}"
        )


@pytest.mark.parametrize("lineno,rec", RESOLUTIONS, ids=ids_for(RESOLUTIONS))
def test_resolution_cites_a_source(lineno, rec):
    src = rec.get("resolution_source")
    assert isinstance(src, str) and src.strip(), (
        f"line {lineno}: resolution_source is empty - rule 5, cite everything"
    )


# ----------------------------------------------------------- per-slug ordering
def _by_slug(records):
    out = defaultdict(list)
    for lineno, rec in records:
        out[rec.get("slug")].append((lineno, rec))
    return out


SLUGS = sorted(s for s in _by_slug(FORECASTS) if isinstance(s, str))


@pytest.mark.parametrize("slug", SLUGS)
def test_versions_are_one_to_n_without_gaps_or_duplicates(slug):
    versions = [r.get("version") for _, r in _by_slug(FORECASTS)[slug]]
    assert all(isinstance(v, int) and v > 0 for v in versions), (
        f"{slug}: versions must be positive ints, got {versions}"
    )
    expected = list(range(1, len(versions) + 1))
    assert versions == expected, (
        f"{slug}: versions in file order are {versions}, expected {expected}"
    )


def test_no_duplicate_slug_version_pairs():
    dupes = [
        k
        for k, c in Counter(
            (r.get("slug"), r.get("version")) for _, r in FORECASTS
        ).items()
        if c > 1
    ]
    assert not dupes, f"duplicate (slug, version) records: {dupes}"


@pytest.mark.parametrize("slug", SLUGS)
def test_a_slug_keeps_one_source_type_and_post_id_across_versions(slug):
    recs = [r for _, r in _by_slug(FORECASTS)[slug]]
    for field in ("source", "post_id", "type"):
        values = {r.get(field) for r in recs}
        assert len(values) == 1, f"{slug}: {field} changes across versions: {values}"


def test_at_most_one_resolution_per_slug():
    """``calibration.read_ledger`` keeps the last one, silently dropping earlier ones."""
    dupes = [
        s for s, c in Counter(r.get("slug") for _, r in RESOLUTIONS).items() if c > 1
    ]
    assert not dupes, f"more than one resolution logged for {dupes}"


@pytest.mark.parametrize("lineno,rec", RESOLUTIONS, ids=ids_for(RESOLUTIONS))
def test_resolution_comes_after_every_forecast_for_that_slug(lineno, rec):
    slug = rec.get("slug")
    earlier = [n for n, f in FORECASTS if f.get("slug") == slug and n < lineno]
    later = [n for n, f in FORECASTS if f.get("slug") == slug and n > lineno]
    assert earlier, f"line {lineno}: {slug} resolved with no forecast logged before it"
    assert not later, (
        f"line {lineno}: {slug} has forecast records at lines {later} logged after "
        "its resolution"
    )


# ---------------------------------------------------------------- append-only
@pytest.mark.git
def test_ledger_is_append_only_against_the_last_commit():
    """Rule 8: past forecasts are never edited or deleted, only appended to.

    Compares the working tree against ``HEAD``; a ledger merge conflict resolved
    by dropping a line shows up here.
    """
    try:
        committed = subprocess.run(
            ["git", "show", "HEAD:ledger/forecasts.jsonl"],
            cwd=REPO,
            capture_output=True,
            check=True,
        ).stdout.decode("utf-8")
    except (OSError, subprocess.CalledProcessError) as exc:
        pytest.skip(f"no committed ledger to compare against ({exc})")
    old = committed.splitlines()
    new = LEDGER.read_text(encoding="utf-8").splitlines()
    assert new[: len(old)] == old, (
        "the committed ledger is no longer a prefix of the working copy - "
        "a past record was edited or deleted"
    )
