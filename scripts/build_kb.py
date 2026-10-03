# -*- coding: utf-8 -*-
"""Build the EndDebates multi-topic knowledge base."""
from __future__ import annotations

import json
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
from scripts.kb.i18n import apply_ru_locale  # noqa: E402
from scripts.kb.i18n_common import (  # noqa: E402
    CATALOG_META_RU,
    HUB_UI_EN,
    HUB_UI_RU,
    RU_TOPIC_IDS,
    UI_EN,
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

GROUP_RU = {
    "Scripture": "Писание",
    "God": "Бог",
    "Jesus": "Иисус",
    "Ethics": "Этика",
    "Israel–Palestine": "Israel–Palestine",
    "Live": "Live",
}


def _dump_js(var_assigns: list[tuple[str, dict]]) -> str:
    parts = []
    first_name = None
    for name, obj in var_assigns:
        payload = json.dumps(obj, ensure_ascii=False, indent=2)
        parts.append(f"window.{name} = {payload};")
        if first_name is None:
            first_name = name
    if first_name and all(n != "TOPIC_DATA" for n, _ in var_assigns):
        parts.append(f"window.TOPIC_DATA = window.{first_name};")
    return "\n".join(parts) + "\n"


def _write_json(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _with_en_ui(topic: dict) -> dict:
    out = dict(topic)
    meta = dict(out.get("meta") or {})
    ui = dict(UI_EN)
    ui.update(meta.get("ui") or {})
    meta["ui"] = ui
    if not meta.get("lang"):
        meta["lang"] = "en"
    out["meta"] = meta
    return out


def write_topic(en_topic: dict, ru_topic: dict | None) -> Path:
    tid = en_topic["id"]
    out_dir = ROOT / "topics" / tid
    out_dir.mkdir(parents=True, exist_ok=True)

    en_out = _with_en_ui(en_topic)
    default = ru_topic if ru_topic is not None else en_out

    _write_json(out_dir / "data.json", default)
    _write_json(out_dir / "data.en.json", en_out)
    (out_dir / "data.js").write_text(
        _dump_js([("TOPIC_DATA_RU" if ru_topic is not None else "TOPIC_DATA", default)]),
        encoding="utf-8",
    )
    (out_dir / "data.en.js").write_text(
        _dump_js([("TOPIC_DATA_EN", en_out)]),
        encoding="utf-8",
    )

    display = default
    template = (ROOT / "topics" / "_template.html").read_text(encoding="utf-8")
    html = (
        template.replace("TOPIC_TITLE", display["meta"]["title"])
        .replace("TOPIC_DESC", display["meta"].get("purpose") or display["meta"]["thesis"])
        .replace("TOPIC_LANG", display["meta"].get("lang") or "ru")
    )
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    return out_dir


def _catalog_text(en: str, ru: str) -> dict:
    return {"en": en, "ru": ru}


def _catalog_row(en_topic: dict, ru_topic: dict | None, counts: dict) -> dict:
    tid = en_topic["id"]
    meta_en = CATALOG_META.get(tid, {})
    meta_ru = CATALOG_META_RU.get(tid, {})
    en_title = en_topic["meta"]["title"]
    ru_src = ru_topic or en_topic
    ru_title = meta_ru.get("title") or ru_src["meta"]["title"]
    en_blurb = meta_en.get("blurb") or en_topic["meta"].get("purpose", "")
    ru_blurb = meta_ru.get("blurb") or ru_src["meta"].get("purpose", en_blurb)
    en_group = meta_en.get("group") or "Topics"
    ru_group = meta_ru.get("group") or GROUP_RU.get(en_group, en_group)
    return {
        "id": tid,
        "title": _catalog_text(en_title, ru_title),
        "thesis": _catalog_text(en_topic["meta"]["thesis"], ru_src["meta"]["thesis"]),
        "blurb": _catalog_text(en_blurb, ru_blurb),
        "group": _catalog_text(en_group, ru_group),
        "path": f"topics/{tid}/",
        "counts": counts,
        "bilingual": tid in RU_TOPIC_IDS,
    }


def _write_payload(path: Path, obj: dict) -> None:
    _write_json(path, obj)
    if path.suffix == ".json":
        js = path.with_suffix(".js")
        js.write_text(
            "window.TOPIC_CATALOG = " + json.dumps(obj, ensure_ascii=False, indent=2) + ";\n",
            encoding="utf-8",
        )


def _share_materials(catalog: list[dict]) -> None:
    want = {"p52", "birmingham", "dss", "p46", "sinaiticus", "sanaa"}
    hist_ru = json.loads((ROOT / "topics/historicity/data.json").read_text(encoding="utf-8"))
    hist_en = json.loads((ROOT / "topics/historicity/data.en.json").read_text(encoding="utf-8"))
    mats_ru = [m for m in hist_ru.get("materials", []) if m.get("id") in want]
    mats_en = [m for m in hist_en.get("materials", []) if m.get("id") in want]
    for tid in ("historical-jesus", "jesus-vision"):
        ru_path = ROOT / "topics" / tid / "data.json"
        en_path = ROOT / "topics" / tid / "data.en.json"
        ru = json.loads(ru_path.read_text(encoding="utf-8"))
        en = json.loads(en_path.read_text(encoding="utf-8"))
        ru["materials"] = mats_ru
        en["materials"] = mats_en
        _write_json(ru_path, ru)
        _write_json(en_path, en)
        (ROOT / "topics" / tid / "data.js").write_text(
            _dump_js([("TOPIC_DATA_RU", ru)]),
            encoding="utf-8",
        )
        (ROOT / "topics" / tid / "data.en.js").write_text(
            _dump_js([("TOPIC_DATA_EN", en)]),
            encoding="utf-8",
        )
        for item in catalog:
            if item["id"] == tid:
                item["counts"]["materials"] = len(mats_ru)


def main() -> None:
    catalog = []
    for mod in MODULES:
        en_topic = mod.topic()
        tid = en_topic["id"]
        ru_topic = apply_ru_locale(en_topic) if tid in RU_TOPIC_IDS else None
        write_topic(en_topic, ru_topic)
        display = ru_topic or en_topic
        counts = {
            "arguments": len(display.get("arguments") or []),
            "materials": len(display.get("materials") or []),
            "cards": len(display.get("opponent_cards") or []),
            "debates": len(display.get("debates") or []),
        }
        catalog.append(_catalog_row(en_topic, ru_topic, counts))
        print(
            f"OK {tid}: args={counts['arguments']} "
            f"mats={counts['materials']} cards={counts['cards']} "
            f"lang={'ru+en' if ru_topic is not None else display['meta'].get('lang', 'en')}"
        )

    _share_materials(catalog)

    if (ROOT / "topics" / "ostrovsky" / "index.html").exists():
        catalog.append(
            {
                "id": "ostrovsky",
                "title": _catalog_text("Ошибки Островского", "Ошибки Островского"),
                "thesis": _catalog_text(
                    "Разбор эфира 29.08.2026: транскрипт и кандидаты для ролика.",
                    "Разбор эфира 29.08.2026: транскрипт и кандидаты для ролика.",
                ),
                "blurb": _catalog_text(
                    "RU: диспут Островский × Юлиана — ошибки, таймкоды, транскрипт.",
                    "RU: диспут Островский × Юлиана — ошибки, таймкоды, транскрипт.",
                ),
                "group": _catalog_text("Live", "Live"),
                "path": "topics/ostrovsky/",
                "counts": {
                    "arguments": 20,
                    "materials": 0,
                    "cards": 20,
                    "debates": 1,
                },
                "bilingual": False,
            }
        )

    catalog_obj = {
        "default_lang": "ru",
        "ui": {"en": HUB_UI_EN, "ru": HUB_UI_RU},
        "topics": catalog,
    }
    cat_path = ROOT / "topics" / "catalog.json"
    _write_payload(cat_path, catalog_obj)

    patch = ROOT / "scripts" / "patch_local_media.py"
    if patch.exists():
        import runpy

        runpy.run_path(str(patch))

    print(f"Catalog: {cat_path} ({len(catalog)} topics)")


if __name__ == "__main__":
    main()
