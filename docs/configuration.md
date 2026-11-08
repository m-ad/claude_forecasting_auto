# Configuration

Everything the bot reads from its environment, in one place. GitHub: Settings → Secrets and
variables → Actions, as **repository** secrets and variables. Environment secrets (Settings →
Environments) do not reach these jobs: the only job that declares an `environment:` is
publish-page's deploy job (`github-pages`, which Pages requires), and it reads no secret, so
an environment secret would arrive everywhere as an empty string. `tests/test_bot.py` fails if a workflow uses a secret or variable
that is not listed here.

## Secrets (required)

| Secret | Used by | What it is |
|---|---|---|
| `METACULUS_API_KEY` | sweep gate, scaffold and submit steps; daily sync; results page (read-only: leaderboards) | The **bot account's** API token (Metaculus → Settings → My Forecasting Bots). Never given to the forecaster session. |
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
| `MAX_WEB_SEARCHES` | `50` (`DEFAULT_MAX_SEARCHES` in `scripts/search_budget.py`) | `WebSearch` tool calls per forecaster session, main agent and scouts together. Past it a `PreToolUse` hook (`scripts/search_budget.py`) refuses further searches with a reason telling the model to stop searching and to log once every scout has reported, and `log_forecast.py` waives the research floor. The main agent has no per-agent cap: it may use whatever the scouts leave. `WebFetch` is counted, never capped. `0` removes the cap. One tool call can bill several search requests: compare `search_tool_calls` with `web_searches` in `ledger/usage.jsonl` before tuning it. |
| `MAX_WEB_SEARCHES_PER_SCOUT` | `8` (`DEFAULT_MAX_PER_SCOUT` in `scripts/search_budget.py`) | `WebSearch` tool calls per research-scout, so one scout cannot spend the session's budget. The scouts together also never take the last `MAX_WEB_SEARCHES_PER_SCOUT` searches the main agent has not used: one scout's allowance is reserved for it. With the defaults, `MAX_SCOUTS` scouts plus that reserve fit inside `MAX_WEB_SEARCHES` (a test checks it); if you raise this variable or lower `MAX_WEB_SEARCHES`, keep (`MAX_SCOUTS` + 1) × `MAX_WEB_SEARCHES_PER_SCOUT` ≤ `MAX_WEB_SEARCHES`, or the last scouts to search are cut off by the session's share before their own cap. Keyed on the `agent_id` the CLI puts into hook input from a subagent (since CLI 2.1.69); an empty `search_calls_by_agent` in a session with scouts means the cap was not in force. `0` removes the cap. |
| `MAX_QUESTIONS_PER_RUN` | `6` | How many questions one sweep takes on; the rest wait for the next sweep. The allowance cap (below) and the weekly budget can lower it further. |
| `MAX_PARALLEL` | `3` | How many questions are forecast at the same time within a sweep. |
| `FORECAST_MODE` | `auto` | The sweep's research mode. `auto`: the gate (`scripts/allowance.py`) picks `deep`, or `lean` once the estimated Claude allowance passes `LEAN_AT_5H` or `LEAN_AT_7D`. `deep` or `lean` forces the mode; the stop lines and the allowance cap still apply. The `mode` input of a manual run overrides it. An unknown value means `auto`. |
| `MODEL_LEAN` | unset (= `MODEL_FORECAST`) | Model for **lean** sessions only. |
| `ALLOWANCE_5H_USD_EQUIV` | `16` (`DEFAULT_ALLOWANCE_USD` in `scripts/allowance.py`) | API-equivalent dollars one 5-hour window of the Claude subscription holds; `100 /` it is the allowance points one dollar uses. The default is the lowest cap round 2 hit ($16–24). With no allowance reading in `ledger/usage.jsonl` (issue #20) the gate estimates the 5-hour use as trailing-5-hour spend divided by it. Lower it if sessions are refused before the gate stops; interactive Claude use draws on the same allowance and is not in the ledger. |
| `ALLOWANCE_7D_USD_EQUIV` | `100` (`DEFAULT_ALLOWANCE_USD` in `scripts/allowance.py`) | The same for the 7-day window; round 2 hit the weekly cap at about $100. Used only with a 7-day reading or reset time from the CLI: without one the 7-day window does not gate, because a trailing 7-day sum would block for days after the real weekly reset. |
| `ALLOWANCE_STOP_5H` | `95` (`DEFAULT_STOP` in `scripts/allowance.py`) | Estimated 5-hour use, in percent, at which the gate starts nothing until the window clears (`reason: allowance_exhausted until <time>`, one `bot-health` comment per exhaustion). Also the line the per-run cap keeps under: `floor((stop − use) / (cost per session × points per dollar))`. |
| `ALLOWANCE_STOP_7D` | `98` (`DEFAULT_STOP` in `scripts/allowance.py`) | The same for the 7-day window. |
| `LEAN_AT_5H` | `60` (`DEFAULT_LEAN_AT` in `scripts/allowance.py`) | Estimated 5-hour use, in percent, from which `FORECAST_MODE=auto` runs lean sessions. |
| `LEAN_AT_7D` | `75` (`DEFAULT_LEAN_AT` in `scripts/allowance.py`) | The same for the 7-day window. |
| `WEEKLY_BUDGET_USD_EQUIV` | unset (= no budget) | Trailing-7-day API-equivalent spend at which the gate stops starting sessions; from 80 % of it, at most 2 questions per run. Set it after measuring a round (`uv run scripts/record_usage.py report`). |
| `PAGE_ENABLED` | unset (= off) | Publishes the results page (`publish-page.yml`) to GitHub Pages after every daily sync and on pushes to `main` that touch the data, when exactly `true`. Manual runs ignore it. Needs Settings → Pages → Source: **GitHub Actions** once, and a plan that offers Pages for the repository; the site is public even when the repository is private. |
| `CLAUDE_CODE_VERSION` | `latest` | npm version of `@anthropic-ai/claude-code`. Unpinned by default so new models and fixes arrive on their own; pin a version (e.g. `2.1.302`) if a release breaks the sweep. Each job prints the version it installed in its Step Summary. |

## Fixed in files, not variables

| Setting | Where | Value |
|---|---|---|
| Sweep cadence | `.github/workflows/tournament-sweep.yml` (`cron`) | every 30 min, at :11 and :41 |
| Daily sync time | `.github/workflows/tournament-sync.yml` (`cron`) | 03:23 UTC |
| Results page rebuild | `.github/workflows/publish-page.yml` (`on:`) | after every tournament-sync run; pushes to `main` touching `ledger/`, `meta.yaml` or the builder |
| Research subagent model | `.claude/agents/research-scout.md` (`model:`) | `sonnet` |
| Research floor for one-shot questions | `scripts/log_forecast.py` (`MIN_SEARCHES`, `REQUIRED_CATEGORIES`, `WAIVER_MINUTES`) | `MIN_SEARCHES` = `15` searches done (`$RESEARCH_MIN_SEARCHES` replaces it; the sweep sets it only in lean mode); at least one done in each of `REQUIRED_CATEGORIES` = `resolution_source`, `news`, `markets`, `base_rate`, `disconfirmation` (one naming the assumption it tests in `tests`); an `adjustments` list with each event once; waived `WAIVER_MINUTES` = `8` min before `$FORECAST_DEADLINE`, or once `MAX_WEB_SEARCHES` is used |
| PDF extraction | `pyproject.toml` group `research` (`pymupdf4llm`), `scripts/pdf_text.py` | pinned `1.28.2`; first 30 pages unless `--pages` |
| Tool permissions of the forecaster session | `.claude/settings.ci.json` | allowlist; `dontAsk` mode |
| Search budget hook | `.claude/settings.ci.json` (`hooks.PreToolUse`, `hooks.SubagentStart`, `hooks.SubagentStop`), `scripts/search_budget.py` | runs as `.venv/bin/python -I`; counts `WebSearch`/`WebFetch`/`Agent` calls and tracks running subagents (and counts their starts) in `$RUNNER_TEMP/search-budget.json` (atomic replace under a `.lock` file); states the caps on an agent's first search, counts down from `NUDGE_SHARE` of a cap; fails open without the file |
| Research-scouts per session | `scripts/search_budget.py` (`MAX_SCOUTS`) | `MAX_SCOUTS` = `5`; a further `Agent` call from the main agent is refused |
| Logging waits for running scouts | `scripts/log_forecast.py` (`_check_scouts`, `WAIVER_MINUTES`) | `add` on a one-shot question is refused while a subagent the hook saw start has not stopped; waived `WAIVER_MINUTES` before `$FORECAST_DEADLINE` |
| Which tournaments are polled, in what priority | `tournaments/registry.yaml` (`uv run scripts/tournament_registry.py`) | `minibench` active |
| Too late to start a question | `scripts/tournament_poll.py` (`MIN_MINUTES_LEFT`) | 20 minutes before close |
| Lean mode | `.github/workflows/tournament-sweep.yml`, forecast job (when `matrix.q.mode == 'lean'`) | no research-scouts (`--disallowedTools Agent Task`), `--effort medium`, `RESEARCH_MIN_SEARCHES` = `6`, `MAX_WEB_SEARCHES` = `10`, `MODEL_LEAN` if set, and the prompt adds "Research mode: lean — follow SKILL.md § Lean mode." |
| Cost per session, for the allowance cap | `scripts/allowance.py` (`PRIOR_COST`, `COST_WINDOW`, `COST_MIN_SAMPLES`) | median `cost_usd_equiv` of the last `COST_WINDOW` = `20` sessions of the mode (`config.mode` in `ledger/usage.jsonl`); `PRIOR_COST` (deep $1.7, lean $0.6) until `COST_MIN_SAMPLES` = `3` exist |
| A refused session with no reset time | `scripts/allowance.py` (`decide`) | the next sweep starts one lean probe, not a full batch |

## Manual run inputs (Actions → tournament-sweep → Run workflow)

| Input | Effect |
|---|---|
| `tournament` | Poll only this slug, e.g. `bot-testing-area` (registered or not). |
| `post_ids` | Forecast only these posts (still subject to every guard). |
| `max_questions` | Cap for this run, overriding `MAX_QUESTIONS_PER_RUN`. The allowance cap still applies. |
| `mode` | `auto`, `deep` or `lean` for this run, overriding `FORECAST_MODE`. |
| `dry_run` | Forecast, upload the question folder and the search-budget file (`_temp/search-budget.json` in the archive) as an artifact, submit and commit nothing. |

## Local use

| Variable | When |
|---|---|
| `METACULUS_API_KEY` (or `METACULUS_TOKEN`) | Any script that calls Metaculus (`metaculus_api.py`, `new_question.py`, `tournament_poll.py`). Reading is harmless; `submit_metaculus.py` without `--dry-run` posts for real. |
