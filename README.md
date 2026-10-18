# EndDebates

Knowledge base for Islam vs Christianity debates: steelmanned arguments, manuscripts/materials, opponent cards, sources.

## Open

```bash
npx --yes serve .
```

- Hub: http://localhost:5173/
- Historicity (with papyri/mushaf gallery): http://localhost:5173/topics/historicity/
- Qur'anic miracles (i'jaz): http://localhost:5173/topics/quranic-miracles/
- Trinity vs Tawhid: http://localhost:5173/topics/trinity/

Live:

- GitHub Pages: https://severin12am.github.io/enddebates/
- Netlify: https://enddebates-kb.netlify.app/

## Topics

| Topic | Path |
|------|------|
| Historicity of Bible vs Qur'an | `topics/historicity/` |
| Christian critiques of Islam | `topics/critiques/` |
| Qur'anic miracles (i'jaz) + sincerity | `topics/quranic-miracles/` |
| Trinity vs Tawhid | `topics/trinity/` |
| Rules of warfare | `topics/warfare/` |
| Which is more moral | `topics/morality/` |
| Women | `topics/women/` |
| Slavery | `topics/slavery/` |
| Non-believers | `topics/nonbelievers/` |
| Historical Jesus | `topics/historical-jesus/` |
| Vision of Jesus | `topics/jesus-vision/` |

## Rebuild

```bash
python scripts/build_kb.py
```

Topic modules live in `scripts/kb/`. Shared UI in `shared/`.

## Design rules for this KB

1. Define terms before slogans  
2. Steelman both sides  
3. Attach receipts (primary + academic)  
4. Name the crux  
5. No declared winner on the page — prepare to argue, not to cosplay certainty  
