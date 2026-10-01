# 🛡️ CyberBrief — SOC — Thursday, 01 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. DIVD says Zammad zero-days enabled AI-driven network breach
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/)

DIVD's own network was breached because attackers exploited two previously unknown security holes (zero-days) in Zammad, a help-desk ticketing system they were using. This matters because it shows that even security researchers and defensive organizations can be compromised, and that chaining multiple vulnerabilities together makes attacks more powerful. Defenders now need to patch Zammad immediately, review their logs for suspicious activity, and consider using alternative ticketing systems while waiting for fixes.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets
*The Hacker News* — [read more](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)

Attackers used a patched flaw (CVE-2026-73570) in Zimbra email software to plant persistent backdoors called web shells and steal login credentials from mailboxes. This matters because email systems are critical targets—compromised mailboxes expose sensitive communications and can be used to launch further attacks. Defenders must apply the patch urgently, scan servers for web shells, reset credentials for any exposed accounts, and monitor for unauthorized email access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 3. CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/)

A critical flaw in MikroTik RouterOS allows attackers to remotely execute malicious commands or crash routers without needing valid login credentials. This matters because routers are network gatekeepers—compromising them affects everything connected behind them. Defenders should urgently patch or replace affected routers, isolate them during patching, and monitor for suspicious remote connections.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 4. Zammad Zero-Days Exploited in AI-Powered DIVD Hack
*SecurityWeek* — [read more](https://www.securityweek.com/zammad-zero-days-exploited-in-ai-powered-divd-hack/)

Attackers chained two Zammad vulnerabilities to take over user sessions, run arbitrary code (remote code execution), and gain highest-level system access (root privileges). This matters because attackers went from initial breach to complete system control. Defenders must patch both flaws together, invalidate existing sessions, reset administrative credentials, and audit what attackers accessed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. Cisco Patches Exploited Catalyst SD-WAN Zero-Day Vulnerability
*SecurityWeek* — [read more](https://www.securityweek.com/cisco-patches-exploited-catalyst-sd-wan-zero-day-vulnerability/)

A previously unknown flaw in Cisco SD-WAN appliances allows unauthenticated attackers to remotely log in with administrator-level permissions and control the device. This matters because SD-WAN devices manage network traffic across multiple locations—full administrative access is catastrophic. Defenders must apply patches immediately, implement network access controls to limit who can reach these appliances, and change all admin passwords.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 6. Bitget hacked via zero-day in third-party security products
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)

Bitget cryptocurrency exchange lost $387.5 million after attackers exploited a zero-day flaw not in Bitget's own code, but in third-party security software running on their systems. This matters because defenders often trust security tools without realizing they can become attack entry points. Defenders should inventory all third-party security software, monitor vendor advisories closely, sandbox security tools with minimal privileges, and diversify tools to avoid single points of failure.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 7. Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html)

Researchers publicly revealed how to exploit a critical Citrix NetScaler flaw (CVE-2026-88772, scored 9.5/10 severity) involving a memory overflow that lets attackers run malicious code without authentication. This matters because published exploit details make attacks easier for criminals, and NetScaler appliances often sit at network edges protecting critical infrastructure. Defenders must patch immediately before exploit code becomes widely automated, monitor for exploitation attempts, and assume devices may already be compromised.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 8. CISA Adds Exploited Cisco Catalyst SD-WAN Manager Auth Bypass to KEV
*The Hacker News* — [read more](https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html)

A critical Cisco SD-WAN Manager flaw allows unauthenticated attackers to bypass login requirements and gain admin access—and CISA confirmed it's actively being exploited in the wild. This matters because many organizations use this software to manage distributed networks, and active exploitation means attackers are using this vulnerability right now. Defenders must patch immediately, assume breach, review logs for unauthorized access, and reset all credentials.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-71362** | Adobe Commerce and Magento Incorrect Authorization Vulnerability  | – | 88% | ⚠️ YES (KEV) |
| **CVE-2026-76504** | Cisco Catalyst SD-WAN Manager Hex Encoding Vulnerability | 9.8 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-87902** | WordPress Core Remote File Inclusion Vulnerability | – | 20% | ⚠️ YES (KEV) |
| **CVE-2026-93616** | Check Point Multiple Products Path Traversal Vulnerability | – | 20% | ⚠️ YES (KEV) |
| **CVE-2026-85102** | Check Point Multiple Products Improper Certificate Validation Vulnerability | – | 8% | ⚠️ YES (KEV) |

**CVE-2026-71362** — Adobe Commerce and Magento e-commerce platforms have an authorization bypass flaw (CVE-2026-71362) that could let attackers access data or functions they shouldn't be able to reach. This matters because e-commerce platforms handle payment data and customer information—improper access controls can lead to data theft. Defenders must patch, audit user access logs, verify data wasn't stolen, and test authorization controls.

**CVE-2026-76504** — The Cisco SD-WAN Manager authentication bypass occurs because the system incorrectly handles URL encoding in requests, allowing attackers to skip login checks and access the system as an administrator. This matters because improper URL encoding is a common but critical mistake that bypasses security controls entirely. Defenders must apply the patch, review code for similar encoding flaws, and implement Web Application Firewalls (WAF) to catch malformed requests.

**CVE-2026-87902** — WordPress Core contains a remote file inclusion vulnerability (CVE-2026-87902) that could allow attackers to trick the system into loading malicious code from external servers. This matters because WordPress powers millions of websites—a widely exploitable flaw affects many targets. Defenders must update WordPress immediately, audit plugins for similar flaws, restrict where WordPress can load files from, and monitor for suspicious external file requests.

**CVE-2026-93616** — Check Point security products have a path traversal vulnerability (CVE-2026-93616) allowing attackers to access files and folders outside their intended directories by manipulating file paths. This matters because Check Point products protect networks—if attackers escape normal access controls, they can steal sensitive files or configuration data. Defenders must patch, audit what files attackers may have accessed, and implement file system restrictions.

**CVE-2026-85102** — Check Point products incorrectly validate security certificates (CVE-2026-85102), potentially allowing attackers to impersonate legitimate servers or intercept encrypted communications. This matters because certificate validation is a core trust mechanism—without proper checks, attackers can perform man-in-the-middle attacks and decrypt supposedly secure traffic. Defenders must patch, revoke any certificates used maliciously, implement certificate pinning where possible, and monitor for suspicious connections.

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*