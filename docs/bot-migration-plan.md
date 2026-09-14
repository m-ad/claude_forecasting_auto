# Migration plan: from operator-driven workbench to autonomous CI forecasting bot

**Status**: in progress — Phase 0 partly landed. **Live progress and the numbered step list live
in [`bot-migration-progress.md`](bot-migration-progress.md)**, which is also where deviations
from this document are recorded. This file stays the written contract and is not edited to match
what was actually built.
**Written**: 2026-09-13 · **Revised**: 2026-09-13 (rev 2)
**Target**: a Metaculus bot account competing in **MiniBench** first, then the
**Fall 2026 FutureEval Bot Tournament**, driven entirely by Claude Code in GitHub Actions.

This document is the implementation contract for subsequent agent runs. Read it end to end
before touching code. Phases are ordered by dependency; do not start a phase before its
predecessors are green.

---

## 1. What we are building

Today the repo is a **human-in-the-loop workbench**: the operator types `/forecast <url>`,
Claude researches for an hour, writes `questions/<slug>/forecast.md`, logs a ledger line, and
the operator commits. Forecasts live only in this repo.

After this migration the repo is a **bot**:

- GitHub Actions invokes Claude Code on a schedule; no human types anything.
- Forecasts are **submitted to Metaculus** through the bot account's API token.
- Tournaments are registered once; questions are discovered, forecast, and resolved
  automatically. **MiniBench and FutureEval are the same code path** — see §2.6.
- All state lands on a dedicated branch, `live-bot`, via direct commits (no PRs).
- Model selection per job is configuration. **Defaults are Sonnet**, not Opus (§9.3).
- Every run records what it spent (§9.4) and every failure records how to recover (§10).

The existing slash commands (`/forecast`, `/update`, `/resolve`, `/status`) stay — they are the
same skills the bot runs, and they are the operator's manual override and local debug path.
`/review` is removed (§5.2).

---

## 2. Six facts that shape the design

Verified against Metaculus's own documentation and bot template on 2026-09-13. They are the
reason several things below look different from a first sketch.

### 2.1 Tournament questions are open for **90 minutes**

> "Questions will launch at random hours during the week and will be open for 1.5 hours each."
> "Questions can be released at a rate of up to 5 questions at a time from either series."
> — [FutureEval Bot Tournament Resources Page](https://www.metaculus.com/notebooks/38928/futureeval-resources-page/)

**Consequence**: a Tuesday/Friday cadence would miss essentially every tournament question.
Discovery and forecasting must run on a ~20-minute poll. The official
[`Metaculus/metac-bot-template`](https://github.com/Metaculus/metac-bot-template) workflow uses
`cron: "7,27,47 * * * *"` for exactly this reason.

This does **not** invalidate the operator's requested Tue/Fri `status --act` job — that job
serves long-horizon, operator-added questions (Metaculus Cup, ad-hoc) where updating is allowed.
The two cadences do different work. See §12.

### 2.2 **One forecast per question.** Resubmission is a rules violation

> "Bot makers should only submit one forecast per question in these bot-only tournaments" …
> "a bot maker cannot decide that they don't like their bot's forecast and rerun the bot on
> that question." — same source

**Consequence**: the repo's update loop (`/update`, tripwires, `next_review`) is **disabled for
tournament questions**. `meta.yaml` grows `tournament.one_shot`; the update path refuses such a
question; `status.py` never surfaces one for review. Local re-analysis for the calibration
record is still fine — what is forbidden is a second `POST` to Metaculus.

### 2.3 Bots must leave a **private comment** on every question they forecast

> "Bots are required to leave comments on questions they forecast, though bots should only
> leave private comments." — same source

**Consequence**: submission is two calls (forecast + comment), and the comment is mandatory.
`is_private: true` — a public comment is the wrong thing.

**Keep the comment minimal.** It is a compliance artefact, not a deliverable. The comment body
is **exactly the repo's existing three-line summary block** and nothing else:

```
**Date**: 2026-09-14
**Forecast**: Median 12.0%, IQR [8.0%, 18.0%]
**Thesis**: <1–3 sentences: the reference class, the one or two drivers that moved it, and the
single fact the forecast is most sensitive to.>
```

Target 400–700 characters. No source list, no scenario table, no markdown headings. Do not
spend a single extra turn composing it — it is a copy of the block already written into
`forecast.md`, and `metaculus_submit.py` extracts it mechanically rather than asking the model
to write it twice.

### 2.4 The community prediction is **hidden** on tournament questions

Bot-tournament questions close before the CP is revealed, and the Pro tournament is private,
specifically so bots cannot copy better forecasters.

**Consequence**: `AGENTS.md` §4 ("weight Pros and gold above the CP", "flag disagreement between
the three cohorts") is inapplicable in tournament mode. The market comparison table will mostly
be empty. The forecast skill must record "hidden — bot tournament" and move on rather than
spending turns on a fetch that returns nothing, and the methodology leans harder on the outside
view because the crowd anchor is gone.

### 2.5 A season is **300–500 questions** across ~4 months

**The binding constraint on this project.** The current methodology (≥15 sources, scenario
tables, sensitivity analysis, tripwires) costs on the order of an hour of Opus per question.
Multiplied by 400 questions on a subscription, this exhausts a Max plan's weekly quota within
days — and it does not fit in a 90-minute window anyway.

**A "tournament mode" methodology variant is mandatory, not optional** (§8.3). It keeps what
drives calibration (outside view first, explicit decomposition, disconfirming search, an IQR)
and drops what serves a *revisitable* forecast (tripwires, `next_review`, multi-scenario
sensitivity tables, charts, a separate `research.md`).

### 2.6 MiniBench is the same pipeline with different parameters — start there

| | MiniBench | FutureEval seasonal |
|---|---|---|
| Slug | `minibench` (stable, always the active project) | per season, e.g. `summer-futureeval-2026`; Fall 2026 slug **not yet public** |
| Cadence | new round **Monday every other week** | continuous, ~4-month season |
| Volume | **~60 questions per round** (~30/week while a round runs) | 300–500 per season |
| Question window | 1.5 h | 1.5 h |
| Question source | auto-created **and auto-resolved by an LLM** from varied sources | curated |
| Scoring | **spot peer score** (log-based, proper) | same family |
| Prize | $1k bi-weekly, paid out with the seasonal prizes | $50k seasonal |
| Noise | "slightly noisier" per Metaculus | lower |

**Consequences for the design:**

- The registry (§7.3) must hold **several simultaneously active tournaments**, and
  `tournament_poll.py` must aggregate open questions across all of them. This is not a
  "FutureEval bot that also does MiniBench" — it is a multi-tournament bot from day one.
- MiniBench's every-other-Monday cadence means a bursty load: near-zero for a week, then ~30
  questions in a week arriving up to 5 at a time. `MAX_FORECASTS_PER_RUN` and the weekly budget
  guard (§10.4) must survive that burst without draining the allowance.
- MiniBench questions are **LLM-generated and LLM-resolved**. Resolution criteria are
  occasionally ambiguous or mechanically literal. Rule 1 of `AGENTS.md` (read the resolution
  criteria first) matters *more* here, not less — it is the cheapest edge available.
- Because MiniBench is unscored-adjacent, low-stakes and high-frequency, it is the right place
  to measure real token cost per forecast (§9.4) before the season starts.
- `bot-testing-area` is unscored and exists for smoke tests. Register it first.

---

## 3. Operator setup checklist — the manual steps

Everything here must be done by a human; no agent can do it. Work top to bottom. Items marked
**[blocking]** stop the corresponding phase until done.

### 3.1 Metaculus

- [ ] **[blocking]** Create a **bot account** on Metaculus (a separate account from the
      operator's own — forecasting from a non-bot account in a bot tournament is a rules
      violation). Register it as a bot at <https://www.metaculus.com/futureeval/participate/>.
- [ ] **[blocking]** Copy its API token from the same page.
- [ ] Confirm the bot account appears on the `bot-testing-area` tournament page.
- [ ] After the Fall 2026 tournament is announced, note its **slug** from the tournament URL
      and register it with `/add-tournament <url>` (the slug is not knowable today — §16.1).
- [ ] Fill in the bot-maker survey when prompted; it is required to receive prizes.

### 3.2 Anthropic / Claude Code

- [ ] **[blocking]** Run `claude setup-token` locally on the subscription account and copy the
      long-lived OAuth token. This is the "CLAUDE_TOKEN" — the action input is
      `claude_code_oauth_token`, and using it bills the **subscription**, not the API.
- [ ] Install the [Claude GitHub App](https://github.com/apps/claude) on this repository.
- [ ] Put a **calendar reminder** to regenerate the OAuth token before it expires. When it
      expires, every workflow fails at once and the bot silently stops competing (§10.5 makes
      that failure loud, but only the operator can fix it).

### 3.3 GitHub — repository secrets

Settings → Secrets and variables → Actions → **Secrets**:

- [ ] **[blocking]** `CLAUDE_CODE_OAUTH_TOKEN` — from §3.2
- [ ] **[blocking]** `METACULUS_BOT_TOKEN` — from §3.1

### 3.4 GitHub — repository variables

Settings → Secrets and variables → Actions → **Variables**. All optional: every workflow has a
built-in default, listed in §9.3. Set them only to override.

- [ ] `MODEL_FORECAST`, `MODEL_UPDATE`, `MODEL_TRIAGE`, `MODEL_RESOLVE`,
      `MODEL_TOURNAMENT_SYNC`, `MODEL_SUBAGENT_RESEARCH`, `MODEL_SUBAGENT_FETCH`
- [ ] `MAX_FORECASTS_PER_RUN`, `MAX_TURNS_FORECAST`, `MAX_MINUTES_PER_QUESTION`
- [ ] `WEEKLY_BUDGET_USD_EQUIV` — the spend guard (§10.4). **Set this deliberately**; it is the
      only thing standing between a bad deploy and a drained allowance.
- [ ] `SWEEP_ENABLED` — kill switch, set to `false` to stop the 20-minute job immediately

### 3.5 GitHub — repository settings

- [ ] **[blocking]** Create the `live-bot` branch: `git branch live-bot main && git push -u origin live-bot`
- [ ] Keep `main` as the **default branch** — GitHub only fires `schedule` events for workflows
      on the default branch.
- [x] **Visibility: start private, go public later** (operator decision, 2026-09-13). This is
      workable and costs a few dollars a month — see §12.5 for the arithmetic and §12.6 for the
      checklist to run *before* flipping to public.
- [ ] **[blocking]** Set a non-zero **Actions spending limit** (Settings → Billing → Spending
      limits). The default on most accounts is **$0**, which means workflows simply stop the
      moment the included minutes run out — mid-month, silently, with no failed run to notice.
      That is the exact silent-failure mode this design works hard to avoid everywhere else.
      $10–20/month is enough headroom (§12.5); set an email alert at 75%.
- [ ] Create a fine-grained PAT with **read access to billing** and store it as
      `BILLING_READ_TOKEN`, so the bot can record Actions-minutes consumption alongside token
      consumption (§9.5). Optional — the bot degrades gracefully without it (§16.9).
- [ ] Do **not** add branch protection to `live-bot` requiring PRs — the bot commits directly.
- [ ] Confirm the account that last edits a workflow's `cron:` line is a **human** account.
      `claude-code-action` rejects bot actors on scheduled runs unless listed in `allowed_bots`.
- [ ] Enable Issues (the failure reporter opens one tracking issue — §10.5).

### 3.6 Local machine (for development and manual runs)

- [ ] `export METACULUS_BOT_TOKEN=...` in the local shell profile.
- [ ] `uv sync --group dev`
- [ ] `uv run pre-commit install` (§11.2)

### 3.7 Commit identity — decide once

The bot's commits need an author. **Recommended:**

```
git config user.name  "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
```

Why this over the operator's own address:

- No personal email appears in a public commit history.
- GitHub renders it with the Actions avatar and a `bot` badge, so machine commits are visually
  distinct from the operator's.
- Bot commits stay **out of the contribution graph** — which matters when the bot makes ~50
  commits a week and would otherwise make that graph meaningless.
- It is the conventional CI identity, so downstream tooling recognises it.


Never use a real personal address. 

---

## 4. Target repository layout

```
.github/workflows/
├── tests.yml                     # existing; extend triggers to live-bot
├── tournament-sweep.yml          # NEW  every 20 min — discover + forecast + submit
├── tournament-sync.yml           # NEW  daily      — roster reconcile + resolutions + scores
└── triage.yml                    # NEW  Tue/Fri    — /status --act on non-tournament questions

.claude/
├── agents/                       # NEW  rendered at CI start from *.md.tmpl (gitignored)
├── commands/                     # + add-tournament.md, tournament-sweep.md; − review.md
├── settings.json                 # local/interactive
├── settings.ci.json              # NEW  permissions for autonomous runs
└── skills/
    ├── forecast-workflow/        # MODIFIED — tournament mode, Metaculus submission
    ├── forecast-update/          # MODIFIED — refuses one_shot questions
    ├── metaculus-aggregations/   # REWRITTEN — thin wrapper over metaculus_api.py
    ├── metaculus-scraper/        # DELETED
    ├── add-tournament/           # NEW
    ├── update-tournament/        # NEW
    └── tournament-sweep/         # NEW

scripts/
├── _common.py                    # MODIFIED — registry helpers, lazy question index
├── metaculus_api.py              # NEW  token-authenticated client (single source of truth)
├── metaculus_cdf.py              # NEW  percentiles -> 201-point CDF
├── metaculus_submit.py           # NEW  deterministic submit + comment for one slug
├── tournament_poll.py            # NEW  no-LLM CI gate: is there work, and may we spend?
├── tournament_registry.py        # NEW  add/list/sync registered tournaments
├── record_usage.py               # NEW  parse execution_file -> ledger/usage.jsonl
├── usage_report.py               # NEW  rolling spend report + --check budget guard
├── record_error.py               # NEW  structured failure record + health/circuit breaker
├── validate_state.py             # NEW  data-integrity gate (pre-commit AND CI)
├── budget.py                     # NEW  per-question wall-clock budget helper
├── render_agents.py              # NEW  *.md.tmpl -> .claude/agents/*.md from env
├── ci_commit.sh                  # NEW  validate + commit + rebase-push with backoff
├── new_question.py               # MODIFIED — --from-json, question_id, tournament block
├── log_forecast.py               # MODIFIED — percentiles, submission state, one-shot guard
├── status.py                     # MODIFIED — excludes one_shot; --json
└── calibration.py                # MODIFIED — records official peer scores from the API

ledger/
├── forecasts.jsonl               # EMPTIED in Phase 0 — forecasts, resolutions, submissions
├── usage.jsonl                   # NEW  one line per CI run: tokens, cost-equivalent, turns
├── errors.jsonl                  # NEW  one line per failure, with a reproduction command
└── health.json                   # NEW  circuit-breaker state

tournaments/                      # NEW
├── registry.yaml                 # one entry per registered tournament
└── <slug>/roster.json            # last roster snapshot (evidence trail)

questions/                        # EMPTIED in Phase 0
docs/
├── tournament-protocol.md        # NEW  the bot's operating rules
├── runbook.md                    # NEW  what to do when the bot breaks
└── bot-migration-plan.md         # this file
```

---

## 5. Phase 0 — Clean the state, and delete what the bot does not need

### 5.1 Clear the forecasting record

The existing 17 questions and 20 ledger lines belong to the operator-driven era and would
corrupt the bot's calibration record — different methodology, different question population,
human-set review cadences.

```bash
git switch -c bot-migration main

git rm -r --quiet questions/*/            # 17 dirs, 127 files
touch questions/.gitkeep && git add questions/.gitkeep

: > ledger/forecasts.jsonl                # truncate; log_forecast.py appends
git add ledger/forecasts.jsonl

uv run scripts/status.py --index          # regenerate INDEX.md from empty state
git add INDEX.md

uv run ruff check . && uv run pytest -q
```

`tests/test_ledger.py` already has an `empty ledger` skip and `tests/test_scripts.py` a
`no questions scaffolded` skip. **If any test fails on empty state, fix the test, not the
cleanup** — an empty repo is the bot's legitimate starting condition.

Outside git: `git worktree prune` (a stale worktree points at
`C:/Users/Michael/Desktop/tmp/claude_forecasting/.claude/worktrees/…`, not this checkout), and
delete the merged local branches `testing` and `claude/us-model-evaluations-forecast-672746`.

### 5.2 Delete what is now dead weight

| Remove | Why | Reversible? |
|---|---|---|
| `.claude/skills/metaculus-scraper/` (whole dir) | A Playwright page-scraper that returns only the headline CP. With a bot token it has no remaining purpose. | Yes — it is in git history |
| The Playwright/Cloudflare path inside `metaculus_aggregations.py` (~500 of its 604 lines) | The entire module exists to defeat an anonymous-access challenge that a token removes. Keep only `fetch_aggregations()` as a thin wrapper. | Yes |
| `playwright` from `[project.dependencies]` | CI must not install a browser; it is minutes and cache for nothing. | Yes |
| `matplotlib` from `[project.dependencies]` → move to an optional `viz` group | Only `calibration.py --plot` uses it, and it already lazy-imports with a helpful error message. Tournament mode generates no charts. | Yes |
| `.claude/commands/review.md` (`/review`) | Red-teaming a forecast by hand has no place in an autonomous one-shot bot; nothing invokes it. | Yes |
| `charts/` directory creation in `new_question.py` for tournament questions | 500 permanently empty directories. | — |
| `research.md` for tournament questions | A second file to write per question, for a forecast that is never revisited. Evidence goes in `forecast.md`'s Evidence section. Make `test_research_log_is_not_an_empty_stub` skip one-shot questions. | — |

Do **not** delete: `templates/`, `docs/`, `scripts/`, `tests/`, `ledger/README.md`,
`docs/sources.md`.

---

## 6. Phase 1 — Metaculus API layer

The bot token makes the Playwright workaround obsolete. Everything Metaculus goes through one
module.

### 6.1 `scripts/metaculus_api.py`

Add `requests>=2.32` to `pyproject.toml`.

Verified contract (from `Metaculus/metac-bot-template/main_with_no_framework.py`):

```python
API_BASE_URL = "https://www.metaculus.com/api"
AUTH_HEADERS = {"Authorization": f"Token {os.environ['METACULUS_BOT_TOKEN']}"}
```

| Function | Endpoint | Notes |
|---|---|---|
| `list_tournament_posts(slug, statuses="open")` | `GET /posts/` | params: `limit`, `offset`, `order_by=-hotness`, `forecast_type=binary,multiple_choice,numeric,discrete`, `tournaments=[slug]`, `statuses`, `include_description=true`. Paginate on `offset`. |
| `get_post(post_id)` | `GET /posts/{post_id}/` | **`post["question"]["id"]` is the `question_id` and differs from `post_id`** — the forecast POST needs the question id. |
| `my_forecast_exists(post)` | — | `post["question"]["my_forecasts"]["latest"]["forecast_values"] is not None`, in a try/except. The authoritative "already forecast?" check — **needs no local state**, which is what makes the CI gate cheap. |
| `submit_forecast(question_id, payload)` | `POST /questions/forecast/` | Body is a **list**: `[{"question": qid, "source": "api", **payload}]`. |
| `post_comment(post_id, text)` | `POST /comments/create/` | `{"text", "parent": None, "included_forecast": True, "is_private": True, "on_post": post_id}` |
| `get_tournament(slug)` | `GET /tournaments/{slug}/` | name, dates, question count — used by `add-tournament`. |
| `get_aggregations(post_id, methods)` | `GET /aggregation_explorer/` | **VERIFY** (§16.2). Only used for non-tournament questions. |

Forecast payload shapes:

```python
# binary
{"probability_yes": 0.12, "probability_yes_per_category": None, "continuous_cdf": None}
# multiple_choice
{"probability_yes": None, "probability_yes_per_category": {"A": 0.62, "B": 0.25, "C": 0.13}, "continuous_cdf": None}
# numeric / discrete / date
{"probability_yes": None, "probability_yes_per_category": None, "continuous_cdf": [<201 floats>]}
```

**Error discipline in this module** (it is the main source of runtime failure):

- One retry with a short backoff on `5xx` and connection errors. **No retry on `4xx`** — a 400
  means a malformed payload and retrying burns budget to fail identically.
- Raise a typed `MetaculusError(stage, status, body, hint)` so `record_error.py` can write a
  useful record without the agent having to interpret an HTTP dump.
- A `401/403` raises `MetaculusAuthError`, which the gate treats as fatal for the whole run —
  never as a per-question failure to retry across five questions.

### 6.2 The CDF problem — do not improvise this

A numeric/date submission is a **201-point CDF**, and the API rejects malformed ones. The
constraints are non-obvious: strictly increasing, a minimum step between adjacent points, a
maximum PMF value per bucket (0.2), open/closed bound handling, and `zero_point` log-scaling.

**Port the `Percentile` / `NumericDistribution` classes from the bot template**
(`main_with_no_framework.py`, lines ~660–1120) into `scripts/metaculus_cdf.py` rather than
writing a new one.

- The agent supplies percentiles `{10, 25, 50, 75, 90}` — which the existing methodology already
  produces via median + IQR, extended at the tails.
- `metaculus_cdf.percentiles_to_cdf(...)` produces the 201 floats.
- `tests/test_cdf.py`: monotonicity, length 201, endpoints, open-vs-closed bounds, a
  `zero_point` case, and a rejection test for non-monotone input.

This is the highest-risk code in the migration: a silent CDF bug means every numeric forecast is
rejected or badly mis-shaped, and it cannot be retracted.

### 6.3 `scripts/metaculus_submit.py`

```bash
uv run scripts/metaculus_submit.py <slug> [--dry-run]
```

Deterministic, no LLM. Reads `questions/<slug>/meta.yaml` and `forecast.md`, then:

1. Refuse if `meta.tournament.submitted` is set (one shot).
2. Refuse if `my_forecast_exists()` says Metaculus already holds a forecast from this account.
3. Exit **0 with a `missed_window` record** if the question is no longer `open` — a closed
   window is a normal outcome, not a crash.
4. Build the payload from `meta.current` (+ `meta.percentiles` for continuous types).
5. `submit_forecast(...)`, then `post_comment(...)` with **the summary block extracted verbatim
   from `forecast.md`** (§2.3) — the script parses the `**Date**/**Forecast**/**Thesis**` block,
   it does not ask a model to write one.
6. Write `tournament.submitted`, `tournament.submitted_forecast`, `tournament.comment_posted`
   back into `meta.yaml`; append a `submission` event to `ledger/forecasts.jsonl`.
7. If the forecast succeeds but the comment fails, **record it and exit 0** — the forecast is in
   and cannot be redone. `tournament.comment_posted: false` is picked up and retried by the
   daily sync, which is the only place a comment retry belongs.

**Why a script and not the agent POSTing directly**: the payload shape, the one-shot guard and
the CDF are exactly what an LLM gets subtly wrong under time pressure, and the result is
unrecoverable. Tested Python does the irreversible part; the agent's only job is the judgement.

### 6.4 Rewrite `metaculus-aggregations`, delete `metaculus-scraper`

`metaculus_aggregations.py` keeps its CLI (`<post_id> --comments N --history --json`) and its
`fetch_aggregations()` signature so callers do not break, but becomes a thin wrapper over
`metaculus_api.py`. SKILL.md loses the Cloudflare essay. `metaculus-scraper` is deleted along
with its row in `SKILLS.md`.

---

## 7. Phase 2 — Schema changes

### 7.1 `meta.yaml`

```yaml
question_id: 43510            # NEW, top level — Metaculus's internal id, != post_id
tournament:                   # NEW, null for operator-added questions
  slug: "minibench"
  mode: "one_shot"            # one_shot | updatable
  registered: "2026-09-14"
  opened:  "2026-09-14T11:03:00Z"
  closes:  "2026-09-14T12:33:00Z"
  submitted: null             # ISO-8601 UTC of a successful submission, or null
  submitted_forecast: null    # exactly what was sent, for the audit trail
  comment_posted: false
  official_score: null        # NEW — the peer score Metaculus reports after resolution
  missed_window: false        # NEW — discovered too late, or budget-skipped
percentiles: null             # NEW — {10,25,50,75,90} for numeric/date/discrete
```

Update `templates/meta.yaml` and `tests/conftest.py`'s `META_KEYS`, then add `tests/test_meta.py`
cases:

- `tournament.mode == "one_shot"` ⟹ `tripwires == []` and `next_review is null`.
- `tournament.submitted` non-null ⟹ `current.version == 1`.
- `question_id` is an int whenever `source == "metaculus"`.
- `percentiles` present and monotone for `type in {numeric, date, discrete}` that were submitted.
- `missed_window: true` ⟹ `status in {dropped, resolved}` and `submitted is null`.

### 7.2 Ledger — a third event type

```json
{"ts":"…","event":"submission","slug":"…","post_id":45501,"question_id":45507,
 "tournament":"minibench","payload":{},"comment_posted":true,"api_status":201}
```

Extend `EVENTS` in `tests/conftest.py`; add `tests/test_ledger.py` assertions: every
`submission` has a preceding `forecast` for the same slug, and **no slug has two `submission`
records** — the append-only enforcement of the one-shot rule.

### 7.3 `tournaments/registry.yaml` — multi-tournament from day one

```yaml
tournaments:
  - slug: "bot-testing-area"
    url: "https://www.metaculus.com/tournament/bot-testing-area/"
    name: "Bot Testing Area"
    added: "2026-09-14"
    active: true
    mode: "one_shot"          # one_shot (bot tournaments) | updatable (Metaculus Cup)
    scored: false             # bot-testing-area does not affect ranking
    priority: 3               # lower number wins when the per-run budget is tight
    last_sync: null
    last_sweep: null
    seen_post_ids: []
  - slug: "minibench"
    name: "MiniBench"
    active: true
    mode: "one_shot"
    scored: true
    priority: 1
```

`priority` matters because MiniBench and FutureEval can burst simultaneously. When more open
questions exist than `MAX_FORECASTS_PER_RUN` allows, the sweep takes them in order of
(`priority`, soonest `closes`) — scored tournaments before smoke-test ones, and within a
tournament, the question about to close first.

`mode: updatable` keeps the Metaculus Cup in the normal `/update` loop with tripwires intact.

---

## 8. Phase 3 — Skills

### 8.1 `add-tournament` (NEW)

`/add-tournament <metaculus tournament url> [--priority N] [--mode one_shot|updatable]`

1. Parse the slug from `/tournament/<slug>/`.
2. `GET /api/tournaments/<slug>/` to confirm it exists and read name and dates.
3. Upsert into `tournaments/registry.yaml` (re-adding updates in place).
4. Run one immediate `update-tournament` sync to populate the roster.
5. Report name, slug, question count, open count, mode, priority.

Almost entirely deterministic — the work lives in `scripts/tournament_registry.py add <url>`
and the skill is a thin wrapper. Runs cheaply on Sonnet.

### 8.2 `update-tournament` (NEW) — the slow reconcile job

Runs daily. **Never forecasts and never submits a new forecast.**

For each `active: true` tournament:

1. Fetch the full roster (all statuses, paginated); snapshot to `tournaments/<slug>/roster.json`.
2. **New questions** — for each post id not in `seen_post_ids`, scaffold `questions/<slug>/` at
   `version: 0` with the `tournament` block filled in. Metadata only: title, type,
   `question_id`, open/close times, resolution criteria, fine print, units and bounds. Add to
   `seen_post_ids`.
3. **Missed windows** — any tracked question now closed with `submitted: null` gets
   `missed_window: true`, `status: dropped`. This is the metric that tells the operator the
   sweep cadence or the budget is wrong.
4. **Comment retries** — any question with `submitted` set and `comment_posted: false` gets one
   comment retry (§6.3 step 7).
5. **Resolutions** — for each tracked question now `resolved`: run `log_forecast.py resolve`,
   append a short `## Resolution — <date>` to `forecast.md`, and **record the official peer
   score from the API rather than recomputing it** — MiniBench and FutureEval score with a spot
   peer score against the other bots, which is not reproducible locally.
6. **Drift** — reconcile close times and edited resolution criteria. Flag criteria changes
   loudly: a changed criterion invalidates a submitted forecast the bot cannot re-submit.
7. Regenerate `INDEX.md` (**only here**, not in the sweep — §14.4), run `validate_state.py`,
   commit to `live-bot`.

### 8.3 `tournament-sweep` (NEW) — the fast competition path

The skill that scores points. Invoked by the 20-minute workflow, **only after the no-LLM gate
says there is work and the budget allows it** (§9.2, §10.4).

For each question the gate handed it, in (`priority`, soonest `closes`) order, up to
`MAX_FORECASTS_PER_RUN`:

1. Scaffold, or reuse the v0 folder `update-tournament` already made.
2. Read resolution criteria + fine print. **Write the "What resolves YES" digest first**, before
   forming any view. Rule 1 of `AGENTS.md` survives tournament mode intact — it is the highest
   expected value per token spent, and doubly so on LLM-generated MiniBench questions (§2.6).
3. **Outside view**: name a reference class and a base rate, or state explicitly that you
   cannot. Non-negotiable.
4. **Research fan-out**: spawn 2–3 `research-scout` subagents (§9.1) in parallel on independent
   streams — typically (a) primary/official data, (b) recent news, (c) explicit disconfirmation
   of the emerging view. Each returns a compact dated digest, not raw pages. **Integration and
   the final number stay with the parent model** — per `CLAUDE.md`, calibration lives in the
   integration.
5. **Target 5–8 sources, not 15.** A 90-minute window and a 400-question season do not permit
   more; pretending otherwise produces a padded source list, not a better forecast.
6. Median + IQR; plus 10th/90th percentiles for continuous questions.
7. Skip tripwires, `next_review`, scenario and sensitivity tables, charts, and `research.md`.
   Set `tournament.mode: one_shot`.
8. `log_forecast.py add` → `metaculus_submit.py <slug>` → confirm the submission returned OK.
9. Move to the next question. Commit once at the end of the run, not per question.

**Budget discipline** (§10.3 is the full set of rules):

- Check `uv run scripts/budget.py --remaining` before starting each question. Stop cleanly if
  the remaining wall-clock cannot fit another one.
- Abandon a question that has consumed more than `MAX_MINUTES_PER_QUESTION` (default 8),
  submitting the best current estimate rather than timing out with nothing. An unsubmitted
  forecast scores zero; a mediocre submitted one does not.
- One question failing must not abort the batch — **but two consecutive failures must** (§10.3).

### 8.4 Changes to `forecast-workflow`

- A **Mode** step at the top: `tournament` (a `tournament` block with `mode: one_shot`) vs
  `standard`. Tournament mode follows §8.3; standard mode is unchanged.
- Step 6 gains: *in tournament mode the CP and Pro/gold cohorts are hidden by design. Record
  "hidden — bot tournament" and do not spend turns retrieving them.*
- Step 9 gains the `metaculus_submit.py` call.
- The pre-commit lint/test gate becomes `uv run scripts/validate_state.py` + the fast test
  subset (§11).

### 8.5 Changes to `forecast-update`

- **Hard stop** at the top: if `tournament.mode == "one_shot"` and `tournament.submitted` is
  set, refuse and explain. A second submission is a rules violation.
- A local-only re-analysis is still permitted for the calibration record, but it must not call
  `metaculus_submit.py`. State this explicitly — an agent told to "update the forecast" will
  otherwise reach for the submit script.

---

## 9. Phase 4 — Subagents, models, the cost gate, and usage accounting

### 9.1 Subagents

Defined as templates under `.claude/agents/*.md.tmpl`, rendered at CI start:

| Agent | Default model | Job |
|---|---|---|
| `research-scout` | `MODEL_SUBAGENT_RESEARCH` (Sonnet) | One evidence stream: search, read, return a dated findings digest with URLs. Read-only. |
| `source-checker` | `MODEL_SUBAGENT_FETCH` (Haiku) | Verify a URL is live, extract the specific number or quote, return it with an access date. |
| `resolution-reader` | `MODEL_SUBAGENT_FETCH` (Haiku) | Fetch a post's resolution criteria, fine print and top comments; return a structured digest. |

Read-only tools only (`WebSearch`, `WebFetch`, `Read`, `Grep`, `Glob`, and `Bash` limited to
`uv run scripts/…`). They must not write to `questions/` — the parent owns the deliverable.

Each subagent prompt ends with a hard instruction: *return your digest even if incomplete; never
retry a failed fetch more than once; never spawn further agents.* An unbounded subagent is the
easiest way to lose a token budget invisibly.

This is consistent with `CLAUDE.md`, which already says to fan out on independent evidence
streams but never to delegate the probability judgement. Cheap models gather; the expensive
model judges.

### 9.2 The no-LLM gate

A 20-minute cron is 72 runs/day. Running Claude on all of them is unaffordable and pointless,
since most polls find nothing.

`scripts/tournament_poll.py` is pure Python. In one pass it:

1. Checks the circuit breaker in `ledger/health.json` (§10.5) — open ⟹ exit, no work.
2. Checks the weekly budget via `usage_report.py --check` (§10.4) — over ⟹ exit, no work.
3. Validates `METACULUS_BOT_TOKEN` with one cheap authenticated call — invalid ⟹ **fail the job
   loudly** without ever starting Claude.
4. Lists open posts across all `active` tournaments and drops any where `my_forecast_exists()`.
5. Orders the survivors by (`priority`, `closes`) and emits the first `MAX_FORECASTS_PER_RUN`.

```bash
uv run scripts/tournament_poll.py --github-output
# has_work=true
# questions=[{"post_id":45501,"question_id":45507,"tournament":"minibench",…}]
# reason=ok
```

Because step 4 reads Metaculus's own record of the bot's forecasts, the gate needs **no
repository state**. Expected effect: ~70 of 72 daily runs cost ~20 seconds of Actions time and
zero tokens.

### 9.3 Model configuration — Sonnet by default

GitHub **repository variables**, not secrets — non-sensitive and editable in the UI without a
commit. Every one has a workflow-level default, so an unset variable is fine.

| Variable | Default | Used by |
|---|---|---|
| `MODEL_FORECAST` | **`claude-sonnet-5`** | tournament-sweep, `/forecast` |
| `MODEL_UPDATE` | **`claude-sonnet-5`** | `/update` inside triage |
| `MODEL_TRIAGE` | `claude-sonnet-5` | `/status --act` |
| `MODEL_RESOLVE` | `claude-sonnet-5` | `/resolve` |
| `MODEL_TOURNAMENT_SYNC` | `claude-sonnet-5` | update-tournament |
| `MODEL_SUBAGENT_RESEARCH` | `claude-sonnet-5` | `research-scout` |
| `MODEL_SUBAGENT_FETCH` | `claude-haiku-4-5-20251001` | `source-checker`, `resolution-reader` |
| `MAX_TURNS_FORECAST` | `60` | `claude_args --max-turns` |
| `MAX_FORECASTS_PER_RUN` | `5` | tournament-sweep |
| `MAX_MINUTES_PER_QUESTION` | `8` | tournament-sweep (§12.5 sizes this against Actions minutes) |
| `WEEKLY_BUDGET_USD_EQUIV` | `25` | the spend guard (§10.4) |
| `SWEEP_ENABLED` | `true` | kill switch |

**Start on Sonnet everywhere.** Measure real cost per forecast on MiniBench for two rounds
(§9.4), then decide whether Opus on `MODEL_FORECAST` is worth it — that is a one-variable flip
with no code change. Opus is most defensible on the seasonal tournament, where question quality
is curated and the prize pool is 50× MiniBench's.

Top-level models reach Claude Code via
`claude_args: --model ${{ vars.MODEL_FORECAST || 'claude-sonnet-5' }}`. Subagent models live in
agent frontmatter, which the CLI cannot set, so `render_agents.py` substitutes
`{{MODEL_SUBAGENT_RESEARCH}}` from the environment into `.claude/agents/*.md` before Claude
starts. Gitignore the rendered `.md`; commit only `.md.tmpl`.

### 9.4 Usage accounting — what a forecasting session actually costs

`anthropics/claude-code-action@v1` exposes an **`execution_file`** output: the path to Claude
Code's execution output JSON. Its final `result` record carries `usage` (input, output,
`cache_creation_input_tokens`, `cache_read_input_tokens`), `num_turns`, `duration_ms`,
`total_cost_usd` and a per-model breakdown. That is the reliable source.

> Do **not** parse `~/.claude/projects/**/*.jsonl` instead. Those transcripts have a known bug
> where `output_tokens` is recorded as a placeholder (1–2) rather than the real count, because
> the true value only appears in the streaming result event, which is never persisted.

```yaml
- uses: anthropics/claude-code-action@v1
  id: claude
  # …
- name: Record token usage
  if: always()
  run: |
    uv run scripts/record_usage.py \
      --execution-file "${{ steps.claude.outputs.execution_file }}" \
      --conclusion     "${{ steps.claude.outputs.conclusion }}" \
      --job tournament-sweep --run-id "${{ github.run_id }}" \
      --questions "${{ needs.gate.outputs.question_count }}" \
      --summary >> "$GITHUB_STEP_SUMMARY"
```

`record_usage.py` appends one line per run to `ledger/usage.jsonl`:

```json
{"ts":"2026-09-14T11:31:02Z","job":"tournament-sweep","run_id":"1234567890",
 "conclusion":"success","model":"claude-sonnet-5","questions":3,"submitted":3,
 "duration_s":412,"num_turns":38,"cost_usd_equiv":0.71,"cost_per_question":0.24,
 "tokens":{"input":18422,"output":9106,"cache_read":812004,"cache_write":41220},
 "by_model":{"claude-sonnet-5":{},"claude-haiku-4-5-20251001":{}}}
```

and prints a small table to the run's GitHub Step Summary, so the cost of a session is visible
in the Actions tab without opening any file.

`uv run scripts/usage_report.py` gives the rolling view the operator actually wants:

```text
window   runs  forecasts  tokens(in/out/cache)      cost-equiv  per forecast
7 days     94         31  0.4M / 0.2M / 18.1M       $ 14.82     $ 0.48
30 days   402        126  1.8M / 0.9M / 79.4M       $ 61.05     $ 0.48
```

**Two honest limitations, stated here so nobody builds on a false premise:**

1. `total_cost_usd` is the **API-equivalent price**. On a subscription you are not billed it.
   It is a proxy for how much allowance a run consumed, and it is the best proxy available.
2. **Remaining subscription allowance is not exposed to CI.** There is no API for "how much of
   my weekly limit is left"; `/usage` in an interactive session and the Anthropic console are
   the only views. The literal "before/after allowance" reading is therefore not implementable.
   What §10.4 implements instead is a **cumulative spend guard**: the operator sets a weekly
   cost-equivalent budget, and the bot stops when it is hit. That achieves the goal — not
   draining the pool — without pretending to read a number that is not published.

### 9.5 Actions-minutes accounting — the second meter

While the repo is private, Actions minutes are a metered resource just like tokens, and they run
out the same silent way (§3.5). Track both in the same place.

`record_usage.py` gains an optional second source: when `BILLING_READ_TOKEN` is present it
queries GitHub's billing endpoint for the account's Actions usage and folds the result into the
same `ledger/usage.jsonl` row:

```json
{"ts":"…","job":"tournament-sweep","cost_usd_equiv":0.71,
 "actions":{"minutes_used":1183,"minutes_included":2000,"pct_used":59.2}}
```

`usage_report.py` then prints both meters side by side — which is exactly the number to look at
when deciding whether to raise the sweep cadence:

```text
window   runs  forecasts  token cost-equiv  per forecast   Actions min  of included
7 days     94         31         $ 14.82        $ 0.48             338         17 %
30 days   402        126         $ 61.05        $ 0.48           1,183         59 %
```

Degrade gracefully: no token, or an endpoint that has moved (§16.9), writes
`"actions": {"unavailable": true}` and never fails the job. The Actions meter is nice to have;
the token meter is the one that matters.

---

## 10. Phase 5 — Failures that help you recover, and never drain the budget

The operator's two requirements here pull in opposite directions: *log failures usefully* and
*do not let failure handling burn tokens*. The resolution is a strict division of labour —
**Python does all failure handling; the model does none.**

### 10.1 The rule

> When something fails, the agent records one structured line and moves on. It never diagnoses,
> never retries beyond one attempt, never reads logs to understand an error, and never rewrites
> a script to work around one.

An LLM debugging a 400 from an API is the single most expensive failure mode available, and it
produces nothing a human could not read from the error record in five seconds.

### 10.2 `ledger/errors.jsonl` — one line per failure

```json
{"ts":"2026-09-14T11:22:40Z","job":"tournament-sweep","run_id":"1234567890",
 "slug":"2026-09-14-mc45501-…","post_id":45501,"tournament":"minibench",
 "stage":"submit","error_class":"MetaculusError","status":400,
 "message":"continuous_cdf must be strictly increasing",
 "fatal":false,"action_taken":"question abandoned, batch continued",
 "reproduce":"uv run scripts/metaculus_submit.py 2026-09-14-mc45501-… --dry-run",
 "run_url":"https://github.com/m-ad/claude_forecasting/actions/runs/1234567890"}
```

Stages: `poll`, `scaffold`, `research`, `forecast`, `submit`, `comment`, `commit`, `auth`.

The **`reproduce` field is the point of the whole file** — every record carries the exact
command that re-triggers the failure locally against the same slug. Recovery starts by copying
one line, not by reading a workflow log.

`scripts/record_error.py` is the only writer. The agent calls it; so do the scripts; so does the
workflow's `if: failure()` step, which catches crashes the agent never saw.

### 10.3 Budget protection rules, in the skill

These go verbatim into `tournament-sweep/SKILL.md`:

1. **One retry maximum** per failing operation, then abandon that question. No third attempt.
2. **Never debug a script or API failure in-session.** Call `record_error.py` and continue.
3. **Two consecutive question failures abort the run.** A systemic fault (bad token, schema
   change, broken CDF) fails identically on every question; continuing spends five questions'
   worth of tokens to learn nothing. Commit what succeeded and exit.
4. **Never re-read a file already read** in this session, and never re-run a search that
   returned usable results.
5. **Check `uv run scripts/budget.py --remaining` before each question.** If the remaining
   wall-clock will not fit another question, stop cleanly.
6. **On any `MetaculusAuthError`, abort the entire run immediately.** Auth is not a per-question
   problem.
7. **Prefer submitting a rougher forecast to spending more turns.** A submitted forecast at
   minute 10 beats a better one that never gets sent.

`--max-turns` is the backstop when rules 1–7 are ignored, not the primary control.

### 10.4 The weekly spend guard

`scripts/usage_report.py --check` sums `cost_usd_equiv` over the trailing 7 days in
`ledger/usage.jsonl` and compares it to `WEEKLY_BUDGET_USD_EQUIV`.

- Over budget ⟹ exit non-zero. `tournament_poll.py` calls it as step 2 and reports
  `has_work=false, reason=budget_exceeded`, so **no Claude job starts at all**.
- At 80% ⟹ still runs, but prints a warning into the step summary and lowers the effective
  `MAX_FORECASTS_PER_RUN` to 2, so the tail of the week is spent on the questions closing
  soonest rather than the first five discovered.
- The guard resets on a rolling window, so the bot resumes on its own. No manual reset needed.

This is the mechanism that satisfies "better skip forecasting a question than drain my token
pool for other questions" — and it is enforced in Python, before any model is invoked.

### 10.5 Circuit breaker and visible failure

`ledger/health.json`:

```json
{"consecutive_sweep_failures": 0, "last_success": "2026-09-14T11:31:02Z",
 "breaker_open_until": null, "breaker_reason": null}
```

- 3 consecutive failed sweeps ⟹ `breaker_open_until = now + 6h`. The gate exits immediately
  with `reason=circuit_breaker`, and **no tokens are spent while the bot is broken**.
- The breaker closes automatically after 6 hours, so a transient Metaculus outage self-heals.
- A `MetaculusAuthError` or an OAuth failure opens the breaker for 24 hours — those never
  self-heal, and retrying only burns Actions minutes.

**Making failure visible**, all in plain bash with no token cost:

```yaml
- name: Report failure
  if: failure()
  run: |
    uv run scripts/record_error.py --from-job-context --stage "${{ job.status }}"
    gh issue list --label bot-health --state open --json number \
      | jq -e 'length > 0' >/dev/null \
      && gh issue comment "$(gh issue list --label bot-health --state open --json number -q '.[0].number')" \
           --body-file /tmp/failure-summary.md \
      || gh issue create --label bot-health \
           --title "bot: $(date -u +%F) ${{ github.workflow }} failing" \
           --body-file /tmp/failure-summary.md
```

One issue, reused — not one per failure. It carries the last error records, the breaker state,
and the current 7-day spend.

### 10.7 The Actions-minutes guard (private repo only)

The token budget has a guard (§10.4); while the repo is private, minutes need the symmetric one,
because running out of them stops the bot *without producing a failed run to notice*.

When `record_usage.py` has billing data (§9.5), `tournament_poll.py` adds a fourth pre-flight
check after the budget check:

- **≥ 85% of included minutes used** ⟹ the gate reports `has_work=false,
  reason=actions_minutes_low` on runs where the only open questions belong to tournaments with
  `scored: false`. Smoke-test forecasting is the first thing to sacrifice.
- **≥ 95%** ⟹ the gate skips every sweep and writes one line into the `bot-health` issue. The
  daily sync still runs; it is one job a day and it is what surfaces resolutions.
- The guard resets on the billing cycle, automatically.

Deliberately *not* a hard stop at 100%: the spending limit from §3.5 is the real backstop, and
this guard exists to make the operator notice at 85% rather than discover it at 100%. Delete
this whole section when the repo goes public (§12.6) — minutes become unlimited.

### 10.8 `docs/runbook.md` (NEW)

A one-page table the operator reads at 8 a.m. when something is red:

| Symptom | Likely cause | First command |
|---|---|---|
| All workflows fail, `auth` stage | OAuth token expired | `claude setup-token`, update the secret |
| `has_work=false, reason=budget_exceeded` | Weekly token guard tripped | `uv run scripts/usage_report.py` |
| `has_work=false, reason=actions_minutes_low` | §10.7 guard tripped | `uv run scripts/usage_report.py`; raise the spending limit |
| Nothing runs at all, no failed runs in the tab | Actions **spending limit** hit (§3.5) | Settings → Billing → Spending limits |
| `reason=circuit_breaker` | 3 failed sweeps | `uv run scripts/record_error.py --tail 10` |
| Many `missed_window: true` | Sweep cadence too slow, or budget too tight | §12.5 |
| `submit` stage 400 on numeric questions | CDF bug | `uv run pytest tests/test_cdf.py` |
| Forecasts land but no comment | Comment API change | `uv run scripts/metaculus_submit.py <slug> --dry-run` |

---

## 11. Phase 6 — Data integrity: tests and pre-commit

### 11.1 One validator, two callers

`scripts/validate_state.py` is the single entry point for every integrity check, so the local
hook and CI cannot drift apart:

- `meta.yaml` ↔ ledger ↔ `INDEX.md` agreement (the existing `test_consistency.py` invariants).
- **One-shot uniqueness**: no slug has two `submission` records; no one-shot question has
  `current.version > 1`.
- **Append-only**: the committed ledger is a prefix of the working-tree ledger — rule 8, checked
  mechanically rather than trusted.
- Registry schema: every entry has a slug, mode, priority; no duplicate slugs.
- `percentiles` monotone; stored percentiles round-trip through `metaculus_cdf` without error.
- `tournament.submitted` implies a `submission` ledger record, and vice versa.

```bash
uv run scripts/validate_state.py            # everything
uv run scripts/validate_state.py --changed  # only slugs touched vs origin/live-bot
```

### 11.2 Pre-commit

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.16.5
    hooks: [{id: ruff, args: [--fix]}, {id: ruff-format}]
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks: [{id: check-yaml}, {id: check-json}, {id: end-of-file-fixer}, {id: trailing-whitespace}]
  - repo: local
    hooks:
      - id: validate-state
        name: forecast state integrity
        entry: uv run scripts/validate_state.py --changed
        language: system
        pass_filenames: false
      - id: pytest-fast
        name: fast data tests
        entry: uv run pytest -q tests/test_meta.py tests/test_ledger.py tests/test_cdf.py
        language: system
        pass_filenames: false
```

Operator installs it once with `uv run pre-commit install` (§3.6).

**In CI, do not run `pre-commit`** — it re-installs hook environments on every run, which is
minutes for nothing. `ci_commit.sh` calls the same underlying commands directly:
`ruff check .` → `validate_state.py --changed` → the fast test subset → commit → rebase-push.

### 11.3 Making the test suite survive 500 questions

The data tests parametrise per question. At 500 questions that is tens of thousands of cases and
the pre-commit gate becomes unusable.

- Add a `--changed-only` pytest option in `tests/conftest.py` that parametrises only over
  questions touched relative to `origin/live-bot`. Default it on when `CI_FAST=1`.
- The sweep and triage jobs run `CI_FAST=1` (changed questions only).
- The **daily sync job runs the full suite** over every question — once a day, which is the
  right cadence for catching slow drift.
- `tests.yml` on `main` keeps running everything, unchanged.

---

## 12. Phase 7 — GitHub Actions

### 12.1 Branch strategy

- `main` stays the default branch. **GitHub only fires `schedule` for workflows on the default
  branch**, so all three workflow files must be merged to `main` to run at all.
- Bot state is committed to **`live-bot`**, directly, no PRs.
- Every bot job checks out `live-bot`, then `git merge --no-edit origin/main`, so code changes
  reach the running bot within one cycle. Merge, not rebase — the branch is long-lived.
- All three workflows share `concurrency: {group: live-bot-writer, cancel-in-progress: false}`.
  Belt and braces: `ci_commit.sh` does `git pull --rebase origin live-bot` with the 4-attempt
  exponential backoff from `CLAUDE.md` before pushing.
- Extend `tests.yml` to `push: branches: [main, live-bot]`. Pushes made with `GITHUB_TOKEN` do
  not trigger workflows, so the bot's own gate must run inside the job — which it does.

### 12.2 `tournament-sweep.yml` — every 20 minutes

```yaml
name: tournament-sweep
on:
  schedule:
    - cron: "7,37 * * * *"         # every 30 min — see §12.5 for the cost/miss trade-off
  workflow_dispatch:

concurrency:
  group: live-bot-writer
  cancel-in-progress: false

jobs:
  gate:
    if: vars.SWEEP_ENABLED != 'false'
    runs-on: ubuntu-latest
    timeout-minutes: 5
    outputs:
      has_work:       ${{ steps.poll.outputs.has_work }}
      questions:      ${{ steps.poll.outputs.questions }}
      question_count: ${{ steps.poll.outputs.question_count }}
      reason:         ${{ steps.poll.outputs.reason }}
    steps:
      - uses: actions/checkout@v5
        with: { ref: live-bot, fetch-depth: 1 }
      - uses: astral-sh/setup-uv@v7
        with: { python-version: "3.13", enable-cache: true,
                cache-dependency-glob: "pyproject.toml" }
      - id: poll
        env:
          METACULUS_BOT_TOKEN:     ${{ secrets.METACULUS_BOT_TOKEN }}
          WEEKLY_BUDGET_USD_EQUIV: ${{ vars.WEEKLY_BUDGET_USD_EQUIV || '25' }}
          MAX_FORECASTS_PER_RUN:   ${{ vars.MAX_FORECASTS_PER_RUN || '5' }}
        run: uv run scripts/tournament_poll.py --github-output

  forecast:
    needs: gate
    if: needs.gate.outputs.has_work == 'true'
    runs-on: ubuntu-latest
    timeout-minutes: 75            # < the 90-minute question window
    permissions: { contents: write, id-token: write, issues: write }
    steps:
      - uses: actions/checkout@v5
        with: { ref: live-bot, fetch-depth: 0 }
      - name: Identity and sync with main
        run: |
          git config user.name  "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git merge --no-edit origin/main
      - uses: astral-sh/setup-uv@v7
        with: { python-version: "3.13", enable-cache: true,
                cache-dependency-glob: "pyproject.toml" }
      - run: uv sync --group dev
      - name: Render subagent definitions
        env:
          MODEL_SUBAGENT_RESEARCH: ${{ vars.MODEL_SUBAGENT_RESEARCH || 'claude-sonnet-5' }}
          MODEL_SUBAGENT_FETCH:    ${{ vars.MODEL_SUBAGENT_FETCH || 'claude-haiku-4-5-20251001' }}
        run: uv run scripts/render_agents.py
      - uses: anthropics/claude-code-action@v1
        id: claude
        env:
          METACULUS_BOT_TOKEN:      ${{ secrets.METACULUS_BOT_TOKEN }}
          SWEEP_QUESTIONS:          ${{ needs.gate.outputs.questions }}
          MAX_FORECASTS_PER_RUN:    ${{ vars.MAX_FORECASTS_PER_RUN || '5' }}
          MAX_MINUTES_PER_QUESTION: ${{ vars.MAX_MINUTES_PER_QUESTION || '8' }}
          CI_FAST: "1"
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: "/tournament-sweep"
          settings: .claude/settings.ci.json
          claude_args: |
            --model ${{ vars.MODEL_FORECAST || 'claude-sonnet-5' }}
            --max-turns ${{ vars.MAX_TURNS_FORECAST || '60' }}
            --permission-mode acceptEdits
      - name: Record token usage
        if: always()
        run: |
          uv run scripts/record_usage.py \
            --execution-file "${{ steps.claude.outputs.execution_file }}" \
            --conclusion "${{ steps.claude.outputs.conclusion }}" \
            --job tournament-sweep --run-id "${{ github.run_id }}" \
            --questions "${{ needs.gate.outputs.question_count }}" \
            --summary >> "$GITHUB_STEP_SUMMARY"
      - name: Commit and push
        if: always()
        run: ./scripts/ci_commit.sh "sweep: ${{ needs.gate.outputs.question_count }} question(s)"
      - name: Report failure
        if: failure()
        env: { GH_TOKEN: "${{ github.token }}" }
        run: ./scripts/report_failure.sh tournament-sweep
```

Note `if: always()` on the usage and commit steps: a run that fails partway still records what
it spent and still commits the forecasts it did complete. Losing a submitted forecast's local
record would break the one-shot guard on the next run.

### 12.3 `tournament-sync.yml` — daily

```yaml
on:
  schedule:
    - cron: "23 3 * * *"           # 03:23 UTC daily
  workflow_dispatch:
    inputs:
      tournament: { description: "slug, or blank for all", required: false }
```

Prompt `/update-tournament`, model `${{ vars.MODEL_TOURNAMENT_SYNC || 'claude-sonnet-5' }}`,
`timeout-minutes: 45`, **full test suite** (no `CI_FAST`), same usage-recording and
failure-reporting steps.

Daily rather than the "every X days" originally suggested: resolutions land daily, comment
retries and missed-window bookkeeping should not wait, and the run is cheap on Sonnet. To make
it every X days, use an explicit weekday list (`cron: "23 3 * * 1,4"`) rather than `*/X` in the
day-of-month field — `*/3` restarts each month and fires on the 31st and the 1st back to back.

### 12.4 `triage.yml` — Tuesday and Friday

```yaml
on:
  schedule:
    - cron: "17 1 * * 2,5"
  workflow_dispatch:
```

Prompt `/status --act`, model `${{ vars.MODEL_TRIAGE || 'claude-sonnet-5' }}`,
`timeout-minutes: 90`.

`status.py --act` must **skip questions with `tournament.mode == "one_shot"`** — this job exists
for long-horizon operator questions and the Metaculus Cup, not for questions that can never be
updated.

### 12.5 Actions-minutes budget on a private repository

The repo starts **private**, so Actions minutes are metered. Three facts drive the arithmetic:

1. **Billing rounds each job up to the nearest whole minute, independently.** A gate job that
   finishes in 15 seconds bills **one full minute**. There is no optimisation below that floor —
   removing `actions/checkout`, skipping `uv sync`, using stdlib `urllib` instead of `requests`:
   all of it saves real seconds and **zero billed minutes**. The only lever on gate cost is *how
   many times it runs*.
2. Included minutes per month for private repos: **Free 2,000 · Pro 3,000 · Team 3,000**.
3. Overage on a Linux 2-core runner is **$0.006/minute** — which turns out to be the decisive
   number.

**The gate, by cadence** (billed minutes/month, and this is a floor, not an estimate):

| Sweep cron | Runs/day | Gate min/month | Chances to catch a 90-min window |
|---|---|---|---|
| `7,27,47 * * * *` (every 20 min) | 72 | **2,160** | 4 (3 after scheduler delay) |
| `7,37 * * * *` (every 30 min) | 48 | **1,440** | 3 (2 after delay) |
| `17 * * * *` (hourly) | 24 | 720 | 1 (may miss entirely) |

Note that the 20-minute cadence **exceeds the Free tier on the gate alone**, before a single
forecast runs.

**The forecast job**, sized on MiniBench (~60 questions per round, a round every other Monday
≈ 130 questions/month), at ~2 minutes of setup plus `MAX_MINUTES_PER_QUESTION` per question:

| `MAX_MINUTES_PER_QUESTION` | Forecast min/month |
|---|---|
| 12 | ~1,650 |
| 8 (the §9.3 default) | ~1,140 |
| 6 | ~880 |

**Recommendation — and it is cheaper than it looks:**

Run `7,37 * * * *` (every 30 minutes) with `MAX_MINUTES_PER_QUESTION: 8`. That is
1,440 + 1,140 ≈ **2,600 minutes/month**, so on the Free tier you pay for ~600 overage minutes:

> **≈ $3.60/month.** Even the most expensive configuration here — 20-minute sweep, 12 minutes a
> question, ~3,800 minutes — costs about **$11/month** in overage on Free, or **$5/month** on Pro.

So do **not** compromise the tournament to save minutes. Set the spending limit (§3.5), start at
the 30-minute cadence, and let the data decide: `missed_window: true` counts from §8.2 step 3
are the exact measurement of what the slower cadence costs you. If the first MiniBench round
shows material misses, move to `7,27,47` and accept roughly $7 more per month.

Two private-repo bonuses worth knowing: the **60-day scheduled-workflow auto-disable applies to
public repositories**, not private ones, so the schedule cannot lapse while private (and once
public, the bot's daily commits keep it alive anyway); and secrets are never exposed to fork
pull requests, because there are no outside forks.

### 12.6 Going public later — do this before flipping the switch

Two of these must be built **from day one**, because flipping to public exposes the entire git
history and history cannot be cleaned retroactively without a rewrite.

- [ ] **Redact secrets in `record_error.py` from the first commit.** API error bodies can echo
      request headers. Before writing any record to `ledger/errors.jsonl`, strip
      `Authorization` headers, anything matching a token shape, and the `METACULUS_BOT_TOKEN` /
      `CLAUDE_CODE_OAUTH_TOKEN` values read from the environment. Add a unit test that feeds a
      token-bearing error body through the writer and asserts the token is absent from the
      output. **This is not a pre-flip task — it is a Phase 5 requirement**, because a leaked
      token in an old commit survives the flip.
- [ ] **Never commit a raw API response wholesale.** `tournaments/<slug>/roster.json` and
      `questions/*/raw/*.json` are fine — they are public Metaculus data — but filter response
      headers out of anything snapshotted.
- [ ] Before flipping: scan the full history with `gitleaks detect` or `trufflehog git file://.`
      and read the diff of `ledger/errors.jsonl` end to end.
- [ ] Rotate both secrets at the moment of flipping, on principle. It costs ten minutes and
      removes the whole class of "was anything ever in there" questions.
- [ ] Decide whether publishing forecasts and reasoning **mid-season** is acceptable. It is
      within the rules and normal in this tournament — the bot's private Metaculus comments are
      made public at intervals anyway — but competing bot makers can read your scaffold while
      you are still being scored against them. Flipping between seasons is the conservative
      choice.
- [ ] After flipping: Actions minutes become **unlimited**, so raise the sweep to
      `7,27,47 * * * *` and drop the minutes guard (§10.7). Remember the 60-day auto-disable now
      applies — irrelevant while the bot commits daily, relevant if you ever pause it.

---

## 13. Recommended schedule — and why

**`17 1 * * 2,5` — 01:17 UTC Tuesday and Friday** for triage.

That is **03:17 CEST** in summer and **02:17 CET** in winter, bracketing the requested 3 a.m.
local. GitHub cron is UTC-only and ignores DST, so a fixed local hour is not achievable; this
keeps the run in the small hours year-round.

Reasoning, by weight:

1. **After the US session has fully closed** (21:00 UTC) and after the US evening news cycle, so
   a re-fetched Kalshi or Polymarket price is a real close, not a mid-session quote.
2. **Before US data releases.** BLS and most US federal statistics drop at 08:30 ET
   (12:30/13:30 UTC). At 01:17 UTC the job never straddles a release.
3. **Off the hour.** GitHub's shared scheduler is oversubscribed at `:00` and worst at 00:00
   UTC, where runs are routinely delayed 10+ minutes or skipped. `:17` is uncontended.
4. **Tuesday/Friday splits the week 3/4**, matching the weekend news gap.

Companions: `23 3 * * *` for the daily sync (different hour and minute from triage so they never
queue behind each other), and **`7,37 * * * *` for the sweep** — every 30 minutes, which gives
two to three attempts inside a 90-minute window. The official Metaculus template uses
`7,27,47 * * * *`; we start one step slower because the repo is private and the gate bills a
full minute per run either way (§12.5). Raise it to the template's cadence once
`missed_window` counts justify the extra ~$7/month, or immediately on going public. MiniBench rounds
start **Monday every other week**, so expect the sweep to do real work in Monday–Friday bursts
and almost nothing in the off week; that is the shape the budget guard must tolerate.

---

## 14. Code optimisations for the bot-centric workload

Beyond the deletions in §5.2, these are the changes that matter once the repo holds hundreds of
questions and runs 70× a day.

1. **`new_question.py --from-json`** — scaffold from the roster payload the poll already
   fetched. Saves one API call per question and removes the last import of the Playwright path.
2. **No `charts/`, no `research.md` for one-shot questions.** Two fewer writes per question and
   hundreds fewer empty directories; `test_research_log_is_not_an_empty_stub` skips them.
3. **Lazy question loading.** `_common.all_questions()` parses every `meta.yaml` on every call.
   Add `slugs()` (directory listing only) and let callers load what they need; keep
   `all_questions()` for the daily full pass.
4. **`INDEX.md` is regenerated only by the daily sync**, and lists open questions in full with a
   one-line summary for resolved ones. A 500-row table rewritten 70× a day is pure git churn and
   a guaranteed source of rebase conflicts between concurrent jobs.
5. **`status.py --json`** so the triage workflow and any future tooling consume structured
   output instead of re-parsing a human table.
6. **`log_forecast.py` gains `--percentiles` and `--tournament`**, and refuses to log a v2 on a
   one-shot question — the guard belongs at the write, not only in review.
7. **`calibration.py` records official scores.** MiniBench and FutureEval use a spot peer score
   computed against the other bots, which is not reproducible locally. Store what the API
   reports at resolution; keep the local Brier/log score as a secondary, self-consistent
   measure.
8. **`--changed-only` test parametrisation** (§11.3) — without it the pre-commit gate becomes
   unusable at a few hundred questions.
9. **Cache `uv` by `pyproject.toml`** in every workflow (`tests.yml` already does) and skip
   `uv sync --group dev` entirely in the gate job, which needs only `requests` and `pyyaml`.

---

## 15. Docs to update

| File | Change |
|---|---|
| `AGENTS.md` | New §"Operating modes": standard vs tournament. Amend §4 (CP hidden on tournament questions), §5 (5–8 sources in tournament mode), and rule 8 (one-shot carve-out). |
| `CLAUDE.md` | CI runs commit to `live-bot` by design, superseding "never commit unless asked". Document the model variables, the subagent roster, and the §10.3 budget rules. |
| `docs/tournament-protocol.md` | NEW. The 90-minute window, one shot, private comments (with the exact short format), hidden CP, MiniBench vs FutureEval, what to do when a window is missed. |
| `docs/runbook.md` | NEW. §10.8 — the symptom→command table, including the Actions spending-limit failure mode. |
| `docs/methodology.md` | New §"Tournament mode": the reduced checklist and *why* each dropped step is safe to drop. |
| `docs/update-protocol.md` | One-shot carve-out; replace the `claude -p "/status --act"` snippet with a pointer to `triage.yml`. |
| `docs/output-format.md` | Short-form tournament forecast block, and the Metaculus comment format (§2.3). |
| `SKILLS.md` | Add the three new skills; drop `metaculus-scraper` and `/review`. |
| `README.md` | Rewrite the top: this is a bot, here is how it runs, here is the kill switch, here is the cost report. |

---

## 16. Open questions to verify during implementation

Each one silently breaks a workflow if wrong. Do not paper over any of them.

1. **The Fall 2026 slug is not yet public.** Summer was `summer-futureeval-2026`, Spring
   `spring-aib-2026`. Discover it from the tournament URL at registration time — which is why
   `add-tournament` takes a URL, not a constant. `minibench` and `bot-testing-area` are stable
   and can be registered today.
2. **`GET /api/aggregation_explorer/`** — confirm the authenticated path, its parameter names
   (`post_id`? `question_id`?), and whether Pro/gold cohorts are exposed to a bot token at all.
   Only matters for non-tournament questions.
3. **Comment constraints** on `/api/comments/create/`: length limit, and whether
   `included_forecast: true` requires the forecast to already exist (submit first, then comment).
4. **Rate limits** for bot tokens. The 20-minute poll across several tournaments plus
   per-question detail fetches is modest, but confirm before raising `MAX_FORECASTS_PER_RUN`.
5. **Does the 90-minute window apply to FutureEval proper or only MiniBench?** The resources
   page states it for both. Verify against live questions in the first week and relax the sweep
   cadence if the real window is longer — that directly reduces the §12.5 minutes problem.
6. **`claude-code-action`'s human-actor check** rejects bot actors on scheduled runs, which
   GitHub attributes to whoever last edited the `cron` line. Confirm that is a human account.
7. **`execution_file` schema stability.** §9.4 depends on the final `result` record's shape.
   Write `record_usage.py` defensively: if the expected fields are missing, log a zero-cost
   record with `"parse_failed": true` rather than failing the job.
8. **Real cost per forecast.** Measure over two MiniBench rounds on Sonnet before deciding
   whether Opus is affordable for the seasonal tournament.
9. **GitHub billing endpoint for Actions minutes** (§9.5). The classic path is
   `GET /users/{user}/settings/billing/actions`; accounts migrated to the enhanced billing
   platform use a different one, and the default `GITHUB_TOKEN` does **not** carry billing
   scope — hence the separate `BILLING_READ_TOKEN` in §3.5. Verify which endpoint this account
   answers on, and make `record_usage.py` write `"actions": {"unavailable": true}` rather than
   fail when neither works. This meter is a convenience, never a dependency.

---

## 17. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| A malformed CDF silently mis-shapes every numeric forecast | High | Port the reference implementation; `tests/test_cdf.py`; dry-run on `bot-testing-area` |
| Double submission → rules violation | High | Four guards: `meta.tournament.submitted`, remote `my_forecast_exists()`, ledger uniqueness test, `log_forecast.py` refusing a v2 |
| Subscription quota drained | High | No-LLM gate; weekly spend guard (§10.4); circuit breaker; Sonnet defaults; §10.3 rules |
| An agent burning turns debugging a failure | High | §10.1 — Python handles all failures; two consecutive failures abort the run |
| OAuth token expiry stops the bot silently | Medium | Gate fails loudly on auth; breaker opens 24h; tracking issue opened; calendar reminder in §3.2 |
| Actions minutes exhausted mid-month (private repo) | Medium | Spending limit set to a non-zero value (§3.5); the §10.7 minutes guard warns at 85%; overage is ~$0.006/min so the real cost is single-digit dollars (§12.5) |
| A secret leaks into `errors.jsonl`, then the repo goes public | Medium | Redaction in `record_error.py` from the first commit, with a unit test (§12.6) |
| `live-bot` drifts from `main` | Medium | Merge `origin/main` at the start of every bot job |
| `INDEX.md` rebase conflicts between concurrent jobs | Medium | Regenerated only by the daily sync (§14.4) |
| Test suite unusable at 500 questions | Medium | `--changed-only` (§11.3) |
| Tournament mode leaks into standard forecasts | Medium | Mode derives from `meta.tournament`, never from a flag the agent picks |
| MiniBench's LLM-written criteria resolve counter-intuitively | Low–Medium | Rule 1 first, always; record the misread in the resolution post-mortem |

---

## 18. Definition of done

- [ ] Phase 0: `questions/` empty, ledger empty, lint and tests green; §5.2 deletions merged.
- [ ] `metaculus_api.py` fetches a post, lists rosters for `minibench` **and**
      `bot-testing-area`, and reports `my_forecast_exists` correctly.
- [ ] `tests/test_cdf.py` green; a numeric forecast is **accepted** by `bot-testing-area`.
- [ ] `/add-tournament https://www.metaculus.com/tournament/bot-testing-area/` registers and
      populates a roster; a second tournament registers alongside it and both appear in one poll.
- [ ] `update-tournament` scaffolds new questions at v0, retries a missing comment, marks a
      missed window, and records a resolution with its official score.
- [ ] `tournament-sweep` forecasts a `bot-testing-area` question, submits it, posts a **private**
      comment in the short format, and commits to `live-bot` — verified on the question page.
- [ ] A second sweep on the same question is refused by all four one-shot guards.
- [ ] `ledger/usage.jsonl` has a row per run; `usage_report.py` prints cost per forecast; the
      GitHub Step Summary shows it without opening a file.
- [ ] `WEEKLY_BUDGET_USD_EQUIV=0` makes the gate report `budget_exceeded` and **no Claude job
      starts**.
- [ ] A deliberately broken `METACULUS_BOT_TOKEN` fails at the gate, opens the breaker, creates
      one `bot-health` issue, and spends **zero tokens**.
- [ ] A deliberately broken CDF produces one `errors.jsonl` record with a working `reproduce`
      command, and the batch continues.
- [ ] `pre-commit run --all-files` passes locally; `validate_state.py` catches a hand-corrupted
      `meta.yaml` and a deleted ledger line.
- [ ] `SWEEP_ENABLED=false` stops the sweep within one cycle.
- [ ] `ledger/usage.jsonl` rows carry the Actions-minutes meter, or `unavailable: true` — and
      the job passes either way.
- [ ] An error body containing a fake `Authorization: Token abc123` header is written to
      `errors.jsonl` with the token **redacted**, proven by a unit test (§12.6).
- [ ] A non-zero Actions **spending limit** is set, with an alert at 75% (§3.5).
- [ ] No personal email address appears anywhere in the repo or in a commit author field.
- [ ] All three workflows run green from `workflow_dispatch` before any `cron` line is added.
- [ ] Docs in §15 updated; `AGENTS.md` and `CLAUDE.md` describe the bot, not the workbench.

---

## 19. Suggested implementation order

1. **Phase 0** — cleanup and deletions. One PR, mergeable immediately.
2. **§6.1–6.2** — API client + CDF + tests. The riskiest code, done first and in isolation.
3. **Phase 2** — schemas and their tests.
4. **§6.3–6.4** — submit script, aggregations rewrite, scraper deletion.
5. **Phase 6 (§11)** — validator and pre-commit, *before* the skills, so every later phase is
   guarded from the first commit.
6. **Phase 3** — skills: `add-tournament`, then `update-tournament`, then `tournament-sweep`.
7. **Phase 4 + 5 (§9, §10)** — subagents, model config, poll gate, usage accounting, error
   handling and budget guard. The gate and the guard must exist before any `cron` line does.
8. **Phase 7 (§12)** — workflows, `workflow_dispatch` only at first. Add `schedule:` last.
9. **Docs (§15).**
10. **Soak on `bot-testing-area` for a week**, then register **`minibench`** and run one full
    round end to end. Measure cost per forecast. Only then register the Fall 2026 season.
