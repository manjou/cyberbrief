# 🛡️ CyberBrief — SOC — Thursday, 26 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. Hackers now exploit critical Drupal RCE flaw to hijack sites
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-drupal-rce-flaw-to-hijack-sites/)

The Drupal security team has confirmed that a critical vulnerability that lets attackers hijack unpatched sites has been actively exploited since at least Thursday.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Drupal Fail2Install Exploit Details Emerge as Critical RCE Flaw Faces Active Exploitation
*The Hacker News* — [read more](https://thehackernews.com/2026/11/drupal-fail2install-exploit-details.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a critical flaw impacting Drupal to its Known Exploited Vulnerabilities (KEV) catalog, requiring federal agencies to apply the fixes by November 27, 2026. The vulnerability, tracked as CVE-2026-132165 aka Fail2Install (CVSS score: 9.8), is a case of remote code execution (RCE) impacting Drupal core. "Drupal Core

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Hackers Exploit Two GeoServer Flaws as Researchers Warn of Unauthenticated RCE Chains
*The Hacker News* — [read more](https://thehackernews.com/2026/11/hackers-exploit-two-geoserver-flaws-as.html)

Threat actors are actively exploiting two newly patched security flaws in GeoServer, according to watchTowr. The vulnerabilities in question are CVE-2026-120705 and CVE-2026-129243, details of which are below - CVE-2026-120705 (CVSS score: 8.6) - An arbitrary file read vulnerability that could enable an attacker to access local text files readable by the GeoServer process or fetch

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 4. Remus malware steals Gmail messages via fake Google Sheets extension
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/remus-malware-steals-gmail-messages-via-fake-google-sheets-extension/)

The Remus infostealer is stealing Gmail messages through a stealthy malicious Chrome extension, a capability the malware operators marketed as a zero-day exploit in Google's email service.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 5. 1Password Hacked, Customer Data and Source Code Stolen in GitHub Account Breach
*The Hacker News* — [read more](https://thehackernews.com/2026/11/1password-hacked-customer-data-and.html)

Popular password management software 1Password on Wednesday disclosed a security incident involving its backend systems that led to the unauthorized access of some customer information, but emphasized that customer password vaults and other secrets were not accessed. "While we took immediate steps to contain the incident, the attacker gained access to some of our backend systems and accessed a

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 6. Drupal Warns of New Highly Critical Site Takeover Vulnerability Under Active Exploitation
*The Hacker News* — [read more](https://thehackernews.com/2026/11/drupal-warns-of-new-highly-critical.html)

Drupal has warned of a new "highly critical" security flaw impacting Drupal core that it said has been exploited in the wild. The vulnerability, tracked as CVE-2026-136716 (CVSS score: N/A), has been described as a case of improper checking for unusual or exceptional conditions. It also relates to CVE-2026-132165 aka Fail2Install in that it addresses remaining vulnerable installation states

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Mitel MiCollab Zero-Days Exploited in Suspected AI-Assisted Attacks
*SecurityWeek* — [read more](https://www.securityweek.com/mitel-micollab-zero-days-exploited-in-suspected-ai-assisted-attacks/)

Accenture says hackers exploited MiCollab flaws before Mitel’s advisory, likely aided by AI, in a suspected extortion campaign.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 8. Two Newly Disclosed GeoServer Vulnerabilities Under Attack
*SecurityWeek* — [read more](https://www.securityweek.com/two-newly-disclosed-geoserver-vulnerabilities-under-attack/)

Attackers are probing GeoServer instances for two high-severity flaws that can be chained with other bugs for unauthenticated RCE.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2024-10441** | Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability | – | 3% | ⚠️ YES (KEV) · ransomware |
| **CVE-2026-133469** | Vates Xen Orchestra Improper Validation of Specified Type of Input Vulnerability | – | 32% | ⚠️ YES (KEV) |
| **CVE-2026-133968** | Project MONAI MONAI Label Path Traversal Vulnerability | – | 27% | ⚠️ YES (KEV) |
| **CVE-2026-129448** | Apache Roller Deserialization of Untrusted Data Vulnerability | – | 24% | ⚠️ YES (KEV) |
| **CVE-2026-40217** | BerriAI LiteLLM Unprotected Alternate Channel Vulnerability | – | 20% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*