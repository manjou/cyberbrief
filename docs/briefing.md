# 🛡️ CyberBrief — Sunday, 26 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE
*The Hacker News* — [read more](https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html)

Cl0p ransomware attackers are exploiting security flaws in PTC Windchill and FlexPLM software (tools used for product design and manufacturing) that are exposed to the internet without proper access controls. This matters because these systems often contain valuable intellectual property and design data, making them attractive targets for extortion attacks. Defenders typically patch these applications immediately, restrict internet access to these tools, and monitor for suspicious login attempts or data transfers.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 2. OnTrac notifies customers of data breach after network hack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/)

Hackers broke into OnTrac's internal corporate network and may have stolen customer personal information like names, addresses, and contact details. This is serious because customers' data is now at risk of being sold or misused, and OnTrac faces legal and financial consequences. Defenders respond by securing the network, investigating what data was accessed, notifying affected customers, and implementing stronger access controls and monitoring.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 3. ShinyHunters data leaks fuel $2,000 sextortion email scam
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/shinyhunters-data-leaks-fuel-2-000-sextortion-email-scam/)

Threat actors are taking email addresses from previous data breaches leaked by ShinyHunters and sending fake sextortion emails (threatening to release embarrassing photos unless money is paid). This works because victims see their own real email address and may panic into paying. Defenders educate users that these are scams, filter suspicious emails, and track where breached data is being bought and sold.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 4. Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available
*The Hacker News* — [read more](https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html)

Attackers are actively exploiting a critical flaw in Fastjson (a tool that reads JSON data in Java applications) that allows them to run malicious code without logging in, and no official fix is available yet. This is dangerous because any organization using vulnerable versions is exposed until the vendor releases a patch. Defenders typically isolate affected systems, block suspicious requests, and monitor vendor announcements for fixes or workarounds.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 5. Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git
*The Hacker News* — [read more](https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html)

A security researcher publicly released working attack code for a GitLab flaw six weeks after GitLab released a patch, making it easier for attackers to exploit systems that haven't updated. This is critical because any employee with access to push code changes can now run commands on unpatched servers. Defenders prioritize applying the June 10 patch immediately and monitor for suspicious code pushes or command execution.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 6. DevMan RaaS Portal Centralizes Payload Builds, Victim Management, and Affiliate Payouts
*The Hacker News* — [read more](https://thehackernews.com/2026/07/devman-raas-portal-centralizes-payload.html)

DevMan ransomware operators are running a formal business platform (ransomware-as-a-service, or RaaS) that lets attackers build malware, track victims, and split profits with affiliates, operating like a legitimate software company. This matters because it lowers the technical bar for launching ransomware attacks and shows how organized these criminal enterprises have become. Defenders work with law enforcement, disrupt these platforms when possible, and monitor for DevMan infrastructure and tactics.

> 📋 **ISO 27001:** A.8.13 Information backup

### 7. CTM360 Research Reveals How Insurance Phishing Has Evolved Into Real-Time Account Hijacking
*The Hacker News* — [read more](https://thehackernews.com/2026/07/ctm360-research-reveals-how-insurance.html)

Insurance company phishing attacks have evolved from simple credential theft to real-time account hijacking, where attackers log in immediately while the victim is still on the attacker's fake login page and take over accounts within seconds. This is harder to stop because victims cannot recover compromised accounts after the attacker has already changed passwords and settings. Defenders deploy multi-factor authentication (requiring a second form of verification), real-time login alerts, and educate users to verify URLs before entering credentials.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.5.17 Authentication information

### 8. Steam forum ClickFix attacks infect gamers with XMRig cryptominers
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/steam-forum-clickfix-attacks-infect-gamers-with-xmrig-cryptominers/)

Fake "fix" posts on Steam forums are tricking gamers into downloading files that secretly install XMRig (malware that mines cryptocurrency using the victim's computer without their knowledge). This matters because it wastes computing resources, damages hardware, and generates profit for criminals. Defenders scan downloads for malware signatures, warn users about suspicious posts, disable malicious accounts, and monitor for signs of cryptominers running on systems.

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-63030** | WordPress Core Interpretation Conflict Vulnerability | – | 98% | ⚠️ YES (KEV) |
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 90% | ⚠️ YES (KEV) |
| **CVE-2026-15409** | SonicWall SMA1000 Appliances Server-Side Request Forgery Vulnerability | – | 78% | ⚠️ YES (KEV) |
| **CVE-2026-60137** | WordPress Core SQL Injection Vulnerability | – | 78% | ⚠️ YES (KEV) |
| **CVE-2026-15410** | SonicWall SMA1000 Appliances Code Injection Vulnerability | – | 76% | ⚠️ YES (KEV) |

**CVE-2026-63030** — This vulnerability allows attackers to bypass security checks in WordPress core by exploiting how the software interprets certain code requests differently than expected. Defenders should apply the available patch, monitor for exploitation attempts, and validate all user input going into WordPress.

**CVE-2026-39808** — This flaw in Fortinet FortiSandbox (a security analysis tool) allows attackers to run arbitrary system commands by sending specially crafted requests, potentially giving them full control of the security system itself. Defenders should immediately patch FortiSandbox appliances and restrict network access to these tools since they should not be exposed to untrusted networks.

**CVE-2026-15409** — This vulnerability in SonicWall SMA1000 appliances (remote access security devices) allows attackers to make the appliance fetch files or resources from internal systems that should be protected. Defenders should apply patches, restrict what servers the appliance can communicate with, and monitor for unusual outbound requests.

**CVE-2026-60137** — This SQL injection flaw in WordPress core allows attackers to manipulate database queries by inserting malicious code, potentially exposing or modifying sensitive data stored in the database. Defenders must apply the patch, use database firewalls to block suspicious queries, and audit databases for signs of unauthorized access or changes.

**CVE-2026-15410** — This vulnerability in SonicWall SMA1000 appliances allows attackers to inject and execute malicious code on the appliance itself, potentially compromising the entire remote access system. Defenders should prioritize patching these devices, restrict administrative access, and monitor appliance logs for suspicious activity.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*