# 🛡️ CyberBrief — GRC — Friday, 16 October 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🔥 Top stories

### 1. Next.js Ships Out-of-Band Patch for Two Critical RCE Flaws in Caching and SVG Processing
*The Hacker News* — [read more](https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html)

Next.js released an emergency security patch on October 14 to fix two critical flaws that allow attackers to run malicious code on servers without needing a password. These flaws existed in how the framework handles caching and processes SVG image files. Defenders need to immediately update Next.js to the patched version and review their deployment logs to check if these flaws were exploited before patching.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Critical PwnEscape Linux Kernel Vulnerability Lets Guest VMs Read Host Memory
*The Hacker News* — [read more](https://thehackernews.com/2026/10/critical-pwnescape-linux-kernel.html)

A critical flaw in the Linux kernel allows code running inside a virtual machine to read private data stored in the host computer's memory, breaking the isolation that should separate them. This is serious because cloud providers use virtual machines to isolate different customers' workloads from each other, so this flaw could expose one customer's data to another. Defenders need to patch their Linux kernels, review who has access to run virtual machines, and monitor for suspicious memory-reading activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 3. Hackers exploit Collabora RCE flaw to backdoor Nextcloud servers
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/hackers-exploit-collabora-rce-flaw-to-backdoor-nextcloud-servers/)

Attackers are actively exploiting a critical flaw (CVE-2026-110447) in the Collabora Online application that lets them run arbitrary commands on Nextcloud servers. Nextcloud is popular file-sharing and collaboration software, so compromised servers can lead to data theft or loss. Defenders should immediately update the richdocumentscode app, disable it if updates aren't available, and check server logs for signs of exploitation.

> 📋 **ISO 27001:** A.8.7 Protection against malware, A.8.8 Management of technical vulnerabilities

### 4. Palo Alto Networks warns of PAN-OS RCE flaw exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-pan-os-rce-flaw-exploited-in-attacks/)

Palo Alto Networks discovered a high-severity flaw in PAN-OS (their firewall software) that allows remote code execution, and attackers are already exploiting it in the wild. Firewalls are critical security devices, so compromising them gives attackers control over all network traffic flowing through them. Defenders must apply Palo Alto's security patches immediately and monitor firewall logs for suspicious activity.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.20 Networks security

### 5. BeyondTrust patches zero-day exploited in attacks since August
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/beyondtrust-patches-zero-day-exploited-in-attacks-since-august/)

BeyondTrust discovered that a critical flaw in its Remote Support product has been actively exploited by attackers since August, before a patch was publicly available (this is called a zero-day attack). Remote Support software is used to manage and access computers remotely, so compromising it gives attackers direct access to customer systems. Defenders need to patch immediately, review access logs from August onward for suspicious connections, and check if their systems were compromised.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Drupal Patches Critical Field UI Flaw With Unauthenticated RCE Path via Contributed Modules
*The Hacker News* — [read more](https://thehackernews.com/2026/10/drupal-patches-critical-core-rce-flaw.html)

Drupal released security patches on October 14 for a critical flaw in its Field UI module that allows unauthenticated attackers to run code on vulnerable websites. The flaw cannot be exploited through Drupal core alone—attackers need certain add-on modules installed—but this still affects many real-world sites. Defenders must update Drupal to the patched versions and review which contributed modules are installed on their sites.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. China-Linked Hackers Exploited BeyondTrust Zero-Day to Take Over Remote Support Servers
*The Hacker News* — [read more](https://thehackernews.com/2026/10/china-linked-hackers-exploited.html)

A China-linked hacking group called Armory Castle exploited a critical flaw (CVE-2026-102764) in BeyondTrust Remote Support in August 2026 before the company disclosed or patched it. The attackers gained control of customers' remote support servers, which typically have high-level access to corporate networks. Defenders need to assume their BeyondTrust systems may have been compromised, conduct forensic investigations of activity since August, patch immediately, and reset credentials for accounts that used those servers.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 8. CenterPoint Energy Data Breach Impacts 1 Million Texans
*SecurityWeek* — [read more](https://www.securityweek.com/centerpoint-energy-data-breach-impacts-1-million-texans/)

CenterPoint Energy, a major utility company in Texas, suffered a data breach exposing sensitive personal information (names, addresses, Social Security numbers, driver's licenses) for about 1 million people. This kind of personal data is valuable to criminals for identity theft and fraud. Defenders should monitor breach notification sites, individuals should watch for suspicious credit activity, and companies should implement stronger data protection controls like encryption and access restrictions.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2015-5477** |  ISC BIND Data Processing Errors Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2015-3306** | ProFTPD Improper Access Control Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2016-3081** | Apache Struts Command Injection Vulnerability | – | 96% | ⚠️ YES (KEV) |
| **CVE-2026-76519** | Cisco Secure Email Gateway Relative Path Traversal Vulnerability | 9.8 | 2% | ⚠️ YES (KEV) |
| **CVE-2026-0322** | Palo Alto Networks PAN-OS Code Injection Vulnerability | 8.6 | 1% | ⚠️ YES (KEV) |

**CVE-2015-5477** — CVE-2015-5477 is a flaw in ISC BIND, a widely-used DNS server software, that allows attackers to cause errors in how data is processed and potentially crash the service. DNS is critical infrastructure that translates website names to IP addresses, so disrupting it affects internet availability. Defenders should have patched this years ago if it's still running, but if legacy systems still use old BIND versions, they need urgent updates or network segmentation to isolate them.

**CVE-2015-3306** — CVE-2015-3306 is a flaw in ProFTPD, a file-transfer server software, that improperly controls who can access files. An attacker with limited permissions might be able to access files they shouldn't, or an unauthenticated attacker might gain access to restricted areas. Defenders should update ProFTPD, review file permissions and access controls, and disable the service if it's not actively needed.

**CVE-2016-3081** — CVE-2016-3081 is a command-injection flaw in Apache Struts, a popular framework for building web applications, that allows attackers to execute arbitrary system commands. If a web application built with vulnerable Struts is exploited, the attacker gets the same privileges as the web server process. Defenders should patch Apache Struts immediately, disable or isolate affected applications until patched, and review application logs for signs of exploitation.

**CVE-2026-76519** — CVE-2026-76519 is a flaw in Cisco Secure Email Gateway's malware protection feature that allows unauthenticated remote attackers to write arbitrary files to the server's operating system. Email gateways are often trusted security devices positioned between the internet and internal networks, so compromising them gives attackers a foothold to attack internal systems. Defenders must patch this immediately, restrict network access to the email gateway's management interface, and monitor for suspicious file-write activity.

**CVE-2026-0322** — CVE-2026-0322 is a remote code execution flaw in Palo Alto Networks PAN-OS that allows an authenticated attacker (someone with valid login credentials) with network access to run arbitrary code with root privileges on the firewall. Root privileges mean complete control of the firewall. Defenders should apply the patch immediately, implement strong authentication (multi-factor authentication), restrict network access to the management interface to trusted administrators only, and review logs for unauthorized access attempts.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*