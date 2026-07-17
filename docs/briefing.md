# 🛡️ CyberBrief — Friday, 17 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV
*The Hacker News* — [read more](https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday added a newly patched security flaw impacting Microsoft SharePoint Server to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by July 19, 2026. The vulnerability in question is CVE-2026-58644 (CVSS score: 9.8), a critical deserialization

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. CISA urges immediate action on actively exploited Fortinet flaws
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/)

CISA on Thursday ordered government agencies to prioritize patching two actively exploited vulnerabilities in the Fortinet FortiSandbox threat detection platform. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 3. CISA orders feds to patch actively exploited Oracle flaw by Saturday
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-flaw-by-saturday/)

CISA has ordered federal agencies to secure their systems by Saturday against ongoing attacks exploiting a critical vulnerability in the Oracle E-Business Suite financial application. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. 23andMe to pay $18 million in new genetics data breach settlement
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/23andme-to-pay-18-million-in-new-genetics-data-breach-settlement/)

Genetic testing company 23andMe has agreed to pay $18 million to settle claims from a coalition of 43 attorneys general that it failed to protect customers' genetic data. [...]

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 5. Coca-Cola Suspends US Fairlife Production Due to Ransomware Attack
*SecurityWeek* — [read more](https://www.securityweek.com/coca-cola-suspends-us-fairlife-production-due-to-ransomware-attack/)

The company says the incident has not affected product quality and safety, nor Fairlife’s Canada production. The post Coca-Cola Suspends US Fairlife Production Due to Ransomware Attack appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.24 Incident management planning

### 6. ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories
*The Hacker News* — [read more](https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html)

A lot of this week’s trouble starts with something that looks close enough. A familiar repo. A useful installer. A harmless sync setting. Then the handoff goes bad, the box starts talking to someone else, and the damage moves faster than the explanation. Old bugs are back, weak defaults are earning their keep, and some attack paths are so plain they barely feel like research. Here’s the mess.

> 📋 **ISO 27001:** A.8.13 Information backup

### 7. Zoom warns of critical account takeover vulnerability
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/zoom-warns-of-critical-account-takeover-vulnerability/)

Zoom is warning of a critical vulnerability in its desktop client and software development kit for Windows that could be exploited by an unauthenticated party to hijack accounts. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. New Spirals ransomware encrypts victim network in under 24 hours
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/new-spirals-ransomware-encrypts-victim-network-in-under-24-hours/)

A new ransomware actor called Spirals completed a corporate intrusion, from initial access to data theft and encryption, in less than 24 hours. [...]

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.24 Use of cryptography

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 49% | ⚠️ YES (KEV) |
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 24% | ⚠️ YES (KEV) |
| **CVE-2026-25089** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 23% | ⚠️ YES (KEV) |
| **CVE-2026-56164** | Microsoft SharePoint Server Missing Authentication for Critical Function Vulnerability | – | 6% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*