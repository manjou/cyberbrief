# 🛡️ CyberBrief — SOC — Thursday, 24 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Attackers Exploit WordPress CVE-2026-87902 Within Hours of Disclosure** — A serious security flaw in WordPress (rated 9.2 out of 10 in severity) was publicly announced, and hackers started using it to break into websites within hours. [read more](https://thehackernews.com/2026/09/attackers-exploit-wordpress-cve-2026.html)
- **F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks** — F5 released a security update for its BIG-IP APM (Access Policy Manager, a tool that controls who can access company networks) to fix a previously unknown vulnerability that attackers were already actively exploiting to run code on the system. [read more](https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/)
- **F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers** — A specific vulnerability (CVE-2026-94127) in F5 BIG-IP APM allows attackers to run malicious code on F5 systems without authenticating, but only affects systems using BIG-IP APM to manage OAuth tokens (a system for granting application access). [read more](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html)
- **Arista patches actively exploited VeloCloud Orchestrator zero-day** — Arista released patches for a previously unknown flaw in VeloCloud Orchestrator (on-premises version) that attackers were already actively exploiting. [read more](https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/)
- **Check Point warns of hackers exploiting Security Gateway VPN RCE flaw** — Attackers are actively exploiting CVE-2026-85102, a flaw in Check Point Security Gateway's VPN system that lets them run code without needing any credentials beforehand. [read more](https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/)
- **Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware** — A Chinese hacking group discovered and weaponized two previously unknown flaws—one in Google Chrome and one in Windows—chaining them together to attack targets through fake websites and install malware called CLEANGULP. [read more](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)
- **InfraTrust report warns network management systems under attack** — Attackers are increasingly targeting network management systems (the command-and-control tools for enterprise infrastructure) with several critical vulnerabilities being exploited either before vendors knew about them or shortly after public announcement. [read more](https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/)
- **Critical WordPress Vulnerability Exploited Immediately After Disclosure** — CVE-2026-87902 is a path traversal flaw in WordPress that lets an attacker without a password access files and run code on a WordPress website by manipulating how the website loads files from its directory structure. [read more](https://www.securityweek.com/critical-wordpress-vulnerability-exploited-immediately-after-disclosure/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-93616 (9.8 CVSS, 2% EPSS)

## 🔥 Top stories

### 1. Attackers Exploit WordPress CVE-2026-87902 Within Hours of Disclosure
*The Hacker News* — [read more](https://thehackernews.com/2026/09/attackers-exploit-wordpress-cve-2026.html)

A serious security flaw in WordPress (rated 9.2 out of 10 in severity) was publicly announced, and hackers started using it to break into websites within hours. This matters because attackers can take control of WordPress sites completely without needing a password, putting sensitive data and website visitors at risk. Defenders respond by immediately applying the security patch that WordPress releases, scanning their systems for signs of attack, and temporarily disabling the vulnerable feature if patching takes time.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/)

F5 released a security update for its BIG-IP APM (Access Policy Manager, a tool that controls who can access company networks) to fix a previously unknown vulnerability that attackers were already actively exploiting to run code on the system. This matters because BIG-IP APM often protects critical network access points, so compromising it gives attackers a foothold into the entire network. Defenders prioritize applying this patch immediately, check their systems for evidence of the attack, and review access logs to see if anyone broke in.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers
*The Hacker News* — [read more](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html)

A specific vulnerability (CVE-2026-94127) in F5 BIG-IP APM allows attackers to run malicious code on F5 systems without authenticating, but only affects systems using BIG-IP APM to manage OAuth tokens (a system for granting application access). This matters because these systems control who can access applications across the enterprise, making them a high-value target. Defenders patch systems immediately if they have APM configured as an OAuth server, verify their configuration to see if they're affected, and monitor for suspicious access token activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 4. Arista patches actively exploited VeloCloud Orchestrator zero-day
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/)

Arista released patches for a previously unknown flaw in VeloCloud Orchestrator (on-premises version) that attackers were already actively exploiting. This matters because VeloCloud Orchestrator controls how branch office networks connect to the main company network, so compromising it can expose the entire network to attackers. Defenders prioritize this patch for deployment, check if they run the on-premises version (not cloud-hosted), and review logs for signs of unauthorized access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. Check Point warns of hackers exploiting Security Gateway VPN RCE flaw
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/)

Attackers are actively exploiting CVE-2026-85102, a flaw in Check Point Security Gateway's VPN system that lets them run code without needing any credentials beforehand. This matters because VPNs are often the main entry point into company networks, especially for remote employees, so this vulnerability puts the entire network at risk. Defenders apply Check Point's security patch immediately, require all users to re-authenticate their VPN sessions, and watch for suspicious VPN login patterns.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 6. Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware
*The Hacker News* — [read more](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)

A Chinese hacking group discovered and weaponized two previously unknown flaws—one in Google Chrome and one in Windows—chaining them together to attack targets through fake websites and install malware called CLEANGULP. This matters because chaining multiple vulnerabilities together makes attacks much harder to stop and affects most computers globally. Defenders update both Chrome and Windows immediately when patches are available, avoid clicking suspicious links, and scan computers for CLEANGULP malware if they suspect exposure.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 7. InfraTrust report warns network management systems under attack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/)

Attackers are increasingly targeting network management systems (the command-and-control tools for enterprise infrastructure) with several critical vulnerabilities being exploited either before vendors knew about them or shortly after public announcement. This matters because compromising management systems gives attackers control over the entire infrastructure, not just individual machines. Defenders isolate management systems behind extra security layers, apply patches as soon as available, and closely monitor access to these privileged systems.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 8. Critical WordPress Vulnerability Exploited Immediately After Disclosure
*SecurityWeek* — [read more](https://www.securityweek.com/critical-wordpress-vulnerability-exploited-immediately-after-disclosure/)

CVE-2026-87902 is a path traversal flaw in WordPress that lets an attacker without a password access files and run code on a WordPress website by manipulating how the website loads files from its directory structure. This matters because WordPress powers a large portion of websites globally, making it an attractive target for mass attacks. Defenders update WordPress immediately when this patch is released, check website logs for attempts to exploit this flaw, and use website monitoring tools to detect compromise.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-93616** | Check Point Multiple Products Path Traversal Vulnerability | 9.8 | 2% | ⚠️ YES (KEV) |
| **CVE-2026-94127** | F5 BIG-IP APM Heap-based Buffer Overflow Vulnerability | 9.8 | 1% | ⚠️ YES (KEV) |
| **CVE-2026-42018** | JFrog Artifactory Improper Authentication Vulnerability | – | 11% | ⚠️ YES (KEV) |
| **CVE-2026-85706** | GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability | – | 9% | ⚠️ YES (KEV) |
| **CVE-2026-42016** | JFrog Artifactory Incorrect Authorization Vulnerability | – | 9% | ⚠️ YES (KEV) |

**CVE-2026-93616** — CVE-2026-93616 is a flaw in Check Point Management Server that allows someone without credentials to upload files to the server and execute them as code by exploiting a directory traversal weakness (a technique for accessing files outside the intended directory). This matters because the Management Server is the central control point for Check Point security appliances, so compromising it compromises all protected systems downstream. Defenders patch immediately, restrict who can access the management server, and audit file uploads for anything suspicious.

**CVE-2026-94127** — CVE-2026-94127 affects BIG-IP APM systems that are specifically configured to issue OAuth tokens (a common setup for controlling app access); attackers can craft specific malicious requests to execute code without needing to log in. This matters because OAuth token servers are trusted to grant access to business applications, so compromising them can grant attackers widespread application access. Defenders verify if their BIG-IP APM uses OAuth token issuing and patch immediately if so, review token issuance logs for suspicious activity, and reset any tokens that might be compromised.

**CVE-2026-42018** — CVE-2026-42018 is an improper authentication flaw in JFrog Artifactory (a system that stores and manages software artifacts and dependencies) that may allow unauthorized access. This matters because Artifactory holds all the software components and libraries a company uses, making it a target for supply chain attacks where malicious code can be injected into software builds. Defenders apply the authentication fix, change passwords for Artifactory accounts, verify that only authorized users have access, and scan their build pipeline for suspicious components.

**CVE-2026-85706** — CVE-2026-85706 is a path traversal vulnerability in GitLab Community and Enterprise editions that allows attackers to access files outside the intended directories by manipulating the file path parameter. This matters because GitLab stores source code and can contain secrets like API keys, making it extremely valuable to attackers. Defenders update GitLab immediately, check access logs for suspicious file requests, and scan their repository for any changes or leaked secrets that may have been exposed.

**CVE-2026-42016** — CVE-2026-42016 is an incorrect authorization flaw in JFrog Artifactory where the system doesn't properly verify if a user has permission to perform an action they're requesting (such as accessing restricted software packages). This matters because it can allow users or attackers to access, modify, or delete software components they shouldn't be able to reach, potentially poisoning the software supply chain. Defenders apply the authorization fix, audit who has accessed what in Artifactory, verify that access controls are working correctly after patching, and review if any unauthorized changes were made.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*