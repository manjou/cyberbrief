# LinkedIn announcement — ready to paste

I couldn't keep up with cybersecurity news. So I built something — and it's free for everyone.

Breaking into GRC, I kept drowning: dozens of feeds, hundreds of new CVEs a week, and no way to tell what actually mattered *today*.

CyberBrief is my answer — an open-source daily briefing that prioritizes the way practitioners do:

🔴 CISA KEV first — is it being exploited in the wild right now?
🟠 EPSS second — how likely is exploitation in the next 30 days?
🟡 CVSS last — how bad could it theoretically get?

Every story is explained in plain English (jargon decoder for newcomers included) and mapped to the ISO 27001:2022 Annex A control it touches — so reading the morning news doubles as compliance practice.

⚙️ Zero dependencies, pure Python, no AI required, runs itself for free on GitHub Actions
📰 Today's briefing: https://manjou.github.io/cyberbrief/
🔧 Fork it → your own auto-updating briefing in 5 minutes: https://github.com/manjou/cyberbrief

The one lesson that stuck while building it: a CVSS 9.8 that nobody exploits matters less than a CVSS 7.2 sitting in the KEV catalog. **Prioritization beats severity.**

If you work in security or GRC — I'd genuinely love feedback. Which sources would you add?

#cybersecurity #GRC #ISO27001 #opensource #infosec #vulnerabilitymanagement
