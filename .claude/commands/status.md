---
description: Triage open forecasts — what is due for review, resolving soon, or stale
argument-hint: [--act]
---

Run `uv run scripts/status.py $ARGUMENTS`.

Present the result as a short table ordered by urgency: slug, current forecast, days since last
version, days to resolution, review status, and the reason it surfaced.

Then, for the top 3, name the single most informative thing to check — usually the specific
tripwire most likely to have fired, or the next scheduled data release that resolves ambiguity.

## `--act`

If `--act` was passed, update every question whose review is overdue or whose resolution is
within 7 days — call that the **due set** — in urgency order, and finish with a
one-line-per-question digest of what moved and what did not.

How you run the due set depends on its size:

**Due set ≤ 2 — do them yourself.** Run `/update <slug>` sequentially. Fan-out costs more than
it saves at this size, and two questions in one context let you notice a shared driver.

**Due set > 2 — fan out, one subagent per question.** Each subagent owns exactly one slug from
first byte to ledger entry.

> The boundary that matters: **never split a single question across subagents.** One question,
> one agent, one probability judgement. Delegating the tripwire check to one agent and the
> integration to another is the one thing `CLAUDE.md` forbids — calibration lives in the
> integration step. Delegating a *whole* question is fine, because the agent does its own
> integration.

Before spawning, do two things yourself, in the parent:

1. **Pre-fetch the Metaculus JSON, serially.** Metaculus rate-limits by IP and a tripped limit
   blocks every subagent at once for ~2 minutes, so parallel fetches are the one thing
   guaranteed to stall the whole fan-out. For each Metaculus-sourced slug in the due set, run
   the aggregations script once and cache it:

   ```bash
   uv run .claude/skills/metaculus-aggregations/scripts/metaculus_aggregations.py <POST_ID> \
       --comments 8 --history --json > questions/<slug>/raw/metaculus-<YYYY-MM-DD>.json
   ```

   These are live numbers fetched in this session, so rule 4 is satisfied; the agent reads the
   file instead of re-fetching.
2. **Cap concurrency at 4 in flight.** Launch the next batch as slots free up.

Give every subagent the same brief, with its own slug substituted:

- Load the `forecast-update` skill and follow it end to end; read `docs/update-protocol.md`.
- Its prior is *that question's own last forecast*, not the community prediction.
- Read the pre-fetched `questions/<slug>/raw/metaculus-<date>.json`; **do not** call the
  aggregations script or any other Metaculus endpoint. Market prices, news and primary data
  series it fetches itself.
- It writes `questions/<slug>/forecast.md` (prepend the new version), `meta.yaml`, and its own
  ledger entry via `scripts/log_forecast.py`. Ledger appends are per-slug and append-only, so
  concurrent agents on different slugs do not collide — but an agent must never touch another
  slug's files.
- It must **not** run `git` (no add, no commit, no push), must **not** run
  `scripts/status.py --index`, and must **not** run `ruff`/`pytest`. Those are yours, once, at
  the end.
- "No change" is a valid, publishable result — it writes the version anyway.
- It reports back in this fixed shape, and nothing else:
  `<slug> | v<N> | <prior median/IQR> → <new median/IQR> | mode | <one clause: the driver that
  moved it, or why nothing moved> | tripwires fired: <names or none>`

Then integrate, yourself:

1. Verify rather than trust the reports: read the top version block of each `forecast.md` and
   `tail` the ledger, and confirm one new entry per due slug. An agent that failed or returned
   nothing leaves its question **not updated** — say so explicitly in the digest instead of
   letting it disappear.
2. Look across the digest for what no single agent could see: the same driver moving two
   questions, two updates drifting the same direction, a tripwire that fired in one question and
   should be added to another.
3. Run once, in the repo root: `uv run scripts/status.py --index`, then
   `uv run ruff check --fix .` and `uv run pytest -q`. Fix failures before any commit.
