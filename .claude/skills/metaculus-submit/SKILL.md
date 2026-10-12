---
name: metaculus-submit
description: >-
  Submit the repository's current forecasts to Metaculus as the bot account (METACULUS_API_KEY),
  for one or more slugs or for all open Metaculus questions (--all), optionally limited to one
  tournament. Use ONLY when the operator explicitly asks, in their own message, to submit, post
  or push forecasts to Metaculus, or invokes /metaculus-submit. Never use it as a step of
  another workflow — not after /forecast, /update, /resolve or /status --act, and not because a
  forecast just changed. Submits what the ledger already holds: no research, no updates, no
  ledger entries.
---

# Submit forecasts to Metaculus

Posts the **latest ledger forecast** of each target question to Metaculus under the bot
account. It is a publishing step, and only the operator triggers it:

- **Explicit intent only.** Run this only when the operator asked for a submission in the
  current conversation. No other skill, command or workflow invokes it, and you must not
  chain it onto one ("the update is done, shall I also submit?" is fine to *ask*; submitting
  unasked is not). `tests/test_submit_metaculus.py` fails if another workflow file mentions
  the script.
- **Routines don't submit; the merge does.** A scheduled run's stored prompt is not live
  consent, and Claude Code's auto-mode check blocks the POST. Unattended runs open a PR
  instead. When the operator merges it into `main`, `.github/workflows/submit-metaculus.yml`
  submits exactly the questions whose ledger forecast changed (`scripts/changed_forecasts.py`).
  If a routine prompt asks you to submit, say that submission happens on merge and give the
  operator the numbers.
- **Submit, don't forecast.** The numbers come from the ledger. Each record's `distribution`
  field holds the full forecast. Only older records that predate that field fall back to the
  newest version block of `forecast.md`. Do no research and change no forecast. If a forecast looks stale, say so in
  the report and leave it; revising it is `/update`.
- **Nothing is written to the repo.** The script never touches the ledger, `meta.yaml` or
  `forecast.md`. Keep the spec file in your scratchpad, so there is nothing to commit.

## Arguments

`/metaculus-submit <slug|post id|URL> [...]` or `/metaculus-submit --all [--project "<name>"]`

- `--all` covers **every** open, unresolved Metaculus question in the ledger, across all
  tournaments. If the operator named a tournament ("the Cup questions"), add
  `--project "<exact tournament name>"`, e.g. `--project "Metaculus Cup Fall 2026"`. If
  `--all` seems broader than they meant, ask before submitting.
- `--force` resubmits even where the bot's live forecast already matches. Use it only if asked.

## Steps

### 1. Dry run from the ledger alone

```bash
uv run scripts/submit_metaculus.py <targets> --dry-run
```

This fetches each post once (a ~4 s pause between calls keeps Metaculus' IP rate limit
quiet; do not re-run it in a loop) and prints what it would submit:

- **binary**: the ledger median. Complete.
- **multiple_choice**: the record's option vector. A record logged before the ledger had a
  `distribution` field fails with `v<N> predates the ledger's distribution field; supply its
  option vector in a spec (options: [...])`. The list gives Metaculus' exact option labels.
- **numeric / date / discrete**: the record's `percentiles` or `pmf` when it has them. If not,
  the script falls back to the ledger quartiles with extrapolated tails and tags the line
  `[quartiles only: tails extrapolated]`.
- `= already live`: the bot's current forecast already equals this one and will be skipped.

If nothing failed and nothing is tagged, skip to step 4.

### 2. Legacy records only: build a spec

A spec fills gaps in **older records that predate the `distribution` field**, and nothing
else. The script refuses a spec entry for a record that already has a distribution: the
ledger is the record. Build one entry for each legacy multiple-choice question (required),
and for each legacy numeric/discrete question whose `forecast.md` records more than the
quartiles (preferred). Read the **newest version block** of `questions/<slug>/forecast.md`. Take the values from the `| **Current forecast** |` header
row, and from the version's own percentile, PMF or option table when one exists. Then write
`<scratchpad>/submit-spec.json`:

```json
{
  "<slug>": {"version": 3, "probabilities": {"0": 0.67, "1": 0.24, "2": 0.065, "3": 0.02, "4+": 0.005}},
  "<slug>": {"version": 1, "percentiles": {"5": 186000, "25": 236000, "50": 272000, "75": 320000, "95": 461000}},
  "<slug>": {"version": 1, "pmf": {"0": 0.001, "1": 0.012, "2": 0.06, "3": 0.181, "4": 0.311}}
}
```

- `version` is the ledger's latest version for that slug. The script refuses a mismatch, so a
  vector copied from an older block cannot be submitted.
- Keys of `probabilities` are the **exact Metaculus labels** from step 1. `forecast.md` often
  abbreviates them ("Sudan ERRs" → `Sudan Emergency Response Rooms`, "Kane" →
  `Harry Kane`). Map each one deliberately; never guess between two plausible options.
- Copy the numbers exactly as written. Do not re-derive, smooth or "fix" them. If they don't
  sum to ~1, or `forecast.md` records no full vector for a multiple-choice question, leave
  that question out and report it instead of inventing a split.
- Percentile keys are percent (`"5"`, `"50"`). `"50"` must equal the ledger median, and
  `"25"`/`"75"` must equal the IQR bounds, in the ledger's units. For discrete questions,
  `pmf` keyed by outcome value beats percentiles. The spec passes the same checks as
  `log_forecast.py --distribution`.
- This gap closes by itself: once a question is next updated, its new record carries the
  distribution and needs no spec.

### 3. Dry run with the spec, then check it

```bash
uv run scripts/submit_metaculus.py <targets> --spec <scratchpad>/submit-spec.json --dry-run
```

Check each line against `forecast.md`: the leading option, the echoed q25/q50/q75, and the
mass outside an open bound (`P<min`, `P>max`). A `!` line is a refusal with its reason. Fix
the spec, or report the question as not submitted.

### 4. Submit

Same command without `--dry-run`. Each line reports `→ submitted`, `= already live`, or
`! rejected: HTTP ...` with Metaculus' reason. The exit code is non-zero if anything failed.

### 5. Report

Give the operator one table: slug, version submitted, what was submitted (P(yes), the
option vector, or median/IQR), and the outcome. List separately what was **not** submitted
and why: unchanged, closed, group post, legacy record without a spec, or rejected. Also flag questions whose latest
version is old, or which close soon, as candidates for `/update`. **Do not** offer to log the
submission to the ledger; the ledger records forecasts, not submissions.

## Limits

- **Group-of-questions posts** (one post, several sub-questions, e.g. the SPR `mc15240`
  pair) are refused; the ledger does not map slugs to sub-question ids.
- **Quartile-only CDFs** are an approximation: the tails are exponential beyond the quartiles,
  heavier than a normal distribution. A recorded `percentiles` distribution with p5/p95, or a
  PMF, is always better.
- The script mixes ~2% uniform mass into every CDF so that each bin clears Metaculus' minimum
  step. This moves quartiles by well under one grid step.
