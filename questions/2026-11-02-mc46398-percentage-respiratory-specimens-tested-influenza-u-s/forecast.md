# What percentage of respiratory specimens tested for influenza in U.S. clinical laboratories will be positive in CDC's FluView report for Week 44 (week ending November 7, 2026)?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46398/ |
| **Tournament** | minibench — one shot, window 2026-11-02T12:31:12Z -> 2026-11-02T15:31:12Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | Median 11.5, IQR [10.4, 12.8] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the number printed as the national "No. of positive specimens (%)" for clinical labs in the Week 44 FluView edition (MMWR week 44, ending Sat 2026-11-07, due Fri 2026-11-13), as first published (later revisions ignored). Last published edition is Week 42 (ending 2026-10-24): 4,061 / 53,102 = 7.6%. Week 43 (ending 2026-10-31, due 2026-11-06) is not yet out (URL returns 404 on 2026-11-02). So the target is **two** weekly steps beyond the last value (week 42 → 43 → 44), not one; the question text's "one-week-ahead" framing counts from the Week 43 edition, which I will not see. No fallback needed; the narrative-text fallback would give the same number. Gap: weekly steps so far were +1.1, +0.7, +1.9 pp (wk 39→42); two more steps of similar size give about 10–12%.

### Outside view

Reference class: the 14 historical two-week windows (2017-18 to 2025-26) in which national clinical-lab percent positive started at 5–9%. Two-week ratio ranged 1.13–2.6, median about 1.6–1.8, i.e. +1.4 to +8.4 pp, median about +3.7 pp. Applied to 7.6% that gives roughly 9.5–13%, centre 11–12%. Caveat: those windows come mostly from December main-wave growth, so they overstate typical growth for a slow early build-up. This season's own weekly ratios: 1.28, 1.14, 1.33 (avg about 1.25/wk, i.e. about 1.55 over two weeks → 11.8).

### Inside view

Growth ratios per week of 1.10 / 1.20 / 1.30 / 1.40 give 9.2 / 10.9 / 12.8 / 14.9. Evidence for continued growth: CDC says activity is rising and above normal for the time of year, 8 of 10 HHS regions rose in Week 42, ED visits, admissions and ILI all rose, FluSight expects increases through Nov 14, and 98.9% of subtyped A is a single H1N1 lineage (shared susceptibility; West Coast states reportedly already near 10%, spreading east). The 2022-23 H1N1/H3N2 wave went 5.2 → 7.9 → 12.3 over the same weeks (ratio 2.4 over two weeks). Evidence for slower growth: Week 41 step was only +0.7, regions 1 and 10 were flat, ILI is still below baseline, CDC cautions an early rise doesn't mean a big peak, and single-week noise (site mix, specimen volume) is ±0.5 pp. Median set at 11.5, slightly below the pure two-week ratio median because early-season build-ups grow more slowly than December waves. Tails: left to about 9 (stall), right to about 16 (2022-23-like explosive growth).

Distribution (percentiles): 5%: 9.0, 10%: 9.6, 25%: 10.4, 50%: 11.5, 75%: 12.8, 90%: 14.3, 95%: 15.4.

### Evidence

- Week 42 (ending 2026-10-24): 7.6% (4,061/53,102); cumulative since Oct 4 6.0%; 98.2% influenza A; 98.9% of subtyped A is H1N1pdm09; ILI 2.4% (baseline 2.9%); NHSN admissions 1.8/100k [1].
- Week 41: 5.7% (2,918/51,490) [2]. Week 40 5.0%, week 39 3.6% as first published (scout reading of those pages) [3].
- Historical series (clinical labs, wk42→wk44): 2022-23 5.18→12.27; 2019-20 2.12→5.53; 2023-24 1.49→2.57; 2024-25 0.73→1.23; 2025-26 0.65→1.10 [4][5]. 2026-27 is far ahead of any of these except 2022-23.
- CDC FluSight ensemble: likely increase in admissions and ED share to week ending Nov 14 [6]. CDC expects a moderate season peaking Dec–Feb [7].
- Local news (Oct 23): about 10% positivity in HI, CA, AZ, NV, WA, spreading east; novel H1N1 variant [8] (secondary source).

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Polymarket / Kalshi / Manifold | none found on percent positive | 2026-11-02 | only 2025-26 hospitalization-rate markets |
| CDC FluSight | increase expected in admissions to Nov 14 | 2026-10-30 | does not forecast lab percent positive |

### What would change my mind

The Week 43 figure (published Nov 6; I will not see it): a Week 43 value at or below about 8.3% would pull the forecast toward 9–10; a value of 10%+ would push it to 13–15. Also, any sign that West Coast saturation is spreading (more regions flat) would lower it.

### Sources

1. https://www.cdc.gov/fluview/surveillance/2026-week-42.html (accessed 2026-11-02)
2. https://www.cdc.gov/fluview/surveillance/2026-week-41.html (accessed 2026-11-02)
3. https://www.cdc.gov/fluview/surveillance/2026-week-40.html and 2026-week-39.html (accessed 2026-11-02)
4. https://www.cdc.gov/flu/weekly/weeklyarchives2022-2023/data/whoAllregt_cl45.html (accessed 2026-11-02)
5. https://www.cdc.gov/flu/weekly/weeklyarchives2025-2026/data/whoAllregt_cl43.html and https://www.cdc.gov/flu/weekly/weeklyarchives2023-2024/data/whoAllregt_cl47.html (accessed 2026-11-02)
6. https://www.cdc.gov/flu-forecasting/data-vis/current-week.html (accessed 2026-11-02)
7. https://cdc.gov/flu/season/2026-2027.html (search snippet; accessed 2026-11-02)
8. https://www.click2houston.com/news/local/2026/10/23/heres-why-health-officials-say-this-years-flu-season-is-starting-early-mutated-virus-lead-to-early-flu-season/ (accessed 2026-11-02)

**Question**: [What percentage of respiratory specimens tested for influenza in U.S. clinical laboratories will be positive in CDC's FluView report for Week 44 (week ending November 7, 2026)?](https://www.metaculus.com/questions/46398/)
**Date**: 2026-11-02
**Forecast**: Median 11.5%, IQR [10.4%, 12.8%]
**Thesis**: Week 42 was 7.6% with weekly ratios of about 1.25 and broad regional growth; two more weeks at that pace, tempered by early-season noise and signs of West Coast flattening, give about 11.5%. The forecast is most sensitive to whether weekly growth stays above about 1.15x or stalls.
