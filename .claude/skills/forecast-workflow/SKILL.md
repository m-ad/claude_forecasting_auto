---
name: forecast-workflow
description: >-
  End-to-end workflow for producing a new calibrated probabilistic forecast for an individual,
  non-tournament question in this repository (a Metaculus question the maintainer added, or a
  free-text question): scaffolding the question folder, reading resolution criteria,
  establishing a reference-class base rate, checking prediction-market prices, building scenarios
  and an interquartile range, and writing forecast.md plus the ledger entry. Use whenever the user asks for a forecast, a probability, a prediction, gives a
  Metaculus/Kalshi/Polymarket/Manifold URL or question ID, says "forecast this", "what are the
  odds", "how likely is", or invokes /forecast. Do not use for revisiting an existing forecast —
  that is forecast-update — or for a bot-tournament question, which is tournament-forecast.
---

# New forecast workflow

Read `docs/methodology.md` and `docs/output-format.md` before writing anything. High effort.
Create a task list; this has more than six steps.

**Mode check first.** If the question belongs to a bot tournament (MiniBench, a FutureEval
season — the post's `tournaments` in its `raw/` snapshot, or a `tournament` block with
`mode: one_shot` in `meta.yaml`), stop and use `tournament-forecast` instead: one forecast per
question, no human in the loop, and the sweep submits it. This skill is for everything else.

## Step 1 — Scaffold

```bash
uv run scripts/new_question.py --url "<metaculus url>"     # or --title "..." --type binary
```

It creates `questions/<YYYY-MM-DD>-<src><id>-<slug>/` with `meta.yaml`, `forecast.md`,
`research.md` and `raw/`, pre-filled from the templates, and prints the slug — use it below.

For a Metaculus question it fills title, type, `question_id`, unit and dates from the official
API and caches the question text to `raw/metaculus-question-<date>.json`. Verify the fields; do
not trust the slug it derived from a truncated title if the question is really about something
else.

## Step 2 — Read the question properly

Read `raw/metaculus-question-<date>.json`: resolution criteria, fine print, background, bounds
and options. (`uv run scripts/metaculus_api.py post <post_id>` prints the same, fresh.) Staff
comments are available to the bot token; other comments and the community prediction are not.

Write the "What resolves YES" digest into `forecast.md` now, before forming any opinion.

Bot tokens see `null` question text before a question opens (`status: upcoming` —
`new_question.py` warns). The criteria are published on the page; scaffold again once the
question opens rather than forecast on an assumed resolution source.

## Step 3 — Outside view

Reference class, n, window, raw base rate, source. Scale to the question window. Record in
`research.md` with the source. If several classes disagree, keep all of them.

## Step 4 — Inside view

Decompose into a chain or a set of paths with explicit numbers. Identify the actors and their
incentives. Identify what has to be true.

## Step 5 — Evidence sweep

Search broadly — target ≥ 15 distinct sources, varied phrasings (see `docs/sources.md`).
Log every meaningful search and finding in `research.md`, including dead ends: the next update
needs to know what you already ruled out. Actively look for evidence *against* your emerging
view. For paywalled pages retry with the `https://archive.is/` prefix.

Snapshot volatile numbers into `raw/` with dated filenames.

## Step 6 — Other forecasters

Fill the market-comparison table: Kalshi, Polymarket, Manifold (discounted), Sentinel, Mantic,
GJOpen/INFER if applicable. Record the Metaculus row as "hidden": the bot token cannot see the
community prediction, and no CP is logged. If you differ from a liquid market by more than 10
percentage points, search again for the fact you are missing before you write the
justification.

## Step 7 — Scenarios, distribution, sensitivity

3–5 weighted mutually exclusive scenarios → median and IQR. Then a sensitivity table for the
2–3 load-bearing assumptions. Run the calibration-hygiene checks in `docs/methodology.md` §7.

## Step 8 — Tripwires

3–6 dated, observable signals with direction and magnitude. Copy them into `meta.yaml`.
Set `next_review` using the cadence table in `docs/update-protocol.md`.

## Step 9 — Write and log

Write `forecast.md` in the exact format of `docs/output-format.md` (header block + `## v1 …`),
then:

```bash
uv run scripts/log_forecast.py add <slug> \
    --median 0.12 --lower 0.08 --upper 0.18 \
    --thesis "..." --next-review 2026-10-31
```

`--next-review` belongs to updatable questions only. A one-shot tournament question never gets
one — and never reaches this workflow: `log_forecast.py` refuses `--next-review` on it.

**Record the full distribution with `--distribution`** whenever the median and IQR are not the
whole forecast. The ledger is the only machine-readable record, and a summary can't be scored
against an outcome it doesn't describe:

- **multiple choice — required** (`log_forecast.py` refuses without it). The option vector,
  keyed by the **exact Metaculus option labels** (from the cached `raw/metaculus-question-*.json`, not
  the shortened names in `forecast.md`), as fractions summing to 1. `--median` is the leading
  option's probability and must equal its entry. Put the vector in a JSON file and pass it as
  `@file` when a label contains quotes:
  `--distribution '{"probabilities": {"Likud": 0.381, "Yashar": 0.61, "Other": 0.009}}'`
- **numeric / date — recommended** when you have more than quartiles:
  `--distribution '{"percentiles": {"5": 186000, "25": 236000, "50": 272000, "75": 320000, "95": 461000}}'`
  (`"50"` required and equal to `--median`; `"25"`/`"75"` equal to `--lower`/`--upper`).
- **discrete — recommended**: `{"pmf": {"0": 0.001, "1": 0.012, ...}}` (outcome value → probability).

Then `uv run scripts/status.py --index` to refresh `INDEX.md`.

**Before committing**, run both and fix any failures — this is a repo-edit workflow, per
`CLAUDE.md`'s Git section:

```bash
uv run ruff check .
uv run pytest -q
```

## Step 10 — Report

Reply in chat with: the market-comparison table, the 3–5 line reasoning core, and the summary
block — which opens with the clickable `**Question**: [title](url)` line (from `meta.yaml`),
then Date / Forecast / Thesis. Give the path to `forecast.md`. No charts (AGENTS.md §7).

This workflow never submits to Metaculus. Only the sweep submits, and only one-shot
tournament questions.

## Non-Metaculus questions

Same workflow, minus Step 2's Metaculus snapshot. Use `--title/--type` on `new_question.py`,
`src` = `ks`/`pm`/`mf`/`x`. Write your own resolution criteria into `forecast.md` and make them
explicit and falsifiable — an unfalsifiable question cannot be scored, and a forecast that
cannot be scored does not belong in the ledger.
