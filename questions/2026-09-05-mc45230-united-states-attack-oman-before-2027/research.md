# Research log — Will the United States attack Oman before 2027?

## Question mechanics

- **Resolves YES** if, before 2027-01-01, the US carries out a military attack against Oman's
  **territory or military forces**, **purposefully or accidentally**.
- **Territory includes territorial waters** (12 nm — and in the Strait of Hormuz that is the
  entire southern half of the waterway).
- Must **physically affect** Oman's territory or forces. Cyberattacks, warning shots in
  international waters, non-physical actions: excluded.
- Disputed attribution → credible sources, or **ambiguous**. If there is no credible-source
  consensus that an incident occurred inside Omani territory, and neither the US nor Oman
  claims it did, that incident does not count.
- Window: 2026-09-05 → 2026-12-31 = **117 days**.

### The load-bearing ambiguity (unresolved as of 2026-09-05)

Metaculus user **ChaosCondensate** filed an admin clarification request on 2026-09-04, still
unanswered when the question opens on 2026-09-07:

> The Strait of Hormuz traffic separation lanes lie within Omani territorial waters (12 nm from
> Musandam). If US forces strike an Iranian vessel, a mine-laying craft, or a blockade-running
> merchant ship, and credible sources place that strike inside Omani territorial waters, does
> that count …?

**tejvn** proposed a consent carve-out: attacks on Omani territory *without Omani consent*
resolve YES regardless of target; *with* consent, NO.

This is not a footnote — it is most of the question. See the two-reading decomposition below.

## Situation as of 2026-09-05 (established facts)

| Date | Event |
|---|---|
| 2026-02-28 | US + Israel launch air war on Iran ("Operation Epic Fury" / "Roaring Lion"); Khamenei reported killed. IRGC blocks the Strait, mines it, attacks merchant shipping. ~25% of seaborne oil trade disrupted |
| 2026-03-01→ | **Iran** strikes **Oman**: drones/missiles on Duqm, Salalah, Sohar, Bukha, Mina Al Fahal, plus US military infrastructure *in Oman*. **14 killed, 35 injured** |
| 2026-03-14 | US orders non-essential staff out of Oman |
| 2026-04-13→05-29 | US naval blockade of Iranian ports |
| **2026-05-04/05** | **Operation Project Freedom**: CENTCOM escort operation — destroyers, 100+ aircraft, 15,000 personnel. **The US Navy / JMIC directs all commercial traffic out of the traditional lanes and into Omani territorial waters**, an "enhanced security area", with warships positioned to respond to Iranian interference |
| 2026-05-27 | Trump: Oman "will behave just like everybody else or we'll have to blow 'em up" |
| 2026-06-17 | MoU signed; hostilities resume after |
| 2026-07-08 | Ceasefire collapses; Iran attacks commercial vessels to assert sovereignty over the strait |
| 2026-08 | Iran strikes ≥13 commercial vessels; 2 seafarers killed. Iran–Oman reach an understanding on a new shipping route / dual-corridor scheme (south = Omani waters, free; north = Iranian waters, Iranian approval) |
| **2026-08-17** | 60-day negotiation window expires with no deal. Trump to Fox News: **"If Oman gets in the way, we'll bomb the s--- out of them."** |
| 2026-09-01→04 | US resumes strikes on Iranian targets in the Strait, including **two unidentified ships**. Crisis Group: neither side wants full-scale war; the stalemate is "increasingly unsustainable" for both. ~5–7 mb/d transiting in August, trending up |

**The two states are not adversaries.** Oman is a US treaty-level partner (2019 access agreement
covering Duqm and Salalah remains in effect, free trade agreement, S&T agreement), Iran has been
bombing Oman and US assets in Oman, and Oman is the channel through which the US talks to Tehran.
Trump's grievance is that Oman is brokering a Hormuz settlement that **excludes** the US and
would let Iran legitimise control of the northern corridor — not that Oman is hostile.

## Reference classes considered

| Class | n | Window | Base rate | Kept? |
|---|---|---|---|---|
| A. US military attacks on a GCC state (Oman, Saudi, UAE, Qatar, Kuwait, Bahrain) | 0 | 1971–2026 (55 y) | **~0** | kept — this is the dominant prior |
| B. Explicit, public US-presidential threats to bomb a **non-adversary** state converting to an actual strike within ~6 months (Trump: Mexico/cartels, Denmark/Greenland, Nigeria, Oman ×2; historically N. Korea "fire and fury") | ~6–8 | 2017–2026 | **~5–10%** | kept — primary for the deliberate path |
| C. Hazard rate of a US attack on Oman during this war: 0 events in 6.2 months of maximum-intensity operations. Jeffreys/Poisson → λ ≈ 0.5/6.2 = 0.08/mo → P(≥1 in 3.9 mo) ≈ 27% | — | Feb–Sep 2026 | ~27% | kept as an **upper** bound; over-generous because it treats the process as homogeneous, when the risk is concentrated in rhetoric spikes — and the Aug-17 spike has already passed without action |
| D. Accidental/errant US munitions physically affecting a partner state's territory during an air campaign (e.g. friendly-fire and off-target incidents in Syria, Iraq, Yemen ops) | several | 2014–2026 | low but non-zero per campaign-quarter | kept for the accident path |

**Key negative observation**: the trigger Trump named — an Oman–Iran deal on the strait — has
already *fired* (August 2026) and produced a threat, not a strike. That is direct evidence on the
conversion rate of these particular threats, and it points down.

## Decomposition — the two readings

`P(YES) = P(literal) × P(YES | literal) + P(intent) × P(YES | intent)`

**Reading L (literal)**: any US attack physically occurring inside Omani territory/territorial
waters counts, regardless of target or consent.
- `P(a US kinetic engagement occurs inside Omani territorial waters in 117 days)` — **high, ~0.75**.
  The US has deliberately routed the shipping it escorts into Omani waters, Iran attacks that
  shipping, and US destroyers engage the attackers there.
- `P(credible-source consensus places it inside the 12-nm line)` ≈ **0.6**. Reporting says
  "off the coast of Oman", "northeast of Khasab", "Gulf of Oman"; explicit territorial-water
  attribution usually requires an Omani protest or a US/UKMTO/JMIC position report.
- → `P(YES | L) ≈ 0.75 × 0.6 ≈ 0.45–0.60`. Take **0.50**.
- `P(L adopted)` ≈ **0.12**. Against it: the title, background and fine print are all framed
  around US–Oman hostilities; the phrase "attack **against** Oman's territory or military forces"
  reads target-directed; tejvn's consent carve-out is well-argued and Metaculus admins routinely
  adopt such proposals; and resolving "Will the US attack Oman?" YES because a US destroyer shot
  down an Iranian drone over Omani water with Oman's blessing would be seen as a bad resolution.

**Reading I (intent)**: the attack must be against Oman, or at least without Omani consent.
- Deliberate US strike on Oman as a coercive act: **0.035** (class A ≈ 0, class B ≈ 5–10%,
  discounted because the named trigger already fired without a strike, because Oman hosts US
  access the US would lose, and because attacking Oman destroys the only channel to Tehran).
- Accidental US munition physically affecting Omani territory or forces (errant missile, an Omani
  patrol boat or fishing vessel hit during a strike on an Iranian craft, off-target ordnance on
  Musandam), reported and attributed: **0.05**. Note US *intercepts* over Oman producing falling
  debris should not count — an intercept is not an attack against Oman.
- Oman actively obstructs (denies transit, enforces the Iran–Oman corridor against US escorts) →
  US strikes Omani assets, or Oman publicly protests a US strike in its waters as an attack:
  **0.03**.
- → `P(YES | I) = 1 − (0.965 × 0.95 × 0.97) ≈ **0.111**`.

`P(YES) = 0.12 × 0.50 + 0.88 × 0.111 = 0.060 + 0.098 = **0.158**`

Haircut: **−3 pp** for the ambiguous-resolution sink. The fine print offers "ambiguous" explicitly,
and the most likely genuinely-contested incidents (a strike whose 12-nm status is disputed) are
exactly the ones that route to ambiguous rather than YES.

→ **≈ 12%**.

## Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-09-05 | Metaculus #45230 JSON | Status `upcoming`, CP hidden until 2026-09-08T17:00Z, 25 forecasters already in; 3 comments, all about the territorial-waters ambiguity | frames the whole analysis |
| 2026-09-05 | Wikipedia "2026 Strait of Hormuz crisis" | War from 2026-02-28; Iran mines/blocks the strait; US blockade Apr–May; Project Freedom from May 4; MoU June 17; hostilities resume. CENTCOM retaliatory strikes named as on **Iranian** territory (Qeshm Island), not Omani | ↓ six months, no US strike on Oman |
| 2026-09-05 | Wikipedia "2026 Iranian strikes on Oman" | **Iran** struck Duqm, Salalah, Sohar and US military infrastructure in Oman from 2026-03-01; 14 dead, 35 injured; US ordered non-essential staff out 03-14; 2019 Duqm/Salalah access agreement still in effect; "The US did **not** strike Omani territory" | ↓↓ decisive: Oman is a co-victim of Iran, not a US target |
| 2026-09-05 | Wikipedia / CNN / The National / army-recognition on **Project Freedom** | **US Navy directs commercial traffic into Omani territorial waters** ("enhanced security area"), destroyers positioned to respond to Iranian interference | ↑↑ makes a US kinetic engagement *inside Omani waters* likely — the whole Reading-L path |
| 2026-09-05 | Al Jazeera 2026-08-18 "Why has Trump threatened to bomb Oman – for a second time?" | Grievance = Iran–Oman bilateral Hormuz deal excluding the US, plus transit tolls; "strong ties, multiple cooperation treaties"; Iran has struck US assets in Oman. **No analyst puts a probability on an actual US attack** | ↓ threat is about exclusion from a deal, not hostility |
| 2026-09-05 | CNN 2026-08-17 / 08-18, Washington Post 2026-08-17, CBS live blog | Trump: "If Oman gets in the way, we'll bomb the s--- out of them"; 60-day window expired; Omanis angered, observers "puzzled" | ↑ rhetoric, ↓ substance |
| 2026-09-05 | JPost analysis "Trump's threats put Oman's balancing act under growing pressure" | Oman "not appeared fazed"; continues mediating; hardening critical infrastructure | ↓ no Omani behaviour change that would trigger the threat |
| 2026-09-05 | USNI News 2026-09-04 (403 to fetch; read via search index) | US and Iran trading strikes in the Strait this week, incl. two unidentified ships. **Locations not specified** | either — the exact kind of incident whose 12-nm status decides this question |
| 2026-09-05 | CNN 2026-09-04 (451 to fetch; archive.is blocked in this sandbox; read via search index) + Crisis Group "Hormuz 1 September 2026" | Neither side wants full-scale war; stalemate "increasingly unsustainable"; ~5–7 mb/d transiting in August, trending up | ↓ mild de-escalation trend |
| 2026-09-05 | Polymarket / Kalshi search | **No market on a US attack on Oman.** Adjacent: "US forces enter Iran by Dec 31" ~90% ($115M); Hormuz-normalisation 11% by Apr 30; Iran–Oman Hormuz agreement 37% (late Aug, after a 47 pp weekly slide) | no direct anchor; confirms an intense but Iran-focused market |
| 2026-09-05 | Search: Sentinel Team, GJOpen, INFER on US–Oman | nothing found | — |

## Dead ends and ruled-out hypotheses

- **"Oman was attacked, so this may resolve YES."** Oman *has* been attacked repeatedly in 2026 —
  by **Iran**. Attribution is the whole question. Anyone skimming "Omani port hit by drones"
  headlines will be far too high.
- **US intercepts over Oman producing debris**: an air-defence intercept is not "a military attack
  against Oman's territory". Ruled out as a YES path.
- **Warning shots / cyber**: explicitly excluded by fine print.
- Aggregator sites (hormuzstraitmonitor.com, needsomefun.net, alexa.ng, global-political-spotlight)
  surfaced in search and were used only where corroborated by Wikipedia, CNN, Al Jazeera, WaPo,
  USNI or Crisis Group.
- Direct fetches of USNI (403) and CNN (451) failed; archive.is is blocked in this sandbox. Those
  two items rest on search-index snippets and are flagged as such in the source list.

## Open questions to chase next time

1. **Did Metaculus admins answer ChaosCondensate's clarification request, and how?** This is worth
   more than any news event. A literal ruling roughly quadruples the forecast.
2. Has any US strike been credibly located inside the 12-nm Omani limit (UKMTO/JMIC position
   reports, Omani foreign-ministry statements)?
3. Has Oman formally protested any *US* action, as opposed to Iranian ones?
4. Is the Iran–Oman corridor agreement formalised, and does the US move to obstruct it?
5. Does Project Freedom resume at full tempo, and does the escort corridor stay inside Omani waters?
