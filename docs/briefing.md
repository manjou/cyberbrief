# 🛡️ CyberBrief — SOC — Thursday, 13 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. Cisco ASA and FTD Flaw Exploited in the Wild Can Trigger Remote DoS
*The Hacker News* — [read more](https://thehackernews.com/2026/08/cisco-asa-and-ftd-flaw-exploited-in.html)

Cisco discovered a serious flaw in their firewall products (ASA and FTD) that attackers are already using to crash these devices remotely. This matters because firewalls are critical security tools that protect networks, so crashing them leaves companies vulnerable to further attacks. Defenders need to apply Cisco's security patches immediately and monitor their firewall logs for signs of attack attempts.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 2. Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor
*The Hacker News* — [read more](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

North Korea's Lazarus Group discovered and exploited a previously unknown Windows flaw to break into defense and aerospace companies in multiple countries, installing hidden backdoor software (ForestTiger) that gives them ongoing access. This is serious because aerospace and defense organizations hold sensitive information, and backdoors allow attackers to steal data or launch future attacks undetected. Defenders must apply Microsoft's patch, scan systems for the ForestTiger backdoor, and assume their networks may have been compromised until proven otherwise.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 3. Fresh Windows Zero-Day Exploited in North Korean Cyberattacks
*SecurityWeek* — [read more](https://www.securityweek.com/fresh-windows-zero-day-exploited-in-north-korean-cyberattacks/)

Attackers used a Windows zero-day (previously unknown vulnerability) to gain complete control of victim systems and install the ForestTiger backdoor for persistent access. This matters because full system control means attackers can steal anything, modify files, or use the computer to attack other networks. Defenders should patch Windows immediately, hunt for ForestTiger indicators of compromise, and implement detection rules to catch similar backdoor activity.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 4. SAP Commerce Cloud Flaw Could Let Unauthenticated Attackers Execute Arbitrary Code
*The Hacker News* — [read more](https://thehackernews.com/2026/08/sap-commerce-cloud-flaw-could-let.html)

SAP released an emergency patch for a maximum-severity flaw in their Commerce Cloud product that would let attackers without login credentials run any code they want on affected systems. This is critical because it requires no authentication (meaning attackers don't need a username/password) and affects a widely-used e-commerce platform. Defenders must patch SAP Commerce Cloud immediately, review access logs for suspicious activity, and scan systems for signs of unauthorized code execution.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 5. Cisco warns of ASA and FTD VPN flaw exploited to crash devices
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisco-warns-of-asa-and-ftd-vpn-flaw-exploited-to-crash-devices/)

Cisco reported that attackers are actively exploiting a high-severity flaw in Secure Firewall (ASA and FTD) to remotely crash these devices and knock them offline. This matters because a crashed firewall stops protecting the network, potentially allowing attackers to access protected systems. Defenders should urgently apply patches, enable monitoring for crash attempts, and test failover systems to ensure backup protection if the firewall goes down.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 6. Microsoft Plugs Nearly 400 Security Holes
*Krebs on Security* — [read more](https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/)

Microsoft released patches for nearly 400 security holes across Windows and their software products, including one flaw that attackers are already exploiting and two others that details were publicly shared. This matters because the volume of vulnerabilities means some systems will be patched late, giving attackers a window to attack unpatched computers. Defenders should prioritize patching the actively exploited vulnerability first, test patches before deploying widely, and track which systems remain unpatched.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Stealthy ‘City-Forum’ Attacks Target Salesforce and ServiceNow With Custom Toolset
*SecurityWeek* — [read more](https://www.securityweek.com/stealthy-city-forum-attacks-target-salesforce-and-servicenow-with-custom-toolset/)

Researchers discovered a new attack campaign (City-Forum) targeting Salesforce and ServiceNow by exploiting guest access features to quietly gather and steal exposed customer data without leaving obvious traces. This matters because Salesforce and ServiceNow store sensitive customer and business information, so this attack likely affected many companies using these platforms. Defenders should audit guest access settings, enable detailed logging, search for signs of unauthorized data access, and consider restricting or requiring authentication for guest features.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 8. SharePoint Vulnerability Exploited Shortly After PoC Release
*SecurityWeek* — [read more](https://www.securityweek.com/sharepoint-vulnerability-exploited-shortly-after-poc-release/)

A SharePoint vulnerability that Microsoft patched in July was later exploited in real attacks after someone publicly released proof-of-concept code showing how the flaw works. This matters because public exploit code makes attacks easier and more widespread since attackers don't need to develop their own tools. Defenders should have already applied the July patch, but if they haven't, they need to do so urgently and verify no breach occurred.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-8037** | Progress LoadMaster Command Injection Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-34486** | Apache Tomcat Missing Encryption of Sensitive Data Vulnerability | – | 83% | ⚠️ YES (KEV) |
| **CVE-2026-20349** | Cisco Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD) Heap Inspection Vulnerability | 8.6 | 1% | ⚠️ YES (KEV) |
| **CVE-2026-9198** | IBM Langflow Code Injection Vulnerability | – | 17% | ⚠️ YES (KEV) |
| **CVE-2026-63077** | JetBrains TeamCity Deserialization of Untrusted Data Vulnerability | – | 11% | ⚠️ YES (KEV) |

**CVE-2026-8037** — Progress LoadMaster contains a command injection vulnerability (CVE-2026-8037) that allows attackers to inject malicious commands into the system. This matters because LoadMaster is a load balancer that sits in front of critical applications, so compromising it gives attackers access to important systems. Defenders should apply Progress patches, restrict access to LoadMaster administration interfaces, and monitor for suspicious command execution.

**CVE-2026-34486** — Apache Tomcat has a vulnerability (CVE-2026-34486) where sensitive data is stored without encryption, meaning attackers who access the system can read confidential information in plain text. This matters because unencrypted sensitive data (like passwords or tokens) is easy for attackers to steal and misuse. Defenders should update Tomcat, encrypt sensitive data at rest, review access controls, and search for evidence of data theft.

**CVE-2026-20349** — CVE-2026-20349 is a flaw in Cisco's Secure Firewall VPN service where unauthenticated remote attackers can send specially crafted requests to crash the firewall device. This matters because VPN is often the remote access point for employees, so crashing it disables secure remote work and potentially leaves networks exposed. Defenders must patch Cisco Secure Firewall immediately, monitor VPN logs for malicious requests, and ensure backup VPN capacity is available.

**CVE-2026-9198** — IBM Langflow contains a code injection vulnerability (CVE-2026-9198) where attackers can insert and execute malicious code within the application. This matters because code injection gives attackers complete control to steal data, modify systems, or move deeper into the network. Defenders should update IBM Langflow, restrict network access to it, review activity logs for suspicious code execution, and scan for signs of compromise.

**CVE-2026-63077** — JetBrains TeamCity has a deserialization vulnerability (CVE-2026-63077) where untrusted data is processed in a way that allows attackers to execute arbitrary code. This matters because TeamCity is used for software builds and deployments, so compromising it could let attackers inject malicious code into software products. Defenders must patch TeamCity immediately, audit recent builds for tampering, restrict network access, and implement additional validation of serialized data.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*