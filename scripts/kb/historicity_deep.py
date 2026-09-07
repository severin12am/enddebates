# -*- coding: utf-8 -*-
"""Top-10 historicity arguments with quotes, data points, nested counters, manuscripts."""

def Q(text, who, work, url=None):
    d = {"text": text, "who": who, "work": work}
    if url:
        d["url"] = url
    return d


def S(label, url, note=None):
    d = {"label": label, "url": url}
    if note:
        d["note"] = note
    return d


def D(fact, source, url=None):
    d = {"fact": fact, "source": source}
    if url:
        d["url"] = url
        d["label"] = fact
        d["note"] = source
    return d


def M(label, url, note):
    return {"label": label, "url": url, "note": note, "title": label}


TOP10 = [
    {
        "id": "qiraat-holes",
        "rank": 1,
        "importance": "Top 10",
        "cluster": "Qur'an text",
        "title": "Letter-perfect preservation vs ahruf / qira'at",
        "type": "definition + history",
        "popularity": "The live-debate killer after 2020",
        "why_it_matters": (
            "This is the most common street claim ('every letter identical') colliding with the most common "
            "academic complexity (seven ahruf, ten qira'at). If you don't pin the preservation thesis, you talk past each other."
        ),
        "christian": {
            "claim": (
                "If preservation means one dictated wording reproduced letter-for-letter, multiple canonical readings "
                "with occasional meaning differences falsify the slogan. Yasir Qadhi said the standard narrative has holes."
            ),
            "case": (
                "Hafs vs Warsh (and the ten canonical qira'at) are not 'pronunciation only' in every verse. "
                "Examples used in debates: Q 2:184 fidyatun ta'ami miskin / masakin; Q 3:146 qatala / qutila; "
                "Q 85:22 mahfuzin / mahfuzun. Christian apologists treat Qadhi 2020 as peer testimony against folk dawah."
            ),
            "quotes": [
                Q(
                    "It's very clear that the standard narrative has holes in it. That's what I'm gonna say. The standard narrative does not answer some very pressing questions.",
                    "Yasir Qadhi",
                    "Interview with Mohammed Hijab, 8 June 2020",
                    "https://en.wikipedia.org/wiki/Yasir_Qadhi",
                ),
                Q(
                    "These are very, very difficult issues and the most advanced of our scholars, they're not quite fully certain how to solve all of the unanswered questions.",
                    "Yasir Qadhi",
                    "Same interview (ahruf/qira'at discussion)",
                    "https://www.worldviewsummit.org/post/muslim-scholar-says-holes-in-traditional-account-of-quran",
                ),
            ],
            "data_points": [
                D("Ten canonical qira'at (plus famous non-canonical reports) are taught as Qur'an, not as 'errors'.", "Classical qira'at literature; Ibn Mujahid's seven"),
                D("Some variants change grammar/meaning, not only dialect phonetics.", "Standard comparison lists Hafs/Warsh"),
                D("Qadhi later distinguished 'holes in the dictation model of ahruf/qira'at' from 'the Qur'an is unpreserved'.", "Wikipedia summary of Qadhi 2024 chapter"),
            ],
            "manuscripts": [
                M("Compare Hafs 1924 Cairo vs Warsh Maghribi prints of the same surah", "https://quran.com", "Printed witnesses of two canonical readings"),
            ],
            "sources": [
                S("Wikipedia — Qadhi ahruf/qira'at remarks", "https://en.wikipedia.org/wiki/Yasir_Qadhi"),
                S("Yaqeen — Uthmanic Codex (how qira'at sit on rasm)", "https://yaqeeninstitute.org/read/paper/the-uthmanic-codex-understanding-how-the-quran-was-preserved"),
            ],
        },
        "muslim": {
            "claim": (
                "Preservation includes licensed multiplicity inside an Uthmanic rasm. Qira'at are authorized recitation "
                "modes, not rival books. Folk 'PDF-identical' claims are the problem, not the manuscript record."
            ),
            "case": (
                "Hadith of seven ahruf is early. Uthmanic rasm can host multiple vowelizations/hamzas. "
                "van Putten: almost all manuscripts share one Uthmanic text-type. Qadhi was attacking a brittle "
                "popular story, then proposed a 'divine permission' model rather than 'the Qur'an is lost'."
            ),
            "quotes": [
                Q(
                    "All Quranic manuscripts, with one exception, belong to the same Uthmanic text type.",
                    "Marijn van Putten",
                    "BSOAS 82 (2019), 'The Grace of God'…",
                    "https://doi.org/10.1017/s0041977x19000338",
                ),
                Q(
                    "Qadhi later insisted that he was only referring to the preservation of the Qira'at and Ahruf themselves rather than to the preservation of the Qur'an.",
                    "Secondary summary of Qadhi's clarification",
                    "Wikipedia: Yasir Qadhi",
                    "https://en.wikipedia.org/wiki/Yasir_Qadhi",
                ),
            ],
            "data_points": [
                D("Canonical qira'at are constrained by the Uthmanic consonantal skeleton.", "Classical usul al-qira'at"),
                D("Muslims have recited multiple accepted readings for centuries without treating them as 'different Qur'ans' in the Christian-canon sense.", "Islamic liturgical practice"),
            ],
            "manuscripts": [
                M("Corpus Coranicum — early rasm witnesses", "https://corpuscoranicum.de/en/manuscripts", "Check that early Hijazi leaves track Uthmanic wording"),
            ],
            "sources": [
                S("van Putten 2019 (DOI)", "https://doi.org/10.1017/s0041977x19000338"),
                S("Yaqeen Uthmanic Codex", "https://yaqeeninstitute.org/read/paper/the-uthmanic-codex-understanding-how-the-quran-was-preserved"),
            ],
        },
        "counters": [
            {
                "against": "Christian overread of Qadhi",
                "claim": "Qadhi admitted the Qur'an is not preserved.",
                "reply": "He said the popular dictation-story of ahruf/qira'at has holes. He did not recant wahy or mass oral transmission. Quote him, then quote his clarification.",
                "sources": [S("Wikipedia clarification", "https://en.wikipedia.org/wiki/Yasir_Qadhi")],
            },
            {
                "against": "Muslim 'pronunciation only'",
                "claim": "All differences are just accents.",
                "reply": "Some are; some change number, voice (active/passive), or syntax. Grant the small ones; fight only where meaning moves.",
            },
        ],
        "live": {
            "if_they_say": "Every letter of the Qur'an is identical worldwide.",
            "you_say": "Identical rasm, or identical Hafs print, or all ten qira'at? Pick one thesis before we score the evidence.",
            "dont_overclaim": "Do not turn qira'at into '93,000 different Qur'ans' unless you can explain the counting method.",
        },
        "crux": "Is preservation identity of letters, identity of rasm, or identity of an authorized reading corpus?",
        "debate_use": "Force a one-sentence preservation thesis. Then Sanaa/Uthman/Birmingham become relevant instead of slogan tennis.",
        "counter_to_christian": "NT critical editions also choose among readings; plurality exists on both sides.",
        "counter_to_muslim": "If meanings differ, a strict dictation model must explain why two wordings are both 'the' Qur'an.",
    },
    {
        "id": "uthmanic-rasm",
        "rank": 2,
        "importance": "Top 10",
        "cluster": "Qur'an text",
        "title": "Uthmanic standardization, burning, and a single written archetype",
        "type": "history",
        "popularity": "Very high",
        "why_it_matters": (
            "Christian critiques treat Uthman's project as evidence-destruction. Muslim replies treat it as unification "
            "of an already-known text. van Putten's orthography work is the best non-confessional referee."
        ),
        "christian": {
            "claim": (
                "Uthman commissioned an official text and ordered other materials burned (Bukhari 4987). "
                "That is canon control, not transparent preservation like competing biblical manuscripts."
            ),
            "case": (
                "If rival companion copies existed (Ibn Mas'ud, Ubayy), burning them removes the empirical trail. "
                "A state-standardized scripture cannot later boast that 'no variants ever existed.'"
            ),
            "quotes": [
                Q(
                    "Uthman sent to every Muslim province one copy of what they had copied, and ordered that all the other Qur'anic materials, whether written in fragmentary manuscripts or whole copies, be burnt.",
                    "Sahih al-Bukhari 4987 (standard English reports)",
                    "Book of the Virtues of the Qur'an — compilation report",
                    "https://sunnah.com/bukhari:4987",
                ),
            ],
            "data_points": [
                D("Islamic tradition itself reports regional recitation disputes prompting Uthman's project (Hudhayfa).", "Bukhari compilation narratives"),
                D("Companion-codex reports (Ibn Mas'ud, Ubayy) include sura-order and wording differences.", "Classical tafsir / masahif literature"),
            ],
            "manuscripts": [
                M("Bukhari 4987 text", "https://sunnah.com/bukhari:4987", "Primary narrative of standardization and burning"),
            ],
            "sources": [
                S("Sahih al-Bukhari 4987", "https://sunnah.com/bukhari:4987"),
                S("TGC popularization of the burning argument", "https://www.thegospelcoalition.org/article/muslim-bible-apologetics/"),
            ],
        },
        "muslim": {
            "claim": (
                "Shared spelling quirks across early mushafs show they were copied from one written archetype — "
                "Uthman transmitted, he did not invent a late book."
            ),
            "case": (
                "van Putten examined ni'mat ('grace') spelled with ta' vs ta' marbuta in the same Qur'anic positions "
                "across 14 early manuscripts. The pattern repeats too tightly to be independent oral dictation. "
                "Sadeghi: among early text-types, Uthmanic is the better transcript of a Prophetic prototype."
            ),
            "quotes": [
                Q(
                    "Even the specific rasm with all its orthographic idiosyncrasies points to a single written archetype, which was copied from one mushaf to the other through copying from a written exemplar.",
                    "Marijn van Putten",
                    "BSOAS 82 (2019)",
                    "https://doi.org/10.1017/s0041977x19000338",
                ),
                Q(
                    "The only way that such a consistent reproduction can be explained is by assuming that all the documents that belong to the Uthmanic text type go back to a single written archetype whose spelling was strictly copied from one copy to the next.",
                    "Marijn van Putten",
                    "BSOAS 82 (2019), conclusion",
                    "https://scholarlypublications.universiteitleiden.nl/access/item%3A2911085/view",
                ),
            ],
            "data_points": [
                D("van Putten 2019: 14 early manuscripts; ni'mat spelling locked to verse-position.", "BSOAS 82.2, pp. 233–244", "https://doi.org/10.1017/s0041977x19000338"),
                D("Oral mutawatir + written rasm is the classical dual-lock story; manuscripts now support the written-copying half.", "Yaqeen / van Putten"),
            ],
            "manuscripts": [
                M("Corpus Coranicum early Hijazi set", "https://corpuscoranicum.de/en/manuscripts", "Compare rasm across regional copies"),
            ],
            "sources": [
                S("van Putten DOI", "https://doi.org/10.1017/s0041977x19000338"),
                S("Open PDF (Leiden)", "https://scholarlypublications.universiteitleiden.nl/access/item%3A2911085/view"),
                S("Yaqeen Uthmanic Codex", "https://yaqeeninstitute.org/read/paper/the-uthmanic-codex-understanding-how-the-quran-was-preserved"),
            ],
        },
        "counters": [
            {
                "against": "Christian burning argument",
                "claim": "Burning proves the original was lost.",
                "reply": "Burning explains why we cannot inspect every rival. It does not, by itself, prove invention. Archetype evidence is independent of the hadith's motives.",
            },
            {
                "against": "Muslim 'no variants ever'",
                "claim": "Uthman proves perfect identity from day one.",
                "reply": "The hadith only makes sense if differences already existed. Preservation after canonization ≠ clone-identical first copies.",
            },
        ],
        "live": {
            "if_they_say": "Uthman burned the evidence so the Qur'an is unreliable.",
            "you_say": "Then explain van Putten's locked spelling pattern across surviving early copies. Burning rivals ≠ late fabrication of the rasm we have.",
            "dont_overclaim": "Don't deny companion differences; don't treat burning as a miracle of transparency either.",
        },
        "crux": "Was Uthman transmitting a fixed revelation or selecting among living textual options?",
        "debate_use": "Concede companion differences existed; fight over whether they threaten Prophetic origin.",
        "counter_to_christian": "Christian history also had canon politics and suppression of rival books.",
        "counter_to_muslim": "If alternatives were burned, empirical comparison is partly destroyed by design.",
    },
    {
        "id": "sanaa",
        "rank": 3,
        "importance": "Top 10",
        "cluster": "Qur'an text",
        "title": "Sanaa palimpsest (C-1): non-Uthmanic Qur'an text-type",
        "type": "history",
        "popularity": "Very high in modern debates",
        "why_it_matters": (
            "This is the one manuscript both sides desperately want. Critics: 'see, the Qur'an changed.' "
            "Muslim academics: 'see, companion codices were real and Uthmanic is still closer to the prototype.'"
        ),
        "christian": {
            "claim": (
                "The lower text of Sanaa 1 is a different Qur'anic text-type: word/phrase substitutions, "
                "omissions/additions — so 'one unchanged Qur'an from the first copy' is false."
            ),
            "case": (
                "Sadeghi & Goudarzi: it is the only substantial witness beside the Uthmanic tradition. "
                "Variants resemble reports about Ibn Mas'ud/Ubayy, sometimes more frequent. Upper text is standard — "
                "the lower text was scraped. That is a physical picture of replacement."
            ),
            "quotes": [
                Q(
                    "The lower text of San'a 1 is at present the most important document for the history of the Qur'an. As the only known extant copy from a textual tradition beside the standard Uthmanic one, it has the greatest potential of any known manuscript to shed light on the early history of the scripture.",
                    "Behnam Sadeghi & Mohsen Goudarzi",
                    "Der Islam 87 (2012), p. 1",
                    "https://historyofinformation.com/detail.php?id=180",
                ),
            ],
            "data_points": [
                D("Lower layer: non-Uthmanic rasm type (C-1).", "Sadeghi & Bergmann, Arabica 57 (2010)"),
                D("Reported example: Q 2:87 lower wa-atharihi vs standard wa-qaffayna min ba'dihi type substitutions.", "History of Information summary of Sadeghi"),
                D("Sura order inside extant leaves largely matches, but companion reports include different sura orders.", "Sadeghi 2012"),
            ],
            "manuscripts": [
                M("Islamic Awareness Sanaa dossier (images + literature)", "https://www.islamic-awareness.org/quran/text/mss/soth.html", "Best public packet"),
                M("Wikipedia: Sanaa manuscript", "https://en.wikipedia.org/wiki/Sanaa_manuscript", "Literature map"),
            ],
            "sources": [
                S("Sadeghi & Bergmann 2010 PDF", "https://bible-quran.com/wp-content/uploads/2013/01/Sadeghi-Bergmann-The-Codex-of-a-Companion-of-the-Prophet-and-the-quran-of-the-Prophet.pdf"),
                S("Hilali, The Sanaa Palimpsest (IIS)", "https://www.iis.ac.uk/publications-listing/the-sanaa-palimpsest/"),
            ],
        },
        "muslim": {
            "claim": (
                "C-1 is a companion-codex style secondary tradition. Stemmatics indicate Uthmanic wording is older/"
                "closer to a Prophetic prototype — Sanaa confirms early hearing/writing, not 8th-century invention."
            ),
            "case": (
                "Sadeghi & Bergmann: polarity analysis favors Uthmanic as earlier wording. The palimpsest shows "
                "suras were already formed before Uthman's standardization. Semi-oral first writing explains "
                "companion differences without a 'lost original book replaced centuries later' story."
            ),
            "quotes": [
                Q(
                    "The analysis shows that the suras were formed earlier [than Uthman c. 650]. Furthermore… the inception of at least some Qur'anic textual traditions must have involved semi-oral transmission, most likely via hearers who wrote down a text that was recited by the Prophet.",
                    "Sadeghi & Goudarzi",
                    "Der Islam 87 (2012)",
                    "https://experts.umn.edu/en/publications/san%C4%81-1-and-the-origins-of-the-qur%C4%81n/",
                ),
                Q(
                    "The wording of Uthman's codex is older than that of C-1.",
                    "Sadeghi & Bergmann (paraphrase of polarity-analysis conclusion)",
                    "Arabica 57 (2010)",
                    "https://bible-quran.com/wp-content/uploads/2013/01/Sadeghi-Bergmann-The-Codex-of-a-Companion-of-the-Prophet-and-the-quran-of-the-Prophet.pdf",
                ),
            ],
            "data_points": [
                D("Upper text ≈ standard Uthmanic Qur'an.", "Palimpsest description"),
                D("Sadeghi: Uthmanic sits in the majority between C-1 and Ibn Mas'ud reports — either more faithful copy of a prototype or a hybrid of companion readings.", "Arabica 2010 stemma discussion"),
            ],
            "manuscripts": [
                M("DAM 01-27.1 / Codex Sanaa 1", "https://en.wikipedia.org/wiki/Sanaa_manuscript", "Lower text = C-1"),
            ],
            "sources": [
                S("Sadeghi & Bergmann 2010", "https://bible-quran.com/wp-content/uploads/2013/01/Sadeghi-Bergmann-The-Codex-of-a-Companion-of-the-Prophet-and-the-quran-of-the-Prophet.pdf"),
            ],
        },
        "counters": [
            {
                "against": "Christian 'rewritten Qur'an'",
                "claim": "Sanaa proves the Qur'an was fabricated later.",
                "reply": "A 7th-century non-Uthmanic type is the opposite of a late invention from nothing. It is early multiplicity.",
            },
            {
                "against": "Muslim 'ignore Sanaa'",
                "claim": "It's just a student notebook / scribal junk.",
                "reply": "Hilali's teaching-copy hypothesis exists — argue it. Don't pretend the lower text isn't Qur'anic material. Sadeghi treats it as a real text-type.",
            },
        ],
        "live": {
            "if_they_say": "Sanaa proves the Qur'an was rewritten.",
            "you_say": "It proves a second early text-type existed. Sadeghi still argues Uthmanic is closer to the prototype. That's not 'lost book in the Abbasid period.'",
            "dont_overclaim": "Don't say Sanaa matches today's mushaf word-for-word. Don't say it is a different religion's scripture.",
        },
        "crux": "Does C-1 refute Prophetic origin, or only refute a folk model of clone-identical first copies?",
        "debate_use": "Memorize both uses of Sanaa. Ask if the opponent has read Sadeghi or only clips.",
        "counter_to_christian": "One divergent palimpsest is not thousands of Qur'ans.",
        "counter_to_muslim": "If companion codices differed in wording, verbatim-identity slogans fail.",
    },
    {
        "id": "birmingham",
        "rank": 4,
        "importance": "Top 10",
        "cluster": "Qur'an text",
        "title": "Birmingham folios and radiocarbon dating",
        "type": "history + method",
        "popularity": "High",
        "why_it_matters": "Best Muslim visual for 'close to Muhammad.' Best Christian caution: parchment ≠ ink, range ≠ point date.",
        "christian": {
            "claim": (
                "C-14 dates the animal's death (parchment), not the writing event. Paleography may sit later. "
                "Media 'oldest Qur'an / unchanged' overclaim is not the academic result."
            ),
            "case": (
                "Oxford dated Mingana 1572a parchment 568–645 CE at 95.4%. That range starts before the traditional "
                "first revelation and ends around Uthman. Gabriel Reynolds and others: combine C-14 with paleography; "
                "do not treat the lower bound as 'Muhammad's scribe.'"
            ),
            "quotes": [
                Q(
                    "Radiocarbon dating of the Birmingham Qur'an folios… between AD 568 and 645 with 95.4% accuracy.",
                    "University of Birmingham",
                    "2015 announcement",
                    "https://www.birmingham.ac.uk/news-archive/2015/birmingham-quran-manuscript-dated-among-the-oldest-in-the-world",
                ),
            ],
            "data_points": [
                D("C-14 dates parchment collagen, not carbon in ink.", "Standard radiocarbon method note"),
                D("Folios are a few leaves, not a complete mushaf.", "Mingana 1572a description"),
                D("Text type is early Uthmanic, not Sanaa C-1.", "Academic consensus on Birmingham leaves"),
            ],
            "manuscripts": [
                M("Birmingham University announcement + images", "https://www.birmingham.ac.uk/news-archive/2015/birmingham-quran-manuscript-dated-among-the-oldest-in-the-world", "Official plate"),
                M("VMR Mingana 1572a", "http://vmr.bham.ac.uk/Collections/Mingana/Islamic_Arabic_1572a/table/", "Manuscript viewer"),
            ],
            "sources": [
                S("Birmingham news", "https://www.birmingham.ac.uk/news-archive/2015/birmingham-quran-manuscript-dated-among-the-oldest-in-the-world"),
                S("Islamic Awareness C-14 dossier", "https://www.islamic-awareness.org/quran/text/mss/radio"),
            ],
        },
        "muslim": {
            "claim": (
                "Even with method caveats, a 7th-century Hijazi Qur'an this close to Muhammad's lifetime is "
                "extraordinary proximity compared with many biblical autograph gaps."
            ),
            "case": (
                "David Thomas (Birmingham): the portions are very close to the form read today. Multiple early "
                "Hijazi manuscripts (not only Birmingham) now cluster in the first Islamic century."
            ),
            "quotes": [
                Q(
                    "These portions must have been in a form that is very close to the form of the Qur'an read today, supporting the view that the text has undergone little or no alteration and that it can be dated to a point very close to the time it was [revealed].",
                    "Prof. David Thomas (as quoted in Birmingham announcement)",
                    "University of Birmingham, 2015",
                    "https://www.birmingham.ac.uk/news-archive/2015/birmingham-quran-manuscript-dated-among-the-oldest-in-the-world",
                ),
            ],
            "data_points": [
                D("Mingana 1572a belongs with BnF Arabe 328c (same codex).", "Islamic Awareness / Fedeli"),
                D("Other C-14'd Hijazi fragments also land in 7th c. ranges.", "Islamic Awareness radio page"),
            ],
            "manuscripts": [
                M("Birmingham folio 1 recto (Wikimedia)", "https://commons.wikimedia.org/wiki/File:Birmingham_Quran_manuscript_folio_1_recto.jpg", "Public plate"),
            ],
            "sources": [
                S("Islamic Awareness radiocarbon", "https://www.islamic-awareness.org/quran/text/mss/radio"),
            ],
        },
        "counters": [
            {
                "against": "Muslim knock-out C-14",
                "claim": "Science proved the Qur'an is unchanged.",
                "reply": "Science dated skin. The text is early and Uthmanic-type — that is strong. It is not a lab certificate of letter-identity or divine origin.",
            },
        ],
        "live": {
            "if_they_say": "Birmingham manuscript proves the Qur'an is unchanged.",
            "you_say": "It dates parchment to a range, covers a few leaves, and the text is early Uthmanic-type. Impressive proximity — not a total proof.",
            "dont_overclaim": "Don't call the lower bound 'before Islam so the Qur'an predates Muhammad' without paleography. Don't dismiss it as 'just a fake date.'",
        },
        "crux": "What does C-14 actually date — and what claim is being smuggled from that date?",
        "debate_use": "Never let a C-14 slide stand without: parchment or ink? range or point estimate? complete book or leaves?",
        "counter_to_christian": "Early dates are still impressive versus many biblical autograph gaps.",
        "counter_to_muslim": "Parchment reuse / animal age means C-14 is a soft terminus.",
    },
    {
        "id": "brubaker",
        "rank": 5,
        "importance": "Top 10",
        "cluster": "Qur'an text",
        "title": "Scribal corrections in early Qur'an manuscripts (Brubaker)",
        "type": "history + method",
        "popularity": "High in YouTube apologetics; contested in journals",
        "why_it_matters": "Photos of erasures look like 'gotcha corruption.' Academic reviews say the inference to late doctrinal editing is not shown.",
        "christian": {
            "claim": "Physical insertions and erasures show the text was altered toward a later standard — evidence of fluidity.",
            "case": (
                "Daniel Brubaker, Corrections in Early Qur'an Manuscripts (2019), popularized 20 examples. "
                "Apologetics infers the Hafs 1924 print is an endpoint of editorial drift, not a frozen 7th-century recitation."
            ),
            "quotes": [
                Q(
                    "We are told that a survey of these manuscripts… will 'challenge the traditional assertions about the transmission of the Quran'… Unfortunately, the bold claims are left unsubstantiated.",
                    "Hythem Sidky (review)",
                    "Al-'Usur al-Wusta / MEM review of Brubaker",
                    "https://www.middleeastmedievalists.com/wp-content/uploads/2019/11/UW-27-Sidky.pdf",
                ),
            ],
            "data_points": [
                D("Early Qur'an manuscripts do contain visible corrections — that fact is not in dispute.", "Brubaker plates; Sidky agrees the photos are useful"),
                D("The disputed move is: correction = theological rewriting toward Cairo 1924.", "Sidky / Altikulac"),
            ],
            "manuscripts": [
                M("Brubaker project / Variant Qur'an", "https://www.danielbrubaker.com/quran-and-islam/variant-quran-marks-1st-anniversary/", "Apologetic presentation of corrections"),
            ],
            "sources": [
                S("Sidky review PDF", "https://www.middleeastmedievalists.com/wp-content/uploads/2019/11/UW-27-Sidky.pdf"),
            ],
        },
        "muslim": {
            "claim": (
                "Corrections are ordinary scribal error-fixes aligning copies to a known text. Brubaker overinterprets. "
                "Uncorrected early witnesses already match the rasm."
            ),
            "case": (
                "Sidky: give scribal error first consideration; most examples are best explained that way. "
                "Tayyar Altikulac (IRCICA) published a refutation. NT manuscripts are full of the same phenomena."
            ),
            "quotes": [
                Q(
                    "If the objective of Brubaker's book is to demonstrate the humanity of the scribes involved in transmitting the Quranic text, it certainly succeeds… Where it falls short… [is] the vast majority of [examples] are best explained [as scribal error].",
                    "Hythem Sidky",
                    "Review of Brubaker (paraphrase of the review's verdict)",
                    "https://www.middleeastmedievalists.com/wp-content/uploads/2019/11/UW-27-Sidky.pdf",
                ),
            ],
            "data_points": [
                D("IRCICA: Altikulac, Refutation of Daniel Alan Brubaker (2020).", "Ankara University faculty review", "https://dergipark.org.tr/en/pub/auifd/article/1070291"),
            ],
            "manuscripts": [
                M("Any early Hijazi leaf with a visible overstrike", "https://corpuscoranicum.de/en/manuscripts", "Compare with uncorrected parallels of the same verse"),
            ],
            "sources": [
                S("Sidky review", "https://www.middleeastmedievalists.com/wp-content/uploads/2019/11/UW-27-Sidky.pdf"),
                S("Altikulac refutation notice", "https://dergipark.org.tr/en/pub/auifd/article/1070291"),
            ],
        },
        "counters": [
            {
                "against": "Photo-of-erasure gotcha",
                "claim": "This photo proves tahrif.",
                "reply": "Ask for the control: an early uncorrected parallel of the same verse. Hand-copied Bibles look the same under a lens.",
            },
        ],
        "live": {
            "if_they_say": "Brubaker's photos show corruption.",
            "you_say": "Photos show corrections. Sidky: usually scribal fixes; the bold late-creation thesis is not demonstrated.",
            "dont_overclaim": "Don't pretend manuscripts were never touched. Don't treat every overstrike as a council rewriting doctrine.",
        },
        "crux": "Do corrections converge on an early archetype or manufacture a later one?",
        "debate_use": "If they show an erasure, demand a stemma, not a vibe.",
        "counter_to_christian": "NT manuscripts are full of corrections too.",
        "counter_to_muslim": "Patterns of correction still deserve study; dismissiveness is not a method.",
    },
    {
        "id": "nt-variants",
        "rank": 6,
        "importance": "Top 10",
        "cluster": "Bible text",
        "title": "New Testament variants and reconstructability",
        "type": "history + method",
        "popularity": "Very high",
        "why_it_matters": "Muslim opening move is almost always '400,000 variants.' If you cannot explain counting, you lose the room.",
        "christian": {
            "claim": (
                "Despite a huge variant count, the NT is reconstructable with high confidence for nearly all passages; "
                "meaningful-and-viable cases are known, published, and few."
            ),
            "case": (
                "Wallace: a variant is a place of difference, not 'times manuscripts.' Most are spelling/nonsense. "
                "Meaningful and viable: generously ~<0.1%. Showcase: longer ending of Mark; Pericope Adulterae; "
                "Comma Johanneum (not original). Critical editions flag them — that is honesty, not collapse."
            ),
            "quotes": [
                Q(
                    "The vast majority of NT variants are minor… Among 400,000 textual variants of the NT, over 99% make no difference to the meaning, and less than 1% are both meaningful and viable.",
                    "Daniel B. Wallace (course summary of his standard taxonomy)",
                    "BiblicalTraining NT605 / CSNTM-adjacent teaching",
                    "https://www.biblicaltraining.org/learn/institute/nt605-textual-criticism",
                ),
                Q(
                    "By Dan's generous estimate, [meaningful and viable variants are] less than one-tenth of 1 percent of all variants, around 1,500 in total.",
                    "Wallace interviewed on Logos 'What in the Word?'",
                    "Is the New Testament Text Reliable?",
                    "https://www.logos.com/grow/witw-new-testament-reliability/",
                ),
            ],
            "data_points": [
                D("Greek NT ~138,000 words; variant estimates often ~400,000 (counting method matters).", "Wallace / Ehrman debates"),
                D("P52 (John 18), P66 (John), P46 (Paul) are 2nd/3rd-c. papyri — not 4th-c. invention.", "CSNTM"),
                D("Codex Sinaiticus & Vaticanus: mid-4th c. nearly complete Greek Bibles.", "codexsinaiticus.org; DigiVatLib"),
            ],
            "manuscripts": [
                M("P52 Rylands (CSNTM)", "https://manuscripts.csntm.org/Manuscript/View/GA_P52", "Earliest often-cited John fragment"),
                M("Codex Sinaiticus", "https://codexsinaiticus.org/en/manuscript.aspx", "Includes famous Mark ending issues"),
                M("INTF / NT.VMR", "https://ntvmr.uni-muenster.de/", "Where variants are catalogued, not hidden"),
            ],
            "sources": [
                S("Wallace vs Ehrman 2011", "https://www.youtube.com/watch?v=WRHjZCKRIu4"),
                S("Wallace on counting variants", "https://danielbwallace.com/2013/09/09/the-number-of-textual-variants-an-evangelical-miscalculation/"),
                S("INTF", "https://www.uni-muenster.de/INTF/"),
            ],
        },
        "muslim": {
            "claim": (
                "The early manuscript gap plus theologically loaded variants undercut claims of a stable inspired text "
                "comparable to the Qur'an's early rasm lock."
            ),
            "case": (
                "Ehrman popularizes: more differences than words; first-century silence; scribes changed texts for "
                "theological reasons (e.g. anti-adoptionist). Mark 16 and John 8 were read as Scripture for centuries "
                "then demoted. That is not 'we always knew the original.'"
            ),
            "quotes": [
                Q(
                    "There are more differences among our manuscripts than there are words in the New Testament.",
                    "Bart D. Ehrman (standard debate formulation)",
                    "Greer-Heard / popular lectures; cf. Misquoting Jesus",
                    "https://www.baptistpress.com/resource-library/news/wallace-ehrman-debate-n-t-reliability/",
                ),
            ],
            "data_points": [
                D("Mark 16:9–20 absent from Sinaiticus & Vaticanus.", "NA28 apparatus"),
                D("John 7:53–8:11 missing from earliest witnesses.", "NA28"),
                D("1 John 5:7 Comma Johanneum is a late Latin interpolation.", "Standard TC"),
            ],
            "manuscripts": [
                M("Sinaiticus Mark ending", "https://codexsinaiticus.org/en/manuscript.aspx", "Show the page live if possible"),
            ],
            "sources": [
                S("Ehrman, Misquoting Jesus", "https://www.harpercollins.com/products/misquoting-jesus-bart-d-ehrman"),
            ],
        },
        "counters": [
            {
                "against": "400k scare",
                "claim": "There are 400,000 different Bibles.",
                "reply": "Variants are counted per difference-location, then multiplied in bad methods. Ask which variant changes a doctrine and whether NA28 already footnotes it.",
            },
            {
                "against": "Muslim Ehrman cherry-pick",
                "claim": "Ehrman destroyed the Bible so Islam wins.",
                "reply": "Ehrman still reconstructs a text and calls crucifixion rock-bottom certain. If you use him against inspiration, you inherit him against Q 4:157.",
            },
        ],
        "live": {
            "if_they_say": "There are 400,000 New Testament variants.",
            "you_say": "Most are spelling. Name one that is both meaningful and viable — then look it up in a critical edition.",
            "dont_overclaim": "Don't claim we have the autographs. Don't claim zero theologically interesting variants.",
        },
        "crux": "Are we measuring 'number of differences' or 'ability to recover an early text'?",
        "debate_use": "Have Mark 16, John 8, 1 John 5:7 ready — and what the critical text does with each.",
        "counter_to_christian": "Early gap still matters; some variants are theologically loaded.",
        "counter_to_muslim": "Citing Ehrman against the Bible while rejecting his Jesus history is cherry-picking.",
    },
    {
        "id": "ot-dss",
        "rank": 7,
        "importance": "Top 10",
        "cluster": "Bible text",
        "title": "Old Testament: Masoretic Text, Septuagint, Dead Sea Scrolls",
        "type": "history",
        "popularity": "High (often neglected vs NT)",
        "why_it_matters": "Muslims attack 'medieval Leningrad Codex.' Christians overclaim 'DSS prove zero change.' Both need Tov.",
        "christian": {
            "claim": (
                "Dead Sea Scrolls push Hebrew Bible traditions back centuries before Islam. Continuity with later MT "
                "is substantial; plurality is real but bounded."
            ),
            "case": (
                "Great Isaiah Scroll (~2nd c. BCE) is recognizably Isaiah. Some DSS confirm MT; some support LXX-like "
                "editions (esp. Jeremiah/Samuel). This is ancient textual culture, not 'rabbis invented the OT after Muhammad.'"
            ),
            "quotes": [
                Q(
                    "The traditional witnesses… Masoretic Text and the Septuagint… The Dead Sea Scrolls… remain the most significant source of information for the study of ancient Scripture.",
                    "Emanuel Tov (handbook framing)",
                    "The Text-Critical Use of the Septuagint / TCHB tradition",
                    "https://www.eisenbrauns.org/books/titles/978-1-57506-328-7.html",
                ),
            ],
            "data_points": [
                D("Leningrad Codex 1008/09 CE is the oldest complete MT — late as a complete book, not as a tradition.", "Codex dating"),
                D("DSS: 3rd c. BCE – 1st c. CE.", "Leon Levy DSS library"),
                D("Jeremiah LXX is substantially shorter — a real literary edition, not a typo.", "Tov, literary criticism of Jeremiah"),
            ],
            "manuscripts": [
                M("Leon Levy DSS Digital Library", "https://www.deadseascrolls.org.il/", "Primary image corpus"),
                M("Great Isaiah Scroll (IMJ)", "https://dss.collections.imj.org.il/", "Continuous Isaiah"),
            ],
            "sources": [
                S("Tov, Textual Criticism of the Hebrew Bible", "https://www.fortresspress.com/store/product/9780800696641/Textual-Criticism-of-the-Hebrew-Bible"),
            ],
        },
        "muslim": {
            "claim": (
                "OT textual plurality (MT/LXX/SP/DSS) and late complete MT exemplars show the Hebrew Bible was not "
                "preserved as a single fixed text like the Uthmanic rasm."
            ),
            "case": (
                "Samaritan Pentateuch diverges; Jeremiah has two editions; Christians argue internally which is "
                "'original.' Compared with Uthmanic unity, the OT looks fluid."
            ),
            "quotes": [],
            "data_points": [
                D("Samaritan Pentateuch: thousands of differences from MT, subset aligning with LXX.", "Standard intro figures"),
            ],
            "manuscripts": [
                M("Leningrad Codex (complete MT)", "https://archive.org/details/Leningrad_Codex", "Show the date honestly"),
            ],
            "sources": [
                S("Tov on LXX", "https://www.eisenbrauns.org/books/titles/978-1-57506-328-7.html"),
            ],
        },
        "counters": [
            {
                "against": "Muslim 'medieval invention'",
                "claim": "The OT appears in 1008 so it is late.",
                "reply": "DSS smash that. Date of oldest complete copy ≠ date of composition or of the tradition.",
            },
        ],
        "live": {
            "if_they_say": "Dead Sea Scrolls prove the OT is unchanged.",
            "you_say": "They prove early Hebrew traditions and much continuity — and real plurality. Good against medieval-invention slogans; not proof of zero variation.",
            "dont_overclaim": "Keep OT and NT unbundled. Don't hide Jeremiah's two editions.",
        },
        "crux": "Is textual plurality evidence of corruption or of a normal ancient textual culture?",
        "debate_use": "One DSS example that confirms MT + one that supports LXX.",
        "counter_to_christian": "Don't pretend one OT text-type always wins.",
        "counter_to_muslim": "Literary editions ≠ 'Bible invented in the Middle Ages.'",
    },
    {
        "id": "islamic-dilemma",
        "rank": 8,
        "importance": "Top 10",
        "cluster": "Cross-scripture",
        "title": "Islamic dilemma: Qur'an affirms prior scripture",
        "type": "theology + history",
        "popularity": "Very high",
        "why_it_matters": "Best Christian offensive tool on this topic. If Injil = the four Gospels' doctrine, Islam collides with its own book.",
        "christian": {
            "claim": (
                "The Qur'an tells People of the Gospel to judge by what they have; 7th-c. Bible ≈ today's in core; "
                "therefore Islam affirms a Bible that contradicts Islam."
            ),
            "case": (
                "Q 5:47; 5:68; 10:94; 3:3–4. Manuscripts of NT/OT already exist in the 7th century (Sinaiticus etc. "
                "are 4th c.). Post-Muhammad corruption cannot rescue the dilemma."
            ),
            "quotes": [
                Q(
                    "Let the People of the Gospel judge by what Allah has revealed therein.",
                    "Qur'an 5:47",
                    "Primary text",
                    "https://quran.com/5/47",
                ),
            ],
            "data_points": [
                D("4th-c. complete-ish Greek Bibles predate Islam by ~300 years.", "Sinaiticus / Vaticanus"),
                D("Peshitta and other versions were already in use in the late antique Near East.", "Syriac biblical versions"),
            ],
            "manuscripts": [
                M("Codex Sinaiticus (pre-Islamic Greek Bible)", "https://codexsinaiticus.org/en/", "What 'the Book' could mean physically"),
            ],
            "sources": [
                S("Q 5:47", "https://quran.com/5/47"),
                S("Q 10:94", "https://quran.com/10/94"),
                S("Reynolds on tahrif", "https://almuslih.org/wp-content/uploads/Library/Reynolds,%20G%20-%20The%20Quranic%20accusation.pdf"),
            ],
        },
        "muslim": {
            "claim": (
                "Affirmation is of revelation/guidance within prior books, not of every later Christian doctrine. "
                "Injil ≠ four-Gospel Nicene packet. Qur'an is muhaymin (5:48)."
            ),
            "case": (
                "Abdullah Saeed: Qur'an reveres Tawrat/Injil while criticizing people who distort words from their places. "
                "Ally: 'contains guidance and light' ≠ 'is entirely guidance and light.' Tahrif often = meaning, not always total rewrite."
            ),
            "quotes": [
                Q(
                    "Since the 'authorized' scriptures of Jews and Christians remain very much today as they existed at the time of the Prophet, it is difficult to argue that the Qur'anic references to Tawrat and Injil were only to the 'pure' Tawrat and Injil as existed at the time of Moses and Jesus.",
                    "Abdullah Saeed",
                    "The Charge of Distortion of Jewish and Christian Scriptures",
                    "https://bible-quran-video.s3.amazonaws.com/Documents/The-Charge-of-Distortion-of-Jewish-and-Christian-Scriptures_Abdullah+Saeed.pdf",
                ),
            ],
            "data_points": [
                D("Q 5:48: Qur'an as muhaymin over previous scripture.", "https://quran.com/5/48"),
                D("Q 4:46; 5:13: yuharrifuna — distort words from their places.", "Tahrif verses"),
            ],
            "manuscripts": [],
            "sources": [
                S("Saeed PDF", "https://bible-quran-video.s3.amazonaws.com/Documents/The-Charge-of-Distortion-of-Jewish-and-Christian-Scriptures_Abdullah+Saeed.pdf"),
                S("Ally reply to White on 5:47", "https://shabirally.wordpress.com/2012/05/21/a-response-to-james-whites-some-brief-thoughts-regarding-liberal-scholarship-redaction-criticism-and-islam-part-1/"),
            ],
        },
        "counters": [
            {
                "against": "Christian blank-check affirmation",
                "claim": "5:47 means every Gospel sentence is God's word.",
                "reply": "Ally's ingredient argument: a pot containing salt is not only salt. Then fight crucifixion as a separate historical question.",
            },
        ],
        "live": {
            "if_they_say": "The Qur'an confirms the Bible, so Muslims must accept the Gospels.",
            "you_say": "Define Injil. Affirmation of guidance therein is not a blank check for Nicene doctrine. Then argue the historical content (cross) separately.",
            "dont_overclaim": "Don't pretend the 7th-c. Injil was a lost single book nobody can describe. Don't pretend 5:47 doesn't exist.",
        },
        "crux": "What object does 'Injil' refer to in Q 5 — and what propositional content is affirmed?",
        "debate_use": "Prepare Ally/Saeed as the precise Muslim reply; then don't hide 4:157.",
        "counter_to_christian": "If Gospel means a book given to Jesus, four Gospels are already a category mismatch.",
        "counter_to_muslim": "If the available Injil in the 7th c. taught crucifixion/deity, partial-affirmation still collides.",
    },
    {
        "id": "method-symmetry",
        "rank": 9,
        "importance": "Top 10",
        "cluster": "Method",
        "title": "Method symmetry: critical tools both ways",
        "type": "method",
        "popularity": "Very high among trained debaters",
        "why_it_matters": "James White's judo: you cannot use Dunn/Ehrman as a sword on the Gospels and a shield for the Qur'an.",
        "christian": {
            "claim": (
                "If form/redaction criticism can dissolve Gospel historicity, the same toolkit dissolves sira/hadith "
                "and treats Qur'anic Jesus material as late and non-historical."
            ),
            "case": (
                "Scholars Ally cites would not validate Jesus speaking from the cradle as history. Infancy Gospel "
                "parallels (clay birds) would be called 'apocryphal dependence' if found in the NT."
            ),
            "quotes": [
                Q(
                    "I do not think that the Qur'an has any particular insights about the historical Jesus that are to be taken as independent reports by historical scholars. Neither does any other historical scholar that I know.",
                    "Bart D. Ehrman",
                    "Does My Work on the Historical Jesus Confirm the Quran?",
                    "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/",
                ),
            ],
            "data_points": [
                D("Clay birds: Infancy Gospel of Thomas ↔ Q 3:49 / 5:110.", "Reynolds / standard parallel lists"),
                D("Cradle speech: late antique Christian lore ↔ Q 19:29–33.", "Arabic Infancy Gospel discussions"),
            ],
            "manuscripts": [],
            "sources": [
                S("Ehrman blog", "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/"),
                S("White on Ally / liberal scholarship", "https://www.aomin.org/aoblog/uncategorized/a-response-to-dr-shabir-ally-part-1/"),
            ],
        },
        "muslim": {
            "claim": (
                "The Qur'an's claim-structure differs: one revelatory book in one language vs a multi-author library. "
                "Even critical scholars often affirm early Qur'anic rasm fixation."
            ),
            "case": (
                "Genre difference is real. Islamic sciences have isnad criticism. van Putten/Sadeghi are not 'liberal "
                "Muslim Ehrmans' in the sense of dissolving the 7th-century text; they often lock it earlier."
            ),
            "quotes": [
                Q(
                    "A definitive answer to this question cannot be found by examining the Muslim tradition, but should rather be based on a study of the text of the early Quranic manuscripts.",
                    "Marijn van Putten",
                    "BSOAS 2019 — method statement",
                    "https://doi.org/10.1017/s0041977x19000338",
                ),
            ],
            "data_points": [
                D("Critical Qur'anic studies often date a written Uthmanic archetype to the 7th century, not the 9th.", "van Putten / Sinai / Déroche stream"),
            ],
            "manuscripts": [],
            "sources": [
                S("van Putten 2019", "https://doi.org/10.1017/s0041977x19000338"),
            ],
        },
        "counters": [
            {
                "against": "Special pleading",
                "claim": "My book is revelation so your tools don't apply.",
                "reply": "Then say so and leave the 'historicity' motion. If the motion is public history, tools apply both ways.",
            },
        ],
        "live": {
            "if_they_say": "Liberal scholars proved the Gospels are late legends.",
            "you_say": "Name the scholars. Would they treat Qur'anic Jesus sayings as 30s-CE history? If not, you borrowed a sword that cuts your own book.",
            "dont_overclaim": "Don't pretend genre differences are zero. Don't pretend they are infinite either.",
        },
        "crux": "What is the shared historical method both sides accept before theology?",
        "debate_use": "45-second symmetry speech. Reuse every round.",
        "counter_to_christian": "Difference of genre is real; not every biblical tool maps 1:1.",
        "counter_to_muslim": "If you use Metzger against Mark, you need a reason not to use Déroche/van Putten critically.",
    },
    {
        "id": "event-vs-book",
        "rank": 10,
        "importance": "Top 10",
        "cluster": "Origins",
        "title": "Book reliability vs event reliability (Jesus' crucifixion as the test)",
        "type": "history + theology",
        "popularity": "Very high",
        "why_it_matters": (
            "You can win 'whose book was copied earlier' and still lose 'whose book matches the best-attested event "
            "about Jesus.' Don't let the motion smear these together."
        ),
        "christian": {
            "claim": (
                "On the historical Jesus, mainstream scholarship aligns with crucifixion; Qur'an 4:157 is the collision. "
                "That is an event-historicity failure even if Qur'anic rasm is early."
            ),
            "case": (
                "Josephus, Tacitus, all four Gospels, Paul (1 Cor 15; Phil 2). Ehrman (non-Christian): rock-bottom certain. "
                "A perfectly preserved sentence can still be historically false."
            ),
            "quotes": [
                Q(
                    "I am convinced beyond a shadow of a doubt that Jesus was physically crucified and died on the cross. That is rock-bottom certain in my books. And it stands completely [at] odds with standard Islamic beliefs.",
                    "Bart D. Ehrman",
                    "Does My Work on the Historical Jesus Confirm the Quran?",
                    "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/",
                ),
                Q(
                    "Christus, from whom the name had its origin, suffered the extreme penalty during the reign of Tiberius at the hands of one of our procurators, Pontius Pilatus.",
                    "Tacitus",
                    "Annals 15.44",
                    "https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44",
                ),
            ],
            "data_points": [
                D("Q 4:157 is the sole Qur'anic locus usually read as denying crucifixion.", "https://quran.com/4/157"),
                D("1 Cor 15:3–8 is commonly dated within a few years of the crucifixion as received tradition.", "Standard Pauline chronology"),
            ],
            "manuscripts": [
                M("P46 (Pauline papyri incl. crucifixion kerygma)", "https://en.wikipedia.org/wiki/Papyrus_46", "Early copy of early content"),
            ],
            "sources": [
                S("Ehrman blog", "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/"),
                S("Craig on Qur'an & crucifixion", "https://www.reasonablefaith.org/writings/question-answer/the-quran-and-the-crucifixion-of-jesus"),
                S("Q 4:157", "https://quran.com/4/157-158"),
            ],
        },
        "muslim": {
            "claim": (
                "4:157 can be read as denying Jewish triumph/agency, not the public event; tafsir substitution is not "
                "identical to the verse. Revelation can correct historians."
            ),
            "case": (
                "Lawson: tafsir, not the bare wording, hardens into categorical denial. Some Isma'ili and modern academic "
                "readings keep historicity of a crucifixion-looking event. Also: Q 3:55 / 19:33 are used internally."
            ),
            "quotes": [
                Q(
                    "The point is that tafsir, not the Qur'an, denies the Crucifixion.",
                    "Todd Lawson (as commonly cited in this debate)",
                    "The Crucifixion and the Qur'an",
                    "https://almuslih.org/wp-content/uploads/2024/12/Lawson-T-%E2%80%93-The-Crucifixion-and-the-Quran.pdf",
                ),
            ],
            "data_points": [
                D("Majority Sunni tafsir: substitution / non-death on the cross.", "Tabari, etc."),
                D("Minority: some Isma'ili and modern academic readings of 4:157 as denying the boast.", "AJIS survey"),
            ],
            "manuscripts": [],
            "sources": [
                S("Lawson PDF", "https://almuslih.org/wp-content/uploads/2024/12/Lawson-T-%E2%80%93-The-Crucifixion-and-the-Quran.pdf"),
                S("AJIS — non-monolithic crucifixion views", "https://ajis.com.au/index.php/ajis/article/view/585"),
            ],
        },
        "counters": [
            {
                "against": "Muslim 'appearance' escape",
                "claim": "Historians only have appearances, which the Qur'an already grants.",
                "reply": "Craig: that concedes the historical evidence. Then you need a miracle-of-illusion against all sources. Say that openly.",
            },
        ],
        "live": {
            "if_they_say": "The Qur'an is better preserved so it is more historical.",
            "you_say": "Preservation of wording ≠ accuracy about 30 CE events. Split the motion: book-as-artifact vs crucifixion-as-event.",
            "dont_overclaim": "Don't pretend 4:157 is unambiguous. Don't pretend historians treat the Qur'an as a Jesus source.",
        },
        "crux": "Is tonight's standard public historical method, or revelatory authority?",
        "debate_use": "If the motion says historicity, pin the standard to public history in the first minute.",
        "counter_to_christian": "Historical consensus is not infallible.",
        "counter_to_muslim": "If you enter a historicity debate, positivist method is the agreed arena.",
    },
]
