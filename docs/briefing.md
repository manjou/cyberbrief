# 🛡️ CyberBrief — Friday, 24 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. Check Point warns of SmartConsole zero-day exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/)

Israeli cybersecurity firm Check Point Software has addressed an actively exploited zero-day flaw in the company's SmartConsole graphical user interface (GUI) admin panel. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Data Breach Confirmed After Australian Energy Giant Origin Is Hacked
*SecurityWeek* — [read more](https://www.securityweek.com/data-breach-confirmed-after-australian-energy-giant-origin-is-hacked/)

A hacker claims to have stolen the information of 2 million Origin Energy customers and is threatening to leak it. The post Data Breach Confirmed After Australian Energy Giant Origin Is Hacked appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 3. New Check Point Zero-Day Vulnerability Exploited in the Wild
*SecurityWeek* — [read more](https://www.securityweek.com/new-check-point-zero-day-vulnerability-exploited-in-the-wild/)

The vulnerability tracked as CVE-2026-16232 has been exploited against customers with certain configurations. The post New Check Point Zero-Day Vulnerability Exploited in the Wild appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. New msaRAT malware uses Chrome, Edge browsers to route C2 traffic
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/new-msarat-malware-uses-chrome-edge-browsers-to-route-c2-traffic/)

The Chaos ransomware gang is using a new backdoor dubbed msaRAT that hides command-and-control (C2) communication by routing it through the Chrome or Edge browsers. [...]

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.7 Protection against malware

### 5. Australian energy provider Origin says data breach exposes client data
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/)

Origin Energy has confirmed that an unauthorized party accessed and subsequently leaked customer data online, exposing sensitive personally identifiable information (PII), among others. [...]

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 6. Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
*The Hacker News* — [read more](https://thehackernews.com/2026/07/russian-espionage-group-exploited.html)

A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA, CISA and partner agencies published

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 7. Check Point Patches Exploited SmartConsole Flaw Allowing Full Admin Access
*The Hacker News* — [read more](https://thehackernews.com/2026/07/check-point-patches-exploited.html)

Check Point has released security updates to address multiple vulnerabilities impacting Security Management and Multi-Domain Management (MDSM) products, including a critical flaw that has come under active exploitation in the wild. The security flaw, tracked as CVE-2026-16232 (CVSS score: 9.3), is an authentication bypass affecting the Check Point SmartConsole login process that allows an

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 8. Clop ransomware targets Windchill, FlexPLM in data theft attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/)

The Clop ransomware gang (also tracked as Cl0p) is targeting Internet-exposed PTC Windchill and FlexPLM instances in a new data theft extortion campaign. [...]

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.34 Privacy and protection of PII

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2026-0770** | Langflow Inclusion of Functionality from Untrusted Control Sphere Vulnerability | – | 55% | ⚠️ YES (KEV) |
| **CVE-2026-16232** | Check Point SmartConsole Improper Authentication Vulnerability | 9.1 | 1% | ⚠️ YES (KEV) |
| **CVE-2026-63030** | WordPress Core Interpretation Conflict Vulnerability | – | 39% | ⚠️ YES (KEV) |
| **CVE-2026-25089** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 36% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*