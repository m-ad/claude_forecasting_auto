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
| `SWEEP_ENABLED` | unset (= off) | The kill switch. Scheduled sweeps and syncs (GitHub's `schedule`, and the external scheduler's dispatches with `scheduled: true`) run only when it is exactly `true`. Manual runs ignore it. |
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
| Sweep cadence | the cron-job.org sweep job (below); fallback `cron` in `.github/workflows/tournament-sweep.yml` | every 30 min, at :11 and :41 |
| Daily sync time | the cron-job.org sync job (below); fallback `cron` in `.github/workflows/tournament-sync.yml` | 03:23 UTC |
| Research subagent model | `.claude/agents/research-scout.md` (`model:`) | `sonnet` |
| Research floor for one-shot questions | `scripts/log_forecast.py` (`MIN_SEARCHES`, `REQUIRED_CATEGORIES`, `WAIVER_MINUTES`) | 15 searches done; resolution source, news, markets, base rate, disconfirmation; waived 8 min before the deadline |
| PDF extraction | `pyproject.toml` group `research` (`pymupdf4llm`), `scripts/pdf_text.py` | pinned `1.28.2`; first 30 pages unless `--pages` |
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
| `scheduled` | Obey `SWEEP_ENABLED` like a scheduled run. Set by the external scheduler; leave it off by hand. `tournament-sync` has this input too. |

## External scheduler (cron-job.org)

GitHub's `schedule` trigger is best effort: in the week from 2026-10-18 it fired for 42 of
~332 sweep slots (13 %), a median 4.2 h apart, while a question is open for 3 h. The clock
the bot relies on is [cron-job.org](https://cron-job.org), which starts both workflows
through the GitHub API (`workflow_dispatch`). Its settings live there, not in this
repository; the GitHub schedules stay as a fallback (free: the repository is public).

**Token.** A fine-grained personal access token (GitHub → Settings → Developer settings →
Personal access tokens → Fine-grained tokens) with:

- Repository access: only `m-ad/claude_forecasting_auto`.
- Repository permissions: **Actions: Read and write**, nothing else (Metadata: read is
  added automatically).
- An expiry, with the date in your calendar. A lapsed token makes every dispatch fail with
  HTTP 401, and only the fallback schedule is left.

Not a classic token (its `repo` scope can push to `main`) and not `repository_dispatch`
(it needs Contents: write). With Actions: write, a leaked token can start, cancel and
delete workflow runs, but cannot read secrets or push code, and every run it starts still
passes the gate's guards. cron-job.org does not verify TLS certificates (its FAQ): one
more reason to keep the token this narrow.

**Jobs.** One per workflow, time zone UTC:

| Field | Sweep | Sync |
|---|---|---|
| URL | `https://api.github.com/repos/m-ad/claude_forecasting_auto/actions/workflows/tournament-sweep.yml/dispatches` | the same with `tournament-sync.yml` |
| Schedule | every hour, minutes 11 and 41 | daily, 03:23 |
| Method | `POST` | `POST` |
| Headers | `Authorization: Bearer <token>`, `Accept: application/vnd.github+json`, `X-GitHub-Api-Version: 2022-11-28`, `Content-Type: application/json` | the same |
| Body | `{"ref": "main", "inputs": {"scheduled": "true"}}` | the same |
| Notifications | on failure, and when the job is disabled | the same |

`"scheduled": "true"` is what makes a dispatch obey the kill switch; without it the run
counts as manual. GitHub answers a good request with a 2xx status. Test the token and body
before saving the job:

```bash
curl -sS -o /dev/null -w '%{http_code}\n' -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/m-ad/claude_forecasting_auto/actions/workflows/tournament-sweep.yml/dispatches \
  -d '{"ref": "main", "inputs": {"scheduled": "true"}}'
```

| Status | Meaning |
|---|---|
| 2xx | Dispatched: a `workflow_dispatch` run appears under Actions. |
| 401 | Token wrong or expired. |
| 403 | Token lacks Actions: write. |
| 404 | Token cannot see the repository, or the workflow file name is wrong. |
| 422 | `main` has no `scheduled` input (this setup is not merged), or the JSON is malformed. |

## Local use

| Variable | When |
|---|---|
| `METACULUS_API_KEY` (or `METACULUS_TOKEN`) | Any script that calls Metaculus (`metaculus_api.py`, `new_question.py`, `tournament_poll.py`). Reading is harmless; `submit_metaculus.py` without `--dry-run` posts for real. |
