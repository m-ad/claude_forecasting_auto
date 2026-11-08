# Runbook — when something is red

| Symptom | Likely cause | First thing to do |
|---|---|---|
| Sweep runs but every gate says `nothing_open` | No open tournament questions (normal in MiniBench's second week) | Nothing. `uv run scripts/metaculus_api.py open minibench` to confirm |
| Gate fails: `[auth] no token (set METACULUS_API_KEY)` | The secret is missing, or stored as an *environment* secret; the job log then shows `METACULUS_API_KEY: ` empty | Add it under Settings → Secrets and variables → Actions → **Repository secrets** (same for `CLAUDE_CODE_OAUTH_TOKEN`) |
| Gate fails: "Metaculus token refused" | `METACULUS_API_KEY` wrong, rotated or revoked | Regenerate in Metaculus → Settings → My Forecasting Bots; update the secret |
| Gate fails: "Cloudflare challenge" | Metaculus' edge blocked the runner's IP range | Wait; the next cycle retries from another runner. Never work around it (rule) |
| Forecast step logs `Ignoring 22 permissions.allow entries from .claude/settings.json: this workspace has not been trusted` | Expected. The runner's checkout is never marked trusted, so the CLI drops the *interactive* allowlist and the session runs on `.claude/settings.ci.json` alone, as designed | Nothing. Do **not** set `hasTrustDialogAccepted`: it would add `Bash(uv run:*)` and `Bash(python3 scripts/:*)` to the forecaster's allowlist |
| Forecast step fails at once with an auth error | `CLAUDE_CODE_OAUTH_TOKEN` expired | `claude setup-token`, update the secret |
| `reason=allowance_exhausted until <time>` in the gate summary, one `bot-health` comment per exhaustion | The estimated Claude allowance passed `ALLOWANCE_STOP_5H`/`_7D`, or the last session was refused with a known reset (`scripts/allowance.py`) | Nothing: the sweep resumes on its own after `<time>`. `uv run scripts/allowance.py` shows the estimate. If sessions are refused *before* the gate stops, lower `ALLOWANCE_5H_USD_EQUIV`; if it stops long before any refusal, raise it |
| `reason=allowance_lean` / `allowance_low` | The allowance is tight: lean sessions only, or no room for even one before the stop line | Intended. `FORECAST_MODE=deep` (or the run's `mode` input) forces deep sessions; the stop line still applies |
| `reason=allowance_refused_probe`, one session per sweep | The last session was refused and the ledger has no reset time for it (the CLI's rate-limit events are not recorded yet, issue #20) | Intended: one lean probe a sweep finds when the window is back. A refused probe still fails its job and comments on `bot-health` |
| `reason=budget_exceeded` in the gate summary | Trailing-7-day spend ≥ `WEEKLY_BUDGET_USD_EQUIV` | `uv run scripts/record_usage.py report`; raise the budget or wait (rolling window) |
| Nothing runs at all, no failed runs | Actions spending limit hit (private repo), or `SWEEP_ENABLED` not `true` | Settings → Billing → Spending limits; Settings → Variables |
| Many `missed_window: true` in `INDEX.md` | Cadence too slow, runs queued, or forecasts overrunning | Check run durations; raise `MAX_PARALLEL`; lower `MAX_MINUTES_PER_QUESTION` |
| Submit step: `HTTP 400` on a numeric/discrete question | Malformed CDF or bounds the builder did not expect | `uv run scripts/submit_metaculus.py <slug> --dry-run`; `uv run pytest tests/test_submit_metaculus.py` |
| Submit step: "already live" | An earlier run submitted but its record was lost | Nothing to resubmit (rule). Note it; the sync warns about it daily |
| `log_forecast.py add`: "N subagent(s) still running" | A scout had not finished, or its `SubagentStop` never reached the hook | Intended while scouts work: the session waits for their digests. If it recurs with no scout running (a lost `SubagentStop`), the waiver still logs `WAIVER_MINUTES` before the deadline; check `active_agents` in the budget file of a `dry_run` |
| `ledger/usage.jsonl`: `subagents_started` below `scouts_spawned`, or `subagents_running_at_exit` > 0 | The `SubagentStart` or `SubagentStop` hook did not reach `scripts/search_budget.py` (CLI change), or a scout was still running when the session was killed | With starts missing, `log_forecast.py` cannot see running scouts and its wait does nothing; with stops missing, logging waits for the deadline waiver. Check the CLI version in the Step Summary and the `hooks` in `.claude/settings.ci.json` |
| "Search budget used" refusals in the transcript; `search_calls_denied` > 0 in `ledger/usage.jsonl` | The session reached `MAX_WEB_SEARCHES`, a scout `MAX_WEB_SEARCHES_PER_SCOUT`, the scouts their share (the cap less the main agent's reserve), or the main agent `MAX_SCOUTS` spawns (`scripts/search_budget.py`) | Intended. If forecasts get thin, compare `search_tool_calls` with `web_searches` (billed) and raise the variable; `0` removes a cap |
| Step Summary: "budget file unreadable: the hook ran, its counts are lost" | The hook ran, but `$RUNNER_TEMP/search-budget.json` is not valid JSON (the hook writes it atomically, so most likely the session's Python overwrote it) | The caps restarted from 0 when the hook next read it; look for `uv run python` writing to `$RUNNER_TEMP` in the transcript |
| Step Summary: "no budget file: the search-budget hook did not run" | The hooks in `.claude/settings.ci.json` did not fire (CLI change, hooks disabled) or could not start (`.venv/bin/python` missing: the install step's `uv sync` failed) — searches were not capped | Check the CLI version in the Step Summary; run a `dry_run` and look for `search-budget` in the transcript; pin `CLAUDE_CODE_VERSION` if a release dropped hooks |
| Submit step: "no forecast logged" | The session timed out or never ran `log_forecast.py add` — or gave up after a **research-floor** refusal | Read the run's Step Summary; check `permission_denials` in `ledger/usage.jsonl` and the question's `raw/research-log-*.json`. The floor waives itself 8 minutes before the deadline, so a session that keeps going always logs |
| `web_searches` low or `subagents` 0 in `ledger/usage.jsonl` | The model is stopping early despite the floor (or the CLI stopped reporting `subagent_stats`: `subagents` is then `null`) | Compare with `raw/research-log-*.json` of the same question; tighten `.claude/skills/tournament-forecast/SKILL.md`, never per question (tournament rule) |
| `pdf_text.py`: "did not return a PDF" / connection reset | The URL is an HTML landing page, or the host's bot shield dislikes the agent | Use `WebFetch` on the page; the script sends a generic `pdf-text/1.0` user agent on purpose (a `Mozilla/…` agent over Python's TLS gets reset by USDA's shield) |
| Commit step: "validation failed" | A data test failed on the bot's new files (often a malformed `forecast.md`) | The state was committed anyway (by design). Fix the file by hand on `main`, or the template/skill if it recurs |
| Commit step: "could not push" | Five rebase/push attempts lost to concurrent pushes, or branch protection on `main` | Re-run the job's commit by hand from the logs; check branch protection allows `github-actions[bot]` |
| Forecasts land but `comment_posted: false` | Comment API error | The daily sync retries; if it keeps failing, `uv run scripts/submit_metaculus.py <slug> --dry-run` shows the comment |
| publish-page fails at `configure-pages`: "Get Pages site failed" | GitHub Pages is not enabled for Actions, or the plan offers no Pages for a private repository | Settings → Pages → Build and deployment → Source: **GitHub Actions**; otherwise unset `PAGE_ENABLED` |
| The Pages site serves the repository's own files (`INDEX.html`, `ledger/*.jsonl`, `questions/…/forecast.html`) instead of the results page | Settings → Pages → Source is **Deploy from a branch**: GitHub's own Jekyll build then publishes the branch itself on every push, and `publish-page.yml` cannot deploy over it | Switch Source to **GitHub Actions**, then run publish-page once; its deployment replaces the branch-built site |
| Results page says "Leaderboards unavailable: …" | A Metaculus error or a changed leaderboard response; the page was published without ranks | The note carries the error. `uv run scripts/build_page.py --out _site` locally with the token reproduces it |
| Results page: rank "not listed; ~N of M (estimate)" | The bot has no entry on the tournament's leaderboard (Metaculus excluded it, or has not counted it yet); N places the sum of its synced peer scores among the ranked entries | Check the bot's eligibility with Metaculus (participation form, bot approval). The estimate is not an official rank |
| Open `bot-health` issue | Any of the above | The issue lists run links; start from the newest |

## Actions minutes (private repository)

GitHub bills each job rounded up to a whole minute. The gate runs 48×/day ≈ 1,440 minutes a
month on its own; each forecast job is ~2 minutes of setup plus the forecast (≤ 25). At ~150
tournament questions a month that is roughly 1,440 + 150 × 20 ≈ 4,400 minutes, against 2,000
(Free) or 3,000 (Pro) included; overage on Linux runners was $0.006/minute when the plan was
written (≈ $10–15/month — check current GitHub pricing). A **public** repository has unlimited
minutes. With a $0 spending limit the schedule simply stops mid-month.

## Kill switch

Repository variable `SWEEP_ENABLED` ≠ `true` stops the scheduled sweep and sync from the next
cycle. A running job finishes. Manual runs (Run workflow) still work — that is the smoke test.
