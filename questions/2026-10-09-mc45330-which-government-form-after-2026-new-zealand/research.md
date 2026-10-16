# Research log — Which government will form after the 2026 New Zealand general election?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: the New Zealand Government (seating plan for the 55th Parliament); a government is formed on appointment by the Governor-General (Cabinet Manual).
- Release schedule / cutoff: election 7 Nov 2026; official results 27 Nov; writ return 3 Dec (legal deadline 15 Jan 2027). The Metaculus question closes 6 Nov, before the vote.
- Edge cases and ambiguities: "None before January" if nobody is sworn in by 31 Dec. Caretaker governments do not count. A minority government with confidence and supply still counts as led by the major party.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| MMP government led by Labour or National | 10 | 1996–2023 | 100% | election history | yes ("Other" ≈ 1%) |
| First-term government re-elected for a second term (MMP) | 3 | 2002, 2011, 2020 | 3/3 | election history | weak, low weight |
| Days election → swearing-in > 54 | 10 | 1996–2023 | 1/10 (1996) | 1News 2023; Newsroom 2017; memory for older years (1996: 10 Dec deal, 16 Dec swearing-in, not re-verified) | yes → about 8% overall |

## Decomposition

Monte Carlo over the polling average (`raw/seat-sim-2026-10-09.py`). P(right majority) 36%. P(left + TOP majority, left ≥ right) 30%. P(left + TOP majority, right larger, TOP pivotal) 28%. P(other hung) 6%. P(TOP clears) 71%.
Conditional mapping → National-led 47.2 / Labour-led 44.6 / none 8.1. I moved 0.7pp to "Other". Final: 46.5 / 44.5 / 8.0 / 1.0.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-09 | Metaculus aggregations script | criteria and fine print; upcoming, n=2, no CP | — |
| 2026-10-09 | Wikipedia opinion polling | 15 latest polls plus seat projections; latest Curia: right 65; Verian: left + TOP + TPM 65 | core input |
| 2026-10-09 | Wikipedia 2026 election | dates (official 27 Nov, writ 3 Dec); National rules out TOP; Labour–Greens pact (Feb 2026); TPM holds 6 of 7 Māori seats | timing → "none" option |
| 2026-10-09 | "Opportunity Party coalition ... Peters ... Hipkins" | Labour rules out NZ First (~10 Aug); TOP won't back Peters as foreign minister | removes Labour+NZF path |
| 2026-10-09 | interest.co.nz TOP bottom lines (29 Sep) | 5 bottom lines; Hipkins hasn't ruled TOP out | TOP leans left |
| 2026-10-09 | Waatea (19 Aug) | Hipkins: TPM unlikely to get senior roles; Luxon rules out TPM | TPM votes left regardless |
| 2026-10-09 | Spinoff Whakaata Māori–Curia polls | TPM dominant on Māori roll; Maipi-Clarke +19 in Hauraki-Waikato | overhang 2–4 likely |
| 2026-10-09 | Polymarket gamma API (3 markets) | coalition: Nat+ACT+NZF 43, Lab+Grn 26.9, Lab+Grn+TPM 17, Other 7.8; PM: Luxon 55.5 / Hipkins 44; most seats: Lab 54 / Nat 45.5 | cross-check; near coin flip |
| 2026-10-09 | Kiwipolls (8 Oct) | Coalition retains 40.05%, Opposition 3.75%, disputed 56.2% | TOP-pivotal is modal |
| 2026-10-09 | election2026.nz (5 Oct) | L57 / TOP7 / R59 of 123 | same |
| 2026-10-09 | Manifold API | Luxon PM on 1 Feb 2027 52–53%; TOP ≥1 seat 74–84% | discounted |
| 2026-10-09 | formation timelines 2023/2017 | 2023: 44 days; 2017: deal at 26 days, sworn in 26 Oct (33 days) | timing base rate |

## Dead ends and ruled-out hypotheses

- TAB (New Zealand bookmaker) odds: not found via search.
- No Good Judgment Open, INFER, Sentinel or Mantic item found on NZ government formation (not searched exhaustively; check next time).
- Grand coalition (National + Labour): Polymarket 0.7%; ignored except inside "Other"-adjacent noise.

## Open questions to chase next time

- Metaculus CP, Pro and gold after 18 Oct.
- Does TOP declare a preference, or a willingness to abstain? Does National soften its TOP rule-out?
- Final-fortnight polls on TOP vs 5%; Mt Albert electorate polling for Qiulae Wong.
- Leader-debate effects; NZ First trajectory.

## 2026-10-16 — v2 update log
- Metaculus snapshot `raw/metaculus-2026-10-16.json` (pre-fetched): n=58, CP/Pro/gold hidden until 2026-10-18; 2 comments (55%, 56% National-led).
- Polymarket gamma API re-fetched (`raw/polymarket-*-2026-10-16.json`): coalition Nat+ACT+NZF 39.5 (was 43.0), Lab+Grn 33.0 (26.9), Lab+Grn+TPM 16.5 (17.0), Other 9.05; Luxon 52.5 (55.5), Hipkins 45 (44); most seats Lab 54 / Nat 45.
- Wikipedia polling (accessed 2026-10-16): new polls Verian 8–12 Oct (TOP 8), Anacta 6–10 Oct (TOP 5.4). 7-poll mean TOP ≈ 6.2, right ≈ 48.3, left ≈ 44.4.
- 1News 13 Oct: Wong — approach largest party first, then second; may wait for specials. Luxon re-rules out TOP and grand coalition.
- RNZ 9 Oct live: Hipkins — TOP vote is "giving your vote away"; "no deals pre-election".
- Kiwipolls 13 Oct: coalition retains 38.9 / disputed 58.4 / opposition 2.8. election2026.nz 12 Oct: L57/TOP7/R59.
- Searches: "Opportunity Party poll ... October 2026"; "Luxon Opportunity rule out confidence supply ..."; "Qiulae Wong Labour coalition confidence supply"; "Hipkins Opportunity Party coalition election campaign news".
- Note: leading option flipped to Labour-led (45.5 vs 44.5), so ledger median/IQR now refer to Labour-led.
