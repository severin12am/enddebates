# -*- coding: utf-8 -*-
"""Build the EndDebates multi-topic knowledge base."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.kb import (  # noqa: E402
    critiques,
    historical_jesus,
    historicity,
    israel_palestine,
    jesus_not_god_ru,
    jesus_vision,
    morality,
    nonbelievers,
    slavery,
    trinity,
    warfare,
    women,
)

MODULES = [
    historicity,
    critiques,
    trinity,
    warfare,
    morality,
    women,
    slavery,
    nonbelievers,
    historical_jesus,
    jesus_vision,
    jesus_not_god_ru,
    israel_palestine,
]

CATALOG_META = {
    "historicity": {
        "blurb": "Live desk + viewers: Sidky stemma, Wallace variant-count, Tov/DSS, Sinaiticus, Birmingham.",
        "group": "Scripture",
    },
    "critiques": {
        "blurb": "Top Christian apologetic critiques of Islam with documented counters, including Ataie on preservation.",
        "group": "Scripture",
    },
    "trinity": {
        "blurb": "Trinity vs Tawhid — coherence, simplicity, revelation, worship.",
        "group": "God",
    },
    "historical-jesus": {
        "blurb": "Who tracks the scholarly historical Jesus more closely?",
        "group": "Jesus",
    },
    "jesus-vision": {
        "blurb": "Incarnate Son vs prophet-Messiah — rational and historical scoring.",
        "group": "Jesus",
    },
    "jesus-not-god-ru": {
        "blurb": "RU: стихи за Троицу с ответами; почему Иисус не Бог.",
        "group": "Jesus",
    },
    "warfare": {
        "blurb": "Just war vs jihad / siyar — cause, conduct, classical vs reform.",
        "group": "Ethics",
    },
    "morality": {
        "blurb": "Foundational moral vision: grace, deeds, law, conscience, outcomes.",
        "group": "Ethics",
    },
    "women": {
        "blurb": "Texts, classical law, and modern outcomes on women.",
        "group": "Ethics",
    },
    "slavery": {
        "blurb": "Regulation vs abolition — scripture, history, and moral development.",
        "group": "Ethics",
    },
    "nonbelievers": {
        "blurb": "Dhimma, apostasy, missions, religious liberty.",
        "group": "Ethics",
    },
    "israel-palestine": {
        "blurb": "Two peoples, one land: 1948, occupation, refugees, Gaza, law, end-states — steelmanned, no press officer.",
        "group": "Israel–Palestine",
    },
}


def write_topic(topic: dict) -> Path:
    tid = topic["id"]
    out_dir = ROOT / "topics" / tid
    out_dir.mkdir(parents=True, exist_ok=True)

    # data.js
    (out_dir / "data.js").write_text(
        "window.TOPIC_DATA = " + json.dumps(topic, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )
    (out_dir / "data.json").write_text(
        json.dumps(topic, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # index.html from template
    template = (ROOT / "topics" / "_template.html").read_text(encoding="utf-8")
    html = (
        template.replace("TOPIC_TITLE", topic["meta"]["title"])
        .replace("TOPIC_DESC", topic["meta"].get("purpose") or topic["meta"]["thesis"])
        .replace("TOPIC_LANG", topic["meta"].get("lang") or "en")
    )
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    return out_dir


def main() -> None:
    catalog = []
    for mod in MODULES:
        topic = mod.topic()
        tid = topic["id"]
        write_topic(topic)
        meta = CATALOG_META.get(tid, {})
        catalog.append(
            {
                "id": tid,
                "title": topic["meta"]["title"],
                "thesis": topic["meta"]["thesis"],
                "blurb": meta.get("blurb") or topic["meta"].get("purpose", ""),
                "group": meta.get("group") or "Topics",
                "path": f"topics/{tid}/",
                "counts": {
                    "arguments": len(topic.get("arguments") or []),
                    "materials": len(topic.get("materials") or []),
                    "cards": len(topic.get("opponent_cards") or []),
                    "debates": len(topic.get("debates") or []),
                },
            }
        )
        print(
            f"OK {tid}: args={len(topic.get('arguments') or [])} "
            f"mats={len(topic.get('materials') or [])} cards={len(topic.get('opponent_cards') or [])}"
        )

    cat_path = ROOT / "topics" / "catalog.json"
    cat_path.write_text(json.dumps({"topics": catalog}, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "topics" / "catalog.js").write_text(
        "window.TOPIC_CATALOG = " + json.dumps({"topics": catalog}, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )

    # Share core manuscript materials into Jesus topics
    hist_data = json.loads((ROOT / "topics/historicity/data.json").read_text(encoding="utf-8"))
    want = {"p52", "birmingham", "dss", "p46", "sinaiticus", "sanaa"}
    shared_mats = [m for m in hist_data.get("materials", []) if m.get("id") in want]
    for tid in ("historical-jesus", "jesus-vision"):
        p = ROOT / "topics" / tid / "data.json"
        d = json.loads(p.read_text(encoding="utf-8"))
        d["materials"] = shared_mats
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        (ROOT / "topics" / tid / "data.js").write_text(
            "window.TOPIC_DATA = " + json.dumps(d, ensure_ascii=False, indent=2) + ";\n",
            encoding="utf-8",
        )
        for item in catalog:
            if item["id"] == tid:
                item["counts"]["materials"] = len(shared_mats)

    if (ROOT / "topics" / "ostrovsky" / "index.html").exists():
        catalog.append(
            {
                "id": "ostrovsky",
                "title": "Ошибки Островского",
                "thesis": "Разбор эфира 29.08.2026: транскрипт и кандидаты для ролика.",
                "blurb": "RU: диспут Островский × Юлиана — ошибки, таймкоды, транскрипт.",
                "group": "Live",
                "path": "topics/ostrovsky/",
                "counts": {
                    "arguments": 20,
                    "materials": 0,
                    "cards": 20,
                    "debates": 1,
                },
            }
        )

    cat_path.write_text(json.dumps({"topics": catalog}, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "topics" / "catalog.js").write_text(
        "window.TOPIC_CATALOG = " + json.dumps({"topics": catalog}, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )

    # Prefer local media files for historicity gallery when present
    patch = ROOT / "scripts" / "patch_local_media.py"
    if patch.exists():
        import runpy

        runpy.run_path(str(patch))

    print(f"Catalog: {cat_path} ({len(catalog)} topics)")


if __name__ == "__main__":
    main()
