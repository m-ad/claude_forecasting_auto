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

---

# v2 — Re-analysis — 2026-09-17

## Tripwire check (v1's list), run before any general search

| # | Tripwire | Status | Evidence |
|---|---|---|---|
| 1 | First hurricane by 2026-09-30 | not fired | still 0 hurricanes; the 11 Sep satellite-era record is now broken |
| 2 | Any system reaches Cat 3 | not fired | nothing has reached Cat 1 all season |
| 3 | NHC TWO ≥60% 7-day, western Caribbean | not fired | 17 Sep 02:00 EDT outlook: only AL98, subtropical, east of Bermuda, 40%/40% |
| 4 | ONI ASO/SON below +1.5 | **fired in reverse** | CPC 10 Sep: Niño 3.4 +1.8 °C (Aug), >90% very strong, 75% OND beats every event since 1950 |
| 5 | 2026-10-15 with zero hurricanes | not due | 28 days out |
| 6 | Further CSU/NOAA downward revision | partial | neither issues post-August seasonal updates; CSU two-week (2 Sep) verified below-normal; Klotzbach 10 Sep stats are the equivalent |
| 7 | CP on reveal <30% or >62% | **FIRED (low)** | CP at 2026-09-10 17:01Z = **27.3%**; Pro 49.0%, gold 41.7% at the same instant |

Tripwire 7 firing is what set the mode to **Re-analysis**. Second qualifying condition: a
real-money market exists (v1 said none did) and disagreed with v1 by 18.5 pp.

## What v1 got wrong

- **"No market found."** `KXHURCTOTMAJ-26DEC01` on Kalshi has traded this exact quantity since
  2026-04-01. v1's search used natural-language queries against the web UI; the series only
  surfaced via a differently-phrased search, and the price had to come from the public API
  (`api.elections.kalshi.com/trade-api/v2/markets?series_ticker=…`) because the UI returns 429.
  **Lesson: query prediction-market APIs by series ticker, not the site by prose.**
- **Tripwire 4 was written one-sided.** "ONI below +1.5" had no companion clause for El Niño
  coming in *stronger* than assumed, which is what happened. Tripwires on a continuous driver
  need both tails.
- v1's reference classes A/B/C were scored over whole seasons, which double-counts the three
  months already spent. v2 scores the remaining window only.

## Reference class, rebuilt: majors after 17 September in super-El-Niño seasons

Set from RONI (Relative Oceanic Niño Index — Niño 3.4 anomaly measured against tropical-mean SST,
which removes the global warming trend), three-month max in Jun–Nov: 1972, 1982, 1987, 1997,
2002, 2015.

| Year | Majors after 17 Sep | Which | Verified via |
|---|---|---|---|
| 1972 | 0 | none all season | — |
| 1982 | 1 | Debby, Cat 4 on 18 Sep | Wikipedia (Hurricane Debby 1982) |
| 1987 | 1 | Emily, Cat 3, 22 Sep | Wikipedia (Hurricane Emily 1987) |
| 1997 | 0 | Erika peaked 8 Sep | — |
| 2002 | 2 | Isidore (Cat 3, ~21 Sep), Lili (Cat 4, 2–3 Oct) | Wikipedia (both) |
| 2015 | 1 | Joaquin, Cat 4, 1 Oct, from a non-tropical low | Wikipedia + NHC TCR AL112015 |

Mean **0.83**; 4/6 seasons ≥ 1; empirical P(0) = **33%**. Every one of these six already had a
hurricane by 17 September — 2026 has none. That gap is the whole conditioning argument.

Climatological cross-check: ~85% of Atlantic major-hurricane activity falls 20 Aug – 10 Oct, 96%
of major-hurricane days in Aug–Oct (NHC climatology). 28 of the 51 core days are spent on 17 Sep
→ ~44% of climatological major activity still ahead → 3.2 × 0.44 ≈ **1.41** on a normal season.

## Rate construction

λ₀ = 0.83 (reference class). Marginal multipliers, each already discounted for collinearity:
record-low ACE 0.55 · record shear 0.75 · El Niño stronger than all analogues 0.85 · empty basin
today 0.90 → product 0.32. Used **0.37** instead, because the most likely failure of this chain
is double-counting four correlated pieces of one causal story, and that error is one-directional.
λ ≈ 0.31. Climatology route: 1.41 × 0.28 ≈ 0.39. **Centre λ = 0.35.**

Mixture over λ (0.20 / 0.35 / 0.60 / 1.10 at weights 0.30 / 0.40 / 0.22 / 0.08) →
0: 67.5 · 1: 25.0 · 2: 6.0 · 3: 1.3 · 4+: 0.3.

Shaded to **0: 63.0 · 1: 26.0 · 2: 8.5 · 3: 2.0 · 4+: 0.5** (mean 0.51): −4.5 pp on `0` for
WeatherTiger's specialist 40%, and `2` fattened toward Kalshi's 12% because the market prices
overdispersion (one favourable window → two majors, the 2002 shape) more strongly than a Poisson
mixture can.

## Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-09-17 | Metaculus #45381, all cohorts + 304-pt history (`METACULUS_FORCE_TLS12=1` required; plain run returned status 0) | CP 52.5 / Pro 53.1 / gold 52.5 on `0`, n=106; CP 27.3% at reveal → 52.5% in 7 days, still climbing | ↑ modest; caps how far above I go |
| 2026-09-17 | Kalshi public API, series `KXHURCTOTMAJ` | `>0` at 33/36¢ → **P(0) ≈ 65.5%**; last trade 02:45Z, 12.1k contracts, 6.5k OI; buckets 0/1/2 = 65.5/19.5/12.0 | ↑↑ new anchor |
| 2026-09-17 | NHC GTWO, 02:00 EDT | only AL98, subtropical, east of Bermuda, 40%/40%; Caribbean and MDR empty | ↑ |
| 2026-09-17 | CPC ENSO Diagnostic Discussion, 2026-09-10 | Niño 3.4 +1.8 °C (Aug); >90% very strong through winter; **75% chance OND RONI exceeds every event since 1950** | ↑↑ |
| 2026-09-17 | Klotzbach via weather.com / Yahoo, 10 Sep | ACE 4.4 = lowest through 10 Sep since 1950; early-Sep 30-day shear strongest since 1979 **by >3 kt** | ↑↑ the key new number |
| 2026-09-17 | WeatherTiger "Friends in Low ACEs", 9 Sep | **40%** P(no major); full-season ACE ≈ 34, 1 major; 20% chance below 1982's record-low 17.4; "no sign of an impending shift" | ↓ the only downward anchor |
| 2026-09-17 | weather.com 10 Sep, AOL, CNN 12 Sep, Insurance Journal 4 Sep | record for latest first hurricane broken; "most tranquil since 1941"; past super-El-Niño years averaged one September hurricane | ↑ |
| 2026-09-17 | Wikipedia 2026 season | still 5 named storms / 0 hurricanes / 0 majors; ACE 4.4 through 12 Sep; no active systems; Fay and Gonzalo unused | ↑ |
| 2026-09-17 | Wikipedia + NHC TCR: Debby 1982, Emily 1987, Isidore/Lili 2002, Joaquin 2015 | post-17-Sep majors in super-El-Niño years verified individually rather than recalled | ↓ caps P(0) |
| 2026-09-17 | Fox Weather / weather.com super-El-Niño composite | satellite-era super set = 1972/1982/1987/1997/2002/2015 by 3-month max RONI; those seasons averaged 11/4/2 | frames the class |
| 2026-09-17 | Search: Polymarket, Manifold | still nothing on Atlantic major-hurricane counts | — |

## Dead ends and ruled-out hypotheses (v2)

- **CSU or NOAA September seasonal update.** Does not exist — CSU's final seasonal forecast is the
  August one and NOAA's last update was 2026-08-06. Only CSU's two-week product continues. Do not
  wait for a revision that is not coming; tripwire 6 should have said so.
- **`tropical.colostate.edu` direct fetch** — 403 again, as in v1. Use the search index or
  weather.com write-ups.
- **Kalshi web UI** — HTTP 429. The public API at `api.elections.kalshi.com` is unauthenticated
  and works; `/markets?series_ticker=…` for quotes, `/markets/trades?ticker=…` for freshness.
- **Reading the Kalshi/Metaculus 13 pp gap as a mispricing to trade against.** More likely a lag:
  the CP has climbed monotonically for eight days without levelling, and its comment thread shows
  forecasters anchoring on NOAA's August "0–2 majors" and CSU's "1 major", both issued when only
  two named storms existed.

## Open questions to chase next time (2026-09-24)

1. Did anything form? Specifically, did AL98 or a successor Bermuda-area subtropical low develop,
   and did NHC ever forecast it above Cat 1?
2. Does any model guidance show an October western-Caribbean low-shear break? That is the only
   remaining route to a major and the single highest-value thing to check.
3. Has the Metaculus CP levelled off, and where? A level-off below 63% is evidence against me.
4. Has WeatherTiger updated its P(no major) from the 9 September 40%?
5. CPC ENSO update due ~2026-10-08 — does OND RONI still project above +2.5?

## v3 search log (2026-09-23)

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-09-23 | Metaculus #45381, all cohorts (`METACULUS_FORCE_TLS12=1`), `raw/metaculus-2026-09-23.json` | CP 63.0 / Pro 66.0 / gold 62.6 on `0`, n=122; CP levelled 60–63% since 21 Sep, peak 63.4% | converged on v2; Pros above |
| 2026-09-23 | Kalshi public API, markets + `>0` trades | `>0` 28/33¢, trades 30–37¢ → P(0) ≈ 69.5%; 16.6k vol | ↑ small |
| 2026-09-23 | NHC GTWO 02:00 EDT | no active systems; Cabo Verde wave 20/40%, shear expected to kill it | ↑ small |
| 2026-09-23 | Wikipedia 2026 season; Yale Climate Connections; Lowry substack | Fay 19–22 Sep, 70 mph, far NE Atlantic, from a disturbance NHC flagged late (not AL98); ACE ≈ 6.3 | ↓ small |
| 2026-09-23 | WeatherTiger 18 Sep column | ECMWF ~40% of normal days 1–10, ~70% days 11–17, ~60% days 18–25; less hostile Gulf/W Atlantic late Sep/early Oct | ↓ the main counter-signal |
| 2026-09-23 | WeatherTiger 15 & 21 Sep | paywalled; season 62.4% complete by storm energy on 21 Sep; no public revised P(no major) | hazard input |
| 2026-09-23 | CPC Global Tropics Hazards, 22 Sep | no week-3 Atlantic genesis areas; MJO in W Hemisphere, hard to discern | ↑ small |
| 2026-09-23 | Boston Globe 22 Sep; Klotzbach on X 22 Sep | first season since 1914 without a hurricane this late; no October Gulf systems in super El Niño since 1960; least ACE to date since 1950 | ↑ small |
| 2026-09-23 | CSU two-week 16 Sep | not found in search; next issue 30 Sep | — |
| 2026-09-23 | Polymarket / Manifold | only a named-storm market (stale); no majors market | — |

## Open questions to chase next time (2026-09-30)

1. CSU two-week forecast of 30 Sep — does it corroborate the ECMWF pattern change?
2. Any NHC area in the Gulf/W Caribbean/W Atlantic at ≥ 50% 7-day?
3. Did the Cabo Verde wave or the Mid-Atlantic frontal low become tropical, and how strong?
4. Pros cohort level vs. my 67%.

## v5 search log (2026-10-02)

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-10-02 | NHC TWO, 8 pm EDT 1 Oct | only Fay's remnant SE of Bermuda, 10%/10%, ending by Sunday; "formation not expected" otherwise | ↑↑ basin closed to ~8 Oct |
| 2026-10-02 | Wikipedia 2026 season | 8 NS / 0 H / 0 MH, ACE 10.8; Gonzalo 50 mph, Hanna 45 mph | ↑ |
| 2026-10-02 | Yahoo/USA Today 30 Sep | CSU two-week (30 Sep) 78% below normal, 2% above, through 13 Oct; Klotzbach ~50% hurricane-free season | ↑ (tripwire fired, below-normal side) |
| 2026-10-02 | CPC GTH issued 29 Sep | week-2 20–40% genesis Bay of Campeche / western Caribbean; nothing week 3; MJO signal hard to discern | ↓ |
| 2026-10-02 | Lowry, 1 Oct | DeepMind ensemble >50%, ECMWF ensemble 30–40% for TS in Bay of Campeche 7–9 Oct; record-warm southern Gulf; strong subtropical jet, "sprawling, sloppy subtropical-like system" | ↓ small |
| 2026-10-02 | WeatherTiger 30 Sep | ~1/3 of ensemble members develop SW Gulf 7–10 Oct; El Niño cuts Oct–Nov activity ~60%; >5% US hurricane risk rest of season | ↑ on rate, ↓ small on window |
| 2026-10-02 | Kalshi public API | T0 29/30¢ last 32¢, vol 18.3k (+0.8k); T1 11/14¢; T2 3/4¢ | ↑ anchor |
| 2026-10-02 | metaculus-aggregations, post 45381 | CP 79.5 (n=143), Pros 84.5 (n=11), gold 82.2 (n=36); no comments returned | ↑ (Pros tripwire fired) |
| 2026-10-02 | CNN 1 Oct (El Niño, hurricane-free September) | HTTP 451 to WebFetch | dead end |

Yahoo's article lists Hanna's peak as 70 mph; Wikipedia gives 45 mph (Fay was 70 mph). I used
Wikipedia.

## Open questions to chase next time (2026-10-09)

1. Did the 7–10 Oct southern-Gulf system form, and how strong did it get?
2. CPC ENSO update (~8 Oct): OND RONI level and the peak timing.
3. Any western-Caribbean signal for 14–31 Oct (CPC week 2/3, ECMWF weeklies)?
4. CSU two-week forecast of 14 Oct.
