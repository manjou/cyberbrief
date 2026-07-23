# 🛡️ CyberBrief — Thursday, 23 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. Hackers Exploit Windmill Flaw to Read Arbitrary Server Files Without Authentication
*The Hacker News* — [read more](https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html)

A high-severity security flaw impacting open-source developer platform Windmill has come under active exploitation in the wild, per VulnCheck. The vulnerability in question is CVE-2026-29059 (CVSS score: 7.5), a case of unauthenticated path traversal impacting Windmill's "get_log_file" endpoint ("/api/w/{workspace}/jobs_u/get_log_file/{filename}"). "The filename parameter is concatenated into

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 2. CISA orders urgent action on actively exploited Langflow RCE flaw
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-langflow-rce-flaw/)

The Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday ordered U.S. government agencies to prioritize patching an actively exploited vulnerability in the Langflow visual framework for building AI agents. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Swiss rail giant Stadler rejects $12.3M ransom demand after cyberattack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/swiss-rail-giant-stadler-rejects-123m-ransom-demand-after-cyberattack/)

Swiss rail vehicle manufacturer Stadler Rail says the Everest ransomware gang demanded about $12.3 million after breaching a data exchange platform shared with one of its suppliers. [...]

> 📋 **ISO 27001:** A.8.13 Information backup

### 4. Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts
*SecurityWeek* — [read more](https://www.securityweek.com/suno-paidwork-data-breaches-affect-tens-of-millions-of-accounts/)

Hackers leaked names, email addresses, phone numbers, passwords, and financial information stolen from the two platforms. The post Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.17 Authentication information

### 5. Critical SharePoint RCE flaw exploited to steal machine keys
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/critical-sharepoint-rce-flaw-exploited-to-steal-machine-keys/)

Hackers are actively exploiting the critical CVE-2026-50522 vulnerability in Microsoft SharePoint to steal machine keys and maintain access even after affected servers are patched. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. South Korea discloses data breach impacting diplomats worldwide
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/south-korea-discloses-data-breach-impacting-diplomats-worldwide/)

South Korea disclosed that hackers breached the National Diplomatic Academy's online education system for ten months and stole personal information belonging to current and former employees of the Ministry of Foreign Affairs (MFA), including overseas diplomats. [...]

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.17 Authentication information

### 7. Police Dismantle Kratos Phishing Kit Built to Steal Microsoft 365 Sessions and Bypass MFA
*The Hacker News* — [read more](https://thehackernews.com/2026/07/police-dismantle-kratos-phishing-kit.html)

German and US law enforcement have taken down the core infrastructure of Kratos, described by German investigators as one of the world's most widely used criminal phishing kits, and Indonesian authorities arrested the man they say developed and ran it. In a joint announcement on Monday, the Frankfurt public prosecutor's cybercrime unit (ZIT) and Germany's Federal Criminal Police Office (BKA)

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.8.8 Management of technical vulnerabilities

### 8. Chick-fil-A discloses data breach after credential stuffing attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/chick-fil-a-discloses-data-breach-after-credential-stuffing-attacks/)

American fast food restaurant chain Chick-fil-A is notifying customers of a data breach after their accounts were hacked in a wave of recent credential stuffing attacks. [...]

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.17 Authentication information

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2026-0770** | Langflow Inclusion of Functionality from Untrusted Control Sphere Vulnerability | – | 55% | ⚠️ YES (KEV) |
| **CVE-2026-16232** | Check Point SmartConsole Improper Authentication Vulnerability | 9.1 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-63030** | WordPress Core Interpretation Conflict Vulnerability | – | 39% | ⚠️ YES (KEV) |
| **CVE-2026-25089** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 36% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*