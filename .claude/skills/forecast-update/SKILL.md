---
name: forecast-update
description: >-
  Revisit, revise, or resolve an existing forecast in this repository: check the tripwires from
  the previous version, re-fetch live Metaculus and market numbers, update Bayesianly from the
  previous forecast as prior, prepend a new version with a revision table to forecast.md, and
  log it to the ledger. Also covers resolution and post-mortem scoring. Use whenever the user
  says update, revisit, re-check, refresh, "any news on", "has this changed", "did it resolve",
  or invokes /update, /resolve or /status. Do not use for a brand-new question — that is
  forecast-workflow.
---

# Update workflow

Read `docs/update-protocol.md`. The previous version's tripwire list is your search plan.

## Step 1 — Load the prior

```bash
cat questions/<slug>/meta.yaml
sed -n '1,120p' questions/<slug>/forecast.md      # header + newest version
```

Note: prior median/IQR, version number, date, thesis, tripwires, and what the CP was then.

## Step 2 — Decide mode

`Update` (incremental) or `Re-analysis` (de novo). Go de-novo when the market contradicts you
by > 10 pp without explanation, when > 3 months or > 1/3 of remaining time has passed, when the
question's structure changed, or when your last two updates drifted the same direction.
State the mode in the version header.

## Step 3 — Tripwire check first

Search for each tripwire by name and date. Record fired / not fired / partial in the tripwire
table. **Then** search generally for developments since the last version date.

## Step 4 — Re-fetch live numbers

```bash
uv run .claude/skills/metaculus-aggregations/scripts/metaculus_aggregations.py <POST_ID> \
    --comments 8 --history --json > questions/<slug>/raw/metaculus-<YYYY-MM-DD>.json
```

Plus market prices and the underlying data series. Compare against the snapshot from last time —
the *movement* is the signal, not the level.

## Step 5 — Update

Prior = your last forecast. For each driver state a direction and an effect in percentage points
(or a likelihood ratio). Remember that elapsed quiet time is itself evidence for
event-requiring questions: recompute the remaining-window hazard rate, do not just leave the
number where it was.

**No change is a valid outcome.** Write the version anyway, with the reason ("all four tripwires
unfired; CP moved 1 pp; hazard-rate decay offset by X").

## Step 6 — Write

Prepend `## v<N> — Update|Re-analysis — <date>` to `forecast.md`, opening with the revision
table (one driver per row, prior in the first row, new forecast in the last) and the tripwire
check table. Sections that did not change: `unchanged from v<N-1>`. Rewrite the header block.
Update `meta.yaml`: `current`, `next_review`, revised `tripwires`.

```bash
uv run scripts/log_forecast.py add <slug> --median ... --lower ... --upper ... \
    --cp ... --pro ... --gold ... --thesis "..." --next-review YYYY-MM-DD
uv run scripts/status.py --index
```

**Before committing**, run both and fix any failures — this is a repo-edit workflow, per
`CLAUDE.md`'s Git section:

```bash
uv run ruff check --fix .
uv run pytest -q
```

## Resolution and post-mortem

```bash
uv run scripts/log_forecast.py resolve <slug> --outcome yes|no|<value>
uv run scripts/calibration.py
```

Append a `## Resolution — <date>` section to `forecast.md`, then re-run the lint/test
gate above before committing.

- What happened, via which resolution source, on which date.
- Per-version Brier score (binary) or absolute/quantile error (numeric), and the same for the
  community prediction at the same timestamps — did you beat the crowd?
- **The tripwire that should have existed and did not.** Mandatory. This is the only part of a
  post-mortem that improves future forecasts.
- One line for the calibration record: over- or under-confident, and by how much.

Set `status: resolved` in `meta.yaml`.

## Triage

`uv run scripts/status.py` lists open questions by urgency (review overdue, resolution imminent,
tripwire-heavy, stale). Use it at the start of any "what should I look at" session.

When acting on the triage (`/status --act`) and **more than 2** questions are due, fan out: one
subagent per question, each running this skill end to end for a single slug, with the Metaculus
JSON pre-fetched serially by the parent (parallel fetches trip the per-IP rate limit). Never
split one question across agents — the integration step is where calibration lives. See
`.claude/commands/status.md` for the full brief.
