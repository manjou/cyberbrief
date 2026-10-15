# 🛡️ CyberBrief — SOC — Thursday, 15 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Cisco patches new Secure Email Gateway zero-day exploited in attacks** — Cisco's email security product had a flaw that attackers could exploit without logging in to take full control of the system. [read more](https://www.bleepingcomputer.com/news/security/cisco-patches-actively-exploited-secure-email-gateway-zero-day/)
- **Palo Alto Networks Patches PAN-OS Zero-Day Exploited for Remote Code Execution** — Palo Alto Networks released a fix for a serious flaw in PAN-OS (the operating system running their firewalls) that allows remote code execution—meaning attackers can run commands on the firewall without authentication. [read more](https://www.securityweek.com/palo-alto-networks-patches-pan-os-zero-day-exploited-for-remote-code-execution/)
- **Palo Alto Networks warns of PAN-OS RCE flaw exploited in attacks** — A high-severity flaw (CVE-2026-0322) in Palo Alto's PAN-OS allows attackers to execute code remotely on firewalls, and it's already being actively exploited in real attacks. [read more](https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-pan-os-rce-flaw-exploited-in-attacks/)
- **CISA warns admins to immediately fix Ivanti flaw exploited as zero-day** — CISA (the U.S. [read more](https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-immediately-fix-ivanti-flaw-exploited-as-zero-day/)
- **CISA Urges Immediate Ivanti Connect Secure Updates as Honeypots Log 105 Exploit Attempts** — CISA warned organizations to urgently update Ivanti Connect Secure appliances after discovering an actively exploited vulnerability; honeypot systems (fake targets that log attacks) recorded over 100 exploit attempts. [read more](https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html)
- **Palo Alto Networks Patches PAN-OS Authenticated RCE Flaw Amid Active Exploitation** — Palo Alto Networks patched a serious flaw (CVE-2026-0322, CVSS 8.6) in PAN-OS that allows authenticated users (or attackers with stolen credentials) to execute code on the firewall's management system. [read more](https://thehackernews.com/2026/10/palo-alto-networks-patches-pan-os.html)
- **Langflow's Critical Authenticated RCE Flaw Targeted in 1,423 Honeypot Exploit Attempts** — Threat actors are actively exploiting a critical vulnerability in Langflow (an open-source AI platform by DataStax) to run unauthorized commands; honeypots detected over 1,400 exploit attempts in February 2025. [read more](https://thehackernews.com/2026/10/langflows-critical-authenticated-rce.html)
- **Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in CODE App** — Attackers exploited a flaw in Collabora Online CODE (an optional app in Nextcloud) to install web shells (small malicious scripts) that give them ongoing access to Nextcloud servers. [read more](https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2015-5477 (– CVSS, 99% EPSS)

## 🔥 Top stories

### 1. Cisco patches new Secure Email Gateway zero-day exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisco-patches-actively-exploited-secure-email-gateway-zero-day/)

Cisco's email security product had a flaw that attackers could exploit without logging in to take full control of the system. This matters because email gateways protect organizations from malicious messages, so compromising one gives attackers a foothold to send phishing emails or access company data. Defenders must apply Cisco's patch immediately and monitor their email gateway logs for suspicious activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 2. Palo Alto Networks Patches PAN-OS Zero-Day Exploited for Remote Code Execution
*SecurityWeek* — [read more](https://www.securityweek.com/palo-alto-networks-patches-pan-os-zero-day-exploited-for-remote-code-execution/)

Palo Alto Networks released a fix for a serious flaw in PAN-OS (the operating system running their firewalls) that allows remote code execution—meaning attackers can run commands on the firewall without authentication. This is critical because firewalls are the main barrier between your network and the internet, so compromising one is like unlocking your front door. Defenders should apply the patch right away and check provided Indicators of Compromise (IoCs—technical fingerprints of attacks) to see if they were targeted.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 3. Palo Alto Networks warns of PAN-OS RCE flaw exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-pan-os-rce-flaw-exploited-in-attacks/)

A high-severity flaw (CVE-2026-0322) in Palo Alto's PAN-OS allows attackers to execute code remotely on firewalls, and it's already being actively exploited in real attacks. Firewalls are critical defensive tools, so this vulnerability puts organizations at immediate risk of network infiltration and data theft. Security teams must prioritize patching this flaw and reviewing firewall logs to detect any compromise attempts.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 4. CISA warns admins to immediately fix Ivanti flaw exploited as zero-day
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-immediately-fix-ivanti-flaw-exploited-as-zero-day/)

CISA (the U.S. government's cybersecurity agency) issued an urgent alert about an Ivanti Connect Secure flaw that attackers have been exploiting since October without needing a patch. Ivanti appliances are remote access gateways, so this flaw could let attackers bypass authentication and access internal networks. Defenders should patch immediately, assume breach (meaning act as though attackers already got in), and review access logs from October onward.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. CISA Urges Immediate Ivanti Connect Secure Updates as Honeypots Log 105 Exploit Attempts
*The Hacker News* — [read more](https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html)

CISA warned organizations to urgently update Ivanti Connect Secure appliances after discovering an actively exploited vulnerability; honeypot systems (fake targets that log attacks) recorded over 100 exploit attempts. Ivanti products are often the first thing employees use to access company networks remotely, making this flaw a high-value target for attackers. Organizations must update to the latest version and investigate whether their systems were compromised before the patch was available.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 6. Palo Alto Networks Patches PAN-OS Authenticated RCE Flaw Amid Active Exploitation
*The Hacker News* — [read more](https://thehackernews.com/2026/10/palo-alto-networks-patches-pan-os.html)

Palo Alto Networks patched a serious flaw (CVE-2026-0322, CVSS 8.6) in PAN-OS that allows authenticated users (or attackers with stolen credentials) to execute code on the firewall's management system. While this requires some level of access, it's being actively exploited and lets attackers gain full control of a critical security tool. Defenders should apply the patch immediately, reset firewall administrative credentials, and audit who has had access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Langflow's Critical Authenticated RCE Flaw Targeted in 1,423 Honeypot Exploit Attempts
*The Hacker News* — [read more](https://thehackernews.com/2026/10/langflows-critical-authenticated-rce.html)

Threat actors are actively exploiting a critical vulnerability in Langflow (an open-source AI platform by DataStax) to run unauthorized commands; honeypots detected over 1,400 exploit attempts in February 2025. Langflow is used by developers to build AI applications, so compromise could lead to malicious AI applications or data theft. Organizations using Langflow must patch immediately and review application logs for signs of unauthorized access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in CODE App
*The Hacker News* — [read more](https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html)

Attackers exploited a flaw in Collabora Online CODE (an optional app in Nextcloud) to install web shells (small malicious scripts) that give them ongoing access to Nextcloud servers. Nextcloud is a file-sharing platform, so compromising it gives attackers access to sensitive documents and the ability to backdoor the system for long-term persistence. Defenders should disable the Collabora Online app if not needed, patch if available, and scan for web shells using file integrity monitoring.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2015-5477** |  ISC BIND Data Processing Errors Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2015-3306** | ProFTPD Improper Access Control Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2016-3081** | Apache Struts Command Injection Vulnerability | – | 96% | ⚠️ YES (KEV) |
| **CVE-2026-104935** | Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | 8.6 | 26% | ⚠️ YES (KEV) |
| **CVE-2026-96951** | Microsoft Windows Command Injection Vulnerability | 8.8 | 2% | ⚠️ YES (KEV) |

**CVE-2015-5477** — CVE-2015-5477 is a data processing error vulnerability in ISC BIND (the software that translates domain names to IP addresses). Flaws in DNS software can allow attackers to disrupt internet connectivity or redirect traffic, affecting any organization relying on that DNS server. Defenders should update BIND to patched versions and implement DNS query filtering to limit potential impact.

**CVE-2015-3306** — CVE-2015-3306 is an improper access control flaw in ProFTPD (file transfer software) that could allow attackers to access files they shouldn't have permission to view or modify. FTP servers often store sensitive files, so this flaw could lead to data theft or unauthorized modifications. Defenders should patch ProFTPD, restrict FTP access to necessary users only, and monitor file access logs.

**CVE-2016-3081** — CVE-2016-3081 is a command injection flaw in Apache Struts (a framework developers use to build Java web applications) that lets attackers execute arbitrary commands on the web server. Any web application built with vulnerable Struts versions is at risk of complete compromise. Defenders must update Struts to patched versions in all applications, validate and sanitize user input, and monitor server logs for suspicious command execution.

**CVE-2026-104935** — This Ivanti vulnerability (affecting versions after 22.7R2.14 but before 25.1.3.0) allows attackers to bypass authentication and run commands without logging in, exploiting a spoofing flaw (tricking the system into accepting false identity claims). Ivanti appliances control remote access to networks, so this flaw lets unauthenticated attackers gain entry to internal systems. Defenders must update to version 25.1.3.0 or later and verify that only legitimate users accessed the system before patching.

**CVE-2026-96951** — CVE-2026-96951 is a command injection flaw in Windows Shell that allows unauthenticated attackers to bypass security features and execute commands over the network. The Windows Shell is a core operating system component, so compromising it could give attackers broad control of Windows machines. Defenders should apply Microsoft security patches, implement network segmentation to limit Shell access, and use endpoint detection tools to catch malicious command execution.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*