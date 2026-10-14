# Research log — Will FURA introduce another cultivated meat dish on its menu before July 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: FURA's own menu (https://www.fura.space/menu), observed by the
  resolver. No scheduled data release — this resolves on an observable state of a
  restaurant menu at any point before 2027-07-01.
- Release schedule / cutoff: continuous. Early YES resolution possible the moment a
  qualifying item appears. Scheduled close 2027-06-30 20:00 UTC.
- Edge cases and ambiguities:
  - **"cultured meat other than Japanese quail"** — species-level exclusion, not
    supplier-level. A *new Vow quail format* (another Forged product) does **not** count.
    Anything non-quail does.
  - **Is cultivated *fat* a "cultured meat"?** Hoxton Farms' cultivated pork fat is
    pending SFA approval (expected late 2026 – early 2027). A dish built on cultivated
    pork fat is animal-cell-derived but is not muscle. Unresolved ambiguity; I assume a
    resolver would most likely count it (it is universally reported as a cultivated meat
    product), but weight is small either way.
  - **Is cultivated seafood "meat"?** Probably yes for a resolver, but moot: no cultivated
    seafood is approved for human consumption in Singapore (Umami Bioworks' clearances are
    pet-food only; Avant wound down its Singapore research arm).
  - **Cell-cultured milk is already on FURA's menu** and does not count — it is not meat.
  - The **quail-fat "butter candle"** already on the menu is a quail by-product → excluded.
  - Fine print: a qualifying dish counts **even if later removed**; removal/modification of
    the quail dish is irrelevant; **annulled** if FURA ceases operations before resolution.
  - One comment on the post (dendron, 2026-07-28) asks the author whether the close date
    should have been 2027-01-01. No author reply as of 2026-09-12. If the question were
    silently re-dated to January 2027, P(YES) would fall by roughly half. Treated as a
    live but low-probability administrative risk (~5%), and as a tripwire.

## Current state of the menu (checked 2026-09-12)

https://www.fura.space/menu lists exactly two cultivated items, both cultured Japanese
quail (Vow / "Forged"): "A QUAIL WALKS INTO A BAR" (S$20 parfait) and "A QUAIL WALKS INTO
A MARTINI" (S$25). Nothing non-quail. **The question has not resolved YES.**

## The binding constraint: supply, not FURA's willingness

The single most important fact found: as of the Aleph Farms approval coverage
(2026-08-04), **Vow's cultured quail is the only cultivated meat actually on sale
anywhere in Singapore** — six years after the world's first approval. Singapore has now
authorised six cultivated products (most of any jurisdiction), but authorisation ≠ sale.

| Product | Company | SFA approval | On sale in SG as of 2026-09-12? |
|---|---|---|---|
| Cultivated chicken (FBS process) | Eat Just / GOOD Meat | 2020 | No — Eat Just paused Singapore operations |
| Cultivated chicken (serum-free) | Eat Just / GOOD Meat | 2023 | No — Huber's retail run ended; ops paused |
| Cultured Japanese quail | Vow ("Forged") | 2024-04 | **Yes** — ~17 venues incl. FURA. *Excluded by the question* |
| Cultivated chicken | Parima (Vital Meat) | 2025-10 | No — 11 months, no launch; company declined to give launch plans |
| Cultivated duck / foie gras | Parima (Gourmey) | 2026-04-15 | No — "entering a new phase focused on commercial launch", no date |
| Cultivated Thin-Cut Steak (beef) | Aleph Farms | 2026-08-04 | No — SG production line (with Cell Agritech) targeted H1 2027 |
| Cultivated pork fat | Hoxton Farms | **pending** (filed 2025-11-04) | No — approval expected late 2026 / early 2027 |

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| SFA-approved cultivated products that reached actual commercial sale in SG | 6 | 2020–2026 | 2/6 ever (Eat Just briefly, Vow); 1/6 currently live | Green Queen SFA list + Aleph coverage | **Yes** — the dominant constraint |
| Lag from SFA approval → first Singapore sale, for those that did launch | 2 | 2020, 2024 | ~0 months (both launched at a flagship venue in the approval month) | Eat Just/1880 (2020); Vow/Mandala Club (2024) | Yes — launch, when it happens, is fast and venue-led |
| FURA's own rate of adding a *new cultivated meat* since opening | 1 | Oct 2023 – Sep 2026 (35 mo) | 1 per 35 mo → λ≈0.34/yr → P(≥1 in 9.6 mo) ≈ **24%** | FURA menu history, Forged-by-Vow (2024-07) | Yes — a hard floor-ish anchor |
| FURA lag from product availability → menu placement | 1 | 2024 | ~3 months (Vow approved+launched 2024-04; FURA dish covered 2024-07) | forgedbyvow.com/the-feed/forged-by-fura | Yes — FURA is a fast adopter once supply exists |

The four classes disagree in a useful way: FURA's own adoption behaviour is fast (weeks to
months), but the supply pipeline behind it is slow and has produced exactly one live
product in six years. The forecast is therefore almost entirely a forecast about Parima
and Aleph Farms, not about FURA.

## Decomposition

See `scripts/model.py` (runnable). Paths, each `P(supply live in window) × P(FURA lists it
before 2027-07-01)`, combined with the independence complement:

| Path | P(supply) | P(FURA lists in time) | Contribution |
|---|---|---|---|
| Parima live in SG by 2027-03-31 | 0.40 | 0.60 | 24.0pp |
| Parima live 2027-04-01 … 2027-06-15 (little runway) | 0.15 | 0.33 | 5.0pp |
| Aleph Farms beef live before 2027-06-15 | 0.28 | 0.16 | 4.5pp |
| Other (Eat Just return, Hoxton fat approved+launched, surprise) | 1.00 | 0.05 | 5.0pp |
| **P(YES), raw** | | | **34.4%** |
| **P(YES \| not annulled)**, closure risk 5% | | | **35.6%** |

Reasoning behind the two load-bearing numbers:

- `P(Parima live by 2027-03-31) = 0.40`. For: they hold two SFA approvals, said after the
  duck approval that they are "entering a new phase focused on commercial launch", already
  ran a public tasting of the chicken at Hue in Singapore, sell a tiny-volume luxury item
  (foie gras) that a 2,000 L pilot plant can supply, and need a commercial proof point to
  raise money in a bad funding climate. Against: 11 months of silence on the chicken
  approval, no named partner, no date, production is in France with "decentralized
  manufacturing with partners" in APAC still notional, and the company is a 2025/26 merger
  (Gourmey + Vital Meat) — consolidation under stress.
- `P(FURA lists it | Parima live with runway) = 0.60`. For: FURA is the single most
  obvious showcase venue in Singapore — World's Best Bar at the 2026 Spirited Awards
  (2026-07-27), whole brand is the "Journal of Future Food", and it adopted Vow's quail
  within ~3 months. Against: FURA's menu volumes have so far added *new categories*
  (beanless coffee, jellyfish, corn) rather than a second product in a category it already
  covers; Parima's culinary board is Michelin fine-dining and its one Singapore event was
  at a restaurant, not a bar; menu volumes turn over roughly annually, so timing must line up.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-12 | Metaculus 43281 aggregations (`raw/metaculus-2026-09-12.json`) | CP 42.0% IQR[31.0,47.7] n=27; Pro 40.0% n=5; Gold 42.0% n=15; 43 forecasters. CP opened 60% (2026-06-12), fell to ~42% by 2026-06-19, flat since | Cohorts agree; the early decline suggests others found the same supply constraint |
| 2026-09-12 | fura.space/menu (live) | Only cultured Japanese quail; two dishes. No non-quail cultivated item | Confirms not-yet-resolved; status quo anchor |
| 2026-09-12 | Green Queen, SFA approved-novel-foods list (2026-04-20) | Six cultivated approvals; Parima chicken Oct 2025, duck Apr 2026 | ↑ supply optionality |
| 2026-09-12 | Green Queen / FoodNavigator / AgFunder, Aleph Farms SG approval (2026-08-04) | Thin-Cut Steak approved; SG line with Cell Agritech operational H1 2027; launch "select restaurant partners" H1 2027; **"only Vow's cultivated quail is currently available"** | The pivotal fact. ↓ hard |
| 2026-09-12 | Green Queen / FoodNavigator, Parima duck approval (2026-04-15) | First company approved for two species; "entering a new phase focused on commercial launch"; no date, no partner | Main YES path, but undated |
| 2026-09-12 | Green Queen, Parima/Vital Meat chicken approval (2025-10-28) | Public tasting at Hue restaurant, Singapore; company "did not respond to questions about its launch plans" | ↓ — 11 months, still nothing |
| 2026-09-12 | gourmey.com/news (fetched) | Latest item is the April 2026 Singapore duck approval; nothing about a launch | Absence of expected evidence → ↓ |
| 2026-09-12 | Green Queen, Eat Just pauses Singapore operations | GOOD Meat paused SG ops, reassessing Asia strategy | Removes the oldest approval as a realistic path |
| 2026-09-12 | Green Queen, Hoxton Farms SG filing (2025-11-04) | Cultivated pork fat dossier filed; approval expected late 2026 – early 2027 | Small extra path; also a resolution ambiguity |
| 2026-09-12 | Green Queen, Vow CEO change / layoffs (2026-06-23) | New CEO Alex Andrews; ~30% staff cut 2025 + further May 2026; >5,000 kg/week; still quail-only | Vow adds nothing to YES (quail excluded); mild ecosystem stress signal |
| 2026-09-12 | FoodNavigator, "cultivated meat: who are the survivors?" (2026-05-14) | Believer, Meatable, SciFi Foods ceased operations; investor pullback; Singapore the approval hub | ↓ on supplier execution |
| 2026-09-12 | Cultivated Bites, month in review, August 2026 | Cultimate Foods shut down; no Singapore commercial launch news | ↓, confirms no launch through Aug 2026 |
| 2026-09-12 | Time Out, 2026-07-27 | FURA won **World's Best Bar** and Best International Restaurant Bar, 20th Spirited Awards | ↑ on FURA's attractiveness as a launch partner; ↓ on annulment risk |
| 2026-09-12 | forgedbyvow.com "Forged by Fura" (2024-07-06) | FURA's quail dish live ~3 months after SG approval/launch | ↑ conditional adoption speed |
| 2026-09-12 | The Star, 2026-04-11 | FURA manager Mulia Rahman: needed a licence to serve cultivated meat + SFA authorisation, "had to wait six months" | ↓ — a real per-venue friction on top of supplier availability |
| 2026-09-12 | SFA novel-food framework page | Approval is per product/ingredient and per manufacturing method; no separate published restaurant-level regime | Partially offsets the above; the 6-month wait was probably the first-time/format approval |
| 2026-09-12 | FoodNavigator-Asia, Vow APAC growth (2025-08-14) | >25,000 Forged dishes served since Apr 2024; FURA prices S$20/S$25 | Context on how a successful SG rollout looks |

## Dead ends and ruled-out hypotheses

- **Vow launching a second species.** Checked: Vow has cell lines for 50+ species but is
  quail-only commercially and is cutting costs; no non-quail Vow product is in the SFA
  pipeline. Ruled out as a path.
- **Cultivated seafood.** No human-food approval in Singapore. Umami Bioworks' EU
  registration is pet food; Avant wound down its Singapore research arm. Ruled out.
- **Eat Just / GOOD Meat return.** Operations paused, Asia strategy under review, and the
  "3% cultivated chicken" formulation drew expert criticism — an unlikely fit for a venue
  whose brand is credibility about future food. Kept only inside the 5% "other" bucket.
- **A FURA partnership already announced.** Searched several phrasings pairing FURA with
  Gourmey / Parima / Aleph: nothing. No teaser, no supplier announcement.

## Open questions to chase next time

- Has Parima named a Singapore launch date, distributor or venue?
- Has Aleph Farms' Cell Agritech line come online, and has it named restaurant partners?
- Has Hoxton Farms' pork fat been approved, and would the resolver count cultivated fat?
- Has FURA published "Journal of Future Food, Volume Three", and what is in it?
- Did the question author answer dendron's 2026-07-28 comment about the close date?

## 2026-10-14 — v2 update log

| Search / fetch | Result | Use |
|---|---|---|
| fura.space/menu (live) | two cultivated items, both cultured Japanese quail; "Forged tallow" in bread service (quail by-product) | not resolved |
| Parima news page | latest 2026-07-02 (multi-tonne production with Vow); no Singapore launch | Parima-early hazard decay |
| "Parima Gourmey Singapore launch restaurant" / "Parima news Sept Oct 2026" | nothing after July | absence of evidence |
| Aleph Farms Singapore Oct 2026 | still the August approval coverage; H1 2027 target | unchanged |
| Hoxton Farms SFA approval | still pending, late 2026 – early 2027 guidance | unchanged |
| FURA news 2026 / Volume Three | only July World's Best Bar coverage | unchanged |
| Metaculus (raw/metaculus-2026-10-14.json) | CP 38, Pro 40 (n=3), gold 44 (n=13, IQR 40–82); one comment (close-date query, unanswered) | cohort table |

Open next time: same list as above; also whether the gold cohort's 82% upper quartile reflects a fact (check comments again).
