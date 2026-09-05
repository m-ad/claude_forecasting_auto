# Will FEWS NET classify any area of Sudan as experiencing Famine before 2027?

| | |
|---|---|
| **Source** | Metaculus #45464 — https://www.metaculus.com/questions/45464/ |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-09-07 / 2026-10-31 / 2026-12-31 |
| **Status** | open |
| **Current forecast** | **Median 20.0%, IQR [14.0%, 28.0%]** (v1, 2026-09-05) |
| **Community (as of 2026-09-05)** | **not yet revealed** — question status `upcoming`, CP reveal 2026-09-09T17:00Z (n=13 forecasters already in) |
| **Next review** | 2026-09-19 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-09-05

### What resolves YES

A **FEWS NET** classification map for Sudan whose **"Reported" date falls after August 2026 and
before January 2027** must show at least one *area, urban settlement, or settlement of displaced
populations* in **IPC Phase 5: Famine**, with solid **or reasonable** evidence, **for the current
period**. Three exclusions do most of the work:

1. **Phase 4 with "!"** — "would likely be Phase 5 without assistance" — is explicitly excluded
   by fine print, and FEWS NET applies that annotation widely in Sudan.
2. **"Risk of Famine"** is not a classification. FEWS NET's Sudan pages currently carry the word
   *Famine* in almost every headline while classifying **nothing** in Phase 5. Reading the
   headlines rather than the map legend is the main way to get this question wrong.
3. The **current period**, not a projection. A map projecting Famine for Feb–May 2027 is a NO.

The resolver is FEWS NET (https://fews.net/east-africa/sudan), not the IPC. Publication cadence:
Food Security Outlook ≈ Feb/Jun/Oct, Outlook Update at mid-points, Key Message Updates otherwise
— so roughly **3–5 qualifying maps** in the window. The most recent publication as of today is
the Key Message Update **July 2026 – January 2027**, which classifies no area in Phase 5.

Note one mechanical NO tail: on 2026-08-31 NPR reported the State Department had suspended FEWS
NET reporting on Somalia, Yemen and Afghanistan in mid-August, with coverage varying by "policy
priorities". Sudan was not suspended, but a suspension would force NO regardless of conditions.

### Outside view

The state of the world is **"FEWS NET says credible risk of Famine, and classifies no area in
Phase 5."** The right reference class is therefore *how often such a risk designation converts
into an actual current-period Phase 5 classification within ~4 months.*

| Class | n | Window | Rate |
|---|---|---|---|
| **A (primary)** — FEWS NET "risk of Famine" episodes converting to a current-period Phase 5 classification within ~4 months: Yemen 2017–19 (repeatedly, never), Tigray 2021 (never), South Sudan 2020–22 (never — Pibor 2020 came closest), Somalia 2022 (projected, **did not** materialise after aid scale-up), NE Nigeria 2016/2021 (never formally), Afghanistan 2021–22 (never), Gaza 2024–25 (converted 2025), Sudan 2024 & 2025 (converted twice) | ~25–30 | 2011–2026 | **~10–15%** |
| **B (upper bound)** — share of 4-month windows since Aug 2024 in which a FEWS NET Sudan map carried current-period Phase 5 | 6 | Aug 2024–Aug 2026 | ~75% |
| **C (lower bound / status quo)** — same, but only since the Feb-2026 de-classification | 2 | Feb–Sep 2026 | 0% |
| **D (sanity floor)** — global famine declarations per year, any system (Somalia 2011, S. Sudan 2017, Sudan 2024, Gaza 2025, Sudan 2025) | 5 | 16 years | ~0.3/yr worldwide |

Class B is the trap. It averages over a siege configuration that **no longer exists**: El Fasher
fell to the RSF in late Oct 2025 (ending the siege by capture), and the Dilling and Kadugli sieges
were broken at the end of Jan 2026 with the first major UN convoy on 18 Feb 2026. That is precisely
*why* FEWS NET wrote in February 2026 that "Famine thresholds are no longer met". Class C is the
opposite trap — two observations of a sticky status quo say little about a deteriorating one.

Anchor on **Class A ≈ 12–15%**, adjusted up because Sudan is the world's highest-conversion
environment (two conversions since 2024, against roughly zero for every other risk-of-Famine
country in the same period) and because there are 3–5 independent shots on goal in the window.

### Inside view

`P(YES) = 1 − Π(1 − p_i)` over four roughly-independent paths:

| Path | Mechanism | p |
|---|---|---|
| **A — NW/central North Darfur** (Um Baru, Kernoi, At-Tine) | Famine's **malnutrition threshold is already surpassed**: Dec-2025 surveys put GAM at **52.9%** (SAM 18.1%) in Um Baru and **34.0%** in Kernoi, against a 30% famine threshold. Rainfall is the **driest in the 40-year record**, 20–30 days late, planting 2–4+ weeks behind → effectively no October harvest. Population "largely unreachable by humanitarians." The missing leg is **mortality and food-consumption evidence** — and access is deteriorating, so new evidence is getting *less* likely. FEWS NET has held the GAM data for ~9 months without converting. | 0.12 |
| **B — El Obeid**, North Kordofan | ~**500,000 trapped**, incl. 105,000 IDPs; ~18 months of drone-enforced siege ("a siege without a full encirclement"); food prices **+300%**; WFP (Jul 2026): food stocks "critically depleted by September, exhausted by October", nutrition supplies out from August. Structurally the El Fasher pattern. Against it: the observed lag from siege-tightening to formal classification was ~18 months (El Fasher) and ~30 months (Kadugli); the fast case (Zamzam, ~3 months) needed a pre-existing camp survey. | 0.08 |
| **C — Kadugli / Dilling re-encirclement** | FEWS NET calls the relief corridor volatile and the area heavily contested; both towns still hold populations in Catastrophe, so a re-siege re-crosses thresholds quickly from an already-collapsed baseline. | 0.06 |
| **D — a Q4-2026 IPC/FRC round** lowers the evidentiary bar somewhere not covered above and FEWS NET adopts it on the December map | Post-harvest IPC rounds for Sudan have historically landed Sept–Dec, and the FRC is the mechanism that produced *both* prior conversions. Mostly overlapping A–C; counted as marginal only. | 0.04 |

`1 − (0.88 × 0.92 × 0.94 × 0.96) = **26.9%**`

Adjustments to that:

- **−4 pp** — FEWS NET's own June and July 2026 analyses project through January 2027 and do
  **not** carry Famine as the most-likely outcome anywhere. The institution that resolves this
  question has published what it expects to publish.
- **−3 pp** — the qualifying maps cover **October–January**, the post-harvest period. Even a
  catastrophic harvest is a marginal improvement on the Aug–Sep lean-season peak in most areas,
  and FEWS NET expects calmer eastern areas to reach Stressed (Phase 2).
- **+1 pp** — the "settlement of displaced populations" clause is a genuinely low bar (Zamzam in
  Aug 2024 was exactly that), and 3–5 publications give multiple attempts.
- **No haircut for political interference.** I considered discounting for State Department control
  of FEWS NET, and rejected it: FEWS NET published Famine classifications for Sudan in Oct–Dec 2025
  under this same arrangement. The Somalia/Yemen/Afghanistan suspension enters only as a small
  mechanical-NO tail.

→ **20%**.

### Evidence

**What moved me up.** The Um Baru / Kernoi malnutrition data is the strongest YES evidence:
GAM at 52.9% is not "approaching" the famine threshold, it is 1.8× it. Combined with the driest
rainfall in 40 years and near-total inaccessibility, the *conditions* in NW North Darfur are
almost certainly famine conditions. El Obeid is a second, independent, and rapidly worsening
candidate that did not exist as a famine locus a year ago (LR ≈ 1.6 on the pre-El-Obeid view).

**What moved me down, and moved me more.** Three things.

First, **the mechanism behind the last classification has been dismantled**. El Fasher's siege
ended by RSF capture; Kadugli's and Dilling's by relief. FEWS NET's February 2026 de-classification
was a considered judgement, not an artefact, and it has held for **seven consecutive monthly
publications**.

Second, **the binding constraint is evidence, not conditions**. A Phase 5 classification needs
convergence on three legs — ≥20% of households in extreme food gap, GAM >30%, crude death rate
>2/10,000/day. Um Baru clears the GAM leg spectacularly and FEWS NET *still* declined to classify,
because the areas are unreachable and there is no mortality survey. The Oct-2025 FRC explicitly
could not rule on Dilling "due to extremely limited data availability" even while ruling on
Kadugli next door. Deteriorating access makes the missing evidence *less* likely to appear, not
more. This is the asymmetry most likely to be underweighted by forecasters reading the headlines.

Third, and decisively for calibration: **absence of expected evidence**. If FEWS NET were on the
verge of a Phase 5 classification, I would expect to see it stage the ground — an Alert, a
"Famine likely" or "Famine expected" projection, or an FRC convocation. The June and July 2026
analyses contain none of these; they contain harvest-driven *improvement* assumptions and a
projected fall in assistance targeting from 4.7M to 3.4M people per month. That absence is
evidence of absence here, because staging is exactly what FEWS NET did before Aug 2024 and
Sep 2025 (LR ≈ 0.5 against my inside-view number).

**A misconception worth naming.** Numerous secondary sources — including the IRC, quoted as
recently as August 2026 — write "famine confirmed in El Fasher and Kadugli" in the present tense.
They are restating the October-2025 FRC finding. FEWS NET withdrew it in February 2026. Anyone
forecasting this question off news headlines rather than the map legend will be far too high.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | **not revealed** | 2026-09-05 | question status `upcoming`; CP reveals 2026-09-09T17:00Z; 13 forecasters already submitted |
| Metaculus Pro | not revealed | 2026-09-05 | same |
| Metaculus gold medalists | not revealed | 2026-09-05 | same |
| Kalshi / Polymarket | **no matching market found** | 2026-09-05 | searched; famine classification is not a traded contract |
| Manifold | none found | 2026-09-05 | |
| Sentinel Team | no Sudan-famine-classification number found | 2026-09-05 | searched their published weekly output |
| **FEWS NET itself (implicit)** | Famine **not** the most-likely outcome anywhere through Jan 2027 | 2026-07 | the resolver's own published expectation — the most informative external anchor available |

**Cohort disagreement**: not assessable — all three Metaculus cohorts are hidden until 2026-09-09.
This forecast is therefore fully unanchored, which is methodologically clean but removes the
usual error-check. **This is the single largest reason my IQR is wide.** If the CP on 2026-09-09
lands more than ~12 pp from 20%, that is a mandatory re-analysis trigger, not a nudge.

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | **Status quo holds.** Oct harvest gives partial relief in calmer areas; FEWS NET keeps "Emergency + credible risk of Famine" language on every map through December; no new mortality data emerges from NW North Darfur. | 0.62 | NO |
| 2 | **Deterioration without classification.** El Obeid stocks run out, NW North Darfur worsens, FEWS NET escalates to an Alert and/or projects Famine for the Feb–May 2027 period — but the current-period map stays Phase 4/4! for want of evidence. | 0.17 | **NO** (the most likely way a forecaster loses this bet by being directionally right) |
| 3 | **Evidence arrives.** A mortality or SMART survey reaches NW North Darfur (Um Baru/Kernoi/At-Tine) or an IDP settlement, converging with the existing 34–53% GAM, and FEWS NET classifies Phase 5 on the Oct or Nov map. | 0.10 | YES |
| 4 | **El Obeid collapses fast.** Full encirclement closes the last road in Sept–Oct; conditions in the city and its IDP sites deteriorate faster than the historical classification lag; an FRC review in Nov–Dec confirms Famine and FEWS NET's December map carries it. | 0.07 | YES |
| 5 | **Kadugli/Dilling re-besieged** and re-classified from an already-Catastrophe baseline. | 0.03 | YES |
| 6 | **Mechanical NO** — Sudan reporting suspended or delayed such that no qualifying map publishes in the window. | 0.01 | NO |

Weighted: 0.10 + 0.07 + 0.03 = **0.20**.

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| The binding constraint is *evidence availability*, not conditions | The binding constraint is conditions, and FEWS NET will classify on GAM + convergent qualitative evidence alone (as arguably done for Zamzam) | **~35%** |
| No FRC round convenes for Sudan in Q4 2026 | An FRC review is convened in Nov–Dec 2026 (as in Oct 2025) | **~32%** |
| October harvest gives at least marginal relief outside the front lines | Harvest fails outright nationally (rainfall deficit verifies at the 40-year-worst level everywhere, not just North Darfur) | **~27%** |
| FEWS NET keeps publishing Sudan maps on schedule | Sudan reporting is suspended like Somalia/Yemen/Afghanistan | **~3%** |

### What would change my mind (tripwires)

- [ ] **A FEWS NET Sudan publication with a "Reported" date in Sept–Dec 2026 uses the words "Famine (IPC Phase 5)" for a *current period* area** — by 2026-12-31 → resolves YES; up 80 pp
- [ ] **An IPC Famine Review Committee is convened for Sudan** (announcement by IPC or a partner) — by 2026-11-30 → up 12 pp
- [ ] **A mortality (CDR) or SMART survey is published from Um Baru, Kernoi, At-Tine, Dilling, Kadugli or El Obeid** showing CDR > 2/10,000/day — by 2026-12-15 → up 15 pp
- [ ] **FEWS NET issues an Alert for Sudan, or projects Famine as the most-likely outcome for any period** (this is the staging step that preceded Aug-2024 and Sep-2025) — by 2026-12-15 → up 15 pp
- [ ] **El Obeid is fully encircled / the last supply road closes**, per UN OCHA, WFP or Yale HRL — by 2026-11-30 → up 8 pp
- [ ] **The Sept or Oct 2026 FEWS NET map repeats "credible risk of Famine" with no Phase 5 and no escalation** — by 2026-10-31 → down 6 pp (mechanical: one of ~4 shots spent)
- [ ] **Sudan added to the State Department's suspended-reporting list**, or no Sudan map publishes by 2026-10-31 → down 12 pp
- [ ] **Metaculus CP on reveal (2026-09-09) lands outside 8%–32%** → direction unknown; trigger a full re-analysis rather than a nudge

### Sources

1. FEWS NET — Sudan country page — https://fews.net/east-africa/sudan (accessed 2026-09-05)
2. FEWS NET — Key Message Update, Sudan, July 2026 – January 2027, "Conflict and poor rainfall to drive Emergency and risk of Famine through January" — https://fews.net/east-africa/sudan/key-message-update/july-2026 (accessed 2026-09-05)
3. FEWS NET — Food Security Outlook, Sudan, June 2026 – January 2027, "Emergency and risk of Famine to persist through harvest in the worst-affected areas" — https://fews.net/east-africa/sudan/food-security-outlook/june-2026 (accessed 2026-09-05)
4. FEWS NET — Food Security Outlook, Sudan, February 2026, "Famine thresholds no longer met, but credible risk of Famine persists in parts of Sudan" — https://fews.net/east-africa/sudan/food-security-outlook/february-2026 (accessed 2026-09-05)
5. FEWS NET — Key Message Update, Sudan, March 2026, "The risk of Famine (IPC Phase 5) persists in South Kordofan and North Darfur" — https://fews.net/east-africa/sudan/key-message-update/march-2026 (accessed 2026-09-05)
6. FEWS NET — Key Message Update, Sudan, May 2026, "Emergency and risk of Famine persist in North Darfur and South Kordofan" — https://fews.net/east-africa/sudan/key-message-update/may-2026 (accessed 2026-09-05)
7. FEWS NET — Key Message Update, Sudan, January 2026, "Famine remains possible despite siege breakthrough in South Kordofan" — https://fews.net/east-africa/sudan/key-message-update/january-2026 (accessed 2026-09-05)
8. FEWS NET — Sudan Acute Food Insecurity Classification, April 2026 – September 2026 — https://fews.net/sudan-acute-food-insecurity-classification-april-2026-september-2026 (accessed 2026-09-05)
9. IPC — Famine Review Committee: Sudan, October 2025, Conclusions and Recommendations — https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/IPC_Famine_Review_Committee_Report_Sudan_Oct_2025.pdf (accessed 2026-09-05)
10. IPC — "SUDAN: Famine confirmed in El Fasher and Kadugli towns, 20 other areas at risk of Famine" — https://www.ipcinfo.org/ipcinfo-website/countries-in-focus-archive/issue-137/en/ (accessed 2026-09-05)
11. IPC — "SUDAN: Famine threshold for acute malnutrition surpassed in two more North Darfur localities, crisis worsening in Greater Kordofan" (issue 143) — https://www.ipcinfo.org/ipcinfo-website/countries-in-focus-archive/issue-143/en/ (accessed 2026-09-05; page returned 403 to direct fetch, content read via search index and corroborated by source 12)
12. Save the Children — "Children Dying Because of Hunger as Famine Risks Detected in Two New Locations in Sudan" — https://www.savethechildren.org/us/about-us/media-and-news/2026-press-releases/children-dying-hunger-famine-risks-detected-sudan (accessed 2026-09-05)
13. IPC — Sudan: Acute Food Insecurity Situation for February–May 2026 and Projections for June–September 2026 and October 2026–January 2027 — https://www.ipcinfo.org/ipc-country-analysis/details-map/en/c/1163315/ (accessed 2026-09-05)
14. UNICEF — "Risk of Famine persists as nearly 19.5 million people face acute food insecurity in Sudan" (May 2026) — https://www.unicef.org/press-releases/risk-famine-persists-nearly-195-million-people-face-acute-food-insecurity-sudan (accessed 2026-09-05)
15. WFP — "Famine conditions confirmed in Sudan's El Fasher and Kadugli, but hunger and malnutrition ease where conflict subsides" — https://www.wfp.org/news/famine-conditions-confirmed-sudans-el-fasher-and-kadugli-hunger-and-malnutrition-ease-where (accessed 2026-09-05)
16. UNICEF / WFP — "Joint UN convoy brings vital aid to cut-off communities in Sudan's South Kordofan State" (18 Feb 2026) — https://www.unicef.org/sudan/press-releases/joint-un-convoy-brings-vital-aid-cut-communities-sudans-south-kordofan-state (accessed 2026-09-05)
17. Al Jazeera — "El-Obeid under siege by RSF: Could this be Sudan's next el-Fasher?" (6 Jul 2026) — https://www.aljazeera.com/news/2026/7/6/el-obeid-under-siege-by-rsf-could-this-be-sudans-next-el-fasher (accessed 2026-09-05)
18. WFP via GlobalSecurity — "WFP warns El Obeid is becoming the new epicentre of Sudan's displacement and hunger crisis" (17 Jul 2026) — https://www.globalsecurity.org/military/library/news/2026/07/mil-260717-wfp02.htm (accessed 2026-09-05)
19. Yale Humanitarian Research Lab via allAfrica — "Possible Siege Preparations Around North Kordofan Capital, El Obeid" (Jan 2026) — https://allafrica.com/stories/202601190042.html (accessed 2026-09-05)
20. allAfrica — "Sudan: RSF Claims Control of North Darfur's El Fasher" (Oct 2025) — https://allafrica.com/stories/202510270580.html (accessed 2026-09-05)
21. NPR (via KPCW) — "Whatever happened to the U.S. famine alert system that Trump shut down, then reopened" (31 Aug 2026) — https://www.kpcw.org/npr-news/2026-08-31/whatever-happened-to-the-u-s-famine-alert-system-that-trump-shut-down-then-reopened (accessed 2026-09-05)
22. UN News — "Child malnutrition hits catastrophic levels in parts of Sudan" (Feb 2026) — https://news.un.org/en/story/2026/02/1166898 (accessed 2026-09-05)
23. Arab News — "What the lifting of the RSF's Kadugli siege means for Sudanese civilians" — https://www.arabnews.com/node/2632028/middle-east (accessed 2026-09-05)
24. Metaculus — question #45464 aggregation snapshot (CP not yet revealed) — `raw/metaculus-2026-09-05.json` (accessed 2026-09-05)

**Date**: 2026-09-05
**Forecast**: Median 20.0%, IQR [14.0%, 28.0%]
**Thesis**: FEWS NET withdrew its El Fasher/Kadugli Famine classification in February 2026 after both sieges ended, and has published seven straight months of "Emergency + credible risk of Famine" without classifying anything in Phase 5 — including for Um Baru, where GAM is 52.9% against a 30% threshold, because the missing evidentiary leg is mortality data from areas that are getting *less* accessible, not more [2,3,4,11]. Against that status quo I weight three live deterioration paths — NW North Darfur with no October harvest after the driest rainfall in 40 years, the ~500,000-person El Obeid siege with WFP-projected stock exhaustion in October, and a possible Q4 FRC round [11,17,18] — which together with 3–5 qualifying map publications put this well above the ~12–15% global conversion rate for "risk of Famine" designations, but well below the headlines.
