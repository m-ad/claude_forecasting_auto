# Will the AAA national average price of regular gasoline be below $4.05 per gallon on November 13, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46395/ |
| **Tournament** | minibench — one shot, window 2026-11-02T09:44:45Z -> 2026-11-02T12:44:45Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | closed |
| **Current forecast** | Median 66.0%, IQR [55.0%, 76.0%] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

Resolves YES if AAA's national average for **regular** gasoline (gasprices.aaa.com, "Current Avg." with price-as-of 11/13/26, or the same figure shown as "Yesterday Avg." the next day) is strictly below $4.05. Latest value from the source itself: **$4.1694 as of 11/2/26** ($4.1732 on 11/1; $4.2046 on 10/30; $4.2858 a week earlier; $4.3961 a month earlier). Arithmetic: the target date is 11 days after 11/2; the price must fall by at least 11.95 cents, i.e. about 1.1 c/day. The last 7 days averaged about 1.65 c/day, the last 3 days (Oct 30–Nov 2) 1.2 c/day, but the final day (11/1→11/2) only 0.4 c. There is no fallback to evaluate beyond the "first later date if 11/13 is unpublished" rule (11/13 is a Friday, normally published).

### Outside view

Reference class: the AAA daily average continuing a steady decline over the next ~11 days after a four-week slide of 4.40 → 4.17 (about 23 c, ~5–6 c/week, faster in the last week). Gasoline prices are strongly autocorrelated; a continuation at the October weekly pace (5–6 c/week) would give about 4.09–4.10 on 11/13 (NO), while the last 7-day pace (11.6 c/week) would give about 4.01 (YES). So the pure-trend prior is near a coin flip, a little below. No quantified US sample of 14-day November changes was found (stated plainly; n/a).

### Inside view

Wholesale fell sharply on 11/2: RBOB about $2.99/gal (−5.2% on the day, 9-week low, −7–8% over four weeks; Trading Economics CFD reference, not an official settle), Brent about $108.9 (−4%), WTI about $99.8. The pump-to-RBOB spread is about $1.18, above the roughly $1.00 that I'd consider normal in winter-blend season (this normal range is my assumption, not verified). If RBOB holds near $3.00, equilibrium retail is roughly $3.95–4.05, so retail should keep sliding with the usual lag (declines pass through over ~2–3 weeks, slower than rises). That supports YES and I move about +10 pp from the pure-trend prior. Against: the one-day slowdown (−0.4 c), AAA's own statement that crude above $100 limits declines, oil's large headline-driven swings (Brent was above $113 on Oct 30, up 15% in October), and reports that both sides may prepare for escalation after the Nov 3 midterms. A RBOB rebound of 15–20 c would stall the decline. Asymmetry ("rockets and feathers") means a rebound passes through faster than a fall. Net: about 66%.

### Evidence

- AAA, 11/2/26: Current $4.1694, Yesterday $4.1732, Week Ago $4.2858, Month Ago $4.3961 [1].
- AAA weekly releases: $4.36 (Oct 8), $4.33 (Oct 15), $4.27 (Oct 22, winter blend), $4.22 (Oct 29, "crude oil above $100 limiting further declines") [2].
- Trading Economics, 11/2/26: RBOB 2.9932, −5.17% day; gasoline inventories built unexpectedly, demand weaker, stocks still ~2% below 5-yr average; Brent 108.9 (−4%), Doha/US–Iran diplomacy hopes [3][4].
- Pass-through: FTC working paper finds retail rises ~3–4x as fast as falls [5].
- No scheduled shock in the window beyond the Nov 3 midterms and EIA STEO on Nov 10; OPEC+ held targets through December [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Kalshi / Polymarket | no Nov 13 threshold market found | 2026-11-02 | |
| Manifold | 43–52% for AAA ≤ $4.00 on any day in Nov 2026 | 2026-11-02 | play-money, discounted; the ≤$4.05 on 11/13 condition is somewhat different, roughly consistent with ~55–65% |

### What would change my mind

- A sharp RBOB/Brent rebound (RBOB back above ~$3.20, Brent above $115) after a breakdown of the Qatar-mediated talks: would push toward ~30%.
- AAA daily prints stalling around $4.15 through Nov 6 (decline under 0.5 c/day): would push below 50%. Conversely, RBOB staying under $3.00 with AAA below $4.12 by Nov 6 would push above 80%.

### Sources

1. https://gasprices.aaa.com/ (accessed 2026-11-02)
2. https://gasprices.aaa.com/news/ (accessed 2026-11-02)
3. https://tradingeconomics.com/commodity/gasoline (accessed 2026-11-02)
4. https://tradingeconomics.com/commodity/brent-crude-oil (accessed 2026-11-02)
5. https://www.ftc.gov/sites/default/files/documents/reports/asymmetric-pass-through-u.s.gasoline-prices/wp302_0.pdf (accessed 2026-11-02, search snippet only)
6. https://nairametrics.com/2026/10/05/opec-keeps-november-oil-production-unchanged-at-31-01-million-bpd/ (accessed 2026-11-02, snippet only)
7. https://manifold.markets/event/in-which-months-will-there-be-a-day (accessed 2026-11-02)

**Question**: [Will the AAA national average price of regular gasoline be below $4.05 per gallon on November 13, 2026?](https://www.metaculus.com/questions/46395/)
**Date**: 2026-11-02
**Forecast**: Median 66.0%, IQR [55.0%, 76.0%]
**Thesis**: AAA regular is $4.1694 and needs another ~12 c drop in 11 days; the October trend alone is a coin flip, but wholesale gasoline fell to a 9-week low (~$2.99) on 11/2, leaving the pump price above its likely equilibrium. Most sensitive to whether the Iran-diplomacy-driven crude drop reverses after the Nov 3 midterms.
