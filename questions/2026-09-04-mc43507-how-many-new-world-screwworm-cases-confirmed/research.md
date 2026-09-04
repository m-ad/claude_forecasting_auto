# Research log — Mexico NWS cumulative animal cases before 1 July 2027

Metaculus [#43507](https://www.metaculus.com/questions/43507/). Session 2026-09-04.

---

## 0. Resolution mechanics

- Resolves as **cumulative** animal cases of New World screwworm (NWS) in Mexico on the
  **last USDA APHIS `stop-screwworm/current-status` report published before 2027-07-01**
  (so ~29–30 June 2027), rounded to the nearest 500.
- Range 30,000–100,000, **both bounds open**. Annulled if USDA stops reporting or changes
  criteria so the series is not comparable; the last report must be published no earlier
  than 2027-06-01.
- **Verification note.** The APHIS page renders the Mexico total client-side. `curl` returns
  a static map image plus a CSV (`/sites/default/files/nws-weekly-status.csv`) that lists only
  cases **within 100 miles of the US border** — not the national total. Chromium could not be
  driven through the session proxy (`ERR_CONNECTION_RESET` on every host), and the image
  transfer was cut by the proxy, so I could not read the APHIS total directly this session.
  Cross-check instead: the Metaculus commenter read **35,402** off the APHIS page on
  2026-07-29; linear interpolation of the SENASICA series (30,522 @ 06-24 → 37,241 @ 08-08)
  gives 35,748 at that date, a 1.0% gap. **USDA mirrors SENASICA with a lag of a few days.**
  I therefore forecast the SENASICA series and treat USDA as equal to it.

## 1. The case series (all figures cumulative since 2024-11-20 unless noted)

| Date | Cumulative | Active | Implied cases/day since previous |
|---|---:|---:|---:|
| 2024-11-20 | 0 (first Mexican case, Chiapas) | | |
| 2025-06-15 | 2,214 | | 10.7 |
| 2025-12-10 | — | **1,145 (2025 peak)** | |
| 2026-01-03 (epi wk 1) | 13,217 | | 54.5 (since 06-15) |
| 2026-01-07 | — | 492 (−57% vs peak) | |
| 2026-01-10 (epi wk 2) | 13,335 | | **16.9** ← winter trough |
| 2026-03-01 | 16,628 | | 65 |
| 2026-04-15 | 20,591 | 1,295 | 88 |
| 2026-05-11 | — | 1,682 | |
| 2026-06-24 | 30,522 | | 142 |
| 2026-07-29 | 35,402 (USDA) | | 139 |
| 2026-08-08 | 37,241 | 1,818 | 184 |
| 2026-08-18 | 38,820 | 1,963 | 158 |
| 2026-08-23 | 39,470 | 1,937 | 130 |
| 2026-08-29 | — | 1,905 | |
| 2026-09-02 | **40,684** | ~2,000 | 121 |

Snapshot: `raw/mexico-cumulative-series-2026-09-04.csv`.

**Three readings that matter.**

1. **Incidence has been on a plateau since mid-April 2026**, ~140 ± 20 cases/day.
   It is *not* accelerating. Active cases (a ~15-day prevalence window: SENASICA closes a
   case 15 days after diagnosis if no new larvae) rose 492 → 1,682 between January and May
   but only 1,682 → ~2,000 between May and September — a 3.4× rise then a 1.2× rise.
   Active/15 ≈ 130/day, consistent with the cumulative increments.
2. **The last four intervals decelerate**: 184 → 158 → 130 → 121 cases/day. Real inflection
   or reporting cadence? Too short a run to tell; it is the main live question.
3. **The winter brake is real and sharp.** Dec-2025 → early-Jan-2026: active cases −57%,
   weekly new cases down to 118/week (17/day) in epi week 2 while the epidemic was otherwise
   growing 4–5×/year. Partly the Mexican holiday reporting lull (25 Dec – 6 Jan), but the
   thermal biology backs it: development halts below ~14 °C, adult activity falls below 21 °C
   (Drovers/DTN summaries of the historical programme).

## 2. Geography — why winter 2026-27 should bite harder than 2025-26

Cumulative burden is still southern (Chiapas 7,604, Oaxaca 5,074, Veracruz 4,720,
Yucatán 2,792 @ 08-18) but the **active** burden has moved into temperate highland and
northern states: Zacatecas 179, Puebla 166, Yucatán 117, Jalisco 100, San Luis Potosí 98,
Nayarit 97, Querétaro 86, Chihuahua 74, Guanajuato 69 (active, 08-18). 30 of 32 states have
cases; only Baja California and Baja California Sur are free. Sonora's first case: 2026-08.

Gutierrez et al. 2019 (PMC6849717): year-round endemicity in the historical era was confined
to south Texas, Florida, an eastern band (Nuevo León / Tamaulipas / Veracruz), Yucatán and
tropical southern Mexico; the rest was seasonally re-invaded. That is the shape to expect —
a hard Dec–Mar contraction to the tropical reservoir, then re-expansion from April.

## 3. Sterile insect technique — the dose is one-third of what eradication took

- **COPEG Pacora (Panama)**: ~100 M sterile flies/week, at capacity, built 2006 for the
  Darién barrier. It did **not** prevent Panama going from ~25 cases/yr to >6,500 in 2023.
- **Metapa de Domínguez (Chiapas)**: inaugurated 2026-06-27 ($51 M, Mexico $30 M / USDA $21 M).
  28 M/week mid-July, **35 M/week August 2026**, target **100 M/week by end-2026**,
  possibly 120 M later.
- **Moore Air Base / Edinburg, Texas** ($750 M, 300 M/week): not online in this window.
- Historical field dose in Mexico (Krafsur 1985, via Gutierrez et al. 2019):
  **~386 sterile flies/week/km²**. Mexico's affected area is roughly 1.5 M km² → ~580 M/week
  for a country-wide blanket. Available over Mexico now: ~135 M/week. **~23% of the
  historical rate**, rising to ~35% at Metapa's full ramp.
- And the flies are **not** spread over the burden. USDA states plainly: "our highest priority
  remains protecting the United States". Mexico's own August releases: 14.97 M flies over
  7 Chihuahua municipalities (27 Jul–11 Aug), >40 M over 14 Chihuahua municipalities by 23 Aug.
  The Chiapas/Oaxaca/Veracruz reservoir that generates most cases is essentially untreated.
- Gutierrez et al. 2019 also estimate historical **SIT efficacy at ~1.7%** — the eradication
  was won as much by cold winters and the barrier geometry as by fly numbers.

**Conclusion:** SIT will slow the northward front and protect the US. It will not collapse
Mexico's national case count inside 10 months. Mexico's own stated goal is eradication in
**~5 years** with all three plants running (500 M/week).

## 4. Outside view — reference classes

| Class | n | Observation | Read-across |
|---|---|---|---|
| Central American countries invaded 2023-24 | 6 | None has eradicated. Nicaragua: 27,916 cumulative animal cases from Apr-2024 to mid-2026 and still rising, on a ~5.4 M-head cattle herd, with a $16–17 M/yr budget | Year-3 incidence stays high; no country turned the corner in 24–30 months |
| Panama post-barrier-breach 2023 | 1 | ~25 → >6,500 cases/yr **despite** 100 M sterile flies/week next door | 100 M/week is not a suppression dose for an established outbreak |
| Region-wide | — | >209,400 animal cases and >2,500 human cases across Mexico + Central America since 2023 (CDC, updated 2026-08-11) | The epidemic is regional and self-sustaining |
| Historical NA eradication | 1 | Florida 1957 → Texas 1962 → Mexico 1980s → Panama late 1990s, at up to 500 M flies/week | Decades, not months, at 3× the current dose |
| Model optimum | 1 | Reyes & Barrio 2026 (PLoS ONE): eradication in **60–100 weeks** *if* releases are optimally fed back and applied at the focus within a 120 km radius | The theoretical floor — and 60 weeks from now is Nov 2027, past this window. The real outbreak is 30 states wide, not one focus |

**Outside-view base rate**: an established NWS outbreak with sub-eradication SIT dosing
does not decline materially within 10 months. Naive persistence at the current 121–140/day
over 298 days gives **+36,000 to +42,000 → 77,000–83,000**. Seasonality is the main thing
pulling that down.

## 5. Inside view — the arithmetic that decides this

Cumulative at 2026-09-04 ≈ **40,900** (40,684 @ 09-02 + ~2 days).
Days to the resolving report (2027-06-29): **298**.

Required average daily incidence to hit the community prediction of 60,426:
`(60,426 − 40,900) / 298 = 65.5 cases/day` — **48% of the current rate, sustained for
ten months**. Pure seasonality (4 trough months at ~0.45, 6 months at ~0.9) averages ~0.72 of
today's rate. Getting to 0.48 needs seasonality **plus** roughly a further one-third cut in
the non-winter rate.

Seasonal index used (September = 1.00), from the 2025-26 winter and the thermal biology:
Sep 1.00 · Oct 0.95 · Nov 0.80 · Dec 0.55 · Jan 0.40 · Feb 0.45 · Mar 0.60 · Apr 0.75 ·
May 0.90 · Jun 1.00.

Flat-trend + seasonality only, at 131 cases/day: **+28,500 → ~69,400**.

Monte Carlo (`scratchpad/model.py`, 200k draws): baseline rate N(131, 12); five trend
scenarios interpolated log-linearly from 1.0 today to a terminal multiplier; seasonal
amplitude N(1.0, 0.20); model-error lognormal σ=0.10; 6% chance of a counting-regime
shift short of annulment (×0.30–0.70 on added cases).

    p5 54,500 · p10 57,000 · p25 61,500 · p50 67,000 · p75 74,000 · p90 81,000 · p95 85,500

**Arithmetic floor.** Even an immediate 70% collapse in incidence plus a hard winter adds
~10,000 → ~51,000. Anything below 50,000 requires a reporting change, not an epidemiological
one. P(< 50,000) ≈ 1.3%.

## 6. Searches run (and dead ends)

| Query / target | Outcome |
|---|---|
| APHIS `current-status` page (curl + text strip) | Got the news list and the border-cases CSV; **no national total in the served HTML** |
| Probe for `nws-mexico-*.csv` on aphis.usda.gov | 404/blocked — no Mexico totals file |
| SENASICA Power BI dashboard (`app.powerbi.com/view?r=…`) | Egress proxy closes the tunnel; Chromium/Playwright also `ERR_CONNECTION_RESET` on every host. **Dead end this session** |
| Wayback Machine CDX for a page history | `ws_closed_mid_exchange` ×4, then WebFetch refused for `web.archive.org`. **Dead end** |
| APHIS map JPEG (would carry the printed total) | Proxy cut the binary transfer (`HTTP/2 INTERNAL_ERROR`, then empty reply). **Dead end** |
| `dj.senasica.gob.mx/ASIA/…` official series | Navigation shell only, no data server-side |
| COPEG `situacion-actual` | Narrative only, no country case tables |
| Spanish-language press citing SENASICA weekly reports | **This is the working channel.** Quadratín, El Tiempo Monclova, Excélsior, Diario de México, Periódico Correo all quote the weekly SENASICA cut with dates |
| Kalshi / Polymarket for a Mexico case-count contract | None. Kalshi has `KXSCREWWORMCOUNT` (**US** cases only) |
| Manifold `screwworm` | 6 markets, all US/eradication-flavoured, ≤$1.7k volume. Nothing on Mexican counts |
| Sentinel Team, Mantic, GJOpen, INFER | No matching question found |
| PubMed `Cochliomyia hominivorax Mexico` 2025– | 49 hits; the useful ones are the PLoS ONE control model, the EID human-myiasis series and two niche models. **No published projection of Mexican case counts** |

## 7. What I looked for and did *not* find (absence-of-evidence checks)

- **No** USDA, SENASICA or academic forecast of Mexican case counts for 2027. Nobody has
  published a number to anchor on; the CP is not encoding a hidden expert projection.
- **No** evidence that SENASICA plans to change its case definition or stop the weekly cut.
- **No** evidence of an area-wide sterile-fly programme over southern Mexico — every release
  story in Aug 2026 is Chihuahua/northern.
- **No** Central American precedent of an outbreak turning over inside 30 months.

## 8. Where the community sits and why I differ

CP 60,426 (n=29 recency-weighted), Pro 59,018 (n=5), gold 62,410 (n=15) — all as of
2026-09-03. Total forecasters on the question: 43. The three cohorts agree, and the gold and
recency-weighted histories start from *identical* values, so their agreement is close to a
single low-attention crowd, not three independent panels.

The CP was formed around 2026-06-12 at 62,691 when cumulative stood near 30,000 — i.e. "it
roughly doubles". It has since drifted **down** to 60,426 while realised cases ran ahead of
that path, and a commenter flagged the staleness on 2026-08-02 with no visible correction.
The community's lower quartile (47,133) implies +6,200 cases in ten months = 21/day, an
83% instant collapse — that quartile is a fossil of a June belief, not a live one.

I sit ~11% above the CP in level terms, ~6,600 cases. Given the deceleration in the last
four intervals I do **not** go as high as naive persistence (77k–83k) would suggest.
