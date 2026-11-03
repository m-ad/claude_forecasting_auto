# How many Fifth Circuit news announcements concerning the Judge Ada Brown misconduct proceeding will be dated November 1–12, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46419/ |
| **Tournament** | minibench — one shot, window 2026-11-03T06:49:05Z -> 2026-11-03T09:49:05Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-03 / 2026-11-03 / 2026-11-13 |
| **Status** | closed |
| **Current forecast** | Median 1, IQR [0, 2] (v1, 2026-11-03) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-03

### What resolves YES

The resolved value is a count: entries on https://www.ca5.uscourts.gov/news?month=11&year=2026, as displayed at 17:00 CT on 2026-11-13, whose *listing-column* date is 2026-11-01 to 2026-11-12 inclusive and which concern the Brown misconduct proceeding (title or linked document names Judge Ada Brown, Complaint No. 05-26-90177 or 05-26-90196, or the Council's proceedings against her). Confidential substance does not matter; duplicates count once. Non-Brown notices are excluded.

Arithmetic: the November listing fetched on 2026-11-03 shows "No matching items" (count today = 0). The last Brown entry is dated Oct 30. The window has 12 days (Nov 1–2 are a weekend; ~8 business days Nov 3–12). In October, the 12-day span Oct 19–30 produced 3 Brown entries (Oct 19, 20, 30); September produced 0 (the Sept 21 committee order, Sept 29 Council order, Oct 5 and Oct 16 orders were not posted as news). The scale is 0, 1, 2, 3, 4, 5+ (top bin open).

### Outside view

No clean reference class. Closest: the court's own posting record on this matter, which is bursty and event-driven: 0 posts in the first ~4 weeks of the matter (Sept 21–Oct 18), then 3 in 12 days once the Council chose "transparency" (Oct 19) — about 3 posts in 6 weeks overall, or 0.5/week, which gives ~0.85 expected posts in 12 days. Federal Circuit's Newman matter: committee report to Council order took ~6–7 weeks each time (2023: Jul 31 → Sep 20; 2024: Jul 24 → Sep 6), so a Council order inside the window is unlikely even if a report is filed quickly. Status quo (quiet) is the single most likely bin, but not a majority.

### Inside view

Drivers up: Brown defied the Oct 27 written-question deadline and Oct 30 interview; the Oct 20 order says the committee "must proceed" to file its report without her response; the committee also warned it may expand the investigation (a new order, which the court would likely post as it did Oct 20/30); Brown publicises (emails to ~140 people) which may provoke further public statements. Drivers down: § 360 confidentiality covers the report itself; the Sept orders went unposted, so posting seems keyed to Brown's own disclosures and to transparency choices; Council deliberation and a Council order likely take weeks; 3-month assignment bar runs to ~Dec 29, so no deadline forces action in the window. No public date for the report or a Council meeting was found. I put P(0) ≈ 40%, P(1) ≈ 28%, P(2) ≈ 14%, P(3) ≈ 8%, P(4) ≈ 4%, P(5+) ≈ 6%... expected count ≈ 1.2 with a fat right tail (a report plus Council order plus statements plus orders on scope expansion).

### Evidence

- Court listing, Nov 2026: "No matching items" (accessed 2026-11-03) [1].
- Court listing, Oct 2026: six entries, three Brown (Oct 19 Statement of Judicial Council; Oct 20 Special Committee Order in 05-26-90196; Oct 30 Special Committee Order and Transcript in 90177 & 90196); Sept 2026 listing: no Brown entries [1][2].
- Question text: Brown declined the Oct 17 interview, did not answer by Oct 27, did not appear Oct 30; committee warned it would file its report without her [3][4].
- Search (Nov 3): no reporting dated November on any report, Council order or further committee step [4][5].
- Newman precedent: committee report → Council order ~6–7 weeks [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-03 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-03 | no market on this matter |

### What would change my mind

A dated announcement of the committee's report filing or a Council meeting in the window (would push toward 2–4); evidence that the court posts every order in the matter as a News item (up); or that the Oct 30 transcript order stated the investigation was concluded and the report is confidential (more mass on 0–1).

### Sources

1. https://www.ca5.uscourts.gov/news?month=11&year=2026 (accessed 2026-11-03)
2. https://www.ca5.uscourts.gov/news (and ?month=10 / ?month=9) (accessed 2026-11-03)
3. https://news.bloomberglaw.com/us-law-week/judge-brown-emailed-sealed-court-papers-to-about-140-people (accessed 2026-11-03)
4. https://hotair.com/ed-morrissey/2026/10/30/federal-judge-ordered-to-seek-psychiatric-assessment-after-wild-racist-rants-n3820510 (accessed 2026-11-03)
5. https://dallasexpress.com/state/fifth-circuit-council-orders-psychiatric-exam-in-probe-of-dallas-judge-ada-brown/ (accessed 2026-11-03)
6. https://ipwatchdog.com/2023/09/20/disgraceful-insulting-decision-judicial-council-officially-suspends-newman-one-year-claiming-serious-misconduct/ (accessed 2026-11-03)

**Question**: [How many Fifth Circuit news announcements concerning the Judge Ada Brown misconduct proceeding will be dated November 1–12, 2026?](https://www.metaculus.com/questions/46419/)
**Date**: 2026-11-03
**Forecast**: Median 1 announcements, IQR [0, 2] announcements
**Thesis**: The court's Brown postings are bursty (0 in Sept, 3 in Oct 19–30) and the Nov listing is empty on Nov 3; a committee report or scope-expansion order after Brown's Oct 30 no-show could add posts, but § 360 confidentiality and slow Council timing (Newman: 6–7 weeks) favour 0–2. Most sensitive to whether the court posts the committee's next order.
