# Tests

```bash
uv run pytest              # everything
uv run pytest -rs          # ... and say why anything was skipped
uv run pytest tests/test_ledger.py -q
```

These are mostly **data tests**. The scripts read the ledger and `meta.yaml` with
`.get()` chains that turn a missing key, a stale field, or a percentage stored where a
probability belongs into a quietly wrong row rather than an error. Nothing else in the
repo checks any of it, so each invariant is asserted here, once, with the failure message
naming the offending line or slug.

Every ledger line and every question folder is its own parametrised test case, so a
failure id points straight at the record to fix.

| File | Asserts |
|---|---|
| `test_ledger.py` | JSONL parses; timestamps are UTC and **non-decreasing per slug** (parallel sweep jobs interleave different questions); per-slug versions are 1..N with no gaps or duplicates; medians sit inside their IQR; binary values are fractions, not percent; an optional `distribution` has the shape its question type takes and agrees with its own median/IQR (multiple-choice vector sums to 1 and its leader equals the median; p50/p25/p75 equal median/IQR; the pmf's median is the median); a multiple-choice outcome is an option label; one resolution per slug, logged after its forecasts; `submission` records are 2xx, carry both ids and a tournament, follow a forecast, and **no slug is submitted twice**; a late `comment` follows a comment-less submission; the committed ledger is still a prefix of the working copy (rule 8, append-only) |
| `test_meta.py` | Folder naming; the exact `meta.yaml` key schema at every level; dates parse and run in order; `status`/`resolution`/`next_review` agree (resolved and dropped questions schedule no review); tripwires are dated, directional and bounded, and their `magnitude_unit` matches the question type (`pp` for probability questions, a time unit for date questions, the question's own `unit` for numeric ones); `meta.yaml` survives the `safe_dump` round-trip `log_forecast.py` performs on every write; `raw/` snapshots are valid, dated JSON; `templates/meta.yaml` still renders to the same schema; the `tournament` block's shape, a registered tournament slug, `question_id` on tournament questions, one-shot questions with no tripwires, no `next_review` and at most v1, missed windows closed out and never submitted |
| `test_forecast_md.py` | The fixed format from `docs/output-format.md`: header rows, the append-only sentinel, version sections newest-first and contiguous, required sections per version, the three-line `**Date**/**Forecast**/**Thesis**` block, one-decimal percentages, sources numbered with access dates, relative links that resolve, a post-mortem on resolved questions — and that the header block agrees with `meta.yaml`. One-shot questions use the short form (no scenario/sensitivity tables, ≥ 5 sources, no `research.md`); unlogged drafts (v0) are skipped |
| `test_consistency.py` | `meta.yaml` ↔ ledger ↔ `INDEX.md`: every forecast is logged, `current` equals the latest ledger record, resolutions and submissions appear in both places or neither (same payload, ids, comment state), submissions name registered tournaments, no orphan slugs, `INDEX.md` is not stale |
| `test_tournaments.py` | `tournaments/registry.yaml`: schema, unique slugs, policy fields, scored outranks unscored; the registry module's API and CLI |
| `test_bot.py` | Offline: the API client (token header, user agent, one retry on 5xx, none on 4xx, auth vs. Cloudflare, 429 backoff, redaction, pagination); the gate (budget guard, candidate filtering and order); the usage meter (every CLI output shape, killed runs); the one-shot submit path (each guard stops the POST, forecast then private comment, missed window, failed comment, dry run, comment extraction); the daily sync; and that the CI settings and workflow keep the model away from submission and secrets |
| `test_submit_metaculus.py` | Offline unit tests for the Metaculus submission payloads: binary clipping, multiple-choice label matching and renormalisation, CDFs that obey Metaculus' bound and minimum-step rules and keep the quartiles, spec/ledger version and median agreement, the unchanged-forecast skip; and that no model-facing file (skills, commands, agents) other than the operator's `metaculus-submit` skill references the script |
| `test_scripts.py` | Unit tests for `slugify`, `days_until`, `fmt_forecast`, `find_slug`, `_outcome_value`, `brier`/`log_score`/`summarise`/`buckets`, the multiple-choice scorer (`mc_brier`/`mc_log_score`/`mc_label`/`summarise_mc`, and a `calibration.py` run over a multiple-choice resolution), `distribution_problems`, `log_forecast.py`'s pre-append checks (median inside a non-degenerate IQR, probabilities not percent, `--distribution`), its outcome handling (verbatim multiple-choice labels, yes/no-only binary outcomes, date outcomes as Unix seconds), `cached_options`, `read_ledger`, `new_question.py` scaffolding from the API (group posts, upcoming posts, tournament questions with their raw snapshot, `--reuse`), the one-shot guards and submission records in `log_forecast.py`, `status.py`'s handling of dropped and one-shot questions and its resolution-date fallback, `save_meta`/`load_meta`; plus CLI smoke tests over the real repo |

## Conventions

- Loaders live in `conftest.py` and run at **collection** time — a new question folder or
  a new ledger line adds test cases automatically, with no registration step.
- Vocabularies (`SOURCES`, `QUESTION_TYPES`, `STATUSES`, `MODES`) are re-declared in
  `conftest.py` rather than imported from `scripts/_common.py`, so that a typo in a
  script constant fails a test instead of being asserted against itself.
- A test that cannot apply (an unresolved question, a non-binary format check) calls
  `pytest.skip` with a reason; `-rs` lists them.
- Dates are compared through `conftest.as_date`, which accepts both the quoted strings
  `safe_dump` writes and the `datetime.date` objects PyYAML produces from unquoted ones.

## Adding a test

Assert an invariant some script already *relies on* but never checks. Put the slug or the
line number in the assertion message: these tests are read when they fail, from a
one-line summary, by someone who needs to know which record to open.
