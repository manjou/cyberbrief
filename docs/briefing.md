# 🛡️ CyberBrief — GRC — Friday, 23 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🔥 Top stories

### 1. Arista patches new VeloCloud Orchestrator zero-day exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/)

Arista Networks released patches for a zero-day vulnerability (a previously unknown security flaw) in VeloCloud Orchestrator that attackers were already actively exploiting in real attacks. This matters because organizations using this on-premises version are at immediate risk of being compromised before they patch. Defenders need to apply these patches urgently and check logs to see if the vulnerability was exploited on their systems before the update was released.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. China-Linked Hackers Use ARTEX AI Agents in ConnectWise Supply Chain Attack
*The Hacker News* — [read more](https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html)

A Chinese state-affiliated hacking group called Storm-0940 compromised ConnectWise's Cloud Backup software through its supply chain (meaning they hacked the software vendor, not individual users) and used an AI-based penetration testing tool called ARTEX to explore victim networks. This matters because it affects many organizations that trusted ConnectWise, and shows attackers are using AI automation to move faster through compromised systems. Defenders need to check if they use ConnectWise, apply any available fixes immediately, review their backup systems for unauthorized access, and monitor for signs of AI-based reconnaissance tools being used in their networks.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 3. ThreatsDay: AI Secrets Leak, PingCAP Source Theft, Signal Hang-Up Flaw, Laravel Auth Bypass + 21 More
*The Hacker News* — [read more](https://thehackernews.com/2026/10/threatsday-ai-secrets-leak-pingcap.html)

Multiple critical vulnerabilities were disclosed in a single week across popular software including PHP, GitLab, Linux, Node.js, and others, plus compromised security certificates and hijacked network infrastructure. This matters because defenders face overwhelming work when many serious flaws drop at once, creating a backlog of patching and validation. Teams should prioritize based on what software they actually use, apply patches in order of risk to their environment, and consider temporarily restricting access to affected systems while waiting to patch.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 4. 11 Million Impacted by Capcom Data Breach
*SecurityWeek* — [read more](https://www.securityweek.com/11-million-impacted-by-capcom-data-breach/)

Hackers stole email addresses from Capcom's gaming membership service (CAPCOM ID) affecting 11 million users and changed passwords on 196 accounts, likely to lock legitimate users out or use those accounts for further attacks. This matters because exposed email addresses can be used for targeted phishing, password spraying (trying the same password across many accounts), or sold on criminal forums. Defenders at Capcom need to notify affected users, force password resets, and investigate how the breach occurred to prevent it happening again.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.17 Authentication information

### 5. Capcom confirms data breach affecting 11.7 million accounts
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/capcom-confirms-data-breach-affecting-117-million-accounts/)

Capcom confirmed that more than 11.7 million customer records were stolen from their CAPCOM ID membership service, exposing email addresses and associated account information. This matters because large-scale data exposure puts many customers at risk of identity theft, phishing, and account takeover attacks. Defenders and the company must notify all affected users, provide credit monitoring support, and conduct a full investigation to understand how attackers got in and what data was actually taken.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 6. Machine speed attacks require machine speed detection and response
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/machine-speed-attacks-require-machine-speed-detection-and-response/)

Attackers can now move so fast through compromised systems (stealing credentials and copying files within minutes) that traditional security teams cannot respond in time using manual processes. This matters because the speed advantage means attackers often succeed before security tools even alert defenders. Organizations need to implement automated responses (like immediately revoking stolen credentials or isolating compromised machines) and improve their detection speed through better monitoring and alert prioritization.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.8.8 Management of technical vulnerabilities

### 7. Attackers Exploit Third VeloCloud Orchestrator Zero-Day in Four Months
*SecurityWeek* — [read more](https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/)

A third critical zero-day vulnerability in VeloCloud Orchestrator was discovered within four months, this time a SQL injection flaw (a coding mistake that lets attackers run unauthorized database commands) that allows attackers to gain administrative operator privileges. This matters because the repeated discovery of serious flaws in the same product suggests deeper security issues in how it was built. Defenders using VeloCloud should treat this as urgent, apply patches immediately, and consider whether they trust this vendor enough to continue using it.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 8. Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before Kernel Fixes
*The Hacker News* — [read more](https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html)

Two severe remote code execution flaws (rated 9.0 out of 10 in severity) were publicly disclosed in KSMBD, a Linux file-sharing server built into the kernel, before security fixes were available in the official Linux code. One flaw can be exploited before even authenticating, meaning attackers need no valid login credentials. This matters because any Linux server using KSMBD is potentially vulnerable and there's no official patch yet, creating a gap where attackers can attack systems faster than fixes can be deployed. Defenders should disable KSMBD if not needed, isolate affected systems, and monitor carefully for exploitation attempts.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-105134** | Ahsay AhsayCBS Command Injection Vulnerability | – | 38% | ⚠️ YES (KEV) |
| **CVE-2026-104935** | Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | – | 26% | ⚠️ YES (KEV) |
| **CVE-2026-21589** | Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability | – | 13% | ⚠️ YES (KEV) |
| **CVE-2026-105133** | Ahsay AhsayCBS Improper Authentication Vulnerability | – | 6% | ⚠️ YES (KEV) |
| **CVE-2026-76519** | Cisco Secure Email Gateway Relative Path Traversal Vulnerability | – | 2% | ⚠️ YES (KEV) |

**CVE-2026-105134** — CVE-2026-105134 is a command injection vulnerability in Ahsay AhsayCBS (a backup management system), meaning attackers can inject unauthorized system commands that execute with the application's privileges. This matters because backup systems often have broad access to data and infrastructure, so compromising them could expose or destroy critical backups. Defenders need to apply vendor patches, review who can access this system, and check backup logs for suspicious activity.

**CVE-2026-104935** — CVE-2026-104935 is an authentication bypass flaw in Ivanti Connect Secure (a remote access product) where attackers can spoof their identity to bypass login protections without needing valid credentials. This matters because remote access products are high-value targets—compromising one gives attackers direct entry to an organization's network. Defenders must patch immediately, force password resets, review who accessed the system recently, and strengthen additional security layers like IP restrictions.

**CVE-2026-21589** — CVE-2026-21589 affects multiple Atlassian products and allows unauthorized external parties to access files or directories they shouldn't be able to reach due to improper access controls. This matters because Atlassian tools often store sensitive code, documentation, and configuration data, so exposing directories could leak valuable information. Defenders need to patch, audit what files external users could access, change any compromised credentials, and review user access permissions.

**CVE-2026-105133** — CVE-2026-105133 is an improper authentication flaw in Ahsay AhsayCBS where the system fails to correctly verify user identity before granting access to sensitive backup data. This matters because it could allow unauthorized users to access, modify, or delete backups that organizations rely on for recovery. Defenders must patch this immediately, audit recent access to the system, reset credentials for users with administrative roles, and verify backup integrity.

**CVE-2026-76519** — CVE-2026-76519 is a path traversal vulnerability in Cisco Secure Email Gateway where attackers can manipulate file paths to access files and directories outside the intended restricted areas by using relative paths like '../../../'. This matters because email gateways protect against malware and data loss, so compromising one could allow attackers to bypass security controls. Defenders need to apply patches, review email logs for suspicious file access patterns, and verify the gateway's security settings are correctly configured.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*