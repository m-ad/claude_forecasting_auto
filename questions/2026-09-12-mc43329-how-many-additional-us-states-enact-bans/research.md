# Research log — How many additional US states will enact bans on cultivated meat before July 2027?

Metaculus post 43329 (question 43334). Opened 2026-06-12 (first CP history point),
closes/resolves 2027-07-01. Multiple choice: 0 / 1 / 2 / 3 / 4+.

## Question mechanics

- **Resolution source**: state statute books / governor signings. No scheduled data release —
  resolution is an event count, decided by legislative calendars.
- **Counting rule**: number of *additional* US states enacting a law prohibiting the sale of
  cultivated meat before 2027-07-01. Explicitly excluded: Alabama, Florida, Indiana,
  Mississippi, Montana, Nebraska, South Dakota, Texas (8 states).
- **Signed, not implemented**: fine print says resolution turns on "a ban being signed into
  law, rather than when it is implemented."
- **Full ban only**: must "fully prohibit the sale". Labeling/regulatory laws (Iowa SF 2391)
  and partial bans (e.g. under-21 sales) do not count. Cultivated *dairy*-only bans do not
  count — the definition is "genuine animal meat, including seafood and organs".
- **Sunsets and injunctions**: a sunsetting law (Indiana) or one "later overturned or enjoined"
  (Florida) "will still count if it results in the prohibition of the sale".

### Edge cases and ambiguities

1. **Louisiana (the big one).** Act 742 / SB 152 (Sen. Fesi), the "Cell Cultured Food Products
   Act", was signed 2026-06-01, nominal effective date 2026-08-01. It is a *full* prohibition
   on manufacture/distribution/sale of cell-cultured food products for human consumption —
   but a Senate floor amendment made the Part inoperative: "The provisions of this Part shall
   become effective only upon a final ruling by the United States Supreme Court holding that
   prohibitions on cell cultured food products do not violate the United States Constitution."
   HB 512 carries the same trigger; HB 783 §2 is contingent on HB 512.
   Louisiana is **not** on the exclusion list, and the background text ("As of April 2026 …")
   plainly predates the signing; the question opened 11 days after it.
   - *Counts* on the literal text: signed into law, full scope, state not excluded, and the
     author is generous about laws that do not operate (enjoined laws still count).
   - *Does not count* on a purposive reading: it prohibits nothing today, "must fully prohibit
     the sale … within the state", "will still count **if it results in** the prohibition", and
     it was already enacted before the question opened — questions are not normally resolved by
     facts predating their own opening.
   - Probability the resolver counts it: **q ≈ 0.33** (honest range 0.25–0.45). This is the
     single largest lever in the forecast. **Ask the admin.**
   - Trigger firing before 2027-07-01 is near-impossible: the only live appellate matter is
     *Upside Foods v. Simpson*, an interlocutory PI ruling (11th Cir., 2026-03-23), and a cert
     denial would not be "a final ruling holding that prohibitions … do not violate" the
     Constitution. P ≈ 0.02.
2. **Texas** (ban sunsets 2027-09-01) and **Indiana** (moratorium sunsets 2027-06-30) are both
   excluded, so re-enactments/extensions in their 2027 sessions do not count either way.
3. Ohio HB 10 (signed 2025-12-19) is labeling + school/university procurement only → no count.
   Arizona HB 2762 (2026-06-19), Virginia, Idaho, Louisiana HB 717 — labeling only → no count.

## Calendar structure of the window (2026-09-12 → 2027-07-01)

This is the load-bearing structural fact: **the window is essentially exactly one legislative
session-year, slightly truncated.**

- Sept–Dec 2026: nearly every legislature has adjourned. Only year-round bodies (OH, PA, MI,
  NJ, NY, MA) and special sessions can act. Low channel; Ohio's Nov–Dec lame duck is the only
  non-trivial one, and Ohio already revealed a preference for labeling over a ban.
- Jan–Jun 2027: regular sessions in all 50 states, including the biennial odd-year-only states
  (ND, NV; TX and MT are excluded anyway). ~90–95% of a session-year's enactments are signed
  before July 1 — the southern and plains states that drive this policy adjourn Mar–May.
- 2027 is **year 1 of a new biennium** almost everywhere: every 2026 bill is dead and must be
  reintroduced; nothing carries over from 2025–26.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Full-ban enactments per session-year | 3 yrs | 2024–2026 | 2024: 2 (FL, AL); 2025: 5 (MS, IN, MT, NE, TX); 2026: 1 clean (SD) + 1 contingent (LA) → mean 2.7/yr | NALC compilation; CSG Midwest 2026-05-04 | Yes — but the trend (2→5→1) matters more than the mean |
| Most recent session-year only | 1 | 2026 | 1 | same | Yes — most relevant to 2027, though 2026 was a short/second-year election-year session |
| Odd (first-of-biennium) years only | 1 | 2025 | 5 | same | Kept with low weight — n=1, confounded with the diffusion peak |
| "Passed one chamber, died" → enacted at the next opportunity | 4 state-sessions | 2024–26 | AZ 2024 House→never; OK 2025 House→failed 2026; SD 2025 fail→2026 success; SD 2026 veto→override failed | state legislature records | Yes → ~25–30% per follow-up attempt |
| Policy diffusion S-curve | — | — | 0 (2023) → 2 → 5 → 1: a wave that peaked in 2025 and is in its declining tail; the most receptive states are used up | — | Yes, as the main structural prior |

Blended λ for the window: bottom-up pipeline 1.74 (50%), decaying wave 1.2 (35%),
first-year-of-biennium rebound 2.5 (15%) → **λ ≈ 1.6**.

## Decomposition — per-state hazard in the window

Bottom-up Poisson-binomial. Sum of p = **1.59**.

**Tier 1 — a full ban already passed one chamber, blocked in the other:**

| State | p | Why |
|---|---|---|
| West Virginia | 0.30 | HB 4462 passed the House 2026-02-13, died in Senate Agriculture when the 60-day session ended 2026-03-14. R trifecta, Gov. Morrisey would sign. 2027 session Jan–Mar. |
| South Carolina | 0.26 | H.5096 passed the House **110–0** on 2026-02-19, referred to Senate Agriculture 2026-02-24, never acted on. R trifecta. Discount: 2027 is year 1 of the 127th GA and SC bills carry over to 2028, which *reduces* year-1 urgency. |
| Oklahoma | 0.18 | HB 2829 passed the House in Mar 2025 and died; SB 2121 cleared Senate Ag 9–3 in Feb 2026 and then died in chamber. Two consecutive failures = revealed leadership resistance, not just calendar. |

**Tier 2 — introduced and died, R trifecta, livestock-heavy:** Georgia 0.10 (SB 415 introduced
2026-01-26/27, read and referred, never reached Crossover Day 2026-03-06; sine die 2026-04-02;
GA took labeling instead), Wyoming 0.08, North Dakota 0.08 (2027 biennial session; chose
labeling in 2025), Missouri 0.07, Tennessee 0.06, Idaho 0.05, Arkansas 0.05, Utah 0.04,
Iowa 0.04, Ohio 0.04, Wisconsin 0.04, Kentucky 0.03 (2027 is a 30-day short session; Dem
governor), Kansas 0.03.

**Tail:** all other states combined 0.10; any lame-duck/special session Sept–Dec 2026, 0.04.

Over-dispersion: mixed 70% base / 15% "national salience shock" (all p × 1.7) / 15% "wave over"
(all p × 0.55) to widen both tails. → 0 19.0%, 1 31.7%, 2 26.4%, 3 14.5%, 4+ 8.4% (mean 1.65).

Louisiana overlay at q = 0.33 shifts mass up by one → **0 12.5 / 1 27.5 / 2 28.0 / 3 18.5 /
4+ 13.5**, mean ≈ 1.97, median count 2, count-IQR [1, 3].

## Search log

Searches run 2026-09-12. Phrasings varied: "states banned cultivated meat 2026 legislative
session"; "cultivated meat ban state law 2026 signed governor"; "Georgia SB 415 lab-grown meat
2026 passed failed"; "Oklahoma cultivated meat ban 2026 status"; "West Virginia South Carolina
lab-grown meat ban 2026 died"; "cultivated meat ban enacted August/September 2026 ninth state";
"Louisiana cell-cultured food product ban 2026 Landry signed"; "'cell cultured food product'
Louisiana 'shall become effective' 'United States Supreme Court'"; "2027 prefiled bill ban
cultivated meat"; "Wyoming North Dakota Missouri Kentucky Tennessee lab-grown meat ban 2026";
"Ohio bill ban sale cultivated meat 2026"; "federal bill ban cultivated meat Congress 2026
preemption"; "Upside Foods Eleventh Circuit March 2026 certiorari"; "Wisconsin Evers veto AB
554"; "Texas cultivated meat lawsuit Institute for Justice"; "Polymarket Kalshi Manifold
cultivated meat state ban".

### Findings

- **Enacted full bans, all-time**: FL SB 1084 (signed 2024-05-01), AL SB 23 (2024-05-07),
  MS HB 1006 (Mar 2025), IN HB 1425 (2025-05-06, moratorium 2025-07-01 → 2027-06-30),
  MT HB 401 (2025-05-01), NE LB 246 (May 2025), TX SB 261 (2025, in force 2025-09-01 →
  2027-09-01), SD SB 124 (signed 2026-03-12, in force 2026-07-01 → 2031-06-30).
  Plus LA SB 152 / Act 742 (2026-06-01, contingent — see above).
- **2026 session was a near-shutout.** One clean enactment (SD) from roughly a dozen attempts.
  South Dakota itself needed three tries: HB 1109 failed the Senate (2025-02-20), HB 1077 was
  vetoed by Gov. Rhoden with the override failing (2026-03-30), and only the compromise
  five-year moratorium SB 124 got through. Wisconsin AB 554/SB 560 — a labeling-and-restriction
  bill, *not* a full ban — was vetoed by Gov. Evers on 2026-03-27 as "vague and arbitrary".
- **Litigation cuts pro-ban.** 11th Circuit, *Upside Foods v. Simpson*, 2026-03-23: the Poultry
  Products Inspection Act does not preempt Florida's outright ban, because a product ban is not
  a regulation of facilities, operations or ingredients. In Texas (W.D. Tex., Jan 2026), Judge
  Albright denied Texas's motion to dismiss the dormant-Commerce-Clause claim brought by
  Wildtype and Upside (Institute for Justice) but also denied a preliminary injunction — the
  ban stands during discovery. Net: the legal-risk deterrent for a copycat state is now small.
- **Commercial reality cuts anti-ban.** As of August 2026 **no cultivated meat product is on
  sale to US consumers** — Upside and Wildtype did tastings at an SF charity event only, and
  Upside withdrew its $50m offer for Believer Meats' North Carolina plant. Sector funding and
  headcount are contracting. Nothing to ban → falling salience → falling legislative urgency.
  This is the main reason to expect 2027 to look more like 2026 (1) than like 2025 (5).
- **Federal**: no enacted federal ban or preemption. A proposed "FRESH Act" (Aug 2026) carries a
  preemption provision aimed mainly at state *labeling* rules. USDA-FSIS still has no final
  cultured-meat labeling rule. Not a 2027 driver either way, but worth watching.
- **Markets**: Kalshi's `KXCMEATBAN` series exists but its only events are "Before 2025" and
  "Before 2026" — both expired, **no open contract** covering this window (checked via the
  Kalshi trade API, 2026-09-12). Manifold has nothing comparable (one 2028-horizon market,
  resolved YES; one on a presidential candidate promising a national ban, 54.7%, ~$1.5k volume —
  not informative here). Polymarket: nothing found. Metaculus is the only live comparator.

### Dead ends / ruled out

- LegiScan returns 403 through this egress; used primary legislature sites and NALC instead.
- No evidence of an organized 2027 model-bill campaign (ALEC or similar) — searched, found
  nothing. Absence of expected evidence: if a coordinated 2027 push existed, it would normally
  be visible by September in trade press. Weak evidence *against* the high tail.
- No 2027 prefiled cultivated-meat ban bills found yet. Expected — most states open prefiling
  Nov–Dec 2026. This is the single best tripwire.
- Maine appears in the Metaculus background as a state that "recently considered" a ban; no
  2026 Maine full-ban bill found. Dem trifecta → priced inside the residual tail.
- No new enactment between 2026-06-01 (LA) and 2026-09-12 found in any tracker.
