# Research log — Who will be the 2026 Time Person of the Year?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolves on TIME's announcement (2025's pick, "The Architects of AI", was announced 2025-12-11;
  AP reported the 2026 reveal expected **2026-12-10** — unconfirmed by TIME).
- Multiple-choice options and the group-pick rule: see `forecast.md` digest (Metaculus text).
- Key edge case: **group / concept picks** (e.g. "Artemis II crew", "The Protester") — how they map to
  named options decides a large slice of probability.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Group / collective / concept picks | 9 of 25 (2002, 03, 05, 06, 11, 14, 17, 18, 25) | 2001–2025 | 36% | Wikipedia list; own tally | yes |
| Sitting US president in a midterm year | 0 of 6 (2002, 06, 10, 14, 18, 22) | 2002–2022 | ~0% (ever: rare outside war years — 1942 FDR) | Wikipedia | yes |
| US president / president-elect overall | 6 of 25 (2004, 08, 12, 16, 20, 24) — all in presidential-election years | 2001–2025 | 24%, but 0% in non-election years | Wikipedia | yes |
| Non-US head of state/government | 3 of 25 (Putin 07, Merkel 15, Zelensky 22) | 2001–2025 | 12% | Wikipedia | yes |
| Pope | 1 of 25 (Francis 2013, first year) | 2001–2025 | 4%; Leo XIV was passed over in his first year (2025) | Wikipedia | yes |
| Business / tech individual | 3 of 25 (Bernanke 09, Zuckerberg 10, Musk 21) | 2001–2025 | 12% | Wikipedia | yes |
| Culture / activist individual | 2 of 25 (Thunberg 19, Swift 23) | 2001–2025 | 8% | Wikipedia | yes |
| Sub-national US official | 1 of 25 (Giuliani 2001, 9/11) | 2001–2025 | 4% | Wikipedia | yes (Mamdani) |
| Repeat winner within 2 years | Trump 2016→2024 (8 y); Obama 08→12; none within 2 y since Nixon 71–72 | — | rare | Wikipedia | yes |

## Decomposition

2026's dominant stories (as of 2026-10-17): US–Israel war on Iran from 2026-02-28 (Ali Khamenei killed;
Mojtaba Khamenei successor; Hormuz closure, ceasefires on/off through July), Trump's tariff wars incl.
50% on Canadian goods (Carney's "middle powers" stance), Artemis II crewed lunar flyby (splashdown
2026-04-10), Mamdani's first year as NYC mayor and Democratic midterm surge (Dems ~85–90% to take the
House on 2026-11-03), AI (Anthropic/Amodei, OpenAI/Altman), World Cup 2026 in North America.
TIME's pattern in non-US-election years: often a group/concept or a symbol of a global theme.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-17 | Kalshi API KXTIME-26 (cached `raw/kalshi-2026-10-17.json`) | Mamdani 28/29¢ ($902K vol), Pope Leo 16/18, Carney 12/13, Amodei 7/8, Netanyahu 7/10, Trump 7/8, AI 6/7, Talarico 5/7; sum of mids 1.92 | power-normalised: Mamdani 21%, Leo 11%, Carney 7% |
| 2026-10-17 | Polymarket time-person-of-the-year-2026 ($132K) | Mamdani 28.5, Leo 16, Carney 14.5, Netanyahu 8, Amodei 7.4, Musk 6.5, Trump 6.5, AI 6.3 | agrees with Kalshi |
| 2026-10-17 | AP via WCAX/CTV 2026-09-30 "Carney's stand against Trump ... Time Person of the Year buzz" | Carney 2nd in markets; announcement Dec 10; Galloway endorsement | Carney up |
| 2026-10-17 | Kalshi News blog (earlier) | Trump 28 / Mamdani 20 / Leo 20 at an earlier date | Trump faded |
| 2026-10-17 | vinnews 2026-09-04, thelines, olbg | Mamdani leads since summer; 37¢ in late Aug | trend: Mamdani falling 37→29 |
| 2026-10-17 | casino.org / gamblingsite / covers | overround warning (37¢ ≈ 22% normalised) | supports normalisation |
| 2026-10-17 | NCR: Pope Leo on TIME100 2026 | prominence, Trump critic incl. on Iran deal | Leo modest |
| 2026-10-17 | Pope Leo "resignation" (predictionhunt 2026-07-20) | **false** — AP 2026-07-05 shows normal summer break; predictionhunt pages appear AI-generated | ignore predictionhunt |
| 2026-10-17 | Artemis II splashdown 2026-04-10 (NBC Palm Springs / NASA) | crew Wiseman, Glover, Koch, Hansen | group-pick candidate |
| 2026-10-17 | Iran war timeline (Iran International, Business Standard, Marine Insight) | war from Feb 28; ceasefire April; MoU June 17; Trump declares ceasefire over July 8 | Trump/Netanyahu/Mojtaba relevance |
| 2026-10-17 | Midterm forecasts (defirate, Action Network, Newsweek/Silver Bulletin) | Dems ~85–90% House, Senate ~50/50 | Democratic-figure tail (Mamdani, Talarico, Ossoff) |
| 2026-10-17 | Nobel Peace Prize 2026 (Khaleej Times, nobelprize.org) | awarded 2026-10-09 to Navi Pillay, not Carney | Carney: Nobel narrative gone, small − |
| 2026-10-17 | Israeli election (i24NEWS, Al Jazeera, Wikipedia polling page) | election 2026-10-27; Bennett–Lapid "Together", Eisenkot's Yashar; neither bloc at 61 in polls | Netanyahu tripwire |
| 2026-10-17 | Metaculus API (key) post 45729 | options: Dario Amodei, Artificial Intelligence, Astronaut(s), Mark Carney, Pope Leo XIV, Zohran Mamdani, Elon Musk, Benjamin Netanyahu, Jerome Powell, Marco Rubio, Donald Trump, Other; 9 forecasters pre-open | option map |
| 2026-10-17 | AP 2026-10 (hawaiitribune) | Mamdani Oct-7 statement controversy; campaigning for Dem candidates | — |

## Dead ends and ruled-out hypotheses

- No TIME shortlist yet (normally released ~1 day before announcement).
- Student-newspaper "Japanese macaque" rumour (via predictionhunt) — unverifiable, ignored.

## Open questions to chase next time

- Midterm results 2026-11-03 (a Democratic wave helps Mamdani/Talarico/AOC; a Talarico Senate win in
  Texas would be a TIME-sized story).
- TIME shortlist (~Dec 9) — historically the winner is on it.
- Any new war escalation / peace deal (Iran, Ukraine) in Nov.
