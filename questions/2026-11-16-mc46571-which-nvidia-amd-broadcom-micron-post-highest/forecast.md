# Which of Nvidia, AMD, Broadcom, or Micron will post the highest percentage change in closing share price from the November 13, 2026 close to the November 27, 2026 close?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46571/ |
| **Tournament** | minibench — one shot, window 2026-11-16T04:31:30Z -> 2026-11-16T07:31:30Z |
| **Type** | multiple_choice |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | open |
| **Current forecast** | Median 28.0%, IQR [22.0%, 34.0%] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The option whose stock has the largest (close Nov 27 − close Nov 13) / close Nov 13, from the Yahoo Finance historical "Close" columns. Nov 27 is a half session (1 p.m. ET close); Nov 26 is a holiday. That leaves 8.5 sessions after the Nov 13 base close: Nov 16–20, 23–25, and the Nov 27 half day. It is a relative race: if all four fall, the smallest decline wins. Ties go to the option listed earlier. No forecast is made before the base date. This forecast is made on Mon Nov 16 before the open, so nothing has moved yet. Nov 13 levels from the question text (intraday): NVDA ~$159, AMD ~$531, AVGO ~$341, MU ~$760.

### Outside view

With no edge on drift, the stock most likely to post the highest return over a short window is the most volatile one. Four exchangeable stocks would give 25% each. These four are highly correlated, so the spread in their volatility decides who wins. Realised volatility in Oct–Nov 2026 was highest for AMD (−17% on Nov 5) and MU (30-day implied volatility 60% on Nov 4, range 45–108%). AVGO and NVDA ex-earnings are lower. A vol-only Monte Carlo (correlation 0.65; annualised vol AMD 80%, MU 70%, NVDA and AVGO 60%) gives AMD ~0.29, MU ~0.26, NVDA ~0.22, AVGO ~0.23.

### Inside view

- **NVDA earnings on Nov 17 (after the close)** sit inside the window. Options imply about ±10% (reported), against a historical average of ±6–8% with direction a coin flip. The jump is idiosyncratic to NVDA; I assume peers move about half as much. That lifts NVDA to ~0.25 in `model.py` (AMD 0.28, AVGO 0.22, MU 0.25).
- **Leadership shock and valuation.** NVDA is down ~30% since Oct 12. Mizuho calls it "silly cheap" below 10x earnings and Goldman calls the group "clearly oversold". Against that, Baird downgraded it and Morgan Stanley and BofA dropped it from their top-pick lists. A first report under interim CEO Kress could be a relief rally or a further de-rating. I give a small +1 pp to NVDA, taken from AVGO.
- AVGO (~Dec 10) and MU (~Dec 16) report outside the window. AMD fell the most on Nov 13 (~−9%), which gives some short-term reversal potential. I treat that as noise.

Final: NVDA 26%, AMD 28%, AVGO 21%, MU 25%. This is close to uniform on purpose: two-week relative returns among correlated semis are nearly unforecastable.

### Evidence

- SEC 8-K: Huang resigned Nov 11, 2026; Kress is interim CEO and stays CFO; Harvey Jones is chair [1].
- Nvidia guided Q3 to $108B ±2%; consensus is ~$108.8B revenue and $2.47 EPS; the implied move is ~10.6% (secondary summary) [3].
- NVDA's average earnings-day move is ±6.4–7.6% (8 up, 8 down over 16 reports) [4].
- Analyst views after the shock: "silly cheap" (Mizuho), "clearly oversold" (Goldman); 59 of 64 brokers rate it Buy, median target $314 [5].
- MU 30-day implied volatility was 60.5% on 2026-11-04 [6]. AMD fell 17.3% on 2026-11-05 [7]. AVGO rose 8.8% on Nov 9, and its next earnings are ~Dec 9–10 [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi | no relative-performance market found | 2026-11-16 | only thin NVDA price-level markets [2] |

### What would change my mind

The Nov 17 NVDA print decides most of this. A beat with strong Q4 guidance and a clear succession plan could add 10%+ and make NVDA the favourite. A miss would hand the race to the high-beta names that fall less. A memory-pricing headline (DRAM contract prices) would move MU on its own.

### Sources

1. NVIDIA Form 8-K, CEO transition — https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm (accessed 2026-11-16)
2. 24/7 Wall St., Polymarket NVDA November markets — https://247wallst.com/investing/2026/11/02/polymarket-traders-missed-nvidias-october-drop-heres-what-they-predict-for-november/ (accessed 2026-11-16)
3. MarketPulse, Nvidia Q3 earnings preview — https://www.marketpulse.com/markets/nvidia-nvda-q3-earnings-preview-ai-spending-risks-and-governance-concerns-threaten-major-uptrend/ (accessed 2026-11-16)
4. Regards of Wallstreet, NVDA earnings history — https://www.regardsofwallstreet.com/tools/earnings-history/nvda (accessed 2026-11-16)
5. investingLive, Mizuho's Klein on Nvidia — https://investinglive.com/stocks/mizuho-s-klein-calls-nvidia-silly-cheap-below-10x-earnings-despite-huang-uncertainty/ (accessed 2026-11-16)
6. OptionCharts, MU options overview — https://optioncharts.io/options/MU (accessed 2026-11-16)
7. Motley Fool, Why AMD stock is down today — https://www.fool.com/investing/2026/11/05/why-amd-stock-is-down-today/ (accessed 2026-11-16)
8. 24/7 Wall St., Broadcom best day in nearly a year — https://247wallst.com/investing/2026/11/10/broadcom-just-had-its-best-day-in-nearly-a-year-back-above-1-5-trillion/ (accessed 2026-11-16)
9. FourWeekMBA, Micron up 142% this year — https://fourweekmba.com/ai-micron-is-up-142-this-year-four-hyperscalers-average-1-4/ (accessed 2026-11-16)

**Question**: [Which of Nvidia, AMD, Broadcom, or Micron will post the highest percentage change in closing share price from the November 13, 2026 close to the November 27, 2026 close?](https://www.metaculus.com/questions/46571/)
**Date**: 2026-11-16
**Forecast**: Median 28.0% (AMD), IQR [22.0%, 34.0%]
**Thesis**: Two-week relative returns among four highly correlated chip stocks are close to a coin toss, so the probabilities follow volatility. AMD and Micron are the most volatile, and Nvidia's Nov 17 earnings (about ±10% implied) lift it from below 25% to about 26%. The forecast is most sensitive to the Nvidia print.
