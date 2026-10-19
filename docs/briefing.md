# 🛡️ CyberBrief — SOC — Monday, 19 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. [UPDATE] [hoch] Vercel Next.js: Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3973)

Vercel Next.js (a web framework) has multiple security flaws that attackers can exploit to run their own code on servers or crash services. This matters because Next.js is widely used to build websites, so a flaw could affect many companies at once. Defenders typically apply security patches from Vercel as soon as they're released and monitor their systems for signs of attack.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.6 Capacity management

### 2. ConnectWise Suspends Cloud Backup After Attackers Compromise Microsoft 365 Tenants
*The Hacker News* — [read more](https://thehackernews.com/2026/10/connectwise-suspends-cloud-backup-after.html)

ConnectWise (a management software company) discovered that attackers stole login credentials for seven of its applications and used them to break into customers' Microsoft 365 accounts. This matters because compromised Microsoft 365 accounts give attackers access to email, files, and other sensitive business data. Defenders should immediately reset passwords, check for unauthorized access, and change their ConnectWise credentials.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.23 Cloud services security

### 3. Microsoft: October Windows Server updates break Exchange sign-in, mail flow
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-windows-server-updates-cause-exchange-issues/)

Microsoft's October security updates for Windows Server are causing problems with Exchange Server (email software), preventing users from signing in and receiving mail. This matters because it creates a conflict between staying secure (applying patches) and keeping email working. Defenders should delay applying these updates until Microsoft releases a fix, while monitoring their systems closely for actual security threats.

### 4. OpenCode Console Breach May Have Exposed OpenAI, Anthropic, and Google API Keys
*The Hacker News* — [read more](https://thehackernews.com/2026/10/opencode-console-breach-may-have.html)

An attacker broke into an old system at OpenCode (a development tool company) and may have stolen API keys (access credentials) that users stored there for OpenAI, Anthropic, and Google services. This matters because stolen API keys let attackers use those expensive AI services on someone else's bill and access sensitive data. Defenders should assume their keys were compromised, rotate (replace) them immediately, and monitor for unusual charges.

> 📋 **ISO 27001:** A.5.19 Supplier relationships, A.5.34 Privacy and protection of PII

### 5. [UPDATE] [mittel] Fortinet FortiOS, FortiProxy und FortiSwitch: Schwachstelle ermöglicht Manipulation von Dateien
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1096)

Fortinet's firewall and network products have a flaw that lets an attacker with local access (already on the system) modify or delete files. This matters because file manipulation could disable security features or alter system configurations. Defenders should apply Fortinet's patches and limit which people have direct access to these devices.

### 6. [UPDATE] [mittel] OpenVPN: Mehrere Schwachstellen ermöglichen Umgehen von Sicherheitsvorkehrungen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2707)

OpenVPN (a remote access tool) has multiple flaws that let someone already on the system bypass security protections that are supposed to restrict what they can do. This matters because even a low-privilege attacker could escalate to gain full control. Defenders should update OpenVPN immediately and limit user accounts to only the access they truly need.

> 📋 **ISO 27001:** A.8.20 Networks security

### 7. [UPDATE] [mittel] OpenVPN: Schwachstelle ermöglicht DoS und die Offenlegung von Informationen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2605)

OpenVPN has a flaw that lets someone who is already logged in crash the service (denial of service) or steal sensitive information from it. This matters because it could disrupt remote workers and leak credentials or data. Defenders should patch OpenVPN, monitor for unusual activity from authenticated users, and have backup remote access methods.

> 📋 **ISO 27001:** A.8.6 Capacity management, A.8.20 Networks security

### 8. Hackers exploit SiteGuard WAF flaw to run commands as admins
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-siteguard-waf-flaw-to-run-commands-as-system-root/)

SiteGuard WAF (a web firewall) has a flaw that lets attackers inject operating system commands and run them with top-level (admin/root) privileges on the server. This matters because admin-level access means attackers can do almost anything, including stealing data or installing malware. Defenders should patch immediately and restrict network access to SiteGuard to only trusted locations.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2015-5477** |  ISC BIND Data Processing Errors Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2015-3306** | ProFTPD Improper Access Control Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2016-3081** | Apache Struts Command Injection Vulnerability | – | 96% | ⚠️ YES (KEV) |
| **CVE-2026-104935** | Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | – | 26% | ⚠️ YES (KEV) |
| **CVE-2021-3199** | ONLYOFFICE Docs Server Path Traversal Vulnerability | – | 20% | ⚠️ YES (KEV) |

**CVE-2015-5477** — ISC BIND (DNS software that translates domain names to IP addresses) has a flaw in how it processes data that attackers can exploit. This matters because DNS is critical infrastructure—if it breaks, users can't reach websites. Defenders should update BIND, monitor DNS query logs for suspicious patterns, and have a DNS provider as backup.

**CVE-2015-3306** — ProFTPD (file transfer software) has a flaw that lets attackers bypass access controls and reach files they shouldn't be able to access. This matters because companies often use FTP to share files with partners or customers, and this flaw could expose those files. Defenders should update ProFTPD, disable it if unused, and restrict FTP access by IP address.

**CVE-2016-3081** — Apache Struts (a web application framework) has a flaw that lets attackers inject and run arbitrary commands on the server. This matters because many web applications use Struts, so this could affect multiple systems. Defenders should update Struts immediately, use a web application firewall to block suspicious input, and scan code for this vulnerability.

**CVE-2026-104935** — Ivanti Connect Secure (a remote access VPN product) has a flaw that lets attackers bypass authentication (login requirements) by spoofing (faking) legitimate connections. This matters because VPNs are supposed to be the last line of defense—if you can skip login, attackers get direct access to internal networks. Defenders should patch immediately, reset user sessions, and check logs for unauthorized logins.

**CVE-2021-3199** — ONLYOFFICE Docs Server (document editing software) has a path traversal flaw that lets attackers access files they shouldn't by manipulating file paths in requests. This matters because users typically store sensitive documents in these systems. Defenders should patch immediately, restrict ONLYOFFICE to trusted networks, and monitor for suspicious file access.

## 📖 Jargon decoder

- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*