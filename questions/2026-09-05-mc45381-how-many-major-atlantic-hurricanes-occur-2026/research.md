# Research log — How many Major Atlantic Hurricanes will occur in the 2026 Atlantic hurricane season?

## Question mechanics

- **Type**: multiple choice over counts — `0`, `1`, `2`, `3`, `4+`. Admin confirmed in comments
  (tejvn, 2026-09-05) that the buckets are exhaustive and **4+ includes exactly 4**.
- **Definition**: major hurricane = Category 3+ on Saffir–Simpson, ≥111 mph / 178 km/h sustained.
- **Window**: storms occurring 2026-06-01 → 2026-11-30 inclusive.
- **Resolution source**: NHC storm reports and data **as published on 2026-12-01**. Fine print:
  *any subsequent revisions upgrading or downgrading a storm's intensity will not be considered.*
  → the **operational** count governs, not the final best-track after post-season reanalysis.
  This matters at the margin: post-season Tropical Cyclone Reports (published months later)
  historically upgrade more storms to major status than they downgrade, particularly for systems
  never sampled by reconnaissance aircraft. A small **downward** bias on the resolving count.
- Named cross-reference sources: NHC Tropical Cyclone Advisory Archive and the Monthly Atlantic
  Tropical Weather Summary (issued 1 December for November).

## Season state as of 2026-09-05 (the single most important input)

| Metric | 2026 to date | 1991–2020 normal, full season |
|---|---|---|
| Named storms | **5** (Arthur, Bertha, Cristobal, Dolly, Edouard) | 14 |
| Hurricanes | **0** | 7 |
| Major hurricanes | **0** | 3.2 |
| ACE | **≈ 4.4** | ≈ 123 |

Storm-by-storm peaks: Arthur 45 mph (Jun 17–18), Bertha 60 mph (Jul 19–24), Cristobal 45 mph
(Aug 12–13), Dolly 40 mph (Aug 27–28), Edouard 60 mph (Aug 31–Sep 3). **Nothing has come within
15 mph of hurricane strength all season.**

Two facts make this extreme rather than merely quiet:

1. **The satellite-era record for the latest first Atlantic hurricane is 11 September** — set
   twice, by Gustav (2002) and Humberto (2013). 2026 is days away from breaking it.
2. **NHC's Tropical Weather Outlook of 2026-09-04 forecasts no tropical cyclone formation
   anywhere in the Atlantic, Caribbean or Gulf for the next 7 days** — i.e. straight through the
   10 September climatological peak. The record will therefore almost certainly fall.

Driver: a **strong-to-"super" El Niño** intensifying through the season, driving hostile
vertical wind shear across the basin, partly offset by slightly-above-normal Atlantic SSTs and
weaker-than-average trades.

## Seasonal forecasts on record

| Forecaster | Issued | Named | Hurricanes | **Majors** | ACE |
|---|---|---|---|---|---|
| Tropical Storm Risk (TSR) | Dec 2025 | 14 | 7 | 3 | 125 |
| NOAA CPC (initial) | 2026-05-21 | 8–14 | 3–6 | **1–3** | — |
| UK Met Office | 2026-05-28 | 9 | 5 | 2 | 72 |
| CSU (initial) | 2026-04 | 13 | 6 | 2 | — |
| CSU | 2026-06-10 | 11 | 5 | 2 | — |
| **CSU (final)** | **2026-08-05** | **9** | **4** | **1** | **40–45% of normal** |
| **NOAA CPC (August update)** | **2026-08-06** | **7–13** | **2–6** | **0–2** (70% conf.) | 30–90% of median |
| AccuWeather | pre-season | 11–16 | — | — | — |

NOAA raised P(below-normal season) from 55% → **75%** on 2026-08-06. Every successive revision
by every forecaster has moved **down**. Both August forecasts were issued when only 2 named
storms had formed; three more have since formed and all three failed to reach hurricane strength.

## Reference classes considered

| Class | n | Members / result (major-hurricane count) | Mean | Kept? |
|---|---|---|---|---|
| **A. No hurricane by 5 September** (satellite era) | 4 | **2001: 4** · **2002: 2** · **1984: 1** · **2013: 0** | 1.75 | kept — but *none* of these had an El Niño of this strength; 2001 was a favourable-basin year that then produced Erin, Felix, Iris and Michelle |
| **B. Strong El Niño (ONI ≥ ~1.5 in ASO)** | 7 | 1972: 0 · 1982: 1 · 1987: 1 · 1991: 2 · 1997: 1 · 2015: 2 · 2023: 3 | 1.43 | kept — but **every one of these seven already had a hurricane by 5 September**, most had a major. 2026 is more extreme than the whole class |
| **C. Seasons with total ACE 30–60** | ~10 | 1968:0 · 1972:0 · 1986:0 · 1987:1 · 1993:1 · 1994:0 · 1997:1 · 2013:0 · 1991:2 · 2009:2 | ~0.7 | kept — closest to the ACE trajectory implied by CSU's 40–45%-of-normal |
| D. All seasons 1966–2025 | 60 | — | 3.2 | rejected as an anchor; useful only to show how far 2026 sits from climatology (0-major seasons: 1968, 1972, 1986, 1994, 2013 → 5/60 ≈ **8%** unconditionally) |

Class A is the trap in the *upward* direction (n=4, no El Niño conditioning). Class B is the trap
in the upward direction too, because 2026 is already worse than every member. Class C is the best
match to where the season is actually headed.

## Decomposition

Rate-based construction:

- Climatological majors after ~12 September (the earliest plausible first hurricane, given NHC's
  no-formation-for-7-days outlook on 4 Sep): ≈ **55%** of the seasonal 3.2 → **1.8 majors**.
- Activity multiplier for the remainder of the season. CSU's 40–45%-of-normal is a *whole-season*
  figure that already banked a near-zero first half; the implied remainder is higher than 0.42.
  But the season is running at ~13% of normal ACE pace and El Niño is *intensifying*, so the
  remainder should not be marked up much. Take **0.35–0.50**, centre **0.42**.
- → λ ≈ 1.8 × 0.42 ≈ **0.76**. Widen upward slightly for the western-Caribbean October window,
  which has produced majors even in El Niño years (Lili, Cat 4, 3 Oct 2002; Joaquin, Cat 4, late
  Sep–Oct 2015): **λ ≈ 0.85**.

Poisson(0.85): P(0)=.427, P(1)=.363, P(2)=.154, P(3)=.044, P(4+)=.012. Major-hurricane counts are
over-dispersed relative to Poisson (a single favourable synoptic window can yield two or three),
so shift mass from the centre to both tails, and add the operational-vs-reanalysis downward bias
from the fine print.

**Final: 0 = 47.0% · 1 = 31.0% · 2 = 15.0% · 3 = 5.0% · 4+ = 2.0%** (mean 0.85).

Sanity checks:
- NOAA's 0–2 band at 70% confidence: my P(0–2) = 93%. NOAA's stated ranges run conservatively wide
  in practice, and NOAA's band predates a month of nothing happening. Consistent.
- CSU's point forecast of exactly 1 major sits in my modal region; my distribution is a shade
  more pessimistic than CSU, justified by a month of further deterioration since 5 August.
- Unconditional P(0 majors) is 8%; I am at 47%. That is a 6× update, driven by: 0 hurricanes at
  the peak, ACE at 3.6% of a normal season's total, a record about to break, a super El Niño, and
  a 7-day no-formation outlook. I am comfortable with the size of that update.
- Scope check: if the season had two more months, P(0) would fall substantially — it does not, so
  the number is scope-sensitive in the right direction.

## Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-09-05 | Metaculus #45381 JSON | Status `upcoming`, CP hidden until 2026-09-10T17:00Z, n=20; comment confirms 4+ includes 4 | frames buckets |
| 2026-09-05 | Wikipedia "2026 Atlantic hurricane season" | 5 named storms, **0 hurricanes**, **0 majors**, ACE ≈ 4.4; no active systems; strong El Niño | the core input |
| 2026-09-05 | NHC Graphical Tropical Weather Outlook, dated 2026-09-04 | **No formation expected in the next 7 days** across Atlantic/Caribbean/Gulf | ↓↓ removes the peak week |
| 2026-09-05 | NOAA news release + CPC hurricane outlook, 2026-08-06 | 7–13 named / 2–6 hurricanes / **0–2 majors**; ACE 30–90% of median; P(below normal) 55%→75% | ↓ |
| 2026-09-05 | CSU forecast 2026-08-05 (tropical.colostate.edu/Forecast/2026-08.pdf — **403 to direct fetch**, read via search index and weather.com write-up) | 9 named / 4 hurricanes / **1 major**; ACE & NTC 40–45% of normal; US major-hurricane landfall 32% | ↓ |
| 2026-09-05 | weather.com 2026-09-01, KSAT 2026-09-02, WJHG 2026-09-03, News12 CT 2026-09-03, TechTimes 2026-09-01, Fox Weather | Satellite-era record for latest first hurricane = **11 September** (Gustav 2002, Humberto 2013); 2026 closing on it; outlets openly asking whether the Atlantic could finish with **zero** hurricanes | ↓↓ |
| 2026-09-05 | Historical: 1914 season (first storm 14 Sep, latest start since 1851); 1905 (first hurricane 8 Oct, pre-satellite) | pre-satellite seasons ran later still — the physical possibility of a very late or absent first hurricane is real | ↑ tail on P(0) |
| 2026-09-05 | Reference-class construction (2001, 2002, 2013, 1984; strong-El-Niño years) | A: mean 1.75 · B: mean 1.43 · C: mean ~0.7 | pulls up against my rate model; reconciled by noting 2026 is more suppressed than every member of A and B |
| 2026-09-05 | Search: Polymarket / Kalshi / Manifold Atlantic hurricane count 2026 | **No matching market found** for major-hurricane counts | no external anchor |

## Dead ends and ruled-out hypotheses

- **Anchoring on pre-season forecasts.** TSR's December 2025 call (14/7/3, ACE 125) is worthless
  now; it predates the El Niño signal. Only the August updates carry information, and even they
  are a month stale.
- **"Warm Atlantic SSTs will overcome El Niño", the 2023 argument.** 2023 produced 3 majors
  despite El Niño because record-shattering Atlantic SSTs offset the shear. 2026's SSTs are only
  *slightly* above normal per NOAA — the 2023 escape hatch is not available. Ruled out as a
  reason to mark up.
- **Post-season reanalysis upgrades.** Explicitly excluded by fine print. Do not forecast the
  best-track number; forecast the 1 December operational number.
- **Manifold / Polymarket**: searched, nothing on Atlantic major-hurricane counts.

## Open questions to chase next time

1. Did a first hurricane form, and when? Breaking 11 September is close to mechanical now.
2. What is the ONI value for ASO 2026, and is El Niño still strengthening into October?
3. Is there a western-Caribbean October signal (MJO phase, low shear window)? That is the last
   realistic route to 2+ majors.
4. Does NHC's operational count on 1 December differ from live tracking?
