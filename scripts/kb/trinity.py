# -*- coding: utf-8 -*-
"""Trinity vs Tawhid — which is more rational?"""

DATA = {
    "id": "trinity",
    "meta": {
        "title": "Trinity vs Tawhid: which is more rational?",
        "thesis": (
            "Given monotheism as the shared premise, is classical Trinitarian theism or "
            "Islamic tawhid the more coherent account of God's unity, self-knowledge, and worship?"
        ),
        "purpose": (
            "Steelman Nicene/Athanasian Trinity and Qur'anic/kalām tawhid; map definition traps, "
            "logical objections, and worship-practice implications. No declared winner."
        ),
        "warning": (
            "First 60 seconds: define 'person,' 'essence/ousia,' 'tawhid,' and 'shirk.' "
            "Most rounds collapse because one side attacks a caricature the other never held."
        ),
        "chips": ["theology", "logic", "definition", "worship", "kalām"],
        "labels": {"christian": "Christian / Trinitarian case", "muslim": "Muslim / Tawhid case"},
    },
    "definitions": [
        {
            "term": "Tawhid",
            "precise": (
                "Absolute oneness of God in essence, lordship, and exclusive right to worship; "
                "no partners, no partition of deity, no begotten divine Son."
            ),
            "not": "Not mere 'God is numerically one' as a slogan — includes worship exclusivity.",
        },
        {
            "term": "Trinity (classical)",
            "precise": (
                "One ousia/essence of God in three hypostases/persons (Father, Son, Spirit), "
                "coeternal, consubstantial; not three gods, not one person wearing three masks."
            ),
            "not": "Not modalism, Arian subordinationism, or 'three beings sharing a committee.'",
        },
        {
            "term": "Person / hypostasis",
            "precise": (
                "In patristic use: a distinct subsistence/relator within the one divine essence "
                "(who), not a separate finite center of consciousness in the modern psychological sense."
            ),
            "not": "Do not smuggle modern 'three people' into the debate without flagging it.",
        },
        {
            "term": "Shirk",
            "precise": "Associating partners with God in divinity, attributes, or worship.",
            "not": "Not every high Christology automatically equals pagan polytheism — argue the mapping.",
        },
        {
            "term": "Divine simplicity / attributes",
            "precise": (
                "Whether God's essence is identical with His attributes, and whether personal "
                "distinctions within God threaten that identity."
            ),
            "not": "Not a required opener, but it surfaces when 'parts in God' is alleged.",
        },
        {
            "term": "Begetting / generation",
            "precise": (
                "Eternal relation of Son from Father in Christian theology; not temporal birth "
                "or sexual generation. Qur'an rejects 'God begets' as creaturely category."
            ),
            "not": "Do not debate as if Christians mean God had a consort (Q 6:101 straw).",
        },
    ],
    "arguments": [
        {
            "id": "one-essence-three-persons",
            "rank": 1,
            "cluster": "Logic of unity",
            "title": "One essence / three persons is coherent monotheism",
            "type": "theology + logic",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Monotheism concerns how many divine beings/essences there are (one), not how many "
                    "personal relations subsist in that essence. Trinity is monotheism."
                ),
                "case": (
                    "Nicene Creed: one God; Son consubstantial with the Father. Athanasian Creed: "
                    "neither confounding persons nor dividing substance. Analytic defenses (e.g. Swinburne, "
                    "Leftow, Craig variants) treat 'person' as distinct from 'being.' Worship of Jesus is "
                    "worship of the one God, not a second deity."
                ),
                "sources": [
                    {"label": "Nicene Creed (USCCB)", "url": "https://www.usccb.org/prayers/nicene-creed"},
                    {"label": "Stanford Encyclopedia — Trinity", "url": "https://plato.stanford.edu/entries/trinity/"},
                    {"label": "Athanasian Creed text", "url": "https://www.ccel.org/ccel/schaff/creeds2.iv.i.iv.html"},
                ],
            },
            "muslim": {
                "claim": (
                    "If each person is fully God, thrice over, counting yields three divinities whatever "
                    "the 'essence' vocabulary; tawhid forbids partitioning deity into personal centers of worship."
                ),
                "case": (
                    "Qur'an 4:171; 5:73; 112. Kalām and later critiques (Ibn Taymiyya and others) press: "
                    "either the persons differ by something real — then composition — or they do not — then "
                    "verbal Trinity. Absolute unpartitioned oneness is the rational default of monotheism."
                ),
                "sources": [
                    {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
                    {"label": "Qur'an 112 (al-Ikhlas)", "url": "https://quran.com/112"},
                    {
                        "label": "Erickson — Islamic Monotheism and the Trinity",
                        "url": "https://uwaterloo.ca/grebel/sites/default/files/uploads/documents/cgr-27-1-w2009-4.pdf",
                    },
                ],
            },
            "counter_to_christian": "Essence-language can look like a semantic patch unless 'person' is defined non-tritheistically and non-modally in ordinary English.",
            "counter_to_muslim": "Critiques often target folk tritheism or Mary-as-third; Nicene orthodoxy is not 'third of three' as three gods.",
            "crux": "Is 'one being / three persons' still one God by the standards both sides accept for monotheism?",
            "debate_use": "Whiteboard two columns: Being vs Person. Force both speakers to use the same ontology.",
        },
        {
            "id": "quranic-polemic-target",
            "rank": 2,
            "cluster": "Definition / polemics",
            "title": "Does the Qur'an refute Nicene Trinity or a caricature?",
            "type": "definition + theology",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Key Qur'anic polemics (5:116; 'third of three') misdescribe orthodoxy; therefore Islam's "
                    "rational case against Trinity often hits the wrong target."
                ),
                "case": (
                    "5:116 has Jesus deny that he and Mary were taken as gods beside Allah — Mary is not "
                    "a Trinitarian person. 5:73's 'third of three' reads as tritheism. Christians argue "
                    "revelation that misses the creed cannot adjudicate it."
                ),
                "sources": [
                    {"label": "Qur'an 5:72–73", "url": "https://quran.com/5/72-73"},
                    {"label": "Qur'an 5:116", "url": "https://quran.com/5/116"},
                    {
                        "label": "Christian Century — Allah and the Trinity",
                        "url": "https://www.christiancentury.org/article/2011-02/allah-and-trinity",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Even granting Nicene formulas, ascribing deity and liturgical worship to Jesus is the "
                    "substance the Qur'an condemns; precise creedal jargon does not escape shirk."
                ),
                "case": (
                    "The Qur'an rejects saying 'Three,' divine sonship, and taking a messenger as Lord "
                    "(3:64; 9:31). Whether Mary appears in a polemical scene is secondary to the core: "
                    "no partner in ulūhiyya. Orthodoxy still worships Jesus."
                ),
                "sources": [
                    {"label": "Qur'an 3:64", "url": "https://quran.com/3/64"},
                    {"label": "Qur'an 9:31", "url": "https://quran.com/9/31"},
                    {"label": "Qur'an 5:72", "url": "https://quran.com/5/72"},
                ],
            },
            "counter_to_christian": "A misfire on Mary does not erase other verses against sonship and 'three.'",
            "counter_to_muslim": "If the Qur'an meant Nicene Trinity, why stage Mary as co-deity in 5:116?",
            "crux": "Is the rational dispute about creedal metaphysics or about whether Jesus may be worshipped?",
            "debate_use": "Ask: 'Name the doctrine you refute in one sentence a Nicene Christian would sign.'",
        },
        {
            "id": "divine-love-self",
            "rank": 3,
            "cluster": "Philosophical motives",
            "title": "God as love requires eternal interpersonal life",
            "type": "theology + philosophy",
            "popularity": "High",
            "christian": {
                "claim": (
                    "If God is essentially love (1 John 4:8), and love is interpersonal, then an eternally "
                    "solitary monad must create in order to love — making creation necessary. Trinity allows "
                    "eternal love without dependence on creatures."
                ),
                "case": (
                    "Augustine and later Richard of St. Victor style arguments: lover, beloved, love. "
                    "Swinburne develops social-Trinity versions. Rational theism prefers a God who is "
                    "complete without the world."
                ),
                "sources": [
                    {
                        "label": "1 John 4:8 (NRSVUE)",
                        "url": "https://www.biblegateway.com/passage/?search=1+John+4%3A8&version=NRSVUE",
                    },
                    {
                        "label": "SEP Trinity — Latin vs social models",
                        "url": "https://plato.stanford.edu/entries/trinity/",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "God's love and mercy do not require multiple divine persons; anthropomorphic psychology "
                    "of 'need for a beloved' projects creaturely lack onto God. Tawhid preserves aseity better."
                ),
                "case": (
                    "Allah is al-Wadūd, al-Raḥmān without eternal second persons. Love as will-to-good toward "
                    "creation is not loneliness. Social Trinity risks three centers — closer to tritheism."
                ),
                "sources": [
                    {"label": "Qur'an 11:90 (al-Wadūd)", "url": "https://quran.com/11/90"},
                    {"label": "Qur'an 85:14", "url": "https://quran.com/85/14"},
                ],
            },
            "counter_to_christian": "Equivocates on 'love'; divine love need not be the same genus as human interpersonal affection.",
            "counter_to_muslim": "If God is only related to creatures when they exist, eternal 'God is love' is harder to state.",
            "crux": "Must essential love be interpersonal among divine persons, or can it be dispositional/volitional in one subject?",
            "debate_use": "Press both sides to define 'love' before the aseity argument starts.",
        },
        {
            "id": "self-knowledge",
            "rank": 4,
            "cluster": "Philosophical motives",
            "title": "Divine self-knowledge and the Logos",
            "type": "philosophy + theology",
            "popularity": "Medium",
            "christian": {
                "claim": (
                    "Patristic/Augustinian models: the Son as Word/Image is God's perfect self-knowledge; "
                    "Spirit as love — giving Trinity explanatory depth for mind without parts."
                ),
                "case": (
                    "Psychological analogies (memory, understanding, will) attempt to show plurality of "
                    "relation without plurality of substance. John 1:1–18 funds Logos theology."
                ),
                "sources": [
                    {
                        "label": "John 1:1–14 (NRSVUE)",
                        "url": "https://www.biblegateway.com/passage/?search=John+1%3A1-14&version=NRSVUE",
                    },
                    {
                        "label": "Augustine, De Trinitate (overview)",
                        "url": "https://www.newadvent.org/fathers/1301.htm",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "God's knowledge is an attribute of the one essence; hypostasizing the Word into a second "
                    "person is unnecessary and risks eternal second deity (cf. debates with Christian kalām)."
                ),
                "case": (
                    "Ashʿarī/Māturīdī attribute discourse keeps kalām Allāh without a second god. Qur'an "
                    "calls Jesus a word from God (3:45; 4:171) without making the Word a co-eternal person."
                ),
                "sources": [
                    {"label": "Qur'an 3:45", "url": "https://quran.com/3/45"},
                    {"label": "Qur'an 4:171", "url": "https://quran.com/4/171", "note": "Word cast to Mary — messenger, not third of three."},
                ],
            },
            "counter_to_christian": "Psychological analogies are admitted by their authors to limp; they illustrate more than prove.",
            "counter_to_muslim": "Calling Jesus 'word' while denying Logos-personhood must explain John's worship-level claims.",
            "crux": "Is the Logos a second hypostasis or a non-personal divine attribute/act?",
            "debate_use": "Separate John 1 exegesis from pure philosophical motive arguments.",
        },
        {
            "id": "incarnation-coherence",
            "rank": 5,
            "cluster": "Christology load",
            "title": "Incarnation multiplies rational burden",
            "type": "theology + logic",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Chalcedonian two-natures Christology is demanding but coherent: one person, two natures; "
                    "mysteries are expected of the infinite. Rational theism can accept revealed paradox short of contradiction."
                ),
                "case": (
                    "Philippians 2; Chalcedon 451. Philosophers distinguish contradiction from above-reason "
                    "mystery. If Trinity is true, incarnation is its historical form."
                ),
                "sources": [
                    {
                        "label": "Philippians 2:5–11",
                        "url": "https://www.biblegateway.com/passage/?search=Philippians+2%3A5-11&version=NRSVUE",
                    },
                    {
                        "label": "Chalcedonian Definition",
                        "url": "https://www.earlychurchtexts.com/public/chalcedonian_definition.htm",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Combining full deity and full humanity in one person generates classic contradictions "
                    "(omniscience vs growth; immortality vs death). Tawhid plus a human Messiah is cleaner."
                ),
                "case": (
                    "Qur'an 5:75: Messiah ate food. 4:171 rejects excess. Rational preference for a doctrine "
                    "that does not require special pleading about kenosis, two minds, or reduplicative strategies."
                ),
                "sources": [
                    {"label": "Qur'an 5:75", "url": "https://quran.com/5/75"},
                    {"label": "Qur'an 19:30–35", "url": "https://quran.com/19/30-35"},
                    {"label": "SEP — Incarnation", "url": "https://plato.stanford.edu/entries/incarnation/"},
                ],
            },
            "counter_to_christian": "Mystery cannot be a blank check; show no formal contradiction.",
            "counter_to_muslim": "If God can create ex nihilo, why can't God personally unite a human nature?",
            "crux": "Is incarnation a mystery or a contradiction — and who bears the burden of proof?",
            "debate_use": "Force a formal contradiction claim onto the board before rhetoric about 'impossible.'",
        },
        {
            "id": "worship-practice",
            "rank": 6,
            "cluster": "Worship",
            "title": "Liturgical practice as rationality test",
            "type": "theology + ethics",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Earliest Christian practice worships Jesus (Phil 2; Rev 5; Pliny) while remaining "
                    "Jewish-rooted monotheists — evidence that Trinity tracks lived revelation, not later paganization alone."
                ),
                "case": (
                    "Hurtado/Bauckham: early high Christology. Rational religious epistemology may treat "
                    "apostolic worship pattern as data. Islam's later correction must outweigh that data."
                ),
                "sources": [
                    {
                        "label": "Revelation 5:11–14",
                        "url": "https://www.biblegateway.com/passage/?search=Revelation+5%3A11-14&version=NRSVUE",
                    },
                    {
                        "label": "Pliny to Trajan (Christians singing to Christ)",
                        "url": "https://www.earlychristianwritings.com/text/pliny.html",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Widespread practice can be sincere and still shirk; majority error is possible. "
                    "Rational worship is exclusive to the one God without a human recipient of latria."
                ),
                "case": (
                    "Qur'an diagnoses People of the Book taking rabbis/monks/Messiah as lords (9:31). "
                    "Jesus in Acts-style prayers does not license Nicene ontology if Jesus himself points away (Mark 12:29; John 17:3 as read by Muslims)."
                ),
                "sources": [
                    {"label": "Qur'an 9:31", "url": "https://quran.com/9/31"},
                    {
                        "label": "Mark 12:29; John 17:3",
                        "url": "https://www.biblegateway.com/passage/?search=Mark+12%3A29%3B+John+17%3A3&version=NRSVUE",
                    },
                ],
            },
            "counter_to_christian": "Early worship of Jesus is historical; whether it was intended as full deity is contested.",
            "counter_to_muslim": "If Jesus receives the worship due God in NT texts, Islamic unitarian Jesus must rewrite those texts.",
            "crux": "Does exclusive worship of one God forbid or include worship directed to Jesus as God the Son?",
            "debate_use": "Define latria vs hyperdulia; ask Muslims if any prayer to Jesus is shirk by definition.",
        },
        {
            "id": "occam",
            "rank": 7,
            "cluster": "Logic of unity",
            "title": "Occam: tawhid is simpler",
            "type": "logic",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Simplicity is not the only theoretical virtue; explanatory power regarding revelation, "
                    "atonement, and divine love can favor a more complex model if data require it."
                ),
                "case": (
                    "If Scripture teaches Father, Son, Spirit as divine, multiplying ontology is fidelity, "
                    "not extravagance. Unitarian simplicity that cannot integrate data is false economy."
                ),
                "sources": [
                    {
                        "label": "Matthew 28:19",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+28%3A19&version=NRSVUE",
                    },
                    {
                        "label": "2 Corinthians 13:13",
                        "url": "https://www.biblegateway.com/passage/?search=2+Corinthians+13%3A13&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "All else equal, a single personal God without hypostatic distinctions is the default "
                    "rational monotheism; Trinity adds entities beyond necessity."
                ),
                "case": (
                    "Qur'an 112 is maximal compression: One, eternal, neither begets nor is begotten, "
                    "none comparable. Philosophical monotheism (and Jewish unitarianism) share this default."
                ),
                "sources": [
                    {"label": "Qur'an 112", "url": "https://quran.com/112"},
                    {"label": "Qur'an 2:163", "url": "https://quran.com/2/163"},
                ],
            },
            "counter_to_christian": "You must show the data really require three persons, not proof-text clusters read through later creeds.",
            "counter_to_muslim": "Occam does not decide between rival revelations; it only ranks models after evidence is fixed.",
            "crux": "After fixing the scriptural/historical evidence set, which model is simpler without underfit?",
            "debate_use": "Agree on evidence set before saying 'simpler.'",
        },
        {
            "id": "begotten-not-made",
            "rank": 8,
            "cluster": "Sonship",
            "title": "Eternal generation vs 'God does not beget'",
            "type": "theology + definition",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "'Begotten not made' is eternal relational origin, not biological procreation; "
                    "Qur'anic rejection of begetting attacks a crude sense Christians also reject."
                ),
                "case": (
                    "Nicene: gennhthenta ou poiēthenta. John 1:14, 18; 3:16. Christians deny Allah took "
                    "a consort (Q 6:101) — shared rejection of pagan generation."
                ),
                "sources": [
                    {"label": "Nicene Creed", "url": "https://www.usccb.org/prayers/nicene-creed"},
                    {
                        "label": "John 1:14, 18",
                        "url": "https://www.biblegateway.com/passage/?search=John+1%3A14%2C18&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Any real 'sonship' in deity language still introduces a second who is from another; "
                    "Qur'an closes the category: lam yalid wa lam yūlad."
                ),
                "case": (
                    "Even metaphorical 'son of God' for Jesus becomes metaphysical in church dogma. "
                    "19:35; 112:3; 6:101. Rational speech about God avoids generative metaphors that mislead the masses."
                ),
                "sources": [
                    {"label": "Qur'an 112:3", "url": "https://quran.com/112"},
                    {"label": "Qur'an 19:35", "url": "https://quran.com/19/35"},
                    {"label": "Qur'an 6:101", "url": "https://quran.com/6/101"},
                ],
            },
            "counter_to_christian": "If 'beget' is utterly unlike creaturely begetting, why retain the word that invites misunderstanding?",
            "counter_to_muslim": "Hebrew/Greek 'son of God' idioms are broader; metaphysical reading is not the only option historically.",
            "crux": "Does eternal generation say something true and necessary, or is it a metaphor that tawhid rightly discards?",
            "debate_use": "Ban the word 'beget' for 5 minutes; force paraphrase — then restore and compare.",
        },
        {
            "id": "spirit-as-god",
            "rank": 9,
            "cluster": "Pneumatology",
            "title": "Holy Spirit: person of God or created force / angel?",
            "type": "theology",
            "popularity": "Medium-high",
            "christian": {
                "claim": (
                    "NT speech treats the Spirit as personal and divine (lying to Spirit = lying to God; "
                    "baptismal triad; Romans 8 intercession) — completing Trinity rather than dyad."
                ),
                "case": (
                    "Acts 5:3–4; Matt 28:19; John 14–16. Spirit is not an impersonal energy if He speaks, "
                    "wills, and is blasphemed against."
                ),
                "sources": [
                    {
                        "label": "Acts 5:3–4",
                        "url": "https://www.biblegateway.com/passage/?search=Acts+5%3A3-4&version=NRSVUE",
                    },
                    {
                        "label": "John 14:16–17, 26",
                        "url": "https://www.biblegateway.com/passage/?search=John+14%3A16-17%2C26&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Rūḥ in Qur'an is created agency (often linked to Gabriel or a spirit from God's command); "
                    "deifying Spirit is another form of association."
                ),
                "case": (
                    "17:85: little knowledge of the Spirit. 2:87; 16:102. Islamic angelology/spiritology "
                    "avoids a third uncreated person."
                ),
                "sources": [
                    {"label": "Qur'an 17:85", "url": "https://quran.com/17/85"},
                    {"label": "Qur'an 16:102", "url": "https://quran.com/16/102"},
                ],
            },
            "counter_to_christian": "Personality language can be literary; Jewish spirit-language is not automatically a third hypostasis.",
            "counter_to_muslim": "Christian claim is specifically about NT pneumatology, not Qur'anic rūḥ semantics alone.",
            "crux": "Is the Holy Spirit a distinct uncreated person or a created/functional reality?",
            "debate_use": "Don't let Trinity reduce to Father-Son only; ask for Spirit's status explicitly.",
        },
        {
            "id": "mystery-vs-clarity",
            "rank": 10,
            "cluster": "Epistemology",
            "title": "Mystery license vs rational clarity of tawhid",
            "type": "epistemology",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Finite minds should expect partial opacity about God's inner life; rejecting mystery "
                    "altogether is rationalism that would also gut creation ex nihilo and divine eternity."
                ),
                "case": (
                    "Deut 29:29; Romans 11:33. Creedal theology distinguishes paradox from nonsense. "
                    "Tawhid also has attribute debates (where/how God sits, uncreated Qur'an, etc.)."
                ),
                "sources": [
                    {
                        "label": "Romans 11:33–36",
                        "url": "https://www.biblegateway.com/passage/?search=Romans+11%3A33-36&version=NRSVUE",
                    },
                    {"label": "SEP Trinity", "url": "https://plato.stanford.edu/entries/trinity/"},
                ],
            },
            "muslim": {
                "claim": (
                    "Tawhid's public creed is teachable to a child without metaphysical special pleading; "
                    "a doctrine that needs centuries of councils to avoid heresy is rationally disadvantaged."
                ),
                "case": (
                    "112; 4:171. Fitrah monotheism. Historical explosion of Christological controversies "
                    "is presented as evidence of instability, not profundity."
                ),
                "sources": [
                    {"label": "Qur'an 30:30 (fitrah)", "url": "https://quran.com/30/30"},
                    {"label": "Qur'an 112", "url": "https://quran.com/112"},
                ],
            },
            "counter_to_christian": "Mystery after contradiction charges fail is fine; mystery instead of answering them is not.",
            "counter_to_muslim": "Ease of teaching ≠ truth; quantum physics is hard and still rational.",
            "crux": "When does 'mystery' become an illicit conversation-stopper?",
            "debate_use": "Agree: no side may say 'mystery' until they state what is *not* contradictory.",
        },
        {
            "id": "revelation-priority",
            "rank": 11,
            "cluster": "Epistemology",
            "title": "Whose revelation adjudicates rationality?",
            "type": "epistemology + theology",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "If Jesus is God's self-revelation, rationality includes submitting metaphysics to "
                    "that revelation; pure philosophical unitarianism is incomplete."
                ),
                "case": (
                    "Hebrews 1:1–3; John 14:9. Natural theology may get 'one God'; special revelation "
                    "discloses triune life. Islam's claim must defeat the apostolic witness first."
                ),
                "sources": [
                    {
                        "label": "Hebrews 1:1–3",
                        "url": "https://www.biblegateway.com/passage/?search=Hebrews+1%3A1-3&version=NRSVUE",
                    },
                    {
                        "label": "John 14:9",
                        "url": "https://www.biblegateway.com/passage/?search=John+14%3A9&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "If the Qur'an is God's final word correcting earlier communities, rationality includes "
                    "testing church dogma against that criterion; councils are not self-authenticating."
                ),
                "case": (
                    "5:48 muhaymin; 4:171. Prior books are affirmed in origin but not every later dogma. "
                    "Philosophical clarity of tawhid plus final revelation beats creedal complexity."
                ),
                "sources": [
                    {"label": "Qur'an 5:48", "url": "https://quran.com/5/48"},
                    {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
                ],
            },
            "counter_to_christian": "Assumes the deity of Christ to defend Trinity — circular if that is the dispute.",
            "counter_to_muslim": "Assumes Qur'anic authority to dismiss Trinity — circular in a comparative rationality debate.",
            "crux": "Can 'more rational' be judged by shared philosophical canons alone, or must revelation-claims be settled first?",
            "debate_use": "Split the round: (A) pure philosophy, (B) given Christian canon, (C) given Qur'an — score separately.",
        },
        {
            "id": "moral-worship-unity",
            "rank": 12,
            "cluster": "Worship",
            "title": "Practical monotheism and spiritual psychology",
            "type": "ethics + theology",
            "popularity": "Medium",
            "christian": {
                "claim": (
                    "Trinitarian worship forms a coherent spiritual economy (to the Father, through the Son, "
                    "in the Spirit) without dividing loyalty among gods."
                ),
                "case": (
                    "Liturgical doxologies and baptismal life are argued to deepen, not fracture, devotion. "
                    "Idolatry is worship of creatures as ultimate — Christ is not a creature in orthodoxy."
                ),
                "sources": [
                    {
                        "label": "Ephesians 2:18",
                        "url": "https://www.biblegateway.com/passage/?search=Ephesians+2%3A18&version=NRSVUE",
                    },
                    {
                        "label": "Catechism of the Catholic Church 232–267",
                        "url": "https://www.vatican.va/archive/ENG0015/__P17.HTM",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Tawhid trains the heart toward a single ultimate; multiple divine persons as worship-foci "
                    "predictably slides popular piety toward divided devotion and saint/Messiah excess."
                ),
                "case": (
                    "Historical Christian popular piety (and Qur'anic critique of taking partners) is cited "
                    "as empirical confirmation. Strict tawhid is spiritually safer."
                ),
                "sources": [
                    {"label": "Qur'an 39:3", "url": "https://quran.com/39/3"},
                    {"label": "Qur'an 17:22–23", "url": "https://quran.com/17/22-23"},
                ],
            },
            "counter_to_christian": "Official theology ≠ folk practice; evaluate the lived median, not the best catechism.",
            "counter_to_muslim": "Muslim folk practice also has saint-veneration controversies; knife cuts both ways.",
            "crux": "Should rationality of doctrine be scored by elite formulas or by typical worship patterns?",
            "debate_use": "Concede folk failures on both sides; return to official doctrine vs official doctrine.",
        },
    ],
    "materials": [],
    "debates": [
        {
            "id": "white-ally-trinity",
            "title": "Trinity debates (White / Ally circuit)",
            "year": None,
            "venue": "Multiple",
            "participants": ["James White", "Shabir Ally"],
            "sides": {"christian": "James White", "muslim": "Shabir Ally"},
            "motion": "Is the Trinity biblical / coherent vs Islamic tawhid?",
            "summary": (
                "White presses Greek NT grammar and early high Christology; Ally presses unitarian "
                "readings of Synoptics and Qur'anic clarity. Recurring fight: definition of monotheism."
            ),
            "what_to_steal": [
                "Never debate Trinity without defining person/essence",
                "Ask Ally-style: did Jesus preach Nicene Trinity?",
                "Ask White-style: is worship of Jesus idolatry if he is not God?",
            ],
            "links": [
                {
                    "label": "AOMIN debate archive hub",
                    "url": "https://www.aomin.org/",
                }
            ],
        },
        {
            "id": "qadhi-wood-style",
            "title": "Popular tawhid vs Trinity clash themes",
            "year": None,
            "venue": "Online / campus apologetics",
            "participants": ["Various"],
            "sides": {"christian": "Evangelical apologists", "muslim": "Dawah speakers"},
            "motion": "Whose monotheism is true?",
            "summary": (
                "Street-level pattern: Christians accuse Qur'an of straw-manning; Muslims accuse Christians "
                "of verbal monotheism with practical polytheism."
            ),
            "what_to_steal": ["Steelman the other side's best philosopher, not their worst clip."],
            "links": [
                {"label": "SEP Trinity", "url": "https://plato.stanford.edu/entries/trinity/"},
                {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
            ],
        },
    ],
    "opponent_cards": [
        {
            "trigger": "Christians worship three gods",
            "fast_answer": "Orthodoxy: one essence, three persons. Tritheism is a heresy Christians also condemn. Ask for their definition of 'god' and 'person.'",
            "follow_up": "Then ask whether worship of Jesus is worship of that one essence.",
            "sources": ["Nicene Creed", "SEP Trinity", "Athanasian Creed"],
        },
        {
            "trigger": "The Qur'an refutes the Trinity in 5:116",
            "fast_answer": "5:116 names Jesus and Mary as gods beside Allah — Mary is not a Trinitarian person. Press target accuracy.",
            "follow_up": "Grant that 4:171 still rejects 'three' and sonship; fight the real claim.",
            "sources": ["https://quran.com/5/116", "https://quran.com/4/171"],
        },
        {
            "trigger": "1+1+1=3, so Trinity is illogical",
            "fast_answer": "Christians don't claim three essences. Arithmetic of persons ≠ arithmetic of beings. Demand isomorphic counting rules.",
            "follow_up": "Offer: three persons, one being — then attack/defend that ontology.",
            "sources": ["SEP Trinity"],
        },
        {
            "trigger": "God begetting is pagan",
            "fast_answer": "Eternal generation ≠ sexual procreation. Christians reject Q 6:101's consort picture too.",
            "follow_up": "Ask Muslim: is any use of 'ibn' for Jesus shirk, including metaphorical?",
            "sources": ["Nicene Creed", "https://quran.com/6/101"],
        },
        {
            "trigger": "John 17:3 — Father is the only true God",
            "fast_answer": "Christians read this as economic monotheism / against idols, not as Arian denial of the Son's deity; pair with John 1:1; 20:28.",
            "follow_up": "Ask how Thomas's 'my God' fits a purely unitarian Jesus.",
            "sources": [
                "https://www.biblegateway.com/passage/?search=John+17%3A3%3B+John+20%3A28&version=NRSVUE"
            ],
        },
        {
            "trigger": "Trinity was invented at Nicaea",
            "fast_answer": "Nicaea dogmatized language under conflict; high Christology and triad formulas predate 325. Invention ≠ first creed.",
            "follow_up": "Distinguish development of wording from creation of Jesus-worship ex nihilo.",
            "sources": ["Hurtado summaries", "Philippians 2", "Matthew 28:19"],
        },
        {
            "trigger": "Tawhid is just simpler, so true",
            "fast_answer": "Simplicity is a tie-breaker after evidence, not a trump against revelation claims.",
            "follow_up": "Ask what evidence set we're simplifying over.",
            "sources": ["Philosophy of religion primers on theoretical virtues"],
        },
        {
            "trigger": "If Jesus prayed to the Father he isn't God",
            "fast_answer": "Incarnation: the Son as man prays. Challenge assumes unitarian Christology.",
            "follow_up": "Ask whether any two-natures model could make sense of Gethsemane.",
            "sources": ["Chalcedon", "https://plato.stanford.edu/entries/incarnation/"],
        },
        {
            "trigger": "Christians associate partners — shirk",
            "fast_answer": "By Islamic definition maybe; by Christian definition, worshipping Jesus is worshipping God. The dispute is the definition.",
            "follow_up": "Don't fight the Arabic word; fight whether Jesus is created.",
            "sources": ["https://quran.com/4/48", "Nicene Creed"],
        },
        {
            "trigger": "Three persons means three wills / three gods",
            "fast_answer": "Classical Latin models stress one divine will/operation; social models differ — ask which Christian model they attack.",
            "follow_up": "Don't defend the weakest social-tritheist YouTube version.",
            "sources": ["SEP Trinity — Latin/social"],
        },
        {
            "trigger": "Islam copied Jewish pure monotheism; Christianity paganized it",
            "fast_answer": "Second Temple Judaism is more complex (Word, Wisdom, exalted agents). Still not Nicene Trinity — but 'paganization' is too neat.",
            "follow_up": "Bring the debate back to Jesus' status in earliest sources.",
            "sources": ["Bauckham/Hurtado discussions", "SEP"],
        },
        {
            "trigger": "Mystery is a cop-out",
            "fast_answer": "Agree if used to hide contradiction. Distinguish: unknown how vs known impossible.",
            "follow_up": "Make opponent state the formal contradiction in logic symbols if they can.",
            "sources": ["SEP Trinity / Incarnation"],
        },
    ],
    "checklist": [
        "Open with definitions: essence, person, tawhid, shirk (60–90 seconds)",
        "State whether tonight's standard is pure philosophy, Christian canon, or Qur'an",
        "Steelman Nicene Trinity in one sentence a Muslim would recognize as fair",
        "Steelman tawhid in one sentence a Nicene Christian would recognize as fair",
        "Prepare 5:116 Mary-target jab and the Muslim 'worship is the point' reply",
        "Master 3 Christian texts (Matt 28:19; John 1:1; Phil 2) and 3 Qur'anic (4:171; 5:73; 112)",
        "Decide your concession: what folk Christian talk you will grant as confused",
        "Decide your concession: what Qur'anic polemic you will grant as not Nicene-precise",
        "Drill opponent cards out loud; first sentence must be usable live",
        "Prepare whiteboard: Being vs Person; Love argument; Occam vs data",
        "Closing: restate crux questions, not slogans about 'pagan' or 'three gods'",
        "Bring printed Nicene lines + Q 4:171 + SEP Trinity URL on paper",
    ],
    "positive_cases": {
        "Christian podium": [
            "One divine essence; personal distinctions without tritheism (Nicene/Athanasian)",
            "Apostolic-era worship of Jesus + Spirit language requires more than bare philosophical unitarianism",
            "Trinity explains eternal love/self-knowledge without making creation necessary",
            "Qur'anic polemics often miss Nicene orthodoxy; fight the real doctrine",
        ],
        "Muslim podium": [
            "Unpartitioned oneness (112; 4:171) is the clear rational default of monotheism",
            "Worship of a man (however exalted) is the substance of shirk regardless of essence-talk",
            "Incarnation + eternal generation add mysteries that look like contradictions",
            "Fitrah-accessible creed without councils is an epistemic virtue",
        ],
        "Unity / steelman": [
            "Both sides affirm one Creator and reject pagan pantheons — locate the real fork",
            "Ban straw men: no 'Christians think Mary is God' and no 'Muslims worship a distant tyrant'",
            "Separate philosophical monotheism from historical claims about Jesus",
            "Use academic philosophy (SEP) plus primary texts, not only polemical clips",
        ],
    },
    "bibliography": [
        {
            "tier": "Must-read academic / reference",
            "items": [
                {"label": "Stanford Encyclopedia — Trinity", "url": "https://plato.stanford.edu/entries/trinity/"},
                {"label": "Stanford Encyclopedia — Incarnation", "url": "https://plato.stanford.edu/entries/incarnation/"},
                {"label": "Erickson PDF — Islamic Monotheism and the Trinity", "url": "https://uwaterloo.ca/grebel/sites/default/files/uploads/documents/cgr-27-1-w2009-4.pdf"},
                {"label": "CCC on the Trinity (Vatican)", "url": "https://www.vatican.va/archive/ENG0015/__P17.HTM"},
            ],
        },
        {
            "tier": "Primary texts",
            "items": [
                {"label": "Nicene Creed", "url": "https://www.usccb.org/prayers/nicene-creed"},
                {"label": "Qur'an 4:171; 5:72–73; 5:116; 112", "url": "https://quran.com/4/171"},
                {"label": "John 1; Philippians 2; Matthew 28:19", "url": "https://www.biblegateway.com/passage/?search=John+1%3A1-18&version=NRSVUE"},
            ],
        },
        {
            "tier": "Debate / apologetic",
            "items": [
                {"label": "Christian Century — Allah and the Trinity", "url": "https://www.christiancentury.org/article/2011-02/allah-and-trinity"},
                {"label": "Early Church Texts — Chalcedon", "url": "https://www.earlychurchtexts.com/public/chalcedonian_definition.htm"},
            ],
        },
    ],
}


def topic():
    from .deepen_lib import apply_overlays
    from .trinity_deep import OVERLAYS
    return apply_overlays(DATA, OVERLAYS)
