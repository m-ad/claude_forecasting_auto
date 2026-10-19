# Will Brent crude close above $104 per barrel on October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46130/ |
| **Tournament** | minibench — one shot, window 2026-10-19T03:04:24Z -> 2026-10-19T06:04:24Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 62.0%, IQR [54.0%, 69.0%] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

YES if the Brent crude price that Trading Economics reports for Thursday 29 October 2026 (in practice, the day's close) is **strictly above $104.00/bbl**. $104.00 or lower is NO. If Trading Economics has no value for that date, the front-month ICE Brent settlement from credible sources is used. If the market is closed that day, the most recent prior trading day counts. An LLM resolves this, so the close Trading Economics shows for 29 Oct is what counts; intraday highs and lows do not.

### Outside view

There is no event-type reference class here. The question is a random-walk problem: how likely is a price now at about $107.9 to finish above $104 after roughly 8.5 trading days (the rest of 19 Oct plus 20–23 and 26–29 Oct)?

- **Distance to threshold:** ln(104/107.9) ≈ −3.7%.
- **Volatility:** 2026 Brent has been extremely volatile. The 52-week range is about $58.7–$126.4 [1]. Single-day moves of 6–8% have happened on Iran-war and ceasefire headlines (−6% on the April ceasefire, −8% on a July "pause" in strikes [5][6]). I assume 45–55% annualised, which is about 2.8–3.5% a day.
- **Spread over the horizon:** √8.5 × 3.1% ≈ ±9% (1σ).
- **Driftless lognormal result:** z ≈ 0.40, so P(close > $104) ≈ **65%** (range 63–68% across the volatility assumptions).

### Inside view

Two adjustments, both downward:

1. **Headline skew is to the downside.** The price carries a geopolitical risk premium (Hormuz flows cut, tanker damage, Saudi facility attacks [1][4]). A de-escalation headline (talks, a ceasefire, a strike "pause") has repeatedly removed $6–18 in a session [5][6]. Escalation can add similar amounts, but from $108 the downside jumps are what decide this question. The 2026 average is in the low $90s [1], and sell-side forecasts for Q4 were far lower (JPMorgan about $80 [7]). Momentum still matters on a 10-day horizon, though: Brent gained more than 5% last week and hit a 4-week high [1].
2. **Monday weakness.** On 19 Oct Brent is already down about 1.8% from Friday's ~$110 but "retained most of last week's gains" [1]. The cushion is about $4, roughly 0.4σ.

Net: I take the 65% random-walk figure down about 3 points for jump skew and premium mean reversion, to **62%**. The IQR, 54–69%, reflects uncertainty about volatility and where the price opens this week.

### Evidence

- 19 Oct 2026 (Trading Economics): Brent $107.9, −1.78% on the day. It slipped below $108 after a sharp weekly rise, with Middle East clashes, tanker damage in Hormuz and Ukrainian strikes on Russian energy keeping supply risk high [1].
- 16 Oct 2026: Brent near $110, up more than 5% for the week, on higher freight rates and reduced Hormuz flows. Trading Economics also flagged a 4-week high of $108.28 [1].
- 12 Oct 2026: Brent settled at $106.65, its highest since 15 Sep. On 13 Oct it was $106.04 after attacks on Saudi Arabia and on tankers near Hormuz [4].
- Question background: mid-October range about $103–109; 52-week range $58.72–$126.41; 2026 average in the low $90s [1][question text].
- History of headline shocks: April 2026 two-week US–Iran ceasefire, about −6% to $103.40 and a reported $18 plunge [5]. July 2026 White House pause on Iran attacks, −8% to $89 [6]. The June 60-day ceasefire later lapsed with no talks scheduled [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-19 | — |
| Kalshi (KXBRENTMON, 30 Oct) | not retrieved (HTTP 429) | 2026-10-19 | the 16 Oct weekly snapshot in search results looked stale |
| Polymarket | no Brent close market found; WTI "hit in October" snapshot only | 2026-10-04 | different question; not used |

### What would change my mind

- A credible US–Iran de-escalation headline (talks resuming, a strike pause, Hormuz reopening) before 29 Oct would likely knock $5–10 off and make NO the favourite.
- New escalation (US strikes on Iran, more tanker attacks) would push the probability above 80%.
- The forecast is most sensitive to the assumed volatility and to whether Monday's slide continues. A Brent close already under $104 early this week would move it to roughly 40–45%.

### Sources

1. Trading Economics, Brent crude oil, quote and news feed: https://tradingeconomics.com/commodity/brent-crude-oil (accessed 2026-10-19)
2. Metaculus question 46130, cached question text: https://www.metaculus.com/questions/46130/ (accessed 2026-10-19)
3. Kalshi KXBRENTW market listing (search snippet only): https://kalshi.com/markets/kxbrentw/brent-oil/kxbrentw-26oct1617 (accessed 2026-10-19)
4. IDN Financials, "Brent crude falls to USD 106.04 as markets assess Middle East risks": https://www.idnfinancials.com/news/70194/brent-crude-falls-to-usd-106-04-as-markets-assess-middle-east-risks (accessed 2026-10-19)
5. India TV News, "Oil prices plunge by USD 18 per barrel as US, Iran announce two-week ceasefire": https://www.indiatvnews.com/news/world/oil-prices-plunge-by-usd-18-per-barrel-as-us-iran-announce-two-week-ceasefire-2026-04-08-1036697 (accessed 2026-10-19)
6. FXEmpire, "Crude futures sink but Hormuz and Red Sea risks hold": https://www.fxempire.com/forecasts/article/premium-oil-news-crude-futures-sink-but-hormuz-and-red-sea-risks-hold-1613158 (accessed 2026-10-19)
7. KuCoin News, "JPMorgan downgrades Brent crude outlook for 2026 and 2027": https://www.kucoin.com/news/flash/jpmorgan-downgrades-brent-crude-outlook-for-2026-and-2027 (accessed 2026-10-19)
8. Scripps News, "Trump says no talks planned with Iran after 60-day ceasefire deal expires": https://www.scrippsnews.com/us-news/iran-war/trump-says-no-talks-planned-with-iran-after-60-day-ceasefire-deal-expires (accessed 2026-10-19)

**Question**: [Will Brent crude close above $104 per barrel on October 29, 2026?](https://www.metaculus.com/questions/46130/)
**Date**: 2026-10-19
**Forecast**: Median 62.0%, IQR [54.0%, 69.0%]
**Thesis**: Brent is about $107.9 on 19 Oct (Trading Economics), roughly 3.7% above the threshold with 8.5 trading days left. A driftless lognormal at about 50% annualised volatility gives about 65% for a close above $104. I shade that to 62% because this year's de-escalation headlines have repeatedly cut 6–8% in a day. The forecast is most sensitive to whether a US–Iran de-escalation headline lands before 29 Oct.
