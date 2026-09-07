# -*- coding: utf-8 -*-
"""Merge deep overlays onto topic argument cards."""
from __future__ import annotations

import copy
from typing import Any


def Q(
    text: str,
    who: str,
    work: str,
    url: str | None = None,
    gloss: str | None = None,
    orig: str | None = None,
) -> dict:
    d = {"text": text, "who": who, "work": work}
    if url:
        d["url"] = url
    if gloss:
        d["gloss"] = gloss
    if orig:
        d["orig"] = orig
    return d


def S(label: str, url: str, note: str | None = None) -> dict:
    d = {"label": label, "url": url}
    if note:
        d["note"] = note
    return d


def D(fact: str, source: str, url: str | None = None) -> dict:
    d = {"fact": fact, "source": source, "label": fact, "note": source}
    if url:
        d["url"] = url
    return d


def M(label: str, url: str, note: str) -> dict:
    return {"label": label, "url": url, "note": note, "title": label}


def mark_top10(arguments: list[dict], n: int = 10) -> list[dict]:
    for a in arguments:
        r = a.get("rank")
        try:
            r_int = int(r)
        except (TypeError, ValueError):
            continue
        if 1 <= r_int <= n:
            a["importance"] = "Top 10"
    return arguments


def _merge_lists(existing: list | None, extra: list | None) -> list:
    out = list(existing or [])
    seen = set()
    for item in out:
        if isinstance(item, dict):
            seen.add(
                item.get("text")
                or item.get("url")
                or item.get("fact")
                or item.get("label")
                or item.get("claim")
            )
        else:
            seen.add(str(item))
    for item in extra or []:
        key = None
        if isinstance(item, dict):
            key = (
                item.get("text")
                or item.get("url")
                or item.get("fact")
                or item.get("label")
                or item.get("claim")
            )
        else:
            key = str(item)
        if key and key in seen:
            continue
        out.append(item)
        if key:
            seen.add(key)
    return out


def merge_side(base: dict | None, extra: dict | None) -> dict:
    out = dict(base or {})
    extra = extra or {}
    for k, v in extra.items():
        if k in ("quotes", "data_points", "manuscripts", "sources") and isinstance(v, list):
            out[k] = _merge_lists(out.get(k), v)
        elif v not in (None, "", []):
            out[k] = v
    return out


def apply_overlays(topic: dict, overlays: dict[str, dict]) -> dict:
    topic = copy.deepcopy(topic)
    by_id: dict[str, dict] = {a["id"]: a for a in topic.get("arguments") or [] if a.get("id")}
    for oid, extra in overlays.items():
        extra = dict(extra)
        extra.pop("id", None)
        if oid not in by_id:
            new_arg = {"id": oid, **extra}
            topic.setdefault("arguments", []).append(new_arg)
            by_id[oid] = new_arg
            continue
        a = by_id[oid]
        for k, v in extra.items():
            if k in ("christian", "muslim", "israel", "palestine"):
                a[k] = merge_side(a.get(k) or {}, v)
            elif k == "counters" and isinstance(v, list):
                a[k] = _merge_lists(a.get(k), v)
            elif k == "live" and v:
                a[k] = v
            elif k in ("why_it_matters", "importance", "crux", "debate_use", "popularity", "type", "cluster", "title") and v:
                a[k] = v
            elif isinstance(v, list) and k in ("quotes", "data_points", "manuscripts"):
                a[k] = _merge_lists(a.get(k), v)
    mark_top10(topic.get("arguments") or [])

    # Seed opponent cards from live lines if the topic is thin.
    cards = topic.get("opponent_cards") or []
    if len(cards) < 8:
        for a in topic.get("arguments") or []:
            live = a.get("live") or a.get("live_lines")
            if not live or not live.get("if_they_say"):
                continue
            trig = live["if_they_say"]
            if any(c.get("trigger") == trig for c in cards):
                continue
            cards.append(
                {
                    "trigger": trig,
                    "fast_answer": live.get("you_say") or "",
                    "follow_up": live.get("dont_overclaim") or a.get("crux") or "",
                    "sources": [a.get("title") or a.get("id")],
                }
            )
        topic["opponent_cards"] = cards
    return topic
