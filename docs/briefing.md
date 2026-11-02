# 🛡️ CyberBrief — SOC — Monday, 02 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. Over 1,000 GitLab servers vulnerable to ongoing RCE attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/)

Over 1,000 Internet-exposed GitLab servers are still unpatched against a maximum-severity flaw actively exploited in remote code execution attacks.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 2. Critical Langflow Flaws Could Let Unauthenticated Attackers Run Code on Servers
*The Hacker News* — [read more](https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html)

Two critical flaws in Langflow could let a remote attacker with no account bypass authentication or run arbitrary code, IBM said last week. Langflow is an open-source tool for building AI agents and workflows, and its vulnerability reports go to IBM. Every release from 1.0.0 through 1.12.8 has the flaws, and the only fix is version 1.13.0. Neither flaw is in CISA's Known

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 3. Ivanti Patches Two More Zero-Days Exploited in Connect Secure Attack Chain
*SecurityWeek* — [read more](https://www.securityweek.com/ivanti-patches-two-more-zero-days-exploited-in-connect-secure-attack-chain/)

CISA has added CVE-2026-111357 and CVE-2026-118527 to its KEV catalog after the Ivanti VPN flaws were chained in zero-day attacks.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 4. Alpine Linux rebuilds GitLab after attempted RCE attack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/alpine-linux-rebuilds-gitlab-after-attempted-rce-attack/)

Hackers attempted to exploit a critical GitLab vulnerability in Alpine Linux's development infrastructure on October 20-21, prompting the open-source project to rebuild its GitLab server and reset all passwords over concerns of a possible compromise.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 5. Synology warns of C3RB3R ransomware attacks targeting NAS devices
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/synology-warns-customers-of-ongoing-c3rb3r-ransomware-attacks/)

Taiwanese network-attached storage (NAS) appliance maker Synology warned customers to update their devices immediately due to a surge in C3RB3r ransomware attacks.

> 📋 **ISO 27001:** A.8.13 Information backup

### 6. Is Your SOC Ready for AI Agents? A Maturity Check Before You Deploy
*The Hacker News* — [read more](https://thehackernews.com/2026/11/is-your-soc-ready-for-ai-agents.html)

Forty percent of security teams now use AI every day, and another 56% are testing it. Only 4% have no plans to adopt it, according to Prophet Security's State of AI in Security Operations 2026 survey of more than 250 CISOs, SOC leaders and practitioners. For the teams still testing, the next decision is whether their own SOC is ready. AI SOC readiness has two parts: whether a SOC has the

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Revolve Data Breach Impacts at Least 180,000 People
*SecurityWeek* — [read more](https://www.securityweek.com/revolve-data-breach-impacts-at-least-180000-people/)

Hackers accessed its online shopping platform and stole customers’ personal and payment card information.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 8. Chainalysis Discloses Data Breach Following AI-Driven Cyberattack
*SecurityWeek* — [read more](https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/)

The attackers used offensive agentic techniques to access the company’s systems and internal tools.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-109618** | PHP Memory Corruption Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-109619** | PHP Stale Internal Request-State Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-111497** | Google Brotli Unchecked Return Value Vulnerability | – | 83% | ⚠️ YES (KEV) |
| **CVE-2026-110447** | Collabora Online – Built-in CODE Server OS Command Injection Vulnerability | – | 73% | ⚠️ YES (KEV) |
| **CVE-2026-48356** | Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability | – | 45% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*