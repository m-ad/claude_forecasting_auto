# How many confirmed U.S. measles cases for 2026 will CDC report in its November 27, 2026 update?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46609/ |
| **Tournament** | minibench — one shot, window 2026-11-17T07:43:45Z -> 2026-11-17T10:43:45Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-17 / 2026-11-17 / 2026-11-27 |
| **Status** | closed |
| **Current forecast** | Median 5940, IQR [5830, 6090] (v1, 2026-11-17) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-17

### What resolves YES

The question resolves to the 2026 national cumulative confirmed-case total on CDC's Measles Cases and Outbreaks page in the update **published Friday 27 Nov 2026**, whatever its data cutoff. If nothing is published that day, the **first update published after 26 Nov** governs. Only CDC's number counts: not Johns Hopkins, not state health departments. The scale runs from 5,300 to 6,800, and both bounds are open.

Arithmetic: the latest update, published 13 Nov with data to 12 Nov, shows **5,412** [1]. If CDC publishes on 27 Nov as usual, the updates of 20 Nov and 27 Nov add **2 weekly increments**, the second one in Thanksgiving week (Thursday 26 Nov is a holiday and also the usual noon-Thursday data cutoff). If CDC publishes early on Wednesday 25 Nov, or skips that week, the update of about 4 Dec governs, which means **3 increments**. A Monday or Tuesday release (30 Nov–1 Dec) with a 25 Nov cutoff still means 2. Recent weekly increments: +227 (to 1 Oct), an average of about 241 a week from 1 Oct to 29 Oct, +330 (5 Nov), +230 (12 Nov) [2][3]. Two increments of about 255 put the total near 5,920; three put it near 6,180.

### Outside view

The reference class is the last 8 weeks of this series: increments of 200 to 330 a week, with a mean of about 250. There have been 13 or more consecutive triple-digit weeks [3]. Over two or three weeks, epidemic count series like this one rarely jump in step. Week-to-week noise is about ±30%.

### Inside view

The momentum is mixed:
- **Slowing:** Pennsylvania, the biggest outbreak, has slowed to about 50 cases a week (1,505 on 9 Nov, 1,561 on 16 Nov) [4][5].
- **Rising:** Wisconsin is accelerating, adding about 100 a week (431 on 3 Nov, 551 on 10 Nov, 649 on 13 Nov) [6]. Indiana went from 138 to 188 in about a week [7], and Kentucky is above 200.

Together these support increments of about 230 to 300, not a slowdown.

Monte Carlo model (`model.py`):
- Each increment is drawn lognormal with a median of 255 and σ of 0.28, plus a shared trend shock (σ 0.18).
- The Thanksgiving-week increment is multiplied by a factor between 0.6 and 1.0 for reporting lag.
- Publication timing: 60% chance of a Friday 27 Nov update with 2 increments; 10% a late release with a 25 Nov cutoff (2 increments); 30% that the governing update is about 4 Dec (3 increments).

Output: p5 5,725 / p25 5,835 / p50 5,943 / p75 6,091 / p95 6,355. I widened the tails slightly for a possible batch of backlogged cases or a revision.

### Evidence

- CDC page, updated 13 Nov 2026: "As of November 12, 2026, 5,412 confirmed measles cases". There were 43 outbreaks and none was added that week [1].
- Weekly increments were +330 and then +230 (4.4%), per Contagion Live [2]. CIDRAP reported 13 consecutive triple-digit weeks [3].
- Pennsylvania had 1,561 cases on 16 Nov, 19 of them new since 13 Nov. The Inquirer reports that the outbreak appears to be slowing [4][5][8].
- Wisconsin had 649 cases on 13 Nov, up from 551 on 10 Nov and 431 on 3 Nov [6].
- Indiana had 188 cases on 16 Nov. Kentucky is above 200 [7].
- The Johns Hopkins tracker showed about 5,400 on 6 Nov, against CDC's 5,182 for 5 Nov, so CDC runs about 200 cases (one week) behind the state-level reporting [9].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-17 | |
| Kalshi "Measles cases this year" | 6,000+ at ~72% (stale cached page) | ~Oct 2026 | Full-year market, so it does not match this question; prices are stale |
| Polymarket 2026 thresholds | ≥5,000 at 76% | 2026-09-01 | Already resolved by the data; no market on the 27 Nov figure was found |

### What would change my mind

- **Publication timing.** If CDC publishes on Wednesday 25 Nov, or skips Thanksgiving week, the 4 Dec update with three increments governs. That moves the median up by about 250.
- **The 20 Nov increment.** A figure below 150 would point to a slowdown; one above 350 would point to a Wisconsin- and Midwest-driven acceleration.

### Sources

1. CDC, Measles Cases and Outbreaks — https://www.cdc.gov/measles/data-research/index.html (accessed 2026-11-17)
2. Contagion Live, Measles Update: November 13, 2026 — https://www.contagionlive.com/view/measles-update-november-13-2026 (accessed 2026-11-17)
3. CIDRAP, US measles total for 2026 tops 5,100 cases — https://www.cidrap.umn.edu/measles/us-measles-total-2026-tops-5100-cases (accessed 2026-11-17)
4. PA Department of Health, cases reach 1,561 in 46 counties — https://www.pa.gov/agencies/health/newsroom/pa-department-of-health-provides-statewide-update-on-measles-out18 (accessed 2026-11-17)
5. PA Department of Health, cases reach 1,505 — https://www.pa.gov/agencies/health/newsroom/pa-department-of-health-provides-statewide-update-on-measles-out17 (accessed 2026-11-17)
6. WBAY, Wisconsin measles cases climb to 551 — https://www.wbay.com/2026/11/11/wisconsin-measles-cases-climb-551-us-elimination-status-faces-review/ (accessed 2026-11-17); Wisconsin DHS release, 13 Nov — https://www.dhs.wisconsin.gov/news/releases/111326.htm (accessed 2026-11-17)
7. WDRB, Indiana reports 188 cases, Kentucky tops 200 — https://www.wdrbwave.com/2026/11/17/doctors-warn-about-measles-indiana-reports-188-cases-kentucky-tops-200/ (accessed 2026-11-17)
8. Philadelphia Inquirer, Pennsylvania measles outbreak appears to be slowing — https://www.inquirer.com/health/pennsylvania-measles-outbreak-cases-slowdown-20261102.html (accessed 2026-11-17)
9. Johns Hopkins IVAC tracker coverage — https://publichealth.jhu.edu/ivac/2026/2026-us-measles-cases-surpass-2025-level (accessed 2026-11-17)
10. Kalshi, Measles cases this year — https://kalshi.com/markets/kxmeasles/measles-cases/kxmeasles-26 (accessed 2026-11-17)

**Question**: [How many confirmed U.S. measles cases for 2026 will CDC report in its November 27, 2026 update?](https://www.metaculus.com/questions/46609/)
**Date**: 2026-11-17
**Forecast**: Median 5,940 cases, IQR [5,830, 6,090]
**Thesis**: Recent weekly CDC increments have been 230 to 330, adding to the 5,412 reported on 13 Nov. Pennsylvania is slowing, but Wisconsin, Indiana and Kentucky are rising, so two increments (one of them in Thanksgiving week) give about 5,900. The forecast is most sensitive to whether a 27 Nov update exists: if CDC skips or publishes early, the 4 Dec update (about 6,150) governs.
