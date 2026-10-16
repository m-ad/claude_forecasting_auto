# Research log — How many executions will be carried out in the US in 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: **not yet published** (post "upcoming" until 2026-10-12; API returns
  null resolution_criteria / fine_print on 2026-10-09). Assumed DPIC 2026 execution list.
- Release schedule / cutoff: DPIC updates within ~1 day of each execution. Close 2026-12-02,
  scheduled resolve 2027-01-01. Note close is **before** Hasan's Dec 3 date and all December
  Florida dates — forecasts are frozen with most December uncertainty unresolved.
- Edge cases and ambiguities: military execution (Hasan) counted?; failed execution (Pike,
  TN, 2026-09-30, alive in hospital) — not counted unless DPIC adds; Dec 31 late-evening
  time zone. Tournament: Metaculus Cup Fall 2026; CP reveal 2026-10-15.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| 2026 YTD run-rate | 30 | Jan 1 – Oct 8 | 0.107/day → +9.0 | DPIC 2026 | yes (low anchor) |
| 2026 recent pace | 14 | Jul 1 – Oct 8 | 0.14/day → +11.8 | DPIC 2026 | yes |
| 2025 same window | 13 | Oct 10 – Dec 31, 2025 | +13 | DPIC 2025 | yes (high anchor) |
| Warrant completion 2026, ex-OH/PA | 30/38 | 2026 | 79% | DPIC outcomes 2026 | yes, per-state rates used |
| FL Nov 6 – Dec 31, 2025 | 4 | 2025 | 4 FL executions | DPIC 2025 | yes, for FL new-warrant prior |
| Military executions after presidential approval | 1 (Gray 2008) | 1961– | 0/1 carried out (federal habeas stay) | memory, well-known; verify | yes, qualitative |

## Decomposition

30 done + 9 scheduled (E≈7.1) + FL new warrants Nov 6–Dec 31 (E≈3.4) + others Poisson(0.45).
Monte Carlo in `raw/model_v1.py` with shared logit shock σ=0.4. Output: mean 40.8,
IQR [40, 42], 5–95% [37, 44]. PMF: 36:1.3% 37:3.4% 38:7.2% 39:12.6% 40:17.8% 41:20.0%
42:17.5% 43:11.6% 44:5.7% 45:2.0%.

Per-warrant p: Robertson .96, Reaves .93, Guardado .92, Taylor .87, Weisheit .72,
Rubio .72, Pavatt .72, Dennes .82, Hasan .40.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-09 | Metaculus API post 45255 | MC, options <39/39/40/41/>41; criteria hidden until open 10-12 | assume DPIC |
| 2026-10-09 | DPIC executions/2026 | 30 executions, 6 states, FL 16; updated 10-08 | base 30 |
| 2026-10-09 | DPIC upcoming executions | 9 dates Oct 13 – Dec 3 (Thompson already removed) | core of model |
| 2026-10-09 | DPIC outcomes of warrants 2026 | 58 dates, 30 executed, 19 inactive (11 OH/PA reprieves) | completion base rates |
| 2026-10-09 | DPIC executions/2025 | 47 total; 13 after Oct 8; FL 4 in Nov 6 – Dec 31 | outside view, FL prior |
| 2026-10-09 | "DeSantis signs death warrant November 2026" | Guardado warrant signed Oct 5 for Nov 5; "20th warrant"; FL record | FL pace ↑ |
| 2026-10-09 | Thompson competency | DeSantis withdrew Thompson warrant (Oct 8) — first ever withdrawal | −1 vs naive calendar |
| 2026-10-09 | Christa Pike Tennessee | failed execution 9/30; Gov. Lee halted TN for rest of 2026 (Sutton Dec 3 off) | TN = 0 |
| 2026-10-09 | Weisheit Indiana | Nov 5 date; no drugs acquired yet; clemency hearing Oct 16/19; Braun denied previous two | p=.72 |
| 2026-10-09 | Rubio Texas | competent per trial court Oct 7; CCA review pending | p=.72 |
| 2026-10-09 | TDCJ scheduled executions | only Rubio 11/12, Dennes 11/19 | TX can't add (90-day rule) |
| 2026-10-09 | Pavatt Oklahoma | clemency hearing Oct 14; innocence-type claims; ex-DOC director support | p=.72 |
| 2026-10-09 | Taylor Alabama | Ivey set Nov 5–6 window; no clemency plans; Burton commuted earlier in 2026 | p=.87 |
| 2026-10-09 | Hasan firing squad | Trump approved Oct 2; Army set Dec 3; livestream; counsel Galligan: habeas "distinct possibility" | p=.40 |
| 2026-10-09 | Mississippi date 2026 | nothing; pending requests (Manning/Simon-type) long dormant | others small |
| 2026-10-09 | Arizona warrant 2026 | nothing after McGill (May 20); AG silent; Wikipedia says 1 AZ request pending | others small |
| 2026-10-09 | SC / MO / LA / UT / GA December | none scheduled; GA Humphreys stayed Sep 16 | others small |
| 2026-10-09 | Kalshi/Polymarket/Manifold executions market | none found | no market anchor |

## Dead ends and ruled-out hypotheses

- No prediction market on US 2026 execution counts found (Kalshi, Polymarket, Manifold).
- DPIC outcomes page has a missing row (Reaves Oct 20) — data inconsistency, not a signal.
- "Jesse Guardado" is a 2026 warrant (signed Oct 5), not a 2025 case.

## Open questions to chase next time

- Resolution text (2026-10-12): source and whether military counts.
- CP / Pro / gold on 2026-10-15+.
- Next FL warrant (expected ~Oct 15–25) and its date; any December double-executions.
- Pavatt board vote (Oct 14); Weisheit clemency + drug procurement; Rubio CCA review; Hasan habeas.
- Arizona: identity/date of the pending warrant request, if any.

## 2026-10-16 — v3 update

- DPIC (fetched 2026-10-16, updated 2026-10-13): 31 executions; Robertson executed Oct 13. Upcoming list unchanged apart from that: Reaves 10/20, Weisheit/Taylor/Guardado 11/5, Rubio/Pavatt 11/12, Dennes 11/19, Hasan 12/3. Warrant outcomes: 31 of 58. Snapshots in raw/dpic-*-2026-10-16.html.
- Pavatt: board denied clemency 3–2 on Oct 14 (KOSU, KFOR, News9).
- Hasan: Trump cancels livestream on Oct 15 but says "He will die, as scheduled"; no habeas found.
- Weisheit: defense asks to move the date to Nov 19 for brain scans; clemency testimony Oct 19; drugs unconfirmed (Indiana Capital Chronicle, Oct 13).
- Searched: new Florida warrant after Oct 5 (none found), a ruling on Guardado's protocol suit (none), a Rubio stay (none), Florida drug supply (no shortage reported), other-state December dates (none; Wikipedia lists 13 pending requests: TN 6, TX 4, MS 2, AZ 1).
- Metaculus (pre-fetched raw/metaculus-2026-10-16.json): CP/Pro/gold all ~34–37% on <39 and ~10–12% on >41. The exmateriae comment's Monte Carlo (FL new mean 2.5) gives 26/19/22/18/15.
- Model v3 (raw/model_v3.py): 17.7/16.8/21.0/19.9/24.6. Blended 80/20 with the Pro+gold mean → 21/18/20.5/18.5/22.
