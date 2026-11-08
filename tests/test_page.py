"""The results page: its scores, its costs, its leaderboard lookup, its HTML.

Offline: the leaderboard tests run against fakes of ``metaculus_api``. The data
tests at the bottom hold the real repository to what the page relies on.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys

import allowance as al
import build_page as bp
import metaculus_api as mapi
import page_usage as pu
import pytest
from calibration import mc_brier
from conftest import REPO, SCRIPTS

NOW = dt.datetime(2026, 11, 1, 8, 0, tzinfo=dt.UTC)


# =================================================================== scoring
def test_ranked_brier_is_zero_for_a_step_at_the_outcome():
    assert bp.ranked_brier([0.0, 0.0, 1.0, 1.0], [0, 1, 2, 3], 1.5) == 0.0


def test_ranked_brier_averages_the_threshold_briers():
    # Thresholds "X <= 0..3" for outcome 1 resolve no, yes, yes, yes.
    got = bp.ranked_brier([0.25, 0.5, 0.75, 1.0], [0, 1, 2, 3], 1.0)
    assert got == pytest.approx((0.25**2 + 0.5**2 + 0.25**2 + 0.0) / 4)


@pytest.mark.parametrize(
    ("outcome", "want"),
    [
        ("above_upper_bound", (0.1**2 + 0.9**2) / 2),
        ("below_lower_bound", (0.9**2 + 0.1**2) / 2),
    ],
)
def test_ranked_brier_handles_out_of_bounds_outcomes(outcome, want):
    assert bp.ranked_brier([0.1, 0.9], [0, 1], outcome) == pytest.approx(want)


@pytest.mark.parametrize(
    ("cdf", "xs", "outcome"),
    [([0.5], [0, 1], 0.0), ([], [], 1.0), ([0.2, 0.8], [0, 1], "annulled")],
)
def test_ranked_brier_refuses_what_it_cannot_score(cdf, xs, outcome):
    assert bp.ranked_brier(cdf, xs, outcome) is None


def test_binary_brier_uses_the_submitted_probability():
    meta = {"current": {"median": 0.9}}
    got = bp.score_brier("binary", 0.0, {"probability_yes": 0.57}, meta, None)
    assert got == (pytest.approx(0.57**2), "binary")


def test_binary_brier_falls_back_to_the_logged_median():
    got = bp.score_brier("binary", 1.0, None, {"current": {"median": 0.8}}, None)
    assert got == (pytest.approx(0.04), "binary")


def test_multiple_choice_brier_scores_the_resolved_label():
    probs = {"A": 0.2, "B": 0.5, "C": 0.3}
    payload = {"probability_yes_per_category": probs}
    assert bp.score_brier("multiple_choice", "B", payload, {}, None) == (
        pytest.approx(mc_brier(probs, "B")),
        "multi-class",
    )
    # The legacy float coding of a numeric label still finds its option.
    numeric = {"0": 0.4, "2": 0.6}
    assert (
        bp.score_brier("multiple_choice", 2.0, None, {}, None, numeric)[1]
        == "multi-class"
    )
    assert bp.score_brier("multiple_choice", "Z", payload, {}, None) == (None, None)


def test_numeric_brier_needs_the_cdf_and_the_axis():
    payload = {"continuous_cdf": [0.0, 0.5, 1.0]}
    snap = {"scaling": {"continuous_range": [10, 20, 30]}}
    assert bp.score_brier("numeric", 15.0, payload, {}, snap) == (
        pytest.approx((0.0 + 0.25 + 0.0) / 3),
        "ranked",
    )
    assert bp.score_brier("numeric", 15.0, payload, {}, None) == (None, None)
    assert bp.score_brier("numeric", None, payload, {}, snap) == (None, None)


# ===================================================================== costs
def test_costs_sum_every_run_of_a_slug(tmp_path):
    usage = tmp_path / "usage.jsonl"
    usage.write_text(
        "\n".join(
            [
                json.dumps({"slug": "a", "cost_usd_equiv": 0.5}),
                json.dumps({"slug": "a", "cost_usd_equiv": 0.25}),
                json.dumps({"slug": "b", "cost_usd_equiv": None, "parse_failed": True}),
                json.dumps({"slug": None, "cost_usd_equiv": 9.0}),
                "not json",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    assert bp.costs_by_slug(usage) == {"a": (0.75, 2), "b": (0.0, 1)}


# ============================================================== leaderboards
def _entry(uid, score, rank, status=0, **extra):
    return {
        "user": {"id": uid, "username": f"u{uid}"},
        "score": score,
        "rank": rank,
        "exclusion_status": status,
        "excluded": False,
        "coverage": 10,
        "calculated_on": "2026-10-31T11:43:11Z",
        **extra,
    }


BOARD = {
    "is_primary_leaderboard": True,
    "score_type": "spot_peer_tournament",
    "finalized": False,
    "max_coverage": 10,
    "entries": [
        {
            "user": None,
            "aggregation_method": "recency_weighted",
            "score": 900,
            "rank": 1,
        },
        _entry(1, 500.0, 1, status=2),  # a reference bot: shown, not ranked
        _entry(2, 400.0, 1),
        _entry(3, 100.0, 2),
        _entry(4, -50.0, 3),
    ],
}
PROJECT = {
    "id": 33132,
    "type": "question_series",
    "name": "MiniBench - R",
    "slug": "minibench-r",
}


def test_standing_reads_the_bots_own_entry():
    got = bp.standing(PROJECT, [{"is_primary_leaderboard": False}, BOARD], 3, [1.0])
    assert (got["rank"], got["field"], got["score"]) == (2, 3, 100.0)
    assert got["top_score"] == 400.0, (
        "the reference bot is not the leader of the ranked field"
    )
    assert got["excluded"] is False and got["estimated_rank"] is None
    assert got["url"] == "https://www.metaculus.com/tournament/minibench-r/"
    assert got["calculated_on"] == "2026-10-31"


def test_standing_estimates_a_missing_bot_from_its_synced_scores():
    got = bp.standing(PROJECT, [BOARD], 99, [60.0, 60.0])
    assert got["rank"] is None
    assert (
        got["estimated_rank"] == 2
        and got["local_score"] == 120.0
        and got["local_n"] == 2
    )


def test_standing_marks_an_excluded_entry():
    board = {**BOARD, "entries": [_entry(7, 10.0, 4, status=3)]}
    assert bp.standing(PROJECT, [board], 7, [])["excluded"] is True


def test_discovery_costs_one_post_lookup_per_project(monkeypatch):
    projects = {
        10: {"id": 10, "type": "question_series", "slug": "r1"},
        20: {"id": 20, "type": "tournament", "slug": "t2"},
    }
    home = {1: 10, 2: 10, 3: 10, 4: 20}
    fetched = []

    def get_post(pid, stage="api"):
        fetched.append(pid)
        proj = projects[home[pid]]
        key = "question_series" if proj["type"] == "question_series" else "tournament"
        category = {"id": 5, "type": "category"}
        return {"id": pid, "projects": {key: [proj], "category": [category]}}

    def list_posts(project, statuses="open", **k):
        assert statuses == "closed,resolved"
        return [{"id": p} for p, h in home.items() if h == project]

    monkeypatch.setattr(mapi, "get_post", get_post)
    monkeypatch.setattr(mapi, "list_posts", list_posts)
    found = bp.discover_projects([1, 2, 3, 4], pause=0)
    assert sorted(found) == [10, 20]
    assert found[10]["members"] == {1, 2, 3}
    assert len(fetched) == 2, f"one get_post per project, got {fetched}"


def _rows(**kw):
    base = {
        "slug": "s",
        "title": "T",
        "url": "https://www.metaculus.com/questions/1/",
        "post_id": 1,
        "tournament": "minibench",
        "qtype": "binary",
        "status": "resolved",
        "closed": "2026-10-20",
        "resolves": "2026-10-31",
        "forecast": "57.0%",
    }
    return bp.Row(**{**base, **kw})


def test_leaderboards_are_skipped_without_a_token(monkeypatch):
    for name in mapi.TOKEN_ENVS:
        monkeypatch.delenv(name, raising=False)
    boards, note, bot = bp.leaderboards([_rows()], [])
    assert boards == [] and bot == {} and note.startswith("skipped")


def test_an_api_failure_leaves_a_note_and_never_raises(monkeypatch):
    monkeypatch.setenv("METACULUS_API_KEY", "x" * 12)

    def broken():
        raise mapi.MetaculusError("page", 500, "boom")

    monkeypatch.setattr(mapi, "whoami", broken)
    boards, note, _ = bp.leaderboards([_rows()], [])
    assert boards == [] and note.startswith("unavailable") and "boom" in note


def test_unscored_tournaments_are_not_looked_up(monkeypatch):
    monkeypatch.setenv("METACULUS_API_KEY", "x" * 12)
    monkeypatch.setattr(mapi, "whoami", lambda: pytest.fail("no API call expected"))
    _, note, _ = bp.leaderboards([_rows(tournament="bot-testing-area")], [])
    assert "no closed or resolved question" in note


# ==================================================================== render
def test_page_links_to_metaculus_and_escapes_titles():
    row = _rows(
        title="<script>x</script> & Co",
        brier=0.3249,
        brier_kind="binary",
        peer_score=-1.16,
        outcome="No",
        cost_usd=0.54,
        runs=1,
    )
    page = bp.render_html([row], [], 2, [], "skipped: test", {}, NOW)
    assert "<script>x" not in page and "&lt;script&gt;x&lt;/script&gt; &amp; Co" in page
    assert 'href="https://www.metaculus.com/questions/1/"' in page
    assert "0.325" in page and "-1.2" in page and "0.54" in page
    assert "2 dropped question(s)" in page and "Leaderboards skipped: test." in page


def test_page_shows_rank_or_its_estimate():
    listed = bp.standing(PROJECT, [BOARD], 3, [100.0])
    missing = bp.standing(PROJECT, [BOARD], 99, [100.0])
    page = bp.render_html(
        [], [], 0, [listed, missing], None, {"id": 3, "username": "b"}, NOW
    )
    assert "2 of 3" in page
    assert "not listed; ~2 of 3 by its 1 synced scores (estimate)" in page
    assert 'href="https://www.metaculus.com/accounts/profile/3/"' in page


# ============================================================ the real repo
def test_every_resolved_question_gets_a_brier_and_its_peer_score():
    """The page shows a dash where it cannot score; on this data it never should."""
    resolved, closed, _ = bp.build_rows()
    for row in resolved:
        assert row.url and row.url.startswith("https://www.metaculus.com/"), row.slug
        if row.qtype not in ("binary", "multiple_choice", "numeric", "discrete"):
            continue
        assert row.brier is not None, f"{row.slug}: no Brier score ({row.qtype})"
        assert row.outcome is not None, f"{row.slug}: no outcome"
        if row.tournament:
            assert row.peer_score is not None, f"{row.slug}: no official peer score"
    for row in closed:
        assert row.status == "closed" and row.brier is None, row.slug


def test_cli_builds_the_page_offline(tmp_path):
    env = {k: v for k, v in os.environ.items() if k not in mapi.TOKEN_ENVS}
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "build_page.py"), "--out", str(tmp_path)],
        cwd=REPO,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**env, "PYTHONIOENCODING": "cp1252"},
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    data = json.loads((tmp_path / "results.json").read_text(encoding="utf-8"))
    assert data["leaderboard_note"].startswith("skipped")
    page = (tmp_path / "index.html").read_text(encoding="utf-8")
    assert f"Resolved ({len(data['resolved'])})" in page


def test_page_tables_are_sortable():
    row = _rows(peer_score=1.0, cost_usd=0.5, runs=1)
    page = bp.render_html([row], [row], 0, [], "skipped: test", {}, NOW)
    # Resolved and closed tables; sorting is a progressive enhancement, so the
    # rows must still be in the HTML in build order without it.
    assert page.count('<table class="sortable">') == 2
    assert page.count("<script>") == 1 and "table.sortable" in page


def test_page_css_sort_arrows_are_css_escapes_not_control_characters():
    # "\2195" in a non-raw Python string is an octal escape plus "95" (rendered as □95).
    page = bp.render_html([], [], 0, [], "skipped: test", {}, NOW)
    assert "\\2195" in page and "\\25B2" in page and "\\25BC" in page
    assert not any(ord(c) < 32 and c not in "\n\t" for c in page)


# ================================================================= bot usage
T0 = dt.datetime(2026, 11, 2, 0, 0, tzinfo=dt.UTC)


def _at(hours: float) -> str:
    return (T0 + dt.timedelta(hours=hours)).isoformat()


def _meta(i: int, opened_h: float, submitted: bool = True, tournament: str = "minibench",
          title: str | None = None) -> tuple[str, dict]:
    slug = f"2026-11-02-mc{1000 + i}-q"
    return slug, {"title": title or f"Q{i}", "tournament": {
        "slug": tournament, "opened": _at(opened_h), "closes": _at(opened_h + 3),
        "submitted": _at(opened_h + 1) if submitted else None}}


def _use(slug: str, end_h: float, cost: float = 1.5, *, refused: bool = False, model="opus",
         **extra) -> dict:
    if refused:  # as the old recorder logged a refusal
        return {"ts": _at(end_h), "slug": slug, "model": model, "cost_usd_equiv": 0.0,
                "num_turns": 1, "by_model": {}, "conclusion": "success", "duration_s": 0.5,
                **extra}
    return {"ts": _at(end_h), "slug": slug, "model": model, "cost_usd_equiv": cost,
            "num_turns": 30, "web_searches": 12, "by_model": {model: cost},
            "conclusion": "success", "duration_s": 180, **extra}


def test_usage_section_with_no_usage_says_so_and_still_renders():
    sec = pu.build([], [], al.Config(), shown=3)
    assert sec.rounds == [] and sec.per_slug == {}
    assert "No sessions on MiniBench questions recorded yet" in sec.html
    assert "No MiniBench round recorded yet" in sec.html
    assert "No allowance reading recorded yet" in sec.html
    page = bp.render_html([], [], 0, [], "skipped: test", {}, NOW, sec)
    assert "<h2>Bot usage</h2>" in page


def test_usage_section_with_refused_sessions_only():
    slug, meta = _meta(1, 1.0, submitted=False)
    records = [_use(slug, 1.5, refused=True), _use(slug, 2.5, refused=True)]
    sec = pu.build(records, [(slug, meta)], al.Config(), shown=3)
    (row,) = sec.rounds
    assert (row["questions"], row["submitted"], row["refused"], row["sessions"]) == (1, 0, 2, 2)
    assert row["cost_usd"] == 0 and row["median_searches"] is None and row["models"] == []
    assert 'class="c-refused"' in sec.html and "refused (usage limit)" in sec.html
    assert 'class="c-band"' in sec.html, "the refusal period is shaded"
    assert "usage_limit (inferred)" in sec.html, "an old-style refusal is labelled inferred"
    assert sec.per_slug[slug]["models"] == [] and sec.per_slug[slug]["allowance"] == 0


def test_two_rounds_split_at_a_72_hour_gap_and_the_last_n_are_drawn():
    metas = [_meta(1, 0), _meta(2, 5), _meta(3, 5 + 71.9),  # one round: gaps < 72 h
             _meta(4, 5 + 71.9 + 72, submitted=False)]       # a new round
    records = [_use(metas[0][0], 1), _use(metas[1][0], 6, model="sonnet"),
               _use(metas[3][0], 150, refused=True), _use("other-slug", 7, cost=9.0)]
    sec = pu.build(records, metas, al.Config(), shown=1)
    assert [(r["round"], r["questions"], r["submitted"]) for r in sec.rounds] == [
        (1, 3, 3), (2, 1, 0)
    ]
    assert sec.rounds[0]["cost_usd"] == 3.0, "a session on another question is not counted"
    assert sec.rounds[0]["models"] == ["Opus", "Sonnet"]
    captions = [line for line in sec.html.splitlines() if 'style="margin:0 0 4px">Round' in line]
    assert len(captions) == 1 and ">Round 2: " in captions[0], "only the last round is drawn"
    assert "Round 2</text>" in sec.html, "the session chart marks where round 2 starts"
    # 7-day share: $3 at the configured $100 per week
    assert sec.rounds[0]["allowance_7d_pct"] == 3.0


def test_only_the_round_tournament_counts():
    metas = [_meta(1, 0), _meta(2, 1, tournament="bot-testing-area")]
    qs = pu.tournament_questions(metas)
    assert [q.slug for q in qs] == [metas[0][0]]


def test_refusal_periods_join_refusals_until_a_served_session():
    sessions = pu.parse_usage([
        _use("a", 1, refused=True), _use("b", 2, refused=True),  # one period
        _use("c", 2.5),                                          # served: it ends here
        _use("d", 6, refused=True),                              # a new one
    ])
    (a1, b1), (a2, b2) = pu.refusal_periods(sessions)
    assert a1 == T0 + dt.timedelta(hours=1, seconds=-0.5)
    assert b1 == T0 + dt.timedelta(hours=2.5, seconds=-180), "cut at the served session's start"
    assert b2 - a2 == dt.timedelta(minutes=30, seconds=0.5)


def test_question_rows_carry_model_effort_mode_and_estimated_allowance():
    slug, meta = _meta(1, 0)
    records = [
        _use(slug, 1, cost=1.6, config={"effort": "high", "mode": "deep"}),
        _use(slug, 2, refused=True, model="sonnet", config={"effort": "medium", "mode": "lean"}),
    ]
    sec = pu.build(records, [(slug, meta)], al.Config(), shown=3)
    use = sec.per_slug[slug]
    assert use["models"] == ["Opus"], "a refused session ran no model"
    assert (use["efforts"], use["modes"]) == (["high", "medium"], ["deep", "lean"])
    assert use["allowance"] == pytest.approx(1.6 * 100 / 16)  # 10 % of a 5-hour window
    row = _rows(cost_usd=1.6, runs=2)
    row.models, row.efforts, row.modes, row.allowance_5h_pct = "Opus", "high", "deep", 10.0
    page = bp.render_html([row], [row], 0, [], "skipped: test", {}, NOW, sec)
    assert '<td class="n">10 %</td><td>Opus</td><td>high</td><td>deep</td>' in page
    assert page.count("<th>Est. allowance</th>") == 3, "resolved, closed, per round"


def test_titles_reach_tooltips_escaped():
    slug, meta = _meta(1, 0, title='<img src=x onerror="alert(1)">')
    sec = pu.build([_use(slug, 1)], [(slug, meta)], al.Config(), shown=3)
    assert "<img" not in sec.html and "&lt;img src=x onerror=&quot;alert(1)&quot;&gt;" in sec.html
    assert "textContent" in pu.TIP_JS and "innerHTML" not in pu.TIP_JS


def test_the_tooltip_script_survives_following_the_sort_script():
    # SORT_JS ends in a call; a bare "(function" after it is parsed as a call on its result.
    assert pu.TIP_JS.lstrip().startswith(";(function")


def test_allowance_chart_plots_readings_and_marks_resets():
    slug, meta = _meta(1, 0)
    reading = {"windows": {"five_hour": {"first": 90.0, "last": 92.0,
                                         "resets_at": _at(4)}}}
    sec = pu.build([_use(slug, 1, allowance=reading)], [(slug, meta)], al.Config(), shown=3)
    assert '<circle class="c-5h ring"' in sec.html and "92 %" in sec.html
    assert "5-hour window reset" in sec.html


@pytest.mark.parametrize(("raw", "n"), [(None, 3), ("", 3), ("5", 5), ("0", 3), ("x", 3)])
def test_rounds_shown_follows_page_usage_rounds(monkeypatch, raw, n):
    if raw is None:
        monkeypatch.delenv("PAGE_USAGE_ROUNDS", raising=False)
    else:
        monkeypatch.setenv("PAGE_USAGE_ROUNDS", raw)
    assert pu.rounds_shown() == n


def test_the_real_ledger_builds_a_usage_section_with_its_rounds():
    from _common import all_questions, ledger_records
    from record_usage import USAGE

    sec = pu.build(ledger_records(USAGE), list(all_questions()), al.Config(), shown=3)
    assert sec.rounds, "MiniBench rounds 1 and 2 are in the repository"
    for r in sec.rounds:
        assert 0 <= r["submitted"] <= r["questions"]
        assert r["refused"] <= r["sessions"]
    assert "<h2>Bot usage</h2>" in sec.html
