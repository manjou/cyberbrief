# 🛡️ CyberBrief — GRC — Friday, 25 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Attackers Exploit WordPress CVE-2026-87902 Within Hours of Disclosure** — A serious WordPress security flaw (CVE-2026-87902) was publicly announced, and within hours, attackers began using it to break into websites and take complete control of them. [read more](https://thehackernews.com/2026/09/attackers-exploit-wordpress-cve-2026.html)
- **Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild** — A security weakness in Roundcube Webmail (CVE-2026-48842) that lets attackers access databases without logging in is being actively used in real attacks. [read more](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html)
- **CISA: Ransomware gangs now exploiting critical TeamCity flaw** — Criminal ransomware groups are exploiting a TeamCity flaw (a software build tool) that JetBrains fixed back in July, and U.S. [read more](https://www.bleepingcomputer.com/news/security/cisa-ransomware-gangs-now-exploiting-critical-teamcity-flaw/)
- **WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV** — Two serious security flaws in WSO2 and Adobe Commerce were found being actively exploited, so CISA added them to a public list of known-exploited vulnerabilities that defenders should prioritize. [read more](https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html)
- **Hackers now exploit critical Roundcube flaw in code injection attacks** — A high-severity flaw in Roundcube Webmail from May that was patched is now being used in real attacks to inject malicious code. [read more](https://www.bleepingcomputer.com/news/security/critical-roundcube-flaw-now-actively-exploited-in-code-injection-attacks/)
- **Hackers steal $351.6 million in Bitget crypto exchange hack** — North Korean hackers stole $351.6 million from Bitget, a cryptocurrency exchange, by accessing their hot wallets (funds kept online for quick transactions) and warm wallets (semi-active storage). [read more](https://www.bleepingcomputer.com/news/security/hackers-steal-3516-million-in-bitget-crypto-exchange-hack/)
- **TeamFiltration Campaign Compromises Seven Microsoft 365 Accounts Using Default Passwords** — Attackers compromised over 5,700 Microsoft 365 email accounts across multiple companies using simple default passwords (unchanged login credentials). [read more](https://thehackernews.com/2026/09/teamfiltration-compromises-seven.html)
- **‘SalesBleed’ Flaws in Salesforce Agentforce Enabled Zero-Click Data Exfiltration** — Three flaws in Salesforce Agentforce allowed attackers to take control of AI agents, steal customer data, and send fake phishing emails without user interaction. [read more](https://www.securityweek.com/salesbleed-flaws-in-salesforce-agentforce-enabled-zero-click-data-exfiltration/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-76460 (– CVSS, 14% EPSS)

## 🔥 Top stories

### 1. Attackers Exploit WordPress CVE-2026-87902 Within Hours of Disclosure
*The Hacker News* — [read more](https://thehackernews.com/2026/09/attackers-exploit-wordpress-cve-2026.html)

A serious WordPress security flaw (CVE-2026-87902) was publicly announced, and within hours, attackers began using it to break into websites and take complete control of them. This matters because WordPress powers millions of websites, so a quick-exploited flaw puts many sites at immediate risk. Defenders typically apply security patches immediately, disable the vulnerable feature, or temporarily take affected sites offline until a fix is available.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild
*The Hacker News* — [read more](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html)

A security weakness in Roundcube Webmail (CVE-2026-48842) that lets attackers access databases without logging in is being actively used in real attacks. This is dangerous because email servers are high-value targets that attackers use to steal sensitive information and spread further into networks. Defenders patch the software urgently, update to newer versions, monitor email logs for suspicious activity, and restrict who can access the email server.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 3. CISA: Ransomware gangs now exploiting critical TeamCity flaw
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-ransomware-gangs-now-exploiting-critical-teamcity-flaw/)

Criminal ransomware groups are exploiting a TeamCity flaw (a software build tool) that JetBrains fixed back in July, and U.S. federal agencies have been warned. Ransomware attacks encrypt an organization's files and demand payment, so exploiting build tools gives attackers a way into critical systems. Defenders ensure all TeamCity installations are fully patched, review who has access to build systems, and watch for suspicious deployment or code changes.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 4. WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV
*The Hacker News* — [read more](https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html)

Two serious security flaws in WSO2 and Adobe Commerce were found being actively exploited, so CISA added them to a public list of known-exploited vulnerabilities that defenders should prioritize. When flaws are publicly confirmed as exploited, attackers know they work and will target unpatched systems more aggressively. Defenders treat these vulnerabilities as critical and patch immediately, or implement temporary workarounds if patching is not yet possible.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. Hackers now exploit critical Roundcube flaw in code injection attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/critical-roundcube-flaw-now-actively-exploited-in-code-injection-attacks/)

A high-severity flaw in Roundcube Webmail from May that was patched is now being used in real attacks to inject malicious code. Email systems are common attack targets because they often contain sensitive business data and can be used to compromise entire organizations. Defenders update Roundcube immediately, check email server logs for signs of code injection, and reset credentials for accounts that may have been compromised.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Hackers steal $351.6 million in Bitget crypto exchange hack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-steal-3516-million-in-bitget-crypto-exchange-hack/)

North Korean hackers stole $351.6 million from Bitget, a cryptocurrency exchange, by accessing their hot wallets (funds kept online for quick transactions) and warm wallets (semi-active storage). This matters because large financial thefts damage customer trust and show that even well-resourced companies face advanced criminal threats. Defenders at crypto exchanges improve wallet security using hardware protection, add strict access controls, and monitor for unauthorized fund movements in real time.

### 7. TeamFiltration Campaign Compromises Seven Microsoft 365 Accounts Using Default Passwords
*The Hacker News* — [read more](https://thehackernews.com/2026/09/teamfiltration-compromises-seven.html)

Attackers compromised over 5,700 Microsoft 365 email accounts across multiple companies using simple default passwords (unchanged login credentials). This is serious because email accounts are gateways to sensitive business data, financial records, and access to other company systems. Defenders enforce strong password policies, require password changes from defaults, enable multi-factor authentication (a second login step), and monitor for unusual login activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 8. ‘SalesBleed’ Flaws in Salesforce Agentforce Enabled Zero-Click Data Exfiltration
*SecurityWeek* — [read more](https://www.securityweek.com/salesbleed-flaws-in-salesforce-agentforce-enabled-zero-click-data-exfiltration/)

Three flaws in Salesforce Agentforce allowed attackers to take control of AI agents, steal customer data, and send fake phishing emails without user interaction. This matters because AI agents often handle sensitive customer information and trusted business communications, so compromising them spreads both data theft and fraud. Defenders apply Salesforce security patches, review agent permissions and activity logs, and educate users about verifying unusual agent communications.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-76460** | Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability | – | 14% | ⚠️ YES (KEV) |
| **CVE-2026-42018** | JFrog Artifactory Improper Authentication Vulnerability | – | 10% | ⚠️ YES (KEV) |
| **CVE-2026-85706** | GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability | – | 9% | ⚠️ YES (KEV) |
| **CVE-2026-42016** | JFrog Artifactory Incorrect Authorization Vulnerability | – | 9% | ⚠️ YES (KEV) |
| **CVE-2025-39682** | Linux Kernel Improper Check for Unusual or Exceptional Conditions Vulnerability | – | 3% | ⚠️ YES (KEV) |

**CVE-2026-76460** — Cisco Identity Services Engine (a security authentication tool) has a flaw where it incorrectly uses high-privilege system functions, potentially letting attackers gain unauthorized elevated access. This is critical because authentication systems control access to entire networks, so compromising them gives attackers admin-level control. Defenders patch immediately, limit who can access the authentication system, and monitor for unusual privilege escalation attempts.

**CVE-2026-42018** — JFrog Artifactory (a software repository storage system) has a flaw in how it verifies user identities, potentially allowing unauthorized access to stored software code and components. This matters because software repositories contain the source code and tools companies use to build applications—compromising them lets attackers inject malicious code into software. Defenders patch urgently, review access logs for unauthorized logins, and verify the integrity of stored software.

**CVE-2026-85706** — GitLab Community and Enterprise editions have a path traversal flaw that lets attackers access files they shouldn't be able to reach by using special file path tricks. This is dangerous because GitLab stores source code and deployment scripts—unauthorized access leaks company secrets and lets attackers modify code. Defenders patch immediately, audit who has accessed sensitive files, and review code changes for suspicious modifications.

**CVE-2026-42016** — JFrog Artifactory has a flaw in how it checks permissions, potentially allowing users to access or modify software packages they should not have rights to. This matters because software packages are building blocks used across organizations, so unauthorized modification could spread compromised code organization-wide. Defenders patch immediately, audit permission settings, and verify that sensitive software packages have not been tampered with.

**CVE-2025-39682** — A Linux Kernel flaw fails to properly check for unusual conditions, which could allow attackers to crash systems or potentially execute code with elevated privileges. This is serious because Linux powers servers, cloud infrastructure, and critical systems worldwide—a wide-spread vulnerability puts many organizations at risk. Defenders apply kernel security updates promptly, prioritize patching critical systems, and monitor for system crashes or unusual behavior that could indicate exploitation.

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*