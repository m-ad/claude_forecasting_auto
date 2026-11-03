# What will the month-over-month change in US producer prices excluding food, energy, and trade services be for October 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46418/ |
| **Tournament** | minibench — one shot, window 2026-11-03T04:20:26Z -> 2026-11-03T07:20:26Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-03 / 2026-11-03 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | Median 0.4, IQR [0.3, 0.5] (v1, 2026-11-03) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-03

### What resolves YES

The value is the seasonally adjusted 1-month percent change in the BLS PPI for "final demand less foods, energy, and trade services" for **October 2026**, as first published in the BLS release scheduled for Friday 2026-11-13, 8:30 ET (confirmed on the BLS schedule page, accessed 2026-11-03). It is reported to one decimal; later revisions do not count. Last published period is September 2026 (released 2026-10-15): +0.5%. The target period is the very next month (October), one period ahead, so no multi-period projection. No fallback formulas apply. If the release is delayed it resolves when first published; I found no sign of a shutdown or delay. Recent prints (Table A of the Sept release, as revised): Jan 0.5, Feb 0.5, Mar 0.2, Apr 0.5, May 0.8, Jun 0.2, Jul 0.5, Aug 0.3, Sep 0.5. (The question text says Jul 0.4; the BLS table I fetched shows 0.5 after revisions. First-published values differ from revised ones.) The mean over the last 13 months is about 0.40 and the standard deviation about 0.2.

### Outside view

Reference class: the monthly first-print change of this series over the last 13 months (Sep 2025–Sep 2026; n=13): values 0.2, 0.6, 0.3, 0.1, 0.5, 0.5, 0.2, 0.5, 0.8, 0.2, 0.5, 0.3, 0.5. Mean ≈ 0.40, median 0.5 (mean-based 0.4), range 0.1–0.8, sd ≈ 0.2. The 12-month change is 5.0%, which is 0.41% per month. After a month at or above 0.5 the following month averaged about 0.38 (six cases: 0.3, 0.5, 0.2, 0.8, 0.2, 0.3). Base distribution: centred at 0.4, p10 ≈ 0.15, p90 ≈ 0.7.

### Inside view

Adjustments from the base distribution are small:
- Persistence: tariff pass-through (Section 232 metals regime, April 2026), a Hormuz-driven energy shock, ISM prices paid 77.9 in September and a flash PMI showing the fastest selling-price increases since Aug 2022 all argue the pipeline stays hot. Pushes up slightly.
- Mean reversion: September's 0.5 leaned on transportation and warehousing (+3.4%, after +2.2% in Aug); services less trade, transport and warehousing rose only 0.3% and goods less food and energy 0.3%. October retail diesel was flat to slightly lower on the month average ($6.18/6.28/6.35 weekly vs $6.29 September average), jet fuel remained very high, and the S&P 500 fell about 2.2% in October (mostly late), which can weigh on portfolio-management fees with a lag. Transport and warehousing is the main swing factor; a payback would pull the print to 0.2–0.3.
- Net: median 0.4, a shade below the recent six-month average of 0.47, with a fat right tail (May printed 0.8) and a left tail to 0.0–0.1 (Dec 2025 printed 0.1).

### Evidence

- BLS PPI September 2026 release (2026-10-15): the index rose 0.5% in September after 0.3% in August; 5.0% over 12 months; transport and warehousing +3.4%; goods less foods and energy +0.3%; services less trade/transport/warehousing +0.3% [1][2].
- Headline final demand +1.3% in September, energy +10.8% (excluded from this series, but feeds pass-through into freight) [1][2].
- Next release confirmed for 2026-11-13; no sign of a shutdown or delay in searches [3].
- Fuel (EIA weekly diesel): $6.179 Oct 12, $6.276 Oct 19, $6.352 Oct 26; September average $6.29 (record) [4].
- ISM manufacturing prices paid 77.9 in September; October consensus 77.5 (October release not found) [5]. S&P Global flash PMI (Oct 23): selling prices rising at the fastest rate since Aug 2022 apart from September [6].
- S&P 500: 7,750 end-September to 7,580 on Oct 30, about -2.2% [6].
- Tariffs: IEEPA tariffs struck down in Feb 2026, replaced by Section 122/301 and expanded Section 232; no October-specific tariff shock found [7].
- No economist consensus for this specific series for October is published as of today; headline PPI Manifold market sits near 54% for ≥0.3 (thin, play money) [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-03 | |
| Kalshi / Polymarket | no October core-PPI m/m market found (only YoY headline markets) | 2026-11-03 | |
| Manifold | headline PPI ≥0.3% m/m: ~54% | 2026-11-03 | ~11 trades, headline not this series; discount heavily |
| Consensus | none published for this series | 2026-11-03 | |

### What would change my mind

- A known payback in transportation and warehousing (airline passenger services and freight surged in September): if October CPI airfares or trucking rates collapsed, the median should fall to 0.2–0.3.
- Evidence that October ISM/PMI input prices accelerated further, or a new tariff action effective in October, would raise the median to 0.5 and fatten the upper tail.
- Biggest assumption: that the September transport spike does not fully reverse (tested by disconfirmation searches on airfares, diesel and payback; none showed an October fall in jet fuel or fares).

### Sources

1. https://www.bls.gov/news.release/ppi.nr0.htm (accessed 2026-11-03)
2. https://www.bls.gov/news.release/archives/ppi_10152026.htm (accessed 2026-11-03)
3. https://www.bls.gov/schedule/news_release/ppi.htm (accessed 2026-11-03)
4. https://www.eia.gov/petroleum/gasdiesel/ (accessed 2026-11-03)
5. https://www.ftportfolios.com/Commentary/EconomicResearch/2026/10/1/the-ism-manufacturing-index-declined-to-54.5-in-september (accessed 2026-11-03)
6. https://stockmarketwatch.com/digest/2026-10-30 (accessed 2026-11-03)
7. https://www.cozen.com/news-resources/publications/2026/supreme-court-rules-president-lacks-ieepa-tariff-authority-president-imposes-section-122-tariffs (accessed 2026-11-03)
8. https://manifold.markets/CalibratedGhosts/will-october-2026-us-ppi-final-dema (accessed 2026-11-03)

**Question**: [What will the month-over-month change in US producer prices excluding food, energy, and trade services be for October 2026?](https://www.metaculus.com/questions/46418/)
**Date**: 2026-11-03
**Forecast**: Median 0.4%, IQR [0.3%, 0.5%]
**Thesis**: The series averaged ~0.4% per month over the last 13 months (0.47% over the last six) with a 5.0% annual rate, and inflationary pipeline indicators (ISM prices 77.9, record selling-price PMI) support persistence; a partial payback of September's +3.4% transport and warehousing jump is the main downside risk, and the forecast is most sensitive to that component.
