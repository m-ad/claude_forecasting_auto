# What annualized real GDP growth will the BEA report in its advance estimate for Q3 2026, released October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46124/ |
| **Tournament** | minibench — one shot, window 2026-10-19T00:21:42Z -> 2026-10-19T03:21:42Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-29 |
| **Status** | closed |
| **Current forecast** | Median 3.3, IQR [2.7, 3.85] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

This resolves to the headline real GDP percent change for Q3 2026 (July–September), at a seasonally adjusted annual rate (SAAR), as printed in BEA's "GDP (Advance Estimate), 3rd Quarter 2026" release. That release is scheduled for 2026-10-29 at 8:30 ET. Only the advance print counts; later revisions do not. If the release slips, the first advance estimate published counts. BEA prints to one decimal, so the outcome lands on a 0.1 grid. The question range is 0.5–5.0 with both bounds open, so a print below 0.5 or above 5.0 is possible and lands outside the range.

### Outside view

The reference class is the advance GDP print compared with the Atlanta Fed GDPNow nowcast about ten days before release. GDPNow's historical error against the advance estimate has a root-mean-square of roughly 1.2 percentage points (pp) on its final nowcast (from memory of Atlanta Fed documentation; not re-fetched this session, so treat as approximate). Ten days out, with the advance trade, inventory and September spending data still to come, the error is somewhat larger. The question text says GDPNow tends to run higher than the advance print. The last quarter fits that: Q2 2026's advance print was 1.5%, against a 2.1% consensus and a NY Fed final nowcast of 2.9% [6][5]. So the prior is GDPNow minus a small amount, with an error of about ±1.3pp at one standard deviation.

### Inside view

- GDPNow is 3.6% as of 2026-10-15. It has been 3.6–3.7% all October, down from a 6.2% peak in early August [2][7]. The next update is 2026-10-20.
- The composition is fragile. Inventories add +1.87pp, and net exports subtract about 2.7pp (as of Oct 6) [2]. Two large components that offset each other, both with noisy advance source data, widen the error band. Real consumer spending is tracking 3.6%, which supports a print near 3%.
- Older, slower-moving forecasts are lower: SPF (Survey of Professional Forecasters) median 2.5% (mid-August) [1], NY Fed Staff Nowcast 2.3% (early September) [5]. They pull the centre slightly below GDPNow.
- The prediction markets are the best aggregate. Polymarket gives P(≥3.0%) = 65%, about $45k volume on that bracket [3]. A Kalshi snapshot (date uncertain) shows above 3.0% at 70%, above 3.5% at 32% and above 4.0% at 19% [4]. Together they imply a median near 3.3% and an interquartile range of about 2.9–3.7%.
- Integration: median 3.3%, between the markets (~3.3) and GDPNow (3.6) less its usual overshoot. The tails are wider than the markets imply, because of the inventory and net-export risk and last quarter's 1.4pp miss against the nowcast.

| Percentile | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| Q3 2026 real GDP, % SAAR | 1.5 | 2.0 | 2.7 | 3.3 | 3.85 | 4.5 | 5.0 |

### Evidence

- 2026-10-15: GDPNow Q3 2026 at 3.6%, unchanged from Oct 8. PCE (consumer spending) growth 3.6%; inventory contribution 1.87pp [2] (accessed 2026-10-19).
- 2026-10-06: GDPNow 3.7%; net-exports drag −2.69pp [2][7].
- August 2026: GDPNow peaked at 6.2%, then fell to 4.3% and then 4.03% [7].
- Early September 2026: NY Fed Staff Nowcast for Q3 at 2.3%, 50% interval [1.1, 3.4], 80% interval [0.0, 4.5] [5].
- 2026-07-30: Q2 advance print 1.5%, against a ~2.1% consensus. The NY Fed's final Q2 nowcast was 2.9% [6][5].
- From the question text: Q1 2026 at 2.5% (revised), Q2 2026 at 2.2% (third estimate), SPF Q3 median 2.5% [1].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Polymarket "US GDP growth in Q3 2026?" | ≥3.0%: 65%; 2.5–3.0%: 16%; 2.0–2.5%: 9%; 1.5–2.0%: 2%; <1.5%: ~3% | 2026-10-19 | ~$60k total volume |
| Kalshi KXGDP-26OCT30 | >3.0%: 70%; >3.5%: 32%; >4.0%: 19% | snapshot, date uncertain | from a search snippet; the live page returned HTTP 429 |
| Atlanta Fed GDPNow | 3.6% | 2026-10-15 | model, not a forecast |
| NY Fed Staff Nowcast | 2.3% | early Sep 2026 | stale |
| SPF median | 2.5% | Q3 2026 survey (Aug) | stale |

### What would change my mind

- The advance trade and inventory data due before the release (around Oct 27–28). A narrower goods deficit, or a large inventory build, would push the print toward 4%+. A reversal of the inventory build would pull it toward 2%.
- A sharp move in GDPNow on Oct 20 or later, especially from the September retail sales and personal spending data.

### Sources

1. Metaculus question 46124, cached text (raw/metaculus-question-2026-10-19.json), https://www.metaculus.com/questions/46124/ (accessed 2026-10-19)
2. Atlanta Fed, GDPNow current and past commentaries, https://www.atlantafed.org/research-and-data/data/gdpnow/current-and-past-gdpnow-commentaries (accessed 2026-10-19)
3. Polymarket, GDP quarterly series, https://polymarket.com/series/gdp-quarterly (accessed 2026-10-19)
4. Kalshi, US real GDP growth in Q3 2026, https://kalshi.com/markets/kxgdp/us-real-gdp-growth-in-q3-2026/kxgdp-26oct30 (search snippet, accessed 2026-10-19)
5. MTS Insights, "New York Fed Staff Nowcast: Week of September 4th", https://www.mtsinsights.com/summaries/10798/ (accessed 2026-10-19)
6. BEA, GDP Advance Estimate, 2nd Quarter 2026, https://bea.gov/news/2026/gdp-advance-estimate-2nd-quarter-2026 (via search, accessed 2026-10-19)
7. investinglive / cryptobriefing, GDPNow Q3 2026 updates, https://investinglive.com/news/atlanta-fed-gdpnow-downgrades-q3-growth-estimate-to-4-03-vs-4-31-prior/ and https://cryptobriefing.com/atlanta-fed-gdpnow-q3-2026-growth/ (accessed 2026-10-19)

**Question**: [What annualized real GDP growth will the BEA report in its advance estimate for Q3 2026, released October 29, 2026?](https://www.metaculus.com/questions/46124/)
**Date**: 2026-10-19
**Forecast**: Median 3.3%, IQR [2.7%, 3.85%]
**Thesis**: GDPNow sits at 3.6% (Oct 15), and Polymarket and Kalshi put about 65–70% on a print of 3.0% or more, which centres the advance estimate near 3.3% once GDPNow's usual overshoot is allowed for. The tails are wide because the nowcast rests on a large inventory build (+1.9pp) offset by a large net-export drag (−2.7pp), and the Q2 advance print missed its nowcasts by more than 1pp.
