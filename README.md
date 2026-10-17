# Claude forecasting bot

An autonomous Metaculus bot. GitHub Actions polls the bot tournaments (MiniBench and the
FutureEval seasons); for every open question the bot has not forecast yet, it starts one
Claude Code session that reads the resolution criteria, researches, and logs a calibrated
forecast; deterministic code then submits it through the official Metaculus API with the
private rationale comment the rules require, and commits the record here.

It grew out of the operator-driven workbench `m-ad/claude_forecasting` (merged in as the
base, so upstream improvements arrive with `git merge upstream/main`). The same files still
serve the operator interactively: `/forecast`, `/update`, `/resolve`, `/status`.

Design goals: **every forecast is auditable and scoreable** (a per-question folder plus an
append-only ledger), **no human in the loop on tournament questions** (a rule), **one forecast
per question** (a rule), and **failure handled by Python, never by the model** (cost).

## How a tournament question is handled

```
every 30 min   tournament-sweep.yml
  gate         scripts/tournament_poll.py         (no model; 1 billed minute)
               budget ok? token ok? open questions the bot has not forecast?
  per question one matrix job, up to MAX_PARALLEL at once
    scaffold   scripts/new_question.py --tournament      question text cached to raw/
    forecast   claude -p  (tournament-forecast skill)   ~25 min cap, no Metaculus token
    submit     scripts/submit_metaculus.py              guards -> forecast -> private comment
    record     scripts/record_usage.py                  tokens and cost-equivalent
    commit     scripts/ci_commit.sh                     validate, rebase, push to main
daily 03:23    tournament-sync.yml                      missed windows, comment retries,
               scripts/tournament_sync.py               resolutions + official scores, INDEX.md
```

Tournament questions open at random hours for **3 hours** each; MiniBench rounds start every
other Monday with most of their ~60 questions in the first days. The rules this repository
follows, with sources: `docs/tournament-protocol.md`.

## Setup (operator, once)

1. **Metaculus bot account** — create it from your human account (Settings → My Forecasting
   Bots), copy its API token. Fill in the participation form (3 required questions).
2. **Claude token** — `claude setup-token` on your subscription; it prints a long-lived
   OAuth token. Put a reminder in your calendar for its expiry.
3. **Repository secrets** (Settings → Secrets and variables → Actions): `METACULUS_API_KEY`,
   `CLAUDE_CODE_OAUTH_TOKEN`.
4. **Actions spending limit** (private repo): set it above $0, or the schedule stops
   silently when the included minutes run out. See `docs/runbook.md` for the arithmetic.
5. **Smoke test**: Actions → tournament-sweep → Run workflow, `tournament: bot-testing-area`,
   `max_questions: 1`, `dry_run` ticked: the model forecasts, the folder is uploaded as an
   artifact, nothing is submitted or committed. Then once more without `dry_run`, and check
   the forecast and the private comment on the question page (as the bot: Settings → My
   Forecasting Bots → Switch to Bot Account).
6. **Go live**: repository variable `SWEEP_ENABLED` = `true`. Set it to anything else to stop.

Optional variables (defaults in brackets): `MODEL_FORECAST` [`opus`], `EFFORT_FORECAST`
[`high`], `MAX_MINUTES_PER_QUESTION` [`25`], `MAX_USD_PER_QUESTION` [`15`],
`MAX_QUESTIONS_PER_RUN` [`6`], `MAX_PARALLEL` [`3`], `WEEKLY_BUDGET_USD_EQUIV` [none],
`CLAUDE_CODE_VERSION` [`2.1.302`].

Which tournaments are polled is `tournaments/registry.yaml`:

```bash
uv run scripts/tournament_registry.py list
uv run scripts/tournament_registry.py set fall-futureeval-2026 --active
```

## Watching it

- Each sweep's **Step Summary** shows the gate's decision, the submission, and the run's cost.
- `uv run scripts/record_usage.py report` — rolling 7/30-day cost-equivalent per question.
- An open **`bot-health`** issue means a run failed; it carries the run links.
- `INDEX.md` lists every question; `uv run scripts/calibration.py` scores resolved ones.
- Symptom → command table: `docs/runbook.md`.

Do not change the bot because of what it forecast on a question that is still open: that is
"previewing" under the tournament rules. Read the outputs after close.

## Local use

```bash
uv sync --group dev
export METACULUS_API_KEY=...            # read-only use is fine; submission needs intent
uv run scripts/metaculus_api.py open minibench
claude                                  # /forecast, /update, /resolve, /status
```

Reproduce one CI job by hand: `uv run scripts/new_question.py --post-id <id> --tournament
bot-testing-area`, then ask Claude to follow `.claude/skills/tournament-forecast/SKILL.md`
on the slug, then `uv run scripts/submit_metaculus.py <slug> --dry-run`.

## Layout

```
AGENTS.md                 agent operating manual (CLAUDE.md imports it)
SKILLS.md                 index of skills, commands, scripts and workflows
INDEX.md                  generated table of all questions
docs/
  tournament-protocol.md  the bot-tournament rules and how the bot meets each
  runbook.md              what to do when something is red
  bot-migration-plan.md   the plan (rev 3) and bot-migration-progress.md, the step tracker
  methodology.md          the forecasting checklist, incl. tournament mode
  output-format.md        the fixed deliverable format, incl. the short tournament form
  update-protocol.md      when and how to revisit (operator questions); resolution
questions/<slug>/         meta.yaml · forecast.md · research.md (operator only) · raw/
ledger/forecasts.jsonl    append-only: forecasts, submissions, comments, resolutions
ledger/usage.jsonl        one line per Claude run: tokens, cost-equivalent, turns
tournaments/registry.yaml which tournaments the gate polls
scripts/                  see SKILLS.md
.claude/                  skills, commands, the research-scout agent, settings(.ci).json
.github/workflows/        tournament-sweep · tournament-sync · tests
```

## Tests

```bash
uv run ruff check . && uv run pytest -q
```

Mostly data tests: the ledger's shape and one-submission-per-question rule, the `meta.yaml`
schema (including the tournament block), the fixed `forecast.md` format, and agreement between
`meta.yaml`, the ledger and `INDEX.md`; plus unit tests of the API client, the gate, the CDF
builder and the one-shot submit path against fakes. See `tests/README.md`.
