# What will be Grupo Casas Bahia's (BHIA3) closing share price on 27 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46564/ |
| **Tournament** | minibench — one shot, window 2026-11-16T01:16:26Z -> 2026-11-16T04:16:26Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | open |
| **Current forecast** | Median 0.675, IQR [0.625, 0.73] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The value is the "Close" for BHIA3.SA on the 27 November 2026 session (Black Friday, a normal B3 trading day), from Yahoo Finance's history page, in R$. If there is no print that day, the most recent prior close counts. If a reverse split takes effect by then, the post-split price counts. The question's range is R$0.40–1.20 in R$0.01 steps, with both bounds open. **Arithmetic:** the last close on Yahoo is **R$0.68 on 13 Nov 2026** [1]. The background text says 0.69, but Yahoo's table shows 0.68, and I use the table. The window from 16 Nov to 27 Nov holds **9 trading sessions**: 16–19 Nov, then 23–27 Nov, because 20 Nov is a holiday. The lower bound at 0.40 is −41% from the last close and the upper bound at 1.20 is +76%.

### Outside view

This is the price of an equity in judicial recovery (recuperação judicial) 9 sessions ahead. The anchor is a random walk from R$0.68 with a small downward drift. Volatility comes in two regimes:
- **Calm:** the 9 sessions from 3 to 13 Nov had a daily standard deviation of about 2.5%, with the price between 0.67 and 0.72 [1].
- **Turbulent:** the 25 sessions from mid-October had a daily standard deviation of 12–15% [1]. Over that stretch the price went from 1.60 on 9 Oct to 0.64 on 29 Oct. In August it rose about 60% in one day on a court ruling [3].

Distressed equities that sit last in line behind about R$15bn of unsecured debt tend to drift down; Americanas (AMER3) is the analogue [4].

### Inside view

The model (`uv run python -c`, inline) is a mixture: 60% weight on 3.5% daily volatility and 40% on 8.5%, with Student-t (4 degrees of freedom) shocks, scaled to 9 sessions and centred at 0.675. It gives p5/p25/p50/p75/p95 = 0.52 / 0.63 / 0.675 / 0.73 / 0.88. I widened the outer tails a little (p5 to 0.50, p95 to 0.90) because the October history has −24% and −37% single-session moves.
- **Downside:** the Veja report that October revenue fell about 60% year on year [2][5], and the eventual plan, which is likely to be dilutive.
- **Upside:** court or creditor news can move the price 20–60% in a day [3].

There is no scheduled catalyst in the window: Q3 results come on 10 Dec and the plan is due around 20 Dec [2][5].

A reverse split by 27 Nov is very unlikely. None has been proposed. The B3 deadline to get back above R$1 is 1 Mar 2027 [6], and a shareholder meeting needs a call notice weeks in advance. So I put essentially no mass on a split-driven jump above 1.20.

### Evidence

- Yahoo closes [1]:
  - 13 Nov 0.68, 12 Nov 0.68, 11 Nov 0.70, 10 Nov 0.71, 9 Nov 0.72, 3 Nov 0.67.
  - 30 Oct 0.69, 29 Oct 0.64, 28 Oct 0.73, 26 Oct 0.90, 23 Oct 1.44, 9 Oct 1.60.
- 6–7 Nov: Q3 results were postponed to 10 Dec. Veja reported falling revenue (about −60% for October) and about 200 more store closures [2][5].
- 9–11 Nov: the CVM (the securities regulator) sent an ofício. The company replied that no decision on store closures had been taken [2][5].
- No grupamento, capital increase, debt-to-equity conversion or trading suspension has been announced since 1 Nov [2]. The stay period runs to about 15 Feb 2027 [3].
- B3 penny-stock alert: the shares have been below R$1 since 21 Jul, and the deadline to fix this is 1 Mar 2027 [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-16 | no BHIA3 market |
| Listed options | none | 2026-11-16 | none on BHIA3 |

### What would change my mind

- The calm November regime could break. An early plan filing, a creditor deal or a court ruling (for example on the R$1.19bn of withheld funds) could move the price ±30% in a day.
- An unexpected call for a grupamento shareholder meeting that takes effect by 27 Nov would push the price far above the range.

### Sources

1. Yahoo Finance, BHIA3.SA historical data — https://finance.yahoo.com/quote/BHIA3.SA/history/ (accessed 2026-11-16)
2. Investidor10, "Casas Bahia (BHIA3) pede mais prazo e adia balanço" — https://investidor10.com.br/noticias/casas-bahia-bhia3-vai-fechar-lojas-veja-o-que-diz-a-empresa-123824/ (accessed 2026-11-16)
3. BPMoney, "Ações da Casas Bahia disparam 40% após Justiça blindar varejista" — https://bpmoney.com.br/mercado/acoes-da-casas-bahia-bhia3-disparam-40-apos-justica-blindar-varejista-na-recuperacao-judicial/ (accessed 2026-11-16)
4. Suno, Americanas RJ share history — https://www.suno.com.br/noticias/?p=349841 (accessed 2026-11-16)
5. BPMoney, "Casas Bahia nega decisão de fechamento de lojas à CVM" — https://bpmoney.com.br/negocios/empresas/casas-bahia-bhia3-nega-decisao-fechamento-lojas-cvm/ (accessed 2026-11-16)
6. Suno, "Casas Bahia tem até março de 2027 para sair da faixa de penny stock" — https://www.suno.com.br/noticias/?p=664606 (accessed 2026-11-16)
7. Brapi, "Casas Bahia adia balanço do 3T26 para 10 de dezembro" — https://brapi.dev/news/casas-bahia-adia-balanco-do-3t26-para-10-de-dezembro-em-meio-502ec7bc (accessed 2026-11-16)

**Question**: [What will be Grupo Casas Bahia's (BHIA3) closing share price on 27 November 2026?](https://www.metaculus.com/questions/46564/)
**Date**: 2026-11-16
**Forecast**: Median R$0.675, IQR [R$0.625, R$0.73]
**Thesis**: A fat-tailed random walk over 9 sessions from the R$0.68 Yahoo close of 13 Nov. The calm November trading (about 2.5% daily) is blended with October's crash regime, with a slight downward drift for an equity in judicial recovery. No catalyst is scheduled before 27 Nov (Q3 results on 10 Dec, plan due around 20 Dec), and no reverse split is pending. The forecast is most sensitive to an unscheduled court or creditor shock.
