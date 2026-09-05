# Will the United States attack Oman before 2027?

| | |
|---|---|
| **Source** | Metaculus #45230 — https://www.metaculus.com/questions/45230/ |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-09-07 / 2026-11-01 / 2027-01-01 |
| **Status** | open |
| **Current forecast** | **Median 12.0%, IQR [7.0%, 19.0%]** (v1, 2026-09-05) |
| **Community (as of 2026-09-05)** | **not yet revealed** — status `upcoming`, CP reveal 2026-09-08T17:00Z (n=25 forecasters already in) |
| **Next review** | 2026-09-12 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-09-05

### What resolves YES

Before 2027-01-01, the United States carries out a military attack against **Oman's territory or
military forces**, **purposefully or accidentally**. Territory **includes territorial waters** —
which, in the Strait of Hormuz, means the entire southern half of the waterway out to 12 nautical
miles from the Musandam peninsula. The attack must **physically affect** Omani territory or forces:
cyber operations, and warning shots in international waters, do not count. Disputed attribution is
referred to credible sources and may resolve **ambiguous**; an incident with no credible-source
consensus that it happened inside Omani territory, and which neither Washington nor Muscat claims
happened there, does not count at all. Window: **117 days**.

**The load-bearing ambiguity is unresolved.** A clarification request filed on 2026-09-04 by user
*ChaosCondensate* — does a US strike on an *Iranian* vessel that credible sources place inside
Omani territorial waters count? — was still unanswered when I forecast. A second user, *tejvn*,
proposed a consent carve-out (attack on Omani territory without Omani consent → YES regardless of
target; with consent → NO). How admins answer is worth more to this forecast than any plausible
news event, because the US Navy has *deliberately routed the shipping it escorts into Omani
territorial waters* (see below). I therefore forecast a mixture over the two readings rather than
pretending the criteria are settled.

### Outside view

| Class | n | Window | Rate |
|---|---|---|---|
| **A** — US military attacks on a GCC state (Oman, Saudi Arabia, UAE, Qatar, Kuwait, Bahrain) | **0** | 1971–2026, 55 years | **~0** |
| **B (primary for the deliberate path)** — explicit public US-presidential threats to bomb a *non-adversary* state converting to an actual strike within ~6 months (Trump on Mexico/cartels, Denmark over Greenland, Nigeria, Oman ×2; historically "fire and fury" on North Korea) | ~6–8 | 2017–2026 | **~5–10%** |
| **C (upper bound)** — hazard rate implied by this war: **0 US attacks on Oman in 6.2 months** of maximum-intensity operations. Jeffreys/Poisson → λ ≈ 0.08/month → P(≥1 in 3.9 months) ≈ **27%** | — | Feb–Sep 2026 | 27% |
| **D** — errant/accidental US munitions physically affecting a partner state's territory during an air campaign | several | 2014–2026 | low, non-zero per campaign-quarter |

Class C is deliberately generous and should be treated as a ceiling: it assumes a homogeneous
hazard, whereas the risk here is concentrated in rhetorical spikes — and **the spike has already
passed without a strike**. Trump named a trigger ("if Oman gets in the way", specifically the
Iran–Oman strait deal); the trigger fired in August 2026; the response was a second threat, not a
bomb. That is direct evidence on the conversion rate of *these* threats, and it points down.

Class A is the dominant prior and it is stark: in 55 years the United States has attacked Iran,
Iraq, Libya, Syria, Yemen, Afghanistan, Somalia, Sudan and Serbia, and has never attacked a Gulf
Cooperation Council state.

### Inside view

The crucial structural fact, which the question's framing obscures: **the US and Oman are not
adversaries in this war — they are co-victims.** From 2026-03-01 Iran struck Duqm, Salalah, Sohar,
Bukha and Mina Al Fahal *and US military infrastructure inside Oman*, killing 14 Omanis and
injuring 35. The 2019 US access agreement covering Duqm and Salalah remains in effect. Oman is the
channel through which Washington talks to Tehran. Trump's grievance is that Oman is brokering a
Hormuz settlement that **excludes** the US and would legitimise Iranian control of a northern
corridor — a diplomatic affront, not a casus belli.

I therefore split on the reading:

**Reading L — literal.** Any US attack physically occurring inside Omani territory or territorial
waters counts, whatever the target and whoever consented.

- P(a US kinetic engagement occurs inside Omani territorial waters within 117 days) ≈ **0.75**.
  Under Operation Project Freedom (launched 2026-05-04, CENTCOM: destroyers, 100+ aircraft, 15,000
  personnel) the US Navy and the Joint Maritime Information Centre **directed all commercial
  traffic out of the traditional lanes and into Omani territorial waters**, an "enhanced security
  area", with warships positioned to respond to Iranian interference. Iran attacked ≥13 commercial
  vessels in August alone. US destroyers engaging those attackers are, geometrically, shooting
  inside Omani waters.
- P(credible sources place a specific incident inside the 12-nm line) ≈ **0.6**. Reporting says
  "off the coast of Oman", "northeast of Khasab", "Gulf of Oman"; explicit territorial-water
  attribution generally requires an Omani protest or a UKMTO/JMIC position report.
- → P(YES | L) ≈ **0.50**.
- **P(L adopted) ≈ 0.12.** The title, background and fine print are framed around US–Oman
  hostilities; "an attack **against** Oman's territory or military forces" reads target-directed;
  the consent carve-out is well-argued and Metaculus admins routinely adopt such proposals; and
  resolving *"Will the US attack Oman?"* YES because a US destroyer downed an Iranian drone over
  Omani water with Muscat's blessing would be a resolution almost everyone would call wrong.

**Reading I — intent.** The attack must be against Oman, or at minimum without Omani consent.

| Path | p |
|---|---|
| Deliberate US strike on Oman as coercion (Trump follows through) | 0.035 |
| Accidental US munition physically affecting Omani territory or forces — errant missile, an Omani patrol boat or fishing vessel hit during a strike on an Iranian craft, off-target ordnance on Musandam — reported and attributed | 0.05 |
| Oman actively obstructs (denies transit, enforces the Iran–Oman corridor against US escorts) and the US strikes Omani assets; **or** Oman publicly protests a specific US strike in its waters as an attack on Oman | 0.03 |

→ P(YES | I) = 1 − (0.965 × 0.95 × 0.97) = **0.111**

`P(YES) = 0.12 × 0.50 + 0.88 × 0.111 = 0.060 + 0.098 = 15.8%`

**−3 pp for the ambiguous sink.** The fine print offers "ambiguous" explicitly, and the incidents
most likely to be genuinely contested — a strike whose 12-nm status is disputed — are exactly the
ones that route to *ambiguous* rather than YES.

→ **12%**.

### Evidence

**Moving up.** Project Freedom is the single most important finding and it is not in the question's
background: the US Navy has *chosen* to conduct its escort mission inside Omani territorial waters.
Combined with an explicit "accidentally counts" clause and a shooting war that produced two US
strikes on ships in the Strait in the week of 1–4 September, this makes a physically-inside-Oman US
engagement close to a base case rather than a tail (LR ≈ 2.5 on the naïve "US doesn't attack
allies" view). Two presidential bombing threats in three months, with the second following the
expiry of a 60-day ultimatum, are a genuine escalation in rhetoric.

**Moving down, and moving me more.** Three things.

First, **six months of the most intense US military operations in the region since 2003 have
produced zero US attacks on Oman**, while producing many Iranian ones. CENTCOM's retaliatory
strikes are documented as hitting Iranian territory (Qeshm Island, Iranian military and
communications sites). Absence of expected evidence: if the US were drifting toward striking Oman,
I would expect at least a boundary incident, an Omani protest against Washington, or a suspension
of the Duqm/Salalah access agreement. None exists (LR ≈ 0.4).

Second, **the named trigger already fired.** Trump's condition was Oman "getting in the way" —
concretely, cutting a bilateral strait deal with Iran. Oman did that in August. The response was a
second verbal threat. Threats that survive their own trigger are cheap talk with high probability.

Third, **the incentives run hard against it.** Attacking Oman would cost the US its Duqm and
Salalah access, its only working channel to Tehran, and GCC cohesion, in exchange for nothing
militarily useful — Oman has no capability the US needs to destroy. Crisis Group's read on
2026-09-01 is that *neither* side wants a return to full-scale war and that the stalemate is
becoming unsustainable for both; oil transit rose to 5–7 mb/d in August. The trend is toward a
deal, not toward opening a second front against a partner.

**A misconception worth naming.** Headlines through 2026 read "Omani port hit by drones", "US
military assets in Oman targeted", "Salalah struck". Every one of those is **Iran** attacking Oman.
A forecaster who anchors on "Oman is being bombed" without checking attribution will be badly high.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | **not revealed** | 2026-09-05 | status `upcoming`; CP reveal 2026-09-08T17:00Z; 25 forecasters already submitted |
| Metaculus Pro | not revealed | 2026-09-05 | same |
| Metaculus gold medalists | not revealed | 2026-09-05 | same |
| Polymarket — *US attack on Oman* | **no such market** | 2026-09-05 | searched |
| Polymarket — US forces enter Iran by 2026-12-31 | ~90% | reported 2026 | ~$115M; confirms an intense, deep, but **Iran-focused** market |
| Polymarket — Hormuz traffic normal by 2026-04-30 / 05-31 | 11% / 33% | earlier 2026 | stale, quoted for context only |
| Polymarket — Iran–Oman Hormuz agreement announced by 2026-08-31 | 37% | late Aug 2026 | after a 47 pp weekly slide; the market did **not** treat an Oman–Iran deal as settled |
| Kalshi — Hormuz closure | $7.3M volume | 2026 | no Oman contract |
| Sentinel Team / GJOpen / INFER | nothing found on US–Oman | 2026-09-05 | searched |

**Cohort disagreement**: not assessable — all three Metaculus cohorts are hidden until 2026-09-08.
There is also **no market anywhere on this specific event**, despite >$200M of Iran-war prediction
volume. That absence is itself weak evidence that traders do not regard a US attack on Oman as a
live, tradeable proposition. My forecast is unanchored, which is why the IQR is wide.

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | **Stalemate or de-escalation.** US–Iran attrition continues or a deal emerges; Oman keeps mediating and keeps absorbing Iranian strikes; Trump keeps threatening; no US munition touches Oman. | 0.68 | NO |
| 2 | **Incidents occur but do not qualify.** US engagements happen inside or near Omani waters, but reporting stays at "off the coast of Oman", no Omani protest against Washington, and admins adopt the intent reading. | 0.14 | NO |
| 3 | **Literal reading + located incident.** Admins rule that any US attack inside the 12-nm line counts, and a strike is credibly placed there. | 0.06 | YES |
| 4 | **Accident.** An errant US munition, or a US strike on an Iranian craft, physically hits Omani territory, an Omani vessel, or Omani forces; attributed. | 0.04 | YES |
| 5 | **Oman obstructs → US strikes Omani assets**, or Muscat formally protests a US strike as an attack on Oman. | 0.02 | YES |
| 6 | **Ambiguous.** A contested incident that admins cannot resolve. | 0.03 | annulled/ambiguous (not YES) |
| 7 | **Trump follows through** — deliberate punitive strike on Oman. | 0.03 | YES |

YES = 0.06 + 0.04 + 0.02 + 0.03 = **0.15** gross; **0.12** after the ambiguity haircut applied
within scenarios 3–5.

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Admins adopt the intent/consent reading (P ≈ 0.88) | Admins adopt the literal "inside 12 nm counts regardless of target" reading | **~50%** |
| Admins adopt the intent reading | Admins explicitly rule that third-party strikes in Omani waters never count | **~9%** |
| Trump's threats are cheap talk (trigger already fired without a strike) | Oman formally blocks US escort transits or signs a defence understanding with Iran | **~30%** |
| The war continues at roughly current intensity | A US–Iran ceasefire holds from October | **~5%** |

### What would change my mind (tripwires)

- [ ] **Metaculus admins answer the 2026-09-04 clarification request** — by 2026-09-20 → literal ruling: up 38 pp; intent/consent ruling: down 3 pp. *Highest-leverage single event.*
- [ ] **US or Omani government, UKMTO or JMIC states that a US strike occurred inside Omani territorial waters** — by 2026-12-31 → up 35 pp
- [ ] **Oman formally protests a US military action** (foreign-ministry statement, ambassador summoned) — by 2026-12-31 → up 20 pp
- [ ] **Oman suspends or restricts the 2019 US access agreement (Duqm/Salalah), or denies US transit/overflight** — by 2026-11-30 → up 15 pp
- [ ] **A US–Iran ceasefire or Hormuz agreement is signed and holds ≥ 30 days** — by 2026-12-15 → down 7 pp
- [ ] **Operation Project Freedom formally ends or moves its escort corridor out of Omani waters** — by 2026-11-30 → down 5 pp
- [ ] **2026-10-31 passes with no reported US munition impact on Omani territory or forces** → down 4 pp (mechanical time decay)
- [ ] **Metaculus CP on reveal (2026-09-08) lands outside 5%–25%** → direction unknown; trigger a re-analysis, not a nudge

### Sources

1. Metaculus — question #45230, resolution criteria, fine print, background and comments — https://www.metaculus.com/questions/45230/ ; snapshot in `raw/metaculus-2026-09-05.json` (accessed 2026-09-05)
2. Wikipedia — "2026 Strait of Hormuz crisis" — https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis (accessed 2026-09-05)
3. Wikipedia — "2026 Iranian strikes on Oman" — https://en.wikipedia.org/wiki/2026_Iranian_strikes_on_Oman (accessed 2026-09-05)
4. Wikipedia — "Operation Project Freedom" — https://en.wikipedia.org/wiki/Operation_Project_Freedom (accessed 2026-09-05)
5. Wikipedia — "2026 United States naval blockade of Iran" — https://en.wikipedia.org/wiki/2026_United_States_naval_blockade_of_Iran (accessed 2026-09-05)
6. Al Jazeera — "Why has Trump threatened to bomb Oman – for a second time?" (18 Aug 2026) — https://www.aljazeera.com/news/2026/8/18/why-has-trump-threatened-to-bomb-oman-for-a-second-time (accessed 2026-09-05)
7. CNN — "Trump's threats anger Omanis, leave observers puzzled" (18 Aug 2026) — https://www.cnn.com/2026/08/18/middleeast/trumps-threats-anger-omanis-intl (accessed 2026-09-05, via search index)
8. CNN live blog — "Deadline to reach US-Iran deal expires, Trump threatens Oman" (17 Aug 2026) — https://www.cnn.com/2026/08/17/world/live-news/iran-war-trump (accessed 2026-09-05)
9. Washington Post — "Trump threatens to bomb Oman if it 'gets in the way'" (17 Aug 2026) — https://www.washingtonpost.com/world/2026/08/17/trump-threatens-bomb-oman-if-it-gets-way/ (accessed 2026-09-05)
10. CBS News live updates — "Trump threatens to bomb Oman with Iran war stuck in stalemate as 60-day negotiation period ends" — https://www.cbsnews.com/live-updates/us-iran-war-deal-expired-strait-of-hormuz/ (accessed 2026-09-05)
11. Fox News — Trump interview confirming the IRGC backchannel and the Oman remark (17 Aug 2026) — https://www.foxnews.com/world/trump-confirms-irgc-backchannel-calls-irans-white-flag-surrender (cited in the question background; accessed 2026-09-05)
12. CNN — Trump's May 2026 warning to Oman — https://edition.cnn.com/2026/05/27/world/live-news/iran-war-us-news#cmpoc4ge900003b6u9s3zjw35 (cited in the question background; accessed 2026-09-05)
13. USNI News — "U.S., Iran Trade Strikes in Strait of Hormuz as Both Battle on Social Media" (4 Sep 2026) — https://news.usni.org/2026/09/04/u-s-iran-trade-strikes-in-strait-of-hormuz-as-both-battle-on-social-media (accessed 2026-09-05; **direct fetch returned HTTP 403 — content from search index only**)
14. CNN — "The US wants to manage the stalemate in the Strait of Hormuz. Iran wants to break it" (4 Sep 2026) — https://www.cnn.com/2026/09/04/middleeast/us-iran-strait-of-hormuz-stalemate-intl (accessed 2026-09-05; **direct fetch returned HTTP 451 and archive.is is blocked in this sandbox — content from search index only**)
15. International Crisis Group — "Hormuz 1 September 2026" — https://www.crisisgroup.org/content/hormuz-1-september-2026-1 (accessed 2026-09-05)
16. Al Jazeera — "Ships attacked in the Strait of Hormuz: What that means for ongoing talks" (7 Jul 2026) — https://www.aljazeera.com/news/2026/7/7/ships-attacked-in-the-strait-of-hormuz-what-that-means-for-ongoing-talks (accessed 2026-09-05)
17. Al Jazeera — "US Embassy in Riyadh, Omani port hit by drones; US base in Bahrain targeted" (3 Mar 2026) — https://aljazeera.com/news/2026/3/3/us-embassy-in-saudi-capital-riyadh-hit-by-drones-fire-reported-ministry (accessed 2026-09-05)
18. Al Jazeera — "Oman renews push for diplomacy, says 'off-ramps available' in Iran war" (3 Mar 2026) — https://www.aljazeera.com/amp/news/2026/3/3/oman-calls-for-immediate-ceasefire-says-off-ramps (accessed 2026-09-05)
19. Jerusalem Post — "Trump's threats put Oman's balancing act under growing pressure" — https://www.jpost.com/middle-east/article-905795 (accessed 2026-09-05)
20. CNBC — "Ship attack in Hormuz kills crew member while Trump says strait is 'open and operating'" (18 Aug 2026) — https://www.cnbc.com/2026/08/18/iran-war-strait-hormuz-ship-traffic-oil.html (accessed 2026-09-05)
21. CNN — "'Project Freedom': Trump's plan to 'guide' ships through the Strait of Hormuz" (4 May 2026) — https://www.cnn.com/2026/05/04/middleeast/project-freedom-hormuz-guide-ships-intl-hnk-ml (accessed 2026-09-05)
22. The National — "Trump's 'Project Freedom': What we know" (4 May 2026) — https://www.thenationalnews.com/news/mena/2026/05/04/iran-warns-us-against-entering-strait-of-hormuz-amid-plan-to-guide-ships-out/ (accessed 2026-09-05)
23. Army Recognition — "Project Freedom Reveals How US Destroyers Would Protect Hormuz Shipping From Iranian Drones and Missiles" — https://www.armyrecognition.com/news/navy-news/2026/project-freedom-reveals-how-us-destroyers-would-protect-hormuz-shipping-from-iranian-drones-and-missiles (accessed 2026-09-05)
24. Congressional Research Service R45281 — "The Strait of Hormuz: Security Developments and Impacts on Oil, Gas, and Other Commodities" — https://www.congress.gov/crs-product/R45281 (accessed 2026-09-05; used for the territorial-waters geography of the strait)
25. ASPI Strategist — "How to lose friends and alienate allies: Trump's approach to Oman" — https://www.aspistrategist.org.au/how-to-lose-friends-and-alienate-allies-trumps-approach-to-oman/ (cited in the question background; accessed 2026-09-05)
26. Polymarket — Iran event pages and Iran–Oman Hormuz agreement contract — https://polymarket.com/iran (accessed 2026-09-05; no US-attacks-Oman market exists)

**Date**: 2026-09-05
**Forecast**: Median 12.0%, IQR [7.0%, 19.0%]
**Thesis**: The United States has never attacked a GCC state in 55 years, and six months of maximum-intensity war have produced many *Iranian* strikes on Oman — Duqm, Salalah, Sohar, 14 dead, plus US assets inside Oman — and zero American ones, while the trigger Trump named (an Iran–Oman strait deal) already fired in August and drew a second threat rather than a bomb [3,6,9]. The real live path is not Trump's rhetoric but geometry: Operation Project Freedom routes the shipping the US Navy escorts *through Omani territorial waters*, so US engagements physically inside Oman are likely, and the forecast is therefore dominated by an unanswered admin clarification — a literal "inside 12 nm counts" ruling would put this near 50%, an intent/consent ruling near 9% [1,4,21].
