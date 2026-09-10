"""Unit tests for the helpers in ``scripts/``.

These are the functions the data tests depend on being correct: slug derivation,
date arithmetic, forecast formatting, ledger parsing and the scoring rules. A bug
here corrupts the calibration record silently, because nothing downstream
re-derives the numbers.
"""

from __future__ import annotations

import datetime as dt
import json
import math
import os
import subprocess
import sys
from typing import Any

import _common
import calibration
import log_forecast
import pytest
import yaml
from conftest import QUESTION_TYPES, REPO, SCRIPTS, SOURCES, SRC_ABBREV, metas


# -------------------------------------------------------------------- slugify
@pytest.mark.parametrize(
    "title,expected",
    [
        (
            "Will there be a bilateral ceasefire in the Russo-Ukrainian conflict before 2027?",
            "bilateral-ceasefire-russo-ukrainian-conflict-before-2027",
        ),
        ("Will OpenAI file for an IPO during 2026?", "openai-file-ipo-during-2026"),
        (
            "The a an of in on at",
            "the-a-an-of-in-on-at",
        ),  # all-stopword titles keep the words
    ],
)
def test_slugify_known_titles(title, expected):
    assert _common.slugify(title) == expected


@pytest.mark.parametrize(
    "title",
    [
        "Will the U.S. C.P.I. exceed 3.5% (year-over-year) by Q1'27?",
        "  ¿Será Ω > 1?  ",
        "A" * 300,
        "2026",
    ],
)
def test_slugify_output_is_always_filesystem_safe(title):
    slug = _common.slugify(title)
    assert slug == slug.lower()
    assert len(slug) <= 60
    assert not slug.startswith("-") and not slug.endswith("-")
    assert "--" not in slug
    assert all(c.isascii() and (c.isalnum() or c == "-") for c in slug), slug


def test_slugify_caps_the_word_count():
    assert (
        _common.slugify(
            "alpha beta gamma delta epsilon zeta eta theta iota", max_words=3
        )
        == "alpha-beta-gamma"
    )


def test_slugify_is_idempotent():
    once = _common.slugify("Will OpenAI file for an IPO during 2026?")
    assert _common.slugify(once) == once


# ----------------------------------------------------------------- days_until
def test_days_until_counts_whole_days_and_goes_negative_after():
    today = dt.date.today()
    assert _common.days_until(today.isoformat()) == 0
    assert _common.days_until((today + dt.timedelta(days=5)).isoformat()) == 5
    assert _common.days_until((today - dt.timedelta(days=3)).isoformat()) == -3


def test_days_until_tolerates_timestamps_and_junk():
    today = dt.date.today().isoformat()
    assert _common.days_until(f"{today}T12:00:00+00:00") == 0
    assert _common.days_until(None) is None
    assert _common.days_until("") is None
    assert _common.days_until("not-a-date") is None
    assert _common.days_until("2026-13-45") is None


# --------------------------------------------------------------- fmt_forecast
def test_fmt_forecast_binary_renders_percentages():
    meta = {"type": "binary", "current": {"median": 0.045, "iqr": [0.02, 0.08]}}
    assert _common.fmt_forecast(meta) == "4.5% [2.0%, 8.0%]"


def test_fmt_forecast_handles_a_missing_forecast_and_a_missing_band():
    assert _common.fmt_forecast({"type": "binary", "current": {}}) == "—"
    assert _common.fmt_forecast({"type": "binary"}) == "—"
    assert (
        _common.fmt_forecast(
            {"type": "binary", "current": {"median": 0.5, "iqr": [None, None]}}
        )
        == "50.0%"
    )


def test_fmt_forecast_numeric_keeps_native_units():
    meta = {"type": "numeric", "current": {"median": 87.8, "iqr": [80.4, 97.0]}}
    assert _common.fmt_forecast(meta) == "87.8 [80.4, 97]"


def test_fmt_forecast_numeric_does_not_go_scientific_on_large_units():
    """A barrels- or dollars-denominated question must stay readable in INDEX.md."""
    meta = {
        "type": "numeric",
        "current": {"median": 282300000.0, "iqr": [280600000.0, 283800000.0]},
    }
    assert _common.fmt_forecast(meta) == "282,300,000 [280,600,000, 283,800,000]"
    assert _common.fmt_number(999999) == "999999"
    assert _common.fmt_number(-1500000.4) == "-1,500,000"


# ------------------------------------------------------------------ find_slug
def test_find_slug_resolves_exact_slug_post_id_and_url():
    known = metas()
    if not known:
        pytest.skip("no questions scaffolded")
    slug, meta = known[0]
    assert _common.find_slug(slug) == slug
    assert _common.find_slug(slug + "/") == slug
    if meta.get("post_id"):
        assert _common.find_slug(str(meta["post_id"])) == slug
        assert (
            _common.find_slug(
                f"https://www.metaculus.com/questions/{meta['post_id']}/whatever/"
            )
            == slug
        )


def test_find_slug_returns_none_when_nothing_or_too_much_matches():
    assert _common.find_slug("definitely-not-a-question-xyzzy") is None
    if len(metas()) > 1:
        # every folder name starts with "20", so a bare "20" is ambiguous
        assert _common.find_slug("20") is None


# ----------------------------------------------------------- outcome coercion
@pytest.mark.parametrize(
    "raw,expected",
    [
        ("yes", 1.0),
        ("YES", 1.0),
        ("true", 1.0),
        ("1", 1.0),
        ("no", 0.0),
        ("No", 0.0),
        ("false", 0.0),
        ("0", 0.0),
        ("87.4", 87.4),
        ("-3", -3.0),
        ("2027-01-15", "2027-01-15"),
        ("Option B", "Option B"),
    ],
)
def test_outcome_value_coercion(raw, expected):
    assert log_forecast._outcome_value(raw) == expected


# ------------------------------------------------------- ledger-derived version
def _write_ledger(path, records) -> None:
    path.write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records),
        encoding="utf-8",
    )


def test_count_forecasts_is_zero_without_a_ledger(monkeypatch, tmp_path):
    monkeypatch.setattr(log_forecast, "LEDGER", tmp_path / "nope.jsonl")
    assert log_forecast._count_forecasts("some-slug") == 0


def test_count_forecasts_counts_only_this_slugs_forecast_records(
    monkeypatch, tmp_path
):
    """Resolutions and other slugs must not shift a slug's next version number."""
    path = tmp_path / "forecasts.jsonl"
    _write_ledger(
        path,
        [
            {"event": "forecast", "slug": "a", "version": 1},
            {"event": "forecast", "slug": "b", "version": 1},
            {"event": "forecast", "slug": "a", "version": 2},
            {"event": "resolution", "slug": "a", "outcome": 1.0},
            {"slug": "a", "version": 3},  # legacy record with no event key
        ],
    )
    monkeypatch.setattr(log_forecast, "LEDGER", path)
    assert log_forecast._count_forecasts("a") == 3
    assert log_forecast._count_forecasts("b") == 1
    assert log_forecast._count_forecasts("c") == 0


def test_count_forecasts_survives_a_malformed_line(monkeypatch, tmp_path):
    """One unparseable line must not block appending to an append-only ledger."""
    path = tmp_path / "forecasts.jsonl"
    path.write_text(
        json.dumps({"event": "forecast", "slug": "a", "version": 1})
        + "\n{ this is not json\n\n"
        + json.dumps({"event": "forecast", "slug": "a", "version": 2})
        + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(log_forecast, "LEDGER", path)
    assert log_forecast._count_forecasts("a") == 2


def test_count_forecasts_ignores_a_wrong_version_number(monkeypatch, tmp_path):
    """Counting, not max()+1: a stray version must not open a permanent gap."""
    path = tmp_path / "forecasts.jsonl"
    _write_ledger(
        path,
        [
            {"event": "forecast", "slug": "a", "version": 1},
            {"event": "forecast", "slug": "a", "version": 7},
        ],
    )
    monkeypatch.setattr(log_forecast, "LEDGER", path)
    assert log_forecast._count_forecasts("a") + 1 == 3


# ------------------------------------------------------------- scoring rules
def test_brier_is_squared_error_and_bounded():
    assert calibration.brier(1.0, 1.0) == 0.0
    assert calibration.brier(0.0, 1.0) == 1.0
    assert calibration.brier(0.5, 1.0) == pytest.approx(0.25)
    assert calibration.brier(0.3, 0.0) == pytest.approx(0.09)


def test_log_score_stays_finite_at_the_extremes():
    """EPS clamping is what keeps a 0%-that-happened from poisoning the mean."""
    assert math.isfinite(calibration.log_score(0.0, 1.0))
    assert math.isfinite(calibration.log_score(1.0, 0.0))
    assert calibration.log_score(0.5, 1.0) == pytest.approx(math.log(2))
    assert calibration.log_score(1.0, 1.0) == pytest.approx(0.0, abs=1e-5)


def test_log_score_punishes_confident_mistakes_harder_than_brier():
    conf_wrong = [calibration.log_score(0.99, 0.0), calibration.brier(0.99, 0.0)]
    assert conf_wrong[0] > conf_wrong[1]


def _summarise(pairs: list[tuple[float, float]], label: str) -> dict[str, Any]:
    """``summarise`` is optional-returning; every caller here expects a result."""
    stats = calibration.summarise(pairs, label)
    assert stats is not None, f"summarise returned None for a {len(pairs)}-pair sample"
    return stats


def test_summarise_computes_bias_and_skill():
    pairs = [(0.9, 1.0), (0.8, 1.0), (0.1, 0.0), (0.2, 0.0)]
    stats = _summarise(pairs, "test")
    assert stats["n"] == 4
    assert stats["base_rate"] == pytest.approx(0.5)
    assert stats["mean_forecast"] == pytest.approx(0.5)
    assert stats["bias_pp"] == pytest.approx(0.0)
    assert stats["brier"] == pytest.approx(0.025)
    assert stats["skill_vs_base_rate"] > 0.8  # far better than always saying 50%


def test_summarise_returns_none_on_an_empty_sample():
    assert calibration.summarise([], "empty") is None


def test_skill_is_nan_when_every_outcome_is_identical():
    """With no variance in the outcomes there is no reference to have skill over."""
    stats = _summarise([(0.9, 1.0), (0.8, 1.0)], "all-yes")
    assert math.isnan(stats["skill_vs_base_rate"])


def test_buckets_bin_by_forecast_and_keep_p_equals_one_in_the_last_bin():
    out = calibration.buckets([(0.05, 0.0), (0.07, 1.0), (0.95, 1.0), (1.0, 1.0)])
    names = [b[0] for b in out]
    assert names[0] == "0%–10%" and names[-1] == "90%–100%"
    assert out[0][1] == 2 and out[-1][1] == 2  # p=1.0 does not overflow into a 11th bin
    assert out[0][3] == pytest.approx(0.5)  # one of the two low forecasts happened


def test_buckets_cover_the_whole_unit_interval():
    pairs = [(i / 20, float(i % 2)) for i in range(21)]
    assert sum(b[1] for b in calibration.buckets(pairs)) == len(pairs)


# --------------------------------------------------------------- ledger reads
def test_read_ledger_groups_by_slug_and_keeps_resolutions_apart():
    forecasts, resolutions = calibration.read_ledger()
    for slug, recs in forecasts.items():
        assert all(r.get("event") != "resolution" for r in recs), (
            f"{slug}: a resolution leaked into the forecast list"
        )
    for slug, rec in resolutions.items():
        assert rec.get("event") == "resolution"
        assert slug in forecasts, f"{slug}: resolved without any forecast to score"


def test_read_ledger_tolerates_trailing_blank_lines(tmp_path, monkeypatch):
    path = tmp_path / "forecasts.jsonl"
    rec = {
        "ts": "2026-01-01T00:00:00+00:00",
        "event": "forecast",
        "slug": "s",
        "version": 1,
        "median": 0.5,
    }
    path.write_text(json.dumps(rec) + "\n\n", encoding="utf-8")
    monkeypatch.setattr(calibration, "LEDGER", path)
    forecasts, resolutions = calibration.read_ledger()
    assert list(forecasts) == ["s"] and not resolutions


def test_read_ledger_on_a_missing_file_returns_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(calibration, "LEDGER", tmp_path / "nope.jsonl")
    assert calibration.read_ledger() == ({}, {})


# ------------------------------------------------------------ meta round-trip
def test_save_meta_then_load_meta_preserves_the_document(tmp_path, monkeypatch):
    monkeypatch.setattr(_common, "QUESTIONS", tmp_path)
    (tmp_path / "demo").mkdir()
    doc = {
        "slug": "demo",
        "title": "Ünïcode — em dash?",
        "tags": ["a", "b"],
        "current": {"version": 2, "iqr": [0.1, 0.2]},
        "next_review": "2026-09-01",
    }
    _common.save_meta("demo", doc)
    assert _common.load_meta("demo") == doc


def test_save_meta_writes_utf8_without_escaping():
    """``allow_unicode=True``: an escaped title is unreadable in a diff."""
    dumped = yaml.safe_dump({"title": "Ünïcode"}, sort_keys=False, allow_unicode=True)
    assert "Ünïcode" in dumped


# ---------------------------------------------------- vocabularies stay in sync
def test_src_abbrev_matches_the_tests_expectation():
    assert _common.SRC_ABBREV == SRC_ABBREV
    assert set(_common.SRC_ABBREV) == SOURCES


def test_new_question_offers_exactly_the_known_sources_and_types():
    """``--source``/``--type`` choices are the only gate on what enters a slug."""
    help_text = subprocess.run(
        [sys.executable, str(SCRIPTS / "new_question.py"), "--help"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    for source in SOURCES:
        assert source in help_text, (
            f"new_question.py --source cannot produce {source!r}"
        )
    for qtype in QUESTION_TYPES:
        assert qtype in help_text, f"new_question.py --type cannot produce {qtype!r}"


def test_abbreviations_are_unique():
    assert len(set(_common.SRC_ABBREV.values())) == len(_common.SRC_ABBREV)


# ------------------------------------------------------------- smoke: the CLIs
CLI_INVOCATIONS = [
    ["status.py"],
    ["status.py", "--all"],
    ["calibration.py"],
    ["calibration.py", "--latest-only"],
    ["log_forecast.py", "--help"],
    ["new_question.py", "--help"],
]


def _run_cli(argv, encoding="utf-8"):
    env = {**os.environ, "PYTHONIOENCODING": encoding}
    return subprocess.run(
        [sys.executable, str(SCRIPTS / argv[0]), *argv[1:]],
        cwd=REPO,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        check=False,  # the exit code is what the caller asserts on
    )


@pytest.mark.parametrize(
    "argv", CLI_INVOCATIONS, ids=[" ".join(a) for a in CLI_INVOCATIONS]
)
def test_cli_runs_clean_against_the_real_repo(argv):
    """Catches import errors and any crash on the current data shape."""
    proc = _run_cli(argv)
    assert proc.returncode == 0, f"{' '.join(argv)} failed:\n{proc.stderr}"
    assert "Traceback" not in proc.stderr


@pytest.mark.parametrize(
    "argv", CLI_INVOCATIONS, ids=[" ".join(a) for a in CLI_INVOCATIONS]
)
def test_cli_output_survives_a_non_utf8_console(argv):
    """The scripts print ``→``, ``·`` and ``—``; a cp1252 stdout must not kill them.

    This is the default on a Windows console and whenever output is piped there,
    so a script that only works under UTF-8 is a script the operator cannot run.
    """
    proc = _run_cli(argv, encoding="cp1252")
    assert "UnicodeEncodeError" not in proc.stderr, (
        f"{' '.join(argv)} crashed on a cp1252 stdout:\n{proc.stderr[-500:]}"
    )
    assert proc.returncode == 0, f"{' '.join(argv)} failed:\n{proc.stderr}"


def test_status_find_resolves_a_real_slug():
    known = metas()
    if not known:
        pytest.skip("no questions scaffolded")
    slug = known[0][0]
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "status.py"), "--find", slug],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    )
    assert proc.stdout.strip() == slug


def test_all_questions_sees_every_folder():
    assert {s for s, _ in _common.all_questions()} == {s for s, _ in metas()}
