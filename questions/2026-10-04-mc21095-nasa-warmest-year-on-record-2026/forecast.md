# Will 2026 be the warmest year on record, according to NASA?

| | |
|---|---|
| **Source** | Metaculus #21095 (question group), subquestion id **21098** (label "2026") — https://www.metaculus.com/questions/21095/will-the-following-years-be-the-warmest-year-on-record-according-to-nasa/ |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2024-01-25 / 2027-01-01 / 2027-01-15 (NASA's annual announcement, usually mid-January) |
| **Status** | open |
| **Current forecast** | **Median 59.0%, IQR [49.0%, 68.0%]** (v2, 2026-10-04) |
| **Community (as of 2026-10-04)** | **not retrieved**: three fetch attempts returned HTTP 403 (Cloudflare), and the bot API key hides aggregations (116 forecasters on the group). Operator-relayed comments cite the ERA5-based Climate Brink dashboard (85.5% → 37%; 20.6% on 2026-10-03) and Berkeley Earth's July update (69%) |
| **Next review** | 2026-10-16 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v2 — Update — 2026-10-04

Trigger: the operator relayed three Metaculus community comments the same day. Mode: **Update**. v1 is hours old; the question structure is unchanged.

### Revision

| Driver | Direction | Effect |
|---|---|---|
| Prior (v1, 2026-10-04) | — | Median 51.0%, IQR [43.0%, 60.0%] |
| **The Climate Brink dashboard is ERA5, not NASA.** Its header reads "ERA5 · daily", and the record values it ranks against (2024 = 1.5987, 2023 = 1.4823, 2025 = 1.4711 °C above pre-industrial) are ERA5's [20]. The quoted 85.5% → 37% → **20.6% (2026-10-03)** is the ERA5 record probability. Its projection history shows why: the 2026 annual peaked at 1.6275 on 09-08 and has fallen ~0.002 °C/day since, as late-September ERA5 cooled [21]. v1 already used ERA5 daily data through 10-02, so this decline is **not new information** for the GISTEMP estimate. For calibration: when Carbon Brief put GISTEMP at 65%, ERA5 stood at 13% [6]. ERA5's 20.6% now is not lower than then | → | 0 pp |
| **New information: EC46 dynamical October forecast plus the dashboard's Oct–Dec projection.** The dashboard's ERA5 October projection is 1.81 °C above pre-industrial, i.e. ≈ 0.96 vs 1991–2020 (p05 0.77, p25 0.89, p75 1.04), from ECMWF's 50-member EC46 initialised 10-02 [22]. Its annual projection of 1.5826 against a YTD of 1.4930 implies **ERA5 Oct–Dec ≈ 0.97 (1991–2020)** [21]. That is a rebound from the 0.68–0.70 of 1–2 October, which v1 had treated as mildly bearish. Mapped with an **Oct–Dec-specific** GISS-on-ERA5 regression (2010–2025: GISS = 0.616 + 0.894·ERA5, residual sd 0.043; 2026 residuals running +0.03), that gives **GISS Oct–Dec ≈ 1.51**, against v1's 1.445 (which corresponds to ERA5 ≈ 0.89). I weight the dashboard 50%, because its daily projection has been revised down for 3½ weeks and EC46 skill fades after week 3. Blend: **Oct–Dec 1.475 ± 0.07** → annual 1.301 ± 0.020; buckets ≤1.28: 21% · =1.29: 17% · 1.30–31: 38% · ≥1.32: 25%; P(≥1.29) = 80%; P(Metaculus YES) = 64% | ↑ | **+13 pp** |
| **Markets unchanged** at Kalshi 63.6/64.0 and Polymarket 70.5% on the same rules (ties count) [15][16]. My market-definition number is now 80%, 10–16 pp above them. That gap requires humility. A plausible mispricing story: traders anchoring on the falling ERA5 dashboard. That is speculation. I shade halfway toward the markets: market-definition ≈ 75% | ↓ | **−5 pp** |
| Berkeley Earth July update (69%, published 2026-08-13; the commenter is "higher") [10] | → | 0 pp (already in v1) |
| **New forecast** | | **Median 59.0%, IQR [49.0%, 68.0%]** |

### Tripwire check

| Tripwire from v1 | Fired? | Note |
|---|---|---|
| GISTEMP September ≥ 1.45 (up) / ≤ 1.33 (down), by 10-20 | not yet | release ~10-14 |
| ERA5 October ≥ 0.85 (up) / ≤ 0.72 (down), by 11-10 | not yet | 1–2 Oct at 0.69; EC46 median 0.96 |
| Nov–Dec required mean > 1.55 after the October print | not yet | — |
| Metaculus or NASA statement on ties | not yet | comments relayed by the operator do not address ties |

### What resolves YES

unchanged from v1. Note the misconception in the relayed comments: neither the dashboard figure nor Berkeley Earth's is a NASA number. ERA5 is a **much harder** bar for 2026 than GISTEMP. 2026 so far trails 2024 by 0.10 °C in ERA5 (Jan–Sep 0.616 vs the 2024 annual 0.719), but by only 0.07 °C in GISTEMP (Jan–Aug 1.224 vs 1.29). So ERA5 needs Oct–Dec ≈ 1.02, while GISTEMP needs only the ERA5-equivalent of ≈ 0.86–0.90.

### Outside view

unchanged from v1

### Inside view

As v1, with the Oct–Dec input re-centred from 1.445 to **1.475 ± 0.07** (see Revision). Monte Carlo sensitivity at v2 settings: Oct–Dec 1.45 → 54%; 1.475 → 64%; 1.50 → 73%; dashboard-only 1.51 → 76%; September 1.37 instead of 1.40 → 60%. After the 5 pp shading toward the markets: **59%**.

### Evidence

v1 evidence stands, plus the dashboard data in the Revision table (raw CSVs snapshotted as `raw/climatebrink-*-2026-10-04.csv`). Absent: still no Metaculus admin ruling on ties.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP / Pro / gold | **not retrieved** | 2026-10-04 | 3rd attempt: HTTP 403 |
| Kalshi KXGTEMP-26 (LOTI > 1.28; ties count) | 63.6–64.0% | 2026-10-04 (re-fetched) | unchanged; 378,599 contracts [15] |
| Polymarket (GISS graph.txt; tie = rank 1) | 70.5% | 2026-10-04 (re-fetched) | unchanged [16] |
| Climate Brink dashboard, **ERA5** record probability | 20.6% | 2026-10-03 | peak ~90% around 09-08; different dataset [20] |
| Berkeley Earth (own dataset) | 69% | 2026-08-13 | [10] |
| Hausfather / Carbon Brief, GISTEMP | 65% | 2026-07-24 | ERA5 was 13% at the time [6] |

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | October rebound fails (ERA5 Oct ≤ 0.80), Oct–Dec ≤ 1.40 → ≤ 1.28 | 24% | NO (~1%) |
| 2 | Oct–Dec ~1.41–1.44 → exact 1.29 tie | 18% | ~55% |
| 3 | EC46-like rebound, Oct–Dec ~1.45–1.52 → 1.30–1.31 | 37% | ~80% |
| 4 | Dashboard-or-warmer, Oct–Dec ≥ 1.53 → ≥ 1.32 | 21% | ~97% |

Weighted ≈ 0.24·0.01 + 0.18·0.55 + 0.37·0.80 + 0.21·0.97 ≈ **0.60** (rounded to 59 with the market shading).

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Dashboard weight 50% | 100% (trust EC46 and the regression fully) / 0% (v1) | ~72% / ~52% |
| Tie mapping 0.55 / 0.80 | any nominal ≥ 1.29 counts as YES | ~76% |
| No market shading | — | ~64% |

### What would change my mind (tripwires)

- [ ] NASA GISTEMP September 2026 (release ~2026-10-14) ≥ 1.45 °C → up 8 pp; ≤ 1.33 °C → down 12 pp
- [ ] ERA5 October month-to-date (Climate Pulse CSV) through 10-15 averages ≤ 0.78 °C, i.e. the EC46 rebound is not materialising → down 10 pp
- [ ] Copernicus ERA5 October 2026 monthly anomaly (~2026-11-06) ≥ 0.90 °C → up 10 pp; ≤ 0.78 °C → down 15 pp
- [ ] After the GISTEMP October print, the Nov–Dec mean needed for a 2-dp 1.30 exceeds 1.55 °C → down ~30 pp
- [ ] Metaculus admin comment, or NASA wording, on tie treatment (by 2027-01-14) → re-analyse, ±15 pp

### Sources

Sources 1–19 as in v1; those re-used in this version are repeated, followed by the new ones:

1. NASA GISS, GISTEMP v4 monthly table — https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv (accessed 2026-10-04)
3. Copernicus Climate Pulse, ERA5 daily series — https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv (accessed 2026-10-04)
6. Carbon Brief, "State of the climate: Rapidly developing El Niño raises chance of record-warm 2026", 2026-07-24 — https://www.carbonbrief.org/state-of-the-climate-rapidly-developing-el-nino-raises-chance-of-record-warm-2026 (accessed 2026-10-04)
10. Berkeley Earth, "July 2026 Temperature Update", 2026-08-13 — https://berkeleyearth.org/july-2026-temperature-update/ (accessed 2026-10-04)
15. Kalshi API, KXGTEMP-26-P0 — https://api.elections.kalshi.com/trade-api/v2/markets/KXGTEMP-26-P0 (accessed 2026-10-04, re-fetched)
16. Polymarket, "Where will 2026 rank among the hottest years on record?" — https://polymarket.com/event/where-will-2026-rank-among-the-hottest-years-on-record (accessed 2026-10-04, re-fetched)
20. The Climate Brink climate dashboard (Z. Hausfather), "ERA5 · daily", rank probabilities regenerated 2026-10-03 — https://dashboard.theclimatebrink.com/assets/data/rank_probabilities.csv (accessed 2026-10-04; snapshot in `raw/`)
21. Same dashboard, annual prediction and projection history — https://dashboard.theclimatebrink.com/assets/data/projection_history.csv (accessed 2026-10-04; snapshot in `raw/`)
22. Same dashboard, October 2026 monthly projection (EC46 blend, init 2026-10-02) — https://dashboard.theclimatebrink.com/assets/data/monthly_projection.csv (accessed 2026-10-04; snapshot in `raw/`)
23. Metaculus community comments on post 21095, relayed by the operator — https://www.metaculus.com/questions/21095/ (accessed 2026-10-04, relayed by the operator)

**Date**: 2026-10-04
**Forecast**: Median 59.0%, IQR [49.0%, 68.0%]
**Thesis**: The relayed 85.5% → 37% → 20.6% figures come from Hausfather's ERA5 dashboard, not NASA. ERA5 is a much harder bar, and its late-September decline was already in v1. The genuinely new input is the dashboard's EC46 October forecast and Oct–Dec projection (ERA5 ≈ 0.97). Mapped to GISTEMP, that lifts the 2026 central estimate from 1.294 to ~1.30–1.31 °C. Blended 50/50 with v1, shaded toward unchanged markets (Kalshi 64%, Polymarket 70.5%), and with ~17% of the mass still an exact tie, the result is 59%.

---

## v1 — Initial forecast — 2026-10-04

### What resolves YES

The subquestion resolves YES if **NASA officially reports that 2026 is the hottest year on record to date**, otherwise NO. There is no fine print. The operative data is NASA GISS's GISTEMP v4 Land-Ocean Temperature Index (LOTI). NASA publishes it monthly, around the 10th–15th of the following month, and announces the annual result in mid-January, jointly with NOAA (2025's came on 2026-01-14 [13]). **The bar is 2024 at 1.29 °C** above 1951–1980 in the current table (2-decimal annual values [2]). 2023 = 1.17 and 2025 = 1.19. Edge cases matter more than usual here:

1. **Ties and "effectively tied".** NASA reports annual values to two decimals and labels small margins as ties. In January 2021 a nominally +0.01 °C year was announced as "2020 tied with 2016 for warmest year on record" [14]. In January 2026, 2025 (+0.02 vs 2023) was "effectively tied" [13]. In the current table 2016 and 2020 are both 1.01 [2]. With the 2026 central estimate *right on* 1.29, about 21% of the probability mass is an exact 2-decimal tie and about 35% is a +0.01/+0.02 "effectively tied" margin. How Metaculus resolves "tied for the warmest year" is **not specified**. I assume P(YES | exact tie) ≈ 55% and P(YES | +0.01–0.02) ≈ 80%.
2. **Market definitions differ.** Kalshi resolves YES on LOTI 2026 > 1.28 (so a 1.29 tie counts) [15]. Polymarket counts a tie as rank 1 [16]. Both are therefore *easier* than this question, by roughly 15–17 pp.
3. GISTEMP revises back-months by ±0.01–0.02 as late station data arrive. A revision of 2024 itself, or of Jan–Aug 2026, could flip a tie.
4. Institutional risk: GISS has been under budget and political pressure, and NASA's 2025 release omitted any mention of climate change [13]. A missing or late "official report" is possible but unlikely (≈3%). Metaculus would more likely wait or annul than resolve NO.

### Outside view

- **Record frequency.** In GISTEMP, about 30% of years in 1996–2025 were new records (1997, 1998, 2005, 2010, 2014, 2015, 2016, 2020-tie, 2023, 2024). That is the unconditional prior. It is nearly useless by October, when 8 of 12 months are known.
- **The relevant reference class is "strong El Niño onset years":** how much warmer is Sep–Dec than Jan–Aug in GISTEMP? 2026 needs Sep–Dec to average **≥ 1.41 °C** to reach 1.29 (a tie) and **≥ 1.44 °C** to reach 1.30. That is a jump of **+0.18 / +0.21 °C** over the Jan–Aug mean of 1.224 [1].

| Onset year | RONI JAS | Sep–Dec minus Jan–Aug (GISTEMP) |
|---|---|---|
| 1972 | 1.40 | +0.10 |
| 1982 (El Chichón) | 1.14 | +0.12 |
| 1997 | 1.84 | +0.19 |
| 2015 | 1.54 | +0.21 |
| 2023 | 0.79 | +0.34 |
| **2026** | **1.69** | needs +0.18 (tie) / +0.21 (record) |
| All years 1960–2025 | — | mean −0.01, sd 0.12 |

Of the four clean analogs (excluding the volcanic 1982), 3/4 reach the tie threshold and 2/4 the strict-record threshold. **Outside-view prior ≈ 50–60% for "tie or better", ≈ 40–50% for a strict 2-dp record.**

### Inside view

The arithmetic is closed-form: annual = (Jan–Aug sum 9.79 + Sep + Oct + Nov + Dec) / 12 [1].

- **Jan–Aug 2026 (GISTEMP):** 1.09, 1.25, 1.32, 1.17, 1.13, 1.18, 1.25, **1.40**. August is the warmest August in GISTEMP by 0.10 °C [1][12].
- **September 2026 (not yet published by NASA):** ERA5 (the European ECMWF reanalysis) September mean anomaly is 0.82 °C vs 1991–2020, the 2nd-warmest September after 2023 (0.93) [3][11]. Mapped with a GISTEMP-on-ERA5 regression (n = 320 months, residual sd 0.055, recent offset +0.02), that gives **Sep ≈ 1.40 ± 0.05**.
- **Oct–Dec:** global temperature lags Niño-3.4 by ~3 months, so Oct–Dec responds to the Jul–Sep Pacific state. That state is already observed: ONI (Oceanic Niño Index) JAS = 2.16, the highest JAS on record, and RONI (relative ONI) JAS = 1.69 [4]. Niño-3.4 was ~3.1 °C on 2026-09-21 and is forecast to peak around 4 °C in Nov [5][8]. Two estimates of Oct–Dec:
  - A regression of monthly GISTEMP on a quadratic trend plus RONI lagged 3 months (1980–2025, β = 0.073 °C per RONI unit), plus the persistent recent residual (+0.05 to +0.08), gives Oct/Nov/Dec ≈ 1.40/1.43/1.46, **mean ≈ 1.43**.
  - Anchoring on the Aug–Sep level (1.40) plus the typical strong-El-Niño Oct–Dec rise (1982 +0.16, 1997 +0.15, 2015 +0.28, 2023 +0.04, 1972 0.00) gives **≈ 1.47**.
  - Blend: **Oct–Dec ≈ 1.445 ± 0.065**.
- **Against:** ERA5 fell from ~0.88 in mid-September to 0.68–0.70 on 1–2 October [3], below the 0.86 Oct–Dec average that a record needs in ERA5 terms. Two days carry little weight across a 92-day window, but they argue against the warm (2023-style) branch.
- **Monte Carlo** (400k draws; Sep and Oct–Dec correlated; ±0.005 revision noise): annual 2026 = **1.294 ± 0.019 °C**. Bucket probabilities: ≤1.28: 32% · =1.29: 21% · 1.30–1.31: 35% · ≥1.32: 13%. **P(≥1.29, market definition) = 68%.** Mapping the buckets through the resolution-language assumptions gives **P(Metaculus YES) ≈ 51%**.

![2026 outcome buckets](charts/2026-outcome-buckets.png)

### Evidence

| Evidence | LR (likelihood ratio) | Note |
|---|---|---|
| August 2026 GISTEMP 1.40, a record August [1][12] | ~1.5 (up) | Carbon Brief's and Berkeley's July/Aug models expected roughly 1.30 |
| ERA5 September only 2nd-warmest, ~0.11 °C below Sep 2023 [3][11] | ~0.9 | in line with expectation, not a spike |
| ERA5 1–2 Oct dip to 0.68–0.70 [3] | ~0.9 | short-lived dips are common; 2024 started October at 0.70 and averaged 0.80 |
| Historic El Niño: RONI JAS 1.69, Niño-3.4 ~3.1 and rising, CPC >90% very strong [4][5][8] | already in the model | mostly a 2027 effect because of the lag |
| GISTEMP-specific odds from model-based forecasters: Hausfather 65% (data through June) [9], Berkeley Earth 69% for its own dataset (data through July) [10] | — | both count "nominal record". Closest to my 68% market-definition number |

**Absent evidence:** I found no Metaculus admin statement on tie handling (comments could not be fetched). That is the single largest unresolved definitional risk.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP / Pro / gold | **not retrieved** | 2026-10-04 | HTTP 403 ×2; bot API key hides aggregations; 116 forecasters on the group |
| Kalshi KXGTEMP-26 "2026 hottest year" | **63.6–64.0%** (bid/ask) | 2026-10-04 | 378,599 contracts traded; YES if LOTI > 1.28, **tie counts** [15] |
| Kalshi KXGTEMP-27 (mislabelled duplicate of the 2026 market) | 66–68% | 2026-10-04 | 26,728 contracts, thin [15] |
| Polymarket "2026 hottest year on record" | **70.5%** (bid 0.70 / ask 0.71) | 2026-10-04 | $667k volume on this leg, $3.58M on the event; resolves on GISS graph.txt No_Smoothing, **tie = YES** [16] |
| Manifold "Will 2026 be the hottest year on record?" | 77.3% | 2026-10-04 | 113 bettors, play money, resolution source not checked; discounted [17] |
| Hausfather / Carbon Brief, GISTEMP-specific | 65% | 2026-07-24 | data through June, before the August record [6][9] |
| Berkeley Earth (own dataset) | 69% | 2026-08-13 | data through July [10] |

**Reconciliation:** my market-definition probability (68%) sits inside the Kalshi–Polymarket band (64–71%). The 17 pp gap down to my Metaculus number is entirely the **tie and "effectively tied" discount**, not a different climate view. If you think Metaculus will resolve any nominal ≥1.29 as YES, my number becomes ~66%.

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | Oct–Dec ≤ 1.38 (October dip persists, El Niño's lagged effect arrives late) → 2026 ≤ 1.28 | 32% | NO (~1%) |
| 2 | Oct–Dec ~1.39–1.42 → exact tie at 1.29; NASA says "tied with 2024" | 21% | coin flip on admin reading (~55%) |
| 3 | Oct–Dec ~1.43–1.48 → 1.30–1.31; NASA "slightly warmer than 2024, effectively tied" or "warmest" | 35% | likely YES (~80%) |
| 4 | Oct–Dec ≥ 1.49 (2023-style late surge) → ≥ 1.32, clear record | 12% | YES (~97%) |

Weighted P(YES) = 0.32·0.01 + 0.21·0.55 + 0.35·0.80 + 0.12·0.97 ≈ **0.51**.

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Oct–Dec mean 1.445 | 1.43 (pure regression) / 1.50 (2023 analog) | 44% / 73% |
| Sep GISTEMP ≈ 1.40 | 1.36 | 45% |
| P(YES \| tie) 0.55, P(YES \| +0.01–0.02) 0.80 | admins resolve on any nominal ≥ 1.29 (both 1.0) | ~66% |
| Same | NASA's "tied" wording → NO; only ≥ +0.03 counts | ~16% |

Calibration checks: the would-I-take-either-side test holds at 51%. The number is not a round anchor. The IQR [43, 60] reflects that Sep/Oct prints alone can move it ±10 pp, and that resolution-language uncertainty cannot be resolved before January.

### What would change my mind (tripwires)

- [ ] NASA GISTEMP September 2026 (release ~2026-10-14) ≥ 1.45 °C → up 10 pp; ≤ 1.33 °C → down 10 pp
- [ ] Copernicus ERA5 October 2026 monthly anomaly (bulletin ~2026-11-06) ≥ 0.85 °C → up 12 pp; ≤ 0.72 °C → down 12 pp
- [ ] After the GISTEMP October print (~2026-11-15), the Nov–Dec mean needed for a 2-dp 1.30 exceeds 1.55 °C → down ~30 pp
- [ ] Metaculus admin comment, or NASA wording, on how a 2026-vs-2024 tie is treated (by 2027-01-14) → re-analyse; swings of ±15 pp are possible

### Sources

1. NASA GISS, GISTEMP v4 GLB.Ts+dSST monthly table — https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv (accessed 2026-10-04; snapshot in `raw/`)
2. NASA GISS, Global Land-Ocean annual means (graph.txt, No_Smoothing) — https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt (accessed 2026-10-04; snapshot in `raw/`)
3. Copernicus Climate Pulse, ERA5 daily global 2 m temperature series — https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv (accessed 2026-10-04; 2023–2026 excerpt in `raw/`)
4. NOAA CPC, RONI and ONI indices — https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt and https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt (accessed 2026-10-04)
5. NOAA CPC, ENSO Diagnostic Discussion, 2026-09-10 — https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml (accessed 2026-10-04)
6. Carbon Brief, "State of the climate: Rapidly developing El Niño raises chance of record-warm 2026", 2026-07-24 — https://www.carbonbrief.org/state-of-the-climate-rapidly-developing-el-nino-raises-chance-of-record-warm-2026 (accessed 2026-10-04)
7. Carbon Brief, "State of the climate: Strong El Niño puts 2026 on track for second-warmest year", 2026-04-21 — https://www.carbonbrief.org/state-of-the-climate-strong-el-nino-puts-2026-on-track-for-second-warmest-year/ (accessed 2026-10-04)
8. Carbon Brief, "Analysis: 'Super El Niño' breaks 'remarkable' all-time record", 2026-09-21 — https://www.carbonbrief.org/analysis-super-el-nino-reaches-remarkable-all-time-record (accessed 2026-10-04)
9. Z. Hausfather, "Why Hansen may end up being right about 2026" (Skeptical Science repost of The Climate Brink), 2026-08-03 — https://skepticalscience.com/print.php?n=6585 (accessed 2026-10-04)
10. Berkeley Earth, "July 2026 Temperature Update", 2026-08-13 — https://berkeleyearth.org/?p=9536 (accessed 2026-10-04)
11. Fox Weather, "After the hottest summer on record, where will September rank in the history books?", 2026-09-24 — https://www.foxweather.com/weather-news/after-hottest-summer-record-how-september-rank-history-books-heat (accessed 2026-10-04)
12. Copernicus C3S, August 2026 bulletin (joint-hottest month on record) — https://climate.copernicus.eu/copernicus-august-was-worlds-joint-hottest-month-record-pushing-global-temperatures-back-above (accessed 2026-10-04)
13. NASA, "NASA Releases Global Temperature Data" (2025 annual), 2026-01-14 — https://www.nasa.gov/news-release/nasa-releases-global-temperature-data (accessed 2026-10-04)
14. NASA SVS, "NASA Finds 2020 Tied for Hottest Year on Record" — https://svs.gsfc.nasa.gov/vis/a010000/a013700/a013799/script_30722_00.html (accessed 2026-10-04)
15. Kalshi API, markets KXGTEMP-26-P0 and KXGTEMP-27-P0 — https://api.elections.kalshi.com/trade-api/v2/markets/KXGTEMP-26-P0 (accessed 2026-10-04; snapshot in `raw/`)
16. Polymarket, "Where will 2026 rank among the hottest years on record?" — https://polymarket.com/event/where-will-2026-rank-among-the-hottest-years-on-record (via gamma API, accessed 2026-10-04; snapshot in `raw/`)
17. Manifold, "Will 2026 be the hottest year on record?" — https://manifold.markets/itsTomekK/will-2026-be-the-hottest-year-on-re (accessed 2026-10-04)
18. WMO, Global Annual to Decadal Climate Update 2026–2030, 2026-05-28 — https://wmo.int/media/news/new-report-suggests-more-global-temperature-records-ahead (accessed 2026-10-04)
19. Metaculus API, post 21095 metadata (bot key; no aggregations) — https://www.metaculus.com/questions/21095/ (accessed 2026-10-04; snapshot in `raw/`)

**Date**: 2026-10-04
**Forecast**: Median 51.0%, IQR [43.0%, 60.0%]
**Thesis**: GISTEMP Jan–Aug 2026 averages 1.224 °C. With September ≈ 1.40 (ERA5-mapped) and a lagged historic El Niño pushing Oct–Dec to ≈ 1.445, 2026 lands at 1.294 ± 0.019 °C, right on 2024's 1.29. That is 68% for "≥ 1.29", matching Kalshi (64%) and Polymarket (70.5%), whose rules count ties. About 56% of the mass is a tie or "effectively tied" margin, which NASA has historically announced as "tied" (2020 vs 2016), so the Metaculus-specific probability is about 51%.
