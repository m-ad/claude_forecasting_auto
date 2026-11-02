# What will Hon Hai (Foxconn) report as net profit attributable to owners of the parent for Q3 2026 (in NT$ billions)?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46372/ |
| **Tournament** | minibench — one shot, window 2026-11-02T02:12:04Z -> 2026-11-02T05:12:04Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-12 |
| **Status** | closed |
| **Current forecast** | Median 80, IQR [75.5, 84.5] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the "Profit (Loss) Attributable to Owner of the Parent" figure for 1 Jul – 30 Sep 2026, as printed in Hon Hai's Q3 2026 results slide deck (due 12 Nov 2026), in NT$ millions divided by 1,000. Consolidated profit including non-controlling interests (NCI, the minority shareholders' share) does not count. The first published figure is final. Both bounds are open, so an outcome below 60 or above 95 is scored at the edge bins. Arithmetic: Q3 revenue is already known at NT$3,026.9bn, up 19.8% on Q2's 2,525.9bn. In Q2, 3.75% operating margin gave 94.7bn of operating profit; non-operating income was about 0, tax 26.2%, and NCI took 10.1bn, leaving 59.97bn. The same conversion on Q3 revenue gives about 113.5 × 0.738 × 0.856 ≈ 71.7bn. Each extra NT$10bn of non-operating income adds about 6.5bn attributable.

### Outside view

There is no clean frequency-based reference class, so the anchor is the company's own margin structure (net margin to the parent: Q3'25 2.80%, Q2'26 2.37%). Applied to NT$3,027bn that gives 71.7–84.8bn, with a midpoint of about 78. History against consensus: Q3'25 actual 57.67bn vs LSEG 50.4bn (+14%); Q2'26 59.97 vs 58.8 (+2%); Q4'25 a large miss on non-operating items. One quarter in three deviated by 15% or more from consensus.

### Inside view

- **Bottom-up via the main subsidiary.** Foxconn Industrial Internet (FII, about 84% owned) earned RMB 16.63bn attributable in Q3, +26.5% QoQ from about RMB 13.15bn [3]. At about NT$4.4–4.55 per RMB that is roughly NT$73–76bn. FII alone earned about NT$58bn in Q2, when Hon Hai's consolidated profit was 70bn, so the rest of the group netted about 12bn after the FX loss. In Q3'25 the rest of the group netted about 22bn. With Q3 FX flat and iPhone seasonality, the rest of the group plausibly adds 15–25bn. That puts consolidated profit at about 90–100bn and, after NCI of about 14–15bn, attributable profit at about 76–85bn.
- **Monte Carlo** (`model.py`). Inputs: operating margin 3.75% ± 0.12 pp, non-operating income +8 ± 8bn (FX flat over Q3: 31.837 → 31.852 [5][6]), tax 23.5% ± 2 pp, NCI share 14.5% ± 1.5 pp. Output: p5 69.3, p25 75.2, p50 79.4, p75 83.7, p95 89.9.
- I widened the tails slightly for one-off non-operating items (equity-method results at Sharp and Innolux, investment gains or losses), which drove the Q4'25 miss.
- The two methods agree: median 80, IQR 75.5–84.5. The analyst range quoted in the question (72–86bn) sits inside my 10–90 band.

### Evidence

- Q3 2026 revenue was NT$3,026.9bn, +47% YoY, against an LSEG SmartEstimate of 2.83tn (reported 5 Oct 2026) [1][7].
- Q2 2026 net profit was 59.97bn vs an LSEG consensus of 58.8bn; operating margin 3.75%, gross margin 6.12% [2].
- Q3 2025 net profit was 57.67bn vs LSEG 50.4bn [4].
- FII Q3 2026: net attributable RMB 16.634bn (+60.35% YoY), revenue RMB 383.55bn (+57.7%), 9M gross margin 7.09%. Released 29 Oct 2026 [3].
- USD/TWD closed at 31.837 on 30 Jun 2026 and 31.852 on 30 Sep 2026, so the spot FX move over the quarter was negligible [5][6].
- On 5 Sep 2026 Foxconn said Q3 would outperform market expectations on AI demand [7]. Its 2026 operating margin target is "3.2%+".

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-02 | |
| Local analyst models (per question text) | EPS NT$5.10–6.11 → 72–86bn | Oct 2026 | not independently found |
| Polymarket / Kalshi / Manifold | none found | 2026-11-02 | |
| LSEG Q3 profit consensus | not found | 2026-11-02 | |

### What would change my mind

- **Non-operating income.** A large investment, impairment or hedging loss (as in Q4'25) could push the result below 70. A big equity-method or disposal gain could push it above 88.
- **Operating margin.** Dilution from the AI rack mix taking operating margin to 3.5% costs about 5bn; a margin of 3.9% adds about 3.5bn.

### Sources

1. Foxconn Q3 revenue report (Reuters via FourWeekMBA), https://fourweekmba.com/ai-foxconn-q3-revenue-t3-03-trillion-47-percent-ai-demand-recor/ (accessed 2026-11-02)
2. The Star, "Taiwan's Foxconn reports 35% rise in Q2 profit, beats forecasts", https://www.thestar.com.my/tech/tech-news/2026/08/12/taiwan039s-foxconn-reports-35-rise-in-q2-profit-beats-forecasts (accessed 2026-11-02)
3. 10jqka, FII nine-month net profit above RMB 40bn, https://stock.10jqka.com.cn/20261030/c681314558.shtml (accessed 2026-11-02); H1: https://stock.10jqka.com.cn/20260811/c678868469.shtml
4. Business Recorder, Foxconn Q3 2025 profit beats, https://www.brecorder.com/news/40392055 (accessed 2026-11-02)
5. Focus Taiwan, USD/TWD close 30 Sep 2026, https://focustaiwan.tw/business/202609300010 (accessed 2026-11-02)
6. Focus Taiwan, USD/TWD close 30 Jun 2026, https://focustaiwan.tw/business/202606300012 (accessed 2026-11-02; via search summary)
7. The Star, "Foxconn says third quarter to outperform market expectations", https://www.thestar.com.my/tech/tech-news/2026/09/05/foxconn-says-third-quarter-to-outperform-market-expectations-on-ai-strength (accessed 2026-11-02; snippet)

**Question**: [What will Hon Hai (Foxconn) report as net profit attributable to owners of the parent for Q3 2026 (in NT$ billions)?](https://www.metaculus.com/questions/46372/)
**Date**: 2026-11-02
**Forecast**: Median 80.0 NT$B, IQR [75.5 NT$B, 84.5 NT$B]
**Thesis**: Known Q3 revenue of NT$3,027bn at Hon Hai's 2.4–2.8% net margin gives 72–85bn. Subsidiary FII's record RMB 16.6bn Q3 profit (+26% QoQ) and a flat NT dollar over the quarter (so no repeat of Q2's FX loss) centre it near 80bn. The forecast is most sensitive to one-off non-operating items and the minority-interest share.
