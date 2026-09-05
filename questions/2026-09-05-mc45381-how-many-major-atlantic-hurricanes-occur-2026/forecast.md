# How many Major Atlantic Hurricanes will occur in the 2026 Atlantic hurricane season?

| | |
|---|---|
| **Source** | Metaculus #45381 — https://www.metaculus.com/questions/45381/ |
| **Type** | multiple choice — options `0`, `1`, `2`, `3`, `4+` |
| **Opened / Closes / Resolves** | 2026-09-07 / 2026-10-16 / 2026-11-30 (NHC data as of 2026-12-01) |
| **Status** | open |
| **Current forecast** | **0: 47.0% · 1: 31.0% · 2: 15.0% · 3: 5.0% · 4+: 2.0%** — leading option `0`, IQR [40.0%, 54.0%] (v1, 2026-09-05) |
| **Community (as of 2026-09-05)** | **not yet revealed** — status `upcoming`, CP reveal 2026-09-10T17:00Z (n=20 forecasters already in) |
| **Next review** | 2026-09-19 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-09-05

### What resolves YES (which option)

The number of **major hurricanes** — Category 3 or higher on the Saffir–Simpson scale, sustained
winds ≥ 111 mph / 178 km/h — occurring in the Atlantic basin between **1 June and 30 November 2026
inclusive**, as reported by the **National Hurricane Center on 1 December 2026**. Buckets are
`0`, `1`, `2`, `3`, `4+`; an admin confirmed in comments on 2026-09-05 that they are exhaustive
and that **4+ includes exactly 4**.

Two details in the fine print do real work:

- **The 1 December operational count governs.** "Any subsequent revisions upgrading or downgrading
  a storm's intensity will not be considered." Post-season Tropical Cyclone Reports, published
  months later, historically upgrade more storms to major status than they downgrade — especially
  systems never sampled by reconnaissance aircraft. This is a small but real **downward** bias on
  the resolving number relative to the eventual best-track.
- Named cross-reference sources are the NHC Advisory Archive and the Monthly Atlantic Tropical
  Weather Summary, the December issue of which covers November.

### Outside view

Unconditionally, the 1991–2020 normal is **3.2 major hurricanes**, and only **5 of 60** seasons
since 1966 (1968, 1972, 1986, 1994, 2013) finished with zero — a base rate of **8%**. That is the
wrong anchor here, because the season is already three months old and has produced nothing.

| Class | n | Members (major-hurricane count) | Mean |
|---|---|---|---|
| **A — no hurricane by 5 September** (satellite era) | 4 | 2001: **4** · 2002: **2** · 1984: **1** · 2013: **0** | 1.75 |
| **B — strong El Niño, ONI ≥ ~1.5 in ASO** | 7 | 1972: 0 · 1982: 1 · 1987: 1 · 1991: 2 · 1997: 1 · 2015: 2 · 2023: 3 | 1.43 |
| **C — seasons with total ACE 30–60** | ~10 | 1968:0 · 1972:0 · 1986:0 · 1994:0 · 2013:0 · 1987:1 · 1993:1 · 1997:1 · 1991:2 · 2009:2 | ~0.7 |

Classes A and B both pull **upward**, and both are contaminated in the same way: **every one of
the seven strong-El-Niño years already had a hurricane by 5 September**, most of them a major
(Bob Cat 3 on 19 Aug 1991; Danny Cat 3 on 21 Aug 2015; three majors by 5 Sep 2023). And none of
the four members of class A had an El Niño of this strength — 2001, the 4-major case, was a
favourable-basin year that then produced Erin, Felix, Iris and Michelle. 2026 is more suppressed
than every member of both classes. **Class C**, matched to where the ACE trajectory is actually
heading, is the honest anchor at ~0.7.

### Inside view

**Where the season actually stands on 2026-09-05:**

| Metric | 2026 to date | Full-season normal |
|---|---|---|
| Named storms | **5** — Arthur (45 mph), Bertha (60), Cristobal (45), Dolly (40), Edouard (60) | 14 |
| Hurricanes | **0** | 7 |
| Major hurricanes | **0** | 3.2 |
| ACE | **≈ 4.4** (3.6% of a normal season) | ≈ 123 |

Nothing has come within 15 mph of hurricane strength all year. Two facts make this extreme rather
than merely quiet:

1. **The satellite-era record for the latest first Atlantic hurricane is 11 September**, set twice
   — Gustav (2002) and Humberto (2013). 2026 is days from breaking it, and US outlets are openly
   asking whether the basin could finish with *zero* hurricanes.
2. **NHC's Tropical Weather Outlook of 4 September 2026 forecasts no tropical cyclone formation
   anywhere in the Atlantic, Caribbean or Gulf for the following seven days** — straight through
   the 10 September climatological peak. The record will therefore almost certainly fall, and the
   effective remaining window starts around **12 September**.

**Rate construction.** Climatologically ~55% of a season's major hurricanes form after 12
September → 1.8 majors on a normal season. CSU's final August call was ACE and NTC at **40–45% of
normal**; since that figure already banks a near-zero first half, the implied remainder multiplier
is somewhat higher, but the season is running at ~13% of normal ACE pace and El Niño is
*intensifying*, so it should not be marked up much. Take 0.42.

`λ ≈ 1.8 × 0.42 ≈ 0.76`, widened to **λ ≈ 0.85** for the western-Caribbean October window, which
has delivered majors even under El Niño — Lili (Cat 4, 3 Oct 2002) and Joaquin (Cat 4, late
Sep–Oct 2015) are the proof that a single favourable synoptic window is enough.

Poisson(0.85) gives 0: 42.7% · 1: 36.3% · 2: 15.4% · 3: 4.4% · 4+: 1.2%. Major-hurricane counts
are over-dispersed relative to Poisson — one favourable window can produce two or three — so mass
moves from the centre to both tails; and the fine print's operational-count rule shifts a little
more onto the low side.

**Final distribution: 0 = 47.0% · 1 = 31.0% · 2 = 15.0% · 3 = 5.0% · 4+ = 2.0%** (mean 0.85).

![Forecast distribution over major-hurricane counts, with NOAA's August 2026 outlook range shaded](charts/major_hurricane_distribution.png)

### Evidence

Every seasonal forecaster has revised **down**, monotonically, all year:

| Forecaster | Issued | Named | Hurricanes | **Majors** | ACE |
|---|---|---|---|---|---|
| Tropical Storm Risk | Dec 2025 | 14 | 7 | 3 | 125 |
| NOAA CPC | 2026-05-21 | 8–14 | 3–6 | 1–3 | — |
| UK Met Office | 2026-05-28 | 9 | 5 | 2 | 72 |
| CSU | 2026-06-10 | 11 | 5 | 2 | — |
| **CSU (final)** | **2026-08-05** | **9** | **4** | **1** | **40–45% of normal** |
| **NOAA CPC (Aug update)** | **2026-08-06** | **7–13** | **2–6** | **0–2** (70% conf.) | 30–90% of median |

NOAA also raised P(below-normal season) from 55% to **75%**. Crucially, **both August forecasts
were issued when only two named storms had formed**; three more have since formed and every one
failed to reach hurricane strength. A month of pure downside news is not yet in those numbers.

**What would have to be true for me to be wrong on the high side**, and whether I see it: the 2023
escape hatch — record Atlantic SSTs overwhelming El Niño shear — is not available, because NOAA
describes 2026 Atlantic SSTs as only *slightly* above normal, not record-breaking. I looked for it
specifically and it is absent. Absence of expected evidence: if the basin were about to turn, I
would expect NHC to be flagging African-wave activity in the first week of September; instead it
flags nothing for seven days (LR ≈ 0.5 against the higher counts).

**What keeps me off zero as a modal certainty**: class A shows that a record-late first hurricane
does **not** imply a dead season. 2002's first hurricane came on 11 September and the season still
produced Isidore (Cat 3) and Lili (Cat 4). Late-season western-Caribbean development is the
mechanism, and it is exactly what a suppressed main-development-region season leaves behind. That
is why P(1) is still 31% and P(2) is a non-trivial 15%.

**A misconception worth naming.** "Zero hurricanes so far" and "zero major hurricanes" are being
conflated in coverage. The question asks only about Category 3+. A season can produce four
Category 1–2 hurricanes in October and still resolve `0` — and given a shear-dominated basin,
weak, short-lived hurricanes are exactly the most likely form of any late activity. The `0` bucket
is therefore fatter than the "will there be any hurricane at all?" framing suggests.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | **not revealed** | 2026-09-05 | status `upcoming`; CP reveal 2026-09-10T17:00Z; 20 forecasters already submitted |
| Metaculus Pro | not revealed | 2026-09-05 | same |
| Metaculus gold medalists | not revealed | 2026-09-05 | same |
| **NOAA CPC** | 0–2 majors, 70% confidence; P(below normal) 75% | 2026-08-06 | official; the closest thing to a market on this question |
| **CSU (Klotzbach et al.)** | **1** major; ACE/NTC 40–45% of normal | 2026-08-05 | best-track-record academic forecaster |
| UK Met Office | 2 majors, ACE 72 | 2026-05-28 | stale — pre-dates the El Niño confirmation |
| Tropical Storm Risk | 3 majors, ACE 125 | Dec 2025 | badly stale; ignore |
| Polymarket / Kalshi / Manifold | **no market found** | 2026-09-05 | searched |

**Cohort disagreement**: not assessable — all three Metaculus cohorts are hidden until 2026-09-10.
My distribution is a shade more pessimistic than CSU's point forecast of 1 (my mean is 0.85), which
is justified by a further month of nothing since 5 August, and it sits comfortably inside NOAA's
0–2 band (I give that band 93%).

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | **Shear wins outright.** El Niño peaks strong through October; the first hurricane forms mid-to-late September or later and stays Cat 1–2; the October Caribbean window never opens. | 0.47 | **0** |
| 2 | **One window opens.** A single low-shear western-Caribbean or Bahamas period in late September or October produces one Cat 3+ system. | 0.31 | **1** |
| 3 | **Two windows, or one storm plus a late-October Caribbean major** (the 2002 Isidore/Lili shape). | 0.15 | **2** |
| 4 | **Basin recovers.** El Niño stalls, MJO delivers a sustained favourable phase, and the season back-loads hard. | 0.05 | **3** |
| 5 | **2001 repeat** — record-late start followed by a genuinely active October–November. | 0.02 | **4+** |

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Remaining-season activity ≈ 42% of normal (λ ≈ 0.85) | El Niño weakens and the remainder runs at ~70% of normal (λ ≈ 1.3) | 0: 30% · 1: 33% · 2: 22% · 3: 10% · 4+: 5% |
| Remaining-season activity ≈ 42% of normal | Shear stays hostile through November (λ ≈ 0.45) | 0: 62% · 1: 27% · 2: 8% · 3: 2.5% · 4+: 0.5% |
| First hurricane forms ~12–20 September | No hurricane at all forms before 1 October | 0: ~70% · 1: ~22% · 2: ~6% · 3+: ~2% |
| The operational 1 December count governs | Final best-track governed (it does not) | shift ~2 pp from `0`/`1` upward |

### What would change my mind (tripwires)

- [ ] **First Atlantic hurricane of 2026 forms** — by 2026-09-30 → shifts ~8 pp from `0` to `1`/`2`; if it forms after 2026-09-30, shift ~12 pp *onto* `0`
- [ ] **Any Atlantic system reaches Category 3** — by 2026-11-30 → `0` collapses to ~0%; mass moves to `1`/`2`
- [ ] **NHC Tropical Weather Outlook flags a ≥ 60% 7-day formation chance in the western Caribbean** — by 2026-10-31 → up ~6 pp on `1`+`2`, down on `0`
- [ ] **CPC ONI update shows El Niño peaking or weakening earlier than forecast** (ASO/SON value below +1.5) — by 2026-10-15 → up ~7 pp on `2`+`3`
- [ ] **2026-10-15 passes with still zero hurricanes** → `0` rises to ~72%
- [ ] **CSU or NOAA issue any further downward revision** — by 2026-10-16 (question close) → up ~4 pp on `0`
- [ ] **Metaculus CP on reveal (2026-09-10) puts `0` below 30% or above 62%** → direction unknown; trigger a re-analysis rather than a nudge

### Sources

1. Metaculus — question #45381, resolution criteria, fine print, background, comments — https://www.metaculus.com/questions/45381/ ; snapshot in `raw/metaculus-2026-09-05.json` (accessed 2026-09-05)
2. Wikipedia — "2026 Atlantic hurricane season" — https://en.wikipedia.org/wiki/2026_Atlantic_hurricane_season (accessed 2026-09-05)
3. NOAA National Hurricane Center — Graphical Tropical Weather Outlook, dated 2026-09-04 — https://www.nhc.noaa.gov/gtwo.php (accessed 2026-09-05)
4. NOAA — "NOAA maintains prediction for below-normal Atlantic hurricane season" (August update, 2026-08-06) — https://www.noaa.gov/news-release/noaa-maintains-prediction-for-below-normal-atlantic-hurricane-season (accessed 2026-09-05)
5. NOAA CPC — 2026 Atlantic Hurricane Season Outlook — https://www.cpc.ncep.noaa.gov/products/outlooks/hurricane.shtml (accessed 2026-09-05)
6. NOAA — "NOAA predicts below-normal 2026 Atlantic hurricane season" (May outlook) — https://www.noaa.gov/news-release/noaa-predicts-below-normal-2026-atlantic-hurricane-season (accessed 2026-09-05)
7. Colorado State University (Klotzbach et al.) — "Forecast of Atlantic Hurricane Activity for 2026", August 2026 — https://tropical.colostate.edu/Forecast/2026-08.pdf (accessed 2026-09-05; **direct fetch returned HTTP 403 — figures taken from the search index and corroborated by source 9**)
8. Colorado State University — CSU seasonal forecast archive — https://tropical.colostate.edu/archive.html (accessed 2026-09-05)
9. weather.com — "Atlantic hurricane season likely to be very quiet, final CSU says" (5 Aug 2026) — https://weather.com/2026/08/05/storms/hurricane/atlantic-hurricane-season-outlook-csu-august-final-update (accessed 2026-09-05)
10. weather.com — "2026 Atlantic season's first hurricane: A record wait?" (1 Sep 2026) — https://weather.com/2026/09/01/storms/hurricane/first-hurricane-atlantic-record-long-wait-2026 (accessed 2026-09-05)
11. Fox Weather — "2026 Atlantic hurricane season nears historic territory for latest first hurricane amid looming Super El Niño" — https://www.foxweather.com/weather-news/atlantic-hurricane-season-late-first-hurricane-super-el-nino-2026 (accessed 2026-09-05; **direct fetch returned HTTP 404 — content from search index**)
12. Fox Weather — "NOAA releases updated 2026 Atlantic hurricane outlook as looming 'Super' El Niño aims to limit activity" — https://www.foxweather.com/weather-news/noaa-2026-hurricane-season-forecast-august-super-el-nino (accessed 2026-09-05)
13. KSAT — "Could the 2026 hurricane season beat a record? Possibly!" (2 Sep 2026) — https://www.ksat.com/weather/2026/09/02/could-the-2026-hurricane-season-beat-a-record-possibly/ (accessed 2026-09-05)
14. WJHG — "Historic lack of hurricanes inches closer to all-time record in the Atlantic Basin" (3 Sep 2026) — https://www.wjhg.com/2026/09/03/historic-lack-hurricanes-inches-closer-all-time-record-atlantic-basin/ (accessed 2026-09-05)
15. News 12 Connecticut — "Could The Atlantic Have No Hurricanes For The First Time On Record" (3 Sep 2026) — https://connecticut.news12.com/2026/09/03/could-the-atlantic-have-no-hurricanes-for-the-first-time-on-record/7CO2eGCBDyRXacSNQ9Ocbl (accessed 2026-09-05)
16. TechTimes — "Atlantic Hurricane Season Has Zero Hurricanes, 10 Days From Breaking Record" (1 Sep 2026) — https://www.techtimes.com/articles/326117/20260901/atlantic-hurricane-season-has-zero-hurricanes-10-days-breaking-record.htm (accessed 2026-09-05)
17. AccuWeather — "Atlantic hurricane season forecast 2026: 11-16 named storms predicted" — https://www.accuweather.com/en/hurricane/atlantic-hurricane-season-forecast-2026-11-16-named-storms-predicted-by-accuweather/1875776 (accessed 2026-09-05)
18. NOAA NHC — Saffir–Simpson Hurricane Wind Scale — https://www.nhc.noaa.gov/aboutsshws.php (accessed 2026-09-05)
19. NOAA NHC — 2026 Atlantic Tropical Cyclone Reports index — https://www.nhc.noaa.gov/data/tcr/index.php (accessed 2026-09-05)
20. NOAA NHC — Monthly Atlantic Tropical Weather Summary — https://www.nhc.noaa.gov/text/MIATWSAT.shtml (accessed 2026-09-05)
21. Wikipedia — "1914 Atlantic hurricane season" (latest season start on record, 14 September 1914) — https://en.wikipedia.org/wiki/1914_Atlantic_hurricane_season (accessed 2026-09-05)
22. Wikipedia — "2013 Atlantic hurricane season" and "2002 Atlantic hurricane season" (the two 11-September first-hurricane analogues) — https://en.wikipedia.org/wiki/2013_Atlantic_hurricane_season (accessed 2026-09-05)
23. Climate Central — Climate Reporting Resources: 2026 Hurricane Season — https://www.climatecentral.org/climate-matters/hurricane-season (accessed 2026-09-05)
24. Fox News — "Humberto becomes first hurricane of 2013" (11 Sep 2013) — https://www.foxnews.com/world/humberto-becomes-first-hurricane-of-2013 (accessed 2026-09-05; used to date the record)

**Date**: 2026-09-05
**Forecast**: 0: 47.0%, 1: 31.0%, 2: 15.0%, 3: 5.0%, 4+: 2.0% — leading option `0`, IQR [40.0%, 54.0%]
**Thesis**: With 96 days of season gone the Atlantic has 5 named storms, **zero** hurricanes and an ACE of 4.4 against a normal-season 123, a super El Niño is still intensifying, and NHC's 4 September outlook forecasts no formation for seven days — straight through the climatological peak — so the satellite-era record for the latest first hurricane (11 September, 2002 and 2013) will almost certainly fall [2,3,10,11]. Building the count from the ~55% of climatological majors that form after 12 September, scaled by CSU's 40–45%-of-normal activity, gives λ ≈ 0.85, which puts `0` and `1` together at 78%; I hold 22% on 2 or more because 2002 shows a record-late start is fully compatible with an Isidore/Lili October [4,7,9].
