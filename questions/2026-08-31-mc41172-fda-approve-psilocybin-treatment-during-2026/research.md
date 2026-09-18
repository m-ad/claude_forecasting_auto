# Research log — Will the FDA approve a psilocybin treatment during 2026?

Metaculus #41172 · opened 2025-12-19 (first CP point) · closes 2026-12-31
Working session: 2026-08-31. All numbers fetched live this session unless marked otherwise.

---

## 0. Question parsing

Resolution criteria (verbatim): *"This question will resolve as **Yes** if the US Food and Drug
Administration approves a psilocybin treatment during 2026."*

Fine print (verbatim): *"This question only refers to market authorisation for medical treatment
in humans, including emergency use authorisations. For purposes of this question, a 'psilocybin
treatment' is defined as any drug with psilocybin as its active ingredient."*

Reading notes / edge cases:

- **Active ingredient must be psilocybin itself.** This excludes psilocin analogues and
  deuterated derivatives (Cybin's CYB003), 5-MeO-DMT / mebufotenin (atai–Beckley BPL-003),
  methylone (Transcend TSND-201) and MDMA (Lykos). Only Compass Pathways' COMP360 and Usona
  Institute's psilocybin qualify as live US programs.
- **"Approves" = an FDA approval letter.** DEA rescheduling from Schedule I is a *separate*
  downstream step (~90 days statutory practice) and is NOT required for YES. This is the single
  most common misreading of this question: "commercial launch H1 2027" is compatible with an
  FDA approval letter in December 2026.
- **Timing is calendar-year, on the FDA action date**, not the announcement or the launch.
- The fine print admits EUAs. No plausible EUA pathway exists for a depression drug; ignore.
- Status quo is NO. Psilocybin has never been FDA-approved for any indication.

Resolution source: FDA approval letter / Drugs@FDA / FDA press announcement. No scheduled
release date — this is an event question, not a data-cutoff question.

---

## 1. Live Metaculus numbers (fetched 2026-08-31, snapshot in `raw/metaculus-2026-08-31.json`)

| Cohort | Latest | IQR | n |
|---|---|---|---|
| recency_weighted (CP) | **12.0%** | [9.0%, 15.0%] | 244 |
| metaculus_pros | **14.2%** | [10.4%, 16.0%] | 23 |
| gold_medalists | **12.0%** | [9.0%, 14.2%] | 81 |

Total forecasters on the post: 753. As-of timestamp on all three: 2026-08-31 01:22 UTC.

Trajectory (month-start values, from the history array):

| Month | CP | Pro | Gold |
|---|---|---|---|
| 2025-12 | 20% | 10% | 20% |
| 2026-01 | 20% | 6% | 6% |
| 2026-02 | 18% | 13% | 12% |
| 2026-03 | 15% | 15% | 15% |
| 2026-04 | 13% | 17% | 17% |
| 2026-05 | 15% | **33%** | 20% |
| 2026-06 | 20% | 25% | 20% |
| 2026-07 | 20% | 21% | 20% |
| 2026-08 | 15% | 16% | 15% |
| 2026-08-31 | 12% | 14.2% | 12% |

Read: the Pro cohort spiked to 33% in early May, immediately after the 2026-04-24
rolling-review + CNPV news, then decayed steadily as the calendar burned without an NDA
completion. All three cohorts are now converged within ~2pp. **No material cohort
disagreement** — the usual "go looking for what you missed" trigger does not fire.

Top comments (7 fetched): the substantive ones are `josheee` (10%, regulatory-timeline
grounds), `bromo` (timeline arithmetic pushing PDUFA into 2027), `geoffodlum` (base rate 0%,
Lykos precedent), `MaxA` (posted the CNPV news). No one has flagged a resolution ambiguity;
the criteria are clean. Nobody in the comments has done the CNPV-precedent arithmetic that
this forecast rests on — the comments predate the CNPV track record accumulating.

---

## 2. Outside view — three partial reference classes

**Class A — "NDA not yet submitted on 31 August → FDA approval by 31 December of the same
year."** Under conventional PDUFA arithmetic (60-day filing review, then a 6-month priority or
10-month standard review clock) this is arithmetically impossible; historically ≈0%. n is
effectively the whole NME approval history. This is the class the Metaculus comments are
implicitly using, and it is the reason the CP sits low. It is also the class that the CNPV
program was explicitly designed to break.

**Class B — Commissioner's National Priority Voucher (CNPV) applications, filing → decision.**
This is the load-bearing class. Published day counts (PRV Watch dashboard, Bracken Group,
The Pharma Letter, FDA press announcements), all fetched 2026-08-31:

| Product | Decision date | Days from filing |
|---|---|---|
| Hernexeos (zongertinib) | 2026-02-26 | 44 |
| Tec-Dara (teclistamab + daratumumab) | 2026-03-05 | 55 |
| Wegovy HD (semaglutide 7.2 mg) | 2026-03-20 | 54 |
| Foundayo (orforglipron) | 2026-04-01 | 50 |
| Otarmeni (OTOF gene therapy) | 2026-04-23 | 61 (from BLA filing) |
| Lipfendra (oral PCSK9) | 2026-07-15 | 24 |

Median ≈ 52 days, range 24–61. Program totals as of 2026-08: **22 vouchers awarded, ~11
approvals, 1 CRL** (bitopertin, 2026-02-13). Naive approval rate 11/12 ≈ 92%, heavily
selection-biased upward (FDA hands vouchers to applications it already likes).

The Pharma Letter describes the procedural sequence as: ~60-day pre-submission period →
filing check of 2–3 weeks → 30–60 day review. FDA's own CNPV page states the 1–2 month goal
but **does not say what event starts the clock**; Compass's own press release says
"1-2 month review time **following filing** of a New Drug Application."

**Class C — biotech "we will submit in Q4" guidance given in Q3 → actually submits that
quarter.** No clean published statistic found; the ~85% figure circulating in analyst
commentary on CMPS is consistent with the usual rule of thumb. Within the quarter, submissions
cluster late — this is the single most important prior in the whole forecast.

**Class D — first-in-class interventional psychiatry with a complex REMS.** Spravato
(esketamine), the closest analogue: NDA received 2018-09-04, advisory committee 2019-02-12,
approved 2019-03-05 = **182 days** with priority review and an adcomm. Pre-CNPV, but it shows
FDA's habitual posture on supervised-administration psychiatry: adcomm plus a REMS negotiated
through the review cycle.

Class A says ~0%. Class B says the review itself is not the binding constraint. Class C says
the submission date is. Class D says an adcomm is a live risk that would end 2026 outright.

---

## 3. Inside view — the causal chain

Only one candidate can plausibly produce a 2026 approval: **COMP360** (Compass Pathways,
synthetic psilocybin, treatment-resistant depression).

```
P(YES) ≈ P(rolling NDA submission completed on date C)
       × P(FDA files it and issues a decision by 2026-12-31 | C)
       × P(that decision is an approval, not a CRL)
```

Established facts (all this session):

- **COMP005** (first pivotal, June 2025): −3.6 MADRS points at week 6, single 25 mg dose vs
  inert placebo. 25% of the 25 mg arm hit a ≥25% MADRS reduction.
- **COMP006** (second pivotal, press release 2026-02-17): −3.8 MADRS points (95% CI
  [−5.8, −1.8]), p<0.001, two 25 mg doses three weeks apart vs a **1 mg active-ish comparator**;
  581 dosed (25 mg n=296, 1 mg n=143). 39% of the 25 mg arm hit ≥25% MADRS reduction. SAEs in
  6 participants (2%) of the 25 mg arm; suicidal ideation <1% across both trials; the one
  serious suicidal-behaviour event was in the **1 mg comparator** arm.
- **2026-07-07**: 26-week Part B durability data from COMP006 positive. **This was the last
  gating clinical dataset.** Everything since is assembly, CMC and labelling.
- **2026-04-18**: Executive Order *Accelerating Medical Treatments for Serious Mental Illness*.
- **2026-04-24**: FDA grants Compass a rolling NDA submission-and-review agreement AND a CNPV;
  same day Usona (psilocybin/MDD) and Transcend (methylone/PTSD) receive CNPVs.
- **2026-07-14**: FDA final guidance *Psychedelic Drugs: Considerations for Clinical
  Investigations* published in the Federal Register — endorses low-dose/psychoactive
  comparators, central blinded raters, expectancy questionnaires. COMP006's 1 mg comparator
  design is *aligned* with this; COMP005's inert placebo less so.
- **2026-08-12** (Q2 results, earnings call, and Canaccord Genuity conference): "some modules
  of the NDA submitted", "on track to complete all modules in **Q4**", "commercial launch
  expected in **first half of 2027**", "launch-readiness on track for end of 2026".
- Management (Canaccord, 2026-08-12) explicitly flagged the key uncertainty: FDA "may or may
  not take the typical, traditional 60-day acceptance period", and said the expected decision
  date is likely to fall outside the 1–2 month window even if the agency tries to move faster.
- REMS: "will not be finalized until we receive approval"; minimum 6-hour monitoring expected.
- DEA: management expects ~90 days post-approval, with the EO pushing FDA–DEA coordination.
  **Irrelevant to this question's resolution** but it is why launch guidance is H1 2027.

Guidance stability: "complete an NDA submission in Q4" has been the company line since the
2026-02-17 COMP006 release and was reaffirmed 2026-08-12. Six months of unchanged guidance is
a decent sign it holds — but it has also never been sharpened to a month, and the last clinical
data landed 2026-07-07 with the company still not pulling the date forward into Q3.

### Timing arithmetic

Let C = completion date of the rolling submission, G = gap from C to FDA "filing", R = review
duration from filing. Need C + G + R ≤ 2026-12-31.

R distribution taken from Class B: median ~52 days, 24–61 observed.
G is the crux, and is genuinely unknown:

| G branch | Weight | Rationale |
|---|---|---|
| G ≤ 14 days | 0.35 | Rolling review already underway since April; CNPV "tumor-board" model; political priority |
| G ≈ 15–35 days | 0.30 | Compressed filing check (Pharma Letter's "2–3 weeks") |
| G ≈ 60 days | 0.35 | FDA applies the traditional filing period, as management warned it might |

⇒ P(total elapsed T = G+R ≤ 84 days) ≈ 0.53; ≤ 69 days ≈ 0.36; ≤ 53 days ≈ 0.15;
≤ 38 days ≈ 0.04.

Completion-date distribution for C (Class C prior, back-weighted within the quarter, 85% mass
inside Q4):

| Window | P(C) | Days to 12-31 | P(T ≤ that) | Contribution |
|---|---|---|---|---|
| Oct 1–15 | 0.08 | ~84 | 0.53 | 0.042 |
| Oct 16–31 | 0.12 | ~69 | 0.36 | 0.043 |
| Nov 1–15 | 0.14 | ~53 | 0.15 | 0.021 |
| Nov 16–30 | 0.16 | ~38 | 0.04 | 0.006 |
| Dec 1–15 | 0.16 | ~23 | 0.005 | 0.001 |
| Dec 16–31 | 0.19 | ~8 | ~0 | 0.000 |
| slips to 2027 | 0.15 | — | 0 | 0.000 |
| **P(FDA decision in 2026)** | | | | **≈ 0.113** |

P(decision is an approval | a decision arrives inside 2026) ≈ **0.85**. Rationale: two
positive pivotals, clean safety, breakthrough designation, CNPV's 11/12 record, and the
selection effect that FDA only moves this fast when it is comfortable. Held below 0.9 by
first-time-sponsor CMC/facility-inspection risk (Compass has never had a product approved),
REMS negotiation, the modest MADRS delta, and the bitopertin CRL showing CNPV can produce a
*fast no*.

0.113 × 0.85 ≈ 0.096. Plus ≤0.5pp for Usona or an unforeseen route ⇒ **≈ 10–11%**.

Sensitivity to the completion prior: front-loading Q4 (Oct 0.25 / Nov 0.30 / Dec 0.30 / slip
0.15) lifts P(decision in 2026) to 0.139 and P(YES) to ~12.3%. The whole forecast lives in the
range **10–13%** and the completion-date distribution is what moves it.

Adcomm overlay: no Psychopharmacologic Drugs Advisory Committee meeting for COMP360 has been
noticed as of 2026-08-31 (searched; absent). For the first-ever classic-psychedelic approval,
an adcomm is a real possibility (P ≈ 0.3), and it would end 2026 outright. Partly absorbed in
the G≈60 branch; the residual is why I sit slightly *below* the 12% CP rather than above it.

Conjunction check: the story needs (i) an early-Q4 completion, (ii) FDA waiving or compressing
the filing step, (iii) no adcomm, (iv) a ~50-day review, (v) an approval rather than a CRL.
Five conditions ⇒ the answer must be well below the least likely of them. 11% passes.

---

## 4. Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | 12.0% (n=244) | 2026-08-31 | IQR [9%, 15%] |
| Metaculus Pro | 14.2% (n=23) | 2026-08-31 | peaked 33% in May, decaying |
| Metaculus gold | 12.0% (n=81) | 2026-08-31 | tracks CP |
| Manifold "[ACX 2026] Will the FDA approve a psilocybin treatment during 2026?" | 15.9% | 2026-08-31 | $22.4k volume — high for Manifold, but play-money; discount |
| Polymarket "FDA approves a psychedelic for medical use in 2026?" | resolved YES | closed 2026-05-06 | **Not a signal.** Its psychedelic list includes DXM and PCP, and it counts ANDAs; no classic psychedelic was FDA-approved by May 2026, so it resolved on a routine generic. Definitional artifact. $46k volume |
| Kalshi | no matching market | 2026-08-31 | Searched the open-events API; only KXFDAAPPROVE-MDMA (no volume, no quotes) exists |
| Sentinel Team, Mantic, GJOpen, INFER | no matching question found | 2026-08-31 | searched; dead end |
| Sell-side | "approval around end of 2026" (Jefferies); consensus PT $23.75, 15/16 Buy | 2026-08 | equity analysts are structurally optimistic on timing |
| FDA Commissioner Makary | "as soon as this summer" / "late summer or fall 2026" | 2026-04/05 | **Already missed.** Direct evidence that FDA-leadership timing optimism over-predicts here |

I sit at 11%, i.e. 1pp below the CP, 3pp below the Pro cohort, 1pp below gold. No gap over
10pp against any liquid market or against agreeing Pro+gold cohorts, so no special
justification is owed. The small negative tilt vs the Pros is the adcomm residual plus the
back-weighted completion prior.

---

## 5. Searches run (2026-08-31)

Productive:
1. "Compass Pathways COMP360 NDA rolling submission August 2026" → Q4 completion reaffirmed
2. "COMP006 phase 3 results psilocybin treatment-resistant depression 2026" → effect sizes
3. Fetch: Compass Q2/H1 2026 results (BioSpace) → "complete all modules in Q4", launch H1 2027
4. "Compass Pathways COMP360 launch 2027 FDA decision expected timing guidance" → analyst view
5. "Commissioner's National Priority Voucher CNPV first approvals track record 2026" → approvals list
6. "FDA national priority voucher review time actual approvals how fast 2026" → 44/55-day figures
7. Fetch: FDA CNPV pilot page → program mechanics, approval dates, caveats
8. Fetch: Compass 2026-04-24 CNPV/rolling-review press release → "following filing of an NDA"
9. Fetch: Motley Fool CMPS Q2 2026 earnings-call transcript → REMS, DEA, Q4 filing
10. Fetch: Canaccord Genuity conference transcript (2026-08-12) → the 60-day-acceptance uncertainty
11. Fetch: PRV Watch CNPV dashboard → per-drug day counts, bitopertin CRL, both psilocybin vouchers
12. Fetch: Bracken Group CNPV one-year review → 44/55/50/61-day figures, clock measured from filing
13. "Makary FDA psilocybin approval comments 2026" → the missed summer prediction
14. "FDA final guidance psychedelic drugs July 2026 functional unblinding" → 2026-07-14 final guidance
15. "COMP005 COMP006 MADRS effect size criticism" → "modest magnitude" commentary
16. Fetch: Compass COMP006 press release (2026-02-17) → −3.8 MADRS, CI, n, safety
17. Fetch: STAT 2025-11-04 → "late 2026 or early 2027, nine to 12 months earlier"
18. Polymarket gamma API → the psychedelic market closed 2026-05-06, resolved YES
19. Manifold API → ACX 2026 psilocybin market at 15.9%, $22.4k volume
20. Kalshi events API → no psilocybin market
21. "Usona Institute psilocybin national priority voucher MDD NDA timeline" → uAspire enrolled Nov 2025, no topline
22. "Spravato esketamine NDA submission ... approval ... timeline" → 182 days, adcomm 2019-02-12
23. "Lykos MDMA resubmission August 2026" → **corrected a bad claim** (below)

Dead ends and corrections:
- An aggregator claimed Lykos resubmitted its MDMA NDA in August 2026. **False.** Lykos must
  run a new Phase 3; realistic resubmission 2028–2029. Do not carry this into the next update.
- No advisory-committee notice for COMP360 found anywhere (FDA calendar, trade press, company
  disclosure, earnings call). Treated as genuine absence, not as evidence of no adcomm — FDA
  typically notices adcomms ~2 months out, so an October notice remains possible.
- vicentellp.com (COMP360/REMS legal analysis) and nbcnews.com both returned HTTP 403; not read.
  The Vicente piece looked substantive and is worth retrying via archive.is at the next update.
- Searched Sentinel Team and Mantic for psychedelic-approval coverage: nothing matching.
- No public statement anywhere narrowing "Q4" to a month. This is the single highest-value
  missing fact and the main thing to hunt at the next update.

---

# v2 working log — 2026-09-18

## Tooling note

`metaculus-aggregations` failed on the first call this session with "status 0 / no HTTP
response". This is the **local egress proxy resetting Chromium's TLS 1.3 ClientHello**, not a
Cloudflare challenge. `METACULUS_FORCE_TLS12=1` fixes it; it worked first time for all four
questions updated this session.

## Searches run

- Metaculus #41172, three cohorts + history + 10 comments (`raw/metaculus-2026-09-18.json`).
  **No new comment since 2026-07-11** — the 1–2 pp cohort drift is unargued anywhere public.
- "Compass Pathways COMP360 NDA submission September 2026" → Deutsche Bank 2026 Healthcare
  Summit, 2026-09-17. Investing.com transcript fetched and read.
- FDA Psychopharmacologic Drugs Advisory Committee page + advisory-committee calendar +
  Federal Register: **no COMP360 meeting noticed**.
- Polymarket `fda-approves-a-psychedelic-for-medical-use-in-2026` via gamma API — confirmed
  closed and resolved YES (the definitional artifact identified in v1). No signal.
- Manifold search API — ACX mirror **15.8%**, flat against v1's 15.9% despite 18 days of
  calendar burn.
- Usona: no filing, no guidance, nothing new.

## The one thing worth carrying forward

The cohorts are decaying **linearly** with the calendar (12 → 11 over 18 days) while the correct
decay is **convex**: the probability mass sits in an early-October completion, and every quiet
day destroys that branch while the November/December branches were already worth ~nothing. If
this reading is right, the gap between me and the CP should *widen* through October and then
collapse the moment a completion is (or is not) announced. That is a falsifiable prediction about
the CP's own trajectory, and worth checking at the next review.

## Open questions to chase next time

1. Any statement anywhere narrowing "Q4" to a month. Still the highest-value missing fact.
2. FDA adcomm calendar — a notice before 2026-10-31 effectively ends the question.
3. Whether Compass files an 8-K on filing acceptance (they filed one for the CNPV award, so the
   precedent is that this would be disclosed promptly).
4. Q3 2026 earnings call date and content (~mid-November).
5. Whether any published CNPV case ever documents the submission-completion → "filing" gap.
   That single number carries ~7 of the 9.5 points and is currently pure mechanism-reasoning.
