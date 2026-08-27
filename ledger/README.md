# Ledger

`forecasts.jsonl` — one JSON object per line, append-only, never edited.

Two record shapes:

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
```

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
