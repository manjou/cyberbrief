# 🛡️ CyberBrief — Net+ — Wednesday, 14 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🔥 Top stories

### 1. Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN
*SecurityWeek* — [read more](https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn/)

An attacker found a flaw in Ivanti Connect Secure (a VPN appliance that controls access to company networks) that lets them run commands with root privileges (maximum access) without even logging in, and this works even on systems with the latest security patches applied. This matters because VPN appliances are often a first entry point into corporate networks, so complete bypass means attackers can gain deep access. Defenders respond by applying emergency patches immediately, blocking suspicious traffic patterns, and checking logs to see if the flaw was exploited.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 2. Ivanti warns of Connect Secure zero-day exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/ivanti-warns-of-connect-secure-zero-day-exploited-in-attacks/)

Ivanti discovered that someone was actively using a previously unknown security flaw in their Connect Secure VPN product to break in, and they told all customers to patch right away. This matters because active exploitation means real attacks are happening now, not just theoretical scenarios. Defenders prioritize this above other work, apply patches as fast as possible, and watch for signs of compromise on their systems.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 3. Citrix, Fortinet, Ivanti Patch 29 Vulnerabilities Across Their Products
*SecurityWeek* — [read more](https://www.securityweek.com/citrix-fortinet-ivanti-patch-29-vulnerabilities-across-their-products/)

Citrix, Fortinet, and Ivanti all released patches for 29 security flaws, some of which are critical—meaning attackers could skip login checks, run their own code, or steal authentication details used to verify user identity. This matters because defenders need to patch multiple vendor products and a delay in any one of them leaves that system exposed. Defenders create a patch schedule across all three vendors, test patches in a safe environment first, then roll them out in order of severity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 4. Attacker Chains Three Ivanti Connect Secure Zero-Days for Root Access, Only Two Patched So Far
*The Hacker News* — [read more](https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html)

A security researcher found that attackers were chaining three separate zero-day flaws (previously unknown vulnerabilities) in Ivanti Connect Secure together to gain root access without authentication, but Ivanti has only released fixes for two of them so far. This matters because until all three are patched, attackers can still exploit the unfixed one to regain access. Defenders apply the two available patches immediately, isolate affected systems or disable the VPN if possible, and wait urgently for the third patch.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. Microsoft October 2026 Patch Tuesday fixes 1,411 flaws, 3 zero-days
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2026-patch-tuesday-fixes-1-411-flaws-3-zero-days/)

Microsoft released security updates on their monthly Patch Tuesday that fix 1,411 separate vulnerabilities, which is unusually high, and three of these are zero-days (one is already being exploited in real attacks, two are public knowledge but not yet widely exploited). This matters because the huge number means organizations have a lot of testing and deployment work, and the exploited zero-day requires fastest attention. Defenders prioritize the exploited zero-day, test patches for critical systems first, and deploy in waves to minimize disruption.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 6. Microsoft Patches Record 1,413 Vulnerabilities, Including Exploited Windows Zero-Day
*SecurityWeek* — [read more](https://www.securityweek.com/microsoft-patches-record-1413-vulnerabilities-including-exploited-windows-zero-day/)

Microsoft released patches for 1,413 security flaws, with CVE-2026-96951 being a Windows security feature bypass that attackers are already using in real attacks. This matters because Windows runs on most corporate machines, so this flaw is high-value for attackers. Defenders deploy this patch to all Windows systems as their top priority, often within hours, and monitor for signs of exploitation.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Ghostscript flaw lets hackers hijack servers via PDF uploads
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/ghostscript-flaw-lets-hackers-hijack-servers-via-pdf-uploads/)

A critical flaw in Ghostscript (a PDF processing tool used by many servers) allows an attacker to craft a malicious PDF file that, when the server processes it, can run arbitrary commands and take over the server. This matters because many organizations automatically process PDFs from users (converting formats, extracting text, etc.), creating an easy attack vector. Defenders apply the patch immediately, restrict PDF uploads if possible, and scan for suspicious PDF files that may have been uploaded.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. OpenAI Employee Arrested for Allegedly Planting Hidden Recorder in Executive Conference Room
*The Hacker News* — [read more](https://thehackernews.com/2026/10/openai-employee-arrested-for-allegedly.html)

An OpenAI employee was arrested for secretly planting a hidden recording device in a conference room to capture sensitive conversations, which is a physical security and insider threat incident rather than a cyber attack. This matters because it shows that security risks come from people, not just software, and that executives and sensitive projects can be targeted by insiders. Defenders respond by reviewing physical security controls, conducting insider threat training, and investigating whether any confidential information was compromised.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2015-5477** |  ISC BIND Data Processing Errors Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2015-3306** | ProFTPD Improper Access Control Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2016-3081** | Apache Struts Command Injection Vulnerability | – | 96% | ⚠️ YES (KEV) |
| **CVE-2026-104935** | Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | 8.6 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-104286** | Fortinet FortiMail Path Traversal Vulnerability | – | 2% | ⚠️ YES (KEV) |

**CVE-2015-5477** — CVE-2015-5477 is a data processing error in ISC BIND (DNS software that translates domain names to IP addresses), which is old and likely already patched in modern systems. This matters mainly as a historical reference or if legacy systems are still running unpatched versions. Defenders check if any systems still run vulnerable BIND versions and update them, as DNS compromise can redirect users to malicious sites.

**CVE-2015-3306** — CVE-2015-3306 is an improper access control flaw in ProFTPD (file transfer software), meaning someone could access files they shouldn't be allowed to, and this is an older vulnerability likely already addressed. This matters if legacy file servers still run old ProFTPD versions without patches. Defenders inventory all FTP systems, patch or replace vulnerable versions, and restrict FTP usage in favor of more secure alternatives.

**CVE-2016-3081** — CVE-2016-3081 is a command injection flaw in Apache Struts (a Java web framework), allowing attackers to run their own commands through specially crafted web requests, and this is from 2016 so most systems have moved past it. This matters if any web applications built with old Struts versions are still in production. Defenders check if their Java applications use vulnerable Struts versions, apply patches or updates, and run web application firewalls to block injection attempts.

**CVE-2026-104935** — CVE-2026-104935 is an authentication bypass flaw in Ivanti Connect Secure versions newer than 22.7R2.14 but before 25.1.3.0, allowing remote attackers to run arbitrary commands without logging in. This matters because it affects the range of Ivanti versions most organizations are likely running, creating widespread exposure. Defenders apply the patch to version 25.1.3.0 or later immediately, or implement network-level restrictions if patching is delayed.

**CVE-2026-104286** — CVE-2026-104286 is a path traversal flaw in Fortinet FortiMail (email security appliance), which means an attacker can read or modify files outside the intended directory, potentially accessing sensitive data or configuration files. This matters because email gateways see all incoming and outgoing messages, so compromise could expose confidential communications. Defenders apply Fortinet's patch immediately and review email gateway logs for suspicious file access patterns.

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*