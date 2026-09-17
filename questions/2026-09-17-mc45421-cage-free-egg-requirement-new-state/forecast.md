# Will at least one additional U.S. state enact a cage-free egg requirement before July 2027?

| | |
|---|---|
| **Source** | Metaculus #45421 — https://www.metaculus.com/questions/45421/ |
| **Type** | binary |
| **Opened / Closes / Resolves** | — / 2026-12-18 / 2027-07-01 |
| **Status** | open |
| **Current forecast** | **Median 12.0%, IQR [8.5%, 17.0%]** (v1, 2026-09-17) |
| **Community (as of 2026-09-17)** | none — question is `upcoming`, CP reveals 2026-09-20 (n=4) |
| **Next review** | 2026-10-17 |

![Adoption history and scenario weights](charts/overview.png)

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-09-17

### What resolves YES

Before 2027-07-01, a U.S. state that did **not** already have a cage-free law in effect as of
2026-09-01 must enact a new cage-free requirement — defined as a law or rule that either bans
cages for in-state hens **or** bans the sale of eggs from non-cage-free hens. Four clauses do most
of the work. (1) The ten excluded states are named: AZ, CA, CO, MA, MI, NV, OR, RI, UT, WA — so the
entire 2025–26 rollback story inside those ten states is **irrelevant to resolution**. (2) Passage
by the **legislature alone suffices, "regardless of the action or inaction of the state's
governor"** — a vetoed bill still resolves YES. (3) Three routes count: legislature, ballot
measure, or state administrative action. (4) The requirement **need not take effect** before 2027 —
a 2035 phase-in counts. A production-only ban counts too (the Utah 2021 and Rhode Island 2018
model), which makes a low-cost symbolic vote in a state with no egg industry a live path. There is
no mechanical resolution source and no scheduled data release: this is decided by legislative
events and adjudicated by Metaculus admins against the public record. Residual ambiguity sits in
whether a *partial* measure (a cage-space upgrade short of cage-free, or an institutional
procurement rule) would be counted; I give that ~1.5%.

### Outside view

Reference class: a state adopting, for the first time, a genuine cage-free requirement. Earlier
"enriched cage" space laws (CA 2008, MI 2009, OR 2011, WA 2011) are excluded — they permitted
colony cages, and each of those states later passed a separate true cage-free law.

**2016:** MA · **2018:** CA, RI · **2019:** MI, OR, WA, AZ · **2020:** CO · **2021:** NV, UT ·
**2022–2026: none.** (Animal Welfare Institute anti-confinement tracker, page current to Feb 2026;
cross-checked against ASPCA's confinement-ban table. AWI records no new farm-animal confinement
enactment of any kind since New Jersey 2023, and that one covers crates, not hens.)

Ten states in six years, then five consecutive years at zero.

| Class | Rate | Scaled to the 0.786-yr window |
|---|---|---|
| Full era 2016–2026 (10 in 11 yr) | λ = 0.91/yr | P(≥1) = 51% |
| Wave only 2016–2021 (10 in 6 yr) | λ = 1.67/yr | P(≥1) = 73% |
| **Post-wave 2022–2026 (0 in 5 yr)** | Jeffreys λ ≈ 0.10/yr | **P(≥1) = 7.6%** |
| **Per-state-session, post-wave (0 of ~60)** | p ≈ 0.83%/session | **11 sessions → 8.8%** |
| Per-state-session, wave era (10 of ~84) | p ≈ 11.9%/session | 11 sessions → 75% |

The classes disagree by a factor of nine. **The whole forecast is a bet on whether the 2022–2026
drought is a regime break or a run of bad luck.** Rule of three on five zero-years caps the annual
rate at λ < 0.60/yr (95%), i.e. P(≥1) < 38% even under the most charitable reading of the data
alone. Blending 0.80 (break is real) × 8% + 0.15 (temporary pause) × 30% + 0.05 (noise) × 60%
gives ≈ 13.9% as the outside-view starting point. The status-quo prior for a
"will-X-change-by-D" question over 9.4 months pulls the same direction.

### Inside view

`P(YES) = 1 − Π(1 − p_i)` over four routes.

**Route 1 — a legislature passes a bill in the Jan–Jun 2027 session (≈13%).** Nearly all of the
probability. The window captures one essentially complete regular-session cycle for every plausible
state. Candidates, each with a session adjourning before or near 2027-07-01: NY 3.0% · NJ 2.5% ·
CT 2.0% · ME 2.0% · MD 1.5% · NM 1.5% · IL 1.5% · MN 1.0% · DE/HI/VT/VA combined 3.0% · any other
state (including a red-state United Egg Producers-brokered deal on the Utah-2021 model) 1.5%. Taken
as independent that is 17.9%; they are not independent — all eleven face the same national
headwinds — so I discount to ~13%.

**Route 2 — ballot measure (≈0.5%).** Effectively closed. Nothing cage-free was certified for the
November 2026 ballot, and the next odd-year opportunities (Maine, Ohio) fall in November 2027,
after the deadline.

**Route 3 — state administrative action (≈1.5%).** Precedent exists (Arizona's 2019–22
rulemaking), but Arizona itself has retreated and its rule is under a separation-of-powers attack,
which makes other agencies less likely to try, not more.

**Route 4 — resolver counts an edge case (≈2.0%).** A partial measure, or incremental action by a
state not on the exclusion list (Ohio's Livestock Care Standards Board is the interesting one,
since Ohio is *not* excluded despite having 2010 confinement rules).

Combined: `1 − (0.87 × 0.995 × 0.985 × 0.98) ≈ 16.4%`, shaded down because the Route-1 per-state
numbers are generous against a record of zero observed committee movement anywhere.

**What has to be true for YES**: a candidate state prioritises the bill → it survives its
agriculture committee → it clears both chambers before 2027-07-01. Not one of those three steps has
been observed in any unlisted state in four years.

### Evidence

Everything found in this sweep points the same way, which is itself a warning — so I searched
explicitly for the opposite and record the failure to find it.

**Against YES (the drivers):**

- **The flagship bill is inert.** New York S950 / A652 — the most-cited candidate — sits in the
  Senate Agriculture Committee; its complete 2025–26 action history is "referred 2025-01-08" and
  "re-referred 2026-01-07". Versions have been introduced since 2019 and none has reached a floor.
  LR ≈ 0.4 against the main YES path.
- **Federal executive hostility.** DOJ sued California (2025-07) and Michigan (2026-01-22),
  arguing the Egg Products Inspection Act preempts state cage-free sales bans. A state enacting
  now buys litigation. LR ≈ 0.6.
- **Pending federal preemption.** The House passed H.R. 7567 (Farm, Food and National Security Act
  of 2026) 224–200 on 2026-04-30 including §12006, the Save Our Bacon Act, which would nullify
  Prop 12-style laws. Senate Agriculture excluded it from its draft, and conference is unresolved.
  Pendency alone gives a legislator a free reason to wait. LR ≈ 0.7.
- **Advocacy capacity is fully committed to defense.** Humane World for Animals' and ASPCA's entire
  2026 farm-animal output is Farm Bill defense and rollback defense; the state wins they publicise
  are cockfighting (MD) and pet abandonment (FL). The organisations that manufactured the
  2016–2021 wave are not currently running an offensive state campaign. LR ≈ 0.5.
- **The wave's engine is gone.** Colorado 2020, Utah 2021 and the Arizona rule were negotiated
  deals struck because corporate cage-free pledges targeting 2025 made the transition look
  inevitable. Those pledges stalled; United Egg Producers and the Farm Bureaus are now on offense
  for repeal.

**For YES (and why it does not carry further):**

- **The bar is genuinely low.** Legislative passage alone suffices, the governor is irrelevant,
  administrative action counts, and a production-only ban counts. A blue state with no egg industry
  could do this in an afternoon as a states'-rights gesture. This is the main reason I do not go
  below 10%.
- **The price argument has weakened.** Retail eggs peaked at $6.23/dozen in March 2025 and were
  $2.19 in May 2026 (−35% YoY), with wholesale below $1 in early 2026. The core 2025 talking point
  against mandates is much less available. LR ≈ 1.3.
- **States' authority survived its first federal test.** *United States v. California* was
  dismissed for lack of standing on 2026-03-18 (Judge Scarsi, C.D. Cal.), who warned against "a
  campaign of preemption suits under the aegis of its sovereignty." Save Our Bacon was kept out of
  the Senate draft (Aug 2026). LR ≈ 1.2.
- **A backlash channel exists.** DOJ suits plus attempted federal preemption could galvanise a blue
  legislature into passing a cage-free law precisely as a sovereignty statement. This is
  **speculative** — I found no instance of a legislator proposing it — but it is the most plausible
  story under which this question resolves YES, and it carries most of Scenario 3.

**Evidence I expected to see under YES and did not find** (absence of expected evidence is evidence
of absence here): no pre-filed 2027 cage-free bill in any candidate state; no 2025 or 2026 committee
hearing, favourable report, or one-chamber passage in any unlisted state; no advocacy organisation
naming a target state for 2027; no certified 2026 ballot measure. A bill positioned to pass in
spring 2027 would normally have left at least one of these traces by September 2026.

**Counter-weight against my own sweep:** HPAI returned to commercial flocks in 12 states by June
2026. A renewed price spike into the 2027 session would remove the one favourable trend.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | **no data** | 2026-09-17 | question `upcoming`; CP reveals 2026-09-20 |
| Metaculus Pro | **no data** | 2026-09-17 | cohort returns `latest: null` |
| Metaculus gold medalists | **no data** | 2026-09-17 | cohort returns `latest: null` |
| Metaculus forecaster count | 4 | 2026-09-17 | Animal Futures Tournament, newly opened |
| Polymarket | none | 2026-09-17 | no matching market found |
| Kalshi | none | 2026-09-17 | no matching market found |
| Manifold | none | 2026-09-17 | no matching market found |
| Sentinel Team / Mantic / GJOpen / INFER | none | 2026-09-17 | no matching question found |

**No cohort disagreement to flag, because no cohort has data.** This forecast is fully unanchored:
nothing constrains it toward or away from a crowd. That cuts both ways — no herding risk, but also
no correction if I have misread the legislative landscape. It is the main reason the IQR below is
wider than the evidence quality alone would justify, and the reason the CP reveal on 2026-09-20 is
a tripwire rather than a routine check.

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | Status quo: 2027 sessions come and go with cage-free bills stuck in agriculture committees; the Farm Bill preemption fight dominates the issue space | 0.720 | NO |
| 2 | Defensive year: attention goes to rollback fights and DOJ litigation in the ten existing states; no new state acts | 0.160 | NO |
| 3 | A blue state (NY, CT, ME, NJ, MD or NM) passes a cage-free bill — plausibly production-only — before 2027-07-01, at least partly as an anti-preemption statement | 0.080 | **YES** |
| 4 | Negotiated industry deal on the Utah-2021 model, or a state agriculture department rulemaking | 0.025 | **YES** |
| 5 | Resolver counts an edge case: a partial measure, or incremental action by a state not on the exclusion list (e.g. Ohio) | 0.015 | **YES** |

YES = 0.080 + 0.025 + 0.015 = **0.120**.

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| The 2022–2026 drought is a real regime break (weight 0.80) | The 2016–2021 wave rate still applies and five zero-years were luck | **~45%** |
| No candidate state has a bill positioned to move in 2027 | A cage-free bill is found already reported favourably out of committee in a Democratic-trifecta state | **~25%** |
| Federal preemption stays pending but unenacted | Save Our Bacon (§12006) is enacted in the final Farm Bill before the 2027 sessions open | **~5%** |
| Retail eggs stay near $2/dozen | HPAI drives retail eggs back above $4/dozen by February 2027 | **~7%** |

Calibration checks: conjunction holds (three sequential hurdles, none observed); scope behaves
(doubling the window to two session cycles gives 1 − 0.88² ≈ 23%, which is the right shape); the
number is not a round anchor; and at 12.0% I am close to indifferent between the two sides, would
sell at 20% and buy at 7%.

### What would change my mind (tripwires)

- [ ] **2026-09-20** — Metaculus CP reveals more than 10 pp away from 12.0% with n ≥ 20 → re-analyse
      from scratch rather than nudge (direction unknown).
- [ ] **By 2026-12-31** — Farm Bill conference report includes §12006 / Save Our Bacon preemption
      language → **down 6 pp**. (If it is stripped in conference → up 2 pp.)
- [ ] **By 2027-02-28** — any cage-free bill in a state outside the ten excluded is reported
      favourably out of an agriculture committee → **up 12 pp**.
- [ ] **By 2027-03-31** — any such bill passes one full chamber, or is placed on a floor calendar in
      NY, CT, ME, NJ, MD or NM → **up 20 pp**.
- [ ] **By 2027-02-28** — BLS/USDA average retail price of Grade A large eggs reaches $4.00/dozen or
      higher → **down 4 pp**.
- [ ] **By 2027-05-31** — at least 8 of the 11 candidate legislatures adjourn sine die with no
      cage-free bill having passed a chamber → **down 8 pp** (mechanical: the remaining window
      shrinks to almost nothing).

### Sources

Directly fetched (full page read):

1. Metaculus #45421, *Will at least one additional U.S. state enact a cage-free egg requirement
   before July 2027?* — https://www.metaculus.com/questions/45421/ (aggregation API snapshot in
   `raw/metaculus-2026-09-17.json`, accessed 2026-09-17)
2. ASPCA, *Farm Animal Confinement Bans by State* —
   https://www.aspca.org/improving-laws-animals/public-policy/farm-animal-confinement-bans
   (accessed 2026-09-17)
3. Animal Welfare Institute, *Farmed Animal Anti-Confinement Legislation* —
   https://awionline.org/policy-efforts/farmed-animal-anti-confinement-legislation/ (page content
   current to Feb 2026; accessed 2026-09-17)
4. New York State Senate, *Bill S950 (2025–2026)* —
   https://www.nysenate.gov/legislation/bills/2025/S950 (accessed 2026-09-17)
5. Animal Agriculture Alliance, *States rolling back legislation on cage-free eggs* —
   https://animalagalliance.org/egg-prices-cage-free-mandates-legislation/ (published 2025-04-01;
   accessed 2026-09-17)
6. USDA Economic Research Service, *Number of States with restrictions on egg-laying hen
   confinement is small but growing* — https://www.ers.usda.gov/data-products/charts-of-note/106005
   (published 2023-03-10; accessed 2026-09-17)

Consulted via search results (headline and summary only, not fully fetched — treat the detail as
second-hand):

7. Civil Eats, *Trump DOJ Sues Michigan to Overturn Cage-Free Egg Law* (2026-01-28) —
   https://civileats.com/2026/01/28/trump-doj-sues-michigan-to-overturn-cage-free-egg-law/ (accessed 2026-09-17)
8. National Law Review, *DOJ Files Suit Against Michigan Over Cage-Free Egg Law* —
   https://natlawreview.com/article/doj-sues-michigan-over-cage-free-egg-law (accessed 2026-09-17)
9. National Law Review, *District Court Rules that DOJ Has No Standing to Challenge California's
   Egg Standards on Preemption Grounds* (2026-04) —
   https://natlawreview.com/article/district-court-rules-doj-has-no-standing-challenge-californias-egg-standards (accessed 2026-09-17)
10. Courthouse News Service, *Judge fries Trump's challenge to California egg laws* —
    https://www.courthousenews.com/judge-fries-trumps-challenge-to-california-egg-laws/ (accessed 2026-09-17)
11. Civil Rights Litigation Clearinghouse, *United States v. California*, 2:25-cv-06230 (C.D. Cal.)
    — https://clearinghouse.net/case/46779/ (accessed 2026-09-17)
12. Congress.gov, *H.R. 7567 — Farm, Food, and National Security Act of 2026* —
    https://www.congress.gov/bill/119th-congress/house-bill/7567 (accessed 2026-09-17)
13. Congress.gov, *S.1326 — Food Security and Farm Protection Act* —
    https://www.congress.gov/bill/119th-congress/senate-bill/1326 (accessed 2026-09-17)
14. Humane World Action Fund, *Animal protection triumphs in the Senate: 'Save Our Bacon Act'
    abandoned as Farm Bill stalls ahead of summer recess* (2026-08) —
    https://humaneaction.org/press-release/2026/08/senate-farm-bill-save-our-bacon-act-august-update (accessed 2026-09-17)
15. Humane World Action Fund, *Animal welfare laws threatened as Farm Bill passes U.S. House in
    largely party-line vote* (2026-04) —
    https://humaneaction.org/press-release/2026/04/animal-welfare-laws-threatened-farm-bill-passes-us-house-largely-party-line (accessed 2026-09-17)
16. Animal Welfare Institute, *Cage-Free Laws in the Crosshairs*, AWI Quarterly Spring 2025 —
    https://awionline.org/awi-quarterly/spring-2025/cage-free-laws-crosshairs (accessed 2026-09-17)
17. KJZZ, *Arizona will require cage-free eggs in 2026. This bill would overturn that rule*
    (2025-03-04) —
    https://www.kjzz.org/politics/2025-03-04/arizona-will-require-cage-free-eggs-in-2026-this-bill-would-overturn-that-rule (accessed 2026-09-17)
18. Michigan Senate Republicans, *Theis introduces legislation to repeal cage-free egg mandates*
    (2025-01) — https://www.misenategop.com/theis-introduces-legislation-to-repeal-cage-free-egg-mandates-and-provide-relief-to-farmers-and-consumers/ (accessed 2026-09-17)
19. Congressional Research Service IF12949, *U.S. Egg Production and Retail Prices* —
    https://www.congress.gov/crs_external_products/IF/HTML/IF12949.html (accessed 2026-09-17)
20. Tech Times, *Bird Flu Returns to 12 States: Egg Prices That Finally Fell Could Rise Again*
    (2026-06-30) —
    https://www.techtimes.com/articles/319400/20260630/bird-flu-returns-12-states-egg-prices-that-finally-fell-could-rise-again.htm (accessed 2026-09-17)
21. Ballotpedia, *2026 ballot measures* and *Potential 2026 ballot measures* —
    https://ballotpedia.org/2026_ballot_measures (accessed 2026-09-17)
22. Metaculus, *Forecasting the Future of Animals* (Animal Futures Tournament notebook) —
    https://www.metaculus.com/notebooks/43978/ (accessed 2026-09-17)

Rejected as unreliable:

23. East Coast Egg Farmers, *NJ & NY Cage-Free Egg Laws Explained for 2026* —
    https://eastcoasteggfarmers.com/egg-hub/nj-ny-cage-free-egg-laws-2026 — asserts New Jersey and
    New York have enacted cage-free requirements. Contradicted by ASPCA, AWI and the NY Senate bill
    record. Do not re-use. (accessed 2026-09-17)

**Date**: 2026-09-17
**Forecast**: Median 12.0%, IQR [8.5%, 17.0%]
**Thesis**: Ten states adopted cage-free requirements in 2016–2021 and none has since, and the
mechanism behind that stop is nameable — negotiated industry deals dried up, DOJ is suing
California and Michigan on Egg Products Inspection Act preemption, House-passed H.R. 7567 §12006
would nullify such laws, and the advocacy groups that built the wave are spending 2026 entirely on
defense (AWI tracker, ASPCA, Humane World). Against that, the resolution bar is unusually low —
legislative passage alone suffices regardless of the governor, administrative action counts, and a
production-only ban counts — and the Jan–Jun 2027 window covers one full session for roughly eleven
plausible states, of which none has moved a bill out of committee in four years (NY S950 is still in
Agriculture Committee as of 2026-01-07).
