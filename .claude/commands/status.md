---
description: Triage open forecasts — what is due for review, resolving soon, or stale
argument-hint: [--act]
---

Run `uv run scripts/status.py $ARGUMENTS`.

Present the result as a short table ordered by urgency: slug, current forecast, days since last
version, days to resolution, review status, and the reason it surfaced.

Then, for the top 3, name the single most informative thing to check — usually the specific
tripwire most likely to have fired, or the next scheduled data release that resolves ambiguity.

If `--act` was passed, actually run `/update` on every question whose review is overdue or whose
resolution is within 7 days, in urgency order, and finish with a one-line-per-question digest of
what moved and what did not.
