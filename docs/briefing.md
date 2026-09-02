# 🛡️ CyberBrief — Net+ — Wednesday, 02 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **SonicWall warns of actively exploited SMA1000 zero-day flaws** — SonicWall discovered two previously unknown vulnerabilities (zero-days) in their SMA1000 remote access device that attackers are already using in real attacks by combining them together. [read more](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-actively-exploited-sma1000-zero-day-flaws/)
- **GeoNetwork Fixes Unauthenticated RCE Chain Affecting Government Geoportal Backends** — GeoNetwork, software that manages geographic data for government agencies, had two security gaps that attackers could chain together to run malicious code without needing a password. [read more](https://thehackernews.com/2026/09/geonetwork-fixes-unauthenticated-rce.html)
- **Critical Langflow flaw exploited to steal OpenAI and AWS keys** — Criminals found an unauthenticated remote code execution flaw (CVE-2026-0768) in Langflow, an AI development tool, and are actively exploiting it to steal sensitive credentials like OpenAI and AWS access keys from compromised systems. [read more](https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/)
- **Attackers Exploit Critical Switchvox Flaw to Deploy Reverse Shells Without Credentials** — A critical SQL injection vulnerability (CVE-2026-9586, severity 9.3) in Sangoma Switchvox VoIP systems allows attackers to run malicious code without authentication and deploy reverse shells (a backdoor giving attacker remote control). [read more](https://thehackernews.com/2026/09/attackers-exploit-critical-switchvox.html)
- **SonicWall Warns of Two SMA1000 Zero-Days Exploited in Attacks** — Two SonicWall SMA1000 vulnerabilities (CVE-2026-83549 and CVE-2026-83548) can be stacked together by attackers to gain complete remote control without any credentials, and active exploitation is occurring. [read more](https://www.securityweek.com/sonicwall-warns-of-two-sma1000-zero-days-exploited-in-attacks/)
- **Ransomware Gang Claims Nutex Health Data Breach** — A ransomware gang claims to have stolen a large amount of sensitive data from Nutex Health, including patient records, employee information, and financial data, which the company confirmed to the SEC. [read more](https://www.securityweek.com/ransomware-gang-claims-nutex-health-data-breach/)
- **Authorities Turn Sality's P2P Network Against Itself, Cutting Off New Malware Payloads** — U.S. [read more](https://thehackernews.com/2026/09/authorities-turn-salitys-p2p-network.html)
- **Researchers Use Claude to Port Pre-Auth RCE Exploit From One PLC Model to Another** — Researchers demonstrated using an AI tool (Claude) to convert a working remote code execution exploit designed for one WAGO industrial controller model into a working exploit for a different model, proving AI can accelerate the adaptation of attacks. [read more](https://thehackernews.com/2026/09/researchers-use-claude-to-port-pre-auth.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-60004 (– CVSS, 87% EPSS)

## 🔥 Top stories

### 1. SonicWall warns of actively exploited SMA1000 zero-day flaws
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-actively-exploited-sma1000-zero-day-flaws/)

SonicWall discovered two previously unknown vulnerabilities (zero-days) in their SMA1000 remote access device that attackers are already using in real attacks by combining them together. This matters because SMA1000 devices control who can access company networks remotely, so compromising them gives attackers a direct path inside. Defenders need to apply SonicWall's emergency patches immediately and monitor their SMA1000 devices for suspicious activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. GeoNetwork Fixes Unauthenticated RCE Chain Affecting Government Geoportal Backends
*The Hacker News* — [read more](https://thehackernews.com/2026/09/geonetwork-fixes-unauthenticated-rce.html)

GeoNetwork, software that manages geographic data for government agencies, had two security gaps that attackers could chain together to run malicious code without needing a password. This is serious because government geoportals (map/data portals) rely on this software, and unauthorized access could expose sensitive geographic or infrastructure information. The vendor released fixes in July 2026, so administrators must update their systems to patched versions 4.4.12 or 4.2.17 right away.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Critical Langflow flaw exploited to steal OpenAI and AWS keys
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/)

Criminals found an unauthenticated remote code execution flaw (CVE-2026-0768) in Langflow, an AI development tool, and are actively exploiting it to steal sensitive credentials like OpenAI and AWS access keys from compromised systems. This matters because stolen cloud credentials let attackers run expensive compute jobs, access stored data, or pivot deeper into the network. Organizations using Langflow should immediately patch or isolate affected instances and rotate any exposed credentials.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 4. Attackers Exploit Critical Switchvox Flaw to Deploy Reverse Shells Without Credentials
*The Hacker News* — [read more](https://thehackernews.com/2026/09/attackers-exploit-critical-switchvox.html)

A critical SQL injection vulnerability (CVE-2026-9586, severity 9.3) in Sangoma Switchvox VoIP systems allows attackers to run malicious code without authentication and deploy reverse shells (a backdoor giving attacker remote control). This is severe because VoIP systems often sit on corporate networks with access to phone records and internal communications. Defenders must patch immediately, restrict network access to Switchvox devices, and monitor for unauthorized connections.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 5. SonicWall Warns of Two SMA1000 Zero-Days Exploited in Attacks
*SecurityWeek* — [read more](https://www.securityweek.com/sonicwall-warns-of-two-sma1000-zero-days-exploited-in-attacks/)

Two SonicWall SMA1000 vulnerabilities (CVE-2026-83549 and CVE-2026-83548) can be stacked together by attackers to gain complete remote control without any credentials, and active exploitation is occurring. This matters because compromised remote access devices become a gateway for attackers to infiltrate entire networks. Organizations must prioritize patching these flaws, review access logs for suspicious activity, and consider temporarily restricting remote access until systems are secured.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Ransomware Gang Claims Nutex Health Data Breach
*SecurityWeek* — [read more](https://www.securityweek.com/ransomware-gang-claims-nutex-health-data-breach/)

A ransomware gang claims to have stolen a large amount of sensitive data from Nutex Health, including patient records, employee information, and financial data, which the company confirmed to the SEC. This matters because healthcare data is highly regulated and worth money on the black market, and the breach may trigger legal and compliance obligations. Defenders should assume this data will be misused and monitor for fraud; affected individuals must be notified per healthcare privacy laws.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.34 Privacy and protection of PII

### 7. Authorities Turn Sality's P2P Network Against Itself, Cutting Off New Malware Payloads
*The Hacker News* — [read more](https://thehackernews.com/2026/09/authorities-turn-salitys-p2p-network.html)

U.S. and European law enforcement took control of the Sality botnet's peer-to-peer (P2P) network infrastructure in a coordinated August 2026 operation, preventing attackers from sending new malware instructions to infected computers. This matters because botnets allow criminals to remotely control thousands of compromised devices for attacks or data theft. Organizations should scan for and remove Sality malware infections, which researchers can now better identify since the botnet is disrupted.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 8. Researchers Use Claude to Port Pre-Auth RCE Exploit From One PLC Model to Another
*The Hacker News* — [read more](https://thehackernews.com/2026/09/researchers-use-claude-to-port-pre-auth.html)

Researchers demonstrated using an AI tool (Claude) to convert a working remote code execution exploit designed for one WAGO industrial controller model into a working exploit for a different model, proving AI can accelerate the adaptation of attacks. This matters because industrial controllers (PLCs) operate critical infrastructure like factories and power systems, and easier exploit adaptation means more widespread risk. Defenders of industrial systems must aggressively patch devices, segment networks, and monitor for unauthorized code execution.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-60004** | Gitea Code Injection Vulnerability | – | 87% | ⚠️ YES (KEV) |
| **CVE-2021-23758** | Ajax.NET Professional Deserialization of Untrusted Data Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2019-1068** | Microsoft SQL Server Remote Code Execution Vulnerability | – | 53% | ⚠️ YES (KEV) |
| **CVE-2023-49105** | ownCloud Improper Authentication Vulnerability | – | 43% | ⚠️ YES (KEV) |
| **CVE-2026-21962** | Oracle HTTP Server and Oracle Weblogic Server Proxy Plug-in Improper Access Control Vulnerability | – | 42% | ⚠️ YES (KEV) |

**CVE-2026-60004** — CVE-2026-60004 is a code injection vulnerability in Gitea, a self-hosted git repository platform, that allows attackers to inject and execute malicious code. This matters because Gitea often holds proprietary source code and development tools, so compromise can leak intellectual property or inject backdoors into software. Teams using Gitea must apply available patches, restrict who can commit code, and audit recent commits for suspicious changes.

**CVE-2021-23758** — CVE-2021-23758 is a deserialization vulnerability in Ajax.NET Professional, a web development library that improperly handles untrusted data, allowing remote code execution. This matters because deserialization flaws turn data that should be inert into executable code, giving attackers a direct path to compromise. Developers must update the library, avoid deserializing untrusted input, and validate all incoming data.

**CVE-2019-1068** — CVE-2019-1068 is a remote code execution vulnerability in Microsoft SQL Server that allows attackers to run malicious commands on database servers. This matters because SQL Servers often store the most sensitive business and customer data, so compromise means total data exposure and possible ransomware deployment. Organizations must apply Microsoft patches, restrict network access to SQL Servers, and monitor for unusual database activity.

**CVE-2023-49105** — CVE-2023-49105 is an improper authentication flaw in ownCloud, a file-sharing and collaboration platform, that could allow attackers to bypass login controls and access files without valid credentials. This matters because ownCloud instances often store confidential company or personal files, and broken authentication means anyone can access them. Administrators must patch ownCloud immediately, audit access logs for unauthorized logins, and consider requiring additional security layers like multi-factor authentication.

**CVE-2026-21962** — CVE-2026-21962 is an improper access control flaw in Oracle HTTP Server and WebLogic Server proxy plugins that allows attackers to access resources they shouldn't be allowed to reach. This matters because these Oracle components often front-end critical applications and databases, so broken access controls bypass intended security boundaries. Organizations must patch Oracle components, review and tighten access control rules, and audit logs for attempts to access restricted resources.

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