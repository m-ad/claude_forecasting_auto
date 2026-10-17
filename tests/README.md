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
| `test_ledger.py` | JSONL parses; timestamps are UTC and **non-decreasing in file order**; per-slug versions are 1..N with no gaps or duplicates; medians sit inside their IQR; binary values are fractions, not percent; an optional `distribution` has the shape its question type takes and agrees with its own median/IQR (multiple-choice vector sums to 1 and its leader equals the median; p50/p25/p75 equal median/IQR; the pmf's median is the median); a multiple-choice outcome is an option label; one resolution per slug, logged after its forecasts; the committed ledger is still a prefix of the working copy (rule 8, append-only) |
| `test_meta.py` | Folder naming; the exact `meta.yaml` key schema at every level; dates parse and run in order; `status`/`resolution`/`next_review` agree (resolved and dropped questions schedule no review); tripwires are dated, directional and bounded, and their `magnitude_unit` matches the question type (`pp` for probability questions, a time unit for date questions, the question's own `unit` for numeric ones); `meta.yaml` survives the `safe_dump` round-trip `log_forecast.py` performs on every write; `raw/` snapshots are valid, dated JSON; `templates/meta.yaml` still renders to the same schema |
| `test_forecast_md.py` | The fixed format from `docs/output-format.md`: header rows, the append-only sentinel, version sections newest-first and contiguous, required sections per version, the three-line `**Date**/**Forecast**/**Thesis**` block, one-decimal percentages, sources numbered with access dates, relative links that resolve, a post-mortem on resolved questions — and that the header block agrees with `meta.yaml` |
| `test_consistency.py` | `meta.yaml` ↔ ledger ↔ `INDEX.md`: every forecast is logged, `current` equals the latest ledger record, resolutions appear in both places or neither, no orphan slugs, `INDEX.md` is not stale |
| `test_submit_metaculus.py` | Offline unit tests for the Metaculus submission payloads: binary clipping, multiple-choice label matching and renormalisation, CDFs that obey Metaculus' bound and minimum-step rules and keep the quartiles, spec/ledger version and median agreement, the unchanged-forecast skip; and that no workflow file other than the `metaculus-submit` skill references the script |
| `test_metaculus_skills.py` | Offline regression tests for the two Metaculus access skills: proxy parsing without credentials, the TLS 1.2 downgrade triggers, Cloudflare-challenge detection, all cohorts in one request, the backoff length, no `HeadlessChrome` user agent, unscaling and display formats, the `METACULUS_API_KEY` path and its browser fallback, group posts, upcoming posts behind a challenged explorer, and pool blocks (the circuit breaker and its marker, the `blocked` metadata result, `fetch_many` sharing one browser, exit codes) |
| `test_scripts.py` | Unit tests for `slugify`, `days_until`, `fmt_forecast`, `find_slug`, `_outcome_value`, `brier`/`log_score`/`summarise`/`buckets`, the multiple-choice scorer (`mc_brier`/`mc_log_score`/`mc_label`/`summarise_mc`, and a `calibration.py` run over a multiple-choice resolution), `distribution_problems`, `log_forecast.py`'s pre-append checks (median inside a non-degenerate IQR, probabilities not percent, `--distribution`), its outcome handling (verbatim multiple-choice labels, yes/no-only binary outcomes, date outcomes as Unix seconds), `cached_options`, `read_ledger`, `fetch_metaculus.py`'s cache naming (a blocked fetch is cached as `metaculus-api-<date>.json`) and slug resolution, `status.py`'s handling of dropped questions and its resolution-date fallback, `save_meta`/`load_meta`; plus CLI smoke tests over the real repo |

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
