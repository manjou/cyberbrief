"""Map stories to ISO/IEC 27001:2022 Annex A controls and explain jargon.

Keyword-driven on purpose: transparent, free, and good enough to turn every
news item into a small compliance-thinking exercise.
"""

from __future__ import annotations

# keyword -> (control id, control name)
ISO_MAP = [
    (("ransomware", "backup", "wiper"), ("A.8.13", "Information backup")),
    (("malware", "trojan", "botnet", "infostealer", "backdoor"), ("A.8.7", "Protection against malware")),
    (("phishing", "social engineering", "smishing", "vishing"), ("A.6.3", "Awareness, education and training")),
    (("patch", "vulnerability", "cve-", "exploit", "zero-day", "0-day", "rce"), ("A.8.8", "Management of technical vulnerabilities")),
    (("supply chain", "third-party", "vendor", "dependency", "npm", "pypi"), ("A.5.19", "Supplier relationships")),
    (("data breach", "leak", "exposed", "stolen data", "exfiltrat"), ("A.5.34", "Privacy and protection of PII")),
    (("ddos", "denial of service", "outage", "availability"), ("A.8.6", "Capacity management")),
    (("cloud", "aws", "azure", "gcp", "s3 bucket", "saas"), ("A.5.23", "Cloud services security")),
    (("credential", "password", "mfa", "2fa", "authentication", "token"), ("A.5.17", "Authentication information")),
    (("insider", "employee", "privilege"), ("A.8.2", "Privileged access rights")),
    (("incident", "response", "forensic"), ("A.5.24", "Incident management planning")),
    (("vpn", "firewall", "router", "network device", "gateway"), ("A.8.20", "Networks security")),
    (("encryption", "cryptograph", "certificate", "tls"), ("A.8.24", "Use of cryptography")),
]

GLOSSARY = {
    "KEV": "CISA's Known Exploited Vulnerabilities catalog — CVEs confirmed to be abused by attackers in the real world. If it's in KEV, patching it jumps to the top of the list.",
    "EPSS": "Exploit Prediction Scoring System — a 0-100% probability that a CVE will be exploited in the next 30 days. Better prioritization signal than CVSS alone.",
    "CVSS": "Common Vulnerability Scoring System — rates how bad a vulnerability *could* be (0-10). High CVSS does not mean anyone is actually exploiting it.",
    "CVE": "Common Vulnerabilities and Exposures — the global ID system for security flaws, e.g. CVE-2026-12345.",
    "RCE": "Remote Code Execution — the worst-case flaw: an attacker runs their own code on your system over the network.",
    "zero-day": "A vulnerability attackers exploit before the vendor has released a patch — defenders start at zero days of warning.",
    "ransomware": "Malware that encrypts your files and demands payment. Modern gangs also steal data first and threaten to publish it (double extortion).",
}


def map_controls(text: str, max_controls: int = 2) -> list[tuple[str, str]]:
    lower = text.lower()
    hits = []
    for keywords, control in ISO_MAP:
        if any(kw in lower for kw in keywords) and control not in hits:
            hits.append(control)
    return hits[:max_controls]
