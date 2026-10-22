# 🛡️ CyberBrief — SOC — Thursday, 22 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Widespread PHP Flaw May Cause Many Site Outages Today** — A flaw in PHP (the software that powers about 70% of websites) lets attackers take complete control of affected servers, which is why you're seeing lots of 404 errors as sites go down or get shut down preemptively. [read more](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/)
- **PHP ships emergency patches for critical PHP2Shell flaws** — PHP released emergency security patches for two critical vulnerabilities (PHP2Shell) that allow remote code execution (RCE, meaning running unauthorized commands on a server) without needing login credentials. [read more](https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/)
- **China-Linked Hackers Use ARTEX AI Agents in ConnectWise Supply Chain Attack** — A Chinese state-backed hacking group compromised ConnectWise Cloud Backup software in the supply chain (meaning the attacker broke into the vendor's systems, not individual customers' networks) and used an AI-based penetration testing tool called ARTEX to move through victim networks. [read more](https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html)
- **PHP Issues Emergency Patches for Two Critical PHP2Shell RCE Flaws as Exploit Attempts Emerge** — PHP released emergency security updates fixing two critical remote code execution flaws that let attackers run commands on web servers without any account access—the fixes are available in specific patched versions (8.5.12, 8.4.27, 8.3.36, and 8.2.35). [read more](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html)
- **CISA: SafePay ransomware hit over 600 critical infrastructure orgs** — The SafePay ransomware gang has attacked and successfully encrypted data on over 600 critical infrastructure organizations (power plants, hospitals, utilities, etc.) since 2024, according to CISA (a U.S. [read more](https://www.bleepingcomputer.com/news/security/cisa-and-fbi-safepay-ransomware-has-hit-over-600-critical-infrastructure-organizations/)
- **Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases** — GitLab released a patch for a flaw (rated 10.0, the highest severity) that lets unauthenticated attackers run code on self-managed GitLab servers, and the flaw exists in every version released since 2014—even organizations that patched 9 days earlier are still vulnerable. [read more](https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html)
- **Authorities disrupt nearly 11,000 cybercrime networks in Africa** — Law enforcement agencies worldwide arrested over 1,400 cybercriminals and shut down nearly 11,000 criminal networks in Operation Serengeti III, targeting business email compromise scams, ransomware gangs, and online fraud. [read more](https://www.bleepingcomputer.com/news/security/authorities-disrupt-nearly-11-000-cybercrime-networks-in-africa/)
- **LiteLLM Suspects GitHub Token Leak in AI Gateway Logs Behind Malicious Package Release** — Attackers compromised LiteLLM's code release system and pushed a malicious version of their Python software package that included a credential stealer and backdoor; the compromise suggests attackers leaked stolen GitHub tokens (security credentials) from system logs to gain access. [read more](https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2015-5477 (– CVSS, 99% EPSS)

## 🔥 Top stories

### 1. Widespread PHP Flaw May Cause Many Site Outages Today
*Krebs on Security* — [read more](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/)

A flaw in PHP (the software that powers about 70% of websites) lets attackers take complete control of affected servers, which is why you're seeing lots of 404 errors as sites go down or get shut down preemptively. This matters because it's widespread—affecting millions of websites—and attackers already have working attack code. Defenders need to update PHP immediately to patched versions and monitor their systems for signs of compromise.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.6 Capacity management

### 2. PHP ships emergency patches for critical PHP2Shell flaws
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/)

PHP released emergency security patches for two critical vulnerabilities (PHP2Shell) that allow remote code execution (RCE, meaning running unauthorized commands on a server) without needing login credentials. This matters because the flaws are in the core language itself, affecting a huge portion of the internet, and updates are emergency-only because exploits are actively being used. Defenders must apply patches to all affected PHP versions as their highest priority.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 3. China-Linked Hackers Use ARTEX AI Agents in ConnectWise Supply Chain Attack
*The Hacker News* — [read more](https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html)

A Chinese state-backed hacking group compromised ConnectWise Cloud Backup software in the supply chain (meaning the attacker broke into the vendor's systems, not individual customers' networks) and used an AI-based penetration testing tool called ARTEX to move through victim networks. This matters because supply chain attacks affect thousands of organizations at once, and the use of AI tools shows sophisticated attacker capabilities. Defenders need to patch ConnectWise immediately, hunt for unauthorized access in their systems, and monitor for the specific tools this group is known to use.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 4. PHP Issues Emergency Patches for Two Critical PHP2Shell RCE Flaws as Exploit Attempts Emerge
*The Hacker News* — [read more](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html)

PHP released emergency security updates fixing two critical remote code execution flaws that let attackers run commands on web servers without any account access—the fixes are available in specific patched versions (8.5.12, 8.4.27, 8.3.36, and 8.2.35). This matters because it's a core language vulnerability affecting millions of sites, and partial patches don't help. Defenders must update to the full patched versions and verify the update actually took effect.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 5. CISA: SafePay ransomware hit over 600 critical infrastructure orgs
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-and-fbi-safepay-ransomware-has-hit-over-600-critical-infrastructure-organizations/)

The SafePay ransomware gang has attacked and successfully encrypted data on over 600 critical infrastructure organizations (power plants, hospitals, utilities, etc.) since 2024, according to CISA (a U.S. government cybersecurity agency). This matters because critical infrastructure attacks can endanger public safety and national security, and 600 breaches means this group is highly active and successful. Defenders in critical infrastructure must assume they're a target, enforce strong backup strategies, and implement detection tools specifically tuned for ransomware.

> 📋 **ISO 27001:** A.8.13 Information backup

### 6. Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases
*The Hacker News* — [read more](https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html)

GitLab released a patch for a flaw (rated 10.0, the highest severity) that lets unauthenticated attackers run code on self-managed GitLab servers, and the flaw exists in every version released since 2014—even organizations that patched 9 days earlier are still vulnerable. This matters because GitLab is used by many organizations to store and manage code, so a breach can compromise source code and secrets, and the wide affected range means almost all GitLab users need to patch immediately. Defenders must apply the October 21 patch regardless of previous patch dates and scan server logs for suspicious activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Authorities disrupt nearly 11,000 cybercrime networks in Africa
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/authorities-disrupt-nearly-11-000-cybercrime-networks-in-africa/)

Law enforcement agencies worldwide arrested over 1,400 cybercriminals and shut down nearly 11,000 criminal networks in Operation Serengeti III, targeting business email compromise scams, ransomware gangs, and online fraud. This matters because it shows that coordinated law enforcement action can disrupt criminal operations at scale. Defenders should use this window to strengthen defenses against these attack types, knowing that some of the criminals behind recent attacks are now arrested or displaced.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 8. LiteLLM Suspects GitHub Token Leak in AI Gateway Logs Behind Malicious Package Release
*The Hacker News* — [read more](https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html)

Attackers compromised LiteLLM's code release system and pushed a malicious version of their Python software package that included a credential stealer and backdoor; the compromise suggests attackers leaked stolen GitHub tokens (security credentials) from system logs to gain access. This matters because Python packages are widely downloaded and trusted, so a compromised package can infect thousands of developer machines and systems, and it shows that logging systems can leak secrets if not properly protected. Defenders need to audit their Python package versions, rotate any GitHub credentials, and implement secret detection in logs.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.19 Supplier relationships

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2015-5477** |  ISC BIND Data Processing Errors Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2015-3306** | ProFTPD Improper Access Control Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2016-3081** | Apache Struts Command Injection Vulnerability | – | 96% | ⚠️ YES (KEV) |
| **CVE-2026-104935** | Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | – | 26% | ⚠️ YES (KEV) |
| **CVE-2021-3199** | ONLYOFFICE Docs Server Path Traversal Vulnerability | – | 20% | ⚠️ YES (KEV) |

**CVE-2015-5477** — CVE-2015-5477 is a vulnerability in ISC BIND (the software that translates domain names to IP addresses) where improper data processing allows attackers to cause problems with DNS services. This matters because DNS is foundational to the internet, so disruptions affect all web services. Defenders should ensure BIND is patched and monitor for unusual DNS query patterns.

**CVE-2015-3306** — CVE-2015-3306 is an access control flaw in ProFTPD (file transfer software) that lets users access files they shouldn't have permission to reach. This matters because file servers often hold sensitive company data. Defenders need to update ProFTPD and audit who has accessed which files.

**CVE-2016-3081** — CVE-2016-3081 is a command injection flaw in Apache Struts (web development framework) where attackers can run arbitrary commands by exploiting how the framework processes user input. This matters because Struts powers many business web applications, so compromise could affect entire organizations. Defenders must patch Struts and review web application logs for suspicious commands.

**CVE-2026-104935** — CVE-2026-104935 is an authentication bypass flaw in Ivanti Connect Secure (remote access software) where attackers can trick the system into granting access by spoofing identity, allowing them to bypass login. This matters because remote access software is a primary target—a breach means attackers can enter corporate networks without credentials. Defenders need to patch immediately and add additional authentication checks (like requiring a second factor).

**CVE-2021-3199** — CVE-2021-3199 is a path traversal flaw in ONLYOFFICE Docs Server where attackers can access files outside the intended directory by manipulating file paths (like using "../" to go up folders), potentially reading sensitive documents. This matters because document servers hold confidential company files. Defenders must patch ONLYOFFICE and audit logs for attempted path traversal attacks.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

<sub>Sources unavailable this run: NVD: TimeoutError</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*