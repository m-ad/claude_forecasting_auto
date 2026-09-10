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

---

# v2 — Re-analysis — 2026-09-10

## Access failure that bounds this version

`metaculus.com` served a Cloudflare **managed challenge** (`HTTP 403`, `cf-mitigated: challenge`,
`server: cloudflare`, "Just a moment..." interstitial) to every access path tried:

| Path | Attempts | Result |
|---|---|---|
| `.claude/skills/metaculus-aggregations/scripts/metaculus_aggregations.py 45230 --comments 12 --history --json` | 5 | `RuntimeError: No aggregation JSON for post 45230 (last status 403)` |
| `.claude/skills/metaculus-scraper/scripts/metaculus_scrape.py` (fallback) | 2 | venv Playwright pins browser build 1234; only 1194 is installed. With the executable path patched, `page.goto` → `net::ERR_CONNECTION_RESET` when Chromium was given the proxy explicitly |
| plain `curl` on `/questions/45230/` and `/api/posts/45230/` | 2 | 403, `cf-mitigated: challenge` |

**Not retrieved**: CP (first reveal was due 2026-09-08T17:00Z), Pro, gold medalists, forecaster
count, and the comment thread — including whether admins answered ChaosCondensate's 2026-09-04
clarification request. Recorded in `raw/metaculus-2026-09-10-FETCH-FAILED.json`.

Consequence: two of eight v1 tripwires are unverifiable, and v2 stays unanchored to the community.
`next_review` is one week, not two, so the fetch can be re-attempted early.

Wikipedia was reachable via the MediaWiki `action=parse` API and carried most of the load instead.
`ukmto.org` also returns 403 to this container; JMIC content came from the search index.

## What changed the number

### 1. The US strike log — the decisive negative finding

Wikipedia's "List of ships attacked by the United States" [2], cross-read against CENTCOM reporting,
gives locations for every named engagement:

| Vessel | Date | Location |
|---|---|---|
| *Touska* | 19 Apr | northern Arabian Sea (USS *Spruance*) |
| *Deep Sea*, *Sevin* | Apr | off Malaysia |
| *Dorena*, *Derya* | Apr | off India |
| two unnamed | Apr | Indian Ocean |
| unnamed tanker | 24 Apr | Persian Gulf (USS *Rafael Peralta*) |
| *Sevan* | 25 Apr | Arabian Sea (USS *Pinckney*) |
| *Lian Star* | 30 May | Gulf of Oman |
| *Marivex* | 8 Jun | Gulf of Oman |
| *Jalveer* | 11 Jun | Gulf of Oman (2× Hellfire) |
| *Belma* | 15 Jul | Persian Gulf |
| *Lavine* | 24 Jul | (disabled) |
| *Downy* | 5 Sep | near Kharg Island |
| *Stark 1* | 5 Sep | near Jask |
| *Kylo* | 5 Sep | Gulf of Oman |

**Zero inside Omani territorial waters.** Meanwhile the *Iranian* attack log is full of precise
Omani-water positions: 5 nm north of Khasab, 52 nm off Muscat, 8 nm northeast of Limah, 7.5 nm
southeast of Dahit, "the Omani side of the Strait" (*Kavomaleas*, *Acheloos*, 20 Jul), 4 nm from the
Omani coast (*Senegal Prosperity*, 30 Aug, JMIC Update 092) [3,6].

This kills v1's `P(engagement inside the belt) = 0.75`. Replaced by a Jeffreys/Poisson rate on the
observed record — 0 events in ~5.0 months of US operations in the strait, λ ≈ 0.10/mo,
P(≥1 in 3.7 mo) ≈ 31%, ×0.65 for the traffic collapse → **≈ 0.21**.

**Trap named**: "Gulf of Oman" ≠ Omani territorial waters. Three of this week's US strikes are
headlined "in the Gulf of Oman" and none is in the 12-nm belt. This is the mirror image of v1's
warning (Iranian strikes on Oman misread as American) and it cuts the other way.

### 2. Operation Project Freedom is not what v1 described

Wikipedia's infobox: **date 4–5 May 2026 (1 day), outcome "Temporarily halted"** [4]. Trump paused
it on 5 May; the NYT read is that Saudi Arabia had denied the US its bases and airspace over it.
Hegseth said in mid-June "Project Freedom never stopped, and we've run 125 million barrels of oil
through the straits", so it is not dead — but Lloyd's List reports owners and insurers said it never
gave "sufficient clarity or credible protection to justify resuming transits".

The JMIC "enhanced security area" is real and *is* inside Omani territorial waters: JMIC Advisory
Note 004-26 of 4 May placed it south of the Traffic Separation Scheme, advising coordination with
Omani authorities on VHF 16 [5]. The geometry was right in v1; the event rate it was supposed to
imply was not.

### 3. Traffic collapse

| Metric | Value | As of | Source |
|---|---|---|---|
| PortWatch transits through the strait | **6** (vs 85/day pre-crisis) | 2026-08-30 | Straits Daily Brief [10] |
| Commodity ships/day, trailing 10 days | ~10, lowest since May | ~2026-09-07 | shipping data via ABC [11] |
| Large ships since early September | none | 2026-09-08 | Kpler via [2] |
| Missile strikes in the strait, 6 Jul – early Sep | 27 | 2026-09-07 | Kpler via [2] |

Almost nothing is left in the corridor for a US warship to escort.

### 4. Oman consents to Western naval activity in its waters

- **4 Jul**: the UK and France state Oman has committed to work with them on safe navigation through
  its territorial waters; Iran warns them off [3].
- **25 Aug**: US officials confirm the US Navy cleared >100 suspected mines from the Traffic
  Separation Scheme — "Oman's primary maritime corridor with Iran" — with underwater drones and
  private contractors detonating them [3].

Explosive US activity inside Omani territorial waters, with consent, that nobody has called an
attack on Oman. The consent carve-out is already operating in the world, whatever the admins rule.

### 5. The named trigger fired twice more and drew nothing

- 17 Aug: Iran states it reached an agreement with Oman on Hormuz traffic.
- 26 Aug: IRGC announces Iran–Oman deals on the Hormuz "share and its revenue"; the joint statement
  asserts sovereignty over territorial waters and sets up a foreign-ministry working group [13].
- The route: **outbound through a southern lane in Omani waters coordinated with Iran**, inbound
  through Iranian waters [13].
- US response through 10 Sep: none. Critical Threats' 7 Sep Iran Update does not mention Oman once [8].

### 6. Escalation — the one upward driver

- 5 Sep: IRGC Aerospace Force fires ballistic missiles at a US carrier and a destroyer (missed); US
  destroys/disables three Iranian tankers in response [8,9].
- 6 Sep: Iran's SNSC secretary Rezaei announces a "restricted maritime zone" from the US blockade
  line through the strait into the Persian Gulf [7,8].
- Trump: "we will have to hit them very hard" over activity at Pickaxe Mountain [7].
- 9 Sep: *Hercules Star* (1 dead, 1 missing) and *New Andros* attacked by Iran [2].

Raises the accident hazard — which is why that path was held near its v1 value rather than decayed —
without creating a path to a deliberate strike on Muscat.

## Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-09-10 | `metaculus_aggregations.py 45230` ×5, `metaculus_scrape.py` ×2, `curl` ×2 | Cloudflare managed challenge, 403 everywhere | **blocks two tripwires** |
| 2026-09-10 | Wikipedia `action=parse` — "2026 Strait of Hormuz crisis" | Sept timeline; US-attacked-ships table with locations; Kpler traffic numbers | ↓↓ the literal path |
| 2026-09-10 | Wikipedia `action=parse` — "Operation Project Freedom" | 1-day op, paused 5 May; Saudi denied bases; Lloyd's List on non-resumption; Hegseth "never stopped" | ↓ v1's central mechanism |
| 2026-09-10 | Wikipedia `action=parse` — "2026 Iranian strikes on Oman" | 4 Jul UK/France navigation commitment; 25 Aug US mine clearance in Oman's corridor; precise Omani-water positions for Iranian attacks | ↓ (consent) / ↑ (locatability) |
| 2026-09-10 | Search — JMIC/UKMTO "enhanced security area" | Advisory Note 004-26 (4 May): area south of the TSS, **inside Omani territorial waters**, VHF 16 coordination with Oman | confirms v1's geometry |
| 2026-09-10 | Search — JMIC Update 092 (1 Sep) | Threat level SEVERE; *Senegal Prosperity* attacked 30 Aug "4 nm from the coast of Oman" | ↑ locatability |
| 2026-09-10 | Critical Threats — Iran Update, 7 Sep | 5 Sep IRGC BMs at US carrier + US strikes on 3 tankers; 6 Sep Iranian "restricted zone"; 7 Sep Jizan refinery. **No mention of Oman** | ↑ intensity, ↓ Oman salience |
| 2026-09-10 | Straits Daily Brief, 8 Sep | PortWatch: 6 transits on 2026-08-30 vs 85/day baseline | ↓ escort exposure |
| 2026-09-10 | Al Jazeera 26 Aug + Oman MFA joint statement | Iran–Oman temporary route: outbound southern lane in Omani waters coordinated with Iran; sovereignty language; joint working group | ↓ deliberate path |
| 2026-09-10 | Search — Duqm/Salalah access agreement Sept 2026 | 2019 agreement still in effect; no restriction. Saudi Arabia and Kuwait restricted US access on 7 May, not Oman | ↓ obstruction path |
| 2026-09-10 | Search — Polymarket, Kalshi, Manifold, Sentinel, GJOpen, INFER on US–Oman | still no market and no question anywhere | no anchor |
| 2026-09-10 | Search — Trump on Oman since 17 Aug | Nothing new beyond the 17 Aug threat and "we'd handle them very easily" | ↓ cheap talk |

## Arithmetic

```
Reading L:  P(engagement inside 12-nm belt) 0.21  ×  P(credibly located) 0.75  =  0.16
Reading I:  1 − (1−0.025)(1−0.045)(1−0.020)                                    =  0.088
P(YES)   =  0.12 × 0.16  +  0.88 × 0.088  =  0.019 + 0.077                     =  0.096
haircut  =  −0.9 pp (accident path routed to the no-consensus clause)
            −0.3 pp (residual contested-12-nm case)
→ 8.4%
```

## Open questions carried into v3

1. **Re-fetch Metaculus.** CP, Pro, gold, forecaster count, and the admin thread. Highest priority.
   If the CP is outside 4%–18%, re-analyse rather than nudge.
2. Does Iran enforce its 6 Sep "prohibited zone" against traffic in the southern (Omani) lane, and
   does the US escort against it? That restores the exposure mechanism v1 assumed.
3. Does the interim US–Iran–Oman agreement land, and do transits recover above ~40/day?
4. Any UKMTO/JMIC position inside 12 nm of the Omani coast for a *US* engagement.
5. Any US munition, errant or otherwise, on Omani soil — still zero after 6.4 months.
