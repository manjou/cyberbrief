"""Rank news items and CVEs by real-world urgency — no AI required.

Scoring signals, in order of trust:
  1. CISA KEV membership  — the CVE is being exploited in the wild right now
  2. EPSS score           — predicted probability of exploitation in the next 30 days
  3. CVSS base score      — theoretical severity
  4. Impact keywords      — ransomware, zero-day, supply chain, ...
  5. Source weight + recency
"""

from __future__ import annotations

from datetime import datetime, timezone

KEYWORD_SCORES = {
    "zero-day": 30, "0-day": 30, "actively exploited": 30, "in the wild": 25,
    "ransomware": 25, "supply chain": 22, "backdoor": 20, "critical": 15,
    "data breach": 18, "breach": 12, "rce": 18, "remote code execution": 18,
    "patch now": 20, "emergency": 18, "unauthenticated": 15, "wormable": 25,
    "botnet": 12, "phishing": 8, "apt": 12, "nation-state": 12, "cisa": 10,
    "vpn": 10, "firewall": 10, "microsoft": 8, "exchange": 10, "vmware": 10,
    "citrix": 10, "fortinet": 12, "ivanti": 12, "leak": 10, "stolen": 10,
}

DEDUP_STOPWORDS = frozenset(
    "the a an of to in on for with and or new says after over from by is are "
    "hackers hacker attack attacks security cyber".split()
)


def _keyword_score(text: str) -> int:
    lower = text.lower()
    return sum(pts for kw, pts in KEYWORD_SCORES.items() if kw in lower)


def _title_tokens(title: str) -> frozenset[str]:
    words = [w.strip(".,:;!?'\"()").lower() for w in title.split()]
    return frozenset(w for w in words if len(w) > 3 and w not in DEDUP_STOPWORDS)


def dedupe(items: list[dict]) -> list[dict]:
    """Drop stories whose titles overlap heavily with an already-kept one."""
    kept: list[tuple[frozenset, dict]] = []
    for item in items:
        tokens = _title_tokens(item["title"])
        duplicate = False
        for seen_tokens, _ in kept:
            union = tokens | seen_tokens
            if union and len(tokens & seen_tokens) / len(union) > 0.5:
                duplicate = True
                break
        if not duplicate:
            kept.append((tokens, item))
    return [item for _, item in kept]


def rank_news(items: list[dict], top_n: int = 8) -> list[dict]:
    now = datetime.now(timezone.utc)
    for item in items:
        text = f"{item['title']} {item['summary']}"
        score = _keyword_score(text) * item.get("weight", 1.0)
        age_h = (now - item["published"]).total_seconds() / 3600 if item.get("published") else 36
        score += max(0.0, 12 - age_h / 3)  # freshness bonus, fades over ~36h
        item["score"] = round(score, 1)
    ranked = sorted(items, key=lambda i: i["score"], reverse=True)
    return dedupe(ranked)[:top_n]


def rank_cves(kev: list[dict], nvd: list[dict], epss: dict[str, float], top_n: int = 5) -> list[dict]:
    merged: dict[str, dict] = {}
    for v in nvd:
        merged[v["cve"]] = v
    for v in kev:  # KEV wins on collision, keep NVD details if present
        merged[v["cve"]] = {**merged.get(v["cve"], {}), **v}

    for v in merged.values():
        v["epss"] = epss.get(v["cve"], 0.0)
        score = 0.0
        if v.get("kev"):
            score += 50
        if v.get("ransomware"):
            score += 20
        score += v["epss"] * 40
        score += v.get("cvss", 0.0) * 2
        v["score"] = round(score, 1)

    return sorted(merged.values(), key=lambda v: v["score"], reverse=True)[:top_n]
