# -*- coding: utf-8 -*-
from .deepen_lib import D, M, Q, S

OVERLAYS = {
    "one-essence-three-persons": {
        "why_it_matters": (
            "If this fork is not locked, every later argument (worship, incarnation, Qur'anic polemic) "
            "is just name-calling: 'you worship three gods' vs 'you don't understand person vs essence.'"
        ),
        "christian": {
            "quotes": [
                Q(
                    "We worship one God in Trinity, and Trinity in Unity; neither confounding the Persons, nor dividing the Substance.",
                    "Athanasian Creed",
                    "Quicunque vult (received Western text)",
                    "https://www.ccel.org/ccel/schaff/creeds2.iv.i.iv.html",
                ),
                Q(
                    "The Trinity is One. We do not confess three Gods, but one God in three persons, the 'consubstantial Trinity'.",
                    "Catechism of the Catholic Church",
                    "CCC 253",
                    "https://www.vatican.va/archive/ENG0015/__P17.HTM",
                ),
            ],
            "data_points": [
                D("Nicene homoousios: Son is of one substance with the Father, not a second god.", "Nicene Creed", "https://www.usccb.org/prayers/nicene-creed"),
                D("Patristic 'person' (hypostasis) is not modern 'three human personalities in one skull.'", "SEP Trinity", "https://plato.stanford.edu/entries/trinity/"),
            ],
            "sources": [
                S("Stanford Encyclopedia — Trinity", "https://plato.stanford.edu/entries/trinity/"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Say, He is Allah, One. Allah, the Eternal Refuge. He neither begets nor is born, nor is there to Him any equivalent.",
                    "Qur'an 112:1–4",
                    "Sūrat al-Ikhlāṣ",
                    "https://quran.com/112",
                ),
                Q(
                    "O People of the Book, do not commit excess in your religion… The Messiah, Jesus, the son of Mary, was but a messenger of Allah… So believe in Allah and His messengers. And do not say, 'Three'; desist — it is better for you. Allah is but one God.",
                    "Qur'an 4:171",
                    "Primary text",
                    "https://quran.com/4/171",
                ),
            ],
            "data_points": [
                D("If each person is 'fully God,' a Muslim counts three who may be addressed as God — essence-talk does not cancel the count of worship-receivers.", "Standard kalām / dawah counting argument"),
                D("Q 5:73 condemns those who say 'Allah is the third of three.'", "Qur'an 5:73", "https://quran.com/5/73"),
            ],
        },
        "counters": [
            {
                "against": "Muslim tritheism charge",
                "claim": "Christians worship three gods.",
                "reply": "Ask them to quote a creed that says three gods. Then ask whether their objection is to counting persons or to the metaphysics of one ousia. Those are different fights.",
            },
            {
                "against": "Christian word-magic",
                "claim": "Saying 'one essence' automatically makes it monotheism.",
                "reply": "Show how the three are not three independent centers of will in a way that yields three gods. Social Trinity models must answer this; Latin models must answer 'is this modalism?'",
            },
        ],
        "live": {
            "if_they_say": "The Trinity is three gods.",
            "you_say": "Quote the creed you think we hold. We confess one God, one essence; 'person' is not a second deity. If your target is three independent gods, you are not hitting Nicene Christianity.",
            "dont_overclaim": "Do not pretend the metaphysics is easy. Do not pretend the Qur'an is discussing Hegel.",
        },
    },
    "quranic-polemic-target": {
        "why_it_matters": (
            "Best Muslim offensive text-set (4:171, 5:73, 5:116) vs best Christian dodge: "
            "'the Qur'an refutes a heresy, not us.' If 5:116 is the Trinity, Islam scores; if it is Jesus+Mary Tritheism, the score reverses."
        ),
        "christian": {
            "quotes": [
                Q(
                    "And [beware the Day] when Allah will say, 'O Jesus, Son of Mary, did you say to the people, \"Take me and my mother as deities besides Allah?\"'",
                    "Qur'an 5:116",
                    "Primary text",
                    "https://quran.com/5/116",
                ),
            ],
            "data_points": [
                D("Nicene Trinity is Father, Son, Spirit — Mary is not a divine person in catholic creeds.", "Nicene / CCC"),
                D("5:116's triad (Jesus, Mary, God) does not match Father-Son-Spirit.", "Plain reading of 5:116"),
            ],
            "sources": [
                S("Gabriel Said Reynolds on Qur'anic Christians", "https://brill.com/display/title/16716"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "They have certainly disbelieved who say, 'Allah is the third of three.' And there is no god except one God.",
                    "Qur'an 5:73",
                    "Primary text",
                    "https://quran.com/5/73",
                ),
            ],
            "data_points": [
                D("Even if 5:116 pictures a popular error, 4:171 still forbids 'Three' and divine sonship.", "Q 4:171"),
                D("Lived Christian worship of Jesus (and historically of Mary in some popular piety) is the Qur'an's practical target, not a seminar on Cappadocian terminology.", "Standard tafsir trajectory"),
            ],
        },
        "counters": [
            {
                "against": "Christian 'wrong Trinity' dismiss",
                "claim": "5:116 proves Muhammad didn't know the Trinity, so ignore the rest.",
                "reply": "5:116 is one verse. You still owe an answer to 4:171, 5:72–73, 9:30, and 112. Category error vs. total ignorance are different claims.",
            },
        ],
        "live": {
            "if_they_say": "The Qur'an thinks Christians worship Mary as the third of the Trinity.",
            "you_say": "5:116 names Jesus and Mary as alleged gods beside Allah — that is a piety/Tritheism shot. Then read 4:171, which hits 'Three' and sonship without Mary. Don't collapse all verses into 5:116.",
            "dont_overclaim": "Christians: don't pretend no Christian ever treated Mary in godlike ways. Muslims: don't pretend 5:116 is a lecture on homoousios.",
        },
    },
    "divine-love-self": {
        "why_it_matters": "Highest-level Christian philosophical case: God is love eternally, so God is not a solitary will who only becomes relational after creating.",
        "christian": {
            "quotes": [
                Q(
                    "God is love.",
                    "1 John 4:8",
                    "NT primary text",
                    "https://www.biblegateway.com/passage/?search=1%20John%204%3A8&version=NRSVUE",
                ),
                Q(
                    "If God is love, there must be in God a Lover, a Beloved, and the Love that unites them — a classic Augustinian sketch of why absolute solitude sits awkwardly with 'God is love' as God's essence, not a later hobby.",
                    "Augustinian tradition (paraphrase of De Trinitate's lover–beloved–love motif)",
                    "De Trinitate VIII–IX",
                    "https://www.newadvent.org/fathers/1301.htm",
                ),
            ],
            "data_points": [
                D("The argument is: essential love is interpersonal; creation is contingent; therefore interpersonal life in God is not creation-dependent.", "Richard of St. Victor / modern analytic retrievals"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "And He is the Forgiving, the Loving.",
                    "Qur'an 85:14",
                    "Al-Wadūd as a name of the one God",
                    "https://quran.com/85/14",
                ),
            ],
            "data_points": [
                D("Ashʿarī/Māturīdī theology: God is eternally knowing, willing, living without requiring a second divine person as beloved.", "Classical kalām"),
                D("Love can be an essential attribute directed to creation when it exists, or a self-regard that does not split the essence.", "Standard tawhid reply"),
            ],
        },
        "counters": [
            {
                "against": "Christian necessity of three",
                "claim": "Love proves three persons.",
                "reply": "Even if love suggests 'more than a lonely monad,' it does not deductively yield exactly Father, Son, and Spirit, or incarnation. At most it pressures unitarian solitude.",
            },
        ],
        "live": {
            "if_they_say": "A unitarian God cannot be love until He creates, so He needs creatures.",
            "you_say": "That is a philosophical pressure, not a proof of the Nicene triad. Ask whether Islam's al-Wadūd is an eternal attribute or a relation that begins with the world — then compare to Trinity as claimed revelation, not as the only metaphysical patch.",
            "dont_overclaim": "Don't say Muslims think God is unloving. Don't say the Trinity is 'proved' by 1 John 4:8.",
        },
    },
    "self-knowledge": {
        "why_it_matters": "Logos arguments try to make the Son metaphysically inevitable. Muslims treat this as Greek overlay.",
        "christian": {
            "quotes": [
                Q(
                    "In the beginning was the Word, and the Word was with God, and the Word was God.",
                    "John 1:1",
                    "NT primary text",
                    "https://www.biblegateway.com/passage/?search=John%201%3A1&version=NRSVUE",
                ),
            ],
            "data_points": [
                D("Patristic Logos: God's eternal self-knowledge/expression is not a creature.", "John 1 + Nicene"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "When He decrees a matter, He only says to it, 'Be,' and it is.",
                    "Qur'an 2:117",
                    "Kun fa-yakūn — speech as command, not a second person",
                    "https://quran.com/2/117",
                ),
            ],
            "data_points": [
                D("Kalām: God's knowledge and speech (kalām) are attributes, not hypostases you pray to.", "Ashʿarī / Māturīdī"),
                D("The Qur'an calls Jesus a 'word from Him' (3:45; 4:171) without making the Word a second deity.", "Q 3:45; 4:171"),
            ],
        },
        "live": {
            "if_they_say": "God's Word must be God, or God was once mute/unknowing.",
            "you_say": "Distinguish attribute from person. Islam can grant eternal speech/knowledge without a second worship-receiver. John 1 is the Christian claim; it is not a compulsory philosophy for all theists.",
            "dont_overclaim": "Don't turn kalām into 'Muslims think God is silent.' Don't treat John 1 as a logic puzzle that ends debate.",
        },
    },
    "incarnation-coherence": {
        "why_it_matters": "Even if Trinity is coherent, incarnation adds: infinite God is a particular first-century Jew. This is often the heavier rational burden.",
        "christian": {
            "quotes": [
                Q(
                    "…who, though he was in the form of God, did not regard equality with God as something to be exploited, but emptied himself… being born in human likeness.",
                    "Philippians 2:6–7",
                    "NT primary text",
                    "https://www.biblegateway.com/passage/?search=Philippians%202%3A5-11&version=NRSVUE",
                ),
                Q(
                    "We confess one and the same Son… complete in Godhead and complete in manhood… acknowledged in two natures, without confusion, without change, without division, without separation.",
                    "Council of Chalcedon (451)",
                    "Definition of Faith",
                    "https://www.earlychurchtexts.com/public/chalcedonian_definition.htm",
                ),
            ],
            "data_points": [
                D("Chalcedon is the classical 'how' answer: two natures, one person — not a hybrid demigod.", "451 CE definition"),
                D("SEP: incarnation debates include kenosis, two-minds, and composition models — live philosophical literature, not only slogans.", "https://plato.stanford.edu/entries/incarnation/"),
            ],
            "sources": [
                S("Stanford Encyclopedia — Incarnation", "https://plato.stanford.edu/entries/incarnation/"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "It is not for Allah to take a son; exalted is He. When He decrees a matter, He only says to it, 'Be,' and it is.",
                    "Qur'an 19:35",
                    "Primary text",
                    "https://quran.com/19/35",
                ),
            ],
            "data_points": [
                D("Category objection: the uncreated does not become a created body; hunger, sleep, and death are not predicated of God.", "Q 5:75 — Messiah ate food"),
                D("Q 5:17: 'They have certainly disbelieved who say that Allah is the Messiah, son of Mary.'", "https://quran.com/5/17"),
            ],
        },
        "counters": [
            {
                "against": "Muslim 'God in a womb is absurd'",
                "claim": "Incarnation is a logical contradiction.",
                "reply": "Contradiction requires the same attribute in the same respect. Chalcedon predicates divine attributes of the divine nature and human attributes of the human nature, united in one person. Attack that distinction; don't just shout 'impossible.'",
            },
        ],
        "live": {
            "if_they_say": "God cannot enter a womb, eat, or die.",
            "you_say": "As God qua divine nature, Christians agree. The claim is that the person of the Son assumed a human nature. If you reject the two-natures grammar, say so — that is the real crux.",
            "dont_overclaim": "Don't say incarnation is 'simple.' Don't say Muslims have never heard of natures/person.",
        },
    },
    "worship-practice": {
        "why_it_matters": "Lived liturgy is what the Qur'an often seems to see: people calling on Jesus. Philosophy can wait; prayer cannot.",
        "christian": {
            "quotes": [
                Q(
                    "…at the name of Jesus every knee should bend, in heaven and on earth and under the earth, and every tongue should confess that Jesus Christ is Lord…",
                    "Philippians 2:10–11",
                    "NT primary text (Isaiah 45:23 applied to Jesus)",
                    "https://www.biblegateway.com/passage/?search=Philippians%202%3A10-11&version=NRSVUE",
                ),
            ],
            "data_points": [
                D("Larry Hurtado: earliest Christian circles offered Jesus a pattern of devotion otherwise reserved for God in Jewish monotheism.", "Hurtado, Lord Jesus Christ"),
                D("Baptism 'in the name of the Father and of the Son and of the Holy Spirit' is first-century liturgical data (Matt 28:19), not a medieval invention.", "Matt 28:19"),
            ],
            "sources": [
                S("Matt 28:19", "https://www.biblegateway.com/passage/?search=Matthew%2028%3A19&version=NRSVUE"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "You [alone] we worship, and You [alone] we ask for help.",
                    "Qur'an 1:5",
                    "Al-Fātiḥah — worship exclusivity",
                    "https://quran.com/1/5",
                ),
            ],
            "data_points": [
                D("Shirk is defined by worship-direction, not by a seminar distinction your average parish does not live.", "Islamic ʿibādah analysis"),
                D("If Jesus receives prayer, praise, and salvation-trust, tawhid scores that as associating a partner — whatever 'through the Son to the Father' theory is offered afterward.", "Practical-worship argument"),
            ],
        },
        "live": {
            "if_they_say": "Do you pray to Jesus?",
            "you_say": "Christians: yes, as worship of the one God through the incarnate Son — then explain why that is not a second god. Muslims: yes they do, and that is the data 5:72 is aimed at. Don't let the answer hide in vocabulary.",
            "dont_overclaim": "Don't pretend all Christians pray identically. Don't pretend no Christian distinguishes latria/dulia.",
        },
    },
    "occam": {
        "why_it_matters": "Simplest Muslim logic hit. Christian reply must be: extra structure is not multiplying gods, it is claimed revealed inner life of the one God.",
        "christian": {
            "quotes": [
                Q(
                    "The Trinity is a mystery of faith in the strict sense… We can know it only because God has revealed it.",
                    "Catechism of the Catholic Church",
                    "CCC 237 (abridged sense of the paragraph)",
                    "https://www.vatican.va/archive/ENG0015/__P17.HTM",
                ),
            ],
            "data_points": [
                D("Occam's razor trims unnecessary entities; it does not forbid revealed distinctions if they do explanatory work (creation, salvation, worship data).", "Philosophy of religion reply"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Allah has not taken any son, nor has there ever been with Him any god. [If there had been], then each god would have taken what it created, and some of them would have sought to overcome others.",
                    "Qur'an 23:91",
                    "Primary text — rivalry reductio",
                    "https://quran.com/23/91",
                ),
            ],
            "data_points": [
                D("A doctrine that needs councils, anathemas, and a technical lexicon to avoid tritheism/modalism has a higher error-cost than 'God is one.'", "Dawah Occam line"),
            ],
        },
        "live": {
            "if_they_say": "Tawhid is just simpler, so it wins.",
            "you_say": "Simpler than what? 'One person, one essence' is simpler than 'three persons, one essence.' That is not yet 'true.' If the world includes incarnation and resurrection claims, the simpler map may be too small.",
            "dont_overclaim": "Don't treat simplicity as a proof. Don't treat mystery as a blank check.",
        },
    },
    "begotten-not-made": {
        "why_it_matters": "Lexical collision: Greek gennaō / 'only-begotten' vs Arabic walada. Most street debates are this dictionary fight.",
        "christian": {
            "quotes": [
                Q(
                    "I believe in one Lord Jesus Christ, the Only Begotten Son of God, born of the Father before all ages… begotten, not made, consubstantial with the Father.",
                    "Nicene-Constantinopolitan Creed",
                    "Received liturgical text",
                    "https://www.usccb.org/prayers/nicene-creed",
                ),
            ],
            "data_points": [
                D("Nicene 'begotten' is eternal relation, not a temporal birth from a consort.", "Anti-Arian settlement"),
                D("Q 6:101 attacks the idea that God has a companion/consort — Christians should concede that target is not Chalcedon.", "https://quran.com/6/101"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "He neither begets nor is born.",
                    "Qur'an 112:3",
                    "Lam yalid wa-lam yūlad",
                    "https://quran.com/112",
                ),
            ],
            "data_points": [
                D("If 'Son' is more than a title of honor, it still imports creaturely generation language onto God.", "Q 19:88–93"),
                D("Q 19:88–92: claiming a son is an enormity that nearly tears the heavens.", "https://quran.com/19/88"),
            ],
        },
        "live": {
            "if_they_say": "Christians say God had a son like pagans.",
            "you_say": "Ask which Christian document teaches sexual generation. Then fight the real issue: is eternal generation still a 'son' the Qur'an forbids, or only biological sonship?",
            "dont_overclaim": "Don't mock 112 as if it were illiterate. Don't pretend 'begotten' is an everyday English word.",
        },
    },
    "spirit-as-god": {
        "why_it_matters": "Often the neglected third. If the Spirit is not God, the Trinity fails even if Jesus were divine.",
        "christian": {
            "quotes": [
                Q(
                    "Why has Satan filled your heart to lie to the Holy Spirit? … You have not lied to man but to God.",
                    "Acts 5:3–4",
                    "NT identification of Spirit with God",
                    "https://www.biblegateway.com/passage/?search=Acts%205%3A3-4&version=NRSVUE",
                ),
            ],
            "data_points": [
                D("Matthew 28:19 places the Spirit in the baptismal name beside Father and Son.", "Matt 28:19"),
                D("John 14–16: the Spirit as personal paraklētos, not a mere force.", "Farewell discourse"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "The Messiah, Jesus, the son of Mary, was but a messenger of Allah and His word which He directed to Mary and a soul [spirit] from Him.",
                    "Qur'an 4:171",
                    "Rūḥ minhu — Jesus as spirit from God, not Spirit as third person",
                    "https://quran.com/4/171",
                ),
            ],
            "data_points": [
                D("In the Qur'an, rūḥ is typically created: the spirit from God's command (17:85), Jibrīl, or the breath given to Mary/Adam.", "Q 17:85; 19:17"),
                D("Identifying the Spirit with a divine person looks to Muslims like a later church development.", "Islamic reading of church history"),
            ],
        },
        "live": {
            "if_they_say": "The Holy Spirit is just the angel Gabriel or a force.",
            "you_say": "In the NT the Spirit is lied to as God (Acts 5) and named in baptism. In the Qur'an rūḥ is not a co-equal person. That's a collision of pneumatology, not a footnote.",
            "dont_overclaim": "Don't flatten all Jewish ruach uses into Nicene pneumatology. Don't pretend 4:171 means the Christian Holy Spirit.",
        },
    },
    "mystery-vs-clarity": {
        "why_it_matters": "Closing rhetoric of almost every round: is mystery humility or a get-out-of-logic card?",
        "christian": {
            "quotes": [
                Q(
                    "If you understood him, he would not be God.",
                    "Augustine (often-cited line on divine incomprehensibility)",
                    "Sermon 117, 5 (standard attribution in this debate)",
                    "https://www.newadvent.org/fathers/1603.htm",
                ),
            ],
            "data_points": [
                D("Mystery in catholic theology is not 'contradiction we celebrate'; it is a revealed reality that exceeds comprehensive grasp.", "CCC 237 / classic distinction"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Allah does not shy from using the example of a mosquito or even something smaller.",
                    "Qur'an 2:26",
                    "Clarity / accessibility motif — God explains",
                    "https://quran.com/2/26",
                ),
            ],
            "data_points": [
                D("Fitrah argument: a fisherman should be able to know whom to worship without a council lexicon.", "Popular tawhid rhetoric, grounded in Q 30:30"),
            ],
        },
        "live": {
            "if_they_say": "You just hide behind mystery.",
            "you_say": "Mystery is allowed after a coherent grammar is on the table (one ousia, three hypostases, two natures). If the grammar is contradictory, mystery cannot save it. If it is coherent but deep, mystery is not a cheat.",
            "dont_overclaim": "Don't use mystery to skip 5:116. Don't use 'clear Qur'an' to skip mutashābihāt (Q 3:7).",
        },
    },
    "revelation-priority": {
        "why_it_matters": "Meta-crux: maybe neither side can 'win' Trinity vs Tawhid by pure reason. Then the fight returns to which revelation is historically true.",
        "christian": {
            "data_points": [
                D("If Jesus rose, high Christology is historically motivated even if metaphysics is hard.", "1 Cor 15 as Christian hinge"),
                D("Rationality of Trinity is then posterior to the identity of Jesus.", "Classic 'Christology first' order"),
            ],
        },
        "muslim": {
            "data_points": [
                D("If the Qur'an is the intact final revelation, tawhid adjudicates earlier Christian metaphysics as excess (ghuluww).", "Q 4:171; 5:77"),
                D("Then the live debate should move to historicity/prophethood, not endless Occam.", "Method note"),
            ],
        },
        "live": {
            "if_they_say": "Reason alone proves my view of God.",
            "you_say": "Then we should be able to settle it without scripture. If we cannot, admit that revelation-priority is doing the work and switch motions to 'which revelation?'",
            "dont_overclaim": "Don't pretend philosophy is useless. Don't pretend it is sufficient.",
        },
    },
    "moral-worship-unity": {
        "why_it_matters": "Pastoral close: what kind of heart does each doctrine train?",
        "live": {
            "if_they_say": "Tawhid produces purer worship; Trinity confuses the heart.",
            "you_say": "Ask for the mechanism: does addressing Father, Son, and Spirit split allegiance, or is it one God named three ways in prayer? Then ask whether unitarian worship can include the historical Jesus without remainder. This is psychology, not a syllogism — say so.",
            "dont_overclaim": "Don't diagnose 1.8 billion worshipers from a slogan. Don't pretend no Trinitarian has ever lapsed into practical tritheism.",
        },
    },
    "white-ally-trinity": {
        "live": {
            "if_they_say": "White vs Ally already settled the Trinity.",
            "you_say": "Steal their definition moves, not their victory lap. Force person vs being in the first minute, then 5:116 vs 4:171. The recording is a drill tape, not a referee.",
            "dont_overclaim": "Don't cite a debate as if it were a council. Don't skip the primary texts they actually read.",
        },
    },
    "qadhi-wood-style": {
        "live": {
            "if_they_say": "Popular dawah already refuted the Trinity.",
            "you_say": "Ask which Trinity they refuted. If it is Father-Mother-Son or three gods, they missed Nicene. If it is worship of Jesus, they hit the live nerve — then do incarnation, not memes.",
            "dont_overclaim": "Don't treat Wood clips as Augustine. Don't treat a 60-second dawah reel as Taftāzānī.",
        },
    },
}
