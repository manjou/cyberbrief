# 🛡️ CyberBrief — SOC — Monday, 16 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. TSMC employee data breach linked to cloud provider
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/tsmc-employee-data-breach-linked-to-cloud-provider/)

Taiwan Semiconductor Manufacturing Company (TSMC) confirmed that personal employee data has been leaked online after a threat actor put 6.9GB of information allegedly stolen from the company up for auction.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.23 Cloud services security

### 2. Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch
*SecurityWeek* — [read more](https://www.securityweek.com/telegram-widgets-hit-by-rce-demos-malware-warning-days-after-launch/)

Kaspersky suspects exploitation of Telegram’s new widgets to deliver WebRAT, as researchers demo RCE and Pavel Durov disputes the claims.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 3. Scans for LiteLLM/Starlette (CVE-2026-42271, CVE-2026-48710), (Mon, Nov 16th)
*SANS ISC* — [read more](https://isc.sans.edu/diary/rss/33522)

This weekend, we started seeing requests for /mcp-rest/test/tools/list hitting our honeypots. These requests appear to attempt to exploit CVE-2026-42271 and CVE-2026-48710. Horizon3.ai published a short write-up about how these vulnerabilities can be chained to achieve remote code execution without authentication &#x5b;Horizon3&#x5d;&#xd;

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 4. Microsoft Rules Out Cyberattack in Outage, Warns of Phishing Campaign
*SecurityWeek* — [read more](https://www.securityweek.com/microsoft-rules-out-cyberattack-in-outage-warns-of-phishing-campaign/)

Phishing emails posing as Microsoft 365 service notices referenced the real outage incident and threatened to delete held messages.

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.8.6 Capacity management

### 5. Cursor Says Stolen Fireworks AI Key Led to Trojanized Claude Code Extension Incident
*The Hacker News* — [read more](https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html)

The compromise of Anthropic's official Claude Code extension on Cursor's extension marketplace was the result of the theft of an access key that was exposed in the wake of a breach targeting Fireworks AI. "An attacker obtained an access key we had issued to Fireworks," Cursor said in a Friday update. "The key was exposed by Fireworks, and the attacker used it to copy data from a read-only

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.5.34 Privacy and protection of PII

### 6. Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify, and Other Apps for API Keys
*The Hacker News* — [read more](https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html)

Attackers' AI agents have been hunting for weak spots in internet-exposed AI apps such as LiteLLM, One API, and Dify to steal the AI provider keys stored inside, according to the agents' own records. The records, which Amazon's threat intelligence team captured with decoy servers, describe stolen keys being used to run the AI models that powered the search for more keys. The team said this

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 7. BO Team Exploits Log4Shell in VMware vCenter, Compromises Russian Firm's Code-Signing Server
*The Hacker News* — [read more](https://thehackernews.com/2026/11/bo-team-exploits-log4shell-in-vmware.html)

An investigation into suspicious activity within a Russian software developer's network has uncovered a months-long compromise of its development infrastructure and a software code-signing server. The activity, documented by Kaspersky's ICS CERT team after it was contacted by the affected developer in June 2025, has been attributed to a threat actor named BO Team (aka Black Owl, Hoody Hyena,

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. Uber Data Breach Impacts 150,000 People
*SecurityWeek* — [read more](https://www.securityweek.com/uber-data-breach-impacts-150000-people/)

Hackers compromised a third-party services provider and stole names, addresses, and driver’s license numbers.

> 📋 **ISO 27001:** A.5.19 Supplier relationships, A.5.34 Privacy and protection of PII

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-123158** | OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability | – | 19% | ⚠️ YES (KEV) |
| **CVE-2026-116606** | Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 11% | ⚠️ YES (KEV) |
| **CVE-2026-111560** | Barracuda Networks Multiple Products OS Command Injection Vulnerability | – | 9% | ⚠️ YES (KEV) |
| **CVE-2026-116779** | SignalWire FreeSwitch Code Injection Vulnerability | – | 2% | ⚠️ YES (KEV) |
| **CVE-2026-123039** | Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability | – | 2% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*