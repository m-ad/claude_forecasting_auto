# Configuration

Everything the bot reads from its environment, in one place. GitHub: Settings → Secrets and
variables → Actions, as **repository** secrets and variables. Environment secrets (Settings →
Environments) do not reach these jobs: no job declares an `environment:`, so GitHub passes
them in as empty strings. `tests/test_bot.py` fails if a workflow uses a secret or variable
that is not listed here.

## Secrets (required)

| Secret | Used by | What it is |
|---|---|---|
| `METACULUS_API_KEY` | sweep gate, scaffold and submit steps; daily sync | The **bot account's** API token (Metaculus → Settings → My Forecasting Bots). Never given to the forecaster session. |
| `CLAUDE_CODE_OAUTH_TOKEN` | sweep forecast step only | Long-lived Claude subscription token from `claude setup-token`. It expires: put the date in your calendar. |

Without both, the sweep fails at its first step and opens a `bot-health` issue.

## Repository variables (all optional)

| Variable | Default | Effect |
|---|---|---|
| `SWEEP_ENABLED` | unset (= off) | The kill switch. Scheduled sweeps and syncs run only when it is exactly `true`. Manual runs ignore it. |
| `MODEL_FORECAST` | `opus` | Model for the forecaster session (`claude --model`): an alias (`opus`, `sonnet`, `fable`) or a full model id. Aliases resolve to the newest model the installed CLI knows. |
| `EFFORT_FORECAST` | `high` | `claude --effort`: `low`, `medium`, `high`, `xhigh`, `max`. |
| `MAX_MINUTES_PER_QUESTION` | `25` | Timeout of the forecaster step. What was logged before it fires is still submitted. |
| `MAX_USD_PER_QUESTION` | `15` | `claude --max-budget-usd` per session, in API-equivalent dollars. `0` removes the cap (the timeout still applies). |
| `MAX_QUESTIONS_PER_RUN` | `6` | How many questions one sweep takes on; the rest wait for the next sweep. |
| `MAX_PARALLEL` | `3` | How many questions are forecast at the same time within a sweep. |
| `WEEKLY_BUDGET_USD_EQUIV` | unset (= no budget) | Trailing-7-day API-equivalent spend at which the gate stops starting sessions; from 80 % of it, at most 2 questions per run. Set it after measuring a round (`uv run scripts/record_usage.py report`). |
| `CLAUDE_CODE_VERSION` | `latest` | npm version of `@anthropic-ai/claude-code`. Unpinned by default so new models and fixes arrive on their own; pin a version (e.g. `2.1.302`) if a release breaks the sweep. Each job prints the version it installed in its Step Summary. |

## Fixed in files, not variables

| Setting | Where | Value |
|---|---|---|
| Sweep cadence | `.github/workflows/tournament-sweep.yml` (`cron`) | every 30 min, at :11 and :41 |
| Daily sync time | `.github/workflows/tournament-sync.yml` (`cron`) | 03:23 UTC |
| Research subagent model | `.claude/agents/research-scout.md` (`model:`) | `sonnet` |
| Tool permissions of the forecaster session | `.claude/settings.ci.json` | allowlist; `dontAsk` mode |
| Which tournaments are polled, in what priority | `tournaments/registry.yaml` (`uv run scripts/tournament_registry.py`) | `minibench` active |
| Too late to start a question | `scripts/tournament_poll.py` (`MIN_MINUTES_LEFT`) | 20 minutes before close |

## Manual run inputs (Actions → tournament-sweep → Run workflow)

| Input | Effect |
|---|---|
| `tournament` | Poll only this slug, e.g. `bot-testing-area` (registered or not). |
| `post_ids` | Forecast only these posts (still subject to every guard). |
| `max_questions` | Cap for this run, overriding `MAX_QUESTIONS_PER_RUN`. |
| `dry_run` | Forecast, upload the question folder as an artifact, submit and commit nothing. |

## Local use

| Variable | When |
|---|---|
| `METACULUS_API_KEY` (or `METACULUS_TOKEN`) | Any script that calls Metaculus (`metaculus_api.py`, `new_question.py`, `tournament_poll.py`). Reading is harmless; `submit_metaculus.py` without `--dry-run` posts for real. |
