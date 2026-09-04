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
| `test_ledger.py` | JSONL parses; timestamps are UTC and **non-decreasing in file order**; per-slug versions are 1..N with no gaps or duplicates; medians sit inside their IQR; binary values are fractions, not percent; one resolution per slug, logged after its forecasts; the committed ledger is still a prefix of the working copy (rule 8, append-only) |
| `test_meta.py` | Folder naming; the exact `meta.yaml` key schema at every level; dates parse and run in order; `status`/`resolution`/`next_review` agree; tripwires are dated, directional and bounded, and their `magnitude_unit` matches the question type (`pp` for probability questions, a time unit for date questions, the question's own `unit` for numeric ones); `meta.yaml` survives the `safe_dump` round-trip `log_forecast.py` performs on every write; `raw/` snapshots are valid, dated JSON; `templates/meta.yaml` still renders to the same schema |
| `test_forecast_md.py` | The fixed format from `docs/output-format.md`: header rows, the append-only sentinel, version sections newest-first and contiguous, required sections per version, the three-line `**Date**/**Forecast**/**Thesis**` block, one-decimal percentages, sources numbered with access dates, relative links that resolve, a post-mortem on resolved questions — and that the header block agrees with `meta.yaml` |
| `test_consistency.py` | `meta.yaml` ↔ ledger ↔ `INDEX.md`: every forecast is logged, `current` equals the latest ledger record, resolutions appear in both places or neither, no orphan slugs, `INDEX.md` is not stale |
| `test_scripts.py` | Unit tests for `slugify`, `days_until`, `fmt_forecast`, `find_slug`, `_outcome_value`, `brier`/`log_score`/`summarise`/`buckets`, `read_ledger`, `save_meta`/`load_meta`; plus CLI smoke tests over the real repo |

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
