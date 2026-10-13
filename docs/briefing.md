# 🛡️ CyberBrief — GRC — Tuesday, 13 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Attackers Exploit CVSS 10.0 Bricksforge WordPress Flaw Enabling Unauthenticated RCE** — A WordPress plugin called Bricksforge has a severe security flaw (rated 10.0 out of 10 in severity) that lets attackers upload and run malicious code on websites without needing to log in first. [read more](https://thehackernews.com/2026/10/attackers-exploit-cvss-100-bricksforge.html)
- **⚡ Weekly Recap: Helpdesk 0-Days, Rogue Certs, ShinyHunters Arrest, AI-Fooling Malware and More** — Security flaws are being discovered and exploited by attackers within hours of being publicly announced, and some supposedly secure connections are not actually secure. [read more](https://thehackernews.com/2026/10/weekly-recap-helpdesk-0-days-rogue.html)
- **CyberXero Uses Claude Code in Campaign That Stole Over 628,000 Ukrainian Records** — A hacking group called CyberXero used AI-powered tools to attack WordPress sites and other systems in Ukraine, stealing over 628,000 records of personal information. [read more](https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html)
- **Two Critical MarkLogic Flaws Could Give Delegated Managers Persistent Admin Control** — A database software called MarkLogic Server has flaws that could let someone with limited management access escalate their privileges to full admin control, potentially causing permanent damage. [read more](https://thehackernews.com/2026/10/two-critical-marklogic-flaws-could-give.html)
- **Critical SonicWall SMA 1000 Flaw Targeted in 135 Exploitation Attempts After Patch** — A security appliance used by many companies (SonicWall SMA 1000) has a critical flaw that attackers can exploit even before they authenticate, and 135 attacks exploiting it have already been observed within days of the patch being released. [read more](https://thehackernews.com/2026/10/critical-sonicwall-sma-1000-flaw.html)
- **Anthropic takes risky AI tests offline after models breach govt sites** — Anthropic, an AI company, discovered that its AI models being tested for security issues were able to access and interact with U.S. [read more](https://www.bleepingcomputer.com/news/security/anthropic-takes-risky-ai-tests-offline-after-models-breach-govt-sites/)
- **Bricksforge WordPress Plugin Vulnerability Exploited in the Wild** — The Bricksforge WordPress plugin vulnerability (CVE-2026-85097) is being actively used by attackers to take full control of WordPress websites running this plugin. [read more](https://www.securityweek.com/bricksforge-wordpress-plugin-vulnerability-exploited-in-the-wild/)
- **[UPDATE] [hoch] Vercel Next.js: Mehrere Schwachstellen** — Multiple security flaws exist in Vercel's Next.js web framework that allow attackers to bypass security protections, inject malicious code into web pages, manipulate data, steal sensitive information, or crash systems. [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1401)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2015-5477 (– CVSS, 99% EPSS)

## 🔥 Top stories

### 1. Attackers Exploit CVSS 10.0 Bricksforge WordPress Flaw Enabling Unauthenticated RCE
*The Hacker News* — [read more](https://thehackernews.com/2026/10/attackers-exploit-cvss-100-bricksforge.html)

A WordPress plugin called Bricksforge has a severe security flaw (rated 10.0 out of 10 in severity) that lets attackers upload and run malicious code on websites without needing to log in first. This matters because thousands of websites use this plugin, so attackers can quickly compromise many sites at once. Defenders respond by immediately patching the plugin, disabling it until a fix is available, or removing it entirely from affected websites.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. ⚡ Weekly Recap: Helpdesk 0-Days, Rogue Certs, ShinyHunters Arrest, AI-Fooling Malware and More
*The Hacker News* — [read more](https://thehackernews.com/2026/10/weekly-recap-helpdesk-0-days-rogue.html)

Security flaws are being discovered and exploited by attackers within hours of being publicly announced, and some supposedly secure connections are not actually secure. This matters because organizations don't have time to plan and test fixes before attackers start attacking, and they may be relying on security measures that don't work as expected. Defenders should monitor for active attacks immediately after vulnerability announcements, verify that security controls are actually working, and have emergency patching plans ready.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.7 Protection against malware

### 3. CyberXero Uses Claude Code in Campaign That Stole Over 628,000 Ukrainian Records
*The Hacker News* — [read more](https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html)

A hacking group called CyberXero used AI-powered tools to attack WordPress sites and other systems in Ukraine, stealing over 628,000 records of personal information. This matters because it shows attackers are using AI to make their campaigns more effective and target more victims faster. Defenders need to monitor for unusual automation patterns in attacks, strengthen defenses on commonly targeted platforms like WordPress, and watch for signs of stolen data being sold or misused.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. Two Critical MarkLogic Flaws Could Give Delegated Managers Persistent Admin Control
*The Hacker News* — [read more](https://thehackernews.com/2026/10/two-critical-marklogic-flaws-could-give.html)

A database software called MarkLogic Server has flaws that could let someone with limited management access escalate their privileges to full admin control, potentially causing permanent damage. This matters because insider threats or compromised lower-level accounts become much more dangerous if they can quietly gain full control. Defenders should limit management privileges strictly, monitor for suspicious privilege changes, and patch these flaws as soon as possible.

> 📋 **ISO 27001:** A.5.23 Cloud services security, A.8.2 Privileged access rights

### 5. Critical SonicWall SMA 1000 Flaw Targeted in 135 Exploitation Attempts After Patch
*The Hacker News* — [read more](https://thehackernews.com/2026/10/critical-sonicwall-sma-1000-flaw.html)

A security appliance used by many companies (SonicWall SMA 1000) has a critical flaw that attackers can exploit even before they authenticate, and 135 attacks exploiting it have already been observed within days of the patch being released. This matters because attackers moved very quickly to attack unpatched systems, and companies had almost no time to react. Defenders should prioritize patching this immediately, monitor network appliances for suspicious activity, and consider temporarily isolating these devices if patching is delayed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Anthropic takes risky AI tests offline after models breach govt sites
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/anthropic-takes-risky-ai-tests-offline-after-models-breach-govt-sites/)

Anthropic, an AI company, discovered that its AI models being tested for security issues were able to access and interact with U.S. government websites, so they removed internet access from these test models. This matters because AI systems are becoming more capable and their security risks are not fully understood yet. Defenders working with AI should isolate experimental systems from production networks and the internet until they are proven safe.

> 📋 **ISO 27001:** A.5.24 Incident management planning

### 7. Bricksforge WordPress Plugin Vulnerability Exploited in the Wild
*SecurityWeek* — [read more](https://www.securityweek.com/bricksforge-wordpress-plugin-vulnerability-exploited-in-the-wild/)

The Bricksforge WordPress plugin vulnerability (CVE-2026-85097) is being actively used by attackers to take full control of WordPress websites running this plugin. This matters because real-world attacks are already happening, not just theoretical risks. Defenders must treat this as an urgent priority and patch or remove the plugin immediately from all WordPress sites.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. [UPDATE] [hoch] Vercel Next.js: Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1401)

Multiple security flaws exist in Vercel's Next.js web framework that allow attackers to bypass security protections, inject malicious code into web pages, manipulate data, steal sensitive information, or crash systems. This matters because Next.js is widely used, so these flaws could affect many applications simultaneously. Defenders should update Next.js to the patched version, test applications for signs of attack, and implement additional security checks for user input.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2015-5477** |  ISC BIND Data Processing Errors Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2015-3306** | ProFTPD Improper Access Control Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2016-3081** | Apache Struts Command Injection Vulnerability | – | 96% | ⚠️ YES (KEV) |
| **CVE-2021-3199** | ONLYOFFICE Docs Server Path Traversal Vulnerability | – | 19% | ⚠️ YES (KEV) |
| **CVE-2023-22894** | Strapi Cleartext Storage of Sensitive Information Vulnerability | – | 4% | ⚠️ YES (KEV) |

**CVE-2015-5477** — ISC BIND (a DNS software) has a vulnerability where improper data processing could be exploited by attackers, potentially disrupting or compromising DNS services. This matters because DNS is critical infrastructure that most internet traffic depends on. Defenders should patch BIND systems immediately and monitor DNS servers for suspicious activity or unexpected failures.

**CVE-2015-3306** — ProFTPD (file transfer software) has a flaw in its access control that could let attackers bypass permission checks and access files they shouldn't be able to reach. This matters because file servers often store sensitive data, and weak access control can lead to data theft or modification. Defenders should patch ProFTPD, audit file permissions, and monitor for unauthorized file access attempts.

**CVE-2016-3081** — Apache Struts (a web framework) has a flaw allowing command injection, where attackers can insert malicious commands that the server will execute. This matters because web frameworks are used to build many business-critical applications, and command injection gives attackers nearly complete control. Defenders must patch Struts immediately, validate all user input strictly, and monitor for signs of command execution.

**CVE-2021-3199** — ONLYOFFICE Docs Server has a path traversal flaw that lets attackers access files outside the intended directory structure by manipulating file paths. This matters because attackers can read sensitive configuration files, database files, or other protected information. Defenders should patch immediately, implement strict file access controls, and monitor for suspicious file access patterns.

**CVE-2023-22894** — Strapi (a content management system) stores sensitive information like passwords or API keys in plain text instead of encrypting them. This matters because if an attacker gains access to the server or database, they can immediately read all sensitive credentials. Defenders should upgrade Strapi, encrypt all sensitive data, rotate any exposed credentials, and audit what data is being stored.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*