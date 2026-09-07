# 🛡️ CyberBrief — SOC — Monday, 07 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw** — N-able released a fourth emergency fix in five weeks for N-central software because attackers found and exploited a critical flaw that lets them run code without permission on affected servers. [read more](https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html)
- **N-able patches max severity N-central flaw amid ongoing attacks** — N-able issued an emergency patch for a maximum-severity (the worst rating) flaw in their N-central remote monitoring and management platform that allows attackers to execute arbitrary code and take control of systems. [read more](https://www.bleepingcomputer.com/news/security/n-able-patches-max-severity-n-central-flaw-amid-ongoing-attacks/)
- **JSCeal Malware Can Bypass Google Authentication Using Stolen Session Cookies** — Researchers found JSCeal, a malware written in JavaScript that steals login credentials, watches user activity, intercepts network traffic, and can bypass Google's two-factor authentication by stealing existing session cookies (which act like reusable login tokens). [read more](https://thehackernews.com/2026/09/jsceal-malware-can-bypass-google.html)
- **Critical MikroTik Vulnerability - Patch Now, (Sun, Sep 6th)** — MikroTik released a patch for a flaw that allows attackers to log into SSH (a remote management tool) without a password, and this flaw was already being exploited by attackers in real attacks. [read more](https://isc.sans.edu/diary/rss/33314)
- **Attackers conceal phishing lures using invisible Unicode characters** — Attackers are using invisible Unicode characters (special text characters not visible on screen) hidden in phishing emails to disguise malicious links and bypass email security filters that scan for suspicious content. [read more](https://www.bleepingcomputer.com/news/security/attackers-conceal-phishing-lures-using-invisible-unicode-characters/)
- **Hackers exploit new MikroTik RouterOS flaws to hijack routers** — Attackers are chaining together two recently disclosed MikroTik router vulnerabilities to gain full control of routers that have SSH (remote management access) exposed to the internet. [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-new-mikrotik-routeros-flaws-to-hijack-routers/)
- **[UPDATE] [kritisch] Microsoft Windows Produkte: Mehrere Schwachstellen** — Microsoft released a critical patch addressing multiple vulnerabilities in Windows products that could allow attackers to escalate their access level, execute arbitrary code, crash systems, steal data, display false information, or manipulate data. [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2316)
- **Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication** — Attackers are exploiting a flaw in MikroTik routers where the SSH service is accessible from the internet but does not properly require authentication, allowing attackers to log in and gain complete administrative control without a password. [read more](https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-60004 (– CVSS, 87% EPSS)

## 🔥 Top stories

### 1. N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw
*The Hacker News* — [read more](https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html)

N-able released a fourth emergency fix in five weeks for N-central software because attackers found and exploited a critical flaw that lets them run code without permission on affected servers. This matters because N-central manages many companies' IT infrastructure, so compromised servers could affect hundreds of customer networks. Defenders must apply Hotfix 4 immediately to all on-premises N-central installations, even if they patched just days earlier with Hotfix 3, and should assume systems may have been attacked already.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.24 Incident management planning

### 2. N-able patches max severity N-central flaw amid ongoing attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/n-able-patches-max-severity-n-central-flaw-amid-ongoing-attacks/)

N-able issued an emergency patch for a maximum-severity (the worst rating) flaw in their N-central remote monitoring and management platform that allows attackers to execute arbitrary code and take control of systems. This is critical because RMM platforms are trusted entry points to customer networks, meaning a compromised platform can spread attacks to many organizations simultaneously. Defenders should treat this as a priority incident—apply the patch immediately, check logs for unauthorized access, and consider isolating affected systems while patching.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. JSCeal Malware Can Bypass Google Authentication Using Stolen Session Cookies
*The Hacker News* — [read more](https://thehackernews.com/2026/09/jsceal-malware-can-bypass-google.html)

Researchers found JSCeal, a malware written in JavaScript that steals login credentials, watches user activity, intercepts network traffic, and can bypass Google's two-factor authentication by stealing existing session cookies (which act like reusable login tokens). This matters because it defeats multi-factor authentication—a key security control—making accounts vulnerable even with strong passwords. Defenders should monitor for unusual JavaScript execution in browsers, enforce strict cookie policies, and consider additional verification for sensitive account changes.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 4. Critical MikroTik Vulnerability - Patch Now, (Sun, Sep 6th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33314)

MikroTik released a patch for a flaw that allows attackers to log into SSH (a remote management tool) without a password, and this flaw was already being exploited by attackers in real attacks. The guidance says to assume any affected device has been compromised because attackers typically create backdoor accounts that persist even after patching. Defenders must patch immediately, change all administrative credentials, audit user accounts for unauthorized additions, and review logs for unauthorized access dating back weeks.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 5. Attackers conceal phishing lures using invisible Unicode characters
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/attackers-conceal-phishing-lures-using-invisible-unicode-characters/)

Attackers are using invisible Unicode characters (special text characters not visible on screen) hidden in phishing emails to disguise malicious links and bypass email security filters that scan for suspicious content. This matters because it defeats automated defenses designed to catch phishing attempts, increasing the chance a user clicks a malicious link. Defenders should use email security tools that detect Unicode obfuscation tricks, train users to verify sender addresses carefully, and consider blocking emails with suspicious Unicode encoding.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training

### 6. Hackers exploit new MikroTik RouterOS flaws to hijack routers
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-new-mikrotik-routeros-flaws-to-hijack-routers/)

Attackers are chaining together two recently disclosed MikroTik router vulnerabilities to gain full control of routers that have SSH (remote management access) exposed to the internet. This matters because routers protect entire networks, so a compromised router becomes an entry point to attack all connected devices and networks. Defenders must ensure routers are fully patched to the latest version, disable or restrict SSH access from the internet using firewall rules, and monitor router logs for suspicious login attempts.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 7. [UPDATE] [kritisch] Microsoft Windows Produkte: Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2316)

Microsoft released a critical patch addressing multiple vulnerabilities in Windows products that could allow attackers to escalate their access level, execute arbitrary code, crash systems, steal data, display false information, or manipulate data. This matters because Windows runs on billions of devices globally, so widespread vulnerabilities create risk across the entire digital infrastructure. Defenders should apply Windows security updates immediately through Windows Update or patch management systems and prioritize patching systems exposed to the internet.

> 📋 **ISO 27001:** A.8.6 Capacity management

### 8. Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication
*The Hacker News* — [read more](https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html)

Attackers are exploiting a flaw in MikroTik routers where the SSH service is accessible from the internet but does not properly require authentication, allowing attackers to log in and gain complete administrative control without a password. This matters because routers are foundational to network security—compromised routers can eavesdrop on all traffic, redirect users to fake sites, or launch attacks against connected networks. Defenders must restrict SSH access to only trusted internal networks using firewall rules, ensure SSH password authentication is enabled and uses strong credentials, and assume any exposed router may be compromised.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-60004** | Gitea Code Injection Vulnerability | – | 87% | ⚠️ YES (KEV) |
| **CVE-2021-23758** | Ajax.NET Professional Deserialization of Untrusted Data Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2019-1068** | Microsoft SQL Server Remote Code Execution Vulnerability | – | 53% | ⚠️ YES (KEV) |
| **CVE-2023-49105** | ownCloud Improper Authentication Vulnerability | – | 43% | ⚠️ YES (KEV) |
| **CVE-2026-21962** | Oracle HTTP Server and Oracle Weblogic Server Proxy Plug-in Improper Access Control Vulnerability | – | 42% | ⚠️ YES (KEV) |

**CVE-2026-60004** — CVE-2026-60004 is a code injection vulnerability in Gitea (a self-hosted code repository platform) that allows attackers to inject and execute malicious code. This matters because code repositories often contain sensitive source code and credentials, so compromised repositories can leak intellectual property or provide attackers with blueprints to attack applications. Defenders should update Gitea immediately, restrict repository access to authorized personnel only, and audit recent commits for suspicious changes.

**CVE-2021-23758** — CVE-2021-23758 is a deserialization flaw in Ajax.NET Professional (a library for web applications) that allows attackers to execute arbitrary code by sending specially crafted data that the application processes without validation. This matters because deserialization flaws are a common attack vector for remote code execution, giving attackers full control of affected systems. Defenders should update Ajax.NET Professional immediately, implement input validation and authentication checks, and monitor applications for suspicious activity.

**CVE-2019-1068** — CVE-2019-1068 is a remote code execution flaw in Microsoft SQL Server that allows attackers to execute arbitrary code and potentially take control of database servers. This matters because SQL servers store critical business data, so a compromised server leaks data and becomes a pivot point to attack other systems. Defenders should apply Microsoft's security updates immediately, restrict SQL Server network access to only authorized applications and users, and monitor for unusual database activity or connections.

**CVE-2023-49105** — CVE-2023-49105 is an improper authentication flaw in ownCloud (a file storage and collaboration platform) that allows attackers to bypass login requirements and access files without valid credentials. This matters because it circumvents the primary security control protecting stored files and user data. Defenders should update ownCloud immediately, enforce strong passwords and multi-factor authentication, and audit access logs for unauthorized file access.

**CVE-2026-21962** — CVE-2026-21962 is an improper access control flaw in Oracle HTTP Server and Oracle WebLogic Server proxy plugins that allows attackers to bypass security restrictions and access resources they should not have permission to reach. This matters because these products sit at the gateway of many enterprise applications, so bypassed controls can expose confidential data or allow unauthorized system modifications. Defenders should apply Oracle security patches immediately, implement strict access control policies, and monitor proxy logs for unauthorized access attempts.

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*