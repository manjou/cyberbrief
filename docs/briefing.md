# 🛡️ CyberBrief — SOC — Thursday, 12 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🔥 Top stories

### 1. Maersk confirms data breach as WhiteArmor ransomware demands $5 million
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/maersk-confirms-data-breach-as-whitearmor-ransomware-demands-5-million/)

Maersk announced that a threat actor gained unauthorized access to a local legacy system inherited through an earlier acquisition and extracted data from it.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.34 Privacy and protection of PII

### 2. N-able releases security hotfixes for zero-day vulnerabilities
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/n-able-releases-security-hotfixes-for-zero-day-vulnerabilities/)

N-able released hotfixes to address zero-day bugs affecting its N-central remote monitoring and management (RMM) platform, which were publicly disclosed over the weekend and forced it to take vulnerable hosted environments offline.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Hackers Target N-central Zero-Days as N-able Rushes Patches
*SecurityWeek* — [read more](https://www.securityweek.com/hackers-target-n-central-zero-days-as-n-able-rushes-patches/)

The malicious activity started shortly after a researcher dropped over 30 zero-days. N-able patched the unauthenticated ones.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html)

PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325, carries a CVSS v4 score of 9.2 out of a maximum of 10.0. It has been described as a case of improper input validation and deserialization of untrusted data that could result in

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. CISA flags Cisco BroadWorks flaw as actively exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-flags-cisco-broadworks-flaw-as-actively-exploited-in-attacks/)

The US Cybersecurity and Infrastructure Security Agency (CISA) warned on Tuesday that hackers are now exploiting a high-severity Cisco BroadWorks vulnerability in attacks.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches
*The Hacker News* — [read more](https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) Tuesday added two security flaws impacting Cisco BroadWorks and Openwave Messaging Webtop Media Transcoder to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. Details of the vulnerabilities are below - CVE-2026-20320 (CVSS score: 7.5) - An improper restriction of XML external entity

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 7. Hackers plant GSocket on Linux servers for persistent access
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-plant-gsocket-on-linux-servers-for-persistent-access/)

Multiple threat actors are abusing GSocket, a legitimate open-source remote access tool, to maintain access to Linux servers even after patching the vulnerabilities exploited to gain initial access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. eBPF Rootkits: Why Underground Actors Are Taking Notice
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/ebpf-rootkits-why-underground-actors-are-taking-notice/)

Linux eBPF rootkits can hide malicious activity and evade traditional detection methods without loading kernel modules. Flare reveals how these techniques are spreading through underground forums, where threat actors are sharing rootkit source code, tutorials, and exploits targeting Linux systems.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-97229** | GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability | – | 65% | ⚠️ YES (KEV) |
| **CVE-2026-125350** | Google Chromium Use-After-Free Vulnerability | 8.8 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-123158** | OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability | – | 17% | ⚠️ YES (KEV) |
| **CVE-2026-116779** | SignalWire FreeSwitch Code Injection Vulnerability | – | 2% | ⚠️ YES (KEV) |
| **CVE-2026-116606** | Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 2% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*