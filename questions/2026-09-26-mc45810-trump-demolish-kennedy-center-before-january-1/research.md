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

## Update 2026-10-04 (v2)

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-04 | Metaculus aggregations 45810 (raw/metaculus-2026-10-04.json) | Open since 09-28. CP 7.0% [4.9,10] n=91 (opened 9–12.5%, down to 6–7% from 09-30); Pros 7.0% [7,12] n=9 (noisy 15→7); gold 10.0% [4,12] n=28. Comments list empty | ↑ partial weight (0.2 log-odds) |
| 2026-10-04 | Kalshi API (raw/kalshi-2026-10-04.json) | KXKENNEDYDEMOLITION-27 bid 2/ask 4/last 5¢, vol 14.4k, OI 9.3k. **Rules: FULL demolition only; partial, component removal, strip-to-steel excluded.** KXKENNEDYDEMOVOTE-27 10/18 last 2, thin. Facade name before 2027: 22/28. Reopen markets thin | ↓ small; Kalshi YES ⊂ Metaculus YES |
| 2026-10-04 | Kalshi events endpoint | Paginating /events trips 429 quickly; found tickers after ~70 pages. Next time hit /events/<ticker> directly | method |
| 2026-10-04 | Lee objection (East Idaho/AP 09-29; Forbes 09-29) | Lee blocked UC Mon 09-28; bill reintroduced both chambers 09-29 (Merkley, Pingree); Lee office: "partisan scaremongering" (snippet, primary not seen) | ↑ tiny |
| 2026-10-04 | ABC 10-01 internal email | Floca: remain temporarily closed; egress assessment (exits blocked during soffit repairs) 1–2 weeks; "not a reopening date"; court update due Fri 10-02 | path C slightly ↑; reopen tripwire dead |
| 2026-10-04 | The Hill / WaPo 10-01, Time interview | Trump: "I'm not committing to anything. We're going to see how it plays out in court"; building in "terrible, terrible shape" | → |
| 2026-10-04 | Deadline / CNN 10-02 | Kennedy Center Honors moved to Capital One Arena | closure through Dec |
| 2026-10-04 | Washington Sun on 09-23 filing | ~150 lb plaster fell 60 ft; water in transformer vault; rigging problems; "no finding that the center needs to be demolished" | ↓ (already in v1) |
| 2026-10-04 | CourtListener DCPL v. Board (snippet) | PI denied; relied on ED sworn testimony Center "would not be demolished or rebuilt". Opinion date not confirmed | ↓ small |
| 2026-10-04 | Manifold API | "demolished during Trump's presidency" 32%, 15 traders, to 2029 | not comparable |
| 2026-10-04 | Searches for contractor/permit/notice/SCOTUS/D.C. Cir. argument | nothing found | tripwires unfired |

Dead ends: CNN (451), Deadline (402 tollbit), The Hill, WaPo, Forbes (403), CourtListener body empty.

Open next time: content of the 10-02 court status report; egress assessment result (~10-08–10-15); D.C. Circuit 26-5224 argument date; any board meeting notice; CR text (Dec 11?) for a rider; Metaculus comments via browser.

## 2026-10-14 — v3 update log

| Search / fetch | Result | Use |
|---|---|---|
| "Kennedy Center demolition notice court October 2026" | only Sept 17 order coverage | notice tripwire unfired |
| Beatty v. Trump status report Oct 2026 | motion to compel (10-05); PowerPoint + 163-p JLL plan unsealing, redactions due 10-14, reply 10-19 | litigation focus is closure |
| CourtListener RECAP doc 94 (snippet) | 10-02 status report: Walter P Moore final soffit report 9-25, 46/278 panels severe; egress procedures under JLL/ATSR assessment | repairs framing |
| Newsweek 10-08 | JLL plan described as renovation; no demolition | path C watch |
| Kalshi API (raw/kalshi-2026-10-14.json) | demolition 2/3¢, no trades since 10-04; reopen before 2028 21/30¢ | flat |
| Metaculus (raw/metaculus-2026-10-14.json) | CP 4.4, Pro 8 (n=8), gold 4.4; comments at 4–5% | pooling anchor ~5% |

Dead ends: CourtListener API throttled (125/day), docket page 403.

Open next time: egress assessment result; unsealed JLL plan contents after 10-19; any board meeting notice; D.C. Circuit argument date.
