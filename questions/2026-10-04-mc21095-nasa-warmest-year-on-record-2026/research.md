# Research log — Will 2026 be the warmest year on record, according to NASA?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: NASA GISS GISTEMP v4 LOTI; the annual press release is mid-January (2025's: 2026-01-14). Monthly data around the 10th–15th of the following month.
- The bar: 2024 = **1.29** in graph.txt No_Smoothing (the mean of the 2-dp monthly values is 1.286). 2025 = 1.19, 2023 = 1.17.
- Release schedule / cutoff: Sep 2026 GISTEMP ~2026-10-14; Oct ~mid-Nov; Nov ~mid-Dec; Dec + annual ~2027-01-14.
- Edge cases and ambiguities:
  - **Ties.** NASA headline 2021: "2020 tied with 2016" for a +0.01 margin. 2026-01: 2025 vs 2023 (+0.02) "effectively tied". Metaculus criteria say only "officially reports that the year is the hottest year on record". Nothing on ties. Comments could not be read (403).
  - Kalshi (>1.28) and Polymarket (tie = rank 1) both count a 1.29 tie as YES, so they are not directly comparable with this question.
  - GISTEMP back-revisions of ±0.01–0.02 per month are routine.
  - Group-level siblings: 2024 resolved (NASA called 2024 a record), 2025 resolved (NASA: 2nd, tied with 2023). The resolution values are hidden from the bot key.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| GISTEMP record years, all years | 30 | 1996–2025 | ~30–33% | graph.txt | no (8 of 12 months known) |
| Strong-El-Niño onset years: Sep–Dec minus Jan–Aug ≥ +0.18 (tie) | 4 (1972, 1997, 2015, 2023) | 1972–2023 | 3/4 | GISTEMP monthly | yes |
| Same, ≥ +0.21 (strict 1.30) | 4 | 1972–2023 | 2/4 | GISTEMP monthly | yes |
| All years, Sep–Dec minus Jan–Aug | 66 | 1960–2025 | mean −0.007, sd 0.117 | GISTEMP monthly | context |
| OND minus Aug–Sep, strong onset years (GISTEMP) | 8 | 1957–2023 | 1957 −0.04, 1965 +0.03, 1972 0.00, 1982 +0.16, 1987 +0.06, 1997 +0.15, 2015 +0.28, 2023 +0.04 | GISTEMP monthly | yes |

## Decomposition

- Annual = (9.79 + Sep + Oct + Nov + Dec)/12. For a 2-dp 1.29 the Sep–Dec mean must be ≥ 1.4075; for 1.30, ≥ 1.4375.
- Sep estimate: ERA5 Sep 2026 = 0.819 (1991–2020 base; 30 days). Regression GISS = 0.617 + 0.937·ERA5 (2000–2026, n = 320, resid sd 0.055, lag-1 autocorrelation 0.42) gives 1.384; the 2024–26 residual mean is +0.020, so **Sep ≈ 1.40 ± 0.05**.
- Oct–Dec regression: GISS monthly ~ 1 + t + t² + RONI(lag 3), 1980–2025. β ≈ 0.073; residual sd 0.131 (long-window misfit); residual mean over 2023–25 is +0.083; the 2026 residuals Jan–Aug are −0.05, +0.11, +0.18, +0.02, −0.03, −0.01, +0.03, +0.14. Model predictions: Sep 1.30, Oct 1.33, Nov 1.36, Dec ~1.39. Adding a persistent residual of ~+0.07 gives Oct–Dec ≈ 1.43.
- Monte Carlo, `mc2026` (deleted from raw/ because raw is for data; recreate from this spec): Sep ~ N(1.40, 0.05); OND = 1.445 + 0.3·(Sep − 1.40) + N(0, 0.065); revision noise N(0, 0.005). The annual is rounded to 2 dp and mapped as ≤1.28 → 0.01, 1.29 → 0.55, 1.30–1.31 → 0.80, ≥1.32 → 0.97.
  - central: mean 1.294, sd 0.019; buckets 0.32/0.21/0.35/0.13; P(≥1.29) = 0.681; P(YES) ≈ 0.51 (0.507 with P(tie) = 0.5)
  - OND 1.43 → 0.44 / 0.61; OND 1.47 → 0.61 / 0.79; OND 1.50 → 0.73 / 0.88; Sep 1.36 → 0.45 / 0.61; OND sd 0.09 → 0.50 / 0.64

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-04 | Metaculus aggregations script (×2, 3 min apart) | 403 (Cloudflare); scraper fails with ERR_CERT_AUTHORITY_INVALID | no CP / Pro / gold |
| 2026-10-04 | Metaculus API via bot key | metadata: 116 forecasters; subquestions 2024/2025 resolved; 2027 (id 45424) added 2026-08-18; no fine print | — |
| 2026-10-04 | GISTEMP CSV + graph.txt | Jan–Aug 2026 = 1.09, 1.25, 1.32, 1.17, 1.13, 1.18, 1.25, 1.40; 2024 = 1.29 | core |
| 2026-10-04 | Copernicus Climate Pulse ERA5 daily CSV | Sep 2026 0.819 (2nd after 2023 0.93); Aug 0.85 (record); 1–2 Oct 0.695, 0.679 | Sep ≈ 1.40 GISS; slight down from early October |
| 2026-10-04 | CPC RONI / ONI / ERSST Niño | ONI JAS 2.16 (record for JAS); RONI JAS 1.69 (1997: 1.84, 2015: 1.54, 2023: 0.79) | ENSO strength similar to 1997/2015 in relative terms |
| 2026-10-04 | CPC ENSO discussion 2026-09-10 | >90% very strong; 75% "historic" (RONI ≥ 2.5) for OND | 2027 mainly |
| 2026-10-04 | Carbon Brief 2026-07-24 | 35% composite; per dataset: GISTEMP 65%, Berkeley 66%, HadCRUT 35%, NOAA 24%, ERA5 13%, JRA-3Q 9%; 2027: 92% | anchor for "nominal" record |
| 2026-10-04 | Carbon Brief 2026-04-21 | 19% (April); 2027 likely record if super El Niño | history |
| 2026-10-04 | Carbon Brief 2026-09-21 | Niño-3.4 3.11 °C; RONI ~2.5 mid-Sep; peak ~4.1 (80% 3.4–4.6) | ENSO |
| 2026-10-04 | Hausfather (SkS) 2026-08-03 | GISTEMP ~65%; 2027 91% | anchor |
| 2026-10-04 | Berkeley Earth July update 2026-08-13 | 69% record in its dataset; 30% 2nd | anchor |
| 2026-10-04 | Fox Weather 2026-09-24 | ERA5 Sep tracking 2nd warmest, ~0.2 °F below 2023 | consistent with the CSV |
| 2026-10-04 | NOAA / Copernicus August 2026 reporting (search summaries) | Aug 2026 warmest August; ties July 2023 as the warmest month (ERA5) | consistent |
| 2026-10-04 | NASA 2025 release 2026-01-14 | "effectively tied" wording; no mention of climate change | resolution-language risk |
| 2026-10-04 | NASA SVS 2020 tied | "2020 Tied for Hottest Year on Record" at +0.01 | tie precedent |
| 2026-10-04 | Kalshi API KXGTEMP-26-P0 | 63.6 / 64.0 bid/ask; 378,599 contracts; YES if > 1.28 | market |
| 2026-10-04 | Kalshi KXGTEMP-27 event | a mislabelled 2026 duplicate, 66–68% | not a 2027 market |
| 2026-10-04 | Polymarket gamma public-search | 2026 hottest 70.5% (0.70 / 0.71), 2nd 25.5%; tie = rank 1 | market |
| 2026-10-04 | Manifold search | 2026 hottest 77.3% (113 bettors); 2030 33% (23) | discounted |
| 2026-10-04 | WMO decadal 2026-05-28 | 86% at least one of 2026–30 > 2024 | 2027 / 2030 context |
| 2026-10-04 | IGCC 2025 (Forster et al.) | human-induced rate 0.27 [0.2–0.4] °C/decade | trend prior |
| 2026-10-04 | Sentinel search | no Sentinel-specific forecast found; only press echoes of Hausfather / Berkeley | none |

## Dead ends and ruled-out hypotheses

- Climate Reanalyzer JSON endpoints return 403 ("Houston, we've had a problem"). Use the Copernicus Climate Pulse CSV instead.
- metaculus-scraper: Playwright TLS error through the proxy (ERR_CERT_AUTHORITY_INVALID).
- Berkeley Earth August 2026 update: not found by search on 2026-10-04 (probably published but not indexed).
- Polymarket 2027 market: none found.

## Open questions to chase next time

- **Metaculus comments**: any admin ruling on ties? Retry the aggregations fetch at the next update.
- GISTEMP Sep 2026 print (~10-14). Then ERA5 October from the Climate Pulse CSV (just recompute the monthly mean).
- Does NASA's Jan-2027 release say "tied" or "warmest"? Watch for GISS staffing / budget news before then.
