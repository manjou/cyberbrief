# 🛡️ CyberBrief — Wednesday, 22 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. WordPress wp2shell Exploitation Grows as Public Exploit Fuels Mass Scanning
*The Hacker News* — [read more](https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html)

Attackers have begun to exploit two critical vulnerabilities in WordPress that, when combined together, enable unauthenticated remote code execution (RCE) and complete compromise of vulnerable websites. The two security flaws, tracked as CVE-2026-63030 and CVE-2026-60137, have been codenamed wp2shell. "By the early hours of Saturday morning (UTC), successful exploitation was already well

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Critical Palo Alto VPN bug now exploited by Qilin ransomware gang
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/critical-globalprotect-vpn-bug-now-exploited-in-ransomware-attacks/)

The Qilin ransomware gang is exploiting a critical PAN-OS GlobalProtect authentication bypass flaw to breach victims' networks, according to cybersecurity company Arctic Wolf. [...]

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 3. Anubis ransomware claims Coca-Cola Fairlife attack, threatens data leak
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/anubis-ransomware-claims-coca-cola-fairlife-attack-threatens-data-leak/)

The Anubis ransomware gang has claimed responsibility for the cyberattack on Coca-Cola's Fairlife dairy subsidiary, threatening to publish allegedly stolen corporate data unless the company pays a ransom. [...]

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.34 Privacy and protection of PII

### 4. Critical SharePoint RCE flaw exploited to steal machine keys
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/critical-sharepoint-rce-flaw-exploited-to-steal-machine-keys/)

Hackers are actively exploiting the critical CVE-2026-50522 vulnerability in Microsoft SharePoint to steal machine keys and maintain access even after affected servers are patched. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Estée Lauder discloses data breach via Oracle E-Business flaw
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/est-e-lauder-discloses-data-breach-via-oracle-e-business-flaw/)

Cosmetics giant Estée Lauder is notifying employees of a data breach after hackers exploited a flaw in Oracle E-Business Suite that the company used for human resources (HR) operations. [...]

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 6. Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC
*The Hacker News* — [read more](https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html)

A third SharePoint Server flaw patched by Microsoft as part of its Patch Tuesday update for July 2026 has come under active exploitation, per watchTowr. The vulnerability in question is CVE-2026-50522 (CVSS score: 9.8), a critical deserialization of untrusted data in Microsoft Office SharePoint that could allow an unauthorized attacker to execute code over a network. Microsoft credited DEVCORE

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. New ENCFORGE Ransomware Targets AI Model Files in Langflow RCE Attack
*The Hacker News* — [read more](https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html)

Researchers at Sysdig have linked a second attack on the same Langflow server to JADEPUFFER, the AI-agent-driven operator it first documented earlier this month. The same operator has now been spotted deploying ENCFORGE, a new compiled Go ransomware designed to encrypt model weights, vector indexes, training datasets, and other AI infrastructure files across the host filesystem. The entry

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 8. Police Dismantle Kratos Phishing Kit Built to Steal Microsoft 365 Sessions and Bypass MFA
*The Hacker News* — [read more](https://thehackernews.com/2026/07/police-dismantle-kratos-phishing-kit.html)

German and US law enforcement have taken down the core infrastructure of Kratos, described by German investigators as one of the world's most widely used criminal phishing kits, and Indonesian authorities arrested the man they say developed and ran it. In a joint announcement on Monday, the Frankfurt public prosecutor's cybercrime unit (ZIT) and Germany's Federal Criminal Police Office (BKA)

> 📋 **ISO 27001:** A.6.3 Awareness, education and training, A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-39808** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 84% | ⚠️ YES (KEV) |
| **CVE-2026-25089** | Fortinet FortiSandbox OS Command Injection Vulnerability | – | 36% | ⚠️ YES (KEV) |
| **CVE-2008-4128** | Cisco IOS Cross-Site Request Forgery Vulnerability | – | 24% | ⚠️ YES (KEV) |
| **CVE-2026-0770** | Langflow Inclusion of Functionality from Untrusted Control Sphere Vulnerability | – | 10% | ⚠️ YES (KEV) |
| **CVE-2026-63030** | WordPress Core Interpretation Conflict Vulnerability | – | 9% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*