# Will 2027 be the warmest year on record, according to NASA?

| | |
|---|---|
| **Source** | Metaculus #21095 (question group), subquestion id **45424** (label "2027", added 2026-08-18) — https://www.metaculus.com/questions/21095/will-the-following-years-be-the-warmest-year-on-record-according-to-nasa/ |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-08-18 / 2028-01-01 / 2028-01-15 (NASA's annual announcement, mid-January) |
| **Status** | open |
| **Current forecast** | **Median 89.0%, IQR [84.0%, 93.0%]** (v1, 2026-10-04) |
| **Community (as of 2026-10-04)** | **not retrieved**: Metaculus returned HTTP 403 to the aggregations fetcher twice; the bot API key hides aggregations |
| **Next review** | 2026-11-04 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-04

### What resolves YES

YES if **NASA officially reports 2027 as the hottest year on record to date** in GISTEMP v4 LOTI, the annual figure announced around mid-January 2028. 2027 must beat **every earlier year, 2026 included**. The bar today is 2024 at 1.29 °C (1951–1980 base). 2026 is tracking 1.29 ± 0.02, so the effective bar is max(1.29, 2026) ≈ 1.30. NASA announces small margins (≤ 0.02 °C) as "tied" (2020 vs 2016) or "effectively tied" (2025 vs 2023). Resolution of a tie is unspecified; see the [2026 sibling](../2026-10-04-mc21095-nasa-warmest-year-on-record-2026/forecast.md). At the margins expected for 2027 (~+0.10) this matters only in the tail.

### Outside view

- **Year after a strong El Niño onset year, GISTEMP:** 1998 (after 1997) record by +0.14; 2016 (after 2015) record by +0.11; 2024 (after 2023) record by +0.12. 1983 (after 1982) rose, but El Chichón's aerosols muddy it. **3/3 clean analogs set a record**, by +0.11 to +0.15 °C over the onset year.
- Unconditional GISTEMP record frequency 1996–2025 is about 30%. That figure is irrelevant once the ENSO phase is known.
- **Prior: ~85–92%.** With n = 3, the analogs alone cannot support more than ~90%.

### Inside view

- **El Niño:** Niño-3.4 was ~3.1 °C on 2026-09-21. Models put the peak around 4.1 °C in about November 2026, beyond the 2015–16 record [3][4]. CPC gives >90% for a very strong event through winter 2026–27 [3]. Global temperature lags Niño-3.4 by ~3–4 months, so the peak global response falls in **Jan–Apr 2027**. Super El Niños typically decay into neutral or La Niña by mid-following-year. The late-2027 La Niña costs little, because its own lag pushes most of its effect into 2028.
- **Annual Monte Carlo** (300k draws): T = level(2026, ENSO-adjusted) + trend × years + β·RONI(lag 3, annual mean) + AR(1) noise + volcanic shocks + a solar-cycle decline. Assumptions: trend 0.032 ± 0.007 °C/yr (IGCC 2025 puts human-induced warming at 0.27 [0.2–0.4] °C/decade [6]); β = 0.09; RONI_2027 ~ N(1.1, 0.35); 2%/yr chance of a 0.1–0.35 °C volcanic hit; noise sd 0.055.
  - Result: **2027 median 1.40 °C**; P(2027 beats max(2024, 2026) at 2 dp) = 92%; mapped through the tie language, **P(YES) ≈ 90%**.
  - Variants: slow trend 88%, fast trend 91%, β = 0.07 86%, β = 0.12 92%, early El Niño collapse (RONI_2027 = 0.7) 80%, noise sd 0.075 85%.
- **Residual risks:** a Pinatubo-class eruption before mid-2027 (~1.5%) would end it. An unusually hot late 2026 (2026 ≥ 1.33) raises the bar. NASA could fail to publish (~2%).

### Evidence

- Carbon Brief (2026-07-24): 2027 central estimate ~1.71 °C above pre-industrial (90% range 1.49–1.93) and a 92% chance of a new record across datasets [1].
- Hausfather (2026-08-03): 91% that 2027 sets a record [2].
- WMO decadal update (2026-05-28): 86% that at least one year in 2026–2030 beats 2024. It names 2027 as the likely record year because of the El Niño [5].
- Berkeley Earth (2026-08-13) expects "a strong chance of a further record" in 2027 [7].
- Since those July–August numbers, the El Niño has strengthened beyond the median forecasts [4]: LR ≈ 1.2 in favour.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP / Pro / gold | **not retrieved** | 2026-10-04 | HTTP 403 ×2; bot key hides aggregations |
| Carbon Brief (Hausfather), multi-dataset | 92% | 2026-07-24 | not GISTEMP-specific [1] |
| Hausfather (The Climate Brink) | 91% | 2026-08-03 | [2] |
| WMO / Met Office decadal | 86% that *any* year 2026–30 beats 2024 | 2026-05-28 | upper bound on "2027 specifically" when made; El Niño forecasts have strengthened since [5] |
| Kalshi / Polymarket 2027 market | none found | 2026-10-04 | Kalshi's KXGTEMP-27 ticker is a mislabelled duplicate of the 2026 market |

I sit slightly below the 91–92% model-based numbers. The reasons are this question's stricter definition (GISTEMP only, NASA wording, ties) and the extra bar from a possibly record-level 2026.

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | El Niño peaks Nov–Jan as forecast and decays by mid-2027; 2027 ≈ 1.38–1.45 | 70% | YES (~97%) |
| 2 | Peak extends into spring 2027, slow decay; 2027 ≥ 1.45 | 15% | YES (~99%) |
| 3 | Early collapse into La Niña by MJJ 2027 and/or very hot late 2026 (≥ 1.33) narrows the margin to ≤ 0.03 | 12% | coin flip to likely (~55%) |
| 4 | Pinatubo-class eruption, or NASA does not publish | 3% | NO (~5%) |

Weighted ≈ 0.70·0.97 + 0.15·0.99 + 0.12·0.55 + 0.03·0.05 ≈ **0.89**.

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| RONI_2027 (lagged annual mean) ≈ 1.1 | 0.7 (fast decay) | ~80% |
| ENSO coefficient β = 0.09 | 0.07 | ~86% |
| No large eruption (~1.5%/yr) | Pinatubo-class eruption by mid-2027 | ~45% |

### What would change my mind (tripwires)

- [ ] Stratospheric eruption injecting ≥ 10 Tg SO2 before 2027-09-30 → down ~40 pp
- [ ] NASA's annual 2026 value (~2027-01-14) ≥ 1.33 °C → down 4 pp
- [ ] GISTEMP Jan–Mar 2027 mean ≥ 1.50 °C → up 5 pp; ≤ 1.36 °C → down 15 pp (by 2027-04-20)
- [ ] CPC shows El Niño ended by AMJ 2027 with La Niña favoured (≥ 50%) for JAS 2027 → down 4 pp (by 2027-05-15)

### Sources

1. Carbon Brief, "State of the climate: Rapidly developing El Niño raises chance of record-warm 2026", 2026-07-24 — https://www.carbonbrief.org/state-of-the-climate-rapidly-developing-el-nino-raises-chance-of-record-warm-2026 (accessed 2026-10-04)
2. Z. Hausfather, "Why Hansen may end up being right about 2026" (Skeptical Science repost), 2026-08-03 — https://skepticalscience.com/print.php?n=6585 (accessed 2026-10-04)
3. NOAA CPC, ENSO Diagnostic Discussion, 2026-09-10 — https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml (accessed 2026-10-04)
4. Carbon Brief, "Analysis: 'Super El Niño' breaks 'remarkable' all-time record", 2026-09-21 — https://www.carbonbrief.org/analysis-super-el-nino-reaches-remarkable-all-time-record (accessed 2026-10-04)
5. WMO, Global Annual to Decadal Climate Update 2026–2030, 2026-05-28 — https://wmo.int/media/news/new-report-suggests-more-global-temperature-records-ahead (accessed 2026-10-04)
6. Forster et al., "Indicators of Global Climate Change 2025" (ESSD) — https://research.wur.nl/en/publications/indicators-of-global-climate-change-2025-annual-update-of-key-ind (accessed 2026-10-04)
7. Berkeley Earth, "July 2026 Temperature Update", 2026-08-13 — https://berkeleyearth.org/?p=9536 (accessed 2026-10-04)
8. NASA GISS, GISTEMP v4 annual and monthly tables — https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv (accessed 2026-10-04)
9. NOAA CPC, RONI index — https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt (accessed 2026-10-04; snapshot in `raw/`)
10. Kalshi API, KXGTEMP-27-P0 (mislabelled 2026 duplicate) — https://api.elections.kalshi.com/trade-api/v2/events/KXGTEMP-27 (accessed 2026-10-04)

**Date**: 2026-10-04
**Forecast**: Median 89.0%, IQR [84.0%, 93.0%]
**Thesis**: A record El Niño (Niño-3.4 ~3.1 °C and heading for ~4 °C in November, CPC >90% very strong) peaks just before 2027. GISTEMP's lagged response puts 2027 near 1.40 °C against a bar of about 1.30, and every clean analog year after a strong onset year (1998, 2016, 2024) set a record. Residual risks are an early collapse into La Niña, a Pinatubo-class eruption, an unusually hot 2026 raising the bar, and NASA's "tied" wording at small margins.
