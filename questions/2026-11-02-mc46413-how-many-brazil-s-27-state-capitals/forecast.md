# How many of Brazil's 27 state capitals will the InfoGripe bulletin of 12 November 2026 list at alert, risk or high-risk level with a rising long-term SRAG trend?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46413/ |
| **Tournament** | minibench — one shot, window 2026-11-02T23:47:30Z -> 2026-11-03T02:47:30Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-03 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | Median 4, IQR [2, 5] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The value is the number of capitals named in the capitals statement ("X das 27 capitais apresentam nível de atividade de SRAG em alerta, risco ou alto risco … com sinal de crescimento … na tendência de longo prazo") of the InfoGripe "Resumo" released Thursday 12 Nov 2026. Capitals at alert level without growth (e.g. Brasília, Florianópolis at SE 42) are excluded. Arithmetic: the latest edition is SE 42 (18–24 Oct 2026, data to 24/10, released 29 Oct; read from the PDF itself) with count 5. SE 43 (25–31 Oct) is due 5 Nov (the PDF returns 404 today). The target edition is SE 44 (1–7 Nov), released 12 Nov: **two weekly editions ahead** of the latest known. Seven capitals were at alert level or above at SE 42 (5 growing + 2 not growing), so the count is mostly bounded by that pool plus any new entrants. Scale: 0–10 with open upper bound.

### Outside view

Reference class: weekly counts from the same bulletin. 2026 SE 38–42: 3, 5, 0, 5, 5 (mean 3.6; sd ≈ 2.3). Other 2026 editions: SE 31 = 2, SE 32 = 4, (seasonal peaks SE 16 = 13, SE 26 = 9). Same weeks last year, read from the PDFs: 2025 SE 42 = 6, SE 44 = 3, SE 45 = 2; Nov–Dec 2025 stayed at about 0–5. Swings of 5 in a week occur (SE 39 → 40 → 41), so persistence over two weeks is weak. Prior: centred ~3.5–4 with a right tail.

### Inside view

Up from the base: national SRAG shows growth on the 3-week signal, and covid (MT, MS, SP, RJ) and metapneumovirus (SP, RJ, BA, PE, SE) are rising from low levels, so a count below 2 is less likely than the 2025 late-Nov experience suggests. Down: the mix is rhinovirus-dominated with no influenza or RSV wave signalled, and late-year counts historically fade; Brazil's Nov 2025 analogues were 2–3. No SE 43 data exist yet. I take a median of 4 with a right-skewed tail (8+ needs a new wave, about 5%). The only adjustment from the raw recent mean is −0.5 for the 2025 same-week analogues (see the research log).

Discrete distribution I hold (P of each count): 0: 7%, 1: 9%, 2: 12%, 3: 15%, 4: 16%, 5: 16%, 6: 11%, 7: 7%, 8: 4%, 9: 2%, 10+: 1%.

### Evidence

- SE 42 bulletin, accessed 2026-11-02 [1][2]: 5 capitals with growth (Aracaju, Belém, Cuiabá, João Pessoa, Rio de Janeiro); Brasília and Florianópolis at alert without growth. National long-term oscillation, short-term growth. Rhinovirus 53.3% of positives in the last 4 weeks.
- SE 38–41 counts as given in the question text (3, 5, 0, 5); SE 40 = 0 and the SE 39 list were cross-checked in news [4][5].
- 2025 analogues read from the PDFs [3]: SE 42 = 6, SE 44 = 3 (Florianópolis, João Pessoa, Palmas), SE 45 = 2 (Porto Alegre, São Paulo).
- Scout digest: Nov–Dec 2025 range 0–5; 8+ only at seasonal peaks (2026 SE 16 = 13, SE 26 = 9; 2025 SE 40 = 10).
- SE 43 PDF: 404 on 2026-11-02, not yet released.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-02 | niche topic; Brazil blocks the platforms |

### What would change my mind

- The SE 43 bulletin (5 Nov) is not visible to me; a count of 7+ there, or a covid/metapneumovirus surge in SP/RJ, would move the median up to 5–6, while 0–1 would pull it to 2–3.
- A sudden revision of nowcast data or a change in how the bulletin words the capitals sentence could shift the count unpredictably.

### Sources

1. https://agencia.fiocruz.br/sites/agencia.fiocruz.br/files/Resumo_InfoGripe_2026_42.pdf (accessed 2026-11-02)
2. https://fiocruz.br/noticia/2026/10/infogripe-cinco-estados-tem-srag-em-nivel-de-alerta-ou-risco-com-sinal-de (accessed 2026-11-02)
3. https://agencia.fiocruz.br/sites/agencia.fiocruz.br/files/Resumo_InfoGripe_2025_44.pdf (also _42, _45) (accessed 2026-11-02)
4. https://portal.afya.com.br/infectologia/srag-no-brasil-mantem-estabilidade-mas-sergipe-segue-em-alerta (accessed 2026-11-02)
5. https://brasil61.com/n/fiocruz-alerta-para-crescimento-de-casos-graves-de-sindrome-respiratoria-em-tres-estados-bras2617280 (accessed 2026-11-02)
6. https://conexaoitajuba.com.br/infogripe-alerta-aumento-de-srag-entre-criancas-em-ms-pa-e-rj (accessed 2026-11-02)

**Question**: [How many of Brazil's 27 state capitals will the InfoGripe bulletin of 12 November 2026 list at alert, risk or high-risk level with a rising long-term SRAG trend?](https://www.metaculus.com/questions/46413/)
**Date**: 2026-11-02
**Forecast**: Median 4 capitals, IQR [2, 5]
**Thesis**: Weekly counts have swung between 0 and 5 (SE 38–42: 3, 5, 0, 5, 5) and the same weeks in 2025 gave 2–6, so I centre on 4 with a right tail. The target is two editions beyond the latest known (SE 42 = 5), and the count is most sensitive to whether covid or metapneumovirus growth in the Southeast capitals continues.
