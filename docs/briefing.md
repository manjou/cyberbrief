# 🛡️ CyberBrief — Tuesday, 14 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. CISA warns of actively exploited RCE flaws in Joomla extensions
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-rce-flaws-in-joomla-extensions/)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning that attackers are exploiting vulnerabilities in the iCagenda and Balbooa Forms extensions for Joomla to achieve remote code execution through arbitrary file uploads. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days
*The Hacker News* — [read more](https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added two maximum-severity security flaws impacting iCagenda and Balbooa extensions for Joomla to its Known Exploited Vulnerabilities (KEV) catalog, following reports of zero-day exploitation in the wild. The vulnerabilities, both rated 10.0 on the CVSS scoring system, are below - CVE-2026-48939 - A vulnerability in the

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 3. Centers Laboratory Data Breach Affects 540,000 Individuals
*SecurityWeek* — [read more](https://www.securityweek.com/centers-laboratory-data-breach-affects-540000-individuals/)

The WorldLeaks extortion group claimed to have stolen 720 GB of data from the healthcare testing and laboratory services provider. The post Centers Laboratory Data Breach Affects 540,000 Individuals appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 4. ⚡ Weekly Recap: ShareFile Threat, Citrix Bleed 2 Ransomware, AI Coding Attacks, and More
*The Hacker News* — [read more](https://thehackernews.com/2026/07/weekly-recap-sharefile-threat-citrix.html)

Somewhere right now, a security tool is quietly finding bugs faster than any human can fix them. That's supposed to be the good news. The catch is that the attackers have the same tools, pointed the other way, and they don't file tickets. That's the shape of this week. Trusted code turns on the people who installed it. Old bugs from last year are still landing because the fix sat in a queue too

> 📋 **ISO 27001:** A.8.13 Information backup

### 5. Microsoft Maps Year-Long ShinyHunters-Linked Salesforce Data Theft Across Three Paths
*The Hacker News* — [read more](https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html)

Attackers whose methods line up with the data-extortion group ShinyHunters have spent the past year walking into corporate Salesforce environments without exploiting a single flaw in the platform. The way in has been the trust the organization had already extended, usually through the OAuth connections that tie Salesforce to the apps and third-party vendors around it. In

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 6. Lessons Learned from CISA’s Recent GitHub Leak
*Krebs on Security* — [read more](https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/)

The Cybersecurity and Infrastructure Security Agency (CISA) has issued a postmortem on a data leak in which a contractor published dozens of internal CISA credentials -- including AWS Govcloud keys -- in a public GitHub repository for almost six months before being notified by KrebsOnSecurity. Experts say the gaps identified in the agency's initial response provide important lessons that all security teams should absorb.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.23 Cloud services security

### 7. Breach at the Beach: Play the Ultimate Entra ID CTF
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/breach-at-the-beach-play-the-ultimate-entra-id-ctf/)

Learn how attackers abuse Entra ID through a free hands-on Capture the Flag. Varonis created the Breach at the Beach CTF to teach defenders how to investigate Entra ID attack techniques using realistic scenarios. [...]

### 8. Hackers backdoor Jscrambler npm package with infostealer malware
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-backdoor-jscrambler-npm-package-with-infostealer-malware/)

The Jscrambler client-side web security company disclosed that a threat actor published a malicious version of its npm package that has been downloaded almost 1,500 times. [...]

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.19 Supplier relationships

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 12% | ⚠️ YES (KEV) |
| **CVE-2026-45659** | Microsoft SharePoint Server Deserialization of Untrusted Data Vulnerability | – | 3% | ⚠️ YES (KEV) |
| **CVE-2026-56290** | Joomlack Page Builder Improper Access Control Vulnerability | – | 3% | ⚠️ YES (KEV) |
| **CVE-2026-48939** | iCagenda Unrestricted Upload of File with Dangerous Type Vulnerability | – | 2% | ⚠️ YES (KEV) |

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