# 🛡️ CyberBrief

**A free, open-source daily cybersecurity briefing — ranked by real-world urgency, explained for humans.**

Staying current in security is a firehose problem: dozens of feeds, hundreds of CVEs, and no signal about what actually matters *today*. CyberBrief solves the prioritization problem the way practitioners do:

> **CISA KEV** (is it being exploited right now?) → **EPSS** (how likely is exploitation soon?) → **CVSS** (how bad could it be?)

…and packages the result as a clean daily page, in plain English, with each story mapped to the **ISO/IEC 27001:2022 Annex A control** it relates to — so every headline doubles as a small GRC exercise.

**[📰 Read today's briefing →](https://manjou.github.io/cyberbrief/)**

## What it does

Every weekday morning, Mon-Fri (GitHub Actions, 05:30 UTC — no runs on weekends), CyberBrief:

1. Pulls the top security news feeds — The Hacker News, BleepingComputer, Krebs on Security, SANS ISC, Schneier, SecurityWeek, CERT-Bund
2. Pulls the **CISA Known Exploited Vulnerabilities** catalog and recent high-severity CVEs from **NVD**, enriched with **EPSS** exploit-probability scores
3. Ranks and dedupes everything with a transparent scoring model — **no AI required, zero dependencies, pure Python stdlib**
4. Publishes an HTML briefing (GitHub Pages) + Markdown version, with a jargon decoder for newcomers and ISO 27001 control tags on every story

Optionally, set an `ANTHROPIC_API_KEY` secret and each item gets a 2–3 sentence beginner-friendly explanation from Claude (one batched Haiku call ≈ a cent a day). If the AI call fails for any reason (bad/expired key, rate limit, outage), that's surfaced visibly on the page as "Sources unavailable this run" instead of silently degrading to raw feed text.

### Weekday themes

Each weekday has a focus, so no single day tries to cover everything:

| Day | Theme | Focus |
|-----|-------|-------|
| Mon | SOC | Active exploitation, incident response, threat activity |
| Tue | GRC | Breaches, regulation, compliance impact |
| Wed | Net+ | Network infrastructure — a lighter refresh day |
| Thu | SOC | Active exploitation, incident response, threat activity |
| Fri | GRC | Breaches, regulation, compliance impact |

Themes bias ranking toward the day's focus (see `cyberbrief/theme.py`) but never exclude everything else — a quiet day for one theme still fills out with the best overall stories, so the briefing is never empty. Edit `WEEKDAY_THEME` and `THEME_KEYWORDS` in `theme.py` to change the rotation or focus areas.

### 5pm recap

A second run at ~17:00 (15:00 UTC, Mon-Fri) adds a condensed one-line-per-story recap on top of the same page — no new fetching, no new AI cost, just a quick-scan summary of the exact same morning items, for anyone who didn't finish reading before then.

## Run it yourself

```bash
git clone https://github.com/manjou/cyberbrief
cd cyberbrief
python -m cyberbrief          # writes docs/index.html + docs/briefing.md
open docs/index.html
```

No pip install. No accounts. Python 3.10+ is the only requirement.

### Host your own daily briefing

1. Fork this repo
2. Settings → Pages → deploy from branch `main`, folder `/docs`
3. Done — the included workflow regenerates your page every morning
4. (Optional) add `ANTHROPIC_API_KEY` in Settings → Secrets for AI explanations

### Customize

Edit `feeds.json` — add or remove feeds, change how many stories/CVEs you want, tune the minimum CVSS. The scoring keywords live in `cyberbrief/rank.py`, the ISO 27001 mapping in `cyberbrief/iso.py`.

## Why the ranking works this way

| Signal | Question it answers | Weight |
|--------|--------------------|--------|
| CISA KEV | Is this exploited **in the wild right now**? | +50 |
| Known ransomware use | Are ransomware gangs using it? | +20 |
| EPSS | Probability of exploitation in the next 30 days | ×40 |
| CVSS | Theoretical worst-case severity | ×2 |

A CVSS 9.8 that nobody exploits matters less than a CVSS 7.2 in the KEV catalog. That's the single most useful prioritization lesson in vulnerability management — and this tool encodes it.

## License

MIT — use it, fork it, ship it to your team.

---

*Built by [Bernd Janzen](https://www.linkedin.com/) while studying for a GRC career — because the best way to learn threat awareness is to automate it.*
