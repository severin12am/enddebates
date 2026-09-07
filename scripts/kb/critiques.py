# -*- coding: utf-8 -*-
"""Christian critiques of Islam — migrated Topic 01."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def topic() -> dict:
    path = ROOT / "data" / "christian-critiques-of-islam.json"
    raw = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"arguments": []}

    arguments = []
    for a in raw.get("arguments", []):
        arg = {
            "id": a["id"],
            "rank": a.get("rank"),
            "cluster": a.get("type") or "Critique",
            "title": a["title"],
            "type": a.get("type"),
            "popularity": a.get("popularity"),
            "christian": {
                "claim": a["christian"]["claim"],
                "case": a["christian"]["case"],
                "sources": a["christian"].get("receipts") or a["christian"].get("sources") or [],
            },
            "muslim": {
                "claim": a["response"]["claim"],
                "case": a["response"]["case"],
                "sources": a["response"].get("receipts") or a["response"].get("sources") or [],
            },
            "counter_to_christian": "See Muslim case and crux.",
            "counter_to_muslim": "See Christian case and crux.",
            "crux": a.get("crux", ""),
            "debate_use": "Steelman the critique, then the response; name the crux aloud.",
        }
        arguments.append(arg)

    from .deepen_lib import apply_overlays
    from .critiques_deep import OVERLAYS

    t = raw.get("topic", {})
    built = {
        "id": "critiques",
        "meta": {
            "title": t.get("title") or "Christian critiques of Islam",
            "thesis": t.get("thesis")
            or "Do the most common Christian arguments against Islam withstand the strongest documented counters?",
            "purpose": t.get("scope")
            or "Mapped popular Christian critiques with documented Muslim/academic responses.",
            "warning": "Steelmans both sides. No declared winner.",
            "chips": ["Topic 01", "Apologetics map", "Receipts"],
            "labels": {"christian": "Christian critique", "muslim": "Documented response"},
        },
        "definitions": [
            {
                "term": "Steelman",
                "precise": "State the other side's argument in its strongest form before answering.",
                "not": "Not strawman or slogan swap.",
            },
            {
                "term": "Crux",
                "precise": "The specific question that would actually resolve a disagreement fork.",
                "not": "Not the loudest talking point.",
            },
        ],
        "arguments": arguments,
        "materials": [],
        "debates": [],
        "opponent_cards": [
            {
                "trigger": "Islam denies the crucifixion so it's false",
                "fast_answer": "State the historical consensus, then ask whether 4:157 denies the event or the boast — and cite Lawson/AJIS diversity.",
                "follow_up": "Don't pretend Muslim views are monolithic.",
                "sources": ["Qur'an 4:157", "Ehrman", "Lawson"],
            },
            {
                "trigger": "The Qur'an confirms the Bible so Islam collapses",
                "fast_answer": "Define Injil. Use Saeed/Ally: guidance therein ≠ wholesale Nicene endorsement.",
                "follow_up": "Then fight crucifixion/deity as separate historical questions.",
                "sources": ["Q 5:47", "Saeed", "Ally"],
            },
        ],
        "checklist": t.get("method")
        or [
            "Name the critique precisely",
            "Steelman the response",
            "Cite one primary text each side",
            "State the crux",
        ],
        "positive_cases": {
            "Christian podium": ["Use historical consensus carefully", "Force method symmetry", "Define terms"],
            "Muslim podium": ["Show internal diversity", "Use academic Muslim sources", "Separate slogan from fiqh"],
            "Unity / steelman": ["Map forks not tribes", "Share receipts", "Name cruxes"],
        },
        "bibliography": [
            {
                "tier": "Start here",
                "items": [
                    {"label": "Topic data JSON", "url": "../data/christian-critiques-of-islam.json"},
                    {"label": "Qur'an.com", "url": "https://quran.com"},
                ],
            }
        ],
    }
    return apply_overlays(built, OVERLAYS)
