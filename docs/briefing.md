# 🛡️ CyberBrief — Net+ — Wednesday, 23 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks** — F5 released patches for a critical flaw in BIG-IP APM (Access Policy Manager, a tool that controls who can access applications) that attackers were already exploiting to run code remotely on the system. [read more](https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/)
- **F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers** — Attackers found a way to exploit a flaw in F5 BIG-IP APM when it's set up to issue login tokens (OAuth authorization)—they can send malicious requests without logging in and execute code on the system. [read more](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html)
- **Critical F5 BIG-IP Vulnerability Exploited as Zero-Day** — A critical flaw in F5 BIG-IP allows attackers to send specially crafted network traffic that executes code on the device, and they don't need valid login credentials to do it. [read more](https://www.securityweek.com/critical-f5-big-ip-vulnerability-exploited-as-zero-day/)
- **Check Point warns of Management Server zero-day exploited in attacks** — Check Point released emergency fixes for a critical flaw in their Security Management Server (the central control system that manages all security policies) that lets attackers run malicious scripts without proper authorization. [read more](https://www.bleepingcomputer.com/news/security/check-point-patches-management-server-zero-day-exploited-in-attacks/)
- **Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials** — A critical flaw in Bifrost, an open-source system that routes AI requests to services like ChatGPT, allows attackers to run commands on the Bifrost server by simply sending one malicious web request—no login required. [read more](https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html)
- **New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups** — Arista discovered a critical flaw in VeloCloud Orchestrator, the server that controls SD-WAN edge devices (hardware that routes network traffic), and attackers are already exploiting it to gain privileged access without logging in. [read more](https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html)
- **Arista Urges Immediate Patching of Exploited VCO Zero-Day** — A critical flaw in VeloCloud Orchestrator allows remote attackers to access privileged functions and sensitive capabilities without any login credentials, and attackers are actively exploiting this. [read more](https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/)
- **Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware** — A Chinese hacking group exploited two connected security flaws in Google Chrome and Microsoft Windows (vulnerabilities that were not yet publicly known) to trick users into visiting fake websites and install malware called CLEANGULP. [read more](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-20079 (– CVSS, 76% EPSS)

## 🔥 Top stories

### 1. F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/)

F5 released patches for a critical flaw in BIG-IP APM (Access Policy Manager, a tool that controls who can access applications) that attackers were already exploiting to run code remotely on the system. This matters because BIG-IP APM often sits between users and important applications, so compromising it gives attackers broad access to an organization's systems. Defenders typically apply the patch immediately and check logs to see if anyone exploited this flaw before the patch was installed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers
*The Hacker News* — [read more](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html)

Attackers found a way to exploit a flaw in F5 BIG-IP APM when it's set up to issue login tokens (OAuth authorization)—they can send malicious requests without logging in and execute code on the system. This is especially dangerous because OAuth servers handle login requests from many applications and users, making them attractive targets. Defenders should prioritize patching systems that use BIG-IP APM for OAuth, monitor for suspicious token requests, and check if the system was compromised before patching.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 3. Critical F5 BIG-IP Vulnerability Exploited as Zero-Day
*SecurityWeek* — [read more](https://www.securityweek.com/critical-f5-big-ip-vulnerability-exploited-as-zero-day/)

A critical flaw in F5 BIG-IP allows attackers to send specially crafted network traffic that executes code on the device, and they don't need valid login credentials to do it. This matters because BIG-IP often handles traffic for many applications, so compromising it could affect many systems at once. Defenders need to patch immediately, restrict network access to BIG-IP management interfaces, and review network logs for suspicious traffic patterns.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. Check Point warns of Management Server zero-day exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/check-point-patches-management-server-zero-day-exploited-in-attacks/)

Check Point released emergency fixes for a critical flaw in their Security Management Server (the central control system that manages all security policies) that lets attackers run malicious scripts without proper authorization. This is critical because the management server controls security across an entire organization, so compromising it gives attackers control over all protections. Defenders should apply these hotfixes urgently and review who accessed the management server recently.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials
*The Hacker News* — [read more](https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html)

A critical flaw in Bifrost, an open-source system that routes AI requests to services like ChatGPT, allows attackers to run commands on the Bifrost server by simply sending one malicious web request—no login required. This matters because Bifrost sits between applications and AI services, so controlling it could let attackers spy on or manipulate AI requests. Defenders should update Bifrost immediately, limit network access to it, and monitor for suspicious command patterns in logs.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 6. New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups
*The Hacker News* — [read more](https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html)

Arista discovered a critical flaw in VeloCloud Orchestrator, the server that controls SD-WAN edge devices (hardware that routes network traffic), and attackers are already exploiting it to gain privileged access without logging in. This matters because the orchestrator controls how network traffic flows across an organization, so compromising it could disrupt network operations or redirect traffic to attackers. Defenders should patch immediately, especially systems using certificate-based authentication, and review VCO logs for unauthorized access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 7. Arista Urges Immediate Patching of Exploited VCO Zero-Day
*SecurityWeek* — [read more](https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/)

A critical flaw in VeloCloud Orchestrator allows remote attackers to access privileged functions and sensitive capabilities without any login credentials, and attackers are actively exploiting this. This matters because the orchestrator manages the entire SD-WAN infrastructure, so this flaw could give attackers control over critical network paths. Defenders should treat this as an emergency patch priority and monitor for unusual administrative activity on the orchestrator.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 8. Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware
*The Hacker News* — [read more](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)

A Chinese hacking group exploited two connected security flaws in Google Chrome and Microsoft Windows (vulnerabilities that were not yet publicly known) to trick users into visiting fake websites and install malware called CLEANGULP. This matters because zero-day exploits are especially dangerous—security patches don't exist yet—so traditional defenses can't stop them. Defenders should keep systems fully updated once patches release, be cautious of unexpected links, and monitor for suspicious processes that might indicate infection.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-20079** | Cisco Firewall Management Center Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 76% | ⚠️ YES (KEV) |
| **CVE-2026-93616** | Check Point Multiple Products Path Traversal Vulnerability | 9.8 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-94127** | F5 BIG-IP APM Heap-based Buffer Overflow Vulnerability | 9.8 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-93952** | Arista VeloCloud Orchestrator Improper Input Validation Vulnerability | 10.0 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-19490** | Citrix NetScaler Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 6% | ⚠️ YES (KEV) |

**CVE-2026-20079** — A flaw in Cisco Firewall Management Center (the system that controls Cisco firewalls) allows attackers to bypass authentication using an alternate access method, meaning they can get in without proper credentials. This matters because the management center controls all firewall rules, so compromising it gives attackers the ability to disable security controls. Defenders should apply the Cisco patch, enforce multi-factor authentication (requiring multiple forms of proof), and limit which networks can access the management center.

**CVE-2026-93616** — A flaw in Check Point Management Server allows unauthenticated attackers to navigate the file system and upload malicious scripts that automatically execute on the server. This matters because the management server is the central control point for all Check Point security tools across an organization, so this flaw could compromise every protected system. Defenders must patch urgently, restrict file upload capabilities, and review recent file uploads and script executions for signs of compromise.

**CVE-2026-94127** — When F5 BIG-IP APM is configured to issue login tokens (OAuth), a flaw in how it processes requests allows attackers to execute code without logging in first. This matters only for organizations using BIG-IP specifically for OAuth token issuance, but for those organizations it's critical because login systems are high-value targets. Defenders should identify which BIG-IP systems have OAuth configured, patch them immediately, and audit token-related logs for suspicious activity.

**CVE-2026-93952** — A flaw in VeloCloud Orchestrator (an on-premises version running in an organization's data center) lets remote attackers access privileged functions without authentication, potentially compromising the security, accuracy, and availability of the entire SD-WAN infrastructure and the data it carries. This matters because VeloCloud Orchestrator controls all SD-WAN edge devices, so compromising it could disrupt network operations across multiple locations. Defenders should patch immediately, implement network segmentation to restrict access to the orchestrator, and audit administrative logs for unauthorized changes.

**CVE-2026-19490** — A flaw in Citrix NetScaler (an application delivery and security system) allows attackers to bypass authentication using an alternate access path or method, letting them reach protected applications and data without proper credentials. This matters because NetScaler often protects critical business applications, so this flaw could allow unauthorized access to sensitive systems. Defenders should apply the Citrix security update, enable multi-factor authentication for administrative access, and restrict which networks can reach the NetScaler.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*