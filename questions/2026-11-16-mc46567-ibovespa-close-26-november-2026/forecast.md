# What will the Ibovespa close at on 26 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46567/ |
| **Tournament** | minibench — one shot, window 2026-11-16T02:29:17Z -> 2026-11-16T05:29:17Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-26 |
| **Status** | resolved |
| **Current forecast** | Median 172600, IQR [168000, 177100] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The question resolves to the "Close" value (not "Adj Close") in the Yahoo Finance ^BVSP history row for Thursday 26 Nov 2026, in index points. The range runs from 150,000 to 195,000 and both bounds are open. The latest close is **172,458 on Fri 13 Nov** (Yahoo, fetched 2026-11-16 [1]; Estadão/InfoMoney give 172,457.76 [2]). The question background says 172,013.72, which is wrong: +0.66% on 12 Nov's 171,324 gives 172,455. The sessions left are 16, 17, 18, 19, 23, 24, 25 and 26 Nov. That is **8 sessions**, because B3 is closed on Fri 20 Nov [6]. The range spans 172,458 −13% / +13%.

### Outside view

Over 8 sessions the index behaves roughly as a random walk with no drift. In normal times the Ibovespa's annualised volatility is ~20–22%, about 1.3% a day, or ~3.7% over 8 sessions. This regime is not normal. On 26 Oct the index fell 13.88% and triggered a circuit breaker. BOVA11 options were pricing 44–46% implied volatility through the runoff [3][4]. In November, daily moves have run 0.4–2.2%. I use ~1.5% a day, or **σ ≈ 4.3% (~7,400 points) over 8 sessions**, with fatter tails than a normal distribution.

### Inside view

- **Fiscal votes this week:** four Senate amendments to PLP 299/2026 on 17 Nov, then a Chamber vote expected ~18 Nov [2][5]. The market already treats the package as short-term relief and insufficient on debt [7]. Passage is mostly priced in. Watering it down or rejecting it is the bigger tail, so I add a mild left skew.
- **Rebound vs. outflow:** historically, Brazilian post-election selloffs have often partly reversed [8]. Against that, foreigners pulled R$8.4bn after the runoff and XP downgraded Brazil to neutral [9]. The index rose 2.35% last week, and the dollar is at its 2026 high (R$5.66) [2]. I see no net drift and put the median slightly above spot, at 172,600.
- **External factors:** Nvidia earnings and the Fed minutes this week. US markets are closed for Thanksgiving on 26 Nov, so that session will be thin [10].
- No scouts were used: the clock was tight, and the answer rests on one price series plus volatility.

Quartiles ≈ ±2.7% and 5–95% ≈ −7.5%/+7.3%, which is wider than a normal with σ 4.3% would give.

### Evidence

- Yahoo ^BVSP: 13 Nov close 172,458; 9–13 Nov closes 172,236 / 171,337 / 172,060 / 171,324 / 172,458; 3 Nov low 164,447 [1].
- Senate approved the base text 45–31 on 12 Nov; amendments on 17 Nov; R$50–60bn impact in 2027 [2][5].
- Foreign outflow of R$8.4bn after the election (5 Nov report) [9].
- No Ibovespa market on Polymarket or Kalshi.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi | none found | 2026-11-16 | |
| Ibovespa future | ~172.5k | undated snippet | roughly at spot |
| Banks (JPM, MS, BTG) | expect a "correction period" | late Oct 2026 | qualitative [11] |

### What would change my mind

- A Chamber rejection or heavy dilution of PLP 299 around 18 Nov: a 3–6% downside move is plausible.
- A large shift in US rates or Nvidia-driven global risk sentiment.

### Sources

1. Yahoo Finance ^BVSP history, https://finance.yahoo.com/quote/%5EBVSP/history/ (accessed 2026-11-16)
2. B3 Bora Investir, "Ibovespa B3 sobe 0,66% após aprovação de pacote fiscal", https://borainvestir.b3.com.br/noticias/mercado/ibovespa-b3-sobe-066-apos-aprovacao-de-pacote-fiscal-dolar-fica-praticamente-estavel/ (accessed 2026-11-16)
3. InfoMoney, options before the runoff, https://www.infomoney.com.br/mercados/opcoes-bbas3-petr4-bova11-risco-segundo-turno/ (accessed 2026-11-16)
4. Genial, largest daily falls of the Ibovespa, https://analisa.genialinvestimentos.com.br/macro-strategy/analises/maiores-quedas-diarias-ibovespa-historia/ (accessed 2026-11-16)
5. Correio Braziliense, Chamber to vote on the PLP after the Senate, https://www.correiobraziliense.com.br/politica/2026/11/7538158-ajuste-fiscal-guimaraes-diz-que-camara-votara-plp-imediatamente-apos-senado.html (accessed 2026-11-16)
6. B3 2026 trading calendar, https://www.b3.com.br/pt_br/noticias/calendario-de-negociacao-da-b3-confira-o-funcionamento-da-bolsa-em-2026.htm (accessed 2026-11-16)
7. InfoMoney, "Do alívio à cautela", https://infomoney.com.br/mercados/do-alivio-a-cautela-por-que-o-mercado-diminuiu-animo-sobre-o-pacote-de-ajuste-fiscal (accessed 2026-11-16)
8. NeoFeed, post-election hangover can be short, https://neofeed.com.br/negocios/bolsa-despenca-com-vitoria-de-lula-mas-passado-mostra-que-ressaca-eleitoral-pode-ser-curta/ (accessed 2026-11-16)
9. Gazeta do Povo, foreigners withdraw R$8.4bn, https://www.gazetadopovo.com.br/economia/ibovespa-estrangeiros-retiram-bolsa-lula/ (accessed 2026-11-16)
10. Business Standard live blog, 16 Nov 2026, https://business-standard.com/amp/markets/news/stock-market-live-nse-bse-sensex-today-nifty50-gift-nifty-crude-oil-prices-november-16-126111600051_1.html (accessed 2026-11-16)
11. InfoMoney, 26 Oct 2026 circuit breaker, https://www.infomoney.com.br/mercados/ibovespa-hoje-bolsa-de-valores-ao-vivo-26102026/ (accessed 2026-11-16)

**Question**: [What will the Ibovespa close at on 26 November 2026?](https://www.metaculus.com/questions/46567/)
**Date**: 2026-11-16
**Forecast**: Median 172,600, IQR [168,000, 177,100]
**Thesis**: An 8-session random walk from the 13 Nov close of 172,458 (Yahoo), widened for post-runoff volatility (σ ≈ 4.3%, fat tails). The fiscal-package votes in the Senate (17 Nov) and Chamber (~18 Nov) are the main event risk, with a mild left skew. The forecast is most sensitive to how the Chamber treats PLP 299.

## Resolution — 2026-11-28

Resolved **176800.0** (synced from the Metaculus API). The bot's forecast was 172600 [168000, 177100]. Official spot peer score: +3.49.
