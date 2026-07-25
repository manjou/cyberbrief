# 🛡️ CyberBrief — Saturday, 25 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. Kimi K3 Agents Found Redis Zero-Days and Built RCE Exploit, Researchers Say
*The Hacker News* — [read more](https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html)

Redis shipped seven security releases on July 23 after researchers published authenticated RCE PoCs for stock Redis 6.2.22, 7.4.9, 8.6.4, and 8.8.0. All four chains require RESTORE. The Streams chains also need EVAL and XGROUP; the 8.8.0 chain needs EVAL and the bundled RedisBloom module. Redis says the underlying memory flaws may lead to remote code execution. Redis 6.2.23, 7.2.15, and 7.4.10

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. OnTrac notifies customers of data breach after network hack
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/)

OnTrac parcel delivery company is informing that hackers breached its corporate network and may have accessed personal details belonging to its customers. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 3. Data Breach Confirmed After Australian Energy Giant Origin Is Hacked
*SecurityWeek* — [read more](https://www.securityweek.com/data-breach-confirmed-after-australian-energy-giant-origin-is-hacked/)

A hacker claims to have stolen the information of 2 million Origin Energy customers and is threatening to leak it. The post Data Breach Confirmed After Australian Energy Giant Origin Is Hacked appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 4. Australian energy provider Origin says data breach exposes client data
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/)

Origin Energy has confirmed that an unauthorized party accessed and subsequently leaked customer data online, exposing sensitive personally identifiable information (PII), among others. [...]

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 5. Hermes AI agent used to automate attack on Thai Finance Ministry
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hermes-ai-agent-used-to-automate-attack-on-thai-finance-ministry/)

A threat actor used the open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation activity during an alleged breach of Thailand's Ministry of Finance. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Chick-fil-A data breach affects more than 13,000 customers
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/chick-fil-a-data-breach-affects-more-than-13-000-customers/)

Chick-fil-A has confirmed that over 13,000 customers had their accounts breached in a wave of credential stuffing attacks targeting its website and mobile app between June 17 and June 19. [...]

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.17 Authentication information

### 7. Clop ransomware targets Windchill, FlexPLM in data theft attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/)

The Clop ransomware gang (also tracked as Cl0p) is targeting Internet-exposed PTC Windchill and FlexPLM instances in a new data theft extortion campaign. [...]

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.34 Privacy and protection of PII

### 8. In Other News: Dolphin X AI-Powered Malware, Car Anti-Theft Device Hack, 400 Linux Kernel Flaws
*SecurityWeek* — [read more](https://www.securityweek.com/in-other-news-dolphin-x-ai-powered-malware-car-anti-theft-device-hack-400-linux-kernel-flaws/)

Noteworthy stories that might have slipped under the radar: Siemens ROX II industrial switch vulnerabilities, Russian Zimbra webmail espionage campaign, Stadler Rail ransomware extortion attempt. The post In Other News: Dolphin X AI-Powered Malware, Car Anti-Theft Device Hack, 400 Linux Kernel Flaws appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.7 Protection against malware

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-63030** | WordPress Core Interpretation Conflict Vulnerability | – | 98% | ⚠️ YES (KEV) |
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 90% | ⚠️ YES (KEV) |
| **CVE-2026-15409** | SonicWall SMA1000 Appliances Server-Side Request Forgery Vulnerability | – | 78% | ⚠️ YES (KEV) |
| **CVE-2026-60137** | WordPress Core SQL Injection Vulnerability | – | 78% | ⚠️ YES (KEV) |
| **CVE-2026-15410** | SonicWall SMA1000 Appliances Code Injection Vulnerability | – | 76% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*