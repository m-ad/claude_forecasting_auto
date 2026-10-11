# Research log — Will the Trump administration or a GOP state governor deploy armed officers or troops to a polling or early voting site in 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: Metaculus admins, on "credible sources" reporting (Bright Line Watch contributed question).
- Window: any time a site is open for in-person voting for the 2026 general elections. In-person early voting
  began ~2026-09-18 (MN, VA, …); DC 2026-10-26 → 11-01 plus Election Day 11-03; Shelby Co. TN 10-14 → 10-29;
  Miami-Dade 10-19 → 11-01. Closes 2026-11-02 13:00 UTC; resolves 2026-11-06.
- Edge cases and ambiguities:
  - "Armed with firearms" must be reported. No 2026 incident report so far states this explicitly.
  - Incidental proximity is excluded, as is any case lacking "uncontroversial credible reporting" of deliberate deployment.
  - Drop-box-only sites are excluded, so the DC Foggy Bottom Guard incident (2026-10-08) does not count.
  - County and city police are excluded; state troopers count only if ordered or specifically authorised by a GOP governor.
  - Runoffs (GA, LA in Dec) may arguably fall under "2026 general elections". Small extra mass.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Modern US general elections with deliberate armed federal / GOP-gov state-police deployment to open polls | ~14 federal generals 1970–2024, ~0 clear cases | 1970–2024 | ≈2–5% / election | § 592 compliance history; Texas 2020 "no plan for polling locations" | yes, as a floor |
| Trump-era 2025–26 elections: deliberate federal entries into open sites | Nov 2025 + 2026 primaries: 1 clear (Syracuse) + 1 alleged pair (Hennepin); 0 with armed reported | 2025-11 → 2026-09 | ~1–2 per primary season | Democracy Docket, WSKG, Common Cause | yes, main |

## Decomposition

- λ (deliberate federal entries at open sites during the general) ≈ 0.5–1.0, so P(≥1) ≈ 0.40–0.63.
  Use 0.40 for "occurs and credibly reported", after agent caution.
- P(counted | occurs) ≈ 0.45: armed must be established, deemed deliberate, ≤250 ft. P1 ≈ 0.18.
- P2 overt federal deployment ≈ 0.04; P3 GOP governor ≈ 0.03; P4 lenient incidental ≈ 0.025.
- 1 − 0.82·0.96·0.97·0.975 ≈ 0.26.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-11 | Metaculus 46051 via aggregations script | upcoming; opens 10-12; CP reveal 10-15; 4 forecasters; no comments | criteria digest |
| 2026-10-11 | DC Guard ballot drop box (Task & Purpose, Common Dreams, Hoodline) | 3 Guard members at the Foggy Bottom drop box on 10-08; JTF-DC: troops "directed not to monitor or secure polling locations"; 2,978 troops in DC (10-05), staying to 2029 | drop box excluded; P4 path only |
| 2026-10-11 | ICE at polls 2026 (Votebeat, NPR, AP, Civic Media) | DHS: "not planning operations targeting polling locations"; Mullin: warrants or threats possible; Patel won't rule out FBI | P1 kept moderate |
| 2026-10-11 | Syracuse ICE poll worker (Democracy Docket, WSKG) | 2026-06-23 primary: 2 ICE agents entered the open Central Library site to serve a notice; armed not reported | key Class-B datapoint ↑ |
| 2026-10-11 | Hennepin County lawsuit (Democracy Docket 10-07; Common Cause) | DHS investigators entered an early-voting site at the Government Center twice in 5 months (dates and purpose unclear); amended LULAC v. DHS adds DOJ/FBI and an alleged FBI policy allowing armed agents at polls | ↑ slight |
| 2026-10-11 | San Antonio (SA Current) | 2026-05-20: DPS traffic stop plus 9 ICE officers in a polling-site lot, runoff early voting; incidental | shows near-misses happen; would be NO |
| 2026-10-11 | Santa Maria CA (Democracy Docket) | 2026-10-05 ICE detention by a drop-box lot | excluded (drop box) |
| 2026-10-11 | DOJ monitors (Spotlight PA, CBS, Democracy Docket) | ~1,000 monitors planned; AZ primary used prosecutors plus 1 FBI special agent; Blanche 10-04: monitors not armed agents | P2 small |
| 2026-10-11 | Gen. Caine letter (AP 2026-08-31) | no plans for military or federalised Guard at polls | ↓ P2 |
| 2026-10-11 | Hegseth memo 09-22 (ABC, Wash Times) | cyber and intel only; no polling-site deployment | ↓ P2 |
| 2026-10-11 | Trump Time interview 10-01 (HuffPost, AP) | "don't rule anything out or in" on emergency / Insurrection Act; "Haven't thought of it" on ICE at polls | ≈ neutral, salience |
| 2026-10-11 | GOP governors (Georgia 11Alive; Landry New Orleans; Memphis) | Kemp: same as past; LA Guard left NOLA Aug 2026; Memphis Guard status in Oct 2026 unverified | P3 small |
| 2026-10-11 | Lawsuits (KAXE/NPR; Nation of Change) | LULAC v. DHS; DSCC/DCCC/DGA v. DHS/ICE/FBI (09-23); NAACP-led VRA §11(b) suit; no rulings yet | watch for PI |
| 2026-10-11 | Manifold API (5 markets) | 62.9% / 39.7% / 36.5% / 23.6% / 58.7% (1 trader); all broader or low volume | discounted cross-check |
| 2026-10-11 | Polymarket gamma public-search ("polling", "troops polls", "ICE polls", "National Guard polling") | no relevant market | — |
| 2026-10-11 | Kalshi API | 429 rate-limited; web search found no matching market | — |
| 2026-10-11 | Votebeat 37-expert survey | 27/37 at least somewhat likely: some military or law enforcement at or near polls | broad; ↑ slight |
| 2026-10-11 | Miami ICE impersonator (ABC) | fake ICE agent arrested at a Miami polling site | shows false-positive reports will occur; needs real-agency verification |

## Dead ends and ruled-out hypotheses

- No Sentinel, Mantic, GJOpen or INFER question found.
- Texas DPS deployment to polls in 2022–26: nothing found (only Abbott's 2020 Guard to cities, explicitly not at polls).
- Washington Post "troops loitering by mistake" article not directly retrievable; the Guard's statement is via Task & Purpose.
- Whether the DC Guard is armed in Oct 2026: not confirmed.
- Dodger Stadium Nov 2025: no source confirms an active vote center within 250 ft.

## Open questions to chase next time

- Metaculus CP / Pro / gold after the 2026-10-15 reveal; read the comments for the resolver's stance on Syracuse-type events and "armed".
- Dates of the Hennepin early-voting-site entries: inside the general window (≥ 2026-09-18)? If so, were the agents armed?
- PI hearing dates in LULAC v. DHS and DSCC v. DHS.
- Any DHS field guidance on polling places.
- Memphis Tennessee Guard status, and its proximity to Shelby Co. early-vote sites (10-14 → 10-29).
