#!/usr/bin/env python3
"""Record what a Claude Code run spent, and report rolling spend.

The sweep runs ``claude -p ... --output-format stream-json --verbose``; every turn
of the session ends in a ``type: result`` event carrying ``total_cost_usd``,
``usage`` (input, output, cache read/write tokens), ``num_turns``, ``duration_ms``,
a per-model ``modelUsage`` breakdown, the turn's ``permission_denials`` and the
session's cumulative ``subagent_stats``. ``record`` merges those events into one
line of ``ledger/usage.jsonl`` and a small table for the run's GitHub Step Summary;
``report`` prints the rolling 7/30-day view; the gate reads ``weekly_spend()`` for
the budget guard.

``record`` also keeps, from the rest of the stream (issue #20): the ``system/init``
line (``model_resolved``, ``claude_code_version``), every ``rate_limit_event``
(``allowance``, ``delta_allowance`` and the verbatim ``rate_limit_events_raw``), and
assistant messages carrying an ``error``. ``conclusion`` is ``usage_limit`` when the
subscription refused the session, else ``error`` when the result says ``is_error``,
else the result's ``subtype``: before, a refused session was recorded as a one-turn
``success``. With ``--config`` it writes ``config``, the run's settings from an
explicit allowlist of environment variables (``CONFIG_ENV``), never an environment
dump.

Why the stream and not ``--output-format json``: a subagent runs in the background,
so the main agent's turn ends while it works and a second turn starts when it
reports. ``json`` prints only the last turn's result and silently drops the
earlier turns' cost and denials (checked with CLI 2.1.303 on 2026-10-19).

Two honest limitations:

- ``total_cost_usd`` is the **API-equivalent** price. On a subscription token it
  is not billed; it is the best available proxy for how much allowance a run used.
- Remaining subscription allowance is not reported to the gate directly:
  ``scripts/allowance.py`` estimates it from these records (spend, and the CLI's
  rate-limit readings once they are recorded), next to the weekly budget the
  maintainer sets.

Parsing is defensive by design: a missing or truncated file (a run killed by its
timeout) records ``parse_failed: true`` and zero cost, and never fails the job.

Examples
--------
    uv run scripts/record_usage.py record --result claude.jsonl --job sweep \\
        --slug 2026-10-19-mc46101-x --run-id 123 --summary >> "$GITHUB_STEP_SUMMARY"
    uv run scripts/record_usage.py report
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import log_forecast
import search_budget
from _common import REPO, ledger_records
from search_budget import read_state

USAGE = REPO / "ledger" / "usage.jsonl"


def _num(value: Any) -> float:
    return float(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else 0.0


def _denied(result: dict[str, Any]) -> list[str]:
    """Name each denied tool call: ``Bash:<program>`` for shell commands, else the tool.

    Only the program name is kept, never the arguments: this line is committed, and a
    denied command built by an injected prompt could carry a secret it had read.
    """
    names = []
    for d in result.get("permission_denials") or []:
        tool = str((d or {}).get("tool_name") or "?")
        command = str(((d or {}).get("tool_input") or {}).get("command") or "")
        program = re.match(r"[\w./-]{1,40}", command.strip())
        names.append(f"{tool}:{program.group(0)}" if tool == "Bash" and program else tool)
    return names


def _lines(text: str) -> list[Any]:
    """Every JSON value in ``claude -p`` output: one object, an array, or JSON Lines."""
    text = text.strip()
    if not text:
        return []
    try:
        doc = json.loads(text)
        return doc if isinstance(doc, list) else [doc]
    except json.JSONDecodeError:
        out = []
        for line in text.splitlines():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return out


def parse_stream(text: str) -> dict[str, Any]:
    """Everything ``record`` keeps from a session's output, in stream order.

    Returns
    -------
    dict
        ``result``: the per-turn ``result`` events merged (``merge_results``), or None;
        ``results``: those events unmerged; ``init``: the ``system/init`` event or None;
        ``rate_limits``: every ``rate_limit_event``'s ``rate_limit_info``;
        ``assistant_errors``: ``(error, text)`` of every assistant message that carries
        an ``error`` (a refused or failed API call; its text is the CLI's error
        message, never tool content).
    """
    out: dict[str, Any] = {
        "result": None, "results": [], "init": None, "rate_limits": [], "assistant_errors": [],
    }
    for ev in _lines(text):
        if not isinstance(ev, dict):
            continue
        kind = ev.get("type")
        if kind == "result":
            out["results"].append(ev)
        elif kind == "system" and ev.get("subtype") == "init" and out["init"] is None:
            out["init"] = ev
        elif kind == "rate_limit_event" and isinstance(ev.get("rate_limit_info"), dict):
            out["rate_limits"].append(ev["rate_limit_info"])
        elif kind == "assistant" and ev.get("error"):
            content = (ev.get("message") or {}).get("content") or []
            words = " ".join(
                str(b.get("text") or "") for b in content
                if isinstance(b, dict) and b.get("type") == "text"
            )
            out["assistant_errors"].append((str(ev["error"]), words))
    if out["results"]:
        out["result"] = merge_results(out["results"])
    return out


def parse_result(text: str) -> dict[str, Any] | None:
    """The session's ``result`` from ``claude -p`` output, or None.

    Accepts a single object, a JSON array of messages, or JSON Lines (stream
    output). Several ``type: result`` records -- one per turn -- are merged into
    one (``merge_results``).
    """
    return parse_stream(text)["result"]


# ------------------------------------------------------------- allowance telemetry
def utilization_pct(value: Any) -> float | None:
    """A rate-limit ``utilization`` in percent.

    The CLI reports a fraction (Claude Code 2.1.110, the last release shipped as
    JavaScript, checked 2026-11-08: it prints ``Math.floor(utilization * 100)`` %), the
    SDK's usage probe a percentage; so a value up to 1 is read as a fraction. The CLI
    sends a reading only at its warning thresholds (5 h: 90 %; 7 d: 25, 50, 75 %),
    which keeps a percentage reading above 1 in practice.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)) or math.isnan(value):
        return None
    if value < 0:
        return None
    return round(float(value) * 100, 2) if value <= 1 else round(float(value), 2)


def parse_instant(value: Any) -> dt.datetime | None:
    """A UTC instant from Unix seconds (the CLI's ``resetsAt``), milliseconds or ISO-8601."""
    if isinstance(value, (int, float)) and not isinstance(value, bool) and not math.isnan(value):
        # Milliseconds are 1000x larger; no Unix-seconds reset lies beyond the year 5000.
        try:
            return dt.datetime.fromtimestamp(value / 1000 if value > 1e11 else value, dt.UTC)
        except (OverflowError, OSError, ValueError):
            return None
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        out = dt.datetime.fromisoformat(value.strip())
    except ValueError:
        return None
    return out if out.tzinfo else out.replace(tzinfo=dt.UTC)


def _iso(value: Any) -> str | None:
    when = parse_instant(value)
    return when.astimezone(dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ") if when else None


def refuses(info: dict[str, Any]) -> bool:
    """Whether a ``rate_limit_info`` refused the session.

    ``rejected`` while extra usage is in use (``isUsingOverage``) is not a refusal: the
    calls go on, billed as overage.
    """
    return info.get("status") == "rejected" and not info.get("isUsingOverage")


def allowance_summary(events: list[dict[str, Any]]) -> dict[str, Any] | None:
    """The ``allowance`` field of a usage record from the session's rate-limit events.

    One event names one window (``rateLimitType``); the CLI emits one whenever the
    rate-limit state changes. Per window: the ``first`` and ``last`` reading in percent
    (None where no event carried one) and the newest ``resets_at``. ``rejected_window``
    and ``rejected_until`` name the window that refused the session and its reset.
    """
    if not events:
        return None
    windows: dict[str, dict[str, Any]] = {}
    for ev in events:
        name = ev.get("rateLimitType")
        if not isinstance(name, str):
            continue
        w = windows.setdefault(name, {"first": None, "last": None, "resets_at": None})
        reading = utilization_pct(ev.get("utilization"))
        if reading is not None:
            w["first"] = reading if w["first"] is None else w["first"]
            w["last"] = reading
        w["resets_at"] = _iso(ev.get("resetsAt")) or w["resets_at"]
    enabled = None
    for ev in events:
        if isinstance(ev.get("overageEnabled"), bool):
            enabled = ev["overageEnabled"]
        elif ev.get("overageStatus") in ("allowed", "allowed_warning", "rejected"):
            enabled = ev["overageStatus"] != "rejected"
    refused = [ev for ev in events if refuses(ev)]
    out: dict[str, Any] = {
        "events": len(events),
        "status": events[-1].get("status"),
        "rejected": bool(refused),
        "windows": windows,
        "overage": {
            "enabled": enabled,
            "in_use": any(bool(ev.get("isUsingOverage") or ev.get("overageInUse"))
                          for ev in events),
        },
    }
    if refused:
        out["rejected_window"] = refused[-1].get("rateLimitType")
        out["rejected_until"] = _iso(refused[-1].get("resetsAt"))
    return out


# Anything token-shaped, before an error message is committed: an API error can echo a
# header, and the repository may be public.
_SECRET_SHAPES = re.compile(
    r"(?i)sk-ant-[\w-]+|bearer\s+\S+|token\s+[\w.-]{16,}|[A-Za-z0-9_\-]{40,}"
)
_SECRET_ENVS = ("CLAUDE_CODE_OAUTH_TOKEN", "ANTHROPIC_API_KEY", "METACULUS_API_KEY",
                "METACULUS_TOKEN", "GITHUB_TOKEN", "GH_TOKEN")


def scrub(text: str, limit: int = 200) -> str:
    """``text`` cut to ``limit`` characters with secrets and token shapes removed."""
    out = str(text)
    for name in _SECRET_ENVS:
        secret = os.environ.get(name, "").strip()
        if len(secret) >= 8:
            out = out.replace(secret, "[REDACTED]")
    out = _SECRET_SHAPES.sub("[REDACTED]", out)
    return " ".join(out.split())[:limit]


def _errors(stream: dict[str, Any]) -> list[str]:
    """Error messages of the session: result ``errors``, a failed turn's text, API errors."""
    found: list[str] = []
    for r in stream.get("results") or []:
        found += [str(e) for e in r.get("errors") or [] if e]
        if r.get("is_error") and r.get("result"):
            found.append(str(r["result"]))
    found += [f"{code}: {text}" if text else code
              for code, text in stream.get("assistant_errors") or []]
    out: list[str] = []
    for e in (scrub(e) for e in found):
        if e and e not in out:
            out.append(e)
    return out[:10]


def stream_fields(stream: dict[str, Any] | None) -> dict[str, Any]:
    """The usage-record fields from the stream beyond the result: model, CLI, allowance."""
    if not stream:
        return {}
    init = stream.get("init") or {}
    events = stream.get("rate_limits") or []
    allowance = allowance_summary(events)
    out: dict[str, Any] = {
        "model_resolved": init.get("model"),
        "claude_code_version": init.get("claude_code_version"),
    }
    if allowance:
        out["allowance"] = allowance
        out["delta_allowance"] = {
            name: round(w["last"] - w["first"], 2)
            for name, w in allowance["windows"].items()
            if w["first"] is not None and w["last"] is not None
        }
        # Verbatim until the events' shape is known from real sweeps (issue #20); they
        # carry rate-limit state only, no content and no credentials.
        out["rate_limit_events_raw"] = events[-50:]
    result = stream.get("result") or {}
    if result.get("terminal_reason"):
        out["terminal_reason"] = result["terminal_reason"]
    errors = _errors(stream)
    if errors:
        out["errors"] = errors
    return {k: v for k, v in out.items() if v is not None}


def conclusion(result: dict[str, Any] | None, stream: dict[str, Any] | None,
               exit_code: int | None) -> str:
    """``usage_limit`` before ``error`` before the result's ``subtype``.

    A refused session ends in a one-turn ``result`` whose ``subtype`` is ``success``;
    before issue #20 it was recorded as one. The refusal shows in an assistant message
    with ``error: "rate_limit"`` or a ``rejected`` rate-limit event.
    """
    stream = stream or {}
    if any(code == "rate_limit" for code, _ in stream.get("assistant_errors") or []) or any(
        refuses(ev) for ev in stream.get("rate_limits") or []
    ):
        return "usage_limit"
    if result is None:
        return "timeout" if exit_code in (124, 137, 143) else "no_result"
    if result.get("is_error"):
        return "error"
    return result.get("subtype") or "success"


def _sum_numbers(dicts: list[dict[str, Any]]) -> dict[str, Any]:
    """Key-wise sum of the numeric fields of ``dicts``, recursing into sub-dicts.

    Non-numeric fields keep the last value seen.
    """
    out: dict[str, Any] = {}
    for d in dicts:
        for key, value in d.items():
            if isinstance(value, dict):
                out[key] = _sum_numbers([out.get(key) or {}, value])
            elif isinstance(value, (int, float)) and not isinstance(value, bool):
                out[key] = _num(out.get(key)) + value
            else:
                out[key] = value
    return out


def merge_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    """One result for the whole session from its per-turn ``result`` events.

    Cost, tokens, turns, duration and per-model usage are per turn, so they are
    summed; ``permission_denials`` are per turn, so they are concatenated;
    ``subagent_stats`` and ``subtype`` are the session's state, so the last turn's
    value stands (verified 2026-10-19: a denial appears only in the turn that hit
    it, while ``subagent_stats.spawned`` repeats in every turn).
    """
    if len(results) == 1:
        return results[0]
    merged = dict(results[-1])
    for key in ("total_cost_usd", "duration_ms", "num_turns"):
        merged[key] = sum(_num(r.get(key)) for r in results)
    merged["usage"] = _sum_numbers([r.get("usage") or {} for r in results])
    merged["modelUsage"] = _sum_numbers([r.get("modelUsage") or {} for r in results])
    merged["permission_denials"] = [
        d for r in results for d in (r.get("permission_denials") or [])
    ]
    return merged


def usage_record(
    result: dict[str, Any] | None,
    *,
    job: str,
    run_id: str | None,
    slug: str | None,
    model: str | None,
    exit_code: int | None = None,
    budget: dict[str, Any] | None = None,
    stream: dict[str, Any] | None = None,
    config: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """One ``ledger/usage.jsonl`` line from a parsed result (or its absence).

    ``budget`` is the search-budget hook's file (``scripts/search_budget.py``); its
    tool-call counts sit next to ``web_searches``, which counts billed search requests.
    None (no file: the hook did not run) records them as None, not 0. ``stream`` is
    ``parse_stream``'s output: the resolved model, the CLI version, the allowance
    telemetry and the errors come from it, and it decides a refusal. ``config`` is
    ``config_snapshot()``: what the run was configured to do.
    """
    rec: dict[str, Any] = {
        "ts": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "job": job,
        "run_id": run_id,
        "slug": slug,
        "model": model,
        **({"config": config} if config else {}),
        **stream_fields(stream),
        **budget_fields(budget),
    }
    if result is None:
        return {
            **rec,
            "conclusion": conclusion(None, stream, exit_code),
            "parse_failed": True,
            "cost_usd_equiv": 0.0,
        }
    usage = result.get("usage") or {}
    model_usage = [m or {} for m in (result.get("modelUsage") or {}).values()]
    by_model = {
        name: round(_num((m or {}).get("costUSD")), 4)
        for name, m in (result.get("modelUsage") or {}).items()
    }
    # The CLI's WebSearch tool runs its own model call, so its searches show up in
    # modelUsage and not in the top-level server_tool_use; take whichever saw more.
    stats = result.get("subagent_stats") or {}
    web_searches = max(
        sum(_num(m.get("webSearchRequests")) for m in model_usage),
        _num((usage.get("server_tool_use") or {}).get("web_search_requests")),
    )
    return {
        **rec,
        "conclusion": conclusion(result, stream, exit_code),
        "parse_failed": False,
        "duration_s": round(_num(result.get("duration_ms")) / 1000, 1),
        "num_turns": int(_num(result.get("num_turns"))),
        "cost_usd_equiv": round(_num(result.get("total_cost_usd")), 4),
        # `usage` covers the main agent only; modelUsage covers every agent (scouts,
        # the WebSearch tool's own model).
        "tokens": {
            "input": int(_num(usage.get("input_tokens"))),
            "output": int(_num(usage.get("output_tokens"))),
            "cache_read": int(_num(usage.get("cache_read_input_tokens"))),
            "cache_write": int(_num(usage.get("cache_creation_input_tokens"))),
        },
        "tokens_all": {
            key: int(sum(_num(m.get(field)) for m in model_usage))
            for key, field in (
                ("input", "inputTokens"),
                ("output", "outputTokens"),
                ("cache_read", "cacheReadInputTokens"),
                ("cache_write", "cacheCreationInputTokens"),
            )
        },
        "web_searches": int(web_searches),
        # Subagents (the research-scouts) spawned by the session; absent before the
        # CLI reported subagent_stats, so None there rather than a misleading 0.
        "subagents": int(_num(stats.get("spawned"))) if stats else None,
        "subagent_types": dict(stats.get("by_type") or {}) if stats else {},
        "permission_denials": len(result.get("permission_denials") or []),
        "denied": _denied(result),
        "by_model": by_model,
    }


# The run configuration a usage record carries: config key -> environment variable the
# sweep sets. An explicit allowlist, never an environment dump: the forecast job's
# environment holds the Claude token, and these lines are committed.
CONFIG_ENV = {
    "model": "MODEL",
    "effort": "EFFORT",
    "max_usd": "MAX_USD",
    "minutes": "MINUTES",
    "max_parallel": "MAX_PARALLEL",
    "max_questions_per_run": "MAX_QUESTIONS_PER_RUN",
    "weekly_budget_usd_equiv": "WEEKLY_BUDGET_USD_EQUIV",
    "claude_code_version_requested": "CLAUDE_CODE_VERSION",
    "mode": "MODE",
    "event": "GITHUB_EVENT_NAME",
    "run_attempt": "GITHUB_RUN_ATTEMPT",
    "sha": "GITHUB_SHA",
    "dry_run": "DRY_RUN",
}
# Read from the repository rather than the environment: the effective values.
CONFIG_DERIVED = ("scout_model", "min_searches", "max_web_searches")
CONFIG_KEYS = (*CONFIG_ENV, *CONFIG_DERIVED)
_CONFIG_NUMBERS = {
    "max_usd": float, "minutes": int, "max_parallel": int, "max_questions_per_run": int,
    "weekly_budget_usd_equiv": float, "run_attempt": int,
}
SCOUT_AGENT = REPO / ".claude" / "agents" / "research-scout.md"


def scout_model(path: Path = SCOUT_AGENT) -> str | None:
    """The ``model:`` of the research-scout agent's front matter, or None."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    head = text.split("---", 2)[1] if text.startswith("---") else ""
    found = re.search(r"(?m)^model:\s*([\w.:-]+)\s*$", head)
    return found.group(1) if found else None


def config_snapshot() -> dict[str, Any]:
    """The run's configuration from ``CONFIG_ENV`` and the repository (``CONFIG_KEYS``).

    Unset or empty values are None; numbers and the dry-run flag are typed; the commit
    is shortened to 7 characters. ``min_searches`` and ``max_web_searches`` are the
    effective research floor and search cap, as ``log_forecast.py`` and the search
    hook compute them from the same environment.
    """
    out: dict[str, Any] = {}
    for key, var in CONFIG_ENV.items():
        raw = os.environ.get(var, "").strip()
        value: Any = raw or None
        if value is not None and key in _CONFIG_NUMBERS:
            try:
                value = _CONFIG_NUMBERS[key](raw)
            except ValueError:
                value = None
        if key == "dry_run":
            value = raw.lower() == "true"
        if key == "sha" and value:
            value = raw[:7]
        out[key] = value
    out["scout_model"] = scout_model()
    out["min_searches"] = log_forecast.min_searches()
    out["max_web_searches"] = search_budget.caps()[0]
    return out


def budget_fields(budget: dict[str, Any] | None) -> dict[str, Any]:
    """The search-budget hook's counts for a usage record.

    ``search_budget_file`` says which case it is: ``missing`` (None: the hook never
    wrote, so it did not run), ``unreadable`` (the hook ran but its file is damaged:
    counts unknown, recorded as None rather than a misleading 0) or ``ok``.
    """
    status = (
        "missing" if budget is None else "unreadable" if budget.get("unreadable") else "ok"
    )
    ok = status == "ok"
    b = budget or {}
    by_agent = b.get("by_agent") if isinstance(b.get("by_agent"), dict) else {}
    return {
        "search_budget_file": status,
        "search_tool_calls": b.get("searches") if ok else None,
        "fetch_tool_calls": b.get("fetches") if ok else None,
        "search_calls_denied": b.get("denied") if ok else None,
        # Searches per subagent; empty with scouts spawned means the CLI sent no
        # agent_id, so the per-scout cap was not in force.
        "search_calls_by_agent": (
            {k: (v or {}).get("searches", 0) for k, v in by_agent.items()} if ok else None
        ),
        "scouts_spawned": b.get("scouts_spawned") if ok else None,
        # Equal to scouts_spawned, with none running at exit, shows the SubagentStart
        # and SubagentStop hooks fire, so log_forecast.py's wait for scouts is real.
        "subagents_started": b.get("subagents_started") if ok else None,
        "subagents_running_at_exit": len(b.get("active_agents") or {}) if ok else None,
        "search_cap": b.get("max_searches") if ok else None,
        "search_cap_per_scout": b.get("max_per_scout") if ok else None,
    }


def append(rec: dict[str, Any], path: Path = USAGE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def spend_since(since: dt.datetime, path: Path = USAGE) -> tuple[float, int, int]:
    """``(cost, runs, slugs)`` over usage records at or after ``since``."""
    cost, runs, slugs = 0.0, 0, set()
    for rec in ledger_records(path):
        try:
            ts = dt.datetime.fromisoformat(str(rec.get("ts")))
        except ValueError:
            continue
        if ts >= since:
            cost += _num(rec.get("cost_usd_equiv"))
            runs += 1
            if rec.get("slug"):
                slugs.add(rec["slug"])
    return cost, runs, len(slugs)


def weekly_spend(now: dt.datetime | None = None, path: Path = USAGE) -> float:
    """Cost-equivalent spent over the trailing seven days -- the gate's budget input."""
    now = now or dt.datetime.now(dt.UTC)
    return spend_since(now - dt.timedelta(days=7), path)[0]


def _allowance_cell(rec: dict[str, Any]) -> str:
    allowance = rec.get("allowance")
    if not allowance:
        return "- (no rate-limit event)"
    windows = allowance.get("windows") or {}

    def one(name: str) -> str:
        w = windows.get(name) or {}
        reading = "-" if w.get("last") is None else f"{w['last']:.0f} %"
        return reading + (f" (resets {w['resets_at']})" if w.get("resets_at") else "")

    status = allowance.get("status") or "-"
    return f"{one('five_hour')} / {one('seven_day')}; status {status}"


def summary_table(rec: dict[str, Any]) -> str:
    """Markdown for the GitHub Step Summary: the run's cost without opening a file."""
    tok = rec.get("tokens") or {}
    rows = [
        ("question", rec.get("slug") or "-"),
        ("model", rec.get("model") or "-"),
        (
            "model resolved / CLI",
            f"{rec.get('model_resolved') or '-'} / {rec.get('claude_code_version') or '-'}",
        ),
        ("mode / effort", " / ".join(
            str((rec.get("config") or {}).get(k) or "-") for k in ("mode", "effort")
        )),
        ("allowance (5 h / 7 d, last reading)", _allowance_cell(rec)),
        ("conclusion", rec.get("conclusion")),
        ("cost (API-equivalent)", f"${rec.get('cost_usd_equiv', 0):.2f}"),
        ("turns", rec.get("num_turns", "-")),
        ("duration", f"{rec.get('duration_s', '-')} s"),
        (
            "tokens in/out/cache-read/cache-write",
            (
                f"{tok.get('input', 0)}/{tok.get('output', 0)}/"
                f"{tok.get('cache_read', 0)}/{tok.get('cache_write', 0)}"
            ),
        ),
        ("web searches (all agents)", rec.get("web_searches", "-")),
        (
            "WebSearch / WebFetch tool calls (denied)",
            {
                "missing": "- (no budget file: the search-budget hook did not run)",
                "unreadable": "- (budget file unreadable: the hook ran, its counts are lost)",
            }.get(rec.get("search_budget_file"), "-")
            if rec.get("search_tool_calls") is None
            else f"{rec['search_tool_calls']}/{rec.get('search_cap') or 'no cap'} / "
            f"{rec.get('fetch_tool_calls')} ({rec.get('search_calls_denied')})",
        ),
        (
            "WebSearch calls per scout",
            str(rec.get("search_calls_by_agent") or "-").replace("|", "/"),
        ),
        (
            "subagents",
            "-"
            if rec.get("subagents") is None
            else f"{rec['subagents']} "
            + str(rec.get("subagent_types") or {}).replace("|", "/"),
        ),
        (
            "subagents spawned / started / running at exit (hook)",
            "-"
            if rec.get("subagents_started") is None
            else f"{rec.get('scouts_spawned')} / {rec['subagents_started']} / "
            f"{rec.get('subagents_running_at_exit')}",
        ),
        ("permission denials", rec.get("permission_denials", "-")),
        ("denied", ", ".join(rec.get("denied") or []) or "-"),
    ]
    week = weekly_spend()
    return "\n".join(
        ["### Claude usage", "", "| | |", "|---|---|"]
        + [f"| {k} | {v} |" for k, v in rows]
        + ["", f"Trailing 7-day spend: ${week:.2f}", ""]
    )


def report(now: dt.datetime | None = None) -> str:
    now = now or dt.datetime.now(dt.UTC)
    lines = [f"{'window':<8} {'runs':>5} {'questions':>9} {'cost-equiv':>11} {'per question':>13}"]
    for days in (7, 30):
        cost, runs, n = spend_since(now - dt.timedelta(days=days))
        per = f"${cost / n:.2f}" if n else "-"
        lines.append(f"{days:>2} days  {runs:>5} {n:>9} {'$' + format(cost, '.2f'):>11} {per:>13}")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("record", help="append one run to ledger/usage.jsonl")
    r.add_argument(
        "--result", type=Path, required=True, help="claude -p output (stream-json or json)"
    )
    r.add_argument("--job", required=True)
    r.add_argument("--run-id")
    r.add_argument("--slug")
    r.add_argument("--model")
    r.add_argument("--exit-code", type=int, help="the claude step's exit code")
    r.add_argument(
        "--config",
        action="store_true",
        help="record the run configuration (CONFIG_ENV variables and the repository)",
    )
    r.add_argument(
        "--search-budget",
        type=Path,
        help="the search-budget hook's file ($SEARCH_BUDGET_FILE), for tool-call counts",
    )
    r.add_argument("--summary", action="store_true", help="print a Markdown table")
    sub.add_parser("report", help="rolling 7/30-day spend")
    args = ap.parse_args()

    if args.cmd == "report":
        print(report())
        return
    try:
        text = args.result.read_text(encoding="utf-8", errors="replace")
    except OSError:
        text = ""
    stream = parse_stream(text)
    rec = usage_record(
        stream["result"],
        job=args.job,
        run_id=args.run_id,
        slug=args.slug,
        model=args.model,
        exit_code=args.exit_code,
        budget=read_state(args.search_budget) if args.search_budget else None,
        stream=stream,
        config=config_snapshot() if args.config else None,
    )
    append(rec)
    if args.summary:
        print(summary_table(rec))


if __name__ == "__main__":
    main()
