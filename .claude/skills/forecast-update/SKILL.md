---
name: forecast-update
description: >-
  Revisit, revise, or resolve an existing forecast in this repository: check the tripwires from
  the previous version, re-fetch live market and source numbers, update Bayesianly from the
  previous forecast as prior, prepend a new version with a revision table to forecast.md, and
  log it to the ledger. Also covers resolution and post-mortem scoring. Use whenever the user
  says update, revisit, re-check, refresh, "any news on", "has this changed", "did it resolve",
  or invokes /update, /resolve or /status. Do not use for a brand-new question — that is
  forecast-workflow — and never for a one-shot tournament question, which is never revisited.
---

# Update workflow

**Hard stop first.** If `meta.yaml` has `tournament.mode: one_shot`, refuse: a bot-tournament
question takes exactly one forecast, and a second submission is a rules violation. Say so and
stop. (Its resolution is recorded by the daily `tournament-sync`, not here.) An operator who
wants a private re-analysis for the calibration record can have one in chat, but it is never
logged and never submitted.

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
uv run scripts/metaculus_api.py post <post_id> > questions/<slug>/raw/metaculus-question-<YYYY-MM-DD>.json
```

That refreshes the question text (criteria edits happen; staff clarifications too). The
community prediction is not available to the bot token. Then market prices and the underlying
data series. Compare against the snapshot from last time —
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

The version's closing summary block, and your chat reply, open with the clickable
`**Question**: [title](url)` line (from `meta.yaml`), then Date / Forecast / Thesis — see
`docs/output-format.md`.

```bash
uv run scripts/log_forecast.py add <slug> --median ... --lower ... --upper ... \
    --cp ... --pro ... --gold ... --thesis "..." --next-review YYYY-MM-DD \
    --distribution '...'   # required for multiple choice; see below
uv run scripts/status.py --index
```

`--distribution` records this version's full forecast, in the same form as
`forecast-workflow` step 9: the option vector for multiple choice (**required**, exact Metaculus
labels); `percentiles` or `pmf` for numeric/date/discrete when you have more than quartiles.
Write the **new** version's values, never the prior's. Versions logged before the field existed
lack it, and that is fine: the ledger is append-only and they stay as they are.

**Before committing**, run both and fix any failures — this is a repo-edit workflow, per
`CLAUDE.md`'s Git section:

```bash
uv run ruff check --fix .
uv run pytest -q
```

## Resolution and post-mortem

```bash
uv run scripts/log_forecast.py resolve <slug> --outcome yes|no|<value>|"<exact option label>"
uv run scripts/calibration.py
```

Append a `## Resolution — <date>` section to `forecast.md`, then re-run the lint/test
gate above before committing.

- What happened, via which resolution source, on which date.
- Per-version Brier score (binary), multi-class Brier + log score (multiple choice), or
  absolute/quantile error (numeric), and the same for the
  community prediction at the same timestamps — did you beat the crowd?
- **The tripwire that should have existed and did not.** Mandatory. This is the only part of a
  post-mortem that improves future forecasts.
- One line for the calibration record: over- or under-confident, and by how much.

`log_forecast.py resolve` already sets `status: resolved`, the `resolution` block and
`next_review: null` in `meta.yaml`; rewrite the `forecast.md` header to match.

## Triage

`uv run scripts/status.py` lists open questions by urgency (review overdue, resolution imminent,
last version stale). One-shot tournament questions never need review. Use it at the start of any "what should I look at" session.

When acting on the triage (`/status --act`) and **more than 2** questions are due, fan out: one
subagent per question, each running this skill end to end for a single slug, with the Metaculus
question text pre-fetched serially by the parent (the API rate-limits per IP). Never
split one question across agents — the integration step is where calibration lives. The one
exception runs the other way: two or three questions that share a resolution source or evidence
base (the cage-free/broiler commitment pair, say) go to *one* agent, so the research happens once
and the forecasts stay mutually consistent. See `.claude/commands/status.md` for the full brief.
