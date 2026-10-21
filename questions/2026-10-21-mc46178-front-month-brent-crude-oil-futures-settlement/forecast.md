# What will the front-month Brent crude oil futures settlement price be on October 30, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46178/ |
| **Tournament** | minibench — one shot, window 2026-10-21T01:12:58Z -> 2026-10-21T04:12:58Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-21 / 2026-10-21 / 2026-10-31 |
| **Status** | open |
| **Current forecast** | Median 108, IQR [103, 113.5] (v1, 2026-10-21) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-21

### What resolves YES

The question resolves to the daily settlement ("Last") price, in $/bbl, of the front-month ICE Brent continuous contract for trading date Friday 30 October 2026, as shown on Barchart's CB*0 historical page. Other credible sources are the fallback. The bounds are open: values below $80 or above $135 count at their actual level. One mechanical detail matters. The December 2026 contract expires on that same day, the last business day of October [5]. The question's fine print expects the December contract to be the one used. If Barchart's continuous series has already rolled to January 2027 on 30 Oct, the printed value would be about $3 lower, because the curve is in steep backwardation (later contracts trade below nearer ones).

### Outside view

This is a random walk from the latest futures price over 8 settlements. December Brent settled at $108.79 on 20 Oct [1] and traded around $109.6–110.0 early on 21 Oct [1][2]. Implied volatility is high: the CBOE crude oil volatility index (OVX) was 50.7 on 19 Oct [6], so a 1-sigma move over 8 trading days is about 8.5–9%, roughly ±$9.5. Prices this year have swung $10 or more on single Iran-diplomacy headlines; Brent was $71–87 during earlier peace hopes [7]. That argues for fat tails.

### Inside view

The futures price already reflects the market's expectation, so I put no strong drift on it. Analyst forecasts sit below spot (Goldman's December target is $90, EIA's Q4 average is $104.7 [4][8]). Against them, tanker attacks in Hormuz and Houthi strikes keep a risk premium in place [1]. The two roughly offset, apart from a slight tilt toward mean reversion after the five-month high. I ran a Monte Carlo (`model.py`): start $109.6, 48% annualised volatility, Student-t(4) shocks, and a 35% chance that the printed value is the January contract (minus ~$3 ± 1). It gives p5/25/50/75/95 = 94.7 / 103.2 / 108.2 / 113.3 / 123.3. I widened the tails slightly for jump risk from a US–Iran deal or an escalation.

### Evidence

- 20 Oct 2026: December Brent settled at $108.79 (−$0.76) after a five-month intraday high of $111.99. WTI November expired at $101.79 [1].
- 21 Oct 2026: Brent was about $110.0 (+1.1%), up about 10.9% month on month [2].
- Recent settles: 16 Oct $109.86, 7 Oct $100.20, 6 Oct $100.58 [3]. That is a sharp rally through October.
- Drivers: Iran–Pakistan mediation talks, with a diplomat denying a deal is imminent; at least 18 vessels attacked in two weeks; Hormuz flows at about 70–80% of prewar levels [1][2]. On the bearish side, Russian diesel sanctions are suspended and the US is weighing shadow-fleet licences [1][3].
- OPEC+ holds its next meeting on 1 Nov, after resolution. November targets are flat [3].
- The Dec–Jan spread was about $3.6 on 1 Oct and about $2.6–3 on other recent dates [9].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-21 | — |
| Kalshi weekly/monthly Brent (30 Oct) | not retrievable (HTTP 429) | 2026-10-21 | market exists |
| Polymarket | no end-October Brent market found | 2026-10-21 | — |
| EIA STEO (Oct) | Q4 average $104.69 | Oct 2026 | secondary report [4] |
| Trading Economics | $113.86 end of quarter | 2026-10-21 | model-based [2] |

### What would change my mind

- A signed US–Iran deal or a reopening of Hormuz would push the median toward $95 or lower.
- A major escalation, such as a successful strike on Saudi export infrastructure, would add $10 or more.
- Firm knowledge of whether Barchart's CB*0 rolls to January before the December contract expires would move the median by about ±$1.

### Sources

1. Reuters via Yahoo Finance, "Brent falls as Iran's president discusses mediation with Pakistani army chief", 20 Oct 2026 — https://finance.yahoo.com/news/oil-eases-markets-assess-potential-005750414.html (accessed 2026-10-21)
2. Trading Economics, Brent crude oil — https://tradingeconomics.com/commodity/brent-crude-oil (accessed 2026-10-21)
3. QNA, oil settlement 7 Oct — https://qna.org.qa/en/News-Area/News/2026-10/8/oil-prices-close-lower-at-settlement ; Enerdata OPEC+ November targets — https://www.enerdata.net/publications/daily-energy-news/opec-keeps-november-2026-production-targets-unchanged-amid-supply-disruptions.html (accessed 2026-10-21)
4. Ship & Bunker on the EIA October STEO — https://shipandbunker.com/news/world/921080-ship-bunker-raises-q4-bunker-price-outlook-by-another-124mt-as-eia-puts-q4-brent-above-100 (accessed 2026-10-21)
5. ICE Brent futures contract specification (expiry rule) — https://www.ice.com/api/productguide/spec/219/pdf (accessed 2026-10-21)
6. FRED, CBOE Crude Oil Volatility Index (OVXCLS) — https://fred.stlouisfed.org/data/OVXCLS (accessed 2026-10-21)
7. Trading Economics Brent news archive / The Daily Star on 2026 peace-deal selloffs — https://www.thedailystar.net/business/news/brent-falls-lowest-march-expected-peace-deal-4197646 (accessed 2026-10-21)
8. Angel One, oil prices and the Russia–Ukraine energy ceasefire, 12 Oct 2026 (Goldman December $90) — https://www.angelone.in/news/commodities/crude-oil-prices-fall-on-hopes-of-russia-ukraine-energy-ceasefire-october-12-2026 (accessed 2026-10-21)
9. stock3, Brent curve structure — https://stock3.com/news/warum-brent-fuer-november-104-usd-kostet-und-ein-jahr-spaeter-nur-80-usd-17293882 (accessed 2026-10-21)
10. Tokenpost, "Brent Crude Futures Settle at $108.79" — https://www.tokenpost.com/news/investing/36004 (accessed 2026-10-21)

**Question**: [What will the front-month Brent crude oil futures settlement price be on October 30, 2026?](https://www.metaculus.com/questions/46178/)
**Date**: 2026-10-21
**Forecast**: Median 108.0 $/bbl, IQR [103.0, 113.5] $/bbl
**Thesis**: A random walk from December Brent at about $109–110 (settled $108.79 on 20 Oct, per Reuters), with OVX near 51 implying roughly ±$9.5 over 8 trading days, and fat tails for US–Iran deal or escalation headlines. The median is shaded about $1 lower because the December contract expires on 30 Oct and Barchart's continuous series may already show the January contract, about $3 cheaper in backwardation.
