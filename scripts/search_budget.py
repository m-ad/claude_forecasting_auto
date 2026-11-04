#!/usr/bin/env python3
"""``PreToolUse`` hook: count web tool calls and cap ``WebSearch`` per session.

Registered in ``.claude/settings.ci.json`` for ``WebSearch|WebFetch``, so it runs
before every such call of the forecaster session and of its research-scouts. One
session once billed 234 searches (issue #19): five scouts searched in parallel and
nothing stopped them. The cap turns that into a refusal the model can read and act on.

Behaviour, per call:

- ``WebFetch`` is counted, never refused. Fetching is how a forecast gets its numbers
  from the source rather than a snippet; the cap is on finding pages, not reading them.
- ``WebSearch`` is counted against ``$MAX_WEB_SEARCHES`` (unset or empty:
  ``DEFAULT_MAX_SEARCHES``) for the whole session, and -- when the hook input names the
  calling subagent (``agent_id``) -- against ``$MAX_WEB_SEARCHES_PER_SCOUT`` (unset or
  empty: ``DEFAULT_MAX_PER_SCOUT``) for that subagent, so one scout cannot spend the
  budget the others and the main agent need. The CLI puts ``agent_id`` into every hook
  input from a subagent since 2.1.69 (its changelog; the 2.1.317 binary checked
  2026-11-03). On an older CLI only the session cap binds. ``no_agent_id`` in the
  budget file counts the searches that came without one (the main agent's, and every
  call on such a CLI); an empty ``by_agent`` in a session that spawned scouts means the
  per-scout cap was not in force.
- An agent's first search is allowed with a note stating both caps, so the model
  learns the budget from the hook rather than from numbers copied into its
  instructions. From ``NUDGE_SHARE`` of a cap the call is allowed with a countdown
  (``additionalContext``); at the cap it is refused with a reason that tells the model
  to stop searching and log. ``0`` disables a cap.

These defaults are the only place the numbers live: the sweep passes the repository
variables through unset, and ``docs/configuration.md`` names the constants (a test
keeps its Default column in step with them).

State lives in ``$SEARCH_BUDGET_FILE``, a JSON object updated under ``flock``
because scouts call in parallel. ``log_forecast.py`` reads it to waive the research
floor once the session cap is used (a cap below the floor must never trap a session),
and ``record_usage.py`` copies its counts into ``ledger/usage.jsonl``.

The hook fails open: without ``$SEARCH_BUDGET_FILE``, or on any error, it allows the
call and says why on stderr. It is a cost control, not a security boundary -- the
session's ``uv run python`` can rewrite the file. Stdlib only: it runs as
``python3 -I``, outside the project's virtualenv.

The counts are of **tool calls**. Billing counts server-side search requests, and one
``WebSearch`` call can issue several (``web_searches`` in the usage record), so the
ratio of the two is what to tune the cap with.
"""

from __future__ import annotations

import datetime as dt
import fcntl
import json
import math
import os
import sys
from pathlib import Path
from typing import Any

DEFAULT_MAX_SEARCHES = 50
# Sized so that five scouts (the usual spawn) leave the main agent a fifth of
# DEFAULT_MAX_SEARCHES for the resolution source and its own disconfirmation search; a
# scout's brief is one narrow stream.
DEFAULT_MAX_PER_SCOUT = 8
NUDGE_SHARE = 0.8


def _cap(name: str, default: int) -> int:
    """A non-negative integer from the environment; ``default`` if unset or malformed."""
    try:
        value = int(os.environ.get(name, "").strip())
    except ValueError:
        return default
    return value if value >= 0 else default


def caps() -> tuple[int, int]:
    """``(session cap, per-scout cap)`` from the environment; 0 means no cap."""
    return (
        _cap("MAX_WEB_SEARCHES", DEFAULT_MAX_SEARCHES),
        _cap("MAX_WEB_SEARCHES_PER_SCOUT", DEFAULT_MAX_PER_SCOUT),
    )


def budget_path() -> Path | None:
    """The budget file named by ``$SEARCH_BUDGET_FILE``, or None when unset."""
    raw = os.environ.get("SEARCH_BUDGET_FILE", "").strip()
    return Path(raw) if raw else None


def read_state(path: Path | None = None) -> dict[str, Any] | None:
    """The budget file's content, or None if there is none or it is unreadable."""
    path = path or budget_path()
    if path is None:
        return None
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return state if isinstance(state, dict) else None


def session_cap_used(state: dict[str, Any] | None) -> bool:
    """Whether the session-wide search cap has been reached."""
    if not state:
        return False
    cap = state.get("max_searches")
    return isinstance(cap, int) and cap > 0 and int(state.get("searches") or 0) >= cap


def _empty_state() -> dict[str, Any]:
    return {
        "searches": 0,
        "fetches": 0,
        "denied": 0,
        "no_agent_id": 0,
        "by_agent": {},
        "cap_reached_at": None,
    }


def _nudge(used: int, cap: int) -> bool:
    return cap > 0 and used >= math.ceil(NUDGE_SHARE * cap)


def decide(
    state: dict[str, Any],
    tool: str,
    agent_id: str | None,
    max_searches: int,
    max_per_scout: int,
    now: str,
) -> dict[str, Any] | None:
    """Update ``state`` in place for one call; return the hook output, None to allow.

    Parameters
    ----------
    state
        The budget file's content (``_empty_state`` shape); mutated.
    tool
        ``WebSearch`` or ``WebFetch``; anything else passes uncounted.
    agent_id
        The calling subagent, or None for the main agent (or a CLI that does not say).
    max_searches, max_per_scout
        The caps; 0 disables one.
    now
        Timestamp recorded when the session cap is first reached.

    Returns
    -------
    dict or None
        ``hookSpecificOutput`` JSON for the CLI: a refusal, or an allowed call with a
        nudge. None means allow silently.
    """
    for key, value in _empty_state().items():
        state.setdefault(key, value)
    state["max_searches"], state["max_per_scout"] = max_searches, max_per_scout
    agent = None
    if agent_id:
        agent = state["by_agent"].setdefault(agent_id, {"searches": 0, "fetches": 0})

    if tool == "WebFetch":
        state["fetches"] += 1
        if agent is not None:
            agent["fetches"] += 1
        return None
    if tool != "WebSearch":
        return None

    if max_searches and state["searches"] >= max_searches:
        state["denied"] += 1
        return _deny(
            f"Search budget used ({state['searches']}/{max_searches} WebSearch calls this "
            "session). Stop searching. WebFetch still works for a page you already found "
            "whose exact figure the forecast rests on; otherwise integrate what you have, "
            "write forecast.md and log the forecast now -- the research floor is waived. "
            "Mark planned searches you did not run as skipped in the research log."
            if agent is None
            else f"Session search budget used ({state['searches']}/{max_searches}). Stop "
            "searching and return your digest now with what you have."
        )
    if agent is not None and max_per_scout and agent["searches"] >= max_per_scout:
        state["denied"] += 1
        return _deny(
            f"Your search budget is used ({agent['searches']}/{max_per_scout} WebSearch "
            "calls for this scout). Stop searching: fetch at most the pages you already "
            "found that your brief needs, then return your digest now."
        )

    state["searches"] += 1
    if agent is not None:
        agent["searches"] += 1
    else:
        state["no_agent_id"] += 1
    if max_searches and state["searches"] >= max_searches and not state["cap_reached_at"]:
        state["cap_reached_at"] = now

    notes = []
    first = agent["searches"] == 1 if agent is not None else state["no_agent_id"] == 1
    if first:
        notes.append(
            "Search budget: "
            + (f"{max_searches} WebSearch calls this session" if max_searches else "no session cap")
            + (
                f", {max_per_scout} per scout" if max_per_scout else ", no per-scout cap"
            )
            + "; WebFetch is not capped."
        )
    if _nudge(state["searches"], max_searches):
        notes.append(
            f"{state['searches']}/{max_searches} WebSearch calls of the session budget used, "
            f"{max_searches - state['searches']} left: spend them on the resolution source, "
            "markets and the disconfirmation search."
        )
    if agent is not None and _nudge(agent["searches"], max_per_scout):
        notes.append(
            f"This scout has used {agent['searches']}/{max_per_scout} of its WebSearch calls."
        )
    if not notes:
        return None
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": " ".join(notes),
        }
    }


def _deny(reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


def run(hook_input: dict[str, Any], path: Path) -> dict[str, Any] | None:
    """Apply one hook call to the budget file at ``path`` under an exclusive lock."""
    max_searches, max_per_scout = caps()
    agent_id = hook_input.get("agent_id") or None
    now = dt.datetime.now(dt.UTC).isoformat(timespec="seconds")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_RDWR | os.O_CREAT, 0o644)
    with os.fdopen(fd, "r+", encoding="utf-8") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        text = fh.read()
        try:
            state = json.loads(text) if text.strip() else _empty_state()
        except ValueError:
            # A torn or hand-edited file: start over rather than block every call.
            state = _empty_state()
        if not isinstance(state, dict):
            state = _empty_state()
        out = decide(
            state, str(hook_input.get("tool_name") or ""), agent_id,
            max_searches, max_per_scout, now,
        )
        fh.seek(0)
        fh.truncate()
        fh.write(json.dumps(state, sort_keys=True))
        fh.flush()
    return out


def main() -> None:
    path = budget_path()
    if path is None:
        print("search_budget: $SEARCH_BUDGET_FILE unset, not counting", file=sys.stderr)
        return
    try:
        hook_input = json.load(sys.stdin)
        out = run(hook_input if isinstance(hook_input, dict) else {}, path)
    except Exception as exc:  # noqa: BLE001 -- fail open: a broken counter must not stop research
        print(f"search_budget: failing open: {exc!r}", file=sys.stderr)
        return
    if out is not None:
        print(json.dumps(out))


if __name__ == "__main__":
    main()
