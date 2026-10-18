# Ledger

`forecasts.jsonl` — one JSON object per line, append-only, never edited.

Four record shapes (`log_forecast.py` is the only writer of all four):

```jsonc
// a forecast version
{"ts":"2026-08-27T10:04:00+00:00","event":"forecast","slug":"2026-08-27-mc43505-...",
 "version":1,"source":"metaculus","post_id":43505,"type":"binary",
 "median":0.12,"iqr":[0.08,0.18],
 "community":{"cp":0.09,"pro":0.07,"gold":0.08,"n_forecasters":312},
 "thesis":"...","mode":"initial"}

// a resolution
{"ts":"2027-01-15T09:00:00+00:00","event":"resolution","slug":"2026-08-27-mc43505-...",
 "type":"binary","outcome":1.0,"resolution_source":"BEA advance estimate, 2027-01-15"}

// a submission the Metaculus API accepted (one-shot tournament questions)
{"ts":"2026-10-19T14:31:02+00:00","event":"submission","slug":"2026-10-19-mc46101-...",
 "post_id":46101,"question_id":46340,"tournament":"minibench",
 "payload":{"probability_yes":0.12},"comment_posted":true,"api_status":201}

// a rationale comment that went up after its submission (the daily sync's retry)
{"ts":"2026-10-20T03:24:10+00:00","event":"comment","slug":"2026-10-19-mc46101-...",
 "post_id":46101,"api_status":201}
```

One-shot rule, enforced by the tests: a slug has at most one `submission`, and it follows a
`forecast` for the same slug. Timestamps run forward per slug (parallel sweep jobs interleave
different questions; `.gitattributes` merges the file with git's `union` driver).

`usage.jsonl` — one line per Claude Code run in CI: job, slug, model, turns, duration,
tokens, API-equivalent `cost_usd_equiv`, web searches, permission denials. Written by
`scripts/record_usage.py`; the gate's weekly budget guard reads it.

Optional on a forecast record: `distribution`, the full forecast where median and IQR are
not all of it — `{"probabilities": {...}}` (required for multiple choice, exact option
labels), `{"percentiles": {...}}` (numeric/date/discrete) or `{"pmf": {...}}` (discrete).
`log_forecast.py add --distribution` validates it against the median and IQR.

Units: binary and multiple-choice values are fractions in [0, 1]; numeric values are native
units; date values (median, IQR and the resolution `outcome`) are Unix seconds.
`log_forecast.py` refuses a malformed forecast or outcome *before* appending, because a bad
line cannot be removed afterwards.

Why a separate ledger when `forecast.md` already has the numbers: scoring across
questions needs a stable machine-readable record. Parsing markdown for calibration
analysis works right up until the day it doesn't, and by then the history is
unrecoverable.

Because every *version* is logged, `calibration.py` can answer more than "was I right":
it can show whether your updates moved in the right direction, and whether you beat the
community prediction at the same points in time.

```bash
uv run scripts/calibration.py                 # all versions
uv run scripts/calibration.py --latest-only   # final version per question only
uv run scripts/calibration.py --plot cal.png
```
