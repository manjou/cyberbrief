# 🛡️ CyberBrief — Tuesday, 21 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. ⚡ Weekly Recap: WordPress RCE, SonicWall 0-Days, AI Service Attacks, SharePoint 0-Day and More
*The Hacker News* — [read more](https://thehackernews.com/2026/07/weekly-recap-wordpress-rce-sonicwall-0.html)

A single request should not be able to do this much. But this week, small inputs led to code execution, memory loss, stolen keys, and disabled security tools. The paths were often simple: exposed systems, weak checks, old drivers, fake prompts, and public code used for malware delivery. Some bugs were new. Others were already being used before defenders had time to patch. Here is the full

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 2. Estée Lauder discloses data breach via Oracle E-Business flaw
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/est-e-lauder-discloses-data-breach-via-oracle-e-business-flaw/)

Cosmetics giant Estée Lauder is notifying customers of a data breach after hackers exploited a flaw in Oracle E-Business Suite that the company used for human resources (HR) operations. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 3. New ENCFORGE Ransomware Targets AI Model Files in Langflow RCE Attack
*The Hacker News* — [read more](https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html)

Researchers at Sysdig have linked a second attack on the same Langflow server to JADEPUFFER, the AI-agent-driven operator it first documented earlier this month. The same operator has now been spotted deploying ENCFORGE, a new compiled Go ransomware designed to encrypt model weights, vector indexes, training datasets, and other AI infrastructure files across the host filesystem. The entry

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 4. SonicWall SMA1000 flaws exploited as zero-days to push custom malware
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/sonicwall-sma1000-flaws-exploited-as-zero-days-to-push-custom-malware/)

Two recently disclosed SonicWall SMA1000 vulnerabilities were exploited in zero-day attacks for weeks, allowing threat actors to install custom malware on vulnerable VPN appliances. [...]

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 5. Critical NGINX Vulnerability Can Crash Workers and May Allow Remote Code Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/07/critical-nginx-vulnerability-can-crash.html)

F5 has shipped fixes for a critical nginx flaw that lets a remote, unauthenticated attacker trigger a heap buffer overflow in the worker process with crafted HTTP requests. CVE-2026-42533 was patched on July 15 in nginx 1.30.4 (stable) and 1.31.3 (mainline), and in NGINX Plus 37.0.3.1; anyone on an earlier build should upgrade. Triggering it can crash or restart the worker, causing a denial of

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. WordPress Exploitation Underway (CVE-2026-63030), (Mon, Jul 20th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33168)

Last week, Searchlight Cyber released details about a vulnerability they are calling "wp2shell". The vulnerability was initially announced without a CVE number. But now has been assigned CVE-2026-63030. Many WordPress plugin vulnerabilities are never assigned CVE numbers. But wp2shell is different. It is a SQL injection vulnerability in WordPress Core, not a plugin, and can lead to unauthenticated remote code execution. Shortly after being announced, the vulnerability started to be exploited.&#x

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html)

Threat actors are now exploiting a recently disclosed critical security flaw impacting ServiceNow AI Platform, according to Defused Cyber. In a post shared on X, the threat intelligence firm said it's observing in-the-wild exploitation of CVE-2026-6875 (CVSS score: 9.5), a sandbox escape vulnerability that could allow an unauthenticated user to run arbitrary code. Patches for the flaw were

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. Russian-Speaking Hacker Uses Google Gemini CLI to Control Botnet of Eight Dental Clinic PCs
*The Hacker News* — [read more](https://thehackernews.com/2026/07/russian-speaking-hacker-uses-google.html)

A solo Russian-speaking threat actor known as "bandcampro" outsourced a chunk of their operations to Google's open-source Gemini CLI artificial intelligence (AI) and commandeered a live botnet. The findings come from an analysis of 200 Gemini CLI session logs between March 19 and April 21, 2026, which found the threat actor using AI, among other things, to crack passwords, set up a residential

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2026-25089** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 36% | ⚠️ YES (KEV) |
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 24% | ⚠️ YES (KEV) |
| **CVE-2026-56291** | Balbooa Forms Unrestricted Upload of File with Dangerous Type Vulnerability | – | 9% | ⚠️ YES (KEV) |

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