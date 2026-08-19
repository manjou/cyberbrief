# 🛡️ CyberBrief — Net+ — Wednesday, 19 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🔥 Top stories

### 1. CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE
*The Hacker News* — [read more](https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html)

A critical flaw in Ray (a Python tool for running distributed computing tasks) is being actively exploited by attackers to run malicious code directly in web browsers. This matters because Ray is widely used by organizations for data processing and AI work, so vulnerable systems could be compromised at scale. Defenders patch Ray immediately, monitor for suspicious activity, and check their systems for signs of prior exploitation.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. CISA: Windows Task Host flaw now exploited by ransomware gangs
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/)

Ransomware gangs have started exploiting a Windows vulnerability in Task Host (a Windows system component) that was first reported as at-risk in April. This matters because it gives attackers an easier way to gain control of Windows systems and deploy ransomware without needing user interaction. Defenders apply the available patch urgently, monitor for exploitation attempts in logs, and treat any suspicious Task Host activity as a potential intrusion.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 3. Ransom Busters Claims It Hacked Ransomware Servers, Asks Victims for Up to $60,000
*The Hacker News* — [read more](https://thehackernews.com/2026/08/ransom-busters-claims-it-hacked.html)

A group calling themselves 'Ransom Busters' is contacting organizations that have already been hit by ransomware, offering to delete stolen data from ransomware gang servers for $20,000–$60,000 per victim. This matters because it's unclear whether these offers are legitimate recovery help or a scam to steal additional money from already-victimized companies. Defenders inform affected organizations to be extremely skeptical, verify any such claims independently, and involve law enforcement before making payments to unknown third parties.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.19 Supplier relationships

### 4. Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads
*The Hacker News* — [read more](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

A critical flaw in Forminator, a WordPress form-building plugin used by over 600,000 sites, allows attackers without credentials to upload and run malicious PHP code on vulnerable websites. This matters because attackers could take over any WordPress site using this plugin without needing legitimate access, affecting large numbers of businesses. Defenders immediately update Forminator to the patched version, scan for signs of malicious file uploads, and review file repositories for suspicious PHP files.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Attackers Exploit MLflow SSRF Flaw to Steal Cloud Credentials and Secrets
*The Hacker News* — [read more](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)

Two critical flaws in MLflow (an AI platform) and FUXA (industrial automation software) allow attackers to bypass normal access controls (SSRF attacks) and steal cloud credentials and secrets like API keys. This matters because credentials can unlock access to cloud infrastructure, databases, and sensitive systems, potentially leading to complete data theft. Defenders patch both tools immediately, rotate affected credentials, monitor for unauthorized API usage, and restrict where these tools can access on the network.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 6. Clop created custom web shell for Windchill data theft attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/)

The Clop ransomware gang created a custom hacking tool designed specifically for PTC Windchill (engineering/product data management software) that can steal credentials and files directly from servers. This matters because it shows attackers are building specialized tools targeting specific business software, making attacks more effective against organizations using Windchill. Defenders audit Windchill servers for unauthorized access, patch PTC software, review user credentials, and monitor for the specific behaviors this web shell performs.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.17 Authentication information

### 7. Heights Finance Data Breach Impacts at Least 1.2 Million Individuals
*SecurityWeek* — [read more](https://www.securityweek.com/heights-finance-data-breach-impacts-at-least-1-2-million-individuals/)

Hackers accessed Heights Finance's systems and stole personal data on at least 1.2 million people, including names, addresses, phone numbers, Social Security numbers, and financial information. This matters because this data can be used for identity theft, fraud, and spam attacks against victims for years to come. Defenders (in this case Heights Finance) notify affected people, offer credit monitoring, investigate how the breach occurred, and implement stronger access controls to prevent recurrence.

> 📋 **ISO 27001:** A.5.19 Supplier relationships, A.5.34 Privacy and protection of PII

### 8. GitLab Patches Critical Code Injection Vulnerability
*SecurityWeek* — [read more](https://www.securityweek.com/gitlab-patches-critical-code-injection-vulnerability/)

GitLab, a platform for managing and sharing code, has a flaw that allows unauthenticated attackers (those without valid login credentials) to modify code, delete user accounts, and remove entire projects. This matters because attackers could sabotage code repositories, destroy development work, or inject malicious code without being detected as a known user. Defenders patch GitLab immediately, review access logs for suspicious activity, restore from backups if needed, and restrict external access to GitLab instances.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-8037** | Progress LoadMaster Command Injection Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-33824** | Microsoft Internet Key Exchange (IKE) Service Extensions Double Free Vulnerability | – | 56% | ⚠️ YES (KEV) |
| **CVE-2026-59310** | Broadcom VMware vCenter Path Traversal Vulnerability | – | 1% | ⚠️ YES (KEV) |
| **CVE-2026-20349** | Cisco Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD) Heap Inspection Vulnerability | – | 1% | ⚠️ YES (KEV) |
| **CVE-2026-63077** | JetBrains TeamCity Deserialization of Untrusted Data Vulnerability | – | 11% | ⚠️ YES (KEV) |

**CVE-2026-8037** — Progress LoadMaster (a load-balancing appliance that distributes network traffic) has a command injection vulnerability (CVE-2026-8037) that allows attackers to run arbitrary system commands on the device. This matters because compromising a load balancer gives attackers a central point to spy on or manipulate traffic flowing through an organization's network. Defenders patch LoadMaster, audit configuration changes, monitor command execution logs, and check for signs of suspicious network traffic interception.

**CVE-2026-33824** — Microsoft's IKE (Internet Key Exchange) Service Extensions have a double free vulnerability (CVE-2026-33824), meaning memory is freed twice, which can crash the system or allow code execution. This matters because IKE is used to establish encrypted VPN connections, so compromising it could expose remote access and encrypted communications. Defenders apply Microsoft security updates, monitor systems for unexpected crashes, and review VPN connection logs for anomalies.

**CVE-2026-59310** — Broadcom VMware vCenter has a path traversal vulnerability (CVE-2026-59310) that allows attackers to access files they shouldn't be able to reach by exploiting how the software handles file paths. This matters because vCenter manages all virtual machines in a data center, so unauthorized file access could expose sensitive configuration data and credentials for all hosted systems. Defenders patch vCenter immediately, review file access logs, audit who has accessed sensitive configuration files, and scan for evidence of prior exploitation.

**CVE-2026-20349** — Cisco Secure Firewall devices (ASA and FTD models) have a heap inspection vulnerability (CVE-2026-20349) that exposes sensitive memory information used to manage the firewall's operations. This matters because attackers can use this leaked information to craft more effective attacks or bypass the firewall's security controls. Defenders apply Cisco patches immediately, monitor firewall logs for exploitation attempts, and review network traffic for signs of breach.

**CVE-2026-63077** — JetBrains TeamCity (a continuous integration/continuous deployment platform for automating software builds) has a deserialization vulnerability (CVE-2026-63077) that allows attackers to run arbitrary code by crafting malicious input during the data parsing process. This matters because TeamCity controls the automated building and deployment of software, so compromising it could inject malicious code into an organization's products. Defenders patch TeamCity immediately, review build logs and artifacts for tampering, rotate credentials, and audit what code has been deployed recently.

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*