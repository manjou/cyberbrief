# 🛡️ CyberBrief — GRC — Friday, 04 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Google Releases Chrome Update to Patch Actively Exploited V8 Zero-Day** — Google released a security update for Chrome that fixes a bug in V8 (the JavaScript engine) that attackers were already actively exploiting in real attacks. [read more](https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html)
- **Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon** — A researcher publicly released code demonstrating how to exploit a privilege escalation flaw in CrowdStrike Falcon (a security tool that runs on computers with high system permissions). [read more](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)
- **Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws** — Attackers are actively exploiting two serious vulnerabilities in popular WordPress plugins (Super Forms and Elementor Pro) that allow remote code execution (running their own code on the website server). [read more](https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html)
- **Cisco Warns of Unpatched Secure Email Flaws, Patches Critical Switch Vulnerabilities** — Cisco disclosed flaws in their secure email system that could leak encrypted email contents, and separately released patches for switch software bugs that could allow attackers remote code execution and to bypass authentication. [read more](https://www.securityweek.com/cisco-warns-of-unpatched-secure-email-flaws-patches-critical-switch-vulnerabilities/)
- **French hospital fined €500,000 after breach exposes data of 727,000** — A French hospital failed to properly secure patient data, which resulted in a breach exposing information on 727,000 people and a €500,000 fine from the data protection authority. [read more](https://www.bleepingcomputer.com/news/security/french-hospital-fined-500-000-after-breach-exposes-data-of-727-000/)
- **HPE patches critical ArubaOS-CX remote code execution flaw** — HPE released a security patch for a critical vulnerability in ArubaOS-CX (network operating system software) that could allow remote code execution on network switches. [read more](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)
- **Thomson Reuters Court Software Breach May Have Exposed SSNs and Sealed Data** — Thomson Reuters disclosed that unauthorized attackers accessed files from C-Track, their court case management software, in March 2026, potentially exposing social security numbers and sealed legal documents across multiple U.S. [read more](https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html)
- **Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root** — Cisco patched a critical flaw in Nexus 9000 network switches that allows an attacker without any credentials to remotely execute code with root privileges (full system control) and released a security hardening update. [read more](https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-60004 (– CVSS, 87% EPSS)

## 🔥 Top stories

### 1. Google Releases Chrome Update to Patch Actively Exploited V8 Zero-Day
*The Hacker News* — [read more](https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html)

Google released a security update for Chrome that fixes a bug in V8 (the JavaScript engine) that attackers were already actively exploiting in real attacks. This matters because the bug allowed attackers to confuse data types in memory, potentially letting them run malicious code on users' computers. Defenders respond by pushing out the update to users as quickly as possible and monitoring their systems to see if anyone was compromised before the patch was available.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon
*The Hacker News* — [read more](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)

A researcher publicly released code demonstrating how to exploit a privilege escalation flaw in CrowdStrike Falcon (a security tool that runs on computers with high system permissions). This matters because an attacker who gains initial access to a system could use this exploit to escalate their permissions from limited user to administrator-level, giving them full control. Defenders immediately apply the CrowdStrike patch, monitor for suspicious privilege escalation attempts, and review logs to check if anyone exploited this before the fix was available.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 3. Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws
*The Hacker News* — [read more](https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html)

Attackers are actively exploiting two serious vulnerabilities in popular WordPress plugins (Super Forms and Elementor Pro) that allow remote code execution (running their own code on the website server). This matters because websites using these unpatched plugins can be completely compromised and used to steal data or spread malware. Defenders update these plugins immediately, scan their websites for signs of exploitation, and block malicious traffic patterns associated with these attacks.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 4. Cisco Warns of Unpatched Secure Email Flaws, Patches Critical Switch Vulnerabilities
*SecurityWeek* — [read more](https://www.securityweek.com/cisco-warns-of-unpatched-secure-email-flaws-patches-critical-switch-vulnerabilities/)

Cisco disclosed flaws in their secure email system that could leak encrypted email contents, and separately released patches for switch software bugs that could allow attackers remote code execution and to bypass authentication. This matters because email breaches expose sensitive communications and switch vulnerabilities expose the entire network infrastructure. Defenders prioritize patching the switch vulnerabilities immediately due to their critical impact, and apply email patches while evaluating any encrypted messages that may have been exposed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. French hospital fined €500,000 after breach exposes data of 727,000
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/french-hospital-fined-500-000-after-breach-exposes-data-of-727-000/)

A French hospital failed to properly secure patient data, which resulted in a breach exposing information on 727,000 people and a €500,000 fine from the data protection authority. This matters because inadequate data protection violates privacy regulations and harms patients whose personal information is exposed to misuse. Defenders (and all organizations) implement strong access controls, encryption, monitoring systems, and regular security audits to prevent breaches and comply with legal requirements.

### 6. HPE patches critical ArubaOS-CX remote code execution flaw
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)

HPE released a security patch for a critical vulnerability in ArubaOS-CX (network operating system software) that could allow remote code execution on network switches. This matters because compromised network switches can be used to monitor, intercept, or disrupt all traffic on the network. Defenders apply this patch to all affected switches urgently and monitor for any suspicious activity that might indicate exploitation attempts.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Thomson Reuters Court Software Breach May Have Exposed SSNs and Sealed Data
*The Hacker News* — [read more](https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html)

Thomson Reuters disclosed that unauthorized attackers accessed files from C-Track, their court case management software, in March 2026, potentially exposing social security numbers and sealed legal documents across multiple U.S. states and Canada. This matters because exposed SSNs enable identity theft and exposed sealed documents violate court confidentiality and privacy. Defenders investigate how the breach occurred, notify affected users, patch vulnerabilities, and work with courts and law enforcement on the incident.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 8. Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root
*The Hacker News* — [read more](https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html)

Cisco patched a critical flaw in Nexus 9000 network switches that allows an attacker without any credentials to remotely execute code with root privileges (full system control) and released a security hardening update. This matters because network infrastructure switches are a prime target—compromising them gives attackers control of all network traffic and access to everything connected. Defenders treat this as extremely urgent, apply patches immediately, and review firewall rules to restrict access to switch management interfaces.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-60004** | Gitea Code Injection Vulnerability | – | 87% | ⚠️ YES (KEV) |
| **CVE-2021-23758** | Ajax.NET Professional Deserialization of Untrusted Data Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2019-1068** | Microsoft SQL Server Remote Code Execution Vulnerability | – | 53% | ⚠️ YES (KEV) |
| **CVE-2023-49105** | ownCloud Improper Authentication Vulnerability | – | 43% | ⚠️ YES (KEV) |
| **CVE-2026-21962** | Oracle HTTP Server and Oracle Weblogic Server Proxy Plug-in Improper Access Control Vulnerability | – | 42% | ⚠️ YES (KEV) |

**CVE-2026-60004** — Gitea (a code repository platform) contains a code injection vulnerability that could allow attackers to execute arbitrary code on the server. This matters because code repositories store source code and deployment credentials; compromising them allows attackers to inject malicious code into software before it's deployed. Defenders apply available patches, review repository access logs for suspicious activity, and scan code for signs of tampering.

**CVE-2021-23758** — Ajax.NET Professional has a deserialization vulnerability (the process of converting data back into objects is unsafe) that allows untrusted data to become executable code. This matters because attackers can craft malicious data that, when processed by the application, executes code they control. Defenders apply patches, avoid deserializing data from untrusted sources, and use code review to identify risky deserialization patterns.

**CVE-2019-1068** — Microsoft SQL Server has a remote code execution vulnerability that allows attackers to run code on the database server without proper access. This matters because SQL databases typically store an organization's most sensitive data; compromising the database server exposes everything. Defenders apply Microsoft's security patch immediately and restrict network access to database servers through firewalls.

**CVE-2023-49105** — ownCloud (a file sharing and sync platform) has an improper authentication vulnerability, meaning it doesn't verify users' identities correctly. This matters because attackers could bypass login requirements and access files and data without credentials. Defenders patch ownCloud immediately, force password resets for all users, review access logs to identify unauthorized access, and check for stolen data.

**CVE-2026-21962** — Oracle's HTTP Server and WebLogic Server proxy plug-in has an improper access control flaw that allows attackers to access resources or functions they shouldn't be able to reach. This matters because these servers often sit on the network edge; compromising them gives attackers a foothold to attack internal systems. Defenders apply Oracle's security patches, review firewall rules restricting access, and audit logs for unauthorized access attempts.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*