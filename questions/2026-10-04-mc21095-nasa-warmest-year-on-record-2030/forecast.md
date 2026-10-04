# Will 2030 be the warmest year on record, according to NASA?

| | |
|---|---|
| **Source** | Metaculus #21095 (question group), subquestion id **21099** (label "2030") — https://www.metaculus.com/questions/21095/will-the-following-years-be-the-warmest-year-on-record-according-to-nasa/ |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2024-01-25 / 2031-01-01 / 2031-01-15 (NASA's annual announcement, mid-January) |
| **Status** | open |
| **Current forecast** | **Median 27.0%, IQR [19.0%, 34.0%]** (v1, 2026-10-04) |
| **Community (as of 2026-10-04)** | **not retrieved**: Metaculus returned HTTP 403 to the aggregations fetcher twice; the bot API key hides aggregations |
| **Next review** | 2027-01-20 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-04

### What resolves YES

YES if **NASA officially reports 2030 as the hottest year on record to date** (GISTEMP v4 LOTI, announced around mid-January 2031). 2030 must beat **every year through 2029**, which almost certainly includes the 2027 super-El-Niño year (expected ~1.40 °C on the 1951–1980 base; see the [2027 sibling](../2026-10-04-mc21095-nasa-warmest-year-on-record-2027/forecast.md)), and possibly 2028/2029. NASA announces margins of ≤ 0.02 °C as "tied"/"effectively tied"; resolution of a tie is unspecified (assumed ~55–80% YES, as in the [2026 sibling](../2026-10-04-mc21095-nasa-warmest-year-on-record-2026/forecast.md)).

### Outside view

- **Unconditional:** about 30% of GISTEMP years in 1996–2025 were records [1]. Under an accelerating trend that rate should rise, not fall.
- **Conditional, three years after a super-El-Niño peak year:** 2001 after 1998 (0.54 vs 0.61, no) and 2019 after 2016 (0.98 vs 1.01, no). In 1998 → 2005 the record stood for 7 years; in 2016 → 2020 it stood for 4 years (to a tie) and 7 years (to 2023). n = 2, 0/2. That suggests **~15–25%**, adjusted up for faster warming now.
- **Trend vs ENSO arithmetic:** at ~0.03 °C/yr, three years of trend (2027 → 2030) add ≈ +0.09–0.10 °C. That is about the size of the ENSO boost 2027 is expected to carry above its trend line. So 2030 needs at least a neutral-to-warm ENSO state to clear 2027, and must also beat 2028–29.

### Inside view

- **Annual Monte Carlo** (300k draws; the same model as the 2027 sibling): level from the 2026 nowcast; trend 0.032 ± 0.007 °C/yr; β = 0.09 per unit of lagged annual RONI. RONI_2028 ~ N(−0.5, 0.6) (post-super-El-Niño La Niña tendency); RONI_2029/2030 ~ AR(0.2) with sd 0.75; AR(1) noise sd 0.055; 2%/yr volcanic risk; solar cycle 25 declining toward its ~2030 minimum (−0.012 °C/yr from 2026).
  - Result: **2030 median ≈ 1.36 °C vs 2027 ≈ 1.40**, and **P(record) ≈ 26%**.
  - Variants: slow trend (0.022/yr) 19%, fast trend (0.040/yr) 32%, no solar decline 36%, early 2027 El Niño collapse 33%, β = 0.12 22%.
- **Arguments for higher:** warming may be accelerating beyond 0.03 °C/yr (Hansen's aerosol-reduction thesis; IGCC 2025 puts the human-induced rate at 0.27 [0.2–0.4] °C/decade, so the upper end is plausible [2]). The WMO decadal ensemble range for 2026–2030 reaches 1.9 °C above pre-industrial [3]. And ENSO in 2029–30 is a coin toss that will not be known until ~mid-2030 (speculative: El Niño recurrence intervals of 2–7 years make a 2029–30 event plausible after a 2026–27 one).
- **Arguments for lower:** the solar-cycle minimum around 2030 is worth ~−0.03 to −0.05 °C relative to the 2024–26 maximum (an assumption; magnitude uncertain). The 2027 bar may be very high (≥ 1.45). And 2028 or 2029 could set records themselves.

### Evidence

- WMO (2026-05-28): 86% that at least one year in 2026–2030 beats 2024, driven mainly by 2027 [3]. That is consistent with my 2027 = 89% and leaves little information about 2030 specifically.
- No public forecast specifically for 2030 as a record year was found beyond Manifold.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP / Pro / gold | **not retrieved** | 2026-10-04 | HTTP 403 ×2; bot key hides aggregations |
| Manifold "Will 2030 be the warmest year on record?" | 33% | 2026-10-04 | 23 bettors, play money, resolution dataset unverified; discounted [4] |
| WMO decadal (any year 2026–30 > 2024) | 86% | 2026-05-28 | not specific to 2030 [3] |

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | El Niño develops in 2029–30 (lagged ENSO positive in 2030) | 25% | ~60% record |
| 2 | ENSO-neutral 2030 | 45% | ~22% record |
| 3 | La Niña-influenced 2030, or a large volcanic eruption in 2029–30 | 30% | ~8% record |

Weighted ≈ 0.25·0.60 + 0.45·0.22 + 0.30·0.08 ≈ **0.27**.

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Trend 0.032 °C/yr | 0.040 (Hansen-style acceleration) / 0.022 | ~32% / ~19% |
| Solar decline −0.012 °C/yr to 2030 | no solar effect | ~36% |
| 2027 ≈ 1.40 | 2027 ≥ 1.48 | ~18% |

### What would change my mind (tripwires)

- [ ] NASA's 2027 annual value (~2028-01-15) ≥ 1.48 °C → down 8 pp; ≤ 1.38 °C → up 8 pp
- [ ] 2028 or 2029 sets a new GISTEMP record (raises the bar) → down 8 pp
- [ ] CPC June 2030 outlook ≥ 60% El Niño for SON 2030 → up 15 pp; La Niña persisting through 2030 → down 12 pp
- [ ] Stratospheric eruption ≥ 10 Tg SO2 between 2029-07-01 and 2030-09-30 → down 20 pp

### Sources

1. NASA GISS, GISTEMP v4 annual table (graph.txt) — https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt (accessed 2026-10-04)
2. Forster et al., "Indicators of Global Climate Change 2025" (ESSD) — https://research.wur.nl/en/publications/indicators-of-global-climate-change-2025-annual-update-of-key-ind (accessed 2026-10-04)
3. WMO, Global Annual to Decadal Climate Update 2026–2030, 2026-05-28 — https://wmo.int/media/news/new-report-suggests-more-global-temperature-records-ahead (accessed 2026-10-04)
4. Manifold, "Will 2030 be the warmest year on record?" — https://manifold.markets/itsTomekK/will-2030-be-the-hottest-year-on-re (accessed 2026-10-04)
5. NOAA CPC, RONI index — https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt (accessed 2026-10-04; snapshot in `raw/`)
6. Carbon Brief, "State of the climate: Rapidly developing El Niño raises chance of record-warm 2026", 2026-07-24 — https://www.carbonbrief.org/state-of-the-climate-rapidly-developing-el-nino-raises-chance-of-record-warm-2026 (accessed 2026-10-04) — 2027 central estimate (the bar 2030 must clear)
7. Carbon Brief, "Analysis: 'Super El Niño' breaks 'remarkable' all-time record", 2026-09-21 — https://www.carbonbrief.org/analysis-super-el-nino-reaches-remarkable-all-time-record (accessed 2026-10-04)
8. NOAA CPC, ENSO Diagnostic Discussion, 2026-09-10 — https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml (accessed 2026-10-04)
9. Z. Hausfather, "Why Hansen may end up being right about 2026" (Skeptical Science repost), 2026-08-03 — https://skepticalscience.com/print.php?n=6585 (accessed 2026-10-04) — Hansen acceleration thesis, 2027 at 91%
10. NASA GISS, GISTEMP v4 monthly table — https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv (accessed 2026-10-04)
11. NASA, "NASA Releases Global Temperature Data" (2025 annual, "effectively tied" wording), 2026-01-14 — https://www.nasa.gov/news-release/nasa-releases-global-temperature-data (accessed 2026-10-04)
12. NASA SVS, "NASA Finds 2020 Tied for Hottest Year on Record" — https://svs.gsfc.nasa.gov/vis/a010000/a013700/a013799/script_30722_00.html (accessed 2026-10-04)
13. Berkeley Earth, "July 2026 Temperature Update", 2026-08-13 — https://berkeleyearth.org/?p=9536 (accessed 2026-10-04)

**Date**: 2026-10-04
**Forecast**: Median 27.0%, IQR [19.0%, 34.0%]
**Thesis**: 2030 must clear the 2027 super-El-Niño year (~1.40 °C). Three years of ~0.03 °C/yr trend roughly cancel 2027's ENSO boost, so the outcome hinges on ENSO in 2029–30 and on whether 2028–29 set records first. After the last two super El Niños, the year three years later was not a record (2001, 2019). An annual trend+ENSO+noise simulation gives ~26%, slightly below Manifold's thin 33%; faster-than-expected warming is the main upside risk.
