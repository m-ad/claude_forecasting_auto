# Research log — Will José Mourinho still be the manager for Real Madrid on December 31, 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: none named. Club announcements and press. YES requires Mourinho to be
  manager *continuously* from the question opening (2026-10-06 17:00 UTC) to 2026-12-31 12:00 UTC.
- Release schedule / cutoff: the event can happen any day. Closes 2026-12-01, resolves 2026-12-31.
- Access note: on 2026-10-05 the official API (bot key) returned `description` /
  `resolution_criteria` / `fine_print` = null because the question was "upcoming". The browser
  path (`_Fetcher.get_json('/api-proxy/posts/45857/')`) returned the full text. Cached in
  `raw/question-text-2026-10-05.json`. The aggregations JSON has no CP yet (reveal 2026-10-10 17:00 UTC).
- Edge cases: touchline bans and illness do not count as a break (my reading). A dismissal
  announced before Dec 31 but effective later is probably NO. Pérez often sacks in January
  (Benítez 4 Jan 2016, Alonso 12 Jan 2026), and January exits fall outside the window.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Manager in post ~Oct 5 leaves before Dec 31, Real Madrid seasons 2000-01…2025-26 | 26 | 2000–2025 | 4/26 = 15% exit | Wikipedia list of RM managers | yes |
| First-season summer hires still in post early Oct, exit before Dec 31 | 10 | 2003–2025 | 1/10 = 10% exit | same | yes |
| Mourinho's career: in-season sackings | 5 | 2007–2025 | all in season 2–3 at the club (Fenerbahçe in Aug of season 2) | Wikipedia José Mourinho | qualitative |

Exits in class A: García Remón 30-12-2004, Luxemburgo 4-12-2005, Schuster 9-12-2008, Lopetegui 29-10-2018.
Near-misses: Benítez 4-1-2016, Alonso 12-1-2026, Solari 11-3-2019.

## Decomposition

NO = P(crisis) 0.30 × P(act before Dec 31 | crisis) 0.35 + other exits 0.02 + no-crisis sacking 0.005 ≈ 0.13.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-05 | Wikipedia 2026–27 RM season | 8 games: 6W 2L; 4th, 15 pts from 7; contract to 30 Jun 2029 | baseline |
| 2026-10-05 | laliga.com standings | MD8 pending: Barça 21, Atleti 16, Betis 16, RM 15 | slight ↓ |
| 2026-10-05 | Goal 17 Sep "loses battle with dressing room" (citing Sport) | narrative of player power; no sacking talk | LR ~1.2 toward NO |
| 2026-10-05 | beIN 22 Sep (Vinícius), FootballTransfers Sep | form/structure problems | small ↓ |
| 2026-10-05 | Pérez re-election June 2026 (65%), "firm intention" to hire Mourinho | high political cost of an early sacking | ↑ |
| 2026-10-05 | ESPN: first Clásico 25 Oct at Camp Nou (MD10) | main risk date | — |
| 2026-10-05 | RM official: UCL MD2 Roma away 14 Oct; Villarreal home after the break | schedule | — |
| 2026-10-05 | bettingodds.com sack race; Polymarket next RM manager | no live odds on Mourinho leaving | none |
| 2026-10-05 | "Barcelona 7-0 Real Madrid Oct 4" (ESPN) | **women's Liga F** match, irrelevant | ruled out |

## Dead ends and ruled-out hypotheses

- The ESPN "Barcelona 7–0 Real Madrid (Oct 4, 2026)" result is the women's team (Liga F). Not relevant.
- A search summary claiming "RM beat Villarreal 3–1 on Oct 4" mixed in the 2025 fixture. The
  Villarreal game is the first one after the merged Sept/Oct international window.
- BBC (fetch blocked), Managing Madrid (403).

## Open questions to chase next time

- Metaculus CP / Pro / gold after reveal (2026-10-10).
- Results vs Villarreal (~Oct 10), Roma (Oct 14), Clásico (Oct 25). Gap to the leader after MD10.
- Any Spanish press (Marca, AS, El País, The Athletic) on Pérez's patience or on candidates being sounded out.

---

## 2026-10-12 — v2 update

Metaculus: browser path Cloudflare-blocked (403); bot-key API only (`raw/metaculus-api-2026-10-12.json`):
status open, n=70, criteria unchanged, fine print empty, aggregations hidden. No CP/Pro/gold today.

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-12 | Wikipedia 2026–27 RM season; ESPN report | W 1–0 Villarreal 10 Oct (Diomande 62'); Vinícius red 72'; 18 pts | → |
| 2026-10-12 | laliga.com standings | MD8: Barça 24, Atleti 19, Betis 19, RM 18; gap still 6 | → |
| 2026-10-12 | Mundiario 8 Oct | dressing-room order "not yet imposed"; Tchouaméni–Valverde feud patched | small ↓ |
| 2026-10-12 | beIN 9 Oct; Yahoo/Marca | Mourinho backs Vinícius publicly; Marca says patience with Vini near limit | small ↓ |
| 2026-10-12 | EN/ES searches "Pérez patience/destitución/sustituto Mourinho" | nothing on board weighing dismissal | ↑ (absence) |
| 2026-10-12 | Manifold API search | Prop bets: "Mourinho sacked before end of season" 24% (15 traders, M$844) | consistent; discounted |
| 2026-10-12 | Polymarket gamma public-search "Mourinho" | only closed markets | none |
| 2026-10-12 | Kalshi events API | no matching market | none |
| 2026-10-12 | sack-race odds search | only 2018–19 PL pages | none |

Dead ends: a laopinion.com "Mourinho ordena silencio" result is from March 2012, not relevant.

Next time: Metaculus CP/Pro/gold if the browser path works; results vs Roma, Sevilla, Leipzig and
Barcelona (25 Oct); Vinícius suspension length; any Pérez statement.
