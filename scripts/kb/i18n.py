# -*- coding: utf-8 -*-
"""Apply committed Russian locale JSON onto English topic payloads."""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any

from .i18n_common import UI_RU, RU_TOPIC_IDS

ROOT = Path(__file__).resolve().parents[2]
LOCALE_DIR = Path(__file__).resolve().parent / "locales" / "ru"

# Keys that must never be replaced from locale overlays (structure / links / ids).
SKIP_KEYS = frozenset(
    {
        "id",
        "url",
        "image",
        "viewer_url",
        "path",
        "url_en",
        "orig",
        "lang",
        "rank",
        "type",
        "year",
    }
)

# Whole-object replacements (dict keys themselves are translated, e.g. positive_cases).
REPLACE_KEYS = frozenset({"positive_cases"})

# Bible book names → Synodal abbreviations (longer phrases first).
_BIBLE_REF_MAP = [
    (r"\b1 Corinthians\b", "1 Кор"),
    (r"\b2 Corinthians\b", "2 Кор"),
    (r"\b1 Thessalonians\b", "1 Фес"),
    (r"\b2 Thessalonians\b", "2 Фес"),
    (r"\b1 Timothy\b", "1 Тим"),
    (r"\b2 Timothy\b", "2 Тим"),
    (r"\b1 Peter\b", "1 Пет"),
    (r"\b2 Peter\b", "2 Пет"),
    (r"\b1 John\b", "1 Ин"),
    (r"\b2 John\b", "2 Ин"),
    (r"\b3 John\b", "3 Ин"),
    (r"\b1 Samuel\b", "1 Цар"),
    (r"\b2 Samuel\b", "2 Цар"),
    (r"\b1 Kings\b", "3 Цар"),
    (r"\b2 Kings\b", "4 Цар"),
    (r"\b1 Chronicles\b", "1 Пар"),
    (r"\b2 Chronicles\b", "2 Пар"),
    (r"\bMatthew\b", "Мф"),
    (r"\bMark\b", "Мк"),
    (r"\bLuke\b", "Лк"),
    (r"\bJohn\b", "Ин"),
    (r"\bActs\b", "Деян"),
    (r"\bRomans\b", "Рим"),
    (r"\bGalatians\b", "Гал"),
    (r"\bEphesians\b", "Еф"),
    (r"\bPhilippians\b", "Флп"),
    (r"\bColossians\b", "Кол"),
    (r"\bHebrews\b", "Евр"),
    (r"\bJames\b", "Иак"),
    (r"\bJude\b", "Иуд"),
    (r"\bRevelation\b", "Откр"),
    (r"\bGenesis\b", "Быт"),
    (r"\bExodus\b", "Исх"),
    (r"\bLeviticus\b", "Лев"),
    (r"\bDeuteronomy\b", "Втор"),
    (r"\bIsaiah\b", "Ис"),
    (r"\bJeremiah\b", "Иер"),
    (r"\bPsalm\b", "Пс"),
    (r"\bPsalms\b", "Пс"),
    (r"\bQur'an\b", "Коран"),
    (r"\bQuran\b", "Коран"),
]


def _looks_like_url(s: str) -> bool:
    s = s.strip()
    return s.startswith("http://") or s.startswith("https://") or s.startswith("www.")


def _normalize_bible_refs(text: str) -> str:
    if not text or not isinstance(text, str):
        return text
    out = text
    for pat, repl in _BIBLE_REF_MAP:
        out = re.sub(pat, repl, out)
    # Qur'an 4:157 → «Коран 4:157» when not already quoted
    out = re.sub(r"(?<![«\"])Коран\s+(\d+:\d+)", r"«Коран \1»", out)
    return out


def _merge_locale(base: Any, overlay: Any) -> Any:
    """Deep-merge overlay onto base; overlay wins for translatable leaves."""
    if overlay is None:
        return base
    if isinstance(base, dict) and isinstance(overlay, dict):
        out = copy.deepcopy(base)
        for key, oval in overlay.items():
            if key in SKIP_KEYS:
                continue
            if key in REPLACE_KEYS:
                out[key] = copy.deepcopy(oval)
                continue
            if key not in out:
                out[key] = copy.deepcopy(oval)
                continue
            out[key] = _merge_locale(out[key], oval)
        if (
            "text" in out
            and "who" in out
            and not out.get("orig")
            and isinstance(base.get("text"), str)
            and base.get("text") != out.get("text")
        ):
            out["orig"] = base["text"]
        return out
    if isinstance(base, list) and isinstance(overlay, list):
        if not overlay:
            return copy.deepcopy(base)
        if all(isinstance(x, dict) and x.get("id") for x in base) and all(
            isinstance(x, dict) and x.get("id") for x in overlay
        ):
            by_id = {item["id"]: item for item in overlay}
            merged = []
            for item in base:
                oid = item.get("id")
                if oid and oid in by_id:
                    merged.append(_merge_locale(item, by_id[oid]))
                else:
                    merged.append(copy.deepcopy(item))
            return merged
        if all(isinstance(x, dict) for x in base) and all(isinstance(x, dict) for x in overlay):
            return _merge_locale_list_by_index(base, overlay)
        if all(isinstance(x, str) for x in overlay):
            return [_normalize_bible_refs(x) for x in overlay]
        return _merge_locale_list_by_index(base, overlay)
    if isinstance(overlay, str) and overlay.strip():
        if _looks_like_url(overlay):
            return base
        return _normalize_bible_refs(overlay)
    return copy.deepcopy(overlay) if overlay is not None else base


def _merge_locale_list_by_index(base: list, overlay: list) -> list:
    out = []
    for i, item in enumerate(base):
        if i < len(overlay):
            out.append(_merge_locale(item, overlay[i]))
        else:
            out.append(copy.deepcopy(item))
    return out


def load_ru_locale(topic_id: str) -> dict | None:
    path = LOCALE_DIR / f"{topic_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def apply_ru_locale(en_topic: dict) -> dict:
    tid = en_topic.get("id", "")
    if tid not in RU_TOPIC_IDS:
        return en_topic
    overlay = load_ru_locale(tid)
    if not overlay:
        print(f"WARN: missing Russian locale for {tid}; English left in place")
        ru = copy.deepcopy(en_topic)
        meta = ru.setdefault("meta", {})
        meta["lang"] = "ru"
        meta["ui"] = {**UI_RU, **(meta.get("ui") or {})}
        return ru
    ru = _merge_locale(en_topic, overlay)
    ru = copy.deepcopy(ru)
    meta = ru.setdefault("meta", {})
    meta["lang"] = "ru"
    meta["ui"] = {**UI_RU, **(meta.get("ui") or {})}
    labels = meta.get("labels") or {}
    if labels.get("christian") == "Christian case":
        labels["christian"] = "Христианский тезис"
    if labels.get("muslim") == "Muslim case":
        labels["muslim"] = "Мусульманский тезис"
    meta["labels"] = labels
    if meta.get("importance") == "Top 10":
        meta["importance"] = "Топ-10"
    for arg in ru.get("arguments") or []:
        if arg.get("importance") == "Top 10":
            arg["importance"] = "Топ-10"
    return ru


def export_en_topic(topic: dict) -> None:
    """Write English snapshot for translators (optional dev helper)."""
    tid = topic["id"]
    out = LOCALE_DIR.parent / "en" / f"{tid}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(topic, ensure_ascii=False, indent=2), encoding="utf-8")
