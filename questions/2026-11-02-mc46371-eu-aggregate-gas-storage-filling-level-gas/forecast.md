# What will the EU aggregate gas storage filling level be for gas day 12 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46371/ |
| **Tournament** | minibench — one shot, window 2026-11-02T01:57:40Z -> 2026-11-02T04:57:40Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | Median 72.6, IQR [71.9, 73.3] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the "full" field (percent of working gas volume) in GIE AGSI+'s **"EU"** dataset (not "Europe") for gas day **2026-11-12**, as first published (expected 13 Nov). Later revisions don't count. Last known value: **74.64% on gas day 30 Oct** (845.5 TWh of 1,132.8 TWh, −0.13 pp d/d, net withdrawal ~1.49 TWh/d) [1]. A secondary tracker shows **74.6%** updated 1 Nov [2]. So the horizon is 13 gas days (31 Oct–12 Nov). Each 1 pp equals 11.3 TWh, so 1.5 TWh/d ≈ −0.13 pp/d and 2.4 TWh/d (the five-year November average withdrawal [4]) ≈ −0.21 pp/d. Over 13 days: −0.13/d → 72.9, −0.16/d → 72.6, −0.21/d → 71.9, −0.30/d → 70.7, and 0/d → 74.6. Both bounds (68, 77) are open, and 68 needs a pace of −0.51 pp/d, which would be extreme for early November.

### Outside view

The reference class is the net change in EU storage from ~1 Nov to ~12 Nov in recent years [6][7]:

| Year | Change over ~11 days | Driver |
|---|---|---|
| 2022 | ~0 to +0.4 pp | mild, near-full |
| 2023 | ~0 pp | mild, near-full |
| 2024 | ~−1.6 pp in 9 days (−0.18/d) | Dunkelflaute (cold, windless spell) |
| 2025 | November withdrawals averaged 2.8 TWh/d (~−0.25/d) for the whole month [4] | colder, tighter |

Early November averages from ~0 to −0.25 pp/d. Years near 100% full understate withdrawal, because full storage pushes LNG elsewhere. A tight year like 2026 resembles 2021, 2024 and 2025 more. Base pace is ~−0.15 pp/d, which gives ~72.7.

### Inside view

- Net withdrawals are **already under way**: the level fell from 74.93 (26 Oct) to 74.64 (30 Oct) [1][3]. Because the heating season is ramping up, the pace should rise above late-October's −0.13 pp/d.
- **Tight supply** pushes toward faster drawdown: the Hormuz LNG disruption, TTF at ~€95, and Austria, Slovakia and Czechia already withdrawing [1]. **High prices** push the other way, through demand destruction and LNG cargoes pulled toward Europe.
- **Weather**: Météo-France sees 2–8 Nov slightly below normal, "not a true winter blast". Cold air is possible in Germany ~7 Nov. The forecast SSW (sudden stratospheric warming) ~6 Nov typically reaches the surface 1–3 weeks later, so the main cold risk is after 12 Nov [5]. Seasonal outlooks lean warm for November.
- The secondary tracker shows +0.10 pp on its latest day [2], a hint that mild or windy days can still pause withdrawals.

Model: average pace ~N(−0.16, 0.07) pp/d over 13 days, with a slightly fatter cold tail. Median 72.6, IQR 71.9–73.3, p5 70.6, p95 74.4.

### Evidence

- AGSI+ via the question text: 74.64% on 30 Oct 2026, 74.93% on 26 Oct, peak ~75% [1].
- EnergyRiskIQ: EU 74.6%, updated 2026-11-01, +0.10 pp d/d, withdrawals averaging 1,535 GWh/d (accessed 2026-11-02) [2].
- Global Energy Flow: 74.93% on gas day 26 Oct, +0.02 pp that day [3].
- Argus: November 2025 withdrawals were 2.8 TWh/d against a five-year average of 2.4 TWh/d [4].
- Polar-vortex and weather outlook from Sortiraparis/Météo-France, updated 29 Oct 2026 [5].
- 2024 analogue: 93.37% on 10 Nov 2024 (TASS citing GIE) [6]. 2022 analogue: ~95.4% on 11 Nov [7].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-02 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-02 | |
| Third-party tracker (question text) | ~71% by 23 Nov | late Oct 2026 | implies ~72.5 on 12 Nov |

### What would change my mind

The 12-day average withdrawal pace is the only real driver. A persistent cold, low-wind high-pressure block over central Europe in the 5–12 Nov window (2024-style Dunkelflaute) would push the outcome toward 70–71. A mild, windy Atlantic pattern with strong LNG sendout would hold it near 74. I could not see AGSI+ values for 31 Oct and 1 Nov directly.

### Sources

1. Metaculus question text citing the AGSI+ API and bne IntelliNews, 28 Oct 2026, cached in raw/metaculus-question-2026-11-02.json (accessed 2026-11-02)
2. https://energyriskiq.com/gas-storage-levels-in-europe (accessed 2026-11-02)
3. https://global-energy-flow.com/storage/trajectory/ (accessed 2026-11-02)
4. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2760842-eu-gas-stocks-at-four-year-low-on-1-december (accessed 2026-11-02)
5. https://www.sortiraparis.com/en/news/in-paris/articles/356403-polar-vortex-an-exceptional-phenomenon-expected-in-early-november-what-impact-will-it-have-on-france (accessed 2026-11-02)
6. https://tass.com/economy/1870973 (accessed 2026-11-02)
7. https://tass.com/economy/1535123 (accessed 2026-11-02)

**Question**: [What will the EU aggregate gas storage filling level be for gas day 12 November 2026?](https://www.metaculus.com/questions/46371/)
**Date**: 2026-11-02
**Forecast**: Median 72.6%, IQR [71.9%, 73.3%]
**Thesis**: EU storage was 74.64% on 30 Oct and net withdrawals of ~0.13 pp/day were already under way (AGSI+). Past early-November drawdowns ran from 0 to −0.25 pp/day, and tight LNG supply points to the faster end, so I project ~−0.16 pp/day over 13 days. The result is most sensitive to whether a cold, windless spell arrives before 12 Nov; the forecast SSW mostly lands later.
