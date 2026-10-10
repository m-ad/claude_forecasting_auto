---
description: Record a question's resolution, score every version, write the post-mortem
argument-hint: <slug> <yes|no|value|"option label">
---

Resolve: **$ARGUMENTS**

1. Verify the resolution against the **question's own resolution source**, not against news
   coverage of it. Quote the value/decision and its publication date.
   **For Metaculus questions the source is Metaculus's own posted resolution** (the `resolution`
   field / resolved banner), not the underlying event. Look it up there and use it verbatim; do
   not resolve from the event yourself. If Metaculus has not resolved it yet, say so and stop —
   do not log a resolution. Cite the underlying event only as context.
2. `uv run scripts/log_forecast.py resolve <slug> --outcome <outcome>`. For multiple choice the
   outcome is the exact option label, quoted.
3. Append a `## Resolution — <date>` section to `questions/<slug>/forecast.md` containing:
   - what happened and via which source;
   - a per-version score table (Brier for binary; multi-class Brier + log score for multiple
     choice, from each version's recorded option vector; absolute + quantile-coverage error for
     numeric/date), with the Metaculus community prediction at the same timestamps as the
     benchmark — state plainly whether you beat the crowd;
   - **the tripwire that should have existed and did not** (mandatory);
   - one line on calibration: over- or under-confident, and by how much.
4. Set `status: resolved` in `meta.yaml`.
5. `uv run scripts/calibration.py` and report how the overall record moved.
