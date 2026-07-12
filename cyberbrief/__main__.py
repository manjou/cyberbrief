"""CLI entry point: python -m cyberbrief [--out DIR] [--config feeds.json]"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import explain, fetch, rank, render


def main() -> int:
    parser = argparse.ArgumentParser(prog="cyberbrief", description="Daily security briefing generator")
    parser.add_argument("--config", default="feeds.json", help="path to feeds config")
    parser.add_argument("--out", default="docs", help="output directory")
    parser.add_argument("--no-ai", action="store_true", help="skip AI explanations even if API key is set")
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text())

    print("Fetching news feeds...", file=sys.stderr)
    news, errors = fetch.fetch_news(config)
    print(f"  {len(news)} recent items ({len(errors)} feeds failed)", file=sys.stderr)

    print("Fetching CISA KEV + NVD...", file=sys.stderr)
    kev = _safe(fetch.fetch_kev, errors, "CISA KEV")
    nvd = _safe(lambda: fetch.fetch_nvd_recent(config.get("min_cvss", 8.0)), errors, "NVD")

    stories = rank.rank_news(news, config.get("top_stories", 8))

    cve_ids = sorted({v["cve"] for v in kev + nvd})
    epss = fetch.fetch_epss(cve_ids) if cve_ids else {}
    cves = rank.rank_cves(kev, nvd, epss, config.get("top_cves", 5))
    print(f"  {len(stories)} stories, {len(cves)} CVEs selected", file=sys.stderr)

    if not args.no_ai:
        explanations = explain.explain_items(stories + cves)
        for idx, text in explanations.items():
            (stories + cves)[idx]["explanation"] = text
        if explanations:
            print(f"  AI explanations added for {len(explanations)} items", file=sys.stderr)

    out = Path(args.out)
    (out / "archive").mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    html_page = render.to_html(stories, cves, errors)
    (out / "index.html").write_text(html_page)
    (out / "archive" / f"{today}.html").write_text(html_page)
    (out / "briefing.md").write_text(render.to_markdown(stories, cves, errors))
    _write_archive_index(out / "archive")

    print(f"Briefing written to {out}/index.html and {out}/briefing.md", file=sys.stderr)
    return 0


def _safe(fn, errors: list[str], label: str):
    try:
        return fn()
    except Exception as exc:  # noqa: BLE001 - source outages must not kill the run
        errors.append(f"{label}: {type(exc).__name__}")
        return []


def _write_archive_index(archive_dir: Path) -> None:
    days = sorted((p.stem for p in archive_dir.glob("????-??-??.html")), reverse=True)
    links = "".join(f"<li><a href='{d}.html'>{d}</a></li>" for d in days)
    archive_dir.joinpath("index.html").write_text(
        "<!doctype html><meta charset='utf-8'><title>CyberBrief archive</title>"
        f"<body style='font-family:sans-serif;max-width:640px;margin:2rem auto'><h1>Archive</h1><ul>{links}</ul>"
    )


if __name__ == "__main__":
    sys.exit(main())
