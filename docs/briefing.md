# 🛡️ CyberBrief — Thursday, 16 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. CISA Urges Immediate Patching of Exploited SharePoint Vulnerabilities
*SecurityWeek* — [read more](https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-sharepoint-vulnerabilities/)

Three vulnerabilities are actively exploited in attacks, including two that have been targeted as zero-days. The post CISA Urges Immediate Patching of Exploited SharePoint Vulnerabilities appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. SonicWall warns of SMA1000 flaws exploited in zero-day attacks, patch now
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-sma1000-flaws-exploited-in-zero-day-attacks-patch-now/)

SonicWall warns that threat actors have been exploiting two SMA1000 vulnerabilities, tracked as CVE-2026-15409 and CVE-2026-15410, in zero-day attacks and urges customers to install the newly released security updates. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 3. Two SonicWall SMA 1000 Zero-Days Exploited, One Could Enable Admin Commands
*The Hacker News* — [read more](https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html)

SonicWall has warned of active exploitation of two zero-day vulnerabilities impacting Secure Mobile Access (SMA) 1000 series appliances, one of which could be exploited to achieve arbitrary command execution. The vulnerabilities are listed below - CVE-2026-15409 (CVSS score: 10.0) - A Server-side request forgery (SSRF) vulnerability that a remote unauthenticated attacker could exploit to

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. CISA warns admins to patch actively exploited SharePoint flaws
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-patch-actively-exploited-sharepoint-flaws/)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned Tuesday that attackers are actively exploiting three vulnerabilities to hack Internet-exposed on-premises SharePoint Server instances. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 5. Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday
*The Hacker News* — [read more](https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html)

Security researcher Chaotic Eclipse (aka Nightmare-Eclipse) has released a new proof-of-concept (PoC) exploit called LegacyHive. It has been described as a Windows User Profile Service arbitrary hive load elevation of privileges vulnerability. The Windows User Profile Service, also referred to as ProfSvc, is a core system component that manages user accounts and environments. "The PoC requires

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 6. Vulnerabilities Patched by Fortinet, Ivanti, ServiceNow
*SecurityWeek* — [read more](https://www.securityweek.com/vulnerabilities-patched-by-fortinet-ivanti-servicenow/)

A critical security defect in the ServiceNow AI platform could allow remote attackers to execute arbitrary code. The post Vulnerabilities Patched by Fortinet, Ivanti, ServiceNow appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Nightmare Eclipse Drops ‘LegacyHive’ Windows Zero-Day
*SecurityWeek* — [read more](https://www.securityweek.com/nightmare-eclipse-drops-legacyhive-windows-zero-day/)

The researcher stripped the proof-of-concept (PoC) exploit to prevent immediate exploitation of the vulnerability. The post Nightmare Eclipse Drops LegacyHive Windows Zero-Day appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack
*The Hacker News* — [read more](https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html)

Microsoft shipped its largest Patch Tuesday on record today, and two of the fixes close holes that attackers are already exploiting. The release covers 622 of Microsoft's own CVEs by its Security Update Guide count, more than triple June's previous high of around 200. Those two live bugs are the ones to grab first. Microsoft credits incident responders for both. Both are

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-56164** | Microsoft SharePoint Server Missing Authentication for Critical Function Vulnerability | 9.8 | 7% | ⚠️ YES (KEV) |
| **CVE-2026-15409** | SonicWall SMA1000 Appliances Server-Side Request Forgery Vulnerability | 10.0 | 1% | ⚠️ YES (KEV) |
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 24% | ⚠️ YES (KEV) |
| **CVE-2026-56290** | Joomlack Page Builder Improper Access Control Vulnerability | – | 3% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*