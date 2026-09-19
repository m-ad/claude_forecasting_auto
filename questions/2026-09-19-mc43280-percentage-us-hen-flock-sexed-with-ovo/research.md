# Research log — What percentage of the US hen flock will be sexed with in-ovo sexing technology in Q1 2027? (MC 43280)

Paired with `2026-09-19-mc43279-percentage-eu-hen-flock-sexed-with-ovo`. Same resolver and
much of the same source set; the EU log carries the resolver-cadence detail and the EU
trend, and both are needed for an update.

## Question mechanics

- **Resolution source**: Innovate Animal Ag (IAA). Vendor survey ÷ IAA's own flock estimate.
  No government series.
- **Criteria**: "the percentage of the US' hen flock that was sexed with in-ovo technology
  according to official Innovate Animal Ag reporting **as of Q1 2027**."
- **Fine print**: if Q1-2027 reporting is not released **before July 2027**, or if IAA changes
  criteria so prior reporting is not comparable → another comparable source, else **annulled**.
- **Asymmetry with the EU question**: #43279's criteria were edited on 2026-07-30 to "the
  first such number published in 2027" because IAA moved its report from April to July.
  **#43280 was not edited** and keeps the Q1-2027 as-of requirement plus the July backstop.
  Given the 2026 report was published in July with a 1 June as-of date, the annulment branch
  is live. Annulment is costless for the ledger, so I forecast conditional on resolution and
  spread weight over plausible as-of dates.
- **Stock, not flow.** IAA counts hens in the standing flock. This is the key mechanic:
  with ~180 M pullets placed per year against a 307.9 M-hen flock, full turnover takes ~1.7
  years, so a producer converting its hatchery input on 1 Jan 2027 has converted ~15% of its
  own standing flock by mid-2027.
- **Published US data points**: "<1% of the US' ~310 M head commercial layer flock" in **both**
  the 2025 and the 2026 report. IAA explicitly **declines to forecast** the US: "Given the
  uncertainties here, we opted not to make a numerical forecast for the US market."

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| US flock turnover ceiling | — | — | ~180 M pullets/yr vs 307.9 M hens ⇒ ~1.7 yr to replace the flock | USDA NASS; WATTPoultry Feb-2026 figure | **Kept — the hard cap** |
| UEP's 2016 pledge to end culling by 2020 | 1 | 2016–2020 | Negotiated with The Humane League; conditioned on "commercially available and economically feasible"; **never delivered** | CSMonitor 2016-06-12; UEP statement | **Kept — closest US precedent, and negative** |
| EU from its own sub-1% start | 1 | 2020–2024 | ~2% → 23% over 4 yrs | IAA | Partly — EU growth was mandate-driven, the US has no mandate |
| Norway / Switzerland voluntary launches | 2 | 1.5–4 yrs | Norway 22% at 18 months; Switzerland 85–100% | IAA, AgFunderNews | **Discounted** — small, concentrated markets with one or two dominant hatcheries; the US has ~50 significant producers and 90% white eggs |
| IAA's "147% CAGR, faster than LED/iPhone/colour TV" framing (quoted in the question background) | — | — | implies S-curve take-off | IAA | **Rejected for the US** — see the misconception note in `forecast.md` |

## Decomposition

Bottom-up against USDA's 307.9 M table-egg layers (1 Feb 2026):

| Producer | Basis for the number | Hens Jun-2026 | Added by ~Jun-2027 |
|---|---|---|---|
| NestFresh (Hidden Villa Ranch) | 100% converted as of June 2026 on **>800,000 chicks cumulative** since 2025 ⇒ whole laying flock well under 1 M | 0.8 M | 0.1 M |
| Sauder's Eggs | Commitment limited to *new* Free Range / Organic / Pasture Raised flocks packed after Aug 2026, "provided their source can meet demand" | 0.3 M | 0.4 M |
| Kipster USA | Own brand launches early 2027 | 0.2 M | 0.1 M |
| Vital Farms | >10 M-hen network; in-ovo birds "scheduled to **arrive at its farms in early 2027**" via Hy-Line NA's Cheggy | 0.0 M | 2.0 M |
| McLean Farms + other early adopters | scattered press mentions | 0.4 M | 0.3 M |
| Unattributed, to reconcile with IAA's sub-1% Jun-2026 base | residual | 0.9 M | 1.2 M |
| **Total** | | **2.6 M** | **4.1 M ⇒ ≈2.2%** |

Structural brakes, in order:
1. **No mandate.** Walmart names in-ovo sexing as a supplier "focus area" (Feb 2025) with **no
   deadline and no share**. UEP's Hatch Check (June 2025) is a labelling/audit scheme, not a
   commitment; UEP's stated position is "when it is economically and operationally feasible".
2. **White eggs.** ~90% of the US market. Cheggy is hyperspectral feather-colour ⇒ brown only.
   White-capable: Respeggt, Orbem MRI (2 US machines, 3rd in 2027), MatrixSpec/SANOVO HyperEye
   (day-4, white+brown) with global launch **late 2026 / early 2027** — too late for a Q1-2027
   *stock*.
3. **~1 US cent per egg** pass-through, unproven with consumers.
4. **HPAI churn** — 12.4 M layers depopulated in 2026 to date. Cuts both ways; no evidence
   replacement chicks are in-ovo sexed.

Capacity is **not** binding: two Cheggy machines at Hy-Line NA could scan ~200–300 M eggs/yr
at high utilisation against ~400 M needed for the whole US flock; Orbem puts national
coverage at 12–15 large hatcheries.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-19 | `metaculus_aggregations.py 43280 --comments 10 --history` | CP 3.23 [1.72, 5.48] n=30; Pro 3.63 n=6; gold 3.35 n=15. CP opened ~6.6 on 2026-06-12 and fell to ~3.2 | Anchor; the crowd has already revised **down** once |
| 2026-09-19 | Comment by `jvlegend`, 2026-07-05 | "median stays in the low single digits, with upside if one or two large US integrations adopt quickly" | Confirms the crowd's reasoning shape; no new facts |
| 2026-09-19 | IAA 2026 report | US **<1%** at 2026-06-01; >4% of the flock has *announced* a transition; IAA declines to forecast the US | Base level; the 4% is announced, not realised |
| 2026-09-19 | AgFunderNews 2026-09-09 | **Vital Farms birds arrive early 2027**; Kipster USA brand early 2027; Cheggy brown-only; 90% white market; UEP "far from proven out" quote | **Strongest downward constraint.** LR ≈ 3:1 against 3.2% |
| 2026-09-19 | IAA Q2 2026 roundup | NestFresh 100% converted, **>800,000 chicks cumulative** | Sizes the specialty segment at ~0.3% of the US. LR ≈ 2:1 against high numbers |
| 2026-09-19 | AgFunderNews 2026-07-27 (Orbem) | 2 US systems, 3rd in 2027; ~24 k eggs/h or ~1 M females/yr per module; 12–15 hatcheries for national coverage; ~1 cent/egg; "we expect an announcement from one of the big retailers very soon" | Capacity not binding; keeps the right tail alive |
| 2026-09-19 | Searched Cal-Maine, Rose Acre, Versova, Hillandale, Michael Foods + "in-ovo sexing 2026" | **Nothing.** No commodity integrator commitment found | Absence of expected evidence ⇒ evidence of absence; a Q1-2027-visible conversion would have needed a mid-2026 announcement |
| 2026-09-19 | The Humane League on Walmart (2025-02-20) | Supplier guidelines name in-ovo sexing; **no deadline, no share** | Downward vs. the "Walmart commits" headline |
| 2026-09-19 | WATTPoultry, UEP Hatch Check (June 2025) | Third-party audit + segregation + day-15 sexing; a certification, not a commitment | Neutral-to-down |
| 2026-09-19 | Sauder's Eggs in-ovo page | Scope limited to new specialty flocks from Aug 2026, conditional on supply | Downward vs. treating Sauder's as a full transition |
| 2026-09-19 | Feedstuffs / PRNewswire on NestFresh | Hidden Villa Ranch = 24th largest US producer, ~4 M layers; NestFresh is the brand, not the whole company | Explains why 100% of NestFresh ≠ 4 M hens |
| 2026-09-19 | WATTPoultry, US egg market 2026 | 307.9 M table-egg layers at 2026-02-01 (+2.9% y/y); 12.4 M depopulated in 2026 to date | Denominator |
| 2026-09-19 | CSMonitor 2016 + UEP statement | UEP's 2016 pledge to end culling by 2020, conditioned on feasibility; not delivered | Negative base rate for voluntary US pledges |
| 2026-09-19 | PubMed `in ovo sexing poultry hatchery` 2025– | Chen et al. 2026 (DOI 10.3389/fbioe.2026.1785893): "none meet commercial requirements" for a general method | Supports the white-egg bottleneck |
| 2026-09-19 | Kalshi / Polymarket / Manifold / Sentinel / Mantic / GJOpen / INFER | No market or question found | Metaculus only |

## Dead ends and ruled-out hypotheses

- **mdpi.com and sciencedirect.com review articles** — HTTP 403 through the proxy. Use PubMed
  / PMC mirrors instead (PMC13465435 looked like the MDPI one).
- **wattagnet.com "Top 25 US egg producers in 2024"** — HTTP 403 on fetch. I could not get
  flock-size rankings for Sauder's, Vital Farms or MPS from a primary list; the hen counts in
  the decomposition are therefore *estimates*, uncertain to roughly ±40% each. Try
  `eggindustry-digital.com` ("The 52 largest US egg producers in 2026") next update.
- **A commodity-integrator commitment** — searched five of the largest producers by name.
  None found. This is a finding, not a gap.
- **Vital Farms disclosure of in-ovo share** — not in any public filing I found. Worth checking
  their next 10-Q/earnings call.
- **Direct Metaculus access** — `curl`/`WebFetch` 403 as documented; the aggregations script
  needs `METACULUS_FORCE_TLS12=1` in this environment or it returns `status 0`.

## Open questions to chase next time

1. Does IAA publish any US figure before July 2027, and with what as-of date? If not, the
   annulment branch fires.
2. Vital Farms: what share of its >10 M-hen network is in-ovo sexed, and when does the
   conversion complete? Check the next 10-Q and earnings call.
3. Hy-Line North America: are its Cheggy machines running for Vital Farms only, or for its
   whole brown book? That is the difference between ~2% and ~6% by 2028.
4. Did MatrixSpec/SANOVO HyperEye actually launch commercially in late 2026 / early 2027, and
   into which hatchery? First white-layer commodity installation is the real US tripwire.
5. Better flock-size numbers for Sauder's, MPS/Kipster and Hidden Villa Ranch's NestFresh
   brand — the bottom-up rests on estimates.
