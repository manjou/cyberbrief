# 🛡️ CyberBrief — Net+ — Wednesday, 18 November 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: network infrastructure — a lighter refresh day.*

## 🔥 Top stories

### 1. Oracle to Patch 11 Java Flaws Today as Critical OpenJDK RCE (CVE-2026-114938) Report Emerges
*The Hacker News* — [read more](https://thehackernews.com/2026/11/oracle-to-patch-11-java-flaws-today-as.html)

Oracle is preparing to release security patches for 11 vulnerabilities in Java SE on Tuesday, November 17, 2026, all of which may be exploited remotely without authentication, as separate reports warn of a potentially critical remote code execution (RCE) flaw affecting OpenJDK. The 11 vulnerabilities carry a maximum CVSS 3.1 severity score of 8.1, according to Oracle's advance security notice.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Critical Java4Shell flaw allows RCE attacks on major Java applications
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/critical-java4shell-flaw-allows-rce-attacks-on-major-java-applications/)

A critical vulnerability dubbed Java4Shell in OpenJDK, the open-source implementation of Java, can allow unauthenticated attackers to remotely execute code on popular enterprise applications, including Jenkins, Atlassian Jira, Confluence, and Keycloak.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 3. Hackers Exploiting Critical Puppet RCE Flaw Affecting Enterprise Management Servers
*The Hacker News* — [read more](https://thehackernews.com/2026/11/hackers-exploiting-critical-puppet-rce.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a critical security flaw impacting Perforce Puppet, an enterprise infrastructure-as-code (IaC) and configuration management platform, to its Known Exploited Vulnerabilities (KEV) catalog, citing reports of active exploitation. The vulnerability, tracked as CVE-2026-115731 (CVSS score: 9.4), is a case of

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 4. CISA Urges Immediate Patching of Java4Shell Flaw That Could Allow Remote Code Execution
*The Hacker News* — [read more](https://thehackernews.com/2026/11/cisa-urges-immediate-patching-of.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has urged organizations to immediately patch a newly disclosed critical security flaw impacting Oracle Java. The flaw, tracked as CVE-2026-114938 (CVSS score: 8.1), refers to a case of out-of-bounds write that can lead to denial-of-service (DoS) or remote code execution under certain conditions. "This critical memory-corruption

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Apache warns of Roller RCE vulnerability exploited in attacks
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/apache-warns-of-roller-rce-vulnerability-exploited-in-attacks/)

Apache has released security updates to address a critical Roller flaw that threat actors are exploiting to gain code execution on vulnerable servers.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 6. Hackers Found a Way Around GitHub SHA Pinning. This Webinar Explains How to Close the Gap
*The Hacker News* — [read more](https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html)

Pinning GitHub Actions to an exact version of their code, known as SHA pinning, has become the go-to defense against software supply chain attacks. Attackers have already found a way around it. In March 2026, the hackers who hijacked Trivy, a widely used open-source security scanner, planted malicious code that looked like it came from GitHub's official checkout tool. They even labeled it a

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.19 Supplier relationships

### 7. Russian APT Poses as Employee of Hacked Firm to Breach Another US Organization
*SecurityWeek* — [read more](https://www.securityweek.com/russian-apt-poses-as-employee-of-hacked-firm-to-breach-another-us-organization/)

Star Blizzard weaponized data and identities stolen in late 2025 to phish and compromise a US organization.

> 📋 **ISO 27001:** A.8.2 Privileged access rights

### 8. Java4Shell Vulnerability Puts Many Enterprise Applications at Risk of Takeover
*SecurityWeek* — [read more](https://www.securityweek.com/java4shell-vulnerability-puts-many-enterprise-applications-at-risk-of-takeover/)

Calif demonstrated remote code execution in Jira, Jenkins and Keycloak, while VulnCheck says real-world RCE requires per-target work

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-123039** | Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability | – | 2% | ⚠️ YES (KEV) |
| **CVE-2026-20320** | Cisco BroadWorks Improper Restriction of XML External Entity Reference Vulnerability | – | 1% | ⚠️ YES (KEV) |
| **CVE-2026-19868** | SonicWall SonicOS SSLVPN Use of Single-factor Authentication Vulnerability | – | 1% | ⚠️ YES (KEV) |
| **CVE-2026-123158** | OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability | – | 19% | ⚠️ YES (KEV) |
| **CVE-2026-116606** | Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability | – | 11% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

<sub>Sources unavailable this run: AI explanations (HTTPError)</sub>

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*