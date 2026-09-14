# Bot migration — step tracker

Companion to [`bot-migration-plan.md`](bot-migration-plan.md). The plan says **what** to build
and why; this file says **what is done** and gives every unit of work a stable handle.

**How to use it**: say *"implement step P1.2"*. Steps are numbered `P<phase>.<n>` and the number
never changes once assigned — if the plan is revised, a step is marked `dropped` or a new one is
appended, never renumbered.

**Rules for whoever works on a step:**

1. Read the plan section named in the step's **Plan §** column before starting. The plan is the
   contract; this file is only the index.
2. Do not start a step whose `Blocked by` is unmet. Phases are ordered by dependency.
3. On finishing, update the step's row here (status, date, commit) **in the same commit** as the
   work. A tracker that lags the code is worse than no tracker.
4. If a step turns out to be wrong or impossible as written, mark it `blocked` with a one-line
   reason in **Notes** and say so to the operator. Do not silently redefine it.

**Status vocabulary**: `todo` · `in progress` · `done` · `blocked` · `deferred` (correct, but
belongs to a later phase than the plan says) · `dropped` (no longer wanted).

---

## Progress at a glance

| Phase | Name | Steps | Done |
|---|---|---|---|
| **M** | Operator setup (manual — not agent work) | 5 | 0 / 5 |
| **P0** | Clean the state, delete dead weight | 8 | 5 / 8 |
| **P1** | Metaculus API layer | 5 | 0 / 5 |
| **P2** | Schema changes | 3 | **3 / 3** |
| **P3** | Skills | 5 | 0 / 5 |
| **P4** | Subagents, models, gate, usage accounting | 6 | 0 / 6 |
| **P5** | Failure handling and budget guards | 6 | 0 / 6 |
| **P6** | Data integrity: validator, pre-commit, fast tests | 4 | 0 / 4 |
| **P7** | GitHub Actions workflows | 5 | 0 / 5 |
| **P8** | Docs | 3 | 0 / 3 |
| **P9** | Soak and go live | 4 | 0 / 4 |
| | | **54** | **8** |

Recommended order: P0 → P1.1–P1.2 → P2 → P1.3–P1.5 → P6 → P3 → P4 → P5 → P7 → P8 → P9.
P6 lands before P3 on purpose: the validator guards every later phase from its first commit.

---

## M — Operator setup (human only, no agent can do these)

Plan §3. **[blocking]** items stop the phase named in *Blocks*.

| Step | Task | Plan § | Blocks | Status |
|---|---|---|---|---|
| M.1 | Create the Metaculus **bot account**, register it at `/futureeval/participate/`, copy the API token | 3.1 | P1, P9 | todo |
| M.2 | `claude setup-token` → `CLAUDE_CODE_OAUTH_TOKEN`; install the Claude GitHub App; calendar reminder for token expiry | 3.2 | P7 | todo |
| M.3 | Repo secrets: `CLAUDE_CODE_OAUTH_TOKEN`, `METACULUS_BOT_TOKEN` | 3.3 | P7 | todo |
| M.4 | Create the `live-bot` branch; keep `main` default; set a **non-zero Actions spending limit** with a 75% alert | 3.5 | P7 | todo |
| M.5 | Repo variables (models, `MAX_*`, `WEEKLY_BUDGET_USD_EQUIV`, `SWEEP_ENABLED`) — all optional, defaults exist | 3.4 | — | todo |

> M.4's spending limit defaults to **$0** on most accounts, which stops every workflow
> mid-month with no failed run to notice. It is the one setup item with a silent failure mode.

---

## P0 — Clean the state, delete dead weight

Plan §5.

| Step | Task | Plan § | Status | Done | Notes |
|---|---|---|---|---|---|
| P0.1 | `git rm -r questions/*/`, add `questions/.gitkeep` | 5.1 | blocked | | Blocked on a Bash permission rule in this session — the operator must run it or grant `Bash(git rm:*)` |
| P0.2 | Truncate `ledger/forecasts.jsonl`; regenerate `INDEX.md` via `status.py --index` | 5.1 | blocked | | Same permission block |
| P0.3 | Make the test suite pass on empty state | 5.1 | **done** | 2026-09-13 | `test_ledger_is_append_only_against_the_last_commit` now exempts a *fully* empty working copy; a partial line drop still fails |
| P0.4 | Delete `.claude/skills/metaculus-scraper/` and its `SKILLS.md` row | 5.2 | blocked | | Docs references removed 2026-09-13; the directory deletion is blocked |
| P0.5 | Delete `.claude/commands/review.md` (`/review`) and its references | 5.2 | blocked | | Docs references removed 2026-09-13; the file deletion is blocked |
| P0.6 | Remove the **whole visualization path**: `matplotlib`, `calibration.py --plot`, `charts/` creation, the "add a chart" instruction | 5.2 | **done** | 2026-09-14 | Widened past the plan on operator instruction — the plan only moved matplotlib to an optional group. See *Deviations* below |
| P0.7 | Gut the Playwright/Cloudflare path in `metaculus_aggregations.py`; drop the `playwright` dependency | 5.2 | deferred → P1.5 | | Its replacement is `metaculus_api.py`, which is P1.1. Doing it here leaves **no working Metaculus access at all** until P1 lands |
| P0.8 | Skip `research.md` for tournament questions | 5.2 | **done** | 2026-09-14 | Landed with P2.1, as deferred. `new_question.py --tournament <slug>` with `--tournament-mode one_shot` does not scaffold `research.md`, and `test_scaffolded_files_all_exist` exempts exactly those questions |

---

## P1 — Metaculus API layer

Plan §6. The riskiest code in the migration; build and test it in isolation.

| Step | Task | Plan § | Blocked by | Status |
|---|---|---|---|---|
| P1.1 | `scripts/metaculus_api.py` — token client: `list_tournament_posts`, `get_post`, `my_forecast_exists`, `submit_forecast`, `post_comment`, `get_tournament`, `get_aggregations`. Typed `MetaculusError` / `MetaculusAuthError`; one retry on 5xx, **none on 4xx**. Add `requests>=2.32` | 6.1 | M.1 | todo |
| P1.2 | `scripts/metaculus_cdf.py` — **port** `Percentile`/`NumericDistribution` from the bot template, do not rewrite. Plus `tests/test_cdf.py`: monotonicity, length 201, endpoints, open/closed bounds, `zero_point`, non-monotone rejection | 6.2 | P1.1 | todo |
| P1.3 | `scripts/metaculus_submit.py` — deterministic submit + private comment for one slug, `--dry-run`, four one-shot guards, `missed_window` exit 0, comment-failure exit 0 | 6.3 | P1.1, P1.2, P2.1, P2.2 | todo |
| P1.4 | Verify §16 open questions 2–4: `aggregation_explorer` auth path and params; comment length limit and `included_forecast` ordering; bot-token rate limits | 16.2–16.4 | P1.1 | todo |
| P1.5 | Rewrite `metaculus_aggregations.py` as a thin wrapper over `metaculus_api.py` (same CLI, same `fetch_aggregations()` signature); strip the Cloudflare essay from SKILL.md; drop `playwright`; delete the scraper skill | 6.4 | P1.1, P0.4 | todo |

---

## P2 — Schema changes

Plan §7.

| Step | Task | Plan § | Blocked by | Status | Done | Notes |
|---|---|---|---|---|---|---|
| P2.1 | `meta.yaml`: add `question_id`, the `tournament` block, `percentiles`. Update `templates/meta.yaml`, `conftest.py`'s `META_KEYS`, and the five new `test_meta.py` cases | 7.1 | — | **done** | 2026-09-14 | All five cases landed, plus a registry cross-check and a percentile/IQR agreement check. Writers added so the fields are not write-only: `new_question.py --tournament/--question-id` and `log_forecast.py add --p10/--p90`. The 17 legacy folders were migrated; see deviations D5–D6 |
| P2.2 | Ledger: third event type `submission`. Extend `EVENTS`; assert every `submission` has a preceding `forecast` and **no slug has two** | 7.2 | — | **done** | 2026-09-14 | Both invariants landed, plus record shape, 2xx-only, and `meta.tournament` ↔ ledger agreement in `test_consistency.py`. Writer: `log_forecast.py submit`, which P1.3 calls rather than appending itself (deviation D7) |
| P2.3 | `tournaments/registry.yaml` + `scripts/tournament_registry.py` — multi-tournament from day one, with `priority` and `mode` | 7.3 | — | **done** | 2026-09-14 | CLI `list/get/add/set/touch` + module API (`active_tournaments()`, `mark_seen()`) for the P4.3 gate. Seeded with `bot-testing-area` (active) and `minibench` (**parked**, see D8) |

---

## P3 — Skills

Plan §8.

| Step | Task | Plan § | Blocked by | Status |
|---|---|---|---|---|
| P3.1 | `add-tournament` skill + `/add-tournament` command — thin wrapper over `tournament_registry.py add <url>` | 8.1 | P2.3, P1.1 | todo |
| P3.2 | `update-tournament` skill — daily reconcile: roster, new questions at v0, missed windows, comment retries, resolutions with **official peer scores**, criteria drift, `INDEX.md` | 8.2 | P3.1, P1.3 | todo |
| P3.3 | `tournament-sweep` skill — the fast path. Resolution digest first, outside view, 2–3 research subagents, 5–8 sources, median + IQR + percentiles, submit, commit once per run | 8.3 | P3.2, P4.1, P5.3 | todo |
| P3.4 | `forecast-workflow`: add the **Mode** step (tournament vs standard); CP recorded as "hidden — bot tournament"; the submit call; the new pre-commit gate | 8.4 | P3.3 | todo |
| P3.5 | `forecast-update`: **hard stop** on a submitted one-shot question; local re-analysis allowed but must never call `metaculus_submit.py` | 8.5 | P2.1 | todo |

---

## P4 — Subagents, models, the gate, usage accounting

Plan §9.

| Step | Task | Plan § | Blocked by | Status |
|---|---|---|---|---|
| P4.1 | `.claude/agents/*.md.tmpl` — `research-scout`, `source-checker`, `resolution-reader`. Read-only tools; hard "never spawn further agents" instruction | 9.1 | — | todo |
| P4.2 | `scripts/render_agents.py` — substitute `{{MODEL_*}}` from env into `.claude/agents/*.md`; gitignore the rendered files | 9.3 | P4.1 | todo |
| P4.3 | `scripts/tournament_poll.py` — the **no-LLM gate**: breaker, budget, token validation, open posts across all tournaments, `my_forecast_exists` filter, priority order, `--github-output` | 9.2 | P2.3, P1.1, P5.4, P5.5 | todo |
| P4.4 | `scripts/record_usage.py` — parse `execution_file` → `ledger/usage.jsonl` + Step Summary. **Defensive**: missing fields ⟹ `parse_failed: true`, never fail the job | 9.4, 16.7 | — | todo |
| P4.5 | `scripts/usage_report.py` — rolling 7/30-day spend table, cost per forecast, `--check` for the budget guard | 9.4 | P4.4 | todo |
| P4.6 | Actions-minutes meter in `record_usage.py` via `BILLING_READ_TOKEN`; verify which billing endpoint this account answers on; `unavailable: true` on failure | 9.5, 16.9 | P4.4 | todo |

---

## P5 — Failure handling and budget guards

Plan §10. **The division of labour is the whole point: Python does all failure handling, the
model does none.**

| Step | Task | Plan § | Blocked by | Status |
|---|---|---|---|---|
| P5.1 | `scripts/record_error.py` + `ledger/errors.jsonl` — one line per failure, every record carrying a working `reproduce` command | 10.2 | — | todo |
| P5.2 | **Secret redaction** in `record_error.py`, with a unit test proving an `Authorization: Token …` header in an error body is redacted | 12.6, 18 | P5.1 | todo |
| P5.3 | The seven budget rules, verbatim, in `tournament-sweep/SKILL.md`; `scripts/budget.py --remaining` | 10.3 | — | todo |
| P5.4 | The weekly spend guard: `usage_report.py --check`, 80% soft landing (`MAX_FORECASTS_PER_RUN` → 2), rolling reset | 10.4 | P4.5 | todo |
| P5.5 | Circuit breaker `ledger/health.json` — 3 failed sweeps ⟹ 6 h open; auth failure ⟹ 24 h. Plus the single reused `bot-health` issue | 10.5 | P5.1 | todo |
| P5.6 | The Actions-minutes guard: 85% ⟹ skip unscored tournaments, 95% ⟹ skip all sweeps. **Delete this step's code when the repo goes public** | 10.7 | P4.6, P4.3 | todo |

---

## P6 — Data integrity

Plan §11. Land this **before** P3 so every later phase is guarded from its first commit.

| Step | Task | Plan § | Blocked by | Status |
|---|---|---|---|---|
| P6.1 | `scripts/validate_state.py` — one validator, two callers. `--changed` mode | 11.1 | P2.1, P2.2, P2.3 | todo |
| P6.2 | `.pre-commit-config.yaml` (ruff, yaml/json, validate-state, fast tests). **Never run `pre-commit` in CI** | 11.2 | P6.1 | todo |
| P6.3 | `scripts/ci_commit.sh` — `ruff` → `validate_state --changed` → fast tests → commit → rebase-push with 4-attempt backoff | 11.2 | P6.1 | todo |
| P6.4 | `--changed-only` pytest option in `conftest.py`, on by default under `CI_FAST=1`; sync job runs the full suite | 11.3 | — | todo |

---

## P7 — GitHub Actions

Plan §12. **Add `workflow_dispatch` first and `schedule:` last** — no `cron` line until the gate
(P4.3) and the guards (P5.4, P5.5) exist and all three workflows have run green manually.

| Step | Task | Plan § | Blocked by | Status |
|---|---|---|---|---|
| P7.1 | Branch strategy: `live-bot` write target, `merge origin/main` per job, shared `concurrency: live-bot-writer`, extend `tests.yml` to `live-bot` | 12.1 | M.4 | todo |
| P7.2 | `tournament-sweep.yml` — gate job + Claude job, `CI_FAST=1`, usage recording, failure reporting | 12.2 | P4.3, P3.3, P6.3 | todo |
| P7.3 | `tournament-sync.yml` — daily 03:23 UTC, full test suite, `timeout-minutes: 45` | 12.3 | P3.2, P6.3 | todo |
| P7.4 | `triage.yml` — Tue/Fri; `status.py --act` must **skip `one_shot` questions** | 12.4 | P3.5, P2.1 | todo |
| P7.5 | Verify §16.6: `claude-code-action`'s human-actor check attributes scheduled runs to whoever last edited the `cron` line — confirm that is a human account | 16.6 | P7.2 | todo |

---

## P8 — Docs

Plan §15. Do these as the phases land, not in one lump at the end.

| Step | Task | Plan § | Status |
|---|---|---|---|
| P8.1 | `docs/tournament-protocol.md` (NEW) — 90-minute window, one shot, private comment format, hidden CP, MiniBench vs FutureEval, missed windows | 15 | todo |
| P8.2 | `docs/runbook.md` (NEW) — the symptom→command table | 10.8 | todo |
| P8.3 | Amend `AGENTS.md` (operating modes, §4, §5, rule 8 carve-out), `CLAUDE.md`, `methodology.md`, `update-protocol.md`, `output-format.md`, `SKILLS.md`, `README.md` | 15 | **partly done** — see note |

> **P8.3, partial (2026-09-14).** P2 landed schema rules the docs contradicted, so the
> contradictions were fixed with it rather than left for later: the one-shot carve-out to rule 3
> and the ledger's three event types in `AGENTS.md`, the tournament pointer in `update-protocol.md`,
> the new layout and script rows in `README.md`/`SKILLS.md`, and the new invariants in
> `tests/README.md`. P8.3 still owns everything else on its list — operating modes, §4 and §5 of
> `AGENTS.md`, `methodology.md` and `output-format.md` — which depends on P1 and P3 existing.

---

## P9 — Soak and go live

Plan §19 step 10, §18.

| Step | Task | Plan § | Blocked by | Status |
|---|---|---|---|---|
| P9.1 | Register `bot-testing-area`; run the full definition-of-done checklist (§18) against it | 18 | P7 | todo |
| P9.2 | Soak on `bot-testing-area` for a week. Confirm `SWEEP_ENABLED=false` stops the sweep within one cycle, and `WEEKLY_BUDGET_USD_EQUIV=0` starts no Claude job | 19 | P9.1 | todo |
| P9.3 | Register `minibench`; run one full round end to end; **measure real cost per forecast** over two rounds before deciding Sonnet vs Opus | 19, 16.8 | P9.2 | todo |
| P9.4 | Register the Fall 2026 FutureEval season once its slug is public (§16.1 — not knowable today) | 16.1 | P9.3 | todo |

---

## Deviations from the plan

Recorded here rather than edited into the plan, so the plan stays the written contract and the
divergence stays visible.

| # | Plan says | We did | Why |
|---|---|---|---|
| D1 | §5.2: move `matplotlib` to an optional `viz` group | Removed the visualization path **entirely** — the dependency, `calibration.py --plot`, `charts/` directory creation, and the "add a chart" instruction in `AGENTS.md` §7 and `forecast-workflow` | Operator instruction, 2026-09-14: keep it simple. An optional group is still a code path to maintain, and the bot has no reader who needs a figure. Also removes the binary-file problem in the GitHub MCP push fallback |
| D2 | §5.2 puts the `metaculus_aggregations.py` gutting and the `playwright` removal in Phase 0 | Deferred to **P1.5** | §6.4 defines the replacement as a wrapper over `metaculus_api.py`, which is P1.1, and §19's own ordering agrees. Doing it in P0 leaves the repo with no working Metaculus access for the whole gap |
| D3 | §5.2 puts skipping `research.md` for tournament questions in Phase 0 | Deferred to **P2.1** | Conditioned on `tournament.mode == one_shot`, which P2.1 introduces. Nothing can identify a tournament question today |
| D4 | §5.1: `git worktree prune`, delete local `testing` and `claude/us-model-evaluations-forecast-672746` | Not applicable in CI | Those live on the operator's Windows machine, not in the container. Operator to run locally |
| D5 | §7.1: "`question_id` is an int whenever `source == metaculus`" | Enforced, with **one named exemption** in `test_meta.py` (`GROUP_FOLDER_EXEMPTIONS`) | `questions/2026-09-04-mc45386-givewell-…` is a single folder covering *two* subquestions of one group post, so no single `question_id` describes it. The bot scaffolds one folder per subquestion (the SPR pair is the precedent), so the rule is right going forward and this is legacy debt. The exemption list empties itself when P0.1 clears `questions/` |
| D6 | The plan does not say where the legacy `question_id`s come from | Backfilled from each folder's own `raw/*.json` snapshots, not re-fetched | Rule 4 ("fresh data only") governs *forecast* numbers; a Metaculus question id is an immutable identifier, and the repo's own snapshot trail is a better source than a live fetch that Cloudflare 403s today (D2). 16 of 17 resolved this way |
| D7 | §7.2 defines the `submission` record; §6.3 gives the writer to `metaculus_submit.py` (P1.3) | Added `log_forecast.py submit` now, as the only writer | An event type with no producer is not a schema, it is a comment. Writing the ledger line and `meta.tournament.{submitted, submitted_forecast, comment_posted}` in one place is also what lets `test_consistency.py` assert they agree. P1.3 keeps its job — call the API — and calls this to record the result |
| D8 | §7.3's example registry has MiniBench `active: true` | Seeded `active: false` | §19/P9 soaks on `bot-testing-area` first and only registers MiniBench at P9.3. An active MiniBench row would let the first working sweep (P4.3) spend real, *scored* forecasts before the soak. P9.3 flips it with `tournament_registry.py set minibench --active` |

**Writers added ahead of their phase**: P2 is a schema phase, but three small writers landed
with it — `new_question.py --tournament`, `log_forecast.py add --p10/--p90`, and
`log_forecast.py submit`. Each exists so that a schema field has exactly one producer and the
test suite can hold two records against each other; none of them talks to Metaculus, which stays
P1's job.

**Known inconsistency while P0.4 is blocked**: the docs no longer mention a Metaculus fallback,
but `.claude/skills/metaculus-scraper/` still exists on disk and `metaculus_aggregations.py`
still carries its Playwright path. This resolves at P1.5.
