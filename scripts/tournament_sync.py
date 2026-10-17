#!/usr/bin/env python3
"""Daily reconcile of tournament questions against Metaculus. Deterministic: no model.

For every tournament question this repository holds that is not yet resolved or
dropped, it asks the API what happened since and records it:

- **Missed window**: closed with nothing submitted -> ``missed_window: true``,
  ``status: dropped``. The count of these is the measurement of whether the sweep
  cadence and budget are right.
- **Missing comment**: submitted but the rationale comment failed -> one retry.
  Comments are required for prize eligibility.
- **Closed**: submitted and closed, awaiting resolution -> ``status: closed``.
- **Resolved**: the outcome goes to the ledger (``log_forecast.py resolve``), the
  bot's official score (spot peer score, which cannot be recomputed locally since
  it is relative to the other bots) to ``tournament.official_score``, and a short
  ``## Resolution`` note to ``forecast.md``. Annulled/ambiguous -> ``dropped``.
- **Lost record**: Metaculus holds a bot forecast this repo has no record of -> a
  warning only; nothing is invented to fill the gap.

Then ``INDEX.md`` is regenerated -- only here, never in the sweep, so concurrent
sweep jobs never fight over it.

Examples
--------
    uv run scripts/tournament_sync.py
    uv run scripts/tournament_sync.py --dry-run
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import log_forecast
import metaculus_api as mapi
from _common import (
    QUESTIONS,
    all_questions,
    fmt_forecast,
    load_meta,
    save_meta,
    set_forecast_header,
    today,
)
from status import write_index
from submit_metaculus import (
    SubmitError,
    comment_text,
    mark_missed_window,
    select_question,
    subquestion_id,
)

VOID_RESOLUTIONS = {"annulled", "ambiguous"}
# Preference order among the score names Metaculus may report for the bot.
SCORE_KEYS = ("spot_peer_score", "peer_score")


def official_score(question: dict[str, Any]) -> float | None:
    """The bot's tournament score on ``question``, if Metaculus reports one."""
    data = (question.get("my_forecasts") or {}).get("score_data") or {}
    for key in SCORE_KEYS:
        value = data.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value)
    return None


def _outcome_arg(question: dict[str, Any]) -> str:
    """Metaculus' ``resolution`` as the string ``log_forecast.py resolve`` takes."""
    res = question.get("resolution")
    if question.get("type") == "date" and isinstance(res, str):
        return res[:10]
    return str(res)


def record_resolution(slug: str, question: dict[str, Any]) -> str:
    """Log a resolved question; returns a one-line description."""
    meta = load_meta(slug)
    res = question.get("resolution")
    if str(res).lower() in VOID_RESOLUTIONS:
        meta["status"] = "dropped"
        meta["next_review"] = None
        save_meta(slug, meta)
        set_forecast_header(slug, "Status", "dropped")
        return f"{res} -> dropped"
    log_forecast.cmd_resolve(
        argparse.Namespace(
            slug=slug,
            outcome=_outcome_arg(question),
            date=today(),
            source=f"Metaculus API: question {question.get('id')} resolution",
        )
    )
    meta = load_meta(slug)
    score = official_score(question)
    meta["tournament"]["official_score"] = score
    save_meta(slug, meta)
    set_forecast_header(slug, "Status", "resolved")
    note = (
        f"\n\n## Resolution — {today()}\n\n"
        f"Resolved **{res}** (synced from the Metaculus API). The bot's forecast was "
        f"{fmt_forecast(meta)}. Official spot peer score: "
        f"{'not yet reported' if score is None else f'{score:+.2f}'}.\n"
    )
    path = QUESTIONS / slug / "forecast.md"
    path.write_text(path.read_text(encoding="utf-8").rstrip("\n") + note, encoding="utf-8")
    return f"resolved {res} (score {score})"


def sync_one(slug: str, meta: dict[str, Any], dry_run: bool) -> str | None:
    """Reconcile one question; returns what changed, or None."""
    tour = meta["tournament"]
    post = mapi.get_post(int(meta["post_id"]), stage="sync")
    q = select_question(post, subquestion_id(meta.get("url")))
    status = q.get("status") or post.get("status")
    if not tour.get("submitted"):
        if mapi.live_values(q) is not None:
            return "WARNING: Metaculus holds a bot forecast with no local record"
        if not mapi.is_open(post, q):
            if not dry_run:
                mark_missed_window(slug)
            return "missed window -> dropped"
        return None
    done = []
    if not tour.get("comment_posted"):
        if dry_run:
            done.append("would retry the comment")
        else:
            try:
                code = mapi.post_comment(int(meta["post_id"]), comment_text(slug))
                log_forecast.record_late_comment(slug, code)
                done.append("comment posted")
            except (mapi.MetaculusError, SubmitError) as exc:
                done.append(f"comment retry failed: {exc}")
    if status == "resolved" and q.get("resolution") is not None:
        done.append("would record resolution" if dry_run else record_resolution(slug, q))
    elif status in ("closed", "resolved") and meta.get("status") == "open":
        if not dry_run:
            meta = load_meta(slug)
            meta["status"] = "closed"
            save_meta(slug, meta)
            set_forecast_header(slug, "Status", "closed")
        done.append("closed")
    return "; ".join(done) or None


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--dry-run", action="store_true", help="report, change nothing")
    args = ap.parse_args()

    changes, failures = 0, 0
    for slug, meta in all_questions():
        if not meta.get("tournament") or meta.get("status") in ("resolved", "dropped"):
            continue
        if not meta.get("post_id"):
            continue
        try:
            what = sync_one(slug, meta, args.dry_run)
        except mapi.MetaculusAuthError as exc:
            sys.exit(f"! {exc}")
        except (mapi.MetaculusError, SubmitError, SystemExit, ValueError) as exc:
            print(f"! {slug}: {exc}")
            failures += 1
            continue
        if what:
            changes += 1
            print(f"{slug}: {what}")
        time.sleep(0.5)
    if not args.dry_run:
        write_index()
    print(f"\n{changes} question(s) changed, {failures} failed")
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
