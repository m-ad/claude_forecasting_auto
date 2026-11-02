# What will Japan's October 2026 domestic corporate goods price index (CGPI) year-on-year change be?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46387/ |
| **Tournament** | minibench — one shot, window 2026-11-02T06:53:30Z -> 2026-11-02T09:53:30Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-12 |
| **Status** | open |
| **Current forecast** | Median 6.5, IQR [6.2, 6.8] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the headline year-on-year (前年同月比) change of the domestic CGPI (all commodities, 2020 = 100, fixed base) for October 2026. The figure comes from the BOJ's preliminary October 2026 release (cgpi2610.pdf), due 8:50 JST on 2026-11-12, and is reported to one decimal place. Later revisions do not count. The chained and summer-electricity-adjusted variants do not count. The range is 4.5–8.5 and both bounds are open.

The arithmetic: the latest release is September 2026 (published 2026-10-13), at 135.7, −0.3 % m/m and +6.8 % y/y. That release's own table shows October 2025, the base month, at **+0.5 % m/m** (current vintage; the first print was +0.4 %). The target is one month ahead. y/y(Oct) ≈ 1.068 × (1 + m) / 1.005 − 1, where m is the October 2026 month-on-month change. A flat October gives **≈ 6.3 %**, and each 0.1 pp of m/m adds about 0.1 pp. Getting above 7.2 % needs m ≈ +0.9 %. Getting below 5.4 % needs m ≈ −0.9 %.

### Outside view

The reference class is one-month changes in this series. In 2026 the m/m changes were 0.3, 0.0, 1.1, 2.8, 1.1, 0.6, 0.4, −0.3, −0.3; outside the April oil shock, most were within ±0.6 pp. On the base effect alone (m = 0), y/y would be ≈ 6.3 %, with an m/m spread of about ±0.4 pp at one standard deviation. Preliminary-to-revised changes to the September level add a further ~0.1 pp.

### Inside view

The October 2026 m/m drivers, as I see them:
- **Electricity and city gas (+).** The July–September 2026 usage subsidy ended with September usage and was not extended for October; it returns in December. It was larger than the 2025 one: 1.8 yen/kWh high-voltage in 2026, against a summer-2025 scheme of about 2.0–2.4 yen/kWh low-voltage. The utility step-up in October 2026 should therefore exceed October 2025's, which is already in the base. Tokyo CPI for October 2026 supports this: electricity y/y swung from −2.6 % to +1.7 % and city gas from −0.5 % to +4.9 %. That swing means the October 2026 m/m outran the October 2025 m/m. Effect: +0.2 pp.
- **Oil (+, small).** Brent averaged ~$125 over 1–27 October against ~$114 in September (FRED, scout calculation), and the yen was flat at ~158. The gasoline subsidy (~43 yen/L) damps the pass-through to domestic petroleum products, which fell 2.2 % m/m in September despite higher crude. Effect: +0.1 pp.
- **Rice and farm products (−).** The new-crop price slump (−8.8 % m/m in September) probably continues. Effect: −0.1 pp.
- Copper is flat and non-ferrous metals are flat. The end of the summer electricity tier happens in both years, so it nets out.

The October 2026 m/m comes out at ≈ +0.2–0.3 %, giving a **median of 6.5 %**. The tails are wide for oil volatility (a $20 daily swing on 2 October), revision of the September level, and uncertain subsidy accounting.

### Evidence

- Sep 2026 preliminary: 135.7, −0.3 % m/m, +6.8 % y/y. The table shows Oct 2025 at +0.5 % m/m and Sep 2025 at +0.5 %. Sep contributions were agriculture −0.42 pp and petroleum −0.15 pp. [1]
- The consensus for September had been 7.6 %, so the print missed by 0.8 pp. A Reuters-quoted economist expects re-acceleration but "no sign of … accelerating sharply" (2026-10-13). [2]
- METI approved the July–September 2026 subsidies (low-voltage 3.5/4.5/3.5 yen/kWh, high-voltage 1.8/2.3/1.8), with nothing for October. Reports say the subsidy returns for December–February (29 October). [3][4]
- Tokyo CPI for October 2026 (30 October): energy +2.2 % y/y (September −1.9 %), electricity +1.7 % (−2.6 %), city gas +4.9 % (−0.5 %). [5]
- Brent averaged ~$114 in September and ~$125 over 1–27 October. USD/JPY averaged ~157.9 in October, about flat. LME copper was about flat at ~$14.4k. [6][7]
- Oct 2025 first print: +0.4 % m/m, +2.7 % y/y. [8]

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-02 | |
| Economist consensus | not found | 2026-11-02 | none published yet |
| Kalshi / Polymarket | no CGPI market | 2026-11-02 | |
| Trading Economics model | 7.8 % by end of quarter | 2026-11-02 | mechanical; discounted |

### What would change my mind

- Evidence that the BOJ books the subsidy end differently from what I assumed (for example, spread over two months, or that the 2025 base already carried a larger utility jump). That would move the median down by ~0.2.
- A large October fall in domestic petroleum product or farm prices, below −3 % and −5 % respectively, would point to ~6.0 %.

### Sources

1. BOJ, 企業物価指数（2026年9月速報）, https://www.boj.or.jp/statistics/pi/cgpi_release/cgpi2609.pdf (accessed 2026-11-02)
2. Reuters via The Star, "Japan's wholesale inflation remains elevated…", https://www.thestar.com.my/business/business-news/2026/10/13/japan039s-wholesale-inflation-remains-elevated-keeps-alive-boj-rate-hike-view (accessed 2026-11-02)
3. METI Kanto, 2026-06-12 subsidy approval, https://www.kanto.meti.go.jp/press/data/20260612gas_jigyo_press.pdf (accessed 2026-11-02; search summary)
4. vegcale, end of subsidy October 2026, https://vegcale.com/2026/08/12/electricity-gas-subsidy-end-october-2026/ (accessed 2026-11-02)
5. ActionForex, Tokyo CPI October 2026, https://www.actionforex.com/?p=659199 (accessed 2026-11-02)
6. FRED Brent daily, https://fred.stlouisfed.org/data/DCOILBRENTEU.txt (accessed 2026-11-02)
7. Pound Sterling Live USD/JPY 2026 history, https://www.poundsterlinglive.com/history/USD-JPY-2026 (accessed 2026-11-02)
8. investingLive, Japan October 2025 PPI, https://investinglive.com/news/japan-october-ppi-04-mm-expected-03-27-yy-expected-25-20251112/amp (accessed 2026-11-02)

**Question**: [What will Japan's October 2026 domestic corporate goods price index (CGPI) year-on-year change be?](https://www.metaculus.com/questions/46387/)
**Date**: 2026-11-02
**Forecast**: Median 6.5%, IQR [6.2%, 6.8%]
**Thesis**: The +0.5 % m/m in the October 2025 base month pulls a flat October 2026 down to ~6.3 % y/y. The end of the larger 2026 electricity/gas subsidy and higher October crude should lift October m/m to about +0.2–0.3 %, partly offset by falling rice prices. The forecast is most sensitive to how the BOJ records the subsidy end in October.
