# Bot migration — step tracker

Companion to [`bot-migration-plan.md`](bot-migration-plan.md) (rev 3, 2026-10-17). The plan
says **what** and why; this file says **what is done**, and gives every unit of work a stable
handle.

**How to use it**: say *"implement step P11.2"*. Step numbers never change once assigned: when
the plan is revised a step is marked `dropped`/`superseded` or a new one is appended.

**Rules for whoever works on a step:**

1. Read the plan section named in the step before starting.
2. Do not start a step whose `Blocked by` is unmet.
3. On finishing, update the step's row here **in the same commit** as the work.
4. If a step is wrong or impossible as written, mark it `blocked` with a one-line reason and
   say so to the maintainer. Do not silently redefine it.

**Status vocabulary**: `todo` · `in progress` · `done` · `blocked` · `deferred` · `dropped` ·
`superseded` (replaced by a later step, named in the notes).

---

## Progress at a glance (2026-10-18)

| Phase | Name | State |
|---|---|---|
| **M** | Maintainer setup | M.1–M.8 done (2026-10-18); M.9 open (seasonal) |
| P0 | Clean state, delete dead weight | done (P0.7 done via P10.3) |
| P1 | Metaculus API layer | done, superseded in part by upstream's CDF builder (P10) |
| P2 | Schema | done; re-applied on the new base (P10.4) |
| P3 | Skills | done in rev-3 form (P11) |
| P4 | Subagents, models, gate, usage | done in rev-3 form; P4.2/P4.6 dropped |
| P5 | Failure handling, budget guards | partly done; breaker and error log deferred (P12) |
| P6 | Data integrity | superseded by tests + `ci_commit.sh` |
| P7 | GitHub Actions | sweep run on GitHub (manual smoke test, 2026-10-18); first scheduled sweep and `tournament-sync` not yet observed |
| P8 | Docs | done |
| P9 | Soak and go live | P9.1 done (= M.6); P9.3 is the round starting 2026-10-19 |
| **P10** | Restart from upstream (rev 3) | done |
| **P11** | MiniBench pipeline (rev 3) | done (verified offline + live dry run) |
| **P12** | After the first round | todo |

---

## M — Maintainer setup (human only)

Plan §4. M.1–M.8 done 2026-10-18 (marked by the maintainer): nothing on the maintainer side
stands between `main` and the MiniBench round of 2026-10-19. M.9 recurs every season.

| Step | Task | Status | Notes |
|---|---|---|---|
| M.1 | Metaculus bot account + API token | **done** | `my-claude-forecasting`, `is_bot: true` (API, 2026-10-17); primary-bot setting and participation form included in the maintainer's sign-off, 2026-10-18 |
| M.2 | `claude setup-token` → secret `CLAUDE_CODE_OAUTH_TOKEN`; expiry reminder | **done** | 2026-10-18; the forecast step authenticated in Actions ([run 39119704362](https://github.com/m-ad/claude_forecasting_auto/actions/runs/39119704362), [run 39120996084](https://github.com/m-ad/claude_forecasting_auto/actions/runs/39120996084)) |
| M.3 | Secret `METACULUS_API_KEY` | **done** | 2026-10-18; gate, scaffold and submit authenticated. Renamed from rev 2's `METACULUS_BOT_TOKEN` |
| M.4 | Merge the branch into `main`; no branch protection blocking `github-actions[bot]` | **done** | [PR #4](https://github.com/m-ad/claude_forecasting_auto/pull/4) merged 2026-10-18 (`5bcb529`); `github-actions[bot]` pushed to `main` (`23cff82`, `18a99d7`). Was "create `live-bot`" — dropped with the branch (D10) |
| M.5 | Actions spending limit > $0 + alert (private repo), or make the repo public | **done** | 2026-10-18, maintainer |
| M.6 | Smoke test on `bot-testing-area` (dry run, then real) | **done** | 2026-10-18. Dry run [39119704362](https://github.com/m-ad/claude_forecasting_auto/actions/runs/39119704362) (artifact `dry-run-43326`); real run [39120996084](https://github.com/m-ad/claude_forecasting_auto/actions/runs/39120996084): posts 43326 (multiple choice) and 43323 (numeric) submitted, `comment_posted: true`, HTTP 201. Findings for P12.1 in plan §8 |
| M.7 | `SWEEP_ENABLED=true` | **done** | 2026-10-18 |
| M.8 | `WEEKLY_BUDGET_USD_EQUIV` from measured spend | **done** | 2026-10-18, before the first round; the only measured spend then was the smoke test ($0.22–0.26 per question on `sonnet`, `ledger/usage.jsonl`). Re-derive from the round's spend in P12.3 |
| M.9 | Seasonal bot survey; AskNews renewal if used | todo | required for prizes |

---

## P0–P9 — rev-2 steps, status under rev 3

| Step | Task (rev 2) | Status | Notes |
|---|---|---|---|
| P0.1 | `git rm` question folders | done | 2026-09-14, maintainer (`c1a8693`) |
| P0.2 | Truncate the ledger, regenerate INDEX | done | 2026-09-14 |
| P0.3 | Test suite passes on empty state | done | still holds on the new base |
| P0.4 | Delete `metaculus-scraper` | done | upstream reintroduced it; deleted again in the merge (`27fd744`) |
| P0.5 | Delete `/review` | done | stays deleted on the new base |
| P0.6 | Remove the visualization path | done | re-applied on the new base: no matplotlib, no `--plot`, no `charts/` |
| P0.7 | Gut the Playwright path, drop `playwright` | **done** | 2026-10-17, P10.3: deleted outright instead of wrapped |
| P0.8 | No `research.md` for one-shot questions | done | re-applied (P10.4) |
| P1.1 | `metaculus_api.py` token client | **done** | 2026-10-17. stdlib urllib, typed errors, one 5xx retry, no 4xx retry, 429 backoff, redaction. `get_tournament` uses `/api/projects/tournaments/<slug>/` (the rev-2 path 404s) |
| P1.2 | Port the template's CDF classes + `test_cdf.py` | superseded | upstream's `submit_metaculus.py` builder (point masses, max-step cap, bound rules) with `tests/test_submit_metaculus.py`; verified live against real scalings |
| P1.3 | Deterministic submit + private comment, guards, missed window | **done** | 2026-10-17, inside `submit_metaculus.py` (one-shot path) rather than a new script |
| P1.4 | Verify aggregation explorer, comment limits, rate limits | partly | explorer: moot (no aggregations). Comment POST: works (smoke test, 2026-10-18; plan §8.4); length limit not yet hit. Rate limits: the scripts pace and back off |
| P1.5 | Aggregations as an API wrapper | dropped | no aggregation lookups at all (maintainer instruction) |
| P2.1 | `meta.yaml`: `question_id`, `tournament`, `percentiles` | done | re-applied; `percentiles` replaced by the ledger `distribution` (D12) |
| P2.2 | Ledger `submission` event | done | re-applied; plus a `comment` event for late comments |
| P2.3 | Tournament registry | done | simplified: maintainer-only, no bot-written fields (D11) |
| P3.1 | `add-tournament` skill | dropped | `tournament_registry.py add` is enough for a handful of tournaments |
| P3.2 | `update-tournament` skill (daily reconcile) | superseded | P11.6, deterministic script, no model |
| P3.3 | `tournament-sweep` skill | superseded | P11.4 `tournament-forecast`, one question per session |
| P3.4 | `forecast-workflow` Mode step | done | redirects tournament questions to `tournament-forecast` |
| P3.5 | `forecast-update` hard stop on one-shot | done | |
| P4.1 | Subagent templates | done | `research-scout` only; `source-checker`/`resolution-reader` dropped (criteria are cached to `raw/`) |
| P4.2 | `render_agents.py` | dropped | model alias in frontmatter |
| P4.3 | `tournament_poll.py` gate | **done** | 2026-10-17, stateless; verified live |
| P4.4 | `record_usage.py` | **done** | parses `claude -p --output-format json`; defensive |
| P4.5 | `usage_report.py` | done | as `record_usage.py report` |
| P4.6 | Actions-minutes billing meter | dropped | not worth a PAT and an unstable endpoint; the runbook has the arithmetic |
| P5.1 | `record_error.py` + `errors.jsonl` | deferred | P12.2 |
| P5.2 | Secret redaction | **done** | in `metaculus_api.redact()`, unit-tested; extend to `errors.jsonl` with P12.2 |
| P5.3 | Budget rules in the skill | done | seven rules in `tournament-forecast`; step timeout instead of `budget.py` |
| P5.4 | Weekly spend guard | **done** | in the gate, with the 80 % soft landing |
| P5.5 | Circuit breaker | deferred | P12.2 |
| P5.6 | Actions-minutes guard | dropped | with P4.6 |
| P6.1 | `validate_state.py` | dropped | the data tests are the validator |
| P6.2 | Pre-commit config | deferred | optional, local only |
| P6.3 | `ci_commit.sh` | **done** | plus INDEX regeneration and union merge |
| P6.4 | `--changed-only` pytest | deferred | needed only at a few hundred questions |
| P7.1 | `live-bot` branch strategy | dropped | D10: the bot commits to `main` |
| P7.2 | `tournament-sweep.yml` | **done** | written, actionlint-clean; run on GitHub 2026-10-18 (manual: dry run, then real) |
| P7.3 | `tournament-sync.yml` | **done** | written, actionlint-clean; not yet run on GitHub (first schedule 2026-10-19 03:23 UTC) |
| P7.4 | `triage.yml` | deferred | no long-horizon bot questions yet |
| P7.5 | Verify the action's human-actor check | dropped | CLI instead of the action |
| P8.1 | `docs/tournament-protocol.md` | done | |
| P8.2 | `docs/runbook.md` | done | |
| P8.3 | Amend AGENTS/CLAUDE/methodology/output-format/README/SKILLS | done | 2026-10-17 |
| P9.1 | Definition-of-done checklist on `bot-testing-area` | **done** | = M.6, 2026-10-18 |
| P9.2 | Soak a week on `bot-testing-area` | dropped | no week left before the round; the dry-run + real smoke test replaces it, and MiniBench's first day is watched instead |
| P9.3 | First MiniBench round end to end; measure cost | todo | round of 2026-10-19 |
| P9.4 | Register the Fall 2026 season | done | registered **inactive** (`fall-futureeval-2026`); activation is P12.5 |

---

## P10 — Restart from upstream (rev 3)

| Step | Task | Status | Commit |
|---|---|---|---|
| P10.1 | Merge `upstream/main` (3ef2827) with provenance; keep upstream code/tests/templates, not its questions or ledger | done | `27fd744` |
| P10.2 | Delete browser/scraper/aggregation skills, `fetch_metaculus.py`, fetch-robustness doc, their tests | done | `27fd744` |
| P10.3 | Delete the merge-to-submit workflow and `changed_forecasts.py` (a human approval is a human in the loop); drop playwright/matplotlib | done | `27fd744` |
| P10.4 | Re-apply the fork's schema on upstream: `question_id`, `tournament`, submission/comment events, registry, one-shot tests | done | `27fd744` |
| P10.5 | `new_question.py` from the API; question text cached to `raw/` | done | `27fd744` |

## P11 — MiniBench pipeline (rev 3)

| Step | Task | Status | Commit |
|---|---|---|---|
| P11.1 | One-shot path in `submit_metaculus.py`: guards, forecast, private comment (newest version block), ledger record, missed window | done | `27fd744`, `9fee1ed` |
| P11.2 | Gate `tournament_poll.py` with budget guard | done | `9fee1ed` |
| P11.3 | `tournament-sweep.yml`: matrix per question, CLI, step timeout, no secrets in the model step, dry-run mode, `bot-health` issue | done | `9fee1ed` + docs commit |
| P11.4 | `tournament-forecast` skill, `research-scout` agent, `settings.ci.json` | done | `9fee1ed` |
| P11.5 | `record_usage.py`; `ci_commit.sh` with union merge and INDEX regeneration (simulated with two concurrent clones) | done | `9fee1ed` |
| P11.6 | `tournament_sync.py` + `tournament-sync.yml` | done | `9fee1ed` |
| P11.7 | Live read-only verification: gate, scaffold, payloads for binary/MC/numeric/discrete | done | 2026-10-17, nothing submitted |
| P11.8 | Let the forecaster run Python models (`uv run python`, numpy/scipy); `scripts/ci_guard.py` restores everything outside the question folder before submit; venv rebuilt, git hooks off | done | maintainer review on PR #4, 2026-10-17 |
| P11.9 | Review round on PR #4: submit skill removed (CI is the only submission path); the human is a *maintainer* who only configures; no CP recorded anywhere; `docs/configuration.md` (+ a test that every workflow secret/variable is documented); Claude Code unpinned by default | done | 2026-10-17 |

## P12 — After the first round

| Step | Task | Blocked by | Status |
|---|---|---|---|
| P12.1 | Review the first day's runs: permission denials, timeouts, comment POST, cost per question (plan §8) | M.7 | todo |
| P12.2 | `errors.jsonl` with redaction and `reproduce`; circuit breaker | P12.1 | todo |
| P12.3 | Set `WEEKLY_BUDGET_USD_EQUIV`; decide `MODEL_FORECAST` on measured cost | P9.3 | todo |
| P12.4 | Calibration review on resolved MiniBench questions; backtest prompt changes on closed questions only | round resolves (~2026-11-06) | todo |
| P12.5 | Activate `fall-futureeval-2026` | P12.1 | todo |
| P12.6 | Cache the npm install of Claude Code in the forecast job | — | todo |
| P12.7 | Optional hard isolation: forecaster in a read-only job, submit/commit in a fresh job that takes only the question folder (reusable workflow per matrix entry) | maintainer decision | todo |
| P12.8 | Let the bot forecast individual questions the maintainer adds (updatable mode: sweep or a scheduled update job, plus automated submission of updates) | maintainer decision | todo |

---

## Deviations from the plan

D1–D9 (rev 2) are in git history (`git show 393bda3:docs/bot-migration-progress.md`); their
substance survives in the rows above. New with rev 3:

| # | Plan (rev 2) said | Rev 3 does | Why |
|---|---|---|---|
| D10 | Bot state on `live-bot` | Commits to `main` | Parallel per-question jobs each merging `main` into `live-bot` create duplicate merge commits on rebase; one branch removes that and a setup step |
| D11 | Registry stores `seen_post_ids`, `last_sweep`, `last_sync` | Maintainer-only registry | Stateless gate; no bot writes, no conflicts |
| D12 | `meta.percentiles` + `--p10/--p90` | Ledger `distribution` | Upstream's single, validated record of the full forecast |
| D13 | Comment = 3-line summary | Comment = newest version block | The rules want the comment to represent the reasoning |
| D14 | `claude-code-action` | Claude Code CLI | Simpler auth, no actor checks, cost in the JSON result |
| D15 | Sonnet everywhere | Opus forecaster, Sonnet subagent | Frontier-model effect in the FutureEval survey; measured cost decides (P12.3) |
