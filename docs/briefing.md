# 🛡️ CyberBrief — Sunday, 12 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. Hackers Weaponize Balochistan Police Portal in Multi-Group Espionage Campaigns
*The Hacker News* — [read more](https://thehackernews.com/2026/07/hackers-weaponize-balochistan-police.html)

Cybersecurity researchers have disclosed details of sustained cyber espionage activity against several Pakistani law enforcement organizations undertaken by suspected China- and India-aligned threat actors between February 2024 and April 2026. "At Balochistan Police, the compromised assets included servers hosting web applications that manage police and citizen data, such as criminal and

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Claude Fable 5 stays free for paid users until July 19 as Anthropic buys more time
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-stays-free-for-paid-users-until-july-19-as-anthropic-buys-more-time/)

Anthropic has just extended access to Claude Fable 5 for paid subscribers until July 19, giving you another week to keep using the most powerful model. [...]

### 3. RedHook Android malware now uses Wireless ADB for shell access
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/redhook-android-malware-now-uses-wireless-adb-for-shell-access/)

A new version of the RedHook Android malware abuses the Android Wireless Debugging (Wireless ADB) mechanism in a novel way to gain shell-level privileges without requiring a computer connection. [...]

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.2 Privileged access rights

### 4. Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install
*The Hacker News* — [read more](https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html)

The jscrambler npm package was compromised, and simply installing its 8.14.0 release runs an infostealer on your machine. Published on July 11, 2026, the malicious version carries a preinstall hook that drops and executes a native binary, one build each for Windows, macOS, and Linux. Socket flagged the release six minutes after it was published. If you or one of your

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.19 Supplier relationships

### 5. Ghost Accounts Abuse GitHub API in Mass Recon Campaign
*SecurityWeek* — [read more](https://www.securityweek.com/ghost-accounts-abuse-github-api-in-mass-recon-campaign/)

Multiple campaigns are using ghost accounts to map GitHub organizations, including their repositories and members. The post Ghost Accounts Abuse GitHub API in Mass Recon Campaign appeared first on SecurityWeek .

### 6. Australia warns of global campaign targeting vulnerable CMS platforms
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/australia-warns-of-global-campaign-targeting-vulnerable-cms-platforms/)

The Australian Cyber Security Centre (ACSC) issued an alert about a global exploitation campaign targeting vulnerable content management systems (CMS) and plugins. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. 'Ghostcommit' hides prompt injection in images to fool AI agents, steal secrets
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/)

A PNG hiding a prompt injection could steal your repo's secrets, researchers demonstrate. The technique, dubbed 'Ghostcommit,' slipped past AI code reviewers CodeRabbit and Bugbot, which never open image files at all, then convinced a coding agent to read a repo's .env and write every secret into the code as a list of numbers. [...]

### 8. Wireshark 4.6.7 Released, (Sat, Jul 11th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33146)

Wireshark release 4.6.7 fixes 12 vulnerabilities and 16 bugs.&#xd;

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2026-45659** | Microsoft SharePoint Server Deserialization of Untrusted Data Vulnerability | – | 3% | ⚠️ YES (KEV) |
| **CVE-2026-56290** | Joomlack Page Builder Improper Access Control Vulnerability | – | 3% | ⚠️ YES (KEV) |
| **CVE-2026-48939** | iCagenda Unrestricted Upload of File with Dangerous Type Vulnerability | – | 2% | ⚠️ YES (KEV) |
| **CVE-2026-48908** | JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability | – | 2% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*