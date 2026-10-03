# -*- coding: utf-8 -*-
"""Write English topic snapshots for translators."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.build_kb import MODULES  # noqa: E402
from scripts.kb.i18n_common import RU_TOPIC_IDS  # noqa: E402

OUT = ROOT / "scripts" / "kb" / "locales" / "_en_src"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for mod in MODULES:
        topic = mod.topic()
        tid = topic["id"]
        if tid not in RU_TOPIC_IDS:
            continue
        path = OUT / f"{tid}.json"
        path.write_text(json.dumps(topic, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{tid}: {path.stat().st_size} bytes, args={len(topic.get('arguments') or [])}")


if __name__ == "__main__":
    main()
