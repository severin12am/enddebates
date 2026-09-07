# -*- coding: utf-8 -*-
"""Israel–Palestine: steelmanned national claims, law, and history — not a religion scorecard."""
from .deepen_lib import D, Q, S, apply_overlays

DATA = {
    "id": "israel-palestine",
    "meta": {
        "title": "Israel–Palestine: the 10 arguments that actually matter",
        "thesis": (
            "Two peoples claim the same land with overlapping histories of indigeneity, displacement, "
            "war, and law. Which claims survive when you separate 1948 from 1967, civilians from armed "
            "factions, and self-determination from holy-war slogans?"
        ),
        "purpose": (
            "Live-debate prep: competing national claims, 1947–49, occupation and settlements, refugees, "
            "Jerusalem, armed factions, Gaza/Oct 7, international law, end-states, and poison words. "
            "Columns are national cases, not 'Judaism vs Islam.'"
        ),
        "warning": (
            "This is not a religion-winner page. Many Palestinians are Christian; many Israeli critics are Jewish. "
            "Define: occupation, refugee, genocide, apartheid, terrorism, resistance, from the river to the sea. "
            "Atrocity ping-pong without a timeline is not an argument."
        ),
        "chips": ["national claims", "law", "1948 / 1967", "Gaza", "live debate"],
        "labels": {
            "israel": "Israeli / Zionist case",
            "palestine": "Palestinian case",
        },
        "side_keys": ["israel", "palestine"],
    },
    "definitions": [
        {
            "term": "Zionism",
            "precise": "Jewish national self-determination in part of the historic Land of Israel; varieties range from liberal two-state Zionism to maximalist/religious forms.",
            "not": "Not identical with 'all Jews,' 'Judaism,' or every Israeli government policy.",
        },
        {
            "term": "Palestinian people",
            "precise": "Arabic-speaking people of historic Palestine with a modern national identity (crystallized especially in the 20th century) claiming self-determination in that land.",
            "not": "Not 'there are no Palestinians' — that slogan is a debate own-goal, not a history paper.",
        },
        {
            "term": "Occupation (law)",
            "precise": "In IHL, effective control of territory by a hostile army. UN majority and ICJ treat West Bank (and often Gaza, contested) as occupied; Israel disputes Gaza post-2005 and some WB legal theories (disputed vs occupied).",
            "not": "Not a synonym for 'all of Israel inside the Green Line is occupied' unless you argue 1948 that way explicitly.",
        },
        {
            "term": "Nakba / Independence",
            "precise": "1947–49: UN partition, Arab rejection, war, ~700k Palestinian refugees, Israeli statehood, and Jewish refugees from Arab countries as a paired file.",
            "not": "Not a single massacre clip, and not a immaculate volunteer transfer.",
        },
        {
            "term": "Two-state vs one-state",
            "precise": "End-state: partition into Israel + Palestine, or one polity (binational, federative, or winner-take-all).",
            "not": "Not the same as a ceasefire, and not the same as 'from the river to the sea' as a chant until you define the rights of the losing people.",
        },
        {
            "term": "Terrorism / resistance",
            "precise": "Must specify target: combatants vs civilians; and authority: state army vs non-state group. Law of armed conflict still binds both.",
            "not": "Not 'whatever my side does is resistance and whatever yours does is terror.'",
        },
    ],
    "arguments": [
        {
            "id": "self-determination",
            "rank": 1,
            "cluster": "National claims",
            "title": "Two self-determination claims on one land",
            "type": "history + politics",
            "popularity": "Very high",
            "why_it_matters": "If you deny one people is a people, you are not doing 2026 politics — you are doing erasure. If you deny the other has any tie, same sin.",
            "israel": {
                "claim": "Jews are a people with continuous historical, liturgical, and demographic ties to the land, entitled to self-determination after millennia of exile and modern persecution, including the Holocaust.",
                "case": (
                    "Hebrew kingdoms, Second Temple, continuous minority presence, 19th–20th c. national revival, Balfour (1917), "
                    "League of Nations Mandate recognizing a Jewish national home, Holocaust as proof that minority status in Europe was lethal. "
                    "UNGA 181 proposed partition as the legal-political compromise among two national claims."
                ),
                "quotes": [
                    Q(
                        "His Majesty's Government view with favour the establishment in Palestine of a national home for the Jewish people… it being clearly understood that nothing shall be done which may prejudice the civil and religious rights of existing non-Jewish communities in Palestine…",
                        "Balfour Declaration",
                        "2 November 1917",
                        "https://www.nationalarchives.gov.uk/education/resources/balfour-declaration/",
                    ),
                ],
                "data_points": [
                    D("League of Nations Mandate for Palestine (1922) incorporated the Balfour policy in international law of the time.", "Avalon / UN documentation", "https://avalon.law.yale.edu/20th_century/palmanda.asp"),
                    D("UNGA Resolution 181 (II), 29 Nov 1947: partition into Arab and Jewish states with economic union and a special Jerusalem regime.", "UN", "https://www.un.org/unispal/document/auto-insert-185393/"),
                ],
                "sources": [
                    S("Balfour Declaration (UK National Archives)", "https://www.nationalarchives.gov.uk/education/resources/balfour-declaration/"),
                    S("UNGA 181", "https://www.un.org/unispal/document/auto-insert-185393/"),
                ],
            },
            "palestine": {
                "claim": "Arabic-speaking inhabitants were the majority of Ottoman/Mandate Palestine; their self-determination cannot be subordinated to a settler-national project backed by imperial Britain.",
                "case": (
                    "By the late Ottoman and Mandate censuses, Muslims and Christians were the large majority. Wilsonian self-determination after WWI was applied unevenly. "
                    "The Mandate's Jewish-national-home clause is, on this view, a colonial override of the indigenous majority. Palestinian nationalism is a normal 20th-c. anti-colonial nation, not a later invention to annoy Jews."
                ),
                "quotes": [
                    Q(
                        "Nothing shall be done which may prejudice the civil and religious rights of existing non-Jewish communities in Palestine.",
                        "Balfour Declaration (the clause Palestinians cite as broken)",
                        "2 November 1917",
                        "https://www.nationalarchives.gov.uk/education/resources/balfour-declaration/",
                    ),
                ],
                "data_points": [
                    D("Mandate-era majority was Arab; Jewish population grew rapidly via immigration under the Mandate, which Arabs experienced as demographic conquest.", "Standard Mandate demography summaries (McCarthy / Abu Lughod debates exist — cite a source, don't meme)"),
                    D("Article 22 of the League Covenant spoke of peoples not yet able to stand by themselves — Palestinians argue they were placed under a Mandate that privileged another nation.", "League Covenant Art. 22"),
                ],
                "sources": [
                    S("UN: Origins and Evolution of the Palestine Problem", "https://www.un.org/unispal/history/"),
                ],
            },
            "counters": [
                {
                    "against": "Israeli 'no Palestinian people'",
                    "claim": "Palestine was empty / Palestinians are just southern Syrians.",
                    "reply": "Peoplehood is political and historical, not a DNA test. By the mid-20th century a Palestinian national claim is as real as other post-Ottoman nations. Erasure loses the room.",
                },
                {
                    "against": "Palestinian 'pure settler-colony, zero Jewish peoplehood'",
                    "claim": "Israel is only Europe in the Middle East.",
                    "reply": "Mizrahi/Sephardi Jews, continuous presence, and Hebrew antiquity are real. Settler-colonial theory can describe 20th-c. immigration without deleting Jewish peoplehood. Both/and is harder and truer.",
                },
            ],
            "live": {
                "if_they_say": "It's simple: one side is indigenous, the other is not.",
                "you_say": "Both have indigeneity stories that are not nothing. The live question is how two self-determination claims share one land — partition, federation, or elimination. Elimination slogans are the tell.",
                "dont_overclaim": "Don't do 'Palestinians didn't exist in 1800' as a mic drop. Don't do 'Jews have no connection' as a mic drop.",
            },
            "crux": "Are both peoples entitled to self-determination in this land, and what map does that imply?",
            "debate_use": "Force a yes/no: does the other people get a political existence, or only mercy?",
        },
        {
            "id": "1948",
            "rank": 2,
            "cluster": "1947–49",
            "title": "1947–49: partition, war, Nakba, independence",
            "type": "history",
            "popularity": "Very high",
            "why_it_matters": "Every later argument smuggles a 1948 morality play. Split military history from ethnic cleansing debates from legal title.",
            "israel": {
                "claim": "Jewish leadership accepted UNGA 181; Arab states and the Palestinian leadership rejected partition and launched/joined a war to prevent a Jewish state; Israel survived and the refugee outcome is war, not a unique original sin.",
                "case": (
                    "Nov 1947 partition → civil war → May 1948 Arab state invasion. Benny Morris (not a hasbara pamphlet) documents both expulsions and flight. "
                    "Jewish communities in Arab countries were also emptied in the following years — a dual refugee story often omitted."
                ),
                "quotes": [
                    Q(
                        "The [UN Special] Committee recommends… partition.",
                        "UNSCOP / UNGA 181 framework (paraphrase of the adopted plan)",
                        "UNGA Resolution 181 (II)",
                        "https://www.un.org/unispal/document/auto-insert-185393/",
                    ),
                ],
                "data_points": [
                    D("~700,000 Palestinian refugees in 1947–49 is the standard order of magnitude in UN/UNRWA origin stories.", "UNRWA / UN figures"),
                    D("Hundreds of thousands of Jews left or were driven from Arab countries after 1948; most were absorbed by Israel.", "Standard demographic histories (still argue numbers honestly)"),
                ],
                "sources": [
                    S("UNGA 181 text", "https://www.un.org/unispal/document/auto-insert-185393/"),
                    S("Benny Morris, 1948 (overview)", "https://yalebooks.yale.edu/book/9780300151125/1948/"),
                ],
            },
            "palestine": {
                "claim": "Partition awarded a minority a disproportionate share; Plan Dalet and massacres (Deir Yassin) show expulsion was policy or at least a foreseeable machine of war; the Nakba is the founding injustice, not a weather event.",
                "case": (
                    "Walid Khalidi and Ilan Pappé argue ethnic cleansing / transfer thinking was Zionist strategy, not an accident. "
                    "UNGA 194 (III) §11: refugees 'wishing to return to their homes and live at peace with their neighbours should be permitted to do so.' Israel blocked return."
                ),
                "quotes": [
                    Q(
                        "…the refugees wishing to return to their homes and live at peace with their neighbours should be permitted to do so at the earliest practicable date, and that compensation should be paid for the property of those choosing not to return…",
                        "UNGA Resolution 194 (III), paragraph 11",
                        "11 December 1948",
                        "https://www.un.org/unispal/document/auto-insert-184159/",
                    ),
                ],
                "data_points": [
                    D("Deir Yassin (9 April 1948) is the emblematic massacre in Palestinian memory; casualty figures and Irgun/Lehi vs Haganah roles are still argued — don't invent a number, cite a historian.", "Morris / Khalidi file"),
                    D("Hundreds of Palestinian villages were depopulated; mapping projects (e.g. Khalidi's All That Remains) are the documentary backbone.", "Institute for Palestine Studies"),
                ],
                "sources": [
                    S("UNGA 194 (III)", "https://www.un.org/unispal/document/auto-insert-184159/"),
                    S("UNRWA: Palestine refugees", "https://www.unrwa.org/palestine-refugees"),
                ],
            },
            "counters": [
                {
                    "against": "Israeli 'they started it so anything follows'",
                    "claim": "Rejecting 181 makes the Nakba the Arabs' fault entirely.",
                    "reply": "War explains refugees; it does not automatically license every expulsion or bar every return. Cause of war and justice of specific expulsions are two questions.",
                },
                {
                    "against": "Palestinian 'immaculate victimhood'",
                    "claim": "Zionists did all the violence; Arabs never attacked.",
                    "reply": "1947–48 was a two-sided civil war then a state-to-state war. Civilian flight, expulsions, and massacres occurred. A one-villain timeline will be shredded by Morris-level detail.",
                },
            ],
            "live": {
                "if_they_say": "Israel was created by stealing the land in 1948.",
                "you_say": "Ask: partition share vs war vs expulsions vs no-return. Those are four claims. Then put UNGA 181, 194, and the Jewish-refugee file on the same table.",
                "dont_overclaim": "Don't say nobody was expelled. Don't say it was only a tourist vacation that ended badly.",
            },
            "crux": "Was 1948 a defensive war of survival, an ethnic-cleansing founding, or a brutal mix — and what remedy follows 75 years later?",
            "debate_use": "Ban the word 'stole' until a mechanism is named: title, war, flight, massacre, or all.",
        },
        {
            "id": "1967-occupation",
            "rank": 3,
            "cluster": "Occupation",
            "title": "1967, occupation, UNSC 242, settlements",
            "type": "law + history",
            "popularity": "Very high",
            "why_it_matters": "You can grant 1948 Israel and still fight 1967. Mixing them is how debates become mush.",
            "israel": {
                "claim": "1967 was a defensive war; 242 calls for peace and secure boundaries, not a suicide shrink to Auschwitz lines; settlements are disputed legal theory plus security, not simple theft of a Palestinian state that did not exist there.",
                "case": (
                    "Egypt's closure of the Straits of Tiran, troop movements, and expulsion of UNEF preceded the war. "
                    "Israel: Gaza is not occupied since 2005 disengagement (contested). West Bank: belligerent occupation with unique title claims (disputed territory). "
                    "Settlements: Israeli legal advisers (e.g. 1967–68 debates) split; political right treats them as rightful."
                ),
                "quotes": [
                    Q(
                        "…Withdrawal of Israel armed forces from territories occupied in the recent conflict; Termination of all claims or states of belligerency and respect for and acknowledgement of the sovereignty, territorial integrity and political independence of every State in the area and their right to live in peace within secure and recognized boundaries…",
                        "UN Security Council Resolution 242",
                        "22 November 1967",
                        "https://www.un.org/securitycouncil/content/resolutions-adopted-security-council-1967",
                    ),
                ],
                "data_points": [
                    D("242 says 'territories' not 'the territories' in the English text — the famous article fight used to argue less-than-full withdrawal.", "English vs French text debate"),
                    D("Oslo Accords created Areas A/B/C; they did not freeze a final border.", "Oslo II (1995)"),
                ],
                "sources": [
                    S("UNSC 242 (UN page / text widely reproduced)", "https://peacemaker.un.org/israelopt-resolution242"),
                    S("ICRC: occupation", "https://www.icrc.org/en/doc/resources/documents/misc/634kfc.htm"),
                ],
            },
            "palestine": {
                "claim": "The West Bank, East Jerusalem, and Gaza are occupied Palestinian territory; settlements violate Art. 49(6) of the Fourth Geneva Convention; occupation has become annexation-by-facts.",
                "case": (
                    "UNSC 2334 (2016): settlements have no legal validity. ICJ 2004 Wall advisory opinion: occupation + wall route violate international law. "
                    "Settler violence and dual legal systems in the West Bank are the lived core, not a seminar on 242's missing 'the'."
                ),
                "quotes": [
                    Q(
                        "The Occupying Power shall not deport or transfer parts of its own civilian population into the territory it occupies.",
                        "Fourth Geneva Convention",
                        "Article 49(6)",
                        "https://ihl-databases.icrc.org/en/ihl-treaties/gciv-1949/article-49",
                    ),
                ],
                "data_points": [
                    D("UNSC 2334 (23 Dec 2016) condemns settlements as a flagrant violation under international law (US abstained).", "https://undocs.org/S/RES/2334(2016)"),
                    D("Settlement population in the West Bank (excluding East Jerusalem) is in the hundreds of thousands — cite the latest Peace Now / CBS figure in the room, don't freeze a 2010 number.", "Peace Now / Yesha Council competing counts"),
                ],
                "sources": [
                    S("ICJ 2004 Wall advisory opinion", "https://www.icj-cij.org/case/131"),
                    S("UNSC 2334", "https://undocs.org/S/RES/2334(2016)"),
                ],
            },
            "counters": [
                {
                    "against": "Israeli 'no occupation because no prior sovereign'",
                    "claim": "Jordan/Egypt weren't legitimate, so Geneva 49 doesn't apply.",
                    "reply": "Even if title is disputed, IHL occupation is about effective control of a hostile army over a population — most states and the ICJ still apply it. Argue the law; don't pretend the debate doesn't exist.",
                },
            ],
            "live": {
                "if_they_say": "The occupation is the whole conflict.",
                "you_say": "1967 is the occupation file. 1948 is a different file. Gaza after 2005 is a third (control of air/sea/borders vs boots). Don't let one word do three jobs.",
                "dont_overclaim": "Don't say settlements are just suburbs. Don't say every Israeli inside the Green Line is a settler unless you are openly anti-1948.",
            },
            "crux": "Does IHL occupation + Art. 49(6) describe the West Bank today, and what withdrawal/peace package 242 actually requires?",
            "debate_use": "Draw a map: Green Line, East Jerusalem, Area C, Gaza fence. Fingers on a map beat adjectives.",
        },
        {
            "id": "refugees",
            "rank": 4,
            "cluster": "Refugees",
            "title": "Refugees: UNRWA, return, and the Jewish exodus",
            "type": "law + ethics",
            "popularity": "Very high",
            "why_it_matters": "Right of return is either a human-rights core or a demographic veto on Israel as a Jewish state. Say which.",
            "israel": {
                "claim": "A unique hereditary UNRWA status plus a demand to 'return' into Israel (not a Palestinian state) is a plan to unwind 1948, unlike every other refugee file that was resettled; Jewish refugees from Arab lands were absorbed without a perpetual UN agency.",
                "case": (
                    "UNHCR vs UNRWA: descendant registration is the structural difference. Palestinian leadership historically tied return to the destruction of Israel's Jewish majority. "
                    "Peace packages (Camp David/Clinton parameters) offered a state + compensation + limited return; maximal return was rejected."
                ),
                "data_points": [
                    D("UNRWA registers descendants of 1948 refugees; critics call this unique, defenders call it normal for a still-stateless population.", "https://www.unrwa.org/palestine-refugees"),
                    D("Jewish refugees from Arab countries: order of magnitude ~800k in standard accounts used in this debate — verify the historian you cite.", "JJAC / academic estimates"),
                ],
                "sources": [
                    S("UNRWA: Palestine refugees", "https://www.unrwa.org/palestine-refugees"),
                    S("UNGA 194 §11", "https://www.un.org/unispal/document/auto-insert-184159/"),
                ],
            },
            "palestine": {
                "claim": "Refugee status continues because return and compensation in 194 §11 were never implemented; descendants remain stateless or camp-bound because the original expulsion/flight was not remedied, not because of a UN conspiracy.",
                "case": (
                    "Other refugees also have children. The uniqueness is the prohibition on return to homes now inside Israel, plus occupation blocking a state that could absorb them. "
                    "Individual return vs collective political return can be distinguished — but deleting 194 is deleting the UN's own paper."
                ),
                "quotes": [
                    Q(
                        "…the refugees wishing to return to their homes and live at peace with their neighbours should be permitted to do so…",
                        "UNGA 194 (III) §11",
                        "11 December 1948",
                        "https://www.un.org/unispal/document/auto-insert-184159/",
                    ),
                ],
                "data_points": [
                    D("Camps in Lebanon/Syria/Jordan/WB/Gaza are the empirical file: rights, employment bans (Lebanon), and UNRWA schools.", "UNRWA field reporting"),
                ],
                "sources": [
                    S("UNRWA", "https://www.unrwa.org/"),
                ],
            },
            "live": {
                "if_they_say": "Just let all refugees return, problem solved.",
                "you_say": "Return to a Palestinian state vs return to Jaffa/Haifa inside Israel are different proposals. One is two-state; the other is a one-state demographic strategy. Which are you arguing?",
                "dont_overclaim": "Don't mock camps. Don't pretend 194 is a bus ticket issued yesterday.",
            },
            "crux": "Is 'return' a family-level human right into 1948 Israel, a right into a future Palestine, compensation, or some mix?",
            "debate_use": "Force a number: how many people, to which side of the Green Line, with what citizenship.",
        },
        {
            "id": "jerusalem",
            "rank": 5,
            "cluster": "Holy city",
            "title": "Jerusalem and the holy sites",
            "type": "history + religion + law",
            "popularity": "Very high",
            "why_it_matters": "The city is where nationalism, archaeology, and worship collide. Temple Mount / Ḥaram al-Sharīf is a war-starting sentence if mishandled.",
            "israel": {
                "claim": "Jerusalem is the historical Jewish capital; 1967 reunified a city Jordan had ethnically cleansed of Jews (Old City, 1948–67); Jewish prayer rights on the Mount are still constrained; 181's corpus separatum is a dead letter after Arab rejection and war.",
                "case": (
                    "Western Wall access after 1967 is the Jewish core. Israeli law (1980 Basic Law: Jerusalem) asserts united capital. "
                    "Status quo: Jordan/Waqf administer the compound; Israel security control. Polls: Israeli mainstream will not re-divide the city as in 1948–67."
                ),
                "data_points": [
                    D("Jordanian period: Jewish access to the Old City/Western Wall was barred.", "1949 armistice practice / standard histories"),
                    D("UNGA 181 proposed an international corpus separatum for Jerusalem — never implemented.", "UNGA 181 Part III"),
                ],
                "sources": [
                    S("UNGA 181 Part III (Jerusalem)", "https://www.un.org/unispal/document/auto-insert-185393/"),
                ],
            },
            "palestine": {
                "claim": "East Jerusalem is occupied Palestinian territory; settlements in the east, home demolitions, and permit regimes are annexation; the Ḥaram is a Muslim holy site whose sovereignty cannot be Israeli without humiliation.",
                "case": (
                    "ICJ/UN majority: East Jerusalem occupied. Palestinian Christians and Muslims both have deep roots. "
                    "A capital in East Jerusalem is the Palestinian red line in every serious negotiation file (Oslo, Camp David, Taba, Kerry)."
                ),
                "data_points": [
                    D("Most states do not recognize Israeli sovereignty over East Jerusalem (embassy politics after 2018 is the exception file).", "UN / embassy map"),
                ],
                "sources": [
                    S("ICJ 2004 (includes East Jerusalem in occupied territory analysis)", "https://www.icj-cij.org/case/131"),
                ],
            },
            "live": {
                "if_they_say": "Jerusalem is Jewish / Jerusalem is Muslim, period.",
                "you_say": "It is historically Jewish, Christian, and Muslim. The live question is sovereignty, municipal rights, and access — not a monopoly on holiness. Split Old City holy basin from modern neighborhoods if you want a deal-shaped sentence.",
                "dont_overclaim": "Don't deny the Temple. Don't deny the Ḥaram. Don't make 2026 policy out of a crusade sermon.",
            },
            "crux": "Can both nations have a capital in Jerusalem without one owning the compound as a humiliation prize?",
            "debate_use": "Use a map of the Old City. Name the status quo. Then argue change.",
        },
        {
            "id": "factions",
            "rank": 6,
            "cluster": "Actors",
            "title": "PLO, PA, Hamas, and who speaks for Palestinians",
            "type": "politics",
            "popularity": "Very high",
            "why_it_matters": "Israelis ask 'partner for peace.' Palestinians ask 'which Israel — the one that signed Oslo or the one that expanded settlements?' Name the actor.",
            "israel": {
                "claim": "Hamas's 1988 covenant is eliminationist and antisemitic; even the 2017 document still rejects Israel's right to exist; you cannot run a peace process with a faction whose founding document sacralizes destruction.",
                "case": (
                    "1988 Hamas Covenant cites the Protocols and frames the fight as religious. 2017: accepts a state on 1967 lines as national consensus without recognizing Israel. "
                    "Second Intifada suicide bombings and rocket fire are the Israeli civilian-memory core. PLO charter historically denied Israel's legitimacy (later letters of recognition are the counter-file)."
                ),
                "quotes": [
                    Q(
                        "Israel will exist and will continue to exist until Islam will obliterate it, just as it obliterated others before it.",
                        "Hamas Covenant (1988), opening (standard English translations used in this debate)",
                        "The Covenant of the Islamic Resistance Movement",
                        "https://avalon.law.yale.edu/20th_century/hamas.asp",
                    ),
                ],
                "data_points": [
                    D("Hamas 2017 Document of General Principles: 1967 lines as a formula of national consensus, without recognizing Israel.", "https://www.middleeasteye.net/news/hamas-2017-document-full"),
                    D("US, EU, UK, etc. list Hamas as a terrorist organization (listings are political-legal facts, not theology).", "Treasury / EU lists"),
                ],
                "sources": [
                    S("Hamas Covenant 1988 (Avalon)", "https://avalon.law.yale.edu/20th_century/hamas.asp"),
                ],
            },
            "palestine": {
                "claim": "The PLO recognized Israel (1993); the PA is the diplomatic address; Hamas is also a product of occupation and of Israeli tolerance in the 1980s against the PLO — reduce it to a cartoon and you cannot explain Gaza elections 2006 or why armed struggle has a constituency.",
                "case": (
                    "Oslo letters: Arafat recognition of Israel; Israel recognition of PLO. Subsequent collapse is mutual (settlements, incitement, terror). "
                    "Hamas won 2006 PLC elections. Treating all Palestinians as Hamas is the mirror of treating all Jews as a cabinet. Resistance vs terrorism still has to obey distinction — but so does occupation."
                ),
                "quotes": [
                    Q(
                        "The PLO recognizes the right of the State of Israel to exist in peace and security.",
                        "Yasser Arafat to Yitzhak Rabin",
                        "9 September 1993 (Oslo recognition letter)",
                        "https://www.un.org/unispal/document/auto-insert-180687/",
                    ),
                ],
                "data_points": [
                    D("Palestinian National Council 1996: covenant clauses inconsistent with letters of recognition were declared inoperative (implementation debates remain).", "PNC 1996 / Clinton Gaza appearance file"),
                ],
                "sources": [
                    S("Oslo exchange of letters", "https://www.un.org/unispal/document/auto-insert-180687/"),
                ],
            },
            "live": {
                "if_they_say": "There is no partner for peace.",
                "you_say": "Name the partner you would accept: PA minus Hamas? Hamas after demilitarization? A new leadership? Then ask Israel: freeze settlements in a real map or not? 'No partner' can be true of a month and false as a metaphysics.",
                "dont_overclaim": "Don't quote 1988 as if 2017 and Oslo never happened. Don't quote Oslo as if Hamas and the Second Intifada never happened.",
            },
            "crux": "Who has a mandate to end claims, and what security/recognition package would make that mandate real?",
            "debate_use": "Always ask: are we indicting a charter, an election, a tunnel, or a whole people?",
        },
        {
            "id": "gaza-oct7",
            "rank": 7,
            "cluster": "Gaza",
            "title": "Gaza, blockade, 7 October 2023, and the war that followed",
            "type": "history + IHL",
            "popularity": "Very high (the live room, 2023–26)",
            "why_it_matters": "This is the argument people actually came to have. You must hold Oct 7 and Gaza's civilian dead in the same moral field without cancellation.",
            "israel": {
                "claim": "7 October was a massacre of civilians, sexual violence, and hostage-taking that any state would answer with war to destroy Hamas's military capacity; Hamas embeds in civilian areas; casualty numbers from Hamas-run health authorities need caution; Israel seeks to degrade a genocidal actor, not the Palestinian people.",
                "case": (
                    "UN and multiple governments condemned the 7 Oct attacks. Hostages remain a distinct IHL file (captives). "
                    "Israel: blockade is a lawful siege-like control against a hostile entity that ran Gaza after 2007; humanitarian law requires aid, not Hamas's survival as an army."
                ),
                "data_points": [
                    D("~1,200 killed in Israel on 7 Oct 2023 is the widely used Israeli figure (verify current official count in the room).", "Israeli government / UN reporting"),
                    D("Hostages taken into Gaza are a continuing war crime if civilians are held.", "IHL hostage-taking"),
                ],
                "sources": [
                    S("UN: 7 October reporting (verify latest UNISPAL / OHCHR)", "https://www.un.org/unispal/"),
                    S("IHL: distinction and proportionality", "https://www.icrc.org/en/war-and-law/conduct-hostilities"),
                ],
            },
            "palestine": {
                "claim": "Gaza was under blockade for years before 2023; the scale of killing, displacement, and destruction after Oct 7 is not 'self-defense unlimited'; ICJ provisional measures in South Africa v. Israel show a plausible genocide case is not a fringe tweet; collective punishment is the Palestinian name for the siege.",
                "case": (
                    "Even granting Oct 7 as a crime, IHL still binds the stronger army: distinction, proportionality, precautions. "
                    "Hospital/school strikes, famine warnings (IPC), and population transfer fears are the indictment. A people cannot be punished for a faction."
                ),
                "data_points": [
                    D("Gaza Health Ministry casualty totals are the figures most media use; Israeli and academic critiques of methodology exist — flag the source, don't pretend there is no count.", "MOH Gaza / UN OCHA aggregations"),
                    D("ICJ Order of 26 Jan 2024: provisional measures in South Africa v. Israel (not a final genocide verdict).", "https://www.icj-cij.org/case/192"),
                ],
                "sources": [
                    S("ICJ: Application of the Genocide Convention (South Africa v. Israel)", "https://www.icj-cij.org/case/192"),
                    S("OCHA oPt", "https://www.ochaopt.org/"),
                ],
            },
            "counters": [
                {
                    "against": "Israeli 'no civilians in Gaza'",
                    "claim": "Everyone is Hamas.",
                    "reply": "That is a war crime waiting to happen. Distinction is not optional because the enemy is barbaric.",
                },
                {
                    "against": "Palestinian 'Oct 7 was resistance, full stop'",
                    "claim": "Killing civilians at a music festival is just a prison break.",
                    "reply": "IHL does not license massacre because of blockade. Resistance against occupation and murder of civilians are not the same act.",
                },
            ],
            "live": {
                "if_they_say": "It's a genocide / it's just self-defense.",
                "you_say": "Genocide is a specific intent crime (Genocide Convention Art. II). Self-defense is UN Charter Art. 51 plus IHL limits. Neither word is a substitute for: what happened on 7 Oct, what is happening to civilians in Gaza, and what end-state the war is for. Use ICJ language carefully: plausible risk ≠ final judgment.",
                "dont_overclaim": "Don't deny Oct 7. Don't deny Gaza's dead. Don't treat Twitter as the ICJ.",
            },
            "crux": "What are the lawful objects of the war, and has the conduct stayed inside distinction/proportionality even if the cause is granted?",
            "debate_use": "Minute one: condemn the massacre. Minute two: IHL limits. Minute three: hostages and a political horizon. Skip any minute and you look like a faction press officer.",
        },
        {
            "id": "ihl-apartheid",
            "rank": 8,
            "cluster": "Law",
            "title": "International law: occupation, apartheid accusation, ICJ/ICC",
            "type": "law",
            "popularity": "High among trained debaters",
            "why_it_matters": "Law-talk is how campuses fight. If you cannot define apartheid and occupation, you will be eaten by NGOs or by hasbara lawyers.",
            "israel": {
                "claim": "Apartheid is a specific crime (1973 Convention / Rome Statute) built on South Africa's racial domination; Israel is a nation-state with Arab citizens who vote; the WB is a conflict/occupation file, not a racial caste state; ICC/ICJ processes are politicized (UNGA majorities).",
                "case": (
                    "Arab Israelis in the Knesset are the domestic rebuttal. Security barriers after the Second Intifada reduced suicide bombings (Israeli claim). "
                    "Counter: HRW/Amnesty/B'Tselem apartheid reports exist — answer them point by point (movement, nationality law, Gaza), don't shout 'antisemitism' as a definition."
                ),
                "data_points": [
                    D("Rome Statute Art. 7(2)(h): apartheid as inhumane acts in a context of systematic oppression by one racial group over another.", "https://www.icc-cpi.int/sites/default/files/RS-Eng.pdf"),
                    D("Nation-State Law (2018) is the text critics use to argue constitutional hierarchy of Jewish self-determination.", "Knesset / official translation"),
                ],
                "sources": [
                    S("Rome Statute (PDF)", "https://www.icc-cpi.int/sites/default/files/RS-Eng.pdf"),
                ],
            },
            "palestine": {
                "claim": "From the river to the sea as a single Israeli-controlled regime (sovereign Israel + occupation + Gaza siege) meets the legal definition of apartheid: two legal systems, movement permits, and domination.",
                "case": (
                    "B'Tselem 2021: 'A regime of Jewish supremacy from the Jordan River to the Mediterranean Sea.' HRW 2021, Amnesty 2022. "
                    "ICJ 2024 advisory proceedings on occupation (UNGA request) are the state-level law track. This is not 'mean checkpoints'; it is a structure."
                ),
                "data_points": [
                    D("B'Tselem position paper (12 Jan 2021) is the Israeli human-rights organization's apartheid framing.", "https://www.btselem.org/publications/fulltext/202101_this_is_apartheid"),
                    D("Amnesty International 2022 report: Israel's apartheid against Palestinians.", "https://www.amnesty.org/en/latest/news/2022/02/israels-apartheid-against-palestinians-a-cruel-system-of-domination-and-a-crime-against-humanity/"),
                ],
                "sources": [
                    S("B'Tselem: This is apartheid", "https://www.btselem.org/publications/fulltext/202101_this_is_apartheid"),
                    S("ICJ case 131 (Wall)", "https://www.icj-cij.org/case/131"),
                ],
            },
            "live": {
                "if_they_say": "Israel is an apartheid state, full stop.",
                "you_say": "Define the unit: inside the Green Line, or the whole land including WB/Gaza? Apartheid is a legal term. If you mean occupation + settlement dual law, say that — it may be easier to prove than the racial-group element. If you mean 1948 Israel as South Africa, you owe Arab-Israeli voting a sentence.",
                "dont_overclaim": "Don't treat NGO reports as statutes. Don't treat UNGA votes as physics. Don't treat checkpoints as a vibe.",
            },
            "crux": "Which territorial unit is the alleged apartheid regime, and which inhumane acts are systematic domination rather than wartime security?",
            "debate_use": "Read Rome Statute definitions aloud. Then pick three facts. Law without facts is chanting; facts without law are just horror stories.",
        },
        {
            "id": "end-state",
            "rank": 9,
            "cluster": "End-state",
            "title": "Two-state, one-state, and 'from the river to the sea'",
            "type": "politics",
            "popularity": "Very high",
            "why_it_matters": "If the slogan does not specify citizenship for the losing people, it is a polite elimination. Both sides have versions.",
            "israel": {
                "claim": "A Jewish nation-state alongside a demilitarized Palestinian state is the only stable liberal-national compromise; one-state 'return' is Israel’s destruction; river-to-sea in Hamas usage is not a human-rights poem.",
                "case": (
                    "Clinton parameters / Olmert-Abbas near-misses are the adult two-state file. Israeli right: Jordan-is-Palestine or indefinite control. "
                    "Jewish self-determination is not unique wickedness among nation-states. A binational state with maximal return is, in Israeli eyes, Lebanonization plus a Jewish minority under a hostile majority."
                ),
                "data_points": [
                    D("Polls on two-state support swing with the last war — cite the latest PCPSR / Israel Democracy Institute numbers, not 1993 nostalgia.", "PCPSR / IDI"),
                ],
                "sources": [
                    S("Clinton Parameters (2000) summary", "https://peacemaker.un.org/clinton-parameters2000"),
                ],
            },
            "palestine": {
                "claim": "Two-state is being buried by settlements; one democratic state with equal rights is the rights-consistent answer; 'from the river to the sea' can mean equal citizenship, not a bloodbath — but speakers must say which.",
                "case": (
                    "Area C fragmentation makes a contiguous state look like Swiss cheese. Some Palestinian/Israeli left intellectuals argue one-state is already the reality (one army) and should become one citizenship. "
                    "Critics of the chant point to Hamas/1948 PLO usage as eliminationist — the burden is on the chanter to specify Jews' rights the day after."
                ),
                "data_points": [
                    D("PLO 1970s 'democratic secular state' formula vs 1988 two-state political declaration — history of end-states is not a single poster.", "PNC 1988"),
                ],
                "sources": [
                    S("Palestinian Declaration of Independence (1988) / two-state turn", "https://www.un.org/unispal/document/auto-insert-178258/"),
                ],
            },
            "live": {
                "if_they_say": "From the river to the sea, Palestine will be free.",
                "you_say": "Free how? Equal citizenship for Jews and Palestinians, two states, or a state without Jews? If you cannot answer in one sentence, you are chanting an ambiguity that the worst actors will fill.",
                "dont_overclaim": "Don't treat every chanter as Hamas. Don't treat every Israeli flag as a settlement map.",
            },
            "crux": "The day after the slogan wins, what passport does a Jewish family in Tel Aviv hold — and what passport does a refugee family in Lebanon hold?",
            "debate_use": "Make both sides draw the map and the citizenship table. Poetry is not a constitution.",
        },
        {
            "id": "poison",
            "rank": 10,
            "cluster": "Discourse",
            "title": "Antisemitism, Islamophobia, and how the debate gets poisoned",
            "type": "ethics + method",
            "popularity": "Very high",
            "why_it_matters": "If criticism of Israel is always antisemitism, Palestinians cannot speak. If any Jewish self-defense is always genocide, Jews cannot speak. Both silencers are active.",
            "israel": {
                "claim": "IHRA working definition: denying Jewish self-determination and applying double standards can be antisemitic; 7 Oct celebrations and synagogue attacks show the spillover is real, not a PR trick.",
                "case": (
                    "IHRA examples include comparing Israeli policy to Nazis and holding Jews collectively responsible. Campus harassment after Oct 7 is data. "
                    "Counter-abuse: governments have used IHRA to chill occupation criticism — that abuse does not erase actual antisemitism."
                ),
                "quotes": [
                    Q(
                        "Antisemitism is a certain perception of Jews, which may be expressed as hatred toward Jews…",
                        "IHRA working definition of antisemitism (opening)",
                        "IHRA plenary, 2016",
                        "https://www.holocaustremembrance.com/resources/working-definitions-charters/working-definition-antisemitism",
                    ),
                ],
                "sources": [
                    S("IHRA working definition", "https://www.holocaustremembrance.com/resources/working-definitions-charters/working-definition-antisemitism"),
                ],
            },
            "palestine": {
                "claim": "The Jerusalem Declaration and many Jewish scholars distinguish Israel-criticism from antisemitism; Islamophobia and anti-Arab racism spike with every war; 'human shields' and 'animals' talk is dehumanization too.",
                "case": (
                    "JDA 2021: it is not antisemitic to support boycott or a one-state solution as such. "
                    "Gaza's dead include a large civilian share; if your discourse cannot say 'Palestinian civilian,' it is not moral clarity."
                ),
                "quotes": [
                    Q(
                        "It is not antisemitic to support arrangements that accord full equality to all inhabitants “between the river and the sea,” whether in two states, a binational state, unitary democratic state, federal state, or in whatever form.",
                        "Jerusalem Declaration on Antisemitism",
                        "Guideline 2 (2021)",
                        "https://jerusalemdeclaration.org/",
                    ),
                ],
                "sources": [
                    S("Jerusalem Declaration on Antisemitism", "https://jerusalemdeclaration.org/"),
                ],
            },
            "live": {
                "if_they_say": "Anti-Zionism is always antisemitism / never antisemitism.",
                "you_say": "Always and never are both false. Targeting Jews as Jews is antisemitism. Targeting a state's policy is not automatically. Targeting 'the Jews' for Gaza is. Use IHRA and JDA as competing tools, then look at the specific sentence said in the room.",
                "dont_overclaim": "Don't call every protest a pogrom. Don't call every synagogue a settlement.",
            },
            "crux": "Which specific sentences are racist, and which are political claims that must be allowed even if they sting?",
            "debate_use": "Quote the actual chant or tweet. Definitions without exhibits are theology.",
        },
    ],
    "materials": [],
    "debates": [
        {
            "id": "maps-not-vibes",
            "title": "How to run this debate without becoming a press officer",
            "year": 2026,
            "venue": "Prep note",
            "participants": ["You"],
            "motion": "Keep 1948, 1967, and 2023 in separate folders until someone earns the right to merge them.",
            "summary": "The highest-skill move is a timeline on paper. The lowest-skill move is a body-count chant.",
            "key_moves": {
                "Israeli / Zionist case": [
                    "Self-determination + 181 acceptance + Oct 7 distinction",
                    "Demand a Palestinian end-state that includes Jewish political existence",
                ],
                "Palestinian case": [
                    "Majority indigeneity + Nakba/occupation law + IHL limits even after a massacre",
                    "Demand an Israeli end-state that includes Palestinian political existence",
                ],
            },
            "what_to_steal": [
                "Maps",
                "UN texts read aloud",
                "Charters dated",
                "No metaphysical 'no partner'",
            ],
            "links": [
                {"label": "UNISPAL", "url": "https://www.un.org/unispal/"},
                {"label": "Peacemaker document collection", "url": "https://peacemaker.un.org/"},
            ],
        }
    ],
    "opponent_cards": [],
    "checklist": [
        "Draw Green Line, East Jerusalem, Gaza, Golan on a scrap of paper",
        "Separate 1948 / 1967 / 2005 / 2007 / 2023",
        "Read UNSC 242 and UNGA 194 §11 aloud once",
        "Read one paragraph of Hamas 1988 and one of the 1993 recognition letter",
        "Define genocide, apartheid, occupation, refugee before using them",
        "Condemn civilian targeting on both sides before your 'but'",
        "Ask the river-to-sea speaker what passport Tel Aviv holds the day after",
        "Ask the 'no partner' speaker what map they would sign tomorrow",
    ],
    "positive_cases": {
        "Israeli podium": [
            "Jewish peoplehood and 181 as a compromise, not a theft from nowhere",
            "Oct 7 as a real massacre that any state would war-answer",
            "Demand a Palestinian politics that can say Israel will remain",
        ],
        "Palestinian podium": [
            "Majority society under Mandate + Nakba as a real dispossession",
            "Occupation/settlements as a live legal and human file",
            "Demand an Israeli politics that can say Palestinians will remain as a people with a state or equal citizenship — specified",
        ],
        "Unity / steelman": [
            "Two peoples, one land, no elimination slogans",
            "IHL binds the weaker and the stronger",
            "Maps and dates beat adjectives",
        ],
    },
    "bibliography": [
        {
            "tier": "Primary diplomatic / legal",
            "items": [
                {"label": "Balfour Declaration", "url": "https://www.nationalarchives.gov.uk/education/resources/balfour-declaration/"},
                {"label": "UNGA 181", "url": "https://www.un.org/unispal/document/auto-insert-185393/"},
                {"label": "UNGA 194 §11", "url": "https://www.un.org/unispal/document/auto-insert-184159/"},
                {"label": "UNSC 242", "url": "https://peacemaker.un.org/israelopt-resolution242"},
                {"label": "Fourth Geneva Convention Art. 49", "url": "https://ihl-databases.icrc.org/en/ihl-treaties/gciv-1949/article-49"},
                {"label": "Oslo recognition letters", "url": "https://www.un.org/unispal/document/auto-insert-180687/"},
                {"label": "ICJ Wall opinion (2004)", "url": "https://www.icj-cij.org/case/131"},
                {"label": "ICJ South Africa v. Israel", "url": "https://www.icj-cij.org/case/192"},
            ],
        },
        {
            "tier": "Actors' documents",
            "items": [
                {"label": "Hamas Covenant 1988", "url": "https://avalon.law.yale.edu/20th_century/hamas.asp"},
                {"label": "IHRA working definition", "url": "https://www.holocaustremembrance.com/resources/working-definitions-charters/working-definition-antisemitism"},
                {"label": "Jerusalem Declaration on Antisemitism", "url": "https://jerusalemdeclaration.org/"},
            ],
        },
        {
            "tier": "Human rights / contested legal frames",
            "items": [
                {"label": "B'Tselem: This is apartheid", "url": "https://www.btselem.org/publications/fulltext/202101_this_is_apartheid"},
                {"label": "Amnesty 2022 apartheid report (news/summary)", "url": "https://www.amnesty.org/en/latest/news/2022/02/israels-apartheid-against-palestinians-a-cruel-system-of-domination-and-a-crime-against-humanity/"},
            ],
        },
    ],
}


def topic():
    return apply_overlays(DATA, {})
