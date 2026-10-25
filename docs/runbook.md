# Runbook — when something is red

| Symptom | Likely cause | First thing to do |
|---|---|---|
| Sweep runs but every gate says `nothing_open` | No open tournament questions (normal in MiniBench's second week) | Nothing. `uv run scripts/metaculus_api.py open minibench` to confirm |
| Gate fails: `[auth] no token (set METACULUS_API_KEY)` | The secret is missing, or stored as an *environment* secret; the job log then shows `METACULUS_API_KEY: ` empty | Add it under Settings → Secrets and variables → Actions → **Repository secrets** (same for `CLAUDE_CODE_OAUTH_TOKEN`) |
| Gate fails: "Metaculus token refused" | `METACULUS_API_KEY` wrong, rotated or revoked | Regenerate in Metaculus → Settings → My Forecasting Bots; update the secret |
| Gate fails: "Cloudflare challenge" | Metaculus' edge blocked the runner's IP range | Wait; the next cycle retries from another runner. Never work around it (rule) |
| Forecast step logs `Ignoring 22 permissions.allow entries from .claude/settings.json: this workspace has not been trusted` | Expected. The runner's checkout is never marked trusted, so the CLI drops the *interactive* allowlist and the session runs on `.claude/settings.ci.json` alone, as designed | Nothing. Do **not** set `hasTrustDialogAccepted`: it would add `Bash(uv run:*)` and `Bash(python3 scripts/:*)` to the forecaster's allowlist |
| Forecast step fails at once with an auth error | `CLAUDE_CODE_OAUTH_TOKEN` expired | `claude setup-token`, update the secret |
| `reason=budget_exceeded` in the gate summary | Trailing-7-day spend ≥ `WEEKLY_BUDGET_USD_EQUIV` | `uv run scripts/record_usage.py report`; raise the budget or wait (rolling window) |
| Nothing runs at all, no failed runs | Actions spending limit hit (private repo), or `SWEEP_ENABLED` not `true` | Settings → Billing → Spending limits; Settings → Variables |
| Sweeps hours apart, Actions lists only `schedule` runs | The cron-job.org jobs fail or were disabled (it disables a job after 25 failures in a row), most often an expired token (401) | cron-job.org → the job's history; renew the token, re-enable the job. Status codes: `docs/configuration.md`, "External scheduler" |
| Many `missed_window: true` in `INDEX.md` | Cadence too slow, runs queued, or forecasts overrunning | Check run durations; raise `MAX_PARALLEL`; lower `MAX_MINUTES_PER_QUESTION` |
| Submit step: `HTTP 400` on a numeric/discrete question | Malformed CDF or bounds the builder did not expect | `uv run scripts/submit_metaculus.py <slug> --dry-run`; `uv run pytest tests/test_submit_metaculus.py` |
| Submit step: "already live" | An earlier run submitted but its record was lost | Nothing to resubmit (rule). Note it; the sync warns about it daily |
| Submit step: "no forecast logged" | The session timed out or never ran `log_forecast.py add` — or gave up after a **research-floor** refusal | Read the run's Step Summary; check `permission_denials` in `ledger/usage.jsonl` and the question's `raw/research-log-*.json`. The floor waives itself 8 minutes before the deadline, so a session that keeps going always logs |
| `web_searches` low or `subagents` 0 in `ledger/usage.jsonl` | The model is stopping early despite the floor (or the CLI stopped reporting `subagent_stats`: `subagents` is then `null`) | Compare with `raw/research-log-*.json` of the same question; tighten `.claude/skills/tournament-forecast/SKILL.md`, never per question (tournament rule) |
| `pdf_text.py`: "did not return a PDF" / connection reset | The URL is an HTML landing page, or the host's bot shield dislikes the agent | Use `WebFetch` on the page; the script sends a generic `pdf-text/1.0` user agent on purpose (a `Mozilla/…` agent over Python's TLS gets reset by USDA's shield) |
| Commit step: "validation failed" | A data test failed on the bot's new files (often a malformed `forecast.md`) | The state was committed anyway (by design). Fix the file by hand on `main`, or the template/skill if it recurs |
| Commit step: "could not push" | Five rebase/push attempts lost to concurrent pushes, or branch protection on `main` | Re-run the job's commit by hand from the logs; check branch protection allows `github-actions[bot]` |
| Forecasts land but `comment_posted: false` | Comment API error | The daily sync retries; if it keeps failing, `uv run scripts/submit_metaculus.py <slug> --dry-run` shows the comment |
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
It stops the cron-job.org dispatches only because they send `scheduled: true`; a job whose
body lost that input runs regardless, so pause the cron-job.org jobs as well.
