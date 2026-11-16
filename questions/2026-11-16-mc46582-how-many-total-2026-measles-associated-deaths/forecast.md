# How many total 2026 measles-associated deaths will CDC's measles data page report as of November 26, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46582/ |
| **Tournament** | minibench — one shot, window 2026-11-16T09:38:14Z -> 2026-11-16T12:38:14Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | open |
| **Current forecast** | Median 7.8, IQR [6.8, 9] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The value in the "Total Deaths" row, "2026" column of the "U.S. Deaths" table on CDC's "Measles Cases and Outbreaks" page (cdc.gov/measles/data-research/index.html) as displayed at 23:59 UTC on 26 Nov 2026. State or media counts do not count. Today the page shows **6** (updated 13 Nov, data as of Thu 12 Nov) [1]. Periods: the last published data cutoff is Thu 12 Nov; the next regular cutoff is Thu 19 Nov (published ~19–20 Nov); the one after falls on Thanksgiving, Thu 26 Nov. That update may come early (~25 Nov), late (after the resolution moment, so it would not count), or be skipped. So **one or two** more refreshes count before resolution. Bins run 4…12, with open tails (<4 and >12). Gap to the state tallies: states report 10 (PA 7, WI 2, NY 1) [3][4][5], so CDC is 4 short. CDC added +1 and then +2 in its last two updates.

### Outside view

There is no clean reference class: this counter is new, and since CDC switched to NCHS (National Center for Health Statistics) death-certificate verification, it has lagged the states [2][6]. Its 2026 path: 1 (late Sep) → 2 (29 Sep) → 3 (29 Oct) → 4 (5 Nov) → 6 (12 Nov) [1][2][7]. That is about 0.6/week since late September and 1.5/week over the last two weeks. The status quo (6) is the floor of the plausible range, since CDC has never cut the 2026 figure after it posted. The exception is the August removal of two PA deaths at the HHS Secretary's request, which happened before those deaths were counted in the current series [6].

### Inside view

- There are 4 state-reported deaths CDC has not yet counted. Two were announced on 13 Nov, after the 12 Nov cutoff (PA Montour; WI Grant County) [3][5]. The other two are probably the disputed August Lancaster deaths or other deaths still in NCHS review. Speculation: CDC does not name the states it counts.
- New deaths are arriving fast (5 state-reported deaths between 2 and 13 Nov) [4][5], but NCHS coding lags, so deaths after about 18 Nov are unlikely to reach CDC by 26 Nov.
- Most likely outcome: the 19 Nov update adds 1–2 (to 7–8), and a Thanksgiving-week update, if one appears in time, adds 0–1 more. Median ~7.8. The tails allow for no additions at all (6) and for a fast catch-up to the state count plus new deaths (10–12).
- Distribution (probability per bin): ≤5 3%, 6 15%, 7 25%, 8 25%, 9 15%, 10 8%, 11 4%, 12 2%, >12 3%.

### Evidence

- CDC page: 6 deaths, 5,412 cases, updated 13 Nov 2026 (data as of 12 Nov) [1].
- Reuters/US News, 12 Nov: CDC confirms 6 deaths. CDC uses NCHS mortality data and did not name the states [2].
- PA DOH, 13 Nov: 7th PA death (Montour) [3]. WI DHS, 13 Nov: 2nd WI death [5]. NY first death, 2 Nov [4].
- CIDRAP / Al Jazeera, 13–14 Nov: states report 10 deaths versus CDC's 6 [4][6].
- The CDC weekly update was delayed once (28 Aug). No November delay found; no announced Thanksgiving schedule [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Kalshi / Polymarket | no death-count market found | 2026-11-16 | case-count markets only |

### What would change my mind

How fast NCHS verifies the two 13 Nov deaths: if the 19 Nov refresh still shows 6, the median falls to ~6.5. The Thanksgiving-week schedule matters too: an early update on 25 Nov adds upside, and a skipped one caps the outcome at the 19 Nov value.

### Sources

1. CDC, Measles Cases and Outbreaks — https://www.cdc.gov/measles/data-research/index.html (accessed 2026-11-16)
2. US News/Reuters, "US CDC Confirms Six Measles-Related Deaths in 2026" — https://www.usnews.com/news/top-news/articles/2026-11-12/us-cdc-confirms-six-measles-related-deaths-in-2026 (accessed 2026-11-16)
3. Pennsylvania DOH, seventh measles-associated death — https://www.pa.gov/agencies/health/newsroom/pa-department-of-health-confirms-seventh-measles-associated-deat (accessed 2026-11-16)
4. CIDRAP, "2 more people die of measles complications as US cases top 5,400" — https://www.cidrap.umn.edu/measles/2-more-people-die-measles-complications-us-cases-top-5400 (accessed 2026-11-16)
5. Wisconsin DHS, second measles death — https://www.dhs.wisconsin.gov/news/releases/111326.htm (accessed 2026-11-16)
6. Al Jazeera, "US loses measles-free status as two more deaths reported" — https://www.aljazeera.com/news/2026/11/14/measles-associated-deaths-reach-10-in-us-after-two-more-deaths-reported (accessed 2026-11-16)
7. CIDRAP, "CDC's new tracking method for measles deaths puzzles experts" — https://www.cidrap.umn.edu/measles/cdc-s-new-tracking-method-measles-deaths-puzzles-experts (accessed 2026-11-16)
8. CNN, "Trump's new CDC director ordered delay in counting 2 measles-related deaths" — https://www.cnn.com/2026/09/01/health/cdc-measles-deaths (accessed 2026-11-16)

**Question**: [How many total 2026 measles-associated deaths will CDC's measles data page report as of November 26, 2026?](https://www.metaculus.com/questions/46582/)
**Date**: 2026-11-16
**Forecast**: Median 7.8 deaths, IQR [6.8, 9.0] deaths
**Thesis**: CDC's NCHS-verified count (6 as of 12 Nov) lags the states' 10 and rose +1 and +2 in its last two weekly updates. With one or two refreshes left before 26 Nov (Thanksgiving may cost one), it most likely reaches 7–8. The outcome is most sensitive to how fast NCHS verifies the two deaths announced on 13 Nov.
