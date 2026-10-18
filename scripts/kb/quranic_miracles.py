# -*- coding: utf-8 -*-
"""Qur'anic miracles (i'jaz): literary first, then linguistic, historical, scientific.

Not an apologetic pamphlet. Each card steelmans the miracle claim, then the
skeptical / academic / classical-literal reading that apologetics often drops.
No declared winner.
"""
from __future__ import annotations

from .deepen_lib import D, Q, S, apply_overlays

QUR = "https://quran.com/{}"


def qv(path: str, note: str | None = None, label: str | None = None) -> dict:
    lab = label or ("Q " + path.replace("/", ":"))
    return S(lab, QUR.format(path), note)


def side(claim: str, case: str = "", *, quotes=None, data_points=None, sources=None) -> dict:
    d: dict = {"claim": claim, "case": case}
    if quotes:
        d["quotes"] = quotes
    if data_points:
        d["data_points"] = data_points
    if sources:
        d["sources"] = sources
    return d


def card(
    id: str,
    rank: int,
    cluster: str,
    title: str,
    *,
    typ: str,
    popularity: str,
    why: str,
    claimant: dict,
    critic: dict,
    live: dict,
    crux: str,
    debate_use: str,
    counters=None,
) -> dict:
    d = {
        "id": id,
        "rank": rank,
        "cluster": cluster,
        "title": title,
        "type": typ,
        "popularity": popularity,
        "why_it_matters": why,
        "claimant": claimant,
        "critic": critic,
        "live": live,
        "crux": crux,
        "debate_use": debate_use,
    }
    if counters:
        d["counters"] = counters
    return d


def V(path: str, hook: str, ref: str | None = None) -> dict:
    return {
        "ref": ref or ("Q " + path.replace("/", ":")),
        "hook": hook,
        "url": QUR.format(path),
    }


def G(id: str, title: str, miracle: str, critic: str, verses: list[dict]) -> dict:
    return {
        "id": id,
        "title": title,
        "move": miracle,
        "christian": critic,
        "verses": verses,
        "count": len(verses),
    }


ARGUMENTS = [
    card(
        "tahaddi",
        1,
        "Literary",
        "The challenge (taḥaddī): produce a sūrah like it",
        typ="method + literature",
        popularity="Very high",
        why=(
            "This is the Qur'an's own miracle claim. If 'like it' has no public test, "
            "every later i'jaz argument is unfalsifiable branding."
        ),
        claimant=side(
            "Q 2:23, 10:38, 11:13, 17:88 dare humans and jinn to produce the like of the Qur'an. Fourteen centuries of Arabic have not met it; that unmet challenge is the miracle.",
            "Classical ʿulamāʾ (al-Khaṭṭābī, al-Rummānī, al-Jurjānī) treat inimitability as the public sign of prophecy: unique naẓm (arrangement of words and meanings), not circus physics. "
            "The shortest unit challenged is a sūrah. Failure of Musaylima, of modern pastiches, and of the entire poetic canon is taken as the result. "
            "Nouman Ali Khan's English teaching restates this: the miracle is the speech itself, which an unlettered messenger could not have authored.",
            quotes=[
                Q(
                    "Say, if mankind and jinn gathered to produce the like of this Qur'an, they could not produce the like of it, even if they were to each other assistants.",
                    "Qur'an 17:88",
                    "Challenge verse",
                    "https://quran.com/17/88",
                ),
            ],
            data_points=[
                D("Challenge verses: 2:23–24; 10:38; 11:13; 17:88; 52:34.", "Quran.com"),
                D("Classical theory of i'jaz is literary (naẓm, balāgha), not embryology or Big Bang.", "al-Jurjānī, Dalāʾil al-iʿjāz"),
            ],
            sources=[
                qv("17/88", "Mankind and jinn cannot produce the like."),
                qv("2/23", "Produce a sūrah like it."),
                S("al-Jurjānī — Dalāʾil al-iʿjāz (overview)", "https://plato.stanford.edu/entries/arabic-islamic-language/"),
            ],
        ),
        critic=side(
            "The challenge does not specify a scoring rubric. 'Not like it' is then used to disqualify every attempt, which makes the claim unfalsifiable. Literary greatness is real; divinity does not follow.",
            "Arabic already had a high oral-poetic culture; inimitability contests (muʿāraḍa) were a known genre. Later Muslim judges are not a neutral court. "
            "Ummī is read as 'illiterate' in dawah and as 'gentile / unscriptured' in much academic work — the premise 'an illiterate man wrote this' is not secure. "
            "Homer, the Hebrew Bible, and Shakespeare also have devotees who call the text unmatched. A unique religious register is not a laboratory result. "
            "If the criterion is 'moves believers in Arabic,' it cannot be adjudicated by non-Arabic speakers, which is most of the human race.",
            quotes=[
                Q(
                    "The Qur'an's 'challenge' is not a well-posed empirical test. Any produced text can be dismissed as unlike the inimitable original, by definition.",
                    "Standard philosophy-of-religion objection",
                    "Unfalsifiability of taḥaddī (paraphrase of a common analytic critique)",
                ),
            ],
            data_points=[
                D("Musaylima and other ridda-era speakers produced rhymed utterances that Muslims judged inferior — the judgment is intra-communal.", "Early Islamic historiography (sīra / maghāzī)"),
                D("Ummī: 'illiterate' vs 'not of the scriptured peoples' is a live philological dispute.", "EQ / academic lexica on ummī"),
            ],
            sources=[
                S("Stanford Encyclopedia — Arabic linguistic thought (Jurjānī context)", "https://plato.stanford.edu/entries/arabic-islamic-language/"),
            ],
        ),
        counters=[
            {
                "against": "Pastiche attempts",
                "claim": "Someone on the internet wrote a sūrah, so the challenge is met.",
                "reply": "That is not how either side scores. Ask what the criterion is first. If they cannot name one a non-Muslim Arabist could apply, the challenge is theology, not a contest.",
            },
            {
                "against": "Dismissing all literary quality",
                "claim": "The Qur'an is just bad Arabic / a jumble.",
                "reply": "That is a 19th-century hangover. Nöldeke disliked some shifts; Jurjānī, Sells, Neuwirth, and Farrin describe a real aesthetic. Quality ≠ prophecy. Do not win a cheap round by sounding like you cannot hear the text.",
            },
        ],
        live={
            "if_they_say": "Nobody has met the Qur'an's challenge in 1400 years.",
            "you_say": "Name the public test. If 'like it' means 'indistinguishable to a Muslim jury,' the challenge cannot fail. Separate: (1) is the Arabic extraordinary, (2) is that a proof of God.",
            "dont_overclaim": "Don't pretend the Qur'an is aesthetically ordinary. Don't pretend unmet taḥaddī is a controlled experiment.",
        },
        crux="Is there a publicly specified, non-circular test for 'a sūrah like it,' or is i'jaz a verdict of the believing community?",
        debate_use="Force a rubric before trading examples. Then decide whether literary uniqueness, if granted, licenses a metaphysical conclusion.",
    ),
    card(
        "ring-composition",
        2,
        "Literary",
        "Ring composition / chiasmus / concentric design",
        typ="literary structure",
        popularity="Very high",
        why=(
            "This is the flagship modern literary-miracle claim (Farrin, Cuypers, then Nouman Ali Khan's popularization). "
            "It answers the old charge that the Qur'an is disjointed — without needing microscopes."
        ),
        claimant=side(
            "Sūrahs such as al-Baqara and Yūsuf, and on some accounts the corpus as a whole, are built as rings: A–B–C–B'–A', with the theological payload at the centre. That is too tight to be accident or late committee stitching.",
            "Raymond Farrin maps parallel, chiastic, and concentric symmetries at verse, sūrah, pair, group, and whole-Muṣḥaf scale; he reads this as evidence of unified composition. "
            "Michel Cuypers applies 'Semitic rhetoric' (the biblical-studies toolkit of Roland Meynet) to Qur'anic sūrahs and finds the same symmetries. "
            "Mustansir Mir, via Farāhī and Iṣlāḥī, had already argued that each sūrah has an ʿamūd (pillar-theme) and that arrangement is exegetically load-bearing. "
            "Bayyinah / Nouman Ali Khan popularized ring charts for English audiences: the 'middle nation' (2:143) sitting at the structural middle of al-Baqara is the emblematic exhibit.",
            quotes=[
                Q(
                    "Farrin applies to the Qur'an critical tools such as ring composition to argue that the received text … is not a jumble of revelations … but a carefully composed text filled with deep structural parallels.",
                    "Martyn Smith",
                    "blurb for Farrin, Structure and Qur'anic Interpretation",
                    "https://www.whitecloudpress.com/structure-and-qur-anic-interpretation/",
                ),
            ],
            data_points=[
                D("Al-Baqara: commonly analysed as a large ring whose centre is the umma wasaṭ / qibla passage (around 2:142–152).", "Farrin 2014; popular NAK charts"),
                D("Yūsuf is the stock 'complete story in one sūrah' plus proposed concentric scenes around the reunion/recognition.", "Literary studies of Q 12"),
                D("Cuypers: symmetry, not Greek linear rhetoric, is the compositional code of Semitic sacred speech.", "Cuypers, The Composition of the Qur'an (2015)"),
            ],
            sources=[
                S("Farrin 2014 — Structure and Qur'anic Interpretation", "https://iqsaweb.org/2014/11/24/farrin_structure-and-quranic-interpretation/"),
                S("Cuypers — Semitic rhetoric / naẓm", "https://doi.org/10.3366/jqs.2011.0003"),
                S("Mustansir Mir — Coherence in the Qur'an", "https://archive.org/details/CoherenceInTheQuranMustansirMir"),
            ],
        ),
        critic=side(
            "Ring structure is a real ancient Near Eastern habit (Bible, Homer, Ugarit). Finding it in the Qur'an shows participation in a known aesthetic, not a unique divine fingerprint. The maps are often drawn after the conclusion.",
            "Nicolai Sinai's review of Cuypers and Farrin ('Going Round in Circles') is the academic brake: unit-cuts are under-determined; rhyme is under-used; once you may choose the joints, rings become easy to 'discover.' "
            "Biblical studies already spent a century on chiasmus — including notorious over-mapping. The same temptation is now in Qur'anic studies. "
            "A redactor can impose symmetry as well as an author; structure does not by itself date the text to Muhammad or to God. "
            "If chiasmus is proof of God, large parts of the Hebrew Bible are equally miraculous on the same rule — which Muslim polemic against biblical 'corruption' then has to swallow or special-plead.",
            quotes=[
                Q(
                    "Going Round in Circles",
                    "Nicolai Sinai",
                    "Review essay on Cuypers and Farrin, Journal of Qur'anic Studies 19.2 (2017)",
                    "https://www.euppublishing.com/doi/abs/10.3366/jqs.2017.0284",
                ),
            ],
            data_points=[
                D("Chiasmus is standard in biblical rhetoric (e.g. many psalms, Genesis narratives). Uniqueness fails if the device is shared.", "Biblical rhetorical criticism"),
                D("Farrin's whole-Qur'an ring (centring 54–55) is more speculative than intra-sūrah rings.", "Farrin 2014, conclusion; even sympathetic reviewers flag this"),
            ],
            sources=[
                S("Sinai 2017 review essay (JQS)", "https://www.euppublishing.com/doi/abs/10.3366/jqs.2017.0284"),
                S("IQSA notice of Farrin", "https://iqsaweb.org/2014/11/24/farrin_structure-and-quranic-interpretation/"),
            ],
        ),
        counters=[
            {
                "against": "Apologetic overclaim",
                "claim": "Only God could have nested rings in 6236 verses.",
                "reply": "Oral composers and redactors produce rings. Grant the art; ask why this art is a theistic proof rather than a literary fact.",
            },
            {
                "against": "Skeptical overclaim",
                "claim": "There is no structure; Orientalists settled that.",
                "reply": "The disjointedness cliché is outdated. Argue Sinai's methodological caution, not 1860.",
            },
        ],
        live={
            "if_they_say": "Ring structure in al-Baqara proves the Qur'an is from God.",
            "you_say": "Grant the chart if the joints are argued, not doodled. Then: Bible and ancient poetry do this too. Structure is evidence of design-in-the-literary-sense, not of a sender outside the world — unless you apply the same rule to every chiastic scripture.",
            "dont_overclaim": "Don't call Farrin a dawah pamphlet; he is a literary Arabist. Don't treat every colour-coded triangle as peer-reviewed.",
        },
        crux="Are proposed rings constrained enough to be discoveries rather than drawings — and if real, do they prove divinity or only composition?",
        debate_use="Ask them to justify two or three joints in one sūrah. Then apply the same standard to a biblical chiasm.",
    ),
    card(
        "iltifat",
        3,
        "Literary",
        "Iltifāt: sudden shifts of person, number, tense",
        typ="rhetoric / grammar",
        popularity="Very high",
        why=(
            "Nöldeke called person-shifts ugly; Muslim balāgha and Abdel Haleem call them a device. "
            "Nouman Ali Khan's teaching lives here: the jump is the point."
        ),
        claimant=side(
            "Iltifāt (literally 'turning') is a named Arabic rhetorical figure: the speaker switches person (He/We/I, you/they), number, or tense to wake the listener, shift intimacy, or mark theology. It is not a slip.",
            "M.A.S. Abdel Haleem's 1992 BSOAS article is the academic receipt against Nöldeke's 'nicht schöner Weise.' Classical critics (Ibn al-Athīr, al-Zarkashī, al-Suyūṭī) already catalogued the types. "
            "Standard exhibit: Q 1:5–7 moves from third-person praise of God to second-person 'You we worship'; Q 10:22–23, 36:22, and many 'We/He' divine-voice shifts. "
            "Bayyinah lessons treat each jump as a camera-cut: from narration to address, from majesty (We) to singularity (I), from talking about a group to pinning one hearer. "
            "If translators flatten the pronouns into consistent English, the device vanishes and Western readers infer chaos.",
            quotes=[
                Q(
                    "The grammatical persons change from time to time in the Qur'ān in an unusual and not beautiful way (nicht schöner Weise).",
                    "Theodor Nöldeke",
                    "Neue Beiträge zur semitischen Sprachwissenschaft (quoted by Abdel Haleem 1992)",
                    "https://doi.org/10.1017/S0041977X00003621",
                ),
                Q(
                    "Ibn al-Athīr … classed it among the 'remarkable things and exquisite subtleties we have found in the Glorious Qur'ān.'",
                    "M.A.S. Abdel Haleem",
                    "Grammatical Shift for Rhetorical Purposes: Iltifāt…, BSOAS 55.3 (1992)",
                    "https://doi.org/10.1017/S0041977X00003621",
                ),
            ],
            data_points=[
                D("Abdel Haleem 1992: shifts are patterned, not random; types include person, number, addressee, tense, case, noun-for-pronoun.", "BSOAS 55.3"),
                D("Q 1:5 is the textbook He → You turn at the hinge of al-Fātiḥa.", "https://quran.com/1"),
            ],
            sources=[
                S("Abdel Haleem 1992 (DOI)", "https://doi.org/10.1017/S0041977X00003621"),
                S("SOAS eprints PDF", "https://eprints.soas.ac.uk/7308"),
                qv("1/5", "Iyyāka naʿbudu — the Fātiḥa turn"),
            ],
        ),
        critic=side(
            "Some shifts are powerful rhetoric. Some look like oral composition, formula-splicing, or later editorial joins. Calling every anomaly iltifāt is an unfalsifiable rescue.",
            "Nöldeke was aesthetically prejudiced, but he was pointing at a real roughness that even Muslim grammarians sometimes filed under ḍarūra or variant reading rather than beauty. "
            "Oral performance (Neuwirth) predicts person-shifts because the reciter re-orients to a live audience. That is skill; it is also human. "
            "A device attested in pre-Islamic poetry and in the Bible (Hebrew also switches persons) cannot be a unique Qur'anic miracle. "
            "The live abuse: when a pronoun has no plausible rhetorical payoff, apologetics still stamps 'iltifāt' and ends the inquiry.",
            data_points=[
                D("Person-shift exists in pre-Islamic qaṣīda and in biblical Hebrew narrative/poetry. Shared toolkit, not a fingerprint.", "Arabic balāgha manuals; Hebrew stylistics"),
                D("Some 'shifts' coincide with proposed secondary insertions or formula boundaries in critical sūrah analysis.", "Neuwirth / Sinai literary-historical school"),
            ],
            sources=[
                S("Abdel Haleem 1992 — read the examples, not only the slogan", "https://eprints.soas.ac.uk/7308"),
            ],
        ),
        counters=[
            {
                "against": "Grammar-error slogan",
                "claim": "Iltifāt is just bad grammar.",
                "reply": "That is not how Arabic rhetoric works. Name the type, show a parallel in Jāhilī poetry or Qur'anic pattern, then argue payoff. 'Error' is a Western-schoolroom category.",
            },
            {
                "against": "Everything is iltifāt",
                "claim": "Every pronoun jump is a miracle.",
                "reply": "Then the term explains nothing. Demand a meaning-difference the shift produces. If none, you may have a join, a formula, or a qirāʾa.",
            },
        ],
        live={
            "if_they_say": "The Qur'an switches 'He' and 'We' because Muhammad got confused.",
            "you_say": "Read Abdel Haleem against Nöldeke. Then ask whether a named, pre-existing balāgha device is a miracle or just how this register talks. Confusion is the weak skeptical line; 'attested rhetoric ≠ divinity' is the strong one.",
            "dont_overclaim": "Don't call Nöldeke the last word. Don't call every shift a fingerprint of God.",
        },
        crux="For a given shift: is there a patterned rhetorical payoff, an oral-formula join, or an unfalsifiable sticker that says 'iltifāt'?",
        debate_use="Do one verse on the whiteboard. If they cannot say what the camera-cut does, they are slogan-ing. If you cannot allow any join to be messy, you are slogan-ing too.",
    ),
    card(
        "nazm-coherence",
        4,
        "Literary",
        "Naẓm: the sūrah as a unity, not a scrapbook",
        typ="literary / exegetical method",
        popularity="High",
        why="The 'disjointed Qur'an' jibe is still used in Christian and New Atheist polemic. Farāhī–Iṣlāḥī–Mir is the Muslim literary answer; it is older than YouTube i'jaz.",
        claimant=side(
            "Each sūrah has a governing theme (ʿamūd). Adjacent sūrahs pair. Occasions of revelation do not license reading the Muṣḥaf as shuffled index cards.",
            "Ḥamīd al-Dīn Farāhī and Amīn Aḥsan Iṣlāḥī rebuilt tafsīr around naẓm. Mustansir Mir's Coherence in the Qur'an is the English doorway. "
            "Neal Robinson (Discovering the Qur'an) — a non-Muslim — also argued for sequential and structural reading against the 'no context' pamphlet. "
            "This is closer to classical munāsabāt (sūra-connectivity) than to Bucaille. NAK's 'sūrah as a conversation' is the popular form.",
            quotes=[
                Q(
                    "With most Muslim exegetes, the basic unit of Qur'an study is one or a few verses taken in isolation…",
                    "Mustansir Mir",
                    "Coherence in the Qur'an (describing the problem Iṣlāḥī attacked)",
                    "https://archive.org/details/CoherenceInTheQuranMustansirMir",
                ),
            ],
            sources=[
                S("Mir — Coherence in the Qur'an", "https://archive.org/details/CoherenceInTheQuranMustansirMir"),
                S("Cuypers on naẓm via Semitic rhetoric", "https://doi.org/10.3366/jqs.2011.0003"),
            ],
        ),
        critic=side(
            "Thematic unity can be found in any corpus if the theme is allowed to be vague ('guidance,' 'tawḥīd,' 'judgment'). Some sūrahs are composite on the face of the text.",
            "Even Muslim tradition records staggered revelation and later arrangement. Unity of recitation-sūrah is not automatically unity of first delivery. "
            "Academic literary-historical work (Neuwirth, Sinai) often grants inner-sūrah craft and still reconstructs growth, Medinan insertions in Meccan sūrahs, and editorial frames. "
            "Iṣlāḥī's ʿamūd is sometimes a Procrustean bed: verses that do not fit are declared 'preamble' or 'parenthesis' until they do.",
            data_points=[
                D("Traditional asbāb al-nuzūl already imply many sūrahs are multi-occasion. Naẓm is a reading strategy for the compiled text.", "ʿUlūm al-Qurʾān manuals"),
                D("Proposed Medinan insertions in Meccan sūrahs are a standard (contestable) tool in critical sūrah studies.", "Neuwirth school"),
            ],
            sources=[
                S("Mir — Coherence in the Qur'an", "https://archive.org/details/CoherenceInTheQuranMustansirMir"),
            ],
        ),
        live={
            "if_they_say": "The Qur'an is a jumble with no order.",
            "you_say": "That is not the state of the field. Ask whether they mean (a) linear Greco-Roman oration, which it is not, or (b) no craft, which literary studies no longer hold. Then separate compiled unity from single-sitting authorship.",
            "dont_overclaim": "Don't hide asbāb al-nuzūl. Don't hide that ʿamūd can be painted on.",
        },
        crux="Is sūrah-unity a property of the compiled text, of the original delivery, or of the interpreter's theme?",
        debate_use="Pick one short sūrah both of you have read. Map theme vs. proposed join. Do not fight in slogans about 114 chapters.",
    ),
    card(
        "lexical-precision",
        5,
        "Literary",
        "Lexical precision: why this word, not its near-synonym",
        typ="balāgha / pedagogy",
        popularity="Very high",
        why="This is Nouman Ali Khan's home turf. It is also the easiest place for confirmation bias: after the fact, every synonym feels inevitable.",
        claimant=side(
            "Qur'anic word choice is never 'close enough.' Roots, patterns, definite vs indefinite, and tiny differences between parallel stories are load-bearing. That density is the miracle non-Arabic speakers miss.",
            "Exhibits: raḥmān vs raḥīm; islam vs īmān vs iḥsān; parallel punishment stories that swap one verb; the claim that no synonym is wasted. "
            "Classical balāgha (Jurjānī on naẓm as the fit of meaning to wording) is the high ancestor. NAK / Bayyinah Divine Speech is the mass-market form: 'what happens if you swap this word.' "
            "Mutashābihāt that differ by a letter are treated as intended pedagogical contrast, not oral drift.",
            data_points=[
                D("Jurjānī: eloquence is not rare words; it is the arrangement that makes this wording the only wording.", "Dalāʾil al-iʿjāz"),
                D("Popular NAK method: compare two similar āyāt and narrate why the difference is theologically required.", "Bayyinah Divine Speech"),
            ],
            sources=[
                qv("55/1-4", "Al-Raḥmān taught the Qur'an — a typical NAK lexical door"),
                S("Stanford Encyclopedia — Arabic linguistic thought", "https://plato.stanford.edu/entries/arabic-islamic-language/"),
            ],
        ),
        critic=side(
            "Post-hoc synonym sermons always work. Oral formulae, rhyme-force (fāṣila), and later theological reading can explain many 'precise' swaps without a divine thesaurus.",
            "If two parallel pericopes differ, the miracle-reading says 'deliberate contrast'; the critical reading says 'performance variants / memory / redaction.' Both can produce a story. "
            "English analog: clever close-reading of Shakespeare is real, and it does not make Shakespeare a prophet. "
            "Some NAK-style lessons smuggle weak etymology (root-mysticism) that professional Arabic linguistics does not carry.",
            data_points=[
                D("End-rhyme (fāṣila) sometimes selects a word that also happens to be theologically usable — dual explanation.", "Qur'anic rhyme studies"),
                D("Formulaic oral composition (Parry–Lord applied cautiously to early Arabic) predicts near-synonym slots.", "Oral-formulaic theory"),
            ],
            sources=[
                S("Michael Sells — Approaching the Qur'an (sound and meaning)", "https://www.whitecloudpress.com/approaching-the-quran/"),
            ],
        ),
        live={
            "if_they_say": "Every Qur'anic word is the only possible word.",
            "you_say": "Ask for a swap that would break the meaning, not a homily. Then: even if the wording is superb, superb wording is what great texts have. Precision is a literary claim until you add a second premise that only God is precise.",
            "dont_overclaim": "Don't mock Arabic study. Don't treat Bayyinah as a critical edition.",
        },
        crux="Is a given word-choice forced by meaning, by rhyme/formula, or by later preaching that cannot imagine an alternative?",
        debate_use="Demand one minimal pair (two āyāt, one swapped verb). Score: semantic necessity vs. homily.",
    ),
    card(
        "sound-saj",
        6,
        "Literary",
        "Sound: sajʿ, fāṣila, rhythm, and aural design",
        typ="orality / poetics",
        popularity="High",
        why="The Qur'an insists it is not poetry (36:69, 69:41) while using rhyme and cadence. That paradox is either a unique genre-miracle or a known late-antique rhymed register.",
        claimant=side(
            "The recitation is a designed sound-object: end-rhyme that can shift when the meaning shifts, dense assonance, and a cadence that is not metrical poetry and not flat prose. That third genre is part of the taḥaddī.",
            "Michael Sells trains ears on the early Meccan sūrahs as acoustic events. The claim: translation cannot carry the miracle because the miracle is partly phonetic. "
            "When a sūrah changes its end-rhyme at a thematic hinge, that is read as structural punctuation (a cousin of ring-mapping).",
            quotes=[
                Q(
                    "It is not the word of a poet; little do you believe.",
                    "Qur'an 69:41",
                    "Genre claim",
                    "https://quran.com/69/41",
                ),
            ],
            sources=[
                qv("69/41"),
                qv("36/69"),
                S("Sells — Approaching the Qur'an", "https://www.whitecloudpress.com/approaching-the-quran/"),
            ],
        ),
        critic=side(
            "Sajʿ of the kuhhān (soothsayers) is the nearby late-antique register. The Qur'an protests it is not poetry because contemporaries heard it in that neighbourhood. Rhymed prose is historically situated, not genre-ex nihilo.",
            "Early opponents' accusation 'poet / soothsayer / possessed' (Q 52:29–30, 69:40–42) is evidence of reception, not of uniqueness. "
            "Some fāṣila words look selected for sound first (a known cost of sajʿ). That cuts against total semantic inevitability. "
            "Aural power is not a truth-maker: liturgy, mantra, and oratory all move people.",
            data_points=[
                D("Q 69 and 52 explicitly fend off 'poet' and 'soothsayer' labels — the comparison was live in the first audience.", "https://quran.com/69"),
                D("Neuwirth: Meccan sūrahs as liturgical-oral communication, not books written for silent reading.", "Neuwirth, The Qur'an and Late Antiquity"),
            ],
            sources=[
                qv("52/29-30"),
                S("Angelika Neuwirth — The Qur'an and Late Antiquity (overview)", "https://global.oup.com/academic/product/the-quran-and-late-antiquity-9780190921286"),
            ],
        ),
        live={
            "if_they_say": "It's not poetry and not prose — that's the miracle.",
            "you_say": "It's rhymed, rhythmic sacral speech in a culture that already had sajʿ. Unique mix is possible; 'never heard on earth' is a slogan. Play a recitation, then ask what would count as a human analog.",
            "dont_overclaim": "Don't deny the sound. Don't deny the kāhin comparison the Qur'an itself is busy fighting.",
        },
        crux="Is Qur'anic sajʿ a new genre only God could invent, or a transformation of known Arabian rhymed registers?",
        debate_use="Define poetry (ʿarūḍ meter) vs sajʿ before anyone says 'not poetry.' Then the 36:69 line is about meter, not about 'no rhetoric.'",
    ),
    card(
        "yusuf-narrative",
        7,
        "Literary",
        "Yūsuf as a complete narrative (and the 'best of stories')",
        typ="narrative art",
        popularity="High",
        why="Q 12 is the exhibit when someone says the Qur'an cannot tell a story. It is also the exhibit for biblical-intertextual debate.",
        claimant=side(
            "Sūrat Yūsuf is a single, closed, morally aimed novella with irony, delayed recognition, and a stated lesson. That is literary control, not scraps.",
            "Q 12:3 calls it aḥsan al-qaṣaṣ. Compared with Genesis 37–50, the Qur'anic telling is tighter, less dynastic-soap, more tawḥīd. "
            "Proposed rings in the sūrah (brothers' plot ↔ reunion; two dreams; two temptations) are used as a literary-miracle chart. "
            "NAK and many khaṭībs use Yūsuf as proof that the Qur'an can do long-form when it wants — so other sūrahs' 'jumps' are choices, not inability.",
            sources=[
                qv("12/3", "aḥsan al-qaṣaṣ"),
                S("Farrin / literary studies of Q 12", "https://iqsaweb.org/2014/11/24/farrin_structure-and-quranic-interpretation/"),
            ],
        ),
        critic=side(
            "A good retelling of a well-known Joseph cycle is what late-antique preaching does. Genesis is the longer source-tradition; the Qur'an is a homiletic recast, not an independent historical report.",
            "Missing are Genesis's Judah-Tamar, Joseph's political land-policy, etc. That can be 'refinement' or 'loss of memory / different midrashic mix.' "
            "Some distinctive Qur'anic details (the shirt from the back, the banquet of women) have Jewish and Christian narrative cousins. "
            "One polished sūrah does not make every sūrah a novella; it shows the corpus can do this genre.",
            data_points=[
                D("Joseph is the rare Qur'anic prophet-story told in one continuous sūrah rather than in scattered pericopes.", "Contrast Q 12 with Mūsā across many sūrahs"),
                D("Intertextual studies treat Q 12 as conversation with Genesis plus later lore, not as a vacuum.", "Reynolds, The Qur'an and the Bible"),
            ],
            sources=[
                S("Gabriel Said Reynolds — The Qur'an and the Bible", "https://yalebooks.yale.edu/book/9780300181320/the-quran-and-the-bible/"),
            ],
        ),
        live={
            "if_they_say": "The Qur'an can't even tell a story straight.",
            "you_say": "Open Yūsuf. Then decide whether 'straight' means 'Genesis order' or 'its own homiletic order.' Quality of Q 12 is not in serious dispute; source-dependence is.",
            "dont_overclaim": "Don't say Q 12 has no biblical relationship. Don't say the rest of the Qur'an is therefore also a novella.",
        },
        crux="Is Q 12 independent revelation that happens to parallel Genesis, or a literary recast of a shared late-antique Joseph tradition?",
        debate_use="List three details unique to Genesis and three unique to Q 12. Argue dependence vs. selective retelling vs. shared oral pool.",
    ),
    card(
        "classical-vs-modern-ijaz",
        8,
        "Literary",
        "Classical i'jaz (Jurjānī) vs modern 'miracle hunting'",
        typ="method",
        popularity="High",
        why="Mixing Jurjānī with Bucaille and with ring-charts hides that 'Qur'anic miracle' has meant three different things.",
        claimant=side(
            "The core claim was always the speech. Modern literary analysis (rings, iltifāt, naẓm) is a continuation of balāgha with new diagrams. Scientific i'jaz is an optional extra.",
            "Al-Jurjānī: i'jaz is in naẓm — the fusion of wording and meaning — not in rare words or in future science. "
            "A Muslim can therefore drop embryology slides and still have the classical case. NAK is closer to this lane than Harun Yahya is.",
            sources=[
                S("Stanford Encyclopedia — Arabic linguistic thought", "https://plato.stanford.edu/entries/arabic-islamic-language/"),
                S("Ahmad Dallal on science and the Qur'an (EQ-related work)", "https://yalebooks.yale.edu/book/9780300177718/islam-science-and-the-challenge-of-history/"),
            ],
        ),
        critic=side(
            "Modern dawah often needs scientific i'jaz because non-Arabic audiences cannot hear naẓm. That is a category shift: from 'taste this Arabic' to 'the verse predicted NASA.' The second is doing different, weaker work.",
            "Classical scholars also claimed ghayb (unseen news) and sometimes cosmic signs — so the split is not absolute. "
            "But 20th-century Bucailleism is historically new as a mass proof. Ahmad Dallal and others treat it as a modern anxiety about science, not as tafsīr as-usual. "
            "Hamza Tzortzis publicly walked back the scientific-miracle method while keeping a literary i'jaz case — an internal Muslim tell that the categories were fused for the stage.",
            data_points=[
                D("Bucaille, The Bible, the Qur'an and Science (1976) is the mass-market origin of modern i'jaz ʿilmī.", "https://al-bab.com/science-and-quran"),
                D("Tzortzis: later essay criticizing scientific-miracle apologetics as methodologically unsound.", "Hamza Tzortzis, 'Does the Qur'an Contain Scientific Miracles?'"),
            ],
            sources=[
                S("al-bab — Science and the Qur'an (history of Bucailleism)", "https://al-bab.com/science-and-quran"),
                S("Tzortzis — Does the Qur'an Contain Scientific Miracles?", "https://www.hamzatzortzis.com/does-the-quran-contain-scientific-miracles-a-new-approach/"),
            ],
        ),
        live={
            "if_they_say": "The miracle of the Qur'an is science.",
            "you_say": "That is not what Jurjānī was doing. Ask them to pick a lane: speech, or concordism. Mixing lanes lets them retreat from whichever one you just broke.",
            "dont_overclaim": "Don't tell Muslims they are forbidden from literary i'jaz if science slides fail. Don't tell them Jurjānī already taught Big Bang.",
        },
        crux="Are we scoring 7th-century Arabic rhetoric, or 20th-century scientific concordism? They are not the same argument.",
        debate_use="Make them choose one proof-type for the timed round. Literary can survive a failed embryology slide. Concordism cannot hide behind iltifāt.",
    ),
    card(
        "dhul-qarnayn-mud",
        9,
        "Historical",
        "Dhū l-Qarnayn and the sun setting in a muddy spring (18:86)",
        typ="history + cosmology + intertext",
        popularity="Very high",
        why=(
            "The honesty test for this whole page. If a 'miracle' desk cannot allow a literal or legendary reading, it is apologetics. "
            "If your 'error' page cannot allow phenomenological and qirāʾa complexity, it is polemic."
        ),
        claimant=side(
            "Wajada ('he found') reports Dhū l-Qarnayn's visual experience at a western shore: the sun appeared to set in a dark/muddy (or hot) spring. Ibn Kathīr: anyone at the sea sees this. No cosmology is asserted.",
            "Two canonical readings: ḥamiʾa (muddy) and ḥāmiya (hot). al-Ṭabarī knows both. "
            "Jalālayn and many modern translations insert 'as if' / 'appeared.' "
            "Dhū l-Qarnayn is often identified with Cyrus (moralized monotheist king) rather than Alexander, detaching the passage from the Alexander Romance's cosmology. "
            "The point of the pericope is justice at the edges of power (18:87–88), not astrophysics.",
            quotes=[
                Q(
                    "Until, when he reached the setting of the sun, he found it setting in a muddy spring, and found by it a people…",
                    "Qur'an 18:86",
                    "Hafs reading ḥamiʾa",
                    "https://quran.com/18/86",
                ),
                Q(
                    "…he saw the sun as if it were setting in the ocean. This is something which everyone who goes to the coast can see: it looks as if the sun is setting into the sea but in fact it never leaves its path…",
                    "Ibn Kathīr",
                    "Tafsīr on 18:86",
                    "https://quran.com/18:86/tafsirs/en-tafisr-ibn-kathir",
                ),
            ],
            data_points=[
                D("Qirāʾāt: ḥamiʾa (muddy) vs ḥāmiya (hot). Both are canonical; neither says 'nuclear fusion.'", "al-Ṭabarī on 18:86"),
                D("Ibn Kathīr explicitly rejects storyteller versions in which the traveller reaches the sun's astronomical setting-place.", "Tafsīr Ibn Kathīr 18:86"),
            ],
            sources=[
                qv("18/86"),
                S("Ibn Kathīr on 18:86 (quran.com)", "https://quran.com/18:86/tafsirs/en-tafisr-ibn-kathir"),
                S("al-Ṭabarī on 18:86", "https://quran.com/al-kahf/86/tafsirs/ar-tafsir-al-tabari"),
            ],
        ),
        critic=side(
            "The passage is a recast of the late-antique Alexander Legend: the hero reaches the place where the sun sets in a fetid sea. Early tafsīr and hadith cosmology are often more literal than modern 'it just looked like that.'",
            "Kevin van Bladel and others argue Q 18:83–102 tracks the Syriac Alexander Legend (Neshana) closely: western journey, fetid sun-set waters, eastern rising, gates against apocalyptic peoples. "
            "If the narrator wanted phenomenology, Arabic can mark simile; here God reports what the hero found, including a people at the sun's setting-place. "
            "Muqātil, Ibn ʿAbbās/Kaʿb reports in al-Ṭabarī, and pre-Islamic verse cited there treat a real muddy spring. "
            "The Abu Dharr hadith of the sun's setting, prostration under the Throne, and asking permission to rise (tied to 36:38) shows a 7th/8th-century cosmology in the same community that is not 'optical illusion at the beach.'",
            quotes=[
                Q(
                    "The Qur'an's 'spring of dark mud' is the motif-level heir of that fetid sea.",
                    "Historical-critical summary of the Alexander-Legend parallel",
                    "Dhū l-Qarnayn / setting-sun file",
                    "https://historicalchristian.faith/doctrine/doctrines/dhul-qarnayn/arguments/setting-sun-cosmology.html",
                ),
            ],
            data_points=[
                D("Alexander Legend: sun sets in a fetid/muddy ocean at the world's western edge — the narrative cousin of 18:86.", "van Bladel in Reynolds (ed.), The Qur'an in Its Historical Context"),
                D("Sahih al-Bukhari: sun prostrates beneath the Throne at sunset and asks leave to rise (Abu Dharr).", "https://sunnah.com/bukhari:3199"),
            ],
            sources=[
                S("van Bladel — Alexander Legend in Q 18 (chapter overview via Reynolds 2008)", "https://www.routledge.com/The-Quran-in-Its-Historical-Context/Reynolds/p/book/9780415491693"),
                S("Abu Dharr / sun hadith (Bukhari 3199)", "https://sunnah.com/bukhari:3199"),
                qv("36/38", "Sun running to a resting-place (mustaqarr)"),
            ],
        ),
        counters=[
            {
                "against": "Apologetic 'only a metaphor'",
                "claim": "No pre-modern Muslim read 18:86 as a real setting-place.",
                "reply": "False. Phenomenology is one classical option (Ibn Kathīr). Literal and legendary-geographic options are also in the tafsīr archive. Cite both.",
            },
            {
                "against": "Skeptical 'gotcha cosmology'",
                "claim": "18:86 alone falsifies Islam at a stroke.",
                "reply": "Only if (a) the verse asserts divine astrophysics rather than the traveller's finding, and (b) your rule also kills every biblical 'the sun stood still' as the same class. Apply the rule to both canons or admit genre.",
            },
        ],
        live={
            "if_they_say": "The Qur'an says the sun sets in a muddy puddle.",
            "you_say": "Read 18:86 aloud, then Ibn Kathīr's 'as if at the coast,' then the Alexander-Legend parallel, then Bukhari 3199. The honest position is: modern apologetics prefers appearance; early narrative context and some hadith cosmology are more concrete. Do not let either side hide a source.",
            "dont_overclaim": "Don't pretend ḥāmiya vs ḥamiʾa solves cosmology. Don't pretend Ibn Kathīr is the only tafsīr.",
        },
        crux="Does 18:86 assert a world-edge cosmology (shared with the Alexander Legend), or report a traveller's sight of a western sea — and which reading did the first audiences hear?",
        debate_use="This is the objectivity card. Put Legend, tafsīr, qirāʾa, and hadith on the table before anyone says 'miracle' or 'disproved.'",
    ),
    card(
        "concordism-method",
        10,
        "Scientific",
        "I'jaz ʿilmī as a method: concordism, not tafsīr",
        typ="method / science",
        popularity="Very high",
        why="If you do not kill the method, you will play 40 separate verse-whack-a-mole games. Bucaille, Moore, Yahya, Naik vs Dallal, Edis, Tzortzis's later essay.",
        claimant=side(
            "Q 41:53 promises signs in the horizons and in selves. When a verse stably matches a later discovery, that is a sign for this age. The method is: read the Arabic without forcing, then look at nature.",
            "Maurice Bucaille (1976) contrasted biblical 'errors' with Qur'anic 'anticipation.' Keith Moore's Islamic-edition embryology gave the claim medical prestige. "
            "Zaghloul El-Naggar, Zakir Naik, and Harun Yahya industrialized the slides. The steelman: God talks to all centuries; later science is a delayed tafsīr of what the words always allowed.",
            quotes=[
                Q(
                    "We shall show them Our signs in the horizons and in themselves until it becomes clear to them that it is the truth.",
                    "Qur'an 41:53",
                    "Proof-text of modern i'jaz ʿilmī",
                    "https://quran.com/41/53",
                ),
            ],
            sources=[
                qv("41/53"),
                S("Bucailleism as a historical phenomenon", "https://al-bab.com/science-and-quran"),
            ],
        ),
        critic=side(
            "Concordism: after a discovery, hunt a verse whose semantic range can be stretched to fit; ignore classical tafsīr, neighbouring verses, and misses. The same method 'finds' relativity in the Vedas and Big Bang in Genesis 1.",
            "Ahmad Dallal: this is a modern response to colonial scientific prestige, not classical exegesis. "
            "The method is asymmetric: hits are miracles; misses (18:86, 86:6–7, bones-before-flesh if read biologically, seven-band cosmos) become metaphor. "
            "Polysemy is then a one-way valve. Tzortzis's later critique from inside dawah is the receipt that the method was oversold.",
            data_points=[
                D("The same 41:53 was not used as a NASA-prediction engine by Ṭabarī or Rāzī. The genre is modern.", "History of tafsīr vs 20th-c i'jaz ʿilmī"),
                D("Parallel concordism exists for the Bible and Hindu texts — so 'my scripture predicted science' is a cheap universal.", "Comparative concordism"),
            ],
            sources=[
                S("Dallal — Islam, Science, and the Challenge of History", "https://yalebooks.yale.edu/book/9780300177718/islam-science-and-the-challenge-of-history/"),
                S("Tzortzis walk-back", "https://www.hamzatzortzis.com/does-the-quran-contain-scientific-miracles-a-new-approach/"),
                S("al-bab on Bucaille", "https://al-bab.com/science-and-quran"),
            ],
        ),
        live={
            "if_they_say": "The Qur'an predicted modern science.",
            "you_say": "Ask for the pre-discovery tafsīr, not the post-discovery slide. Then apply the same stretch to a miss. If hits are literal and misses are 'just imagery,' the method cannot lose.",
            "dont_overclaim": "Don't deny that some verses are compatible with later science. Compatibility is not prediction.",
        },
        crux="Is a scientific-miracle claim scored against 7th-century reachable meanings, or against 21st-century meanings the Arabic can be made to bear?",
        debate_use="Write the rule on paper before verses: no post-hoc stretch; classical range first; misses count.",
    ),
    card(
        "oral-poetics",
        11,
        "Literary",
        "Oral-aural poetics, 'qul,' and liturgical performance",
        typ="orality",
        popularity="Medium",
        why="A lot of 'jumps' that look like book-errors are performance features. That helps the literary case and also the human-author case.",
        claimant=side(
            "The Qur'an is shaped for recitation: vocatives, 'say' (qul), audience switches, refrain (e.g. al-Raḥmān 55). That is sophisticated oral literature, not dictation-noise.",
            "Neuwirth reads early sūrahs as liturgy-in-formation. Sells: sound is meaning. Refrain and call-response are design.",
            sources=[
                qv("55/13", "Which of your Lord's favours will you deny? — refrain"),
                S("Sells — Approaching the Qur'an", "https://www.whitecloudpress.com/approaching-the-quran/"),
            ],
        ),
        critic=side(
            "Oral art is exactly what gifted 7th-century reciters produce. Liturgical growth over a career (and after) predicts seams. Performance explains craft and composite-ness together.",
            "Qul can mark a later instructional frame. Refrains are cheap in oral culture (Psalm 136). Skill here is not scarce.",
            sources=[
                S("Neuwirth — The Qur'an and Late Antiquity", "https://global.oup.com/academic/product/the-quran-and-late-antiquity-9780190921286"),
            ],
        ),
        live={
            "if_they_say": "Random topic changes prove incompetence.",
            "you_say": "Try hearing it as liturgy, not as a modern chapter. Then: liturgy can be human. Oral craft ≠ God, but it does kill the 'incompetent editor' sneer.",
            "dont_overclaim": "Don't turn Neuwirth into a dawah witness. She is not arguing prophecy.",
        },
        crux="Are seams and switches liturgical art, redactional joins, or both?",
        debate_use="Play 30 seconds of Q 55. Argue refrain as design vs. as oral filler.",
    ),
    card(
        "biblical-intertext",
        12,
        "Literary",
        "Intertextual rewriting of biblical and extra-biblical lore",
        typ="literature + sources",
        popularity="High",
        why="Muslims call this 'correcting previous scripture.' Critics call it 'late-antique remix.' Both are literary claims before they are historical ones.",
        claimant=side(
            "The Qur'an knowingly re-reads prior revelation: same prophets, different theology (no crucifixion as Christian salvation; Abraham as proto-Muslim; Jesus as prophet). That is a literary-theological program, not plagiarism.",
            "Cuypers and Reynolds document deep biblical texture. The steelman: this is how scripture talks to scripture (as Chronicles re-reads Kings; as John re-reads Moses). "
            "Differences are then 'taḥrīf correction,' not mistakes.",
            sources=[
                S("Reynolds — The Qur'an and the Bible", "https://yalebooks.yale.edu/book/9780300181320/the-quran-and-the-bible/"),
                S("Cuypers on re-reading prior texts", "https://www.oasiscenter.eu/en/the-rule-of-the-koran-semitic-rhetoric"),
            ],
        ),
        critic=side(
            "A 7th-century preacher in a biblical world will sound biblical. When the recast matches Syriac homily, Infancy Gospel, or Alexander Legend more than the canonical Bible, 'correction of a lost original' is an extra hypothesis.",
            "Literary dependence can be oral and honorific, not copying a codex. But then 'historical miracle of unknown details' collapses into 'details current in the milieu.' "
            "You cannot use dependence as sophisticated theology in one breath and as 'Muhammad couldn't have known this' in the next.",
            sources=[
                S("Reynolds — The Qur'an and the Bible", "https://yalebooks.yale.edu/book/9780300181320/the-quran-and-the-bible/"),
            ],
        ),
        live={
            "if_they_say": "Muhammad stole the Bible.",
            "you_say": "It's a late-antique biblical world. Ask whether a given pericope tracks the canonical Bible or a homily/apocryphon. 'Steal' is a schoolyard word for intertextuality. 'Could not have known' is then usually false.",
            "dont_overclaim": "Don't deny the biblical texture. Don't call every parallel theft.",
        },
        crux="Is divergence from the Bible a correction of a lost original, a new theology, or a mix of lore the milieu already had?",
        debate_use="Pick one story (Sleepers, Alexander, infancy Jesus). Source-map it before anyone says miracle or theft.",
    ),
    card(
        "concision-density",
        13,
        "Literary",
        "Concision and semantic density (ījāz)",
        typ="style",
        popularity="Medium",
        why="A classical praise-term: much meaning in few words. Easy to claim; hard to score without Arabic.",
        claimant=side(
            "Short Meccan sūrahs pack eschatology, ethics, and sound in a handful of cola. That compression is a named virtue of i'jaz.",
            "Q 103, 108, 112 as exhibits. Jurjānī-style: removing a word collapses the meaning. NAK: English needs a paragraph where Arabic used a construct.",
            sources=[qv("112"), qv("103")],
        ),
        critic=side(
            "Compression is what slogans, oracles, and sajʿ do. Ambiguity can be read as depth or as under-specification. Untranslatability is true of all dense poetry.",
            "If extra meanings are generated by later tafsīr, the density was not all in the 7th-century hearer.",
            sources=[S("Sells — Approaching the Qur'an", "https://www.whitecloudpress.com/approaching-the-quran/")],
        ),
        live={
            "if_they_say": "You need a page of English for one āyah.",
            "you_say": "Often true of poetry. Density is a literary fact. It becomes a miracle only with the extra premise that this density is unmatched and unmatched-implies-God.",
            "dont_overclaim": "Don't pretend translation failure is unique to Arabic. Don't pretend Q 112 is shallow.",
        },
        crux="Is the compression unmatched in Arabic sacral speech, or typical of short oracular genres?",
        debate_use="Compare Q 112 with the Shema or a short Syriac homiletic line. Score uniqueness, not piety.",
    ),
    card(
        "oaths-imagery",
        14,
        "Literary",
        "Oaths, cosmic images, and sudden turns",
        typ="rhetoric",
        popularity="Medium",
        why="Early Meccan oath-clusters (wa-l-ʿādiyāt, wa-l-ṭīn, wa-l-shams) are a literary signature NAK and Sells both linger on.",
        claimant=side(
            "Series of oaths build a riddle whose answer is a moral/eschatological punch. The structure is deliberate suspense.",
            "Q 91, 93, 100. Images (charging mares, fig, night) are not random décor; they set up the asserted claim.",
            sources=[qv("91"), qv("93"), qv("100")],
        ),
        critic=side(
            "Arabian oath-style and biblical oath/creation catalogues exist. Impressive rhetoric, shared toolbox.",
            "Sometimes the logical link from oath-image to conclusion is associative rather than tight — oral riddle, not geometry.",
            sources=[qv("91")],
        ),
        live={
            "if_they_say": "Random swearing by horses and figs.",
            "you_say": "It's a genre: oath-cluster → assertion. Hear Q 91. Then: genre-competence is not prophecy.",
            "dont_overclaim": "Don't call it random. Don't call a qaṣīda oath-cluster impossible for humans.",
        },
        crux="Are oath-series a unique Qur'anic logic, or a shared Arabian/biblical rhetorical form?",
        debate_use="Read Q 91 in Arabic if anyone can; then translate the hinge 'qad aflaḥa…'",
    ),
    card(
        "unlettered-author",
        15,
        "Literary",
        "The unlettered messenger as literary premise",
        typ="authorship",
        popularity="Very high",
        why="Without ummī-as-illiterate, 'he could not have produced this' weakens. With it, the literary case becomes an origin story.",
        claimant=side(
            "Q 7:157 and the sīra present a messenger who did not produce books. The literary height is therefore not his craft but revelation.",
            "Dawah form: no notebooks, no poetic apprenticeship, no biblical library in Mecca, yet Yūsuf and legal rhetoric and balāgha.",
            sources=[qv("7/157", "al-nabī al-ummī"), qv("29/48")],
        ),
        critic=side(
            "Ummī plausibly means 'of the unscriptured,' not 'cannot write.' Late antique Ḥijāz had poets, scribes, and biblical lore in circulation (including via trade and Ḥanīfs). Oral genius is common in such cultures.",
            "Q 29:48 'you did not recite a book before' is compatible with oral biblical knowledge. The sīra is also a piety-narrative. "
            "Secretaries, Khadīja's Christian relative Waraqa, and the Qur'an's own opponents calling him a poet are part of the same file.",
            sources=[
                qv("29/48"),
                S("EQ / academic discussion of ummī (summary entry points via Reynolds milieu)", "https://yalebooks.yale.edu/book/9780300181320/the-quran-and-the-bible/"),
            ],
        ),
        live={
            "if_they_say": "An illiterate man could not write this.",
            "you_say": "Prove illiterate, not ummī. Then prove isolation from biblical and poetic speech. Then remember oral composers exist. Three premises, not one slogan.",
            "dont_overclaim": "Don't call him a librarian. Don't call the Ḥijāz a cultural vacuum.",
        },
        crux="Does ummī mean illiterate isolation, or 'not of the People of the Book' in a world already full of scripture-talk?",
        debate_use="Define ummī from usage (2:78, 3:20, 7:157, 62:2) before the Dickensian illiteracy story.",
    ),
    # Linguistic
    card(
        "clear-arabic",
        16,
        "Linguistic",
        "'Clear Arabic' vs hapax, opacity, and translation loss",
        typ="linguistics",
        popularity="High",
        why="Q 16:103, 26:195, 41:44 claim lisān ʿarabī mubīn. Obscure words and hapax are then either depth or a problem.",
        claimant=side(
            "The Qur'an is in clear Arabic, unmatched in purity and force. Difficult words are rare, eloquent, or theologically deep. Translation loss proves the miracle lives in Arabic.",
            "Mubīn is taken as 'self-explaining / lucid.' Loanwords are Arabized. Hapax are precision tools.",
            sources=[qv("26/195"), qv("16/103"), qv("41/44")],
        ),
        critic=side(
            "Mubīn can mean 'plainly Arabic' (not foreign speech) rather than 'easy.' The Qur'an itself mentions people calling it foreign (16:103). Early tafsīr debates gharīb words; that is not 'every child understood every line.'",
            "Untranslatability is true of Torah Hebrew and of poetry. It is not a unique miracle-marker.",
            sources=[qv("16/103"), qv("3/7", "muḥkam vs mutashābih")],
        ),
        live={
            "if_they_say": "It's perfectly clear Arabic.",
            "you_say": "Clear as in 'this is Arabic, not Persian,' or clear as in 'no gharīb, no mutashābih'? Q 3:7 exists. Don't equivocate.",
            "dont_overclaim": "Don't call the Qur'an gobbledygook. Don't call it a primer.",
        },
        crux="Does mubīn claim lucidity of content, or Arabic as the vehicle versus 'aʿjamī' speech?",
        debate_use="Read 16:103 and 3:7 as a pair. They tension.",
    ),
    card(
        "loanwords",
        17,
        "Linguistic",
        "Loanwords: Syriac, Ethiopic, Persian, Greek",
        typ="historical linguistics",
        popularity="High",
        why="Purity-miracle vs 'the Ḥijāz was multilingual.' Arthur Jeffery's Foreign Vocabulary is the old critical list; Muslim answers distinguish Arabized vs 'this isn't Arabic.'",
        claimant=side(
            "Fully Arabized loans are normal in every language and do not punctured i'jaz. The sentence-level naẓm is still Arabic. Some 'loans' are disputed cognates.",
            "Classical mufassirūn already noted words of foreign origin (Suyūṭī's lists). That did not cancel i'jaz for them because i'jaz was arrangement, not lexical isolation.",
            sources=[
                qv("16/103", "The 'foreign teaching' accusation"),
                S("Arthur Jeffery — The Foreign Vocabulary of the Qur'an (classic list)", "https://archive.org/details/foreignvocabular0000jeff"),
            ],
        ),
        critic=side(
            "A high density of Christian-Palestinian Aramaic/Syriac religious vocabulary (Arthur Jeffery; Luxenberg's stronger, much-contested thesis) situates the text in a biblical-lingo world. That supports milieu, not isolation-miracle.",
            "Luxenberg overreached (reading the Qur'an as a Syriac lectionary). Do not need him. Mainstream: loans and calques are expected and they weaken 'no contact with prior scripture.'",
            sources=[
                S("Jeffery — Foreign Vocabulary", "https://archive.org/details/foreignvocabular0000jeff"),
            ],
        ),
        live={
            "if_they_say": "The Qur'an has foreign words so it's not a miracle.",
            "you_say": "English is full of loans and can still be great. The live issue is whether loans show a scriptural milieu (they do) and whether Jurjānī-style i'jaz required a loan-free lexicon (it didn't).",
            "dont_overclaim": "Don't use Luxenberg as if he were consensus. Don't claim a chemically pure Arabic.",
        },
        crux="Do loans threaten i'jaz (if i'jaz was lexical purity) or only the isolation story (if i'jaz was naẓm)?",
        debate_use="Separate Jeffery (mainstream lists) from Luxenberg (outlier). Argue milieu, not 'gotcha Persian.'",
    ),
    card(
        "grammar-anomalies",
        18,
        "Linguistic",
        "Grammatical anomalies: error, dialect, or eloquence?",
        typ="syntax",
        popularity="High",
        why="Christian polemic still lists 5:69, 20:63, 4:162, 2:177. Muslim grammarians already fought over them. Either side that pretends the list is new is bluffing.",
        claimant=side(
            "Apparent agreement 'errors' are dialect, ḥaml ʿalā l-maʿnā (agreement with sense), or rhetorical. The seven/ten readings and early grammarians knew the files. Not a modern discovery of incompetence.",
            "Exhibits: hādhāni vs hādhayn (20:63), al-ṣābiʾūn in a seemingly accusative list (5:69). Answers: other qirāʾāt; Hijazi usage; 'eloquent ungrammaticality' as shibboleth of i'jaz.",
            sources=[
                qv("20/63"),
                qv("5/69"),
                qv("4/162"),
            ],
        ),
        critic=side(
            "Some anomalies look like the kind of thing oral recitation and later rasm freeze into sacredness, then grammarians theologize. 'It's eloquent because it's in the Qur'an' is circular.",
            "If a student wrote 20:63 in a grammar exam, many teachers would mark it. Calling every mark-down 'balāgha' is the unfalsifiable move again. "
            "Variant qirāʾāt that 'fix' the grammar cut against a single frozen miracle-wording.",
            sources=[
                qv("20/63"),
                S("Critical discussions of Qur'anic Arabic vs later fuṣḥā norms (field overview)", "https://plato.stanford.edu/entries/arabic-islamic-language/"),
            ],
        ),
        live={
            "if_they_say": "The Qur'an has grammar mistakes.",
            "you_say": "Show the āyah, the expected case-ending, the qirāʾa, and a parallel in early Arabic. Then: is it dialect, sense-agreement, or a frozen oral wrinkle? 'Mistake' assumes later school grammar as the judge of 7th-century speech.",
            "dont_overclaim": "Don't say there are zero hard files. Don't say hard files = illiterate author.",
        },
        crux="Is later Sībawayh-style grammar the right court for Qur'anic Arabic, or is the Qur'an itself a primary witness of an earlier/register-mixed Arabic?",
        debate_use="Do 20:63 on the board with two qirāʾāt. Circular 'it's correct because revealed' vs lazy 'gotcha error.'",
    ),
    card(
        "qiraat",
        19,
        "Linguistic",
        "Qirāʾāt: richness of meaning vs plurality of the wording",
        typ="textual plurality",
        popularity="High",
        why="Ahruf/qirāʾāt are a miracle of flexibility in dawah and a problem for 'every letter is a scientific constant' in i'jaz ʿilmī.",
        claimant=side(
            "Multiple canonical readings are an intended mercy (seven aḥruf). Meaning-branching is richness, not instability. All are revealed.",
            "Example: 18:86 ḥamiʾa / ḥāmiya; 30:2–5 timing nuances; maliki vs māliki in Q 1:4. I'jaz includes this elasticity.",
            sources=[
                qv("1/4", "maliki / māliki yawm al-dīn"),
                S("Historicity topic in this hub (manuscripts / readings)", "../historicity/"),
            ],
        ),
        critic=side(
            "If wording is multiple, verse-level scientific and numerical miracles that depend on one Cairo 1924 Hafs consonant-and-vowel choice are methodologically broken. Richness here is instability there.",
            "Some variants change law or theology, not just flavour. That is a textual-history file (see Historicity), not a literary-miracle slide.",
            sources=[
                S("EndDebates — Historicity", "../historicity/"),
            ],
        ),
        live={
            "if_they_say": "Every letter is a miracle / the text is one letter.",
            "you_say": "Ask which qirāʾa. If they never have, their i'jaz ʿilmī is Hafs-only. Literary i'jaz can survive variants; letter-counting cannot.",
            "dont_overclaim": "Don't pretend variants are only pronunciation. Don't pretend they make the Qur'an 'lost.'",
        },
        crux="Are canonical readings a designed semantic surplus, or a historical plurality that blocks letter-level miracle claims?",
        debate_use="Tie this to the numerical-19 card and to 18:86. One wording or several?",
    ),
    card(
        "hapax-roots",
        20,
        "Linguistic",
        "Unique roots, rare words, and 'only the Qur'an uses this'",
        typ="lexicon",
        popularity="Medium",
        why="Dawah lists of hapax as fingerprints; linguists see normal literary vocabulary.",
        claimant=side(
            "Rare words are placed with surgical fit. Statistical uniqueness of some roots is a sign.",
            "Popular lists (words appearing once) are taken as anti-formula evidence.",
            sources=[qv("113"), qv("114")],
        ),
        critic=side(
            "Hapax legomena are common in small corpora and in poetry. They are not a miracle-statistic without a baseline against the whole Jāhilī + early Arabic corpus.",
            "Some 'unique' words are hapax because the corpus is short, not because a deity coined them.",
            sources=[S("Jeffery — Foreign Vocabulary (rare/foreign overlap)", "https://archive.org/details/foreignvocabular0000jeff")],
        ),
        live={
            "if_they_say": "This word appears only once — miracle.",
            "you_say": "Hapax is normal. Ask for a baseline frequency model, not a wow-count.",
            "dont_overclaim": "Don't dump hapax as 'errors.' Don't dump hapax as fingerprints.",
        },
        crux="Relative to what corpus is a hapax surprising?",
        debate_use="Demand a denominator (size of Qur'an vs. size of early Arabic poetry).",
    ),
    # Historical
    card(
        "rum-prophecy",
        21,
        "Historical",
        "The Byzantine (Rūm) victory prophecy (30:2–4)",
        typ="prophecy + geography",
        popularity="Very high",
        why="The most-cited historical/predictive miracle. Also the 'lowest land of the Dead Sea' scientific overlay.",
        claimant=side(
            "Q 30:2–4 predicted a Byzantine rebound against the Sasanians 'in a few years' (biḍʿi sinīn, 3–9) after a defeat. Heraclius's 620s recovery fulfilled it. Adnā l-arḍ as 'lowest land' matches the Dead Sea basin, unknown as a geodetic fact.",
            "Traditional: news of a Persian win reached Mecca; the verse consoled Muslims and was vindicated. "
            "Modern overlay: the battlefield was near the Dead Sea, the lowest exposed land on earth — a scientific bonus.",
            quotes=[
                Q(
                    "The Romans have been defeated in the nearest/lowest land, but they, after their defeat, will be victorious within a few years.",
                    "Qur'an 30:2–4 (sense)",
                    "Rūm pericope",
                    "https://quran.com/30/2-4",
                ),
            ],
            sources=[qv("30/2-4")],
        ),
        critic=side(
            "A mid-war 'they will bounce back in a few years' is a risky but human political hope, especially if dated after the tide had hints of turning. Adnā classically means 'nearest' (the Levant relative to Arabia), not 'lowest elevation.' The Dead Sea reading is concordism.",
            "Variant reading issues and the flexibility of biḍʿ (up to nine years) widen the target. "
            "If the sūrah is dated after Heraclius's successes, it is vaticinium ex eventu. Dating is the whole fight. "
            "Sasanian-Byzantine war news travelled; this is not knowledge of an isolated desert with no caravans.",
            data_points=[
                D("Adnā l-arḍ: 'nearest land' is the ordinary lexical sense; 'lowest land' is a modern scientific reading.", "Classical lexica / tafsīr vs modern i'jaz slides"),
                D("Heraclius's counter-offensives culminate in the late 620s; bidʿ covers a comfortable window.", "Byzantine-Sasanian war of 602–628"),
            ],
            sources=[
                qv("30/2-4"),
            ],
        ),
        live={
            "if_they_say": "The Qur'an predicted Rome's victory and the Dead Sea's elevation.",
            "you_say": "Split the card. (1) Prophecy: date the sūrah or you have nothing. (2) Lowest land: show a classical tafsīr that says elevation, not 'nearest.' Without that, it's Bucaille on a war headline.",
            "dont_overclaim": "Don't call it a coin-flip with no risk. Don't call Dead Sea geodesy a 7th-century tafsīr.",
        },
        crux="Is 30:2–4 a dated prediction before the rebound, a hope during a known war, or a retrospective — and does adnā mean nearest or lowest?",
        debate_use="Ban the Dead Sea slide until adnā is argued from pre-modern usage. Fight the prophecy on dating.",
    ),
    card(
        "pharaoh-body",
        22,
        "Historical",
        "Pharaoh's body as a sign (10:92)",
        typ="history + archaeology",
        popularity="Very high",
        why="Mass dawah: Ramesses II's mummy is the drowned king. Egyptology does not play along for free.",
        claimant=side(
            "Q 10:92: God will save Pharaoh's body as a sign. The mummies of New Kingdom kings, identified in modern times, fulfill a 7th-century claim no Arab could check.",
            "Bucaille popularized a medical reading of Ramesses II / Merneptah. The verse is taken as specific corpse-preservation, not merely 'you'll be a lesson in stories.'",
            sources=[qv("10/92")],
        ),
        critic=side(
            "Which Pharaoh? The Qur'an does not name him. Many drowned-king traditions exist. Egyptian royal mummification was the elite default, not a shock. A preserved royal corpse is what Egypt does.",
            "Ramesses II probably died old, not drowned in the Delta. Identification is a slideshow, not a consensus excavation of Exodus. "
            "10:92 can mean the body will be rescued from the sea as a warning to the living, in-story, not 'on display in Cairo in 1902.'",
            sources=[qv("10/92")],
        ),
        live={
            "if_they_say": "Ramesses II's mummy proves 10:92.",
            "you_say": "Name the king the verse names (it doesn't). Then: mummification is Egyptian routine. Then: did that king drown? If any mummy counts, the prophecy is unfalsifiable.",
            "dont_overclaim": "Don't deny 10:92 says the body is a sign. Don't baptize a tourist mummy as Exodus.",
        },
        crux="Is 10:92 an in-narrative warning about that drowned king, or a prediction of a modern museum identification?",
        debate_use="Force a named Pharaoh. If they won't name one, the miracle is a blank cheque.",
    ),
    card(
        "haman",
        23,
        "Historical",
        "Hāmān at Pharaoh's court (and the tower)",
        typ="history + names",
        popularity="High",
        why="Anachronism file vs Egyptological-name file. Bucaille and Islamic Awareness vs biblical Esther chronology.",
        claimant=side(
            "Hāmān is an Egyptian high official under Pharaoh, tasked with baking bricks and building high (28:38, 40:36–37). That is not the Persian Haman of Esther. Hieroglyphic names in the ḥ-m-n range and a 'overseer of stone-workers' inscription are offered as hits.",
            "Islamic Awareness: literary-transition from Esther is not forced; the Qur'an also uses 'king' for Joseph's era and 'Pharaoh' for Moses, which some claim matches Egyptological title history better than the Bible.",
            sources=[
                qv("28/38"),
                qv("40/36-37"),
                S("Islamic Awareness — Haman file", "https://www.islamic-awareness.org/quran/contrad/external/haman.html"),
            ],
        ),
        critic=side(
            "Haman + Pharaoh + a baked-brick tower to heaven looks like Esther's Haman + Exodus' Pharaoh + Genesis 11's Babel, compressed. The Vienna inscription used in dawah does not give a vizier named Haman matching the Qur'anic role; Egyptologists have disputed the readings.",
            "Esther's Haman is a millennium later in Persia. If the Qur'an meant a different person, the name-coincidence with the most famous Jewish-enemy Haman is a huge own-goal or a literary merge. "
            "Bucaille's hieroglyph move is a long controversy (Katz / Answering-Islam vs IA); do not cite either blog as Egyptology. Ask for a signed reading from a mainstream Egyptologist of that object.",
            sources=[
                S("Islamic Awareness — Haman (the best Muslim packet)", "https://www.islamic-awareness.org/quran/contrad/external/haman.html"),
                qv("28/6"),
            ],
        ),
        live={
            "if_they_say": "Haman in Egypt is a Quranic blunder / a hieroglyphic miracle.",
            "you_say": "Two live options: literary merge of known villains, or a distinct Egyptian Hāmān. The inscription argument is only as good as a current Egyptologist's reading of that specific object — not a 1990s slide.",
            "dont_overclaim": "Don't treat Esther as modern historiography. Don't treat a blog as the Cairo Museum.",
        },
        crux="Is Qur'anic Hāmān the Esther villain misplaced, a literary type-name, or a recoverable Egyptian official?",
        debate_use="Insist on the primary inscription photo + a living Egyptologist, or drop the 'hieroglyph miracle.' Then argue the Babel-brick motif separately.",
    ),
    card(
        "mary-aaron",
        24,
        "Historical",
        "Mary, sister of Aaron, daughter of ʿImrān",
        typ="names / typology",
        popularity="Very high",
        why="The most-used 'Qur'an mixed Mary with Miriam' Christian critique. Muslim answers: honorific, typology, or different genealogy.",
        claimant=side(
            "Umm ʿImrān / ukht Hārūn is an honorific: Mary is in the priestly house, likened to Miriam. The Qur'an knows the difference between Moses' era and Jesus' era (different sūrahs, different casts). A 7th-century Arab mixing them would also mix Pharaoh into the nativity; he doesn't.",
            "Q 19:28: 'sister of Aaron' as clan language (as 'brother of X' in Arabic). 3:35–45 is a distinct Maryam narrative.",
            sources=[qv("19/28"), qv("3/35-45")],
        ),
        critic=side(
            "The simplest reading is a conflation of Maryam (Mary) with Miriam bint Amram/Imran, sister of Moses and Aaron — a known Christian polemic already in the 8th century (John of Damascus). Honorific 'sister' is possible but convenient.",
            "If the Qur'an wanted 'of Aaron's line,' it could say so more clearly. The name ʿImrān = Amram is the tell. "
            "Typology (Mary as new Miriam) is a sophisticated literary reading — grant it as literature, then it is not a historical genealogy miracle.",
            sources=[qv("19/28"), qv("66/12")],
        ),
        live={
            "if_they_say": "Muhammad thought Mary was Moses' sister.",
            "you_say": "Read 19:28 next to the Jesus infancy material in 19 and 3. Then: honorific/clan vs. conflation. Both have been live since the first Christian-Muslim polemic. Neither is a new Reddit find.",
            "dont_overclaim": "Don't pretend 19:28 is easy. Don't pretend the Qur'an has no timeline elsewhere.",
        },
        crux="Is ukht Hārūn clan/typology language, or a collapsed Mary-Miriam identification?",
        debate_use="Ask what would count as a disconfirmation of the honorific reading. If nothing, it is unfalsifiable.",
    ),
    card(
        "samiri",
        25,
        "Historical",
        "Al-Sāmirī at the golden calf",
        typ="history + names",
        popularity="Medium",
        why="Samaritans as a people are post-Moses in standard history. The Qur'anic calf-maker's title looks anachronistic — or like a different etymology.",
        claimant=side(
            "Al-Sāmirī is a personal/epithet not meaning 'the Samaritan ethnically.' Roots and tafsīr give a name or a place-epithet that need not be the later Samaritans of Nablus.",
            "The Qur'an also diverges from Exodus by blaming a figure other than (or alongside) Aaron — a theological retell, not a timeline textbook.",
            sources=[qv("20/85-97")],
        ),
        critic=side(
            "In Arabic al-Sāmirī is naturally 'the Samaritan.' Samaritans as a distinct group are associated with post-exilic / Iron Age developments, not the Sinai wandering. That is a standard anachronism claim.",
            "It may be midrashic: a later villain-type projected back. Literary, not historical precision.",
            sources=[qv("20/85")],
        ),
        live={
            "if_they_say": "Samaritans didn't exist in Moses' time.",
            "you_say": "If the word is an ethnonym, that's a real problem for historical literalism. If it's a name, show that from Arabic usage, not from the need to win. Don't skip Aaron's different role in Q 20 either — that's the theological rewrite.",
            "dont_overclaim": "Don't collapse all of Q 20 into a name-gotcha.",
        },
        crux="Is al-Sāmirī an ethnonym (anachronism) or a personal name/epithet (no ethnic claim)?",
        debate_use="Lexicon first, Wikipedia chronology second.",
    ),
    card(
        "infancy-gospel",
        26,
        "Historical",
        "Jesus's infancy: speaking cradle, clay birds, Table",
        typ="intertext + history",
        popularity="High",
        why="Literary miracle of 'unknown Christian truth' vs dependence on Infancy Gospel of Thomas, Syriac tradition, and the Last Supper inverted as māʾida.",
        claimant=side(
            "Details absent from the canonical four Gospels but present in the Qur'an (3:49, 5:110, 19:29–33, 5:112–115) restore true Jesus against church editing — or reveal what God authenticates independently.",
            "Speaking infant and clay birds are then not 'apocrypha copied' but 'apocrypha that happened to keep a true memory' or parallel revelation.",
            sources=[qv("3/49"), qv("19/29"), qv("5/110"), qv("5/112-115")],
        ),
        critic=side(
            "These are famous extra-canonical Christian tales circulating in the East. A 7th-century reciter does not need a lost authentic Gospel; he needs the milieu Reynolds maps. Independent confirmation would require a reason to think the Infancy Gospel is historically true, which almost no historian grants.",
            "The māʾida can be read as a riff on Eucharist / agape, not as unknown history. "
            "If apocrypha are 'corrupted,' using them as miracle-history is inconsistent.",
            sources=[
                S("Reynolds — The Qur'an and the Bible", "https://yalebooks.yale.edu/book/9780300181320/the-quran-and-the-bible/"),
                qv("5/110"),
            ],
        ),
        live={
            "if_they_say": "The Qur'an knew Jesus stories the Church hid.",
            "you_say": "Those stories were not hidden in the East; they were popular. Hidden-from-Nicene-canon ≠ hidden-from-Syriac-Christians. Ask whether infancy miracles are history or homily.",
            "dont_overclaim": "Don't say no Christian ever told clay-bird stories. Don't say canonical-only Jesus is the only Christian Jesus the Ḥijāz could meet.",
        },
        crux="Are infancy miracles recovered history, shared lore, or theology in narrative form?",
        debate_use="Put Infancy Gospel of Thomas next to 3:49. Argue dependence vs common tradition vs revelation.",
    ),
    card(
        "ad-thamud",
        27,
        "Historical",
        "ʿĀd, Thamūd, and archaeology",
        typ="archaeology",
        popularity="Medium",
        why="Rock-cut tombs at al-Ḥijr / Madāʾin Ṣāliḥ vs 'lost peoples only the Qur'an knew.'",
        claimant=side(
            "Thamūd are archaeologically real (Lihyanite/Nabataean Madāʾin Ṣāliḥ; earlier Thamudic references). ʿĀd and Iram (89:6–8) have been tied to Arabian sites. The Qur'an preserves memory of destroyed Arabian peoples the Bible barely has.",
            "Q 15:80–84; 89:6–9. The 'virgin historical content' is Arabian, which fits a Ḥijāzī revelation.",
            sources=[qv("89/6-9"), qv("15/80-84")],
        ),
        critic=side(
            "Thamūd as a name in Arabian inscriptions and later Nabataean tombs at al-Ḥijr does not automatically confirm the Qur'anic prophet Ṣāliḥ or the she-camel miracle. Archaeology of a people ≠ archaeology of a miracle.",
            "Iram of the pillars has been a magnet for over-identification (Ubar, etc.). "
            "Local destroyed-people stories are what Arabian memory would already have.",
            sources=[qv("7/73-79")],
        ),
        live={
            "if_they_say": "UNESCO sites prove Ṣāliḥ.",
            "you_say": "Sites prove a people and a landscape of rock dwellings. They do not prove the she-camel. Don't confuse toponyms with tafsīr.",
            "dont_overclaim": "Don't say Thamūd are fictional. Don't say Madāʾin Ṣāliḥ is a video of Q 7.",
        },
        crux="Does archaeological Thamūd confirm the Qur'anic narrative, or only that the Qur'an uses real Arabian names?",
        debate_use="Split people / place / miracle. Only the last is i'jaz if it happened.",
    ),
    card(
        "moon-split",
        28,
        "Historical",
        "The splitting of the moon (54:1–2)",
        typ="miracle report",
        popularity="High",
        why="Not a literary device claim — a physical-sign claim in the same i'jaz culture. Historians ask why the world did not notice.",
        claimant=side(
            "Q 54:1 reports a past sign (inshaqqa) that the pagans dismissed as magic. Hadith multiply eyewitnesses. Some moderns add NASA 'split moon' folklore (weak even among Muslims).",
            "Classical: a muʿjiza for Quraysh, not a verse-structure miracle. Still filed under 'signs.'",
            sources=[qv("54/1-2")],
        ),
        critic=side(
            "A globally visible astronomical rupture should leave independent records. It doesn't in any convincing way. Literary-eschatological reading: the Hour's portents, not a Meccan tourist event. NASA-split memes are junk.",
            "If it is eschatology, it is not a 7th-century public miracle. If it is history, the silence of the sky-watching world is the problem.",
            sources=[qv("54/1")],
        ),
        live={
            "if_they_say": "NASA proved the moon split.",
            "you_say": "That meme is false. Stay in 54:1: past miracle vs Hour-sign. Don't launder hadith through a space agency.",
            "dont_overclaim": "Don't mock people for believing muʿjizāt if they don't claim NASA. Don't claim NASA.",
        },
        crux="Is 54:1 a past public astronomical event, an eschatological image, or a local sign whose global silence is unsurprising?",
        debate_use="Kill the NASA slide in ten seconds, then have the real genre fight.",
    ),
    card(
        "kaaba-abraham",
        29,
        "Historical",
        "Abraham, Ishmael, and the Kaʿba",
        typ="sacred history",
        popularity="High",
        why="A historical-miracle if true (patriarchs in Mecca). A literary-theological claim if it is 7th-century identity-making.",
        claimant=side(
            "Q 2:124–129, 22:26–29: Abraham and Ishmael found/purify the House. This restores Ishmaelite Abrahamic history the Bible marginalized.",
            "The rite-origin is then revelation, not later myth.",
            sources=[qv("2/124-129"), qv("22/26-29")],
        ),
        critic=side(
            "There is no extra-Qur'anic 2nd-millennium evidence of Abraham in Mecca. Critical historians read this as Islam's Abrahamic re-rooting of an Arabian sanctuary — theologically powerful, archaeologically unsecured.",
            "Biblical Abraham is Levantine/Mesopotamian in the received narrative. The 'Bible hid Mecca' claim is not how ancient Near Eastern evidence works.",
            sources=[qv("2/127")],
        ),
        live={
            "if_they_say": "Abraham built the Kaʿba — that's history.",
            "you_say": "It's Qur'anic sacred history. Ask what extra-Qur'anic control would confirm or falsify it. If none, it is creed, not a historical miracle.",
            "dont_overclaim": "Don't sneer at a sanctuary's origin-story as if other religions had CCTV of Abraham. Don't call it a documented dig.",
        },
        crux="Is Abraham-in-Mecca a recoverable historical event or a theological genealogy of the sanctuary?",
        debate_use="Demand the control evidence. Sacred history can be believed without being i'jaz ʿilmī.",
    ),
    # Scientific
    card(
        "embryology",
        30,
        "Scientific",
        "Embryology (23:12–14, 22:5): leech, chewed flesh, bones then meat",
        typ="science + ancient medicine",
        popularity="Very high",
        why="The flagship scientific miracle. Also the flagship Galen-parallel file. Score method, then Arabic, then biology.",
        claimant=side(
            "Nuṭfa → ʿalaqa (leech-like clinging clot) → muḍgha (chewed lump / somites) → bones then clothed with flesh. Moore: appearance matches early embryos visible only with later science. 'Three veils of darkness' (39:6) = abdominal wall, uterus, membranes.",
            "Bucaille and Moore (Islamic edition of The Developing Human) gave the claim institutional sheen. Mixed drop (nuṭfa amshāj, 76:2) is read as zygote/genetic mix.",
            quotes=[
                Q(
                    "Then We made the drop into a clinging/leech-like form, then We made the clinging form into a chewed lump, then We made the lump bones, then We clothed the bones with flesh…",
                    "Qur'an 23:14 (sense)",
                    "Embryology pericope",
                    "https://quran.com/23/14",
                ),
                Q(
                    "At first I was astonished by the accuracy of the statements that were recorded in the 7th century AD, before the science of embryology was established.",
                    "Keith L. Moore",
                    "Foreword / Islamic-edition context (widely quoted; see al-bab history)",
                    "https://al-bab.com/science-and-quran",
                ),
            ],
            sources=[
                qv("23/12-14"),
                qv("22/5"),
                qv("39/6"),
                S("Moore 1986 JIMA article", "https://doi.org/10.5915/18-1-8693"),
            ],
        ),
        critic=side(
            "The sequence tracks Galen's De Semine / Hippocratic embryology: semen → blood-like → flesh → bones/outline → formed infant. Bones-then-flesh as a biological order is wrong (cartilage/bone and muscle overlap). ʿAlaqa in classical tafsīr is a blood clot, not a microscope-leech. Moore's involvement was dawah-commissioned; it is not independent embryology consensus.",
            "Greek medicine was in the late-antique air (even if full Arabic Galen comes later, the four-stage picture is old). "
            "If you read 23:14 as poetry of creation, it need not be a textbook; if you insist it is a textbook, it is a 2nd-century one. "
            "You cannot praise 'chewed somites' as only-God-could-know and also deny that a blood-clot reading was the historical meaning.",
            data_points=[
                D("Galen, De Semine: four periods from semen to formed child — the comparison is the critical backbone.", "Galen, On Semen"),
                D("Classical tafsīr: ʿalaqa as congealed blood is default; 'leech' is a modern visual overlay.", "Tafsīr tradition on 23:14"),
            ],
            sources=[
                qv("23/12-14"),
                S("History of Bucaille/Moore embryology slides", "https://al-bab.com/science-and-quran"),
            ],
        ),
        counters=[
            {
                "against": "Leech photograph",
                "claim": "The 23-day embryo looks like a leech, so ʿalaqa is a miracle.",
                "reply": "Appearance-to-a-modern-photo is not 7th-century semantics. Clot/leech/cling are all in the root. Show which one Ṭabarī had. Photos are not lexica.",
            },
            {
                "against": "Skeptical over-precision",
                "claim": "The Qur'an teaches semen is stored in the uterus as a clot, period, Islam is false.",
                "reply": "If the genre is signs-of-creation speech, not Galen 2.0, 'false textbook' may be the wrong court. But then withdraw the Moore slides. You don't get textbook-when-winning and poetry-when-losing.",
            },
        ],
        live={
            "if_they_say": "The Qur'an taught embryology 1000 years early.",
            "you_say": "Read 23:12–14, then Galen's stages, then Moore's leech photo, then classical 'clot.' Hits require the modern gloss; the ancient parallel is uncomfortably close. Pick: poetry of creation, or biology textbook.",
            "dont_overclaim": "Don't deny Moore said impressed things. Don't treat Moore as the field. Don't skip Galen.",
        },
        crux="Is 23:12–14 independent, accurate embryology — or late-antique generation-talk that modern slides re-gloss?",
        debate_use="Method card first: no photos as lexica. Then Galen table vs Qur'an table. Then genre.",
    ),
    card(
        "sulb-taraib",
        31,
        "Scientific",
        "Semen from backbone and ribs (86:5–7)",
        typ="science + anatomy",
        popularity="High",
        why="A miss that concordism has to metaphorize. Objectivity requires putting it next to embryology, not in a footnote.",
        claimant=side(
            "Ṣulb and tarāʾib refer to the pelvic/reproductive region, gonads' embryonic origin near the spine, or 'from between the loins and the breastbone' as idiom for the sexual body. Not a urology textbook error.",
            "Some moderns: testes develop in the abdominal region near the spine. Others: poetic merism for the whole torso.",
            sources=[qv("86/5-7")],
        ),
        critic=side(
            "Classical tafsīr commonly: fluid issued from the man's backbone and the woman's chest/ribs. That matches ancient generation theories, not modern urology. Embryonic gonad migration is a post-hoc stretch the words do not specify.",
            "If embryology 23:14 is literal-scientific, 86:6–7 gets the same court — and loses. If 86 is idiom, 23 may be idiom too.",
            sources=[qv("86/6-7")],
        ),
        live={
            "if_they_say": "The Qur'an says sperm comes from the spine.",
            "you_say": "That's a fair reading of many tafsīrs of 86:6–7. The rescue is idiom or embryology-of-gonads. You don't get to keep 23:14 as NASA-grade and 86 as poetry without a rule you apply to both.",
            "dont_overclaim": "Don't pretend 86 is a popular dawah slide. It isn't — that's the tell.",
        },
        crux="One rule for 23:14 and 86:6–7: both scientific, or both literary signs?",
        debate_use="This is the symmetry enforcer for the embryology card.",
    ),
    card(
        "expanding-universe",
        32,
        "Scientific",
        "Expanding universe (51:47) and 'heavens and earth were joined' (21:30)",
        typ="science + lexicon",
        popularity="Very high",
        why="Big Bang / Hubble as i'jaz. Lexical fight: mūsiʿūn, ratq/fatq.",
        claimant=side(
            "51:47 innā la-mūsiʿūn = 'we are expanding it.' 21:30: heavens and earth were sewn, then split — Big Bang plus nebular separation.",
            "Modern translations often render 51:47 as expansion. 21:30 is paired with 'every living thing from water' as a science cluster.",
            sources=[qv("51/47"), qv("21/30")],
        ),
        critic=side(
            "Mūsiʿūn classically: 'we are ample / able / made it vast' — a statement of power, not Hubble's law. Ratq/fatq in 21:30 sits next to rain and plants; many tafsīrs: sky and earth were closed, then rain/vegetation opened. That is a water-cycle creation image, not FLRW cosmology.",
            "Genesis 1 also has heaven-and-earth beginning and waters. Concordism is cheap across canons. "
            "If 51:47 is expansion, the Qur'an's seven-layered, lamp-in-the-lowest-heaven cosmos (67:3, 71:15, 67:5) still has to be faced with the same literalism.",
            sources=[qv("51/47"), qv("21/30"), qv("67/3")],
        ),
        live={
            "if_they_say": "The Qur'an taught the expanding universe.",
            "you_say": "Parse mūsiʿūn from Lane/tafsīr, not from a 2005 pamphlet. Then read 21:30 with 21:31 (mountains, water). Context looks like inhabitable-earth creation, not a physics paper.",
            "dont_overclaim": "Don't say the Arabic cannot bear 'expander.' Don't say it must mean Hubble.",
        },
        crux="Do 51:47 and 21:30, in pre-modern usage and context, assert cosmic expansion and a primordial singularity — or creation-power and a rain/earth opening?",
        debate_use="No Hubble slide until a classical lexicon is opened. Then apply the same literalism to seven heavens.",
    ),
    card(
        "iron-mountains-seas",
        33,
        "Scientific",
        "Iron 'sent down,' mountains as pegs, two seas that don't mix",
        typ="science cluster",
        popularity="Very high",
        why="Three of the most-shared slides. They travel together and fall together under the same method rule.",
        claimant=side(
            "57:25: iron was 'sent down' — meteoritic/extra-terrestrial origin. 78:6–7, 16:15: mountains as pegs / isostasy, stabilizing the crust. 55:19–20, 25:53: a barrier (barzakh) between seas — halocline / estuary physics.",
            "Each is taken as knowledge a desert man would not have.",
            sources=[qv("57/25"), qv("78/6-7"), qv("16/15"), qv("55/19-20"), qv("25/53")],
        ),
        critic=side(
            "Anzala 'send down' is used for cattle, garments, and the Qur'an (39:6, 7:26) — it is revelation-idiom, not a meteorite paper. Mountains as tent-pegs is a desert image; mountains also sit at faults and do not magically 'stop earthquakes' as slides claim. Seas: anyone at an estuary sees a visible line; mixing still occurs; the verses also read as blessing/poetry (al-Raḥmān), not fluid dynamics.",
            "Isostasy is a 19th-century theory and does not mean 'pegs prevent shaking' in the slide sense. "
            "25:53's 'forbidding barrier' between sweet and salt is a known shoreline observation.",
            data_points=[
                D("Q 7:26: God 'sent down' clothing — same verb family as 57:25's iron.", "https://quran.com/7/26"),
                D("Estuary fronts are visible to sailors; they are not unmixed at the molecular level.", "Physical oceanography vs 55:19–20 slides"),
            ],
            sources=[
                qv("57/25"),
                qv("7/26", "garments 'sent down'"),
                qv("55/19-20"),
            ],
        ),
        live={
            "if_they_say": "Iron from space, mountains pegs, seas that don't mix.",
            "you_say": "Three method tests: (1) anzala elsewhere, (2) what tafsīr said mountains do, (3) whether a sailor needed NASA to see a silt line. Cluster them so they can't retreat one-by-one into metaphor.",
            "dont_overclaim": "Don't say the verses are stupid. Don't say they are JGR-Space Physics.",
        },
        crux="Are these verses phenomenological/idiomatic praise of creation, or encoded modern geophysics?",
        debate_use="Force the verb anzala to be consistent across iron, clothes, and livestock.",
    ),
    card(
        "cosmology-sun-earth",
        34,
        "Scientific",
        "Sun's course, resting-place, orbits, and the shape of the earth",
        typ="cosmology",
        popularity="Very high",
        why="36:38, 18:86, 21:33, 36:40, 79:30, 88:20 — the cosmic file as a set, not a cherry.",
        claimant=side(
            "21:33 / 36:40: sun and moon swim in orbits — heliophysics/orbiting. 79:30 daḥāhā: egg-shaped / ostrich-egg earth (geoid). 'Spread out' verses are from a human vantage, like the Bible's. 36:38's mustaqarr is a term of a stable solar system, or a qirāʾa 'no resting place.'",
            "Phenomenological language is allowed for sunrise vocabulary in every scripture. The distinctive claims are orbit and geoid.",
            sources=[qv("21/33"), qv("36/38"), qv("36/40"), qv("79/30"), qv("88/20")],
        ),
        critic=side(
            "A sun that runs to a resting-place (36:38) and a lamp placed in the lowest heaven (71:16, 67:5) plus seven stacked heavens is a late-antique layered cosmos, not Copernicus. Daḥā is 'spread/stretched' in classical usage; 'ostrich egg' is a modern pun on a related noun. Flat-appearing earth (laid out, pegged with mountains) is the plain image.",
            "Qirāʾa la mustaqarra lahu is sometimes used to escape 36:38. That is a variant, not a Hubble photo. "
            "Orbits (falak) can be the old celestial-sphere paths of sun and moon around a central earth — which is exactly what ancient astronomy said.",
            sources=[
                qv("36/38"),
                qv("71/15-16"),
                qv("67/5"),
                qv("79/30"),
                S("Abu Dharr sun hadith", "https://sunnah.com/bukhari:3199"),
            ],
        ),
        live={
            "if_they_say": "The Qur'an said the earth is egg-shaped and the sun orbits.",
            "you_say": "Daḥāhā = spread, unless you smuggle duḥya. Falak = celestial course, which Ptolemy also had. Then 67:5 stars as missiles against devils — include the ugly verses in the same cosmology, or admit the genre is not astrophysics.",
            "dont_overclaim": "Don't say the Qur'an teaches a disc as a scientific assertion if you won't let the other side use 88:20. Don't say geoid is in the root.",
        },
        crux="Is Qur'anic cosmology a 7th-century layered sky with a spread-out earth, or a coded modern orrery — and can one rule read 21:33 and 67:5 together?",
        debate_use="Bundle 18:86, 36:38, 67:5, 79:30. No orphan 'orbit' verse.",
    ),
    card(
        "anatomy-modern-bundle",
        35,
        "Scientific",
        "Forehead of the liar, fingerprints, skin pain, milk, bee, ant",
        typ="science cluster",
        popularity="High",
        why="The leftover slide-deck: 96:15–16, 75:4, 4:56, 16:66, 16:68–69, 27:18. Individually thin; together they show the method.",
        claimant=side(
            "96:15–16: nāṣiya (forelock) of a lying sinner — prefrontal cortex. 75:4: fingertips restored — dermatoglyphics. 4:56: skins replaced to renew pain — nociceptors in skin. 16:66: milk from between dung and blood. 16:68 feminine bee. 27:18 ants communicate.",
            "Each is a 'how could he know.'",
            sources=[qv("96/15-16"), qv("75/4"), qv("4/56"), qv("16/66"), qv("16/68-69"), qv("27/18")],
        ),
        critic=side(
            "Grabbing a forelock is a known humiliation idiom (also biblical). Fingertips in 75:4 are about resurrection-power ('even his fingertips'), not forensic science. Pain in skin is ordinary observation (burns). Milk: livestock farmers see udders near guts; the verse is a blessing, and the physiology is not a textbook of mammary glands. Feminine bee: Arabic naḥl can be morphologically treated in ways grammarians discuss; worker-bee sex is not a 7th-century microanatomy claim. Ant speech is fable-genre (Solomon) like talking hoopoe — if ants are science, the hoopoe is too.",
            "This bundle is where i'jaz ʿilmī becomes parody-prone. That does not refute literary i'jaz. It refutes slide culture.",
            sources=[qv("75/4"), qv("27/18-28")],
        ),
        live={
            "if_they_say": "The Qur'an knew the prefrontal cortex.",
            "you_say": "Nāṣiya is the forelock. Humiliation-by-forelock is an idiom. If 27:18 is entomology, the talking bird in the next passage is ornithology. Genre.",
            "dont_overclaim": "Don't mock 16:66 as stupid; farmers are not fools. Don't call it histology.",
        },
        crux="Are these verses idioms, blessings, and Solomon-narrative, or encoded modern biology?",
        debate_use="Offer to concede the whole bundle as non-scientific if they concede 27:18 is not a myrmecology paper. Then return to literary i'jaz.",
    ),
    card(
        "time-relativity",
        36,
        "Scientific",
        "A day is a thousand / fifty thousand years (time dilation)",
        typ="science + eschatology",
        popularity="Medium",
        why="Relativity slides. The verses are about God's day vs human day in judgment contexts.",
        claimant=side(
            "22:47, 32:5 (thousand years), 70:4 (fifty thousand) encode time dilation / multiple time-rates.",
            "Different 'days' for different cosmic processes.",
            sources=[qv("22/47"), qv("32/5"), qv("70/4")],
        ),
        critic=side(
            "Biblical and extra-biblical 'a thousand years as a day' (Psalm 90:4, 2 Peter 3:8) already exist. 70:4's 50,000 is an eschatological shock-number, not Lorentz transformation. Inconsistent multipliers (1k vs 50k) are a problem for a physics reading and normal for rhetoric.",
            "If 22:47 is relativity, the Bible has the same physics. Comparative concordism is not a Qur'anic exclusive.",
            sources=[qv("70/4")],
        ),
        live={
            "if_they_say": "The Qur'an taught relativity.",
            "you_say": "Psalm 90:4 did too, then. This is theologic time, not GPS satellites. Inconsistent ratios kill the physics reading.",
            "dont_overclaim": "Don't deny the verses stress divine/human time disparity.",
        },
        crux="Are variable 'days' eschatological rhetoric (shared with the Bible) or physics?",
        debate_use="Read Psalm 90:4 next to 22:47. Comparative concordism.",
    ),
    card(
        "numerical-19",
        37,
        "Scientific",
        "Number 19, word-counts, and letter miracles",
        typ="numerology",
        popularity="Medium",
        why="Rashad Khalifa's 19; popular dawah word-counts (dunyā vs ākhira, land vs sea percentages). A different species of i'jaz, usually weaker.",
        claimant=side(
            "Q 74:30 'over it is nineteen' is a key. Counts of words, letters, and Bismillah-related structures show a mathematical seal no human editor could hold across 23 years.",
            "Land/sea word-count ≈ earth's water cover; equal counts of paired terms.",
            sources=[qv("74/30")],
        ),
        critic=side(
            "Khalifa declared himself a messenger, stripped two verses, and was rejected by mainstream Islam — the 19-system is a sectarian machine. Counts depend on which qirāʾa, whether to count Bismillah, hamza, and headings. Paired-word equalities have been repeatedly shown to need fudges. Percentage-of-earth slides fail on Arabic polysemy (baḥr ≠ 'ocean cover').",
            "Numerology is the cheapest concordism: large texts always contain patterns if you search with enough knobs.",
            sources=[qv("74/30")],
        ),
        live={
            "if_they_say": "The number 19 proves the Qur'an.",
            "you_say": "That's Khalifa. Mainstream Muslims already dumped the prophet-claim. Word-counts need a published, qirāʾa-specified method you could fail. If the knobs always find a pattern, it isn't a seal.",
            "dont_overclaim": "Don't smear all literary i'jaz with 19. Don't treat 74:30 as a hash function.",
        },
        crux="Is there a pre-specified, fail-able counting protocol — or an adjustable hunt?",
        debate_use="Ask for the protocol in writing before any number. Mention qirāʾāt.",
    ),
    card(
        "seven-heavens-missiles",
        38,
        "Scientific",
        "Seven heavens, lamps, and stars as missiles against devils",
        typ="cosmology",
        popularity="High",
        why="The verses scientific i'jaz must metaphorize. Objectivity: they belong in the same cosmology as 'orbits.'",
        claimant=side(
            "Seven heavens are seven cosmic layers / atmospheres / scales of creation, not a stack of solid domes. Stars as 'missiles' (67:5, 72:8–9) are meteors, a real phenomenon, described from earth.",
            "Ancient audiences needed image-language. The phenomenon (shooting stars) is true.",
            sources=[qv("67/3-5"), qv("71/15"), qv("72/8-9")],
        ),
        critic=side(
            "The picture is a guarded, layered sky with lamps in the lowest heaven, used to pelt eavesdropping jinn — a late-antique enchanted cosmos. If 51:47 is allowed to be Hubble, 67:5 gets to be a dome with projectiles. Meteor-as-missile is still a cosmology of demons, not astronomy.",
            "Seven is a symbolic integer across the Near East (and in the Bible). Not a data count of atmospheric layers.",
            sources=[qv("67/5"), qv("37/6-10")],
        ),
        live={
            "if_they_say": "Seven atmospheres / shooting stars are meteors — science.",
            "you_say": "Meteors are real. Jinn-eavesdropping is not a physics paper. If you keep the jinn, it's theology. If you drop the jinn to save science, you're editing.",
            "dont_overclaim": "Don't say pre-modern Muslims didn't imagine a stacked sky. Don't say 67:5 is 'just a lie.' It's a cosmos.",
        },
        crux="Is the seven-heaven, star-missile sky a figurative weather report, or the actual world-picture of the text?",
        debate_use="Pair with 51:47. Same literalism both ways.",
    ),
    card(
        "water-cycle-pairs",
        39,
        "Scientific",
        "Rain cycle, barriers of water, and 'pairs' in creation",
        typ="science",
        popularity="Medium",
        why="Water-cycle verses are among the more empirically modest claims; 'pairs' get over-read as genetics.",
        claimant=side(
            "24:43, 30:48, 39:21 etc. describe evaporation-wind-rain-revival of land with a tightness ancient error-myths (underground reservoirs only) lacked. 51:49 / 36:36: pairs in what they do not know — plant sexuality / matter-antimatter / chromosomes.",
            "These are among the more observationally modest slides. Rain-as-cycle is at least compatible with what anyone can watch; the stretch is when 'pairs' becomes genetics.",
            sources=[qv("24/43"), qv("30/48"), qv("51/49"), qv("36/36")],
        ),
        critic=side(
            "Rain cycles were not a secret in late antiquity (even if popular myths varied). The verses are creation-theology, and they are compatible with observation. Compatibility ≠ prediction. 'Pairs' is a creation refrain (male/female, opposites); stretching it to antimatter is concordism at its most elastic.",
            "Score rain as a modest observational plus if you want. Do not let that plus launder antimatter or chromosomes.",
            sources=[qv("23/18"), qv("36/36")],
        ),
        live={
            "if_they_say": "The Qur'an described the water cycle and genetics.",
            "you_say": "Rain-as-mercy is observationally true and theologically aimed. 'Pairs of what you do not know' is not a genome paper. Score modest claims as modest.",
            "dont_overclaim": "Don't call the Qur'an a meteorology error-book. Don't call it Mendel.",
        },
        crux="Where does accurate nature-observation end and encoded modern science begin?",
        debate_use="Concede observational rain. Refuse antimatter. Show the slide-deck's gradient of abuse.",
    ),
    card(
        "preservation-as-miracle",
        40,
        "Historical",
        "Preservation (15:9) as a miracle — pointer, not a second historicity page",
        typ="textual history",
        popularity="Very high",
        why="Often dumped into i'jaz. This hub already has a Historicity topic. Here: only the miracle-claim shape.",
        claimant=side(
            "Q 15:9 is a promise of preservation. The unmatched manuscript situation and oral ḥifẓ are the miracle of history, not of rings or embryos.",
            "See the Historicity desk for Birmingham, Ṣanʿāʾ, qirāʾāt, and the Bible comparison.",
            sources=[
                qv("15/9"),
                S("EndDebates — Historicity of the Qur'an vs the Bible", "../historicity/"),
            ],
        ),
        critic=side(
            "Preservation is a separate argument (textual transmission), and it has its own variants, Ṣanʿāʾ lower text, and canonical readings. It should not be used as a trump when literary or scientific i'jaz fails — and it should not be spared criticism it gets on the Historicity page.",
            "15:9 does not decide 18:86. Do not launder cosmology through ḥifẓ.",
            sources=[S("EndDebates — Historicity", "../historicity/")],
        ),
        live={
            "if_they_say": "God promised to guard it, so all other miracles follow.",
            "you_say": "15:9 is a preservation claim. It does not decide 18:86 or 23:14. Send the round to Historicity if that's the fight. Don't launder cosmology through ḥifẓ.",
            "dont_overclaim": "Don't deny the oral/manuscript story is strong relative to many ancient books. Don't treat 15:9 as a science verse.",
        },
        crux="Is preservation a distinct historical claim that must be scored on manuscripts — not as a blanket i'jaz win?",
        debate_use="Park it. This page is literary-first i'jaz. Transmission has its own room in the hub.",
    ),
    # Sincerity (Hassan Ali, Argument from Sincerity — steelman + remainder)
    card(
        "sincerity-four-hypotheses",
        41,
        "Sincerity",
        "Four hypotheses: liar, insane, sincerely mistaken, genuine revelation",
        typ="method + prophecy",
        popularity="Very high",
        why=(
            "This is the Muhammad-side cousin of Lewis's trilemma, rebuilt so 'sincerely mistaken' is on the table. "
            "If the menu is wrong, the inference to God is cheap."
        ),
        claimant=side(
            "When Muhammad claimed revelation he was lying, insane, sincerely mistaken, or actually receiving it. "
            "Patricia Crone already grants the historical floor: the Qur'an is utterances he made believing they came from God. "
            "Close liar and insane, and the live fight is mistaken vs genuine — not 'maybe he never existed.'",
            "Hassan Ali's 2026 cumulative-case opener states the menu this way so the Christian 'maybe Jesus never claimed deity' leak does not apply: the claim-to-revelation is in the text itself. "
            "Aliens, demons, and time-travel are parked because they can undercut any religion's evidence equally. "
            "The Qur'an's own oath in 53:2–4 ('your companion has not strayed… he does not speak from desire') is the insider version of the same fork.",
            quotes=[
                Q(
                    "Most importantly, we can be reasonably sure that the Qur'an is a collection of utterances that he made in the belief that they had been revealed to him by God.",
                    "Patricia Crone",
                    "What do we actually know about Mohammed? (openDemocracy, 10 June 2008)",
                    "https://www.opendemocracy.net/en/mohammed-3866jsp/",
                ),
            ],
            data_points=[
                D("Lewis popularized liar / lunatic / Lord for Jesus; the Muslim analog must add 'sincerely mistaken' or it inherits the same hole.", "C.S. Lewis, Mere Christianity; Ali 2026"),
                D("Crone: he uttered all or most of the Qur'an; he is not responsible for the later arrangement.", "openDemocracy 2008"),
            ],
            sources=[
                S(
                    "Hassan Ali — Argument from Sincerity (Niche of Lights)",
                    "https://aporetic93.substack.com/p/argument-from-sincerity",
                ),
                S("Crone 2008 — What do we actually know about Mohammed?", "https://www.opendemocracy.net/en/mohammed-3866jsp/"),
                qv("53/2-4", "He does not speak from his own desire"),
            ],
        ),
        critic=side(
            "Crone's sentence is about belief, not about God speaking. A historian can grant 'he thought it was revelation' and stop. "
            "The menu is also incomplete: pious fraud (mission sincere, means flexible); mixed career (early conviction, later political convenience); communal / redacted Qur'an (not one man's 23-year inner life); literary-prophetic convention. "
            "'We will not consider demons' is a modeling choice, not a proof they are impossible.",
            "Lewis's trilemma leaked because sincere-but-wrong is the ordinary human case. Ali puts that option on the list — good — but then treats 'rare + successful' as enough to retire it. "
            "Success is not a fifth metaphysical hypothesis. It is what we already knew: Islam happened. "
            "If the remainder after 'not a calculating liar' and 'not DSM-psychotic' is still large, 'therefore God' is a leap, not a close.",
            quotes=[
                Q(
                    "To say that Muhammad was sincere does not imply that he was correct in his beliefs. A man may be sincere but mistaken.",
                    "W. Montgomery Watt",
                    "Muhammad, Prophet and Statesman (1961)",
                ),
            ],
            data_points=[
                D("Watt, Rodinson, Lewis, and Crone are routinely quoted for sincerity and routinely refuse a historian's supernatural verdict.", "Watt 1961; Lewis 1950; Crone 2008"),
                D("Revisionist and 'late compilation' models relocate some of the embarrassment-data from Muhammad's mouth to later tradents — the four-box then misfires.", "Qur'anic studies debate on collection/arrangement"),
            ],
            sources=[
                S("Crone 2008 (same essay: belief, not arrangement, not God)", "https://www.opendemocracy.net/en/mohammed-3866jsp/"),
                S("Ali 2026 — the menu being answered", "https://aporetic93.substack.com/p/argument-from-sincerity"),
            ],
        ),
        counters=[
            {
                "against": "Cheap skeptic",
                "claim": "Muhammad never existed / never claimed revelation.",
                "reply": "That is not the academic floor. Fight Crone's sentence if you want; do not skip to mythicism as a reflex.",
            },
            {
                "against": "Cheap dawah",
                "claim": "Liar, lunatic, or Lord — same as Jesus.",
                "reply": "Name 'sincerely mistaken' first. If you hide it, you are running Lewis's leak, not a case.",
            },
        ],
        live={
            "if_they_say": "He was either a liar, mad, or a prophet.",
            "you_say": "Add sincerely mistaken, pious fraud, and mixed career. Crone gets you 'he believed.' Watt already said belief ≠ correctness. Then argue the remainder; don't pretend the menu has three boxes.",
            "dont_overclaim": "Don't do mythicism. Don't call Crone a witness for i'jaz.",
        },
        crux="Does closing 'calculating fraud' and 'clinical psychosis' leave genuine revelation as the leftover — or only 'he believed,' which historians already grant?",
        debate_use="Force the four-box (plus leftovers) before trading Hira stories. Then: sincerity is the premise of the next cards, not the conclusion.",
    ),
    card(
        "sincerity-rebukes",
        42,
        "Sincerity",
        "Qur'anic rebukes and preserved accusations as anti-liar evidence",
        typ="criterion of embarrassment",
        popularity="High",
        why="If a fraud is writing scripture, 80:1–10, 75:16–19, and 16:103 look like unforced errors. Or like a genre that signals authenticity.",
        claimant=side(
            "The Qur'an rebukes Muhammad for rushing the recitation (75:16–19, 20:114) and for frowning off a blind man to court an elite (80:1–10). "
            "It also preserves the charge that 'a man teaches him' (16:103) instead of deleting the rumor. "
            "A calculating impostor does not invent awkward delivery, then scold himself for it, then keep the foreign-teacher smear on the record.",
            "Ali: even a mastermind-manipulator story struggles with 'why fake clumsy reception only to critique it.' "
            "The easier reading is that he took the speech as coming from an external authority that could also correct him. "
            "16:103 answers in Arabic vs aʿjamī — it does not pretend no one named a tutor.",
            quotes=[
                Q(
                    "[Prophet], do not rush your tongue in an attempt to hasten [your memorization of] the Revelation.",
                    "Qur'an 75:16",
                    "Abdel Haleem translation (as cited by Ali)",
                    "https://quran.com/75/16",
                ),
                Q(
                    "We know very well that they say, 'It is a man who teaches him,' but the language of the person they allude to is foreign, while this revelation is in clear Arabic.",
                    "Qur'an 16:103",
                    "Abdel Haleem",
                    "https://quran.com/16/103",
                ),
            ],
            data_points=[
                D("Rebuke cluster: 75:16–19; 20:114; 80:1–10. Accusation preserved: 16:103.", "Quran.com; Ali 2026"),
                D("80 is traditionally tied to Ibn Umm Maktūm — a named, checkable social awkwardness, not a vague piety slogan.", "Classical asbāb / tafsīr"),
            ],
            sources=[
                qv("80/1-10", "He frowned and turned away"),
                qv("75/16-19", "Do not rush your tongue"),
                qv("20/114", "Do not rush to recite before it is complete"),
                qv("16/103", "A man teaches him"),
                S("Ali 2026 — rebukes as anti-liar", "https://aporetic93.substack.com/p/argument-from-sincerity"),
            ],
        ),
        critic=side(
            "Self-rebuke is a known prophetic and biblical register (Nathan, Jonah, Paul's weakness). It can be piety-signaling, not a leak. "
            "80:1–10 can be the community explaining an awkward salon moment; that is how asbāb often work, not CCTV. "
            "16:103 is a rebuttal, not a confession: it names the rumor to kill it on linguistic grounds. Keeping a smear you then refute is ordinary polemic.",
            "Criterion of embarrassment assumes we know what a 7th-century author would find too costly to invent. We don't, especially if some of this was shaped in transmission. "
            "If later redactors arranged the muṣḥaf (Crone's own next sentence), 'why would Muhammad write this' is sometimes the wrong subject. "
            "A sincere speaker can still be a sincere reciter of material that includes community memory and biblical lore.",
            quotes=[
                Q(
                    "The book may not preserve all the messages he claimed to have received, and he is not responsible for the arrangement in which we have them.",
                    "Patricia Crone",
                    "What do we actually know about Mohammed? (2008)",
                    "https://www.opendemocracy.net/en/mohammed-3866jsp/",
                ),
            ],
            data_points=[
                D("Embarrassment-criteria in gospel studies have the same trap: later communities also keep 'costly' stories because they preach.", "NT method debates (criterion of embarrassment)"),
                D("16:103 sits next to the 'clear Arabic' file — it is as much a language-miracle verse as a sincerity verse.", "Q 16:103; this desk's 'clear-arabic' card"),
            ],
            sources=[
                qv("16/103"),
                S("Crone 2008 on collection/arrangement", "https://www.opendemocracy.net/en/mohammed-3866jsp/"),
            ],
        ),
        live={
            "if_they_say": "A liar would never write 80:1–10 or keep 16:103.",
            "you_say": "Self-rebuke is a genre. 16:103 is a rebuttal, not a leak. Grant that fraud-as-cool-mastermind is a bad story. That still lands you at sincerity, not at God.",
            "dont_overclaim": "Don't call 80 a nothing-burger. Don't treat every awkward āyah as a courtroom confession.",
        },
        crux="Do the rebuke and rumor-verses make calculating authorship unlikely — and if so, is that already the historians' sincerity, or a proof of an external speaker?",
        debate_use="Read 80 and 16:103 aloud. Separate 'not a novelist covering his tracks' from 'therefore Gabriel.'",
    ),
    card(
        "sincerity-mecca-persistence",
        43,
        "Sincerity",
        "Hira terror, Meccan years without gain, 'soft' temperament",
        typ="biography / sīra",
        popularity="High",
        why="The anti-liar case is not only verses. It is: he was scared, he stayed poor and mocked for years, and the tradition did not hide the fear.",
        claimant=side(
            "Sīra and ḥadīth have him terrified at the first revelations — fearing madness or a jinn — then persisting in Mecca for years with a handful of followers, mostly kin and the weak, under elite ridicule. "
            "Rodinson: crises of doubt make a cool ambition-plan look fake, and later piety would not invent such human traits from scratch. "
            "Nöldeke: a 'soft, even fearful' man whom the inner voice would not leave in peace. Andrae: introverted fear of brutal contact. "
            "That profile plus no early worldly payoff is a bad fit for imposture.",
            "Ali leans on Görke–Schoeler: the earliest ʿUrwa-layer reports are independently transmitted enough to count as early-attested, not Abbasid novellas. "
            "Daniel Peterson: the mode-of-revelation descriptions pass embarrassment. "
            "Public preaching against a hostile town, given that temperament, is more compulsive conviction than careerism.",
            quotes=[
                Q(
                    "A study of Muhammad's earliest messages, coupled with a perusal of accounts of the crises of doubt or despair which preceded or accompanied them, can only produce a skeptical attitude towards the theories which see them as evidence of a coolly calculated plan… Tradition, concerned to stress the supernatural affiliations of Muhammad's personality, would not have invented from scratch such very human traits.",
                    "Maxime Rodinson",
                    "Muhammad (1971), p. 78 (as cited by Ali)",
                ),
            ],
            data_points=[
                D("Standard Meccan period: roughly a decade of small following before any polity.", "Sīra outline; Watt, Muhammad at Mecca"),
                D("Görke & Schoeler 2024: ʿUrwa ibn al-Zubayr corpus as the earliest recoverable Muslim biographical layer (two+ independent strands).", "Gerlach Press, SLAEI 27"),
            ],
            sources=[
                S("Görke & Schoeler 2024 — ʿUrwa corpus", "https://gerlachpress.com/index.php?art_no=9783959941266"),
                S("Ali 2026 — Hira / persistence / temperament", "https://aporetic93.substack.com/p/argument-from-sincerity"),
                qv("73/1-5", "Cloaked one — early night-vigil strain"),
                qv("15/97", "We know your breast is tight because of what they say"),
            ],
        ),
        critic=side(
            "The 'no worldly gain' cut is Mecca-only. Medina has raids, a polity, wives, and a winner's archive. A two-act life can be sincere in act one and interested in act two — or sincere throughout and still mistaken. "
            "Fear-at-Hira is also a theophany trope (Isaiah, Ezekiel, Mary). Piety invents humanity when humanity preaches. "
            "ʿUrwa is early relative to Ibn Isḥāq, not CCTV; he is still a generation on, via ʿĀʾisha, inside the family.",
            "Nöldeke's 'soft/fearful' line is an explanation of sincerity, not of revelation — Ali quotes it as if temperament-plus-persistence needs God. "
            "Failed prophets also persist (Musaylima until the Yamāma; many late-antique holy men). We are studying the one whose community wrote the books and took the towns. "
            "Selection, not a controlled trial of 'introverts don't preach unless Gabriel.'",
            quotes=[
                Q(
                    "The modern historian will not readily believe that so great and significant a movement was started by a self-seeking impostor. Nor will he be satisfied with a purely supernatural explanation… rather, like Gibbon, will he seek… the secondary causes of the rapid growth of the new faith.",
                    "Bernard Lewis",
                    "The Arabs in History (1950), p. 45 (as cited by Ali — note the second sentence)",
                ),
            ],
            data_points=[
                D("Lewis is in Ali's sincerity chorus and explicitly sends the historian to secondary causes, not to God.", "Arabs in History, p. 45"),
                D("Hira / first-revelation narratives vary in the sources (vision, hearing, covering, Waraqa). Variation is not fatal, but it is not one snapshot.", "Sīra / ḥadīth file"),
            ],
            sources=[
                S("Ali 2026 (the biographical pile)", "https://aporetic93.substack.com/p/argument-from-sincerity"),
            ],
        ),
        live={
            "if_they_say": "He preached for years with nothing to gain, terrified it was a demon. Liars don't do that.",
            "you_say": "Grant Meccan sincerity. Then: Medina is not 'nothing to gain,' theophany-fear is a genre, and Lewis — in the same chorus — wants secondary causes, not a miracle. Persistence ≠ correctness.",
            "dont_overclaim": "Don't cartoon him as a con-man from day one. Don't freeze the story at year three and hide year twenty.",
        },
        crux="Do early fear and Meccan cost rule out cool fraud — and does that already exhaust the biographical argument, once Medina and selection are back on the table?",
        debate_use="Split Mecca / Medina. Then ask whether Nöldeke/Rodinson are being quoted through their last sentence or only their first.",
    ),
    card(
        "sincerity-expert-chorus",
        44,
        "Sincerity",
        "The non-Muslim sincerity chorus (Watt, Nöldeke, Rodinson, Crone…)",
        typ="historiography",
        popularity="High",
        why="Dawah treats 'even Orientalists admit he was sincere' as a score. The chorus is real. What they admitted is the fight.",
        claimant=side(
            "A long, mixed bench — Geiger, Nöldeke, Andrae, Bell, Arberry, Watt, Paret, Rodinson, Lewis, Welch, Crone — rejects the impostor thesis. "
            "Watt: persecution, the character of the early believers, and the scale of the result 'argue his fundamental integrity'; imposture 'raises more problems than it solves.' "
            "Welch: unshakable belief that he was called, from beginning to end, is the clue to the success. "
            "That convergence is not first-order evidence, but it is a serious prior against the liar box.",
            "Ali's point is modest if read strictly: expert testimony piles up against fraud, so the live options are mistaken vs genuine. "
            "You do not need Muslim ʿulamāʾ to retire the Victorian 'ambitious impostor.'",
            quotes=[
                Q(
                    "His readiness to undergo persecution for his beliefs, the high moral character of the men who believed in him and looked up to him as leader, and the greatness of his ultimate achievement—all argue his fundamental integrity. To suppose Muhammad an impostor raises more problems than it solves.",
                    "W. Montgomery Watt",
                    "Muhammad at Mecca (1953), p. 52",
                ),
                Q(
                    "A genuine Muhammad is much less difficult to explain than a fraudulent one.",
                    "Maxime Rodinson",
                    "Muhammad (1971), p. 78 (as cited by Ali)",
                ),
            ],
            data_points=[
                D("Ali's sample also includes Geiger 1896, Andrae 1936, Bell 1970, Paret 1957, Arberry 1953, Welch in EI.", "Ali 2026 notes 8–18"),
                D("Crone 2008 is the skeptical-endorsement exhibit: revisionist on much else, still 'in the belief that they had been revealed to him.'", "openDemocracy 2008"),
            ],
            sources=[
                S("Ali 2026 — expert excerpts", "https://aporetic93.substack.com/p/argument-from-sincerity"),
                S("Crone 2008", "https://www.opendemocracy.net/en/mohammed-3866jsp/"),
            ],
        ),
        critic=side(
            "Read the next sentence. Watt: sincere ≠ correct; the experiences may come from the unconscious. "
            "Lewis: not an impostor, and not a supernatural explanation. Rodinson writes as a Marxist historian, not as a shahāda. "
            "Crone's 'belief' line is the floor of critical scholarship, not a convert's coda. "
            "Quoting this bench for Islam is quoting them against their own last paragraph.",
            "Expert convergence that he was not a cartoon fraud is real and should be granted. Expert convergence that Gabriel spoke is not a thing. "
            "Welch's 'unshakable belief explains success' is social psychology: conviction moves people. That is also how many human movements work.",
            quotes=[
                Q(
                    "To say that Muhammad was sincere does not imply that he was correct in his beliefs. A man may be sincere but mistaken.",
                    "W. Montgomery Watt",
                    "Muhammad, Prophet and Statesman (1961)",
                ),
            ],
            data_points=[
                D("The same names appear in both columns of this desk: sincerity yes, i'jaz / prophecy as historian's verdict no.", "Watt, Rodinson, Lewis, Crone"),
            ],
            sources=[
                S("Ali 2026 (the list being read)", "https://aporetic93.substack.com/p/argument-from-sincerity"),
            ],
        ),
        live={
            "if_they_say": "Even the Orientalists say he was sincere — so he was a prophet.",
            "you_say": "They say sincere. Watt's next line is 'sincere but mistaken.' Lewis wants Gibbon's secondary causes. Grant the chorus against fraud; do not launder it into Gabriel.",
            "dont_overclaim": "Don't revive the Victorian impostor as if it were the academy. Don't treat Watt as a hidden Muslim.",
        },
        crux="Does the historian's sincerity-consensus retire the liar box only — or is it being asked to do the work of a miracle?",
        debate_use="Read Watt p. 52 and Watt 1961 'sincere but mistaken' as a pair. Same scholar, two sentences, two jobs.",
    ),
    card(
        "sincerity-pathology",
        45,
        "Sincerity",
        "No DSM box: psychosis, thought-insertion, temporal-lobe epilepsy",
        typ="psychology / diagnosis-at-a-distance",
        popularity="Medium",
        why="If 'insane' is the skeptic's leftover once fraud dies, the profile (age 40, 20+ years, structured sajʿ, high function) is the exhibit.",
        claimant=side(
            "Historically reconstructed profile: sudden episodic verbal auditory hallucination or thought-insertion from about age 40; structured, coherent, rhymed sacral prose believed to be from an external agent; twenty-plus years; otherwise high-functioning commander, judge, teacher. "
            "No known mental disorder fully fits. Psychosis can give voices, not this output minus clinically significant impairment. "
            "Temporal-lobe epilepsy might give sudden structured speech; it does not by itself give the full 'external agent' delusion plus no dysfunction.",
            "A disorder, by definition, involves distress, impairment, or dysfunction. The archive shows a successful community-builder until death. "
            "So 'insane' is a slogan that does not survive contact with the (granted) biographical sketch. Something else is needed — mistaken or genuine.",
            quotes=[
                Q(
                    "The really powerful factor in Muhammad's life and the essential clue to his extraordinary success was his unshakable belief from beginning to end that he had been called by God.",
                    "Alford T. Welch",
                    "Encyclopaedia of Islam, 'Muhammad' (as cited by Ali)",
                ),
            ],
            data_points=[
                D("Ali's fork inside the 'external' feeling: verbal auditory hallucination vs thought-insertion.", "Ali 2026, 'Was Muhammad Insane?'"),
            ],
            sources=[
                S("Ali 2026 — pathology section", "https://aporetic93.substack.com/p/argument-from-sincerity"),
            ],
        ),
        critic=side(
            "Retrospective psychiatry on a 7th-century figure known through sīra is not a diagnosis. 'No box fully fits' is true of most reconstructed geniuses and most prophets. "
            "The profile is built from the winning community's picture of success — then 'success' is used to rule out impairment. That is circular. "
            "High function plus religious experience is common in the ethnographic record. DSM 'impairment' is a modern clinic rule, not a metaphysical filter.",
            "You do not need a single DSM code to name ecstatic prophecy, grief-visions, sleep-related episodes, or culturally patterned hearing. "
            "TLE, temporal-lobe religiosity, and bipolar-spectrum creativity are live hypotheses in the older literature precisely because they are messy, not because they 'fully fit.' "
            "Failure of one label is not success of Gabriel. It is failure of armchair DSM.",
            data_points=[
                D("Historical-figure diagnosis (Jesus, Joan, Muhammad, van Gogh) is repeatedly warned against in psychiatry/history-of-medicine.", "Method literature on retrospective diagnosis"),
                D("If 'high-functioning' is in the inclusion criteria, impairment is excluded by construction.", "Ali's own profile sketch"),
            ],
            sources=[
                S("Ali 2026 — the profile being tested", "https://aporetic93.substack.com/p/argument-from-sincerity"),
            ],
        ),
        live={
            "if_they_say": "No mental illness produces 23 years of the Qur'an and a state.",
            "you_say": "No mental-illness label is required. 'Doesn't match DSM' is not 'therefore revelation.' Don't diagnose him from Ibn Isḥāq; don't call conviction psychosis either.",
            "dont_overclaim": "Don't amateur-diagnose epilepsy on stage. Don't treat 'he ran a polity' as a brain scan.",
        },
        crux="Is 'insane' a real leftover hypothesis that fails on the profile — or a straw box whose failure does no work toward God?",
        debate_use="Grant: not a cartoon madman. Then refuse the jump. The live remainder is still 'mistaken vs genuine.'",
    ),
    card(
        "sincerity-mistaken-output",
        46,
        "Sincerity",
        "Sincerely mistaken: sensory overrides, Joan of Arc, Smith, civilizational scale",
        typ="psychology + uniqueness",
        popularity="High",
        why="This is Ali's real payload: not 'he wasn't a liar,' but 'rare inner state plus unmatched output is surprising unless God.'",
        claimant=side(
            "Non-pathological 'sensory override' (Luhrmann) is usually rare, brief, and non-distressing — once or twice in a life. That is not Muhammad's pattern. "
            "Closer is the Joan of Arc pattern: frequent, vivid, non-distressing. That pattern is already extremely rare; his output (Qur'an + a world religion) then sits on top of it. "
            "There is no established pipeline from 'rare non-clinical voice-hearing' to civilizational success. The conjunction is what is striking under 'sincerely mistaken.'",
            "Napoleon has scale, not the rare revelatory state. Joan has the state, not the civilizational output. Joseph Smith lacks both a strong sincerity file and that scale. "
            "None of the stock parallels hold all three: strong sincerity evidence, extremely rare mental state, extremely influential output. Genuine revelation explains the whole pattern without a lottery.",
            quotes=[
                Q(
                    "The anthropological evidence suggests that there are three patterns of hallucinations: experiences in which hallucinations are rare, brief, and not distressing; hallucinations that are frequent, extended, and distressing; and hallucinations that are frequent but not distressing.",
                    "T. M. Luhrmann",
                    "Hallucinations and Sensory Overrides, Annual Review of Anthropology 40 (2011)",
                    "https://doi.org/10.1146/annurev-anthro-081309-145819",
                ),
            ],
            data_points=[
                D("Ali's three-element test: (1) strong sincerity evidence, (2) extremely rare non-pathological state, (3) extremely influential output.", "Ali 2026, 'Doesn't this prove too much?'"),
                D("Luhrmann 2011 is the cited psychology/anthropology receipt for 'sensory override.'", "Annu. Rev. Anthropol. 40:71–85"),
            ],
            sources=[
                S("Luhrmann 2011 — Hallucinations and Sensory Overrides", "https://doi.org/10.1146/annurev-anthro-081309-145819"),
                S("Ali 2026 — mistaken + parallels", "https://aporetic93.substack.com/p/argument-from-sincerity"),
            ],
        ),
        critic=side(
            "Luhrmann's third pattern is exactly frequent, non-distressing hearing — and she argues it is culturally invited and trainable (prayer, absorption, local theory of mind). "
            "That undercuts 'extremely rare outlier, therefore surprising.' Religious specialists are over-represented in pattern three by design. "
            "The conjunction is also post-selected: we are having this conversation because this movement won. Unsuccessful voice-hearers are invisible. Low-probability events occur; rarity is not a sender.",
            "Islam's scale has Lewis/Gibbon secondary causes (late antique vacuum, Arab military success, a portable law). Scale is not an independent miracle-meter sitting next to the psychology. "
            "Joan of Arc 'lacks civilizational scale' is a goalpost: she changed a war and was executed at 19. Smith: many historians grant sincere visionary experience; Mormonism is not a rounding error. "
            "If the test is 'sincerity + voices + a big after-effect,' it will keep matching human religion. If the test is 'as big as Islam,' only Islam can pass — that is uniqueness by definition.",
            quotes=[
                Q(
                    "Nor will he be satisfied with a purely supernatural explanation… rather, like Gibbon, will he seek… the secondary causes of the rapid growth of the new faith.",
                    "Bernard Lewis",
                    "The Arabs in History (1950), p. 45",
                ),
            ],
            data_points=[
                D("Luhrmann: local theory of mind + attentional training can shape even perception — pattern-three hearing is not a lightning-strike lottery only.", "Luhrmann 2011 abstract"),
                D("Watt already named the remainder Ali is trying to close: sincere, and possibly mistaken, with the unconscious as a candidate source of the 'from God' feeling.", "Watt 1961"),
            ],
            sources=[
                S("Luhrmann 2011 DOI", "https://doi.org/10.1146/annurev-anthro-081309-145819"),
                S("Ali 2026", "https://aporetic93.substack.com/p/argument-from-sincerity"),
            ],
        ),
        counters=[
            {
                "against": "Proves too much",
                "claim": "Then Joan of Arc and Joseph Smith are prophets too.",
                "reply": "Ask which of the three elements they actually grant. Then ask whether 'civilizational scale' is an independent clue or just 'Islam won.' Don't let uniqueness be defined as 'the biggest one.'",
            },
            {
                "against": "Skeptical shrug",
                "claim": "People hear voices, religion happens, nothing to see.",
                "reply": "That is too cheap. Grant the sincerity file and the oddness of the output. Then argue secondary causes and Luhrmann's trained pattern-three — not 'all prophets are identical.'",
            },
        ],
        live={
            "if_they_say": "Rare psyche plus the Qur'an plus Islam is too much coincidence unless God.",
            "you_say": "Luhrmann's pattern three is frequent non-distressing hearing, and it is culturally trained. Scale has conquest-and-vacuum explanations. Uniqueness-by-'biggest' only ever picks the winner. Remainder is still Watt's: sincere, maybe mistaken.",
            "dont_overclaim": "Don't flatten Muhammad into 'just another Smith.' Don't treat rarity as a likelihood ratio for Gabriel.",
        },
        crux="Is the conjunction (sincerity + rare inner state + civilizational output) surprising enough to prefer genuine revelation — or is it what a selected winner looks like under trained religious experience plus ordinary history?",
        debate_use="Grant the three elements one by one. Then: is scale independent of the thing being explained? Then read Luhrmann's third pattern, not only her first.",
    ),
]


VERSE_CATALOG = [
    G(
        "challenge",
        "Taḥaddī — the challenge verses",
        "Produce a sūrah like it. This is the Qur'an's own preferred miracle.",
        "Without a public rubric, 'like it' is judged by the believing community. Literary height is not thereby disproved — only the contest setup.",
        [
            V("17/88", "Mankind and jinn cannot produce the like"),
            V("2/23", "Produce a sūrah like it"),
            V("10/38", "A sūrah like it"),
            V("11/13", "Ten sūrahs like it"),
            V("52/34", "A ḥadīth like it"),
        ],
    ),
    G(
        "iltifat-ring",
        "Iltifāt and structural hinges",
        "Person-shifts and centre-verses are the literary-miracle exhibits NAK popularized.",
        "Shared Semitic rhetoric (Bible included). A hinge can be art or a join. Maps need constrained joints.",
        [
            V("1/5", "Fātiḥa: He-praise → You we worship"),
            V("2/143", "Umma wasaṭ — proposed centre of al-Baqara's ring"),
            V("10/22-23", "Abdel Haleem's person-shift examples neighbourhood"),
            V("12/3", "Yūsuf: the 'best of stories' as long-form control"),
        ],
    ),
    G(
        "problem-cosmology",
        "Cosmology collision verses (read these before NASA slides)",
        "Miracle-reading: phenomenology, idiom, or coded modern physics.",
        "Critical reading: late-antique layered sky, world-edge sun, enchanted meteors. Classical tafsīr is often more concrete than modern slides.",
        [
            V("18/86", "Sun found setting in a muddy/hot spring"),
            V("36/38", "Sun runs to a resting-place"),
            V("67/5", "Lamps of the lowest heaven as missiles against devils"),
            V("71/15-16", "Seven heavens; moon a light, sun a lamp"),
            V("79/30", "Earth 'spread' (daḥāhā) — egg-claim lives here"),
            V("21/33", "Sun and moon in a falak — orbit slide"),
        ],
    ),
    G(
        "science-hits",
        "Scientific-i'jaz proof-texts (the slide deck)",
        "Read as anticipation: embryology, expansion, iron, mountains, seas, Rūm, Pharaoh's body.",
        "Read as concordism: Galen, 'vast' not Hubble, anzala-idiom, visible estuaries, nearest not lowest land, unnamed mummy.",
        [
            V("23/12-14", "Nuṭfa ʿalaqa muḍgha bones flesh"),
            V("22/5", "Parallel creation-stages"),
            V("51/47", "Innā la-mūsiʿūn"),
            V("21/30", "Heavens and earth were joined, then split"),
            V("57/25", "Iron sent down"),
            V("78/6-7", "Mountains as pegs"),
            V("55/19-20", "Two seas, a barrier"),
            V("30/2-4", "Rūm defeated then victorious"),
            V("10/92", "Pharaoh's body as a sign"),
            V("41/53", "Signs in the horizons — method verse"),
        ],
    ),
    G(
        "science-misses",
        "Verses apologetics must metaphorize (symmetry test)",
        "If these are idiom/poetry, the 'hits' may be too. One rule.",
        "If the hits are science textbooks, these get the same court.",
        [
            V("86/5-7", "Brought forth from between backbone and ribs"),
            V("18/86", "Muddy spring — again, because it is both history and cosmos"),
            V("67/5", "Stars as shayāṭīn-missiles"),
            V("4/157", "Crucifixion file — historical, not scientific, but often adjacent in 'errors' lists"),
            V("19/28", "Sister of Aaron"),
            V("28/38", "Hāmān, bake for me a tower"),
        ],
    ),
    G(
        "genre-orality",
        "Genre: not poet, not soothsayer; oaths and refrains",
        "A third register: sajʿ that refuses the poet label.",
        "The refusal is evidence the comparison was live. Kāhin-sajʿ is the nearby human analog.",
        [
            V("69/40-42", "Not a poet's word, not a kāhin's"),
            V("36/69", "We did not teach him poetry"),
            V("55/13", "Refrain of al-Raḥmān"),
            V("91/1-10", "Oath-series then moral punch"),
            V("96/15-16", "Forelock — idiom vs prefrontal cortex"),
        ],
    ),
    G(
        "sincerity",
        "Sincerity / anti-liar verses (Ali 2026 file)",
        "Rebukes and preserved smears: a fraud would not write these. 53:2–4 is the Qur'an's own sincerity oath.",
        "Self-rebuke is a prophetic genre; 16:103 is a rebuttal; historians already grant belief. Awkward āyah ≠ Gabriel.",
        [
            V("80/1-10", "Frowned at the blind man — social rebuke"),
            V("75/16-19", "Do not rush your tongue"),
            V("20/114", "Do not rush to recite before it is complete"),
            V("16/103", "They say a man teaches him"),
            V("53/2-4", "Your companion has not strayed; he does not speak from desire"),
            V("15/97", "Your breast is tight because of what they say"),
            V("73/1-5", "Cloaked one — early strain of the call"),
        ],
    ),
]


OPENING_SPEECH = {
    "title": "How to talk about 'Qur'anic miracles' without doing daʿwa or hatchet-work",
    "lede": (
        "Read this first. The point is not to win Islam or to sink it. The point is to stop treating "
        "'i'jaz' as one blob. Literary craft, linguistic oddity, historical claim, and scientific concordism "
        "are four different games with four different scoring rules. "
        "A fifth game — Muhammad's sincerity — is not i'jaz. Do not launder it through rings or embryos."
    ),
    "paragraphs": [
        {
            "text": (
                "Start where the Qur'an starts. The challenge verses do not say 'find a microscope.' "
                "They say: produce speech like this. Classical i'jaz — Jurjānī, not YouTube — is about naẓm, "
                "the fit of wording and meaning. If you are a Muslim who cares about the tradition, that is the "
                "home field. If you are a critic, attacking Bucaille while ignoring Abdel Haleem is fighting a "
                "street pamphlet and calling it the madrasa."
            ),
            "refs": [
                {"ref": "Q 17:88", "url": "https://quran.com/17/88"},
                {"ref": "Q 2:23", "url": "https://quran.com/2/23"},
            ],
        },
        {
            "text": (
                "Literary features are real enough to argue. Ring maps of al-Baqara and Yūsuf, iltifāt as a named "
                "balāgha device, sūrah-level naẓm in the Farāhī–Iṣlāḥī–Mir line, sound in Sells, liturgical orality "
                "in Neuwirth — none of that is a hallucination of dawah. Nouman Ali Khan is the mass popularizer of "
                "this lane in English. The critic's adult move is not 'Nöldeke thought pronoun shifts were ugly, case closed.' "
                "It is: this is ancient Near Eastern craft (the Bible does chiasmus; Arabic already had sajʿ). Craft is not "
                "a laboratory proof of God. Uniqueness has to be argued against the actual toolbox, not against a cartoon of 'jumble.'"
            ),
            "refs": [
                {"ref": "Abdel Haleem 1992", "url": "https://doi.org/10.1017/S0041977X00003621"},
                {"ref": "Farrin 2014", "url": "https://iqsaweb.org/2014/11/24/farrin_structure-and-quranic-interpretation/"},
            ],
        },
        {
            "text": (
                "Then say the sentence apologetics hates: some verses were read more literally than the slide. "
                "Dhū l-Qarnayn finds the sun setting in a muddy or hot spring. Ibn Kathīr can say 'as at the seashore.' "
                "Early reports and the Alexander Legend can say a world-edge fetid sea. Abu Dharr's sun-hadith is not a NASA briefing. "
                "If your Islam requires that 18:86 never have been heard as cosmology, you are protecting a modern reconstruction, "
                "not reporting the archive. If your atheism requires that a travel-narrative verb 'he found' is a physics assertion "
                "and that Joshua's sun standing still is 'just poetry,' you are running a kangaroo court."
            ),
            "refs": [
                {"ref": "Q 18:86", "url": "https://quran.com/18/86"},
                {"ref": "Ibn Kathīr 18:86", "url": "https://quran.com/18:86/tafsirs/en-tafisr-ibn-kathir"},
            ],
        },
        {
            "text": (
                "Scientific i'jaz is a 20th-century genre. Bucaille, Moore, El-Naggar, Naik. The method is concordism: "
                "after the discovery, widen the Arabic until it fits; when it does not fit — backbone and ribs, star-missiles, "
                "bones then flesh as biology — call it metaphor. Hamza Tzortzis later criticized that method from inside the "
                "same dawah world. Ahmad Dallal historicized it. You may still find 23:14 impressive. You may find it Galenic. "
                "What you may not do is score hits in 2020 semantics and misses in 720 rhetoric."
            ),
            "refs": [
                {"ref": "Q 23:14", "url": "https://quran.com/23/14"},
                {"ref": "Q 86:6-7", "url": "https://quran.com/86/6-7"},
            ],
        },
        {
            "text": (
                "Historical files are one-by-one: Rūm and dating; Hāmān as merge or Egyptian name; Mary as typology or mix-up; "
                "infancy miracles as Syriac lore; Pharaoh's corpse as unnamed mummy. None of these is settled by shouting 'context' "
                "or 'gotcha.' And preservation is a different topic in this hub — do not launder a cosmology debate through 15:9."
            ),
            "refs": [
                {"ref": "Q 30:2-4", "url": "https://quran.com/30/2-4"},
                {"ref": "Historicity desk", "url": "../historicity/"},
            ],
        },
        {
            "text": (
                "The crux, said once: a literary masterpiece can be human. A human text can still be believed as revelation on other grounds. "
                "A revealed text can still talk in 7th-century images. Those three sentences, held together, are what this page is for. "
                "Pick a lane for the round — speech, history, science, or sincerity — and put the misses on the same table as the hits."
            ),
            "refs": [
                {"ref": "Q 41:53", "url": "https://quran.com/41/53"},
            ],
        },
        {
            "text": (
                "Sincerity is a different lane. Hassan Ali's 2026 'Argument from Sincerity' is the clean modern form: liar, insane, sincerely mistaken, or genuine; "
                "Crone already grants he believed the utterances were from God; rebukes (80, 75, 16:103), Hira-fear, Meccan cost, and a historian-chorus (Watt, Nöldeke, Rodinson) pile up against cool fraud; "
                "no DSM box 'fully fits'; the payload is then rare inner state plus civilizational output. "
                "The adult critic does not revive the Victorian impostor. The adult critic reads Watt's next sentence — sincere ≠ correct — and Luhrmann's third pattern (frequent, non-distressing, culturally trained hearing), "
                "and does not let 'Islam is big' count as an independent miracle. Grant sincerity. Then argue the remainder."
            ),
            "refs": [
                {"ref": "Ali 2026", "url": "https://aporetic93.substack.com/p/argument-from-sincerity"},
                {"ref": "Crone 2008", "url": "https://www.opendemocracy.net/en/mohammed-3866jsp/"},
                {"ref": "Luhrmann 2011", "url": "https://doi.org/10.1146/annurev-anthro-081309-145819"},
                {"ref": "Q 80:1-10", "url": "https://quran.com/80/1-10"},
            ],
        },
    ],
}


DATA = {
    "id": "quranic-miracles",
    "meta": {
        "title": "Qur'anic miracles (i'jaz): literary first — then linguistic, historical, scientific",
        "thesis": (
            "What are the strongest 'miracle' claims Muslims actually make for the Qur'an — starting with literary "
            "features (ring composition, iltifāt, naẓm, sound) that Nouman Ali Khan popularized — then the argument from "
            "Muhammad's sincerity (liar / insane / mistaken / genuine) — and which of them survive when you allow the "
            "readings that do not help apologetics?"
        ),
        "purpose": (
            "A desk for i'jaz that is not a dawah pamphlet: steelman the claim, then the skeptical, academic, or "
            "classical-literal counter. Literary craft first. Scientific concordism last, with the same rule for hits and misses. "
            "Sincerity is a fifth lane: grant the historian's 'he believed,' then argue the remainder. "
            "No declared winner."
        ),
        "warning": (
            "Objectivity rule: 18:86, 86:6–7, 67:5, Galen-on-embryology, and the Alexander Legend stay on the table. "
            "So do Farrin, Abdel Haleem, Jurjānī, and the taḥaddī verses. Do not run only one half of the archive. "
            "Literary quality is not 'Islam wins.' A 7th-century image is not 'Islam dies.' "
            "Watt's sincerity is not Watt's Gabriel."
        ),
        "chips": ["i'jaz", "literary first", "iltifāt", "rings", "sincerity", "concordism", "18:86"],
        "labels": {
            "claimant": "Miracle claim (steelman)",
            "critic": "Skeptical / academic / literal-archive case",
        },
        "side_keys": ["claimant", "critic"],
        "default_tab": "arguments",
        "ui": {
            "tab_arguments": "Miracle claims",
            "tab_verses": "Verses",
            "tab_speech": "Method speech",
            "intro_brief": "Lock what 'miracle' means. Literary i'jaz, historical sign, scientific concordism, and sincerity are not one argument.",
            "intro_arguments": "Each card: the best version of the miracle claim, then the best version of the doubt — including readings Muslims use in tafsīr and then drop on stage.",
            "intro_verses": "Verses the claims hang on. First note is the miracle-reading; second is the critical or classical-literal reading.",
            "intro_speech": "A method opener, not a verdict. Copy it if you need a fair round.",
            "h_definitions": "Words that smuggle the conclusion",
            "h_positive": "How to stand on either podium without lying",
            "unitarian_move": "Miracle-claim reading: ",
            "christian_reply": "Critical / alternate reading: ",
            "search_placeholder": "Search: iltifāt, ring, sincerity, 80:1, Watt, 18:86, Galen, Farrin…",
        },
    },
    "definitions": [
        {
            "term": "I'jaz",
            "precise": "The claim that the Qur'an is inimitable as a sign of its source. Classically: speech (naẓm, balāgha), sometimes unseen news. Modernly: also science, numbers, archaeology.",
            "not": "Not automatically 'scientifically ahead of its time.' That is i'jaz ʿilmī, a later genre.",
        },
        {
            "term": "Taḥaddī",
            "precise": "The challenge to produce the like of the Qur'an (2:23, 10:38, 11:13, 17:88). The Qur'an's own preferred public sign.",
            "not": "Not a specified exam with blind judging. If 'like it' is defined by the defendant, the challenge cannot fail.",
        },
        {
            "term": "Iltifāt",
            "precise": "A named Arabic rhetorical 'turn': shift of person, number, addressee, tense, or noun/pronoun, used for effect. Abdel Haleem 1992 vs Nöldeke's aesthetic complaint.",
            "not": "Not a sticker you may paste on every rough join so that nothing can count as oral seam or later insertion.",
        },
        {
            "term": "Ring / chiasmus / concentrism",
            "precise": "Symmetry patterns A–B–C–B'–A' (or ABB'A', AB A'B'). Farrin and Cuypers map them in sūrahs; biblical studies mapped them first. NAK popularized the charts.",
            "not": "Not a divine fingerprint by default. The Bible and other ancient literatures do this. Maps are only as good as the joints.",
        },
        {
            "term": "Naẓm",
            "precise": "Arrangement. In Jurjānī: the wording-meaning fit that constitutes eloquence. In Farāhī/Iṣlāḥī/Mir: sūrah-level thematic unity (ʿamūd).",
            "not": "Not 'the 1924 Cairo page looks pretty.' Not automatically 'one sitting, one author, no redaction.'",
        },
        {
            "term": "Concordism (i'jaz ʿilmī)",
            "precise": "Reading modern scientific results back into verses whose pre-modern range was wider or different. Bucaille 1976 is the mass-market start.",
            "not": "Not 'the verse is compatible with some later fact.' Compatibility is cheap. Prediction requires 7th-century reachable meaning and a fail condition.",
        },
        {
            "term": "Phenomenological language",
            "precise": "Describing how things appear (sun 'sets,' sky 'above'). Every natural language does this. A fair defence of some cosmic verses.",
            "not": "Not a free pass when the narrative is a hero reaching the sun's setting-place among a people, or when hadith add a sun prostrating under the Throne.",
        },
        {
            "term": "Ummī",
            "precise": "Qur'anic epithet of the Prophet (7:157). Dawah: illiterate. Much academic usage: gentile / unscriptured / not of the People of the Book.",
            "not": "Not a settled synonym of 'could not have heard a poet or a Christian homily in Arabia.'",
        },
        {
            "term": "Qirāʾāt / aḥruf",
            "precise": "Canonical recitations with real differences (e.g. 18:86 muddy vs hot). Literary i'jaz can live with them. Letter-counting and some 'scientific constants' cannot.",
            "not": "Not 'the Qur'an is lost.' Not 'there is only pronunciation.'",
        },
        {
            "term": "Argument from sincerity",
            "precise": "Muhammad was not a calculating liar (and not a cartoon madman); therefore the remaining live options are sincerely mistaken vs genuine revelation. Modern form: Ali 2026. Classical dawah often skips 'mistaken' and runs a Lewis trilemma.",
            "not": "Not 'Orientalists admitted he was a prophet.' Most of the chorus grant belief and refuse a historian's supernatural verdict (Watt, Lewis, Rodinson, Crone).",
        },
        {
            "term": "Criterion of embarrassment",
            "precise": "A report that costs the hero (rebukes in 80, 75, 20:114; the tutor-smear in 16:103; Hira-fear) is less likely to be a cool fabrication. Used as anti-liar evidence.",
            "not": "Not a lie detector. Later communities also keep costly stories because they preach. Self-rebuke is a prophetic genre.",
        },
        {
            "term": "Sensory override",
            "precise": "Luhrmann's non-pathological term for hallucination-like experience. Three patterns: rare/brief/non-distressing; frequent/distressing; frequent/non-distressing (often culturally trained).",
            "not": "Not 'once or twice in a lifetime' as the only natural option. Pattern three is the Joan-of-Arc / prayer-specialist file.",
        },
        {
            "term": "Objectivity rule (this page)",
            "precise": "The reading that hurts the miracle-claim stays visible: muddy spring, Galen, Alexander Legend, sister of Aaron, 86:6–7, star-missiles. So does the reading that helps: Ibn Kathīr's seashore, Abdel Haleem, Farrin, Jurjānī.",
            "not": "Not 'Islam is false because 18:86.' Not 'Islam is true because a ring chart exists.'",
        },
    ],
    "arguments": ARGUMENTS,
    "opening_speech": OPENING_SPEECH,
    "verse_catalog": VERSE_CATALOG,
    "materials": [],
    "debates": [
        {
            "id": "lanes",
            "title": "Run i'jaz in lanes, or you will cheat",
            "year": 2026,
            "venue": "Prep note",
            "participants": ["You"],
            "motion": "Literary i'jaz, historical signs, and scientific concordism may not rescue one another mid-round.",
            "summary": (
                "If embryology fails, iltifāt is still a real file. If rings are real, 18:86 is still a file. "
                "The dishonest move is to treat every win as 'the Qur'an' and every loss as 'that's just language.'"
            ),
            "key_moves": {
                "Miracle claim (steelman)": [
                    "Open with taḥaddī and Jurjānī, not NASA",
                    "Use Abdel Haleem / Farrin / Mir as receipts, NAK as pedagogy",
                    "If you use science, pre-commit to a 7th-century meaning and accept 86:6–7 under the same rule",
                ],
                "Skeptical / academic case": [
                    "Grant craft; deny unique-therefore-God",
                    "Put Alexander Legend and Galen on the table without 1860 'jumble' sneers",
                    "Do not run Bible-as-poetry and Qur'an-as-textbook in the same breath",
                ],
            },
            "what_to_steal": [
                "One sūrah, one joint, one lexicon — not 40 slides",
                "Classical tafsīr on the 'miss' verses",
                "Sinai on rings; van Bladel on Q 18; Dallal on concordism",
            ],
            "links": [
                {"label": "Abdel Haleem 1992", "url": "https://doi.org/10.1017/S0041977X00003621"},
                {"label": "Farrin 2014 notice", "url": "https://iqsaweb.org/2014/11/24/farrin_structure-and-quranic-interpretation/"},
                {"label": "Tzortzis on scientific miracles", "url": "https://www.hamzatzortzis.com/does-the-quran-contain-scientific-miracles-a-new-approach/"},
            ],
        }
    ],
    "opponent_cards": [
        {
            "trigger": "Ring structure in al-Baqara proves God wrote it",
            "fast_answer": "Grant the chart only if the joints are argued. Then: chiasmus is a shared ancient tool (Bible too). Structure ≠ sender.",
            "follow_up": "Sinai, 'Going Round in Circles.' NAK is a teacher, Farrin is the receipt.",
            "sources": ["Farrin 2014", "Sinai 2017", "Q 2:143"],
        },
        {
            "trigger": "The Qur'an switches He/We because Muhammad was confused",
            "fast_answer": "That's the weak skeptical line. Iltifāt is a named device; Abdel Haleem vs Nöldeke. The strong line: attested rhetoric ≠ divinity.",
            "follow_up": "Do one verse. If there is no payoff, don't stamp 'iltifāt' as magic either.",
            "sources": ["Abdel Haleem 1992", "Q 1:5"],
        },
        {
            "trigger": "Nobody has met the challenge in 1400 years",
            "fast_answer": "What is the rubric a non-Muslim Arabist could apply? If the jury is the defendant, the contest cannot fail.",
            "follow_up": "Separate extraordinary Arabic from a proof of God.",
            "sources": ["Q 17:88", "Q 2:23"],
        },
        {
            "trigger": "The sun sets in a muddy puddle so Islam is false",
            "fast_answer": "Read 18:86, Ibn Kathīr's seashore phenomenology, the Alexander Legend parallel, and Bukhari 3199. Then argue which first audiences heard. Don't one-liner it.",
            "follow_up": "Apply the same genre rule to biblical cosmology.",
            "sources": ["Q 18:86", "Ibn Kathīr", "van Bladel"],
        },
        {
            "trigger": "The Qur'an predicted embryology",
            "fast_answer": "Table 23:12–14 next to Galen. ʿAlaqa as clot in tafsīr vs leech-photo. Then 86:6–7 under the same rule. Hits and misses, one court.",
            "follow_up": "Moore was impressed; Moore is not the field. Tzortzis later attacked the method.",
            "sources": ["Q 23:14", "Q 86:6-7", "al-bab Bucaille history"],
        },
        {
            "trigger": "It's not poetry and not prose — that's the miracle",
            "fast_answer": "It's sajʿ in a culture that already had kāhin-sajʿ. The Qur'an fends off 'poet' because people heard a cousin-genre. Unique mix ≠ no analog.",
            "follow_up": "Define ʿarūḍ meter before quoting 36:69.",
            "sources": ["Q 69:41", "Q 36:69"],
        },
        {
            "trigger": "An illiterate man could not produce this",
            "fast_answer": "Ummī may mean unscriptured, not illiterate. Arabia had poets and biblical talk. Oral genius exists. Three premises, not one.",
            "follow_up": "Q 29:48 ≠ 'never heard a homily.'",
            "sources": ["Q 7:157", "Q 29:48"],
        },
        {
            "trigger": "Mary is called sister of Aaron — mix-up",
            "fast_answer": "Honorific/clan vs conflation with Miriam. Live since John of Damascus. Ask what would falsify 'ukht = of Aaron's house.'",
            "follow_up": "Don't pretend 19:28 is trivial either way.",
            "sources": ["Q 19:28", "Q 3:35-45"],
        },
        {
            "trigger": "Haman in Egypt is a blunder / a hieroglyph miracle",
            "fast_answer": "Literary merge (Esther+Pharaoh+Babel) vs distinct Hāmān. Inscription claims need a living Egyptologist on that object, not a 1990s slide.",
            "follow_up": "IA packet vs the anachronism intuition — both stay on the table.",
            "sources": ["Q 28:38", "Islamic Awareness Haman"],
        },
        {
            "trigger": "The number 19 / word-counts prove it",
            "fast_answer": "Khalifa's 19 is sectarian. Counts need a fail-able protocol and a chosen qirāʾa. Pattern-hunting always 'succeeds.'",
            "follow_up": "Don't smear Jurjānī with Rashad Khalifa.",
            "sources": ["Q 74:30"],
        },
        {
            "trigger": "He was either a liar, mad, or a prophet",
            "fast_answer": "Add sincerely mistaken. Crone already grants he believed. Watt: sincere ≠ correct. Closing fraud is not closing the case.",
            "follow_up": "Ali 2026 is the clean form of the argument. Read it; then read Watt 1961 and Luhrmann's third pattern.",
            "sources": ["Ali 2026", "Watt 1961", "Crone 2008"],
        },
        {
            "trigger": "A liar would never write 80:1–10 or keep 16:103",
            "fast_answer": "Self-rebuke is a genre. 16:103 is a rebuttal, not a leak. Grant: bad fit for cool fraud. That is sincerity, not Gabriel.",
            "follow_up": "Then Hira-fear and Meccan cost — same split: anti-liar, not a proof.",
            "sources": ["Q 80:1-10", "Q 16:103"],
        },
        {
            "trigger": "Even the Orientalists say he was sincere",
            "fast_answer": "They say sincere. Lewis wants secondary causes. Watt's next line is mistaken. Don't launder the chorus into i'jaz.",
            "follow_up": "Read the last paragraph of each excerpt, not only the first.",
            "sources": ["Watt 1953/1961", "Lewis 1950", "Crone 2008"],
        },
        {
            "trigger": "Rare psyche plus Islam is too much coincidence unless God",
            "fast_answer": "Luhrmann pattern three is frequent, non-distressing, culturally trained. Scale has conquest-and-vacuum explanations. Uniqueness-by-biggest only ever picks the winner.",
            "follow_up": "Napoleon / Joan / Smith: ask whether 'civilizational scale' is independent of the thing explained.",
            "sources": ["Luhrmann 2011", "Ali 2026"],
        },
        {
            "trigger": "All i'jaz is just Bucailleism",
            "fast_answer": "False. Jurjānī and iltifāt and naẓm are a different century and a different claim. Attack concordism; don't pretend you refuted balāgha.",
            "follow_up": "Make them pick a lane.",
            "sources": ["classical i'jaz", "Dallal", "Tzortzis walk-back"],
        },
        {
            "trigger": "The Qur'an is a disjointed jumble",
            "fast_answer": "That is not the state of literary studies. Argue over-mapped rings (Sinai), not 1860. Hear Q 12 and Q 55 before you sneer.",
            "follow_up": "Composite-ness and craft can coexist.",
            "sources": ["Mir", "Robinson", "Sells"],
        },
    ],
    "checklist": [
        "Name the lane: literary / linguistic / historical / scientific / sincerity. No mid-round lane-change.",
        "For literary claims: show a joint or a shift's payoff, then a non-Qur'anic analog (Bible, sajʿ, qaṣīda).",
        "For taḥaddī: demand a rubric a hostile Arabist could apply.",
        "For science: pre-modern tafsīr first; photos are not lexica; misses (86:6–7, 67:5, 18:86) use the same rule as hits.",
        "For 18:86: Ibn Kathīr and Alexander Legend and Bukhari 3199 — all three, or you are preaching.",
        "For embryology: Galen table next to 23:14 before Moore's leech.",
        "For rings: one sūrah, three joints, Sinai's caution.",
        "Qirāʾa specified before any letter-count or 'the Arabic word is X.'",
        "Ummī defined from usage, not from a movie about illiteracy.",
        "Sincerity: grant the historian's 'he believed.' Then argue remainder (Watt 1961, Luhrmann pattern three, Medina/selection). Do not revive the Victorian impostor as if it were the academy.",
        "Do not quote Watt/Lewis/Rodinson/Crone for Gabriel. They are the anti-liar chorus, not a shahāda.",
        "Preservation fights go to the Historicity topic — do not launder them here.",
    ],
    "positive_cases": {
        "Miracle-claim podium": [
            "Lead with taḥaddī, naẓm, iltifāt, sound — the Qur'an's own kind of sign",
            "Sincerity as a separate lane: Ali's four-box, rebukes, Hira, the historian-chorus — then ask for the remainder",
            "Cite Abdel Haleem, Farrin/Cuypers, Mir, Jurjānī; use NAK as a teacher not as a primary source",
            "If you use science, announce the rule and swallow 86:6–7 under it, or don't use science",
        ],
        "Skeptical podium": [
            "Grant that 'jumble' is a dead thesis; fight uniqueness and inference-to-God",
            "Put Legend, Galen, and classical literal tafsīr on the table without culture-war grin",
            "Apply genre consistently to Bible and Qur'an",
            "Grant historian-sincerity; do not revive the Victorian impostor; then Watt 1961 + Luhrmann pattern three",
        ],
        "Unity / steelman": [
            "Five lanes, five scores. A ring can be real and 18:86 can still be a late-antique cosmos.",
            "A revealed text may talk in 7th-century images; a human text may be superb.",
            "Sincerity can be real and 18:86 can still be a late-antique cosmos. Different lanes.",
            "No declared winner on this page — shared archive first",
        ],
    },
    "bibliography": [
        {
            "tier": "Literary i'jaz (start here)",
            "items": [
                {"label": "Abdel Haleem — Iltifāt, BSOAS 55.3 (1992)", "url": "https://doi.org/10.1017/S0041977X00003621"},
                {"label": "Abdel Haleem PDF (SOAS eprints)", "url": "https://eprints.soas.ac.uk/7308"},
                {"label": "Farrin — Structure and Qur'anic Interpretation (2014)", "url": "https://iqsaweb.org/2014/11/24/farrin_structure-and-quranic-interpretation/"},
                {"label": "Cuypers — Semitic rhetoric / naẓm (JQS 2011)", "url": "https://doi.org/10.3366/jqs.2011.0003"},
                {"label": "Mustansir Mir — Coherence in the Qur'an", "url": "https://archive.org/details/CoherenceInTheQuranMustansirMir"},
                {"label": "Sinai — Going Round in Circles (JQS 19.2, 2017)", "url": "https://www.euppublishing.com/doi/abs/10.3366/jqs.2017.0284"},
                {"label": "Sells — Approaching the Qur'an", "url": "https://www.whitecloudpress.com/approaching-the-quran/"},
            ],
        },
        {
            "tier": "Milieu, intertext, 18:86",
            "items": [
                {"label": "Reynolds — The Qur'an and the Bible", "url": "https://yalebooks.yale.edu/book/9780300181320/the-quran-and-the-bible/"},
                {"label": "Reynolds (ed.) — The Qur'an in Its Historical Context (van Bladel on Alexander)", "url": "https://www.routledge.com/The-Quran-in-Its-Historical-Context/Reynolds/p/book/9780415491693"},
                {"label": "Q 18:86", "url": "https://quran.com/18/86"},
                {"label": "Ibn Kathīr on 18:86", "url": "https://quran.com/18:86/tafsirs/en-tafisr-ibn-kathir"},
                {"label": "Bukhari 3199 (sun / Throne)", "url": "https://sunnah.com/bukhari:3199"},
            ],
        },
        {
            "tier": "Science / concordism",
            "items": [
                {"label": "al-bab — Science and the Qur'an (Bucaille/Moore history)", "url": "https://al-bab.com/science-and-quran"},
                {"label": "Moore 1986 JIMA embryology article", "url": "https://doi.org/10.5915/18-1-8693"},
                {"label": "Dallal — Islam, Science, and the Challenge of History", "url": "https://yalebooks.yale.edu/book/9780300177718/islam-science-and-the-challenge-of-history/"},
                {"label": "Tzortzis — Does the Qur'an Contain Scientific Miracles?", "url": "https://www.hamzatzortzis.com/does-the-quran-contain-scientific-miracles-a-new-approach/"},
                {"label": "Q 23:12–14", "url": "https://quran.com/23/12-14"},
                {"label": "Q 86:5–7", "url": "https://quran.com/86/5-7"},
            ],
        },
        {
            "tier": "Historical collision files",
            "items": [
                {"label": "Q 30:2–4 (Rūm)", "url": "https://quran.com/30/2-4"},
                {"label": "Islamic Awareness — Haman", "url": "https://www.islamic-awareness.org/quran/contrad/external/haman.html"},
                {"label": "Q 19:28 (sister of Aaron)", "url": "https://quran.com/19/28"},
                {"label": "Q 10:92 (Pharaoh's body)", "url": "https://quran.com/10/92"},
            ],
        },
        {
            "tier": "Sincerity / prophetic psychology",
            "items": [
                {"label": "Hassan Ali — Argument from Sincerity (2026)", "url": "https://aporetic93.substack.com/p/argument-from-sincerity"},
                {"label": "Patricia Crone — What do we actually know about Mohammed? (2008)", "url": "https://www.opendemocracy.net/en/mohammed-3866jsp/"},
                {"label": "T. M. Luhrmann — Hallucinations and Sensory Overrides (2011)", "url": "https://doi.org/10.1146/annurev-anthro-081309-145819"},
                {"label": "Görke & Schoeler — The Earliest Writings on the Life of Muḥammad (2024)", "url": "https://gerlachpress.com/index.php?art_no=9783959941266"},
                {"label": "Q 80:1–10 (frowned)", "url": "https://quran.com/80/1-10"},
                {"label": "Q 16:103 (a man teaches him)", "url": "https://quran.com/16/103"},
                {"label": "Q 53:2–4 (not from desire)", "url": "https://quran.com/53/2-4"},
            ],
        },
        {
            "tier": "Popular literary teaching (not a primary academic source)",
            "items": [
                {"label": "Nouman Ali Khan / Bayyinah — Divine Speech (pedagogy of balāgha)", "url": "https://bayyinah.com/"},
            ],
        },
    ],
}


def topic() -> dict:
    return apply_overlays(DATA, {})
