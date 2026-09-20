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
