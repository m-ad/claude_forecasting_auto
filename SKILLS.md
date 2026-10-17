# Skills index

Project skills live in `.claude/skills/<name>/SKILL.md` and load automatically when their
description matches. This file is the human-readable map.

| Skill | Use when | Entry point |
|---|---|---|
| **tournament-forecast** | One bot-tournament question (one-shot), unattended in CI or as its local debug path. Never submits. | `.claude/skills/tournament-forecast/SKILL.md` |
| **forecast-workflow** | A new operator question needs a forecast from scratch. | `.claude/skills/forecast-workflow/SKILL.md` |
| **forecast-update** | An operator question needs revisiting, or resolved and needs a post-mortem. Refuses one-shot questions. | `.claude/skills/forecast-update/SKILL.md` |
| **metaculus-submit** | **Operator request only:** submit current ledger forecasts of non-tournament questions to Metaculus as the bot. Never part of another workflow. | `.claude/skills/metaculus-submit/SKILL.md` |

Subagent: **research-scout** (`.claude/agents/research-scout.md`) — one narrow evidence
stream, read-only, returns a dated digest. At most two per tournament question.

## Slash commands

| Command | Does |
|---|---|
| `/forecast <url or question text>` | Full new-question workflow: scaffold, research, forecast, log. |
| `/update <slug>` | Tripwire-driven Bayesian update of an existing operator forecast. |
| `/resolve <slug> <outcome>` | Record resolution, score it, write the post-mortem. |
| `/status` | Triage: what is due for review, what resolves soon, what is stale. |

## Scripts

| Script | Does |
|---|---|
| `scripts/metaculus_api.py` | The only Metaculus client: official API, bot token, typed errors, redaction. CLI: `whoami`, `post`, `open`, `tournament`. |
| `scripts/new_question.py` | Scaffold a question folder (from the API for Metaculus), cache the question text to `raw/`; `--tournament` for bot questions, `--reuse` for the sweep. |
| `scripts/log_forecast.py` | Append a forecast (with `--distribution`), a resolution, or (from the submit script) a submission/late comment to `ledger/forecasts.jsonl`. Refuses a second forecast on a one-shot question. |
| `scripts/submit_metaculus.py` | Submit to Metaculus. One-shot questions: guards, forecast, private comment, ledger record (run by the sweep). Others: operator-invoked only. |
| `scripts/tournament_poll.py` | The sweep's no-LLM gate: budget, token, open unforecast questions in priority order. |
| `scripts/tournament_sync.py` | Daily reconcile: missed windows, comment retries, resolutions with official scores, `INDEX.md`. |
| `scripts/tournament_registry.py` | Read/write `tournaments/registry.yaml` (operator only). |
| `scripts/record_usage.py` | Token/cost record per Claude run (`ledger/usage.jsonl`) and the rolling spend report. |
| `scripts/ci_commit.sh` | The workflows' commit step: validate, commit, rebase-push with backoff. |
| `scripts/ci_guard.py` | After the forecaster session: undo every change outside its question folder and its own ledger lines (stdlib only, run from `HEAD`). |
| `scripts/status.py` | List questions by urgency; `--index` regenerates `INDEX.md`. |
| `scripts/calibration.py` | Brier / log score, calibration buckets. |

All Python scripts run under `uv run <path>`.

## Workflows

| Workflow | When | Does |
|---|---|---|
| `tournament-sweep.yml` | every 30 min (opt-in: `SWEEP_ENABLED=true`), or manually | gate → one job per open question: scaffold, forecast, submit, commit |
| `tournament-sync.yml` | daily 03:23 UTC, or manually | deterministic reconcile, full test suite, commit |
| `tests.yml` | pull requests, pushes to `main` | ruff + pytest |
