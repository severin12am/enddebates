# -*- coding: utf-8 -*-
"""Who follows the historical Jesus more?"""

DATA = {
    "id": "historical-jesus",
    "meta": {
        "title": "Who follows the historical Jesus more?",
        "thesis": (
            "Using public historical methods (not later creeds or later revelations alone), "
            "does mainstream Christian faith or Islamic Christology better track the Jesus of history?"
        ),
        "purpose": (
            "Steelman criteria of authenticity, crucifixion consensus, prophet-within-Judaism readings, "
            "and Qur'anic Jesus. Separate 'historical Jesus' from 'Christ of faith' and 'Isa of the Qur'an.'"
        ),
        "warning": (
            "If you smuggle Nicene orthodoxy or Qur'anic inerrancy into 'historical' method without saying so, "
            "you are cheating. Announce your epistemology in minute one."
        ),
        "chips": ["history", "Jesus", "crucifixion", "method", "Christology"],
        "labels": {"christian": "Christian case", "muslim": "Muslim case"},
    },
    "definitions": [
        {
            "term": "Historical Jesus",
            "precise": (
                "Jesus as reconstructed by historical methods from early sources (primarily NT, some "
                "extracanonical/Jewish/Roman notices), provisional and debated."
            ),
            "not": "Not automatically the Nicene consubstantial Son — that is a theological claim.",
        },
        {
            "term": "Christ of faith",
            "precise": "Jesus as confessed in worship and creed by Christian communities.",
            "not": "Not identical with every historian's reconstruction.",
        },
        {
            "term": "Qur'anic Isa",
            "precise": "Jesus as presented in the Qur'an: Messiah, word, prophet, not divine, crucifixion denied/apparent.",
            "not": "Not simply 'the Muslim historical Jesus' without argument — it is revelation-claim content.",
        },
        {
            "term": "Criteria of authenticity",
            "precise": (
                "Tools historians have used (multiple attestation, embarrassment, coherence, etc.) — "
                "now heavily critiqued but still appear in debates."
            ),
            "not": "Not laboratory certainty.",
        },
        {
            "term": "High / low Christology",
            "precise": "Degree to which Jesus is described with divine status/worship in early sources.",
            "not": "Not a simple dating rule that earlier always means lower.",
        },
        {
            "term": "Public historical method",
            "precise": "Standards shareable with non-Christians/non-Muslims: sources, corroboration, context.",
            "not": "Not 'my scripture wins because my scripture says so.'",
        },
    ],
    "arguments": [
        {
            "id": "crucifixion-consensus",
            "rank": 1,
            "cluster": "Core facts",
            "title": "Crucifixion as historical bedrock",
            "type": "history",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Jesus' crucifixion under Pilate is among the most secure facts about him; "
                    "Qur'an 4:157 places Islam against the historical consensus."
                ),
                "case": (
                    "Multiple attestation; Tacitus Annals 15.44; Josephus; embarrassment criterion. "
                    "Ehrman: 'rock-bottom certain.' Following historical Jesus requires accepting the cross event."
                ),
                "sources": [
                    {
                        "label": "Ehrman — Does my work confirm the Qur'an?",
                        "url": "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/",
                    },
                    {
                        "label": "Tacitus Annals 15.44",
                        "url": "https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44",
                    },
                    {
                        "label": "Craig — Qur'an and crucifixion",
                        "url": "https://www.reasonablefaith.org/writings/question-answer/the-quran-and-the-crucifixion-of-jesus",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "4:157 can deny Jewish success/boast or affirm divine rescue amid appearance; "
                    "historians reconstruct appearances, not metaphysical outcomes. Revelation corrects the record."
                ),
                "case": (
                    "Todd Lawson: tafsir hardened denial; minority readings differ. "
                    "If the motion allows revelatory epistemology, consensus is not final."
                ),
                "sources": [
                    {"label": "Qur'an 4:157–158", "url": "https://quran.com/4/157-158"},
                    {
                        "label": "Lawson — The Crucifixion and the Qur'an (PDF)",
                        "url": "https://almuslih.org/wp-content/uploads/2024/12/Lawson-T-%E2%80%93-The-Crucifixion-and-the-Quran.pdf",
                    },
                    {
                        "label": "AJIS — Revisiting Crucifixion within Islam",
                        "url": "https://ajis.com.au/index.php/ajis/article/view/585",
                    },
                ],
            },
            "counter_to_christian": "Consensus can be wrong; ancient world believed many false things widely.",
            "counter_to_muslim": "In a 'historical Jesus' motion, public method outranks later revelation unless renegotiated.",
            "crux": "Is tonight's tribunal public history or final revelation?",
            "debate_use": "Lock the tribunal in the first minute; it decides this argument.",
        },
        {
            "id": "jewish-monotheist",
            "rank": 2,
            "cluster": "Identity",
            "title": "Jesus as apocalyptic Jewish monotheist prophet",
            "type": "history + theology",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Even as Jewish prophet, Jesus' authority claims, unique sonship language, and "
                    "earliest worship by Jews push beyond 'mere prophet' — Islam underfits the data."
                ),
                "case": (
                    "Mark 2 authority to forgive; Abba intimacy; Phil 2 early hymn. "
                    "Sanders/Ehrman agree on apocalyptic prophet core — Christians argue more is also historical."
                ),
                "sources": [
                    {
                        "label": "Mark 2:1–12",
                        "url": "https://www.biblegateway.com/passage/?search=Mark+2%3A1-12&version=NRSVUE",
                    },
                    {
                        "label": "Philippians 2:6–11",
                        "url": "https://www.biblegateway.com/passage/?search=Philippians+2%3A6-11&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "The best historical fit is a Torah-faithful prophet proclaiming the kingdom — "
                    "aligning with Islamic Rasul Christology more than Nicene deity."
                ),
                "case": (
                    "Mark 12:29 Shema; Matt 15:24; John 17:3 as used in debate. "
                    "High Christology is post-Easter development (classic critical line Muslims borrow)."
                ),
                "sources": [
                    {
                        "label": "Mark 12:29–34",
                        "url": "https://www.biblegateway.com/passage/?search=Mark+12%3A29-34&version=NRSVUE",
                    },
                    {
                        "label": "John 17:3",
                        "url": "https://www.biblegateway.com/passage/?search=John+17%3A3&version=NRSVUE",
                    },
                    {"label": "Qur'an 3:49–51", "url": "https://quran.com/3/49-51"},
                ],
            },
            "counter_to_christian": "Forgiveness authority can be prophetic agency, not ontological deity.",
            "counter_to_muslim": "Selective use of critical scholarship that also affirms crucifixion is inconsistent if 4:157 is hard denial.",
            "crux": "Does the historical core stop at prophet, or include claims that imply more?",
            "debate_use": "List 5 nearly-certain facts both accept, then see who needs fewer ad hoc moves.",
        },
        {
            "id": "resurrection-claim",
            "rank": 3,
            "cluster": "Core facts",
            "title": "Death, burial, and resurrection appearances",
            "type": "history + theology",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "Early creed in 1 Cor 15:3–8 is within years of the cross; historical Jesus research "
                    "that ignores Easter proclamation underplays why the movement exploded."
                ),
                "case": (
                    "Habermas minimal facts approach (debated); empty tomb arguments. "
                    "Islam's denial of death undercuts the historical explanation of Christian origins."
                ),
                "sources": [
                    {
                        "label": "1 Corinthians 15:3–8",
                        "url": "https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A3-8&version=NRSVUE",
                    },
                    {
                        "label": "SEP — Resurrection (overview entry points via philosophy of religion)",
                        "url": "https://plato.stanford.edu/entries/miracles/",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Appearances and enthusiasm do not prove bodily resurrection or deity; "
                    "alternative explanations exist; Qur'an affirms God raised Jesus without Christian soteriology."
                ),
                "case": (
                    "3:55; 4:158. Legend growth and cognitive science of visions are available to critics."
                ),
                "sources": [
                    {"label": "Qur'an 3:55", "url": "https://quran.com/3/55"},
                    {"label": "Qur'an 4:158", "url": "https://quran.com/4/158"},
                ],
            },
            "counter_to_christian": "Minimal facts debates are apologetic; many historians remain agnostic on resurrection as history.",
            "counter_to_muslim": "Still need a historical explanation for the rise of resurrection belief in Jerusalem.",
            "crux": "Must a 'follower of historical Jesus' take a position on Easter as history?",
            "debate_use": "Separate: (1) disciples believed he rose (2) he rose. Score them apart.",
        },
        {
            "id": "source-proximity",
            "rank": 4,
            "cluster": "Method",
            "title": "Source proximity: 1st-century vs 7th-century",
            "type": "history + method",
            "popularity": "Very high",
            "christian": {
                "claim": (
                    "First-century sources geographically and chronologically close to Jesus beat "
                    "a seventh-century Arabian revelation for historical reconstruction."
                ),
                "case": (
                    "Mark, Paul, Q-ish material, Aramaic substrate arguments. "
                    "Qur'anic Jesus is theologically mediated centuries later."
                ),
                "sources": [
                    {
                        "label": "Oxford Bibliographies — Historical Jesus (gateway)",
                        "url": "https://www.oxfordbibliographies.com/display/document/obo-9780195393361/obo-9780195393361-0022.xml",
                    },
                    {
                        "label": "Pauline letters chronology context (Bible Gateway Romans)",
                        "url": "https://www.biblegateway.com/passage/?search=Romans+1&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Later revelation from God can correct corrupted memory; also critical dating puts "
                    "Gospels decades out with theology. Proximity ≠ accuracy."
                ),
                "case": (
                    "If God speaks in the 7th c., historical 'nearness' is not the decisive criterion. "
                    "Muslims also cite alleged Gospel corruption."
                ),
                "sources": [
                    {"label": "Qur'an 5:48", "url": "https://quran.com/5/48"},
                    {"label": "Qur'an 2:79", "url": "https://quran.com/2/79"},
                ],
            },
            "counter_to_christian": "Proximity argument assumes naturalist historiography — declare it.",
            "counter_to_muslim": "If you use critical skepticism on Gospels, apply analogous skepticism to early Islamic reports about Jesus.",
            "crux": "Can a later revelatory text outrank earlier multiply attested historical sources in a history debate?",
            "debate_use": "Make both sign a method card: naturalist history / open to miracle / revelation-first.",
        },
        {
            "id": "law-torah",
            "rank": 5,
            "cluster": "Teaching",
            "title": "Jesus and the Torah",
            "type": "history",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Jesus intensifies Torah (Matt 5) and relativizes some boundaries (Mark 7 debates) "
                    "in ways that neither simple Muslim sharīʿa-continuity nor antinomian myth captures — "
                    "but Christian Torah-free Gentile mission needs Acts/Paul as development."
                ),
                "case": (
                    "Complex: Matt 5:17–20 vs Mark 7:19 editorial note. Historical Jesus is Jewish, not a Nicene seminary professor."
                ),
                "sources": [
                    {
                        "label": "Matthew 5:17–20",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+5%3A17-20&version=NRSVUE",
                    },
                    {
                        "label": "Mark 7:1–23",
                        "url": "https://www.biblegateway.com/passage/?search=Mark+7%3A1-23&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Qur'an presents Jesus as confirming Torah (3:50; 5:46) — closer to a historical "
                    "Jewish Jesus than Pauline law-free gospel."
                ),
                "case": (
                    "Muslims argue Paul diverted Jesus' Torah-affirming mission. James/Jerusalem Christianity as foil."
                ),
                "sources": [
                    {"label": "Qur'an 3:50", "url": "https://quran.com/3/50"},
                    {"label": "Qur'an 5:46", "url": "https://quran.com/5/46"},
                    {
                        "label": "Matthew 5:17–18",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+5%3A17-18&version=NRSVUE",
                    },
                ],
            },
            "counter_to_christian": "If historical Jesus is Torah-affirming, Gentile church practice needs justification.",
            "counter_to_muslim": "Qur'anic 'confirming Torah' still rejects key Jewish-Christian claims (crucifixion, sonship).",
            "crux": "Who is the truer heir of Jesus' Torah stance: Pauline churches or Islamic prophetology?",
            "debate_use": "Don't let 'Paul vs Jesus' become a substitute for source work on Jesus himself.",
        },
        {
            "id": "titles",
            "rank": 6,
            "cluster": "Identity",
            "title": "Messiah, Son of Man, Son of God",
            "type": "history + exegesis",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Historical titles — Messiah, Son of Man — plus early Son of God worship language "
                    "exceed Islam's 'created messenger' ceiling."
                ),
                "case": (
                    "Mark 14:61–62; Daniel 7 intertext; Romans 1:3–4. Semantic range is debated but not empty."
                ),
                "sources": [
                    {
                        "label": "Mark 14:61–62",
                        "url": "https://www.biblegateway.com/passage/?search=Mark+14%3A61-62&version=NRSVUE",
                    },
                    {
                        "label": "Romans 1:3–4",
                        "url": "https://www.biblegateway.com/passage/?search=Romans+1%3A3-4&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Messiah in Jewish context is not God; 'son of God' can be honorific; "
                    "Qur'an accepts Messiahship (3:45) while rejecting metaphysical sonship."
                ),
                "case": (
                    "3:45; 4:171. Muslims claim to keep the historical title and discard later ontology."
                ),
                "sources": [
                    {"label": "Qur'an 3:45", "url": "https://quran.com/3/45"},
                    {"label": "Qur'an 4:171", "url": "https://quran.com/4/171"},
                ],
            },
            "counter_to_christian": "Title maximalism often reads later Christology back into Semitic honor language.",
            "counter_to_muslim": "Earliest Christian use of titles in worship is data, not only later councils.",
            "crux": "What did 'Messiah' and 'Son of God' mean in Jesus' milieu — and what did his followers do with them?",
            "debate_use": "Define each title on a whiteboard before quoting.",
        },
        {
            "id": "sayings-authenticity",
            "rank": 7,
            "cluster": "Method",
            "title": "Which sayings go back to Jesus?",
            "type": "history + method",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Enough authentic teaching (parables, kingdom, love commands) survives that Christian "
                    "discipleship still tracks Jesus better than a Qur'anic portrait missing the cross and kingdom narrative."
                ),
                "case": (
                    "Parable tradition; Lord's prayer; love commands. Critical editions still leave a recognizable Jesus."
                ),
                "sources": [
                    {
                        "label": "Mark 12:28–34",
                        "url": "https://www.biblegateway.com/passage/?search=Mark+12%3A28-34&version=NRSVUE",
                    },
                    {
                        "label": "Luke 11:2–4",
                        "url": "https://www.biblegateway.com/passage/?search=Luke+11%3A2-4&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "If Christians admit heavy redaction, they cannot demand Muslims accept Johannine deity "
                    "sayings as historical Jesus. Islamic selectivity mirrors critical selectivity — with revelation as guide."
                ),
                "case": (
                    "John vs Synoptics gap. Muslims prefer Synoptic-sounding monotheistic sayings."
                ),
                "sources": [
                    {
                        "label": "John 10:30 vs Mark 10:18 contrast pair",
                        "url": "https://www.biblegateway.com/passage/?search=John+10%3A30%3B+Mark+10%3A18&version=NRSVUE",
                    },
                    {"label": "Qur'an 5:116–117", "url": "https://quran.com/5/116-117"},
                ],
            },
            "counter_to_christian": "Recognizable ≠ Nicene.",
            "counter_to_muslim": "Revelation-as-guide exits historical method; admit the lane change.",
            "crux": "What percentage of Synoptic Jesus is required to 'follow' him historically?",
            "debate_use": "Each side lists 10 sayings they accept as authentic — compare overlap.",
        },
        {
            "id": "james-jerusalem",
            "rank": 8,
            "cluster": "Early movement",
            "title": "James and the Jerusalem Jesus movement",
            "type": "history",
            "popularity": "Medium-high",
            "christian": {
                "claim": (
                    "Jerusalem leadership (James) was Jesus-following Judaism that still proclaimed "
                    "crucified-and-risen Messiah — not an Islamic prophetology."
                ),
                "case": (
                    "Galatians 1–2; Josephus on James. Continuity with resurrection kerygma."
                ),
                "sources": [
                    {
                        "label": "Galatians 1:18–19; 2:9",
                        "url": "https://www.biblegateway.com/passage/?search=Galatians+1%3A18-19%3B+2%3A9&version=NRSVUE",
                    }
                ],
            },
            "muslim": {
                "claim": (
                    "A Torah-observant Jerusalem Christianity is closer to Islamic Jesus than later Gentile Christology; "
                    "Pauline victory was a fork away from Jesus."
                ),
                "case": (
                    "Appeal to Ebionite-like reconstructions (historically fraught but popular in debate)."
                ),
                "sources": [
                    {
                        "label": "Qur'an 5:46–47",
                        "url": "https://quran.com/5/46-47",
                    },
                    {
                        "label": "Acts 21:20 (many thousands zealous for the law)",
                        "url": "https://www.biblegateway.com/passage/?search=Acts+21%3A20&version=NRSVUE",
                    },
                ],
            },
            "counter_to_christian": "James' exact Christology is underdetermined.",
            "counter_to_muslim": "Ebionite projection is often apologetic wishful history.",
            "crux": "Was the earliest Jesus movement's center of gravity closer to Islam or to Pauline Christ-faith?",
            "debate_use": "Stick to Galatians/Acts/Josephus before medieval sect labels.",
        },
        {
            "id": "miracles",
            "rank": 9,
            "cluster": "Teaching",
            "title": "Miracles: shared claim, different meaning",
            "type": "history + theology",
            "popularity": "Medium",
            "christian": {
                "claim": (
                    "Miracles as kingdom signs are multiply attested; historical Jesus research often grants "
                    "healer/exorcist reputation — fitting Gospels more than a minimal messenger."
                ),
                "case": (
                    "Sanders: Jesus was a miracle worker in reputation. Christian claim: signs cohere with authority."
                ),
                "sources": [
                    {
                        "label": "Mark 1:21–34",
                        "url": "https://www.biblegateway.com/passage/?search=Mark+1%3A21-34&version=NRSVUE",
                    }
                ],
            },
            "muslim": {
                "claim": (
                    "Qur'an affirms Jesus' miracles by God's permission (5:110) — so miracle agreement "
                    "doesn't award deity or crucifixion to Christians."
                ),
                "case": (
                    "5:110; 3:49. Shared wonder-working, Islamic interpretation."
                ),
                "sources": [
                    {"label": "Qur'an 5:110", "url": "https://quran.com/5/110"},
                    {"label": "Qur'an 3:49", "url": "https://quran.com/3/49"},
                ],
            },
            "counter_to_christian": "Miracle reputation ≠ ontological status.",
            "counter_to_muslim": "Agreement on miracles increases pressure to explain why Islamic historiography rejects the cross consensus.",
            "crux": "Do miracles function as prophetic accreditation only, or as more?",
            "debate_use": "Mark shared affirmations to isolate real disagreements.",
        },
        {
            "id": "following-today",
            "rank": 10,
            "cluster": "Discipleship",
            "title": "What 'following' means: creed vs practice",
            "type": "ethics + history",
            "popularity": "High",
            "christian": {
                "claim": (
                    "Following Jesus includes trusting his death/resurrection and embodying Sermon ethics; "
                    "Islam's Isa lacks the cross-shaped center of the historical movement."
                ),
                "case": (
                    "If the historical movement was cross-centered from the earliest creed, "
                    "omitting it is not 'following.'"
                ),
                "sources": [
                    {
                        "label": "1 Corinthians 15:3–5",
                        "url": "https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A3-5&version=NRSVUE",
                    },
                    {
                        "label": "Matthew 5–7",
                        "url": "https://www.biblegateway.com/passage/?search=Matthew+5&version=NRSVUE",
                    },
                ],
            },
            "muslim": {
                "claim": (
                    "Following Jesus means tawhid, prayer, purity, and gospel ethics without later Trinity; "
                    "Muslims may claim better practice of Jewish-Christian moral monotheism."
                ),
                "case": (
                    "Qur'an 3:51 worship God my Lord and yours. Practice tests vs creedal metaphysics."
                ),
                "sources": [
                    {"label": "Qur'an 3:51", "url": "https://quran.com/3/51"},
                    {"label": "Qur'an 19:36", "url": "https://quran.com/19/36"},
                ],
            },
            "counter_to_christian": "Creeds can displace Sermon practice — hypocrisy risk.",
            "counter_to_muslim": "Moral monotheism without the movement's death/resurrection kerygma may be a different religion's Jesus.",
            "crux": "Is 'following Jesus' primarily orthodoxy about his identity or orthopraxy of his teaching?",
            "debate_use": "Split the ballot: identity score and practice score.",
        },
    ],
    "materials": [],
    "debates": [
        {
            "id": "ally-white-jesus",
            "title": "Jesus in Bible and Qur'an debates",
            "year": None,
            "venue": "Public apologetics",
            "participants": ["Shabir Ally", "James White / others"],
            "sides": {"christian": "High Christology + history", "muslim": "Unitarian Synoptic Jesus + Qur'an"},
            "motion": "Who was Jesus / who represents him?",
            "summary": (
                "Ally leverages critical scholarship against deity; Christians press consistency on crucifixion "
                "and early worship."
            ),
            "what_to_steal": [
                "Method consistency test",
                "Force crucifixion before Christology stacking",
            ],
            "links": [
                {
                    "label": "Ehrman blog on Qur'an vs historical Jesus",
                    "url": "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/",
                }
            ],
        }
    ],
    "opponent_cards": [
        {
            "trigger": "Historians agree with the Muslim Jesus",
            "fast_answer": "Name one: crucifixion? Most don't. Don't conflate 'not Nicene' with 'Islamic Isa.'",
            "follow_up": "Quote Ehrman's crucifixion line.",
            "sources": ["https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/"],
        },
        {
            "trigger": "The Qur'an confirms the historical Jesus",
            "fast_answer": "It affirms prophethood/messiahship/miracles and collides on crucifixion/deity. Partial overlap ≠ confirmation.",
            "follow_up": "List overlaps and collisions explicitly.",
            "sources": ["https://quran.com/4/157", "https://quran.com/3/45"],
        },
        {
            "trigger": "Jesus never said 'I am God'",
            "fast_answer": "Debate whether that is required. Bring authority claims, worship patterns, and John vs Synoptics honestly.",
            "follow_up": "Ask what would count as a claim in Jewish idiom.",
            "sources": ["Mark 2", "Philippians 2", "John 10:30"],
        },
        {
            "trigger": "Paul invented Christianity",
            "fast_answer": "Paul persecuted a Jesus movement that already existed; 1 Cor 15 creed is received. Paul ≠ inventor ex nihilo.",
            "follow_up": "Discuss development without conspiracy.",
            "sources": ["Galatians 1", "1 Corinthians 15:3–8"],
        },
        {
            "trigger": "4:157 is only denying Jewish boasts",
            "fast_answer": "Possible reading — argue it. Majority tafsir and common Muslim belief still deny the crucifixion event.",
            "follow_up": "Ask opponent's personal position on whether Jesus died on the cross.",
            "sources": ["https://quran.com/4/157-158", "Lawson PDF"],
        },
        {
            "trigger": "John is late and useless",
            "fast_answer": "For historical Jesus, Synoptics weigh more. Christianity doesn't rest on John alone; nor can Islam cherry-pick John 17:3 only.",
            "follow_up": "Apply equal skepticism to favorite verses.",
            "sources": ["Mark 12:29", "John 17:3"],
        },
        {
            "trigger": "Historical method can't touch miracles, so Christianity loses",
            "fast_answer": "Then both lose miracle claims including Qur'anic Jesus signs — or both allow them. Keep symmetry.",
            "follow_up": "Return to crucifixion as non-miracle event claim.",
            "sources": ["Method card"],
        },
        {
            "trigger": "Jesus was a Muslim",
            "fast_answer": "If Muslim = submitter to God, word game. If Muslim = 7th-c. Sharīʿa follower, anachronism.",
            "follow_up": "Define Islam in the sentence.",
            "sources": ["https://quran.com/3/52", "historical method"],
        },
        {
            "trigger": "Nicene Christians follow Greek philosophy not Jesus",
            "fast_answer": "Development used Greek terms; the dispute is whether it tracks apostolic claims. Fight substance.",
            "follow_up": "Early Jewish Christian worship of Jesus predates Nicaea.",
            "sources": ["Philippians 2", "Hurtado/Bauckham discussions"],
        },
        {
            "trigger": "Embarrassment criterion proves nothing",
            "fast_answer": "Grant criterion wars. Crucifixion still multiply attested including enemies. Don't need one tool.",
            "follow_up": "Stack attestation channels.",
            "sources": ["Tacitus", "Josephus", "Paul", "Mark"],
        },
    ],
    "checklist": [
        "Announce epistemology: public history vs revelation-first",
        "Define historical Jesus vs Christ of faith vs Qur'anic Isa",
        "Lock crucifixion as first clash under public history",
        "Prepare 5 shared near-certainties and 5 collisions",
        "Master 1 Cor 15, Mark 12:29, Mark 14:61–62, Q 4:157, 3:45, 4:171",
        "Method consistency jab ready (Ally/White style)",
        "Separate resurrection belief fact from resurrection event claim",
        "Decide how much critical scholarship you will use without sawing off your branch",
        "Drill cards; kill 'historians agree with Islam' overclaim",
        "Split identity vs practice scoring for 'follows'",
        "Closing: who needs fewer ad hoc moves after method is fixed?",
        "Bring Ehrman crucifixion quote + Q 4:157 printout",
    ],
    "positive_cases": {
        "Christian podium": [
            "Crucifixion (and early resurrection proclamation) as historical movement center",
            "First-century source proximity for reconstruction",
            "Early high devotion/authority claims exceed 'mere prophet' ceiling",
            "Islamic Isa collides with mainstream historical consensus at 4:157",
        ],
        "Muslim podium": [
            "Historical Jesus as Jewish monotheist prophet fits Qur'anic Messiah-prophet better than Nicene deity",
            "Torah-confirming portrait vs law-free Pauline mission",
            "Shared miracle/messiah data without metaphysical sonship",
            "Critical Gospel scholarship undercuts simple 'Bible Jesus = God' historical claims",
        ],
        "Unity / steelman": [
            "Both should fear anachronism: Nicene seminary Jesus and 7th-c. fiqh Jesus",
            "State method before conclusions",
            "Use critical scholars symmetrically",
            "Separate overlapping moral teaching from identity claims",
        ],
    },
    "bibliography": [
        {
            "tier": "History / method",
            "items": [
                {"label": "Ehrman blog — historical Jesus vs Qur'an", "url": "https://ehrmanblog.org/does-my-work-on-the-historical-jesus-confirm-the-quran/"},
                {"label": "Oxford Bibliographies — Historical Jesus", "url": "https://www.oxfordbibliographies.com/display/document/obo-9780195393361/obo-9780195393361-0022.xml"},
                {"label": "Tacitus Annals 15.44", "url": "https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44"},
                {"label": "Lawson PDF — Crucifixion and the Qur'an", "url": "https://almuslih.org/wp-content/uploads/2024/12/Lawson-T-%E2%80%93-The-Crucifixion-and-the-Quran.pdf"},
            ],
        },
        {
            "tier": "Primary",
            "items": [
                {"label": "1 Corinthians 15; Mark 2; 12; 14; Matthew 5", "url": "https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A3-8&version=NRSVUE"},
                {"label": "Qur'an 3:45–55; 4:157–158; 4:171; 5:110", "url": "https://quran.com/4/157-158"},
            ],
        },
        {
            "tier": "Apologetic",
            "items": [
                {"label": "Craig — Qur'an and crucifixion", "url": "https://www.reasonablefaith.org/writings/question-answer/the-quran-and-the-crucifixion-of-jesus"},
                {"label": "AJIS crucifixion survey", "url": "https://ajis.com.au/index.php/ajis/article/view/585"},
            ],
        },
    ],
}


def topic():
    from .deepen_lib import apply_overlays
    from .ehrman_gospel_reliability_args import ARGUMENTS as EHRMAN_ARGS
    from .ehrman_gospel_reliability_args import DEBATE as EHRMAN_DEBATE
    from .ehrman_gospel_reliability_args import OPPONENT_CARDS as EHRMAN_CARDS
    from .jesus_deep import HISTORICAL

    topic = apply_overlays(DATA, HISTORICAL)
    seen = {a.get("id") for a in topic.get("arguments") or []}
    for arg in EHRMAN_ARGS:
        if arg.get("id") not in seen:
            topic.setdefault("arguments", []).append(arg)
            seen.add(arg.get("id"))
    debate_ids = {d.get("id") for d in topic.get("debates") or []}
    if EHRMAN_DEBATE.get("id") not in debate_ids:
        topic.setdefault("debates", []).append(EHRMAN_DEBATE)
    triggers = {c.get("trigger") for c in topic.get("opponent_cards") or []}
    for card in EHRMAN_CARDS:
        if card.get("trigger") not in triggers:
            topic.setdefault("opponent_cards", []).append(card)
    return topic
