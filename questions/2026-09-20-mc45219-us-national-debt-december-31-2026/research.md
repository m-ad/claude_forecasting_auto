# Research log — What will be the US national debt on December 31, 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- **Resolution source**: Treasury Fiscal Data, "Debt to the Penny", field
  `tot_pub_debt_out_amt` (Total Public Debt Outstanding) for `record_date = 2026-12-31`.
  API: `https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny`.
- **Release schedule / cutoff**: published each business day, ~3–4pm ET the *following*
  business day. 2026-12-31 is a Thursday and a Treasury business day, so a genuine
  2026-12-31 record will exist; it should post on Monday 2027-01-04 (2027-01-01 is a
  Friday federal holiday). No revision risk worth modelling — Debt to the Penny is a
  settled accounting figure, not a survey estimate.
- **Metaculus mechanics**: numeric question, range 40.5T–42.5T with **open upper and lower
  bounds**, 200 buckets of $10bn. `cp_reveal_time = 2026-09-25T17:00Z`, so on the day of
  this forecast (2026-09-20) there is **no community prediction, no Pro and no gold
  aggregation** — 6 forecasters, all hidden. Closes 2026-11-30 (a month before the event),
  so forecasters must commit before the November refunding revision and before the
  December CR deadline resolves.
- **Edge cases / ambiguities**:
  - TPDO ≠ *debt subject to limit*. On 2026-09-17 TPDO was $40.0933T while debt subject to
    limit was $39.9033T — a $190bn gap (unamortized discount $186.0bn, Federal Financing
    Bank $3.6bn, other $0.5bn). The statutory limit binds the *smaller* number. Anyone
    reading "$41.1T debt limit" as a cap on the headline debt figure is off by ~$190bn.
  - Question asks for the *level*, not the change. There is no realistic path to a
    decrease: even a full-quarter shutdown leaves mandatory spending and interest running.
  - No fine print. Background text is descriptive only and contains one number worth
    checking: it says end-2025 debt was "just over $38.5 trillion" — the actual
    2025-12-31 Debt to the Penny value is $38.5140T. ✓

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Calendar-year Dec-31→Dec-31 % growth in TPDO | 13 | 2013–2025 | mean +6.9%, median +6.1% (excl. 2020: mean +5.8%) | Debt to the Penny | Partly — wrong window, used only as a scale check |
| **17 Sep → 31 Dec % change in TPDO** | 14 | 2012–2025 | mean +2.75%, median +2.65%, range +1.68% to +4.25% | Debt to the Penny | **Yes — primary outside view** |
| Same, excluding debt-ceiling-distorted and COVID years (2015, 2017, 2020, 2021, 2022) | 9 | 2012–2025 | mean +2.64%, sd 0.44pp | Debt to the Penny | **Yes — used for dispersion** |
| Same, last three years only (2023 +2.89%, 2024 +2.45%, 2025 +2.72%) | 3 | 2023–2025 | mean +2.69% | Debt to the Penny | **Yes — closest deficit regime** |
| Ratio of Q4 daily borrowing rate to Jan–Sep daily rate | 3 | 2023–2025 | 1.46×, 1.59×, 1.98× (mean 1.68×) | Debt to the Penny | Yes — independent cross-check |
| Oct–Dec change in **intragovernmental** holdings | 4 | 2022–2025 | +$272bn, +$226bn, +$224bn, +$308bn | Debt to the Penny | **Yes — the load-bearing seasonal** |

Scaled to the question window from the 2026-09-17 level of $40.0933T:
median +2.65% → **$41.16T**; last-three-years mean +2.69% → **$41.17T**;
clean-years mean +2.64% → **$41.15T**. Clean-years sd 0.44pp ≈ **$176bn**.

## Decomposition

Identity used throughout: `ΔTPDO = Δ(debt held by public) + Δ(intragovernmental holdings)`,
and `Δpublic ≈ unified deficit + Δcash(TGA) + other means of financing`.

Verified on Oct–Dec 2025: deficit $602.4bn (MTS) + ΔTGA −$17.8bn → $584.6bn vs actual
Δpublic $569.0bn (other means of financing −$15.6bn). Δintragov was +$307.5bn.
Total ΔTPDO +$876.5bn. ✓

**The intragovernmental seasonal is the single most under-appreciated driver.** Over
2026-01-01 → 2026-09-17 intragov holdings rose only **+$33bn** while public debt rose
+$1,546bn; but every Oct–Dec quarter adds $224–308bn of intragov debt, because the federal
retirement trust funds (CSRDF, Military Retirement Fund) and the social-insurance trust
funds receive their large start-of-fiscal-year credits on 1 October and invest them in
Government Account Series securities. These are intragovernmental transfers that net to
zero in the unified deficit but *do* create debt.

Central build (all $bn):

| Component | Value | Basis |
|---|---|---|
| TPDO 2026-09-17 (actual) | 40,093.3 | Debt to the Penny |
| + 18–30 Sep stub | +130 | 2023/24/25 stubs were +0.37%, +0.32%, +0.39% of the 17 Sep level → +$144bn; shaded to +$130bn because TGA already sits at $972.7bn vs Treasury's $950bn end-Sep assumption |
| + Oct–Dec Δ public | +653 | Treasury's 2026-08-03 estimate of $628bn privately-held net marketable borrowing, −$20bn for Treasury's recent tendency to over-estimate (FY26 Q1 est 569 → actual 550; FY26 Q2 est 574 → actual ≈534; FY26 Q3 est 189 → actual 190), +$45bn measured wedge between Δpublic and privately-held borrowing |
| + Oct–Dec Δ intragov | +285 | 2022–25 range $224–308bn, scaled for a 5.4% larger intragov stock |
| **= TPDO 2026-12-31** | **41,161** | |

The "wedge" exists because privately-held net marketable borrowing excludes SOMA auction
add-ons and excludes nonmarketable issuance (savings bonds, SLGS). Measured directly:
FY26 Q1 +$19bn, FY26 Q2 +$50bn (using an inferred $534bn actual), FY26 Q3 +$60bn. Used
+$45bn. With QT over (FOMC stopped runoff 2025-12-18) and the Fed now making
reserve-management purchases, SOMA is *growing* — Treasuries on the balance sheet +$353bn
year-on-year as of 2026-09-16 — which makes the wedge positive rather than negative.

**Debt-ceiling arithmetic.** Statutory limit $41,103,996mn (DTS, 2026-09-17), set by OBBBA
on 2025-07-04 (+$5.0tn from $36.104tn). Debt subject to limit $39,903,258mn → headroom
**$1,200.7bn**. Since TPDO sits ~$190–196bn above debt subject to limit, the arithmetic cap
on the *question's* quantity is ≈ **$41.30tn**; Treasury needs auction-settlement room, so
the practical cap is ≈ **$41.28tn**. The central forecast is $120bn under it. BPC (June
2026) projects the limit is reached "late winter to mid-summer 2027", which is consistent:
my central path leaves ~$140bn of headroom at year-end, i.e. the limit binds in
Jan–Feb 2027 unless Treasury runs cash down first.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-20 | `metaculus_aggregations.py 45219 --comments 15 --history` (needed `METACULUS_FORCE_TLS12=1`; without it the scaffolder got status 0) | status=upcoming, 6 forecasters, CP hidden until 2026-09-25, **zero comments**, range 40.5–42.5T open-bounded | No anchor available; forecast is fully independent |
| 2026-09-20 | Debt to the Penny API, 2012–2026 daily (3,694 rows) | 2026-09-17 = $40.0933T; $40T first crossed **2026-08-18**; $39T on 2026-03-17 | Base level; milestone pace ~5 months/$1tn in 2026 |
| 2026-09-20 | Same, Sep-17→Dec-31 increments 2012–2025 | mean +2.75%, median +2.65% | Outside view |
| 2026-09-20 | Same, public/intragov split 2022–2026 | Oct–Dec intragov +$224–308bn every year; +$33bn over Jan–Sep 2026 | Identified the dominant seasonal |
| 2026-09-20 | DTS `debt_subject_to_limit` | Limit $41,103,996mn; DSL $39,903,258mn; headroom $1,200.7bn; non-limit debt $190.1bn | Right tail truncated at ≈$41.28–41.30T |
| 2026-09-20 | DTS `operating_cash_balance` | TGA close 2026-09-17 = $972.7bn; opened FY2026 at $890.8bn | Slightly above Treasury's $950bn end-Sep assumption |
| 2026-09-20 | Treasury press release sb0584 (2026-08-03) | Oct–Dec 2026 privately-held net marketable borrowing **$628bn**, end-Dec cash **$850bn**; Jul–Sep $739bn / $950bn | Primary inside-view anchor |
| 2026-09-20 | Treasury Presentation to TBAC, FY2026 Q3 (74pp, parsed locally) | Confirms both figures; PD median FY2027 deficit $2,008bn (25th 1,960 / 75th 2,114), OMB $2,172bn, CBO Feb $1,887bn; PD FY2027 privately-held borrowing $2,105bn; explicit statement that estimates are current-law and exclude new legislation | Confirms anchor; gives FY2027 deficit spread |
| 2026-09-20 | MTS Table 1 (monthly deficits, FY2024–FY2026) | FY2026 Q1 (Oct–Dec 2025) deficit $602.4bn; FY2025 Q1 $510.0bn; FY2025 total $1,775bn; FY2026 through Aug $1,966bn | Deficit-scaling cross-check (gives a *lower* answer, ≈$41.06T) |
| 2026-09-20 | CBO Monthly Budget Review, Sept 2026 (via CRFB + The Hill) | FY2026 deficit now projected **$2.1tn**, up $200bn from February, "mostly" because customs duties came in ~$250bn below projection after the IEEPA ruling | Explains why debt hit $40T early; already in Treasury's estimate |
| 2026-09-20 | Supreme Court IEEPA ruling (2026-02-20, 6–3) + CIT refund order (2026-03-04); Penn Wharton, Holland & Knight, Skadden, Cato | ~$166bn collected; up to ~$175bn refundable; $104.3bn authorised / $71.1bn paid by 2026-06-29; ~$128.7bn accepted for processing by 2026-07-31 | Residual refunds are an Oct–Dec upside of perhaps $20–40bn, mostly already in Treasury's number |
| 2026-09-20 | H.R. 6500 / P.L. 119-103, signed 2026-09-02 | FY2027 CR funds government **through 2026-12-11** | A lapse from 12 Dec would defer ~$25–40bn of outlays into 2027 → left-tail driver |
| 2026-09-20 | Federal Reserve H.4.1 (2026-09-17) + Balance Sheet Developments | QT stopped 2025-12-18; reserve-management purchases of short Treasuries under way; Treasuries $4,554bn, +$353bn y/y | Makes the borrowing→debt wedge positive |
| 2026-09-20 | BPC "When will we reach the debt limit (again)?" (June 2026) | Limit reached "late winter to mid-summer 2027"; extraordinary measures then last ~6–9 months | Independent confirmation the ceiling does not bind in 2026 |
| 2026-09-20 | Kalshi API: series `KXTRUFPDEBT` ("Total Public Debt on <date>"), `KXDEBTLEVEL`, `KXDEBTGROWTH26`, `KXUSDEBTMON`, `KXDEBTGROWTH` | `KXTRUFPDEBT` has only **finalized 2026-07-31** strikes; no open Dec-2026 market. `KXDEBTGROWTH` is "during the Trump Administration" (closes 2029), no prices | No market anchor |
| 2026-09-20 | Polymarket gamma API `search=national debt`, Manifold `search-markets` | Nothing matching; Manifold has only "When will US debt pass $50tn?" (vol 65, play money) | No market anchor |
| 2026-09-20 | "$2,000 tariff dividend" status | Not enacted; no bill has passed either chamber; Section 122 authority expired 2026-07-24 | 4% weight on a year-end fiscal package, and cash could barely move by 31 Dec even if enacted |

## Dead ends and ruled-out hypotheses

- **"The debt ceiling caps the answer at $41.1T."** False as stated — the limit binds debt
  *subject to limit*, which runs ~$190bn below the headline figure. The cap on the answer
  is ≈$41.28–41.30T, and it truncates only the top ~6% of the distribution.
- **Naive constant-daily-rate extrapolation.** 2026 has run at $6.07bn/day (Jan 1 → Sep 17);
  105 more days at that rate gives only $40.73T. This is wrong because Oct–Dec is the
  heaviest borrowing quarter: the Q4/Jan–Sep daily-rate ratio was 1.46× (2023), 1.59×
  (2024), 1.98× (2025). Applying the 1.68× mean gives +$1,071bn → $41.16T, matching the
  seasonal-percentage method.
- **Scaling the FY2027 deficit by the historical Q1 share.** Q1 was 28.7% of the fiscal-year
  deficit in both FY2025 and FY2026; 28.7% × a $2,050bn FY2027 deficit is $588bn, which
  would imply ≈$41.06T. Treasury's own $628bn borrowing estimate implies a materially
  larger Q1 (~$730bn once the $100bn cash drawdown is added back) — plausible because
  Oct–Dec 2025 still collected IEEPA tariffs (~$80bn/quarter) that Oct–Dec 2026 will not,
  and residual refunds are still being paid. Kept as the main left-tail scenario rather
  than discarded.
- **Tariff-dividend cheques as a Q4 shock.** Not enacted, no vehicle has passed a chamber,
  and Treasury could not disburse before 31 Dec even on a November enactment.
- **A December shutdown as a big downside.** Checked against the 43-day Oct–Nov 2025
  shutdown: TPDO still rose $402bn in October 2025 and $357bn in November 2025. Mandatory
  spending and interest do not stop. Worth only ~$25–40bn.
- **Market anchors.** Genuinely absent (see search log). Do not re-hunt for a Kalshi
  December strike without first checking whether `KXTRUFPDEBT` has been re-listed.

## Open questions to chase next time

1. **Metaculus CP reveals 2026-09-25** — pull all three cohorts then. If Pro/gold cluster
   materially away from $41.16T, find the fact I missed before defending the number.
2. **Treasury quarterly refunding, ~2026-11-02** — the Oct–Dec privately-held borrowing
   estimate is revised and the Jan–Mar 2027 estimate is published for the first time. This
   is the single highest-information scheduled event before the question closes.
3. Actual FY2026 final MTS (~2026-10-15) and the September 2026 surplus/deficit.
4. Whether Treasury signals a *higher* end-December cash target than $850bn in order to
   pre-fund the 2027 debt-limit episode — the main upside mechanism.
5. Whether the November TBAC minutes discuss ceiling-driven issuance management.
6. Actual October and November Debt to the Penny month-ends versus the central path
   ($40.72T and $40.98T).

**Tooling note (fixed in this branch):** the `METACULUS_FORCE_TLS12=1` workaround the search
log records is no longer needed. `metaculus_aggregations.py` now relaunches on TLS 1.2
whenever an attempt returns `status 0`, not only when the exception carries a reset marker,
so a plain `new_question.py --url` scaffold works first time. Verified live on post 45219
with the variable unset.

## 2026-10-15 — v3 update (Update mode; median $40.92T → $40.91T, IQR [$40.86T, $40.98T] → [$40.86T, $40.96T])

(No dated section was appended for v2 on 2026-10-09; v2's evidence is itemised in forecast.md.)

### Metaculus status

- Fresh CP / Pro / gold: **unavailable**. The parent session ran the aggregations script once
  after a 200 s cool-down and got 403 (Cloudflare managed challenge). I made no Metaculus calls
  myself. The bot-key API (`raw/metaculus-api-2026-10-15.json`) shows the question open, 118
  forecasters (107 on 10-09), comment_count 15 (12 on 10-09), and criteria, scaling and dates
  unchanged.
- **Correction to the brief.** A cohort reading *is* cached: `raw/metaculus-2026-10-09.json`
  holds recency_weighted / metaculus_pros / gold_medalists as of 2026-10-09 05:00Z.
  - CP $41.049T, IQR [40.885, 41.262], n=106.
  - Pro $41.006T, IQR [40.877, 41.159], n=10.
  - Gold $41.013T, IQR [40.857, 41.187], n=31.
  - The file also has 340 history points and 8 comments.
  - It postdates the v2 ledger entry (04:08Z), which is why v2 said "unavailable".
  - It is used in v3 as a dated, 6-day-old reference. It is **not** logged as today's
    community value; the ledger gets `n_forecasters` only.
- Cohort trajectories since the 2026-09-21 open: Pro $41.109T → $41.006T; gold
  $41.079T → $41.013T; CP $41.120T → $41.049T. All three are drifting toward this forecast.
- Comments in that snapshot:
  - DeRuina flags the Dec-31 trust-fund interest credit. It is real (+$44–74bn single-day
    intragov in 2016–25, except 2020–21) and already sits inside the Oct 13 → Dec 31 reference
    class.
  - DeRuina also claims TPDO is only ~$30bn above debt subject to limit. Wrong: the gap was
    $198.4bn on 2026-10-13.
  - Koboh extrapolates linearly to ~$40.8T. DaiLothbrook maps the $628bn estimate to $41.13T
    using the 2022–25 intragov seasonal, which is the v1 error.

### Search / data log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-15 | DTTP API 2026-09-01 … 10-13 (`raw/debt-to-penny-2026-10-15.json`) | 10-13: TPDO 40,343.9; public 32,483.6; intragov 7,860.2 ($bn). Since 10-07: +59.8 (public +44.4, intragov +15.5) | Re-base; intragov drift slightly firm |
| 2026-10-15 | DTTP history 2015-09 … 2025-12 (2,789 rows) | Oct 13 → Dec 31: 2022 +275, 2023 +472, 2024 +511, 2025 +629; % 0.88 / 1.41 / 1.43 / 1.66. Intragov Oct 13 → Dec 31 median +33 (2016–25 ex-2021; range −39 … +98). Oct 7 → 13 TPDO range −4 … +33 (2026: +60) | Outside view $40.88–40.95T |
| 2026-10-15 | DTS operating cash (`raw/dts-operating-cash-2026-10-15.json`) + TGA history 2022–26 | TGA 984.0 (9-30) → 893.7 (10-1) → 885.8 (10-7) → 920.2 (10-13). TPDO − TGA: 39,187.8 → 39,423.7. Net-financing proxy (Δpublic − ΔTGA) Sep 30 → Oct 13: 2026 122; 2025 134; 2024 150 (2026's window misses the 2nd-Wednesday SS payment on 10-14) | No deficit signal yet; built TGA-neutral tripwires |
| 2026-10-15 | DTS debt subject to limit (`raw/dts-debt-subject-to-limit-2026-10-15.json`) | DSL 40,145.5; limit 41,104.0; headroom 958.5; unamortized discount 194.3, FFB 3.6, other 0.5 | Ceiling non-binding |
| 2026-10-15 | DTS public debt transactions (`raw/dts-public-debt-transactions-2026-10-15.json`) | MTD to 10-13: bills +73.4, notes −1.3, bonds −12.0, TIPS +2.7; GAS issues 5,904.3 / redemptions 5,790.8 (net +113.4 = intragov change) | Confirms the decomposition |
| 2026-10-15 | DTS deposits/withdrawals (Table II), 10-13 vs 2025-10-10/14/15 and 2024-10-11/15 | CBP withdrawals MTD 2.95 vs 0.71 a year ago, so residual IEEPA refunds are trickling out. Customs deposits are partial-month and uninformative. Summed "ex-debt" totals do not reconcile with the TGA identity (double-counted rows), so I did not use them | Dead end for a deficit read |
| 2026-10-15 | MTS Table 1 via API | Latest month is Aug 2026 (Sep MTS not yet in the API). Q1 deficits: **FY2024 $510.0bn, FY2025 $711.0bn, FY2026 $602.4bn**. Jun–Sep: 2026 120 / 432 / 167 / 28 (Sep from CBO) = 747; 2025 −27 / 291 / 345 / −198 = 411 | **v1's research log mislabelled FY2024 Q1 ($510bn) as FY2025 Q1.** The 28.7% Q1-share statistic was mis-paired. Correct shares: 28.1% / 40.0% / 30.2% |
| 2026-10-15 | WebSearch "intragovernmental holdings October 1 2026 … Military Retirement Fund" → OMB FY2027 Budget Appendix `civ_fy2027.pdf` (downloaded, pdftotext) | **Payment to Military Retirement Fund: $154,387mn (2025 actual), $161,413mn (2026 est), $23,451mn (2027 est).** MRF fund balance (investments) 1,806.9 → 1,984.6 → 2,057.8 ($bn). Narrative: amortization schedule set by the DoW Retirement Board of Actuaries; no reason given for the drop | **Key finding.** Explains ~90% of the Oct-1 GAS shortfall (net +80 vs +230 in 2025). "Deferred credit" scenario 15% → 3% |
| 2026-10-15 | CBO MBR Sept 2026 (PDF 403; via search), CRFB 10-08, AAF 10-08 | FY2026 deficit $1,993bn (6.2% of GDP), +$218bn y/y; outlays $7,396bn (+6%), interest +$115bn (+11%), corporate −16%, customs −$22bn after ~$130bn of $166bn IEEPA refunds; Sep deficit $28bn | Hot run-rate; supports the Treasury-plan path over the soft path |
| 2026-10-15 | Treasury sb0590 (2026-08-05 refunding statement) | Next refunding announcement **Wed 2026-11-04** (borrowing estimate normally the Monday, 11-02); coupon sizes unchanged "for at least the next several quarters" | Tripwire dates |
| 2026-10-15 | Kitco/Reuters 2026-02-02 | Oct–Dec 2025: Nov est $569bn → actual $550bn, cash 873 vs 850, "actual borrowing $42bn lower" cash-adjusted. Jan–Mar first est (Nov) ≈ $577bn → $574bn (Feb). Apr–Jun first est $109bn (then $189bn in May per headline). Jul–Sep: $671bn (May) → $739bn (Aug) | Mixed track record; bias −$25bn and the upward-revision risk carried in scenario 4 |
| 2026-10-15 | DTTP Jun 30 → Sep 30 2026 | Δpublic +744 vs $739bn privately-held estimate, cash 984 vs 950 assumed, so the cash-adjusted need was ~$30–90bn below plan, depending on the wedge | Supports a modest negative bias |
| 2026-10-15 | C.H. Robinson 2026-09-17 (CBP declaration to the CIT) | $134.7bn accepted into CAPE; ~$122bn certified and transmitted to Treasury; $1.3bn on hold; Phase 3 (court-ordered reliquidations) from 2026-10-06 | ~$12–36bn of refunds still to come in Q1 FY2027; LR ≈ 1 |
| 2026-10-15 | The Star/Bloomberg (NY Fed RMP pause) | RMPs zero since mid-August, none planned for the period to 10-14; ~$15.6bn/month MBS-to-bill reinvestment continues | Wedge +45 → +35 |
| 2026-10-15 | NTU "Projecting the debt limit" (via search) | Limit reached ~May 2027, X-date ~Feb 2028 | Ceiling irrelevant in 2026 |
| 2026-10-15 | Shutdown / lame-duck searches (AACOM, NASFAA, Steptoe 9-18, Akin Gump [403]) | CR to 2026-12-11 confirmed; lame duck from 11-09; no October reporting of a December shutdown fight | No change |
| 2026-10-15 | Treasury refunding / TBAC searches | No preview or leak of the Nov-2 estimate; the August TBAC assumption of $850bn end-Dec cash still stands | No change |
| 2026-10-15 | Polymarket gamma `peak-us-national-debt-before-2027` | $41T: mid 0.55 (bid 0.25 / ask 0.85, last 0.83), vol $683, unchanged since 10-09, so no trades. $42T: 0.039 | No information |
| 2026-10-15 | Manifold `will-us-gross-federal-debt-reach-41` | 55.8% (81% on 10-09), 8 traders, $204 vol, last bet 10-13 | Weak; direction matches |
| 2026-10-15 | Kalshi KXTRUFPDEBT / KXDEBTLEVEL / KXUSDEBTMON / KXDEBTGROWTH26 / KXUSDEBT | No open markets | — |
| 2026-10-15 | General search "national debt forecast end of 2026" | Nothing beyond the CBO baseline, the Concord Coalition (~$40T by end-2026, stale) and a mirror of the Polymarket page | — |

### Model changes (v3)

- Treasury-plan scenario: Δpublic for the quarter = 628 − 34 (start cash) − 25 (bias) + 35 (wedge)
  = 604, giving $40.922T with intragov 7,893.
- Deficit path: Q1 deficit ≈ 720 (my estimate), so Δpublic = 720 − 15 (other means) − 134 (TGA
  984 → 850) = 571, giving $40.889T.
- v2's deficit path had added the +45 wedge on top of the deficit identity. That was a conceptual
  double count, offset in v2 by the lower deficit it assumed.
- Mixture, with sequential effects on the median:
  - MRF finding −11.5
  - intragov re-base +13
  - deficit cross-check / softer split −2
  - bias and wedge −7
  - heavier tail +7
  - final weights and σ decay −2
  - net −2.3 ($40.915T → $40.913T)
- Tripwires re-specified TGA-neutral (TPDO − TGA), because Oct 31 is a Saturday: the last October
  record is Oct 30 and carries ~$90bn of shifted Nov-1 payments, while the 2y/5y/7y settlement
  moves to Nov 2.

### Dead ends

- CBO MBR PDF: 403 for both WebFetch and curl.
- Akin Gump approps blog: 403.
- metalsmine (Apr–Jun estimate article): 403.
- DTS Table II "ex-debt" sums: rows do not reconcile with the TGA identity; not usable as a
  deficit proxy without a category map.

### Open questions for next time (by 2026-11-03)

1. DTTP for 2026-10-30 (published ~11-02): compute TPDO − TGA against the $39.59–39.71T band.
2. Treasury borrowing estimate, Mon 2026-11-02: Oct–Dec figure vs the $594bn cash-adjusted
   central, the end-Dec cash assumption, and the first Jan–Mar 2027 estimate. The refunding
   statement follows on 11-04.
3. CBO October MBR (~11-09) and the September MTS (whenever the API shows it).
4. Why the MRF payment collapses: check the DoD Office of the Actuary valuation or the Board of
   Actuaries minutes. This is only a curiosity now; it does not change the mechanics.
5. Re-try the Metaculus aggregations when the parent's path reopens. The question closes
   2026-11-30, so the final update must land before then.
