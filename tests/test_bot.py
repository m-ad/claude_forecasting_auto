"""The bot's own machinery: API client, gate, usage meter, one-shot submit, sync.

Everything here runs against fakes -- no network, no token. The irreversible step
(a forecast POST on a one-shot question) gets the most cases: each guard is
tested by showing that the POST is never reached.
"""

from __future__ import annotations

import datetime as dt
import io
import json
import subprocess
import urllib.error

import _common
import ci_guard
import log_forecast
import metaculus_api as mapi
import pytest
import record_usage
import submit_metaculus as sm
import tournament_poll as tp
import tournament_sync as ts
import yaml

NOW = dt.datetime(2026, 10, 19, 15, 0, tzinfo=dt.UTC)


# ======================================================================= API
class _Resp:
    def __init__(self, body: object, status: int = 200):
        self._raw = json.dumps(body).encode()
        self.status = status

    def read(self) -> bytes:
        return self._raw

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def _http_error(code: int, body: str) -> urllib.error.HTTPError:
    return urllib.error.HTTPError("u", code, "x", {}, io.BytesIO(body.encode()))


@pytest.fixture
def wire(monkeypatch):
    """Script ``urlopen``: each call pops the next answer; records the requests."""
    monkeypatch.setenv("METACULUS_API_KEY", "tok-1234567890")
    monkeypatch.setattr(mapi.time, "sleep", lambda s: None)
    calls: list[object] = []
    answers: list[object] = []

    def fake(req, timeout=None):
        calls.append(req)
        ans = answers.pop(0)
        if isinstance(ans, Exception):
            raise ans
        return ans

    monkeypatch.setattr(mapi.urllib.request, "urlopen", fake)
    return calls, answers


def test_request_sends_the_token_and_an_unbanned_user_agent(wire):
    calls, answers = wire
    answers.append(_Resp({"ok": 1}))
    assert mapi.request("GET", "posts/1/") == (200, {"ok": 1})
    req = calls[0]
    assert req.get_header("Authorization") == "Token tok-1234567890"
    assert "Python-urllib" not in req.get_header("User-agent")


def test_a_5xx_is_retried_once_then_succeeds(wire):
    calls, answers = wire
    answers += [_http_error(502, "bad gateway"), _Resp({"ok": 1})]
    assert mapi.get_json("posts/1/") == {"ok": 1}
    assert len(calls) == 2


def test_a_400_is_raised_at_once_not_retried(wire):
    calls, answers = wire
    answers.append(_http_error(400, '{"continuous_cdf": "bad"}'))
    with pytest.raises(mapi.MetaculusError, match="400") as exc:
        mapi.request("POST", "questions/forecast/", body=[{}], stage="submit")
    assert not isinstance(exc.value, mapi.MetaculusAuthError)
    assert len(calls) == 1


def test_a_json_401_is_an_auth_error(wire):
    _calls, answers = wire
    answers.append(_http_error(401, '{"detail": "Invalid token."}'))
    with pytest.raises(mapi.MetaculusAuthError):
        mapi.whoami()


def test_a_cloudflare_page_is_not_mistaken_for_a_bad_token(wire):
    _calls, answers = wire
    answers.append(_http_error(403, "<html><title>Just a moment...</title>cloudflare</html>"))
    with pytest.raises(mapi.MetaculusError, match="Cloudflare") as exc:
        mapi.whoami()
    assert not isinstance(exc.value, mapi.MetaculusAuthError)


def test_429_waits_and_retries(wire):
    calls, answers = wire
    answers += [_http_error(429, "slow down"), _Resp({"ok": 1})]
    assert mapi.get_json("posts/1/") == {"ok": 1}
    assert len(calls) == 2


def test_no_token_is_an_auth_error_before_any_request(wire, monkeypatch):
    calls, _answers = wire
    for name in mapi.TOKEN_ENVS:
        monkeypatch.delenv(name, raising=False)
    with pytest.raises(mapi.MetaculusAuthError):
        mapi.whoami()
    assert calls == []


def test_errors_never_carry_the_token(wire):
    _calls, answers = wire
    answers.append(_http_error(400, "echo: Authorization: Token tok-1234567890"))
    with pytest.raises(mapi.MetaculusError) as exc:
        mapi.get_json("posts/1/")
    assert "tok-1234567890" not in str(exc.value)


def test_list_posts_follows_pagination(wire):
    calls, answers = wire
    answers += [
        _Resp({"results": [{"id": i} for i in range(2)], "next": "more"}),
        _Resp({"results": [{"id": 9}], "next": None}),
    ]
    assert [p["id"] for p in mapi.list_posts("minibench", page_size=2)] == [0, 1, 9]
    assert "offset=2" in calls[1].full_url and "tournaments=minibench" in calls[1].full_url


def test_forecast_body_carries_exactly_one_value_kind():
    (body,) = mapi.forecast_body(7, {"probability_yes": 0.2})
    assert body == {
        "question": 7,
        "source": "api",
        "probability_yes": 0.2,
        "probability_yes_per_category": None,
        "continuous_cdf": None,
    }


def test_live_values_ignores_a_withdrawn_forecast():
    assert mapi.live_values({"my_forecasts": {"latest": None}}) is None
    q = {"my_forecasts": {"latest": {"forecast_values": [0.8, 0.2], "end_time": 1}}}
    assert mapi.live_values(q) is None
    q["my_forecasts"]["latest"]["end_time"] = None
    assert mapi.live_values(q) == [0.8, 0.2]


# ====================================================================== gate
def test_budget_guard_stops_and_soft_lands():
    assert tp.budget_cap(6, None, 999.0) == (6, None)
    assert tp.budget_cap(6, 100.0, 100.0) == (0, "budget_exceeded")
    assert tp.budget_cap(6, 100.0, 85.0) == (2, "budget_soft_landing")
    assert tp.budget_cap(6, 100.0, 10.0) == (6, None)


def _post(pid, qtype="binary", closes="2026-10-19T17:00:00Z", group=False):
    post = {"id": pid, "title": f"Q{pid}", "status": "open", "scheduled_close_time": closes}
    if group:
        post["group_of_questions"] = {"questions": []}
    else:
        post["question"] = {
            "id": pid + 1000,
            "type": qtype,
            "status": "open",
            "scheduled_close_time": closes,
            "my_forecasts": {"latest": None},
        }
    return post


def test_gate_keeps_only_open_unforecast_questions_in_priority_order(monkeypatch):
    posts = {
        "minibench": [
            _post(1, closes="2026-10-19T17:30:00Z"),
            _post(2, closes="2026-10-19T16:30:00Z"),
            _post(3, group=True),
            _post(4, closes="2026-10-19T15:10:00Z"),  # 10 min left
            _post(5),  # already forecast on Metaculus
            _post(6),  # already submitted here
        ],
        "bot-testing-area": [_post(7, closes="2026-10-19T15:40:00Z")],
    }
    live = _post(5)
    live["question"]["my_forecasts"]["latest"] = {"forecast_values": [0.5, 0.5]}
    details = {p["id"]: p for ps in posts.values() for p in ps} | {5: live}
    monkeypatch.setattr(mapi, "list_posts", lambda slug, **k: posts[slug])
    monkeypatch.setattr(mapi, "get_post", lambda pid, stage="api": details[pid])
    monkeypatch.setattr(tp.time, "sleep", lambda s: None)
    monkeypatch.setattr(tp, "local_state", lambda: {6: {"submitted": "2026-10-19T14:00:00+00:00"}})
    tours = [{"slug": "minibench", "priority": 1}, {"slug": "bot-testing-area", "priority": 9}]
    found, skipped = tp.candidates(tours, NOW)
    assert [c["post_id"] for c in found] == [2, 1, 7], "priority, then soonest close"
    assert found[0]["question_id"] == 1002
    reasons = dict(skipped)
    assert "group" in reasons[3] and "< 20 min" in reasons[4]
    assert "already holds" in reasons[5] and "submitted" in reasons[6]


# ===================================================================== usage
RESULT = {
    "type": "result",
    "subtype": "success",
    "is_error": False,
    "duration_ms": 412000,
    "num_turns": 38,
    "total_cost_usd": 1.2345,
    "usage": {
        "input_tokens": 100,
        "output_tokens": 50,
        "cache_read_input_tokens": 9000,
        "cache_creation_input_tokens": 700,
        "server_tool_use": {"web_search_requests": 6},
    },
    "modelUsage": {"claude-opus-x": {"costUSD": 1.0}, "claude-sonnet-x": {"costUSD": 0.2345}},
    "permission_denials": [{"tool_name": "Bash"}],
}


@pytest.mark.parametrize(
    "text",
    [
        json.dumps(RESULT),
        json.dumps([{"type": "system"}, RESULT]),
        "\n".join([json.dumps({"type": "assistant"}), json.dumps(RESULT)]),
    ],
    ids=["object", "array", "jsonl"],
)
def test_usage_parses_every_output_shape(text):
    rec = record_usage.usage_record(
        record_usage.parse_result(text), job="j", run_id="1", slug="s", model="opus"
    )
    assert rec["cost_usd_equiv"] == 1.2345 and rec["num_turns"] == 38
    assert rec["tokens"] == {"input": 100, "output": 50, "cache_read": 9000, "cache_write": 700}
    assert rec["web_searches"] == 6 and rec["permission_denials"] == 1
    assert rec["by_model"]["claude-sonnet-x"] == 0.2345


def test_usage_counts_searches_per_model_and_names_denied_tools():
    # The CLI's WebSearch runs as its own model call: the count lands in modelUsage,
    # not in the top-level usage.server_tool_use.
    result = {
        **RESULT,
        "usage": {"input_tokens": 1},
        "modelUsage": {
            "claude-sonnet-x": {"costUSD": 0.2, "webSearchRequests": 0},
            "claude-haiku-x": {"costUSD": 0.02, "webSearchRequests": 4},
        },
        "permission_denials": [
            {"tool_name": "Bash", "tool_input": {"command": "cat questions/x/raw/q.json | head"}},
            {"tool_name": "Skill", "tool_input": {"skill": "tournament-forecast"}},
        ],
    }
    rec = record_usage.usage_record(result, job="j", run_id="1", slug="s", model="sonnet")
    assert rec["web_searches"] == 4
    assert rec["permission_denials"] == 2
    assert rec["denied"] == ["Bash:cat", "Skill"]


def test_a_killed_run_records_zero_cost_instead_of_failing():
    assert record_usage.parse_result("") is None
    rec = record_usage.usage_record(None, job="j", run_id="1", slug="s", model="m", exit_code=143)
    assert rec["parse_failed"] is True and rec["conclusion"] == "timeout"
    assert rec["cost_usd_equiv"] == 0.0


def test_weekly_spend_counts_only_the_trailing_week(tmp_path):
    path = tmp_path / "usage.jsonl"
    for days, cost in ((1, 2.0), (6, 3.0), (8, 100.0)):
        ts_ = (NOW - dt.timedelta(days=days)).isoformat()
        record_usage.append({"ts": ts_, "cost_usd_equiv": cost, "slug": f"s{days}"}, path)
    assert record_usage.weekly_spend(NOW, path) == 5.0


# ============================================================ one-shot submit
SUMMARY = (
    "**Question**: [Will X?](https://www.metaculus.com/questions/46044/)\n"
    "**Date**: 2026-10-19\n"
    "**Forecast**: Median 12.0%, IQR [8.0%, 18.0%]\n"
    "**Thesis**: Base rate of 10% for similar announcements, nudged up by the "
    "scheduled vote; most sensitive to the vote date.\n"
)


@pytest.fixture
def bot_repo(tmp_path, monkeypatch):
    """A one-question repo with a logged v1 and a fake Metaculus behind it."""
    questions = tmp_path / "questions"
    slug = "2026-10-19-mc46044-will-x"
    (questions / slug / "raw").mkdir(parents=True)
    monkeypatch.setattr(_common, "QUESTIONS", questions)
    monkeypatch.setattr(sm, "QUESTIONS", questions)
    monkeypatch.setattr(ts, "QUESTIONS", questions)
    ledger = tmp_path / "forecasts.jsonl"
    monkeypatch.setattr(log_forecast, "LEDGER", ledger)
    monkeypatch.setattr(sm.time, "sleep", lambda s: None)
    meta = {
        "slug": slug,
        "title": "Will X?",
        "source": "metaculus",
        "url": "https://www.metaculus.com/questions/46044/",
        "post_id": 46044,
        "question_id": 46283,
        "type": "binary",
        "status": "open",
        "tournament": {
            "slug": "minibench",
            "mode": "one_shot",
            "registered": "2026-10-19",
            "opened": "2026-10-19T14:00:00Z",
            "closes": "2026-10-19T17:00:00Z",
            "submitted": None,
            "submitted_forecast": None,
            "comment_posted": False,
            "official_score": None,
            "missed_window": False,
        },
        "current": {"version": 1, "median": 0.12, "iqr": [0.08, 0.18]},
        "next_review": None,
        "resolution": {"outcome": None, "date": None, "source": None},
    }
    _common.save_meta(slug, meta)
    (questions / slug / "forecast.md").write_text(
        "# Will X?\n\n| | |\n|---|---|\n| **Status** | open |\n"
        "| **Current forecast** | Median 12.0%, IQR [8.0%, 18.0%] (v1, 2026-10-19) |\n\n"
        "---\n\n## v1 — Initial forecast — 2026-10-19\n\n### What resolves YES\n\nX.\n\n"
        "<!-- note to self -->\n\n" + SUMMARY,
        encoding="utf-8",
    )
    rec = {
        "event": "forecast", "slug": slug, "version": 1, "source": "metaculus",
        "post_id": 46044, "type": "binary", "median": 0.12, "iqr": [0.08, 0.18],
    }
    ledger.write_text(json.dumps(rec) + "\n", encoding="utf-8")
    post = _post(46044)
    post["question"]["id"] = 46283
    sent: dict[str, list] = {"forecast": [], "comment": []}
    monkeypatch.setattr(mapi, "get_post", lambda pid, stage="api": post)

    def submit(qid, values):
        sent["forecast"].append((qid, values))
        return 201

    def comment(pid, text, private=True):
        sent["comment"].append((pid, text, private))
        return 201

    monkeypatch.setattr(mapi, "submit_forecast", submit)
    monkeypatch.setattr(mapi, "post_comment", comment)
    return {"slug": slug, "rec": rec, "post": post, "sent": sent, "ledger": ledger}


def _ledger(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def test_one_shot_submits_forecast_then_private_comment_and_records_both(bot_repo):
    b = bot_repo
    assert sm.submit_one_shot(b["slug"], b["rec"], dry_run=False) == "submitted"
    assert b["sent"]["forecast"] == [(46283, {"probability_yes": 0.12})]
    (pid, text, private) = b["sent"]["comment"][0]
    assert pid == 46044 and private is True
    assert "### What resolves YES" in text and "**Thesis**:" in text
    assert "note to self" not in text, "HTML comments are not part of the rationale"
    sub = _ledger(b["ledger"])[-1]
    assert sub["event"] == "submission" and sub["api_status"] == 201
    meta = _common.load_meta(b["slug"])
    assert meta["tournament"]["submitted"] == sub["ts"]
    assert meta["tournament"]["comment_posted"] is True


def test_a_second_run_is_refused_without_reaching_the_api(bot_repo):
    b = bot_repo
    sm.submit_one_shot(b["slug"], b["rec"], dry_run=False)
    assert sm.submit_one_shot(b["slug"], b["rec"], dry_run=False) == "already submitted"
    assert len(b["sent"]["forecast"]) == 1


def test_a_live_remote_forecast_blocks_resubmission_even_without_a_local_record(bot_repo):
    b = bot_repo
    b["post"]["question"]["my_forecasts"]["latest"] = {"forecast_values": [0.9, 0.1]}
    assert sm.submit_one_shot(b["slug"], b["rec"], dry_run=False) == "already live"
    assert b["sent"]["forecast"] == []


def test_a_closed_window_is_recorded_as_missed_not_raised(bot_repo):
    b = bot_repo
    b["post"]["status"] = "closed"
    assert sm.submit_one_shot(b["slug"], b["rec"], dry_run=False) == "missed window"
    meta = _common.load_meta(b["slug"])
    assert meta["tournament"]["missed_window"] is True and meta["status"] == "dropped"
    assert "| **Status** | dropped |" in (_common.QUESTIONS / b["slug"] / "forecast.md").read_text(
        encoding="utf-8"
    )
    assert b["sent"]["forecast"] == []


def test_a_failed_comment_keeps_the_forecast_and_flags_the_retry(bot_repo, monkeypatch):
    b = bot_repo

    def broken(pid, text, private=True):
        raise mapi.MetaculusError("comment", 500, "boom")

    monkeypatch.setattr(mapi, "post_comment", broken)
    assert sm.submit_one_shot(b["slug"], b["rec"], dry_run=False) == "submitted-no-comment"
    assert _common.load_meta(b["slug"])["tournament"]["comment_posted"] is False
    assert _ledger(b["ledger"])[-1]["comment_posted"] is False


def test_dry_run_builds_everything_and_sends_nothing(bot_repo):
    b = bot_repo
    assert sm.submit_one_shot(b["slug"], b["rec"], dry_run=True) == "would submit"
    assert b["sent"] == {"forecast": [], "comment": []}
    assert len(_ledger(b["ledger"])) == 1


def test_no_logged_forecast_means_nothing_to_submit(bot_repo):
    b = bot_repo
    assert sm.submit_one_shot(b["slug"], None, dry_run=False) == "no forecast"
    assert b["sent"]["forecast"] == []


def test_comment_is_cut_in_the_middle_never_at_the_summary(bot_repo, monkeypatch):
    b = bot_repo
    path = _common.QUESTIONS / b["slug"] / "forecast.md"
    path.write_text(path.read_text(encoding="utf-8").replace("X.\n", "x" * 20000 + "\n"))
    monkeypatch.setattr(sm, "MAX_COMMENT_CHARS", 2000)
    text = sm.comment_text(b["slug"])
    assert len(text) <= 2000 and "[... truncated ...]" in text
    assert text.endswith(SUMMARY.strip())


def test_an_unfilled_summary_is_not_submitted(bot_repo):
    b = bot_repo
    path = _common.QUESTIONS / b["slug"] / "forecast.md"
    text = path.read_text(encoding="utf-8")
    path.write_text(text[: text.index("**Thesis**:")] + "**Thesis**: \n", encoding="utf-8")
    with pytest.raises(sm.SubmitError, match="summary block"):
        sm.comment_text(b["slug"])


# ====================================================================== sync
def test_sync_closes_out_a_missed_window(bot_repo):
    b = bot_repo
    b["post"]["status"] = "closed"
    meta = _common.load_meta(b["slug"])
    assert ts.sync_one(b["slug"], meta, dry_run=False) == "missed window -> dropped"
    assert _common.load_meta(b["slug"])["status"] == "dropped"


def test_sync_retries_a_missing_comment_and_records_it(bot_repo, monkeypatch):
    b = bot_repo

    def broken(pid, text, private=True):
        raise mapi.MetaculusError("comment", 500, "boom")

    monkeypatch.setattr(mapi, "post_comment", broken)
    sm.submit_one_shot(b["slug"], b["rec"], dry_run=False)
    monkeypatch.setattr(mapi, "post_comment", lambda pid, text, private=True: 201)
    meta = _common.load_meta(b["slug"])
    assert "comment posted" in ts.sync_one(b["slug"], meta, dry_run=False)
    assert _ledger(b["ledger"])[-1]["event"] == "comment"
    assert _common.load_meta(b["slug"])["tournament"]["comment_posted"] is True


def test_sync_records_a_resolution_with_the_official_score(bot_repo):
    b = bot_repo
    sm.submit_one_shot(b["slug"], b["rec"], dry_run=False)
    q = b["post"]["question"]
    b["post"]["status"] = q["status"] = "resolved"
    q["resolution"] = "no"
    q["my_forecasts"]["score_data"] = {"spot_peer_score": 4.2}
    meta = _common.load_meta(b["slug"])
    assert "resolved no" in ts.sync_one(b["slug"], meta, dry_run=False)
    meta = _common.load_meta(b["slug"])
    assert meta["status"] == "resolved" and meta["resolution"]["outcome"] == 0.0
    assert meta["tournament"]["official_score"] == 4.2
    text = (_common.QUESTIONS / b["slug"] / "forecast.md").read_text(encoding="utf-8")
    assert "## Resolution" in text and "+4.20" in text and "| **Status** | resolved |" in text


def test_sync_drops_an_annulled_question(bot_repo):
    b = bot_repo
    sm.submit_one_shot(b["slug"], b["rec"], dry_run=False)
    q = b["post"]["question"]
    b["post"]["status"] = q["status"] = "resolved"
    q["resolution"] = "annulled"
    ts.sync_one(b["slug"], _common.load_meta(b["slug"]), dry_run=False)
    assert _common.load_meta(b["slug"])["status"] == "dropped"


def test_ci_settings_keep_the_model_away_from_submission_and_secrets():
    from conftest import REPO

    settings = json.loads((REPO / ".claude" / "settings.ci.json").read_text("utf-8"))
    deny = settings["permissions"]["deny"]
    for rule in (
        "Bash(uv run scripts/submit_metaculus.py:*)",
        "Bash(git:*)",
        "Read(.git/**)",
        "Read(//proc/**)",
        "Edit(ledger/**)",
    ):
        assert rule in deny, f"settings.ci.json must deny {rule}"
    workflow = yaml.safe_load(
        (REPO / ".github" / "workflows" / "tournament-sweep.yml").read_text("utf-8")
    )
    steps = workflow["jobs"]["forecast"]["steps"]
    claude = next(s for s in steps if s.get("id") == "claude")
    assert "METACULUS_API_KEY" not in claude.get("env", {}), (
        "the forecaster session must not hold the Metaculus token"
    )
    checkout = steps[0]
    assert checkout["with"]["persist-credentials"] is False
    names = [s.get("id") for s in steps]
    assert names.index("claude") < names.index("guard") < names.index("submit"), (
        "the guard must run between the session and the steps that hold secrets"
    )
    for step in steps[names.index("guard") + 1 :]:
        if "METACULUS_API_KEY" in step.get("env", {}) or "GITHUB_TOKEN" in step.get(
            "env", {}
        ):
            assert "steps.guard.outcome == 'success'" in step["if"], step["name"]


# ================================================================ CI guard


@pytest.fixture
def session_repo(tmp_path):
    """A committed repo, then a session that wrote both where it may and may not."""

    def git(*args):
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)

    slug = "2026-10-19-mc46044-will-x"
    files = {
        "scripts/submit_metaculus.py": "SAFE = True\n",
        "pyproject.toml": "[project]\n",
        f"questions/{slug}/meta.yaml": "current: {}\n",
        "questions/other/meta.yaml": "x: 1\n",
        "ledger/forecasts.jsonl": '{"event": "forecast", "slug": "old"}\n',
    }
    for rel, text in files.items():
        (tmp_path / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / rel).write_text(text, encoding="utf-8")
    git("init", "-q")
    git("add", "-A")
    git("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "seed")
    return tmp_path, slug


def test_guard_keeps_the_question_folder_and_undoes_everything_else(session_repo):
    repo, slug = session_repo
    (repo / "scripts/submit_metaculus.py").write_text("SAFE = False\n", encoding="utf-8")
    (repo / "pyproject.toml").unlink()
    (repo / "questions/other/meta.yaml").write_text("x: 2\n", encoding="utf-8")
    (repo / "planted.py").write_text("evil\n", encoding="utf-8")
    (repo / f"questions/{slug}/model.py").write_text("import numpy\n", encoding="utf-8")
    (repo / f"questions/{slug}/meta.yaml").write_text("current: {version: 1}\n")
    actions = ci_guard.guard(slug, repo)
    assert (repo / "scripts/submit_metaculus.py").read_text() == "SAFE = True\n"
    assert (repo / "pyproject.toml").exists()
    assert (repo / "questions/other/meta.yaml").read_text() == "x: 1\n"
    assert not (repo / "planted.py").exists()
    assert (repo / f"questions/{slug}/model.py").exists(), "the session's own model stays"
    assert "version: 1" in (repo / f"questions/{slug}/meta.yaml").read_text()
    assert len(actions) == 4


def test_guard_keeps_only_this_slugs_new_forecast_lines(session_repo):
    repo, slug = session_repo
    ledger = repo / "ledger/forecasts.jsonl"
    good = json.dumps({"event": "forecast", "slug": slug, "version": 1})
    fake_sub = json.dumps({"event": "submission", "slug": slug})
    other = json.dumps({"event": "forecast", "slug": "someone-else"})
    ledger.write_text(ledger.read_text() + f"{good}\n{fake_sub}\n{other}\njunk\n")
    actions = ci_guard.guard(slug, repo)
    lines = ledger.read_text().splitlines()
    assert lines == ['{"event": "forecast", "slug": "old"}', good]
    assert any("dropped 3" in a for a in actions)


def test_guard_restores_a_rewritten_ledger_prefix(session_repo):
    repo, slug = session_repo
    good = json.dumps({"event": "forecast", "slug": slug, "version": 1})
    (repo / "ledger/forecasts.jsonl").write_text(good + "\n", encoding="utf-8")
    ci_guard.guard(slug, repo)
    assert (repo / "ledger/forecasts.jsonl").read_text().splitlines() == [
        '{"event": "forecast", "slug": "old"}',
        good,
    ]


def test_guard_changes_nothing_after_a_clean_session(session_repo):
    repo, slug = session_repo
    good = json.dumps({"event": "forecast", "slug": slug, "version": 1})
    ledger = repo / "ledger/forecasts.jsonl"
    ledger.write_text(ledger.read_text() + good + "\n", encoding="utf-8")
    assert ci_guard.guard(slug, repo) == []


@pytest.mark.parametrize("bad", ["", "../x", ".hidden", "a/b"])
def test_guard_refuses_a_slug_that_could_escape_questions(session_repo, bad):
    repo, _slug = session_repo
    with pytest.raises(ValueError):
        ci_guard.guard(bad, repo)


def test_every_workflow_secret_and_variable_is_documented():
    """docs/configuration.md is the one list of what the bot reads; keep it complete."""
    import re

    from conftest import REPO

    doc = (REPO / "docs" / "configuration.md").read_text("utf-8")
    used = set()
    for wf in (REPO / ".github" / "workflows").glob("*.yml"):
        used |= set(re.findall(r"\b(?:secrets|vars)\.([A-Z][A-Z0-9_]*)", wf.read_text("utf-8")))
    missing = sorted(name for name in used if f"`{name}`" not in doc)
    assert not missing, f"docs/configuration.md does not document {missing}"
