# By 27 November 2026, will Maersk publicly state that personal data was accessed or disclosed in the IT security incident it announced on 11 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46586/ |
| **Tournament** | minibench — one shot, window 2026-11-16T12:43:42Z -> 2026-11-16T15:43:42Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | resolved |
| **Current forecast** | Median 10.0%, IQR [6.0%, 15.0%] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

YES if, by 27 November 2026, Maersk (or a Maersk spokesperson quoted by credible media) publicly says that personal data was accessed, extracted, disclosed or leaked in the incident it announced on 11 November. Personal data here means names, contact details, credentials, driver or employee records, or IMEIs. It counts even if Maersk calls the data old, low-risk or non-sensitive. A general "data extraction" or "we are investigating whether personal data was affected" does not count. Timeline: the statement came out on 11 Nov and today is 16 Nov, so 11 days are left. Whitearmor's 30-day ransom deadline (about 7 Dec, some outlets say ~10 Dec) falls **after** the cutoff, so the usual trigger of a leak dump is unlikely to come before 27 Nov. As of 16 Nov, the only official position is the 11 Nov line: "findings so far strongly suggest no sensitive data has been disclosed" [1][2].

### Outside view

The reference class is large companies that first say "no sensitive data" and are then hit by an extortion group's personal-data claim. Many of them do eventually admit that personal data was involved: Medibank, Yum! Brands, Lee Enterprises, Columbus, Casio and Advantest [6][7]. The admission usually comes 1–4 months later, after forensics and the legal notification clocks, or right after a leak forces it. Fewer than about 15% admit it within roughly 2.5 weeks of the first statement. My rough prior for an admission in this 16-day window is 12–15%.

### Inside view

- Maersk's wording is hedged. "Sensitive" is not the same as "personal", so a later "limited, non-sensitive personal data such as contact details" would count. That keeps the probability off the floor.
- Driver records, phone numbers and emails are plainly personal data. GDPR requires notifying the regulator within 72 hours, and individuals when the risk is high. But notifying the regulator is not public, and letters to individuals from a Hong Kong legacy unit may never reach credible media before 27 Nov.
- Five days in, there is no update, no named spokesperson, and BleepingComputer's questions are unanswered [1]. Maersk looks defensive (−5 pp).
- No samples have been published, and the leak countdown runs past the cutoff [4][5] (−3 pp). An early partial leak to pressure Maersk is possible but not the norm.
- Net: about 10%. The IQR is 6–15%, reflecting doubt about how literally the resolver will read "personal".

### Evidence

- 11 Nov 2026: Maersk confirms unauthorised access to and data extraction from a local legacy system of a previous acquisition. It says "no sensitive data has been disclosed" and that the incident is "isolated to a local system". It gives no data types and says customers will be informed "as more relevant information becomes available" [1][2].
- 10–11 Nov: Whitearmor claims about 100 GB from OCF/LF Logistics, including about 29k driver records, plaintext passwords and 27,842 device logs with phone numbers, emails and IMEIs. It demands $5M with a 30-day countdown. Nothing has been published [1][4][5].
- 12–14 Nov: coverage is commentary only, with no Maersk follow-up [8]. No statement from Datatilsynet (the Danish data protection authority) or Hong Kong's PCPD (privacy commissioner) was found.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-16 | |

### What would change my mind

- Whitearmor publishing driver or staff samples before 27 Nov. That would push Maersk to update and could raise this to 35–50%.
- Hong Kong or Asian press reporting that former LF Logistics drivers or staff received notification letters.
- On the other side, a Maersk update that repeats "no personal data" or stays silent past 20 Nov would take this toward 5%.

### Sources

1. BleepingComputer, "Maersk confirms data breach as WhiteArmor ransomware demands $5 million", https://bleepingcomputer.com/news/security/maersk-confirms-data-breach-as-whitearmor-ransomware-demands-5-million (accessed 2026-11-16)
2. The Register, "Shipping giant Maersk probes 'IT security incident,' data theft", https://www.theregister.com/a/5309096 (accessed 2026-11-16)
3. Maersk advisory, https://www.maersk.com/news/articles/2026/11/11/it-security-incident (accessed 2026-11-16; fetch failed, wording via [1][2])
4. Ingeniøren, https://ing.dk/artikel/maersk-ramt-af-datalaek-hackere-haevder-have-adgang-til-kundedata (accessed 2026-11-16)
5. Cybernews, https://cybernews.com/security/maersk-confirms-cyberattack-ransomware/ (snippet, accessed 2026-11-16)
6. SecurityWeek, Medibank admits customer data stolen, https://www.securityweek.com/australian-health-insurer-medibank-admits-customer-data-stolen-ransomware-attack/amp/ (snippet, accessed 2026-11-16)
7. CyberInsider, Lee Enterprises, https://cyberinsider.com/ransomware-attack-at-lee-enterprises-impacted-nearly-40000-individuals/ (snippet, accessed 2026-11-16)
8. Smart Maritime Network, https://smartmaritimenetwork.com/2026/11/12/maersk-investigates-data-breach-involving-legacy-it-system/ (snippet, accessed 2026-11-16)

**Question**: [By 27 November 2026, will Maersk publicly state that personal data was accessed or disclosed in the IT security incident it announced on 11 November 2026?](https://www.metaculus.com/questions/46586/)
**Date**: 2026-11-16
**Forecast**: Median 10.0%, IQR [6.0%, 15.0%]
**Thesis**: Companies that first say "no sensitive data" usually admit personal-data exposure only 1–4 months later, after forensics or a leak forces it. Here Maersk has said nothing since 11 Nov, and Whitearmor's leak deadline (~7 Dec) falls after the 27 Nov cutoff. The main upside risk is an early sample leak, or Maersk describing the data as "non-sensitive personal data".

## Resolution — 2026-11-28

Resolved **no** (synced from the Metaculus API). The bot's forecast was 10.0% [6.0%, 15.0%]. Official spot peer score: +23.74.
