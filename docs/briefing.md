# 🛡️ CyberBrief — Wednesday, 15 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. SonicWall warns of SMA1000 flaws exploited in zero-day attacks, patch now
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-sma1000-flaws-exploited-in-zero-day-attacks-patch-now/)

SonicWall warns that threat actors have been exploiting two SMA1000 vulnerabilities, tracked as CVE-2026-15409 and CVE-2026-15410, in zero-day attacks and urges customers to install the newly released security updates. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Two SonicWall SMA 1000 Zero-Days Exploited, One Could Enable Admin Commands
*The Hacker News* — [read more](https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html)

SonicWall has warned of active exploitation of two zero-day vulnerabilities impacting Secure Mobile Access (SMA) 1000 series appliances, one of which could be exploited to achieve arbitrary command execution. The vulnerabilities are listed below - CVE-2026-15409 (CVSS score: 10.0) - A Server-side request forgery (SSRF) vulnerability that a remote unauthenticated attacker could exploit to

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Progress confirms ShareFile zero-day flaw behind Storage Zone shutdown
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/)

Progress Software has confirmed that a high-severity zero-day vulnerability is behind the emergency shutdown of ShareFile Storage Zone Controllers last week and has released security updates to patch the flaw. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. SonicWall Issues Urgent SMA Patch Warning for Two Zero-Day Exploits
*SecurityWeek* — [read more](https://www.securityweek.com/sonicwall-issues-urgent-sma-patch-warning-for-two-zero-day-exploits/)

SonicWall SMA1000 zero-day vulnerabilities CVE-2026-15409 and CVE-2026-15410 can be exploited for remote code execution. The post SonicWall Issues Urgent SMA Patch Warning for Two Zero-Day Exploits appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Synopsys Finds No Evidence of Data Breach Amid Bosch Hack Claims
*SecurityWeek* — [read more](https://www.securityweek.com/synopsys-finds-no-evidence-of-data-breach-following-bosch-hack-claims/)

The D1R cybercrime group claimed to have stolen valuable data from Synopsys and Bosch, threatening to leak it unless a ransom is paid. The post Synopsys Finds No Evidence of Data Breach Amid Bosch Hack Claims appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 6. Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack
*The Hacker News* — [read more](https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html)

Microsoft shipped its largest Patch Tuesday on record today, and two of the fixes close holes that attackers are already exploiting. The release covers 622 of Microsoft's own CVEs by its Security Update Guide count, more than triple June's previous high of around 200. Those two live bugs are the ones to grab first. Microsoft credits incident responders for both. Both are

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 7. Microsoft July 2026 Patch Tuesday fixes massive 570 flaws, 3 zero-days
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2026-patch-tuesday-fixes-massive-570-flaws-3-zero-days/)

Today is Microsoft's July 2026 Patch Tuesday, and with it comes security updates for a record-breaking 570 flaws, including two zero-day vulnerabilities exploited in attacks and one publicly disclosed. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 8. Microsoft Patches Record 622 Vulnerabilities, Including Two Exploited Zero-Days
*SecurityWeek* — [read more](https://www.securityweek.com/microsoft-patches-record-622-vulnerabilities-including-two-exploited-zero-days/)

Two flaws in Active Directory and SharePoint Server have been exploited as zero-days, and a BitLocker bug was publicly disclosed. The post Microsoft Patches Record 622 Vulnerabilities, Including Two Exploited Zero-Days appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-15409** | SonicWall SMA1000 Appliances Server-Side Request Forgery Vulnerability | 10.0 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-56164** | Microsoft SharePoint Server Missing Authentication for Critical Function Vulnerability | 9.8 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 24% | ⚠️ YES (KEV) |
| **CVE-2026-45659** | Microsoft SharePoint Server Deserialization of Untrusted Data Vulnerability | – | 3% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*