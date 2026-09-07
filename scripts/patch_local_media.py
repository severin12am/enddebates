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

def main() -> None:
    p = ROOT / "topics/historicity/data.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    for m in d.get("materials", []):
        local = MAP.get(m["id"])
        if local and (ROOT / "topics/historicity" / local).exists():
            m["image"] = local
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "topics/historicity/data.js").write_text(
        "window.TOPIC_DATA = " + json.dumps(d, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )
    print("patched historicity materials to local where available")
    print("local files:", [f.name for f in MEDIA.glob("*")])


if __name__ == "__main__":
    main()
