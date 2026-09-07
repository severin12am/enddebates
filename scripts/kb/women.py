# -*- coding: utf-8 -*-
"""Which tradition is better regarding women?"""

DATA = {
    "id": "women",
    "meta": {
        "title": "Christianity vs Islam: better regarding women?",
        "thesis": (
            "On dignity, legal rights, family law, and lived founding examples, which tradition "
            "offers the stronger moral vision for women — and under which hermeneutic?"
        ),
        "purpose": (
            "Steelman Gospel narratives and Christian patriarchal history alongside Qur'anic reforms, "
            "4:34 debates, polygyny, inheritance, and testimony. Separate scripture, classical law, and modernity."
        ),
        "warning": (
            "Do not compare Jesus' kindness to women against ISIS memes, or Khadija against medieval "
            "witch-trial cartoons. Same century, same genre, same legal level."
        ),
        "chips": ["ethics", "law", "gender", "family", "hermeneutics"],
        "labels": {"christian": "Christian case", "muslim": "Muslim case"},
    },
    "definitions": [
        {
            "term": "Ontological equality",
            "precise": "Equal worth before God as human beings / image-bearers / believing souls.",
            "not": "Not the same as identical legal roles in family or courtroom.",
        },
        {
            "term": "Functional / legal complementarity",
            "precise": "Different rights and duties by sex in marriage, testimony, inheritance, leadership.",
            "not": "Not automatically 'hatred of women' — argue whether the differentials are just.",
        },
        {
            "term": "Qur'an 4:34 (qiwāma / ḍarb)",
            "precise": (
                "Verse on male qiwāma and steps of marital discord ending in a contested term often "
                "translated 'strike.' Interpretation is a major debate locus."
            ),
            "not": "Not a blank check for domestic abuse in responsible tafsir — but not a non-issue.",
        },
        {
            "term": "Polygyny",
            "precise": "Marriage of one man to multiple wives (Qur'an 4:3 conditional; OT also knows it).",
            "not": "Not polyandry; not identical with adultery.",
        },
        {
            "term": "Patristic / canon patriarchy",
            "precise": "Christian historical patterns of male clergy, coverture-like norms, and household codes.",
            "not": "Not identical with Jesus' interactions in the Gospels.",
        },
        {
            "term": "Trajectory hermeneutic",
            "precise": (
                "Reading texts as moving history toward fuller equality (used by some Christians on slavery/gender "
                "and some Muslims on reform)."
            ),
            "not": "Not agreed by complementarians or classical fiqh traditionalists.",
        },
    ],
    "arguments": [
        {
            "id": "jesus-and-women",
            "rank": 1,
            "cluster": "Founding examples",
            "title": "Jesus' treatment of women as moral paradigm",
            "type": "ethics + narrative",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Jesus teaches women, receives their patronage, and appears first to women as "
                    "resurrection witnesses — a dignity pattern superior to later patriarchal religion, including Islamic law."
                ),
                "case": (
                    "Luke 10:38–42; John 4; Luke 8:1–3; John 20:11–18. Founding narrative centers women "
                    "as discipleship models against their culture."
                ),
                "sources": [
                    {
                        "label": "John 20:11–18",
                        "url": "https://www.biblegateway.com/passage/?search=John+20%3A11-18&version=NRSVUE",
                    },
                    {
                        "label": "Luke 10:38–42",
                        "url": "https://www.biblegateway.com/passage/?search=Luke+10%3A38-42&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Islam's founding includes Khadija the employer-wife, Aisha the scholar-transmitter, "
                    "and Qur'anic address to believing women — not a story of female erasure."
                ),
                "case": (
                    "33:35 parallel spiritual status; property and consent norms as reforms in Arabia. "
                    "Gospel kindness does not cancel Christian institutional patriarchy."
                ),
                "sources": [
                    {"label": "Qur'an 33:35", "url": "https://quran.com/33/35"},
                    {"label": "Qur'an 4:32", "url": "https://quran.com/4/32"},
                    {
                        "label": "Yaqeen — women & Islamic scholarship themes",
                        "url": "https://yaqeeninstitute.org/",
                    },
                ],
            },
            "counter_to_christian": "Pauline silence/authority texts and centuries of male-only priesthood complicate the Jesus-only score.",
            "counter_to_muslim": "Elevated early women coexist with enduring legal asymmetries — both must be weighed.",
            "crux": "Do founding narratives outweigh later legal codes when scoring 'better regarding women'?",
            "debate_use": "Split score: narrative dignity vs family law rights.",
        },
        {
            "id": "polygyny",
            "rank": 2,
            "cluster": "Family law",
            "title": "Polygyny: permission vs restriction",
            "type": "ethics + law",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Jesus' two-in-one-flesh ideal and NT elder qualifications assume monogamy; "
                    "Qur'anic polygyny institutionalizes asymmetry harmful to women."
                ),
                "case": (
                    "Matthew 19:4–6; 1 Tim 3:2. Even if 4:3 is 'justice-conditional,' the structure "
                    "privileges male sexual access."
                ),
                "sources": [
                    {
                        "label": "Matthew 19:3–9",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+19%3A3-9&version=NRSVUE",
                    },
                    {"label": "Qur'an 4:3", "url": "https://quran.com/4/3"},
                ],
            },
            "muslim": {
                "claim": (
                    "4:3 restricts a prior unlimited practice, ties plurality to orphan justice, and 4:129 "
                    "warns perfect equality is impossible — often read as pressure toward monogamy."
                ),
                "case": (
                    "OT polygyny undercuts Christian uniqueness. Contextual reform + justice conditions "
                    "beat romanticizing Christian history that still oppressed women."
                ),
                "sources": [
                    {"label": "Qur'an 4:3", "url": "https://quran.com/4/3"},
                    {"label": "Qur'an 4:129", "url": "https://quran.com/4/129"},
                    {
                        "label": "2 Samuel 5:13 (OT polygyny example)",
                        "url": "https://www.biblegateway.com/passage/?search=2+Samuel+5%3A13&version=NRSVUE",
                    },
                ],
            },
            "counter_to_christian": "Christian divorce battles and serial monogamy can mimic polygyny's harms.",
            "counter_to_muslim": "A warning in 4:129 does not erase the legal permission in 4:3.",
            "crux": "Is restricted polygyny moral progress in context, or a lasting injustice relative to monogamy norms?",
            "debate_use": "Ask both sides their rule for widows/orphans in war economies without anachronism.",
        },
        {
            "id": "quran-4-34",
            "rank": 3,
            "cluster": "Family law",
            "title": "Qur'an 4:34 and marital discipline",
            "type": "exegesis + ethics",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "A verse permitting husbands to strike wives (on common translations) is incompatible "
                    "with equal dignity and with Jesus' non-domination ethic."
                ),
                "case": (
                    "4:34 is a centerpiece of Christian critique. Even 'light tap' readings encode "
                    "unilateral male authority in conflict."
                ),
                "sources": [
                    {"label": "Qur'an 4:34", "url": "https://quran.com/4/34"},
                    {
                        "label": "Ephesians 5:25–33 (husband love pattern)",
                        "url": "https://www.biblegateway.com/passage/?search=Ephesians+5%3A25-33&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Classical and modern readings constrain ḍarb severely; many scholars forbid harm; "
                    "some argue non-physical reading. Prophet's example is non-hitting."
                ),
                "case": (
                    "Hadith: best of you do not strike. Reformist and traditional fatwas against abuse. "
                    "Christian household codes also command wife submission (Eph 5:22–24)."
                ),
                "sources": [
                    {"label": "Qur'an 4:34", "url": "https://quran.com/4/34"},
                    {
                        "label": "Ephesians 5:22–24",
                        "url": "https://www.biblegateway.com/passage/?search=Ephesians+5%3A22-24&version=NRSVUE",
                    },
                    {
                        "label": "IslamicStudies / tafsir discussions on 4:34",
                        "url": "https://islamicstudies.info/tafheem.php?sura=4&verse=34",
                    },
                ],
            },
            "counter_to_christian": "Eph 5 submission texts are also contested as hierarchy.",
            "counter_to_muslim": "If the plain sense allows strike, 'our scholars forbid abuse' is damage control unless tied to usūl.",
            "crux": "What does 4:34 originally authorize, and can that authorization be closed without leaving the text?",
            "debate_use": "Require a translation + a named classical tafsir before slogans.",
        },
        {
            "id": "inheritance-testimony",
            "rank": 4,
            "cluster": "Legal status",
            "title": "Inheritance shares and testimony (2:282)",
            "type": "law + ethics",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Half-share inheritance (4:11) and gendered testimony rules encode lesser legal "
                    "personhood incompatible with equal civic dignity."
                ),
                "case": (
                    "4:11; 2:282. Modern human-rights baselines treat these as discriminatory. "
                    "Christian inheritance law in secular states moved to equality."
                ),
                "sources": [
                    {"label": "Qur'an 4:11", "url": "https://quran.com/4/11"},
                    {"label": "Qur'an 2:282", "url": "https://quran.com/2/282"},
                ],
            },
            "muslim": {
                "claim": (
                    "Inheritance differentials correlate with male financial maintenance duties; women keep "
                    "mahr and own property. 2:282 is about specific financial contracts, not women's intellect."
                ),
                "case": (
                    "4:32 earning shares; women inherit as a Qur'anic right when Arabia often excluded them. "
                    "Package justice ≠ atomized identical fractions."
                ),
                "sources": [
                    {"label": "Qur'an 4:32", "url": "https://quran.com/4/32"},
                    {"label": "Qur'an 4:7", "url": "https://quran.com/4/7"},
                    {"label": "Qur'an 2:282", "url": "https://quran.com/2/282"},
                ],
            },
            "counter_to_christian": "Premodern Christian law also restricted women's property and testimony in places.",
            "counter_to_muslim": "Maintenance-duty rationale weakens where women are primary earners — adaptive pressure on the model.",
            "crux": "Is package-deal financial justice still just when social economics change?",
            "debate_use": "Ask: timeless ḥukm or ʿillah-based ruling open to reapplication?",
        },
        {
            "id": "divorce-mahr",
            "rank": 5,
            "cluster": "Family law",
            "title": "Divorce initiative, mahr, and financial protection",
            "type": "law + ethics",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Easy male ṭalāq traditions (however regulated) create insecurity; Gospel marriage "
                    "permanence better protects women from disposable marriage."
                ),
                "case": (
                    "Matthew 19; Catholic indissolubility. Critics highlight triple talaq abuses "
                    "(even where reformed)."
                ),
                "sources": [
                    {
                        "label": "Matthew 19:3–9",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+19%3A3-9&version=NRSVUE",
                    },
                    {
                        "label": "CCC on marriage indissolubility (overview)",
                        "url": "https://www.vatican.va/archive/ENG0015/__P3V.HTM",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Mahr, waiting periods, financial rights, and khulʿ give women tools; absolute "
                    "indissolubility can trap women in abuse. Qur'an regulates divorce rather than romanticizing permanence only."
                ),
                "case": (
                    "2:228–232; 4:35 arbitration. Christian annulment/pastoral practice often recreates "
                    "exit ramps while denying the name divorce."
                ),
                "sources": [
                    {"label": "Qur'an 2:228–232", "url": "https://quran.com/2/228-232"},
                    {"label": "Qur'an 4:35", "url": "https://quran.com/4/35"},
                ],
            },
            "counter_to_christian": "Protestant divorce culture undercuts 'permanence protects women' as a live universal.",
            "counter_to_muslim": "Asymmetric initiation rights still matter even with mahr.",
            "crux": "Which harm is worse: disposable marriage or inescapable marriage?",
            "debate_use": "Use abuse-case hypotheticals on both systems.",
        },
        {
            "id": "modesty-veiling",
            "rank": 6,
            "cluster": "Social norms",
            "title": "Modesty, hijab, and control of women's bodies",
            "type": "ethics + culture",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Compulsory covering regimes and gender segregation often police women unequally; "
                    "Gospel freedom of conscience resists sacralized dress coercion."
                ),
                "case": (
                    "24:31; 33:59 debates. State enforcement (where present) is the moral issue. "
                    "1 Cor 11 hair covering is usually not state law in Christianity."
                ),
                "sources": [
                    {"label": "Qur'an 24:30–31", "url": "https://quran.com/24/30-31"},
                    {"label": "Qur'an 33:59", "url": "https://quran.com/33/59"},
                    {
                        "label": "1 Corinthians 11:5–6",
                        "url": "https://www.biblegateway.com/passage/?search=1+Corinthians+11%3A5-6&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Hijab can be piety and anti-objectification; Qur'an also commands male lowering of gaze. "
                    "Christian purity culture and dress norms also regulated women historically."
                ),
                "case": (
                    "24:30 before 24:31. Agency-affirming Muslim women defend covering as liberation "
                    "from market sexualization — contested, but not reducible to 'oppression' alone."
                ),
                "sources": [
                    {"label": "Qur'an 24:30–31", "url": "https://quran.com/24/30-31"},
                    {
                        "label": "Yaqeen / Muslim women scholarship on hijab debates",
                        "url": "https://yaqeeninstitute.org/",
                    },
                ],
            },
            "counter_to_christian": "Conflating voluntary hijab with state coercion is dishonest.",
            "counter_to_muslim": "Where covering is coerced, 'choice' apologetics fail.",
            "crux": "Is the moral issue the garment, the asymmetry, or the enforcement?",
            "debate_use": "Separate: (1) voluntary piety (2) social pressure (3) state law.",
        },
        {
            "id": "leadership",
            "rank": 7,
            "cluster": "Authority",
            "title": "Religious leadership and female authority",
            "type": "theology + law",
            "popularity": "High",
            "christian": {
                "claim": (
                    "While Catholicism/Orthodoxy restrict priesthood, many Christian bodies ordain women; "
                    "Islam's classical imamate of men for mixed prayer is a harder ceiling."
                ),
                "case": (
                    "Galatians 3:28 as trajectory text; Romans 16 women coworkers. Intra-Christian debate "
                    "is real — and that flexibility is itself a point."
                ),
                "sources": [
                    {
                        "label": "Galatians 3:28",
                        "url": "https://www.biblegateway.com/passage/?search=Galatians+3%3A28&version=NRSVUE",
                    },
                    {
                        "label": "Romans 16:1–7",
                        "url": "https://www.biblegateway.com/passage/?search=Romans+16%3A1-7&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Women transmitted hadith, taught, and influenced law; spiritual equality is explicit. "
                    "Ritual leadership rules are not a verdict on worth — and Christian traditions also bar women priests."
                ),
                "case": (
                    "Aisha's authority; 33:35. Compare like with like: Vatican vs classical fiqh, not "
                    "egalitarian Protestants vs Taliban."
                ),
                "sources": [
                    {"label": "Qur'an 33:35", "url": "https://quran.com/33/35"},
                    {
                        "label": "CCC on holy orders (male only)",
                        "url": "https://www.vatican.va/archive/ENG0015/__P4K.HTM",
                    },
                ],
            },
            "counter_to_christian": "Cherry-picking egalitarian denominations avoids the historic majority position.",
            "counter_to_muslim": "Scholarly women ≠ interchangeable ritual/public authority in classical law.",
            "crux": "Is unequal cultic authority an injustice or a role differentiation compatible with equal worth?",
            "debate_use": "Name the Christian comparator church before claiming victory.",
        },
        {
            "id": "sexual-ethics",
            "rank": 8,
            "cluster": "Sexual ethics",
            "title": "Consent, zina, and double standards",
            "type": "ethics + law",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Hudūd for zina and classical evidentiary asymmetries risk cruel outcomes for women; "
                    "Jesus' handling of the accused woman (John 7:53–8:11 tradition) models mercy."
                ),
                "case": (
                    "Even bracketing authenticity debates on the pericope adulterae, the canonical ethos "
                    "prioritizes mercy over stoning dramas."
                ),
                "sources": [
                    {
                        "label": "John 7:53–8:11",
                        "url": "https://www.biblegateway.com/passage/?search=John+7%3A53-8%3A11&version=NRSVUE",
                    },
                    {"label": "Qur'an 24:2", "url": "https://quran.com/24/2"},
                ],
            },
            "muslim": {
                "claim": (
                    "Qur'an 24 requires four witnesses for zina — high bar protecting against false accusation; "
                    "qadhf punishment for slanderers. Christian purity culture shamed women without due process too."
                ),
                "case": (
                    "24:4–9. Moral seriousness about sex is not misogyny per se; ask about male accountability."
                ),
                "sources": [
                    {"label": "Qur'an 24:2–9", "url": "https://quran.com/24/2-9"},
                    {"label": "Qur'an 17:32", "url": "https://quran.com/17/32"},
                ],
            },
            "counter_to_christian": "John pericope textual status is disputed; don't rest the case only there.",
            "counter_to_muslim": "In practice, pregnancy sometimes functioned as evidence against women unevenly.",
            "crux": "Do high evidentiary bars and hudūd protect or endanger women in real courts?",
            "debate_use": "Distinguish classical ideal procedure from abusive modern implementations.",
        },
        {
            "id": "mary-maryam",
            "rank": 9,
            "cluster": "Founding examples",
            "title": "Mary / Maryam as honor paradigm",
            "type": "theology + narrative",
            "popularity": "Medium-high",
            "christian": {
                "claim": (
                    "Mary as Theotokos and model disciple gives women maximal theological honor inside "
                    "salvation history — not a side character."
                ),
                "case": (
                    "Luke 1; Catholic/Orthodox Marian devotion. Critics of Islam note rejection of "
                    "divine maternity language while still honoring Maryam."
                ),
                "sources": [
                    {
                        "label": "Luke 1:26–56",
                        "url": "https://www.biblegateway.com/passage/?search=Luke+1%3A26-56&version=NRSVUE",
                    },
                    {
                        "label": "CCC on Mary",
                        "url": "https://www.vatican.va/archive/ENG0015/__P2C.HTM",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Maryam has a Qur'anic sūrah; chosen above women of the worlds (3:42); "
                    "honor without goddess confusion — cleaner exaltation."
                ),
                "case": (
                    "3:42; 19. Muslims argue Christian Marian excesses prove the need for tawhid-safe honor."
                ),
                "sources": [
                    {"label": "Qur'an 3:42", "url": "https://quran.com/3/42"},
                    {"label": "Qur'an 19", "url": "https://quran.com/19"},
                ],
            },
            "counter_to_christian": "Honoring Mary coexisted with denying women leadership for centuries.",
            "counter_to_muslim": "Theological honor ≠ equal legal agency in marriage/divorce.",
            "crux": "Does exalted female sacred biography predict just gender law?",
            "debate_use": "Treat as supporting color, not the main legal case.",
        },
        {
            "id": "modern-outcomes",
            "rank": 10,
            "cluster": "Modernity",
            "title": "Modern outcomes and reform pathways",
            "type": "ethics + sociology",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Societies shaped by Christian reform movements earliest delivered women's suffrage "
                    "and legal equality; Islamic family-law reform often lags where classical fiqh is state law."
                ),
                "case": (
                    "Correlation ≠ simple causation, but Christian hermeneutical flexibility on gender "
                    "has wider mainstream institutional expression today."
                ),
                "sources": [
                    {
                        "label": "UN / World Bank gender data portals (comparative)",
                        "url": "https://genderdata.worldbank.org/",
                    }
                ],
            },
            "muslim": {
                "claim": (
                    "Colonialism, oil politics, and dictatorship explain much; Islam itself enabled "
                    "property rights earlier than Europe. Muslim feminists reclaim texts against patriarchy."
                ),
                "case": (
                    "Amina Wadud / progressive tafsir currents; majority-Muslim countries vary widely. "
                    "Essentializing 'Islam' from worst states is bigotry dressed as debate."
                ),
                "sources": [
                    {"label": "Qur'an 4:32", "url": "https://quran.com/4/32"},
                    {
                        "label": "World Bank gender data",
                        "url": "https://genderdata.worldbank.org/",
                    },
                ],
            },
            "counter_to_christian": "Secularization and liberal philosophy, not Nicene dogma alone, drove many reforms.",
            "counter_to_muslim": "If variance is huge, opponents may still ask which textual defaults resist equality.",
            "crux": "How much may modern outcomes count in a scripture-and-tradition debate?",
            "debate_use": "Cap sociology at 2 minutes unless motion is about contemporary policy.",
        },
    ],
    "materials": [],
    "debates": [],
    "opponent_cards": [
        {
            "trigger": "Islam hates women — look at 4:34",
            "fast_answer": "Steelman first: spiritual equality texts, property rights, anti-abuse readings. Then press what ḍarb authorized.",
            "follow_up": "Ask for their tafsir, not only a meme translation.",
            "sources": ["https://quran.com/4/34", "https://quran.com/33/35"],
        },
        {
            "trigger": "Christianity liberated women; Jesus vs Muhammad",
            "fast_answer": "Grant Gospel dignity moves. Then ask about 1 Tim 2, Eph 5, and centuries without women's rights.",
            "follow_up": "Force same-genre comparison: law vs law.",
            "sources": ["Ephesians 5", "1 Timothy 2:11–15"],
        },
        {
            "trigger": "Muslims can have four wives",
            "fast_answer": "Conditional permission + justice requirement + 4:129. Still defend/critique the asymmetry honestly.",
            "follow_up": "Mention OT polygyny if Christian uniqueness is claimed.",
            "sources": ["https://quran.com/4/3", "https://quran.com/4/129"],
        },
        {
            "trigger": "Women are deficient in intelligence (hadith)",
            "fast_answer": "Widely cited; contested in interpretation (legal testimony context vs ontology). Don't pretend it isn't a problem passage.",
            "follow_up": "Pair with Qur'anic intellectual agency examples; ask opponent's ḥadīth hermeneutic.",
            "sources": ["Bukhari 304 discussions", "https://quran.com/2/282"],
        },
        {
            "trigger": "Hijab is oppression",
            "fast_answer": "Specify voluntary vs coerced. Critique coercion; don't erase believing women's agency.",
            "follow_up": "Ask if they also call nuns' habits oppression.",
            "sources": ["https://quran.com/24/31"],
        },
        {
            "trigger": "Galatians 3:28 settles Christian egalitarianism",
            "fast_answer": "Powerful trajectory text — and complementarians restrict it to salvation status. Don't overclaim consensus.",
            "follow_up": "Ask Catholic/Orthodox interlocutors about orders.",
            "sources": ["https://www.biblegateway.com/passage/?search=Galatians+3%3A28&version=NRSVUE"],
        },
        {
            "trigger": "Women inherit half, so they are half worth",
            "fast_answer": "Classical ʿillah: financial obligations differ. Challenge whether that package still fits — without the 'half person' slur.",
            "follow_up": "Ask about female-only estates and other cases where shares equalize.",
            "sources": ["https://quran.com/4/11", "https://quran.com/4/7"],
        },
        {
            "trigger": "Aisha was a child bride",
            "fast_answer": "Hadith reports are central and morally explosive by modern standards; historicize carefully without glib dismissal or unique demonization (ancient marriage ages elsewhere).",
            "follow_up": "Keep focus on enduring law if motion is systemic ethics.",
            "sources": ["Bukhari marriage-age reports", "historical demography caution"],
        },
        {
            "trigger": "Mary proves Islam honors women more",
            "fast_answer": "Qur'an honors Maryam highly. Honor ≠ equal divorce/testimony rights. Don't let poetry replace law.",
            "follow_up": "Affirm 3:42 then return to 4:34/4:3.",
            "sources": ["https://quran.com/3/42"],
        },
        {
            "trigger": "Christianity invented patriarchy",
            "fast_answer": "Patriarchy is older than both. Score reforms and residuals in each system.",
            "follow_up": "Ask for the earliest legal right each scripture clearly grants women.",
            "sources": ["Comparative ancient Near East / late antique law"],
        },
    ],
    "checklist": [
        "Define equality vs identical legal roles in opening",
        "Comparison class: Gospels vs sīrah? Canon law vs fiqh? Modern majorities?",
        "Master 33:35, 4:3, 4:34, 4:11, 2:282 and John 20 / Matt 19 / Eph 5",
        "Prepare steelman of 4:34 constraint readings before attacking",
        "Prepare steelman of Christian historical patriarchy before praising Jesus",
        "Separate hijab piety from state coercion",
        "Decide concessions on both sides (name two each)",
        "Drill opponent cards; avoid cheap 'Islam hates women' openers",
        "Timebox Aisha age debate unless specifically raised",
        "Closing on crux: package justice vs equal civic personhood",
        "Bring one feminist Muslim scholarly source and one complementarian Christian source",
        "No outcome Olympics without data standards",
    ],
    "positive_cases": {
        "Christian podium": [
            "Jesus' discipleship of women and resurrection witness pattern",
            "Monogamy trajectory and husband-love ethic as marital ideal",
            "Wider modern institutional path to women's ordination/legal equality in many churches",
            "Hard problems in 4:34, polygyny, and asymmetric family law",
        ],
        "Muslim podium": [
            "Explicit spiritual equality (33:35) and property/inheritance rights as reform",
            "Mahr, consent norms, and divorce regulation as material protections",
            "Maryam's Qur'anic honor without deification",
            "Christian household codes and historic legal patriarchy block innocence narratives",
        ],
        "Unity / steelman": [
            "Both inherit late-antique patriarchy; ask who reforms what and how",
            "Refuse comparisons that stack best Jesus stories against worst Muslim regimes",
            "Center women's agency voices from both traditions",
            "Distinguish worth before God from courtroom identicality",
        ],
    },
    "bibliography": [
        {
            "tier": "Primary",
            "items": [
                {"label": "Qur'an 4:3; 4:34; 4:11; 4:32; 33:35; 24:30–31", "url": "https://quran.com/4/34"},
                {"label": "John 20; Matthew 19; Ephesians 5; Galatians 3:28", "url": "https://www.biblegateway.com/passage/?search=Galatians+3%3A28&version=NRSVUE"},
            ],
        },
        {
            "tier": "Reference / academic gateways",
            "items": [
                {"label": "Tafheem 4:34", "url": "https://islamicstudies.info/tafheem.php?sura=4&verse=34"},
                {"label": "CCC marriage / orders portals", "url": "https://www.vatican.va/archive/ENG0015/_INDEX.HTM"},
                {"label": "Yaqeen Institute", "url": "https://yaqeeninstitute.org/"},
                {"label": "World Bank Gender Data", "url": "https://genderdata.worldbank.org/"},
            ],
        },
    ],
}


def topic():
    from .deepen_lib import apply_overlays
    from .ethics_deep import WOMEN
    return apply_overlays(DATA, WOMEN)
