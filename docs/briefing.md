# 🛡️ CyberBrief — SOC — Monday, 31 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. TerminalFix Uses Fake Cloudflare CAPTCHAs to Deploy Reverse-Tunnel Backdoor
*The Hacker News* — [read more](https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html)

Attackers created fake CAPTCHA pages (security challenges) that look like Cloudflare's to trick users into copying and running malicious commands in Windows Terminal or PowerShell, which are programs that let you control your computer with text commands. This matters because it's harder to spot than previous tricks since the fake page looks legitimate, and running the command gives attackers a 'backdoor'—a secret way to access your computer remotely. Defenders teach users to be suspicious of unexpected prompts asking them to run commands, and they monitor for unusual PowerShell activity.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.23 Cloud services security

### 2. Extortion Group Claims Manchester Airports Group Data Breach
*SecurityWeek* — [read more](https://www.securityweek.com/extortion-group-claims-manchester-airports-group-data-breach/)

An extortion group called FulcrumSec says they stole over 80 GB of data from Manchester Airports Group and threatened to publish it unless paid. This matters because airport operations data might include security information, passenger details, or employee records that could harm the organization and its customers if exposed. Defenders typically investigate the breach, notify affected people, work with law enforcement, and improve security controls—though paying attackers is generally discouraged because it funds more attacks.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 3. Berlin Won’t Pay Extortion Group Claiming Data Theft
*SecurityWeek* — [read more](https://www.securityweek.com/berlin-wont-pay-extortion-group-claiming-data-theft/)

The Rhysida ransomware group (a group that encrypts data and demands payment) claimed they stole over 5 TB of sensitive data from a German organization and demanded money, but Berlin officials refused to pay. This matters because it shows that paying ransoms doesn't guarantee attackers won't leak the data anyway, and paying funds criminal operations. Defenders focus on preventing the initial breach, improving backups so they don't need to pay, and working with law enforcement to disrupt these groups.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.34 Privacy and protection of PII

### 4. More Details Emerge on Exploited PaperCut Vulnerabilities
*SecurityWeek* — [read more](https://www.securityweek.com/more-details-emerge-on-exploited-papercut-vulnerabilities/)

PaperCut, a popular print management software, released a second emergency security fix for serious flaws that attackers were already exploiting; these flaws are now tracked as CVE-2026-82078 and CVE-2026-81578 (formal identifiers). This matters because organizations using PaperCut are at immediate risk if they don't patch quickly, since attackers know about and are actively using these vulnerabilities. Defenders apply the patch urgently, monitor for signs the vulnerabilities were exploited, and check if their systems were compromised.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. China-Linked Fire Ant Hijacks Cisco Routers to Steal Credentials and Blind Security Logs
*The Hacker News* — [read more](https://thehackernews.com/2026/08/china-linked-fire-ant-hijacks-cisco.html)

A Chinese government-linked hacking group called Fire Ant expanded their cyberattacks from VMware hypervisors (virtual computer hosts) to also target Cisco routers and authentication servers that control network access, aiming to steal login credentials and disable security logging. This matters because routers and authentication systems are critical infrastructure—if compromised, attackers can steal credentials for sensitive systems and hide their tracks by deleting logs. Defenders patch these devices immediately, monitor for unauthorized access and log changes, and use strong credentials with multi-factor authentication (multiple verification steps).

> 📋 **ISO 27001:** A.5.17 Authentication information, A.5.24 Incident management planning

### 6. Judge Says Pentagon’s Measures Against Anthropic Were ‘Illegal and Baseless’
*SecurityWeek* — [read more](https://www.securityweek.com/judge-says-pentagons-measures-against-anthropic-were-illegal-and-baseless/)

A judge ruled that the Pentagon's decision to label Anthropic (an AI company) as a supply chain risk was 'illegal and baseless'—meaning without legal or factual grounds—as part of Anthropic's lawsuit against the government. This matters because it affects how government agencies evaluate technology vendors and may influence AI policy going forward. Defenders in government agencies must ensure their vendor risk decisions follow legal process and are based on actual evidence, not assumptions.

> 📋 **ISO 27001:** A.5.19 Supplier relationships

### 7. Critical Ruby on Rails Vulnerability in Attackers’ Crosshairs
*SecurityWeek* — [read more](https://www.securityweek.com/critical-ruby-on-rails-vulnerability-in-attackers-crosshairs/)

A critical vulnerability in Ruby on Rails (a software framework for building web applications) called KindaRails2Shell allows attackers to read arbitrary files from a server and run their own code remotely. This matters because many websites and applications use Ruby on Rails, so this flaw could expose secrets stored in files and give attackers complete control of affected servers. Defenders patch Ruby on Rails immediately, review logs for suspicious file access, and ensure secrets like passwords are stored securely rather than in plain-text files.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. Anthropic warns infostealer malware is hijacking Claude sessions to drain usage
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/)

Anthropic warned that infostealer malware (malicious software that captures passwords and login information) on some users' computers has stolen their active Claude AI login sessions, allowing attackers to use Claude accounts and rack up usage charges. This matters because attackers can access private conversations, drain user accounts with expensive API calls, and potentially see sensitive information shared with the AI. Defenders should run antivirus scans, change Claude passwords from a clean device, and enable multi-factor authentication if available.

> 📋 **ISO 27001:** A.8.7 Protection against malware

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-60004** | Gitea Code Injection Vulnerability | – | 85% | ⚠️ YES (KEV) |
| **CVE-2021-23758** | Ajax.NET Professional Deserialization of Untrusted Data Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2026-33824** | Microsoft Internet Key Exchange (IKE) Service Extensions Double Free Vulnerability | – | 73% | ⚠️ YES (KEV) |
| **CVE-2019-1068** | Microsoft SQL Server Remote Code Execution Vulnerability | – | 53% | ⚠️ YES (KEV) |
| **CVE-2026-59310** | Broadcom VMware vCenter Path Traversal Vulnerability | – | 46% | ⚠️ YES (KEV) |

**CVE-2026-60004** — A code injection vulnerability in Gitea (a self-hosted code repository tool similar to GitHub) with identifier CVE-2026-60004 allows attackers to inject and execute malicious code. This matters because code repositories often contain source code, secrets, and intellectual property, so compromise could lead to data theft or supply chain attacks affecting customers. Defenders patch Gitea immediately, audit who accessed repositories recently, and rotate any exposed credentials like API keys.

**CVE-2021-23758** — Ajax.NET Professional (a library for building interactive web applications) has a deserialization flaw (CVE-2021-23758) that allows attackers to execute code by sending specially crafted data that the application blindly processes. This matters because deserialization flaws can let attackers run arbitrary code on servers if the application trusts untrusted input. Defenders update or replace the library, validate all incoming data, and monitor for suspicious code execution.

**CVE-2026-33824** — A double-free vulnerability (CVE-2026-33824) in Microsoft's IKE Service Extensions (part of the VPN and network encryption system) allows attackers to crash the service or potentially run code by exploiting improper memory management. This matters because IKE handles sensitive network traffic encryption, and compromising it could expose VPN traffic or enable remote code execution. Defenders apply Microsoft's security patch and monitor for service crashes or unusual network behavior.

**CVE-2019-1068** — A remote code execution flaw in Microsoft SQL Server (CVE-2019-1068) allows attackers to run arbitrary code on database servers without authentication. This matters because SQL servers often hold the most sensitive business data, and unauthenticated remote code execution means attackers can steal or destroy data without needing a username and password. Defenders apply the security patch immediately, restrict SQL Server network access to trusted sources only, and monitor for unauthorized login attempts.

**CVE-2026-59310** — A path traversal vulnerability in Broadcom VMware vCenter (CVE-2026-33824) allows attackers to access files outside their intended directory by manipulating file paths. This matters because vCenter manages virtual machines and infrastructure—compromising it could let attackers access or steal data from multiple virtual servers at once. Defenders patch vCenter urgently, review access logs for suspicious file access, and restrict vCenter network access to authorized administrators only.

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*