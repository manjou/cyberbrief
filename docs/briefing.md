# 🛡️ CyberBrief — GRC — Friday, 14 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🔥 Top stories

### 1. Trezor discloses data breach affecting nearly 14,000 customers
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/trezor-discloses-data-breach-affecting-nearly-14-000-customers/)

Trezor, a company that makes hardware wallets (specialized devices for storing cryptocurrency), had customer information exposed when one of its third-party vendors (ShipMonk, who handles shipping) was compromised. This matters because attackers now have personal details about people who own cryptocurrency, making them targets for fraud and theft. Defenders typically segment networks so that third-party vendors have limited access, require vendors to maintain strong security, and monitor for breaches affecting their supply chain.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 2. Microsoft patches LegacyHive Windows zero-day vulnerability
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-legacyhive-windows-zero-day-vulnerability/)

Microsoft released security patches for a Windows vulnerability called LegacyHive that was publicly disclosed without advance warning (a 'zero-day'), meaning attackers could immediately start using it before patches were available. This matters because Windows runs on most enterprise computers, so a critical flaw could affect thousands of organizations simultaneously. Defenders respond by applying patches as soon as possible, blocking suspicious activity patterns that exploit this flaw, and increasing monitoring during the critical period after disclosure.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Critical VMware vCenter RCE flaw exploited for reverse SSH access
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/)

A serious flaw in VMware vCenter (software that manages virtual machines in data centers) is being actively exploited by attackers to install a backdoor (reverse SSH tool) that gives them persistent remote access. This matters because vCenter is a high-value target controlling an organization's entire virtualized infrastructure, so compromise could expose everything. Defenders immediately patch vCenter systems, hunt for signs of the SSH tool already installed, and monitor vCenter access logs for suspicious activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. Apple sends new ‘Threat Notification’ alerts over mercenary spyware attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/apple/apple-sends-new-threat-notification-alerts-over-mercenary-spyware-attacks/)

Apple is sending direct warnings to iPhone users who appear to be targeted by mercenary spyware (commercial hacking tools sold to governments and wealthy entities), alerting them that their devices may be under attack. This matters because these are highly sophisticated threats that typical security software may not catch, and being targeted suggests you or your organization is of particular interest to powerful actors. Defenders recommend taking the warning seriously, isolating the device, changing passwords from a clean device, and contacting security professionals if the device is used for work.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Attackers Exploit SharePoint Authentication Bypass After Public PoC Release
*The Hacker News* — [read more](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)

Attackers have started actively exploiting CVE-2026-55040, a critical SharePoint flaw (score 9.1 out of 10 severity) involving weak authentication, shortly after someone publicly released proof-of-concept code showing how it works. This matters because SharePoint stores sensitive files for many organizations, and weak authentication means attackers can bypass login controls and access data without valid credentials. Defenders immediately patch SharePoint, review access logs for unauthorized logins, disable the affected feature if patches aren't available yet, and implement additional authentication requirements like multi-factor authentication.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 6. Hackers exploit critical Adobe Commerce flaw to hijack customer accounts
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-adobe-commerce-flaw-to-hijack-customer-accounts/)

Attackers are exploiting CVE-2026-71362 in Adobe Commerce and Magento (e-commerce platforms that run online stores) to take control of customer accounts, potentially stealing payment information or personal data. This matters because these platforms process customer orders and payments, so compromise puts both the store's customers and business at risk. Defenders patch immediately, scan transaction logs for suspicious account takeovers, reset customer passwords if the flaw allowed password changes, and monitor for unauthorized purchases.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Akira hackers disable EDR with Safe Mode, steal data but fail to encrypt
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/)

An Akira ransomware group disabled endpoint detection and response (EDR) security software—which watches for malicious behavior on computers—by restarting the infected system into Safe Mode, a Windows diagnostic mode where EDR doesn't load. This matters because it shows attackers can work around modern security tools using legitimate Windows features, leaving the system vulnerable while they steal data. Defenders should prevent Safe Mode restarts via group policy, monitor unusual restart patterns, ensure EDR can't be easily disabled, and maintain offline backups to recover from ransomware.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.24 Incident management planning

### 8. Adobe Commerce Bug Targeted Immediately After Disclosure
*SecurityWeek* — [read more](https://www.securityweek.com/adobe-commerce-bug-targeted-immediately-after-disclosure/)

The first real attacks exploiting CVE-2026-71362 in Adobe Commerce were detected very quickly after Adobe published patches, suggesting attackers were prepared with exploit code and immediately began targeting unpatched systems. This matters because it demonstrates the short window organizations have to apply patches before exploitation becomes widespread—sometimes measured in hours. Defenders prioritize patching critical vulnerabilities within 24-48 hours, monitor for exploitation attempts during the window before patches are deployed, and assume breach for systems that remain unpatched.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-8037** | Progress LoadMaster Command Injection Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-34486** | Apache Tomcat Missing Encryption of Sensitive Data Vulnerability | – | 83% | ⚠️ YES (KEV) |
| **CVE-2026-9198** | IBM Langflow Code Injection Vulnerability | – | 17% | ⚠️ YES (KEV) |
| **CVE-2026-63077** | JetBrains TeamCity Deserialization of Untrusted Data Vulnerability | – | 11% | ⚠️ YES (KEV) |
| **CVE-2026-72898** | Metabase SQL Injection Vulnerability | – | 10% | ⚠️ YES (KEV) |

**CVE-2026-8037** — CVE-2026-8037 is a command injection vulnerability in Progress LoadMaster (a load-balancing appliance that routes network traffic), allowing attackers to execute arbitrary system commands on the device. This matters because load balancers sit between users and critical servers, giving attackers a central point to compromise or redirect traffic. Defenders patch LoadMaster immediately, restrict management access to trusted networks only, monitor for suspicious commands in logs, and segment load balancers from sensitive backend systems.

**CVE-2026-34486** — CVE-2026-34486 is a flaw in Apache Tomcat (a web server used to run Java applications) where sensitive data is transmitted or stored without encryption, potentially exposing passwords, API keys, or personal information. This matters because unencrypted sensitive data can be read by attackers who intercept network traffic or access storage. Defenders enable encryption for all data in transit (TLS/SSL) and at rest, audit configurations to ensure encryption is active, and scan for unencrypted credentials in logs or storage.

**CVE-2026-9198** — CVE-2026-9198 is a code injection flaw in IBM Langflow (a tool for building AI workflows), allowing attackers to inject and execute malicious code within the application. This matters because code injection gives attackers complete control over the compromised application and potentially the systems it connects to, including databases and APIs. Defenders patch Langflow immediately, review code and workflow definitions for suspicious injected content, restrict Langflow's access to only necessary databases and systems, and monitor execution logs for unexpected commands.

**CVE-2026-63077** — CVE-2026-63077 is a deserialization vulnerability in JetBrains TeamCity (a continuous integration server used in software development), where untrusted data is converted back into executable code, allowing remote code execution. This matters because TeamCity has access to source code repositories, build systems, and deployment tools, so compromise can inject malicious code into software before it reaches customers. Defenders patch TeamCity urgently, review build logs and deployed artifacts for suspicious changes, restrict TeamCity's network access, and monitor for lateral movement to code repositories.

**CVE-2026-72898** — CVE-2026-72898 is a SQL injection vulnerability in Metabase (a business intelligence and dashboarding tool), allowing attackers to inject malicious SQL commands that can read, modify, or delete database data. This matters because Metabase typically connects to core business databases containing customer, financial, and operational data. Defenders patch immediately, review database access logs for unusual queries, restrict Metabase's database permissions to minimum necessary levels, and audit saved queries and dashboards for injected SQL code.

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