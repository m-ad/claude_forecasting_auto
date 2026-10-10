"""Unit tests for the helpers in ``scripts/``.

These are the functions the data tests depend on being correct: slug derivation,
date arithmetic, forecast formatting, ledger parsing and the scoring rules. A bug
here corrupts the calibration record silently, because nothing downstream
re-derives the numbers.
"""

from __future__ import annotations

import argparse
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
import status
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


def test_fmt_forecast_date_renders_iso_dates_in_utc():
    """Date questions store Unix timestamps; INDEX.md must show calendar dates."""
    meta = {
        "type": "date",
        "current": {"median": 2069539200.0, "iqr": [2009145600.0, 2143238400.0]},
    }
    assert _common.fmt_forecast(meta) == "2035-08-01 [2033-09-01, 2037-12-01]"
    # Midnight UTC must not slip to the previous day under a local-time conversion.
    assert _common.fmt_date(0) == "1970-01-01"
    # Community values carry seconds; the date is truncated, not rounded.
    assert _common.fmt_value(2011139602.0, "date") == "2033-09-24"
    assert _common.fmt_value(0.25, "binary") == "25.0%"
    assert _common.fmt_value(87.8, "numeric") == "87.8"


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


# ------------------------------------------------------------------- triage
def test_status_skips_dropped_questions_like_resolved_ones():
    assert status.urgency({"status": "dropped", "current": {"version": 2}})[0] < 0


def test_status_resolution_column_falls_back_to_the_close_date():
    """The table must show the date the urgency score was computed from."""
    assert status.resolves_on({"dates": {"closes": "2027-01-01"}}) == "2027-01-01"
    meta = {"dates": {"closes": "2027-01-01", "resolves": "2027-02-01"}}
    assert status.resolves_on(meta) == "2027-02-01"


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


def test_read_ledger_skips_a_malformed_line_instead_of_crashing(tmp_path, monkeypatch):
    """Scoring shares log_forecast's tolerance; test_ledger.py flags the bad line."""
    path = tmp_path / "forecasts.jsonl"
    rec = {"event": "forecast", "slug": "s", "version": 1, "median": 0.5}
    path.write_text("{ not json\n" + json.dumps(rec) + "\n", encoding="utf-8")
    monkeypatch.setattr(calibration, "LEDGER", path)
    forecasts, _ = calibration.read_ledger()
    assert [r["version"] for r in forecasts["s"]] == [1]


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


# ------------------------------------------------ new_question.py: group posts
# The bug: a group-of-questions post (one subquestion per year, say) has no
# top-level ``question`` in its API JSON, so the type came back None and the
# folder was silently scaffolded as the ``--type`` default, "binary".
_GROUP_POST = {
    "title": "What will be the percentage change in funds raised by GiveWell?",
    "scheduled_close_time": "2028-07-01T00:00:00Z",
    "status": "open",
    "nr_forecasters": 5,
    "group_of_questions": {
        "questions": [
            {"id": 45576, "label": "2028", "type": "numeric"},
            {"id": 45575, "label": "2027", "type": "numeric"},
        ]
    },
}


def _fake_skill(monkeypatch, post=None, res=None):
    """Stand in for the metaculus-aggregations module ``fetch_metaculus`` imports."""
    import types

    mod = types.ModuleType("metaculus_aggregations")
    mod.fetch_post_api = lambda _pid: post

    def fetch_aggregations(_pid, methods=None):
        if res is None:
            raise AssertionError("the browser fallback must not run")
        return res

    mod.fetch_aggregations = fetch_aggregations
    monkeypatch.setitem(sys.modules, "metaculus_aggregations", mod)


def test_group_post_via_the_api_takes_its_subquestions_shared_type(monkeypatch):
    import new_question

    _fake_skill(monkeypatch, post=_GROUP_POST)
    got = new_question.fetch_metaculus(45386)
    assert got["type"] == "numeric"
    assert got["closes"] == "2028-07-01"
    assert got["subquestions"] == [
        {"label": "2028", "id": 45576, "type": "numeric"},
        {"label": "2027", "id": 45575, "type": "numeric"},
    ]


def test_mixed_type_group_reports_no_type_rather_than_guessing(monkeypatch):
    import new_question

    post = json.loads(json.dumps(_GROUP_POST))
    post["group_of_questions"]["questions"][0]["type"] = "binary"
    _fake_skill(monkeypatch, post=post)
    assert new_question.fetch_metaculus(45386)["type"] is None


def test_single_question_post_via_the_api_is_unchanged(monkeypatch):
    import new_question

    post = {
        "title": "Will OpenAI file for an IPO during 2026?",
        "scheduled_close_time": "2026-12-31T00:00:00Z",
        "status": "open",
        "nr_forecasters": 40,
        "question": {"type": "binary"},
    }
    _fake_skill(monkeypatch, post=post)
    got = new_question.fetch_metaculus(41141)
    assert (got["type"], got["closes"], got["subquestions"]) == (
        "binary",
        "2026-12-31",
        [],
    )


def test_group_post_via_the_browser_fallback_keeps_its_subquestions(monkeypatch):
    import types

    import new_question

    sub = types.SimpleNamespace(
        label="2027", question_id=45575, question_type="numeric"
    )
    res = types.SimpleNamespace(
        title="T",
        question_type="numeric",
        scheduled_close_time="2028-07-01T00:00:00Z",
        cp_reveal_time=None,
        status="open",
        nr_forecasters=5,
        subquestions=[sub],
    )
    _fake_skill(monkeypatch, post=None, res=res)
    got = new_question.fetch_metaculus(45386)
    assert got["type"] == "numeric"
    assert got["subquestions"] == [{"label": "2027", "id": 45575, "type": "numeric"}]


def test_group_post_is_scaffolded_with_its_real_type(monkeypatch, tmp_path, capsys):
    import new_question

    # main() prints the folder relative to REPO, so both must move to tmp_path.
    monkeypatch.setattr(new_question, "REPO", tmp_path)
    monkeypatch.setattr(new_question, "QUESTIONS", tmp_path / "questions")
    monkeypatch.setattr(
        new_question,
        "fetch_metaculus",
        lambda _pid: {
            "title": _GROUP_POST["title"],
            "type": "numeric",
            "closes": "2028-07-01",
            "subquestions": [
                {"label": "2027", "id": 45575, "type": "numeric"},
                {"label": "2028", "id": 45576, "type": "numeric"},
            ],
        },
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["new_question.py", "--url", "https://www.metaculus.com/questions/45386/x/"],
    )
    new_question.main()
    out, err = capsys.readouterr()
    slug = out.splitlines()[0]
    assert "mc45386" in slug, "stdout must still open with the slug"
    folder = tmp_path / "questions" / slug
    meta = yaml.safe_load((folder / "meta.yaml").read_text(encoding="utf-8"))
    assert meta["type"] == "numeric", "a group must not fall back to --type binary"
    assert meta["dates"]["closes"] == "2028-07-01"
    assert "group of 2 subquestions" in err
    assert "2027: question 45575 (numeric)" in err


# ------------------------------------- new_question.py: pre-open ("upcoming") posts
# A question can be scaffolded in its pre-prediction phase, before open_time. The
# post-level status then reads "approved" and only question.status says "upcoming";
# the bot-key API also hides the question text until it opens (post 45255,
# verified 2026-10-09), which the agent must not read as "criteria unpublished".
_UPCOMING_POST = {
    "title": "How many executions will be carried out in the US in 2026?",
    "status": "approved",
    "open_time": "2026-10-12T17:00:00Z",
    "scheduled_close_time": "2026-12-02T23:59:00Z",
    "scheduled_resolve_time": "2027-01-01T17:09:00Z",
    "nr_forecasters": 1,
    "question": {
        "type": "multiple_choice",
        "status": "upcoming",
        "open_time": "2026-10-12T17:00:00Z",
        "cp_reveal_time": "2026-10-15T17:00:00Z",
        "resolution_criteria": None,
    },
}


def test_api_post_carries_open_and_resolve_dates_and_the_question_status(monkeypatch):
    import new_question

    _fake_skill(monkeypatch, post=_UPCOMING_POST)
    got = new_question.fetch_metaculus(45255)
    assert (got["opens"], got["closes"], got["resolves"]) == (
        "2026-10-12",
        "2026-12-02",
        "2027-01-01",
    )
    assert got["status"] == "upcoming", "the question status, not the post's 'approved'"
    assert got["cp_reveal"] == "2026-10-15"


def test_upcoming_question_is_scaffolded_with_dates_and_a_warning(
    monkeypatch, tmp_path, capsys
):
    import new_question

    monkeypatch.setattr(new_question, "REPO", tmp_path)
    monkeypatch.setattr(new_question, "QUESTIONS", tmp_path / "questions")
    _fake_skill(monkeypatch, post=_UPCOMING_POST)
    monkeypatch.setattr(
        sys,
        "argv",
        ["new_question.py", "--url", "https://www.metaculus.com/questions/45255/x/"],
    )
    new_question.main()
    out, err = capsys.readouterr()
    folder = tmp_path / "questions" / out.splitlines()[0]
    meta = yaml.safe_load((folder / "meta.yaml").read_text(encoding="utf-8"))
    assert meta["dates"]["opened"] == "2026-10-12"
    assert meta["dates"]["resolves"] == "2027-01-01"
    assert "not open yet" in err and "2026-10-12" in err
    assert "metaculus_aggregations.py" in err, "must point at the browser text path"


# ------------------------------------------------------- full distributions
MC = {"probabilities": {"Likud": 0.381, "Yashar": 0.61, "Other": 0.009}}


@pytest.mark.parametrize(
    "qtype,dist,median,iqr,options,fragment",
    [
        ("binary", {"probabilities": {"a": 1.0, "b": 0.0}}, 0.5, [0.4, 0.6], None,
         "take no distribution"),
        ("multiple_choice", {"percentiles": {"25": 1, "50": 2}}, 0.6, [0.5, 0.7], None,
         "exactly one of"),
        ("multiple_choice", {"probabilities": {"A": 62.0, "B": 38.0}}, 62.0, [50, 70],
         None, "not percent"),
        ("multiple_choice", {"probabilities": {"A": 0.6, "B": 0.3}}, 0.6, [0.5, 0.7],
         None, "sum to"),
        ("multiple_choice", MC, 0.5, [0.4, 0.6], None, "leading option"),
        ("multiple_choice", MC, 0.61, [0.55, 0.67], ["Likud", "Yesh Atid", "Other"],
         "options exactly"),
        ("numeric", {"percentiles": {"25": 1.0, "75": 3.0}}, 2.0, [1.0, 3.0], None,
         "include '50'"),
        ("numeric", {"percentiles": {"25": 1.0, "50": 2.5, "75": 3.0}}, 2.0, [1.0, 3.0],
         None, "differs from the median"),
        ("numeric", {"percentiles": {"10": 5.0, "50": 2.0}}, 2.0, [1.0, 3.0], None,
         "must not decrease"),
        ("discrete", {"pmf": {"3": 0.2, "4": 0.5, "5": 0.3}}, 5.0, [4.0, 5.0], None,
         "not a median"),
    ],
)
def test_distribution_problems_catches_each_kind_of_mismatch(
    qtype, dist, median, iqr, options, fragment
):
    problems = _common.distribution_problems(qtype, dist, median, iqr, options)
    assert any(fragment in p for p in problems), problems


@pytest.mark.parametrize(
    "qtype,dist,median,iqr",
    [
        ("multiple_choice", MC, 0.61, [0.55, 0.67]),
        ("numeric", {"percentiles": {"5": 38, "25": 43.3, "50": 46.5, "75": 49.7}},
         46.5, [43.3, 49.7]),
        ("discrete", {"pmf": {"3": 0.2, "4": 0.5, "5": 0.3}}, 4.0, [3.0, 5.0]),
        ("discrete", {"percentiles": {"25": 3.0, "50": 4.0, "75": 5.0}}, 4.0, [3, 5]),
    ],
)
def test_distribution_problems_accepts_consistent_distributions(qtype, dist, median, iqr):
    options = list(dist.get("probabilities", {})) or None
    assert _common.distribution_problems(qtype, dist, median, iqr, options) == []


def _snapshot(folder, name, post_id, options):
    (folder / "raw").mkdir(parents=True, exist_ok=True)
    (folder / "raw" / name).write_text(
        json.dumps({"post_id": post_id, "options": options}), encoding="utf-8"
    )


def test_cached_options_takes_the_newest_snapshot_of_this_post(tmp_path, monkeypatch):
    monkeypatch.setattr(log_forecast, "QUESTIONS", tmp_path)
    q = tmp_path / "s"
    _snapshot(q, "metaculus-2026-09-01.json", 7, ["A", "B"])
    _snapshot(q, "metaculus-2026-09-20.json", 7, ["A", "B", "C"])
    # A related post cached in the same folder must not be mistaken for this one.
    _snapshot(q, "metaculus-99-2026-09-25.json", 99, ["X", "Y"])
    assert log_forecast.cached_options("s", 7) == ["A", "B", "C"]
    assert log_forecast.cached_options("s", 8) is None
    assert log_forecast.cached_options("s", None) is None


def _add_args(**over) -> argparse.Namespace:
    base = {
        "slug": "s", "median": 0.61, "lower": 0.55, "upper": 0.67, "cp": None,
        "pro": None, "gold": None, "n_forecasters": None, "distribution": None,
        "thesis": "t", "mode": "initial", "next_review": None,
    }
    return argparse.Namespace(**{**base, **over})


@pytest.fixture
def mc_question(tmp_path, monkeypatch):
    """A throwaway multiple-choice question wired into log_forecast."""
    meta = {"type": "multiple_choice", "source": "metaculus", "post_id": 7, "current": {}}
    ledger = tmp_path / "forecasts.jsonl"
    monkeypatch.setattr(log_forecast, "LEDGER", ledger)
    monkeypatch.setattr(log_forecast, "QUESTIONS", tmp_path)
    monkeypatch.setattr(log_forecast, "find_slug", lambda s: s)
    monkeypatch.setattr(log_forecast, "load_meta", lambda s: meta)
    monkeypatch.setattr(log_forecast, "save_meta", lambda s, m: None)
    _snapshot(tmp_path / "s", "metaculus-2026-09-20.json", 7, ["Likud", "Yashar", "Other"])
    return ledger


def _records(ledger) -> list[dict]:
    return [json.loads(x) for x in ledger.read_text(encoding="utf-8").splitlines()]


def test_log_add_refuses_multiple_choice_without_a_distribution(mc_question):
    with pytest.raises(SystemExit, match="need --distribution"):
        log_forecast.cmd_add(_add_args())
    assert not mc_question.exists(), "a refused forecast must not reach the ledger"


def test_log_add_refuses_labels_that_differ_from_the_cached_options(mc_question):
    bad = {"probabilities": {"Likud": 0.381, "Yesh": 0.61, "Other": 0.009}}
    with pytest.raises(SystemExit, match="options exactly"):
        log_forecast.cmd_add(_add_args(distribution=json.dumps(bad)))
    assert not mc_question.exists()


def test_log_add_records_the_distribution_inline_or_from_a_file(mc_question, tmp_path):
    log_forecast.cmd_add(_add_args(distribution=json.dumps(MC)))
    spec = tmp_path / "d.json"
    spec.write_text(json.dumps(MC), encoding="utf-8")
    log_forecast.cmd_add(_add_args(distribution=f"@{spec}", mode="update"))
    recs = _records(mc_question)
    assert [r["distribution"] for r in recs] == [MC, MC]
    assert [r["version"] for r in recs] == [1, 2]


def test_log_add_leaves_the_key_out_when_no_distribution_is_given(tmp_path, monkeypatch):
    """Binary records keep the pre-existing shape exactly."""
    meta = {"type": "binary", "source": "metaculus", "post_id": 7, "current": {}}
    ledger = tmp_path / "forecasts.jsonl"
    monkeypatch.setattr(log_forecast, "LEDGER", ledger)
    monkeypatch.setattr(log_forecast, "find_slug", lambda s: s)
    monkeypatch.setattr(log_forecast, "load_meta", lambda s: meta)
    monkeypatch.setattr(log_forecast, "save_meta", lambda s, m: None)
    log_forecast.cmd_add(_add_args(median=0.2, lower=0.1, upper=0.3))
    assert "distribution" not in _records(ledger)[0]


def test_log_resolve_keeps_a_multiple_choice_label_verbatim(mc_question):
    """An option called "0" must stay "0", not become the number 0.0."""
    ns = argparse.Namespace(slug="s", outcome="Yashar", date=None, source="x")
    log_forecast.cmd_resolve(ns)
    assert _records(mc_question)[-1]["outcome"] == "Yashar"
    with pytest.raises(SystemExit, match="not an option"):
        log_forecast.cmd_resolve(argparse.Namespace(**{**vars(ns), "outcome": "Kadima"}))


@pytest.fixture
def binary_question(tmp_path, monkeypatch):
    """A throwaway question wired into log_forecast; set ``meta["type"]`` to taste."""
    meta = {"type": "binary", "source": "metaculus", "post_id": 7, "current": {}}
    ledger = tmp_path / "forecasts.jsonl"
    monkeypatch.setattr(log_forecast, "LEDGER", ledger)
    monkeypatch.setattr(log_forecast, "find_slug", lambda s: s)
    monkeypatch.setattr(log_forecast, "load_meta", lambda s: meta)
    monkeypatch.setattr(log_forecast, "save_meta", lambda s, m: None)
    return ledger, meta


@pytest.mark.parametrize(
    "median,lower,upper,match",
    [
        (12.0, 8.0, 18.0, "not percent"),  # percent typed for a probability
        (0.5, 0.6, 0.7, "outside the IQR"),
        (0.5, 0.5, 0.5, "degenerate"),
        (float("nan"), 0.1, 0.9, "finite"),
    ],
)
def test_log_add_refuses_a_bad_forecast_before_it_reaches_the_ledger(
    binary_question, median, lower, upper, match
):
    """The ledger is append-only, so a bad line caught afterwards stays forever."""
    ledger, _ = binary_question
    with pytest.raises(SystemExit, match=match):
        log_forecast.cmd_add(_add_args(median=median, lower=lower, upper=upper))
    assert not ledger.exists()


def test_log_add_accepts_native_units_outside_the_unit_interval(binary_question):
    ledger, meta = binary_question
    meta["type"] = "numeric"
    log_forecast.cmd_add(_add_args(median=87.8, lower=80.4, upper=97.0))
    assert _records(ledger)[0]["median"] == 87.8


@pytest.mark.parametrize("raw", ["annulled", "ambiguous", "0.5"])
def test_log_resolve_refuses_a_binary_outcome_that_is_not_yes_or_no(
    binary_question, raw
):
    """An annulled question is dropped, not resolved: calibration.py cannot score it."""
    ledger, _ = binary_question
    ns = argparse.Namespace(slug="s", outcome=raw, date=None, source="x")
    with pytest.raises(SystemExit, match="dropped"):
        log_forecast.cmd_resolve(ns)
    assert not ledger.exists()


def test_log_resolve_stores_a_date_outcome_in_unix_seconds(binary_question):
    """Date IQRs are Unix seconds; an ISO-string outcome could never be scored."""
    ledger, meta = binary_question
    meta["type"] = "date"
    ns = argparse.Namespace(slug="s", outcome="2031-03-31", date=None, source="x")
    log_forecast.cmd_resolve(ns)
    outcome = _records(ledger)[-1]["outcome"]
    assert outcome == dt.datetime(2031, 3, 31, tzinfo=dt.UTC).timestamp()
    with pytest.raises(SystemExit, match="YYYY-MM-DD"):
        log_forecast.cmd_resolve(argparse.Namespace(**{**vars(ns), "outcome": "soon"}))


# ------------------------------------------------------ multiple-choice scoring
def test_mc_brier_and_log_score():
    probs = MC["probabilities"]
    assert calibration.mc_brier(probs, "Yashar") == pytest.approx(
        0.381**2 + 0.39**2 + 0.009**2
    )
    assert calibration.mc_brier({"a": 1.0, "b": 0.0}, "a") == 0.0
    assert calibration.mc_brier({"a": 1.0, "b": 0.0}, "b") == pytest.approx(2.0)
    assert calibration.mc_log_score(probs, "Yashar") == pytest.approx(-math.log(0.61))
    assert math.isfinite(calibration.mc_log_score({"a": 1.0, "b": 0.0}, "b"))


def test_mc_label_recovers_a_legacy_numeric_coding():
    assert calibration.mc_label("1", ["0", "1", "2"]) == "1"
    assert calibration.mc_label(1.0, ["0", "1", "2"]) == "1"
    assert calibration.mc_label("Kadima", ["Likud", "Yashar"]) is None


def test_summarise_mc_skill_is_zero_for_a_uniform_forecaster():
    uniform = {"a": 1 / 3, "b": 1 / 3, "c": 1 / 3}
    stats = calibration.summarise_mc([(uniform, "a"), (uniform, "c")])
    assert stats["skill_vs_uniform"] == pytest.approx(0.0, abs=1e-12)


def test_calibration_scores_multiple_choice_instead_of_crashing(
    tmp_path, monkeypatch, capsys
):
    """Regression: a label outcome used to hit float("Yashar") and kill the run."""
    base = {"source": "metaculus", "post_id": 1, "iqr": [0.55, 0.67], "median": 0.61}
    _write_ledger(
        tmp_path / "l.jsonl",
        [
            {**base, "event": "forecast", "slug": "a", "version": 1,
             "type": "multiple_choice"},
            {**base, "event": "forecast", "slug": "a", "version": 2,
             "type": "multiple_choice", "distribution": MC},
            {"event": "resolution", "slug": "a", "type": "multiple_choice",
             "outcome": "Yashar"},
            {"event": "forecast", "slug": "n", "version": 1, "type": "numeric",
             "median": 5.0, "iqr": [4.0, 6.0]},
            {"event": "resolution", "slug": "n", "type": "numeric",
             "outcome": "above upper bound"},
        ],
    )
    monkeypatch.setattr(calibration, "LEDGER", tmp_path / "l.jsonl")
    monkeypatch.setattr(sys, "argv", ["calibration.py"])
    calibration.main()
    out = capsys.readouterr().out
    assert "== multiple choice ==" in out and "forecasts scored : 1" in out
    assert "multiple choice (no option vector)" in out
    assert "non-numeric outcome" in out


# ------------------------------------------------------------- smoke: the CLIs
CLI_INVOCATIONS = [
    ["status.py"],
    ["status.py", "--all"],
    ["calibration.py"],
    ["calibration.py", "--latest-only"],
    ["log_forecast.py", "--help"],
    ["new_question.py", "--help"],
    ["submit_metaculus.py", "--help"],
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
