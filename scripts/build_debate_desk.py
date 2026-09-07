# -*- coding: utf-8 -*-
"""Build local debate-video desk data.js from transcript.json."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESK = ROOT / "debate-video"
TRANSCRIPT = DESK / "transcript.json"
KB = ROOT / "topics" / "jesus-not-god-ru" / "data.json"

CHAPTER_HINTS = [
    ("intro", "Старт", ["зачем", "пророк", "начн", "привет"]),
    ("trinity-modalism", "Троица / троякое проявление", ["троиц", "трояк", "трое", "отец", "сын", "дух", "проявлен"]),
    ("jesus-prophet", "Иисус — пророк или Бог", ["исус", "пророк", "бог", "божеств", "воплощ"]),
    ("paul-prayer", "Павел, молитва, Аллах", ["павел", "молит", "аллах", "отче", "элах"]),
    ("moses-logic", "Моисей и логика пророков", ["моис", "муса", "логик", "пророк"]),
    ("quran-isa", "Иса в Коране", ["коран", "иса", "исус", "4:171", "5:116", "таухид"]),
    ("verses", "Стихи и доказательства", ["ин ", "матф", "марк", "лук", "иоанн", "стих", "евangel"]),
    ("forgive-one", "Прощение / «Я и Отец одно»", ["прощ", "20:23", "10:30", "17:21", "един"]),
    ("worship", "Поклонение и молитва", ["поклон", "latria", "служ", "молит"]),
    ("close", "Финал", ["итог", "заключ", "спасиб", "давайте"]),
]


def load_kb_links() -> list[dict]:
    if not KB.exists():
        return []
    data = json.loads(KB.read_text(encoding="utf-8"))
    out = []
    for p in data.get("trinity_proofs") or []:
        out.append(
            {
                "label": p.get("they_say") or p.get("hook") or "",
                "hook": p.get("hook") or "",
                "counter": (p.get("counter") or "")[:280],
                "url": "../topics/jesus-not-god-ru/#proofs",
            }
        )
    for c in (data.get("opponent_cards") or [])[:12]:
        out.append(
            {
                "label": c.get("trigger") or "",
                "hook": "",
                "counter": c.get("fast_answer") or "",
                "url": "../topics/jesus-not-god-ru/#cards",
            }
        )
    return out


def suggest_chapters(segments: list[dict]) -> list[dict]:
    chapters = []
    used = set()
    for cid, title, keys in CHAPTER_HINTS:
        best = None
        for seg in segments:
            t = seg["text"].lower()
            if seg["id"] in used:
                continue
            if any(k in t for k in keys):
                best = seg
                break
        if best:
            used.add(best["id"])
            chapters.append(
                {
                    "id": cid,
                    "title": title,
                    "start": best["start"],
                    "start_fmt": best["start_fmt"],
                    "anchor_text": best["text"][:120],
                }
            )
    if segments and (not chapters or chapters[0]["start"] > 30):
        chapters.insert(
            0,
            {
                "id": "start",
                "title": "Начало записи",
                "start": segments[0]["start"],
                "start_fmt": segments[0]["start_fmt"],
                "anchor_text": segments[0]["text"][:120],
            },
        )
    chapters.sort(key=lambda c: c["start"])
    return chapters


def keyword_hits(segments: list[dict]) -> list[dict]:
    terms = [
        "троиц", "пророк", "исус", "аллах", "бог", "коран", "павел", "моис", "муса",
        "ин 10", "ин 20", "ин 17", "ин 8", "мф 28", "прощ", "поклон", "молит",
        "воплощ", "таухид", "един", "дух", "отец", "сын",
    ]
    hits = []
    for seg in segments:
        low = seg["text"].lower()
        matched = [t for t in terms if t in low]
        if matched:
            hits.append(
                {
                    "start": seg["start"],
                    "start_fmt": seg["start_fmt"],
                    "text": seg["text"],
                    "terms": matched,
                }
            )
    return hits[:80]


def main() -> None:
    if not TRANSCRIPT.exists():
        placeholder = {
            "meta": {
                "title": "Дебаты 29.08.2026 — Instagram",
                "status": "waiting_transcript",
                "note": "Запустите: python scripts/transcribe_debate.py",
            },
            "chapters": [],
            "keyword_hits": [],
            "kb_links": load_kb_links(),
            "transcript": {"segments": [], "duration_fmt": "—", "full_text": ""},
            "checklist": [
                "Открыть index.html, загрузить MP4 с рабочего стола",
                "Дождаться transcript.json (python scripts/transcribe_debate.py)",
                "Пересобрать data.js: python scripts/build_debate_desk.py",
                "Пройти главы слева — отметить клипы для монтажа",
                "Сверить спорные стихи с topics/jesus-not-god-ru",
            ],
        }
        (DESK / "data.js").write_text(
            "window.DEBATE_DATA = " + json.dumps(placeholder, ensure_ascii=False, indent=2) + ";\n",
            encoding="utf-8",
        )
        print("Placeholder data.js (no transcript yet)")
        return

    tr = json.loads(TRANSCRIPT.read_text(encoding="utf-8"))
    segments = tr.get("segments") or []
    src = tr.get("source") or {}

    payload = {
        "meta": {
            "title": "Дебаты — Иисус / Троица (29.08.2026)",
            "status": "ready",
            "recorded": src.get("recorded", "2026-08-29"),
            "duration_fmt": tr.get("duration_fmt", ""),
            "duration_sec": tr.get("duration", 0),
            "segment_count": len(segments),
            "model": tr.get("model", ""),
            "video_hint": src.get("video_name", "Screen_Recording_20260829_211742_Instagram.mp4"),
            "video_path": src.get("video", ""),
        },
        "chapters": suggest_chapters(segments),
        "keyword_hits": keyword_hits(segments),
        "kb_links": load_kb_links(),
        "transcript": {
            "segments": segments,
            "duration_fmt": tr.get("duration_fmt", ""),
            "full_text": tr.get("full_text", ""),
        },
        "checklist": [
            "Хук 0:00–0:45: самый острый обмен (пророк vs Бог)",
            "3–5 клипов по 30–90 с — один аргумент на клип",
            "На экране: таймкод + стих (Синодальный + греч. при необходимости)",
            "Не монтировать «победу» — показать стальман и ответ",
            "В описании: ссылка на EndDebates KB (jesus-not-god-ru)",
            "Экспорт субтитров: transcript.srt в этой папке",
        ],
        "video_ideas": [
            {"title": "«Если Иисус Бог — почему не Моисей?»", "terms": ["моис", "муса", "пророк"]},
            {"title": "Троякое проявление vs таухид", "terms": ["троиц", "трояк", "таухид"]},
            {"title": "Иисус молился — кому?", "terms": ["молит", "отче", "аллах"]},
            {"title": "Стихи за божество и ответы", "terms": ["ин ", "стих", "прощ", "10:30"]},
        ],
    }

    (DESK / "data.js").write_text(
        "window.DEBATE_DATA = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )
    (DESK / "data.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Built desk: {len(segments)} segments, {len(payload['chapters'])} chapters")


if __name__ == "__main__":
    main()
