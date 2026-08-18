# 🛡️ CyberBrief — GRC — Tuesday, 18 August 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

*Today's focus: breaches, regulation, and compliance impact.*

## 🔥 Top stories

### 1. Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads
*The Hacker News* — [read more](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)

A WordPress plugin called Forminator, used by over 600,000 websites, has a critical flaw that lets attackers upload and run malicious code without logging in first. This matters because attackers can take complete control of affected websites to steal data, inject malware, or use the site for further attacks. Defenders should immediately update the plugin to the patched version, disable it if a patch isn't available, and check their servers for signs of unauthorized code execution or file uploads.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 2. French tax authority data breach affects 678,000 individuals
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/french-tax-authority-data-breach-affects-678-000-individuals/)

Attackers gained unauthorized access to French tax authority systems and stole personal information belonging to 678,000 people, likely including tax records and identification details. This matters because exposed personal data can be used for identity theft, fraud, or sold on criminal marketplaces, and tax records are particularly sensitive. Defenders and the affected organization should notify impacted individuals, monitor for fraudulent activity, reset compromised credentials, and investigate how attackers gained initial access.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 3. SafePal data breach impacts 39,798 customers, stolen info for sale
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/safepal-data-breach-impacts-39-798-customers-stolen-info-for-sale/)

A vulnerability in SafePal's cryptocurrency wallet service was exploited to steal customer order and personal information from about 39,798 users, and criminals are now selling this data. This matters because stolen customer data can be used for targeted fraud, phishing attacks, or identity theft, and the public sale of data increases the risk of misuse. Defenders should patch the vulnerable function, notify customers to change passwords, monitor for fraudulent transactions, and track where the stolen data is being distributed.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

### 4. Pokémon Center data breach exposes customer info, cancels some orders
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/pokemon-center-data-breach-exposes-customer-info-cancels-some-orders/)

Pokémon Center customer data was stolen by hackers who compromised a third-party logistics company (CEVA Logistics) that handles their shipments. This matters because customer names, addresses, order history, and contact information can be used for targeted fraud or phishing attacks against Pokémon fans. Defenders should verify all systems used by third-party vendors, require stronger security controls from partners, and monitor customer accounts for suspicious activity.

> 📋 **ISO 27001:** A.5.19 Supplier relationships, A.5.34 Privacy and protection of PII

### 5. 680,000 Impacted by French Tax Authority Data Breach
*SecurityWeek* — [read more](https://www.securityweek.com/680000-impacted-by-french-tax-authority-data-breach/)

Hackers obtained stolen usernames and passwords (compromised credentials) and used them to break into French tax authority systems to access both business and personal tax records. This matters because it shows attackers often exploit weak password practices and reused credentials to breach even large government organizations. Defenders should enforce multi-factor authentication (requiring a second verification step beyond passwords), monitor for suspicious login activity, and require employees to use strong unique passwords.

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII, A.5.17 Authentication information

### 6. Microsoft working on Defender patch for ShieldBreak zero-day
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/)

Microsoft is developing a security fix for a previously unknown vulnerability (zero-day) in Windows Defender called ShieldBreak that was publicly revealed by a security researcher. This matters because the vulnerability is currently unpatched, leaving all affected Microsoft Defender users at risk until the patch is released. Defenders should watch for the patch release, apply it immediately when available, and use alternate security tools if they cannot patch quickly.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 7. Philips and GE investigating Clop ransomware data theft claims
*BleepingComputer* — [read more](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)

Major technology companies GE and Philips are investigating whether the Clop ransomware group broke into their systems and stole confidential data. This matters because ransomware gangs typically steal data before encrypting it, meaning they can demand payment either to decrypt files or to keep stolen information secret. Defenders should check logs for unauthorized access, verify data integrity, and prepare for possible extortion demands or data ransom negotiations.

> 📋 **ISO 27001:** A.8.13 Information backup

### 8. 40,000 Impacted by SafePal Data Breach
*SecurityWeek* — [read more](https://www.securityweek.com/40000-impacted-by-safepal-data-breach/)

Hackers exploited a flaw in SafePal's order-tracking feature to access the personal and order information of approximately 40,000 customers. This matters because exposed order data can reveal purchase patterns, shipping addresses, and personal preferences that enable targeted fraud or future attacks. Defenders should fix the vulnerable tracking function, audit what data was accessed, notify affected customers, and implement input validation (checking that user input is safe before processing it).

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.34 Privacy and protection of PII

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-8037** | Progress LoadMaster Command Injection Vulnerability | – | 99% | ⚠️ YES (KEV) |
| **CVE-2026-34486** | Apache Tomcat Missing Encryption of Sensitive Data Vulnerability | – | 83% | ⚠️ YES (KEV) |
| **CVE-2026-9198** | IBM Langflow Code Injection Vulnerability | – | 17% | ⚠️ YES (KEV) |
| **CVE-2026-63077** | JetBrains TeamCity Deserialization of Untrusted Data Vulnerability | – | 11% | ⚠️ YES (KEV) |
| **CVE-2026-72898** | Metabase SQL Injection Vulnerability | – | 10% | ⚠️ YES (KEV) |

**CVE-2026-8037** — A vulnerability in Progress LoadMaster (a load-balancing appliance) allows attackers to inject and execute arbitrary commands on the device by exploiting improper input handling. This matters because compromised load balancers can intercept or redirect all traffic flowing through them, potentially affecting thousands of downstream users and systems. Defenders should patch LoadMaster immediately, restrict administrative access, monitor for suspicious commands being executed, and check device logs for signs of exploitation.

**CVE-2026-34486** — Apache Tomcat (a web application server) has a flaw where sensitive data such as passwords or API keys are stored without encryption in memory or on disk. This matters because if an attacker gains access to the server's files or memory, they can easily read unencrypted secrets and use them to compromise other systems. Defenders should update Tomcat, use external secret management tools to store sensitive data, and enable encryption for data at rest (stored data).

**CVE-2026-9198** — IBM Langflow (a tool for building AI applications) has a code injection vulnerability that allows attackers to execute arbitrary code by inserting malicious input into the application. This matters because attackers can gain full control of servers running Langflow and use them to steal data, deploy malware, or attack connected systems. Defenders should patch Langflow, validate all user inputs before processing them, and run the application with minimal permissions (principle of least privilege).

**CVE-2026-63077** — JetBrains TeamCity (a continuous integration tool) has a flaw in how it handles untrusted data that deserializes (converts serialized data back into executable code) without proper verification. This matters because attackers can craft malicious serialized data that executes arbitrary code when TeamCity processes it. Defenders should patch TeamCity immediately, restrict network access to it, monitor for unusual build job execution, and never accept serialized data from untrusted sources.

**CVE-2026-72898** — Metabase (a business analytics tool) has a SQL injection vulnerability that allows attackers to manipulate database queries by inserting malicious SQL code into user inputs. This matters because attackers can bypass authentication, read sensitive business data, modify or delete records, or escalate their privileges. Defenders should patch Metabase, use parameterized queries (safe SQL statements that separate code from data), and restrict database permissions to only what's necessary.

## 📖 Jargon decoder

- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **ransomware** — Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).
- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*