# -*- coding: utf-8 -*-
"""Sourced academic quotes + manuscript gallery deepen for Historicity.

Quotes are from published abstracts, reviews, and books we opened.
Do not invent wording. Sidky review: Al-ʿUṣūr al-Wusṭā 27 (2019).
"""
from .deepen_lib import D, M, Q, S

SIDKY_REVIEW = "https://www.middleeastmedievalists.com/wp-content/uploads/2019/11/UW-27-Sidky.pdf"
SIDKY_JIQSA = "https://lockwoodonlinejournals.com/index.php/jiqsa/article/view/554"
SIDKY_JAOS = "https://doi.org/10.7817/jaos.143.4.2023.ar029"
VAN_PUTTEN = "https://doi.org/10.1017/s0041977x19000338"
SINAI_II = "https://doi.org/10.1017/s0041977x14000111"
WALLACE_COUNT = "https://danielbwallace.com/2013/09/09/the-number-of-textual-variants-an-evangelical-miscalculation/"
EHRMAN_MSS = "https://ehrmanblog.org/new-testament-manuscripts-good-news-and-bad-news/"
TOV_DSS = "https://www.degruyterbrill.com/document/doi/10.2478/opth-2014-0007/pdf"
SADEGHI = "https://bible-quran.com/wp-content/uploads/2013/01/Sadeghi-Bergmann-The-Codex-of-a-Companion-of-the-Prophet-and-the-quran-of-the-Prophet.pdf"
COOK_NOTE = "Michael Cook, 'The Stemma of the Regional Codices of the Koran,' Graeco-Arabica 9–10 (2004), 103–104 (quoted by Sidky)"

DEFS = [
    {
        "term": "Variant (Wallace definition)",
        "precise": (
            "Any difference from a base text involving spelling, word order, omission, addition, "
            "substitution, or a rewrite. Counted once per wording, not once per manuscript that has it."
        ),
        "not": "Not 'number of manuscripts × misspellings.' That method invents millions of 'errors.'",
    },
    {
        "term": "Meaningful and viable",
        "precise": (
            "A reading that changes sense AND could plausibly go back to the autograph. "
            "Wallace's generous bucket is a sliver of the raw variant count."
        ),
        "not": "Not 'every footnote in NA28 destroys a doctrine.'",
    },
    {
        "term": "Embarrassment of riches (Metzger–Ehrman)",
        "precise": (
            "Compared with classical authors, NT critics have far more copies and earlier ones. "
            "Quantity is a reconstruction advantage; it is also why the variant count is huge."
        ),
        "not": "Not 'we have the autographs.' Most copies are medieval.",
    },
    {
        "term": "Sidky stemma / four ancestral codices",
        "precise": (
            "Phylogenetic analysis of early Qur'an manuscripts reconstructs four ancestral copies "
            "(Medina, Basra, Kufa, Syria/Ḥimṣ), matching the literary rasm reports of ʿUthmānic exemplars."
        ),
        "not": "Not a photo of ʿUthmān's personal mushaf. Not proof of inspiration.",
    },
    {
        "term": "Textual plurality (Tov / Qumran)",
        "precise": (
            "Qumran biblical scrolls show multiple Hebrew text-forms, probably all treated as Scripture. "
            "Judean Desert sites outside Qumran are virtually identical to later MT."
        ),
        "not": "Not 'rabbis invented Isaiah after Muhammad.' Not 'zero change forever.'",
    },
]

MATERIALS = [
    {
        "id": "p45",
        "title": "Papyrus 𝔓45 (Chester Beatty) — Gospels + Acts",
        "kind": "NT papyrus",
        "tradition": "bible",
        "date": "c. 3rd c. CE",
        "significance": (
            "Substantial 3rd-century witness to the four Gospels and Acts. Shows an early collection "
            "already circulating as a unit — not a medieval invention of the fourfold gospel."
        ),
        "debate_use": "Pair with P46/P75: early, extensive, still 150+ years after Jesus. Do not call it an autograph.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/P45_Matthew.jpg/960px-P45_Matthew.jpg",
        "viewer_url": "https://manuscripts.csntm.org/manuscript/Group/GA_P45",
        "sources": [
            {"label": "CSNTM 𝔓45", "url": "https://manuscripts.csntm.org/manuscript/Group/GA_P45"},
            {"label": "Wikipedia 𝔓45", "url": "https://en.wikipedia.org/wiki/Papyrus_45"},
        ],
    },
    {
        "id": "p75",
        "title": "Papyrus 𝔓75 (Bodmer XIV–XV) — Luke + John",
        "kind": "NT papyrus",
        "tradition": "bible",
        "date": "Late 2nd / early 3rd c. CE (debated)",
        "significance": (
            "Close to the Alexandrian text later seen in Vaticanus. Used to argue that a careful "
            "text-type existed early — not only a wild Western text."
        ),
        "debate_use": "Open against 'the Gospels were rewritten in the 4th century.' Still not first-century ink.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Papyrus_75.jpg/960px-Papyrus_75.jpg",
        "viewer_url": "https://manuscripts.csntm.org/manuscript/Group/GA_P75",
        "sources": [
            {"label": "CSNTM 𝔓75", "url": "https://manuscripts.csntm.org/manuscript/Group/GA_P75"},
            {"label": "Wikipedia 𝔓75", "url": "https://en.wikipedia.org/wiki/Papyrus_75"},
        ],
    },
    {
        "id": "alexandrinus",
        "title": "Codex Alexandrinus (A)",
        "kind": "Greek Bible codex",
        "tradition": "bible",
        "date": "5th c. CE",
        "significance": (
            "Nearly complete Greek Bible. Independent check on Sinaiticus/Vaticanus. "
            "Contains the longer ending of Mark — useful when someone says 'all old Bibles omit it.'"
        ),
        "debate_use": "Show that early complete Bibles do not all agree on Mark 16. That is the file.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Codex_Alexandrinus.jpg/960px-Codex_Alexandrinus.jpg",
        "viewer_url": "https://www.bl.uk/collection-items/codex-alexandrinus",
        "sources": [
            {"label": "British Library Alexandrinus", "url": "https://www.bl.uk/collection-items/codex-alexandrinus"},
            {"label": "CSNTM GA 02", "url": "https://manuscripts.csntm.org/manuscript/Group/GA_02"},
        ],
    },
    {
        "id": "bezae",
        "title": "Codex Bezae (D) — Greek/Latin Gospels + Acts",
        "kind": "Greek–Latin bilingual",
        "tradition": "bible",
        "date": "c. 5th c. CE",
        "significance": (
            "The famous 'Western' text: expansions and paraphrases, especially in Acts. "
            "Proof that some early Christians copied with recensional freedom — the opposite of a frozen rasm."
        ),
        "debate_use": "Christian honesty card. Muslim overclaim card if they treat Bezae as 'the' NT.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Codex_Bezae_Greek.jpg/960px-Codex_Bezae_Greek.jpg",
        "viewer_url": "https://cudl.lib.cam.ac.uk/view/MS-NN-00002-00041/1",
        "sources": [
            {"label": "Cambridge Digital Library — Bezae", "url": "https://cudl.lib.cam.ac.uk/view/MS-NN-00002-00041/1"},
        ],
    },
    {
        "id": "aleppo",
        "title": "Aleppo Codex — Masoretic Hebrew Bible",
        "kind": "Hebrew Bible codex",
        "tradition": "bible",
        "date": "c. 930 CE",
        "significance": (
            "Finest complete-ish medieval MT witness (parts lost in 1947). Older and more prized than Leningrad "
            "for many books. Still a 10th-century complete-book horizon."
        ),
        "debate_use": "Don't hide the date. Answer with DSS proto-MT + LXX. Don't pretend this is Ezra's autograph.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Aleppo_Codex_Joshua_1_1.jpg/960px-Aleppo_Codex_Joshua_1_1.jpg",
        "viewer_url": "https://aleppocodex.org/",
        "sources": [
            {"label": "Aleppo Codex site", "url": "https://aleppocodex.org/"},
            {"label": "Wikipedia Aleppo Codex", "url": "https://en.wikipedia.org/wiki/Aleppo_Codex"},
        ],
    },
    {
        "id": "isaiah-scroll",
        "title": "1QIsaᵃ — Great Isaiah Scroll",
        "kind": "Dead Sea Scroll",
        "tradition": "bible",
        "date": "c. 125–100 BCE",
        "significance": (
            "Nearly complete Isaiah a century+ before Jesus. Recognizably the same book as medieval MT, "
            "with thousands of spelling/word differences. Tov's plurality-and-stability in one object."
        ),
        "debate_use": "Open the IMJ viewer live. Scroll to a famous verse. Ask what 'unchanged' means after you look.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Great_Isaiah_Scroll.jpg/960px-Great_Isaiah_Scroll.jpg",
        "viewer_url": "https://dss.collections.imj.org.il/isaiah",
        "sources": [
            {"label": "IMJ Great Isaiah Scroll", "url": "https://dss.collections.imj.org.il/isaiah"},
            {"label": "Leon Levy DSS library", "url": "https://www.deadseascrolls.org.il/"},
        ],
    },
    {
        "id": "cpp-arabe328",
        "title": "Codex Parisino-Petropolitanus (BnF Arabe 328)",
        "kind": "Early Hijazi Qur'an",
        "tradition": "quran",
        "date": "Later 7th c. CE (Déroche: 3rd quarter of 1st/7th c.)",
        "significance": (
            "Large early ʿUthmānic-type witness (~45% with related leaves). Sidky/van Putten use it as a "
            "regional (Syrian) exemplar descendant. Birmingham 1572a is part of the same codex as 328c."
        ),
        "debate_use": "This is the 'show the page' Qur'an leaf, not a tourist Topkapı flyer.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Birmingham_Quran_manuscript_folio_1_recto.jpg/960px-Birmingham_Quran_manuscript_folio_1_recto.jpg",
        "viewer_url": "https://gallica.bnf.fr/ark:/12148/btv1b8415207g",
        "sources": [
            {"label": "Gallica — Arabe 328", "url": "https://gallica.bnf.fr/ark:/12148/btv1b8415207g"},
            {"label": "Islamic Awareness CPP", "url": "https://www.islamic-awareness.org/quran/text/mss/cpp.html"},
        ],
    },
    {
        "id": "bl-or2165",
        "title": "British Library Or. 2165",
        "kind": "Early Hijazi Qur'an",
        "tradition": "quran",
        "date": "1st/7th – early 8th c. (paleography)",
        "significance": (
            "Major early Hijazi mushaf. Dutton noted Syrian regional rasm variants. "
            "Sidky's phylogeny treats it as a descendant of the Syrian ancestral codex."
        ),
        "debate_use": "Ask: does a regional letter-difference (min / no min) equal 'another Qur'an'?",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Birmingham_Quran_manuscript.jpg/960px-Birmingham_Quran_manuscript.jpg",
        "viewer_url": "https://www.bl.uk/collection-items/quran-from-the-8th-century",
        "sources": [
            {"label": "BL collection item", "url": "https://www.bl.uk/collection-items/quran-from-the-8th-century"},
            {"label": "Islamic Awareness Or. 2165", "url": "https://www.islamic-awareness.org/quran/text/mss/bl.html"},
        ],
    },
    {
        "id": "tubingen",
        "title": "Tübingen Ma VI 165",
        "kind": "Early Hijazi/Kufic Qur'an",
        "tradition": "quran",
        "date": "C-14 often cited no later than 675 CE (95.4%)",
        "significance": (
            "Another first-Islamic-century witness (~¼ of the text in some counts). "
            "Used with Birmingham/CPP to show a cluster, not a singleton miracle leaf."
        ),
        "debate_use": "C-14 caveat still applies. Strength is the cluster of 7th-c. ʿUthmānic-type copies.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Birmingham_Quran_manuscript_folio_1_recto.jpg/960px-Birmingham_Quran_manuscript_folio_1_recto.jpg",
        "viewer_url": "https://www.islamic-awareness.org/quran/text/mss/tubingen.html",
        "sources": [
            {"label": "Islamic Awareness Tübingen", "url": "https://www.islamic-awareness.org/quran/text/mss/tubingen.html"},
        ],
    },
    {
        "id": "csntm-hub",
        "title": "CSNTM — Center for the Study of NT Manuscripts",
        "kind": "Research infrastructure",
        "tradition": "infra",
        "date": "Ongoing (Wallace)",
        "significance": (
            "High-resolution images of Greek NT manuscripts. The Christian 'open the leaf' desk. "
            "Use when someone says variants are hidden."
        ),
        "debate_use": "Search GA P52 / 01 / 03 live. Then do the same move on Corpus Coranicum.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5c/P46.jpg",
        "viewer_url": "https://manuscripts.csntm.org/",
        "sources": [
            {"label": "CSNTM manuscript viewer", "url": "https://manuscripts.csntm.org/"},
        ],
    },
    {
        "id": "nquran",
        "title": "nquran.com — ten qirāʾāt / twenty rāwīs",
        "kind": "Reading-tradition viewer",
        "tradition": "infra",
        "date": "Living oral–written corpus",
        "significance": (
            "Verse-by-verse display of how each canonical transmitter reads the same āyah. "
            "The live antidote to a Hyde Park table of 'different Qur'ans.'"
        ),
        "debate_use": "Open Fātiḥa 4 (Mālik/Malik) and 3:26 (only Mālik). That is Ataie's constraint argument on a screen.",
        "image": "",
        "viewer_url": "https://nquran.com",
        "sources": [
            {"label": "nquran.com", "url": "https://nquran.com"},
        ],
    },
]

# Patch broken / placeholder images on existing gallery items.
IMAGE_FIXES = {
    "p66": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Papyrus_66.jpg/960px-Papyrus_66.jpg",
        "tradition": "bible",
    },
    "vaticanus": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Codex_Vaticanus.jpg/960px-Codex_Vaticanus.jpg",
        "tradition": "bible",
    },
    "p52": {"tradition": "bible"},
    "p52-annotated": {"tradition": "bible"},
    "sinaiticus": {"tradition": "bible"},
    "dss": {"tradition": "bible"},
    "p46": {"tradition": "bible"},
    "leningrad": {"tradition": "bible"},
    "intf": {"tradition": "infra"},
    "csntm-hub": {"tradition": "infra"},
    "nquran": {"tradition": "infra"},
    "birmingham": {"tradition": "quran"},
    "birmingham-spread": {"tradition": "quran"},
    "sanaa": {
        "tradition": "quran",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Sanaa_manuscript.jpg/960px-Sanaa_manuscript.jpg",
    },
    "corpus-coranicum": {"tradition": "quran"},
    "bukhari-4987": {
        "tradition": "quran",
        "image": "",
    },
    "ataie-sound-narrative": {"tradition": "quran"},
}

OVERLAYS = {
    "uthmanic-rasm": {
        "muslim": {
            "quotes": [
                Q(
                    "This process of reconstruction identifies four ancestral codices from which all examined manuscripts descend. … Additional evidence is presented for the historicity of the ʿUthmānic canonization and the distribution of four regional exemplars.",
                    "Hythem Sidky",
                    "JIQSA 5 (2020), abstract: On the Regionality of Qurʾānic Codices",
                    SIDKY_JIQSA,
                ),
                Q(
                    "By all indications, the manuscript evidence is consistent with the traditional narrative regarding the ʿUthmānic standardization.",
                    "Hythem Sidky",
                    "Al-ʿUṣūr al-Wusṭā 27 (2019), review of Brubaker, p. 278",
                    SIDKY_REVIEW,
                ),
                Q(
                    "As long as no Quranic passages with a distinct stylistic and terminological profile have been compellingly placed in a late seventh-century context, the traditional dating of the standard rasm (excepting certain orthographical features) to 650 or earlier ought to be our default view.",
                    "Nicolai Sinai",
                    "BSOAS 77.3 (2014), 'When did the consonantal skeleton… Part II'",
                    SINAI_II,
                ),
                Q(
                    "This must count against any suggestion that the variants were invented … We can accordingly infer that we have to do with genuine transmissions from an archetype.",
                    "Michael Cook",
                    COOK_NOTE,
                    "https://www.middleeastmedievalists.com/wp-content/uploads/2019/11/UW-27-Sidky.pdf",
                ),
            ],
            "data_points": [
                D("Sidky: Ḥimṣ, not Damascus, is the likelier city for the Syrian exemplar.", "JIQSA 5 abstract", SIDKY_JIQSA),
                D("Sidky: knowledge of regional rasm variants was accumulated later by inspecting regional muṣḥafs — not a committee press-release in 650.", "JIQSA 5 abstract", SIDKY_JIQSA),
                D("Déroche dates Codex Parisino-Petropolitanus to the 3rd quarter of the 1st/7th c.; it already has the van Putten idiosyncrasies.", "Sidky citing Déroche 2009", SIDKY_REVIEW),
            ],
            "manuscripts": [
                M("BnF Arabe 328 (CPP)", "https://gallica.bnf.fr/ark:/12148/btv1b8415207g", "Early ʿUthmānic-type Hijazi"),
                M("BL Or. 2165", "https://www.bl.uk/collection-items/quran-from-the-8th-century", "Syrian regional rasm"),
            ],
            "sources": [
                S("Sidky JIQSA 5", SIDKY_JIQSA),
                S("Sinai BSOAS 2014 II", SINAI_II),
                S("Sidky Brubaker review (quotes Cook/Sinai/van Putten)", SIDKY_REVIEW),
            ],
        },
        "christian": {
            "quotes": [
                Q(
                    "A comparison of literary reports against the earliest manuscripts reveals that knowledge of the regional variants does not date back to the time of canonization but was accumulated over time through careful scrutiny of regional muṣḥafs.",
                    "Hythem Sidky",
                    "JIQSA 5 (2020), abstract",
                    SIDKY_JIQSA,
                ),
            ],
            "data_points": [
                D("Sidky grants: no surviving copy is identified as one of the four actual ʿUthmānic master copies. He says that is not odd given loss and wear.", "Review pp. 277–278", SIDKY_REVIEW),
            ],
        },
        "live": {
            "if_they_say": "Uthman burned the evidence so the Qur'an is unreliable.",
            "you_say": "Sidky: surviving MSS reconstruct four ancestral regional copies and match the literary stemma. Cook: that pattern counts against invented variants. Burning rivals ≠ late invention of the rasm we have.",
            "dont_overclaim": "Don't claim we have ʿUthmān's autograph. Don't treat a stemma as a miracle.",
        },
    },
    "brubaker": {
        "muslim": {
            "quotes": [
                Q(
                    "If the objective of Brubaker's book is to demonstrate the humanity of the scribes involved in transmitting the Quranic text, it certainly succeeds. … Where it falls short, however, is in its methodology and analysis. … The vast majority of examples in the book are best explained through simple scribal error. The main thesis, namely, that the flexibility of the Quranic text persisted centuries beyond its standardization, remains unproven.",
                    "Hythem Sidky",
                    "Al-ʿUṣūr al-Wusṭā 27 (2019), pp. 287–288",
                    SIDKY_REVIEW,
                ),
                Q(
                    "Corrections apparently in the direction of conformity to the Cairo edition are not evidence of a changing standard, but evidence of the existence of a standard in the first place.",
                    "Hythem Sidky",
                    "Same review, p. 276",
                    SIDKY_REVIEW,
                ),
            ],
        },
        "christian": {
            "quotes": [
                Q(
                    "We are told that a survey of these manuscripts … will 'challenge the traditional assertions about the transmission of the Quran' … Unfortunately, the bold claims are left unsubstantiated.",
                    "Hythem Sidky (stating Brubaker's claim, then rejecting it)",
                    "Al-ʿUṣūr al-Wusṭā 27 (2019), p. 273",
                    SIDKY_REVIEW,
                ),
            ],
        },
        "live": {
            "if_they_say": "Brubaker's photos show corruption.",
            "you_say": "Sidky opened the same photos: most are parablepsis / assimilation of parallels. Convergence on Cairo 1924 is anachronistic — Cairo used medieval rasm books and is more archaic than later classicized mushafs.",
            "dont_overclaim": "Don't pretend scribes never erred. Don't treat every overstrike as a council rewriting doctrine.",
        },
    },
    "qiraat-holes": {
        "muslim": {
            "quotes": [
                Q(
                    "A careful study of the consonantal dotting patterns between the canonical readings reveals independent Medinan, Meccan-Basran, and Kufan regional traditions. … I demonstrate the existence of an inherited oral tradition that likely dates to the time of the ʿUthmānic recension and among the first generation of the followers of Muḥammad.",
                    "Hythem Sidky",
                    "JAOS 143.4 (2023), abstract: Consonantal Dotting and the Oral Quran",
                    SIDKY_JAOS,
                ),
            ],
            "data_points": [
                D("Sidky's target: the claim that qirāʾāt are just later decipherments of a dead rasm with no living oral stream.", "JAOS 2023 abstract", SIDKY_JAOS),
            ],
            "manuscripts": [
                M("nquran.com — 20 transmitters", "https://nquran.com", "See the oral tradition on the page"),
            ],
        },
    },
    "nt-variants": {
        "christian": {
            "quotes": [
                Q(
                    "A variant is simply the difference in wording found in a single manuscript or a group of manuscripts (either way, it's still only one variant) that disagrees with a base text. Further, there aren't only 200,000. … The estimates today are closer to 400,000.",
                    "Daniel B. Wallace",
                    "The Number of Textual Variants: An Evangelical Miscalculation (2013)",
                    WALLACE_COUNT,
                ),
                Q(
                    "In contrast with these figures, the textual critic of the New Testament is embarrassed by the wealth of material. … Several papyrus manuscripts of portions of the New Testament are extant that were copied within a century or so after the composition of the original documents.",
                    "Bruce M. Metzger and Bart D. Ehrman",
                    "The Text of the New Testament, 4th ed., p. 51",
                    "https://global.oup.com/academic/product/the-text-of-the-new-testament-9780195161229",
                ),
                Q(
                    "Indeed, so extensive are these citations that if all other sources for our knowledge of the text of the New Testament were destroyed, they would be sufficient alone for the reconstruction of practically the entire New Testament.",
                    "Bruce M. Metzger and Bart D. Ehrman",
                    "The Text of the New Testament (standard editions, church-fathers chapter)",
                    "https://global.oup.com/academic/product/the-text-of-the-new-testament-9780195161229",
                ),
            ],
            "manuscripts": [
                M("CSNTM viewer", "https://manuscripts.csntm.org/", "Open a leaf mid-round"),
                M("Codex Vaticanus Vat.gr.1209", "https://digi.vatlib.it/view/MSS_Vat.gr.1209", "Alexandrian complete-ish Bible"),
                M("Codex Bezae", "https://cudl.lib.cam.ac.uk/view/MS-NN-00002-00041/1", "Western expansions"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Apart from the smallest fragments, no two of our manuscripts are exactly alike. … It is probably easiest to put the matter in comparative terms: there are more differences in our manuscripts than there are words in the New Testament.",
                    "Bart D. Ehrman",
                    "New Testament Manuscripts: Good News and Bad News (blog)",
                    EHRMAN_MSS,
                ),
                Q(
                    "Most of our manuscripts are from the Middle Ages, many centuries—over a thousand years!—after the originals.",
                    "Bart D. Ehrman",
                    "Same essay",
                    EHRMAN_MSS,
                ),
            ],
            "manuscripts": [
                M("Sinaiticus — Mark ending", "https://codexsinaiticus.org/en/manuscript.aspx?book=34", "16:9–20 absent"),
                M("Vaticanus digital", "https://digi.vatlib.it/view/MSS_Vat.gr.1209", "Same absence"),
            ],
        },
        "live": {
            "if_they_say": "There are 400,000 New Testament variants.",
            "you_say": "Wallace: a variant is a wording difference, counted once. Ehrman agrees the count is huge AND most are spelling. Name one that is meaningful and viable — then open NA28 / Sinaiticus.",
            "dont_overclaim": "Don't claim autographs. Don't claim zero loaded variants. Don't multiply one misspelling by 4,000 copies.",
        },
    },
    "ot-dss": {
        "christian": {
            "quotes": [
                Q(
                    "The Qumran finds (more than 200 fragmentary scrolls) reflect textual plurality, and all the biblical texts were probably considered authoritative. At the same time, the 25 Scripture scrolls from sites in the Judean Desert outside Qumran are virtually identical to the medieval MT.",
                    "Emanuel Tov",
                    "Open Theology / DSS 65-years essay (abstract + body)",
                    TOV_DSS,
                ),
            ],
            "manuscripts": [
                M("1QIsaᵃ IMJ viewer", "https://dss.collections.imj.org.il/isaiah", "Scroll a verse live"),
                M("Aleppo Codex", "https://aleppocodex.org/", "Medieval MT quality"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "When trying to understand the textual situation of the Torah in the Second Temple period, we are faced with a veritable textual plurality that is probably reflected in some ten different textual branches, more than in the other Scripture books.",
                    "Emanuel Tov",
                    "The Two-Fold Division of the Textual Transmission of the Torah",
                    "https://openscholar.huji.ac.il/sites/default/files/he_bible_project/files/e._tov1.pdf",
                ),
            ],
        },
        "live": {
            "if_they_say": "The Old Testament is a medieval book (Leningrad 1008).",
            "you_say": "Leningrad is the oldest complete MT copy. Tov: non-Qumran Judean Desert scrolls are virtually identical to that medieval text; Qumran itself is plural. Open 1QIsaᵃ.",
            "dont_overclaim": "Don't say DSS prove zero variation. Don't say rabbis invented Isaiah after the Qur'an.",
        },
    },
    "birmingham": {
        "muslim": {
            "quotes": [
                Q(
                    "Radiocarbon dating of Quranic fragments has also pushed some manuscripts back to the mid-first/seventh century or before, giving us an unprecedented window into the scripture as it was written, handled, and received by the earliest generation of Muslims.",
                    "Hythem Sidky",
                    "Al-ʿUṣūr al-Wusṭā 27 (2019), p. 273",
                    SIDKY_REVIEW,
                ),
            ],
        },
    },
    "sanaa": {
        "muslim": {
            "manuscripts": [
                M("Islamic Awareness C-1 dossier", "https://www.islamic-awareness.org/quran/text/mss/soth.html", "Images + literature"),
            ],
        },
    },
}

ARGUMENTS = [
    {
        "id": "nt-papyri-gap",
        "rank": 16,
        "cluster": "Bible text",
        "title": "First-century NT silence vs 7th-century Qur'an cluster",
        "type": "history + method",
        "popularity": "The comparison slide both sides want",
        "why_it_matters": (
            "This is the fair comparison: not 'my book vs your slogan,' but extant ink in the century of origin. "
            "Christians should own the gap. Muslims should not smuggle inspiration out of C-14."
        ),
        "christian": {
            "claim": (
                "Zero first-century NT papyri does not mean a 4th-century invention. P52/P66/P75/P46 sit "
                "inside ~100–170 years of composition; classical baselines are worse."
            ),
            "case": (
                "Metzger–Ehrman: several papyri within a century or so of composition; church-father citations "
                "could reconstruct almost the whole NT. The gap is real; the reconstruction engine is also real."
            ),
            "quotes": [
                Q(
                    "Several papyrus manuscripts of portions of the New Testament are extant that were copied within a century or so after the composition of the original documents.",
                    "Metzger and Ehrman",
                    "The Text of the New Testament, 4th ed., p. 51",
                    "https://global.oup.com/academic/product/the-text-of-the-new-testament-9780195161229",
                ),
            ],
            "data_points": [
                D("P52: credit-card John 18, usually 125–175 CE — not first century.", "CSNTM / standard handbooks"),
                D("Complete-ish Gospels: Sinaiticus/Vaticanus, mid-4th c.", "codexsinaiticus.org; DigiVatLib"),
            ],
            "manuscripts": [
                M("P52", "https://manuscripts.csntm.org/Manuscript/View/GA_P52", "Earliest often-cited scrap"),
                M("P46", "https://en.wikipedia.org/wiki/Papyrus_46", "Paul c. 200"),
                M("P75", "https://manuscripts.csntm.org/manuscript/Group/GA_P75", "Luke–John"),
            ],
            "sources": [
                S("Metzger–Ehrman TNT", "https://global.oup.com/academic/product/the-text-of-the-new-testament-9780195161229"),
                S("CSNTM", "https://manuscripts.csntm.org/"),
            ],
        },
        "muslim": {
            "claim": (
                "In the first Islamic century we already have multiple Hijazi witnesses covering essentially "
                "the ʿUthmānic rasm. That proximity is not matched by first-century Christian papyri."
            ),
            "case": (
                "Sidky: C-14 has pushed some fragments to mid-1st/7th c. or before. Birmingham+328c, Tübingen, "
                "CPP, Or. 2165 form a cluster. Comparison is allowed if both sides use the same rule: extant ink, not piety."
            ),
            "quotes": [
                Q(
                    "Radiocarbon dating of Quranic fragments has also pushed some manuscripts back to the mid-first/seventh century or before, giving us an unprecedented window into the scripture as it was written, handled, and received by the earliest generation of Muslims.",
                    "Hythem Sidky",
                    "Al-ʿUṣūr al-Wusṭā 27 (2019), p. 273",
                    SIDKY_REVIEW,
                ),
            ],
            "data_points": [
                D("Ataie/Sidky coverage claim: ʿUthmānic text essentially complete among 7th-c. witnesses — a coverage argument, not one complete dated mushaf.", "Historicity Ataie card + Sidky field"),
            ],
            "manuscripts": [
                M("Birmingham / Mingana 1572a", "http://vmr.bham.ac.uk/Collections/Mingana/Islamic_Arabic_1572a/table/", "C-14 568–645 parchment"),
                M("Gallica Arabe 328", "https://gallica.bnf.fr/ark:/12148/btv1b8415207g", "Same-codex / CPP"),
            ],
            "sources": [
                S("Sidky review", SIDKY_REVIEW),
                S("Islamic Awareness 1st-c. list", "https://www.islamic-awareness.org/quran/text/mss/"),
            ],
        },
        "counters": [
            {
                "against": "Muslim knock-out comparison",
                "claim": "Zero first-century NT MSS means the Gospels are late fiction.",
                "reply": "Absence of 1st-c. copies ≠ 4th-c. composition. Paul is 50s; P52 is 2nd c. Own the gap; don't invent a conspiracy.",
            },
            {
                "against": "Christian whataboutism",
                "claim": "Classical works are worse, so the NT gap doesn't matter.",
                "reply": "Classical baseline helps quantity. It does not create first-century Gospel autographs. Stay in the same metric.",
            },
        ],
        "live": {
            "if_they_say": "There are no first-century New Testament manuscripts, so the Bible is late.",
            "you_say": "Correct on extant 1st-c. ink. Then: P52/P66/P46 inside ~100–170 years, vs Qur'an leaves inside the first Hijrī century. Score proximity. Don't score inspiration from that.",
            "dont_overclaim": "Don't date Birmingham ink to 568. Don't treat P52 as 'John's handwriting.'",
        },
        "crux": "Are we comparing extant witnesses in the century of origin, or theological reliability?",
        "debate_use": "Open P52 and Birmingham on two tabs. State the metric before the slide.",
        "counter_to_christian": "The first-century silence is still a fact the audience can see.",
        "counter_to_muslim": "A 7th-century rasm cluster is not a lab sticker that says 'every aḥruf recited today.'",
    },
    {
        "id": "mark16-john8",
        "rank": 17,
        "cluster": "Bible text",
        "title": "Showcase variants: Mark 16:9–20 and John 7:53–8:11",
        "type": "history",
        "popularity": "The two pages you must be able to open",
        "why_it_matters": (
            "These are not spelling. Christians read them as Scripture for centuries; critical editions now "
            "bracket or omit them. That is either honesty or instability — name which claim you are making."
        ),
        "christian": {
            "claim": (
                "Critical editions flag the longer ending of Mark and the Pericope Adulterae because the "
                "earliest Alexandrian witnesses lack them. Publishing the problem is the opposite of a cover-up."
            ),
            "case": (
                "Sinaiticus and Vaticanus omit Mark 16:9–20. The adulteress pericope is missing from the "
                "earliest papyri and those two codices. NA28/UBS print the data. Doctrine of resurrection "
                "does not rest on Mark 16:9–20 (1 Cor 15 is earlier)."
            ),
            "quotes": [
                Q(
                    "It is quite true that (virtually) no viable variants are major threats to inerrancy; the major problems that the doctrine of inerrancy faces are essentially never found in textually disputed passages in which one reading creates the problem and another erases it.",
                    "Daniel B. Wallace",
                    "The Number of Textual Variants (2013)",
                    WALLACE_COUNT,
                ),
            ],
            "data_points": [
                D("Mark 16:9–20 absent in א and B; present in A and the majority later tradition.", "NA28 apparatus"),
                D("John 7:53–8:11 absent from P66, P75, א, B.", "NA28"),
            ],
            "manuscripts": [
                M("Sinaiticus Mark 16", "https://codexsinaiticus.org/en/manuscript.aspx?book=34", "Show the stop at 16:8"),
                M("Alexandrinus (has longer ending)", "https://www.bl.uk/collection-items/codex-alexandrinus", "Not all old copies omit it"),
            ],
            "sources": [
                S("NA28 / INTF", "https://www.uni-muenster.de/INTF/"),
                S("Wallace 2013", WALLACE_COUNT),
            ],
        },
        "muslim": {
            "claim": (
                "If Christians can demote passages that were printed as Scripture for a millennium, "
                "'we know the original' is a modern editorial achievement, not a preserved autograph."
            ),
            "case": (
                "The audience lived and died hearing Mark 16 and John 8 as the Bible. That is closer to "
                "Ataie's Johannine Comma point: later authorized Bibles contained secondary text. "
                "The Qur'anic parallel would be reciting a shādhdh reading in ṣalāh as if it were mutawātir."
            ),
            "quotes": [
                Q(
                    "There are lots of differences that do matter a lot.",
                    "Bart D. Ehrman",
                    "New Testament Manuscripts: Good News and Bad News",
                    EHRMAN_MSS,
                ),
            ],
            "data_points": [
                D("KJV / liturgical use treated both passages as canonical for centuries.", "Reception history"),
            ],
            "manuscripts": [
                M("Sinaiticus", "https://codexsinaiticus.org/en/", "Open Mark 16 live"),
            ],
            "sources": [
                S("Ehrman blog", EHRMAN_MSS),
            ],
        },
        "counters": [
            {
                "against": "Muslim 'the Bible added stories'",
                "claim": "Christians just invented the resurrection ending.",
                "reply": "1 Cor 15 is 20+ years after the event and independent of Mark 16:9–20. Fight the passage, not the creed, unless you have a better 1st-c. source.",
            },
        ],
        "live": {
            "if_they_say": "The Bible has extra stories later scribes added.",
            "you_say": "Name Mark 16 and John 8. Open Sinaiticus. Then ask whether NA28 bracketing them is corruption or disclosure. Don't pretend 1 Cor 15 depends on Mark's ending.",
            "dont_overclaim": "Don't say no early copy has the longer ending (Alexandrinus does). Don't say these variants are 'just spelling.'",
        },
        "crux": "Is a later-recognized secondary passage proof of collapse, or proof that the apparatus works?",
        "debate_use": "Have two URLs ready. Speak for 40 seconds. Sit down.",
        "counter_to_christian": "Reception history still matters: people trusted a longer Bible.",
        "counter_to_muslim": "If you use this file, you owe the same honesty on companion rasm and C-1.",
    },
    {
        "id": "sidky-oral-qiraat",
        "rank": 18,
        "cluster": "Qur'an text",
        "title": "Sidky: qirāʾāt as inherited oral tradition, not crossword vowels",
        "type": "history + method",
        "popularity": "The academic version of Ataie's Yā-Sīn argument",
        "why_it_matters": (
            "Goldziher/Jeffery-style 'they dotted an empty skeleton' is still the polemic default. "
            "Sidky 2023 is the journal article you cite instead of a vibe."
        ),
        "christian": {
            "claim": (
                "Even if regional oral streams are old, they are still human recitational systems sitting on "
                "an undotted rasm. That is licensed multiplicity, not clone-identity."
            ),
            "case": (
                "Sidky's own JIQSA abstract says knowledge of regional rasm variants accumulated later. "
                "Press the definition: preservation of a living corpus vs preservation of one recitation."
            ),
            "quotes": [
                Q(
                    "A comparison of literary reports against the earliest manuscripts reveals that knowledge of the regional variants does not date back to the time of canonization but was accumulated over time through careful scrutiny of regional muṣḥafs.",
                    "Hythem Sidky",
                    "JIQSA 5 (2020), abstract",
                    SIDKY_JIQSA,
                ),
            ],
            "data_points": [
                D("Undotted early rasm can host more than one reading; that is why ʿUthmān (in the traditional story) left it undotted.", "Ataie / classical ʿulūm"),
            ],
            "manuscripts": [
                M("nquran.com", "https://nquran.com", "Show two rāwīs of one eponym"),
            ],
            "sources": [
                S("Sidky JIQSA", SIDKY_JIQSA),
            ],
        },
        "muslim": {
            "claim": (
                "Canonical readings are not free ijtihād on a crossword. Sidky finds regional dotting patterns "
                "that look inherited from the first generation after Muhammad, not Abbasid invention."
            ),
            "case": (
                "JAOS 2023: independent Medinan, Meccan-Basran, and Kufan traditions; statistical + manuscript "
                "evidence for an oral stream at the ʿUthmānic recension. Pair with the Yā-Sīn pointing constraint."
            ),
            "quotes": [
                Q(
                    "I demonstrate the existence of an inherited oral tradition that likely dates to the time of the ʿUthmānic recension and among the first generation of the followers of Muḥammad.",
                    "Hythem Sidky",
                    "JAOS 143.4 (2023), abstract",
                    SIDKY_JAOS,
                ),
            ],
            "data_points": [
                D("Sidky: some scholars claimed canonical readings are decipherments of the ʿUthmānic text with no living oral tradition — that is the thesis he is testing.", "JAOS 2023 abstract", SIDKY_JAOS),
            ],
            "manuscripts": [
                M("nquran.com", "https://nquran.com", "Oral tradition, verse by verse"),
                M("Corpus Coranicum", "https://corpuscoranicum.de/en/manuscripts", "Early undotted rasm"),
            ],
            "sources": [
                S("Sidky JAOS 2023", SIDKY_JAOS),
            ],
        },
        "counters": [
            {
                "against": "Christian Goldziher",
                "claim": "Reciters just guessed vowels.",
                "reply": "Then why is 3:26 only Mālik among the ten, and Yā-Sīn only one pointing? Sidky: inherited regional oral streams.",
            },
        ],
        "live": {
            "if_they_say": "Qirāʾāt are just later guesses on an empty skeleton.",
            "you_say": "Sidky JAOS 2023: inherited oral tradition likely to the ʿUthmānic generation. Open nquran.com on the verse they named.",
            "dont_overclaim": "Don't say every popular street reading is mutawātir. Don't say Sidky proved wahy.",
        },
        "crux": "Are the ten readings recovered from dots, or received with the rasm?",
        "debate_use": "Cite Sidky, then demonstrate on nquran.com. One minute.",
        "counter_to_christian": "Free pointing would have produced tens of thousands of variants; we have hundreds to low thousands of wording sites.",
        "counter_to_muslim": "An old oral stream can still be human. Age ≠ revelation.",
    },
]

CARDS = [
    {
        "trigger": "Sidky is just a Muslim apologist",
        "fast_answer": "University of Chicago / IQSA. His Brubaker review and JIQSA stemma are the papers critics also have to cite. Quote the page, don't psychoanalyze the man.",
        "follow_up": "If you reject Sidky's stemma, name the competing phylogeny.",
        "sources": [SIDKY_REVIEW, SIDKY_JIQSA],
    },
    {
        "trigger": "There are 200,000 errors in the New Testament",
        "fast_answer": "Wallace: that number used a broken definition (wording × manuscripts). Real critic-count is ~400,000 wording differences, mostly spelling. Ask for a meaningful-and-viable example.",
        "follow_up": "Open Wallace 2013 on a phone. Then open Mark 16 on Sinaiticus.",
        "sources": [WALLACE_COUNT],
    },
    {
        "trigger": "Leningrad Codex is 1008 so the OT is medieval",
        "fast_answer": "Oldest complete MT copy is medieval. Tov: 25 Judean Desert scripture scrolls outside Qumran are virtually identical to that medieval text. Open 1QIsaᵃ.",
        "follow_up": "Grant Qumran plurality (Jeremiah/Samuel/LXX-like). That is Tov, not a dawah meme.",
        "sources": [TOV_DSS],
    },
    {
        "trigger": "Show me Uthman's original mushaf",
        "fast_answer": "Sidky: it is not odd that the four master copies did not survive handling. What survived is a four-node stemma plus early Hijazi leaves. Demand a stemma, not a relic.",
        "follow_up": "Drop Topkapı-as-autograph flyers before they drop them for you.",
        "sources": [SIDKY_REVIEW],
    },
    {
        "trigger": "The church fathers hid the real Bible",
        "fast_answer": "Metzger–Ehrman: patristic citations are so extensive you could reconstruct practically the entire NT from them alone. That is the opposite of a hidden text — it is a noisy, public text.",
        "follow_up": "Noise is why there are variants. Publicity is why we can map them.",
        "sources": ["Metzger–Ehrman, Text of the New Testament"],
    },
    {
        "trigger": "Cairo 1924 invented today's Qur'an",
        "fast_answer": "Sidky: Cairo chose among medieval rasm books (Dānī / Abū Dāwūd) and is often more archaic than classicized later mushafs. Corrections 'toward Cairo' are corrections toward an old standard, not a 1924 novelty.",
        "follow_up": "Warsh prints still exist. 1924 is a Hafs typesetting, not a new rasm.",
        "sources": [SIDKY_REVIEW],
    },
]

BIB_ITEMS = [
    {"label": "Hythem Sidky — review of Brubaker (PDF)", "url": SIDKY_REVIEW},
    {"label": "Hythem Sidky — On the Regionality of Qurʾānic Codices (JIQSA 5)", "url": SIDKY_JIQSA},
    {"label": "Hythem Sidky — Consonantal Dotting and the Oral Quran (JAOS 2023)", "url": SIDKY_JAOS},
    {"label": "Nicolai Sinai — When did the consonantal skeleton… Part II (BSOAS 2014)", "url": SINAI_II},
    {"label": "Marijn van Putten — The Grace of God (BSOAS 2019)", "url": VAN_PUTTEN},
    {"label": "Daniel Wallace — How to count NT variants (2013)", "url": WALLACE_COUNT},
    {"label": "Metzger & Ehrman — The Text of the New Testament", "url": "https://global.oup.com/academic/product/the-text-of-the-new-testament-9780195161229"},
    {"label": "Bart Ehrman — NT manuscripts good news / bad news", "url": EHRMAN_MSS},
    {"label": "Emanuel Tov — DSS and textual plurality", "url": TOV_DSS},
    {"label": "CSNTM manuscript viewer", "url": "https://manuscripts.csntm.org/"},
    {"label": "Corpus Coranicum", "url": "https://corpuscoranicum.de/en/manuscripts"},
]


def apply_image_fixes(materials: list[dict]) -> list[dict]:
    out = []
    have = set()
    for m in materials:
        m = dict(m)
        fix = IMAGE_FIXES.get(m.get("id") or "")
        if fix:
            for k, v in fix.items():
                if v or k == "image":
                    m[k] = v
        if "tradition" not in m:
            title = (m.get("title") or "") + (m.get("kind") or "")
            if any(x in title.lower() for x in ("qur", "mushaf", "hijazi", "bukhari", "sana", "birmingham")):
                m["tradition"] = "quran"
            elif any(x in title.lower() for x in ("papyrus", "codex", "nt ", "hebrew", "dss", "isaiah", "leningrad")):
                m["tradition"] = "bible"
        have.add(m.get("id"))
        out.append(m)
    for m in MATERIALS:
        if m["id"] not in have:
            out.append(m)
    return out
