# 🛡️ CyberBrief — SOC — Monday, 14 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Hackers exploit Tencent app flaw to deploy GrayRabbit malware** — Attackers found and are actively using a serious flaw in Tencent's Sogou Input Method (a typing tool for Windows) to sneak in GrayRabbit malware, which gives them hidden remote access to infected computers. [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-tencent-app-flaw-to-deploy-grayrabbit-malware/)
- **Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data** — Threat actors are sending fake financial scam emails through legitimate email delivery services, then tricking users with messages about passkeys (a newer, supposedly more secure login method) to steal Microsoft cloud account credentials and access sensitive data. [read more](https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html)
- **Revolut discloses data breach exposing financial info, passports** — Revolut accidentally shared customer financial information and passport data with someone claiming to be a government official—who turned out to be a criminal. [read more](https://www.bleepingcomputer.com/news/security/revolut-discloses-data-breach-exposing-financial-info-passports/)
- **Three JFrog Artifactory Flaws Exploited for Backdoor Deployment** — Three security flaws in JFrog Artifactory (a software repository tool) allow attackers to skip normal login procedures and gain admin-level control, which lets them inject malicious code into software updates. [read more](https://www.securityweek.com/three-jfrog-artifactory-flaws-exploited-for-backdoor-deployment/)
- **[UPDATE] [hoch] Red Hat Enterprise Linux (postgis, virtuoso-opensource): Mehrere Schwachstellen** — Several vulnerabilities exist in Red Hat Enterprise Linux packages (postgis and virtuoso-opensource) that attackers can exploit to either crash systems or steal confidential information. [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3306)
- **Telus Warns Customers of Account Breaches** — Telus customers had usernames and passwords stolen, and attackers used these credentials over several months to log into accounts and access personal data and billing information. [read more](https://www.securityweek.com/telus-warns-customers-of-account-breaches/)
- **CISA: Hackers now exploit max severity GitLab flaw in attacks** — Hackers are actively exploiting a critical vulnerability in GitLab (a software development collaboration platform) in real attacks, and the U.S. [read more](https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploit-max-severity-gitlab-flaw-in-attacks/)
- **ConnectWise Patches ScreenConnect Vulnerability Exploited in Worm-Like Attacks** — ConnectWise ScreenConnect (remote access software) has a flaw that allows attackers to send and execute files on a target computer if they have an active remote session connection, spreading like a self-replicating worm. [read more](https://www.securityweek.com/connectwise-patches-screenconnect-vulnerability-exploited-in-worm-like-attacks/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-20079 (– CVSS, 76% EPSS)

## 🔥 Top stories

### 1. Hackers exploit Tencent app flaw to deploy GrayRabbit malware
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-tencent-app-flaw-to-deploy-grayrabbit-malware/)

Attackers found and are actively using a serious flaw in Tencent's Sogou Input Method (a typing tool for Windows) to sneak in GrayRabbit malware, which gives them hidden remote access to infected computers. This matters because input method software runs at a deep system level with high privileges, making it an effective entry point for espionage. Defenders typically patch the vulnerability immediately, monitor for suspicious GrayRabbit signatures, and audit systems that have the affected software installed.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 2. Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data
*The Hacker News* — [read more](https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html)

Threat actors are sending fake financial scam emails through legitimate email delivery services, then tricking users with messages about passkeys (a newer, supposedly more secure login method) to steal Microsoft cloud account credentials and access sensitive data. This matters because passkeys are still new enough that users may not recognize phishing attempts using them, and compromised cloud accounts expose everything stored there. Defenders typically train users to verify login requests directly through official channels, enable additional account security checks, and monitor for unusual cloud access patterns.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.5.19 Supplier relationships

### 3. Revolut discloses data breach exposing financial info, passports
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/revolut-discloses-data-breach-exposing-financial-info-passports/)

Revolut accidentally shared customer financial information and passport data with someone claiming to be a government official—who turned out to be a criminal. This matters because financial records and passport scans are high-value targets for identity theft and fraud, and the breach shows weak verification processes when handling data requests. Defenders typically implement strict data-sharing approval workflows, verify government requests through official channels only, and notify affected customers quickly so they can monitor for fraud.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 4. Three JFrog Artifactory Flaws Exploited for Backdoor Deployment
*SecurityWeek* — [read more](https://www.securityweek.com/three-jfrog-artifactory-flaws-exploited-for-backdoor-deployment/)

Three security flaws in JFrog Artifactory (a software repository tool) allow attackers to skip normal login procedures and gain admin-level control, which lets them inject malicious code into software updates. This matters because Artifactory is central to many software supply chains, so compromising it can poison software used by hundreds of organizations. Defenders typically apply patches immediately, audit who accessed the system during the vulnerability window, and scan stored software for tampering.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 5. [UPDATE] [hoch] Red Hat Enterprise Linux (postgis, virtuoso-opensource): Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3306)

Several vulnerabilities exist in Red Hat Enterprise Linux packages (postgis and virtuoso-opensource) that attackers can exploit to either crash systems or steal confidential information. This matters because Red Hat is widely used in enterprise and critical infrastructure environments, so these flaws affect many organizations. Defenders typically apply security patches promptly, test them in lab environments first, and monitor systems for signs of exploitation.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.6 Capacity management

### 6. Telus Warns Customers of Account Breaches
*SecurityWeek* — [read more](https://www.securityweek.com/telus-warns-customers-of-account-breaches/)

Telus customers had usernames and passwords stolen, and attackers used these credentials over several months to log into accounts and access personal data and billing information. This matters because once credentials are stolen, attackers can impersonate legitimate users and access everything tied to those accounts without triggering typical security alerts. Defenders typically reset passwords for affected customers, enable multi-factor authentication (an extra login verification step), investigate how long attackers had access, and monitor for ongoing misuse.

> 📋 **ISO 27001:** A.5.17 Authentication information

### 7. CISA: Hackers now exploit max severity GitLab flaw in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploit-max-severity-gitlab-flaw-in-attacks/)

Hackers are actively exploiting a critical vulnerability in GitLab (a software development collaboration platform) in real attacks, and the U.S. government agency CISA is alerting organizations to patch immediately. This matters because GitLab often contains source code and development secrets, so compromised instances can expose an organization's entire software pipeline. Defenders typically deploy patches to all GitLab instances, scan for signs of past exploitation, and reset any credentials stored in the system.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. ConnectWise Patches ScreenConnect Vulnerability Exploited in Worm-Like Attacks
*SecurityWeek* — [read more](https://www.securityweek.com/connectwise-patches-screenconnect-vulnerability-exploited-in-worm-like-attacks/)

ConnectWise ScreenConnect (remote access software) has a flaw that allows attackers to send and execute files on a target computer if they have an active remote session connection, spreading like a self-replicating worm. This matters because remote access tools are trusted to connect to critical systems, and this flaw turns them into automatic infection vectors. Defenders typically apply the patch immediately, review logs for suspicious file transfers during remote sessions, and restrict who can initiate remote access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-20079** | Cisco Firewall Management Center Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 76% | ⚠️ YES (KEV) |
| **CVE-2026-48710** | Kludex Starlette HTTP Request/Response Smuggling Vulnerability | – | 36% | ⚠️ YES (KEV) |
| **CVE-2026-9586** | Sangoma Switchvox SQL Injection Vulnerability | – | 12% | ⚠️ YES (KEV) |
| **CVE-2026-83549** | SonicWall SMA1000 Appliances OS Command Injection Vulnerability | – | 9% | ⚠️ YES (KEV) |
| **CVE-2026-82329** | JFrog Artifactory Improper Authentication Vulnerability | – | 8% | ⚠️ YES (KEV) |

**CVE-2026-20079** — Cisco Firewall Management Center, which controls security devices across a network, can be accessed without proper login by bypassing authentication through an alternate technical pathway. This matters because the management center controls access rules for the entire network, so unauthorized access means an attacker can disable security and move freely. Defenders typically apply the patch, require multi-factor authentication for administrative access, and monitor for unauthorized login attempts.

**CVE-2026-48710** — Kludex Starlette (a web framework for building applications) has a vulnerability allowing attackers to manipulate HTTP requests and responses in ways that bypass security controls or smuggle hidden commands into the communication stream. This matters because this type of flaw is subtle and difficult to detect, allowing attackers to sneak payloads past firewalls and security filters. Defenders typically update Starlette to the patched version, add extra validation rules for incoming requests, and monitor network traffic for suspicious patterns.

**CVE-2026-9586** — Sangoma Switchvox telephone system software contains a SQL injection vulnerability, meaning attackers can insert malicious database commands through normal input fields to steal, modify, or delete phone system data. This matters because phone systems often contain call logs, voicemails, and configuration data, and unauthorized changes can disrupt communications or enable eavesdropping. Defenders typically apply patches, validate all user inputs to ensure they cannot contain database commands, and restrict direct database access.

**CVE-2026-83549** — SonicWall SMA1000 appliances (network security devices) have a flaw allowing attackers to inject operating system commands through normal input fields, giving them command-line control of the security device. This matters because these appliances protect network access, so compromising them puts the entire protected network at risk. Defenders typically patch immediately, restrict network access to the appliance management interface, and monitor for suspicious command execution attempts.

**CVE-2026-82329** — JFrog Artifactory has a flaw in its authentication system that allows attackers to access the software repository without valid credentials or with weaker verification than required. This matters because this enables attackers to view, modify, or replace software packages, potentially poisoning any software that uses this repository. Defenders typically apply the patch, audit access logs to detect unauthorized activity, and verify the integrity of stored packages.

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*