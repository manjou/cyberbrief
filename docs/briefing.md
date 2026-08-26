# 🛡️ CyberBrief — Net+ — Wednesday, 26 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data** — A critical security flaw in Oracle's WebLogic Server (enterprise application software) can be exploited by attackers without needing to log in, allowing them to steal sensitive data. [read more](https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html)
- **Hospital operator Nutex Health says data stolen in cyberattack** — An unauthorized person or group gained access to Nutex Health's servers and copied confidential company data without permission. [read more](https://www.bleepingcomputer.com/news/security/hospital-operator-nutex-health-says-data-stolen-in-cyberattack/)
- **LACMA data breach last year exposed social security and medical data** — LACMA experienced a data breach last year where someone accessed and copied visitor and employee information, including social security numbers and medical details. [read more](https://www.bleepingcomputer.com/news/security/lacma-data-breach-last-year-exposed-social-security-and-medical-data/)
- **CISA Warns of Exploited Gitea Vulnerability** — Gitea (a self-hosted code repository platform similar to GitHub) had a remote code execution vulnerability—meaning attackers could run malicious commands on servers running vulnerable versions. [read more](https://www.securityweek.com/cisa-warns-of-exploited-gitea-vulnerability/)
- **Unpatched Calix flaw lets hackers bypass NAT to expose internal devices** — Residential routers made by Calix contain an unpatched security flaw that allows remote attackers to create port-forwarding rules, essentially punching a hole through the router's firewall (NAT, or Network Address Translation) to expose private home or small-business networks to the internet. [read more](https://www.bleepingcomputer.com/news/security/unpatched-calix-flaw-lets-hackers-bypass-nat-to-expose-internal-devices/)
- **Hackers breached over 270 Zimbra servers in ongoing attacks** — Attackers exploited a serious vulnerability in Zimbra Collaboration Suite (an email and collaboration platform) to break into over 270 separate Zimbra installations and execute malicious code on those servers. [read more](https://www.bleepingcomputer.com/news/security/hackers-breached-over-270-zimbra-servers-in-ongoing-attacks/)
- **U.S. Sanctions Iran-Linked Hackers Behind Critical Infrastructure Breaches** — The U.S. [read more](https://thehackernews.com/2026/08/us-sanctions-iran-linked-hackers-behind.html)
- **Police arrests dozens of suspects in global cybercrime crackdown** — Police and cybercrime investigators from 22 countries worked together to identify 263 suspects involved in organized cybercrime networks run by African crime groups, resulting in 58 arrests. [read more](https://www.bleepingcomputer.com/news/security/police-arrests-dozens-of-suspects-in-global-cybercrime-crackdown/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-59310 (– CVSS, 46% EPSS)

## 🔥 Top stories

### 1. Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data
*The Hacker News* — [read more](https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html)

A critical security flaw in Oracle's WebLogic Server (enterprise application software) can be exploited by attackers without needing to log in, allowing them to steal sensitive data. This matters because WebLogic runs mission-critical systems at many large organizations, so this vulnerability puts valuable data at immediate risk. Defenders must apply Oracle's security patches urgently and monitor for suspicious access to these systems, since CISA confirmed attackers are already actively using this flaw.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Hospital operator Nutex Health says data stolen in cyberattack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hospital-operator-nutex-health-says-data-stolen-in-cyberattack/)

An unauthorized person or group gained access to Nutex Health's servers and copied confidential company data without permission. This is serious because healthcare data often includes personal medical records and financial information that patients and employees trust the organization to protect. Organizations respond by notifying affected people, investigating how the breach happened, securing their systems against further attacks, and often offering credit monitoring services to those whose data was stolen.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.24 Incident management planning

### 3. LACMA data breach last year exposed social security and medical data
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/lacma-data-breach-last-year-exposed-social-security-and-medical-data/)

LACMA experienced a data breach last year where someone accessed and copied visitor and employee information, including social security numbers and medical details. This type of breach is harmful because social security numbers and medical records can be used for identity theft or sold on the dark web. Museums and cultural institutions typically respond by investigating the incident, notifying people whose data was compromised, improving access controls to their systems, and implementing stronger monitoring to catch unauthorized access.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.8.2 Privileged access rights

### 4. CISA Warns of Exploited Gitea Vulnerability
*SecurityWeek* — [read more](https://www.securityweek.com/cisa-warns-of-exploited-gitea-vulnerability/)

Gitea (a self-hosted code repository platform similar to GitHub) had a remote code execution vulnerability—meaning attackers could run malicious commands on servers running vulnerable versions. This matters because developers often store source code and secrets in repositories, so compromising a Gitea server can give attackers access to the organization's entire codebase and internal credentials. Defenders must immediately update to the patched version (1.27.1 or later) and audit their Gitea servers for signs of unauthorized access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Unpatched Calix flaw lets hackers bypass NAT to expose internal devices
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/unpatched-calix-flaw-lets-hackers-bypass-nat-to-expose-internal-devices/)

Residential routers made by Calix contain an unpatched security flaw that allows remote attackers to create port-forwarding rules, essentially punching a hole through the router's firewall (NAT, or Network Address Translation) to expose private home or small-business networks to the internet. This is dangerous because it gives attackers direct access to printers, computers, and cameras that were supposed to be protected by the router. Defenders and ISPs must pressure Calix to release a patch, replace vulnerable routers, or implement network-level protections until fixes are available.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 6. Hackers breached over 270 Zimbra servers in ongoing attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-breached-over-270-zimbra-servers-in-ongoing-attacks/)

Attackers exploited a serious vulnerability in Zimbra Collaboration Suite (an email and collaboration platform) to break into over 270 separate Zimbra installations and execute malicious code on those servers. This matters because email servers hold sensitive communications, contacts, and calendar information, so compromising them gives attackers access to private business and personal information. Organizations running Zimbra must immediately patch the vulnerability, force password resets for affected users, and search their email logs for signs of attacker activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. U.S. Sanctions Iran-Linked Hackers Behind Critical Infrastructure Breaches
*The Hacker News* — [read more](https://thehackernews.com/2026/08/us-sanctions-iran-linked-hackers-behind.html)

The U.S. Treasury Department announced economic sanctions against Iranian hacking groups that have broken into critical infrastructure (power grids, water systems, etc.) in the United States and allied nations. This matters because attacks on critical infrastructure can endanger public safety and national security. This type of government response signals that cyber attacks have serious diplomatic and economic consequences, and it typically leads to increased international cooperation on cybercrime enforcement and stricter regulations on organizations doing business with sanctioned entities.

### 8. Police arrests dozens of suspects in global cybercrime crackdown
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/police-arrests-dozens-of-suspects-in-global-cybercrime-crackdown/)

Police and cybercrime investigators from 22 countries worked together to identify 263 suspects involved in organized cybercrime networks run by African crime groups, resulting in 58 arrests. This is significant because it shows international law enforcement is coordinating to disrupt criminal hacking operations at scale. These operations typically involve ransom attacks, fraud, and identity theft, so coordinated enforcement reduces the criminals' ability to operate freely and sends a deterrent message.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-59310** | Broadcom VMware vCenter Path Traversal Vulnerability | – | 46% | ⚠️ YES (KEV) |
| **CVE-2026-33824** | Microsoft Internet Key Exchange (IKE) Service Extensions Double Free Vulnerability | – | 73% | ⚠️ YES (KEV) |
| **CVE-2026-21962** | Oracle HTTP Server and Oracle Weblogic Server Proxy Plug-in Improper Access Control Vulnerability | – | 42% | ⚠️ YES (KEV) |
| **CVE-2025-62593** | Ray-Project Ray Code Injection Vulnerability | – | 17% | ⚠️ YES (KEV) |
| **CVE-2026-64849** | MLflow Server-Side Request Forgery Vulnerability | – | 16% | ⚠️ YES (KEV) |

**CVE-2026-59310** — This is a path traversal vulnerability in Broadcom VMware vCenter (a tool for managing virtual servers in data centers), meaning attackers can use specially crafted requests to access files they shouldn't be able to reach on the system. This matters because vCenter controls hundreds or thousands of virtual machines, so compromising it gives attackers broad access to an organization's entire virtualized infrastructure. Defenders must apply the vendor patch immediately and restrict network access to vCenter to only trusted administrators.

**CVE-2026-33824** — This is a double free vulnerability in Microsoft's Internet Key Exchange (IKE) service, a protocol used for secure VPN connections; the flaw can cause the service to crash or potentially allow code execution. This matters because VPNs protect remote worker connections, so compromising IKE could allow attackers to intercept or block secure remote access. Defenders must apply Microsoft's security updates and monitor VPN infrastructure for crashes or suspicious activity.

**CVE-2026-21962** — This vulnerability is in the proxy plug-in component of Oracle HTTP Server and WebLogic Server that fails to properly check user permissions, potentially allowing unauthorized access to restricted data or functions. This matters because these are widely used enterprise systems handling sensitive business operations. Defenders must apply Oracle's patches, review access logs to see if the flaw was exploited, and ensure proper authentication controls are in place.

**CVE-2025-62593** — Ray (a Python framework for distributed computing) contains a code injection vulnerability that allows attackers to execute arbitrary code on systems running Ray. This matters because Ray is used in data science and machine learning pipelines that often process sensitive data, so compromising Ray could allow attackers to steal data or manipulate results. Defenders must update Ray to the patched version and audit Ray clusters for suspicious activity or code execution.

**CVE-2026-64849** — MLflow (a machine learning experiment tracking platform) contains a Server-Side Request Forgery (SSRF) vulnerability, meaning attackers can trick the MLflow server into making unintended network requests to internal systems that should be unreachable from the internet. This matters because MLflow often runs on internal networks with access to databases and other sensitive services, so an SSRF flaw can expose that internal infrastructure. Defenders must patch MLflow immediately, restrict its network access, and monitor for suspicious outbound requests from the MLflow server.

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*