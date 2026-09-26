"""Unit tests for ``scripts/submit_metaculus.py`` -- no network.

The payload builders are pure functions of (ledger record, post JSON, spec), so
they are tested against synthetic posts shaped like the real API answers.
"""

from __future__ import annotations

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


def _record(qtype: str, median: float, iqr=(0.0, 0.0), version: int = 1) -> dict:
    return {"type": qtype, "median": median, "iqr": list(iqr), "version": version}


# ------------------------------------------------------------------ binary
def test_binary_submits_the_ledger_median_clipped_to_metaculus_bounds():
    p = sm.build_payload("s", _record("binary", 0.23), _post("binary"), None)
    assert p.values == {"probability_yes": 0.23}
    p = sm.build_payload("s", _record("binary", 0.0), _post("binary"), None)
    assert p.values["probability_yes"] == sm.P_MIN


# ------------------------------------------------------------ multiple choice
MC_POST = _post("multiple_choice", options=["Likud", "Yashar", "Other"])


def test_multiple_choice_requires_a_spec():
    with pytest.raises(sm.SubmitError, match="full option vector"):
        sm.build_payload("s", _record("multiple_choice", 0.61), MC_POST, None)


def test_multiple_choice_rejects_labels_that_do_not_match_metaculus():
    spec = {"version": 1, "probabilities": {"Likud": 0.39, "Yesh": 0.61}}
    with pytest.raises(sm.SubmitError, match="match Metaculus exactly"):
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
    with pytest.raises(sm.SubmitError, match="ledger median"):
        sm.build_payload("s", rec, _post("numeric", scaling=NUMERIC_SCALING), spec)


def test_log_scaled_grid_matches_metaculus_unscaling():
    scaling = {
        "range_min": 1.0,
        "range_max": 100.0,
        "zero_point": 0.0,
        "inbound_outcome_count": 2,
    }
    assert sm._grid(scaling) == pytest.approx([1.0, 10.0, 100.0])


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
    assert sm.unchanged(p, post)
    p = sm.build_payload("s", _record("binary", 0.25), post, None)
    assert not sm.unchanged(p, post)


def test_group_posts_are_refused_rather_than_guessed():
    with pytest.raises(sm.SubmitError, match="group-of-questions"):
        sm.build_payload(
            "s", _record("numeric", 1.0), {"id": 1, "question": None}, None
        )


# ------------------------------------------------------------ operator-only
def test_no_other_workflow_invokes_the_submit_script():
    """Submitting is operator-invoked only: no workflow may reference the script.

    Allowed: the script itself, its own skill, its tests and the indexes that
    document it.
    """
    allowed = {
        "scripts/submit_metaculus.py",
        "tests/test_submit_metaculus.py",
        ".claude/skills/metaculus-submit/SKILL.md",
        "SKILLS.md",
        "AGENTS.md",
    }
    offenders = []
    for path in [
        *REPO.glob(".claude/**/*.md"),
        *REPO.glob("docs/*.md"),
        *REPO.glob("scripts/*.py"),
        *REPO.glob("*.md"),
    ]:
        rel = path.relative_to(REPO).as_posix()
        if rel in allowed:
            continue
        if re.search(
            r"submit_metaculus|metaculus-submit", path.read_text(encoding="utf-8")
        ):
            offenders.append(rel)
    assert not offenders, (
        f"only the operator invokes submission; referenced in {offenders}"
    )
