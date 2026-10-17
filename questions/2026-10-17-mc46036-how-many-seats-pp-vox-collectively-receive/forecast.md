# How many seats will PP and Vox collectively receive in the 2026 Spanish general election?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46036/ |
| **Type** | discrete (seats; Metaculus range 165–215, both bounds open) |
| **Opened / Closes / Resolves** | 2026-10-18 / 2026-11-29 / 2026-11-30 |
| **Status** | open |
| **Current forecast** | **Median 197 seats, IQR [189, 205]** (v1, 2026-10-17) |
| **Community (as of 2026-10-17)** | no CP yet (opens 2026-10-18, reveal 2026-10-25) · Pro — · Gold — · n=5 pre-open |
| **Next review** | 2026-10-24 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-17

### What resolves YES
Discrete question: the combined number of Congress of Deputies seats (of 350) won by the Partido
Popular (PP) and Vox in the snap general election of **Sunday 29 November 2026** (Real Decreto
806/2026, BOE 2026-10-06; campaign 13–27 Nov; majority = 176). **Caveat — inferred digest:** the
Metaculus resolution text could not be retrieved (pre-open post; bot-key API returns `null`
criteria, browser fetches Cloudflare-challenged — see `research.md`). Presumed source: official
results (Ministry of the Interior / Junta Electoral Central). Edge cases: (a) **PP–UPN joint list in
Navarre** ("UPN en coalición con el PP", agreed in principle 2026-10-13) — whether its seat(s) count
as PP is unknown; worth ±1; (b) the overseas (CERA) count can move one seat after election night
(2023: PP 136 → 137); (c) open bounds — values <165 or >215 are possible.

### Outside view
Two reference classes:
1. **Final-poll accuracy for the PP+Vox bloc** (2016, Apr-2019, Nov-2019, 2023): errors from about
   −15 to +10 seats, SD ≈ 10, with the two most recent snap-style Sánchez elections (Apr 2019, Jul 2023)
   both *overstating* the right (2023: GAD3 had PP 150, result 137; private polls implied a PP+Vox
   majority, result 170).
2. **Campaign drift after a Sánchez snap call** (2023, n=1): bloc fell ~10–15 seats from early-campaign
   polls to the result as the left mobilised. Weak, but it is exactly this playbook (housing as the
   mobilising issue after Congress sank two housing decrees).

### Inside view
Polling centre (17 private polls, 24 Sep–11 Oct): PP 121–148, Vox 61–74, **bloc median ≈ 201–203**,
range 193 (GESOP) – 212 (Hamalgama); RTVE average 2026-10-05: 137 + 65 = **202**. Combined vote ≈
50–52% (PP 31–34%, Vox 18–19%; 2023: 45.5%). In this range D'Hondt converts ≈4–5 seats per point of
bloc vote. CIS (PSOE 34%, PP 22%; projected ~186 seats) has a strong documented pro-PSOE house effect
and gets low weight.

Adjustments to 202: snap-election left mobilisation −3 · recent right-overstatement −2 → **197**.
Spread: poll error SD ≈ 10 ⊕ six-week campaign drift SD ≈ 6 → SD ≈ 12–13; Student-t(5) for fat tails.

### Evidence
- Polls are unusually consistent: every private pollster since late September has PP+Vox ≥ 189
  (lower bracket bounds); the right's lead held through the snap announcement (LR for "≥190" ≈ 2 vs.
  a world where the bloc is really ~180).
- Vox has nearly doubled since 2023 (12.4% → 18–19%) — more seats in mid-sized provinces, but also
  more fragmentation risk if PP voters return tactically.
- **Disconfirming:** PSOE-commissioned poll (n=7,000) has PSOE 129 vs PP 126 (bloc 197); CIS 186.
  Both are partisan/house-effect outliers but point the same way as the 2023 pattern.
- PP–UPN joint list (if counted) adds ~0–1 vs. separate lists.

### Other forecasters
| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | — | 2026-10-17 | pre-open |
| Metaculus Pro | — | 2026-10-17 | n/a pre-open |
| Metaculus gold medalists | — | 2026-10-17 | n/a pre-open |
| Polymarket "PP + Vox majority?" | 83.5% | 2026-10-17 | $2K volume — thin |
| Polymarket "PP + Vox ≥ 50% of vote?" | 46.5% | 2026-10-17 | $4K volume |
| Polymarket "Spain GE winner: PP" | 84.5% | 2026-10-17 | $54K |
| RTVE poll average | 202 | 2026-10-05 | via JPost/Media Line |

My P(≥176) ≈ 95% vs. Polymarket 83.5%. The market is thin ($2K), and its 46.5% on "≥50% of vote" is
consistent with my centre (bloc vote ≈ 50% ⇔ ≈ 195–200 seats). I would sell the majority market's NO
at 16.5¢; the gap is not from a fact I am missing that I can find.

### Scenarios
| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | 2023 repeat: left mobilises on housing, polls overstate right | 25% | 180–190 |
| 2 | Polls roughly right, mild drift | 45% | 191–204 |
| 3 | Right consolidates / Vox surge beyond polls (Nov-2019 style) | 25% | 205–215 |
| 4 | Tails (<180 or >215) | 5% | — |

### Sensitivity
| Assumption | If instead | Forecast becomes |
|---|---|---|
| −5 seats net adjustment to the poll centre | no adjustment (trust polls) | Median 202, IQR [194, 210] |
| −5 | full 2023-size drift (−14) | Median 188, IQR [180, 196] |
| SD ≈ 13 | SD ≈ 9 (polls more accurate than history) | IQR [191, 203] |

### What would change my mind (tripwires)
- [ ] CIS pre-electoral macro-survey (≈ 2026-11-12) or any three private polls in 13–23 Nov with bloc ≤ 190 → down, 6 seats
- [ ] Private-poll bloc median ≥ 205 in the final publishable week (by 2026-11-23) → up, 4 seats
- [ ] Vox ≤ 16% average in polls published 2026-11-13 to 2026-11-23 → down, 4 seats
- [ ] Proclaimed candidacies (BOE, by ≈ 2026-10-31) show UPN running separately from PP in Navarre → either, 0 (re-check seat attribution)
- [ ] Election-night provisional count 2026-11-29 → mechanical re-forecast

### Sources
1. BOE Real Decreto 806/2026 coverage — Diario de León, "El BOE publica el RD de disolución..." — https://www.diariodeleon.es/nacional/261006/2099432/boe-publica-rd-disolucion-cortes-convocatoria-electoral-29-noviembre.html (accessed 2026-10-17)
2. Libertad Digital, "Sánchez convoca elecciones el 29 de noviembre" (2026-10-05) — https://www.libertaddigital.com/espana/politica/2026-10-05/sanchez-adelanta-las-elecciones-generales-7470157/ (accessed 2026-10-17)
3. Diario de Avisos, "Pedro Sánchez convoca elecciones generales para el 29 de noviembre" — https://diariodeavisos.elespanol.com/2026/10/pedro-sanchez-convoca-elecciones-generales/ (accessed 2026-10-17)
4. INE, Elecciones Generales de 29 de noviembre 2026 — https://www.ine.es/dyngs/CEL/en/index.htm?cid=1699 (accessed 2026-10-17)
5. Wikipedia, Opinion polling for the next Spanish general election — https://en.wikipedia.org/wiki/Opinion_polling_for_the_next_Spanish_general_election (accessed 2026-10-17)
6. Demócrata, Sigma Dos poll (PP 135, Vox 68) — https://www.democrata.es/encuestas/elecciones-generales/encuesta-elecciones-generales-sigma-dos-vox-68-escanos-pp-psoe/ (accessed 2026-10-17)
7. Demócrata, SocioMétrica poll (bloc 207) — https://www.democrata.es/encuestas/elecciones-generales/encuesta-elecciones-generales-vox-gana-5-escanos-psoe-recupera-4-pp-vox-alcanzan-207-segun-sociometrica/ (accessed 2026-10-17)
8. Demócrata, GAD3 poll (bloc 198) — https://www.democrata.es/en/center-of-surveys-and-electoral-polls/general-elections/general-elections-survey-pp-and-vox-lose-four-seats-but-maintain-198-compared-to-the-107-of-psoe-according-to-gad3/ (accessed 2026-10-17)
9. Demócrata, Hamalgama poll (bloc 212) — https://www.democrata.es/en/center-of-surveys-and-electoral-polls/general-elections/general-elections-survey-vox-surpasses-double-the-seats-of-23j-and-maintains-a-majority-of-212-with-the-pp-according-to-hamalgama/ (accessed 2026-10-17)
10. ARA, "What do the polls for the Spanish elections of November 29 say?" (2026-10-09) — https://en.ara.cat/politics/what-do-the-polls-for-the-spanish-elections-of-november-29-say_1_5874100.html (accessed 2026-10-17)
11. Jerusalem Post / Media Line (RTVE average 202) — https://www.jpost.com/international/article-911056 (accessed 2026-10-17)
12. BioBioChile, CIS October barometer (2026-10-15) — https://www.biobiochile.cl/noticias/internacional/europa/2026/10/15/primera-encuesta-para-elecciones-en-espana-da-ventaja-al-psoe-de-sanchez-sobre-partidos-de-derecha.shtml (accessed 2026-10-17)
13. El Independiente, "Así fallaron las encuestas del 23-J" (2023-07-25) — https://www.elindependiente.com/espana/2023/07/25/asi-fallaron-las-encuestas-del-23-j/amp/ (accessed 2026-10-17)
14. Menorca.info, "La mayoría de las encuestas han fallado" (2023-07-26) — https://www.menorca.info/balears/noticias/2023/07/26/1983287/resultado-elecciones-generales-mitad-encuestas-son-malas-fake.html (accessed 2026-10-17)
15. Orain, "Día clave para el futuro de una posible coalición UPN-PP" (2026-10-13) — https://orain.eus/es/politica/2026/10/13/dia-clave-el-futuro-una-posible-coalicion-upn-pp-las-elecciones-generales/ (accessed 2026-10-17)
16. Demócrata, "PP y UPN alcanzan un principio de acuerdo" — https://www.democrata.es/elecciones-generales-espana/pp-upn-acuerdo-coalicion-elecciones-29n/ (accessed 2026-10-17)
17. Polymarket gamma API, Spain general election markets — https://gamma-api.polymarket.com/public-search?q=spain%20election (accessed 2026-10-17; cached `raw/polymarket-2026-10-17.json`)
18. Metaculus API post 46036 (metadata only) — https://www.metaculus.com/questions/46036/ (accessed 2026-10-17; cached `raw/metaculus-2026-10-17.json`)

**Question**: [How many seats will PP and Vox collectively receive in the 2026 Spanish general election?](https://www.metaculus.com/questions/46036/)
**Date**: 2026-10-17
**Forecast**: Median 197 seats, IQR [189, 205]
**Thesis**: Seventeen private polls since late September put PP+Vox at ~202 seats (RTVE average 202) on ~51% of the vote; I shade 5 seats for the 2023-style left mobilisation after a Sánchez snap call and the recent right-overstatement in Spanish polling, with SD ≈ 12 from historical poll error. P(majority ≥176) ≈ 95%.
