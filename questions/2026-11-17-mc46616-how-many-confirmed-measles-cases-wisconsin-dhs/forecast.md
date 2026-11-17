# How many confirmed measles cases will Wisconsin DHS report for 2026 as of November 27, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46616/ |
| **Tournament** | minibench — one shot, window 2026-11-17T18:32:14Z -> 2026-11-17T21:32:14Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-17 / 2026-11-17 / 2026-11-27 |
| **Status** | open |
| **Current forecast** | Median 905, IQR [840, 985] (v1, 2026-11-17) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-17

### What resolves YES

The question resolves to N, the number in the headline sentence ("As of [date], DHS has confirmed N cases of measles in Wisconsin … in 2026") on https://www.dhs.wisconsin.gov/outbreaks/index.htm as displayed at 23:59 UTC on Fri Nov 27, 2026 (17:59 CST). N is taken as published, probable cases included, whatever the "as of" date says. The latest value is **651, as of Nov 13** (page fetched 2026-11-17). DHS updates on Tuesdays and Fridays and sometimes posts a few days after the data date. The figure displayed at resolution will therefore be the Nov 24 data (11 days after Nov 13) or, if the post-Thanksgiving update goes up the same day, the Nov 27 data (14 days). At 20–25 new cases per day that gives 651 + 220–350 ≈ 870–1,000. The range is 500–1,500 with open bounds.

### Outside view

The reference class is the recent trajectory of this series: 267 (Oct 13), 392 (Oct 30), 431 (Nov 3), 477 (Nov 6), 551 (Nov 10), 651 (Nov 13). The daily increase went from ~7/day in October to ~15/day (Nov 3–6), ~18/day (Nov 6–10) and ~33/day (Nov 10–13). In large US outbreaks among unvaccinated people, such as West Texas in 2025, growth lasted for months and then plateaued over 6–8 weeks as the pool of susceptible people ran out. A sharp stop inside two weeks of accelerating growth is unusual.

### Inside view

The Nov 10→13 rise of 100 came from real growth, mainly Grant (153→222) and Jackson (2→45); Columbia already had 33 in September, so it was not a one-off backlog. I do not carry forward the full 33/day because three-day increments are noisy and batchy. I use 18–25/day as the central rate. Against that, reactive vaccination (about 2,000 MMR doses delivered), the Thanksgiving holiday slowing testing and reporting, and posting lags pull the count down. Central scenarios: Nov 24 data at ~20/day ≈ 870, Nov 27 data at ~22/day ≈ 960. The median is 905. Tails: a sharp slowdown or a stale page leaves ~740 (p5). Continued acceleration to 35/day with the Nov 27 update posted gives ~1,150 (p95).

### Evidence

- DHS outbreaks page, fetched 2026-11-17: "As of November 13 … confirmed 651 cases"; 14 hospitalizations, 2 deaths; county counts Grant 222, Lafayette 122, Iowa 97, Columbia 47, Chippewa 45, Jackson 45 [1].
- Press coverage: 649 cases in 20 counties as of Nov 13; second pediatric death announced Nov 13 [2][3].
- DHS measles page: dashboard updated twice a week, cases counted by rash onset [4].
- No report of a slowdown as of Nov 17 (search, 2026-11-17).
- West Texas 2025 ended at ~750 cases after about four months; the decline was attributed to depleted susceptibles and vaccination [5].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-17 | |
| Polymarket / Kalshi | none found | 2026-11-17 | only national CDC-count markets exist |

### What would change my mind

- The Nov 17 or Nov 20 update. Under ~720 would mean the Nov 13 jump was a batch and the pace is closer to 10/day. Over ~800 by Nov 17 would mean ~35/day and push the median past 1,000.
- Whether DHS posts on Fri Nov 27 before 17:59 CST, which is worth ~60–90 cases.

### Sources

1. Wisconsin DHS, Outbreaks, Recalls, and Investigations — https://www.dhs.wisconsin.gov/outbreaks/index.htm (accessed 2026-11-17)
2. Wisconsin DHS news release (second pediatric death) — https://www.dhs.wisconsin.gov/node/154671 (accessed 2026-11-17)
3. Wisconsin DHS news release Nov 5 — https://dhs.wisconsin.gov/news/releases/110526.htm (accessed 2026-11-17)
4. Wisconsin DHS, Immunizations: Measles — https://www.dhs.wisconsin.gov/immunization/measles.htm (accessed 2026-11-17)
5. ABC News, "Measles cases seem to be slowing down in the US" — https://abcnews.com/Health/measles-cases-slowing-us/story?id=122221061 (accessed 2026-11-17)
6. Spectrum News, Columbia County cases Sep 22 — https://spectrumnews1.com/wi/milwaukee/news/2026/09/22/measles-cases-wisconsin (accessed 2026-11-17)

**Question**: [How many confirmed measles cases will Wisconsin DHS report for 2026 as of November 27, 2026?](https://www.metaculus.com/questions/46616/)
**Date**: 2026-11-17
**Forecast**: Median 905 cases, IQR [840 cases, 985 cases]
**Thesis**: DHS shows 651 cases as of Nov 13, and the daily increase rose from ~15 to ~33 over Nov 3–13. Extrapolating 18–25/day for 11–14 days to the Nov 24 or Nov 27 update gives ~870–960. The result depends most on whether reactive vaccination and Thanksgiving slow ascertainment, and on whether the Nov 27 update is posted before resolution.
