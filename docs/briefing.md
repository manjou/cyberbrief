# 🛡️ CyberBrief — Net+ — Wednesday, 28 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🔥 Top stories

### 1. ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws
*The Hacker News* — [read more](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html)

The critical Oracle PeopleSoft bug that ShinyHunters has exploited since May is not one flaw but three chained together, the researchers who reported it said this week. Oracle patched all three under a single identifier, CVE-2026-35273, in June. Its root is a server-side request forgery (SSRF) that reaches an internal management interface because PeopleSoft trusts its own loopback address

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Adobe Commerce PolyShell Attacks Breach Hundreds of Stores as Brotli Exploit Traffic Emerges
*The Hacker News* — [read more](https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added two vulnerabilities impacting Adobe Commerce and Magento, and Google's Brotli decoder library to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerabilities are listed below - CVE-2026-111497 (CVSS score: 9.2) - An unchecked return value vulnerability in

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Japan's GMO urges customers to shut down PCs amid ransomware threat
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/japans-gmo-urges-customers-to-shut-down-pcs-amid-ransomware-threat/)

The GMO Group has urged customers to disconnect their systems from the internet and shut down computers after a threat actor who breached the company's Onamae Desktop Cloud threatened to launch a ransomware attack today.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.23 Cloud services security

### 4. CISA Confirms Active Exploitation of Two PHP2Shell Flaws Enabling Remote Code Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/10/cisa-confirms-active-exploitation-of.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday confirmed active exploitation of the recently patched PHP2Shell flaws by adding them to its Known Exploited Vulnerabilities (KEV) catalog. The PHP vulnerabilities, both rated 9.2 on the CVSS scoring system, facilitate unauthenticated remote code execution on affected deployments - CVE-2026-109618 - An out-of-memory

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. HPE Patches Dozens of Critical Flaws in Networking Products
*SecurityWeek* — [read more](https://www.securityweek.com/hpe-patches-dozens-of-critical-flaws-in-networking-products/)

Eight max-severity security defects could lead to remote code execution and authentication bypass.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 6. CISA confirms PHP2Shell vulnerabilities now exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-confirms-php2shell-vulnerabilities-now-exploited-in-attacks/)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added the PHP2Shell vulnerabilities to its catalog of actively exploited security flaws and ordered federal agencies to patch their systems by Thursday.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 7. Hackers Start Probing Fresh Oracle EBS Vulnerability
*SecurityWeek* — [read more](https://www.securityweek.com/hackers-start-probing-fresh-oracle-ebs-vulnerability/)

CVE-2026-101767 is an unauthenticated SQL injection that can be exploited for remote code execution.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. CISA warns of hackers now exploiting critical Node2Shell flaw
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-now-exploiting-critical-node2shell-flaw/)

On Tuesday, the US Cybersecurity and Infrastructure Security Agency (CISA) confirmed that hackers have begun exploiting a critical Brotli vulnerability known as Node2Shell, Broccoli2Shell, and HTTP2Shell.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-109618** | PHP Memory Corruption Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-109619** | PHP Stale Internal Request-State Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-21589** | Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-105134** | Ahsay AhsayCBS Command Injection Vulnerability | – | 82% | ⚠️ YES (KEV) |
| **CVE-2026-105133** | Ahsay AhsayCBS Improper Authentication Vulnerability | – | 79% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*