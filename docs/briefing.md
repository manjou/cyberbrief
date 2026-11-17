# 🛡️ CyberBrief — GRC — Tuesday, 17 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🔥 Top stories

### 1. N-able Kills Legacy APIs, Patches 17 N-central Zero-Days
*SecurityWeek* — [read more](https://www.securityweek.com/n-able-kills-legacy-apis-patches-17-n-central-zero-days/)

The patches target recently disclosed zero-days, as well as vulnerabilities already exploited in the wild.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Uber notifies drivers of data breach affecting nearly 150,000 people
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/uber-notifies-drivers-of-data-breach-affecting-nearly-150-000-people/)

Ride-hailing company Uber is notifying nearly 150,000 drivers that attackers stole their data after breaching AI infrastructure provider Fireworks in early October.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 3. Access Dental Management Data Breach Impacts Over 340,000
*SecurityWeek* — [read more](https://www.securityweek.com/access-dental-management-data-breach-impacts-over-340000/)

Hackers breached Access Dental’s network and stole personal, health, and insurance information.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 4. Fandango says hackers stole payment card details from checkout pages
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/fandango-says-hackers-stole-payment-card-details-from-checkout-pages/)

Ticket seller Fandango Media is notifying customers about a data breach that exposed payment card details entered on its checkout pages.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 5. Hackers Found a Way Around GitHub SHA Pinning. This Webinar Explains How to Close the Gap
*The Hacker News* — [read more](https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html)

Pinning GitHub Actions to an exact version of their code, known as SHA pinning, has become the go-to defense against software supply chain attacks. Attackers have already found a way around it. In March 2026, the hackers who hijacked Trivy, a widely used open-source security scanner, planted malicious code that looked like it came from GitHub's official checkout tool. They even labeled it a

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 6. Optimizely hack infected CNN, Fox News, BBC, Salesforce sites with malware
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-delivers-malware-to-cnn-fox-news-bbc-salesforce-sites/)

A suspected supply chain attack targeting Optimizely has led to malicious JavaScript being loaded on numerous popular websites, including Zoom, CNN, Fox News, BBC, Salesforce, and GitLab, exposing visitors to scripts designed to steal cryptocurrency and payment information and exploit vulnerabilities in iOS devices.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 7. 7 Tips For Complying with CJIS Password and MFA Requirements
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/7-tips-for-complying-with-cjis-password-and-mfa-requirements/)

The FBI's latest CJIS Security Policy requires law enforcement agencies to strengthen password protections and enforce MFA across privileged and non-privileged accounts. Specops Software outlines seven practical steps to meet these requirements, block compromised passwords, and maintain compliance.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 8. New GitDoor and GraphDoor Backdoors Turn GitHub and SharePoint Into Covert C2 Channels
*The Hacker News* — [read more](https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html)

Government sectors in Asia and Africa have been targeted by an active cyber intrusion campaign that delivers to previously undocumented backdoors that leverage legitimate services like Microsoft SharePoint and GitHub for command‑and‑control (C2). The activity has been codenamed Operation ShadowCloud by Kaspersky. The Russian cybersecurity company said it identified the campaign in early 2026.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.23 Cloud services security

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-123158** | OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability | – | 19% | ⚠️ YES (KEV) |
| **CVE-2026-116606** | Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 11% | ⚠️ YES (KEV) |
| **CVE-2026-111560** | Barracuda Networks Multiple Products OS Command Injection Vulnerability | – | 9% | ⚠️ YES (KEV) |
| **CVE-2026-116779** | SignalWire FreeSwitch Code Injection Vulnerability | – | 2% | ⚠️ YES (KEV) |
| **CVE-2026-123039** | Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability | – | 2% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*