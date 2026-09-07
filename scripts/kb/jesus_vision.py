# -*- coding: utf-8 -*-
"""Whose vision of Jesus is better — rationally and historically?"""

DATA = {
    "id": "jesus-vision",
    "meta": {
        "title": "Whose vision of Jesus is better — rationally and historically?",
        "thesis": (
            "Comparing the Christian vision (incarnate Son, crucified and risen Lord) with the Islamic vision "
            "(exalted human Messiah-prophet), which is more coherent rationally and better grounded historically?"
        ),
        "purpose": (
            "Integrate identity, history, and worship: not only 'did he die?' but 'what must Jesus be "
            "for the story to make sense?' Steelman both portraits as live religious options."
        ),
        "warning": (
            "This overlaps Trinity, historical Jesus, and morality dossiers. Lead with the vision "
            "(who Jesus is and why it matters), then pull receipts. Don't get lost in only 4:157."
        ),
        "chips": ["Jesus", "Christology", "history", "rationality", "worship"],
        "labels": {"christian": "Christian vision", "muslim": "Muslim vision"},
    },
    "definitions": [
        {
            "term": "Christian vision of Jesus",
            "precise": (
                "Eternal Son incarnate, truly God and truly man, crucified for sins, risen, worthy of worship, "
                "returning as judge — with denominational nuances."
            ),
            "not": "Not every modern liberal Protestant minimization.",
        },
        {
            "term": "Islamic vision of Jesus (ʿĪsā)",
            "precise": (
                "Virgin-born Messiah, prophet, word from God, worker of signs by permission, not divine, "
                "not crucified (per majority reading), returning before the Hour in many traditions."
            ),
            "not": "Not a denial that Jesus matters — Islam gives him high honor without deity.",
        },
        {
            "term": "Rational coherence",
            "precise": "Internal consistency of the portrait with monotheism, justice, and Jesus' own role.",
            "not": "Not 'sounds familiar to my culture.'",
        },
        {
            "term": "Historical grounding",
            "precise": "Fit with earliest recoverable data about Jesus and his movement.",
            "not": "Not popularity or later empire success.",
        },
        {
            "term": "Worship-worthiness",
            "precise": "Whether Jesus is a proper recipient of latria/devotion due to God alone.",
            "not": "Not whether Jesus is respected as prophet.",
        },
        {
            "term": "Kenosis / two natures",
            "precise": "Christian strategies for incarnation coherence (self-emptying; Chalcedonian natures).",
            "not": "Not required vocabulary for Muslims — but Christians must be ready to explain.",
        },
    ],
    "arguments": [
        {
            "id": "portrait-fit-history",
            "rank": 1,
            "cluster": "History",
            "title": "Which portrait fits earliest data better?",
            "type": "history",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Earliest sources show a crucified Messiah proclaimed risen and worshipped — "
                    "the Christian vision is the organic development of that data; the Islamic vision truncates it."
                ),
                "case": (
                    "1 Cor 15; Phil 2; Synoptic passion. A prophet who didn't die under Pilate fails "
                    "the first historical filter."
                ),
                "sources": [
                    {
                        "label": "1 Corinthians 15:3–8",
                        "url": "https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A3-8&version=NRSVUE",
                    },
                    {
                        "label": "Philippians 2:6–11",
                        "url": "https://www.biblegateway.com/passage/?search=Philippians+2%3A6-11&version=NRSVUE",
                    },
                    {
                        "label": "Ehrman on crucifixion certainty",
                        "url": "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Earliest recoverable Jesus is a Jewish monotheist prophet — the Islamic vision "
                    "preserves that core while Christian vision inflates post-Easter metaphysics."
                ),
                "case": (
                    "Shema affirmation; prophet-in-Israel paradigm; critical dating of high Johannine discourse."
                ),
                "sources": [
                    {
                        "label": "Mark 12:29",
                        "url": "https://www.biblegateway.com/passage/?search=Mark+12%3A29&version=NRSVUE",
                    },
                    {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
                    {"label": "Qur'an 3:49–51", "url": "https://quran.com/3/49-51"},
                ],
            },
            "counter_to_christian": "Organic development can still be wrong development.",
            "counter_to_muslim": "If you grant critical tools, crucifixion usually comes with the 'prophet' core.",
            "crux": "Is the passion-kerygma historical bedrock or theological overwrite?",
            "debate_use": "Start with a 60-second 'earliest data' dump both must answer.",
        },
        {
            "id": "monotheism-fit",
            "rank": 2,
            "cluster": "Rationality",
            "title": "Fit with monotheism",
            "type": "theology + logic",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Incarnational monotheism (one essence) rationally allows Jesus' worship without "
                    "second god; the vision solves how God reveals Himself personally."
                ),
                "case": (
                    "John 1; Hebrews 1. Trinity dossier applies; here stress Jesus as God's self-word."
                ),
                "sources": [
                    {
                        "label": "John 1:1–18",
                        "url": "https://www.biblegateway.com/passage/?search=John+1%3A1-18&version=NRSVUE",
                    },
                    {
                        "label": "SEP Trinity",
                        "url": "https://plato.stanford.edu/entries/trinity/",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "The Islamic vision is the clean monotheistic portrait: exalted servant, never God. "
                    "Christian vision multiplies rational burdens (Trinity + incarnation)."
                ),
                "case": (
                    "112; 4:171; 5:75. Occam + tawhid: honor Jesus without ontological confusion."
                ),
                "sources": [
                    {"label": "Qur'an 112", "url": "https://quran.com/112"},
                    {"label": "Qur'an 5:75", "url": "https://quran.com/5/75"},
                    {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
                ],
            },
            "counter_to_christian": "Identity theories of incarnation remain philosophically costly.",
            "counter_to_muslim": "Cleanliness that underfits historical worship data may be false economy.",
            "crux": "Prefer simpler monotheism or data-fitting incarnational monotheism?",
            "debate_use": "Score 'simplicity' and 'data fit' as separate numbers.",
        },
        {
            "id": "moral-meaning-cross",
            "rank": 3,
            "cluster": "Rationality",
            "title": "Moral meaning of the cross vs denial",
            "type": "theology + ethics",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "A crucified God-with-us uniquely discloses divine love and justice; "
                    "denying the cross removes the Christian vision's moral center."
                ),
                "case": (
                    "Romans 5:8; 1 Cor 1:18–25. The scandal is the point — wisdom through apparent weakness."
                ),
                "sources": [
                    {
                        "label": "Romans 5:6–11",
                        "url": "https://www.biblegateway.com/passage/?search=Romans+5%3A6-11&version=NRSVUE",
                    },
                    {
                        "label": "1 Corinthians 1:18–25",
                        "url": "https://www.biblegateway.com/passage/?search=1+Corinthians+1%3A18-25&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "God's rescue of His prophet (4:157–158) better fits divine justice than "
                    "orchestrating the killing of His son; mercy does not need blood."
                ),
                "case": (
                    "39:53; 4:157. Vicarious punishment is the rational scandal Muslims refuse."
                ),
                "sources": [
                    {"label": "Qur'an 4:157–158", "url": "https://quran.com/4/157-158"},
                    {"label": "Qur'an 39:53", "url": "https://quran.com/39/53"},
                ],
            },
            "counter_to_christian": "Love could be shown without penal mechanisms — argue necessity.",
            "counter_to_muslim": "If the movement's center was cross-proclamation, rescue-without-death must explain Christian origins.",
            "crux": "Is the cross a moral necessity of love/justice or a moral impossibility for God?",
            "debate_use": "Define 'necessity' — metaphysical, narrative, or pastoral.",
        },
        {
            "id": "word-spirit-titles",
            "rank": 4,
            "cluster": "Shared honors",
            "title": "Shared high titles: word, spirit, messiah",
            "type": "theology",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Qur'anic high titles for Jesus (word, spirit) unstablely sit beside denial of deity; "
                    "Christian vision integrates those honors coherently in Logos Christology."
                ),
                "case": (
                    "4:171 names; John 1 integrates. Muslims must explain why 'word' isn't personal Logos."
                ),
                "sources": [
                    {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
                    {
                        "label": "John 1:1–14",
                        "url": "https://www.biblegateway.com/passage/?search=John+1%3A1-14&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Titles are honorific/creational agency, not ontology; Christian integration "
                    "over-reads Semitic speech into Greek hypostases."
                ),
                "case": (
                    "3:45; 4:171. 'Word cast to Mary' = creative kun command, not second person of Trinity."
                ),
                "sources": [
                    {"label": "Qur'an 3:45", "url": "https://quran.com/3/45"},
                    {"label": "Qur'an 3:59 (Adam analogy)", "url": "https://quran.com/3/59"},
                ],
            },
            "counter_to_christian": "Lexical overlap ≠ conceptual identity across languages/centuries.",
            "counter_to_muslim": "If titles are so high, the worship boundary needs clear principled line.",
            "crux": "Do shared titles favor Christian integration or Islamic non-ontological honor?",
            "debate_use": "Ban the word 'clearly' for this argument — only parse.",
        },
        {
            "id": "virgin-birth",
            "rank": 5,
            "cluster": "Shared honors",
            "title": "Virgin birth: shared sign, divergent meaning",
            "type": "theology + history",
            "popularity": "Medium-high",
            "christian": {
                "claim": (
                    "Virgin birth signals unique Sonship and new-creation Adam typology; "
                    "Islam keeps the sign while rejecting the meaning Christians take it to carry."
                ),
                "case": (
                    "Luke 1; Matt 1. Shared supernatural origin increases pressure on 'mere prophet' minimalism."
                ),
                "sources": [
                    {
                        "label": "Luke 1:26–35",
                        "url": "https://www.biblegateway.com/passage/?search=Luke+1%3A26-35&version=NRSVUE",
                    },
                    {"label": "Qur'an 19:16–22", "url": "https://quran.com/19/16-22"},
                ],
            },
            "muslim": {
                "claim": (
                    "3:59 — Jesus like Adam: created by command; virgin birth shows God's power, not deity of the child."
                ),
                "case": (
                    "Adam had no parents; Jesus' miraculous birth is not a Trinity argument."
                ),
                "sources": [
                    {"label": "Qur'an 3:59", "url": "https://quran.com/3/59"},
                    {"label": "Qur'an 19:35", "url": "https://quran.com/19/35"},
                ],
            },
            "counter_to_christian": "Adam typology can cut Islamic direction too.",
            "counter_to_muslim": "Christians don't argue virgin birth alone proves deity — it coheres in a larger pattern.",
            "crux": "Is virgin birth a sign of unique incarnation or of creative power only?",
            "debate_use": "Treat as supporting argument, not the main hinge.",
        },
        {
            "id": "second-coming",
            "rank": 6,
            "cluster": "Eschatology",
            "title": "Return of Jesus in both visions",
            "type": "theology",
            "popularity": "Medium-high",
            "christian": {
                "claim": (
                    "Jesus' return as judge fits the Christian vision of cosmic Lordship; "
                    "Islamic second-coming traditions implicitly concede extraordinary eschatological status."
                ),
                "case": (
                    "Acts 1:11; Matt 25. Muslim hadith eschatology of Jesus' return is a pressure point on 'only prophet' rhetoric."
                ),
                "sources": [
                    {
                        "label": "Acts 1:9–11",
                        "url": "https://www.biblegateway.com/passage/?search=Acts+1%3A9-11&version=NRSVUE",
                    },
                    {
                        "label": "Matthew 25:31–46",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+25%3A31-46&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Jesus' return (in hadith-based eschatology) is as a follower of Muhammad's sharīʿa, "
                    "breaking the cross — confirming Islam's vision, not Nicene Lordship."
                ),
                "case": (
                    "Popular Muslim eschatology: Jesus denies Christian exaggeration. "
                    "Qur'anic base is thinner; be honest about hadith weight."
                ),
                "sources": [
                    {"label": "Qur'an 43:61 (contested eschatological reading)", "url": "https://quran.com/43/61"},
                    {
                        "label": "Sahih Muslim 2897 (Jesus return themes — check numbering/collections)",
                        "url": "https://sunnah.com/muslim",
                    },
                ],
            },
            "counter_to_christian": "Hadith eschatology isn't Nicene Christology; don't over-claim.",
            "counter_to_muslim": "Why does history culminate with Jesus' return if Muhammad is the seal in all senses?",
            "crux": "Does eschatological Jesus support Christian cosmic Lordship or Islamic finality of Muhammad?",
            "debate_use": "Separate Qur'an-only from hadith-eschatology layers.",
        },
        {
            "id": "prayer-worship",
            "rank": 7,
            "cluster": "Worship",
            "title": "Do you pray to Jesus?",
            "type": "theology + practice",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "New Testament pattern includes prayer/invocation directed to Jesus; "
                    "the vision requires worship. If Jesus is only a prophet, Christian liturgy is idolatry — the stakes are real."
                ),
                "case": (
                    "Acts 7:59; 1 Cor 1:2; Rev 5. Rationally: either Christians are deeply wrong or Muslims under-rank Jesus."
                ),
                "sources": [
                    {
                        "label": "Acts 7:59–60",
                        "url": "https://www.biblegateway.com/passage/?search=Acts+7%3A59-60&version=NRSVUE",
                    },
                    {
                        "label": "Revelation 5:11–14",
                        "url": "https://www.biblegateway.com/passage/?search=Revelation+5%3A11-14&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Prayer to Jesus is the error the Qur'an corrects; true followers of Jesus prayed to the Father alone."
                ),
                "case": (
                    "5:116–117; John 17:3 as unitarian proof-text. Islamic vision protects worship."
                ),
                "sources": [
                    {"label": "Qur'an 5:116–117", "url": "https://quran.com/5/116-117"},
                    {
                        "label": "John 17:3",
                        "url": "https://www.biblegateway.com/passage/?search=John+17%3A3&version=NRSVUE",
                    },
                ],
            },
            "counter_to_christian": "Later liturgical development ≠ Jesus' own teaching on prayer (Lord's Prayer to Father).",
            "counter_to_muslim": "If earliest Christians invoked Jesus, Islamic correction must indict apostolic practice, not only councils.",
            "crux": "Is invoking Jesus required fidelity or defining idolatry?",
            "debate_use": "Ask both speakers to answer yes/no: may a Christian say 'Lord Jesus, have mercy'?",
        },
        {
            "id": "salvation-role",
            "rank": 8,
            "cluster": "Soteriology",
            "title": "Jesus' role in salvation",
            "type": "theology",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Jesus is not only teacher but Savior; the vision stands or falls on unique mediation "
                    "(John 14:6; Acts 4:12)."
                ),
                "case": (
                    "Without unique saving death/resurrection, Jesus becomes one prophet among many — "
                    "a different religion."
                ),
                "sources": [
                    {
                        "label": "John 14:6",
                        "url": "https://www.biblegateway.com/passage/?search=John+14%3A6&version=NRSVUE",
                    },
                    {
                        "label": "Acts 4:12",
                        "url": "https://www.biblegateway.com/passage/?search=Acts+4%3A12&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Jesus saves as prophet by guiding to tawhid; God alone forgives. "
                    "Unique mediation of a God-man is unnecessary and unjust."
                ),
                "case": (
                    "3:51; 19:36; 39:53. The Islamic vision keeps Savior-language for God."
                ),
                "sources": [
                    {"label": "Qur'an 3:51", "url": "https://quran.com/3/51"},
                    {"label": "Qur'an 39:53", "url": "https://quran.com/39/53"},
                ],
            },
            "counter_to_christian": "Exclusivism must face the sincere-outsider problem.",
            "counter_to_muslim": "Guidance-only Jesus undercuts the urgency and content of apostolic preaching.",
            "crux": "Is Jesus Savior in a unique mediatorial sense, or messenger of the Savior-God?",
            "debate_use": "Force a one-sentence soteriology from each side.",
        },
        {
            "id": "injeel-content",
            "rank": 9,
            "cluster": "History",
            "title": "What was the Injīl?",
            "type": "definition + history",
            "popularity": "High",
            "christian": {
                "claim": (
                    "If Injīl means the Gospel about Jesus' death and resurrection, Islam's affirmation "
                    "of Injīl collides with its Christology; if not, 'Gospel' is equivocal."
                ),
                "case": (
                    "Islamic dilemma adjacent: 5:46–47. Christian vision claims continuity with apostolic gospel."
                ),
                "sources": [
                    {"label": "Qur'an 5:46–47", "url": "https://quran.com/5/46-47"},
                    {
                        "label": "1 Corinthians 15:1–5 (Paul's gospel summary)",
                        "url": "https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A1-5&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Injīl is revelation given to Jesus, not identical to four canonical biographies "
                    "with Pauline theology; Christian vision confuses later texts with Jesus' Gospel."
                ),
                "case": (
                    "5:46; tahrif debates. Rational: judge Jesus by Jesus' message, not church canon alone."
                ),
                "sources": [
                    {"label": "Qur'an 5:46", "url": "https://quran.com/5/46"},
                    {
                        "label": "Saeed — Charge of Distortion (PDF gateway)",
                        "url": "https://bible-quran-video.s3.amazonaws.com/Documents/The-Charge-of-Distortion-of-Jewish-and-Christian-Scriptures_Abdullah+Saeed.pdf",
                    },
                ],
            },
            "counter_to_christian": "Equating Injīl with the fourfold canon begs the question.",
            "counter_to_muslim": "A free-floating Injīl without recoverable content is hard to follow historically.",
            "crux": "What publicly recoverable content counts as Jesus' Gospel?",
            "debate_use": "Define Injīl before any dilemma or corruption argument.",
        },
        {
            "id": "prophet-succession",
            "rank": 10,
            "cluster": "Prophetic frame",
            "title": "Finality: Jesus vs Muhammad as hermeneutical key",
            "type": "theology + rationality",
            "popularity": "High",
            "christian": {
                "claim": (
                    "If Jesus is God's final and personal revelation (Heb 1:1–3), later contradictory "
                    "claims about him are rationally secondary."
                ),
                "case": (
                    "Christians argue the best vision of Jesus cannot be adjudicated by a later prophet "
                    "who denies the passion center."
                ),
                "sources": [
                    {
                        "label": "Hebrews 1:1–3",
                        "url": "https://www.biblegateway.com/passage/?search=Hebrews+1%3A1-3&version=NRSVUE",
                    },
                    {
                        "label": "Jude 3",
                        "url": "https://www.biblegateway.com/passage/?search=Jude+1%3A3&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "God's final revelation (Qur'an) clarifies disputes among People of the Book; "
                    "rational humility accepts correction of earlier communities' excess about Jesus."
                ),
                "case": (
                    "5:48; 4:171. Seal of prophets frame (33:40) includes correcting Christology."
                ),
                "sources": [
                    {"label": "Qur'an 5:48", "url": "https://quran.com/5/48"},
                    {"label": "Qur'an 33:40", "url": "https://quran.com/33/40"},
                    {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
                ],
            },
            "counter_to_christian": "Hebrews' finality is itself a faith claim inside the Christian canon.",
            "counter_to_muslim": "Finality claims can't skip historical confrontation with 1st-c. sources.",
            "crux": "Who has standing to give the definitive vision of Jesus — apostolic witnesses or the Qur'an?",
            "debate_use": "This is often the real meta-debate — surface it early.",
        },
        {
            "id": "humanity-full",
            "rank": 11,
            "cluster": "Rationality",
            "title": "Full humanity without docetism",
            "type": "theology",
            "popularity": "Medium",
            "christian": {
                "claim": (
                    "Chalcedonian vision insists on full humanity (hunger, grief, death) against docetism; "
                    "some Islamic substitution readings risk appearing docetic about the cross event."
                ),
                "case": (
                    "Hebrews 2:14–18; John 11:35. Real incarnation requires real death for real solidarity."
                ),
                "sources": [
                    {
                        "label": "Hebrews 2:14–18",
                        "url": "https://www.biblegateway.com/passage/?search=Hebrews+2%3A14-18&version=NRSVUE",
                    },
                    {
                        "label": "Chalcedonian Definition",
                        "url": "https://www.earlychurchtexts.com/public/chalcedonian_definition.htm",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Qur'an stresses Jesus' full creaturely humanity (eats food) precisely against deification; "
                    "denying crucifixion is not docetism about his life but about his enemies' victory."
                ),
                "case": (
                    "5:75; 19:30–33. Islamic vision blocks both Arian and Nicene errors by different means."
                ),
                "sources": [
                    {"label": "Qur'an 5:75", "url": "https://quran.com/5/75"},
                    {"label": "Qur'an 19:30–33", "url": "https://quran.com/19/30-33"},
                ],
            },
            "counter_to_christian": "Two-natures itself risks conceptual docetism if divinity swallows humanity.",
            "counter_to_muslim": "Substitution theories historically often look docetic about the one on the cross.",
            "crux": "Which vision better secures that the real Jesus suffered history's violence?",
            "debate_use": "Ask: who suffered on the cross, if anyone?",
        },
        {
            "id": "transformative-power",
            "rank": 12,
            "cluster": "Existential",
            "title": "Existential / transformative adequacy",
            "type": "ethics + theology",
            "popularity": "Medium",
            "christian": {
                "claim": (
                    "The Christian vision offers personal union with God in Christ and liberation from "
                    "guilt via the cross — existentially thicker than prophet-veneration alone."
                ),
                "case": (
                    "Galatians 2:20; Romans 8. Rational evaluation of a vision includes what it does in moral psychology."
                ),
                "sources": [
                    {
                        "label": "Galatians 2:20",
                        "url": "https://www.biblegateway.com/passage/?search=Galatians+2%3A20&version=NRSVUE",
                    },
                    {
                        "label": "Romans 8:1–4",
                        "url": "https://www.biblegateway.com/passage/?search=Romans+8%3A1-4&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Islamic vision yields ʿubūdiyya without idolatry anxiety: love and follow Jesus "
                    "while worshipping God alone — spiritually safer and clearer."
                ),
                "case": (
                    "3:51; 112. Transformation via tawba, ṣalāh, and following prophets without confusing Creator/creature."
                ),
                "sources": [
                    {"label": "Qur'an 3:51", "url": "https://quran.com/3/51"},
                    {"label": "Qur'an 112", "url": "https://quran.com/112"},
                ],
            },
            "counter_to_christian": "Existential thickness can be psychologically powerful and still false.",
            "counter_to_muslim": "Clarity can be existentially thin if it misses the movement's cross-shaped core.",
            "crux": "Should existential adequacy count heavily, or only as a tiebreaker after history/logic?",
            "debate_use": "Weight this argument last; don't let testimony replace history.",
        },
    ],
    "materials": [],
    "debates": [
        {
            "id": "ally-vs-christian-jesus-nature",
            "title": "Nature / identity of Jesus debates",
            "year": None,
            "venue": "Public circuit",
            "participants": ["Shabir Ally", "Christian apologists"],
            "sides": {"christian": "Divine incarnate Lord", "muslim": "Human Messiah-prophet"},
            "motion": "Is Jesus God? / Which Christology?",
            "summary": (
                "Standard pattern: Synoptic unitarian readings vs early worship + John + creed; "
                "crucifixion returns as historical veto."
            ),
            "what_to_steal": [
                "Define vision before verse tennis",
                "Ask what would falsify each vision",
            ],
            "links": [
                {"label": "SEP Trinity", "url": "https://plato.stanford.edu/entries/trinity/"},
                {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
            ],
        }
    ],
    "opponent_cards": [
        {
            "trigger": "We Muslims love Jesus more — we mention him respectfully",
            "fast_answer": "Honor is real in the Qur'an. The dispute is identity and cross, not courtesy titles.",
            "follow_up": "Ask whether praying to Jesus is shirk by definition.",
            "sources": ["https://quran.com/4/171", "Acts 7:59"],
        },
        {
            "trigger": "Christians worship a man",
            "fast_answer": "On Christian vision, they worship God the Son incarnate — not a mere man. State the ontology.",
            "follow_up": "Then fight whether that ontology is true.",
            "sources": ["Nicene Creed", "John 1"],
        },
        {
            "trigger": "Jesus prophesied Muhammad (61:6)",
            "fast_answer": "That's an Islamic claim about Injīl content. Historically, recover it in 1st-c. sources or concede it's revelation-only.",
            "follow_up": "Don't let it derail crucifixion/identity.",
            "sources": ["https://quran.com/61/6", "John 14–16 Paraclete debates"],
        },
        {
            "trigger": "The Bible is corrupted so only the Qur'an shows the real Jesus",
            "fast_answer": "Specify what kind of tahrif. For history, we still have 1st-c. sources to weigh.",
            "follow_up": "Ask which recoverable Jesus-teachings they accept.",
            "sources": ["Saeed PDF", "1 Corinthians 15"],
        },
        {
            "trigger": "Trinity was invented; Jesus was unitarian",
            "fast_answer": "Distinguish development of terms from eruption of Jesus-devotion. Use historical Jesus dossier tools.",
            "follow_up": "Mark 12:29 AND Phil 2 both on the table.",
            "sources": ["Mark 12:29", "Philippians 2"],
        },
        {
            "trigger": "God would never let His prophet be crucified",
            "fast_answer": "That's a theological intuition. Christian vision: He did, for redemption. Argue justice, don't only intuit.",
            "follow_up": "Ask how they explain the historical consensus.",
            "sources": ["https://quran.com/4/157", "Romans 5", "Ehrman blog"],
        },
        {
            "trigger": "John 17:3 ends the deity debate",
            "fast_answer": "Powerful unitarian-sounding text; Christians read it with John 1 and 20:28. Don't isolate.",
            "follow_up": "Ask how Thomas's confession is classified.",
            "sources": [
                "https://www.biblegateway.com/passage/?search=John+17%3A3%3B+20%3A28&version=NRSVUE"
            ],
        },
        {
            "trigger": "Jesus ate food so he can't be God",
            "fast_answer": "That's anti-Docetism / full humanity — Christians agree he ate. Chalcedon: humanity isn't a veto on deity.",
            "follow_up": "Ask if any incarnation theory could satisfy them in principle.",
            "sources": ["https://quran.com/5/75", "Chalcedon"],
        },
        {
            "trigger": "Your Gospels contradict, so your Jesus vision is incoherent",
            "fast_answer": "Harmonistics vs contradiction claims are a sub-debate. Vision coherence ≠ synopsis of every chronology.",
            "follow_up": "Offer core kerygma shared across sources.",
            "sources": ["1 Corinthians 15", "Mark passion"],
        },
        {
            "trigger": "Islam's Jesus is just a way to deny Christianity",
            "fast_answer": "Steelman: Islam places Jesus in a line of prophets with honor. Then critique collisions.",
            "follow_up": "Affirm virgin birth/miracles overlap before fighting cross/deity.",
            "sources": ["https://quran.com/3/45-49", "https://quran.com/19"],
        },
        {
            "trigger": "If Jesus is God, who ran the universe when he died?",
            "fast_answer": "Classical answer: divine nature didn't cease; death is in the human nature. Explain without mockery.",
            "follow_up": "Invite formal contradiction claim.",
            "sources": ["https://plato.stanford.edu/entries/incarnation/", "Chalcedon"],
        },
        {
            "trigger": "Rational people can't believe incarnation",
            "fast_answer": "Mystery ≠ contradiction. Demand a formal contradiction; cite SEP incarnation models.",
            "follow_up": "Compare burdens: incarnation vs 4:157 vs history.",
            "sources": ["https://plato.stanford.edu/entries/incarnation/"],
        },
    ],
    "checklist": [
        "State both visions in one sentence each at the open",
        "Announce weights: history vs rationality vs existential",
        "Define Injīl before dilemma arguments",
        "Master 1 Cor 15, Phil 2, John 1, Q 4:171, 4:157, 5:75, 3:59",
        "Yes/no: may one pray to Jesus?",
        "Prepare cross necessity vs cross impossibility exchange",
        "Link to trinity and historical_jesus dossiers without dumping whole files",
        "Falsification: what would make you abandon your vision?",
        "Drill cards; steelman Islamic honor of Jesus first",
        "Separate Qur'an-only from hadith eschatology on return",
        "Closing: data fit + monotheism coherence, not slogans",
        "Bring Chalcedon line + Q 4:171 + 1 Cor 15 card",
    ],
    "positive_cases": {
        "Christian podium": [
            "Vision integrates earliest cross/resurrection kerygma and Jesus-devotion",
            "Incarnational monotheism explains worship without crude tritheism",
            "Cross as disclosure of love/justice is existentially and theologically central",
            "Islamic vision underfits passion history and apostolic gospel content",
        ],
        "Muslim podium": [
            "Vision preserves uncompromising tawhid while highly honoring Jesus",
            "Prophet-Messiah portrait better matches Jewish monotheist historical core",
            "Rejects moral scandal of vicarious divine death; mercy without blood",
            "Titles (word/messiah/miracles) without ontological inflation",
        ],
        "Unity / steelman": [
            "Both visions treat Jesus as pivotal — not peripheral",
            "Agree on virgin birth and miracles-by-God's-power as shared affirmations to isolate forks",
            "Distinguish respect, worship, and historical reconstruction",
            "Name the meta-authority: apostolic witnesses vs Qur'an",
        ],
    },
    "bibliography": [
        {
            "tier": "Philosophy / theology",
            "items": [
                {"label": "SEP — Trinity", "url": "https://plato.stanford.edu/entries/trinity/"},
                {"label": "SEP — Incarnation", "url": "https://plato.stanford.edu/entries/incarnation/"},
                {"label": "Chalcedonian Definition", "url": "https://www.earlychurchtexts.com/public/chalcedonian_definition.htm"},
                {"label": "Nicene Creed", "url": "https://www.usccb.org/prayers/nicene-creed"},
            ],
        },
        {
            "tier": "Primary / history",
            "items": [
                {"label": "John 1; Philippians 2; 1 Corinthians 15; Hebrews 1", "url": "https://www.biblegateway.com/passage/?search=John+1%3A1-18&version=NRSVUE"},
                {"label": "Qur'an 3:45–59; 4:157–158; 4:171; 5:75; 5:116–117; 19", "url": "https://quran.com/4/171"},
                {"label": "Ehrman — historical Jesus vs Qur'an", "url": "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/"},
            ],
        },
        {
            "tier": "Islamic studies gateways",
            "items": [
                {"label": "Saeed on scriptural distortion", "url": "https://bible-quran-video.s3.amazonaws.com/Documents/The-Charge-of-Distortion-of-Jewish-and-Christian-Scriptures_Abdullah+Saeed.pdf"},
                {"label": "Lawson — Crucifixion and the Qur'an", "url": "https://almuslih.org/wp-content/uploads/2024/12/Lawson-T-%E2%80%93-The-Crucifixion-and-the-Quran.pdf"},
            ],
        },
    ],
}


def topic():
    from .deepen_lib import apply_overlays
    from .jesus_deep import VISION
    return apply_overlays(DATA, VISION)
