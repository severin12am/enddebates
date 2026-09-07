# -*- coding: utf-8 -*-
"""Which tradition has better rules of warfare?"""

DATA = {
    "id": "warfare",
    "meta": {
        "title": "Christianity vs Islam: better rules of warfare?",
        "thesis": (
            "Comparing scriptural norms, classical just-war / siyar traditions, and historical practice, "
            "which faith's warfare ethic better constrains violence and protects non-combatants?"
        ),
        "purpose": (
            "Steelman just war, crusading history, Qur'anic jihad limits, and classical offensive jihad. "
            "Separate Jesus' personal ethic, Christendom law, Muhammad as statesman, and modern misuse."
        ),
        "warning": (
            "Define the comparison class: Jesus' sayings vs Muhammad's campaigns? Aquinas vs al-Shaybani? "
            "Modern catechism vs ISIS proof-texts? Mixing levels is how both sides cheat."
        ),
        "chips": ["ethics", "history", "just war", "jihad", "law"],
        "labels": {"christian": "Christian case", "muslim": "Muslim case"},
    },
    "definitions": [
        {
            "term": "Just war (ius ad bellum / in bello)",
            "precise": (
                "Western Christian-derived criteria for when war may be started and how it must be fought "
                "(legitimate authority, just cause, proportionality, discrimination, etc.)."
            ),
            "not": "Not identical with everything done by Christian empires.",
        },
        {
            "term": "Jihad",
            "precise": (
                "Struggle; in law often includes armed jihad with rules (siyar). Must specify defensive, "
                "offensive, spiritual, or polemical misuse."
            ),
            "not": "Not a synonym for terrorism or for any Muslim violence.",
        },
        {
            "term": "Non-combatant immunity",
            "precise": "Norm against intentionally targeting civilians, women, children, clergy, etc.",
            "not": "Not the same as zero collateral damage in siege warfare.",
        },
        {
            "term": "Abrogation / naskh (in war verses)",
            "precise": (
                "Claim that later Medinan fighting verses supersede earlier restraint — contested in "
                "scope among Muslim scholars."
            ),
            "not": "Do not assume one popular 'sword verse abrogates all peace' meme settles fiqh.",
        },
        {
            "term": "Christendom vs Jesus' ethic",
            "precise": (
                "Distinguish the Sermon on the Mount's personal enemy-love from later Christian "
                "political theology authorizing force."
            ),
            "not": "Christians may not hide crusade history behind Matthew 5 without argument.",
        },
        {
            "term": "Siyar",
            "precise": "Islamic international/military law genre (e.g. Shaybani) regulating war and peace.",
            "not": "Not identical with every raid narrative in the sīrah.",
        },
    ],
    "arguments": [
        {
            "id": "jesus-enemy-love",
            "rank": 1,
            "cluster": "Founding ethic",
            "title": "Jesus' enemy-love sets a higher bar than armed prophethood",
            "type": "ethics + theology",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "The founder forbids retaliatory violence and loves enemies (Matt 5:38–48); "
                    "Muhammad leads battles. The founding pattern favors Christianity."
                ),
                "case": (
                    "Matthew 26:52; John 18:36. Even when Christians later just-war theorize, the "
                    "canonical center is non-vengeance. Comparative ethics starts with the founder."
                ),
                "sources": [
                    {
                        "label": "Matthew 5:38–48",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+5%3A38-48&version=NRSVUE",
                    },
                    {
                        "label": "Matthew 26:52",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+26%3A52&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Jesus' ethic addresses personal disciples under occupation; Muhammad receives rules "
                    "for a polity facing war. Different roles, not moral failure — and OT holy war complicates Christian claims."
                ),
                "case": (
                    "Qur'an 22:39–40 permission to fight when expelled; 2:190 non-transgression. "
                    "Luke 22:36 and OT conquest narratives show biblical tradition is not pacifist-only."
                ),
                "sources": [
                    {"label": "Qur'an 22:39–40", "url": "https://quran.com/22/39-40"},
                    {"label": "Qur'an 2:190", "url": "https://quran.com/2/190"},
                    {
                        "label": "Luke 22:36",
                        "url": "https://www.biblegateway.com/passage/?search=Luke+22%3A36&version=NRSVUE",
                    },
                ],
            },
            "counter_to_christian": "Selective pacifism: ignore Joshua, Samuel, Revelation warfare imagery, and church history.",
            "counter_to_muslim": "If roles differ, say so — but then don't claim moral equivalence of founding examples without argument.",
            "crux": "Is the morally decisive datum the founder's personal violence profile or the mature legal ethic of each tradition?",
            "debate_use": "Force agreement on comparison class before scoring 'better.'",
        },
        {
            "id": "defensive-jihad",
            "rank": 2,
            "cluster": "Qur'anic norms",
            "title": "Qur'anic fighting is primarily defensive and limited",
            "type": "ethics + exegesis",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "9:5, 9:29, 8:39 and classical offensive jihad show expansionist religious war is structural, "
                    "not a modern distortion."
                ),
                "case": (
                    "Sword-verse rhetoric in apologetics; Maghāzī literature; classical manuals on inviting "
                    "then fighting unbelievers. 'Religion of peace' overclaims fail against sources."
                ),
                "sources": [
                    {"label": "Qur'an 9:5", "url": "https://quran.com/9/5"},
                    {"label": "Qur'an 9:29", "url": "https://quran.com/9/29"},
                    {
                        "label": "EJIL — Use of Force under Islamic Law",
                        "url": "https://academic.oup.com/ejil/article/24/1/343/438602",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Core permissions answer persecution and treaty-breaking; 2:190 and non-combatant "
                    "hadiths constrain excess; extremist readings violate classical limits."
                ),
                "case": (
                    "Tafsir tying 9:5 to specific hostile polytheist groups after pilgrimage season; "
                    "hadith forbidding killing women/children. Modern Muslim majorities reject ISIS proof-texting."
                ),
                "sources": [
                    {"label": "Qur'an 2:190", "url": "https://quran.com/2/190"},
                    {
                        "label": "Tafheem on 2:190",
                        "url": "https://islamicstudies.info/tafheem.php?sura=2&verse=190",
                    },
                    {
                        "label": "First Things — Challenging Radical Islam",
                        "url": "https://firstthings.com/challenging-radical-islam/",
                    },
                ],
            },
            "counter_to_christian": "Quoting 9:5 without asbāb al-nuzūl and without 9:6 safe-conduct is proof-text abuse.",
            "counter_to_muslim": "Classical offensive jihad theories exist; 'only defensive' is not the whole heritage.",
            "crux": "Do Medinan war verses authorize enduring offensive holy war or context-bound defense under limits?",
            "debate_use": "Put 2:190 and 9:5 side by side; demand a reconciliation theory from both.",
        },
        {
            "id": "noncombatants",
            "rank": 3,
            "cluster": "In bello",
            "title": "Non-combatant protections",
            "type": "ethics + law",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Just-war discrimination and modern Christian teaching (e.g. CCC) clearly forbid "
                    "targeting civilians; Islamic sources include harsher siege/slavery outcomes in practice."
                ),
                "case": (
                    "Aquinas ST II-II; CCC 2302–2317. Christians argue their mature doctrine aligns with "
                    "Geneva-like norms more cleanly."
                ),
                "sources": [
                    {
                        "label": "CCC 2302–2317 (safeguarding peace)",
                        "url": "https://www.vatican.va/archive/ENG0015/__P81.HTM",
                    },
                    {
                        "label": "Aquinas on war (New Advent)",
                        "url": "https://www.newadvent.org/summa/3040.htm",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Prophetic instructions forbid killing women, children, and often monks/hermits; "
                    "mutilation and treachery banned — a robust in-bello ethic early in history."
                ),
                "case": (
                    "Abu Bakr's reported directives; hadith collections on non-killing of non-combatants. "
                    "Christendom's massacres (Jerusalem 1099 etc.) undercut moral superiority narratives."
                ),
                "sources": [
                    {
                        "label": "Sahih Muslim 1744a (women/children)",
                        "url": "https://sunnah.com/muslim:1744a",
                    },
                    {
                        "label": "Yaqeen — Jihad, War & Peace (overview papers)",
                        "url": "https://yaqeeninstitute.org/",
                    },
                ],
            },
            "counter_to_christian": "Crusades, wars of religion, and colonial violence are part of the Christian record.",
            "counter_to_muslim": "Siege practice, enslavement of captives, and some ridda/khawārij treatments complicate the soft reading.",
            "crux": "Whose official norms better protect civilians — and how much do historical crimes discount the norms?",
            "debate_use": "Score norms and history on separate ballots.",
        },
        {
            "id": "just-war-tradition",
            "rank": 4,
            "cluster": "Legal traditions",
            "title": "Just war vs siyar as legal achievements",
            "type": "law + history",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Augustine–Aquinas–Vitoria–Grotius trajectory developed criteria that shaped modern "
                    "international law; that is a major moral-intellectual achievement."
                ),
                "case": (
                    "Legitimate authority, just cause, right intention, last resort, proportionality. "
                    "Muslims may parallel this, but Christian genealogy of ius gentium is historically central."
                ),
                "sources": [
                    {
                        "label": "SEP — War",
                        "url": "https://plato.stanford.edu/entries/war/",
                    },
                    {
                        "label": "Aquinas ST II-II Q.40",
                        "url": "https://www.newadvent.org/summa/3040.htm",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Siyar developed rules of treaties, safe-conduct (amān), and categories of combatants "
                    "centuries before Westphalia; Islamic law is not a late borrower of restraint."
                ),
                "case": (
                    "Shaybani's Siyar; amān in 9:6; treaty of Hudaybiyya as precedent. Comparative "
                    "legal history is not a Christian monopoly."
                ),
                "sources": [
                    {"label": "Qur'an 9:6 (safe-conduct)", "url": "https://quran.com/9/6"},
                    {
                        "label": "EJIL Islamic use of force",
                        "url": "https://academic.oup.com/ejil/article/24/1/343/438602",
                    },
                ],
            },
            "counter_to_christian": "Just war also rationalized conquest; genealogy ≠ moral purity.",
            "counter_to_muslim": "Classical dār al-Islām / dār al-ḥarb frames can encode permanent hostility.",
            "crux": "Which legal tradition better institutionalizes restraint as law rather than as piety alone?",
            "debate_use": "Compare Aquinas article and a siyar ruling side by side on civilian targeting.",
        },
        {
            "id": "apostasy-blasphemy-war",
            "rank": 5,
            "cluster": "Adjacent coercion",
            "title": "Religious coercion adjacent to warfare ethics",
            "type": "ethics + law",
            "popularity": "High",
            "christian": {
                "claim": (
                    "NT lacks a death penalty for apostasy; classical ridda law and blasphemy violence "
                    "worsen Islam's overall force-ethic score."
                ),
                "case": (
                    "Bukhari 6922 vs John 6:66–67 freedom to walk away. Even if war rules are comparable, "
                    "internal coercion matters."
                ),
                "sources": [
                    {"label": "Sahih al-Bukhari 6922", "url": "https://sunnah.com/bukhari:6922"},
                    {
                        "label": "John 6:66–69",
                        "url": "https://www.biblegateway.com/passage/?search=John+6%3A66-69&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "2:256 no compulsion; many modern scholars reject capital apostasy for private belief; "
                    "Christian history of heresy executions undercuts uniqueness claims."
                ),
                "case": (
                    "Ridda wars read as political rebellion; Inquisition/heresy laws show Christian "
                    "polities also fused religion and lethal force."
                ),
                "sources": [
                    {"label": "Qur'an 2:256", "url": "https://quran.com/2/256"},
                    {"label": "Qur'an 18:29", "url": "https://quran.com/18/29"},
                ],
            },
            "counter_to_christian": "Christendom enforced orthodoxy with violence for centuries.",
            "counter_to_muslim": "Reformist rejection of apostasy death is not identical with classical consensus.",
            "crux": "Should warfare ethics scoring include domestic religious coercion laws?",
            "debate_use": "If motion is 'rules of warfare,' park apostasy unless opponent opens it.",
        },
        {
            "id": "ot-holy-war",
            "rank": 6,
            "cluster": "Scripture symmetry",
            "title": "Old Testament ḥērem vs Qur'anic jihad",
            "type": "ethics + scripture",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "OT ḥērem is covenantal-historical and not the church's marching orders; the NT "
                    "reframes enemy treatment. Islam's war texts remain operative law in classical fiqh."
                ),
                "case": (
                    "Hermeneutical discontinuity: Joshua ≠ Jesus' mission. Muslim abrogation theories "
                    "keep fighting verses live in a way Christian supersession of ḥērem does not."
                ),
                "sources": [
                    {
                        "label": "Deuteronomy 20",
                        "url": "https://www.biblegateway.com/passage/?search=Deuteronomy+20&version=NRSVUE",
                    },
                    {
                        "label": "Matthew 5 enemy love",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+5%3A43-48&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "If Christians own the whole Bible, ḥērem is harsher than Qur'anic rules; "
                    "special pleading about 'that was then' must be available to Muslims too."
                ),
                "case": (
                    "1 Samuel 15; Deut 20. Comparative scripture ethics cannot baptize OT violence "
                    "while essentializing Qur'an 9."
                ),
                "sources": [
                    {
                        "label": "1 Samuel 15",
                        "url": "https://www.biblegateway.com/passage/?search=1+Samuel+15&version=NRSVUE",
                    },
                    {"label": "Qur'an 2:190–193", "url": "https://quran.com/2/190-193"},
                ],
            },
            "counter_to_christian": "Marcionism is heresy — the OT remains Christian scripture.",
            "counter_to_muslim": "Symmetry requires Muslims to allow Christian progressive revelation arguments.",
            "crux": "May each side restrict operative war ethics to later revelation/hermeneutics?",
            "debate_use": "Demand parallel hermeneutical rules before comparing bloodiest texts.",
        },
        {
            "id": "crusades-colonialism",
            "rank": 7,
            "cluster": "History",
            "title": "Crusades, colonialism, and Maghāzī",
            "type": "history",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Crusades are often politically complex and not simple 'kill all Muslims' doctrine; "
                    "Islamic conquests and slave-raiding likewise. Founder-level ethics still differ."
                ),
                "case": (
                    "Acknowledge sins of Christendom while arguing they violate Jesus more clearly than "
                    "expansionist jihad violates Muhammad's model."
                ),
                "sources": [
                    {
                        "label": "CCC on peace / unjust war themes",
                        "url": "https://www.vatican.va/archive/ENG0015/__P81.HTM",
                    }
                ],
            },
            "muslim": {
                "claim": (
                    "Crusader massacres and later colonial wars under Christian symbols destroy claims "
                    "of uniquely peaceful Christian civilization."
                ),
                "case": (
                    "Jerusalem 1099 narratives; Reconquista; modern wars. Moral scoreboards that ignore "
                    "Christian violence are apologetic, not historical."
                ),
                "sources": [
                    {
                        "label": "Internet Medieval Sourcebook — Crusades",
                        "url": "https://sourcebooks.fordham.edu/sbook1k.asp",
                    }
                ],
            },
            "counter_to_christian": "If practice can indict Islam, it can indict Christianity.",
            "counter_to_muslim": "If practice can indict Christianity, cite Islamic conquest violence too.",
            "crux": "Do historical crimes refute a tradition's rules, or only its faithfulness?",
            "debate_use": "Propose: norms 50%, founder 30%, civilizational practice 20% — then argue weights.",
        },
        {
            "id": "prisoners-spoils",
            "rank": 8,
            "cluster": "In bello",
            "title": "Prisoners, spoils, and slavery in war",
            "type": "ethics + law",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Regulating slavery and sex with captives (e.g. debates on mā malakat aymānukum) "
                    "is a moral deficit relative to Gospel trajectory toward liberation."
                ),
                "case": (
                    "Qur'an 33:50; 4:24 debates; classical fiqh on captives. Christians argue NT seedbed "
                    "abolishes the category over time more cleanly."
                ),
                "sources": [
                    {"label": "Qur'an 4:24", "url": "https://quran.com/4/24"},
                    {
                        "label": "Philemon (status of Onesimus)",
                        "url": "https://www.biblegateway.com/passage/?search=Philemon+1&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Islam regulated and incentivized manumission in a slave economy universal to late antiquity; "
                    "Christian canon also assumes slavery (Eph 6; Col 3)."
                ),
                "case": (
                    "90:13; 24:33. Comparative ancient ethics: both inherit slavery; Islam's war-captive "
                    "rules are of their time, not uniquely evil."
                ),
                "sources": [
                    {"label": "Qur'an 90:12–13", "url": "https://quran.com/90/12-13"},
                    {
                        "label": "Ephesians 6:5–9",
                        "url": "https://www.biblegateway.com/passage/?search=Ephesians+6%3A5-9&version=NRSVUE",
                    },
                ],
            },
            "counter_to_christian": "Christian slaveholding lasted into modernity with biblical defense.",
            "counter_to_muslim": "Regulation is not abolition; moral progress claims need clear trajectory.",
            "crux": "Is regulating war-captive slavery better, worse, or equal to NT household codes?",
            "debate_use": "Keep this argument from swallowing the whole warfare motion — timebox it.",
        },
        {
            "id": "terrorism-takfir",
            "rank": 9,
            "cluster": "Modern misuse",
            "title": "Modern terrorism and proof-texting",
            "type": "ethics + contemporary",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Jihadist groups cite mainstream-accessible texts; the recurrence suggests a "
                    "textual vulnerability Christianity's NT center lacks."
                ),
                "case": (
                    "9:5/9:29 in extremist literature. Christian terrorists usually contradict Jesus more blatantly."
                ),
                "sources": [
                    {"label": "Qur'an 9:5; 9:29", "url": "https://quran.com/9/5"},
                    {
                        "label": "NAMB — Islam and Violence",
                        "url": "https://www.namb.net/apologetics/resource/islam-and-violence/",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Takfīrī terrorism violates siyar, targets civilians, and is condemned by mainstream scholars; "
                    "guilt by extremist citation is like blaming Jesus for KKK misuse of the Bible."
                ),
                "case": (
                    "Open letters against ISIS; classical conditions for jihad (authority, non-combatant rules). "
                    "Method: misuse ≠ meaning."
                ),
                "sources": [
                    {
                        "label": "Letter to Baghdadi (Open Letter)",
                        "url": "https://www.lettertobaghdadi.com/",
                    },
                    {"label": "Qur'an 5:32", "url": "https://quran.com/5/32"},
                ],
            },
            "counter_to_christian": "Christian nationalist violence and crusader romanticism also cite scripture.",
            "counter_to_muslim": "If mainstream classical law includes offensive jihad, 'extremist only' is incomplete.",
            "crux": "Are jihadist readings parasitic distortions or one authentic classical option?",
            "debate_use": "Ask for named madhhab positions, not only Twitter scholars.",
        },
        {
            "id": "proportionality-treaties",
            "rank": 10,
            "cluster": "Qur'anic norms",
            "title": "Treaties, reciprocity, and proportionality",
            "type": "ethics",
            "popularity": "Medium-high",
            "christian": {
                "claim": (
                    "Gospel enemy-love and just-war last resort/proportionality give a clearer path to "
                    "stable peace than expansionist jihad frames."
                ),
                "case": (
                    "Romans 12:17–21; just-war manuals. Peace is not merely temporary hudna pending strength."
                ),
                "sources": [
                    {
                        "label": "Romans 12:17–21",
                        "url": "https://www.biblegateway.com/passage/?search=Romans+12%3A17-21&version=NRSVUE",
                    },
                    {"label": "SEP War", "url": "https://plato.stanford.edu/entries/war/"},
                ],
            },
            "muslim": {
                "claim": (
                    "Qur'an commands fulfillment of covenants (9:4; 16:91) and incline to peace if enemy inclines (8:61); "
                    "Hudaybiyya shows strategic peacemaking."
                ),
                "case": (
                    "Treaty ethics are central. 8:61 is a high-water mark for reciprocal de-escalation."
                ),
                "sources": [
                    {"label": "Qur'an 8:61", "url": "https://quran.com/8/61"},
                    {"label": "Qur'an 16:91", "url": "https://quran.com/16/91"},
                    {"label": "Qur'an 9:4", "url": "https://quran.com/9/4"},
                ],
            },
            "counter_to_christian": "Christian states broke treaties constantly; norms ≠ compliance.",
            "counter_to_muslim": "Debates on whether 8:61 is abrogated by later sūrah 9 must be faced honestly.",
            "crux": "Is peace a stable end-state in each ethic, or a pause in religious struggle?",
            "debate_use": "Ask both: name conditions for ending war permanently with a non-co-religionist state.",
        },
    ],
    "materials": [],
    "debates": [
        {
            "id": "wood-ally-violence",
            "title": "Islam and violence debates (Wood / Ally pattern)",
            "year": None,
            "venue": "Public apologetics",
            "participants": ["David Wood", "Shabir Ally"],
            "sides": {"christian": "David Wood", "muslim": "Shabir Ally"},
            "motion": "Is Islam a religion of peace / how violent are the sources?",
            "summary": (
                "Wood stacks Medinan war texts and sīrah; Ally stresses context, defensive reading, "
                "and Christian violence history."
            ),
            "what_to_steal": [
                "Always define jihad before quoting",
                "Separate Muhammad's battles from ISIS",
                "Bring OT ḥērem when sword verses appear",
            ],
            "links": [
                {
                    "label": "EJIL academic framing",
                    "url": "https://academic.oup.com/ejil/article/24/1/343/438602",
                }
            ],
        }
    ],
    "opponent_cards": [
        {
            "trigger": "Islam is a religion of peace — period",
            "fast_answer": "Ask which texts and which legal school. Peaceful Muslims ≠ settled classical doctrine on offensive jihad.",
            "follow_up": "Offer: many verses command restraint — and some authorize fighting. Both are in the sources.",
            "sources": ["https://quran.com/2/190", "https://quran.com/9/29", "EJIL article"],
        },
        {
            "trigger": "Kill the pagans wherever you find them (9:5)",
            "fast_answer": "Context: specific treaty-breakers after sacred months; 9:6 grants protection if they seek it. Still debate scope — but not a cartoon.",
            "follow_up": "Ask if they apply the same literal forever-reading to Deut 20.",
            "sources": ["https://quran.com/9/5", "https://quran.com/9/6"],
        },
        {
            "trigger": "Jesus said turn the other cheek, so Christianity wins",
            "fast_answer": "Personal ethic vs state ethic. Ask about just war, soldiers in NT, and OT. Comparison class matters.",
            "follow_up": "Grant the Sermon's radicalness; then ask how Christian empires should be scored.",
            "sources": ["Matthew 5", "CCC 2302–2317"],
        },
        {
            "trigger": "Crusades prove Christianity is worse",
            "fast_answer": "Crimes count against practice. They don't automatically make Qur'anic war rules gentler. Score both.",
            "follow_up": "Ask for Islamic conquest counter-examples they accept as parallel.",
            "sources": ["Fordham crusades sourcebook"],
        },
        {
            "trigger": "Jihad just means inner struggle",
            "fast_answer": "Greater/lesser jihad rhetoric exists, but fiqh books regulate armed jihad extensively. Don't erase that.",
            "follow_up": "Define which sense is used in tonight's motion.",
            "sources": ["EJIL", "siyar overviews"],
        },
        {
            "trigger": "Muhammad was a warlord, not a prophet",
            "fast_answer": "That's a conclusion. First compare roles: Jesus non-state teacher vs Moses/David-like lawgiver-leader.",
            "follow_up": "Ask if Moses fails the same test.",
            "sources": ["Qur'an 22:39", "Exodus/Deuteronomy war laws"],
        },
        {
            "trigger": "Just war is just Christian spin for violence",
            "fast_answer": "It can be abused. It also supplies criteria to condemn abusive wars — including Christian ones.",
            "follow_up": "Ask which criterion they reject: discrimination? proportionality?",
            "sources": ["https://plato.stanford.edu/entries/war/"],
        },
        {
            "trigger": "Muslims must fight until all religion is for Allah (8:39)",
            "fast_answer": "Exegetes dispute whether this means end persecution/fitnah or global forced conversion. Force a tafsir.",
            "follow_up": "Pair with 2:256 and 8:61.",
            "sources": ["https://quran.com/8/39", "https://quran.com/2/256", "https://quran.com/8/61"],
        },
        {
            "trigger": "Christianity caused more deaths in history",
            "fast_answer": "Body-count debates depend on centuries, technology, and demography. Prefer norms + founder + representative law.",
            "follow_up": "Refuse unfalsifiable genocide Olympics unless data standards are set.",
            "sources": ["Historical methodology caution"],
        },
        {
            "trigger": "ISIS follows true Islam",
            "fast_answer": "They claim to. Mainstream Open Letter and classical non-combatant rules say they don't. Ask for your opponent's usūl.",
            "follow_up": "Still press classical offensive jihad if that's the real target.",
            "sources": ["https://www.lettertobaghdadi.com/"],
        },
    ],
    "checklist": [
        "Lock comparison class: founder / scripture / classical law / modern teaching",
        "Prepare 60-second definitions: just war, jihad, non-combatant, abrogation",
        "Master 2:190, 8:61, 9:5–6, 9:29 and Matt 5 / Matt 26:52",
        "Prepare OT ḥērem symmetry move and Christian discontinuity reply",
        "Separate in bello rules from ad bellum expansion questions",
        "Decide concessions: Crusades; classical offensive jihad",
        "Drill 10 opponent cards; first line live-ready",
        "Bring Aquinas Q.40 + one siyar/EJIL receipt",
        "Score norms and history separately in closing",
        "No slogan closings: 'religion of peace' or 'Jesus vs warlord' without crux",
        "Timebox slavery/apostasy digressions unless motion includes them",
        "Ask opponent to state conditions for permanent peace with the other faith's polity",
    ],
    "positive_cases": {
        "Christian podium": [
            "Founder's enemy-love and rejection of sword-retaliation is a unique moral center",
            "Just-war criteria (discrimination, proportionality, last resort) are a high legal achievement",
            "NT lacks an apostolic program of religious conquest",
            "Medinan expansionist texts and classical offensive jihad are structural challenges for Islam",
        ],
        "Muslim podium": [
            "Early, explicit non-combatant protections and amān/treaty ethics",
            "Permission to fight answers persecution; 2:190 and 8:61 constrain aggression",
            "Siyar is a mature laws-of-war tradition, not chaos",
            "Christian scripture and history contain ḥērem, crusade, and holy-war practice — no innocence narrative",
        ],
        "Unity / steelman": [
            "Both traditions contain restraint norms and violent chapters — punish proof-texting",
            "Agree on comparison class before scoring",
            "Condemn civilian-targeting terrorism as betrayal of the best in both",
            "Use legal classics (Aquinas, siyar) not only atrocity headlines",
        ],
    },
    "bibliography": [
        {
            "tier": "Academic / legal",
            "items": [
                {"label": "SEP — War", "url": "https://plato.stanford.edu/entries/war/"},
                {"label": "EJIL — Use of Force under Islamic Law", "url": "https://academic.oup.com/ejil/article/24/1/343/438602"},
                {"label": "Aquinas ST II-II Q.40", "url": "https://www.newadvent.org/summa/3040.htm"},
                {"label": "CCC 2302–2317", "url": "https://www.vatican.va/archive/ENG0015/__P81.HTM"},
            ],
        },
        {
            "tier": "Primary",
            "items": [
                {"label": "Qur'an 2:190–193; 8:61; 9:5–6; 9:29; 22:39–40", "url": "https://quran.com/2/190-193"},
                {"label": "Matthew 5:38–48; 26:52", "url": "https://www.biblegateway.com/passage/?search=Matthew+5%3A38-48&version=NRSVUE"},
                {"label": "Sahih Muslim 1744a", "url": "https://sunnah.com/muslim:1744a"},
            ],
        },
        {
            "tier": "Contemporary",
            "items": [
                {"label": "Letter to Baghdadi", "url": "https://www.lettertobaghdadi.com/"},
                {"label": "Tafheem 2:190", "url": "https://islamicstudies.info/tafheem.php?sura=2&verse=190"},
            ],
        },
    ],
}


def topic():
    from .deepen_lib import apply_overlays
    from .ethics_deep import WARFARE
    return apply_overlays(DATA, WARFARE)
