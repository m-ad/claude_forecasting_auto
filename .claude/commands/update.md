---
description: Bayesian update of an existing forecast (tripwire check + live re-fetch)
argument-hint: <slug | metaculus-url | question fragment>
---

Update the forecast for: **$ARGUMENTS**

If that is not an exact slug, resolve it with `uv run scripts/status.py --find "$ARGUMENTS"`
and confirm the match before proceeding.

Load the `forecast-update` skill and follow it. Read `docs/update-protocol.md`.

Order matters: read the prior version first, decide Update vs. Re-analysis, check the v(N−1)
tripwires **by name** before general news search, then re-fetch the live Metaculus cohorts and
market prices and compare against the previous snapshot in `raw/`.

Your prior is your own last forecast, not the community prediction. State a direction and an
effect for every driver. Remember that elapsed time with nothing happening lowers the
probability of event-requiring questions — recompute the hazard rate rather than leaving the
number alone. "No change" is a valid, publishable update.

Prepend the new version with its revision table and tripwire-check table, rewrite the header
block, update `meta.yaml`, log to the ledger, refresh `INDEX.md`.
