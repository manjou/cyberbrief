# 🛡️ CyberBrief — GRC — Tuesday, 06 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre v2 and Ransomware Arrests** — NetScaler, FortiMail, and other widely-used products have unpatched security flaws (called 0-days) that attackers are actively exploiting, plus AI tools leaked that help attackers write malicious code faster. [read more](https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html)
- **Nikkei discloses breaches of employees’ Microsoft, Google email accounts** — Attackers broke into two employee email accounts at Nikkei (a major Japanese publisher) and used one account to send thousands of phishing emails to trick other people into revealing credentials. [read more](https://www.bleepingcomputer.com/news/security/nikkei-discloses-breaches-of-employees-microsoft-google-email-accounts/)
- **8.8 Million Impacted by Data Breach at Denmark’s Central Person Register** — A company with authorized access to Denmark's Central Person Register (a government database of citizen records) was hacked, and attackers stole personal data on 8.8 million people using that company's legitimate access rights. [read more](https://www.securityweek.com/8-8-million-impacted-by-data-breach-at-denmarks-central-person-register/)
- **Rejetto HFS servers now actively scanned for critical RCE flaw** — Attackers are actively scanning the internet for servers running Rejetto HFS software with a known critical flaw (CVE-2026-61500) that lets them forge sessions, take over accounts, or run code remotely. [read more](https://www.bleepingcomputer.com/news/security/rejetto-hfs-servers-now-actively-scanned-for-critical-rce-flaw/)
- **Denmark population registry data breach affects 8.8 million people** — Denmark's Central Population Register (a government database storing personal details on 8.8 million citizens) was breached and personal information was stolen; this is the same incident as item 3 but framed from the registry operator's perspective. [read more](https://www.bleepingcomputer.com/news/security/denmark-population-registry-data-breach-affects-88-million-people/)
- **Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports** — Google stopped accepting vulnerability reports through its bug bounty program for open-source projects like Go and Angular because too many automated tools were submitting invalid or low-quality reports, wasting researcher time. [read more](https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html)
- **250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms** — Hackers stole patient information (names, addresses, medical records, insurance details) from two US healthcare companies in July; about 250,000 people were affected. [read more](https://www.securityweek.com/250000-impacted-by-data-breaches-at-new-jersey-texas-healthcare-firms/)
- **Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products** — A critical flaw in 8 Atlassian products (self-hosted, not cloud versions) allows an attacker to read files from the web application directory without logging in, but only if they already know the exact file name and path. [read more](https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-71362 (– CVSS, 88% EPSS)

## 🔥 Top stories

### 1. ⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre v2 and Ransomware Arrests
*The Hacker News* — [read more](https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html)

NetScaler, FortiMail, and other widely-used products have unpatched security flaws (called 0-days) that attackers are actively exploiting, plus AI tools leaked that help attackers write malicious code faster. This matters because these are trusted infrastructure products, so compromises can affect many organizations at once. Defenders need to monitor vendor advisories closely, patch immediately when fixes arrive, and watch network traffic for signs of exploitation while waiting for patches.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 2. Nikkei discloses breaches of employees’ Microsoft, Google email accounts
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/nikkei-discloses-breaches-of-employees-microsoft-google-email-accounts/)

Attackers broke into two employee email accounts at Nikkei (a major Japanese publisher) and used one account to send thousands of phishing emails to trick other people into revealing credentials. This matters because compromised email accounts give attackers a trusted sender identity, making phishing much more effective and potentially giving them access to sensitive business or customer information. Defenders typically enable multi-factor authentication (MFA) on email, monitor for unusual email sending patterns, and train employees to verify unexpected requests through a second channel.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.8.2 Privileged access rights

### 3. 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register
*SecurityWeek* — [read more](https://www.securityweek.com/8-8-million-impacted-by-data-breach-at-denmarks-central-person-register/)

A company with authorized access to Denmark's Central Person Register (a government database of citizen records) was hacked, and attackers stole personal data on 8.8 million people using that company's legitimate access rights. This matters because it shows that insider access or compromised trusted accounts can bypass many security controls—the attacker didn't break in through a weak firewall, they used a door that was supposed to be open. Defenders focus on limiting what data each user can access (least privilege), logging all data access, and detecting unusual query patterns that suggest misuse.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 4. Rejetto HFS servers now actively scanned for critical RCE flaw
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/rejetto-hfs-servers-now-actively-scanned-for-critical-rce-flaw/)

Attackers are actively scanning the internet for servers running Rejetto HFS software with a known critical flaw (CVE-2026-61500) that lets them forge sessions, take over accounts, or run code remotely. This matters because active scanning means exploitation is happening now, not just a theoretical risk, and many organizations may not know they're running this software. Defenders need to inventory all HFS servers, apply the security patch immediately, or disable the service if it's not essential, and monitor network logs for scan traffic.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Denmark population registry data breach affects 8.8 million people
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/denmark-population-registry-data-breach-affects-88-million-people/)

Denmark's Central Population Register (a government database storing personal details on 8.8 million citizens) was breached and personal information was stolen; this is the same incident as item 3 but framed from the registry operator's perspective. This matters because it affects nearly the entire population of a country, creating risk of identity theft and fraud at massive scale. Defenders and the government typically notify affected citizens, offer credit monitoring, increase authentication requirements for database queries, and investigate how the trusted company's access was compromised.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 6. Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports
*The Hacker News* — [read more](https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html)

Google stopped accepting vulnerability reports through its bug bounty program for open-source projects like Go and Angular because too many automated tools were submitting invalid or low-quality reports, wasting researcher time. This matters because it reduces incentive for security researchers to find bugs in widely-used open-source code, which might slow vulnerability discovery and leave more flaws unpatched. Defenders should still report vulnerabilities through other channels (direct vendor contact, GitHub security advisories) and continue monitoring these projects for fixes released independently.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 7. 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms
*SecurityWeek* — [read more](https://www.securityweek.com/250000-impacted-by-data-breaches-at-new-jersey-texas-healthcare-firms/)

Hackers stole patient information (names, addresses, medical records, insurance details) from two US healthcare companies in July; about 250,000 people were affected. This matters because healthcare data is sensitive and regulated, and attackers often sell it on dark markets or use it for identity theft and insurance fraud. Defenders in healthcare must encrypt patient data at rest and in transit, limit access to patient records by role, undergo regular security audits, and notify affected individuals as required by law.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 8. Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products
*The Hacker News* — [read more](https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html)

A critical flaw in 8 Atlassian products (self-hosted, not cloud versions) allows an attacker to read files from the web application directory without logging in, but only if they already know the exact file name and path. This matters because attackers can extract configuration files, credentials, or keys that are sometimes stored in predictable locations, giving them a foothold for further attacks. Defenders must patch all 8 affected products immediately, move sensitive files outside the web root, and use file permissions to restrict what the web application can read.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-71362** | Adobe Commerce and Magento Incorrect Authorization Vulnerability  | – | 88% | ⚠️ YES (KEV) |
| **CVE-2026-87902** | WordPress Core Remote File Inclusion Vulnerability | – | 46% | ⚠️ YES (KEV) |
| **CVE-2026-93616** | Check Point Multiple Products Path Traversal Vulnerability | – | 20% | ⚠️ YES (KEV) |
| **CVE-2026-85102** | Check Point Multiple Products Improper Certificate Validation Vulnerability | – | 8% | ⚠️ YES (KEV) |
| **CVE-2026-104286** | Fortinet FortiMail Path Traversal Vulnerability | – | 2% | ⚠️ YES (KEV) |

**CVE-2026-71362** — Adobe Commerce and Magento contain an authorization flaw (CVE-2026-71362) that likely allows users to access or modify data they shouldn't have permission to see, such as other customers' orders or admin settings. This matters because it can lead to data theft, financial loss, or store takeover if exploited. Defenders must patch immediately, review access logs for suspicious activity, and verify that role-based permission checks are working correctly after patching.

**CVE-2026-87902** — WordPress Core contains a remote file inclusion flaw (CVE-2026-87902) that lets an attacker load and execute arbitrary code by tricking the application into including malicious files from the internet. This matters because WordPress powers millions of websites, so this flaw is a wide-target opportunity for large-scale compromises. Defenders must update WordPress immediately, remove unnecessary plugins and themes, disable PHP file uploads, and monitor for requests that try to include suspicious URLs.

**CVE-2026-93616** — Check Point products have a path traversal vulnerability (CVE-2026-93616) that lets attackers read or write files outside the intended directory by using special characters like `../` in file paths. This matters because attackers can reach configuration files, logs, or system files that contain credentials and secrets. Defenders must patch immediately, apply strict input validation to file path requests, and restrict file system permissions so the application runs with minimal access.

**CVE-2026-85102** — Check Point products fail to properly validate SSL/TLS certificates (CVE-2026-85102), which means an attacker could potentially perform a man-in-the-middle attack and intercept encrypted traffic without the application detecting the forgery. This matters because it undermines the trust placed in encrypted connections and could let attackers steal credentials or data sent over "secure" connections. Defenders must patch immediately, verify certificate pinning is enabled where applicable, and monitor for suspicious certificate warnings in logs.

**CVE-2026-104286** — Fortinet FortiMail contains a path traversal vulnerability (CVE-2026-85102) that allows attackers to read files outside the intended mail directory by crafting malicious file paths. This matters because email systems often store logs, temporary files, and configuration data that contain passwords, encryption keys, or user information. Defenders must patch immediately, apply strict input filtering on file paths, and restrict the file system permissions of the FortiMail service account.

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*