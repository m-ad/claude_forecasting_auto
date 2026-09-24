# Research log — Will FEWS NET classify any area of Sudan as experiencing Famine before 2027?

## Question mechanics

- **Resolution source**: FEWS NET (Famine Early Warning Systems Network) classification maps
  for Sudan, https://fews.net/east-africa/sudan. The map's **"Reported" date** must fall
  after August 2026 and before January 2027 → roughly the maps published Sept–Dec 2026.
- **Release schedule**: FEWS NET runs a Food Security Outlook (FSO) roughly Feb / June / Oct,
  an Outlook Update at the mid-points, and Key Message Updates (KMU) in the remaining months.
  Latest publication as of 2026-09-05 is the **KMU July 2026 – January 2027**. Expect
  ~3–5 qualifying map publications in the window (Sept KMU, Oct FSO, Nov KMU, Dec Update).
- **What counts**: at least one *area, urban settlement, or settlement of displaced
  populations* in **IPC Phase 5: Famine** with solid **or reasonable** evidence, **for the
  current period**. The IDP-settlement clause is a materially lower bar than a whole
  administrative locality — FEWS NET's Aug-2024 Zamzam classification is exactly this shape.
- **Edge cases / ways this resolves counter-intuitively**:
  - **Phase 4 "!"** (would be Phase 5 without assistance) is explicitly excluded by fine print.
    FEWS NET uses "!" liberally in Sudan.
  - **"Risk of Famine"** language (which FEWS NET currently uses for 7 North Darfur areas plus
    Dilling and Kadugli) is NOT a Phase 5 classification. This is the single most likely way
    to misread the question: FEWS NET's Sudan pages are saturated with the word "Famine"
    while classifying nothing in Phase 5.
  - **Projection ≠ current period.** A map projecting Famine for Feb–May 2027 does not count.
  - An IPC/FRC declaration alone does not resolve YES — it must appear on a FEWS NET map.
    (In practice FEWS NET adopts FRC conclusions quickly, so this is a soft distinction.)
  - FEWS NET publication itself is not guaranteed: in mid-Aug 2026 the State Department
    suspended FEWS NET reporting on Somalia, Yemen and Afghanistan. Sudan was not suspended,
    but a suspension of Sudan reporting would mechanically force NO.

## Timeline reconstruction (the thing that decides this question)

| Date | Event | FEWS NET Sudan Phase 5 in current period? |
|---|---|---|
| Aug 2024 | Zamzam IDP camp classified Famine (FRC + FEWS NET) | YES |
| Dec 2024 | Expanded: Abu Shouk, Al Salam, W. Nuba Mountains | YES |
| 2025 | USAID dismantled; FEWS NET offline for a period, then resumed | partial |
| Sep/Oct 2025 | IPC FRC confirms Famine in **El Fasher town** and **Kadugli town**; 20 more areas at risk | YES |
| late Oct 2025 | **El Fasher falls to RSF** after ~18-month siege — siege mechanism ends, population disperses | YES (Dec 2025 update: famine "expected to persist") |
| end Jan 2026 | **Dilling siege broken**; Kadugli breakthrough imminent | transition |
| Feb 2026 | FEWS NET: *"Famine thresholds no longer met, but credible risk of Famine persists"* | **NO** |
| 18 Feb 2026 | First major UN convoy into Dilling/Kadugli in 3 months (130k people) | NO |
| Mar–Aug 2026 | Continuous "risk of Famine" language; no Phase 5 classification | **NO** (7 straight months) |
| Jul 2026 | KMU Jul 2026 – Jan 2027: risk of Famine in 7 NW/central North Darfur areas + Dilling/Kadugli; **Famine not projected as most likely anywhere through Jan 2027** | NO |

The two areas that carried the last Famine classification both had their causal mechanism
removed: El Fasher's siege ended by capture, Kadugli/Dilling's by relief. That is *why*
thresholds stopped being met, and it is the central status-quo argument for NO.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| A. FEWS NET "credible risk of Famine" designations converting to a current-period Phase 5 classification within ~4 months (global: Yemen 2017–19, Ethiopia/Tigray 2021, S. Sudan 2020–22, Somalia 2022, Afghanistan 2021–22, NE Nigeria 2016/2021, Sudan 2024–26, Gaza 2024–25) | ~25–30 episodes | 2011–2026 | ~10–15% | FEWS NET alert archive | **kept — primary** |
| B. 4-month windows since Aug 2024 in which a FEWS NET Sudan map carried current-period Phase 5 | 6 | Aug 2024 – Aug 2026 | ~4.5/6 ≈ 75% | timeline above | kept as **upper** bound; badly conditioned — it averages over the siege era that has ended |
| C. Windows since the Feb-2026 de-classification | 2 (Feb–May, Jun–Sep 2026) | 2026 | 0/2 | FEWS NET | kept as **lower** bound / status-quo anchor |
| D. Global famine *declarations* per year (any country, any system): Somalia 2011, S. Sudan 2017, Sudan 2024, Gaza 2025, Sudan 2025 | 5 | 2011–2026 (16y) | ~0.3/yr worldwide → ~0.1 per 4-month window worldwide | IPC/FRC records | kept as sanity floor; but Sudan is *the* modal case, so this floor is not binding |

Class A is the right class: the state of the world is "FEWS NET says credible risk, not
famine". Class B is the trap — it is conditioned on a siege configuration that no longer exists.
Anchor ≈ **12–15%**, adjusted upward for Sudan-specific conversion history (2 conversions since
2024, i.e. Sudan converts at well above the global rate) and for having 3–5 shots on goal.

## Decomposition (paths to YES)

`P(YES) = 1 − Π(1 − p_i)` over roughly-independent paths:

| Path | Mechanism | p |
|---|---|---|
| A. **NW/central North Darfur** (Um Baru, Kernoi, At-Tine) | GAM already far past the 30% famine threshold (Um Baru **52.9%**, SAM 18.1%; Kernoi **34.0%**, Dec-2025 surveys). Driest rainfall in the 40-year record → essentially no Oct harvest. Population "largely unreachable by humanitarians". Missing leg is **mortality + food-consumption evidence**, and access is getting worse, not better. FEWS NET has held this GAM data for ~9 months without classifying. | 0.12 |
| B. **El Obeid** (North Kordofan) | ~500,000 trapped incl. 105,000 IDPs; drone-enforced siege ~18 months; food prices +300%; WFP (Jul 2026): food stocks "critically depleted by September, exhausted by October", nutrition supplies out from August. This is the El Fasher pattern. But classification lag from siege-tightening to FRC confirmation ran ~18 months (El Fasher) and ~30 months (Kadugli); Zamzam's 3-month turnaround needed a pre-existing camp survey. | 0.08 |
| C. **Kadugli / Dilling re-encirclement** | Relief corridor since Feb 2026 is described by FEWS NET as volatile and heavily contested; re-siege would re-cross thresholds fast because the population is already in Catastrophe. | 0.06 |
| D. **An IPC/FRC round in Nov–Dec 2026** lowers the evidentiary bar somewhere not covered above, and FEWS NET adopts it on its Dec map | Post-harvest IPC rounds for Sudan have historically landed Sept–Dec. Mostly overlaps A–C; counted as marginal only. | 0.04 |

`1 − (0.88 × 0.92 × 0.94 × 0.96) = 0.269`

Haircuts applied to that 26.9%:
- **−4 pp**: FEWS NET's own Jun/Jul 2026 projection explicitly does *not* carry Famine as the
  most-likely outcome anywhere through Jan 2027. The organisation that resolves this question
  has told us what it currently expects to publish.
- **−3 pp**: the qualifying window (Oct–Jan maps) is the post-harvest period. Even a very bad
  harvest is a *marginal improvement* over the Aug–Sep lean-season peak for most areas.
- **+1 pp**: the IDP-settlement clause is a low bar, and there are 3–5 map publications.
- Political constraint on FEWS NET (State Dept suspensions of Somalia/Yemen/Afghanistan in
  Aug 2026): considered and **not** applied as a haircut — FEWS NET published Famine
  classifications for Sudan in Oct–Dec 2025 under this same arrangement.

→ **≈ 20%**.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-05 | FEWS NET Sudan country page | Latest publication = KMU Jul 2026 – Jan 2027; **no area in Phase 5**; credible risk in 7 NW/central N. Darfur areas + Dilling/Kadugli towns | anchors NO; sets the status quo |
| 2026-09-05 | FEWS NET FSO June 2026 | Explicit: no area currently Phase 5; harvests Oct–Jan give no meaningful relief on front lines; assistance ≈ 20% of need (3.2M of 22M), planned targeting *falls* to 3.4M/month Oct–Dec on funding shortfalls | mildly ↑ (need unmet) but ↓ on classification (they project no famine) |
| 2026-09-05 | FEWS NET KMU July 2026 | North Darfur rainfall 20–30 days late, driest in the 40-year record; planting 2–4+ weeks behind; cholera expanding; ~half of 19 nutrition surveys in 2026 above the Critical GAM threshold, concentrated in western Sudan | ↑ on conditions |
| 2026-09-05 | FEWS NET Feb / Mar / May 2026 | "Famine thresholds no longer met"; risk persists — 7 consecutive months of NO | ↓↓ status quo is sticky |
| 2026-09-05 | IPC "countries in focus" issue 143 + Save the Children | Um Baru GAM 52.9% / SAM 18.1%; Kernoi GAM 34.0% (Dec-2025 surveys) — famine *malnutrition* threshold already surpassed | ↑ strongly on Path A; but note FEWS NET has not converted it in 9 months |
| 2026-09-05 | IPC Feb 2026 – Jan 2027 special report / UNICEF May 2026 | ~135,000 people in Catastrophe across **14 hotspots**; risk of Famine under a reasonable worst-case; no area currently in Famine | confirms the "risk not classification" state |
| 2026-09-05 | Al Jazeera 2026-07-06 "El-Obeid under siege"; WFP Jul 2026 | ~500k trapped incl. 105k IDPs; 18 months of drone-enforced siege; food +300%, water ×2; stocks exhausted by Oct; analyst: outcome "will likely prove identical" to El Fasher | ↑ opens Path B |
| 2026-09-05 | IPC FRC Sudan Oct 2025 report; WFP/UNICEF Nov 2025 | El Fasher + Kadugli Famine "plausible" with reasonable evidence; Dilling undeterminable for lack of data | establishes the evidentiary bar and the data-gap failure mode |
| 2026-09-05 | Al Jazeera / allAfrica Oct 2025 | El Fasher fell to RSF late Oct 2025 after ~18-month siege | ↓ removes the mechanism behind the last classification |
| 2026-09-05 | Arab News / FDD / UNICEF Feb 2026; WFP-UNICEF-UNDP convoy 2026-02-18 | Dilling siege broken end-Jan 2026, Kadugli soon after; first major convoy in 3 months reached 130k | ↓ explains the Feb de-classification |
| 2026-09-05 | NPR/KPCW 2026-08-31 "US famine alert system … shut down, then reopened" | FEWS NET operational but State-Dept-directed; **reporting on Somalia, Yemen, Afghanistan suspended mid-Aug 2026**, resumption promised for September; State says coverage varies with "policy priorities" | ↓ small: adds a tail where Sudan reporting thins; also a mechanical-NO tail |
| 2026-09-05 | Search: Sentinel Team / Kalshi / Polymarket / Manifold on Sudan famine | **No matching market or published probability found** | no external anchor available |

## Dead ends and ruled-out hypotheses

- **"Famine was declared in Sudan, so it is still classified."** Wrong for FEWS NET: the
  Sep/Oct-2025 El Fasher + Kadugli classification was withdrawn in Feb 2026. Several
  secondary sources (IRC, aggregator blogs) still write "famine confirmed in El Fasher and
  Kadugli" in present tense in Aug 2026. They are describing the Oct-2025 FRC finding.
- **Using the IPC as a proxy for FEWS NET.** They diverge: the IPC/FRC classification is a
  periodic committee product; FEWS NET maps are monthly and were the *first* to carry Zamzam.
  Both currently say no Famine.
- **Sentinel Team / prediction markets**: searched, nothing on Sudan famine classification.
- Low-quality aggregator blogs (world-on-fire.com, thehuman-rights.com, akaracookie.wordpress)
  surfaced in search and were **not** used — unverifiable, and they repeat the stale
  "famine confirmed" framing above.

## Open questions to chase next time

1. Did the **Sept/Oct 2026 FEWS NET map** publish, and what "Reported" date does it carry?
2. Is a **new IPC Sudan round / FRC review** convened for Q4 2026? That is the highest-leverage
   unknown — it is the mechanism that produced both prior conversions.
3. Any **mortality (CDR) survey** from NW North Darfur or El Obeid? Mortality is the missing
   evidentiary leg, not malnutrition.
4. El Obeid: does the RSF close the last road, and does WFP's "stocks exhausted by October"
   forecast verify?
5. Was Sudan added to the State Department's list of suspended FEWS NET country reporting?

---

## 2026-09-24 — v2 re-analysis log

- **Metaculus** (`raw/metaculus-2026-09-24.json`): CP 32% [27,36] n=112; Pro 27% [25,35] n=10; gold 28.7% [27,34.8] n=34.
  At reveal 2026-09-09 17:03Z: CP 44%, gold 44%, Pro 33%. CP low ~25% on 15 Sep. The comments
  add no new facts. One commenter had misread "solid only" and corrected it. Another anchors 35–45% on headline language.
- **FEWS NET Aug 2026 Outlook Update** (published 2026-08-31, data to 31 Aug): Phase 4 widespread. *Households*
  in Phase 5 in Um Baru, Kernoi, At-Tiné, and among El Obeid, Kadugli and Dilling IDPs. "Credible risk of Famine
  through January in seven areas". The Famine scenario is conjunctive (escalation + resumed sieges +
  marginal/no harvest). 26 SMART surveys, 12 > 15% GAM, max 26.6% (Beida). No mortality data. WFP
  reached 3.2M in July (<20% of need). ~1.5M more expected to lose aid by year-end.
- **FDW API** (`fdw.fews.net/api/ipcphase/?country_code=SD…`, works without auth; summary in
  `raw/fewsnet-fdw-phase-counts-2026-09-24.json`): Aug 2026 near-term has 0 Phase 5 units (167×P4).
  Phase 5 units exist on maps Jun 2024 – Jan 2026 and on none from Feb 2026 on. **The June 2024 map
  already had 1 Phase 5 unit, i.e. before the Aug 2024 FRC.** This corrects v1's "FRC is the
  mechanism" framing. Useful tool for future checks: count `value==5.0` by `reporting_date`.
- The Aug-31 map is "Reported" August, so it does not qualify. Remaining qualifying maps: Sept KMU, Oct FSO, Nov KMU, Dec KMU.
- **El Obeid**: RSF holds the N/W/S sides, the eastern SAF supply route is open. Heavy drone use (27 events in June). ~15k
  families displaced in since early Aug. Not fully encircled.
- **WFP** (The National, 14 Sep): $206M in 2026 vs $645M in 2025, needs $300M, cut-backs "within weeks". Tawila
  ~950k on half rations. Darfur's driest season since 1984.
- **Dead ends**: no FRC or new IPC Sudan round announced (searched "IPC Famine Review Committee Sudan
  September 2026", "IPC Sudan update October 2026"). No State Dept suspension of Sudan found. Could
  not retrieve the Aug map PNG or geojson links from the fews.net HTML (JS-rendered). Used FDW instead.
