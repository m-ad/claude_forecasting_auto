# What will the EIA report as the week-over-week change in U.S. commercial crude oil inventories (excluding SPR) for the week ending 6 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46406/ |
| **Tournament** | minibench — one shot, window 2026-11-02T16:03:30Z -> 2026-11-02T19:03:30Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-12 |
| **Status** | closed |
| **Current forecast** | Median 700, IQR [-2300, 3700] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves on the "Week-on-week change for United States" figure for commercial crude (excluding SPR) in EIA's Weekly Petroleum Status Report for the week ending Friday **6 November 2026**, published Thursday 12 November 2026, 12:00 ET (Veterans Day shift). The answer is in thousand barrels, draws negative (−1,892 for the week ending 23 October). Revisions later do not matter.

Period arithmetic, from the source: the last published week is 23 Oct 2026 (410,625 kb, −1,892). The week ending 30 Oct is due 4 Nov (not yet out). The target is therefore **two weeks ahead** of the last published week, and only the 6 Nov week's own change counts (not the cumulative change). The bounds are −15,000 to +15,000, open at both ends. No fallback formula applies today.

### Outside view

Reference class: the weekly change in the first week(s) of November, 2019–2025 (n=10 weeks, EIA series): all ten were builds; median about +3.9M bbl, range +1.0M to +13.9M. Recent 52-week volatility is high: standard deviation about 5.6M bbl, with about 28% of weeks in 2025–26 beyond ±5M bbl (35% in 2026).

### Inside view

2026 differs from the seasonal pattern. Four straight draws (−3.2M, −8.6M, −3.1M, −1.9M) took stocks to 410.6M; crude exports were 4.85M b/d in the week of 23 Oct; Brent is near $115; the SPR is at about 283M and nearly stopped draining (−0.1M/week), which removes one source of commercial supply. Against that, refinery utilisation is already sliding (93.4% → 92.8%) into the autumn turnaround window, which usually builds crude; Gulf output is restarting after Hurricane Isaias; DOE SPR exchange barrels (4M authorised, up to 17M requested) would flow into commercial stocks; and some maintenance was deferred to 2027 (modest, about 144 kb/d). I blend the seasonal prior (+3.9M) with the current draw regime (about −3M), leaning slightly toward seasonal, for a median of about +0.7M and a wide, slightly right-skewed distribution (σ about 4.5–5M, fat tails as in 2026).

Adjustment from the last value (−1,892) to the median: one event, the early-November seasonal build pattern.

### Evidence

- EIA, week ending 23 Oct 2026: commercial crude 410,625 kb, change −1,892; consensus had been +15 kb. Cushing −624 kb; production 13,992 kb/d; imports 6,374; exports 4,854 (vs 3,442 prior week); runs 16,526; utilisation 92.8% [1][2][3].
- Recent changes (kb): Sep 25 +922; Oct 2 −3,186; Oct 9 −8,557; Oct 16 −3,060; Oct 23 −1,892 [1].
- Early-Nov changes: 2019 +7,929/+2,219; 2020 +4,277; 2021 +1,002; 2022 +3,925; 2023 +13,869; 2024 +2,149/+2,089; 2025 +5,202/+6,413 [1].
- SPR 282,583 kb, down only 100 kb on the week [1]; DOE exchange of up to 4M bbl authorised on 10 Oct, RFP for up to 17M on 16 Oct [5].
- IIR Energy: fall 2026 planned crude outages 144 kb/d lower than expected pre-war; some work deferred to 2027 [6].
- No API estimate or analyst consensus for the 30 Oct or 6 Nov weeks was available on 2 Nov.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Kalshi KXEIACRUDEW series | not retrieved (HTTP 429) | 2026-11-02 | exists, no price |
| Polymarket / Manifold | none for commercial weekly change | 2026-11-02 | |
| API / Reuters poll | not yet published for these weeks | 2026-11-02 | API for the 6 Nov week comes 10 Nov |

### What would change my mind

The API estimate (10 Nov) and the 4 Nov EIA print for the 30 Oct week: a large build then would reinforce the seasonal case, another big draw the export-driven regime. A sharp fall in prices on a peace deal would cut exports, favouring builds. Because the question is never revisited this is only a note on sensitivity: the median depends mostly on whether the seasonal build is stronger than the 2026 export pull.

### Sources

1. https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCESTUS1&f=W (accessed 2026-11-02)
2. https://boereport.com/2026/10/28/us-crude-stocks-and-distillate-inventories-fall-gasoline-stocks-rise-the-eia-says/amp/ (accessed 2026-11-02)
3. https://ir.eia.gov/wpsr/table1.csv (accessed 2026-11-02)
4. https://investinglive.com/commodities/us-eia-weekly-crude-oil-inventories-5202k-vs-603k-expected-20251105/amp (accessed 2026-11-02)
5. https://energynewsbeat.co/tag/stratigic-petroleum-reserve/ (accessed 2026-11-02)
6. https://www.industrialinfo.com/iirenergy/industry-news/article/some-us-refiners-deferring-maintenance-from-2026-to-2027--362613 (accessed 2026-11-02)
7. https://www.eia.gov/petroleum/supply/weekly/ (accessed 2026-11-02)

**Question**: [What will the EIA report as the week-over-week change in U.S. commercial crude oil inventories (excluding SPR) for the week ending 6 November 2026?](https://www.metaculus.com/questions/46406/)
**Date**: 2026-11-02
**Forecast**: Median 700 thousand bbl, IQR [-2,300, 3,700]
**Thesis**: Early-November weeks were builds in all of 2019–2025 (median +3.9M), but 2026 has four straight draws and heavy exports, so I blend them for a median near +0.7M with wide fat tails (52-week SD about 5.6M). Most sensitive to whether the seasonal refinery-turnaround build appears despite strong exports.
