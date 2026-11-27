# 🛡️ CyberBrief — GRC — Friday, 27 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access** — Details have emerged about a new zero-day vulnerability in Cacti, an open-source network monitoring tool, that could be exploited to achieve remote code execution. [read more](https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html)
- **1Password Hacked, Customer Data and Source Code Stolen in GitHub Account Breach** — Popular password management software 1Password on Wednesday disclosed a security incident involving its backend systems that led to the unauthorized access of some customer information, but emphasized that customer password vaults and other secrets were not accessed. [read more](https://thehackernews.com/2026/11/1password-hacked-customer-data-and.html)
- **100,000 Potentially Impacted by Colorado Data Breach** — Hackers breached the digital identification and document storage application myColorado and accessed user-uploaded data. [read more](https://www.securityweek.com/100000-potentially-impacted-by-colorado-data-breach/)
- **Hex Package Manager Warns of Potential Data Breach** — A vulnerability in hex.pm allowed hackers to run commands on web servers. [read more](https://www.securityweek.com/hex-package-manager-warns-of-potential-data-breach/)
- **In Other News: Tanker Cyberattacks, EU Quantum Act, New VirusTotal Capabilities** — Noteworthy stories that might have slipped under the radar: RansomwareHelp accused of profiting from ransom payments, USDA payment systems breach, cybersecurity firm Radware hacked. [read more](https://www.securityweek.com/in-other-news-tanker-cyberattacks-eu-quantum-act-new-virustotal-capabilities/)
- **US Air Force cloud platform reportedly hacked in latest federal breach** — Hackers have reportedly breached the US Air Force's Cloud One computing platform, adding to a recent wave of cyberattacks affecting US government agencies, including the FBI, CIA, and Treasury Department. [read more](https://www.bleepingcomputer.com/news/security/us-air-force-cloud-platform-reportedly-hacked-in-latest-federal-breach/)
- **Drupal warns of new site takeover flaw exploited in attacks** — The Drupal security team says attackers are exploiting a second critical vulnerability that lets them breach and hijack unpatched websites. [read more](https://www.bleepingcomputer.com/news/security/drupal-warns-of-new-access-bypass-flaw-exploited-in-attacks/)
- **Switzerland Confirms AI-Assisted Cyberattacks Breached Critical Infrastructure Operators** — Attackers using AI agents have broken into computer systems at Swiss organizations in four of five confirmed attacks, the first such cases in the country, the country's cybersecurity agency said yesterday. [read more](https://thehackernews.com/2026/11/switzerland-confirms-ai-assisted.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-132165 (9.8 CVSS, 8% EPSS)

## 🔥 Top stories

### 1. Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access
*The Hacker News* — [read more](https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html)

Details have emerged about a new zero-day vulnerability in Cacti, an open-source network monitoring tool, that could be exploited to achieve remote code execution. The proof-of-concept (PoC) exploit, which has yet to be assigned a CVE identifier, has been tracked as 4HTTP2SHELL and 4HTTP2ROOT. "I found a path from a fresh, unauthenticated HTTP session to command execution as the Cacti server

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. 1Password Hacked, Customer Data and Source Code Stolen in GitHub Account Breach
*The Hacker News* — [read more](https://thehackernews.com/2026/11/1password-hacked-customer-data-and.html)

Popular password management software 1Password on Wednesday disclosed a security incident involving its backend systems that led to the unauthorized access of some customer information, but emphasized that customer password vaults and other secrets were not accessed. "While we took immediate steps to contain the incident, the attacker gained access to some of our backend systems and accessed a

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 3. 100,000 Potentially Impacted by Colorado Data Breach
*SecurityWeek* — [read more](https://www.securityweek.com/100000-potentially-impacted-by-colorado-data-breach/)

Hackers breached the digital identification and document storage application myColorado and accessed user-uploaded data.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 4. Hex Package Manager Warns of Potential Data Breach
*SecurityWeek* — [read more](https://www.securityweek.com/hex-package-manager-warns-of-potential-data-breach/)

A vulnerability in hex.pm allowed hackers to run commands on web servers. No evidence of data modification was found, but database reads are not logged.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 5. In Other News: Tanker Cyberattacks, EU Quantum Act, New VirusTotal Capabilities
*SecurityWeek* — [read more](https://www.securityweek.com/in-other-news-tanker-cyberattacks-eu-quantum-act-new-virustotal-capabilities/)

Noteworthy stories that might have slipped under the radar: RansomwareHelp accused of profiting from ransom payments, USDA payment systems breach, cybersecurity firm Radware hacked.

> 📋 **ISO 27001:** A.8.13 Information backup

### 6. US Air Force cloud platform reportedly hacked in latest federal breach
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/us-air-force-cloud-platform-reportedly-hacked-in-latest-federal-breach/)

Hackers have reportedly breached the US Air Force's Cloud One computing platform, adding to a recent wave of cyberattacks affecting US government agencies, including the FBI, CIA, and Treasury Department.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 7. Drupal warns of new site takeover flaw exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/drupal-warns-of-new-access-bypass-flaw-exploited-in-attacks/)

The Drupal security team says attackers are exploiting a second critical vulnerability that lets them breach and hijack unpatched websites.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. Switzerland Confirms AI-Assisted Cyberattacks Breached Critical Infrastructure Operators
*The Hacker News* — [read more](https://thehackernews.com/2026/11/switzerland-confirms-ai-assisted.html)

Attackers using AI agents have broken into computer systems at Swiss organizations in four of five confirmed attacks, the first such cases in the country, the country's cybersecurity agency said yesterday. Three of the attacks targeted critical infrastructure operators, and two of those succeeded, with no major disruptions reported. The victims have not been named, and it is not known who is

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-132165** | Drupal Core Remote Code Execution Vulnerability | 9.8 | 8% | ⚠️ YES (KEV) |
| **CVE-2024-10441** | Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability | – | 3% | ⚠️ YES (KEV) · ransomware |
| **CVE-2026-133469** | Vates Xen Orchestra Improper Validation of Specified Type of Input Vulnerability | – | 32% | ⚠️ YES (KEV) |
| **CVE-2026-133968** | Project MONAI MONAI Label Path Traversal Vulnerability | – | 27% | ⚠️ YES (KEV) |
| **CVE-2026-129448** | Apache Roller Deserialization of Untrusted Data Vulnerability | – | 24% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*