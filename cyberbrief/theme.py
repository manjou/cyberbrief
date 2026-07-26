"""Weekday content themes: SOC / GRC / Net+ rotation, Monday-Friday only.

Themes bias ranking toward a focus area without excluding everything else --
a quiet news day for one theme still fills out with the next best overall
stories, so the briefing is never empty.
"""

from __future__ import annotations

from datetime import datetime

THEME_KEYWORDS: dict[str, tuple[str, ...]] = {
    "SOC": (
        "ransomware", "actively exploited", "in the wild", "zero-day", "0-day",
        "backdoor", "botnet", "c2", "command and control", "malware", "trojan",
        "phishing", "apt", "nation-state", "wormable", "rce", "remote code execution",
        "unauthenticated", "incident", "forensic", "ioc", "threat actor", "exploit",
    ),
    "GRC": (
        "breach", "data breach", "privacy", "pii", "gdpr", "compliance", "regulation",
        "regulatory", "fine", "lawsuit", "disclos", "cisa orders", "mandate", "audit",
        "policy", "sec filing", "notification", "settlement", "class action",
    ),
    "Net+": (
        "vpn", "firewall", "router", "switch", "dns", "bgp", "network", "protocol",
        "fortinet", "cisco", "citrix", "vmware", "ivanti", "sd-wan", "load balancer",
        "gateway", "subnet", "vlan", "wan", "checkpoint", "check point", "juniper",
    ),
}

NETWORK_VENDOR_KEYWORDS = (
    "fortinet", "cisco", "citrix", "vmware", "ivanti", "checkpoint", "check point",
    "juniper", "paloalto", "palo alto", "sonicwall", "pulse secure", "f5",
)

# Monday=0 .. Sunday=6 (datetime.weekday()); Sat/Sun intentionally absent -> None
WEEKDAY_THEME: dict[int, str] = {0: "SOC", 1: "GRC", 2: "Net+", 3: "SOC", 4: "GRC"}

THEME_BLURB: dict[str, str] = {
    "SOC": "Today's focus: active exploitation, incident response, and threat activity.",
    "GRC": "Today's focus: breaches, regulation, and compliance impact.",
    "Net+": "Today's focus: network infrastructure — a lighter refresh day.",
}


def theme_for_date(dt: datetime) -> str | None:
    return WEEKDAY_THEME.get(dt.weekday())


def theme_score(text: str, theme: str | None) -> float:
    """Bonus points for matching today's theme keywords. 0 if no theme is active."""
    if not theme:
        return 0.0
    lower = text.lower()
    return 10.0 * sum(1 for kw in THEME_KEYWORDS[theme] if kw in lower)
