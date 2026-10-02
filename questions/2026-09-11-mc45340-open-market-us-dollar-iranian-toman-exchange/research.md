# Research log — What will be the open market US dollar/Iranian toman exchange rate on December 31, 2026?

Working notes. Rough is fine; **completeness beats polish**.

## Question mechanics

- **Resolution source — now confirmed from the question itself**: *"the open market US Dollar/
  Iranian Toman exchange rate on December 31, 2026 (Tehran time). One Toman is equal to 10 Rial.
  The primary source for this question will be [Bonbast](https://www.bonbast.com/graph)."* Fine
  print: *"Iran's official Central Bank rate will not be used as resolution, only the market
  rate."* So the working assumption made before the site was reachable was correct.
- **The range is the story.** This is a numeric question scaled **150,000 – 250,000 toman with
  BOTH bounds open**, in 500-toman steps. Bonbast printed **237,500** on 2026-09-11 — **5.3%
  below the ceiling**, after a +74% year. The central forecasting question is therefore not
  "what number" but "does it close above 250,000", and on this distribution it does with
  **65.3%** probability.
- **The question closes 2026-11-30 23:00 UTC**, a full month before the value date. Forecasts
  are locked a month early; a December de-escalation cannot be traded on.
- **Unit trap, load-bearing**: 1 toman = 10 rials. Polymarket's contract is titled
  "USD x Iranian **rials**" and its brackets are in rials; Metaculus asks in **toman**.
  Every Polymarket bracket must be divided by 10 before comparison. Verified empirically:
  the Sep-2026 Polymarket market prices "2.2M+" at 90.5%, and the live rate is
  2,375,000 rial = 237,500 toman — consistent only under the rial reading.
- **Release schedule**: bonbast updates intra-day; a daily figure is conventionally treated
  as final once the next day's is published. No revision risk of consequence.
- **Source-outage risk is real and precedented**: bonbast.com was forced offline in January 2025
  by DDoS attacks after public criticism from the then-CBI governor (Bloomberg, 2025-01-09). The
  question names no fallback.
- **Edge cases**:
  - *Redenomination.* The law passed the Majlis on 2025-10-30 and came into force 2025-12-07:
    **1 new rial = 10,000 old rials = 1,000 toman**, and the *toman* name was dropped from the
    final text. Preparation runs to Dec 2027, dual circulation for three years, old rial
    withdrawn by 2030. **As of 2026-09-12 bonbast, tgju, alanchand and mazaneh all still quote
    old units**, so this is a 2027+ risk rather than a 2026 one — but Polymarket's parallel
    contract carries an explicit conversion clause and **Metaculus's does not**, which is an
    unhedged resolution ambiguity if the switch comes early.
  - *Source outage.* Bonbast is intermittently blocked inside Iran and its JSON endpoint is
    token-gated. If it went dark, resolution would presumably fall back to tgju.org or
    alanchand.
  - *Multiple tiers.* Iran runs several official rates (CBI reference, Markaz-e Mobadele
    exchange-centre rate) well below the street rate. The question is about the **open**
    market; the official tiers are not the answer.

## Live readings (2026-09-11)

| Source | Value | Unit | Note |
|---|---|---|---|
| bonbast.com `usd1` (sell) | 237,500 | toman | last_modified 2026-09-11 20:31 |
| bonbast.com `usd2` (buy) | 237,400 | toman | 0.04% spread |
| tgju.org `price_dollar_rl` close 2026-09-10 | 2,359,750 | rial = 235,975 toman | 0.6% below bonbast |

The two independent sources agree to well under 1%, so the level is not in doubt.

## Reference classes considered

| Class | n | Window | Base rate (111-day multiple) | Source | Kept? |
|---|---|---|---|---|---|
| All 111-day windows, tgju daily free-market series | 3,837 | 2012-01 – 2026-09 | median ×1.064, IQR [0.992, 1.213] | tgju.org daily series | yes, as the floor |
| Post-2018 (maximum-pressure era) windows | 2,348 | 2018-01 – 2026-09 | median ×1.136, IQR [1.001, 1.284] | same | yes, primary |
| Post-2024 windows | 679 | 2024-01 – 2026-09 | median ×1.184, IQR [1.037, 1.302] | same | yes, but momentum-contaminated |
| Same calendar window (11 Sep → 31 Dec), by year | 14 | 2012 – 2025 | median +9.8%, mean +11.7%, IQR [+0.5%, +31.0%] | same | yes, seasonal control |

All four classes were kept: they disagree by ~20,000 toman at the median, which is itself
information about how much the answer depends on which regime you think 2026 resembles.

Annual year-end changes, from the same series (toman/USD):

| Year | 31 Dec | change | Year | 31 Dec | change |
|---|---|---|---|---|---|
| 2011 | 1,590 | — | 2019 | 13,299 | +26.7% |
| 2012 | 3,240 | +103.8% | 2020 | 25,629 | +92.7% |
| 2013 | 3,007 | −7.2% | 2021 | 27,388 | +6.9% |
| 2014 | 3,501 | +16.4% | 2022 | 41,174 | +50.3% |
| 2015 | 3,385 | −3.3% | 2023 | 50,598 | +22.9% |
| 2016 | 3,835 | +13.3% | 2024 | 81,230 | +60.5% |
| 2017 | 4,288 | +11.8% | 2025 | 135,565 | +66.9% |
| 2018 | 10,500 | +144.9% | 2026 YTD | 235,975 | +74.1% |

Two observations that do the work: the toman has **appreciated year-on-year in only 2 of 14
years** (2013 and 2015, both negotiation years — Rouhani's election and the JCPOA), and the
one large *within-year* reversal (2018: 13,716 on 11 Sep → 10,500 on 31 Dec, −23.4%) followed
an overshoot spike very like the one now in progress.

## Decomposition

The end-December level is spot × (war/sanctions path) × (monetary path).

- Monetary floor: liquidity growth and CPI put a structural ~3–4%/month drift into the
  series even in quiet periods. Over 111 days that alone is roughly ×1.10–1.15.
- The war path is the variance. Three branches: escalation continues (rate runs), a
  ceasefire/deal (sharp retracement, as in 2013/2015), stalemate (drift continues).
- Momentum vs. mean reversion: the rate rose **+18.3% in the 15 days to 2026-09-11**
  (200,600 on 27 Aug → 237,500). Spikes of that speed in this series are partly panic
  premium and historically give some of it back; that is what puts real mass below spot.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-11 | bonbast.com `/json` (token + cookie jar) | USD 237,500 toman sell / 237,400 buy, 20:31 | sets the anchor |
| 2026-09-11 | tgju.org `price_dollar_rl` summary table, 3,948 daily rows 2011-11-26 → 2026-09-10 | full free-market history; snapshotted to `raw/` | supplies every base rate above |
| 2026-09-11 | Polymarket gamma-api, `usd-x-iranian-rials-end-of-december` | 6 brackets, $9.4k volume, $18.9k liquidity; implied median ≈ 300,600 toman | primary market comparison |
| 2026-09-11 | Polymarket `usd-x-iranian-rials-end-of-september` | "2.2M+ rial" at 90.5% with $43k volume — i.e. ~9.5% on a fall back below 220,000 toman within 19 days | confirms real two-sided risk |
| 2026-09-11 | Kalshi `/trade-api/v2` events + series probes | no Iranian FX market found | no Kalshi comparison |
| 2026-09-12 | metaculus-aggregations skill, post 45340 (after the upstream fix landed) | numeric, **range 150,000–250,000, both bounds open**; close 2026-11-30T23:00Z; resolution source **Bonbast**; CBI rate excluded; status `upcoming`, n=6, **CP not revealed** | reframes the question around P(> 250,000) |
| 2026-09-12 | Metaculus comment, @Theomachado, 2026-09-11 | Polymarket-derived: **64% the US announces an end to the blockade by 31 Dec** (37% by 31 Oct), but only **19%** Hormuz traffic normal by year-end; 91% no US–Iran meeting by 30 Sep; 62% the Israel–Iran ceasefire holds; **16% a US invasion before 2027**. Rallies fade: the June MoU took 179k→153k (−14%) then back to ~172k within two weeks. Tehran analysts project **240–250k by late December**; one mid-August institutional forecast said ~180k. Since 18 Aug the **UAE has suspended all trade and financial transactions with Iran**, and Dubai's dirham remittance rate effectively sets the Tehran dollar price | raised the de-escalation weight from 0.14 to 0.40 across two branches; pulled the median from 290k down to 272k |
| 2026-09-11 | repo, `questions/2026-09-05-mc45230-*` | in-repo evidence of the US–Iran war: Hormuz closed 2026-02-28, US blockade line, IRGC missiles at a US carrier 2026-09-05 | frames the war branch |

## Dead ends and ruled-out hypotheses

- **metaculus.com was unreachable for the first half of this session** (Cloudflare 403 on every
  path; `ERR_CONNECTION_RESET` on page navigation; `/api/posts/` demands a token). **Fixed
  mid-session** by rebasing onto upstream commit ba7514b / PR #21, which rewrote the skill's
  transport. Operational notes: `--history` hangs on these questions, and a single fetch takes
  100–200s, so background it rather than running under a 120s foreground timeout.
- **archive.org Wayback**: no snapshot of any of the four post IDs. Ruled out.
- **metaforecast.org**: now redirects to quantifieduncertainty.org; the GraphQL endpoint is
  gone. Ruled out as a Metaculus mirror.
- **api.bonbast.com**: 502 through the proxy. The main site's POST `/json` works but only
  with a page token *and* a cookie jar — `{"rest":"1"}` otherwise. Documented above so the
  next update does not rediscover it.

## Open questions to chase next time

- Whether Bonbast's **buy or sell** quote governs (the question says only "the open market
  rate"; the spread is ~0.04%, so this is immaterial in practice but worth pinning).
- The CP, once revealed — the question is `upcoming` at n=6 with no Pro or gold cohort.
- Whether any quoting source switches to new rials before 31 December, which Metaculus's
  criteria do not hedge against.
- CBI intervention capacity: FX reserves accessible under blockade conditions.
- Whether the September spike retraces — the single most informative observable before December.

## v2 search log (2026-10-02)

| Date | Query / source | Finding | Use |
|---|---|---|---|
| 2026-10-02 | Bonbast POST `/json` (token from homepage + cookie jar) | USD 258,700 / 258,600, last modified 05:07 | spot |
| 2026-10-02 | bonbast.com/graph/usd (default view carries 3 Aug – 1 Oct inline in the Chart.js config) | flat 229–236k 13–27 Sep, then 245,000 / 255,800 / 256,200 / 258,700 on 28 Sep – 1 Oct | path; snapshot saved |
| 2026-10-02 | tgju series (v1 snapshot), 90-day windows | post-2018 median ×1.119, IQR [0.997, 1.231]; after ≥8% 21-day rise (n=575): median ×1.133, IQR [0.980, 1.267], P(<0.92) 17% | outside view for v2 |
| 2026-10-02 | Polymarket gamma API: Dec, Oct, blockade-end events | Dec volume $90.0k, implied median ≈ 290k; Oct "2.8M+" 69% on $12.8k; blockade end Oct 31 24.5%, Nov 30 38%, Dec 31 53.7% | market comparison; de-escalation weight |
| 2026-10-02 | metaculus-aggregations, post 45340 | CP/Pro/gold medians all clipped at 250,000; p25 232.0k / 237.0k / 237.9k; n=102–104; 5 comments | community |
| 2026-10-02 | Fortune / PBS / BNN, 29 Sep | rial 2.5M per dollar on 29 Sep; Trump rejected Iran's proposal; Araghchi says talks "more serious" | driver of the jump |
| 2026-10-02 | Al Jazeera 29 Sep; GlobalSecurity day 216 | US response delivered via Qatar 30 Sep; dispute on sequencing; 24 strike-free periods; inflation 61.4% (different measure from v1's 84.4%) | talks branch |
| 2026-10-02 | CBS live updates | Trump: Iran "ready to fold up … right after the election"; possible post-midterm attacks; blockade stays | escalation branch |
| 2026-10-02 | straits.live (PortWatch) | 1 transit 27 Sep (PortWatch); 16–17/day 29–30 Sep incl. dark vessels | Hormuz tripwire not fired |

Metaculus aggregations for this numeric question carry no CDF, so P(>250k) for the cohorts is
unknowable from the API beyond "≥ 50%".
