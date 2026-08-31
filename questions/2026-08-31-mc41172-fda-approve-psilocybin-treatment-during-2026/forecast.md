# Will the FDA approve a psilocybin treatment during 2026?

| | |
|---|---|
| **Source** | Metaculus #41172 — https://www.metaculus.com/questions/41172/will-the-fda-approve-a-psilocybin-treatment-during-2026/ |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2025-12-19 / 2026-12-31 / 2026-12-31 |
| **Status** | open |
| **Current forecast** | **Median 11.0%, IQR [8.0%, 16.0%]** (v1, 2026-08-31) |
| **Community (as of 2026-08-31)** | CP 12.0% (n=244) · Pro 14.2% (n=23) · Gold 12.0% (n=81) |
| **Next review** | 2026-09-14 |

---

## v1 — Initial forecast — 2026-08-31

### What resolves YES

An FDA approval letter, dated on or before 2026-12-31, for a drug whose **active ingredient is
psilocybin**, for human medical use (an EUA would also count, but no such pathway exists here).
The active-ingredient definition is narrow and does the real work: it excludes Cybin's
deuterated psilocin analogue, atai–Beckley's mebufotenin (BPL-003), Transcend's methylone and
Lykos's MDMA. In practice only two US programs qualify — Compass Pathways' **COMP360** for
treatment-resistant depression (TRD) and Usona Institute's psilocybin for MDD — and only
COMP360 is close.

Two traps. First, **DEA rescheduling is not required**: psilocybin is Schedule I, and the
~90-day DEA step follows FDA approval. Compass's "commercial launch in H1 2027" guidance is
therefore fully compatible with a YES resolution in December 2026, and reading launch guidance
as approval guidance is the main way to get this question wrong. Second, the date that matters
is the **FDA action date**, not the announcement, the launch, or the DEA notice. Resolution
source is the FDA approval letter (Drugs@FDA / FDA press announcement); there is no scheduled
release, so this is an event question, not a data-cutoff question. Status quo is NO — psilocybin
has never been FDA-approved for anything.

### Outside view

Four partial reference classes, deliberately kept in disagreement.

**A. "NDA not yet submitted on 31 August → approved by 31 December of the same year."** Under
conventional PDUFA arithmetic (60-day filing review, then a 6- or 10-month clock) this is
arithmetically impossible; the historical rate is ≈0%. This is the class the low Metaculus
comments are using — and it is exactly the class the CNPV program was built to break.

**B. CNPV applications, filing → decision** (the load-bearing class). Published day counts:
Hernexeos 44, Foundayo 50, Wegovy HD 54, Tec-Dara 55, Otarmeni 61, Lipfendra 24. **Median ≈52
days, range 24–61.** Program totals as of August 2026: ~22 vouchers, ~11 approvals, 1 CRL
(bitopertin, 2026-02-13). The review itself is *not* the binding constraint any more. [10][11][12][13]

**C. Biotech "we will submit in Q4" guidance, given in Q3.** Roughly 85% land inside the
quarter, and within the quarter submissions cluster **late**. This is the prior that decides
the forecast.

**D. First-in-class interventional psychiatry with a complex REMS.** Spravato (esketamine):
NDA received 2018-09-04, advisory committee 2019-02-12, approved 2019-03-05 — **182 days**,
with priority review. Pre-CNPV, but it is FDA's habitual posture on supervised-administration
psychiatry: an adcomm plus a REMS negotiated through the cycle. [24]

A says ~0%. B says the review is fast. C says the submission date is the bottleneck. D says an
adcomm is a live tail risk that would end 2026 outright.

### Inside view

```
P(YES) ≈ P(rolling NDA completes on date C) × P(decision issued by 2026-12-31 | C) × P(approval | decision)
```

What is established, as of 2026-08-31:

- **COMP005** (June 2025): −3.6 MADRS at week 6, one 25 mg dose vs inert placebo.
- **COMP006** (2026-02-17): **−3.8 MADRS** (95% CI [−5.8, −1.8]), p<0.001, two 25 mg doses vs a
  1 mg comparator; 581 dosed. SAEs 2% in the 25 mg arm; suicidal ideation <1%; the one serious
  suicidal-behaviour event was in the **1 mg comparator** arm. [7]
- **2026-07-07**: positive 26-week durability data — the **last gating clinical dataset**. [6]
- **2026-04-18** Executive Order on serious mental illness; **2026-04-24** FDA grants Compass a
  rolling NDA submission-and-review agreement plus a **CNPV** ("1–2 month review time following
  filing of an NDA"). Usona and Transcend get CNPVs the same day. [2][15][19]
- **2026-07-14** FDA final psychedelic-trials guidance endorses low-dose/active comparators and
  central blinded raters — COMP006's 1 mg design is aligned with it. [17][18]
- **2026-08-12** (Q2 results + Canaccord): "some modules submitted", "on track to complete all
  modules in **Q4**", launch H1 2027, launch-readiness end-2026. Management explicitly flagged
  that FDA "may or may not take the typical, traditional 60-day acceptance period" and that the
  decision date likely falls outside the 1–2 month window. [3][4][5]

So: the science is done, the political tailwind is real, the review mechanism is fast — and the
NDA is still not filed, eight weeks after the last data landed, with guidance no sharper than
"Q4". **The binding constraint is the filing date.**

Let G = gap from completion to FDA "filing", R = review from filing (Class B: median ~52d).
G is the crux: P(G ≤ 14d) ≈ 0.35 (rolling review live since April, CNPV tumour-board model,
political priority), P(G ≈ 15–35d) ≈ 0.30, P(G ≈ 60d) ≈ 0.35 (the traditional period, as
management warned). That gives P(G+R ≤ 84d) ≈ 0.53, ≤69d ≈ 0.36, ≤53d ≈ 0.15, ≤38d ≈ 0.04.

| Completion window | P(C) | Days to 12-31 | P(decision in 2026 \| C) | Contribution to P(YES) |
|---|---|---|---|---|
| Oct 1–15 | 0.08 | ~84 | 0.53 | 3.6pp |
| Oct 16–31 | 0.12 | ~69 | 0.36 | 3.7pp |
| Nov 1–15 | 0.14 | ~53 | 0.15 | 1.8pp |
| Nov 16–30 | 0.16 | ~38 | 0.04 | 0.5pp |
| Dec 1–15 | 0.16 | ~23 | 0.005 | 0.1pp |
| Dec 16–31 | 0.19 | ~8 | ~0 | 0.0pp |
| slips to 2027 | 0.15 | — | 0 | 0.0pp |

P(FDA decision inside 2026) ≈ **11.3%**. P(approval | decision) ≈ **0.85** — held below 0.9 by
first-time-sponsor CMC and facility-inspection risk (Compass has never had a product approved),
REMS negotiation, the modest MADRS delta, and bitopertin proving CNPV can deliver a *fast no*.
⇒ 9.7pp from COMP360, plus ≤0.5pp for Usona or an unforeseen route.

![Contribution to P(YES) by NDA completion window](charts/completion-window-decomposition.png)

Conjunction check: YES needs (i) an early-Q4 completion, (ii) FDA compressing the filing step,
(iii) no adcomm, (iv) a ~50-day review, (v) approval not CRL. Five conditions — the answer must
sit well under the least likely of them. 11% passes.

### Evidence

| Finding | Direction | Rough LR / effect |
|---|---|---|
| CNPV is real, not rhetoric: 6 published filing→decision times of 24–61 days, ~11 approvals [11][12][13] | ↑ strong | This is what lifts the forecast off the ~0% of Class A. LR ≈ 8 on "review completes fast" |
| Rolling submission live since April; last clinical data in 2026-07-07 [2][6] | ↑ | LR ≈ 2 on "completion happens in Q4" |
| Executive Order + Makary's personal investment in a psychedelic approval [15][16][20] | ↑ | LR ≈ 1.5 on FDA compressing procedure |
| Guidance unchanged at "Q4" since 2026-02-17 and reaffirmed 2026-08-12 [3][7] | → | Stability, but never sharpened to a month |
| **Makary's own "as soon as this summer" prediction has already failed** [20] | ↓ | Direct evidence that FDA-leadership timing optimism over-predicts *on this exact program*. LR ≈ 0.6 |
| Management refuses to claim a 2026 decision; flags the 60-day acceptance period as an open question [5] | ↓ | The people with the most information are hedging. LR ≈ 0.6 |
| No NDA completion in Q3 despite data landing 2026-07-07 [3] | ↓ | Back-weights the completion prior into Nov/Dec |
| Modest effect size (−3.6 / −3.8 MADRS) drew "modest magnitude raises questions" commentary [9] | ↓ mild | Feeds CRL risk, not timing |
| Lykos MDMA CRL (2024-08-09) after a negative adcomm [22][23] | ↓ mild | Precedent for FDA rigour on psychedelics — but its cited defects (functional unblinding, trial conduct, cardiac data) are ones COMP006's 1 mg-comparator design specifically addresses, so it transfers less than the comments assume |

**Evidence I expected to find and did not** — and this is the most important line here: no
Psychopharmacologic Drugs Advisory Committee notice for COMP360 anywhere (FDA calendar, trade
press, company disclosure, the earnings call). For a first-ever classic-psychedelic approval,
an adcomm is a real possibility (~30%) and would kill 2026 outright. FDA typically notices
adcomms ~2 months out, so silence on 2026-08-31 is *weak* evidence against one, not strong —
an October notice remains fully possible. Also absent: any public statement anywhere narrowing
"Q4" to a month. That is the highest-value missing fact in this forecast.

**Speculation, flagged as such:** the guess that FDA waives or compresses the 60-day filing
step is genuinely a guess. There is no published CNPV case where the gap between submission
completion and "filing date" is documented, so the 0.35/0.30/0.35 split over G is reasoning
from mechanism and political incentive, not from data.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | 12.0% (n=244) | 2026-08-31 | IQR [9.0%, 15.0%] |
| Metaculus Pro | 14.2% (n=23) | 2026-08-31 | peaked at 33% in early May, decaying since |
| Metaculus gold medalists | 12.0% (n=81) | 2026-08-31 | tracks CP |
| Manifold — "[ACX 2026] Will the FDA approve a psilocybin treatment during 2026?" | 15.9% | 2026-08-31 | $22.4k volume — heavy for Manifold, but play-money; discounted |
| Polymarket — "FDA approves a psychedelic for medical use in 2026?" | resolved YES, closed 2026-05-06 | 2026-08-31 | **Carries no signal.** Its list includes DXM and PCP and it counts ANDAs; no classic psychedelic was approved by May 2026, so it resolved on a routine generic. Definitional artifact, $46k volume |
| Kalshi | no matching market | 2026-08-31 | only KXFDAAPPROVE-MDMA exists, with no quotes or volume |
| Sentinel Team / Mantic / GJOpen / INFER | no matching question | 2026-08-31 | searched, nothing |
| Sell-side | Jefferies "approval around end of 2026"; consensus PT $23.75, 15/16 Buy | 2026-08 | equity analysts are structurally optimistic on regulatory timing |

**Cohort agreement, not disagreement.** CP 12.0%, Pro 14.2%, gold 12.0% — a 2.2pp spread. The
usual "Pros and gold agree and disagree with me, go find the missed fact" trigger does not
fire. The Pro cohort's May spike to 33% and subsequent decay to 14.2% is the informative
pattern: the smart money priced the CNPV news aggressively, then bled the position down as the
calendar burned without a filing. I sit 1pp below CP and gold and 3pp below the Pros; the tilt
is the adcomm residual plus a completion prior that is back-weighted into December. No gap
above 10pp against anything liquid, so no special justification is owed.

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | Rolling submission completes in October; FDA waives or compresses the filing step; approval letter Nov–Dec 2026 | 0.078 | **YES** |
| 2 | Completion in early-to-mid November; FDA runs a Lipfendra-style ~24–35 day review; approval late December 2026 | 0.026 | **YES** |
| 3 | Usona or another psilocybin route delivers a 2026 approval | 0.006 | **YES** |
| 4 | A decision lands inside 2026 but it is a CRL (CMC/facility inspection, REMS, or durability) | 0.018 | NO |
| 5 | Completion inside Q4 2026, decision (approval or CRL) lands Q1–Q2 2027 — includes every adcomm branch | 0.725 | NO |
| 6 | Completion of the rolling submission slips into 2027 | 0.147 | NO |

P(YES) = 0.078 + 0.026 + 0.006 = **0.110**.

The IQR is wide relative to the median because the whole question turns on one unobserved
number — the completion date — and a single press release could resolve it in either direction
within days. It is *not* a slow-moving, well-anchored estimate.

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Completion mass back-weighted into Nov/Dec (P(Oct) = 0.20) | Compass completes the submission in early October | ~30% |
| P(FDA compresses the filing step to ≤5 weeks) ≈ 0.65 | FDA applies the traditional 60-day filing review | ~3% |
| No advisory committee (implicitly ~70%) | FDA notices a Psychopharmacologic Drugs adcomm for COMP360 | ~2% |
| P(approval \| 2026 decision) = 0.85 | Raised to 0.95 (pure political-will read) | ~12.3% |

### What would change my mind (tripwires)

- [ ] Compass press release or 8-K announcing **completion of the rolling NDA submission on or
      before 2026-10-31** → ↑ **+14 to +19pp** (to ~25–30%).
- [ ] The same announcement dated **2026-11-16 or later**, or no announcement by 2026-11-30 →
      ↓ **−8pp** (to ~3%).
- [ ] Compass or FDA confirms **filing acceptance with a stated 2026 goal/PDUFA date**, by
      2026-11-30 → ↑ **+25pp or more** (to ~40%+).
- [ ] A **Psychopharmacologic Drugs Advisory Committee meeting notice for COMP360** appears in
      the Federal Register or on FDA's advisory-committee calendar, any date → ↓ **−8pp**
      (to ~2–3%); 2026 is over on that signal.
- [ ] **Q3 2026 earnings call (expected ~2026-11-05)** reiterates "Q4" without a completion date,
      or moves guidance into 2027 → ↓ **−5pp**.
- [ ] Any **FDA or Makary public statement naming a 2026 decision date for psilocybin**, by
      2026-11-30 → ↑ **+10pp**.
- [ ] A **CRL issued to COMP360** at any point in 2026 → resolves NO; forecast to 1%.

### Sources

1. Metaculus #41172, "Will the FDA approve a psilocybin treatment during 2026?" — https://www.metaculus.com/questions/41172/will-the-fda-approve-a-psilocybin-treatment-during-2026/ (accessed 2026-08-31; aggregations snapshot in `raw/metaculus-2026-08-31.json`)
2. Compass Pathways, "FDA Granted NDA Rolling Review Request and Awarded Commissioner's National Priority Voucher" (2026-04-24) — https://ir.compasspathways.com/News--Events-/news/news-details/2026/Compass-Pathways-Announces-FDA-Granted-NDA-Rolling-Review-Request-and-Awarded-Commissioners-National-Priority-Voucher/default.aspx (accessed 2026-08-31)
3. Compass Pathways, "Second Quarter and First Half 2026 Financial Results and Business Highlights" (2026-08-12) — https://www.biospace.com/press-releases/compass-pathways-announces-second-quarter-and-first-half-2026-financial-results-and-business-highlights (accessed 2026-08-31)
4. COMPASS Pathways (CMPS) Q2 2026 earnings call transcript, The Motley Fool (2026-08-12) — https://www.fool.com/earnings/call-transcripts/2026/08/12/compass-pathways-cmps-q2-2026-earnings-call-transcript/ (accessed 2026-08-31)
5. "COMPASS Pathways at Canaccord Genuity conference: launch path in focus", Investing.com transcript (2026-08-12) — https://m.investing.com/news/transcripts/compass-pathways-at-canaccord-genuity-conference-launch-path-in-focus-93CH-4855090 (accessed 2026-08-31)
6. Compass Pathways, "Six-Month Data from Second Phase 3 Trial Confirming Rapid and Durable Profile" (2026-07-07) — https://ir.compasspathways.com/News--Events-/news/news-details/2026/Compass-Pathways-Announces-Six-Month-Data-from-Second-Phase-3-Trial-Confirming-Rapid-and-Durable-Profile/default.aspx (accessed 2026-08-31)
7. Compass Pathways, "Successfully Achieves Primary Endpoint in Second Phase 3 Trial (COMP006)" (2026-02-17) — https://ir.compasspathways.com/News--Events-/news/news-details/2026/Compass-Pathways-Successfully-Achieves-Primary-Endpoint-in-Second-Phase-3-Trial-Evaluating-COMP360-Psilocybin-for-Treatment-Resistant-Depression/default.aspx (accessed 2026-08-31)
8. Compass Pathways, "Successfully Achieves Primary Endpoint in First Phase 3 Trial (COMP005)" (2025-06) — https://ir.compasspathways.com/News--Events-/news/news-details/2025/Compass-Pathways-Successfully-Achieves-Primary-Endpoint-in-First-Phase-3-Trial-Evaluating-COMP360-Psilocybin-for-Treatment-Resistant-Depression/default.aspx (accessed 2026-08-31)
9. "Second Positive Phase 3 for Compass' Psilocybin, Though Modest Magnitude Raises Questions", Psychedelic Alpha — https://psychedelicalpha.com/news/breaking-second-positive-phase-3-for-compass-psilocybin-though-modest-magnitude-raises-questions/ (accessed 2026-08-31; headline and summary only)
10. FDA, "Commissioner's National Priority Voucher (CNPV) Pilot Program" — https://www.fda.gov/industry/commissioners-national-priority-voucher-cnpv-pilot-program (accessed 2026-08-31)
11. PRV Watch, "CNPV Dashboard — Commissioner National Priority Voucher Tracker" — https://prvwatch.com/cnpv-dashboard (accessed 2026-08-31)
12. The Bracken Group, "One Year In: Where the FDA Commissioner's National Priority Voucher Pilot Stands" — https://www.thebrackengroup.com/blog/one-year-in-where-the-fda-commissioners-national-priority-voucher-pilot-stands-and-what-sponsors-need-to-know (accessed 2026-08-31)
13. The Pharma Letter, "National priority vouchers: a year of reform?" — https://www.thepharmaletter.com/insights/national-priority-vouchers-a-year-of-reform (accessed 2026-08-31; summary via search, page body did not render)
14. FDA, "FDA Approves First New Molecular Entity Under National Priority Voucher Program" — https://www.fda.gov/news-events/press-announcements/fda-approves-first-new-molecular-entity-under-national-priority-voucher-program (accessed 2026-08-31)
15. The White House, Executive Order "Accelerating Medical Treatments for Serious Mental Illness" (2026-04-18) — https://www.whitehouse.gov/presidential-actions/2026/04/accelerating-medical-treatments-for-serious-mental-illness/ (accessed 2026-08-31)
16. FDA, "FDA Accelerates Action on Treatments for Serious Mental Illness Following Executive Order" — https://www.fda.gov/news-events/press-announcements/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order (accessed 2026-08-31)
17. RAPS, "Psychedelics: FDA offers clarifications, compromises in final clinical trial guidance" — https://www.raps.org/resource/psychedelics-fda-offers-clarifications-compromises-in-final-clinical-trial-guidance.html (accessed 2026-08-31)
18. King & Spalding, "FDA's New Psychedelic Drug Guidance Paves a Path to Approval While Setting a High Evidentiary Bar" — https://www.kslaw.com/news-and-insights/fdas-new-psychedelic-drug-guidance-paves-a-path-to-approval-while-setting-a-high-evidentiary-bar (accessed 2026-08-31)
19. CNN, "FDA moves to fast-track review of psilocybin and methylone for mental health" (2026-04-24) — https://www.cnn.com/2026/04/24/health/fda-psychedelic-drugs-priority-vouchers (accessed 2026-08-31)
20. Citeline Pink Sheet, "Psychedelic Testimonials Alone Cannot Meet Legal Approval Standard, US FDA's Makary Says" — https://insights.citeline.com/pink-sheet/pathways-and-standards/approval-standards/psychedelic-testimonials-alone-cannot-meet-legal-approval-standard-us-fdas-makary-says-OCRVXBPRMJAR3I5LCSA7QER724/ (accessed 2026-08-31)
21. STAT, "Compass Pathways expects earlier FDA approval decision on its psilocybin drug" (2025-11-04) — https://www.statnews.com/2025/11/04/compass-pathways-depression/ (accessed 2026-08-31)
22. Psychedelic Alpha, "Unpacking FDA's MDMA Rejection Letter and the Road Ahead for Lykos" — https://psychedelicalpha.com/news/unpacking-fdas-mdma-rejection-letter-and-the-road-ahead-for-lykos/ (accessed 2026-08-31)
23. BioSpace, "FDA Rejects Lykos' MDMA-Assisted PTSD Therapy After Negative Adcomm" — https://www.biospace.com/drug-development/FDA-Rejects-Lykos-MDMA-Assisted-PTSD-Therapy-After-Negative-Adcomm (accessed 2026-08-31)
24. Drugs.com, "Spravato (esketamine) FDA Approval History" — https://www.drugs.com/history/spravato.html (accessed 2026-08-31)
25. Polymarket, "FDA approves a psychedelic for medical use in 2026?" (gamma API, closed 2026-05-06) — https://polymarket.com/event/fda-approves-a-psychedelic-for-medical-use-in-2026 (accessed 2026-08-31)
26. Manifold Markets, "[ACX 2026] Will the FDA approve a psilocybin treatment during 2026?" (API) — https://manifold.markets/DaftPunkRock/acx-2026-will-the-fda-approve-a-psi (accessed 2026-08-31)
27. Usona Institute, psilocybin programme page — https://www.usonainstitute.org/psilocybin (accessed 2026-08-31)
28. Compass Pathways, "Working with U.S. Department of Veterans Affairs for Investigational Study of Psilocybin" (2026-08) — https://ir.compasspathways.com/News--Events-/news/news-details/2026/Compass-Pathways-Working-with-U-S--Department-of-Veterans-Affairs-for-Investigational-Study-of-Psilocybin/default.aspx (accessed 2026-08-31)

**Date**: 2026-08-31
**Forecast**: Median 11.0%, IQR [8.0%, 16.0%]
**Thesis**: The science and the review mechanism are no longer the constraint — two positive
pivotals, a CNPV whose published record is 24–61 day reviews, and an executive order behind it
— but the NDA is still unfiled on 31 August with guidance no sharper than "Q4", and Q4
submissions cluster in December, which leaves only ~11% of the completion-date mass early
enough for a filing plus a ~50-day review to land inside 2026. Management's own hedging on the
60-day acceptance period, Makary's already-missed "as soon as this summer", and an
unannounced-but-plausible advisory committee hold me a point below the CP.
