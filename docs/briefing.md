# 🛡️ CyberBrief — Sunday, 26 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE
*The Hacker News* — [read more](https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html)

Attackers linked to the Cl0p ransomware group are exploiting security flaws in PTC Windchill and FlexPLM software (product design tools) that are exposed to the internet without proper access controls. This matters because these tools often contain valuable intellectual property and design files, so breaches can lead to data theft and extortion demands. Defenders typically patch these flaws immediately, restrict internet access to these tools, and monitor for signs of compromise.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 2. OnTrac notifies customers of data breach after network hack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/)

OnTrac delivery company discovered that hackers broke into their corporate network and may have stolen customer personal information like names, addresses, and contact details. This matters because stolen personal data can be used for identity theft, fraud, or sold to other criminals. Defenders respond by notifying affected customers, investigating how the breach happened, improving network security, and monitoring for misuse of the stolen data.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 3. ShinyHunters data leaks fuel $2,000 sextortion email scam
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/shinyhunters-data-leaks-fuel-2-000-sextortion-email-scam/)

Threat actors are sending fake extortion emails to people whose email addresses were leaked in previous data breaches by the ShinyHunters group, falsely claiming to have embarrassing videos and demanding $2,000 in Bitcoin to stay quiet. This matters because these scams can cause panic and financial loss, even though the attackers usually don't have the videos they claim to have. Defenders educate users not to pay ransom demands and help organizations warn exposed individuals.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 4. Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available
*The Hacker News* — [read more](https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html)

Attackers are actively exploiting a critical flaw in Fastjson (a Java library used to read JSON data) that lets them run malicious code without logging in, using the privileges of the Java application itself; no official patch is currently available. This matters because Java applications using vulnerable Fastjson versions can be completely compromised, potentially giving attackers full control of servers and data. Defenders monitor for attacks, apply workarounds if available, isolate affected systems, and wait for official patches.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 5. Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git
*The Hacker News* — [read more](https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html)

A security researcher released working exploit code on July 24 for a GitLab flaw that GitLab had already fixed six weeks earlier; the exploit allows any logged-in user who can upload code to run commands with the privileges of the 'git' system account on older unpatched servers. This matters because older GitLab servers that haven't been updated are now at immediate risk, as attackers can use the published code to gain control. Defenders urgently patch GitLab instances, restrict who can upload code, and monitor for suspicious activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 6. DevMan RaaS Portal Centralizes Payload Builds, Victim Management, and Affiliate Payouts
*The Hacker News* — [read more](https://thehackernews.com/2026/07/devman-raas-portal-centralizes-payload.html)

The DevMan ransomware-as-a-service (RaaS) operation runs a centralized web platform that allows criminal affiliates to build custom malware, track victims, and split ransom payments, making ransomware attacks easier to organize and scale. This matters because RaaS platforms lower the barrier to entry for ransomware attacks, allowing less skilled criminals to launch professional-grade extortion campaigns. Defenders track RaaS infrastructure, share indicators of compromise with other organizations, and help victims recover.

> 📋 **ISO 27001:** A.8.13 Information backup

### 7. CTM360 Research Reveals How Insurance Phishing Has Evolved Into Real-Time Account Hijacking
*The Hacker News* — [read more](https://thehackernews.com/2026/07/ctm360-research-reveals-how-insurance.html)

Insurance phishing attacks have evolved beyond stealing login credentials; attackers now compromise accounts in real-time during the phishing session, immediately transferring money or changing settings before the victim realizes something is wrong. This matters because real-time account hijacking bypasses time-based defenses and makes it much harder for customers to stop fraud. Defenders implement multi-factor authentication (requiring a second verification step), monitor for unusual account activity, and train staff to recognize real-time attack indicators.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.5.17 Authentication information

### 8. Steam forum ClickFix attacks infect gamers with XMRig cryptominers
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/steam-forum-clickfix-attacks-infect-gamers-with-xmrig-cryptominers/)

Attackers are posting fake fix guides on Steam gaming forums that appear to solve game or computer problems but actually install XMRig (a cryptomining tool) that secretly uses victims' computer processing power to generate cryptocurrency for criminals. This matters because infected computers slow down, waste electricity, and degrade hardware while enriching the attackers. Defenders scan for cryptominer infections, block known malicious domains, educate users to download fixes only from official sources, and remove malware.

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-63030** | WordPress Core Interpretation Conflict Vulnerability | – | 98% | ⚠️ YES (KEV) |
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 90% | ⚠️ YES (KEV) |
| **CVE-2026-15409** | SonicWall SMA1000 Appliances Server-Side Request Forgery Vulnerability | – | 78% | ⚠️ YES (KEV) |
| **CVE-2026-60137** | WordPress Core SQL Injection Vulnerability | – | 78% | ⚠️ YES (KEV) |
| **CVE-2026-15410** | SonicWall SMA1000 Appliances Code Injection Vulnerability | – | 76% | ⚠️ YES (KEV) |

**CVE-2026-63030** — A vulnerability in WordPress core software allows attackers to exploit how the system interprets certain inputs, potentially leading to unauthorized actions or data exposure on websites using affected versions. This matters because WordPress powers millions of websites, so a core vulnerability puts many sites at risk simultaneously. Defenders apply WordPress security updates immediately, use security plugins to monitor for exploitation attempts, and follow principle of least privilege (limit what plugins and users can do).

**CVE-2026-39808** — Fortinet FortiSandbox (a security tool that analyzes suspicious files) contains a flaw that allows attackers to inject operating system commands, potentially giving them control over the security appliance itself. This matters because FortiSandbox sits in a trusted position within the network, so compromising it can allow attackers to bypass other security defenses. Defenders patch FortiSandbox immediately, restrict access to its management interface, and monitor for suspicious commands.

**CVE-2026-15409** — SonicWall SMA1000 appliances (remote access devices) have a server-side request forgery vulnerability that tricks the device into making unauthorized internal network requests on behalf of attackers, potentially exposing internal systems. This matters because these appliances control who can access the corporate network, so compromising them can give attackers internal network access. Defenders patch immediately, restrict which sites the appliance can contact, monitor traffic for unusual patterns, and segment internal networks.

**CVE-2026-60137** — A flaw in WordPress core software allows attackers to inject malicious SQL database commands through certain inputs, potentially exposing or modifying website data. This matters because WordPress databases often contain customer information, posts, and configuration details that attackers can steal or corrupt. Defenders update WordPress immediately, use security plugins to detect SQL injection attempts, validate all user inputs, and back up databases regularly.

**CVE-2026-15410** — SonicWall SMA1000 appliances contain a code injection vulnerability that allows attackers to inject and execute malicious code on the device, potentially giving full control to an attacker. This matters because these devices control network access, so complete compromise allows attackers to monitor traffic, steal data, or create backdoors into the internal network. Defenders patch urgently, restrict administrative access, monitor for suspicious activity, and segment networks to limit impact.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*