# What will the US core PCE year-over-year inflation rate for September 2026 be, released October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46132/ |
| **Tournament** | minibench — one shot, window 2026-10-19T06:37:15Z -> 2026-10-19T09:37:15Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-29 |
| **Status** | open |
| **Current forecast** | Median 3.1, IQR [3.04, 3.16] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the September 2026 figure in the "Change From Month One Year Ago" table on BEA's core PCE page, which is the year-over-year change in the PCE price index excluding food and energy, to one decimal. It is the value as first published in the Personal Income and Outlays release scheduled for 2026-10-29. Later revisions do not count. If the release is delayed, the first official publication counts. The outcomes are discrete steps of 0.1 pp from 2.6 to 3.8, with open tails at both ends.

### Outside view

The year-over-year rate is a 12-month sum, so one month moves it only by (new m/m − the m/m that drops out from Sep 2025). Recent values from BEA (accessed 2026-10-19) are May 3.2, Jun 3.0, Jul 3.0 and Aug 3.0. Historically, the y/y core PCE rate changes by 0 or ±0.1 pp in most months, and moves of ≥0.2 pp are uncommon outside shocks or annual revisions. The status-quo prior is therefore 3.0, with roughly symmetric ±0.1 steps.

### Inside view

The CPI and PPI for September are already out, and economists translate them into core PCE with good accuracy. The usual nowcast error is about ±0.05 pp on the m/m.
- TD Securities estimates **0.32% m/m**, revised down from 0.36% after the PPI, and sees y/y at **3.1%** [1].
- Nick Timiraos (WSJ) puts the mapping at **~0.34% m/m**, which would push the 12-month rate to **3.1%** [2].
- Core CPI rose 0.3% m/m against a 0.2% consensus [3].

The m/m that drops out (Sep 2025) was about 0.2% in the pre-revision data, so a 0.32–0.34% print adds about 0.1–0.15 pp to the y/y rate. I don't know the unrounded August value: anything from 2.95 to 3.04 is possible after the 2026 annual update. That gives an outcome of 3.1, with real chances of 3.0 (August unrounded low or a soft print) and 3.2 (August unrounded high plus a hot print).

The description's "consensus ~3.3%" (Trading Economics) looks like a model or stale number. The same source expected 3.3% for August, which came in at 3.0%. I give it little weight.

Approximate probability per outcome:

| Outcome | ≤2.8 | 2.9 | 3.0 | 3.1 | 3.2 | 3.3 | ≥3.4 |
|---|---|---|---|---|---|---|---|
| P | 0.02 | 0.04 | 0.20 | 0.50 | 0.19 | 0.04 | 0.01 |

### Evidence

- BEA page (accessed 2026-10-19): Aug 2026 3.0%, Jul 3.0%, Jun 3.0%, May 3.2%. The next release is October 29 [4].
- The August release (Sep 30) showed core +0.2% m/m and 3.0% y/y, against an expected 3.3%. It came with the annual update, which revised data back to 2021 [5].
- After the hot CPI (Oct 14), forecasters raised their September core PCE m/m estimates from about 0.21% to ≥0.3% [3]. After the PPI, TD settled at 0.32% [1], and Timiraos put it at ~0.34% (Oct 15) [2].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | |
| TD Securities | 0.32% m/m, 3.1% y/y | 2026-10-15 | [1] |
| WSJ / Timiraos mapping | ~0.34% m/m, 3.1% y/y | 2026-10-15 | [2] |
| Trading Economics (per question text) | 3.3% y/y | before 2026-10-19 | looks stale or model-based; discounted |
| Kalshi | no current y/y quote found | 2026-10-19 | |

### What would change my mind

- The unrounded August y/y value and the revised Sep-2025 m/m that drops out. These two decide between 3.0, 3.1 and 3.2.
- Any further nowcast revisions, for example from import prices or the PPI's portfolio-management and healthcare components.

### Sources

1. FXStreet, "United States PCE inflation forecast and Fed stance – TD Securities", https://www.fxstreet.com/news/united-states-pce-inflation-forecast-and-fed-stance-td-securities-202610151452 (accessed 2026-10-19)
2. Newsquawk, Timiraos core PCE projection headline, https://www.newsquawk.com/headlines/the-september-cpi-and-ppi-translate-into-a-core-pce-projection-of-around-034-which-would-be-the-highest-monthly-reading-since-january-says-wsjs-timiraos (accessed 2026-10-19)
3. roic.ai, "Wall Street set to raise core PCE inflation forecasts after hot CPI report", https://www.roic.ai/news/wall-street-set-to-raise-core-pce-inflation-forecasts-after-hot-cpi-report-10-14-2026 (accessed 2026-10-19)
4. BEA, PCE price index excluding food and energy, https://www.bea.gov/data/personal-consumption-expenditures-price-index-excluding-food-and-energy (accessed 2026-10-19)
5. Trading Economics, "US PCE inflation rises less than expected in August", https://tradingeconomics.com/united-states/pce-price-index-monthly-change/news/588260 (accessed 2026-10-19)
6. Babypips, "US core PCE August 2026 results", https://www.babypips.com/news/headline-us-core-pce-august-2026-results-gdp-revision-fed-outlook-2026-09-30 (accessed 2026-10-19)

**Question**: [What will the US core PCE year-over-year inflation rate for September 2026 be, released October 29, 2026?](https://www.metaculus.com/questions/46132/)
**Date**: 2026-10-19
**Forecast**: Median 3.10%, IQR [3.04%, 3.16%]
**Thesis**: Core PCE has been 3.0% y/y for three months. Nowcasts that map the hot September CPI and PPI into PCE put September core at 0.32–0.34% m/m and 3.1% y/y (TD Securities, WSJ/Timiraos). That is clearly above the ~0.2% Sep-2025 m/m that drops out. The main uncertainty is the unrounded August level, which splits the risk toward 3.0 or 3.2.
