# 🛡️ CyberBrief — Net+ — Wednesday, 30 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution** — A serious bug (memory overflow—where data is written beyond its intended storage area) was found in Citrix NetScaler, a device that controls network traffic for many organizations, and attackers are actively using it to run malicious code. [read more](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html)
- **Hackers exploit Citrix NetScaler zero-day to deploy web shells** — Attackers used the same Citrix NetScaler vulnerability to install web shells (hidden backdoors for remote access) and tunneling malware, then steal login credentials and move deeper into victim networks. [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-citrix-netscaler-zero-day-to-deploy-web-shells/)
- **Bitget hacked via zero-day in third-party security products** — Hackers broke into Bitget cryptocurrency exchange by exploiting an unknown flaw (zero-day) in third-party security software the company used, stealing $387.5 million. [read more](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)
- **Russian APT Star Blizzard Uses ‘RedFlick’ Infection Chain in Recent Attacks** — A Russian state-sponsored hacking group called Star Blizzard launched phishing campaigns using a malware chain called 'RedFlick' to deploy a backdoor called CosmicPulse. [read more](https://www.securityweek.com/russian-apt-star-blizzard-uses-redflick-infection-chain-in-recent-attacks/)
- **Russia's Star Blizzard Targets 100+ Organizations With Fake Event Invites to Deliver Backdoor** — Star Blizzard sent fake event invitations to over 100 organizations (targeting those connected to Ukraine) to trick users into installing a backdoor on Windows computers. [read more](https://thehackernews.com/2026/09/russias-star-blizzard-targets-100.html)
- **Attackers Exploit NetScaler Flaw for Root Access, Deploy WHIPSHOT and SLAPSHOT** — Unknown attackers exploited the same Citrix NetScaler flaw to gain root-level (complete) access and deployed two malware tools called WHIPSHOT and SLAPSHOT across organizations in North America and Europe in September 2026. [read more](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html)
- **Apple patches CoreGraphics zero-day flaw exploited in attacks** — Apple fixed a zero-day flaw in CoreGraphics (a core system component on iPhones and iPads) that attackers were actively exploiting in highly targeted campaigns against specific individuals. [read more](https://www.bleepingcomputer.com/news/security/apple-patches-coregraphics-zero-day-flaw-exploited-in-attacks/)
- **Former US Air Force members sent to prison over BEC attacks** — Two former US Air Force members were imprisoned for running years-long business email compromise (BEC) and phishing scams, stealing money by impersonating trusted contacts. [read more](https://www.bleepingcomputer.com/news/security/former-us-air-force-members-sent-to-prison-over-bec-attacks/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-71362 (– CVSS, 88% EPSS)

## 🔥 Top stories

### 1. Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html)

A serious bug (memory overflow—where data is written beyond its intended storage area) was found in Citrix NetScaler, a device that controls network traffic for many organizations, and attackers are actively using it to run malicious code. This matters because the flaw requires no authentication, meaning an attacker outside your network can exploit it immediately. Defenders patch the software urgently, monitor for suspicious traffic patterns, and isolate affected devices if patching is delayed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 2. Hackers exploit Citrix NetScaler zero-day to deploy web shells
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-citrix-netscaler-zero-day-to-deploy-web-shells/)

Attackers used the same Citrix NetScaler vulnerability to install web shells (hidden backdoors for remote access) and tunneling malware, then steal login credentials and move deeper into victim networks. This shows the real-world damage—it's not just a technical flaw, it's a direct path to full system compromise. Defenders respond by hunting for web shells on affected servers, resetting credentials, and reviewing network logs for unauthorized lateral movement.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 3. Bitget hacked via zero-day in third-party security products
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)

Hackers broke into Bitget cryptocurrency exchange by exploiting an unknown flaw (zero-day) in third-party security software the company used, stealing $387.5 million. This matters because defenders often trust security tools implicitly, so a flaw in those tools becomes a hidden entry point. Organizations now audit their security vendor's update practices and limit what access security tools are given to minimize damage if they are compromised.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 4. Russian APT Star Blizzard Uses ‘RedFlick’ Infection Chain in Recent Attacks
*SecurityWeek* — [read more](https://www.securityweek.com/russian-apt-star-blizzard-uses-redflick-infection-chain-in-recent-attacks/)

A Russian state-sponsored hacking group called Star Blizzard launched phishing campaigns using a malware chain called 'RedFlick' to deploy a backdoor called CosmicPulse. This matters because state-sponsored groups have more resources and persistence than typical criminals. Defenders block phishing emails, train users to spot suspicious messages, and monitor for known backdoor signatures.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.6.3 Awareness, education and training

### 5. Russia's Star Blizzard Targets 100+ Organizations With Fake Event Invites to Deliver Backdoor
*The Hacker News* — [read more](https://thehackernews.com/2026/09/russias-star-blizzard-targets-100.html)

Star Blizzard sent fake event invitations to over 100 organizations (targeting those connected to Ukraine) to trick users into installing a backdoor on Windows computers. This matters because social engineering is effective—people often trust event invitations—and once the backdoor is installed, attackers have remote control. Defenders educate users on verifying event legitimacy through official channels and deploy tools to block or detect the backdoor.

> 📋 **ISO 27001:** A.8.7 Protection against malware

### 6. Attackers Exploit NetScaler Flaw for Root Access, Deploy WHIPSHOT and SLAPSHOT
*The Hacker News* — [read more](https://thehackernews.com/2026/09/attackers-exploit-netscaler-flaw-for.html)

Unknown attackers exploited the same Citrix NetScaler flaw to gain root-level (complete) access and deployed two malware tools called WHIPSHOT and SLAPSHOT across organizations in North America and Europe in September 2026. This matters because root access means attackers control everything on that device. Defenders assume compromise, rebuild affected systems, and hunt for the malware across their network.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 7. Apple patches CoreGraphics zero-day flaw exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/apple-patches-coregraphics-zero-day-flaw-exploited-in-attacks/)

Apple fixed a zero-day flaw in CoreGraphics (a core system component on iPhones and iPads) that attackers were actively exploiting in highly targeted campaigns against specific individuals. This matters because zero-days are unknown to defenders, so affected devices had no protection until the patch. Users apply security updates immediately, and organizations track which devices received patches.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. Former US Air Force members sent to prison over BEC attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/former-us-air-force-members-sent-to-prison-over-bec-attacks/)

Two former US Air Force members were imprisoned for running years-long business email compromise (BEC) and phishing scams, stealing money by impersonating trusted contacts. This matters as a reminder that insider threats and BEC are serious crimes with real consequences. Defenders implement email authentication (SPF, DKIM, DMARC—technologies that verify an email truly comes from who it claims), train staff on payment verification, and monitor for unusual financial requests.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-71362** | Adobe Commerce and Magento Incorrect Authorization Vulnerability  | – | 88% | ⚠️ YES (KEV) |
| **CVE-2026-93616** | Check Point Multiple Products Path Traversal Vulnerability | – | 20% | ⚠️ YES (KEV) |
| **CVE-2026-76460** | Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability | – | 14% | ⚠️ YES (KEV) |
| **CVE-2026-85102** | Check Point Multiple Products Improper Certificate Validation Vulnerability | – | 8% | ⚠️ YES (KEV) |
| **CVE-2026-86950** | Apple Multiple Products Out-of-Bounds Write Vulnerability | 8.8 | 1% | ⚠️ YES (KEV) |

**CVE-2026-71362** — Adobe Commerce and Magento (e-commerce platforms) have a flaw where authorization checks fail, allowing attackers to access data or functions they shouldn't be able to reach. This matters because e-commerce sites store customer and payment data, so improper access control is a direct data-breach risk. Defenders patch immediately, review access logs for misuse, and test authorization controls on critical features.

**CVE-2026-93616** — Check Point security products have a path traversal vulnerability, meaning attackers can access files outside their intended directory (for example, escaping a sandbox to reach system files). This matters because it can lead to information theft or system compromise on security tools that should be protecting you. Defenders patch, restrict file access permissions at the operating-system level, and monitor for unusual file access patterns.

**CVE-2026-76460** — Cisco Identity Services Engine incorrectly uses privileged APIs (specialized high-permission functions), allowing attackers to perform actions they shouldn't be permitted to do. This matters because Identity Services Engine controls authentication and access across networks, so a flaw here can unlock doors to many systems. Defenders patch, enforce principle of least privilege (giving the software minimum needed permissions), and audit API usage logs.

**CVE-2026-85102** — Check Point products fail to properly validate digital certificates (the digital 'ID cards' that verify a connection is trustworthy), potentially allowing attackers to impersonate legitimate servers. This matters because without proper certificate validation, users can be tricked into connecting to attacker-controlled servers instead of real ones. Defenders patch, enable certificate pinning (locking to known-good certificates), and monitor for suspicious certificate warnings.

**CVE-2026-86950** — Apple fixed an out-of-bounds write flaw (where data is written to memory beyond safe limits) in iOS, iPadOS, and macOS that could be triggered by a maliciously crafted file, leading to arbitrary code execution. This matters because opening a normal-looking file could give attackers complete control of the device. Users update to patched versions immediately, and defenders monitor for suspicious files or unexpected system behavior.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*