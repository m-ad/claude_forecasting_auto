# Research log — Will at least one additional U.S. state enact a cage-free egg requirement before July 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- **Metaculus post 45421** (internal question 45610), part of the **Animal Futures Tournament**
  (Metaculus tournament 2995 / notebook 43978). Fetched 2026-09-17 via
  `metaculus-aggregations`; raw JSON cached at `raw/metaculus-2026-09-17.json`.
- **Resolution source**: Metaculus admin judgement against public records of state enactments.
  No mechanical data series. There is no scheduled release that decides this — it is decided by
  legislative events.
- **Status at forecast time**: `upcoming`. `cp_reveal_time = 2026-09-20T20:55Z`, so **no community
  prediction exists yet** (n=4 forecasters, 0 comments, all three cohorts return `latest: null`).
  This forecast is therefore fully unanchored — a rare and valuable situation, and also a
  higher-variance one.
- `scheduled_close_time = 2026-12-18T23:00Z`. Forecasting closes ~6.5 months *before* the
  resolution window ends. Consequence for the update cadence: the CP freezes in December and
  stops being informative for the decisive Jan–Jun 2027 session period.
- **Window**: today (2026-09-17) → 2027-07-01 = 287 days = 0.786 years.

### Edge cases and ambiguities

1. **Governor irrelevant.** Fine print: "If a state legislature passes a cage-free requirement,
   that will suffice ... regardless of the action or inaction of the state's governor." A vetoed
   bill still resolves YES. This materially lowers the bar and is the single most easily missed
   clause.
2. **Three enactment routes count**: legislature, ballot measure, *or* state administrative
   action. The administrative route has precedent (Arizona Dept. of Agriculture rule).
3. **Production-only bans count.** "bans the use of cages for in-state hens **or** bans the sale
   of eggs from non-cage-free hens." Utah (SB 147, 2021) and Rhode Island (HB 7456, 2018) are
   production-side laws. A near-costless symbolic production ban in a state with almost no egg
   industry qualifies.
4. **Effective date irrelevant.** "The requirement need not come into effect before January 1,
   2027." A 2035 phase-in still resolves YES.
5. **Excluded states (10)**, per fine print as of 2026-09-15: AZ, CA, CO, MA, MI, NV, OR, RI, UT,
   WA. Note the resolver's list does **not** exclude Ohio, New Jersey, Maine, Florida or Kentucky,
   all of which have *some* confinement law — but crate/veal rules, not hen cage-free rules. So a
   new Ohio Livestock Care Standards Board rule, or a New Jersey hen bill, would count as a "new"
   state.
6. **Counter-intuitive resolution**: a state *repealing* or *delaying* its own law does not affect
   this question at all. All of the 2025–26 news flow is about rollback in the ten listed states,
   which is irrelevant to resolution except as evidence about the political climate.
7. Ambiguity risk is low-to-moderate: "enacts a new cage-free requirement" is reasonably crisp,
   but a narrow or partial measure (e.g. a cage-space upgrade short of cage-free, or an
   institutional-procurement rule) could be argued either way. I put ~1.5% on the resolver
   counting such an edge case as YES.

## Reference classes considered

Tight class = a state adopting, for the first time, a genuine **cage-free** requirement (cage ban
for in-state hens or sale ban on non-cage-free eggs). Earlier "enriched cage" space laws
(CA 2008 Prop 2, MI 2009, OR 2011, WA 2011) are **excluded** — they permitted enriched colony
cages, and each of those states later passed a separate true cage-free law.

| Year | New states |
|---|---|
| 2016 | MA (Question 3, ballot) |
| 2017 | — |
| 2018 | CA (Prop 12, ballot), RI (HB 7456) |
| 2019 | MI (SB 174), OR (SB 1019), WA (HB 2049), AZ (Dept. of Ag. rulemaking) |
| 2020 | CO (HB20-1343) |
| 2021 | NV (AB 399), UT (SB 147) |
| 2022–2026 | **none** |

Source: Animal Welfare Institute, *Farmed Animal Anti-Confinement Legislation* (page content as of
Feb 2026, fetched 2026-09-17), cross-checked against ASPCA *Farm Animal Confinement Bans by State*
(fetched 2026-09-17). AWI's own table shows **no new state enactment of any farm-animal
confinement law since New Jersey 2023** (gestation/veal crates, not hens).

| Class | n | Window | Raw base rate | Scaled to 0.786 yr | Source | Kept? |
|---|---|---|---|---|---|---|
| A — full era, all years | 10 states | 2016–2026 (11 yr) | λ = 0.91/yr | P(≥1) = **51%** | AWI / ASPCA | kept, low weight |
| B — wave only | 10 states | 2016–2021 (6 yr) | λ = 1.67/yr | P(≥1) = **73%** | AWI / ASPCA | kept, very low weight |
| C — post-wave regime | 0 states | 2022–2026 (5 yr) | Jeffreys λ ≈ 0.10/yr | P(≥1) = **7.6%** | AWI / ASPCA | **primary** |
| D — per-state-session, post-wave | 0 / ~60 state-sessions | 2022–2026 | Jeffreys p ≈ 0.83%/session | 11 sessions → **8.8%** | derived | **primary cross-check** |
| E — per-state-session, wave era | 10 / ~84 | 2016–2021 | p ≈ 11.9%/session | 11 sessions → **75%** | derived | kept, sanity check on D |

C and D agree at ~8%. A/B/E disagree violently. **The entire forecast is a bet on whether the
2022–2026 drought is a regime break or a run of bad luck.** Rule of three: five years of zero
events puts the 95% upper bound on the annual rate at λ < 0.60/yr, i.e. P(≥1) < 38%.

Blend used: 0.80 × 8% (regime break real) + 0.15 × 30% (partial/temporary pause) + 0.05 × 60%
(drought was noise) ≈ **13.9%**, before inside-view adjustment.

Status-quo prior also applies: "will X change by date D" over 9.4 months, where X requires a
positive legislative act, defaults strongly to NO.

## Decomposition (inside view)

`P(YES) = 1 − Π(1 − p_i)` over four routes.

**Route 1 — a blue-state legislature passes a cage-free bill in the Jan–Jun 2027 session.**
This is where nearly all the probability lives. The window captures one essentially complete
regular-session cycle for the plausible states. Candidate set = states without a cage-free law
that have a Democratic trifecta or a working animal-welfare majority, and a 2027 session that
adjourns before or near 2027-07-01:

| State | 2027 session | Per-state p | Note |
|---|---|---|---|
| New York | Jan–Jun 2027 (new biennium) | 3.0% | flagship bill S950/A652 has sat in Agriculture Committee every session since 2019; last action 2026-01-07 = re-referred to committee |
| New Jersey | year-round, 2026–27 biennium | 2.5% | passed a crate ban in 2023 after a decade and two vetoes; no comparable hen vehicle found |
| Connecticut | Jan–early Jun 2027 (long session) | 2.0% | repeated failures on confinement bills |
| Maine | Dec 2026–Jun 2027 (long session) | 2.0% | small egg sector, historically receptive |
| Maryland | Jan–12 Apr 2027 (90 days) | 1.5% | passes animal bills, has resisted hen mandates |
| New Mexico | Jan–Mar 2027 (60-day general) | 1.5% | negligible egg industry, Dem trifecta |
| Illinois | Jan–31 May 2027 | 1.5% | no history of moving a hen bill |
| Minnesota | Jan–May 2027 (long session) | 1.0% | top-10 egg state, strong farm lobby |
| DE / HI / VT / VA combined | various, all end < Jul 2027 | 3.0% | small, low-salience |
| Any other state (incl. a red-state UEP-brokered deal, Utah-2021 model) | — | 1.5% | |

Naive independent product → P(≥1) ≈ 17.9%. These are **not** independent: all eleven face the same
national headwinds (DOJ litigation, pending federal preemption, egg-price politics, advocacy
capacity diverted to defense). Discounting for that common factor → **Route 1 ≈ 13%**.

**Route 2 — ballot measure.** Effectively closed. No cage-free measure was certified for the
Nov 2026 ballot (searched Ballotpedia's 2026 and potential-2026 lists; only an unrelated Oregon
animal-cruelty-exceptions initiative appears, and it did not qualify). The next odd-year ballot
opportunities (Maine, Ohio) are November 2027, **after** the deadline. → **0.5%**.

**Route 3 — state administrative action.** Precedent exists (Arizona 2019–22 rulemaking). Requires
a state agriculture department with delegated authority plus a willing administration. Arizona's
own retreat (rule pushed to 2034) and the Goldwater Institute separation-of-powers attack on that
rule make agencies less, not more, likely to try. → **1.5%**.

**Route 4 — resolver counts an edge case** (partial measure, or an incremental action by a state
not on the exclusion list such as Ohio). → **2.0%**.

`1 − (0.87 × 0.995 × 0.985 × 0.98) ≈ 16.4%`, which I shade down to ~12–13% because the per-state
numbers in Route 1 are generous relative to the total absence of any observed committee movement.

### Actors and incentives

- **Humane World for Animals (ex-HSUS) / The Humane League / ASPCA / AWI** — the offensive engine
  of the 2016–2021 wave. In 2025–26 their entire farm-animal output is *defensive*: Farm Bill
  preemption, DOJ suits, state rollback bills. Offense capacity is the binding constraint.
- **United Egg Producers / state Farm Bureaus** — during the wave they often *negotiated* cage-free
  bills (CO 2020, UT 2021, AZ rule) because corporate cage-free pledges targeting 2025 made the
  transition look inevitable anyway. With those pledges stalled and prices volatile, the incentive
  to deal has evaporated; they are now on offense for repeal and federal preemption.
- **Federal executive** — actively hostile. DOJ sued California (Jul 2025) and Michigan
  (Jan 2026) on Egg Products Inspection Act preemption grounds.
- **State legislators** — have a ready-made excuse to wait: "Congress may void this within the
  year." That is a cheap reason to leave a bill in committee.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-17 | `metaculus-aggregations` post 45421 | status `upcoming`; CP reveals 2026-09-20; n=4; all cohorts null; no comments | no anchor available; widens IQR |
| 2026-09-17 | ASPCA *Farm Animal Confinement Bans by State* (fetched) | 15 states with some confinement ban; hen cage-free in the 10 listed by Metaculus; AZ delayed to **2034** (Mar 2025), NV suspension authorised (2025), RI + UT postponed to 2030 (2024) | strong regime-break evidence ↓ |
| 2026-09-17 | AWI *Farmed Animal Anti-Confinement Legislation* (fetched, page current to Feb 2026) | enactment table ends at **NJ 2023** (crates); zero new hen laws since 2021 | anchors reference class C ↓ |
| 2026-09-17 | NY Senate S950 bill page (fetched) | still in Senate Agriculture Committee; actions: referred 2025-01-08, re-referred 2026-01-07; never passed either chamber | kills the single most likely YES path ↓↓ |
| 2026-09-17 | Animal Agriculture Alliance, *States rolling back legislation on cage-free eggs* (fetched, pub. 2025-04-01) | lists NV, AZ, MI, CO rollback activity; **no bills creating new requirements anywhere** | ↓ |
| 2026-09-17 | Search: DOJ cage-free lawsuits | DOJ sued **California** 2025-07 and **Michigan** 2026-01-22 on EPIA preemption | ↓ (deterrent) |
| 2026-09-17 | Search: *US v. California* outcome | dismissed for lack of standing 2026-03-18 (Judge Scarsi, C.D. Cal.); leave to amend | partial ↑ (states' authority survived) |
| 2026-09-17 | Search: Farm Bill / Save Our Bacon | House passed **H.R. 7567** 224–200 on 2026-04-30 with §12006 Save Our Bacon preemption; **Senate Ag excluded it** from its draft (Aug 2026); conference unresolved | ↓ while pending; large ↓ if enacted |
| 2026-09-17 | Search: egg prices 2026 | retail peaked $6.23/doz Mar 2025 → **$2.19/doz May 2026** (−35% YoY); wholesale < $1 early 2026; **HPAI returned to 12 states Jun 2026** | mildly ↑ (price argument weakened) but renewed spike risk ↓ |
| 2026-09-17 | Search: Ballotpedia 2026 / potential 2026 measures | no cage-free measure certified; 85 measures certified across 35 states as of 2026-04-01; only an unrelated Oregon animal-cruelty initiative in the potential list | closes ballot route ↓ |
| 2026-09-17 | Search: THL / Humane World 2026 state session wins | all 2026 output is Farm Bill defense + rollback defense; state wins cited are cockfighting (MD) and pet-abandonment (FL) — nothing on hens | ↓ (offense capacity absent) |
| 2026-09-17 | Search: state ag-department cage-free rulemaking 2026 | only Arizona, and in the *repeal* direction (Sen. Bolick bill to strip AZDA authority); Goldwater Institute separation-of-powers challenge to the AZ rule | ↓ on the administrative route |
| 2026-09-17 | Search: Michigan repeal SB 28 | introduced 2025-01-28 by Sen. Theis; no floor vote found | irrelevant to resolution; climate evidence only |
| 2026-09-17 | USDA ERS chart 106005 (fetched, pub. 2023-03-10) | 9 states at that time; restricted-state share of flock <5% pre-2022, projected >13% by 2026; ~87% of US egg production would still legally use cages after 2026 | context; shows how much runway remains untouched |
| 2026-09-17 | Search: Polymarket / Kalshi / Manifold | **no market on this question or anything close** | no market cross-check available |
| 2026-09-17 | Search: Metaculus tournament context | question belongs to the Animal Futures Tournament (~16+ questions, $3,400 prizes) — explains `upcoming` status and tiny n | explains missing CP |

Distinct sources consulted: 20+ (see `forecast.md` §Sources).

## Dead ends and ruled-out hypotheses

- **"New Jersey already has a cage-free requirement."** Claimed by
  `eastcoasteggfarmers.com/egg-hub/nj-ny-cage-free-egg-laws-2026`, a commercial marketing page.
  **False / unreliable**: it cites no statute, and both ASPCA and AWI record New Jersey's 2023 law
  as gestation- and veal-crate only. Metaculus's exclusion list also omits NJ. Do not re-use that
  source. (It cuts the other way anyway — NJ being *without* a law keeps it as a YES candidate.)
- **Rollback news is not resolution-relevant.** Most 2025–26 coverage (NV suspension, AZ delay to
  2034, MI SB 28, CO repeal attempt, RI/UT delay to 2030) concerns the ten excluded states and
  cannot move this question directly. It is evidence about climate, nothing more. Resisted the
  temptation to treat volume of rollback coverage as if it were downward evidence on the merits.
- **A 2026 ballot-measure surprise.** Checked; nothing certified. Ruled out.
- **Searched specifically for disconfirming evidence** ("would become the Nth state", "advocates
  push 2027 session", state-by-state 2026 sweep for IL/MD/CT/VT/HI/NM). Found **none**: no bill in
  any unlisted state was reported out of committee in 2025 or 2026. Absence of expected evidence
  here is real evidence of absence — a bill that was going to pass in spring 2027 would normally
  leave a 2026 committee-hearing or pre-filing trail.

## Open questions to chase next time

1. Does any candidate state pre-file a cage-free bill for the 2027 session (NY, CT, ME, NJ, MD, NM
   pre-file windows open Nov 2026–Jan 2027)? This is the highest-information observable.
2. Farm Bill conference outcome: does §12006 (Save Our Bacon) survive into the enacted text?
3. Does DOJ file an amended complaint in *US v. California*, or win anything in *US v. Michigan*?
4. Composition of state legislatures after 2026-11-03 — any new Democratic trifectas among the
   candidate states (and does VA/NJ hold)?
5. Retail egg price path Nov 2026 – Feb 2027 given the June 2026 HPAI resurgence.
6. Re-check the Metaculus CP after 2026-09-20 reveal, and again near the 2026-12-18 close.

---

## v2 addendum — 2026-09-17 — cross-question coherence check

Triggered by the operator asking how this question relates to the Save Our Bacon Act. Searching the
repo surfaced a sibling forecast that v1 should have consulted and did not.

| Repo question | Forecast | Relevance |
|---|---|---|
| `2026-09-05-mc43616-save-our-bacon-act-enacted-into-law` | 3.0%, IQR [2.0, 4.5] (CP 5%, Pro 3%, Gold 3%, n=61) | **direct** — the federal preemption threat this question's climate argument rests on |
| `2026-09-17-mc43277-...pre-2026` (cage-free corporate pledges) | 11.9% fulfilment | corroborates "the wave's engine is gone" |
| `2026-09-17-mc43278-...pre-2026` (broiler pledges) | 3.8% fulfilment | same |
| `2026-09-12-mc43329-how-many-additional-us-states-enact-bans` | cultivated meat, not eggs | **not** a companion; shares only the tournament template and the state-calendar structure |

Facts taken from mc43616 that v1 lacked: Senate Farm Bill failed in committee 10–11 on 2026-08-06;
P(Farm Bill enacted by 2027-01-03) ≈ 0.22; P(any Prop 12 provision in final text) ≈ 0.10; 32
senators on record against SOB "in any other legislation"; no SOB amendment offered among 48 voted
at the August markup; federal preemption of state farm-animal law 0-for-6 since 2006 and 0-for-2
where the House passed language the Senate omitted (2014 stripped in conference, 2018 defeated).

**The v1 error**: an LR of 0.70 for "pendency of federal preemption deters state legislators" was
applied across the whole window. It should be ~0.92, because the threat is ~62% likely to be
visibly dead before the Jan–Jun 2027 sessions — the only period that carries meaningful
probability. Two methods for the correction: LR re-weighting gives 15.2%, scenario reconstruction
gives 12.4% (but re-imports v1's anchor). Took 14.0%.

**Channel separation** (v1 conflated these): Channel A, "why pass a law Congress will void", scales
with perceived enactment probability — and the people drafting state cage-free bills are the
Humane World lobbyists who organised the 32-senator letter, so they are not deterred; weak.
Channel B, capacity diversion, is outcome-independent and unchanged; this is why the revision is
+2 pp not +6 pp. Channel C, the anti-preemption gesture, runs off the DOJ suits, not the Farm Bill,
and is unaffected.

**Defect found and fixed**: v1 tripwire 2 ("Farm Bill conference report includes §12006") cannot
fire if there is no conference, which is the ~78% case. Retired and replaced with "119th adjourns
sine die with no Farm Bill enacted → up 3 pp".

**Error found in another file, not fixed here** (rule 8 — do not edit another version's record):
`mc43616` v1 dates the DOJ California suit to 2026-07-09 in two places. The docket it cites is
2:25-cv-06230 (filed 2025) and the dismissal was 2026-03-18, which cannot precede filing. Correct
date is July 2025. Flag for that question's next update.

Metaculus re-fetch 2026-09-17 (`raw/metaculus-2026-09-17b.json`): still `upcoming`, n 4 → 5, all
three cohorts null, no comments. Nothing to anchor on; `next_review` shortened to 2026-09-21 to
catch the 2026-09-20 CP reveal.

---

## 2026-09-24 — v3 update

**Metaculus** (`raw/metaculus-2026-09-24.json`, pre-fetched this session): CP revealed 2026-09-20.
Latest 2026-09-23: CP 12% [8, 13] n=14 (15 total); Pro 8% n=2 (was 38% at reveal — single-forecaster
noise; Pro mean 11.6%); gold 12% [8, 13] n=7 (38% at reveal → 10% on 09-22 → 12%). No comments.
CP-reveal tripwire expired unfired (2 pp gap, n < 20).

**Searches run** (2026-09-24): cage-free egg bill state legislature Sept 2026; Farm Bill Sept 2026
Prop 12 / Save Our Bacon; egg prices Sept 2026 bird flu; cage-free bills in NY/NJ/CT/ME/MD/NM 2026;
Humane World 2027 state cage-free; DOJ v. Michigan ruling 2026; BLS egg price Aug 2026; cage-free
news Sept 2026; Senate Ag 12-11 vote.

**Findings**
- Senate Ag Committee reported the Farm Bill (Agricultural Act of 2026) 12–11 party-line on
  2026-09-16 (DTN dates it 09-17), after the 10–11 failure on 08-06; McConnell returned to vote.
  SOB excluded; Ernst's push failed; Hoeven said Prop 12 belongs on the floor. Needs 60 on the floor;
  Democrats want two-year SNAP cost-share delay vs GOP one-year. Hyde-Smith: "difficult, but not
  impossible" this year. My read: P(Farm Bill enacted in 119th) 0.22 → ~0.30. Effect on this
  question via chill factor 0.92 → 0.91: ~−0.1 pp.
- BLS APU0000708111: Aug 2026 $2.272, Jul $2.189, Jun $2.141 (`raw/fred-eggs-2026-09-24.csv`).
  Egg-price tripwire ($4.00) far away.
- DOJ v. Michigan: still on Michigan's motion to dismiss (Apr 2026); no ruling found.
- No new cage-free bill, committee action, ballot measure or rulemaking found in any candidate state.
  NY S950/A652 still in committee. Search results again surfaced the unreliable East Coast Egg Farmers
  page and a search-summary claim that NJ "passed a cage-free requirement" — same error flagged as
  source 23 in v1; ASPCA/AWI remain authoritative. Ignored.
- The Humane League 2026 Eggsposé: corporate pledges past due; consistent with v2's pledge-collapse row.

**Integration**: prior 14.0%. Crowd (CP = gold = 12%) one-directional below me; shrink half the gap
(−1.0). Farm Bill vote −0.1; quiet-week hazard −0.1; round to 13.0%, IQR [9.5, 17.5].
Dead end: no market on Polymarket/Kalshi/Manifold (not re-searched beyond v1/v2's null).

Next review 2026-11-06 — after the 2026-11-03 midterms, since House control is half of the
"threat visibly dead" world weight.
