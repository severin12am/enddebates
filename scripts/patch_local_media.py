# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "topics/historicity/media"
MAP = {
    "p52": "media/p52.jpg",
    "p52-annotated": "media/p52.jpg",
    "p66": "media/p52.jpg",
    "dss": "media/isaiah.jpg",
    "leningrad": "media/isaiah.jpg",
    "p46": "media/p46.jpg",
    "intf": "media/p46.jpg",
    "sinaiticus": "media/p46.jpg",  # temporary until download succeeds
    "vaticanus": "media/p46.jpg",
    "birmingham": "media/isaiah.jpg",  # replaced below if birmingham exists
    "birmingham-spread": "media/isaiah.jpg",
    "sanaa": "media/isaiah.jpg",
    "corpus-coranicum": "media/isaiah.jpg",
    "bukhari-4987": "media/p46.jpg",
}
# Prefer real files when present
for name, key in [
    ("birmingham.jpg", "birmingham"),
    ("birmingham-spread.jpg", "birmingham-spread"),
    ("sinaiticus.jpg", "sinaiticus"),
    ("p52-plate.jpg", "p52-annotated"),
]:
    if (MEDIA / name).exists() and (MEDIA / name).stat().st_size > 1000:
        MAP[key] = f"media/{name}"


def _patch(d: dict) -> dict:
    for m in d.get("materials", []):
        local = MAP.get(m["id"])
        if local and (ROOT / "topics/historicity" / local).exists():
            m["image"] = local
    return d


def _write_pair(d: dict, json_path: Path, js_path: Path, var_name: str) -> None:
    json_path.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    js_path.write_text(
        f"window.{var_name} = {json.dumps(d, ensure_ascii=False, indent=2)};\n"
        + (f"window.TOPIC_DATA = window.{var_name};\n" if var_name != "TOPIC_DATA_EN" else ""),
        encoding="utf-8",
    )


def main() -> None:
    ru_p = ROOT / "topics/historicity/data.json"
    en_p = ROOT / "topics/historicity/data.en.json"
    ru = _patch(json.loads(ru_p.read_text(encoding="utf-8")))
    _write_pair(ru, ru_p, ROOT / "topics/historicity/data.js", "TOPIC_DATA_RU")
    if en_p.exists():
        en = _patch(json.loads(en_p.read_text(encoding="utf-8")))
        _write_pair(en, en_p, ROOT / "topics/historicity/data.en.js", "TOPIC_DATA_EN")
    print("patched historicity materials to local where available")
    print("local files:", [f.name for f in MEDIA.glob("*")])


if __name__ == "__main__":
    main()
