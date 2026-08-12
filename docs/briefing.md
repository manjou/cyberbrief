# 🛡️ CyberBrief — Net+ — Wednesday, 12 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🔥 Top stories

### 1. Microsoft Patch Tuesday August 2026, (Tue, Aug 11th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33236)

Microsoft released security patches for 418 vulnerabilities in August 2026, with 62 being critical severity and 1 already being actively used in real attacks. This matters because attackers often target newly-disclosed vulnerabilities before organizations can apply patches, and the high number of critical flaws means many systems are at risk. Defenders typically prioritize applying patches for critical vulnerabilities and those known to be exploited, often within days, and may temporarily restrict access to affected systems until patches are deployed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 2. CISA: Microsoft SharePoint flaw now exploited in ransomware attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-flaw-now-exploited-in-ransomware-attacks/)

CISA confirmed that ransomware gangs are exploiting a SharePoint vulnerability (a tool used to share files and information in organizations) to break into networks and encrypt data for extortion. This matters because SharePoint is widely used and an actively-exploited vulnerability means attackers have working attack code they can reuse against many targets. Defenders should patch this vulnerability immediately on all SharePoint systems and monitor for suspicious SharePoint activity, particularly file encryption or unusual access patterns.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 3. Gunra Ransomware Exploits Fortinet and Schneider Electric Flaws to Breach Networks
*The Hacker News* — [read more](https://thehackernews.com/2026/08/gunra-ransomware-exploits-fortinet-and.html)

Gunra ransomware criminals are exploiting known vulnerabilities in Fortinet and Schneider Electric products to break into healthcare, finance, and government organizations worldwide. This matters because these sectors handle critical services and sensitive data, and criminals targeting them suggests the flaws are being weaponized at scale. Defenders in these sectors should urgently patch these products, monitor for exploitation attempts, and ensure backups are isolated so ransomware cannot encrypt them.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 4. Cisco warns of ASA and FTD VPN flaw exploited to crash devices
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisco-warns-of-asa-and-ftd-vpn-flaw-exploited-to-crash-devices/)

Cisco discovered that attackers are actively exploiting a denial-of-service vulnerability in its ASA and FTD firewalls—devices that protect network boundaries—to remotely crash them and knock them offline. This matters because a crashed firewall leaves an organization's network temporarily unprotected and causes service outages. Defenders should apply Cisco's security patch immediately and consider temporarily implementing workarounds like rate-limiting VPN connections to prevent crashes while patches are deployed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 5. DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt
*The Hacker News* — [read more](https://thehackernews.com/2026/08/deadlock-ransomware-uses-polygon-smart.html)

The DeadLock ransomware group is using blockchain and decentralized messaging services to manage their extortion operations and make it harder for authorities to shut down their infrastructure. This matters because decentralized systems are distributed across many computers worldwide, making them resilient to takedowns compared to traditional centralized servers. Defenders cannot easily block these channels, so focus shifts to preventing initial compromise through strong access controls and monitoring for unusual data exfiltration.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 6. Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands
*The Hacker News* — [read more](https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html)

Russian state-sponsored hackers are posing as job recruiters to trick IT workers in Ukraine into installing malware-laden VPN software that gives the attackers remote command-and-control capabilities on their machines. This matters because IT workers often have elevated access, making them high-value targets, and social engineering exploits human trust rather than technical vulnerabilities. Defenders should conduct security awareness training, implement email filtering to catch suspicious recruitment messages, and require verification of job opportunities through official company channels.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.6.3 Awareness, education and training

### 7. Cisco Patches Firewall Zero-Day Exploited for DoS Attacks
*SecurityWeek* — [read more](https://www.securityweek.com/cisco-patches-firewall-zero-day-exploited-for-dos-attacks/)

Cisco patched a zero-day vulnerability (CVE-2026-20349) in its firewalls that allows unauthenticated attackers to remotely crash the device by sending specially-crafted requests, causing a denial-of-service. This matters because firewalls are critical security boundaries and an unauthenticated crash means attackers need no credentials or access—just network visibility to the firewall. Defenders should apply this patch immediately as it requires no authentication to exploit, and consider implementing network segmentation to limit who can reach the firewall.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 8. Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack
*The Hacker News* — [read more](https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html)

Microsoft patched a Windows kernel driver vulnerability that is already being actively exploited; an attacker with some code running on a machine can use it to escalate to SYSTEM level—the highest privilege in Windows. This matters because privilege escalation turns a limited foothold into full system control, allowing attackers to steal everything, install backdoors, or move laterally through the network. Defenders should treat this as high-priority, patch immediately, and audit systems for signs of prior exploitation or suspicious privilege changes.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-8037** | Progress LoadMaster Command Injection Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-34486** | Apache Tomcat Missing Encryption of Sensitive Data Vulnerability | – | 83% | ⚠️ YES (KEV) |
| **CVE-2026-20349** | Cisco Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD) Heap Inspection Vulnerability | 8.6 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-72898** | Metabase SQL Injection Vulnerability | 10.0 | 1% | ⚠️ YES (KEV) |
| **CVE-2026-20316** | Cisco Secure Firewall Management Center Use of Hard-coded Password Vulnerability | – | 1% | ⚠️ YES (KEV) |

**CVE-2026-8037** — CVE-2026-8037 is a command injection vulnerability in Progress LoadMaster, meaning an attacker can send specially-crafted input that tricks the software into executing arbitrary operating system commands. This matters because successful command injection gives attackers the ability to run any command with the privileges of the LoadMaster application, potentially compromising dependent systems. Defenders should patch LoadMaster immediately, restrict who can access it over the network, and monitor for suspicious input or unexpected command execution.

**CVE-2026-34486** — CVE-2026-34486 is a vulnerability in Apache Tomcat (a widely-used application server) where sensitive data is not encrypted, making it readable to attackers who intercept traffic or access stored data. This matters because unencrypted sensitive data—like passwords, API keys, or personal information—can be easily stolen and reused for further attacks. Defenders should patch Tomcat, enable encryption for data in transit (HTTPS/TLS) and at rest, and audit what sensitive information their Tomcat instances handle.

**CVE-2026-20349** — CVE-2026-20349 is a denial-of-service flaw in Cisco Secure Firewall that allows an unauthenticated attacker to remotely send traffic that causes the firewall to unexpectedly restart. This matters because restarting a firewall disrupts all traffic flowing through it and temporarily removes network security protections. Defenders should prioritize patching this vulnerability and monitor for unusual traffic patterns targeting their firewalls, as attackers may test for this vulnerability before launching a larger attack.

**CVE-2026-72898** — CVE-2026-72898 is a SQL injection vulnerability in Metabase (a data analytics tool) that allows unauthenticated attackers to inject malicious database queries via the password reset endpoint and gain full administrator access. This matters because administrator access to Metabase means attackers can read all connected databases, modify queries, and potentially extract or manipulate sensitive business data. Defenders should patch Metabase immediately, restrict network access to it, and review who has been granted administrator access recently.

**CVE-2026-20316** — CVE-2026-20316 is a vulnerability in Cisco Secure Firewall Management Center (the central administration console for firewalls) where a hard-coded password is embedded in the software and cannot be changed by administrators. This matters because anyone who knows this password can authenticate to the management console and reconfigure or disable all firewalls the organization manages. Defenders should patch immediately, restrict network access to the management center to only authorized administrators, and monitor access logs for unauthorized login attempts using this credential.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*