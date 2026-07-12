"""Optional AI layer: beginner-friendly explanations via the Claude API.

Runs only when ANTHROPIC_API_KEY is set; the briefing works fine without it.
One batched request per run on claude-haiku-4-5 keeps the cost around a cent.
"""

from __future__ import annotations

import json
import os
import urllib.request

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = os.environ.get("CYBERBRIEF_MODEL", "claude-haiku-4-5-20251001")

PROMPT = """You are writing for a beginner in cybersecurity (junior GRC analyst).
For EACH numbered item below, write 2-3 plain-English sentences covering:
what happened, why it matters, and what defenders typically do about it.
No hype, no jargon without a short inline explanation.

Return ONLY a JSON object mapping item number (string) to explanation. Items:

{items}"""


def explain_items(items: list[dict]) -> dict[int, str]:
    """Returns {index: explanation}. Empty dict if no API key or on any failure."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key or not items:
        return {}

    numbered = "\n".join(
        f"{i + 1}. {it.get('title') or it.get('cve', '')}: "
        f"{(it.get('summary') or it.get('description') or it.get('name', ''))[:300]}"
        for i, it in enumerate(items)
    )
    body = json.dumps({
        "model": MODEL,
        "max_tokens": 2000,
        "messages": [{"role": "user", "content": PROMPT.format(items=numbered)}],
    }).encode()
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            text = json.loads(resp.read())["content"][0]["text"]
        start, end = text.find("{"), text.rfind("}") + 1
        parsed = json.loads(text[start:end])
        return {int(k) - 1: v for k, v in parsed.items()}
    except Exception:  # noqa: BLE001 - AI layer is strictly optional
        return {}
