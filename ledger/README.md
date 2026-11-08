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
tokens (`tokens`: the main agent; `tokens_all`: every agent), API-equivalent
`cost_usd_equiv`, web searches, permission denials. Written by `scripts/record_usage.py`;
the gate's weekly budget guard and its allowance estimate (`scripts/allowance.py`) read
it, and the results page charts it. Since 2026-11-08 (issue #20), each line also carries,
where the CLI reported it:

```jsonc
{"conclusion": "usage_limit",          // or "error" (is_error), else the result's subtype
 "model_resolved": "claude-opus-5-5", "claude_code_version": "2.1.319",
 "config": {"model": "opus", "effort": "high", "mode": "deep", "max_web_searches": 50,
            "min_searches": 15, "scout_model": "sonnet", "sha": "164a625", ...},
 "allowance": {"events": 3, "status": "rejected", "rejected": true,
               "rejected_window": "five_hour", "rejected_until": "2026-11-02T12:10:00Z",
               "windows": {"five_hour": {"first": 90.0, "last": 97.0,
                                         "resets_at": "2026-11-02T12:10:00Z"}},
               "overage": {"enabled": false, "in_use": false}},
 "delta_allowance": {"five_hour": 7.0},  // last - first reading, percent points
 "rate_limit_events_raw": [{"status": "allowed_warning", "rateLimitType": "five_hour",
                            "utilization": 0.9, "resetsAt": 1762085400}],
 "terminal_reason": "api_error", "errors": ["rate_limit: Claude AI usage limit reached"]}
```

Utilization is in percent in `allowance` and verbatim (a 0–1 fraction) in the raw
events; the CLI sends a reading only at its warning thresholds, so most windows carry a
reset time and no reading. A line before 2026-11-08 has none of these fields; there a
one-turn, zero-cost line with an empty `by_model` is a refusal logged as a success.

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
