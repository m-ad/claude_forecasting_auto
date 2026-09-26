# Research log — Will Trump demolish the Kennedy Center before January 1, 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: news reports; Metaculus admins. No data series.
- Release schedule / cutoff: event must occur before 2027-01-01. Question closes 2026-12-15. CP hidden until 2026-09-29.
- Edge cases and ambiguities: "substantially demolished" = more than a de minimis part of the *structure* intentionally destroyed. Author comment (2026-09-26): interior renovation/gutting does NOT count; "structure" = the building itself. Open: exterior soffit/facade removal during "emergency repairs"; a partial teardown begun in late December.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Presidential demolition threats vs. federal landmarks | ~0 | — | n/a | — | no |
| Trump built-environment threat→action (East Wing) | 1 | 2025 | 1/1 fast action, but no court order and White House exempt from NHPA §106 (§107) | NBC 2025-10-23, PolitiFact 2025-10-22 | yes, as upward caution |
| Federal landmark demolition within 3 months under active PI + notice order | few | — | <5% | judgement | yes |

## Decomposition

Path A lawful: P(notice by 11/30) 0.12 × P(courts don't block) 0.20 × P(starts before 1/1) 0.6 ≈ 1.4%
Path B fait accompli ≈ 0.7%
Path C resolution edge (repairs remove structure, counted) ≈ 0.8%
Path D engineering emergency partial teardown ≈ 0.5%
Total ≈ 3.4% → median 3.5%, IQR [1.5, 6.0]

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-26 | Metaculus aggregations 45810 | status upcoming, n=16, CP hidden until 09-29; author clarifies interior gutting ≠ demolition | defines bar |
| 2026-09-26 | "Kennedy Center demolition Trump September 2026" | Trump "ripped down" 09-16; DEMOLISHED poster; National Review "very real possibility"; Axios "can't be demolished overnight" (403) | ↑ salience |
| 2026-09-26 | 30-day notice ruling | Cooper minute order 2026-09-17: 30 days' written notice for any scope change incl. demolition; sworn status report due 09-23 | ↓ strong |
| 2026-09-26 | NBC: DOJ filing 2026-08-25 | "will be required to be taken down"; amphitheater alternative; donors won't give without Trump recognition | ↑ leverage signal |
| 2026-09-26 | Roll Call 09-24, Forbes 09-25, BGov | Merkley + Murkowski bill to bar demolition without Congress; Simpson (R): "not going to tear down"; UC attempt likely to fail; appropriations leverage at year-end | ↓ |
| 2026-09-26 | Kalshi News 09-18 | Kalshi demolition 2026 at 11%; Trump name on facade: 6% by 10/1, 35% by 1/1/27, 43% by 7/27 | anchor |
| 2026-09-26 | Truth Social 09-15 (CNBC) | "Renovation and Reconstruction … cannot begin until such time as the D.C. Circuit rules"; "destined to doom" only if SCOTUS doesn't overturn | ↓ timeline |
| 2026-09-26 | CBS | KC VP PR Roma Daravi: "nothing is being demolished"; fencing and forklift on site | mixed |
| 2026-09-26 | Raw Story / Forbes / WaPo Times on 09-23 declaration | Floca sworn declaration: temporary safety closure (Walter P. Moore report), reopen once fixed; nothing says tear down; closure through ≥09-30, weekly re-eval | ↓ |
| 2026-09-26 | PolitiFact 09-18 | NHPA §106 review, environmental review, federal disposal procedures likely required; ACHP rule rewrite in progress (July 2026) | ↓ |
| 2026-09-26 | East Wing precedent | demolition began 2025-10-20 with little warning after July assurance it wouldn't touch the building | ↑ tail |
| 2026-09-26 | Protests (ABC, Fox5, WUSA) | human chain ~09-19 | → |
| 2026-09-26 | Beatty press release | March 16 board meeting discussed closing and "potentially demolish"; board approved $257M rehab 2026-03-16 (ENR) | context |
| 2026-09-26 | D.C. Circuit appeal on name (26-5224) | denied stay 2026-07-08; merits argument date not found | open |

## Dead ends and ruled-out hypotheses

- Axios local 09-21, Washington Times, NPR, CourtListener docket, Kalshi market page, The Hill analysis: 403/503/429 via WebFetch.
- No Polymarket, Manifold, Sentinel, Mantic, GJOpen market found.
- No evidence of demolition contractor, permit or notice filing as of 2026-09-26.

## Open questions to chase next time

- Metaculus CP/Pro/gold after 2026-09-29 reveal.
- Kalshi market rules (does partial demolition count?) and current price/volume.
- D.C. Circuit merits schedule in Beatty v. Trump (No. 26-5224) and the second name appeal.
- Any 30-day notice filed in D.D.C.; DC Preservation League PI motion outcome.
- CR/appropriations text: demolition-ban rider?
