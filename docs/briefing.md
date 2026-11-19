# 🛡️ CyberBrief — SOC — Thursday, 19 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. Critical Apache Roller RCE Flaw Under Active Exploitation, No Authentication Required
*The Hacker News* — [read more](https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html)

A critical security flaw in Apache Roller, an open-source, Java-based blogging platform, has come under active exploitation in the wild, according to the Apache Software Foundation (ASF) The vulnerability, tracked as CVE-2026-129448 (CVSS score: 9.8), is a case of unauthenticated deserialization in the XML-RPC endpoint that could lead to remote code execution. "Deserialization of Untrusted

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 2. Drupal patches critical RCE flaw, warns exploits may surface quickly
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/)

The Drupal Security Team has patched a critical remote code execution vulnerability that can let attackers take over vulnerable sites.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. CISA Warns of 4 Exploited Flaws Linked to Ransomware, Cryptomining, and LLMjacking Attacks
*The Hacker News* — [read more](https://thehackernews.com/2026/11/cisa-warns-of-4-exploited-flaws-linked.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added four vulnerabilities impacting Synology DiskStation Manager (DSM), BerriAI LiteLLM, Apache Axis, and Vanderbilt University Research Electronic Data Capture (REDCap) to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerabilities are listed below -

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 4. Ruby Releases Fixes for 7 Regex and String Flaws, Warns 5 Have Proof-of-Concept RCE
*The Hacker News* — [read more](https://thehackernews.com/2026/11/ruby-releases-fixes-for-7-regex-and.html)

Ruby contains seven memory-safety flaws in its regular expression engine and its string case-conversion code. For five of them, its maintainers say, proof-of-concept exploits, or PoCs, have shown that crafted input can run code on the machine. "We are aware of PoCs that prove some of them can be used to trigger remote code execution," the maintainers said. The project released fixed versions

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. NVIDIA investigating Gentlemen ransomware breach claims
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/nvidia-investigating-gentlemen-ransomware-breach-claims/)

NVIDIA is investigating claims of a security breach after the Gentlemen ransomware group has added the company to its dark web data leak site.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.34 Privacy and protection of PII

### 6. Apache warns of Roller RCE vulnerability exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/apache-warns-of-roller-rce-vulnerability-exploited-in-attacks/)

Apache has released security updates to address a critical Roller flaw that threat actors are exploiting to gain code execution on vulnerable servers.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Hackers Exploiting Critical Puppet RCE Flaw Affecting Enterprise Management Servers
*The Hacker News* — [read more](https://thehackernews.com/2026/11/hackers-exploiting-critical-puppet-rce.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a critical security flaw impacting Perforce Puppet, an enterprise infrastructure-as-code (IaC) and configuration management platform, to its Known Exploited Vulnerabilities (KEV) catalog, citing reports of active exploitation. The vulnerability, tracked as CVE-2026-115731 (CVSS score: 9.4), is a case of

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. 10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on Servers
*The Hacker News* — [read more](https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html)

A flaw in NGINX's HTTP/2 support can allow an attacker to run code on servers with HTTP/2 enabled, without needing to log in. The decade-old flaw, CVE-2026-123007, dubbed "nginx2root," has been present in NGINX's open-source code since version 1.9.5, released on September 22, 2015. Fixed versions 1.31.9 and 1.30.7 came out today. F5, the company behind NGINX, says attackers can run code where

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-40217** | BerriAI LiteLLM Unprotected Alternate Channel Vulnerability | – | 62% | ⚠️ YES (KEV) |
| **CVE-2026-90817** | Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability | – | 25% | ⚠️ YES (KEV) |
| **CVE-2026-116779** | SignalWire FreeSwitch Code Injection Vulnerability | – | 22% | ⚠️ YES (KEV) |
| **CVE-2026-123158** | OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability | – | 19% | ⚠️ YES (KEV) |
| **CVE-2026-116606** | Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 11% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*