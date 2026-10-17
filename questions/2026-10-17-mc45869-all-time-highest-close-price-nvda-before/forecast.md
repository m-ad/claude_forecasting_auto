# What will be the all-time highest close price of NVDA before January 1, 2027?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/45869/ |
| **Type** | numeric (USD per share; Metaculus range 236–275, both bounds open) |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-12-01 / 2027-01-01 |
| **Status** | open |
| **Current forecast** | **Median $239.24, IQR [$239.24, $262.0]** (v1, 2026-10-17) |
| **Community (as of 2026-10-17)** | no CP yet (question opens 2026-10-19) · Pro — · Gold — · n=11 pre-open |
| **Next review** | 2026-10-31 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-17

### What resolves YES
Numeric question: the highest **daily closing price** NVDA has ever recorded, as it stands after the
last trading session of 2026 (2026-12-31). **Caveat — inferred digest:** the Metaculus resolution text
could not be retrieved this session (the post is pre-open; the bot-key API returns `null` criteria
before opening and every browser fetch was Cloudflare-challenged, see `research.md`). The digest
rests on the title, the API metadata (numeric, range $236–$275, open both ends; scheduled close
2026-12-01, resolution 2027-01-01) and standard practice (split-adjusted closes from a major data
vendor). The $236 lower bound matches the previous record close of $235.74 (2026-05-14), i.e. the
question was written before the October records. Because the answer can never fall below the
current record, the outcome is **floored at $239.24** (close of 2026-10-06; intraday high $243.37
does not count). Edge cases: a stock split (would be split-adjusted), ±$0.13 vendor rounding.

### Outside view
Reference class: the running maximum of a ~40%-volatility mega-cap over 52 trading sessions
(2026-10-19 → 2026-12-31), starting 10.5% below its record. A driftless random walk with
annual σ≈40% has a 52-day σ≈18%; the reflection principle gives
P(max ≥ +11.7%) ≈ 2·(1−Φ(0.61)) ≈ 54% under continuous monitoring, ~48–50% for discrete closes
after the Itô drag. NVDA's own Q4 seasonality (up 20 of 27 years, median +14%, Motley Fool) argues
for a bit more, but it is contaminated by NVDA's extraordinary secular drift, so I give it little weight.

### Inside view
Monte Carlo (200k–400k paths, Student-t(4) daily shocks, earnings gap σ=6% on 2026-11-19):

| Model | P(new record) | Median | p75 | p90 |
|---|---|---|---|---|
| vol 35%, drift 0 | 41.6% | 239.2 | 253.0 | 275.5 |
| vol 42%, drift 0 | 47.5% | 239.2 | 260.1 | 287.4 |
| vol 42%, drift 15% | 52.7% | 241.3 | 266.0 | 294.6 |
| vol 50%, drift 0 | 52.4% | 241.1 | 268.4 | 301.0 |
| bootstrap 2y returns, demeaned | 51.0% | 240.0 | 263.5 | 290.7 |
| **central: vol 42%, drift 5%** | **49.1%** | **239.2** | **262.0** | **289.6** |

The central model gives P(record by 2026-10-30) 11.6% and P(record before earnings) 28.8%: most of
the upside path runs through the 2026-11-18 Q3 FY2027 report (inferred date) and the December
rally window. Volatility inputs: realized 20d 24.8%, 60d 36.8%, 1y 37.3%, 2y 43.8%; options priced a
5.5–6.9% earnings move in May/Aug 2026 against a 7.4% realized average.

### Evidence
- **For a new high (LR ≈ 1.1):** Q2 FY27 beat (rev $96.2B), Q3 guide $108B ±2% with zero China data
  center assumed, FY28 growth framed at ~70% (supply-constrained); ~15× FY28 EPS; $150B buyback;
  consensus target ≈$322. Seasonality.
- **Against (LR ≈ 0.9):** the 2026-10-12→16 "AI-funding" rout (CNBC: >$1T lost by the top-20 AI/semis
  in a week) on rising Treasury yields, neocloud financing doubts, custom silicon (Maia) and Huawei
  share gains; four straight negative next-day earnings reactions before August.
- Net: roughly offsetting → I keep the central model, P(record) ≈ 49–50%.

### Other forecasters
| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | — | 2026-10-17 | pre-open; reveal 2026-10-23 |
| Metaculus Pro | — | 2026-10-17 | not available pre-open |
| Metaculus gold medalists | — | 2026-10-17 | not available pre-open |
| Polymarket "NVDA above $240 in October" | 8.5% | 2026-10-17 | ~$80 volume, noise; my model: 11.6% by 10-30 |
| Kalshi | no matching market | 2026-10-17 | |
| Analyst consensus target | ≈$322 (12-month) | 2026-10-16 | MarketBeat; not a year-end forecast |

No cohort data to compare yet.

### Scenarios
| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | AI-funding scare persists / weak Q4 guide; no new record close | 51% | exactly $239.24 |
| 2 | Recovery to a marginal new record ($239–255) | 18% | ~$247 |
| 3 | Post-earnings / December rally ($255–290) | 21% | ~$270 |
| 4 | Melt-up (>$290) | 10% | ~$305 |

### Sensitivity
| Assumption | If instead | Forecast becomes |
|---|---|---|
| Vol 42% | 35% | P(record) 42%, p75 $253 |
| Vol 42% | 50% | P(record) 52%, median $241, p75 $268 |
| Drift ≈ 0 | +15%/yr (momentum/seasonality) | P(record) 53%, median $241, p75 $266 |

### What would change my mind (tripwires)
- [ ] NVDA close ≥ $230 on or before 2026-10-30 (halfway back) → up, median +$4 (p75 +$8)
- [ ] NVDA close ≤ $195 on or before 2026-11-13 (−8% more before earnings) → down, p75 −$12
- [ ] Q3 FY27 report (≈2026-11-18): Q4 revenue guide ≥ $122B and stock +5% next day → up, p75 +$12
- [ ] Hyperscaler Q3 calls (≈2026-10-27/30) cut 2027 capex guidance → down, p75 −$8
- [ ] Any close > $239.24 before 2026-12-01 → re-anchor floor upward (mechanical, either direction of tails)

### Sources
1. Yahoo Finance chart API, NVDA daily 2y — https://query1.finance.yahoo.com/v8/finance/chart/NVDA?range=2y&interval=1d (accessed 2026-10-17; cached `raw/yahoo-nvda-2026-10-17.json`)
2. StockAnalysis NVDA price history — https://stockanalysis.com/stocks/nvda/history/ (accessed 2026-10-17)
3. Bloomberg, "Nvidia Shares Hit Record High, Market Value Approaches $6 Trillion" (2026-10-02) — https://www.bloomberg.com/news/articles/2026-10-02/nvidia-hits-first-record-since-may-as-value-nears-6-trillion (accessed 2026-10-17)
4. CNBC, "Nvidia, AMD, Dell sink in global tech rout on AI funding worries" (2026-10-15) — https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html (accessed 2026-10-17)
5. Benzinga, "Rising Treasury Yields Trigger Nvidia, AMD Slump" — https://www.benzinga.com/markets/tech/26/10/62393159/rate-pressure-vs-ai-demand-rising-treasury-yields-trigger-nvidia-amd-slump (accessed 2026-10-17)
6. FX Leaders, "Nvidia Stock Extends Slide Toward $200 as ASML Warns" (2026-10-15) — https://www.fxleaders.com/news/2026/10/15/nvidia-stock-nvda-extends-slide-toward-200-as-asml-warns-of-chipmaking-capacity/ (accessed 2026-10-17)
7. MarketBeat, "NVIDIA Shares Down 1.4%" (2026-10-16) — https://www.marketbeat.com/instant-alerts/price-nvidia-nasdaq-nvda-shares-down-14-heres-what-happened-2026-10-16/ (accessed 2026-10-17)
8. Motley Fool, "History Says Nvidia Stock Usually Rises in the Fourth Quarter" (2026-10-14) — https://www.fool.com/investing/2026/10/14/history-says-nvidia-stock-usually-rises-in-the-fourth-quarter-it-has-in-20-of-the-last-27/ (accessed 2026-10-17)
9. XTB, "Nvidia shares react to solid earnings report and stronger guidance" (2026-08-26) — https://www.xtb.com/en/market-analysis/nvidia-shares-react-to-solid-earnings-report-and-stonger-guidance-what-s-next-for-the-ai-giant (accessed 2026-10-17)
10. Webull, "Nvidia Q2 FY2027 Earnings Beats ... Guides Q3 to $108B" — https://www.webull.com/blog/304-Nvidia-Q2-FY2027-Earnings-Beats-Revenue-EPS-Estimates-Guides-Q3-to-108B (accessed 2026-10-17)
11. Wall Street Horizon, Nvidia earnings calendar (inferred 2026-11-18) — https://www.wallstreethorizon.com/nvidia-earnings-calendar (accessed 2026-10-17)
12. SpotGamma, NVDA earnings positional analysis — https://spotgamma.com/nvda-earnings-positional-analysis/ (accessed 2026-10-17)
13. Capital.com, "What can options positioning tell us about post-earnings moves" — https://capital.com/en-eu/analysis/michael-kramer-what-can-options-positioning-tell-us-about-post-earnings-moves (accessed 2026-10-17)
14. heygotrade, "Nvidia Stock News (Oct 16, 2026)" — https://www.heygotrade.com/en/news/nvidia-nvda-stock-news-october-16-2026/ (accessed 2026-10-17)
15. Polymarket, "NVDA above ___ in October 2026" via gamma API — https://gamma-api.polymarket.com/public-search?q=nvidia%20close (accessed 2026-10-17)
16. Metaculus API post 45869 (metadata only) — https://www.metaculus.com/questions/45869/ (accessed 2026-10-17; cached `raw/metaculus-api-2026-10-17.json`)

**Question**: [What will be the all-time highest close price of NVDA before January 1, 2027?](https://www.metaculus.com/questions/45869/)
**Date**: 2026-10-17
**Forecast**: Median $239.24, IQR [$239.24, $262.0]
**Thesis**: NVDA must rise 11.7% from $214.13 to beat its $239.24 record close; a fat-tailed 42%-vol Monte Carlo with a Nov-18 earnings jump puts that at ~49%, so the median sits on the current record with a long right tail (p90 ≈ $290). Strong guidance and Q4 seasonality roughly offset the October AI-funding/rates sell-off (Yahoo data, CNBC, Motley Fool).
