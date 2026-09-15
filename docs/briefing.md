# 🛡️ CyberBrief — GRC — Tuesday, 15 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🔥 Top stories

### 1. China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE
*The Hacker News* — [read more](https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html)

A hacker group linked to China sent fake emails with malicious attachments to targets, using two recently-discovered security holes (one in Chrome browser, one in Windows) to install hidden backdoor software called GRIMWEDGE that lets them spy on victims. This matters because the attacker combined multiple vulnerabilities to get past defenses, and the victims were specifically targeted rather than random. Defenders patch the known vulnerabilities immediately, monitor for suspicious network activity from affected machines, and train users to be skeptical of unexpected emails.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.6.3 Awareness, education and training

### 2. Japan's Digital Agency says VPN flaw exposed 246,000 personnel records
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/japans-digital-agency-says-vpn-flaw-exposed-246-000-personnel-records/)

Japan's government discovered that someone accessed a VPN (virtual private network—a secure tunnel for remote connections) and stole personal information about 246,000 government workers, including names and possibly addresses or ID numbers. This matters because government employee data is sensitive and can be used for blackmail, identity theft, or targeting individuals. Defenders audit who accessed the VPN, reset credentials for exposed accounts, notify affected employees, and review VPN security logs for similar breaches.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.8.2 Privileged access rights

### 3. Root RCE Zero-Day in Cisco Secure Email Gateway Under Active Exploitation
*SecurityWeek* — [read more](https://www.securityweek.com/root-rce-zero-day-in-cisco-secure-email-gateway-under-active-exploitation/)

An attacker can exploit a security flaw in Cisco Secure Email Gateway (a device that filters incoming emails) without even needing login credentials, and then run any command they want with the highest level of system access (root privileges). This matters because email gateways are critical infrastructure that protect entire organizations, and full access means an attacker can steal everything or sabotage systems. Defenders apply Cisco's security patch immediately, isolate affected appliances if patching is delayed, and monitor for suspicious commands being executed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 4. Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html)

Cisco announced that hackers are already actively attacking a critical flaw (CVE-2026-76461) in their Secure Email Gateway product that allows remote attackers to run commands as root (highest privileges) without authentication, with a severity score of 9.8 out of 10. This matters because attackers don't need special access or tricks—they can exploit this flaw against any exposed gateway—making it extremely urgent. Defenders prioritize patching this flaw above almost everything else and may temporarily take gateways offline or restrict access while waiting for patches.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 5. Revolut discloses data breach exposing financial info, passports
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/revolut-discloses-data-breach-exposing-financial-info-passports/)

Fintech company Revolut announced that someone breached their systems and obtained customer financial information and passport details after the company mistakenly shared data with someone pretending to be a government official. This matters because attackers can use financial data to commit fraud and passports for identity theft or document forgery. Defenders notify affected customers, investigate how the social engineering worked, implement stronger verification procedures for data requests, and review access logs.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 6. Personal, Financial Info Exposed in Revolut Data Breach
*SecurityWeek* — [read more](https://www.securityweek.com/personal-financial-info-exposed-in-revolut-data-breach/)

Revolut accidentally gave customer personal and financial information to a scammer who was impersonating a government agency requesting data. This matters because it shows how social engineering (manipulating people into breaking security rules) can bypass technical controls if procedures aren't strict enough. Defenders add verification steps like calling back official numbers, require multiple approvals for sensitive data requests, and train staff on recognizing impersonation attempts.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 7. Cisco patches Secure Email Gateway zero-day exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/new-cisco-secure-email-zero-day-exploited-to-execute-commands-as-root/)

Cisco released a security patch for a critical zero-day vulnerability (a flaw unknown to the public until attackers exploit it) in Secure Email Gateway that attackers were already using in real attacks. This matters because waiting to patch means live attackers are actively compromising systems. Defenders test and deploy the patch as quickly as possible, often within hours, and check logs to see if their systems were already attacked.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 8. Webinar: How malicious OAuth apps can lead to Google Workspace breaches
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/webinar-how-malicious-oauth-apps-can-lead-to-google-workspace-breaches/)

Attackers use social engineering tricks combined with fake applications that request permission to access Google Workspace (Gmail, Drive, etc.) to gain access to company data without needing stolen passwords. This matters because modern authentication is strong, so attackers work around it by tricking users into granting permissions to malicious apps. Defenders restrict what third-party apps can access Google Workspace, audit app permissions regularly, alert users about suspicious permission requests, and train staff on recognizing phishing.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.5.17 Authentication information

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-20079** | Cisco Firewall Management Center Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 76% | ⚠️ YES (KEV) |
| **CVE-2026-76461** | Cisco Secure Email Gateway SQL Injection Vulnerability | 9.8 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-48710** | Kludex Starlette HTTP Request/Response Smuggling Vulnerability | – | 36% | ⚠️ YES (KEV) |
| **CVE-2026-9586** | Sangoma Switchvox SQL Injection Vulnerability | – | 12% | ⚠️ YES (KEV) |
| **CVE-2026-85706** | GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability | – | 11% | ⚠️ YES (KEV) |

**CVE-2026-20079** — A vulnerability in Cisco Firewall Management Center (a tool that manages network firewalls) allows attackers to bypass authentication by using an alternative access method or channel. This matters because firewalls are the first line of defense against network attacks, and their management center is a high-value target—compromising it exposes the entire network. Defenders patch immediately, isolate the management center from untrusted networks, monitor for suspicious login attempts, and review access logs.

**CVE-2026-76461** — A flaw in how Cisco AsyncOS Software for Secure Email Gateway processes incoming emails allows unauthenticated remote attackers to run arbitrary commands with root privileges on the underlying operating system. This matters because email is how most organizations communicate, so a compromised email gateway gives attackers access to all internal communications and systems. Defenders apply patches urgently, check email logs for suspicious activity, isolate gateways if needed, and restore from clean backups if compromise is confirmed.

**CVE-2026-48710** — Kludex Starlette (a web framework—software for building web applications) has a vulnerability that allows attackers to manipulate HTTP requests and responses in ways that bypass security checks, a technique called request/response smuggling. This matters because web applications often contain sensitive data, and smuggling attacks can trick security tools into missing malicious traffic. Developers update the framework immediately, implement stricter input validation, and add monitoring for suspicious request patterns.

**CVE-2026-9586** — Sangoma Switchvox (a phone system) contains a SQL injection vulnerability, meaning attackers can insert malicious database commands through normal input fields to access, modify, or delete data. This matters because phone systems often control voice communications and may store customer information or call records. Defenders apply patches, restrict who can access the system, validate all user input, and monitor database queries for suspicious commands.

**CVE-2026-85706** — GitLab Community and Enterprise Edition have a path traversal vulnerability that lets attackers access files outside the intended directory by using special characters like '../' to move up the folder structure. This matters because GitLab stores source code and configuration files—compromise means attackers can steal intellectual property or find credentials hard-coded in code. Developers patch immediately, audit what files were accessed, rotate any exposed credentials, and add stricter file access controls.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*