# 🛡️ CyberBrief — Monday, 13 July 2026

*Your daily security briefing, ranked by real-world urgency (KEV → EPSS → CVSS), explained for humans.*

## 🔥 Top stories

### 1. iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days
*The Hacker News* — [read more](https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added two maximum-severity security flaws impacting iCagenda and Balbooa extensions for Joomla to its Known Exploited Vulnerabilities (KEV) catalog, following reports of zero-day exploitation in the wild. The vulnerabilities, both rated 10.0 on the CVSS scoring system, are below - CVE-2026-48939 - A vulnerability in the

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities, A.5.23 Cloud services security

### 2. Centers Laboratory Data Breach Affects 540,000 Individuals
*SecurityWeek* — [read more](https://www.securityweek.com/centers-laboratory-data-breach-affects-540000-individuals/)

The WorldLeaks extortion group claimed to have stolen 720 GB of data from the healthcare testing and laboratory services provider. The post Centers Laboratory Data Breach Affects 540,000 Individuals appeared first on SecurityWeek .

> 📋 **ISO 27001:** A.5.34 Privacy and protection of PII

### 3. Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365
*The Hacker News* — [read more](https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html)

An attacker running a live Microsoft 365 phishing operation left a Python web server listening on a public port with directory listing switched on. The command that did it: python3 -m http.server 8080, was still sitting in the readable .bash_history. From that one lapse, French security firm Lexfo lifted the operator's entire toolkit and pivoted through it to two more

> 📋 **ISO 27001:** A.6.3 Awareness, education and training

### 4. [UPDATE] [hoch] Drupal AlternativeCommerce (Basket): Schwachstelle ermöglicht Codeausführung
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1702)

Ein entfernter, anonymer Angreifer kann eine Schwachstelle im Drupal-Modul "AlternativeCommerce" (Basket) ausnutzen, um beliebigen Programmcode auszuführen.

> 📋 **ISO 27001:** A.8.8 Management of technical vulnerabilities

### 5. Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns
*SecurityWeek* — [read more](https://www.securityweek.com/progress-prompts-sharefile-storage-zone-controller-shutdown-amid-security-concerns/)

The company notified customers to manually shut down their servers while it is investigating a credible threat. The post Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns appeared first on SecurityWeek .

### 6. [UPDATE] [mittel] OpenSSL: Mehrere Schwachstellen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0995)

Ein Angreifer kann mehrere Schwachstellen in OpenSSL ausnutzen, um einen Denial of Service Angriff durchzuführen, vertrauliche Informationen offenzulegen oder andere, nicht näher spezifizierte Angriffe durchzuführen.

> 📋 **ISO 27001:** A.8.6 Capacity management

### 7. [UPDATE] [mittel] X.Org X11: Mehrere Schwachstellen ermöglichen nicht näher spezifizierte Auswirkungen, möglicherweise Codeausführung
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2025-0435)

Ein lokaler Angreifer kann mehrere Schwachstellen in X.Org X11 ausnutzen, um nicht spezifizierte Effekte zu verursachen, was möglicherweise zur Ausführung von beliebigem Code führt.

### 8. [UPDATE] [mittel] Golang Go: Mehrere Schwachstellen ermöglichen Offenlegung von Informationen
*CERT-Bund (DE)* — [read more](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2239)

Ein Angreifer kann mehrere Schwachstellen in Golang Go ausnutzen, um Informationen offenzulegen.

## 🚨 CVEs that matter today

| CVE | Why it ranks | CVSS | EPSS | Exploited? |
|-----|--------------|------|------|------------|
| **CVE-2026-48282** | Adobe ColdFusion Path Traversal Vulnerability | – | 29% | ⚠️ YES (KEV) |
| **CVE-2026-45659** | Microsoft SharePoint Server Deserialization of Untrusted Data Vulnerability | – | 3% | ⚠️ YES (KEV) |
| **CVE-2026-56290** | Joomlack Page Builder Improper Access Control Vulnerability | – | 3% | ⚠️ YES (KEV) |
| **CVE-2026-48939** | iCagenda Unrestricted Upload of File with Dangerous Type Vulnerability | – | 2% | ⚠️ YES (KEV) |
| **CVE-2026-48908** | JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability | – | 2% | ⚠️ YES (KEV) |

## 📖 Jargon decoder

- **KEV** — CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.
- **CVSS** — Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.
- **CVE** — Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.
- **RCE** — Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.
- **zero-day** — A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.
- **EPSS** — Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.

---
*Generated by [CyberBrief](https://github.com/manjou/cyberbrief) — free, open source, no AI required.*