"""Unit tests for ``scripts/submit_metaculus.py`` -- no network.

The payload builders are pure functions of (ledger record, post JSON, spec), so
they are tested against synthetic posts shaped like the real API answers.
"""

from __future__ import annotations

import json
import re

import pytest
import submit_metaculus as sm
from conftest import REPO

NUMERIC_SCALING = {
    "range_min": 35,
    "range_max": 55,
    "zero_point": None,
    "open_lower_bound": True,
    "open_upper_bound": True,
    "inbound_outcome_count": 200,
}
DISCRETE_SCALING = {
    "range_min": -0.5,
    "range_max": 10.5,
    "zero_point": None,
    "open_lower_bound": False,
    "open_upper_bound": False,
    "inbound_outcome_count": 11,
}


def _post(qtype: str, **question) -> dict:
    return {"id": 1, "status": "open", "question": {"id": 2, "type": qtype, **question}}


def _record(
    qtype: str, median: float, iqr=(0.0, 0.0), version: int = 1, distribution=None
) -> dict:
    rec = {"type": qtype, "median": median, "iqr": list(iqr), "version": version}
    if distribution is not None:
        rec["distribution"] = distribution
    return rec


# ------------------------------------------------------------------ binary
def test_binary_submits_the_ledger_median_clipped_to_metaculus_bounds():
    p = sm.build_payload("s", _record("binary", 0.23), _post("binary"), None)
    assert p.values == {"probability_yes": 0.23}
    p = sm.build_payload("s", _record("binary", 0.0), _post("binary"), None)
    assert p.values["probability_yes"] == sm.P_MIN


# ------------------------------------------------------------ multiple choice
MC_POST = _post("multiple_choice", options=["Likud", "Yashar", "Other"])


MC_VECTOR = {"Likud": 0.381, "Yashar": 0.61, "Other": 0.009}


def test_multiple_choice_submits_the_ledgers_option_vector():
    rec = _record("multiple_choice", 0.61, distribution={"probabilities": MC_VECTOR})
    p = sm.build_payload("s", rec, MC_POST, None)
    assert p.values["probability_yes_per_category"] == pytest.approx(MC_VECTOR)


def test_legacy_multiple_choice_without_a_distribution_needs_a_spec():
    with pytest.raises(sm.SubmitError, match="predates the ledger's distribution"):
        sm.build_payload("s", _record("multiple_choice", 0.61), MC_POST, None)


def test_spec_for_a_record_that_has_a_distribution_is_refused():
    """The ledger is the record; a spec may only fill gaps, never override it."""
    rec = _record("multiple_choice", 0.61, distribution={"probabilities": MC_VECTOR})
    spec = {"version": 1, "probabilities": MC_VECTOR}
    with pytest.raises(sm.SubmitError, match="already records"):
        sm.build_payload("s", rec, MC_POST, spec)


def test_multiple_choice_rejects_labels_that_do_not_match_metaculus():
    spec = {"version": 1, "probabilities": {"Likud": 0.39, "Yesh": 0.61}}
    with pytest.raises(sm.SubmitError, match="options exactly"):
        sm.build_payload("s", _record("multiple_choice", 0.61), MC_POST, spec)


def test_multiple_choice_floors_tiny_options_and_renormalises():
    spec = {
        "version": 1,
        "probabilities": {"Likud": 0.39, "Yashar": 0.61, "Other": 0.0},
    }
    p = sm.build_payload("s", _record("multiple_choice", 0.61), MC_POST, spec)
    probs = p.values["probability_yes_per_category"]
    assert min(probs.values()) >= sm.P_MIN * 0.99
    assert sum(probs.values()) == pytest.approx(1.0)


def test_spec_from_an_older_version_is_refused():
    spec = {
        "version": 1,
        "probabilities": {"Likud": 0.39, "Yashar": 0.61, "Other": 0.0},
    }
    with pytest.raises(sm.SubmitError, match="re-extract"):
        sm.build_payload(
            "s", _record("multiple_choice", 0.61, version=2), MC_POST, spec
        )


def test_spec_whose_leader_disagrees_with_the_ledger_is_refused():
    spec = {
        "version": 1,
        "probabilities": {"Likud": 0.5, "Yashar": 0.45, "Other": 0.05},
    }
    with pytest.raises(sm.SubmitError, match="leading option"):
        sm.build_payload("s", _record("multiple_choice", 0.61), MC_POST, spec)


# ------------------------------------------------------------------ numeric
def test_numeric_cdf_from_quartiles_keeps_the_quartiles_and_obeys_the_rules():
    rec = _record("numeric", 46.5, (43.3, 49.7))
    p = sm.build_payload("s", rec, _post("numeric", scaling=NUMERIC_SCALING), None)
    cdf = p.values["continuous_cdf"]
    sm.validate_cdf(cdf, NUMERIC_SCALING)  # would raise
    assert p.note  # the quartile-only fallback is flagged
    for q, want in ((0.25, 43.3), (0.5, 46.5), (0.75, 49.7)):
        assert sm.quantile(cdf, NUMERIC_SCALING, q) == pytest.approx(want, abs=0.1)


def test_numeric_forecast_mostly_above_an_open_upper_bound_is_representable():
    scaling = {**NUMERIC_SCALING, "range_min": 150_000, "range_max": 250_000}
    spec = {
        "version": 1,
        "percentiles": {"5": 186e3, "25": 236e3, "50": 272e3, "95": 461e3},
    }
    rec = _record("numeric", 272e3, (236e3, 320e3))
    p = sm.build_payload("s", rec, _post("numeric", scaling=scaling), spec)
    cdf = p.values["continuous_cdf"]
    sm.validate_cdf(cdf, scaling)
    assert 1 - cdf[-1] == pytest.approx(0.65, abs=0.02)  # P(above the range)


def test_numeric_spec_whose_median_disagrees_with_the_ledger_is_refused():
    spec = {"version": 1, "percentiles": {"25": 40, "50": 45, "75": 50}}
    rec = _record("numeric", 46.5, (43.3, 49.7))
    with pytest.raises(sm.SubmitError, match="differs from the median"):
        sm.build_payload("s", rec, _post("numeric", scaling=NUMERIC_SCALING), spec)


def test_numeric_submits_the_ledgers_percentiles_without_the_quartile_note():
    pct = {"5": 38.0, "25": 43.3, "50": 46.5, "75": 49.7, "95": 54.0}
    rec = _record("numeric", 46.5, (43.3, 49.7), distribution={"percentiles": pct})
    p = sm.build_payload("s", rec, _post("numeric", scaling=NUMERIC_SCALING), None)
    assert not p.note
    cdf = p.values["continuous_cdf"]
    assert sm.quantile(cdf, NUMERIC_SCALING, 0.05) == pytest.approx(38.0, abs=0.3)


def test_tied_percentiles_become_a_point_mass_spread_upward_under_the_max_step():
    # A record close the answer cannot fall below puts p5..p50 on one value.
    scaling = {**NUMERIC_SCALING, "range_min": 236, "range_max": 275}
    pct = {"5": 239.24, "25": 239.24, "50": 239.24, "75": 262.0, "95": 309.0}
    rec = _record("numeric", 239.24, (239.24, 262.0), distribution={"percentiles": pct})
    p = sm.build_payload("s", rec, _post("numeric", scaling=scaling), None)
    cdf = p.values["continuous_cdf"]
    sm.validate_cdf(cdf, scaling)  # would raise on a step above 0.2
    xs = sm._grid(scaling)
    below = max(c for x, c in zip(xs, cdf) if x < 239.24)
    assert below == pytest.approx(0.05, abs=0.01)
    # the 45% jump spreads over the bins just above the floor, none below it
    assert 239.24 <= sm.quantile(cdf, scaling, 0.5) <= 240.5
    # the uniform mix shifts in-range quantiles by ~1 here, ties or not
    assert sm.quantile(cdf, scaling, 0.75) == pytest.approx(262.0, abs=1.0)


def test_cdf_step_above_metaculus_maximum_is_refused():
    n = NUMERIC_SCALING["inbound_outcome_count"]
    cdf = [0.001 + 0.5 * i / n for i in range(n + 1)]
    cdf[n // 2 + 1 :] = [c + 0.25 for c in cdf[n // 2 + 1 :]]
    with pytest.raises(sm.SubmitError, match="above"):
        sm.validate_cdf(cdf, NUMERIC_SCALING)


def test_max_step_scales_with_the_outcome_count_like_metaculus():
    # 0.2 * 200 / 11 > 1, so a discrete PMF with a 0.6 outcome is valid.
    pmf = {str(k): 0.04 for k in range(11)}
    pmf["5"] = 0.6
    rec = _record("discrete", 5, (5, 5), distribution={"pmf": pmf})
    p = sm.build_payload("s", rec, _post("discrete", scaling=DISCRETE_SCALING), None)
    sm.validate_cdf(p.values["continuous_cdf"], DISCRETE_SCALING)


def test_percentiles_on_a_single_value_are_refused():
    pct = {"25": 40, "50": 40, "75": 40}
    rec = _record("numeric", 40, (40, 40), distribution={"percentiles": pct})
    with pytest.raises(sm.SubmitError, match="distinct"):
        sm.build_payload("s", rec, _post("numeric", scaling=NUMERIC_SCALING), None)


def test_log_scaled_grid_matches_metaculus_unscaling():
    scaling = {
        "range_min": 1.0,
        "range_max": 100.0,
        "zero_point": 0.0,
        "inbound_outcome_count": 2,
    }
    assert sm._grid(scaling) == pytest.approx([1.0, 10.0, 100.0])


# ------------------------------------------------------------------ date
# Metaculus serves a date question's ``continuous_range`` as ISO timestamps,
# while ``range_min``/``range_max`` are Unix seconds (seen on post 4845).
DATE_SCALING = {
    "range_min": 1594771200.0,  # 2020-07-15
    "range_max": 1893283200.0,  # 2029-12-30
    "zero_point": None,
    "open_lower_bound": False,
    "open_upper_bound": True,
    "inbound_outcome_count": 2,
    "continuous_range": [
        "2020-07-15T00:00:00Z",
        "2025-04-07T12:00:00Z",
        "2029-12-30T00:00:00Z",
    ],
}


def test_date_grid_parses_iso_timestamps_to_unix_seconds():
    assert sm._grid(DATE_SCALING) == pytest.approx(
        [1594771200.0, 1744027200.0, 1893283200.0]
    )


def test_date_question_submits_the_ledgers_percentiles():
    pct = {"10": 1640908800, "25": 1767139200, "50": 1830211200, "75": 1924905600}
    rec = _record(
        "date", 1830211200, (1767139200, 1924905600), distribution={"percentiles": pct}
    )
    p = sm.build_payload("s", rec, _post("date", scaling=DATE_SCALING), None)
    cdf = p.values["continuous_cdf"]
    sm.validate_cdf(cdf, DATE_SCALING)
    assert len(cdf) == 3
    assert 0.6 < cdf[-1] < 0.75  # mass above the open upper bound survives


# ------------------------------------------------------------------ discrete
def test_discrete_pmf_gives_every_outcome_the_minimum_step():
    pmf = {"3": 0.2, "4": 0.5, "5": 0.3}
    rec = _record("discrete", 4.0, (3.0, 5.0))
    spec = {"version": 1, "pmf": pmf}
    p = sm.build_payload("s", rec, _post("discrete", scaling=DISCRETE_SCALING), spec)
    cdf = p.values["continuous_cdf"]
    sm.validate_cdf(cdf, DISCRETE_SCALING)
    assert cdf[0] == 0.0 and cdf[-1] == 1.0 and len(cdf) == 12
    assert cdf[5] - cdf[4] == pytest.approx(0.5, abs=0.01)  # P(4)


def test_discrete_pmf_with_an_impossible_outcome_is_refused():
    with pytest.raises(sm.SubmitError, match="not outcomes"):
        sm.discrete_cdf({"11": 1.0}, DISCRETE_SCALING)


# ------------------------------------------------------------- idempotence
def test_unchanged_compares_against_the_bots_live_forecast():
    post = _post(
        "binary",
        my_forecasts={"latest": {"forecast_values": [0.77, 0.23], "end_time": None}},
    )
    p = sm.build_payload("s", _record("binary", 0.23), post, None)
    assert sm.unchanged(p, post["question"])
    p = sm.build_payload("s", _record("binary", 0.25), post, None)
    assert not sm.unchanged(p, post["question"])


# ------------------------------------------------------------ group posts
# A group-of-questions post (one binary per year on post 21095, say) has no
# top-level ``question``: each sub-question carries its own id, type, status and
# the bot's ``my_forecasts``. The slug's meta.yaml URL pins one with
# ``?sub-question=<id>``, the form Metaculus itself links to.
GROUP_URL = (
    "https://www.metaculus.com/questions/21095/will-the-following-years-be-the-"
    "warmest-year-on-record-according-to-nasa/?sub-question=21098"
)


def _group_post(overrides: dict[int, dict] | None = None) -> dict:
    subs = [
        {"id": 21097, "type": "binary", "label": "2025", "status": "resolved"},
        {"id": 21098, "type": "binary", "label": "2026", "status": "open"},
        {"id": 45424, "type": "binary", "label": "2027", "status": "open"},
    ]
    for q in subs:
        q.update((overrides or {}).get(q["id"], {}))
    return {
        "id": 21095,
        "status": "open",
        "question": None,
        "group_of_questions": {"questions": subs},
    }


def test_subquestion_id_is_read_from_the_metaculus_url():
    assert sm.subquestion_id(GROUP_URL) == 21098
    assert sm.subquestion_id("https://www.metaculus.com/questions/21095/x/") is None
    assert sm.subquestion_id(None) is None


def test_group_post_submits_to_the_pinned_subquestion():
    p = sm.build_payload("s", _record("binary", 0.62), _group_post(), None, 21098)
    assert (p.post_id, p.question_id) == (21095, 21098)
    assert p.body()[0]["question"] == 21098
    assert p.values == {"probability_yes": 0.62}


def test_group_post_without_a_pinned_subquestion_is_refused_not_guessed():
    with pytest.raises(sm.SubmitError, match=r"sub-question=.*2026=21098"):
        sm.build_payload("s", _record("binary", 0.62), _group_post(), None)


def test_subquestion_missing_from_the_group_is_refused():
    with pytest.raises(sm.SubmitError, match="not in post 21095"):
        sm.build_payload("s", _record("binary", 0.62), _group_post(), None, 99)


def test_subquestion_type_is_checked_against_the_ledger():
    post = _group_post({21098: {"type": "numeric"}})
    with pytest.raises(sm.SubmitError, match="Metaculus says 'numeric'"):
        sm.build_payload("s", _record("binary", 0.62), post, None, 21098)


def test_a_closed_subquestion_reads_closed_while_its_post_is_open():
    """Post 15240 stayed open after its September 2026 sub-question closed."""
    post = _group_post({21098: {"status": "closed"}})
    assert sm.select_question(post, 21098)["status"] == "closed"
    assert post["status"] == "open"


def test_unchanged_reads_the_subquestions_own_live_forecast():
    live = {"latest": {"forecast_values": [0.38, 0.62], "end_time": None}}
    post = _group_post({21098: {"my_forecasts": live}})
    q = sm.select_question(post, 21098)
    p = sm.build_payload("s", _record("binary", 0.62), post, None, 21098)
    assert sm.unchanged(p, q)
    other = sm.build_payload("s", _record("binary", 0.62), post, None, 45424)
    assert not sm.unchanged(other, sm.select_question(post, 45424))


def test_non_group_post_without_a_question_is_refused():
    with pytest.raises(sm.SubmitError, match="no question"):
        sm.build_payload(
            "s", _record("numeric", 1.0), {"id": 1, "question": None}, None
        )


# ------------------------------------------------------------- CI-only
def test_no_model_facing_instruction_invokes_the_submit_script():
    """The model never submits: deterministic code does, after the model exits.

    The sweep workflow runs the submit step after the forecaster's session ends,
    with the Metaculus token kept out of that session entirely. The files that
    instruct the model (skills, commands, agents) must therefore never tell it to
    run the script, and the CI permission set must deny it outright.
    """
    offenders = [
        path.relative_to(REPO).as_posix()
        for path in REPO.glob(".claude/**/*.md")
        if re.search(r"submit_metaculus|metaculus-submit", path.read_text("utf-8"))
    ]
    assert not offenders, f"model-facing files reference submission: {offenders}"
    ci = REPO / ".claude" / "settings.ci.json"
    if ci.exists():
        deny = json.loads(ci.read_text("utf-8"))["permissions"]["deny"]
        assert any("submit_metaculus" in rule for rule in deny), (
            ".claude/settings.ci.json must deny the submit script to the model"
        )
