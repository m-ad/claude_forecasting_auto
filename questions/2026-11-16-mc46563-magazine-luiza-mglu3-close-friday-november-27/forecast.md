# What will Magazine Luiza (MGLU3) close at on Friday, November 27, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46563/ |
| **Tournament** | minibench — one shot, window 2026-11-16T01:02:45Z -> 2026-11-16T04:02:45Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | open |
| **Current forecast** | Median 7.7, IQR [6.85, 8.65] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The value is the "Close" column (not Adj Close) for the 27 Nov 2026 row on Yahoo Finance's MGLU3.SA history page. If Yahoo is missing it, cotab3.com.br is used instead, and the question is annulled if B3 does not trade that day. The price is in R$. The range is 4–13 and both bounds are open. The last known close is **R$7.81 on Fri 13 Nov** (Yahoo, fetched 2026-11-16 [1]). The question text says 7.07, but that was the 12 Nov close. B3 is closed on Fri 20 Nov (Consciência Negra, Black Consciousness Day) [3]. That leaves **9 sessions** between 7.81 and the target: 16, 17, 18, 19, 23, 24, 25, 26 and 27 Nov. The 2 Dec shareholders' meeting (AGE) and the 9 Dec Copom (central bank rate committee) meeting both come after the window. Remote voting ballots for the AGE are due 28 Nov [4].

### Outside view

Reference class: a 9-session random walk from the last close. Before the election MGLU3's implied volatility was about 60% a year, roughly 3.8% a day [8]. Since 26 Oct the realised volatility has been far higher: daily moves of −58%, +12%, +17%, −8% and +10% (13 Nov), so at least 8–10% a day. I assume about 6% a day as the regime cools. Over 9 sessions that gives a log-sd of about 0.18, or roughly ±18% for one sigma. I fatten the tails for gaps.

### Inside view

The drift should be close to zero. Bullish factors: a wave of upgrades (BofA R$11, Goldman R$11.50, XP R$11), market-share gains from Casas Bahia's judicial recovery, the Black Friday narrative (Neotrust expects +20.7% y/y in e-commerce) and short interest of 16% that can fuel a squeeze [2,4,5,6]. Bearish factors: profit-taking after a +39% week, the AGE authorising up to about 200% new shares (JPMorgan warns of up to 67% dilution) and a fragile macro backdrop after the election, with the Ibovespa about 16% below its pre-runoff level and the Selic at 13.75% [4,7,9]. My one adjustment: the median sits slightly below the last close, at 7.70 (−1.5%), for dilution overhang and post-spike give-back. Distribution: p5 5.45, p10 5.90, p25 6.85, p50 7.70, p75 8.65, p90 9.85, p95 10.70.

### Evidence

- 9–13 Nov: closes 5.84 → 6.52 → 7.66 → 7.07 → 7.81. Volume was 47–81M a day [1].
- 23–26 Oct: 12.69 → 5.30 after Lula's re-election. The Ibovespa fell 14% and B3 triggered a circuit breaker [2].
- AGE on 2 Dec: an authorised-capital limit of up to 1,551,890,020 shares and removal of the poison pill. JPMorgan considers full use of the limit unlikely in the short term [4].
- No prediction markets cover MGLU3. I found no current option-implied volatility.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi | none found | 2026-11-16 | |
| Sell-side 12-month targets | BofA 11, GS 11.5, XP 11, BBI 7; JPM underweight | 2026-11-12 | 12-month horizon, not a 2-week forecast |

### What would change my mind

The forecast is most sensitive to the volatility assumption. If the stock stays in its 8–10% a day regime, the tails should be wider still. A material fact before the AGE, such as an actual priced share offering, would shift the median down sharply. A fact that withdraws or caps the authorisation would shift it up.

### Sources

1. Yahoo Finance, MGLU3.SA history — https://finance.yahoo.com/quote/MGLU3.SA/history/ (accessed 2026-11-16)
2. Guia do Investidor, "MGLU3 desaba 48% após vitória de Lula" — https://guiadoinvestidor.com.br/mercado/magazine-luiza-mglu3-desaba-48-apos-vitoria-de-lula-e-juros-futuros-superam-16/ (accessed 2026-11-16)
3. B3, trading calendar 2026 — https://www.b3.com.br/pt_br/noticias/calendario-de-negociacao-da-b3-confira-o-funcionamento-da-bolsa-em-2026.htm (accessed 2026-11-16)
4. Guia do Investidor, Goldman vs JPMorgan on dilution — https://guiadoinvestidor.com.br/mercado/magazine-luiza-mglu3-vira-aposta-do-goldman-sachs-mas-jpmorgan-faz-alerta-sobre-diluicao-de-ate-67/ (accessed 2026-11-16)
5. InfoMoney, Black Friday 2026 outlook — https://www.infomoney.com.br/minhas-financas/sem-bets-com-compras-antecipadas-e-tiktok-shop-o-que-esperar-da-black-friday-2026/ (accessed 2026-11-16)
6. Visno, weekly gainers (MGLU3 +39.2%) — https://visnoinvest.com.br/news/16550/mglu3-392-e-beef3-307-lideram-altas-balancos-e-recompras-no-periodo (accessed 2026-11-16)
7. Economic News Brasil, Ibovespa after the election — https://economicnewsbrasil.com.br/2026/11/09/ibovespa-queda-segundo-turno-2026/ (accessed 2026-11-16)
8. TopGrafx, MGLU3 options/IV — https://topgrafx.substack.com/p/mglu3-mercado-vende-puts-exatamente (accessed 2026-11-16)
9. Gazeta Mercantil, Copom holds at 13.75% — https://gazetamercantil.com/copom-mantem-selic-1375-novembro-2026 (accessed 2026-11-16)

**Question**: [What will Magazine Luiza (MGLU3) close at on Friday, November 27, 2026?](https://www.metaculus.com/questions/46563/)
**Date**: 2026-11-16
**Forecast**: Median R$7.70, IQR [R$6.85, R$8.65]
**Thesis**: The forecast is a 9-session random walk from the 13 Nov close of R$7.81 (Yahoo), with about 6% daily volatility and fat tails. The median is shaded slightly down for the 2 Dec dilution vote and give-back after a +39% week. It is most sensitive to whether the extreme post-election volatility persists.
