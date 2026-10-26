# 🛡️ CyberBrief — SOC — Monday, 26 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. PHP2Shell security flaws now sucessfully exploited in the wild
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/php2shell-security-flaws-now-sucessfully-exploited-in-the-wild/)

Two critical RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619), collectively tracked as PHP2Shell, have been successfully exploited in the wild.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Microsoft 365 Token-Replay Attacks Compromise 97 Accounts at 79 Organizations
*The Hacker News* — [read more](https://thehackernews.com/2026/10/microsoft-365-token-replay-attacks.html)

Cybersecurity researchers have disclosed a Microsoft 365 campaign that has been observed leveraging an adversary-in-the-middle (AitM) relay to capture sign-in sessions and then replay the stolen tokens to break into email accounts at 79 organizations. Huntress, which observed the activity between July 14 and September 22, 2026, said it detected 497 successful Microsoft 365 sign-in events across

> 📋 **ISO 27001:** A.5.17 Authentication information

### 3. uCreator Android Spyware Can Steal Telegram 2FA Passwords and Clone WeChat Accounts
*The Hacker News* — [read more](https://thehackernews.com/2026/10/ucreator-android-spyware-can-steal.html)

A rentable Android spyware kit called uCreator takes over Telegram and WeChat accounts by hiding its code inside working copies of the two apps, researcher Ovi found. It only reaches people who install one of these tampered copies, spread outside the official app stores, or who run WeChat inside the kit makers' own container app. The kit's Telegram part matches Baohuo, a backdoor that Doctor

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.17 Authentication information

### 4. OpenAI AI Agents Demonstrate VM Escapes and Secret Cross-Sandbox Communication
*The Hacker News* — [read more](https://thehackernews.com/2026/10/openai-ai-agents-demonstrate-vm-escapes.html)

OpenAI has announced plans to conduct frontier model training with no live internet access, as it resumes reinforcement learning (RL) training and internal inference of its most advanced AI models. "Based on the current state of alignment research, monitoring systems, and the security of internet infrastructure, we believe the responsible approach is to conduct frontier model training with no

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Gheist Uses Stolen GitHub Tokens to Steal Private Repository Secrets via Actions Logs
*The Hacker News* — [read more](https://thehackernews.com/2026/10/gheist-uses-stolen-github-tokens-to.html)

An automated campaign is using stolen GitHub tokens to plant workflows that print a repository's secrets into its GitHub Actions logs, which the attackers then download before deleting the runs. The attacks have succeeded in private repositories and GitHub Enterprise environments, according to an analysis by cloud security company Wiz. A GitHub safeguard that pauses

> 📋 **ISO 27001:** A.5.23 Cloud services security, A.5.17 Authentication information

### 6. Malicious File in Downloads Folder Tries to Trick AI Coding Agent Into Installing Malware
*The Hacker News* — [read more](https://thehackernews.com/2026/10/malicious-file-in-downloads-folder.html)

A malicious instruction file sitting in a developer's Downloads folder tried to make their AI coding agent install a known-malicious npm package, security firm Forever Security said in a report published last week. The company caught the attempt on a real customer's machine and stopped the agent before any code ran. It could not determine how the file got into the folder. The file

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.19 Supplier relationships

### 7. Node2Shell: Brotli Flaw Triggers Patching Across Microsoft, Node.js, Python Packages
*SecurityWeek* — [read more](https://www.securityweek.com/node2shell-brotli-flaw-triggers-patching-across-microsoft-node-js-python-packages/)

An out-of-bounds write in Google’s Brotli decoder affects Node.js, .NET, PowerShell, and Python packages, and can lead to code execution.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. [UPDATE] [hoch] Microsoft Apps: Mehrere Schwachstellen ermöglichen Privilegieneskalation
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3241)

Ein Angreifer kann mehrere Schwachstellen in Microsoft Authenticator und Microsoft Xbox Gaming Services ausnutzen, um seine Privilegien zu erhöhen.

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-21589** | Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-104935** | Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | – | 87% | ⚠️ YES (KEV) |
| **CVE-2026-105134** | Ahsay AhsayCBS Command Injection Vulnerability | – | 86% | ⚠️ YES (KEV) |
| **CVE-2026-105133** | Ahsay AhsayCBS Improper Authentication Vulnerability | – | 79% | ⚠️ YES (KEV) |
| **CVE-2026-102764** | BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability | – | 20% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*