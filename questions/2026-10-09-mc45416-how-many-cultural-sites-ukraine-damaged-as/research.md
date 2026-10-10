# Research log — How many cultural sites in Ukraine will be damaged as of December 31, 2026, according to UNESCO?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: UNESCO tracker https://www.unesco.org/en/ukraine-war/damaged-cultural-sites (headline "N cultural sites have been confirmed as damaged").
- Release schedule / cutoff: irregular. Publication lag is about 8–9 days after the as-of date (as of 29 Sep 2026 → updated 7 Oct; as of 26 Nov 2025 → updated 5 Dec 2025). If there is no update on 31 Dec, the latest 2026 update counts.
- Edge cases and ambiguities: a January-2027 publication with a December as-of date probably does not count. The page has two dates ("As of" and "Last update"). Range 560–660, closed lower bound, open upper bound. Background said 560 (23 Sep); the page now says 563 (29 Sep).
- WebFetch of the main tracker URL works. The `/en/articles/...` mirror and ReliefWeb return 403. The archive.org CDX API connection was reset (blocked from the container).

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Tracker increments, trailing 21 months | 8 intervals | Jan 2025–Sep 2026 | 4.2 sites/mo | UNESCO snapshots, see table in forecast.md | yes |
| Trailing 10 months | — | Nov 2025–Sep 2026 | 5.0/mo | same | yes |
| Since Mar 2026 | — | Mar–Sep 2026 | 6.1/mo | same | yes |
| Since May 2026 | — | May–Sep 2026 | 7.7/mo | same | yes (weighted up because of intensifying strikes) |

## Decomposition

Final = 563 + increment(Δt) where Δt = months from 29 Sep to the as-of date of the last update published in 2026.
P(Δt = 0) ≈ 8%. Otherwise Δt ~ U(1.4, 2.7) months. Rate ~ lognormal(median 7.0, σ_log 0.35). Increment ~ gamma-Poisson(k=4).
Output: p5 563, p10 565, p25 569, p50 575, p75 582, p90 591, p95 599. Script: `raw/sim-2026-10-09.py`; pmf in `raw/forecast-pmf-2026-10-09.json`.
The first run used a 6.3/mo rate median and gave 574 [569, 580]. I raised it to 7.0 after plotting, because the Jul–Sep slope is about 9/mo.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-09 | Metaculus aggregations script | criteria, fine print, background (560 as of 23 Sep; previous update 29 Jul = 545). Upcoming, n=2, no CP | anchor |
| 2026-10-09 | UNESCO tracker WebFetch | 563 as of 29 Sep 2026, last update 7 Oct 2026; breakdown 165/285/43/33/24/8/5 | starting value |
| 2026-10-09 | "UNESCO verified damage cultural sites Ukraine 2025 total" | 476 (22 Jan 2025), 501 (25 Jun 2025), 512 (26 Nov 2025, updated 5 Dec 2025) | time series |
| 2026-10-09 | Wikipedia list of damaged cultural sites | 514 as of 10 Dec 2025 | time series; two updates in Nov/Dec 2025 |
| 2026-10-09 | Georgia Today (2 Apr 2026) | 523 as of 11 Mar 2026 | time series |
| 2026-10-09 | Chytomo (26 May 2026) | 527 in the 13 May 2026 assessment | time series; Mar–May slow (+4) |
| 2026-10-09 | CFR (30 Sep 2026) | 560 by end Sep; civil society ≥ 5,500 sites | confirms; backlog large |
| 2026-10-09 | MinCult Ukraine / Kyiv Post | 1,707 (Mar 2026), 1,990 (end Jul), 2,161 heritage sites (end Sep 2026) | big unverified backlog |
| 2026-10-09 | ICOMOS / UNSC 10179th / UNESCO statements | 15 Jun 2026 strike damaged the Kyiv-Pechersk Lavra and the Dormition Cathedral; Odesa historic centre hit in July | inflow continues |
| 2026-10-09 | ISW 4 Oct 2026; Reuters 7 Oct strike | winter strike campaign began late Sep; 7 Oct mass strike | slight up |
| 2026-10-09 | OHCHR (Türk) via search | civilian casualties Jan–Aug 2026 up 55% y/y | intensity up |
| 2026-10-09 | Manifold API "UNESCO Ukraine" | no relevant market | — |
| 2026-10-09 | archive.org CDX for tracker history | connection reset | dead end |

## Dead ends and ruled-out hypotheses

- Wayback Machine history of the tracker is not reachable from this container (CDX request reset). A fuller time series would pin down the update cadence; next time try the archive.is prefix or a search for "Last update" snippets.
- No prediction market exists on this question.

## Open questions to chase next time

- Is there an October or November update? Check the tracker's "Last update" date.
- Does UNESCO plan a year-end report? That could trigger a late-December update.
- Metaculus CP, Pro and gold numbers after 17 Oct.
