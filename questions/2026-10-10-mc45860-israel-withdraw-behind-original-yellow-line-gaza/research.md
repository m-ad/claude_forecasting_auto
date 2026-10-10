# Research log — Will Israel withdraw behind the original Yellow Line in Gaza before January 1, 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source:
- Release schedule / cutoff:
- Edge cases and ambiguities:

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|

## Decomposition

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|

## Dead ends and ruled-out hypotheses

## Open questions to chase next time


## Session 2026-10-10 (v1)

- Resolution criteria NOT retrieved: API text null (upcoming), aggregations script 403 (Cloudflare), scraper blocked after 170 s. Retry after 2026-10-12.
- Searches: Yellow Line withdrawal Oct 2026; original vs Orange Line; Board of Peace phase two; Hamas disarmament + election; Polymarket/Kalshi Gaza withdrawal (no live matching market found); Crisis Group Sept 2026; Makovsky/Kahana denial (none found).
- Key conflict: Makovsky/Kan (2026-08-18, anonymous) say Israel returned to original line vs J Street (2026-10-09) and Crisis Group (2026-09-21) saying 65–70%.
- Dead ends: i24 and Wikipedia pages stale (Wikipedia last edit 2026-07-28); no Sentinel/Mantic check.
- Next: read criteria, CP/Pro/gold after 2026-10-16, search Israeli election result, ISF/NCAG deployment, OCHA map.

## Session 2026-10-10 (v2: criteria retrieved, same day)

- Criteria retrieved via the aggregations script's own `_Fetcher` calling only `/api-proxy/posts/45860/` (the full script errors first on the aggregation explorer, which has nothing for an unopened question). Saved to `raw/metaculus-post-2026-10-10.json`. Comments: none yet.
- Criteria: announced withdrawal *behind* the original OCHA-mapped Yellow Line, physically vacated, credible sources, held ≥24h; any distance qualifies; Orange Lines irrelevant; background frames YES as Israeli-held share <53%.
- Consequences: the Makovsky/Kan Aug-18 "return to Yellow Line" path is irrelevant (LR≈1); a pullback only from post-ceasefire gains does not count.
- Rafah ISF pilot (Al Jazeera 2026-07-27): about 200 troops, foreign forces "strictly outside the Yellow Line", so it's not a candidate for a local behind-the-line handover.
- UN News 2026-09-12: Palestinians on <40% of Gaza's land.
- Forecast corrected 4.0% [2,8] → 2.0% [1,4]. The operator asked for v1 to be edited, but the append-only ledger test (Rule 8) and the version-count tests block an in-place edit, so the correction is logged as v2 and v1 stays as committed.
- Correction to the line above: the explorer *does* answer upcoming posts (probe 2026-10-10: 200 for 45860 with `open_time` set). The earlier failure was Cloudflare challenging the explorer while `/posts/` passed from the same warmed page. Fixed in `metaculus_aggregations.py` v4.5: a failed explorer on an upcoming post now still returns its criteria and comments.
