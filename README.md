# Forecasting workbench

A Claude Code project for producing calibrated probabilistic forecasts — mostly Metaculus
questions, sometimes anything else — and for keeping them honest over time.

Design goal: **every forecast is auditable and every forecast is scoreable.** The reasoning
lives in a per-question folder that reads like a lab notebook; the numbers live in an
append-only ledger that can be scored against reality.

## Setup

```bash
uv sync
uv run playwright install chromium     # once; needed for Metaculus access
claude                                 # start a session in this directory
```

`www.metaculus.com` must be reachable. `CLAUDE.md` imports `AGENTS.md`, which is the agent's
operating manual — read it if you want to know what the agent will do.

## Use

```
/forecast https://www.metaculus.com/questions/43505/...   # new question, full workflow
/forecast Will the ECB cut rates below 1.5% before July 2027?
/update 2026-08-27-mc43505-us-recession-2027              # tripwire-driven Bayesian update
/review <slug>                                            # red-team, changes nothing
/resolve <slug> yes                                       # score it, write the post-mortem
/status                                                   # what needs attention today
```

Slug arguments are fuzzy — a URL, a post id, or a fragment of the title works.

## Layout

```
AGENTS.md                 agent operating manual (CLAUDE.md imports it)
SKILLS.md                 index of skills, commands and scripts
INDEX.md                  generated table of all questions
docs/
  methodology.md          the forecasting checklist: base rates, decomposition, IQR, biases
  output-format.md        the fixed deliverable format
  update-protocol.md      when and how to revisit; resolution and post-mortem
  sources.md              where to look, and how much to trust it
questions/<slug>/
  meta.yaml               identifiers, dates, current forecast, tripwires, next review
  forecast.md             the deliverable — newest version on top, append-only history
  research.md             working log: searches, base rates, dead ends
  raw/                    dated snapshots of Metaculus aggregations and market prices
  charts/                 generated figures
ledger/forecasts.jsonl    append-only scoreable record of every forecast and resolution
scripts/                  new_question · log_forecast · status · calibration · … (all: SKILLS.md)
templates/                what new_question.py renders into each question folder
tests/                    data and unit tests (see tests/README.md)
.claude/skills/           forecast-workflow · forecast-update · metaculus-aggregations · … (all: SKILLS.md)
.claude/commands/         the slash commands above
```

## Output format

Fixed, so that forecasts stay comparable across months. Every version ends with the block
below, which always opens with a clickable link to the question (the chat reply opens with it too):

```
**Question**: [Will X happen by 2027?](https://www.metaculus.com/questions/12345/)
**Date**: 2026-08-27
**Forecast**: Median 12.0%, IQR [8.0%, 18.0%]
**Thesis**: One to three sentences naming the drivers and the sources they rest on.
```

Updates additionally open with a revision table — prior median/IQR → new, one driver per row —
and a tripwire check. Full template in `docs/output-format.md`.

## The update loop

This is the part most forecasting setups get wrong, so it is mechanised here:

1. Each forecast ends with **tripwires** — dated, observable signals with a direction and a
   magnitude ("IAEA Board resolution referring the file to the UNSC before 2026-11-30 → +15pp").
   In `meta.yaml` the magnitude is unsigned and carries an explicit `magnitude_unit`:
   `pp` for probability questions, `days`/`weeks`/`months` for date questions, and the
   question's own `unit` for numeric ones (`magnitude: 6000`, `magnitude_unit: cases`).
   Vague ones ("further escalation") are not accepted.
2. Each forecast sets a **`next_review` date** from the time-to-resolution cadence table in
   `docs/update-protocol.md`.
3. `/status` ranks open questions by urgency: review overdue, resolution imminent, last version
   stale, or a large gap to the community prediction.
4. `/update <slug>` searches the **tripwires by name first**, then generally; re-fetches the live
   Metaculus cohorts and market prices; and prepends a new version with a revision table. It
   switches to a full de-novo re-analysis when the market contradicts you, when a third of the
   remaining time has elapsed, or when your last two updates drifted the same way.
5. `/resolve` scores every version against the outcome — and against the community prediction at
   the same timestamps — and forces one question: *which tripwire should have existed and did not?*

To run the loop unattended, e.g. weekly:

```bash
claude -p "/status --act" --permission-mode acceptEdits
```

Start without `--act` until you trust it.

## Calibration

```bash
uv run scripts/calibration.py --plot calibration.png
```

Brier score, log score, calibration by bucket, interquartile coverage for numeric questions,
and — the number that actually matters — whether you are beating the Metaculus community
prediction at the same points in time. A forecasting setup that never checks this is a
diary, not a discipline.

## Tests

```bash
uv run pytest
```

Mostly data tests: the ledger's JSONL shape and timestamp ordering, the `meta.yaml` schema,
the fixed `forecast.md` format, and agreement between `meta.yaml`, the ledger and `INDEX.md`.
Every ledger line and every question folder becomes its own test case, so a failure names the
record to fix. See `tests/README.md`.

## Metaculus access

`.claude/skills/metaculus-aggregations/` fetches the community prediction, the Metaculus Pro
cohort and the gold-medalist cohort as structured JSON, plus resolution criteria, fine print
and comments. The Pro and gold cohorts are weighted above the raw community prediction, and
disagreement between the three is treated as signal in its own right. The REST API needs a
token; `curl`/`WebFetch` return 403. The skill's SKILL.md documents the two non-obvious
invariants that keep it working — do not "simplify" them away.
