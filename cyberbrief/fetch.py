"""Fetch security news feeds, CISA KEV, NVD CVEs and EPSS scores.

Pure stdlib: urllib + xml.etree. Every source failure is non-fatal —
a briefing built from the sources that answered beats no briefing.
"""

from __future__ import annotations

import gzip
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

USER_AGENT = "CyberBrief/1.0 (+https://github.com/manjou/cyberbrief)"
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
EPSS_URL = "https://api.first.org/data/v1/epss"

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)


def http_get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
        return data


def _text(elem, *tags) -> str:
    for tag in tags:
        found = elem.find(tag)
        if found is not None and found.text:
            return found.text.strip()
    return ""


def _strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&(#\d+|\w+);", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _parse_date(raw: str):
    if not raw:
        return None
    try:
        return parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        pass
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


ATOM = "{http://www.w3.org/2005/Atom}"


def parse_feed(xml_bytes: bytes, source: str, weight: float) -> list[dict]:
    """Parse RSS 2.0 or Atom into normalized item dicts."""
    root = ET.fromstring(xml_bytes)
    items = []
    for node in root.iter("item"):  # RSS 2.0
        items.append({
            "source": source,
            "weight": weight,
            "title": _text(node, "title"),
            "link": _text(node, "link"),
            "summary": _strip_html(_text(node, "description"))[:500],
            "published": _parse_date(_text(node, "pubDate", "{http://purl.org/dc/elements/1.1/}date")),
        })
    for node in root.iter(f"{ATOM}entry"):  # Atom
        link = ""
        link_el = node.find(f"{ATOM}link")
        if link_el is not None:
            link = link_el.get("href", "")
        items.append({
            "source": source,
            "weight": weight,
            "title": _text(node, f"{ATOM}title"),
            "link": link,
            "summary": _strip_html(_text(node, f"{ATOM}summary", f"{ATOM}content"))[:500],
            "published": _parse_date(_text(node, f"{ATOM}updated", f"{ATOM}published")),
        })
    return items


def fetch_news(config: dict) -> tuple[list[dict], list[str]]:
    """Fetch all configured feeds. Returns (recent items, error notes)."""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=config.get("max_age_hours", 36))
    items, errors = [], []
    for feed in config["news_feeds"]:
        try:
            parsed = parse_feed(http_get(feed["url"]), feed["name"], feed.get("weight", 1.0))
            fresh = [i for i in parsed if i["published"] and i["published"] >= cutoff]
            items.extend(fresh)
        except Exception as exc:  # noqa: BLE001 - any single feed may be down
            errors.append(f"{feed['name']}: {type(exc).__name__}")
    return items, errors


def fetch_kev(days: int = 14) -> list[dict]:
    """CVEs recently added to CISA's Known Exploited Vulnerabilities catalog."""
    data = json.loads(http_get(KEV_URL))
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()
    return [
        {
            "cve": v["cveID"],
            "name": v.get("vulnerabilityName", ""),
            "vendor": v.get("vendorProject", ""),
            "product": v.get("product", ""),
            "date_added": v.get("dateAdded", ""),
            "action": v.get("requiredAction", ""),
            "ransomware": v.get("knownRansomwareCampaignUse", "") == "Known",
            "kev": True,
        }
        for v in data.get("vulnerabilities", [])
        if v.get("dateAdded", "") >= cutoff
    ]


def fetch_nvd_recent(min_cvss: float = 8.0, hours: int = 48) -> list[dict]:
    """Recently published high-severity CVEs from NVD."""
    now = datetime.now(timezone.utc)
    start = (now - timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%S.000")
    end = now.strftime("%Y-%m-%dT%H:%M:%S.000")
    raw = json.loads(http_get(f"{NVD_URL}?pubStartDate={start}&pubEndDate={end}", timeout=60))
    out = []
    for entry in raw.get("vulnerabilities", []):
        cve = entry.get("cve", {})
        score, severity = 0.0, ""
        for metrics in cve.get("metrics", {}).values():
            for m in metrics:
                cvss = m.get("cvssData", {})
                if cvss.get("baseScore", 0) > score:
                    score = cvss["baseScore"]
                    severity = cvss.get("baseSeverity", "")
        if score < min_cvss:
            continue
        desc = next((d["value"] for d in cve.get("descriptions", []) if d.get("lang") == "en"), "")
        out.append({
            "cve": cve.get("id", ""),
            "cvss": score,
            "severity": severity,
            "description": desc[:400],
            "kev": False,
        })
    return out


def fetch_epss(cve_ids: list[str]) -> dict[str, float]:
    """EPSS exploitation-probability scores (0..1) for a list of CVE ids."""
    scores: dict[str, float] = {}
    for i in range(0, len(cve_ids), 50):
        batch = ",".join(cve_ids[i:i + 50])
        try:
            data = json.loads(http_get(f"{EPSS_URL}?cve={batch}"))
            for row in data.get("data", []):
                scores[row["cve"]] = float(row.get("epss", 0.0))
        except Exception:  # noqa: BLE001
            continue
    return scores


def cves_in_text(*texts: str) -> list[str]:
    found: list[str] = []
    for t in texts:
        for m in CVE_RE.findall(t or ""):
            m = m.upper()
            if m not in found:
                found.append(m)
    return found
