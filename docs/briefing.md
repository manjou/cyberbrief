# 🛡️ CyberBrief — SOC — Monday, 17 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **SafePal data breach impacts 39,798 customers, stolen info for sale** — SafePal, a company that makes hardware wallets for storing cryptocurrency, had a security flaw that allowed attackers to steal customer order information from about 39,798 people. [read more](https://www.bleepingcomputer.com/news/security/safepal-data-breach-impacts-39-798-customers-stolen-info-for-sale/)
- **New AmnesiaStealer macOS malware hijacks browser sessions via remote control** — A new malware called AmnesiaStealer is infecting macOS computers through ClickFix attacks (fake tech support pop-ups), and it can remotely hijack a victim's web browser sessions in real-time. [read more](https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/)
- **[UPDATE] [kritisch] SAP Patch Day August 2026: Mehrere Schwachstellen** — SAP, a widely-used enterprise software platform, released multiple critical security patches for August 2026 that fix flaws allowing attackers to run unauthorized code, escalate privileges (gain higher access levels), bypass security controls, and steal sensitive data or login credentials. [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2746)
- **[UPDATE] [hoch] GStreamer: Mehrere Schwachstellen** — GStreamer, a widely-used multimedia library that many applications depend on, has multiple vulnerabilities that attackers can exploit to corrupt data, cause denial-of-service (crash or freeze systems), leak sensitive information, or potentially run arbitrary code. [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2662)
- **[UPDATE] [mittel] Wireshark: Mehrere Schwachstellen ermöglichen Denial of Service** — Wireshark, a network analysis tool used by IT professionals, contains multiple vulnerabilities that remote attackers can exploit to cause denial-of-service attacks (making Wireshark crash or become unusable). [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2806)
- **ISC Stormcast For Monday, August 17th, 2026 https://isc.sans.edu/podcastdetail/10054, (Mon, Aug 17th)** — This is a reference to a cybersecurity podcast episode from the SANS Internet Storm Center; no specific incident details are provided in the entry. [read more](https://isc.sans.edu/diary/rss/33250)
- **Anthropic confirms Claude is down in major outage affecting multiple services** — Anthropic's Claude AI service experienced a major outage affecting multiple services, with users unable to log in and experiencing degraded performance. [read more](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-confirms-claude-is-down-in-major-outage-affecting-multiple-services/)
- **Wireshark 4.6.8 Released, (Sun, Aug 16th)** — Wireshark released version 4.6.8, which fixes 28 security vulnerabilities and 25 software bugs. [read more](https://isc.sans.edu/diary/rss/33248)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-8037 (– CVSS, 99% EPSS)

## 🔥 Top stories

### 1. SafePal data breach impacts 39,798 customers, stolen info for sale
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/safepal-data-breach-impacts-39-798-customers-stolen-info-for-sale/)

SafePal, a company that makes hardware wallets for storing cryptocurrency, had a security flaw that allowed attackers to steal customer order information from about 39,798 people. This matters because the stolen data (names, addresses, payment details) can be used for fraud, identity theft, or targeted phishing attacks against cryptocurrency users. Defenders typically notify affected customers, investigate how the flaw was exploited, patch the vulnerability, monitor for data being sold on dark web markets, and may offer credit monitoring services.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 2. New AmnesiaStealer macOS malware hijacks browser sessions via remote control
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/)

A new malware called AmnesiaStealer is infecting macOS computers through ClickFix attacks (fake tech support pop-ups), and it can remotely hijack a victim's web browser sessions in real-time. This matters because an attacker can impersonate the victim, steal login credentials, transfer money, or access sensitive accounts while the victim watches. Defenders typically block ClickFix domains, educate users not to click suspicious pop-ups, monitor for AmnesiaStealer signatures, and recommend keeping macOS and browsers patched.

> 📋 **ISO 27001:** A.8.7 Protection against malware

### 3. [UPDATE] [kritisch] SAP Patch Day August 2026: Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2746)

SAP, a widely-used enterprise software platform, released multiple critical security patches for August 2026 that fix flaws allowing attackers to run unauthorized code, escalate privileges (gain higher access levels), bypass security controls, and steal sensitive data or login credentials. This matters because SAP systems often contain critical business and financial data, so compromises can have severe business impact across entire organizations. Defenders typically apply patches immediately on a priority schedule, test them in staging environments first, scan systems for signs of exploitation, and prioritize SAP systems in their update schedules.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. [UPDATE] [hoch] GStreamer: Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2662)

GStreamer, a widely-used multimedia library that many applications depend on, has multiple vulnerabilities that attackers can exploit to corrupt data, cause denial-of-service (crash or freeze systems), leak sensitive information, or potentially run arbitrary code. This matters because GStreamer is embedded in many applications and operating systems, so a single flaw can affect numerous programs across many users. Defenders typically update GStreamer immediately, check which applications and systems use it, test updates in non-production environments first, and monitor for exploitation attempts.

### 5. [UPDATE] [mittel] Wireshark: Mehrere Schwachstellen ermöglichen Denial of Service
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2806)

Wireshark, a network analysis tool used by IT professionals, contains multiple vulnerabilities that remote attackers can exploit to cause denial-of-service attacks (making Wireshark crash or become unusable). This matters because compromised analysis tools can disrupt security monitoring or be weaponized if an attacker tricks an analyst into opening a malicious file. Defenders typically update Wireshark promptly, avoid opening untrusted packet capture files, and warn users about the vulnerability.

> 📋 **ISO 27001:** A.8.6 Capacity management

### 6. ISC Stormcast For Monday, August 17th, 2026 https://isc.sans.edu/podcastdetail/10054, (Mon, Aug 17th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33250)

This is a reference to a cybersecurity podcast episode from the SANS Internet Storm Center; no specific incident details are provided in the entry. Without knowing the podcast content, no vulnerability or incident can be assessed. Defenders would typically listen to the podcast to learn about current threats and update their security strategies accordingly.

### 7. Anthropic confirms Claude is down in major outage affecting multiple services
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-confirms-claude-is-down-in-major-outage-affecting-multiple-services/)

Anthropic's Claude AI service experienced a major outage affecting multiple services, with users unable to log in and experiencing degraded performance. This matters because service outages can disrupt workflows for many organizations relying on Claude, and extended outages may indicate a security incident or infrastructure compromise. Defenders typically check official status pages, communicate with their teams, implement backup solutions, monitor for similar issues, and wait for the vendor to restore service and provide a public incident report.

> 📋 **ISO 27001:** A.8.6 Capacity management

### 8. Wireshark 4.6.8 Released, (Sun, Aug 16th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33248)

Wireshark released version 4.6.8, which fixes 28 security vulnerabilities and 25 software bugs. This matters because each vulnerability could have been exploited by attackers to crash the tool or execute code if users opened malicious files. Defenders typically schedule and deploy this update to all systems using Wireshark, prioritizing it as a security patch, and note the fixes for compliance documentation.

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-8037** | Progress LoadMaster Command Injection Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-34486** | Apache Tomcat Missing Encryption of Sensitive Data Vulnerability | – | 83% | ⚠️ YES (KEV) |
| **CVE-2026-9198** | IBM Langflow Code Injection Vulnerability | – | 17% | ⚠️ YES (KEV) |
| **CVE-2026-63077** | JetBrains TeamCity Deserialization of Untrusted Data Vulnerability | – | 11% | ⚠️ YES (KEV) |
| **CVE-2026-72898** | Metabase SQL Injection Vulnerability | – | 10% | ⚠️ YES (KEV) |

**CVE-2026-8037** — Progress LoadMaster, a load-balancing appliance used to distribute network traffic, has a command injection vulnerability (CVE-2026-8037) allowing attackers to run arbitrary system commands. This matters because LoadMaster sits between users and critical applications, so compromising it could allow attackers to intercept traffic, access backend systems, or disrupt services. Defenders typically apply vendor patches, restrict network access to LoadMaster, monitor for suspicious commands in logs, and check for signs of prior exploitation.

**CVE-2026-34486** — Apache Tomcat, a widely-used web application server, has a vulnerability (CVE-2026-34486) where sensitive data is not properly encrypted in storage or transmission. This matters because unencrypted sensitive data can be stolen if an attacker gains access to the server or intercepts network traffic, potentially exposing user credentials, payment information, or personal data. Defenders typically apply the patch, audit their Tomcat configurations to ensure encryption is enabled, review access logs for suspicious activity, and consider re-encrypting any data that may have been exposed.

**CVE-2026-9198** — IBM Langflow, an AI workflow development platform, contains a code injection vulnerability (CVE-2026-9198) allowing attackers to inject and execute malicious code. This matters because an attacker can run arbitrary code within the Langflow environment to steal data, modify workflows, or compromise systems connected to it. Defenders typically update Langflow immediately, validate that workflows have not been tampered with, audit access logs, and restrict who can modify workflows.

**CVE-2026-63077** — JetBrains TeamCity, a continuous integration/continuous deployment (CI/CD) tool used to automate software builds and deployments, has a deserialization vulnerability (CVE-2026-63077) where untrusted data is processed in an unsafe way. This matters because CI/CD tools have high privileges in development environments, so compromising them can allow attackers to inject malicious code into software builds or access source code repositories. Defenders typically patch TeamCity urgently, review build logs for suspicious activity, audit who has access to the system, and consider re-building any software compiled after the vulnerability was introduced.

**CVE-2026-72898** — Metabase, a business intelligence and data visualization tool, contains a SQL injection vulnerability (CVE-2026-72898) allowing attackers to craft malicious queries to access unauthorized data. This matters because Metabase often connects to sensitive business databases and data warehouses, so SQL injection can expose financial records, customer data, or other confidential information. Defenders typically apply the patch, audit Metabase access logs for suspicious queries, review database permissions, validate that no unauthorized data was accessed, and implement query monitoring.

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*