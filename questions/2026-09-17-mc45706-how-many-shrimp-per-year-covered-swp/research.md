# Research log — How many shrimp per year will be covered by SWP's Humane Slaughter Initiative agreements on July 1, 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- **Resolution source**: the headline number on <https://www.shrimpwelfareproject.org/shrimpact>
  ("Shrimps helped (in Expectation each year)"), read by Metaculus on or soon after 2027-07-01.
  Not a statistical release — a charity's own marketing page, updated at SWP's discretion.
- **Release schedule / cutoff**: none. The page carries **no "last updated" date**. Whatever
  is on it when Metaculus looks is the answer. This is a resolution-source risk, not a
  world-state risk, and it is the single most under-appreciated feature of this question.
- **Question type**: `discrete`, 51 bins of 100 M each, nominal range **7.0 – 12.0 bn**,
  `open_lower_bound: true`, `open_upper_bound: true`. Rounded to the nearest 100 M.
  Status on 2026-09-17 was still `upcoming`; `cp_reveal_time` = 2026-09-20T20:55Z,
  3 forecasters, **no CP / Pro / gold aggregation available and no comments**.
- **Edge cases and ambiguities**:
  1. Title says "covered by ... agreements"; resolution says "the estimated Shrimpact". The
     Shrimpact FAQ is explicit that the headline is **committed** volume (all signed MOUs),
     *not* installed capacity (3.6 bn today) and *not* verified use. If SWP re-bases the
     headline onto installed or verified volume, the number **falls** even though the world
     improved. Fine print does not cover this; it only covers "headline replaced by a
     range" (→ resolve at the midpoint). That rule is not neutral: today's range midpoint
     is (4.3 + 8.7)/2 = 6.5 bn against a headline of 6.3 bn, so dropping the headline in
     favour of the range would mechanically add ~0.2 bn.
  2. Retailer commitments explicitly **do not** count (FAQ).
  3. SSFI (Sustainable Shrimp Farmers of India) is being spun out into its own org and is
     not in Shrimpact; if it were folded in, the number would jump.
  4. The headline is a pure arithmetic function of two things: committed tonnage and the
     assumed grams per shrimp. A change to either moves resolution.

## The resolution mechanism, reverse-engineered

From the Guesstimate model SWP links from the Shrimpact page
(<https://www.getguesstimate.com/models/22982>, rendered 2026-09-17, cached in
`raw/guesstimate-22982-2026-09-17.txt`):

- 35 producer rows: (producer's total annual volume MT) × (share committed to stunning).
  My sum = **86,624 MT**; SWP publishes **86,875 MT**. Agreement to 0.3%.
- Scalar cell **14** g/shrimp, with "10 to 20" as the range.
- 86,875 MT ÷ 14 g = **6.20 bn** → published headline **6.3 bn**.
  ÷ 20 g = 4.34 bn → published low **4.3**;  ÷ 10 g = 8.69 bn → published high **8.7**.
- So: `headline = committed_MT × 71,429 shrimp/MT`, and the published range is *only* the
  size-uncertainty band, not a confidence interval on adoption.
- Partners' **total** production in the model = 410,546 MT, of which 86,624 MT (21.1%) is
  committed. Large headroom that does not need new MOUs — but see the one-stunner cap below.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| SWP's own agreement count, monthly increments | 6 obs | 2025-04 → 2026-09 | **+1.12 agreements/month** over 17 months; +1.25/mo over 12 months; +1.36/mo over 8 months; +1.92/mo over the last 2.6 months | SWP press releases, EA Forum, ACE, Aqua Culture Asia Pacific, Shrimpact page | **yes — primary** |
| SWP's own headline value, absolute growth | 4 obs | 2025-04 → 2026-09 | +2.1 bn/yr (17 mo), +2.3 bn/yr (12 mo) | same | yes, as cross-check |
| SWP's own headline value, multiplicative | 4 obs | 2025-04 → 2026-09 | ×1.57/yr (12 mo); SWP itself claims partnerships "essentially doubled each year since 2022" | EA Forum 2025-11-21 | yes, but **discounted** — see below |
| Scaling NGO programmes in general ("S-curve, growth then plateau") | — | — | no clean quantitative class; used only qualitatively | — | partial |

**Why the multiplicative class is discounted.** Applying ×1.57/yr to the *headline value*
implicitly assumes the marginal agreement is as large as the average historical one. It is
not: the early deals were large (5,000–6,000 MT rows in the Guesstimate), while the
programme's published eligibility floor is now **1,800–2,000 MT/producer** and "current
funding allows for one unit per producer only". The empirical marginal is
(6.3 − 4.0) / 15 agreements = **0.153 bn per agreement**, below the 0.175 bn average.
Multiplicative growth *in agreement count* (×1.57/yr) combined with the marginal 0.153 bn
gives ~8.4 bn — close to the linear answer, because 9.4 months is short. The model choice
turns out not to be load-bearing; the *rate* is.

## Decomposition

```
headline(2027-07-01)
  = 6.3
  + [new agreements in the effective window] × [bn per marginal agreement]
  + [widening of committed share at existing partners]
  ± [step change: HSI 2.0 / country-scale deal / large new funder]
  ± [methodology revision: g/shrimp, or re-basing onto installed volume]
  ± [page simply not refreshed]
```

- Effective window: 2026-09-17 → 2027-07-01 is 287 days = 9.43 months, minus residual
  publication staleness. A *constant* publication lag cancels (both endpoints are published
  values), so only 0–1.5 months of extra residual lag is modelled.
- New agreements: rate ~ lognormal, median 1.35/month, 10–90 ≈ 0.73–2.51.
- bn per marginal agreement: N(0.155, 0.018), clipped to [0.11, 0.21].
- Coded in `model.py`; 400k draws; seed 20260917.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-17 | `metaculus_aggregations.py 45706 --comments 15 --history --json` | discrete, bins 7–12 bn both-open, **no CP** (upcoming, reveal 2026-09-20, n=3), no comments | Removes the usual anchor; forecast must be built bottom-up |
| 2026-09-17 | shrimpwelfareproject.org/shrimpact (curl, full text cached) | **6.3 bn (4.3–8.7), 36 agreements, 9 countries, 86,875 MT committed; 20 stunners installed = 54,175 MT ≈ 3.6 bn**; 17 retailer policies listed | The base point, live |
| 2026-09-17 | getguesstimate.com/models/22982 via Playwright (SPA; curl returns shell only) | Full per-producer tonnage table, 14 g/shrimp conversion; reproduces 86,875 MT to 0.3% | Converts the question from "guess a charity's number" to arithmetic on agreement count |
| 2026-09-17 | shrimpwelfareproject.org/humane-slaughter-initiative | Exactly **20 producers** listed = the installed set, not the 36 signed. Floor **1,800–2,000 MT/yr**. Stunner lead time **~6 months** (4-month build + 1–2 shipping). **"Current funding allows for one unit per producer only"** | Caps the "existing partners expand" channel; confirms marginal deal ≈ 1,800–2,000 MT |
| 2026-09-17 | SWP blog + press-releases pages (raw HTML, all entry URLs enumerated) | **Last MOU press release is 2026-01-14 (Trangs Group, the 25th).** Agreements went 25 → 36 with no announcements | Press releases are *not* a usable tripwire any more; the Shrimpact page is |
| 2026-09-17 | EA Forum, "Path to helping 100 billion shrimps" (Aaron Boddy, 2025-11-21) | **24 commitments, ~4.5 bn**; "partnerships essentially doubled each year since 2022"; "**no funding gap**"; $5–10 M would "20x" it; 100 bn by 2030; ~90% of budget to HSI | Anchors the mid-2025 series and the upside narrative |
| 2026-09-17 | same post | **"It's possible that [research/implementation/MEL] is our biggest focus in 2026 (i.e. we may need to slow down to speed up)"** | Strongest stated deceleration risk — but it did **not** bite: Jan→Sep 2026 was the fastest absolute stretch yet |
| 2026-09-17 | EA Forum, "SWP's 2030 Vision & Absorbency Plans" (2025-05-02) | **17 stunners, ~3.3 bn**; 2030 goal "minimum of 50 stunners"; stunner market availability "quite limited" | Earliest series point; note SWP is already at 36 vs a 2030 goal of 50 |
| 2026-09-17 | ACE 2025 charity review | Revenue 2024 $2.9 M; capacity **$3.6 M/yr for 2026 and 2027**, $750k above projected 2025 revenue; 8 stunners deployed, 17 signed; **<10% of revenue recurring** | Funding is not the binding constraint at ~1.4 deals/month ($55k each ⇒ ~$0.9 M/yr) |
| 2026-09-17 | Aqua Culture Asia Pacific, 2026-06-29 | **"31 agreements ... now signed and over 20 stunners already supplied"**; SWP Dir. of Programme Implementation: *"There is no capacity for all the welfare commitments as it stands today. There need to be more supply chains coming online."*; Seajoy going 70% → 100% stunned by end-2027 | Fixes the 2026-06 point (⇒ 1.92 deals/mo over the last 2.6 months); names equipment supply as the real constraint; evidences the share-widening channel |
| 2026-09-17 | Undercurrent / SeafoodSource / Responsible Seafood Advocate, Apr 2026 | Aldi Süd commitment completes **all 11 major UK supermarkets**; Shrimpact page now lists **17** retailers incl. Lidl GB, Auchan, REWE, Aldi Nord/Süd | Demand-side pull is still strengthening into the question window |
| 2026-09-17 | Vetted Causes review (2025-04-27) | Criticism is about **verification**, not about the arithmetic. "SWP is currently unable to monitor stunner usage" | Raises the odds SWP re-bases the headline onto verified use — modelled at 4% |
| 2026-09-17 | Shrimp-industry press (SeafoodSource, S&P Global, vietdata) | US tariffs Aug 2026: India 25% (+25% Russia-oil ⇒ 50%), Vietnam 20%, Indonesia 19%, Ecuador 15%. Ecuador at record volumes | Ambiguous: pushes Asian supply toward EU buyers, who are the ones demanding stunning. Not modelled as a driver |

## Dead ends and ruled-out hypotheses

- **Wayback Machine (web.archive.org) was offline all session** ("Internet Archive services
  are temporarily offline"), both via `http` (egress-blocked) and `https` (IA's own outage
  page / connection reset). This is the one high-value source I could not get: a snapshot
  series of the Shrimpact page would give the true publication cadence and lag directly.
  **Retry this first at the next update.**
- Guesstimate has no usable JSON/API surface (`/models/22982.json`, `/api/models/22982` both
  return the Next.js shell; the old Heroku backend is gone). Playwright render is the way.
- **No prediction market on this.** Searched Manifold, Polymarket, Kalshi, GJOpen/INFER —
  nothing on SWP, Shrimpact or shrimp stunning. Manifold has only a *charity donation* page
  for SWP, not a market. Sentinel and Mantic do not cover animal-welfare metrics.
- "Open Philanthropy exited and left SWP with a gap": **not established.** The Oct 2024
  EA Forum post on the funding landscape concerns **wild** animal welfare (Wild Animal
  Initiative), does not mention SWP, and SWP itself said in Nov 2025 it "doesn't have a
  funding gap". Search snippets conflating the two should not be relied on. Treated as an
  unresolved, low-weight downside.
- ACE/SWP publish no year-by-year target for the headline number, so there is no "official
  2027 figure" to anchor on.

## Open questions to chase next time

1. Wayback series for `/shrimpact` → publication cadence and true lag. **Highest value.**
2. Whether the Guesstimate model row count (35) tracks the stated agreement count (36) with
   a lag — it is the cleanest early-warning signal of the headline about to move.
3. Whether SWP's 2027 funding (post-Navigation-Fund-2026) is secured, and whether any
   $5–10 M "HSI 2.0" money has landed.
4. Whether the 14 g/shrimp conversion is ever revised — it is a pure multiplier on resolution.
5. Whether SWP starts reporting a "verified use" headline alongside or instead of committed.
