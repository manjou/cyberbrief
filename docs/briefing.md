# 🛡️ CyberBrief — Net+ — Wednesday, 09 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days** — Microsoft released patches for 974 security vulnerabilities in a single month, which is a record number, and two of these flaws were already being actively used by attackers before the patches came out. [read more](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html)
- **Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell** — Adobe released an emergency patch for a critical flaw in its e-commerce software (Adobe Commerce and Magento) that attackers were already exploiting to install persistent malware (a backdoor written in the Rust programming language) and web-based shells that give ongoing access. [read more](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html)
- **September 2026 Microsoft Patch Tuesday, (Tue, Sep 8th)** — Microsoft released patches for 973 vulnerabilities in September 2026, which broke the previous record and included 113 critical-severity flaws, with two already being exploited by attackers and none disclosed publicly beforehand. [read more](https://isc.sans.edu/diary/rss/33320)
- **Google warns of new Chrome zero-day bug exploited in attacks** — Google released security updates fixing 230 vulnerabilities in Chrome, including a seventh zero-day flaw that was actively being exploited in attacks during 2026. [read more](https://www.bleepingcomputer.com/news/security/google-patches-seventh-chrome-zero-day-exploited-in-attacks-this-year/)
- **Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox** — Google patched a medium-severity bug in Chrome's V8 JavaScript engine that allowed attackers to execute code inside the browser sandbox (a protected memory area that should limit damage even if code runs). [read more](https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html)
- **Adobe Patches Over 170 Vulnerabilities, Including Commerce Zero-Day** — Adobe released patches for over 170 vulnerabilities, with a particularly critical one (CVE-2026-75650) in Adobe Commerce that allows unauthenticated attackers (those without login credentials) to run arbitrary code on affected systems. [read more](https://www.securityweek.com/adobe-patches-over-170-vulnerabilities-including-commerce-zero-day/)
- **N-able N-central Pre-Auth RCE Flaw Exploited in the Wild** — CISA (a U.S. [read more](https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html)
- **The EU CRA's Real Question: What Shipped, and When Did You Know?** — The European Union's new Cyber Resilience Act requires software vendors to report actively exploited security flaws to authorities within as little as 24 hours starting September 11, 2026, and vendors must accurately document what software versions shipped and when vulnerabilities were discovered. [read more](https://www.bleepingcomputer.com/news/security/the-eu-cras-real-question-what-shipped-and-when-did-you-know/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2021-23758 (– CVSS, 84% EPSS)

## 🔥 Top stories

### 1. Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days
*The Hacker News* — [read more](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html)

Microsoft released patches for 974 security vulnerabilities in a single month, which is a record number, and two of these flaws were already being actively used by attackers before the patches came out. This matters because it shows the scale of security problems that exist in widely-used software and highlights that attackers sometimes move faster than defenders. Defenders respond by prioritizing which patches to install first (usually the exploited ones), testing them in lab environments before deploying company-wide, and communicating urgently with all system administrators to apply updates quickly.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell
*The Hacker News* — [read more](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html)

Adobe released an emergency patch for a critical flaw in its e-commerce software (Adobe Commerce and Magento) that attackers were already exploiting to install persistent malware (a backdoor written in the Rust programming language) and web-based shells that give ongoing access. This matters because e-commerce platforms handle customer data and payment information, so a compromised platform can lead to data theft and financial fraud at scale. Defenders immediately prioritize this patch, scan their systems for signs of previous exploitation, reset credentials for affected accounts, and may temporarily take systems offline if they cannot patch quickly enough.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 3. September 2026 Microsoft Patch Tuesday, (Tue, Sep 8th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33320)

Microsoft released patches for 973 vulnerabilities in September 2026, which broke the previous record and included 113 critical-severity flaws, with two already being exploited by attackers and none disclosed publicly beforehand. This matters because a large number of patches means widespread risk across organizations using Microsoft products, and the fact that attacks started before public disclosure means some organizations were already compromised. Defenders treat this as a high-urgency situation, coordinate with other teams to test and deploy patches as fast as possible while monitoring networks for signs of active exploitation.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

### 4. Google warns of new Chrome zero-day bug exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/google-patches-seventh-chrome-zero-day-exploited-in-attacks-this-year/)

Google released security updates fixing 230 vulnerabilities in Chrome, including a seventh zero-day flaw that was actively being exploited in attacks during 2026. This matters because Chrome is used by billions of people and zero-days (flaws unknown to vendors before attackers find them) are particularly dangerous because there is no advance warning. Defenders push Chrome updates to users urgently through automatic update mechanisms, monitor for signs of compromise, and in some cases may restrict Chrome on sensitive systems until patches are confirmed working.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox
*The Hacker News* — [read more](https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html)

Google patched a medium-severity bug in Chrome's V8 JavaScript engine that allowed attackers to execute code inside the browser sandbox (a protected memory area that should limit damage even if code runs). This matters because even though the sandbox exists to contain attacks, a flaw that breaks out of it could give attackers full access to the computer. Defenders treat this as urgent because the bypass makes the browser's main security boundary less effective, and they prioritize updating all Chrome installations immediately.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Adobe Patches Over 170 Vulnerabilities, Including Commerce Zero-Day
*SecurityWeek* — [read more](https://www.securityweek.com/adobe-patches-over-170-vulnerabilities-including-commerce-zero-day/)

Adobe released patches for over 170 vulnerabilities, with a particularly critical one (CVE-2026-75650) in Adobe Commerce that allows unauthenticated attackers (those without login credentials) to run arbitrary code on affected systems. This matters because anyone on the internet can exploit it without needing to be a customer or employee, making it an immediate widespread risk for any organization using this software. Defenders apply this patch as an emergency, check their systems for evidence of past exploitation, and may isolate affected servers from the internet until patched.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. N-able N-central Pre-Auth RCE Flaw Exploited in the Wild
*The Hacker News* — [read more](https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html)

CISA (a U.S. government cybersecurity agency) officially added a critical flaw in N-able N-central remote management software to its list of known exploited vulnerabilities and required all federal agencies to patch by September 11, 2026. This matters because N-central is used to manage IT infrastructure across many organizations, so a flaw here gives attackers potential access to hundreds of networks at once, and the government mandate signals this is a severe threat. Defenders immediately test and deploy patches, prioritize this above routine updates, and may require vendors to prove they have patched as a contract requirement.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. The EU CRA's Real Question: What Shipped, and When Did You Know?
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/the-eu-cras-real-question-what-shipped-and-when-did-you-know/)

The European Union's new Cyber Resilience Act requires software vendors to report actively exploited security flaws to authorities within as little as 24 hours starting September 11, 2026, and vendors must accurately document what software versions shipped and when vulnerabilities were discovered. This matters because it creates legal accountability for vendors and pushes the responsibility to respond faster, while also meaning organizations need better records of their software supply chain. Defenders must work with vendors to understand patch timelines, maintain accurate inventories of what software they run and when, and establish processes to respond within regulatory deadlines.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2021-23758** | Ajax.NET Professional Deserialization of Untrusted Data Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2019-1068** | Microsoft SQL Server Remote Code Execution Vulnerability | – | 53% | ⚠️ YES (KEV) |
| **CVE-2026-75650** | Adobe Commerce and Magento Improper Neutralization of Special Elements Used in a Template Engine Vulnerability | 10.0 | 1% | ⚠️ YES (KEV) |
| **CVE-2023-49105** | ownCloud Improper Authentication Vulnerability | – | 43% | ⚠️ YES (KEV) |
| **CVE-2026-83549** | SonicWall SMA1000 Appliances OS Command Injection Vulnerability | – | 2% | ⚠️ YES (KEV) |

**CVE-2021-23758** — CVE-2021-23758 is a flaw in Ajax.NET Professional where the software improperly handles untrusted data that gets converted from serialized format (a way of storing complex data), allowing attackers to inject malicious code. This matters because deserialization flaws are a common way attackers execute code, and if an application trusts data it receives from untrusted sources, attackers can exploit that trust. Defenders apply patches for affected versions, avoid passing untrusted data to deserialization functions, and validate all input before processing.

**CVE-2019-1068** — CVE-2019-1068 is a remote code execution vulnerability in Microsoft SQL Server that allows attackers to run arbitrary commands on the database server. This matters because SQL databases often store an organization's most sensitive data, and remote code execution means attackers can access, steal, or destroy that data without needing physical access. Defenders apply patches immediately, restrict network access to SQL servers using firewalls, use strong authentication, and monitor for suspicious activity.

**CVE-2026-75650** — CVE-2026-75650 is a flaw in Adobe Commerce where user input is not properly filtered before being used in template processing (code that generates dynamic web pages), allowing attackers to inject arbitrary code that runs with the same permissions as the current user. This matters because attackers can steal session data, modify content, access databases, or pivot to other systems. Defenders apply patches urgently, scan for signs of exploitation in logs, restrict user permissions, and implement web application firewalls to block malicious input.

**CVE-2023-49105** — CVE-2023-49105 is a flaw in ownCloud (an open-source file storage system) where the authentication system is not working correctly, potentially allowing attackers to bypass login requirements. This matters because it could allow unauthorized access to stored files and data without valid credentials. Defenders apply patches, reset all passwords, review access logs for suspicious logins, and if the patch is not yet available, may restrict access or take the service offline temporarily.

**CVE-2026-83549** — CVE-2026-83549 is a command injection vulnerability in SonicWall SMA1000 appliances (remote access devices) that allows attackers to run operating system commands directly on the device. This matters because these appliances are often the entry point to corporate networks, so compromising one gives attackers a foothold inside the network perimeter. Defenders apply patches immediately, change default credentials, restrict administrative access, monitor appliance logs for suspicious commands, and may temporarily use alternative access methods until patched.

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*