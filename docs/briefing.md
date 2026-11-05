# 🛡️ CyberBrief — SOC — Thursday, 05 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **CISA flags WordPress RCE flaw as actively exploited in attacks** — The US Cybersecurity and Infrastructure Security Agency (CISA) warned federal agencies that attackers have started exploiting a recently patched high-severity WordPress vulnerability in the wild. [read more](https://www.bleepingcomputer.com/news/security/cisa-flags-wordpress-rce-flaw-as-actively-exploited-in-attacks/)
- **Zyxel GS1900 Patch Fails to Block Zero-Day Exploit Allowing Root Command Execution** — Zyxel GS1900 network switches that received the vendor's earlier fix for an actively exploited flaw are still open to the exploit attackers used, researchers at Binarly found. [read more](https://thehackernews.com/2026/11/zyxel-gs1900-patch-fails-to-block-zero.html)
- **CERT-In Flags AI-Driven Attacks as Backdoored ARTEX Exposes 62 Consoles to Root Access** — The Indian Computer Emergency Response Team (CERT-In) has disclosed that an artificial intelligence (AI)-assisted threat actor it tracks as Crafty Falcon is targeting organizations in the Banking, Financial Services, and Insurance (BFSI) sectors in the country. [read more](https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html)
- **APT29-Linked Hackers Hijack Web Analytics Script to Deliver iOS and Android Exploits** — The Russia-linked threat actor known as APT29 is presumed to be behind a large-scale watering hole campaign targeting iOS and Android users through compromised websites, fake domains, and a supply chain attack involving a Ukrainian web analytics service called Plerdy SEO Tracker. [read more](https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html)
- **5 Active Cyber Threats That Put US Enterprises at Risk in October 2026** — October 2026 brought another wave of cyber threats targeting US businesses, with attackers exploiting trusted platforms, legitimate authentication processes, and everyday business workflows. [read more](https://thehackernews.com/2026/11/5-active-cyber-threats-that-put-us.html)
- **Zyxel Switch Hacks Blamed on Patched Flaw Actually Exploited a Zero-Day** — Tracked as CVE-2026-107441, the out-of-bounds write flaw could allow attackers to execute OS commands via crafted HTTP requests. [read more](https://www.securityweek.com/zyxel-switch-hacks-blamed-on-patched-flaw-actually-exploited-a-zero-day/)
- **Zyxel fixes zero-day exploited to hack nearly 1,000 network switches** — Zyxel has patched a zero-day vulnerability in its GS1900 series network switches that hackers exploited to compromise nearly 1,000 devices worldwide and steal configuration files and credentials. [read more](https://www.bleepingcomputer.com/news/security/zyxel-fixes-zero-day-exploited-to-hack-nearly-1-000-network-switches/)
- **Vercel rolls out new protection against stolen session cookie attacks** — Vercel is gradually rolling out Device Bound Session Credentials (DBSC) on its platform as a key defense against information stealer malware. [read more](https://www.bleepingcomputer.com/news/security/vercel-rolls-out-new-protection-against-stolen-session-cookie-attacks/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-109618 (– CVSS, 100% EPSS)

## 🔥 Top stories

### 1. CISA flags WordPress RCE flaw as actively exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-flags-wordpress-rce-flaw-as-actively-exploited-in-attacks/)

The US Cybersecurity and Infrastructure Security Agency (CISA) warned federal agencies that attackers have started exploiting a recently patched high-severity WordPress vulnerability in the wild.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Zyxel GS1900 Patch Fails to Block Zero-Day Exploit Allowing Root Command Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/11/zyxel-gs1900-patch-fails-to-block-zero.html)

Zyxel GS1900 network switches that received the vendor's earlier fix for an actively exploited flaw are still open to the exploit attackers used, researchers at Binarly found. The exploit lets anyone who can reach a switch's web management interface run commands on it without logging in. Zyxel has released new firmware for 10 GS1900 models that closes the hole. The earlier fix is the 2.90

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 3. CERT-In Flags AI-Driven Attacks as Backdoored ARTEX Exposes 62 Consoles to Root Access
*The Hacker News* — [read more](https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html)

The Indian Computer Emergency Response Team (CERT-In) has disclosed that an artificial intelligence (AI)-assisted threat actor it tracks as Crafty Falcon is targeting organizations in the Banking, Financial Services, and Insurance (BFSI) sectors in the country. Describing the threat as active and ongoing, the activity involves the use of publicly-available AI-driven offensive security tools

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.24 Incident management planning

### 4. APT29-Linked Hackers Hijack Web Analytics Script to Deliver iOS and Android Exploits
*The Hacker News* — [read more](https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html)

The Russia-linked threat actor known as APT29 is presumed to be behind a large-scale watering hole campaign targeting iOS and Android users through compromised websites, fake domains, and a supply chain attack involving a Ukrainian web analytics service called Plerdy SEO Tracker. "The injected JavaScript code collects browser and device attributes," Sekoia researchers Amaury-Jacques Garçon and

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 5. 5 Active Cyber Threats That Put US Enterprises at Risk in October 2026
*The Hacker News* — [read more](https://thehackernews.com/2026/11/5-active-cyber-threats-that-put-us.html)

October 2026 brought another wave of cyber threats targeting US businesses, with attackers exploiting trusted platforms, legitimate authentication processes, and everyday business workflows. For enterprises, these campaigns raise the stakes beyond individual security incidents, increasing the risk of financial losses, data breaches, and costly operational disruption. Below, we examine five

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 6. Zyxel Switch Hacks Blamed on Patched Flaw Actually Exploited a Zero-Day
*SecurityWeek* — [read more](https://www.securityweek.com/zyxel-switch-hacks-blamed-on-patched-flaw-actually-exploited-a-zero-day/)

Tracked as CVE-2026-107441, the out-of-bounds write flaw could allow attackers to execute OS commands via crafted HTTP requests.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Zyxel fixes zero-day exploited to hack nearly 1,000 network switches
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/zyxel-fixes-zero-day-exploited-to-hack-nearly-1-000-network-switches/)

Zyxel has patched a zero-day vulnerability in its GS1900 series network switches that hackers exploited to compromise nearly 1,000 devices worldwide and steal configuration files and credentials.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 8. Vercel rolls out new protection against stolen session cookie attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/vercel-rolls-out-new-protection-against-stolen-session-cookie-attacks/)

Vercel is gradually rolling out Device Bound Session Credentials (DBSC) on its platform as a key defense against information stealer malware.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-109618** | PHP Memory Corruption Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-109619** | PHP Stale Internal Request-State Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-111497** | Google Brotli Unchecked Return Value Vulnerability | – | 83% | ⚠️ YES (KEV) |
| **CVE-2026-110447** | Collabora Online – Built-in CODE Server OS Command Injection Vulnerability | – | 73% | ⚠️ YES (KEV) |
| **CVE-2026-97229** | GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability | – | 65% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*