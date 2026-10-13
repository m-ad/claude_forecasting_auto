# Research log — When will virtual reality headset sales exceed 10 million units per year?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: none named. Manufacturer reports summed, or "credible estimates" from
  analytics firms (Nielsen SuperData named as example). Estimates combining several headsets
  must **clearly include only qualifying headsets** (6DoF head tracking + 6DoF first-party
  controllers, or finger-precise hand tracking at admin discretion; occlusive VR, not AR; not
  phone adapters). Same-source differences of cumulative totals allowed.
- Release schedule / cutoff: no schedule. Analysts publish annual VR numbers ~Feb–Mar of the
  following year (Counterpoint, IDC); quarterly ~6–10 weeks after quarter end.
- Range 2020-07-15 … 2029-12-30, **open upper bound**; closes 2030-01-01.
- Edge cases and ambiguities:
  - Resolution date = end of the period in which the 10M is first established (e.g. Dec 31 of
    the year, or end of Q3 if Q1–Q3 already ≥10M). A full-year **2029** hit resolves
    2029-12-31 — one day **past** range_max (2029-12-30 00:00) → effectively "above upper bound".
    Only an in-year cumulative (Q1–Q3 2029) ≥10M lands inside the range for 2029.
  - "Sold" vs. "shipped": every analyst number is shipments (sell-in). Admin call.
  - Retroactive resolution: 2021 (Quest 2 peak) is borderline. Question still open in
    2026-10 despite the 2021/2022 data being public since 2022 — admins have not resolved it,
    and a Nov-2025 comment (exmateriae) tagging admins got no visible answer.
  - Vision Pro: no first-party controllers (it supports Sony's PSVR2 controllers — not
    first-party Apple); qualifies only via the hand-tracking clause. Volumes tiny anyway.
  - Annulment is possible at close if admins cannot establish numbers; not scored.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Qualifying VR, years with ≥10M clearly established | 10 years (2016–2025) | 2016–2025 | 0/10 clearly; 2021 borderline (~9.5–10.2M est.) | IDC 2021, Counterpoint | yes |
| Consumer-electronics category in ≥4 consecutive years of decline that then more than doubles above its prior peak level within 4 years | informal (tablets 2014 peak, 3D TV, MP3 players, consumer drones, wearables-other) | — | rare; ~0–10% | judgement, no formal dataset | yes, loose |
| Analyst (IDC) multi-year AR/VR forecasts vs realised | IDC Mar-2022 forecast >50M AR/VR units in 2026 vs realised ~4–5M VR (IDC's own 2026 MR/VR forecast now 3.2M) | 2022→2026 | overshoot ~10× | IDC 2022 PR; IDC promo page 2026-07 | yes — discount IDC's 10.4M-in-2030 MR forecast |

Raw outside-view P(a year ≥10M *established* by Q3 2029, future path) ≈ 3–5%.

## Decomposition

Two disjoint routes to an in-range resolution:

1. **Retroactive** (admins establish an earlier year, mostly 2021).
   - 2021 qualifying estimate: IDC 11.2M AR/VR × (Meta 78% + Pico ~4% [mixed 6DoF/3DoF] +
     HTC ~2–3% + iQIYI ~1–2% [partly 6DoF] + Sony/Valve/HP ~2–3%) ≈ 87–91% → 9.7–10.2M
     *shipments*; DPVR 5.1% is mostly 3DoF/enterprise (non-qualifying); AR "small fraction".
     Counterpoint: Quest 2 cumulative 4.6M by end-Q1 2021 and 10.4M by end-2021 → ≥5.8M Quest 2
     in Q2–Q4 2021; full-year Quest 2 likely 7–9M depending on Q1. Q4 2021 XR shipments −6% YoY
     (Counterpoint). Meta 2021 Reality Labs revenue $2.27B, consistent with ~6–8M units.
   - Net: 2021 is a coin-flip *at best* on a strict count, and no single source states "≥10M
     qualifying headsets sold in 2021". P(admins resolve to 2021) ≈ 6%.
   - 2022–2024: IDC 2022 AR/VR 8.8M, CCS 9.6M VR+AR; later years lower. Only a lenient read of
     broad "VR headsets" (e.g. Statista 11M for 2023, flagged by exmateriae as including
     non-qualifying devices) gets there → 1.5%.
2. **Future year** (2027, 2028, or Q1–Q3 2029 cumulative).
   - Run-rate: 2024 ≈ 6.5–7M VR (Meta 5.6M IDC, 77% share Counterpoint) → 2025 −28% (~5M) →
     H1 2026 −17%/−18% YoY → 2026 ≈ 3.5–4.5M.
   - Needs ×2.5 in two years. Drivers available: Quest 4 "Griffin" (late 2027 at earliest,
     memos say "improve unit economics" = pricier), Meta VR Glasses ($1,299.99, spring 2027,
     controllers extra), Steam Frame ($1,059+, reservation queue), Galaxy XR, PSVR2 (~1M/yr),
     China robotics-teleoperation demand (small). Headwinds: memory-price surge (Meta raised
     Quest prices Apr-2026), Reality Labs cuts, Meta pivot to AI glasses.
   - P(CY2027 or CY2028 ≥10M established) ≈ 2.5%; P(Q1–Q3 2029 cumulative ≥10M) ≈ 1%.

Total in-range ≈ 11%; above upper bound ≈ 89%.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-13 | Metaculus API/browser (aggregations script) | CP median 2028-01-29 IQR [2025-03-18, ≥2029-12-30] n=17; Pro median ≥2029-12-30, LQ 2027-10-29 (n=4); Gold median 2028-11-02, LQ 2026-03-29 (n=14). Medians drift ~1–3 days/day (stale forecasts) | anchor noted, not adopted |
| 2026-10-13 | Metaculus comments | exmateriae 2024-09/12, 2025-11: data confusing, Statista includes non-qualifying, "very unlikely"; mmmeta 2024-07: 40% of CP in the past — "lack of updating?"; Jgalt 2022-12: CCS 9.6M VR+AR 2022 | supports stale-CP reading |
| 2026-10-13 | IDC 2021 PR (telecomtv mirror; BusinessWire 403) | 2021 AR/VR 11.2M, Meta 78%, DPVR 5.1%, Pico 4.5%, HTC & iQIYI top-5; forecast >50M by 2026 | 2021 borderline; IDC overshoot |
| 2026-10-13 | Counterpoint Quest 2 10M (2022-05-19), Q1-2021 insight | Quest 2 cumulative 10.4M end-2021; 4.6M end-Q1 2021 | 2021 Quest 2 ~7–9M |
| 2026-10-13 | Counterpoint 2024 annual (2025-03-18) | VR −12% in 2024, third straight annual decline, Meta 77% | decline |
| 2026-10-13 | Counterpoint 2025 annual (via search) | VR −28% in 2025, Q4 −44% | decline |
| 2026-10-13 | The Register 2026-01-02 (IDC) | Meta 5.6M Quest 2024; 1.7M Q1–Q3 2025 (−16%); Vision Pro 390k 2024, 45k 2025 | run-rate |
| 2026-10-13 | vr.org 2026-09-11 / PC Gamer (Counterpoint Q2 2026) | VR −18% YoY, −16% QoQ; Meta price hike + memory surge; AR +138% | decline continues |
| 2026-10-13 | Search: Counterpoint Q1 2026 | VR −17% YoY, −39% QoQ | decline continues |
| 2026-10-13 | IDC AR/VR page (updated 2026-07-01) | MR/VR headsets 3.2M 2026 → 10.4M 2030; smart glasses 13.6M 2026 | even optimist IDC ≈ 10M only in 2030 |
| 2026-10-13 | IDC June-2025 PR | AR/VR −12% 2025; predicted +87% 2026 rebound (did not happen per H1 data) | IDC optimism bias |
| 2026-10-13 | TechCrunch 2026-04-16 | Quest 3S $349.99/449.99, Quest 3 $599.99 from 2026-04-19 (RAM shortage) | headwind |
| 2026-10-13 | Variety / qz / IDC blog (Connect 2026-09-23) | Meta VR Glasses $1,299.99 spring 2027, controllers sold separately; no Quest 4 | no mass-market device before late 2027 |
| 2026-10-13 | vr.org Q1 & Q2 2026 Reality Labs | RL Q2 rev $431M (+16% on AI glasses; Quest sales lower), loss $4.62B; CFO: VR spending to decrease | headwind |
| 2026-10-13 | Road to VR / vr.org Quest 4 | Griffin late 2027 at earliest; maybe 2028; "improve unit economics" | headwind |
| 2026-10-13 | vr.org / Wikipedia Steam Frame | launched Sept 2026, $1,059/$1,299, reservation queue | small volume |
| 2026-10-13 | UploadVR / Road to VR (2023) | Meta ~20M Quests lifetime by early 2023 | consistent with ~7–9M peak year |
| 2026-10-13 | Treeview/coopboardgames (low quality) | PSVR2 ~1.7M 2023, 0.8M 2024, ~1.3M 2025 est. | minor |
| 2026-10-13 | Manifold/Polymarket/Kalshi search | no matching market found | — |

## Dead ends and ruled-out hypotheses

- Wellsenn XR / TrendForce / Omdia 2021 VR-only annual totals: not found in English/Chinese
  searches. A clean VR-only 2021 number from a single source would raise S1.
- CNBC 2022-12-28 and BusinessWire IDC PR: HTTP 403 via WebFetch; content taken from the
  Metaculus comment quote and a syndicated mirror.
- Galaxy XR unit sales: none published.

## Open questions to chase next time

- Any admin response on Metaculus about 2021 or about how they will resolve at close.
- Counterpoint Q3 2026 (≈Dec 2026) and full-year 2026 (≈Mar 2027) VR shipments.
- Quest 4 announcement/price; Meta VR Glasses launch volume; Steam Frame volume estimates.
- A VR-only 2021 shipment total from Counterpoint/Wellsenn (would sharpen S1).
