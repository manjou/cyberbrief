# 🛡️ CyberBrief — SOC — Thursday, 29 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: active exploitation, incident response, and threat activity.*

## 🕔 5pm recap

*Didn't get through this morning? Here's the quick version — full detail is still below.*

- **Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls** — Cisco has released patches to address a high-severity security flaw in Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software that it said has been exploited in the wild. [read more](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html)
- **Attackers Exploit Second Cisco Firewall VPN Zero-Day Since August** — An exploited flaw in the Remote Access SSL VPN service lets unauthenticated attackers remotely force ASA and FTD firewalls to reload. [read more](https://www.securityweek.com/attackers-exploit-second-cisco-firewall-vpn-zero-day-since-august/)
- **New Cisco firewall zero-day exploited to crash SSL VPN devices** — Cisco released security updates to patch a denial-of-service zero-day in Adaptive Security Appliance (ASA) and Threat Defense (FTD) software that attackers are exploiting to remotely crash vulnerable firewall devices. [read more](https://www.bleepingcomputer.com/news/security/cisco-warns-of-firewall-zero-day-exploited-to-crash-ssl-vpn-devices/)
- **China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility** — The U.S. [read more](https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html)
- **Cisco SD-WAN Zero-Day Exploitation Tied to Volt Typhoon’s ‘Silent Train’ Network** — Cisco Talos linked SD-WAN key-stealing malware to infrastructure overlapping Volt Typhoon’s Silent Train network, which Lumen detailed. [read more](https://www.securityweek.com/cisco-sd-wan-zero-day-exploitation-tied-to-volt-typhoons-silent-train-network/)
- **ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws** — The critical Oracle PeopleSoft bug that ShinyHunters has exploited since May is not one flaw but three chained together, the researchers who reported it said this week. [read more](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html)
- **Adobe Commerce PolyShell Attacks Breach Hundreds of Stores as Brotli Exploit Traffic Emerges** — The U.S. [read more](https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html)
- **Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch** — Threat actors are beginning to probe for a newly patched critical vulnerability in Oracle E-Business Suite (EBS), according to threat intelligence firm Defused Cyber. [read more](https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html)
- 5 CVEs flagged today (5 in active-exploitation KEV) — top: CVE-2026-109618 (– CVSS, 100% EPSS)

## 🔥 Top stories

### 1. Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls
*The Hacker News* — [read more](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html)

Cisco has released patches to address a high-severity security flaw in Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software that it said has been exploited in the wild. The vulnerability, tracked as CVE-2026-76418, is rated 8.6 on the CVSS scoring system. Successful exploitation could allow an unauthenticated, remote attacker to cause the

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 2. Attackers Exploit Second Cisco Firewall VPN Zero-Day Since August
*SecurityWeek* — [read more](https://www.securityweek.com/attackers-exploit-second-cisco-firewall-vpn-zero-day-since-august/)

An exploited flaw in the Remote Access SSL VPN service lets unauthenticated attackers remotely force ASA and FTD firewalls to reload.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 3. New Cisco firewall zero-day exploited to crash SSL VPN devices
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisco-warns-of-firewall-zero-day-exploited-to-crash-ssl-vpn-devices/)

Cisco released security updates to patch a denial-of-service zero-day in Adaptive Security Appliance (ASA) and Threat Defense (FTD) software that attackers are exploiting to remotely crash vulnerable firewall devices.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 4. China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility
*The Hacker News* — [read more](https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a security flaw impacting Broadcom VMware ESX to its Known Exploited Vulnerabilities (KEV) catalog, after CrowdStrike revealed that it had been weaponized by a China-nexus threat actor known as Warp Panda in attacks targeting the U.S. legal sector. The vulnerability in question is CVE-2026-41709 (CVSS score:

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Cisco SD-WAN Zero-Day Exploitation Tied to Volt Typhoon’s ‘Silent Train’ Network
*SecurityWeek* — [read more](https://www.securityweek.com/cisco-sd-wan-zero-day-exploitation-tied-to-volt-typhoons-silent-train-network/)

Cisco Talos linked SD-WAN key-stealing malware to infrastructure overlapping Volt Typhoon’s Silent Train network, which Lumen detailed.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 6. ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws
*The Hacker News* — [read more](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html)

The critical Oracle PeopleSoft bug that ShinyHunters has exploited since May is not one flaw but three chained together, the researchers who reported it said this week. Oracle patched all three under a single identifier, CVE-2026-35273, in June. Its root is a server-side request forgery (SSRF) that reaches an internal management interface because PeopleSoft trusts its own loopback address

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 7. Adobe Commerce PolyShell Attacks Breach Hundreds of Stores as Brotli Exploit Traffic Emerges
*The Hacker News* — [read more](https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added two vulnerabilities impacting Adobe Commerce and Magento, and Google's Brotli decoder library to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerabilities are listed below - CVE-2026-111497 (CVSS score: 9.2) - An unchecked return value vulnerability in

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch
*The Hacker News* — [read more](https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html)

Threat actors are beginning to probe for a newly patched critical vulnerability in Oracle E-Business Suite (EBS), according to threat intelligence firm Defused Cyber. The vulnerability in question is CVE-2026-101767 (CVSS score: 9.8) , a case of improper authentication in the Oracle Application Object Library of Oracle E-Business Suite. It was patched by Oracle last week as part of its Critical

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-109618** | PHP Memory Corruption Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-109619** | PHP Stale Internal Request-State Vulnerability | – | 100% | ⚠️ YES (KEV) |
| **CVE-2026-21589** | Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-111497** | Google Brotli Unchecked Return Value Vulnerability | – | 88% | ⚠️ YES (KEV) |
| **CVE-2026-48356** | Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability | – | 59% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*