# 🛡️ CyberBrief — GRC — Friday, 18 September 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🔥 Top stories

### 1. Cisco warns of max severity ISE zero-day exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/)

Cisco's Identity Services Engine (ISE)—a system that controls who can access a network—has a critical flaw that hackers are already using to break in. This matters because ISE is widely used by organizations to manage network access, so attackers exploiting it could gain entry to many corporate networks. Defenders need to apply Cisco's security patches immediately and monitor their ISE systems for signs of compromise.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root
*The Hacker News* — [read more](https://thehackernews.com/2026/09/critical-check-point-management-server.html)

Check Point's Security Management Server, which controls firewall rules and admin access, has a flaw that allows someone without a login account to run commands as the highest-level user (root) remotely. This is severe because an attacker gaining root access to the management server can control an entire organization's firewall policies and security. Defenders must patch this immediately and restrict network access to the management server to trusted systems only.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 3. Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone
*The Hacker News* — [read more](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)

Unbound is a DNS resolver (a system that translates domain names to IP addresses) that contains a memory overflow flaw in its DNSSEC validation—the security check for DNS answers. An attacker controlling a malicious DNS zone can crash the resolver or run their own code on it by sending a specially crafted request. Defenders must update Unbound to version 1.26.1 or later and verify that DNS resolvers are only accepting queries from legitimate sources.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. Critical Orkes Conductor Vulnerability Exploited in Attacks
*SecurityWeek* — [read more](https://www.securityweek.com/critical-orkes-conductor-vulnerability-exploited-in-attacks/)

Orkes Conductor is a workflow automation tool with an unauthenticated remote code execution flaw (CVE-2026-58138) that attackers can trigger by submitting malicious workflow definitions. This matters because attackers can gain full control of the system without needing any credentials. Defenders must patch immediately, disable or restrict access to workflow definition uploads, and monitor logs for suspicious workflow submissions.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Revolut Data Breach: 5 Months, 680 High-Profile Accounts, $3M Ransom
*SecurityWeek* — [read more](https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/)

Attackers gained access to Revolut's systems by impersonating an Italian government agency and stealing customer data; this went undetected for five months and affected 680 high-profile accounts before a $3 million ransom demand. This shows how social engineering and poor verification of requests can lead to large-scale data theft. Defenders learn from this that they need strict verification procedures for sensitive data requests, employee security training, and rapid incident detection systems.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 6. Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks
*The Hacker News* — [read more](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)

Cisco ISE has a maximum-severity authentication bypass flaw (CVE-2026-76460, CVSS 10.0) that allows remote attackers without credentials to skip authentication entirely and access the system. This is critical because ISE controls network access for many organizations, so bypassing its authentication gives attackers direct entry. Defenders must apply the emergency patch from Cisco immediately and consider temporarily isolating ISE from untrusted networks.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.17 Authentication information

### 7. BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS
*The Hacker News* — [read more](https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html)

BIND 9, the widely-used DNS server software, had fourteen security flaws fixed in its latest update; one flaw allows an unauthenticated attacker to crash DNS-over-HTTPS (a modern encrypted DNS service) by sending a crafted request. Crashing DNS service disrupts organizations' ability to resolve domain names and access websites. Defenders should update BIND 9 to version 9.20.29 or 9.21.26 and monitor DNS server uptime.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 8. Check Point, Kaspersky, Tanium Patch Product Vulnerabilities
*SecurityWeek* — [read more](https://www.securityweek.com/check-point-kaspersky-tanium-patch-product-vulnerabilities/)

Check Point Security Management and Log Servers have a critical flaw allowing remote code execution with root-level privileges, giving attackers complete control of the firewall management system. This matters because the management server controls all firewall policies and security rules across an organization. Defenders must patch immediately, isolate management servers from untrusted networks, and audit logs for unauthorized access.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.8.2 Privileged access rights

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-20079** | Cisco Firewall Management Center Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 76% | ⚠️ YES (KEV) |
| **CVE-2026-76460** | Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability | 10.0 | 0% | ⚠️ YES (KEV) |
| **CVE-2026-85706** | GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability | – | 12% | ⚠️ YES (KEV) |
| **CVE-2026-19490** | Citrix NetScaler Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 6% | ⚠️ YES (KEV) |
| **CVE-2025-25249** | Fortinet Multiple Products Heap-based Buffer Overflow Vulnerability | – | 2% | ⚠️ YES (KEV) |

**CVE-2026-20079** — CVE-2026-20079 is an authentication bypass flaw in Cisco Firewall Management Center that allows attackers to access the system through an unintended path or method rather than proper login. This is dangerous because the management center controls firewall policies protecting entire networks. Defenders should apply Cisco's patch, enforce multi-factor authentication on management access, and restrict management console access to specific trusted IP addresses.

**CVE-2026-76460** — CVE-2026-76460 is a Cisco ISE API endpoint that doesn't properly verify user identity, allowing unauthenticated attackers to send specially crafted requests and bypass authentication controls. This matters because ISE manages network access for thousands of organizations, so bypassing it grants unauthorized network entry. Defenders must patch immediately, disable unnecessary API endpoints, and add network-level access controls to ISE.

**CVE-2026-85706** — CVE-2026-85706 is a path traversal flaw in GitLab (a code repository and collaboration tool) that allows attackers to read files outside their intended directory by manipulating file paths. This could expose sensitive configuration files, source code, or credentials stored on the GitLab server. Defenders must update GitLab to a patched version and audit logs to see if attackers accessed restricted files.

**CVE-2026-19490** — CVE-2026-19490 is an authentication bypass in Citrix NetScaler (a network access control appliance) that allows attackers to gain access by using an alternate login path instead of the main one. This matters because NetScaler controls who can access corporate resources remotely. Defenders should patch immediately, monitor all access paths for suspicious activity, and enforce strong authentication on all entry points.

**CVE-2025-25249** — CVE-2025-25249 is a heap-based buffer overflow in multiple Fortinet products (a memory safety flaw where data overflows into memory used by other programs). An attacker can exploit this overflow to crash the software or run their own code. Defenders must patch all affected Fortinet products, enable address space layout randomization (ASLR) on servers if available, and monitor for memory corruption errors in logs.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*