# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
hist = json.loads((ROOT / "topics/historicity/data.json").read_text(encoding="utf-8"))
want = {"p52", "birmingham", "dss", "p46", "sinaiticus", "sanaa"}
mats = [m for m in hist["materials"] if m["id"] in want]

for tid in ["historical-jesus", "jesus-vision"]:
    p = ROOT / f"topics/{tid}/data.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    d["materials"] = mats
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / f"topics/{tid}/data.js").write_text(
        "window.TOPIC_DATA = " + json.dumps(d, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )
    print(tid, len(d["materials"]))

cat = json.loads((ROOT / "topics/catalog.json").read_text(encoding="utf-8"))
for t in cat["topics"]:
    dj = json.loads((ROOT / f"topics/{t['id']}/data.json").read_text(encoding="utf-8"))
    t["counts"] = {
        "arguments": len(dj.get("arguments") or []),
        "materials": len(dj.get("materials") or []),
        "cards": len(dj.get("opponent_cards") or []),
        "debates": len(dj.get("debates") or []),
    }
(ROOT / "topics/catalog.json").write_text(json.dumps(cat, ensure_ascii=False, indent=2), encoding="utf-8")
(ROOT / "topics/catalog.js").write_text(
    "window.TOPIC_CATALOG = " + json.dumps(cat, ensure_ascii=False, indent=2) + ";\n",
    encoding="utf-8",
)
print("catalog updated")
