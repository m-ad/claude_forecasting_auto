# What first round vote share will José Maria Neves win in the 2026 Cape Verdean presidential election?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/45418/ |
| **Type** | numeric (% of valid votes; Metaculus range 30–60, both bounds open) |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-11-13 / 2026-11-26 |
| **Status** | open |
| **Current forecast** | **Median 56.5%, IQR [52.5%, 60.5%]** (v1, 2026-10-17) |
| **Community (as of 2026-10-17)** | no CP yet (opens 2026-10-19, reveal 2026-10-25) · Pro — · Gold — · n=5 pre-open |
| **Next review** | 2026-10-24 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-17

### What resolves YES
Numeric question: incumbent President José Maria Neves's share of the vote in the **first round on
Sunday 15 November 2026** (runoff, if needed, 29 November). **Caveat — inferred digest:** the
Metaculus resolution text could not be retrieved (pre-open post; bot-key API returns `null`
criteria, browser fetches Cloudflare-challenged — see `research.md`). Presumed: percentage of
**valid votes** as published by the Comissão Nacional de Eleições (CNE) / Constitutional Court
(blank votes are not valid votes for the 50% threshold, per CNE). Six admitted candidates (CNE Edital
n.º 01/2026, 2026-09-30): Neves (PAICV-backed), Joana Rosa (MpD-backed, ex-Justice Minister), Antero
Tavares, Casimiro de Pina, Gilson Alves, Loisito Tavares de Sousa. Edge cases: share-of-valid vs.
share-of-cast (≈1–3 pp difference — 2021 blanks were 2.2%, invalid 0.8%); provisional vs. final
counts (2021: 51.5% provisional → 51.79% final); diaspora votes included. The range tops out at 60%
(open upper bound), so the question writer expected a close race.

### Outside view
- **Incumbent presidents seeking re-election in Cape Verde: 3/3 won in the first round** — Mascarenhas
  Monteiro 1996 (unopposed, ~80%), Pires 2006 (≈51% vs. Veiga), Fonseca 2016 (74.1%, no PAICV
  candidate). Shares 51–80%; the contested case is 51%.
- **Contested two-bloc first rounds** (2001, 2006, 2011, 2021): winner 38–52%; Neves 2021 **51.79%**
  vs. Veiga 42.39%, minors 5.8% combined (5 candidates).
- Generic: incumbent presidents in stable democracies outperform their party's legislative share.

Base-rate prior for Neves: ≈ 54%, SD ≈ 7.

### Inside view
Share = (1 − minors) × Neves's two-way share vs. Rosa.
- **Minors** (four candidates; Pina 1.8% and Alves 0.8% in 2021; Tavares and Sousa untested): 4–7%,
  centre 5%.
- **Two-way share:** start from the May 2026 legislative result (PAICV ≈ 48%, MpD 44.75% ⇒ ≈ 52/48).
  + incumbency and personal vote (Afrobarometer 2022: 72% approve of the President, ~65% trust;
  2024 round shows a general fall in institutional trust) → +5; + MpD fresh off losing government after
  ten years, with a less-known candidate (Rosa vs. Veiga, an ex-PM, in 2021) → +3; − a possible
  "cohabitation/balance" instinct now that PAICV holds both posts (2011, 2021 produced cohabitation)
  → −2. Centre ≈ 59–60%, SD ≈ 5.
- Neves ≈ 0.95 × 59.5 ≈ **56.5%**.

### Evidence
- No published opinion poll for this race (searched Afrosondagem, Inforpress, Expresso das Ilhas,
  A Nação) — a big source of variance.
- Polymarket "winner": Neves 84%, Rosa 10.6% ($28.5K) → consistent with a median in the mid-50s and
  P(Neves < 50%) ≈ 15–20% (some of Rosa's 10.6% is runoff paths).
- PAICV's clean May win (37/72 seats) and the government honeymoon (PM Carvalho since May) favour the
  incumbent (LR ≈ 1.3 for ">55%").
- Disconfirming: 2006, the only contested incumbent re-election, was ≈51%; Cape Verdean presidential
  races have been close whenever both blocs field a real candidate.

### Other forecasters
| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | — | 2026-10-17 | pre-open |
| Metaculus Pro | — | 2026-10-17 | n/a pre-open |
| Metaculus gold medalists | — | 2026-10-17 | n/a pre-open |
| Polymarket "Cape Verde presidential winner" | Neves 84%, Rosa 10.6% | 2026-10-17 | $28.5K total |
| Polymarket "outright first-round winner?" | Yes 64% | 2026-10-17 | $31 volume — ignored |

My P(Neves > 50% in round 1) ≈ 84% — in line with the winner market (which also counts runoff wins,
so the market implies slightly less first-round strength than I do).

### Scenarios
| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | Incumbent landslide: MpD demoralised, low-turnout PAICV machine | 25% | 60–66% |
| 2 | Comfortable first-round win | 45% | 53–60% |
| 3 | Narrow 2006/2021-style race | 20% | 48–53% |
| 4 | Upset/balance vote, runoff | 10% | < 48% |

### Sensitivity
| Assumption | If instead | Forecast becomes |
|---|---|---|
| Two-way share ≈ 59.5% | equals legislative split (52%) | Median 49.5%, IQR [46%, 53%] |
| Minors ≈ 5% | 9% (a minor candidate catches a protest vote) | Median 54.5% |
| SD ≈ 5 on two-way | SD ≈ 8 (no polls, weak priors) | IQR [51%, 62%] |

### What would change my mind (tripwires)
- [ ] Any published poll (by 2026-11-10) with Neves ≥ 55% or ≤ 48% of decided voters → up/down, 3 pp
- [ ] MpD leadership splits / prominent MpD figures endorse Neves or abstain (by 2026-11-08) → up, 2 pp
- [ ] Government scandal or crisis hitting the PAICV government before 2026-11-13 → down, 2 pp
- [ ] CNE provisional result on election night 2026-11-15 → mechanical re-forecast (either, 0)

### Sources
1. CNE, "Presidenciais 2026: Publicado Edital com a lista definitiva dos candidatos" — https://cne.cv/sala_de_imprensa_/presidenciais-2026-publicado-edital-com-a-lista-definitiva-dos-candidatos/ (accessed 2026-10-17)
2. CNE Presidenciais 2026 site — https://presidenciais2026.cne.cv/ (accessed 2026-10-17)
3. Wikipedia, 2026 Cape Verdean presidential election — https://en.wikipedia.org/wiki/2026_Cape_Verdean_presidential_election (accessed 2026-10-17)
4. Wikipedia, 2021 Cape Verdean presidential election — https://en.wikipedia.org/wiki/2021_Cape_Verdean_presidential_election (accessed 2026-10-17)
5. Wikipedia, 2016 Cape Verdean presidential election — https://en.wikipedia.org/wiki/2016_Cape_Verdean_presidential_election (accessed 2026-10-17)
6. Africanews, "Cape Verde opposition wins parliamentary elections" (2026-05-18) — https://www.africanews.com/2026/05/18/cape-verde-opposition-wins-parliamentary-elections/ (accessed 2026-10-17)
7. IPU Parline, Cabo Verde National Assembly May 2026 election — https://data.ipu.org/parliament/CV/CV-LC01/election/CV-LC01-E20260517/ (accessed 2026-10-17)
8. Wikipedia, 2026 Cape Verdean parliamentary election — https://en.wikipedia.org/wiki/2026_Cape_Verdean_parliamentary_election (accessed 2026-10-17)
9. Observador, "Joana Rosa quer ser avaliada pela competência..." (2026-10-01) — https://observador.pt/2026/10/01/joana-rosa-quer-ser-avaliada-pela-competencia-e-nao-so-por-ser-a-primeira-mulher-candidata-a-presidencia-em-cabo-verde/ (accessed 2026-10-17)
10. Observador, "José Maria Neves quer ser reeleito presidente para debater Cabo Verde 2050" (2026-10-02) — https://observador.pt/2026/10/02/jose-maria-neves-quer-ser-reeleito-presidente-para-debater-cabo-verde-2050/ (accessed 2026-10-17)
11. Expresso das Ilhas, "Candidatos perfilam-se para a corrida" (2026-09-20) — https://expressodasilhas.cv/pais/2026/09/20/candidatos-perfilam-se-para-a-corrida/104682 (accessed 2026-10-17)
12. Rio Times, "Cabo Verde Elects a President on 15 November" — https://www.riotimesonline.com/cabo-verde-presidential-election-us-visitors-2026/ (accessed 2026-10-17)
13. Afrobarometer, "Aumentou o grau de confiança dos cabo-verdianos nas instituições chaves" — https://www.afrobarometer.org/articles/aumentou-o-grau-de-confianca-dos-cabo-verdianos-nas-instituicoes-chaves-mostra-o-inquerito/ (accessed 2026-10-17)
14. RTP África on Afrobarometer R10 trust decline — https://rtpafrica.rtp.pt/?p=29794 (accessed 2026-10-17)
15. Africanews, "Cape Verde: Jorge Fonseca leads in provisional presidential results" (2016) — https://www.africanews.com/2016/10/03/cape-verde-jorge-fonseca-leads-in-provisional-presidential-results// (accessed 2026-10-17)
16. Polymarket gamma API, Cape Verde presidential markets — https://gamma-api.polymarket.com/public-search?q=cape%20verde%20presidential (accessed 2026-10-17; cached `raw/polymarket-2026-10-17.json`)
17. Metaculus API post 45418 (metadata only) — https://www.metaculus.com/questions/45418/ (accessed 2026-10-17; cached `raw/metaculus-api-2026-10-17.json`)

**Question**: [What first round vote share will José Maria Neves win in the 2026 Cape Verdean presidential election?](https://www.metaculus.com/questions/45418/)
**Date**: 2026-10-17
**Forecast**: Median 56.5%, IQR [52.5%, 60.5%]
**Thesis**: Every Cape Verdean incumbent president who sought re-election won in round one, and Neves (51.79% in 2021) now runs with his PAICV freshly in government after its May legislative win (37/72 seats) against an MpD candidate weaker than Veiga; four minor candidates take ~5%. No polls exist, so the band is wide; Polymarket's 84% win price agrees with P(>50%) ≈ 84%.
