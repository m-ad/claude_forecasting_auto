---
name: forecast-workflow
description: >-
  End-to-end workflow for producing a new calibrated probabilistic forecast in this repository:
  scaffolding the question folder, reading resolution criteria, establishing a reference-class
  base rate, pulling the Metaculus community/Pro/gold-medalist aggregations and prediction-market
  prices, building scenarios and an interquartile range, and writing forecast.md plus the ledger
  entry. Use whenever the user asks for a forecast, a probability, a prediction, gives a
  Metaculus/Kalshi/Polymarket/Manifold URL or question ID, says "forecast this", "what are the
  odds", "how likely is", or invokes /forecast. Do not use for revisiting an existing forecast —
  that is forecast-update.
---

# New forecast workflow

Read `docs/methodology.md` and `docs/output-format.md` before writing anything. High effort.
Create a task list; this has more than six steps.

## Step 1 — Scaffold

```bash
uv run scripts/new_question.py --url "<metaculus url>"     # or --title "..." --type binary
```

It creates `questions/<YYYY-MM-DD>-<src><id>-<slug>/` with `meta.yaml`, `forecast.md`,
`research.md` and `raw/`, pre-filled from the templates. It prints the slug — use it below.

For a Metaculus question it also pre-fills the title, type, and resolution dates by calling
the aggregations script. Verify the fields; do not trust the slug it derived from a truncated
title if the question is really about something else.

## Step 2 — Read the question properly

```bash
uv run .claude/skills/metaculus-aggregations/scripts/metaculus_aggregations.py <POST_ID> \
    --comments 10 --history --json > questions/<slug>/raw/metaculus-<YYYY-MM-DD>.json
```

Read resolution criteria, fine print, background, and the top comments (comments frequently
contain the resolution ambiguity everyone else already found). Write the "What resolves YES"
digest into `forecast.md` now, before forming any opinion.

**Deliberately do not anchor yet**: note the CP but do your own Step 3–4 before reconciling.

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

Fill the market-comparison table: Metaculus CP / Pro / gold, Kalshi, Polymarket, Manifold
(discounted), Sentinel, Mantic, GJOpen/INFER if applicable. Flag disagreement between the
Metaculus cohorts explicitly. If you differ from a liquid market or from agreeing Pro + gold
cohorts by more than 10 percentage points, search again for the fact you are missing before
you write the justification.

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
    --cp 0.09 --pro 0.07 --gold 0.08 --n-forecasters 312 \
    --thesis "..." --next-review 2026-10-31
```

Then `uv run scripts/status.py --index` to refresh `INDEX.md`.

**Before committing**, run both and fix any failures — this is a repo-edit workflow, per
`CLAUDE.md`'s Git section:

```bash
uv run ruff check .
uv run pytest -q
```

## Step 10 — Report

Reply in chat with: the market-comparison table, the 3–5 line reasoning core, and the summary
block. Give the path to `forecast.md`. A chart (probability decomposition or scenario weights)
only if it aids understanding — horizontal bars, saved to `questions/<slug>/charts/`.

## Non-Metaculus questions

Same workflow, minus Steps 2's Metaculus fetch. Use `--title/--type` on `new_question.py`,
`src` = `ks`/`pm`/`mf`/`x`. Write your own resolution criteria into `forecast.md` and make them
explicit and falsifiable — an unfalsifiable question cannot be scored, and a forecast that
cannot be scored does not belong in the ledger.
