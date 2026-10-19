# How many new locally acquired dengue cases will the Week 42 FDOH arbovirus report (October 18–24, 2026) show for Florida?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46140/ |
| **Tournament** | minibench — one shot, window 2026-10-19T12:10:44Z -> 2026-10-19T15:10:44Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 59, IQR [44, 76] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The value is the count of locally acquired dengue cases "reported this week" in the "Dengue Cases Acquired in Florida" section of the FDOH (Florida Department of Health) Weekly Arbovirus Surveillance Report for Week 42 (October 18–24, 2026), expected around October 29, 2026. If no single weekly figure is stated, the value is the increase in the 2026 cumulative total from the previous published report. The range runs from 0 to 120 and is closed at 0 and open above 120. This is a count of *reports* in that week, not of illness onsets. It therefore reflects infections from about 1–3 weeks earlier, plus any batching of lab results.

### Outside view

There is no clean reference class: before 2026, Florida's worst year was 2023, with just under 200 local cases for the entire year [3]. That makes 2026 the largest continental-US outbreak in decades. The best prior is this outbreak's own recent run of weekly report counts, taken from the question text and FDOH cumulative totals [1][2][4]:

| Report week | New local cases | Cumulative |
|---|---|---|
| W34 (ending ~Sep 3) | 32 | — |
| W35 | 38 | — |
| W36 | 41 | — |
| W38 (Sep 20–26) | 62 | 252 |
| W39 (Sep 27–Oct 3) | 44 | 296 |
| W40 (Oct 4–10) | 72 | 368 |

Over the last three reports the average is about 59 per week. The trend is still flat to rising, and week-to-week swings are about ±15 (44 vs 72 in consecutive weeks).

### Inside view

- **Pushing it up:** As of W40 the outbreak was still growing, and it had spread to eight counties [2]. Late-October Tampa is still warm enough for *Aedes aegypti* to transmit. Because of the reporting lag, W42 reports partly reflect infections from early October, when transmission was at its peak. Awareness and testing in the Tampa Bay area are high, so detection is good.
- **Pushing it down:** Day-and-night aerial and ground spraying, with local emergencies declared since September [3][5], should start to show 2–4 weeks after it began. Florida's seasonal decline usually starts in late October or November. The W39 dip (44) shows a single week can come in low.
- **Net:** I hold the median near the recent level (~59) and do not extrapolate the W40 spike. Plateau-or-decline and continued growth get roughly equal weight. The tails are wide. A lab backlog clearing in a single week could push the count past 100. A sharp turn after spraying or a reporting lull could drop it into the 20s.

No model was run; the percentiles are a judgemental right-skewed distribution around the recent mean.

### Evidence

- FDOH Week 40 report (Oct 4–10, published Oct 15): "Seventy-two cases of locally acquired dengue were reported this week. In 2026, 368 cases … from eight counties" [2]. I could not parse the PDF text directly. The figure comes from the search-indexed text, and it matches the question text exactly [1].
- Week 39 cumulative: 296, of which 259 in Hillsborough and 20 in Pinellas [4]. Week 38 cumulative: 252 [6]. In the Sep 20–26 report, Hillsborough added 53 cases [5].
- AP, Oct 5: largest outbreak in the continental US in decades; spraying day and night in the Tampa area; local emergencies declared [3].
- WGCU Oct 9 and Infection Control Today Oct 12: cases still rising [7][8]. No news after the W40 report was found to show a turn in the trend (searched 2026-10-19).

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no matching market |

### What would change my mind

The Week 41 report (Oct 11–17, due ~Oct 22) is the single fact this forecast is most sensitive to. Another value of 70 or more would move the median to ~70. A value under 40 would suggest spraying and the season have turned the curve, and would move the median toward ~40. A report restructure or catch-up batch would also shift the result.

### Sources

1. Metaculus question 46140 text, cached in raw/metaculus-question-2026-10-19.json (accessed 2026-10-19)
2. FDOH Weekly Arbovirus Report Week 40 2026, https://www.floridahealth.gov/wp-content/uploads/2026/10/fl-arbovirus-report-w40-2026.pdf (accessed 2026-10-19)
3. Jamaica Gleaner / AP, "Florida seeing largest dengue outbreak in continental US in decades", https://jamaica-gleaner.com/article/news/20261005/florida-seeing-largest-dengue-outbreak-continental-us-decades (accessed 2026-10-19)
4. FDOH Weekly Arbovirus Report Week 39 2026, https://www.floridahealth.gov/wp-content/uploads/2026/10/fl-arbovirus-report-w39-2026.pdf (accessed 2026-10-19)
5. WUSF, "Hillsborough adds 53 dengue cases, gets help from Lee", https://wusf.org/text/health-news-florida/2026-10-02/hillsborough-lee-counties-team-up-control-dengue-fever (accessed 2026-10-19)
6. Mixvale, "Florida confirms 252 local dengue cases in record mainland outbreak", https://www.mixvale.com.br/2026/10/05/florida-confirms-252-local-dengue-cases-in-record-mainland-outbreak/ (accessed 2026-10-19)
7. WGCU, "Dengue fever cases on the rise in Florida", https://www.wgcu.org/health/2026-10-09/dengue-fever-cases-on-the-rise-in-florida (accessed 2026-10-19)
8. Infection Control Today, Florida dengue outbreak 2026, https://www.infectioncontroltoday.com/view/florida-dengue-outbreak-2026-symptoms-testing-treatment-prevention (accessed 2026-10-19)

**Question**: [How many new locally acquired dengue cases will the Week 42 FDOH arbovirus report (October 18–24, 2026) show for Florida?](https://www.metaculus.com/questions/46140/)
**Date**: 2026-10-19
**Forecast**: Median 59 cases, IQR [44 cases, 76 cases]
**Thesis**: The last three FDOH weekly reports showed 62, 44 and 72 new local cases, so the outbreak is still at its peak. Intensive spraying and the end of the mosquito season argue for a plateau or slow decline rather than further growth. The forecast is most sensitive to the Week 41 report (due ~Oct 22) and to batching of lab results.
