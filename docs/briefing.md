# 🛡️ CyberBrief — Net+ — Wednesday, 04 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🔥 Top stories

### 1. CISA flags WordPress RCE flaw as actively exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-flags-wordpress-rce-flaw-as-actively-exploited-in-attacks/)

The US Cybersecurity and Infrastructure Security Agency (CISA) warned federal agencies that attackers have started exploiting a recently patched high-severity WordPress vulnerability in the wild.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Google Warns LLMjacking Attacks Are Costing Some Enterprises Up to $1 Million in Cloud Charges
*The Hacker News* — [read more](https://thehackernews.com/2026/11/google-warns-llmjacking-attacks-are.html)

Google on Monday warned that threat actors are hijacking enterprise access to Large Language Models (LLMs) to fraudulently leverage expensive computing resources and AI services. The tactic is called LLMjacking, a form of resource hijacking adapted for the LLM era, where an attacker obtains an API key through phishing, source code leaks, misconfigured environments, or exposed client-side code

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.8.8 Management of technical vulnerabilities

### 3. Attackers Exploit Critical Siemens IoT2050 Flaw to Plant Remote Command Backdoors
*The Hacker News* — [read more](https://thehackernews.com/2026/11/attackers-exploit-critical-siemens.html)

A maximum-severity security flaw impacting Siemens SIMATIC IoT2050 Advanced devices has come under active exploitation, VulnCheck has revealed. The vulnerability, tracked as CVE-2026-58115 (CVSS score: 10.0), is a case of missing authentication for a critical function that could be exploited by an unauthenticated remote attacker to run arbitrary code. "SIMATIC IoT2050 Advanced devices running

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 4. Synology NAS Devices Targeted in Ransomware Attacks Exploiting Patched DSM Flaw
*The Hacker News* — [read more](https://thehackernews.com/2026/11/synology-nas-devices-targeted-in.html)

Synology is urging customers to update the DiskStation Manager (DSM) software powering its Network Attached Storage (NAS) devices following ransomware attacks. The Taiwanese vendor said it observed threat actors exploiting a vulnerability patched in December 2024 to target devices running outdated versions of DSM. "These attacks aim to encrypt data and extort ransom," it said in a statement

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 5. Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction
*The Hacker News* — [read more](https://thehackernews.com/2026/11/google-patches-critical-android-flaw.html)

A critical Android flaw could allow an attacker to run code on a phone without any user action remotely, Google said in its November security bulletin. The flaw, CVE-2026-58868, affects Android 14 through 17. Phones get the fix with security patch level 2026-11-01 or later, which phone makers and carriers send on their own schedules. As of November 4, Google's bulletin did not report

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Critical Rails Flaw Lets Attackers Write Server Files via Crafted ImageMagick Uploads
*The Hacker News* — [read more](https://thehackernews.com/2026/11/critical-rails-flaw-lets-attackers.html)

A critical flaw in Ruby on Rails could allow an unauthenticated attacker to write arbitrary files on an app's server by uploading a crafted file if the app processes uploads using ImageMagick. The Rails project disclosed the flaw in an advisory and fixed it in versions 8.1.4.1 and 8.0.5.2. The flaw is in Active Storage, the part of Rails that handles file uploads. Some apps store

### 7. China-Aligned Hackers Hijack Sogou Input Method DNS Requests to Deploy DarkVigil Backdoor
*The Hacker News* — [read more](https://thehackernews.com/2026/11/china-aligned-hackers-hijack-sogou.html)

A China-aligned threat actor known as SlippyNunchucks has been attributed to a Domain Name System (DNS) hijacking operation abusing insecure HTTP communications in Windows versions of Sogou Input Method as part of a surveillance campaign designed to deploy an implant called DarkVigil (aka FDMTP). The campaign, observed starting July 1, 2026, is assessed to have targeted organizations and

> 📋 **ISO 27001:** A.8.7 Protection against malware

### 8. WorkOS says attacker used ARTEX AI to breach internal sales app
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/workos-says-attacker-used-artex-ai-to-breach-internal-sales-app/)

Developer platform WorkOS suffered a data breach after a threat actor accessed business contact records and summaries of customer communications.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-109618** | PHP Memory Corruption Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-109619** | PHP Stale Internal Request-State Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-111497** | Google Brotli Unchecked Return Value Vulnerability | – | 83% | ⚠️ YES (KEV) |
| **CVE-2026-110447** | Collabora Online – Built-in CODE Server OS Command Injection Vulnerability | – | 73% | ⚠️ YES (KEV) |
| **CVE-2026-48356** | Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability | – | 45% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*