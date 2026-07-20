# 🛡️ CyberBrief — Monday, 20 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. Critical NGINX Vulnerability Can Crash Workers and May Allow Remote Code Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/07/critical-nginx-vulnerability-can-crash.html)

F5 has shipped fixes for a critical nginx flaw that lets a remote, unauthenticated attacker trigger a heap buffer overflow in the worker process with crafted HTTP requests. CVE-2026-42533 was patched on July 15 in nginx 1.30.4 (stable) and 1.31.3 (mainline), and in NGINX Plus 37.0.3.1; anyone on an earlier build should upgrade. Triggering it can crash or restart the worker, causing a denial of

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. SonicWall SMA Zero-Days Exploited Before Disclosure to Gain Root Access
*The Hacker News* — [read more](https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html)

A previously undocumented threat actor has been attributed to the exploitation of recently disclosed SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances as zero-days prior their public disclosure since June 22, 2026. Cybersecurity company Volexity is tracking the activity under the moniker UTA0533. The discovery was made following an incident response investigation earlier this

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.24 Incident management planning

### 3. World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent
*The Hacker News* — [read more](https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html)

In an ironic twist, open-source artificial intelligence (AI) platform Hugging Face revealed that it was the victim of a hack perpetrated by an autonomous AI agent system. The company said it detected and responded to the incident targeting its production infrastructure earlier last week. "We identified unauthorized access to a limited set of internal datasets and to several credentials used by

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 4. UAC-0145 Uses ClickFix CAPTCHAs to Infect Ukrainian Devices wih Malware
*The Hacker News* — [read more](https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html)

Russian state-sponsored threat actors have been observed leveraging the infamous ClickFix strategy to trick Ukrainian targets into infecting their own machines with data-stealing malware. According to the Computer Emergency Response Team of Ukraine (CERT-UA), the activity has been attributed to UAC-0145, a sub-cluster within Sandworm, an advanced hacking unit affiliated with GRU, Russia's

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.24 Incident management planning

### 5. WP2Shell WordPress Vulnerabilities Exploited in the Wild
*SecurityWeek* — [read more](https://www.securityweek.com/wp2shell-wordpress-vulnerabilities-exploited-in-the-wild/)

Exploitation of the new WordPress vulnerabilities tracked as CVE-2026-60137 and CVE-2026-63030 started soon after disclosure. The post WP2Shell WordPress Vulnerabilities Exploited in the Wild appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines
*The Hacker News* — [read more](https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html)

Cybersecurity researchers have flagged a new software supply chain attack codenamed SleeperGem targeting the Ruby ecosystem after three malicious gems were published to RubyGems with the end goal of serving additional payloads. The rogue gems are listed below - git_credential_manager (versions 2.8.0, 2.8.1, 2.8.2, 2.8.3) - Published on July 18, 2026 Dendreo (versions 1.1.3, 1.1.4) -

> 📋 **ISO 27001:** A.5.19 Supplier relationships, A.5.17 Authentication information

### 7. Chrome 150 Update Patches Severe Memory Safety Bugs
*SecurityWeek* — [read more](https://www.securityweek.com/chrome-150-update-patches-severe-memory-safety-bugs/)

The fresh security update resolves six critical and high-severity use-after-free vulnerabilities. The post Chrome 150 Update Patches Severe Memory Safety Bugs appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. [UPDATE] [hoch] FreeRDP: Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2384)

Ein Angreifer kann mehrere Schwachstellen in FreeRDP ausnutzen, um beliebigen Programmcode auszuführen, Sicherheitsmaßnahmen zu umgehen, vertrauliche Informationen offenzulegen, Daten zu manipulieren oder einen Denial-of-Service-Zustand auszulösen.

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2026-25089** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 36% | ⚠️ YES (KEV) |
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 24% | ⚠️ YES (KEV) |
| **CVE-2026-56291** | Balbooa Forms Unrestricted Upload of File with Dangerous Type Vulnerability | – | 9% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*