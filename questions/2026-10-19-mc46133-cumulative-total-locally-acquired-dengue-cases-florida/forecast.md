# What cumulative total of locally acquired dengue cases in Florida in 2026 will the FDOH Week 42 Arbovirus Surveillance Report show?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46133/ |
| **Tournament** | minibench — one shot, window 2026-10-19T06:48:41Z -> 2026-10-19T09:48:41Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 480, IQR [450, 510] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the year-to-date count printed in the "2026 Dengue Cases Acquired in Florida" section of the Florida Department of Health (FDOH) Weekly Arbovirus Surveillance Report for Week 42 (the week ending 2026-10-24, expected around 2026-10-29). Travel-associated cases do not count. If the Week 42 report is missing, the latest report published by 2026-10-30 and dated after Week 40 is used instead, which would in practice be Week 41. Whatever figure the resolving report prints governs, including any revision. The question's range is 380–600, and both bounds are open.

### Outside view

There is no clean reference class: the 2026 outbreak is already the largest in the continental US in decades, beating the 2023 record of about 200 locally acquired cases [3][4]. The status-quo baseline is the recent run rate. The FDOH cumulative counts are 41 (Week 33), 111 (W35), 190 (W37), 252 (W38), 296 (W39) and 368 (W40) [1][2][5]. The last three weekly increments were +62, +44 and +72, a mean of about 59 per week with a standard deviation of about 14. Week 42 adds two weeks of accrual to 368, so the naive projection is 368 + 2×59 ≈ 486.

### Inside view

- **Upward:** Weekly increments have not yet clearly peaked; the largest so far, +72, is the latest. Reporting lag backfills earlier onsets, and transmission of the DENV-2 serotype in Hillsborough remains active, with positive mosquito pools reported [2].
- **Downward:** Late October brings cooler, drier weather, and the Hillsborough/Pinellas state of emergency has stepped up mosquito spraying [3][6]. Florida's arbovirus transmission usually tapers through late October and November.
- **Report-timing risk:** If the Week 42 PDF is late, Week 41 (about 420–445) resolves instead. I put roughly 5–10% on that, which is why the left tail is fattened.

Net: two-week accrual is centred at about 110 (roughly 55 per week, slightly below the latest week because of seasonality and control efforts). The distribution is skewed right in case the epidemic is still accelerating. Percentiles: p5 410, p10 425, p25 450, p50 480, p75 510, p90 540, p95 562. No model file was written; this is arithmetic on the series above.

### Evidence

- FDOH and the question background: 368 cumulative locally acquired cases as of the Week 40 report (Oct 4–10, published 2026-10-15), 310 of them in Hillsborough [1].
- Week ending Oct 3: +44, total 296; 259 in Hillsborough and 20 in Pinellas (WGCU, 2026-10-09) [5].
- Through Aug 29: 73 cases; all Hillsborough cases are DENV-2; 14 positive mosquito pools (FOX13/WUSF, early Sept) [2][6].
- AP (late Sept): one death, local emergencies declared, the most cases in a single year for any state since the 1940s [3][4].
- The Week 41 PDF returned a 404 on 2026-10-19, as expected since it is not yet published (due around Oct 22) [1].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no matching market |

### What would change my mind

The Week 41 increment (published around Oct 22) is what this forecast depends on most. A Week 41 figure of +90 or more would move the median above 510; +30 or less would point to the epidemic having peaked, with a median nearer 450. A delayed Week 42 report would make Week 41 the resolving figure.

### Sources

1. FDOH Arbovirus Surveillance page and weekly reports, https://www.floridahealth.gov/statistics-data/population-surveillance/arbovirus-surveillance/ (accessed 2026-10-19)
2. FOX13, "Dengue fever: Locally acquired cases surge to 65 across Bay Area", https://www.fox13news.com/news/dengue-fever-local-cases-tampa-bay-area (accessed 2026-10-19)
3. ABC News/AP, "Florida confirms death from dengue as state struggles with recent outbreak", https://abcnews.com/Health/wireStory/florida-confirms-death-dengue-state-struggles-worst-recent-136572973 (accessed 2026-10-19)
4. Gizmodo, "A wildly unusual outbreak of dengue is hitting Florida hard", https://gizmodo.com/a-wildly-unusual-outbreak-of-dengue-is-hitting-florida-hard-as-several-counties-declare-state-of-emergency-2000818145 (accessed 2026-10-19)
5. WGCU, "Dengue fever cases on the rise in Florida" (2026-10-09), https://www.wgcu.org/health/2026-10-09/dengue-fever-cases-on-the-rise-in-florida (accessed 2026-10-19)
6. WUSF, "Hillsborough reports an 'unusual increase' in locally acquired dengue", https://wusf.org/text/health-news-florida/2026-09-04/hillsborough-experiences-dengue-cases-how-to-protect-yourself (accessed 2026-10-19)

**Question**: [What cumulative total of locally acquired dengue cases in Florida in 2026 will the FDOH Week 42 Arbovirus Surveillance Report show?](https://www.metaculus.com/questions/46133/)
**Date**: 2026-10-19
**Forecast**: Median 480 cases, IQR [450 cases, 510 cases]
**Thesis**: The FDOH total was 368 at Week 40, after recent weekly additions of +62, +44 and +72 (mean about 59). Two more weeks at a slightly seasonally damped ~55 per week gives about 480, with a right skew in case the epidemic is still accelerating. The forecast depends most on the Week 41 increment due around Oct 22.
