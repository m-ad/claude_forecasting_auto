# What will the Brent crude oil front-month futures settlement price be on October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46145/ |
| **Tournament** | minibench — one shot, window 2026-10-19T14:29:32Z -> 2026-10-19T17:29:32Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 106.5, IQR [100, 112] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the official ICE Brent settlement price, in USD per barrel, of the December 2026 contract (CBZ26) on Thursday 29 October 2026. The value is read from the "Last" column of the 10/29/2026 row on Barchart's CBZ26 historical-price page. CBZ26 is still the front month that day: ICE Brent December expires on the last business day of October, which is 30 October. If Barchart shows no settlement, credible reports of the front-month settlement are used. If 29 October is not a trading day, the previous trading day's settlement is used. The range is $80–130 and both bounds are open, so a settlement outside that range still resolves to its actual value. That leaves 8 trading sessions after today (19 October).

### Outside view

For an 8-trading-day horizon, the best prior is a random walk from the latest price, with volatility set by the current regime. Brent settled at $109.86 on Friday 16 October, its highest settlement since 19 May [2]. It was trading around $108 on Monday 19 October [3]. Brent has been in a war and Hormuz-disruption regime all year: the 2026 settlement range is about $60–118 [1], and the price moved $100 → $110 → $103.5 → $110 within the first half of October [1][4][2]. Those moves fit an annualised volatility of roughly 50–60%. Over 8 days that is a standard deviation of about 10%, or roughly ±$10–11.

### Inside view

- **Base path (88% weight):** the war continues and Hormuz flows stay about 30% below normal [2]. Tankers are being attacked, and the futures curve is in deep backwardation [5]. I use a fat-tailed walk (Student-t, 4 degrees of freedom) at 55% annualised volatility, centred on $108 with a slight downward drift. That drift allows for the IEA release of 100 million barrels and the US considering easing sanctions on shipping [1].
- **Deal path (12% weight):** Iran says its offer to reopen Hormuz within 7 days "remains on the table". The US wants the nuclear issue dealt with first, and Trump rejected the seven-day ceasefire [3][2]. If a deal or ceasefire is announced, the April ceasefire is the analogue: Brent fell to about $92–93 then [6]. I model this path as centred on $94.
- There is also some upside tail from escalation, such as more tanker strikes or the talks collapsing. The fat tails of the base path cover it.
- A Monte Carlo of this mixture (`model.py`) gives p5 89.1, p10 93.1, p25 99.9, p50 106.2, p75 112.2, p90 118.6, p95 123.6. I rounded these slightly.

### Evidence

- 2026-10-16: Brent settled at $109.86, up $3.94 (3.7%), its highest since 19 May [2].
- 2026-10-19: Brent at $108.05, down $1.81 (1.65%) from the previous close; WTI at $100.68. Iran's offer to reopen Hormuz is still open, but the US wants the nuclear file addressed first [3].
- 2026-10-12: Brent opened at $103.50 after the US announced an energy-infrastructure truce between Russia and Ukraine; it reached $109.97 intraday earlier that week [4].
- 2026-10-14: the Dec 2026 contract settled at $106.06; on 2026-10-05 it settled at $100.32. The EIA's October Short-Term Energy Outlook puts Brent at about $96 on average for 2026 (from the question background [1]).
- Week to 13 October: about 9.5 million barrels per day passed through Hormuz, roughly 30% below pre-war levels, and nine tankers were attacked in a week [2].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Kalshi KXBRENTW (16 Oct close) | ~63% above $99.99, ~49% above $101.99 | 2026-10-16 (from search snippet) | stale, and the settlement came in higher ($109.86); page not fetchable (HTTP 429) |
| EIA STEO | 2026 average about $96 | 2026-10-06 | an annual average, not a forecast for 29 October |

### What would change my mind

- A US–Iran deal on Hormuz, or a ceasefire, announced before 29 October. That would move most of the probability mass to $90–98.
- A further escalation, such as a major attack on Gulf export infrastructure or a full closure of Hormuz, which would push the price toward $120 or above.

### Sources

1. Metaculus question 46145, background and resolution text (cached `raw/metaculus-question-2026-10-19.json`), https://www.metaculus.com/questions/46145/ (accessed 2026-10-19)
2. Web search digest of the Brent settlement on 16 October and the Hormuz flows: The Hill, "Brent crude hits $110 per barrel for first time since May", https://thehill.com/policy/energy-environment/6155062-brent-crude-hits-110/ (accessed 2026-10-19; snippet only, page returned HTTP 403)
3. HDFC Sky, "Gift Nifty points to green start … as Iran's Hormuz offer eases oil", https://hdfcsky.com/news/gift-nifty-points-to-green-start-for-sensex-nifty-as-irans-hormuz-offer-eases-oil-october-19-2026 (accessed 2026-10-19)
4. Procurement Resource, "Brent crude oil falls to 103.50 dollars per barrel", https://www.procurementresource.com/news-and-articles/brent-crude-oil-falls-to-103-50-dollars-per-barrel (accessed 2026-10-19)
5. CMB News, "Crude Oil Market Analysis: Brent Above $110, Futures Backwardation Deepens", https://commodity-board.com/hormuz-shock-pushes-brent-above-110-as-futures-curve-tightens (accessed 2026-10-19; snippet)
6. Hargreaves Lansdown, "Iran ceasefire relief sends shares soaring and energy prices sharply down", https://www.hl.co.uk/news/iran-ceasefire-relief-sends-shares-soaring-and-energy-prices-sharply-down (accessed 2026-10-19; snippet)
7. Kalshi KXBRENTW 16 October market, https://kalshi.com/markets/kxbrentw/brent-oil/kxbrentw-26oct1617 (accessed 2026-10-19; snippet)

**Question**: [What will the Brent crude oil front-month futures settlement price be on October 29, 2026?](https://www.metaculus.com/questions/46145/)
**Date**: 2026-10-19
**Forecast**: Median 106.5 $/bbl, IQR [100.0 $/bbl, 112.0 $/bbl]
**Thesis**: Brent settled at $109.86 on 16 October and was around $108 on 19 October, with the Iran war and Hormuz disruption ongoing. I model a random walk with fat tails at about 55% annualised volatility over 8 trading days. I add a 12% chance of a US–Iran Hormuz deal, which would send the price back toward the low $90s, as after the April ceasefire. The forecast is most sensitive to whether that deal happens before 29 October.
