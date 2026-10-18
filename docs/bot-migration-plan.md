# Plan: an autonomous Claude Code forecasting bot for the Metaculus bot tournaments

**Revision 3 — 2026-10-17.** Supersedes rev 2 (2026-09-13, in git history: `git show
393bda3:docs/bot-migration-plan.md`). Live status and the numbered step list are in
[`bot-migration-progress.md`](bot-migration-progress.md).
**Target**: compete in **MiniBench** from the round starting **2026-10-19**, then the **Fall
2026 FutureEval** season (`fall-futureeval-2026`, running since 2026-09-28), with Claude Code
driven entirely by GitHub Actions and the official Metaculus API.

---

## 1. What changed since rev 2, and why

| Rev 2 said | Rev 3 does | Why |
|---|---|---|
| Keep developing the September fork | **Restart from upstream `claude_forecasting`**, recorded as a real merge (`27fd744`) | Upstream had moved 168 commits: ledger `distribution`s, a tested Metaculus CDF builder, group sub-questions, Windows stdio fixes. A real merge keeps provenance, so later upstream work arrives as `git merge upstream/main` |
| Keep the Playwright aggregation fetcher until a token client exists (P0.7 → P1.5) | **API only, now.** Browser fetcher, scraper, CP/Pro/gold lookups and `fetch_metaculus.py` are deleted; `scripts/metaculus_api.py` is the single client | Maintainer instruction. Bot tokens cannot see aggregations anyway ([1] "Community Prediction (limited)"), and tournament CPs are hidden until close |
| Questions open for 90 minutes; sweep every 20–30 min | **3-hour windows** [1]; sweep every **30 min** | Verified 2026-10-17. The longer window halves the needed cadence |
| Bot state on a `live-bot` branch, `main` merged in per job | **The bot commits to `main`** | With parallel per-question jobs, a merge of `main` into `live-bot` in every job produced duplicate merge commits on rebase; one branch removes the merge step, the bootstrap step and a manual setup item. Revert = set `BOT_BRANCH` and add the merge step back |
| `anthropics/claude-code-action` | **The Claude Code CLI** (`claude -p --output-format json`) with `CLAUDE_CODE_OAUTH_TOKEN` | No GitHub App token exchange, no actor checks on scheduled runs (rev 2 §16.6), and the JSON result carries cost/usage directly |
| One Claude job forecasts up to 5 questions in sequence | **One matrix job per question**, `MAX_PARALLEL` at once | Context does not accumulate across questions (cheaper), a crash costs one question, each job's cost is measured exactly, and parallelism fits bursts of 5–10 open questions |
| The model calls `metaculus_submit.py` | **Deterministic submit step after the model exits**; the model holds no Metaculus token and no push credential | The irreversible step is never the model's. It also makes a model-initiated second submission impossible |
| Comment = the 3-line summary block | **Comment = the newest `forecast.md` version block** (≤ 9,000 chars, summary always kept) | The rules ask that comments "accurately represent the reasoning process and final decision" [1][2]; a thesis line is thin for that. Still extracted mechanically |
| `update-tournament` sync as an LLM skill | **`scripts/tournament_sync.py`, deterministic, no model** | Missed windows, comment retries, resolutions and scores are bookkeeping. Zero tokens |
| Registry written by the bot (`seen_post_ids`, `last_sweep`) | **Registry is maintainer-only**; the gate is stateless | The gate asks Metaculus which questions the bot already forecast. A file only humans write cannot conflict with bot commits |
| `percentiles` field in `meta.yaml`, `--p10/--p90` | **The ledger's `distribution`** (from upstream) | One record of the full forecast, already validated and used by the CDF builder |
| `METACULUS_BOT_TOKEN` | **`METACULUS_API_KEY`** | Upstream's name, and the one this environment already uses |
| Default models Sonnet | **`opus` for the forecaster**, Sonnet for the research subagent; one variable each | The FutureEval survey found frontier models the clearest correlate of performance [2]; peer scores are relative to bots that mostly use them. Revisit after measuring a round (§7) |
| Sweep on by default; kill switch to stop it | **Opt-in**: nothing scheduled runs until `SWEEP_ENABLED=true` | Merging the code must not start spending before the smoke test |

Dropped from rev 2 as not worth their code for MiniBench: `render_agents.py` (agent model in
frontmatter instead), `validate_state.py` + pre-commit (the test suite plus `ci_commit.sh` do
the same job), the `triage.yml` job (no long-horizon bot questions yet), the Actions-minutes
billing meter. Deferred: circuit breaker, `errors.jsonl`. See the tracker.

---

## 2. Facts that shape the design (verified 2026-10-17)

From the resources page [1], the Fall announcement [2], the MiniBench project record [3] and
the official template [4]; details and the rule-by-rule mapping in
[`tournament-protocol.md`](tournament-protocol.md).

1. **Windows are 3 hours**, at random launch times; usually ≤ 5 questions open at once,
   occasionally ~10.
2. **One forecast per question**; rerunning because you dislike a forecast is forbidden.
3. **No human in the loop**: no previewing open-question forecasts and changing the bot; the
   bot must forecast and comment via the API itself. Upstream's "merge the PR = approval"
   submission therefore cannot be used for tournament questions.
4. **Private comments are required** on every forecast, for prizes.
5. **The community prediction is hidden** from bot tokens (all but ~50 questions).
6. **MiniBench**: `minibench` always names the current round. The next round (project 33132)
   starts **2026-10-19 00:00 UTC**, forecasting ends **2026-10-24 17:20 UTC**, 60 questions,
   most in the first days; LLM-written and LLM-resolved questions; spot peer scoring.
7. **Types used**: binary, numeric, discrete, multiple choice (no date questions).
8. The bot account behind `METACULUS_API_KEY` is `my-claude-forecasting`, `is_bot: true`.

---

## 3. Architecture (as built on `claude/inspiring-lamport-wyf3qe`, merged into `main` 2026-10-18)

```
tournament-sweep.yml  cron 11,41 * * * *  (opt-in SWEEP_ENABLED; manual runs always allowed)
 gate (1 job)    tournament_poll.py   budget guard -> token check -> open posts in active
                                      tournaments -> drop: groups, other types, submitted or
                                      closed-out here, < 20 min left, live bot forecast on
                                      Metaculus -> order (priority, close) -> cap
 forecast (matrix, max MAX_PARALLEL, one per question, concurrency key = post id)
   new_question.py --tournament --reuse    folder + raw/metaculus-question-<date>.json
   claude -p (tournament-forecast skill)   step timeout MAX_MINUTES_PER_QUESTION, dontAsk
                                           permissions from settings.ci.json, no secrets
                                           but its own OAuth token
   submit_metaculus.py <slug>              4 guards -> POST forecast -> POST private comment
                                           -> ledger `submission` + meta.tournament
   record_usage.py                         ledger/usage.jsonl + Step Summary
   ci_commit.sh                            fast data tests -> commit -> rebase (ledger union
                                           merge, INDEX regenerated) -> push, 5 attempts
 report-failure  one reused `bot-health` issue
tournament-sync.yml   cron 23 3 * * *    tournament_sync.py: missed windows, comment retries,
                                         closed/resolved + official spot peer score, INDEX;
                                         full test suite; commit
```

Data: `questions/<slug>/` (meta.yaml with the `tournament` block, short-form `forecast.md`,
`raw/`), `ledger/forecasts.jsonl` (forecast · submission · comment · resolution),
`ledger/usage.jsonl`, `tournaments/registry.yaml` (minibench active; fall-futureeval-2026 and
bot-testing-area registered, inactive).

---

## 4. Maintainer setup — what only a human can do

M.1–M.8 done 2026-10-18; M.9 recurs every season. Details in the tracker.

| # | Task | Blocks |
|---|---|---|
| M.1 | Bot account and token — **done** (`my-claude-forecasting`). Confirm in Metaculus settings that it is your **primary** (prize-eligible) bot, and fill in the participation form | — |
| M.2 | `claude setup-token` → secret `CLAUDE_CODE_OAUTH_TOKEN`; calendar reminder for expiry — **done** | everything |
| M.3 | Secret `METACULUS_API_KEY` (the bot token) — **done** | everything |
| M.4 | Merge the branch into `main` (schedules only fire from the default branch); keep `main` free of branch protection that blocks `github-actions[bot]` pushes — **done** | everything |
| M.5 | Private repo: Actions spending limit > $0 with an alert (or make the repo public) — **done** | the schedule |
| M.6 | Smoke test: Run workflow → `tournament: bot-testing-area`, `max_questions: 1` (first with `dry_run` ticked: forecasts, uploads the folder as an artifact, submits and commits nothing; then without it); check the forecast and the private comment as the bot — **done** | go-live |
| M.7 | `SWEEP_ENABLED=true` — **done** | go-live |
| M.8 | After the first round: set `WEEKLY_BUDGET_USD_EQUIV` from the measured spend — **done** (set before the round, from the smoke test; re-derived in §7) | budget guard |
| M.9 | Seasonal: bot survey (required for prizes), AskNews renewal if used | prizes |

---

## 5. CI timing for MiniBench

- **Cadence**: every 30 minutes (`:11`, `:41` — off the congested `:00` and the template's
  `:07/:27/:47`). Worst case a question is seen ~30 min + scheduler delay after opening
  (GitHub delays schedules under load, typically minutes). With a 3-hour window that leaves
  ≥ 2 hours.
- **Per question**: ~2 min setup + ≤ 25 min forecast + ~1 min submit/commit. A question is
  normally submitted 30–60 minutes after it opens.
- **Bursts**: `MAX_QUESTIONS_PER_RUN=6`, `MAX_PARALLEL=3` → 6 questions in ~1 hour; the next
  sweep (queued behind the running one) takes the rest. Ten simultaneous questions all finish
  inside ~1.5 h. Raise `MAX_PARALLEL` if subscription rate limits allow.
- **Too late**: questions with < 20 min left are skipped (0 peer points beats a forecast cut
  off mid-research, which may also never be logged).
- **Early vs. late in the window**: the spot score counts only the final forecast, so waiting
  could add information — but at a 3-hour horizon the gain is small and the miss risk is not.
  Forecast as soon as seen.
- **Off-weeks**: the gate costs one billed minute per run and zero tokens when nothing is open.
- **Minutes (private repo)**: ~1,440/month for the gate, ~20 per question; ~4,400/month at
  ~150 questions — over the Free/Pro allowance, single-digit to low-double-digit dollars of
  overage (re-check current pricing). Hourly cadence halves the gate cost and still leaves
  ≥ 1 h 45 per question; going public makes it free.

---

## 6. What remains

**Phase A — first round (needs the maintainer, then watching):** M.2–M.7 done 2026-10-18;
what remains is to watch the first MiniBench day closely (Step Summaries, `bot-health`),
especially the first real submissions and comments, and the CLI's behaviour in Actions (§8).

**Phase B — hardening (agent work, after the first real runs):**
- `ledger/errors.jsonl` + `record_error.py` with secret redaction and a `reproduce` command;
  circuit breaker (3 failed sweeps → 6 h pause; auth failure → 24 h).
- Lower setup time per job (cache the npm install).

**Phase C — forecast quality (after the first MiniBench results resolve, ~2026-11-06):**
- Calibrate against resolved MiniBench questions: bias by question type, extremeness.
- Backtest on closed questions (allowed by the rules) to compare prompts/models — never on open
  tournament questions.
- Optional: AskNews (free for bot makers) as a research source; a second independent forecast
  pass and median aggregation (the template uses 5 samples).

**Phase D — FutureEval:** activate `fall-futureeval-2026` once MiniBench runs clean
(`uv run scripts/tournament_registry.py set fall-futureeval-2026 --active`).

**Phase E — going public (optional):** scan history for secrets (`gitleaks`), rotate both
tokens, consider mid-season visibility of the scaffold; afterwards Actions minutes are free.

---

## 7. Cost and model choice

Every run's API-equivalent cost lands in `ledger/usage.jsonl`. After the first round:
`uv run scripts/record_usage.py report` → cost per question → re-set
`WEEKLY_BUDGET_USD_EQUIV` (≈ 2× the measured weekly spend; M.8 set a first value from the
smoke test) and decide `MODEL_FORECAST` (`opus` vs `sonnet`) on measured cost against the
subscription's limits. Per-question backstop:
`--max-budget-usd` (`MAX_USD_PER_QUESTION`, default 15) and the step timeout.

---

## 8. Open questions — verify on the first real runs

In brackets: the status after the smoke test of 2026-10-18 (one run, two `bot-testing-area`
questions).

1. `claude -p` in Actions with `CLAUDE_CODE_OAUTH_TOKEN` — expected to work (that is what
   `setup-token` is for). [Works.]
2. `--permission-mode dontAsk` with the CI allowlist: confirm `WebSearch`, `WebFetch` and the
   `research-scout` subagent are usable, and that `permission_denials` in `usage.jsonl` stays 0.
   [Open: 2 denials in each session, tools not yet identified. `web_searches` reads 0 although
   both forecasts cite search results: check the counter too.]
3. `--max-budget-usd` on a subscription token: expected to cap on the computed cost. [Not
   reached: $0.22–0.26 per session.]
4. The comment POST (`included_forecast: true`, private) — first real submission. [Works:
   `comment_posted: true`, HTTP 201, on both.]
5. The score field name in `my_forecasts.score_data` (the sync tries `spot_peer_score`, then
   `peer_score`). [Open until a question resolves.]
6. GitHub's union merge on runners behaves as in the local simulation. [Two parallel jobs
   both landed on `main` a second apart (`23cff82`, `18a99d7`).]

---

## 9. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| A second submission on a question (rules) | High | Four guards, serialised sweeps, per-question concurrency key, ledger test |
| A malformed CDF | High | Upstream's tested builder, local validation before POST, live dry-runs against real scalings (all four types, 2026-10-17) |
| Subscription quota drained | High | Opt-in sweep, per-question timeout and budget cap, weekly guard, `MAX_PARALLEL` |
| OAuth token expiry stops the bot | Medium | Fails loudly; `bot-health` issue; calendar reminder |
| Actions minutes exhausted (private) | Medium | Spending limit > $0; hourly cadence or public repo |
| LLM-written MiniBench criteria resolve counter-intuitively | Medium | Digest-first rule; the criteria are cached and read literally |
| Prompt injection from a web page | Medium | No Metaculus token and no push credential in the session; `ci_guard.py` undoes every change outside the question folder before the secret-holding steps; the virtualenv is rebuilt and git hooks are disabled. **Residual**: the session may run Python (for models), so injected code could read the session's own `CLAUDE_CODE_OAUTH_TOKEN` (revocable). Hard isolation — the session in a separate read-only job that hands over only its question folder — is the upgrade path |
| Maintainer "previews" an open question and tunes the bot | Medium | Documented in the protocol and README: read outputs after close |

---

## 10. Definition of done (MiniBench)

- [x] API-only client; no browser path; tests green.
- [x] Gate, scaffold and payload construction verified live (dry run, all four types).
- [x] One-shot guards, private comment, ledger record — unit-tested against fakes.
- [x] Secrets set; branch merged; smoke test on `bot-testing-area` shows the forecast **and**
      the private comment on the question page.
- [ ] `SWEEP_ENABLED=true`; the first MiniBench questions forecast and commented within their
      windows; no `bot-health` issue left open.
- [ ] After the round resolves: scores in `meta.yaml`, cost per question measured, budget set.

## Sources

1. FutureEval Bot Tournament Resources Page, https://www.metaculus.com/notebooks/38928/futureeval-resources-page/ (accessed 2026-10-17)
2. Announcing Fall 2026 FutureEval Bot Tournament, https://www.metaculus.com/notebooks/45615/ (accessed 2026-10-17)
3. MiniBench project record, `https://www.metaculus.com/api/projects/tournaments/minibench/` (accessed 2026-10-17)
4. Metaculus/metac-bot-template, https://github.com/Metaculus/metac-bot-template (accessed 2026-10-17)
