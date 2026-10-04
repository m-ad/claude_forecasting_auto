# Research log — When will Germany have no coal-fired power plants in its electricity grid?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution: earliest of (a) no coal plant in Germany connected to the grid for ≥ 2 weeks,
  or (b) coal < 1% of Germany's domestic electricity generation over any 12-month period.
  The resolution date is the **end date** of that 2-week / 12-month window.
  Range 2024-12-28 … 2038-12-27, open upper bound (">Dec 27, 2038").
- Resolution source: not named. Background cites Energy-Charts (Fraunhofer ISE), which
  publishes *public net* generation. AGEB/Destatis publish *gross* generation including
  industrial self-supply (~12 TWh more coal in 2025: 106 TWh gross vs 94 TWh public net).
- Release schedule: Energy-Charts is near-real-time (monthly totals available within days);
  AGEB annual figures in December/February. A rolling 12-month window can be checked monthly.
- Edge cases:
  - Path (a) is effectively dead while the hard-coal **Netzreserve** exists (~8.1 GW of hard
    coal in grid reserve for winter 2026/27, BNetzA) — reserve plants stay grid-connected.
    Lignite in "Sicherheitsbereitschaft" also stays connected. So path (b) decides.
  - Under the pure statutory schedule (last LEAG units Boxberg Q/R + Schwarze Pumpe close
    **31 Dec 2038**), path (a) would end ~mid-Jan 2039 → **beyond** the 2038-12-27 bound.
    The question only resolves inside the range if market forces cut coal to < 1% earlier.
  - 1% of generation ≈ 4.5–6 TWh (total 450–600 TWh as electrification grows). A single
    1 GW lignite unit at 50% capacity factor ≈ 4.4 TWh. So "< 1%" ≈ almost no market coal.
  - Gross vs public net matters at the tail: industrial coal self-generation (~1.5 TWh lignite
    + some hard coal in 2025) is excluded from Energy-Charts' public-net series.
  - Reserve plants returning to market "to dampen prices" (coalition agreement 2025) would add
    coal TWh even after market exit.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| UK: years from ~22% coal share to a < 1% 12-month window | 1 | 2015 → ~2024 | ~9 years | DUKES / Carbon Brief (coal 39% 2012 → ~1% 2023; last plant shut 2024-09-30) | yes |
| Spain: ~15–17% → < 1% | 1 | 2017/18 → 2024 | ~6–7 years | REE (1.5% 2023, 0.6% 2024) | yes |
| Greece (lignite country): ~20% (2019) → still several % in 2025, phase-out pushed 2023→2025→2028 | 1 | 2019 → ? | > 6 years, still open | Böll / Enerdata / Argus | yes — lignite tail is sticky |
| European official coal-exit dates achieved vs missed (UK, PT, IE, AT, SE early/on time; IT, GR, FR slipped) | ~8 | 2015–2026 | ~60% on time or early; slippage concentrated where coal is domestic or system-critical | general knowledge, partly verified | yes, qualitative |
| Germany's own statutory schedule | 1 | → 2038-12-31 | implies "> 2038-12-27" | KVBG | yes, as status-quo anchor |
| Market-model predictions of an early German coal exit | several | 2019–2026 | track record: 2021 "CO2 price could trigger exit within 5 years" did **not** happen (coal still 22% in 2025/26) | CLEW 2021 | yes, discount models |

Outside-view synthesis: analog countries took 6–9 years from ~15–22% to < 1% → Germany
(22.4% in 2025) ≈ 2032–2034 if it behaved like UK/Spain; but Germany is lignite-heavy
(mine-mouth, inflexible, legally protected to 2038), the Greek lignite analog is slower, and
the statutory anchor sits beyond the question range. Outside-view median ≈ 2034–2035, with a
fat right tail (≥ 15% beyond 2038).

## Decomposition

Coal generation 2025 (public net, Energy-Charts): lignite 67.2 TWh, hard coal 26.7 TWh = 94 TWh
(≈ 22% share). H1 2026: lignite −3% y/y, hard coal +7% (gas price shock), coal ≈ 21.7%.

Blocks of remaining coal generation and when they go:

| Block | Rough TWh now | Statutory end | Market/political view |
|---|---|---|---|
| RWE Rhineland lignite (Neurath, Niederaußem, Weisweiler) | ~30 | 2030-03-31; 3 units possibly reserve to 2033 | RWE wants to close in 2030; decision on reserve delayed to spring 2027 |
| LEAG Jänschwalde + Boxberg N/P | ~12–15 | end 2028 / end 2029 | on track; units idle for long stretches in winter 2025/26 |
| Lippendorf (LEAG/EnBW), Schkopau (EPH/Uniper) | ~12–14 | 2035 / 2034 | could exit earlier on economics |
| Boxberg Q/R + Schwarze Pumpe (~3.1 GW) | ~15 | 2038-12-31 | LEAG (Jan 2026): "runs per the legal schedule" |
| Hard coal (market, incl. Datteln 4 to 2038) | ~27 | statutory reduction to 0 by 2038; 8 GW cap 2030 | many units into Netzreserve; rebounded in 2026 gas shock |

To get < 1% over 12 months: RWE gone (2030 or 2033), hard coal market generation ~0, and the
last ~5 GW of eastern lignite at very low capacity factor or closed. After 2035 only ~3.1 GW
lignite + Datteln 4 + reserves remain by law; at ~20% CF that is ~5–8 TWh ≈ borderline 1%.

Key drivers: EU ETS price path (EUA ~€80–86 mid-2026; July 2026 Commission proposal softens
LRF to 3.7%/1.7%, cap-zero 2039 → ~2048, but only ~€7/t lower by 2035; a Nordic bank sees
€180–270 by 2040); renewables/storage growth (62% renewables H1 2026); gas prices (2026
Hormuz shock); gas-plant buildout (StromVKG auctions: 4.5 GW bids 2026-09-08, 4.5 GW
2026-12-29, results ~2026-11-03 / 2027-02-23, delivery from Nov 2031); politics (CDU-led
coalition: exit tied to gas-plant build; reserve plants to dampen prices; east-German states
oppose acceleration).

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-04 | Metaculus #7218 aggregations (script) | CP 2033-09-24 [2031-01-19, 2036-05-22] n=29 recent / 46 total; Pro 2034-02-24 [2031-06-21, 2037-07-28] n=4; gold 2033-05-14 [2030-12-14, 2036-02-28] n=20. CP drifted ~1 yr later since Feb 2026 | anchor, noted after own view |
| 2026-10-04 | Fraunhofer ISE press release 2025 data | lignite 67.2 TWh, hard coal 26.7 TWh public net; 94 TWh coal | baseline |
| 2026-10-04 | Tagesspiegel 2026-01-02 | coal 22.4% (106 TWh gross) in 2025; solar overtook lignite | baseline; decline has flatlined 2024→2025 |
| 2026-10-04 | Windmesse/Strom-Report H1 2026 (2026-07-06); stromauskunft | lignite −3%, hard coal +7%, gas +18%; coal ≈ 21.7% | no acceleration; later |
| 2026-10-04 | CLEW 2026-08-11 "Government pushes coal exit stocktake to 2027" | §54/§56 KVBG review due 2026-08-15 delayed to late spring/early summer 2027, waiting for gas auctions; "security of supply from 2031" | later (policy waits on gas plants) |
| 2026-10-04 | Antenne NRW / Aachener Zeitung / cleanthinking | decision on Neurath F/G + Niederaußem K reserve to 2033 delayed to spring 2027; RWE (Krebber) sticks to 2030 | small later |
| 2026-10-04 | ClearBlue Markets, ICAP, CleanTechnica: EU ETS review proposal 2026-07-17 | LRF 3.7% 2031–35, 1.7% from 2036; cap-zero ~2048 instead of 2039; MSR intake 12%; prices ~22% lower 2030, ~€7 lower 2035; EUA €86 on 2026-07-22 | slightly later (softer 2030 price), not decisive |
| 2026-10-04 | Carbon Pulse 2026-09-09 | Nordic bank: EUAs €180–270 by 2040 under proposal | high late-2030s prices → tail compression |
| 2026-10-04 | gmk.center / LSEG | EUA ~€79–82 July 2026; LSEG Q3 2026 avg forecast €79 | baseline |
| 2026-10-04 | CLEW 2026-04-21 (Öko-Institut, Hauke Hermann) | market-driven coal exit likely 2031–2032 | earlier (expert model) |
| 2026-10-04 | CLEW / Aurora modelling (cited in 2026 preview) | last coal plant could close by 2033 | earlier (expert model) |
| 2026-10-04 | LEAG via Niederlausitz-aktuell 2026-01-13 | LEAG plans operation per legal schedule: Jänschwalde end-2028, Lippendorf 2035, Schwarze Pumpe/Boxberg end-2038 | later |
| 2026-10-04 | energiezukunft 2026-01-07 | only 3 of 8 LEAG units running early Jan 2026; Jänschwalde/Boxberg idle for days (wear-and-tear outages); LEAG: coal becoming "seasonal"; €1.75 bn EU-approved compensation | earlier (falling CF) |
| 2026-10-04 | BNetzA via Montel / techzeitgeist | no forced hard-coal closure needed for 2027 or 2029 (market exits outpace legal path); hard-coal Netzreserve ~8.07 GW winter 2026/27 | earlier for hard coal; path (a) blocked |
| 2026-10-04 | Coalition agreement CDU/CSU–SPD 2025 (PwC, zfk, cleanthinking) | 2038 kept; 2030 acceleration off the table; closures/reserve transfers tied to gas-plant build; reserve plants to be used to stabilise prices | later |
| 2026-10-04 | Handelsblatt 2026-03-19 | US attack on Iran / Hormuz blockade → gas price spike; industry (Steag Iqony) demands reserve-coal market return and delayed closures | later |
| 2026-10-04 | t-online 2026-08-31 | economy ministry examining reserve coal use against high prices; SPD opposed; govt: "not currently on the table" | small later; watch |
| 2026-10-04 | c-ober / pv magazine / iwr: StromVKG | law passed 2026-07-09/10; 2×4.5 GW auctions (bids 2026-09-08, 2026-12-29); delivery year from 2031-11 | gas backup only from ~2031–32 → coal backup role persists to then |
| 2026-10-04 | BNetzA Versorgungssicherheitsmonitoring 2025-09-03 | 22–36 GW new gas needed by 2035 | supply-security argument for keeping coal |
| 2026-10-04 | DUKES / Carbon Brief | UK coal 39% 2012 → ~1% 2023; last plant shut 2024-09 | outside view |
| 2026-10-04 | REE | Spain coal 1.5% 2023, 0.6% 2024 | outside view |
| 2026-10-04 | Greece lignite (Böll, Enerdata, pv-magazine) | lignite 20% (2019); exit dates slipped 2023→2025→2028 | lignite tail sticky |
| 2026-10-04 | Bundesrechnungshof 2024 coal-exit report | 2022 review was never done; government tends to miss review deadlines | process slippage |
| 2026-10-04 | CLEW 2021 "rising CO2 price could trigger German coal phase-out within 5 years" | did not materialise (coal 22% in 2025) | discount market models |

## Dead ends and ruled-out hypotheses

- Energy-Charts API (`api.energy-charts.info/public_power`) returned 503 on 2026-10-04 (4 tries);
  used Fraunhofer ISE press releases and press coverage for 2025/H1-2026 figures instead.
- Carbon Pulse and ScienceDirect (Energy Economics 2025 "coal phase-out in Germany and CWE under
  new framework conditions") were paywalled / 403 — abstract-level findings not retrieved.
- No Polymarket/Kalshi/Manifold/GJOpen/INFER market found on this question. Sentinel and Mantic
  have no matching forecast found.
- No 2026 evidence of a political push to extend lignite *beyond* 2038 (east-German premiers
  defend 2038, not later). Kept as a small tail only.

## Open questions to chase next time

- Energy-Charts monthly coal TWh for Jul–Sep 2026 (API down today).
- First StromVKG auction results (~2026-11-03): volume awarded vs 4.5 GW.
- Spring 2027 KVBG stocktake: RWE reserve 2030–33? 2035 acceleration for east?
- ETS trilogue on the July 2026 proposal (LRF, MSR, price-containment).
- Which generation metric would Metaculus admins use (Energy-Charts public net vs AGEB gross)?
