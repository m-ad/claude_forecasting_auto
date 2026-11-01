"""Tests for ``scripts/postmortem.py``: PIT, replay, sample selection, the sync report.

Unit tests run on synthetic folders and ledgers; the repo tests check that every CDF
the bot actually submitted is reproduced by a known rule set, which is what makes a
replay of alternative rules meaningful.
"""

from __future__ import annotations

import json
import subprocess
import sys

import postmortem as pm
import pytest
import submit_metaculus as sm
import yaml
from conftest import REPO, SCRIPTS

SCALING = {
    "range_min": 0.0,
    "range_max": 100.0,
    "zero_point": None,
    "open_lower_bound": True,
    "open_upper_bound": True,
    "inbound_outcome_count": 100,
}
PCT = {"5": 40.0, "10": 42.0, "25": 46.0, "50": 50.0, "75": 54.0, "90": 58.0, "95": 60.0}


# ------------------------------------------------------------------ PIT
def test_pit_and_mass_of_a_uniform_cdf_follow_the_outcomes_position():
    xs = [float(i) for i in range(11)]
    cdf = [i / 10 for i in range(11)]
    assert pm.pit(cdf, xs, 2.5) == pytest.approx(0.25)
    assert pm.outcome_mass(cdf, xs, 2.5) == pytest.approx(0.1)
    shifted = [0.01 + 0.98 * c for c in cdf]
    assert pm.outcome_mass(shifted, xs, -3) == pytest.approx(0.01)  # below an open bound
    assert pm.outcome_mass(shifted, xs, 12) == pytest.approx(0.01)  # above it
    assert pm.pit(shifted, xs, 12) == pytest.approx(0.99)


def test_pit_summary_counts_coverage_tails_and_deciles():
    s = pm.pit_summary([0.05, 0.3, 0.5, 0.97, 0.995, 0.8])
    assert s["n"] == 6
    assert s["inside_iqr"] == 2
    assert s["outside_90"] == 2  # 0.97 and 0.995; 0.05 is on the edge, not outside
    assert s["above_p75"] == 3 and s["below_p25"] == 1
    assert s["deciles"] == [1, 0, 0, 1, 0, 1, 0, 0, 1, 2]


# ------------------------------------------------------------------ loading
def _write_question(root, slug, *, qtype="numeric", score=-12.5, pct=PCT, outcome=93.0,
                    cdf=None, ts="2026-10-19T12:00:00+00:00"):
    folder = root / "questions" / slug
    (folder / "raw").mkdir(parents=True)
    meta = {"slug": slug, "type": qtype, "status": "resolved",
            "tournament": {"slug": "minibench", "official_score": score}}
    (folder / "meta.yaml").write_text(yaml.safe_dump(meta), encoding="utf-8")
    (folder / "raw" / "metaculus-question-2026-10-19.json").write_text(
        json.dumps({"question": {"type": qtype, "scaling": SCALING}}), encoding="utf-8"
    )
    knots = sorted((float(k) / 100, v) for k, v in pct.items())
    cdf = cdf or sm.continuous_cdf(knots, SCALING, mix=0.02, smooth=False)
    median = pct["50"]
    lines = [
        {"ts": ts, "event": "forecast", "slug": slug, "version": 1, "type": qtype,
         "median": median, "iqr": [pct["25"], pct["75"]], "distribution": {"percentiles": pct}},
        {"ts": ts, "event": "submission", "slug": slug, "payload": {"continuous_cdf": cdf}},
        {"ts": "2026-10-31T00:00:00+00:00", "event": "resolution", "slug": slug,
         "type": qtype, "outcome": outcome},
    ]
    with (root / "forecasts.jsonl").open("a", encoding="utf-8") as fh:
        for line in lines:
            fh.write(json.dumps(line) + "\n")


def test_load_rows_joins_meta_ledger_and_snapshot(tmp_path):
    _write_question(tmp_path, "2026-10-19-mc1-a")
    (row,) = pm.load_rows(tmp_path / "questions", tmp_path / "forecasts.jsonl")
    assert row.slug == "2026-10-19-mc1-a"
    assert row.qtype == "numeric" and row.peer == -12.5 and row.outcome == 93.0
    assert row.scaling == SCALING
    assert len(row.submitted_cdf) == SCALING["inbound_outcome_count"] + 1
    assert row.date == "2026-10-19"


def test_unresolved_questions_are_not_loaded(tmp_path):
    _write_question(tmp_path, "2026-10-19-mc1-a")
    ledger = tmp_path / "forecasts.jsonl"
    ledger.write_text(
        "\n".join(ln for ln in ledger.read_text().splitlines() if "resolution" not in ln)
    )
    assert pm.load_rows(tmp_path / "questions", ledger) == []


# ------------------------------------------------------------------ replay
def test_replay_is_measured_against_what_was_submitted(tmp_path):
    _write_question(tmp_path, "2026-10-19-mc1-a", outcome=93.0)  # far right tail
    rows = pm.load_rows(tmp_path / "questions", tmp_path / "forecasts.jsonl")
    deltas = pm.replay(rows)
    (legacy,) = deltas["legacy: linear, floor 2 %"]
    assert legacy[1] == pytest.approx(0.0, abs=1e-9)  # the rules it was submitted with
    (heavy,) = deltas["current, floor 10 %"]
    assert heavy[1] > 0.5  # a heavier floor pays when the outcome is far out


def test_replay_summary_reports_the_spread_and_the_outlier_dependence():
    s = pm.replay_summary([("a", 1.2), ("b", -0.1), ("c", 0.05), ("d", 0.4), ("e", -0.02)])
    assert s["total"] == pytest.approx(1.53)
    assert s["median"] == pytest.approx(0.05)
    assert s["worse"] == 2
    assert s["worst"] == pytest.approx(-0.1)
    assert s["without_top3"] == pytest.approx(-0.12)


def test_pmf_forecasts_are_left_out_of_the_replay(tmp_path):
    _write_question(tmp_path, "2026-10-19-mc1-a")
    rows = pm.load_rows(tmp_path / "questions", tmp_path / "forecasts.jsonl")
    rows[0].forecast["distribution"] = {"pmf": {"1": 1.0}}
    assert all(not v for v in pm.replay(rows).values())


# ------------------------------------------------------------------ sample
def _fake_rows():
    types = ["numeric", "binary", "discrete"]
    return [
        pm.Row(slug=f"s{i:02d}", qtype=types[i % 3], peer=float(i - 10), outcome=1.0,
               forecast={"ts": "2026-10-19T00:00:00+00:00"}, submitted_cdf=None, scaling=None)
        for i in range(30)
    ]


def test_sample_takes_the_worst_and_type_matched_positive_controls():
    worst, controls = pm.sample(_fake_rows(), worst=4, controls=4, seed=7)
    assert [r.slug for r in worst] == ["s00", "s01", "s02", "s03"]
    assert all(r.peer > 0 for r in controls)
    assert sorted(r.qtype for r in controls) == sorted(r.qtype for r in worst)
    assert not {r.slug for r in worst} & {r.slug for r in controls}
    again = pm.sample(_fake_rows(), worst=4, controls=4, seed=7)[1]
    assert [r.slug for r in again] == [r.slug for r in controls]


def test_sample_fills_from_other_types_when_a_type_runs_out():
    rows = [r for r in _fake_rows() if not (r.qtype == "discrete" and r.peer > 0)]
    _worst, controls = pm.sample(rows, worst=3, controls=3, seed=1)
    assert len(controls) == 3 and all(r.peer > 0 for r in controls)


# ------------------------------------------------------------------ report
def test_report_renders_with_nothing_resolved():
    text = pm.report([])
    assert text.startswith("### Post-mortem")
    assert "no resolved question" in text


def test_report_shows_scores_pit_and_replay(tmp_path):
    _write_question(tmp_path, "2026-10-19-mc1-a", outcome=93.0)
    _write_question(tmp_path, "2026-10-19-mc2-b", outcome=50.0, score=8.0)
    rows = pm.load_rows(tmp_path / "questions", tmp_path / "forecasts.jsonl")
    text = pm.report(rows)
    for needle in ("| numeric | 2 |", "PIT", "inside the IQR", "current, floor 10 %"):
        assert needle in text


# ------------------------------------------------------------------ real repo
REPO_ROWS = pm.load_rows()


@pytest.mark.parametrize(
    "row",
    [r for r in REPO_ROWS if r.submitted_cdf and pm.knots_of(r.forecast)],
    ids=lambda r: r.slug,
)
def test_every_submitted_cdf_is_reproduced_by_a_known_rule_set(row):
    knots = pm.knots_of(row.forecast)
    gaps = {
        name: max(abs(a - b) for a, b in zip(
            sm.continuous_cdf(knots, row.scaling, **rules), row.submitted_cdf, strict=True))
        for name, rules in pm.RULE_SETS.items()
    }
    assert min(gaps.values()) < 1e-9, f"{row.slug}: no rule set reproduces it: {gaps}"


def test_cli_report_runs_over_the_repo():
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "postmortem.py"), "report"],
        capture_output=True, text=True, encoding="utf-8", check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "### Post-mortem" in proc.stdout


def test_daily_sync_writes_the_postmortem_report_to_its_summary():
    workflow = yaml.safe_load(
        (REPO / ".github" / "workflows" / "tournament-sync.yml").read_text("utf-8")
    )
    runs = [s.get("run", "") for s in workflow["jobs"]["sync"]["steps"]]
    assert any("scripts/postmortem.py report" in r and "GITHUB_STEP_SUMMARY" in r for r in runs)
