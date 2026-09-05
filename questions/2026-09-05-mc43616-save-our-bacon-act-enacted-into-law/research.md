# Research log — Will the Save Our Bacon Act be enacted into law before July 2027?

Working notes for v1 (2026-09-05).

## Question mechanics

- **Resolution source**: enactment of federal statute (Public Law) before 2027-07-01.
  Verifiable on congress.gov / govinfo. No data-release timing risk — this is an
  event question, not a series question.
- **Enactment routes allowed**: presidential signature, becoming law without signature,
  veto override. Standalone bill *or* a provision inside another vehicle (Farm Bill,
  appropriations, NDAA).
- **Explicitly excluded**: court rulings, executive orders, USDA rulemaking.
  → The Trump DOJ suit against California (filed 2026-07-09, egg provisions) and the
  2026-08/09 livestock executive orders are irrelevant to resolution.
- **Critical edge case (this is where the question is won or lost)**: the fine print kills
  a bill that (a) grandfathers existing state laws, (b) applies only prospectively to laws
  enacted after a cut-off, or (c) has a state opt-out. Nearly every *negotiated* Prop 12
  compromise on the table has one of those features. So the realistic "deal" outcome
  resolves **NO**, not YES. YES requires a clean, retroactive, no-opt-out preemption —
  i.e. essentially the House-passed text surviving intact.
- Pork coverage is what the question turns on; broader livestock coverage is permitted.
- Effective date does not matter, only enactment date.

## Timeline of the window

| Date | Event |
|---|---|
| 2026-09-05 | today; ~9.9 months to the deadline |
| ~mid-Sept 2026 | Boozman's planned second Senate Ag Committee business meeting |
| 2026-09-30 | 2018 Farm Bill (3rd extension) authorities lapse |
| 2026-11-03 | midterm elections |
| 2026-12-11 | FY2027 CR expires → year-end approps package, the main lame-duck vehicle |
| 2027-01-03 | 119th Congress ends; anything unenacted dies |
| 2027-07-01 | question deadline |

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| **This exact policy's own track record** — federal preemption of state farm-animal-welfare laws | 5 prior attempts (2006–2024): King Amdt in 2013/14 Farm Bill (passed House, stripped in conference), King Amdt 2018 (defeated in final negotiations), PICA/EATS 2019, EATS 2023–24, SOB/FSFPA 2025–26 | 20 yrs | **0/5 enacted** → Laplace 1/7 ≈ 14% *per multi-year attempt cycle*, not per 10-month window | Humane World Action Fund ("sixth failed attempt since 2006"); Harvard Animal Law; Barn Raiser | **Kept — dominant class** |
| House-passed provisions surviving Senate + conference when the Senate bill omits them | 2 directly comparable (2013/14, 2018 King Amdt) | — | **0/2** | as above | Kept, small n |
| Introduced bills → law, 119th Congress | ~15–19k introduced | 2 yrs | ~2–4% | congress.gov historical | Kept as a floor sanity check; H.R.4673 itself has **25 cosponsors, all R, zero committee action in 13.5 months** — below-median even for that class |
| House-passed bills → law | — | per Congress | ~20–30% | GovTrack historical | Rejected as primary: H.R.7567 is the vehicle, not this provision, and the Senate has written its own bill |
| Farm bills enacted in a lame-duck session | 2018 Farm Bill (Dec 2018) yes; 2023–25 cycle no (3 extensions) | — | ~1/2 recent | CRS R47659 | Kept for the P(farm bill) leg — **and note 2018 passed *because* the poison pills, King Amdt included, were dropped** |

Time-scaling: the dominant class is per *attempt cycle* (~4–5 years). Our window is
10 months **and** the Senate has already excluded the language once in this cycle, so the
per-cycle 14% must be conditioned down sharply, not used raw.

## Decomposition

P(YES) = sum over near-disjoint paths:

| Path | Chain | P |
|---|---|---|
| 1. Farm bill enacted in 119th **with clean SOB text** | P(farm bill enacted by 2027-01-03) ≈ 0.22 × P(any Prop 12 provision in final) ≈ 0.10 × P(clean, no grandfather/opt-out/prospective-only) ≈ 0.42 | ~0.9% |
| 2. Other 119th vehicle (Dec-2026 approps omnibus, NDAA) | P(big year-end package) ≈ 0.85 × P(clean SOB rides on it) ≈ 0.01 | ~0.8% |
| 3. 120th Congress, Jan–Jun 2027 | P(R keeps House) ≈ 0.2 × P(farm bill or vehicle enacted in first 6 months **and** carries clean SOB) ≈ 0.02, plus a sliver under divided government | ~0.5% |
| 4. Reconciliation (51 votes) | P(FY2027 reconciliation bill) ≈ 0.4 × P(survives Byrd rule as non-incidental) ≈ 0.05 × P(included) ≈ 0.15 | ~0.3% |
| 5. Model error / unknown unknowns | — | +0.4% |
| **Total** | | **~3.0%** |

The conjunction check bites hard on Path 1: it is *anti-correlated*. A farm bill that actually
gets 60 Senate votes is by construction one where the poison pills were traded away — which is
exactly what happened in 2014 and 2018.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-05 | metaculus-aggregations #43616 | CP 5.0% (n=37 recent, 61 total), Pro 3.0% (n=6), Gold 3.0% (n=16), as of 2026-09-04. Trajectory 40% (6/12) → 24% (6/24) → 12% (7/19) → 10% (7/26) → **5% (8/14)** → 5% today. Two step-downs: the 6/23 Senate draft omission and the 8/6 markup failure. | Anchor; cohorts converged, Pro/gold below CP |
| 2026-09-05 | govinfo BILLSTATUS 119hr4673 | SOB introduced 2025-07-23 (Hinson R-IA), **25 cosponsors, 25/25 Republican**, only action = referral to House Ag. No markup in 13.5 months. | ↓ Zero bipartisan base for a standalone path |
| 2026-09-05 | govinfo BILLSTATUS 119s1326 | Senate companion (Ernst, "Food Security and Farm Protection Act") introduced 2025-04-08, **8 cosponsors, all R**, no action since introduction (17 months). | ↓ Senate standalone path is dead |
| 2026-09-05 | govinfo BILLSTATUS 119hr7567 | House Farm Bill passed 2026-04-30, **224–200**; received in Senate 2026-05-19; latest action 2026-05-20 referral to Senate Ag subcommittee. XML current to 2026-08-14. **No Senate floor action at all.** | ↓ Vehicle is parked; Senate writing its own text |
| 2026-09-05 | Humane World Action Fund (June + Aug 2026 releases) | Boozman's 2026-06-23 Senate draft ("Agricultural Act of 2026" / Farm Bill 2.0) **omits SOB**. Framed as the "sixth failed attempt since 2006". | ↓↓ Primary driver |
| 2026-09-05 | RFD-TV, 2026-06-30, Boozman interview | Direct quote: *"We're going to need a number of Democratic votes in order to get this passed on the floor. So, because of that, we really haven't identified anybody who will step up and say that they're for this on the Democratic side."* | ↓↓ Chairman, from a pork state, states the votes do not exist. LR strongly against YES |
| 2026-09-05 | NSAC markup writeup; Farm Policy News; DTN | 2026-08-06 markup **failed 10–11** on party lines. >200 amendments filed, 48 voted; **no Prop 12 / SOB / EATS amendment appears among them**. Cause was SNAP error-rate cost-share (Ds wanted 2-yr delay, Rs offered 1). McConnell absent; a proxy vote cannot be the deciding vote. | ↓ Even SOB's own backers did not force a committee vote |
| 2026-09-05 | AgInfo (Zieba/NPPC) | NPPC: "the fight isn't over… we still have a bit of time in this Congress." Hopes Senate acts in Sept then **moves to conference**. This report says Prop 12 language "went down 10 to 11" — I read that as conflating the overall bill vote; NSAC's amendment list shows no SOB amendment. **Flagged as conflicting; low confidence.** | neutral; flagged |
| 2026-09-05 | Schiff / Padilla press release | **32 senators** (Schiff, Padilla, Booker, Markey + 28) wrote Boozman/Klobuchar objecting to S.1326 "in the next Farm Bill **or in any other legislation**". | ↓↓ 32 > 41 needed? No — but with 53R the majority needs 7 D votes; 32 public Ds against makes 60 unreachable |
| 2026-09-05 | Simon/McGovern/Costa release | **182 House Democrats** on record against H.R.4673. | ↓ Confirms the vehicle-independent opposition |
| 2026-09-05 | National Law Review; Daily Caller NF; Tampa Free Press | Luna(R-FL)–Garbarino(R-NY)–Fitzpatrick(R-PA)–Costa(D-CA) amendment to strike SOB, cosponsored by Mace(R-SC), Lawler(R-NY), Van Drew(R-NJ). **Rules Committee blocked it from a floor vote**; reporting says it had the votes to pass. | ↓ SOB may not command a House floor majority on its own merits |
| 2026-09-05 | Sentient Media | 16 House Rs signed an anti-EATS letter in 2023 on states'-rights grounds; TX Ag Commissioner Sid Miller opposes preemption. | ↓ GOP is not unified |
| 2026-09-05 | CRFB Appropriations Watch FY2027 | FY2027 CR **signed 2026-09-02, funds through 2026-12-11**. No FY2027 approps bill has cleared the Senate committee. Ag approps passed the House 213–210 on 6/4. | Sets the Dec-2026 lame-duck vehicle date |
| 2026-09-05 | Silver Bulletin / 270toWin / Wikipedia 2026 elections | Midterms 2026-11-03. Ds heavily favoured for the House; Senate near even. Generic ballot D+6–7 (early Aug); Trump approval high-30s. | ↓ Path 3 (120th Congress) nearly closed |
| 2026-09-05 | AgBull lame-duck analysis; Brownfield (Thompson) | Thompson wants to pre-conference in August and finish "maybe into the lame duck"; Boozman said passing before the midterms would take "a miracle". | Sets P(farm bill in 119th) ≈ 0.2–0.25 |
| 2026-09-05 | search summary (unverified) | Report that Boozman floated a compromise **grandfathering states with existing laws**. Could not verify against a fetchable primary source. | If true, ↓↓ — a grandfathered fix resolves **NO** by fine print. Left out of the load-bearing chain; recorded as a chase item |

## Dead ends and ruled-out hypotheses

- **Court / executive route.** DOJ sued California 2026-07-09 over Prop 12 egg provisions;
  Trump signed livestock EOs 2026-08 and 2026-09-04. Fine print excludes all of these.
  They matter only as indirect political pressure on Congress.
- **Standalone H.R.4673 / S.1326 passage.** Both parked in committee with R-only cosponsors
  and no action. Effectively zero.
- **congress.gov via WebFetch** returns HTTP 403 in this environment; `nationalhogfarmer.com`
  and `meatingplace.com` also 403; `archive.is` is blocked for WebFetch. Use the
  **govinfo BILLSTATUS bulk XML** (`https://www.govinfo.gov/bulkdata/BILLSTATUS/119/<hr|s>/BILLSTATUS-119<bill>.xml`)
  via `curl` instead — that works and is authoritative. Recorded so the next update does not
  re-discover it.
- **No prediction market found** on Kalshi, Polymarket or Manifold for this question or for
  2026 farm bill passage. Searched; nothing with volume. Sentinel/Mantic do not cover it.

## Open questions to chase next time

1. Did the mid-September Senate Ag business meeting happen, and did it report a bill?
   Was any Prop 12 amendment offered this time, and by whom?
2. Verify or kill the "Boozman floated a grandfather compromise" report from a primary source.
   Because a grandfather clause resolves **NO**, its existence is a *downward* tripwire even
   though it reads like progress for the pork industry.
3. Does the 2018 Farm Bill get a fourth extension on 2026-09-30 or in the December package?
   A fourth extension is the strongest single signal that the reauthorisation — and with it
   the only realistic SOB vehicle — has slipped past the question window.
4. Watch the December 2026 approps package text for a livestock-preemption rider, and watch
   whether any FY2027 reconciliation vehicle materialises.
5. Whether any Senate Democrat publicly moves toward a Prop 12 fix. Boozman's "not a single
   Democrat" is the load-bearing claim; a named defector is the highest-value update signal.
