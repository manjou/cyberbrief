# 🛡️ CyberBrief — SOC — Monday, 28 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation** — Citrix NetScaler ADC and Gateway products contain two serious security holes that allow attackers to execute code remotely without authentication, and hackers are actively using these holes to break into systems. [read more](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)
- **Citrix confirms two NetScaler RCE zero-days exploited in attacks** — Two critical vulnerabilities in Citrix NetScaler (CVE-2026-88771 and CVE-2026-88772) that let attackers run unauthorized code have been confirmed as actively exploited in real attacks. [read more](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/)
- **CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally** — The U.S. [read more](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html)
- **Citrix Confirms 2 NetScaler Zero-Days After Admins Pulled the Plug** — Citrix released security updates to fix two critical remote code execution vulnerabilities (CVE-2026-88771 and CVE-2026-88772) in NetScaler products after administrators began taking affected systems offline due to active attacks. [read more](https://www.securityweek.com/citrix-confirms-2-netscaler-zero-days-after-admins-pulled-the-plug/)
- **JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources** — A threat actor group called JADEPUFFER compromised Azure cloud service principals (automated accounts with special permissions) and used them to delete cloud resources in a customer's environment, representing a new tactic for this group. [read more](https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html)
- **CISA orders feds to patch exploited Citrix flaws by Wednesday** — CISA issued an emergency directive requiring all U.S. [read more](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/)
- **Nvidia Unveils AI Agent Safety Platform With Hardware-Based Watchdog** — Nvidia released a platform designed to keep AI systems operating within pre-defined safe boundaries using hardware-based monitoring (a watchdog mechanism that automatically stops unsafe behavior). [read more](https://www.securityweek.com/nvidia-unveils-ai-agent-safety-platform-with-hardware-based-watchdog/)
- **[NEU] [mittel] Linux Kernel: Mehrere Schwachstellen** — Multiple security flaws exist in the Linux Kernel (the core of Linux operating systems) that could allow attackers to leak sensitive information, cause system crashes, or break memory protection mechanisms. [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3588)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-71362 (– CVSS, 88% EPSS)

## 🔥 Top stories

### 1. Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation
*The Hacker News* — [read more](https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html)

Citrix NetScaler ADC and Gateway products contain two serious security holes that allow attackers to execute code remotely without authentication, and hackers are actively using these holes to break into systems. This matters because NetScaler is a critical networking device used by many organizations, so a flaw affecting it puts many companies at risk simultaneously. Defenders need to apply the security patches Citrix released immediately and check their systems for signs of compromise.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Citrix confirms two NetScaler RCE zero-days exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/)

Two critical vulnerabilities in Citrix NetScaler (CVE-2026-88771 and CVE-2026-88772) that let attackers run unauthorized code have been confirmed as actively exploited in real attacks. This is a top priority because attackers are already using these flaws, meaning organizations could be compromised if not patched quickly. Security teams must prioritize patching these specific CVE numbers and monitor for any suspicious activity on affected systems.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 3. CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally
*The Hacker News* — [read more](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html)

The U.S. government's cybersecurity agency (CISA) officially confirmed that two Citrix NetScaler vulnerabilities are being actively exploited globally and added them to a public watchlist. When CISA adds a vulnerability to this list, it signals that defenders across all sectors should treat it as an urgent threat. Organizations should immediately prioritize patches for CVE-2026-88771 and verify their NetScaler versions are up to date.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 4. Citrix Confirms 2 NetScaler Zero-Days After Admins Pulled the Plug
*SecurityWeek* — [read more](https://www.securityweek.com/citrix-confirms-2-netscaler-zero-days-after-admins-pulled-the-plug/)

Citrix released security updates to fix two critical remote code execution vulnerabilities (CVE-2026-88771 and CVE-2026-88772) in NetScaler products after administrators began taking affected systems offline due to active attacks. This matters because the availability of patches means organizations can now protect themselves rather than having to disconnect critical systems. IT teams should test and deploy these patches to their NetScaler infrastructure as quickly as possible.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources
*The Hacker News* — [read more](https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html)

A threat actor group called JADEPUFFER compromised Azure cloud service principals (automated accounts with special permissions) and used them to delete cloud resources in a customer's environment, representing a new tactic for this group. This matters because compromised service principals can give attackers the same permissions as trusted automated processes, making their malicious actions harder to detect. Defenders should review service principal permissions, enable auditing of service principal activities, and implement multi-factor authentication where possible.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 6. CISA orders feds to patch exploited Citrix flaws by Wednesday
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-citrix-flaws-by-wednesday/)

CISA issued an emergency directive requiring all U.S. federal agencies to patch two critical Citrix NetScaler vulnerabilities by the following Wednesday due to active exploitation. This mandatory order signals the severity of the threat and reflects government-wide risk, meaning private organizations should treat this with similar urgency. Organizations should align their patching timelines with this government deadline and treat it as a business-critical priority.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 7. Nvidia Unveils AI Agent Safety Platform With Hardware-Based Watchdog
*SecurityWeek* — [read more](https://www.securityweek.com/nvidia-unveils-ai-agent-safety-platform-with-hardware-based-watchdog/)

Nvidia released a platform designed to keep AI systems operating within pre-defined safe boundaries using hardware-based monitoring (a watchdog mechanism that automatically stops unsafe behavior). This matters as AI systems become more powerful and are deployed in sensitive environments where uncontrolled behavior could cause harm. Defenders should evaluate AI safety controls when deploying AI tools and consider how to monitor autonomous AI agents in production.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. [NEU] [mittel] Linux Kernel: Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3588)

Multiple security flaws exist in the Linux Kernel (the core of Linux operating systems) that could allow attackers to leak sensitive information, cause system crashes, or break memory protection mechanisms. This matters because Linux runs on servers, cloud infrastructure, and embedded devices worldwide, so widespread kernel flaws affect a huge number of systems. Organizations should apply Linux kernel security updates promptly and monitor vendor advisories for patches relevant to their specific Linux distributions.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-71362** | Adobe Commerce and Magento Incorrect Authorization Vulnerability  | – | 88% | ⚠️ YES (KEV) |
| **CVE-2026-88771** | Citrix NetScaler Improper Input Validation Vulnerability | 9.5 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-88772** | Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability | 9.5 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-76461** | Cisco Secure Email Gateway SQL Injection Vulnerability | – | 28% | ⚠️ YES (KEV) |
| **CVE-2026-93616** | Check Point Multiple Products Path Traversal Vulnerability | – | 20% | ⚠️ YES (KEV) |

**CVE-2026-71362** — An authorization flaw in Adobe Commerce and Magento (e-commerce platforms) allows users to access or modify resources they should not have permission to access. This matters because e-commerce platforms handle payment data and customer information, so authorization flaws could lead to fraud or data theft. Defenders should patch affected Commerce and Magento installations immediately and audit recent user access logs for suspicious activity.

**CVE-2026-88771** — CVE-2026-88771 is a critical flaw in Citrix NetScaler ADC and Gateway that fails to properly validate user input, allowing unauthenticated attackers to compromise the system; it affects versions before 14.1-73.37 and 13.1-64.23. This is one of the two actively exploited vulnerabilities confirmed by CISA and Citrix, making it a top priority. Organizations must identify which NetScaler versions they run and immediately apply the patched versions listed.

**CVE-2026-88772** — CVE-2026-88772 is a second critical flaw in Citrix NetScaler that allows unauthenticated remote code execution or system crashes; affected versions are before 14.1-73.37 and 13.1-64.23. This is the second of the two actively exploited Citrix vulnerabilities and has the same version ranges as CVE-2026-88771, meaning a single patch often fixes both. Defenders should apply patches to all affected version ranges and verify the update was successful.

**CVE-2026-76461** — CVE-2026-76461 is a SQL injection vulnerability in Cisco Secure Email Gateway (a device that filters and scans email traffic) that allows attackers to manipulate database queries. This matters because email gateways sit between external email and internal networks, so a compromise could allow attackers to bypass email security controls. Organizations using this product should apply Cisco security patches and consider implementing additional database query logging to detect suspicious activity.

**CVE-2026-93616** — CVE-2026-93616 is a path traversal vulnerability in Check Point products (likely security or firewall software) that allows attackers to access files outside their intended directory. This matters because it could allow an attacker to read sensitive configuration files or system files they should not access. Defenders should apply Check Point security updates immediately and review access logs to determine if this vulnerability was exploited.

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*