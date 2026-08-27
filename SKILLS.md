# Skills index

Project skills live in `.claude/skills/<name>/SKILL.md` and load automatically when their
description matches. This file is the human-readable map.

| Skill | Use when | Entry point |
|---|---|---|
| **forecast-workflow** | A new question needs a forecast from scratch. | `.claude/skills/forecast-workflow/SKILL.md` |
| **forecast-update** | An existing question needs revisiting, or resolved and needs a post-mortem. | `.claude/skills/forecast-update/SKILL.md` |
| **metaculus-aggregations** | Any Metaculus lookup: community prediction, Pro and gold-medalist cohorts, resolution criteria, comments, history. **Primary Metaculus tool.** | `.claude/skills/metaculus-aggregations/SKILL.md` |
| **metaculus-scraper** | Fallback only, when the api-proxy is hard-blocked. Headline CP only — no cohorts, no comments. | `.claude/skills/metaculus-scraper/SKILL.md` |

## Slash commands

| Command | Does |
|---|---|
| `/forecast <url or question text>` | Full new-question workflow: scaffold, research, forecast, log. |
| `/update <slug>` | Tripwire-driven Bayesian update of an existing forecast. |
| `/resolve <slug> <outcome>` | Record resolution, score it, write the post-mortem. |
| `/status` | Triage: what is due for review, what resolves soon, what is stale. |
| `/review <slug>` | Red-team an existing forecast without changing it. |

## Scripts

| Script | Does |
|---|---|
| `scripts/new_question.py` | Scaffold a question folder from a Metaculus URL or a title. |
| `scripts/log_forecast.py` | Append a forecast or a resolution to `ledger/forecasts.jsonl`. |
| `scripts/status.py` | List questions by urgency; `--index` regenerates `INDEX.md`. |
| `scripts/calibration.py` | Brier / log score, calibration buckets, skill vs. the community. |

All run under `uv run <path>`.
