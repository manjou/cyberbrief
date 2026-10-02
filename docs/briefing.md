# 🛡️ CyberBrief — GRC — Friday, 02 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Fortinet warns of critical FortiMail flaw exploited in zero-day attacks** — Fortinet discovered a serious security flaw in FortiMail (an email security tool) that attackers are already using to break into systems without permission. [read more](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/)
- **Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes** — CISA (a U.S. [read more](https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html)
- **Exploited Fortinet FortiMail Zero-Day Calls for Urgent Action** — CVE-2026-104286 is a 'path traversal' vulnerability, which means attackers can trick the system into writing files outside the intended folder locations, potentially gaining full control. [read more](https://www.securityweek.com/exploited-fortinet-fortimail-zero-day-calls-for-urgent-action/)
- **Police dismantle KillSec ransomware gang allegedly led by 16-year-old** — An international police operation shut down the KillSec ransomware group (criminals who encrypt company data and demand ransom payments), seized their data leak website, and arrested three people, including identifying a 16-year-old as a core leader. [read more](https://www.bleepingcomputer.com/news/security/police-dismantle-killsec-ransomware-gang-allegedly-led-by-16-year-old/)
- **ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories** — This article discusses how common computer functions like model inspection, caching (temporary storage), and compilation can become security weaknesses if they perform unexpected actions or don't properly isolate data. [read more](https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html)
- **Police Shut Down KillSec Ransomware, Identify Alleged Teen Leader** — Police took control of KillSec's leak website (where they posted stolen data to pressure victims into paying ransom) and secured at least 110 terabytes of stolen data, preventing criminals from using it as leverage. [read more](https://www.securityweek.com/police-shut-down-killsec-ransomware-identify-alleged-teen-leader/)
- **CISA Adds Exploited Cisco Catalyst SD-WAN Manager Auth Bypass to KEV** — CISA added a critical authentication bypass flaw in Cisco Catalyst SD-WAN Manager (a network device manager) to its list of actively exploited vulnerabilities, meaning attackers can log in as administrators without valid credentials. [read more](https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html)
- **Hackers stole Pentagon personnel records of over 3 million people** — Hackers breached the Pentagon's human resources database in October 2025 and stole personal records of over 3 million military service members, including likely names, Social Security numbers, and addresses. [read more](https://www.bleepingcomputer.com/news/security/hackers-breach-pentagon-human-resources-management-system-steal-data-of-nearly-3-million-people/)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-71362 (– CVSS, 88% EPSS)

## 🔥 Top stories

### 1. Fortinet warns of critical FortiMail flaw exploited in zero-day attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/)

Fortinet discovered a serious security flaw in FortiMail (an email security tool) that attackers are already using to break into systems without permission. This matters because FortiMail protects email for many organizations, so a working exploit puts thousands of companies at immediate risk. Defenders need to apply Fortinet's security patch as soon as possible and monitor their FortiMail systems for signs of unauthorized access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes
*The Hacker News* — [read more](https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html)

CISA (a U.S. government cybersecurity agency) officially confirmed that FortiMail vulnerability CVE-2026-104286 is being actively exploited in real attacks and added it to their tracking list of dangerous, actively-used flaws. This public confirmation signals that the threat is real and widespread, making it a priority for any organization using FortiMail. Defenders should treat this as urgent and patch immediately, then check their systems for evidence of past attacks.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Exploited Fortinet FortiMail Zero-Day Calls for Urgent Action
*SecurityWeek* — [read more](https://www.securityweek.com/exploited-fortinet-fortimail-zero-day-calls-for-urgent-action/)

CVE-2026-104286 is a 'path traversal' vulnerability, which means attackers can trick the system into writing files outside the intended folder locations, potentially gaining full control. The high CVSS score (9.8 out of 10) reflects how dangerous this is because no authentication is required—anyone on the internet can attempt it. Defenders must patch all affected FortiMail versions and review file integrity logs to detect if attackers already wrote malicious files.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. Police dismantle KillSec ransomware gang allegedly led by 16-year-old
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/police-dismantle-killsec-ransomware-gang-allegedly-led-by-16-year-old/)

An international police operation shut down the KillSec ransomware group (criminals who encrypt company data and demand ransom payments), seized their data leak website, and arrested three people, including identifying a 16-year-old as a core leader. This matters because ransomware causes billions in damage yearly, and dismantling active groups disrupts ongoing attacks and recovers stolen data. Defenders benefit from law enforcement taking down the infrastructure that criminals use to extort victims.

> 📋 **ISO 27001:** A.8.13 Information backup, A.8.8 Management of technical vulnerabilities

### 5. ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories
*The Hacker News* — [read more](https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html)

This article discusses how common computer functions like model inspection, caching (temporary storage), and compilation can become security weaknesses if they perform unexpected actions or don't properly isolate data. These 'boring' features matter because attackers exploit the gap between what a feature is supposed to do and what it actually does—a hidden attack path. Defenders need to audit how systems use these features and ensure proper access controls and data separation.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Police Shut Down KillSec Ransomware, Identify Alleged Teen Leader
*SecurityWeek* — [read more](https://www.securityweek.com/police-shut-down-killsec-ransomware-identify-alleged-teen-leader/)

Police took control of KillSec's leak website (where they posted stolen data to pressure victims into paying ransom) and secured at least 110 terabytes of stolen data, preventing criminals from using it as leverage. This matters because stolen data is leverage for ransom payments and ongoing blackmail, so recovering it removes the attacker's main negotiating tool. Defenders benefit from the recovered data being removed from criminal hands, reducing risk to affected victims.

> 📋 **ISO 27001:** A.8.13 Information backup, A.5.34 Privacy and protection of PII

### 7. CISA Adds Exploited Cisco Catalyst SD-WAN Manager Auth Bypass to KEV
*The Hacker News* — [read more](https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html)

CISA added a critical authentication bypass flaw in Cisco Catalyst SD-WAN Manager (a network device manager) to its list of actively exploited vulnerabilities, meaning attackers can log in as administrators without valid credentials. This matters because SD-WAN Managers control network traffic for many organizations, so bypass flaws let attackers take over entire networks. Defenders must patch immediately and review access logs for suspicious admin-level activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 8. Hackers stole Pentagon personnel records of over 3 million people
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-breach-pentagon-human-resources-management-system-steal-data-of-nearly-3-million-people/)

Hackers breached the Pentagon's human resources database in October 2025 and stole personal records of over 3 million military service members, including likely names, Social Security numbers, and addresses. This matters because this data can be used for identity theft, blackmail, or targeting military personnel and their families. Defenders and affected individuals should monitor credit reports, watch for phishing targeting military communities, and consider identity theft protection.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-71362** | Adobe Commerce and Magento Incorrect Authorization Vulnerability  | – | 88% | ⚠️ YES (KEV) |
| **CVE-2026-76504** | Cisco Catalyst SD-WAN Manager Hex Encoding Vulnerability | 9.8 | 1% | ⚠️ YES (KEV) |
| **CVE-2026-104286** | Fortinet FortiMail Path Traversal Vulnerability | 9.8 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-87902** | WordPress Core Remote File Inclusion Vulnerability | – | 20% | ⚠️ YES (KEV) |
| **CVE-2026-93616** | Check Point Multiple Products Path Traversal Vulnerability | – | 20% | ⚠️ YES (KEV) |

**CVE-2026-71362** — This Adobe Commerce and Magento vulnerability involves incorrect authorization, meaning the system doesn't properly verify user permissions before allowing access to sensitive data or functions. This matters because e-commerce platforms handle payment data and customer information, so permission flaws can expose both. Defenders using these platforms should apply patches and audit user roles to ensure people only have access to what they genuinely need.

**CVE-2026-76504** — CVE-2026-76504 is an authentication bypass in Cisco SD-WAN Manager where attackers can send specially-crafted web requests using URI encoding tricks to log in as admin without credentials. This matters because SD-WAN Managers control how network traffic is routed for large organizations, so admin access means full network control. Defenders must patch, review access logs for suspicious logins, and consider network segmentation to limit damage if breached.

**CVE-2026-104286** — CVE-2026-104286 is a path traversal flaw in FortiMail versions 7.2 through 8.0 that allows unauthenticated attackers to write files anywhere on the system instead of just in intended folders. This matters because file-write access can lead to installing backdoors (persistent unauthorized access), modifying email messages, or taking over the entire server. Defenders must patch all affected versions immediately and check for suspicious files created on FortiMail systems.

**CVE-2026-87902** — WordPress Core Remote File Inclusion (RFI) means attackers can trick a WordPress site into loading and executing malicious code from external sources instead of only loading intended files. This matters because WordPress powers roughly 40% of websites, so RFI flaws put millions of sites at risk for defacement, data theft, or spreading malware. Defenders must update WordPress immediately and use security plugins to restrict file inclusion to trusted sources.

**CVE-2026-93616** — This Check Point vulnerability is a path traversal flaw in their security products, allowing attackers to access files outside intended directories and potentially expose sensitive configuration or data files. This matters because Check Point products are firewalls and security tools used by enterprises to protect networks, so compromising them defeats the entire security layer. Defenders using Check Point must patch immediately and verify their systems were not accessed by reviewing access logs and configurations.

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*