---
name: tournament-forecast
description: >-
  Forecast ONE already-scaffolded bot-tournament question (MiniBench, FutureEval) inside its
  3-hour window: read the cached resolution criteria, outside view, focused research, a median
  plus IQR (and full distribution), the short-form forecast.md, and exactly one ledger entry.
  Used by the tournament-sweep workflow, one session per question; also the local debug path
  for the same job. Never submits and never commits -- the workflow does both after you exit.
  Do not use for non-tournament questions (forecast-workflow) or for revisiting anything (a
  tournament question is never revisited).
---

# Tournament forecast — one question, one shot

You are running unattended in CI. Nobody will answer a question. The workflow scaffolded the
folder, and after you exit it submits whatever you logged, posts your newest `forecast.md`
version as the bot's private rationale comment, and commits. **Your only deliverables are
`questions/<slug>/forecast.md` and one `log_forecast.py add` call.**

Scoring is the **spot peer score**: a log score of your forecast at close, relative to the other
bots. Calibration and sharpness both pay; overconfidence on a wrong side costs far more than
it ever earns. Not forecasting scores 0; a bad forecast scores below 0.

## Rules (budget protection — follow verbatim)

1. **One retry maximum** per failing operation (a fetch, a search), then move on.
2. **Never debug a script or tool failure.** If `log_forecast.py` rejects your input, read its
   message, fix the *input*, retry once. Do not read or edit scripts.
3. **Never re-read a file already read** and never re-run a search that returned usable results.
4. **Watch the clock.** `date -u` tells the time; `$FORECAST_DEADLINE` is when this session is
   killed. Log your forecast **at least 5 minutes before the deadline**, however rough. An
   unlogged forecast is never submitted.
5. **Search enough, then stop.** Aim for **8–16 searches** in total (yours plus any
   `research-scout`'s); go up to **32** when the question needs it — a hard-to-find
   resolution source, conflicting evidence, several independent streams. Cite at least 5
   sources. The clock still wins: rule 4 comes first.
6. **Never** run `git`, never touch `ledger/` by hand, never call Metaculus. The Metaculus token
   is not in this session's environment (GitHub injects secrets per step; only the scaffold
   and submit steps receive it), and the community prediction is hidden on tournament
   questions anyway. Python is for models in your question folder, not for reaching
   anything else. The session starts in the repository root: never `cd`, and run Python
   only as `uv run python` — `cd` and bare `python3` are denied and cost a turn.
7. **Log exactly once.** A second `add` is refused: one forecast per question is a tournament rule.

## Step 1 — Read the question (no network)

- `questions/<slug>/meta.yaml` — type, `question_id`, `tournament.closes`, `unit`.
- `questions/<slug>/raw/metaculus-question-<date>.json` — `resolution_criteria`, `fine_print`,
  `description`, and for numeric/discrete `scaling` (`range_min`, `range_max`,
  `open_lower_bound`, `open_upper_bound`), for multiple choice the exact `options` labels.

MiniBench questions are written and resolved **by an LLM** from a news or data source. Read the
criteria literally: the named source, the exact date and timezone, the threshold, what happens
if the source is not updated. Mechanical literalness is the cheapest edge available.
Do not assume the question has already resolved, or that the event in the title is ongoing,
without checking.

Write `### What resolves YES` in `forecast.md` **first**, before forming a view: one paragraph,
exactly what resolves the question and from which source. For numeric questions: what number,
measured how, as of when, and what the bounds mean.

## Step 2 — Outside view

Name a reference class and its base rate (`### Outside view`), with n and source, or say
explicitly that none fits and why. For "will X happen by date D" questions, the status-quo /
time-left base rate is usually the strongest prior: most things that have not happened yet do
not happen in the next few weeks. For numeric questions: the last value, the recent trend, and
the typical volatility over the horizon.

## Step 3 — Research

Use `WebSearch` / `WebFetch`. Priorities, in order:

1. **The resolution source itself** — the current value, the latest release, its schedule.
   When it is a public page, open it with `WebFetch`: a number the forecast rests on never
   comes from a search snippet alone.
2. **Recent news** (the last days matter most; note dates).
3. **Prediction markets** on the same event (Polymarket, Kalshi, Manifold — discount
   low-volume Manifold). Using other platforms' public forecasts is allowed by the rules.
4. **Disconfirmation**: one deliberate search for evidence against your emerging view.

For a question with genuinely independent streams you may spawn up to **2** `research-scout`
subagents in parallel (e.g. resolution-source data vs. news). Give each a narrow brief and ask
for a dated digest with URLs. Integrate yourself; never delegate the number.

Record what you found under `### Evidence` (dated, with source numbers) and market prices under
`### Other forecasters` (Metaculus row: "hidden — bot tournament").

## Step 4 — Inside view and the number

`### Inside view`: adjust from the base rate with the specific evidence; say how much and why.
`### What would change my mind`: the one or two facts the forecast is most sensitive to (no
tripwire machinery — this question is never revisited, but the reasoning still belongs here).

A quantitative model is welcome when it sharpens the number (combining uncertain
inputs, a Monte Carlo over paths, fitting a distribution to a historical series): write it to
`questions/<slug>/model.py` and run it with `uv run python questions/<slug>/model.py`
(numpy and scipy are installed). Keep it to a few minutes, put its key outputs and
assumptions in `### Inside view`, and never let it write outside your question folder —
anything it changes elsewhere is reverted before submission.

Then fix the forecast:

- **binary** — median probability and an IQR describing your uncertainty about it.
  Stay inside [0.02, 0.98] unless the outcome is already essentially determined by data you
  have seen; log scores punish confident misses hard.
- **multiple_choice** — a probability for **every** option, using the **exact labels** from the
  snapshot, summing to 1, no option below 0.005. The median is the leading option's probability;
  the IQR brackets it.
- **numeric / discrete** — percentiles in native units: `5, 10, 25, 50, 75, 90, 95`. p25/p50/p75
  must equal the `--lower/--median/--upper` you log, exactly. Respect closed bounds (no mass
  outside a closed bound); put tail mass beyond an *open* bound if the value can land there.
  Make tails honestly wide: a numeric miss outside a too-tight interval is the costliest error.

## Step 5 — Write forecast.md

Fill the scaffolded short form. Keep the version heading `## v1 — Initial forecast — <today>`
dated today (UTC). Sections: What resolves YES, Outside view, Inside view, Evidence, Other
forecasters, What would change my mind, Sources (numbered, `URL (accessed YYYY-MM-DD)`, at least
5). End with the fixed block, filled in:

```
**Question**: [<title>](<url>)
**Date**: YYYY-MM-DD
**Forecast**: Median 12.0%, IQR [8.0%, 18.0%]
**Thesis**: <1–3 sentences: the reference class, the one or two drivers that moved it, and the
single fact the forecast is most sensitive to.>
```

Binary percentages to exactly one decimal. Numeric: native units. Multiple choice:
`Median 62.0% (<leading option>), IQR [55.0%, 69.0%]`. This version block **is** the bot's
public rationale once the question closes — write it for a reader.

Leave the header table alone: `log_forecast.py` rewrites the Current forecast row.

## Step 6 — Log (once)

Binary:

```bash
uv run scripts/log_forecast.py add <slug> --median 0.12 --lower 0.08 --upper 0.18 \
    --thesis "<the Thesis sentence>"
```

Multiple choice / numeric / discrete: write the distribution to
`questions/<slug>/raw/distribution-<YYYY-MM-DD>.json` and pass it with `@`:

```bash
# {"probabilities": {"<exact label>": 0.62, "<exact label>": 0.25, "<exact label>": 0.13}}
# {"percentiles": {"5": 590, "10": 598, "25": 610, "50": 622, "75": 635, "90": 648, "95": 655}}
uv run scripts/log_forecast.py add <slug> --median 622 --lower 610 --upper 635 \
    --distribution @questions/<slug>/raw/distribution-2026-10-19.json --thesis "..."
```

No `--next-review`, no `--cp/--pro/--gold`. If it refuses, fix the input per its message and
retry once. Then **stop**: reply with the summary block and exit.
