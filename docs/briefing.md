# 🛡️ CyberBrief — Net+ — Wednesday, 25 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation** — Broadcom has shipped patches to address 23 vulnerabilities impacting VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer, including one critical bug that could be abused to bypass authentication. [read more](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html)
- **Hackers now exploit critical Drupal RCE flaw to hijack sites** — The Drupal security team has confirmed that a critical vulnerability that lets attackers hijack unpatched sites has been actively exploited since at least Thursday. [read more](https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-drupal-rce-flaw-to-hijack-sites/)
- **Drupal Fail2Install Exploit Details Emerge as Critical RCE Flaw Faces Active Exploitation** — The U.S. [read more](https://thehackernews.com/2026/11/drupal-fail2install-exploit-details.html)
- **Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Label Zero-Day** — The U.S. [read more](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)
- **Hackers Exploit Two GeoServer Flaws as Researchers Warn of Unauthenticated RCE Chains** — Threat actors are actively exploiting two newly patched security flaws in GeoServer, according to watchTowr. [read more](https://thehackernews.com/2026/11/hackers-exploit-two-geoserver-flaws-as.html)
- **InfraTrust warns of exploited supply chain flaws in network appliances** — Eclypsium's November InfraTrust report warns that most infrastructure security advisories addressing exploited vulnerabilities over the past month involve flaws in third-party software bundled into products rather than code developed by the vendors themselves. [read more](https://www.bleepingcomputer.com/news/security/infratrust-warns-of-exploited-supply-chain-flaws-in-network-appliances/)
- **Hackers Found a Way Around GitHub SHA Pinning. This Webinar Explains How to Close the Gap** — Pinning GitHub Actions to an exact version of their code, known as SHA pinning, has become the go-to defense against software supply chain attacks. [read more](https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html)
- **Two Newly Disclosed GeoServer Vulnerabilities Under Attack** — Attackers are probing GeoServer instances for two high-severity flaws that can be chained with other bugs for unauthenticated RCE. [read more](https://www.securityweek.com/two-newly-disclosed-geoserver-vulnerabilities-under-attack/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2024-10441 (– CVSS, 3% EPSS)

## 🔥 Top stories

### 1. VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation
*The Hacker News* — [read more](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html)

Broadcom has shipped patches to address 23 vulnerabilities impacting VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer, including one critical bug that could be abused to bypass authentication. The critical vulnerability, tracked as CVE-2026-123903, is rated 9.8 out of 10.0 on the CVSS scoring system. It resides in the VMware Directory Service ("vmdir"). "A malicious actor with

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 2. Hackers now exploit critical Drupal RCE flaw to hijack sites
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-drupal-rce-flaw-to-hijack-sites/)

The Drupal security team has confirmed that a critical vulnerability that lets attackers hijack unpatched sites has been actively exploited since at least Thursday.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Drupal Fail2Install Exploit Details Emerge as Critical RCE Flaw Faces Active Exploitation
*The Hacker News* — [read more](https://thehackernews.com/2026/11/drupal-fail2install-exploit-details.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a critical flaw impacting Drupal to its Known Exploited Vulnerabilities (KEV) catalog, requiring federal agencies to apply the fixes by November 27, 2026. The vulnerability, tracked as CVE-2026-132165 aka Fail2Install (CVSS score: 9.8), is a case of remote code execution (RCE) impacting Drupal core. "Drupal Core

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Label Zero-Day
*The Hacker News* — [read more](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added two flaws impacting N-able MailAssure and MONAI Label to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The critical vulnerabilities are listed below - CVE-2026-134624 (CVSS score: 9.3) - A server-side request forgery (SSRF) vulnerability in N-able MailAssure's LDAP

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. Hackers Exploit Two GeoServer Flaws as Researchers Warn of Unauthenticated RCE Chains
*The Hacker News* — [read more](https://thehackernews.com/2026/11/hackers-exploit-two-geoserver-flaws-as.html)

Threat actors are actively exploiting two newly patched security flaws in GeoServer, according to watchTowr. The vulnerabilities in question are CVE-2026-120705 and CVE-2026-129243, details of which are below - CVE-2026-120705 (CVSS score: 8.6) - An arbitrary file read vulnerability that could enable an attacker to access local text files readable by the GeoServer process or fetch

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 6. InfraTrust warns of exploited supply chain flaws in network appliances
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/infratrust-warns-of-exploited-supply-chain-flaws-in-network-appliances/)

Eclypsium's November InfraTrust report warns that most infrastructure security advisories addressing exploited vulnerabilities over the past month involve flaws in third-party software bundled into products rather than code developed by the vendors themselves.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 7. Hackers Found a Way Around GitHub SHA Pinning. This Webinar Explains How to Close the Gap
*The Hacker News* — [read more](https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html)

Pinning GitHub Actions to an exact version of their code, known as SHA pinning, has become the go-to defense against software supply chain attacks. Attackers have already found a way around it. In March 2026, the hackers who hijacked Trivy, a widely used open-source security scanner, planted malicious code that looked like it came from GitHub's official checkout tool. They even labeled it a

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 8. Two Newly Disclosed GeoServer Vulnerabilities Under Attack
*SecurityWeek* — [read more](https://www.securityweek.com/two-newly-disclosed-geoserver-vulnerabilities-under-attack/)

Attackers are probing GeoServer instances for two high-severity flaws that can be chained with other bugs for unauthenticated RCE.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2024-10441** | Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability | – | 3% | ⚠️ YES (KEV) · ransomware |
| **CVE-2026-123890** | VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 5% | ⚠️ YES (KEV) |
| **CVE-2026-76466** | Cisco Expressway Series Use of Hard-coded Credentials Vulnerability | – | 1% | ⚠️ YES (KEV) |
| **CVE-2026-103406** | Hewlett Packard Enterprise (HPE) Juniper Session Smart Conductor and Session Smart Router OS Command Injection Vulnerability | – | 1% | ⚠️ YES (KEV) |
| **CVE-2026-123039** | Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability | – | 0% | ⚠️ YES (KEV) |

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