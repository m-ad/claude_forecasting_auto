# Research log — How many seats will PP and Vox collectively receive in the 2026 Spanish general election?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: official result of the snap general election to the Congreso de los
  Diputados (350 seats, D'Hondt by province) — see `forecast.md` digest for the exact Metaculus text.
- Election date: **Sunday 29 November 2026** (Sánchez announced the dissolution on 2026-10-05 after
  Congress rejected two housing decree-laws; LOREG fixes election day as the 54th day after the decree).
- Majority line: 176. 2023 result: PP 137 + Vox 33 = 170 (PP 136 on election night, 137 after the
  CERA overseas count).
- Edge cases: PP joint lists with regional partners (2023: UPN ran separately in Navarre, 1 seat);
  the overseas (CERA) vote can move one seat between election night and the final scrutiny.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Final-poll error on PP+Vox bloc, Spanish generals | 4 (2016, 2019A, 2019N, 2023) | 2016–2023 | errors roughly −15 (2019A), +5/+10 (2019N, Vox surge), −8 to −10 (2023), +PP (2016) ⇒ SD ≈ 10 seats, mild right-overstatement tilt | El Independiente / Menorca.info post-mortems of 23J; own recollection of 2019 (flagged) | yes |
| Drift from campaign start (snap call) to result, 2023 | 1 | May–Jul 2023 | early-June polls ≈ 180–185 → result 170 | own recollection, consistent with post-mortems | yes, weak |
| Seats per point of combined vote in the 50% region | — | — | ≈ 4–5 seats per pp of PP+Vox vote | D'Hondt behaviour; 2023 45.5% → 170, polls 51% → ~200 | yes |

## Decomposition

- Polling centre (Oct 1–11, private pollsters, 17 polls): PP+Vox median ≈ 201–203, range 193–212.
  RTVE average 2026-10-05: PP 137 + Vox 65 = 202. CIS (Tezanos, strong pro-PSOE house effect): 186.
- Combined vote in private polls ≈ 50–52% (PP 31–34, Vox 18–19). Polymarket "PP+Vox ≥ 50% of vote" 46.5%.
- Adjustments:
  1. Snap-election mobilisation of the left (2023 analogue): −3 to −5 seats expected drift.
  2. Historical right-overstatement in 2019A and 2023: −2 seats on the mean (half-weight; 2016 and 2019N
     went the other way).
  3. Bloc vote is far above 2023 (45.5%), so D'Hondt bonus is large; losses come mainly in
     marginal 3–5-seat provinces.
- Net centre ≈ 196; SD ≈ 12 (poll error ≈ 10, campaign drift ≈ 6).

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-17 | "elecciones generales 29 de noviembre 2026 Sánchez convoca" | Diario de Avisos, Libertad Digital: snap election called 2026-10-05 for 29 Nov after housing decrees failed | defines question |
| 2026-10-17 | Wikipedia opinion polling next Spanish GE | 25 polls 24 Sep–11 Oct; PP+Vox 186 (CIS) to 212 (Hamalgama) | sets centre ~201 |
| 2026-10-17 | democrata.es Sigma Dos / SocioMétrica / GAD3 / Hamalgama | 203 / 205–207 / 198 / 212 | consistent |
| 2026-10-17 | ARA 2026-10-09 "What do the polls for the Spanish elections of November 29 say?" | PP 31–34%, PSOE 25–27%, Vox 18–19% | vote shares |
| 2026-10-17 | JPost/Media Line on RTVE average 2026-10-05 | PP 137 + Vox 65 = 202 | centre |
| 2026-10-17 | biobiochile / elcomercio.pe on CIS October | PSOE 34.0, PP 22.2, Vox 17.1 (CIS) | outlier, low weight |
| 2026-10-17 | El Independiente / menorca.info / diaridetarragona on 23J poll failure | 2023 polls overstated PP (GAD3 150 vs 137; Sigma Dos 145–150), understated Vox; bloc 169–170 vs majority forecast | −2 seats bias, wider tails |
| 2026-10-17 | BOE via Diario de León / Artículo14 / RTVC / INE | Real Decreto 806/2026 (BOE 2026-10-06): election Sun 29 Nov; campaign 13–27 Nov; Cortes constituted 23 Dec | date confirmed |
| 2026-10-17 | Orain 2026-10-13; Artículo14 / democrata.es | PP–UPN agreement in principle for a joint Navarre list "UPN en coalición con el PP" (pending UPN Consejo Político ratification) | ±1 seat attribution edge case |
| 2026-10-17 | Polymarket spain-general-election-* | PP win 84.5% ($54K); PP+Vox majority 83.5% ($2K); PP+Vox ≥50% vote 46.5% ($4K) | majority prob ~ consistent with my P(≥176) |

## Dead ends and ruled-out hypotheses

- Key Data/Público 2026 average: not found (search returned 2023 items).
- Politico Poll of Polls: not retrieved.

## Open questions to chase next time

- Official candidate lists (any PP joint lists with UPN/others? whether they count).
- Debates schedule; first campaign-period polls (campaign starts 13 Nov; poll publication ban from 24 Nov).
- CIS pre-electoral macro-survey (usually ~2 weeks before election).

## Resolution-text retrieval attempts (2026-10-17, second pass)

- Real criteria still unreadable: bot-key API returns `null` description/criteria/fine print on every endpoint (`/api/posts/<id>/`, `/api/questions/<qid>/`, `/api/posts/?ids=`, `?lang=` variants) while the post is pre-open; browser path fails because the proxy denies `brunhild.challenges.cloudflare.com` (Cloudflare challenge); no Wayback/archive.ph copies; unauthenticated API 403.
- The key-authenticated API **does** return text for open posts (verified on 45515, 45262, 45617, 45670), so the real text becomes readable without Cloudflare once the post opens (open_time below).
- open_time 2026-10-18T17:00Z. Author darkives; their open election question 45670 (Israel, most seats) resolves on the officially reported result and is annulled if the election is cancelled/postponed past 2026-12-31. **Template evidence only** — the PP–UPN joint-list attribution question remains open.
