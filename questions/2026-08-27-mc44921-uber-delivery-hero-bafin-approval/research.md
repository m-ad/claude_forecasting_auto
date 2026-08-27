# Research log — Will Uber's takeover of Delivery Hero be approved by BaFin before September 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: BaFin (Germany's Federal Financial Supervisory Authority) approving
  Uber's Offer Document for its takeover of Delivery Hero SE under the WpÜG, and that document
  being formally published, before 2026-09-01 (i.e. by end of day 2026-08-31).
- Release schedule / cutoff: scheduled_close_time 2026-09-01T00:00:00Z. `nr_forecasters`=81 as
  of 2026-08-27.
- **Critical framing correction**: this question is NOT about antitrust/merger-control approval
  of the Uber–Delivery Hero deal. It is a narrow, mechanical, procedural question about a
  disclosure-document review under German takeover law (WpÜG). Full merger clearance (EU
  Commission, other jurisdictions) is expected to take until H2 2027 and is irrelevant to this
  question's resolution — BaFin's review of the Offer Document is a completeness/adequacy check,
  not a competition assessment. The operator's/task's shorthand "approved" easily misreads this
  as "merger cleared" — it is not. Flagged explicitly in forecast.md.
- Edge cases / fine print:
  - Only the *initial* Offer Document counts; later amendments/supplements don't matter.
  - Price/minor term amendments before publication don't prevent YES, as long as the core deal
    (Uber acquiring DH) is unchanged.
  - If the BCA is terminated or the offer withdrawn/abandoned before an Offer Document is
    published, resolves NO immediately.
  - Publication (not just BaFin's internal sign-off) is what's required — but per WpÜG §14(2)
    the bidder must publish "unverzüglich" (without undue delay) after approval, so approval and
    publication are practically simultaneous (same or next business day).

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Time from friendly-deal announcement (BCA/Investment Agreement) to BaFin-approved, published Offer Document, recent large German WpÜG cash takeovers | 4 | 2022–2024 | 7–41 days (Aareal Bank/Atlantic BidCo: 20d; Software AG/Silver Lake: 26d from initial agmt, 13d from revised offer; Encavis/KKR: 41d; SUSE/EQT: 7d, but EQT was already majority owner — atypically fast) | Company press releases, EQS-News, BaFin site (see search log) | Yes — primary reference class |
| Statutory WpÜG process clock | n/a | per-deal | Submission to BaFin: hard 4-week deadline from the §10 announcement (here: 2026-07-16 → deadline ≈2026-08-13). BaFin review: ordinarily 10 working days from a complete submission; BaFin can grant the bidder up to 5 extra working days to fix a deficient filing; a further multi-week extension exists but is described as reserved for exchange offers (not applicable — this is an all-cash offer) | BaFin EN guidance pages, WpÜG commentary via search | Yes — used to build the scenario timeline |

Scaling to this question's window: announcement (2026-07-16) to cutoff (2026-09-01) = 47
calendar days. 3 of 4 precedent deals resolved inside a 47-day analogous window; Encavis (41
days) barely would have too. **But** as of today (2026-08-27, day 42 of 47), no approval has
been confirmed — i.e., the realized process has already burned through more runway than 3 of
4 precedents without resolving. This is the key update: unconditional base rate says "usually
resolves in time"; the conditional base rate (given no resolution by day 42) is much closer to
a coin flip, because the hazard for approval given the statutory clock is concentrated right
around now (day-42 ≈ Aug-13 submission deadline + 10 working days) through day ~49-56 (15
working days + possible 5-day correction grace), which straddles the Sept-1 cutoff almost
exactly.

## Decomposition

P(YES) = P(Uber submitted at or near the Aug-13 statutory deadline, not materially late)
       × P(BaFin completes review + bidder publishes within the standard ~10 working-day
          track, i.e. by ~Aug-27–28)
       + P(submission on time) × P(BaFin needs 11–15 working days, landing Aug-28–31, still
          inside the window)
       − [adjust for the small chance the BCA is terminated/withdrawn before publication]

Both submission timing and BaFin's processing speed are essentially unobservable to me in
real time (submission itself need not be public), so this decomposes into: "was the process
on the fast side of the historical spread (like Aareal Bank/Software AG) or the slow side
(like Encavis)?" Given deal complexity (largest-ever food-delivery M&A, cross-border US
bidder using a mix of German WpÜG + US Exchange Act Section 14(e) procedures, a concurrent
SSW Partners carve-out sale of 14 markets that likely needs coordinated disclosure in the same
document), I lean toward this deal sitting on the Encavis-like/slower end of the spectrum
rather than the SUSE-like fast end (SUSE's speed was atypical — EQT was already the
controlling shareholder, which is not the case here even though Uber holds ~25% + derivatives).

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-08-27 | Metaculus aggregations API (post 44921) | CP 51% (n=78), Pro 61% (n=6), Gold 50% (n=32); resolution criteria, fine print, background, 9 comments | Anchor; comments surfaced the Aug-13 submission-deadline logic independently |
| 2026-08-27 | WebSearch: "Uber Delivery Hero BaFin offer document approval August 2026" | Only pre-announcement (Jul 16) coverage; no confirmation of BaFin action | No signal either way |
| 2026-08-27 | WebSearch: "Uber Delivery Hero offer document submitted BaFin" | Same — future-tense language in all official statements as of Jul 16 | Confirms not-yet-submitted-as-of-announcement baseline |
| 2026-08-27 | WebSearch: Angebotsunterlage BaFin (German-language phrasing) | No additional results beyond English coverage | Dead end |
| 2026-08-27 | WebFetch delivering-value.com (official deal microsite) | States BaFin permission "has not yet been obtained" (approval still pending as of fetch) | Direct, current confirmation: not yet approved |
| 2026-08-27 | WebFetch ir.deliveryhero.com/news | 404 | Dead end |
| 2026-08-27 | WebSearch: "Delivery Hero Uber takeover news update" | General deal background (Bloomberg, EQS ad-hoc, Food On Demand); board recommends tender "subject to review of the Offer Document" — confirms Offer Document not yet finalized/reviewed by DH board as of latest coverage found | Mild NO signal |
| 2026-08-27 | WebSearch: "Delivery Hero stock news August 26 2026" | DH Q2 2026 trading-update webcast was Aug 26; stock steady; no mention of BaFin/offer-document milestone; separately, Asian regulators call food-delivery sector an "effective oligopoly" (Aug 25) — unrelated to BaFin track but a reminder regulatory attention is elevated globally | No BaFin-specific news; slightly reinforces "still pending" |
| 2026-08-27 | WebSearch + WebFetch: BaFin official published-offer-documents database (bafin.de, EN) | Most recent entries: VINCI/ALL FOR ONE (12.08.2026), Galaxy Germany/Nagarro (06.08.2026, correction 11.08.2026), Bayerische Gewerbebau/Ludwig Beck (21.07.2026), Worthington Steel/Klöckner (15.07.2026), etc. **No Uber/Delivery Hero entry.** | **Direct hard evidence: not yet approved as of the most recent listed entries (≥12.08.2026); reinforced by absence of any news through 2026-08-27** |
| 2026-08-27 | WebSearch: Aareal Bank / Atlantic BidCo timeline | Investment Agreement 2022-04-06 → Offer Document approved/published 2022-04-26 (20 days) | Reference-class data point |
| 2026-08-27 | WebSearch: Encavis / KKR timeline | Announced 2024-03-14 → Offer document approved/published 2024-04-24 (41 days) | Reference-class data point; closest analog in deal complexity terms found |
| 2026-08-27 | WebSearch: Software AG / Silver Lake timeline | Investment Agreement 2023-04-21 (revised offer 2023-05-04) → Offer document published 2023-05-17 (26 days from initial agreement, 13 days from revised offer) | Reference-class data point |
| 2026-08-27 | WebSearch: SUSE / EQT timeline | Announced 2023-08-17 → Offer document published 2023-08-24 (7 days) | Reference-class data point; noted as an outlier because EQT was already SUSE's majority shareholder (simpler/likely pre-cleared informally with BaFin) |
| 2026-08-27 | WebSearch: WpÜG statutory timeline (BaFin EN guidance, CMS/White & Case commentary) | 4-week statutory deadline to submit Offer Document after the §10 announcement; BaFin then has ~10 working days to approve/prohibit, with up to 5 extra working days if it requires the bidder to fix deficiencies; longer extensions reserved for exchange offers (not applicable here, all-cash deal) | Built the scenario timeline (submission ≈Aug-13; approval hazard concentrated Aug-27 through ~Sept-3/8) |
| 2026-08-27 | WebFetch: TradingView copy of the WpÜG §10 announcement (2026-07-16) | Confirms Jul-16 is the formal trigger date for the 4-week submission clock; no explicit deadline stated in the announcement text itself (deadline comes from the statute, not the announcement) | Confirms decomposition's anchor date |
| 2026-08-27 | WebSearch: Uber Q2 2026 earnings (Aug 5) call / prepared remarks PDF | No usable detail on BaFin timeline extracted (PDF text garbled); general deal terms only | Dead end |
| 2026-08-27 | WebSearch: EU antitrust / merger-control status | Confirms EU Commission review is a *separate, much longer* track (companies "confident" of clearing without major issues within ~12 months, expected close H2 2027); irrelevant to BaFin Offer Document question per the fine print | Confirms question is procedural/German-only, not substantive antitrust |
| 2026-08-27 | WebSearch: Polymarket/Kalshi/Manifold for a matching market | No dedicated market found on this specific BaFin/offer-document question | No market comparison available beyond Metaculus |
| 2026-08-27 | WebSearch: Sentinel/Mantic/GJOpen coverage | No coverage found of this narrow a question (checked general search, no dedicated hits) | Not included in comparison table |

**Source count**: ≥18 distinct sources consulted (Metaculus aggregations API + comments;
delivering-value.com; ir.deliveryhero.com; investor.uber.com; Delivery Hero newsroom; SEC 8-K
filings (x2 documents); BaFin published-offer-documents database; BaFin WpÜG EN guidance;
TradingView WpÜG §10 announcement copy; Aareal Bank press release; Encavis/KKR press
coverage (MarketScreener, ESG News); Software AG newscenter (x2 releases); SUSE.com news;
EQS-News ad-hoc releases (x2); Global Competition Review; ad-hoc-news.de stock-news items
(x2); Uber Q2 2026 earnings materials).

## Dead ends and ruled-out hypotheses

- Ruled out treating this as a full merger-control/antitrust-approval question — it is not;
  see "Question mechanics" above. Would have produced a badly wrong (far too low) forecast.
- Could not find any public confirmation of the exact date Uber submitted the Offer Document
  to BaFin (submission itself is not a mandatorily-disclosed event under WpÜG — only the
  approved/published document and the earlier §10 "decision to launch an offer" announcement
  are). Treated as unobservable and modeled via the statutory clock instead.
- ir.deliveryhero.com/news 404s — use deliveryhero.com/newsroom or EQS-News company feed
  instead next time.
- No dedicated prediction market (Polymarket/Kalshi/Manifold) exists for this narrow question;
  don't bother re-searching every update unless a new platform is mentioned.

## Open questions to chase next time

- Did BaFin approve/publish the Offer Document before 2026-09-01? Check the BaFin
  published-offer-documents database directly (fast, authoritative) and
  delivering-value.com first.
- If not yet resolved, look for any news of a BaFin correction request / deficiency letter,
  which would be the clearest signal of a slip past the 10-working-day fast track.
- Watch for the EQS-News ad-hoc feed for Delivery Hero SE and Uber's SEC 8-K filings for the
  actual publication announcement — it will be an ad-hoc disclosure the same day.

## Red-team review (2026-08-27, same-day, no forecast change)

A `/review` pass was run against v1 without modifying forecast.md/meta.yaml. Summary of
findings for the next update to weigh:

- **Reference-class gap**: the n=4 class (SUSE, Aareal, Software AG, Encavis) is uniformly
  small/mid-cap ($2-3B). UniCredit/Commerzbank (~€35-43B, cross-border, same BaFin database)
  took ~60 days from formal offer launch (~March 2026) to published Offer Document (2026-05-05)
  — far outside the 7-41 day range used. Partially confounded (exchange offer, which gets
  BaFin's extended review track — doesn't apply to this all-cash deal), but a legitimate rival
  comparator that was never checked despite being in the same database already queried.
- **Under-modeled conjunction**: Delivery Hero's own board explicitly hadn't finished
  reviewing the Offer Document as of the announcement ("subject to their review" — already in
  our Evidence section but not built into the scenario decomposition), and WpÜG §13 "certain
  funds" financing-confirmation requirements are a distinct, plausible correction-trigger not
  named in the scenario table (only generic "complexity" was).
- **Anchoring tell**: scenario weights (30/15/25/25/5) sum to exactly 45.0%, suspiciously
  round and suspiciously close to "a bit below CP/gold" — plausibly reverse-fit to a target
  rather than independently derived.
- **IQR likely too narrow**: [32%, 58%] (26pp) for a question whose entire mass hinges on two
  structurally unobservable facts (exact submission date, BaFin's review-track assignment);
  the forecast's own sensitivity table shows ±15pp swings from single-assumption changes,
  which argues for something closer to [20%, 65%].
- **Near-miss data-reliability incident**: a finanznachrichten.de WebFetch during the review
  claimed the Offer Document was published today (2026-08-27) with acceptance period Aug 27 -
  Nov 5. Triangulated against three authoritative sources fetched fresh (BaFin's own
  published-offer-documents database, delivering-value.com, SEC EDGAR's live 8-K listing for
  Uber) — all three still show no approval/publication. Judged the finanznachrichten.de hit to
  be a fetch/summarization artifact, not real news. **Lesson for the next update**: never treat
  a single fetched article as resolving evidence this close to the deadline — triangulate
  against BaFin's database + the deal microsite + EDGAR before updating.
- **Alternative the red-team implies**: median ≈30-35%, IQR ≈[18%,50%], given partial (~40%)
  weight — i.e. a blended re-estimate around 35%, IQR [22%, 52%]. Decisive missing fact: the
  actual date Uber submitted the Offer Document to BaFin.
