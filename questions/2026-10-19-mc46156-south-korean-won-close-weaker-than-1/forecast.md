# Will the South Korean won close weaker than 1,340 per US dollar on October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46156/ |
| **Tournament** | minibench — one shot, window 2026-10-19T19:58:17Z -> 2026-10-19T22:58:17Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 30.0%, IQR [22.0%, 38.0%] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

YES if the USD/KRW rate (won per one US dollar) that Trading Economics reports for **October 29, 2026** on its South Korean Won page is **strictly above 1,340.00**. A value of 1,340.00 or lower is NO. Trading Economics' daily value is a market close, not the Seoul 15:30 fix. Its prints have run a few won away from the Seoul close (Oct 14: TE 1,339.27 vs Seoul 1,338.3). If TE has no value dated Oct 29, the Oct 29 close from Wise or Investing.com is used; if no source has one, the question is annulled. The Oct 29 close comes after the FOMC decision of Oct 28, so it includes the market's reaction.

### Outside view

The reference class is a random walk over 8 trading days (Oct 20–29) with the threshold 0.66% above spot. Spot is 1,331.24 on TE for Oct 19 [1]. Realized daily volatility of USD/KRW closes from Oct 1 to 19 was 0.42%, or 0.30% excluding one 15-won drop on Oct 2 [2]. That annualises to roughly 5–7%; the September prints imply similar daily moves of 3–10 won [3]. Eight days at 0.35–0.55% a day gives a standard deviation of about 1.0–1.6% (13–21 won), so 1,340 sits about 0.4–0.65 standard deviations above spot. With no drift, that puts P(>1,340) at about 26–34%.

### Inside view

- **Trend (toward NO).** The won has strengthened from a 1,559 intraday peak on Jul 1 to about 1,330 [3][4]. It is down 3.2% over the month on TE [1] and at its strongest since October 2024 (intraday 1,327.6 on Oct 19) [5]. Exporters are selling dollars on a semiconductor boom [4][6]. TE's model has 1,325 at quarter-end [1].
- **Soft floor (toward YES).** The rate has bounced near 1,331–1,336 several times: Sep 7, Sep 9, Oct 12, Oct 16 and Oct 19 [3][4][7]. On Sep 7 the National Pension Service (NPS) suspended its FX hedging and bought dollars, and the authorities absorbed about $20bn [8]. From Oct 2 to Oct 15, 7 of 10 closes were at or above 1,340 [2]. The level only broke below that band on Oct 16.
- **FOMC Oct 28 (toward YES).** The Fed hiked in September to 3.75–4.00%. On Oct 15 the market put a 25–33% probability on another hike (FedWatch 24.9%, Kalshi 33%) after a hot CPI print [9]. A hike would likely lift USD/KRW by around 0.5–1%. A hold is mildly dollar-negative. The Bank of Korea (BOK) is expected to hold on Oct 22 [9].
- **Foreign equity flows (mixed).** Foreign investors sold KOSPI shares for 7–8 straight sessions, then turned net buyers on Oct 16 [5][10].

**Model** (`model.py`): Student-t daily shocks, daily sd 0.35–0.55%, drift of −0.3% to 0, and a 30% FOMC-hike jump of +0.6% (otherwise −0.15%). This gives P(>1,340) between 19% and 35%; the central case (0.45% sd) gives 24–32%. I put the midpoint near 30%: the trend argues for a lower number, while the policy floor and the hike risk keep it from going much lower.

### Evidence

- TE, Oct 19 2026: "fell to 1,331.2400 on October 19, 2026, down 0.25%"; strengthened 3.18% over a month; quarter-end forecast 1,325.37 [1].
- Daily closes in October from PoundSterlingLive: 1,358.52 (Oct 1), 1,343.34 (Oct 2), 1,337.86–1,342.11 (Oct 5–15), 1,334.65 (Oct 16), 1,332.81 (Oct 19) [2].
- Seoul closes: Oct 14 1,338.3 [10]; Oct 16 1,331.4, down 13.2 after Fed Chair Warsh's IMF remarks, with DXY falling to 101.81 [7]; Oct 19 1,330.3 at 15:30 [5].
- Fed odds for an Oct 28 hike as of Oct 15: FedWatch 24.9%, Kalshi 33% [9].
- NPS hedging suspended and dollar buying near 1,334.7 on Sep 7 2026 [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | |
| Polymarket / Kalshi / Manifold | no matching market | 2026-10-19 | only Polymarket "USD/KRW hit X in 2026" touch markets |
| 30rates (algorithmic) | 1,333 for Oct 29 (1,313–1,353) | 2026-10-19 | low-quality aggregator [11] |
| TE model | 1,325 by end-Q4 | 2026-10-19 | [1] |
| State Street | 1,390–1,400 by year-end | 2026-09-28 | predates the October rally |

### What would change my mind

- A Fed hike on Oct 28. Hike odds are 25–33% and it is the single largest upside risk.
- Signs that the authorities or the NPS are defending the 1,330 area, for example a renewed resumption of NPS dollar buying. That would raise the odds.
- A break below about 1,320 in the next few days would make YES unlikely.

### Sources

1. Trading Economics, South Korean Won — https://tradingeconomics.com/south-korea/currency (accessed 2026-10-19)
2. PoundSterlingLive, USD/KRW 2026 history — https://www.poundsterlinglive.com/history/USD-KRW-2026 (accessed 2026-10-19)
3. Financial News, won closes Sep 2026 — https://en.fnnews.com/news/202609071327373068 and https://en.fnnews.com/news/202609101533266366 (accessed 2026-10-19)
4. Korea JoongAng Daily, "Won nears two-year high against dollar" (Oct 12) — https://www.koreajoongangdaily.com/business/won-nears-twoyear-high-against-dollar/12916231 (accessed 2026-10-19)
5. Korea Times, "Korean won hits over 2-year high against US dollar" (Oct 19) — https://www.koreatimes.co.kr/economy/20261019/korean-won-hits-over-2-year-high-against-us-dollar (accessed 2026-10-19)
6. Trading Economics news, Sep 23 2026 — https://tradingeconomics.com/south-korea/currency/news/585908 (accessed 2026-10-19)
7. Seoul Economic Daily, "Won jumps 13 won…" (Oct 16) — https://en.sedaily.com/finance/2026/10/16/won-jumps-13-won-against-dollar-after-fed-chairs-imf-remarks (accessed 2026-10-19)
8. The Standard (Reuters), NPS suspends FX hedging — https://www.thestandard.com.hk/finance/article/342047/South-Korea-pension-fund-suspends-FX-hedging-as-won-hits-two-year-high-source-says (accessed 2026-10-19)
9. Crypto Briefing, Fed hike odds after CPI (Oct 15) — https://cryptobriefing.com/market-odds-25-bps-fed-hike-october/ (accessed 2026-10-19; secondary source)
10. Korea Times, KOSPI Oct 14 wrap — https://www.koreatimes.co.kr/economy/others/20261014/kospi-falls-for-6th-session-barely-holds-above-6000 (accessed 2026-10-19)
11. 30rates, USD/KRW forecast — https://30rates.com/usd-to-krw-today-forecast-dollar-to-won (accessed 2026-10-19)

**Question**: [Will the South Korean won close weaker than 1,340 per US dollar on October 29, 2026?](https://www.metaculus.com/questions/46156/)
**Date**: 2026-10-19
**Forecast**: Median 30.0%, IQR [22.0%, 38.0%]
**Thesis**: USD/KRW is at 1,331.24 on Trading Economics for Oct 19, 0.66% below the threshold. With 8 trading days of about 0.3–0.5% daily volatility, a random walk gives roughly 26–34%. The won's three-month strengthening trend pulls the number down. Policy support near 1,330 (NPS dollar buying) and a 25–33% chance of a Fed hike on Oct 28 keep upside risk alive, and that hike is the factor the forecast is most sensitive to.
