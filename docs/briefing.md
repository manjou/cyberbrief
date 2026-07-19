# 🛡️ CyberBrief — Sunday, 19 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. WordPress Core "wp2shell" RCE flaws get public exploits, patch now
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/)

Public exploits have been released for the critical "wp2shell" remote code execution vulnerabilities affecting WordPress Core, making it imperative that administrators patch their sites immediately. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Update now: 7-Zip fixes RCE flaw exploitable with malicious archives
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/update-now-7-zip-fixes-rce-flaw-exploitable-with-malicious-archives/)

7-Zip version 26.02 was released to fix a remote code execution vulnerability that could allow attackers to execute malicious code by convincing users to open specially crafted compressed files. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code
*The Hacker News* — [read more](https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html)

Updated July 18, 2026: the two flaws now carry CVE IDs, the full mechanism has been published, a persistent-object-cache condition has surfaced, and a working proof-of-concept is public. The story below reflects all of it. An anonymous HTTP request can run code on a WordPress site. The bug is in core, so a bare install with zero plugins is exploitable. Every 6.9 and 7.0 site was in range until

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 4. Microsoft warns of surge in ACR Stealer attacks on customers
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-surge-in-acr-stealer-attacks-on-customers/)

Microsoft has observed a surge in attacks using the ACR Stealer malware to steal browser-stored passwords, authentication tokens, and sensitive documents from its enterprise customers. [...]

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.17 Authentication information

### 5. Abbott probes two cyber incidents amid extortion claims
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/)

Abbott Laboratories is investigating two separate cybersecurity incidents after confirming unauthorized access to internal legacy Exact Sciences systems in its Cancer Diagnostics business, while also investigating a separate claim that attackers breached its LabCentral portal and stole company data. [...]

> 📋 **ISO 27001:** A.5.24 Incident management planning

### 6. The Future of Age Verification: Your Face Never Leaves Your Device
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/the-future-of-age-verification-your-face-never-leaves-your-device/)

As age verification laws expand worldwide, organizations face growing pressure to protect users' privacy while meeting regulatory requirements. Incode explains how on-device age estimation verifies age without transmitting or storing facial images, reducing biometric privacy risks while supporting compliance. [...]

> 📋 **ISO 27001:** A.5.23 Cloud services security

### 7. Friday Squid Blogging: Squid Washing Up on Cape Cod Beach
*Schneier on Security* — [read more](https://www.schneier.com/blog/archives/2026/07/friday-squid-blogging-squid-washing-up-on-cape-cod-beach.html)

Lots of articles about this . As usual, you can also use this squid post to talk about the security stories in the news that I haven t covered. Blog moderation policy.

### 8. OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests
*The Hacker News* — [read more](https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html)

Eleven bytes will make an unpatched OpenSSL server set aside up to 131 KB of memory for a message that never arrives. On the glibc systems Okta tested, that memory is gone until the process restarts. OpenSSL shipped the HollowByte fix in June with no CVE, no advisory, and no changelog entry pointing at it. Okta's Red Team, which reported the denial-of-service bug and named it, published the

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.24 Use of cryptography

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2026-25089** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 36% | ⚠️ YES (KEV) |
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 24% | ⚠️ YES (KEV) |
| **CVE-2026-56164** | Microsoft SharePoint Server Missing Authentication for Critical Function Vulnerability | – | 6% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*