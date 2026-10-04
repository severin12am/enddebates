# -*- coding: utf-8 -*-
"""Historicity of Bible vs Qur'an — expanded with materials gallery."""
from __future__ import annotations

import json
from pathlib import Path

from .historicity_deep import TOP10
from .deepen_lib import apply_overlays
from . import ataie
from . import historicity_rigor as rigor

ROOT = Path(__file__).resolve().parents[2]


def _load_legacy() -> dict:
    path = ROOT / "historicity" / "data" / "historicity-prep.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def topic() -> dict:
    legacy = _load_legacy()

    materials = [
        {
            "id": "p52",
            "title": "Papyrus 𝔓52 (Rylands) — John 18",
            "kind": "NT papyrus",
            "date": "Usually early–mid 2nd c. CE (debated)",
            "significance": (
                "Tiny fragment of John 18; among the earliest surviving NT witnesses. "
                "Proves a Johannine text was circulating in Egypt within ~100 years of composition — "
                "not photographic proof of events, but strong early textuality evidence."
            ),
            "debate_use": "Use against 'Gospels invented in 4th century.' Do not overclaim 'proves inerrancy.'",
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/32/P52_recto.jpg",
            "viewer_url": "https://manuscripts.csntm.org/Manuscript/View/GA_P52",
            "sources": [
                {"label": "CSNTM GA P52", "url": "https://manuscripts.csntm.org/Manuscript/View/GA_P52"},
                {"label": "Wikipedia: Rylands P52", "url": "https://en.wikipedia.org/wiki/Rylands_Library_Papyrus_P52"},
            ],
        },
        {
            "id": "p52-annotated",
            "title": "𝔓52 annotated plate (John 18)",
            "kind": "NT papyrus (teaching plate)",
            "date": "Fragment usually early–mid 2nd c. CE",
            "significance": (
                "Teaching image of P52 with context. Good slide for audiences who have never seen a papyrus."
            ),
            "debate_use": "Show the physical smallness — humility about what one fragment proves.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/82/Papyrus_52.jpg",
            "viewer_url": "https://commons.wikimedia.org/wiki/File:Papyrus_52.jpg",
            "sources": [
                {"label": "Wikimedia File:Papyrus 52.jpg", "url": "https://commons.wikimedia.org/wiki/File:Papyrus_52.jpg"},
            ],
        },
        {
            "id": "p66",
            "title": "Papyrus 𝔓66 (Bodmer II) — John",
            "kind": "NT papyrus",
            "date": "Late 2nd / early 3rd c. CE",
            "significance": (
                "Substantial papyrus of John. Shows early extensive copying and also scribal corrections — "
                "useful both for abundance arguments and for honest talk about variation."
            ),
            "debate_use": "Pair with P52: early + substantial. Ask opponent what early Islamic parallel they want compared.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/82/Papyrus_52.jpg",
            "viewer_url": "https://manuscripts.csntm.org/manuscript/Group/GA_P66_Bodmer",
            "sources": [
                {"label": "CSNTM P66", "url": "https://manuscripts.csntm.org/manuscript/Group/GA_P66_Bodmer"},
                {"label": "Bodmer Lab", "url": "https://bodmerlab.unige.ch/fr/constellations/papyri"},
            ],
        },
        {
            "id": "sinaiticus",
            "title": "Codex Sinaiticus (א)",
            "kind": "Greek Bible codex",
            "date": "Mid-4th c. CE",
            "significance": (
                "Nearly complete Greek Bible including NT. Landmark for reconstructing the early text; "
                "also contains famous readings (e.g. ending of Mark issues) that honest Christian apologetics must own."
            ),
            "debate_use": "Open the digital leaf live if possible. Transparency > slogan.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Codex_Sinaiticus.jpg/960px-Codex_Sinaiticus.jpg",
            "viewer_url": "https://codexsinaiticus.org/en/manuscript.aspx",
            "sources": [
                {"label": "Codex Sinaiticus Project", "url": "https://codexsinaiticus.org/en/"},
            ],
        },
        {
            "id": "vaticanus",
            "title": "Codex Vaticanus (B)",
            "kind": "Greek Bible codex",
            "date": "Mid-4th c. CE",
            "significance": (
                "Primary Alexandrian witness alongside Sinaiticus. Core of modern critical editions (NA/UBS)."
            ),
            "debate_use": "Cite as evidence that Christians can point to early complete-ish Bibles, not only medieval copies.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Codex_Sinaiticus.jpg/960px-Codex_Sinaiticus.jpg",
            "viewer_url": "https://digi.vatlib.it/view/MSS_Vat.gr.1209",
            "sources": [
                {"label": "DigiVatLib Vat.gr.1209", "url": "https://digi.vatlib.it/view/MSS_Vat.gr.1209"},
                {"label": "CSNTM GA 03", "url": "https://manuscripts.csntm.org/manuscript/Group/GA_03"},
            ],
        },
        {
            "id": "dss",
            "title": "Dead Sea Scrolls — Great Isaiah Scroll",
            "kind": "Jewish manuscript corpus",
            "date": "c. 3rd c. BCE – 1st c. CE",
            "significance": (
                "Pushes Hebrew Bible textual history back centuries before Islam. Shows substantial continuity "
                "with later MT and also real plurality (MT/LXX-like types). Context for Jesus' Judaism."
            ),
            "debate_use": "Destroys 'OT invented in Middle Ages.' Does not prove zero variation.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Great_Isaiah_Scroll.jpg/960px-Great_Isaiah_Scroll.jpg",
            "viewer_url": "https://www.deadseascrolls.org.il/",
            "sources": [
                {"label": "Leon Levy DSS Digital Library", "url": "https://www.deadseascrolls.org.il/"},
                {"label": "Digital DSS (IMJ)", "url": "https://dss.collections.imj.org.il/"},
            ],
        },
        {
            "id": "birmingham",
            "title": "Birmingham Qur'an folios (Mingana 1572a)",
            "kind": "Early Hijazi Qur'an",
            "date": "Parchment C-14 often cited 568–645 CE",
            "significance": (
                "High-profile early Qur'anic leaves. Media overclaimed 'oldest Qur'an'; academically: dates parchment, "
                "not ink; text is early Uthmanic-type. Strong proximity evidence."
            ),
            "debate_use": "Affirm impressiveness; force C-14 literacy (parchment vs writing event).",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Birmingham_Quran_manuscript_folio_1_recto.jpg/960px-Birmingham_Quran_manuscript_folio_1_recto.jpg",
            "viewer_url": "https://www.birmingham.ac.uk/news-archive/2015/birmingham-quran-manuscript-dated-among-the-oldest-in-the-world",
            "sources": [
                {"label": "Birmingham announcement", "url": "https://www.birmingham.ac.uk/news-archive/2015/birmingham-quran-manuscript-dated-among-the-oldest-in-the-world"},
                {"label": "Islamic Awareness C-14 dossier", "url": "https://www.islamic-awareness.org/quran/text/mss/radio"},
                {"label": "VMR Mingana leaf", "url": "http://vmr.bham.ac.uk/Collections/Mingana/Islamic_Arabic_1572a/table/"},
            ],
        },
        {
            "id": "birmingham-spread",
            "title": "Birmingham Qur'an — double folio view",
            "kind": "Early Hijazi Qur'an",
            "date": "Parchment often cited 568–645 CE",
            "significance": "Wider plate of the Birmingham leaves for slide decks and audience orientation.",
            "debate_use": "Use as the visual for 'proximity to Muhammad's lifetime' without overclaiming ink date.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Birmingham_Quran_manuscript.jpg/960px-Birmingham_Quran_manuscript.jpg",
            "viewer_url": "https://commons.wikimedia.org/wiki/File:Birmingham_Quran_manuscript.jpg",
            "sources": [
                {"label": "Wikimedia Birmingham plate", "url": "https://commons.wikimedia.org/wiki/File:Birmingham_Quran_manuscript.jpg"},
            ],
        },
        {
            "id": "sanaa",
            "title": "Ṣanʿāʾ palimpsest (DAM 01-27.1 / C-1)",
            "kind": "Qur'an palimpsest",
            "date": "Lower text 7th c. (non-Uthmanic type)",
            "significance": (
                "Only substantial manuscript witness to a non-Uthmanic Qur'anic text-type. Word/phrase variants; "
                "Sadeghi stemmatics argue Uthmanic closer to prototype. Challenges folk clone-identity; supports early multiplicity."
            ),
            "debate_use": "Both sides can use it — know BOTH uses before the round.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Birmingham_Quran_manuscript.jpg/960px-Birmingham_Quran_manuscript.jpg",
            "viewer_url": "https://en.wikipedia.org/wiki/Sanaa_manuscript",
            "sources": [
                {"label": "Islamic Awareness Sanaa dossier", "url": "https://www.islamic-awareness.org/quran/text/mss/soth.html"},
                {"label": "Sadeghi & Bergmann 2010 PDF", "url": "https://bible-quran.com/wp-content/uploads/2013/01/Sadeghi-Bergmann-The-Codex-of-a-Companion-of-the-Prophet-and-the-quran-of-the-Prophet.pdf"},
                {"label": "Hilali / IIS", "url": "https://www.iis.ac.uk/publications-listing/the-sanaa-palimpsest/"},
            ],
        },
        {
            "id": "corpus-coranicum",
            "title": "Corpus Coranicum / Manuscripta Coranica",
            "kind": "Digital research corpus",
            "date": "Ongoing",
            "significance": (
                "Best scholarly hub for early Qur'an manuscript images, transliterations, and research notes. "
                "Use this instead of viral 'Uthman's personal copy' claims about Topkapı/Samarkand."
            ),
            "debate_use": "When opponent cites Topkapı as Uthman's mushaf, open Corpus Coranicum dating ranges.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Birmingham_Quran_manuscript_folio_1_recto.jpg/960px-Birmingham_Quran_manuscript_folio_1_recto.jpg",
            "viewer_url": "https://corpuscoranicum.de/en/manuscripts",
            "sources": [
                {"label": "Corpus Coranicum manuscripts", "url": "https://corpuscoranicum.de/en/manuscripts"},
                {"label": "van Putten BSOAS 2019", "url": "https://doi.org/10.1017/s0041977x19000338"},
            ],
        },
        {
            "id": "bukhari-4987",
            "title": "Ṣaḥīḥ al-Bukhārī 4987 — Uthmanic collection report",
            "kind": "Hadith / primary narrative",
            "date": "Compilation 9th c.; reports 7th c. events",
            "significance": (
                "Classic account of Zayd's work under Abu Bakr then Uthman, distribution of copies, "
                "and burning of other materials. Central Christian critique text; also central Muslim unification narrative."
            ),
            "debate_use": "Quote the burning clause carefully; pair with van Putten/Sadeghi for academic framing.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Codex_Sinaiticus.jpg/960px-Codex_Sinaiticus.jpg",
            "viewer_url": "https://sunnah.com/bukhari:4987",
            "sources": [
                {"label": "Sunnah.com Bukhari 4987", "url": "https://sunnah.com/bukhari:4987"},
            ],
        },
        {
            "id": "intf",
            "title": "INTF / NT Virtual Manuscript Room",
            "kind": "Research infrastructure",
            "date": "Ongoing",
            "significance": (
                "Münster Institute for New Testament Textual Research — the academic engine behind critical NT editions. "
                "Use to show Christians do not hide variants; they catalogue them."
            ),
            "debate_use": "When '400,000 variants' appears, send people here conceptually: variants are published, not suppressed.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/5/5c/P46.jpg",
            "viewer_url": "https://ntvmr.uni-muenster.de/",
            "sources": [
                {"label": "INTF", "url": "https://www.uni-muenster.de/INTF/"},
                {"label": "NT.VMR", "url": "https://ntvmr.uni-muenster.de/"},
            ],
        },
        {
            "id": "p46",
            "title": "Papyrus 𝔓46 — Pauline letters",
            "kind": "NT papyrus",
            "date": "c. 200 CE (approx.)",
            "significance": (
                "Early collection of Paul. Relevant to historicity because Paul's letters (50s) are earliest Christian literature "
                "and already contain high Christology + crucifixion kerygma."
            ),
            "debate_use": "Bridge from manuscripts to content: early text + early theology of the cross.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/5/5c/P46.jpg",
            "viewer_url": "https://en.wikipedia.org/wiki/Papyrus_46",
            "sources": [
                {"label": "Wikipedia P46", "url": "https://en.wikipedia.org/wiki/Papyrus_46"},
                {"label": "Wikimedia P46", "url": "https://commons.wikimedia.org/wiki/File:P46.jpg"},
            ],
        },
        {
            "id": "leningrad",
            "title": "Leningrad Codex (OT Masoretic)",
            "kind": "Hebrew Bible codex",
            "date": "1008/1009 CE",
            "significance": (
                "Oldest complete MT Hebrew Bible. Often attacked as 'late' — answer with DSS centuries earlier "
                "showing the tradition's antiquity, while admitting medieval complete-codex gap."
            ),
            "debate_use": "Don't hide the date; answer with DSS + LXX + quotations.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Great_Isaiah_Scroll.jpg/960px-Great_Isaiah_Scroll.jpg",
            "viewer_url": "https://archive.org/details/Leningrad_Codex",
            "sources": [
                {"label": "Archive.org Leningrad Codex", "url": "https://archive.org/details/Leningrad_Codex"},
            ],
        },
    ]

    # Normalize legacy arguments to christian/muslim keys
    arguments = []
    for a in legacy.get("arguments", []):
        arg = dict(a)
        if "bible_case" in arg and "christian" not in arg:
            arg["christian"] = arg.pop("bible_case")
        if "quran_case" in arg and "muslim" not in arg:
            arg["muslim"] = arg.pop("quran_case")
        if "counter_to_bible" in arg:
            arg["counter_to_christian"] = arg.pop("counter_to_bible")
        if "counter_to_quran" in arg:
            arg["counter_to_muslim"] = arg.pop("counter_to_quran")
        # normalize sources key
        for side in ("christian", "muslim"):
            if side in arg and "sources" not in arg[side] and "receipts" in arg[side]:
                arg[side]["sources"] = arg[side].pop("receipts")
        arguments.append(arg)

    # Extra arguments beyond legacy
    extras = [
        {
            "id": "oral-vs-written",
            "rank": 12,
            "cluster": "Method",
            "title": "Oral memorization vs manuscript stemmata",
            "type": "method",
            "popularity": "High",
            "christian": {
                "claim": "Oral claims can stabilize a chosen reading; without stemmata they are hard to audit publicly.",
                "case": "Christian reply to hifz: impressive, but companion differences and Sanaa show memory/writing produced plurality. Public manuscript criticism is an epistemic virtue.",
                "sources": [
                    {"label": "Sadeghi on semi-oral transmission", "url": "https://bible-quran.com/wp-content/uploads/2013/01/Sadeghi-Bergmann-The-Codex-of-a-Companion-of-the-Prophet-and-the-quran-of-the-Prophet.pdf"}
                ],
            },
            "muslim": {
                "claim": "Mass memorization + written rasm is a dual lock unmatched by biblical transmission culture.",
                "case": "Living chains of recitation across regions make wholesale undetected rewrite implausible after early canonization.",
                "sources": [
                    {"label": "Yaqeen Uthmanic Codex", "url": "https://yaqeeninstitute.org/read/paper/the-uthmanic-codex-understanding-how-the-quran-was-preserved"}
                ],
            },
            "counter_to_christian": "Early Christian liturgy was also oral; unfair double standard.",
            "counter_to_muslim": "Oral frequency doesn't erase documented companion/qira'at differences.",
            "crux": "What can oral culture prove that manuscripts cannot falsify?",
            "debate_use": "Demand a falsifiable oral claim.",
        },
        {
            "id": "topkapi-myth",
            "rank": 13,
            "cluster": "Qur'an text",
            "title": "Topkapı / Samarkand 'Uthman's mushaf' claims",
            "type": "history",
            "popularity": "High in popular apologetics",
            "christian": {
                "claim": "Popular claims that Topkapı/Samarkand are Uthman's personal copies are not mainstream paleography.",
                "case": "Corpus Coranicum and codicologists typically date these large Kufic mushafs later (often 8th–9th c. type). Using them as autographs is folk history.",
                "sources": [
                    {"label": "Corpus Coranicum manuscripts", "url": "https://corpuscoranicum.de/en/manuscripts"}
                ],
            },
            "muslim": {
                "claim": "Even if not Uthman's hand, early monumental mushafs show early, stable, empire-wide written Qur'an.",
                "case": "The apologetic point can be restated without autograph claims: early Kufic witnesses align with Uthmanic rasm.",
                "sources": [
                    {"label": "van Putten orthographic archetype", "url": "https://doi.org/10.1017/s0041977x19000338"}
                ],
            },
            "counter_to_christian": "Rejecting autograph claims doesn't erase early manuscript strength.",
            "counter_to_muslim": "If your flyer said 'Uthman's copy,' correct it before the debate.",
            "crux": "Are we dating a piety legend or a manuscript?",
            "debate_use": "Concede early mushafs; reject autograph overclaim.",
        },
    ]
    arguments.extend(extras)
    arguments.extend(rigor.ARGUMENTS)

    # Deep Top 10 replace thin legacy cards of the same fight.
    deep_ids = {a["id"] for a in TOP10}
    alias_skip = {"qiraat"}  # replaced by qiraat-holes
    supporting = []
    rank = 12
    for a in arguments:
        if a.get("id") in deep_ids or a.get("id") in alias_skip:
            continue
        a = dict(a)
        a["rank"] = rank
        a.pop("importance", None)
        supporting.append(a)
        rank += 1
    arguments = list(TOP10) + [ataie.ARGUMENT] + supporting

    defs = list(legacy.get("definitions") or [])
    have = {d.get("term") for d in defs}
    if "Historicity" not in have:
        defs.insert(
            0,
            {
                "term": "Historicity",
                "precise": "Traceability of a text/community claims by historical methods.",
                "not": "Not the same as inspired or true.",
            },
        )
        have.add("Historicity")
    for d in ataie.DEFS + rigor.DEFS:
        if d["term"] not in have:
            defs.append(d)

    debates = [ataie.DEBATE] + list(legacy.get("debates") or [])
    cards = list(legacy.get("opponent_cards") or [])
    have_tr = {c.get("trigger") for c in cards}
    for c in ataie.CARDS + rigor.CARDS:
        if c["trigger"] not in have_tr:
            cards.append(c)
    materials.extend(ataie.MATERIALS)
    materials = rigor.apply_image_fixes(materials)

    bib = list(legacy.get("bibliography") or [])
    if not bib:
        bib = [
            {
                "tier": "Must-read",
                "items": [
                    {
                        "label": "Sadeghi & Bergmann 2010",
                        "url": "https://bible-quran.com/wp-content/uploads/2013/01/Sadeghi-Bergmann-The-Codex-of-a-Companion-of-the-Prophet-and-the-quran-of-the-Prophet.pdf",
                    },
                    {
                        "label": "van Putten 2019",
                        "url": "https://doi.org/10.1017/s0041977x19000338",
                    },
                    {
                        "label": "Codex Sinaiticus",
                        "url": "https://codexsinaiticus.org/en/",
                    },
                ],
            }
        ]
    bib.insert(
        0,
        {"tier": "Ataie lecture pack (watch first on qirāʾāt)", "items": ataie.BIB_ITEMS},
    )
    bib.insert(
        1,
        {"tier": "Academics to quote live (Sidky, Sinai, Wallace, Metzger, Tov)", "items": rigor.BIB_ITEMS},
    )

    default_checks = [
        "Define historicity vs preservation in opening",
        "Pick 3 materials to cite cold (P52, Birmingham, Sanaa)",
        "Drill opponent cards",
        "Watch Wallace–Ehrman once",
    ]
    checklist = [
        "Watch Ataie Sound Narrative once with the timestamp list (Debates → first card)",
        "Define uniformic slogan vs multiformic preservation before any qirāʾāt clip",
        "Memorize three names: Sidky (stemma), Wallace (how to count variants), Tov (DSS plurality + proto-MT)",
        "Open two viewers before the round: CSNTM or Sinaiticus, and Corpus Coranicum or Birmingham VMR",
        "If the round turns to 'the Qur'an knows Hebrew,' switch to topics/quran-hebrew-wordplay/ — do not improvise puns",
    ]
    seen_checks = set(checklist)
    for item in legacy.get("prep_checklist") or legacy.get("checklist") or default_checks:
        if item not in seen_checks:
            checklist.append(item)
            seen_checks.add(item)

    cases = dict(legacy.get("positive_cases") or {})
    if not cases:
        cases = {
            "Christian podium": [
                "NT reconstructability vs classical baseline",
                "DSS footprint for Hebrew Bible",
                "Crucifixion consensus vs Q 4:157",
            ],
            "Muslim podium": [
                "Ataie: defend multiformic aḥruf, not Hafs-clone slogans",
                "Short revelatory window + early rasm",
                "Oral-written dual transmission",
                "C-14 proximity of early Hijazi leaves",
            ],
            "Unity / steelman": [
                "Both have serious historical footprints",
                "Folk slogans on both sides are the enemy",
                "Share manuscript viewers before theology",
            ],
        }
    else:
        muslim_podium = list(cases.get("Muslim podium") or [])
        ataie_line = "Ataie: defend multiformic aḥruf, not Hafs-clone slogans"
        if ataie_line not in muslim_podium:
            muslim_podium.insert(0, ataie_line)
        cases["Muslim podium"] = muslim_podium

    meta = legacy.get("meta", {})
    built = {
        "id": "historicity",
        "meta": {
            "title": meta.get("title") or "Historicity of the Qur'an vs the Bible",
            "thesis": meta.get("thesis")
            or "Which scripture has the stronger historical case for textual integrity and proximity to origin — under which definitions?",
            "purpose": meta.get("purpose")
            or "Manuscripts, debates, arguments, and receipts for live debate prep. No declared winner.",
            "warning": meta.get("warning")
            or "Historicity ≠ preservation ≠ inspiration ≠ corruption. Define terms in 60 seconds.",
            "chips": ["Live desk", "Sidky / Wallace / Tov", "Manuscript viewers", "Both sides"],
            "default_tab": "live",
            "labels": {
                "christian": "Bible-historicity case",
                "muslim": "Qur'an-historicity case",
            },
        },
        "definitions": defs,
        "arguments": arguments,
        "materials": materials,
        "debates": debates,
        "opponent_cards": cards,
        "checklist": checklist,
        "positive_cases": cases,
        "bibliography": bib,
    }
    built = apply_overlays(built, {
        **ataie.OVERLAYS,
        "defs-first": {
            "why_it_matters": "Most rounds are lost in the first minute on undefined words.",
            "live": {
                "if_they_say": "The Bible is corrupted and the Qur'an is preserved, period.",
                "you_say": "Define corrupted (rewrite vs interpretation vs canon vs scribal noise) and preserved (letters vs rasm vs qira'at). Until those are locked, you are scoring slogans.",
                "dont_overclaim": "Don't let 'historicity' mean 'inspired.' Don't let 'preservation' mean 'true.'",
            },
        },
        "authorship": {
            "why_it_matters": "Anonymous Gospels vs one reciter is a category fight, not a photocopy fight.",
            "live": {
                "if_they_say": "We don't even know who wrote the Gospels.",
                "you_say": "Traditional authorship is debated; early attribution is not zero. Then ask whether unknown authors kill reconstructable content, and whether sīrah/hadith authorship is being held to the same standard.",
                "dont_overclaim": "Don't pretend Mark signed his papyrus. Don't pretend every hadith is mutawātir.",
            },
        },
        "oral-vs-written": {
            "why_it_matters": "Hifz is impressive; it is not a stemma.",
            "live": {
                "if_they_say": "Millions have it memorized, so it cannot have changed.",
                "you_say": "Memory can stabilize a chosen reading. Companion differences and Sanaa show plurality existed. Ask what oral culture would look like if it were wrong — what would falsify the claim?",
                "dont_overclaim": "Don't sneer at hifz. Don't treat it as carbon-dating.",
            },
        },
        "topkapi-myth": {
            "why_it_matters": "Folk autograph claims are an own-goal waiting to happen.",
            "live": {
                "if_they_say": "We still have Uthman's original mushaf in Istanbul.",
                "you_say": "Paleography usually dates those monumental Kufic copies later. Concede early rasm; drop the autograph flyer. Van Putten's archetype argument is stronger than a tourist caption.",
                "dont_overclaim": "Don't say those mushafs are fakes. Don't say they are signed by Uthman.",
            },
        },
    })
    return apply_overlays(built, rigor.OVERLAYS)
