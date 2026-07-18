# 🛡️ CyberBrief — Saturday, 18 July 2026

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

### 3. In Other News: Iran Tracks US Military Phones, CrashStealer macOS Malware, CVD Blueprint
*SecurityWeek* — [read more](https://www.securityweek.com/in-other-news-iran-tracks-us-military-phones-crashstealer-macos-malware-cvd-blueprint/)

Noteworthy stories that might have slipped under the radar: OpenClaw AI agents exploited via WhatsApp, ransomware hits naval defense firm TKMS, Lidl discloses data breach. The post In Other News: Iran Tracks US Military Phones, CrashStealer macOS Malware, CVD Blueprint appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.7 Protection against malware

### 4. Ernst & Young discloses data breach after support system hack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/ernst-and-young-discloses-data-breach-after-support-system-hack/)

Ernst & Young is notifying customers of a data breach caused by the compromise of a third-party support ticket system used by its IT personnel. [...]

> 📋 **ISO 27001:** A.5.19 Supplier relationships, A.5.34 Privacy and protection of PII

### 5. New Windows LegacyHive zero-day gives hackers admin privileges
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/new-windows-legacyhive-zero-day-exploit-grants-hackers-admin-access/)

A security researcher using the "Nightmare Eclipse" handle has released a Windows zero-day exploit dubbed LegacyHive that allows attackers to escalate privileges on up-to-date Windows systems. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 6. GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft
*The Hacker News* — [read more](https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html)

Cybersecurity researchers have attributed the April 2026 DigiCert security incident to a threat activity cluster dubbed CylindricalCanine. Expel, which shared technical details of the event, described the threat actor as a sub-group of GoldenEyeDog (aka APT-Q-27, Dragon Breath, and Miuuti Group), a Chinese cybercrime group known for its targeting of the gambling and gaming sectors using

> 📋 **ISO 27001:** A.5.24 Incident management planning, A.8.24 Use of cryptography

### 7. Armenia Detains Russian Tourist on U.S. Warrant for REvil Hacker, Lawyers Say Wrong Man
*The Hacker News* — [read more](https://thehackernews.com/2026/07/armenia-detains-russian-tourist-on-us.html)

Armenia has held a Russian tourist named Aleksandr Ermakov in a detention center since June 28, on a U.S. extradition request for a REvil ransomware suspect named Aleksandr Ermakov. His wife, Maria Yurova, told REN TV that border officers pulled him out of the departure hall at Yerevan's Zvartnots airport, held up a phone with a photo of him off his VKontakte page, and walked him into a side

> 📋 **ISO 27001:** A.8.13 Information backup

### 8. Seven Malicious Vite npm Packages Use Blockchain C2 to Deliver a RAT
*The Hacker News* — [read more](https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html)

Cybersecurity researchers have discovered a cluster of seven malicious npm packages targeting the Vite frontend tooling ecosystem as part of a software supply chain attack. The malicious package campaign, codenamed ViteVenom by Checkmarx, marks an expansion of ChainVeil, which was observed using an "unprecedented" four-tier blockchain-based command-and-control (C2) infrastructure spanning Tron,

> 📋 **ISO 27001:** A.5.19 Supplier relationships

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2026-25089** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 36% | ⚠️ YES (KEV) |
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 24% | ⚠️ YES (KEV) |
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