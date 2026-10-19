# What will Argentina's country risk (riesgo país, JP Morgan EMBI+) be at the close on October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46139/ |
| **Tournament** | minibench — one shot, window 2026-10-19T11:46:16Z -> 2026-10-19T14:46:16Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 640, IQR [608, 674] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the closing value, in basis points, of Argentina's riesgo país (JP Morgan's EMBI+ Argentina spread) for the trading day of Thursday 29 October 2026, as shown on Infobae's live indicator page. If Infobae does not show it, Ámbito or Perfil are used instead. If 29 October is not a bond-trading day, the next trading day's close applies. The range is 450–850 bp, and both bounds are open, so values outside the range still count. Sources can differ by a few bp depending on when they take the "close" (the question text says 641 bp on 15 October, while Rava's close for that day was 622). I treat that difference as noise and include it in the width of the distribution.

### Outside view

The reference class is how much the index moves over about 9 trading days, starting from the latest close. Using Rava's daily closes for 1–16 October 2026 [2], daily moves were usually 0–4%, with one day of −8.5% (5 October). That suggests daily volatility of roughly 2.5–3%. Over 9 trading days, that is about ±8–9% for one standard deviation, or about ±50–55 bp around 640. Recent history also shows fat tails: the index fell from 655 to 573 in three sessions (2–6 October) and rose from 589 to 648 in four (12–16 October). The 2026 range so far is about 473 to 655 bp [1][2].

### Inside view

- **Starting point:** Rava's 16 October close was 648 bp, up 4.2% on the day. That was the fourth straight day of increases from 589 and is close to the 2026 high of about 655 [2]. I found no close for 19 October.
- **Drift:** Momentum points up. El Economista quotes analysts calling ~600 "the floor, not the ceiling", citing the climate ahead of the 2027 election [3]. On the other side, the index has fallen back each time it neared 650–655 this year, and early October showed it can drop 10% in days on good news. I set a median of 640, slightly below the last close, as a compromise between momentum and mean reversion. The difference is small compared with the spread.
- **Event risk:** Brazil's presidential runoff is on 25 October, inside the window. The first-round result alone moved the index about −8% in one day [2][4], so the runoff could move it sharply either way. Budget and fiscal negotiations and the debate over the peso's exchange-rate band add risk on both sides. I made the tails wide on both sides, a little wider to the upside, because spreads tend to jump up faster than they come down.
- **Distribution (bp):** p5 560, p10 578, p25 608, p50 640, p75 674, p90 712, p95 740.

### Evidence

- Rava closes (accessed 2026-10-19): 1 Oct 636, 2 Oct 655, 5 Oct 599, 6 Oct 573, 7 Oct 586, 8 Oct 588, 9 Oct 589, 12 Oct 589, 13 Oct 597, 14 Oct 611, 15 Oct 622, 16 Oct 648 [2].
- Perfil, 14 Oct: the index rose to 611 bp, breaking through the 600 level [4].
- Question background: 2026 low of about 473 in mid-August, about 498 on 12 May, and a high of about 650–655 in early October [1].
- Infobae's indicator page loads its number dynamically, and I could not read a value from it [5].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-19 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no market on this spread level found |

### What would change my mind

- The result of the Brazilian runoff on 25 October, and how the market reads it for Argentina.
- A sharp move on 19–20 October, for example a break above 700 or a fall back below 600. That would shift the centre more than any fundamental argument here.

### Sources

1. Metaculus question 46139, background text — https://www.metaculus.com/questions/46139/ (accessed 2026-10-19)
2. Rava, historical riesgo país, 16 Oct 2026 — https://www.rava.com/cotizaciones/historico/riesgo-pais/2026/10/16/ (accessed 2026-10-19)
3. El Economista, "Riesgo país: 600 puntos, piso y no techo" — https://eleconomista.com.ar/economia/riesgo-pais-600-puntos-piso-no-techo-mercado-alerta-milei-elecciones-2027-n98836 (accessed 2026-10-19)
4. Perfil, "El riesgo país sube a 611 puntos básicos y quiebra el piso de los 600" — https://www.perfil.com/noticias/economia/el-riesgo-pais-sube-a-611-puntos-basicos-y-quiebra-el-piso-de-los-600-en-la-plaza-bursatil-a35.phtml (accessed 2026-10-19)
5. Infobae, riesgo país indicator — https://www.infobae.com/economia/indicador/riesgo-pais/ (accessed 2026-10-19)
6. Rava, historical riesgo país, 6 Oct 2026 — https://www.rava.com/cotizaciones/historico/riesgo-pais/2026/10/06/ (accessed 2026-10-19)

**Question**: [What will Argentina's country risk (riesgo país, JP Morgan EMBI+) be at the close on October 29, 2026?](https://www.metaculus.com/questions/46139/)
**Date**: 2026-10-19
**Forecast**: Median 640 bp, IQR [608 bp, 674 bp]
**Thesis**: The last close was 648 bp (Rava, 16 Oct), after four days of increases to near the 2026 high of about 655. Historical volatility of about ±50 bp over 9 trading days sets the width. I center slightly below the last close because the index has fallen back from this level before. The Brazilian runoff on 25 October is the main event risk, so both tails are wide.
