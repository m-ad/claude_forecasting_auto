# Research log — What percentage of the EU hen flock will be sexed with in-ovo sexing technology in Q1 2027? (MC 43279)

Paired with `2026-09-19-mc43280-percentage-us-hen-flock-sexed-with-ovo`. Same resolver, same
source documents — read both logs together; the US log carries the producer-level detail.

## Question mechanics

- **Resolution source**: Innovate Animal Ag (IAA), a US non-profit think tank. No official
  statistical series exists. IAA surveys the in-ovo sexing vendors directly for hen volumes
  and divides by its own EU commercial-layer flock estimate.
- **Metric**: "Share of EU **Commercial** Layer Hens Sexed In-Ovo" (40% in the 2026 report),
  explicitly **not** the newly introduced "including backyard production" metric (35%) —
  admin `skmmcj`, 2026-07-30.
- **Release schedule (this is the crux)**:
  - Annual market-penetration report: April 2024, April 2025, **July 2026** (as-of 1 June 2026).
  - "Yearly Recap" blog: 2026-01-04 for 2025 — **restated** the April-2025 figure, did not
    measure anything new.
  - Quarterly roundups: 2025-06-30, 2025-10-01, 2026-03-31, 2026-07-01 — installation news,
    **no penetration percentages** (checked Q2 2026 directly).
- **Criteria were edited** (admin, 2026-07-30) from "as of Q1 2027" to "the first such
  non-preliminary number published by IAA in 2027", because the report timing moved. **The
  title was not updated** and still says "in Q1 2027".
- **Edge cases and ambiguities**:
  1. *Does a January-2027 Yearly Recap restating the June-2026 40% count as "the first such
     number published in 2027"?* Text says yes; intent (and the title) say no. This is the
     dominant uncertainty — weighted 0.25.
  2. *Denominator revisions.* IAA restated April-2025 from 28% to 34% between reports by
     narrowing the EU flock from 393 M (incl. backyard) to ~340 M (commercial only). Admin
     ruled this is **not** a criteria change, so it does not annul — it just moves the number.
     Arithmetic check: 20% × 389/340 = 22.9% ≈ the restated 23% for April 2024, and
     28% × 393/340 = 32.4% ≈ 34%. The series is internally consistent.
  3. *Annulment* if nothing comparable is published. Costless for the ledger; I forecast
     conditional on resolution.
- **Stock, not flow.** IAA counts hens in the standing flock, not chicks hatched. Confirmed by
  their own Italy commentary: an 18-month flock cycle means a hatchery mandate produces "a
  progressive increase in penetration rather than a single step."

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| IAA's own measured EU series, 2026-rebased basis | 3 points | 2024-04 → 2026-06 | 23% → 34% → 40%; **+11 pp then +5.1 pp/yr** | IAA 2026 report | **Kept — this is the outside view** |
| IAA's own forward base case | 1 | 2026-06 → 2028-07 | 51% (range 47–55%), i.e. +5.3 pp/yr | IAA 2026 report | Kept — the resolver's own view, and it does *not* assume re-acceleration |
| Generic technology-diffusion S-curve (IAA's "147% CAGR, faster than LED/iPhone/colour TV") | — | 2020–2024 | implies acceleration | IAA background text, quoted in the question | **Rejected** — the EU curve is regulation-driven, and pp-increments are already decelerating |
| Non-EU national launches (Switzerland 85–100%, Norway >50%) | 2 | 1.5–4 yrs | fast | AgFunderNews 2026-09-09 | Not applicable — neither is in the EU denominator |

## Decomposition

2026-06-01 → 2027-06-01 increment:

| Driver | Mechanism | pp |
|---|---|---|
| Italy | Ban in force 2027-01-01 (guidelines Oct 2025, day-14 requirement). ~40 M layers = 11.8% of the EU commercial flock. Chicks hatched Jan 2027 enter lay ~May 2027 ⇒ only 10–20% of Italy's flock converted by 2027-06-01 | +1.2 … +2.4 |
| DE / FR / NL | Near saturation; France's white-layer exemption still in force; the Dutch phase-out covers only the 6–7 M hens supplying Dutch table eggs, and Dutch hatcheries already run in-ovo sexing for Germany | +0.5 … +1.5 |
| ES / PL / BE / Nordics | Retailer-led, no mandate | +0.5 … +1.5 |
| EU-level anticipation | Commission Livestock Strategy 2026-07-07 promises a proposal by end-2026; a proposal moves capex, not flocks | 0 … +0.5 |
| **Total** | | **+2.5 … +5.5, centre +4.5** |

⇒ ~43.5% at 2027-04-01, ~44.5% at 2027-06-01. Slightly below naive linear extrapolation
because Italy is back-loaded — which is exactly the convexity IAA's 51%-by-2028 path needs.

Capacity is not binding: Cheggy 20–25 k eggs/h, Omegga Plus up to 50 k/h, HatchTech/Seleggt
~33 M eggs/yr; the EU needs ~400–450 M hatching eggs scanned per year for full coverage.
Binding constraints are willingness to pay (~1 eurocent/egg) and regulation.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-19 | `metaculus_aggregations.py 43279 --comments 10 --history` | CP 41.69 [38.25, 45.08] n=29; Pro 41.35 n=6; gold 41.36 n=15. CP opened ~33.9 on 2026-06-12, stepped to ~41.7 after the July 2026 report printed 40% | Anchor; the step shape suggests the crowd prices "last published number + a little" |
| 2026-09-19 | Comments on 43279 | Admin clarified metric, ruled the 28→34 revision non-breaking, and edited criteria to "first number published in 2027" | **Largest single driver**; created scenario 1 |
| 2026-09-19 | innovateanimalag.org/market-penetration-forecast | 40% at 2026-06-01; 34% at 2025-04-01; 23% at 2024-04-01; 51% base case by July 2028 (47–55%); Italy named as the main 2027–28 driver; flock ~328–346 M; backyard ~42 M | Set the trend and the resolver's own view |
| 2026-09-19 | innovateanimalag.org/blog (index) | Publication cadence: Yearly Recap 2026-01-04; quarterly roundups 2026-03-31, 2026-07-01 | Made the timing scenarios concrete |
| 2026-09-19 | IAA Q2 2026 quarterly roundup | Installation news only, **no penetration %** | Ruled out quarterly roundups as a resolver |
| 2026-09-19 | IAA 2025 Yearly Recap (2026-01-04) | Restates the Q1-2025 28% figure; Germany ~70% at start of 2024; ~175 M male embryos separated since 2022 | Established that the recap restates rather than measures |
| 2026-09-19 | AgFunderNews 2026-09-09 | EU 40%; Switzerland 85%; Norway 52%; Cheggy 20 k eggs/h brown-only; Omegga Plus 50 k/h; Seleggt 33 M eggs/yr | Capacity is not the constraint |
| 2026-09-19 | Italy ban: Eurogroup for Animals, Animal Equality, FoodTimes | Guidelines published Oct 2025; in force 1 Jan 2027; sexing by incubation day 14; ~34 M chicks/yr spared; **ban adds ~40 M layers to EU penetration** | Sized the Italy driver at 11.8% of the flock |
| 2026-09-19 | EU Commission Livestock Strategy, 2026-07-07 | Proposal to end systematic male-chick killing promised by end-2026; no law yet | Small upward nudge; no flock effect by 2027 |
| 2026-09-19 | Netherlands roadmap (IAA blog, WATTPoultry) | Voluntary, covers only 6–7 M hens supplying Dutch table eggs; Dutch hatcheries already equipped for Germany; €0.009/egg | **Downward** — I had over-weighted NL as a 2027 driver |
| 2026-09-19 | France24/AFP | France retains a **legal exemption for white-feathered layers** (>10% of male chicks) | Downward — "banned" ≠ 100% |
| 2026-09-19 | PubMed: `in ovo sexing poultry hatchery` 2025– | Chen et al. 2026 (DOI 10.3389/fbioe.2026.1785893): existing methods strain-limited or require exogenous DNA, "none meet commercial requirements" generally | Confirms incremental, not step-change, diffusion |
| 2026-09-19 | Kalshi / Polymarket / Manifold / Sentinel / Mantic / GJOpen / INFER | No in-ovo sexing market or question found anywhere | Metaculus is the only forecaster comparison available |

## Dead ends and ruled-out hypotheses

- **MDPI review** *Addressing Two Systemic Bottlenecks in Global Poultry Production* (Animals
  16(15):2370) and the ScienceDirect review *Ban of day-old chick culling* — both returned
  **HTTP 403** through the proxy. Not cited. Try a PMC mirror next time: PMC13465435 appeared
  in search results for the MDPI one.
- **Spain / Poland retailer or government commitments with a 2027 date** — searched in English
  and with Spanish/Polish phrasings. **Nothing found.** Mild evidence against re-acceleration;
  worth one more attempt in-language next update.
- **EU capacity shortfall / hatchery backlog** — searched; no evidence of one. Capacity is not
  the constraint.
- **A live IAA "tracker" or dashboard with a continuously updated penetration number** — IAA
  runs an HPAI dashboard and an Egg Chartbook, but penetration appears only in the annual
  report. Ruled out.
- **Direct Metaculus REST/`curl`/`WebFetch`** — 403 as documented. The aggregations script also
  failed with `status 0` until `METACULUS_FORCE_TLS12=1` was set; with that env var it works
  in ~60 s. **Record this for the next session** — `scripts/new_question.py` needs it too.

## Open questions to chase next time

1. Does IAA's 2026 Yearly Recap (expect ~2027-01-04) contain a penetration percentage, and if
   so is it a restatement of 40% or a fresh end-2026 measurement? **This single fact resolves
   most of the band.**
2. Has the admin clarified whether a restated prior-period figure counts? Worth asking on the
   question thread before it closes on 2026-12-31.
3. Italian hatchery readiness: how many in-ovo sexing machines are installed in Italy as of
   Q4 2026? No source found for this yet — try Assoavi, Unaitalia, Zootecnica International.
4. Does IAA plan another denominator refinement for 2027? The 393 M → ~340 M change was worth
   ~6 pp on the printed number.
5. Italy's exact commercial layer flock — I used ~40 M from the "adds ~40 million layers"
   framing in the Italy coverage. Cross-check against Eurostat `apro_ec_poula` next update.
