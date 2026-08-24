# 🛡️ CyberBrief — SOC — Monday, 24 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. ToxicPanda Android malware uses VPN permissions to block Google Play
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/toxicpanda-android-malware-uses-vpn-permissions-to-block-google-play/)

ToxicPanda is malware (malicious software) designed for Android phones that has been updated to attack 349 different apps and respond to 167 different commands from attackers. This matters because it can now affect more apps and perform more harmful actions like blocking legitimate security checks from Google Play Store, making it harder for users to detect. Defenders respond by monitoring for this malware in mobile security tools, blocking its command-and-control servers (the attacker's remote computers), and alerting users of affected Android devices to uninstall compromised apps.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.20 Networks security

### 2. ISC Stormcast For Monday, August 24th, 2026 https://isc.sans.edu/podcastdetail/10064, (Mon, Aug 24th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33276)

This is a reference to a security podcast episode; no specific threat details are provided here. Without knowing the podcast content, there is no particular technical threat to explain or defend against. You would need to listen to or read the actual episode to understand what was discussed.

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-33824** | Microsoft Internet Key Exchange (IKE) Service Extensions Double Free Vulnerability | – | 78% | ⚠️ YES (KEV) |
| **CVE-2026-72898** | Metabase SQL Injection Vulnerability | – | 10% | ⚠️ YES (KEV) |
| **CVE-2026-64849** | MLflow Server-Side Request Forgery Vulnerability | – | 8% | ⚠️ YES (KEV) |
| **CVE-2026-55040** | Microsoft SharePoint Weak Authentication Vulnerability | – | 5% | ⚠️ YES (KEV) |
| **CVE-2026-59310** | Broadcom VMware vCenter Path Traversal Vulnerability | – | 2% | ⚠️ YES (KEV) |

**CVE-2026-33824** — A double free vulnerability in Microsoft's IKE service (a network security tool that encrypts communications) means an attacker can trigger a crash or potentially run malicious code by manipulating how memory is managed. This matters because IKE is used to secure VPN and remote connections, so compromising it could expose sensitive network traffic. Defenders typically apply Microsoft's security patches as soon as they are released, disable IKE if not needed, and monitor systems for unusual crashes or suspicious network activity.

**CVE-2026-72898** — Metabase (a data dashboard tool) contains a SQL injection flaw, meaning an attacker can insert malicious database commands through normal input fields to read or steal data without proper authorization. This matters because Metabase often stores access to sensitive company databases, so this flaw gives attackers a direct path to steal information. Defenders apply patches immediately, restrict who can access Metabase to trusted users only, and monitor database queries for suspicious or unusual patterns.

**CVE-2026-64849** — MLflow is a machine learning tool that has a server-side request forgery (SSRF) vulnerability, allowing an attacker to trick the server into making unauthorized requests to internal systems or services that should be hidden from the internet. This matters because it can expose internal company systems and lead to data theft or lateral movement (moving deeper into a network after initial compromise). Defenders patch the software, restrict network access to MLflow servers, and monitor outbound connections for unexpected requests.

**CVE-2026-55040** — SharePoint (Microsoft's document collaboration platform) has weak authentication in a recent vulnerability, meaning attackers may be able to access files and data without proper password verification or security checks. This matters because SharePoint often stores confidential business documents and intellectual property, making it a high-value target. Defenders enable multi-factor authentication (requiring a second verification method), apply Microsoft patches, and audit who has accessed sensitive documents recently.

**CVE-2026-59310** — VMware vCenter (a tool that manages virtual servers/computers) has a path traversal flaw, allowing attackers to navigate the system's file structure in unintended ways to access or modify files they should not reach. This matters because vCenter controls many virtual servers in a data center, so compromising it gives an attacker control over an entire infrastructure. Defenders patch vCenter immediately, restrict network access to it, use strong authentication, and monitor file access logs for suspicious activity.

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*