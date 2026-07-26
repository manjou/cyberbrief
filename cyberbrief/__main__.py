"""CLI entry point: python -m cyberbrief [--out DIR] [--config feeds.json]"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import explain, fetch, rank, render
from .theme import theme_for_date

CACHE_PATH = Path("cache/latest.json")


def main() -> int:
    parser = argparse.ArgumentParser(prog="cyberbrief", description="Daily security briefing generator")
    parser.add_argument("--config", default="feeds.json", help="path to feeds config")
    parser.add_argument("--out", default="docs", help="output directory")
    parser.add_argument("--no-ai", action="store_true", help="skip AI explanations even if API key is set")
    parser.add_argument(
        "--recap", action="store_true",
        help="regenerate today's page with a condensed 5pm recap section, reusing this morning's "
             "data instead of fetching or calling the AI layer again",
    )
    args = parser.parse_args()

    today_dt = datetime.now(timezone.utc)
    today = today_dt.strftime("%Y-%m-%d")
    theme = theme_for_date(today_dt)

    if args.recap:
        return _recap(args, today)

    config = json.loads(Path(args.config).read_text())

    print("Fetching news feeds...", file=sys.stderr)
    news, errors = fetch.fetch_news(config)
    print(f"  {len(news)} recent items ({len(errors)} feeds failed)", file=sys.stderr)

    print("Fetching CISA KEV + NVD...", file=sys.stderr)
    kev = _safe(fetch.fetch_kev, errors, "CISA KEV")
    nvd = _safe(lambda: fetch.fetch_nvd_recent(config.get("min_cvss", 8.0)), errors, "NVD")

    stories = rank.rank_news(news, config.get("top_stories", 8), theme=theme)

    cve_ids = sorted({v["cve"] for v in kev + nvd})
    epss = fetch.fetch_epss(cve_ids) if cve_ids else {}
    cves = rank.rank_cves(kev, nvd, epss, config.get("top_cves", 5), theme=theme)
    print(f"  {len(stories)} stories, {len(cves)} CVEs selected" + (f" (theme: {theme})" if theme else ""), file=sys.stderr)

    if not args.no_ai:
        explanations, ai_error = explain.explain_items(stories + cves)
        for idx, text in explanations.items():
            (stories + cves)[idx]["explanation"] = text
        if explanations:
            print(f"  AI explanations added for {len(explanations)} items", file=sys.stderr)
        elif ai_error:
            errors.append(f"AI explanations ({ai_error})")
            print(f"  AI explanations failed: {ai_error}", file=sys.stderr)

    _write_outputs(Path(args.out), today, stories, cves, errors, theme, recap=False)

    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(
        {"date": today, "theme": theme, "stories": stories, "cves": cves, "errors": errors}, default=str
    ))

    return 0


def _recap(args: argparse.Namespace, today: str) -> int:
    if not CACHE_PATH.exists():
        print(f"No cached data at {CACHE_PATH} -- run the morning briefing first.", file=sys.stderr)
        return 1
    cached = json.loads(CACHE_PATH.read_text())
    if cached.get("date") != today:
        print(f"Cached data is from {cached.get('date')}, not today ({today}) -- skipping recap.", file=sys.stderr)
        return 1

    _write_outputs(
        Path(args.out), today, cached["stories"], cached["cves"], cached["errors"], cached.get("theme"), recap=True
    )
    print(f"Recap written to {args.out}/index.html and {args.out}/briefing.md", file=sys.stderr)
    return 0


def _write_outputs(
    out: Path, today: str, stories: list[dict], cves: list[dict], errors: list[str],
    theme: str | None, recap: bool,
) -> None:
    (out / "archive").mkdir(parents=True, exist_ok=True)

    html_page = render.to_html(stories, cves, errors, theme=theme, recap=recap)
    (out / "index.html").write_text(html_page)
    (out / "archive" / f"{today}.html").write_text(html_page)
    (out / "briefing.md").write_text(render.to_markdown(stories, cves, errors, theme=theme, recap=recap))
    _write_archive_index(out / "archive")

    print(f"Briefing written to {out}/index.html and {out}/briefing.md", file=sys.stderr)


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
