# -*- coding: utf-8 -*-
from .deepen_lib import D, M, Q, S

HISTORICAL = {
    "crucifixion-consensus": {
        "why_it_matters": "If the motion is 'historical Jesus,' this is usually the single highest-leverage fact. Book-preservation fights are a different motion.",
        "christian": {
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
                D("All four canonical Gospels + Paul (1 Cor 15; Phil 2; Gal 3:13) attest crucifixion.", "NT primary"),
                D("Josephus, Antiquities 18.3.3, in all Greek MSS, mentions Jesus' condemnation under Pilate (Testimonium has Christian coloring; the execution notice is still widely used).", "Josephus Ant. 18.63–64"),
                D("Q 4:157 is the collision verse.", "https://quran.com/4/157"),
            ],
            "manuscripts": [
                M("P46 — early Pauline papyri including crucifixion kerygma", "https://en.wikipedia.org/wiki/Papyrus_46", "Content proximity, not autograph"),
            ],
            "sources": [
                S("Craig on Qur'an & crucifixion", "https://www.reasonablefaith.org/writings/question-answer/the-quran-and-the-crucifixion-of-jesus"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "…they did not kill him, nor did they crucify him; but it was made to appear so to them…",
                    "Qur'an 4:157",
                    "Primary text",
                    "https://quran.com/4/157",
                ),
                Q(
                    "The point is that tafsir, not the Qur'an, denies the Crucifixion.",
                    "Todd Lawson",
                    "The Crucifixion and the Qur'an (as commonly cited in this debate)",
                    "https://almuslih.org/wp-content/uploads/2024/12/Lawson-T-%E2%80%93-The-Crucifixion-and-the-Quran.pdf",
                ),
            ],
            "data_points": [
                D("Majority Sunni tafsir: substitution / non-death on the cross.", "Ṭabarī and later"),
                D("Minority academic/Ismāʿīlī readings: verse denies the boast of success, not necessarily a public crucifixion-looking event.", "AJIS survey"),
            ],
            "sources": [
                S("AJIS — non-monolithic crucifixion views", "https://ajis.com.au/index.php/ajis/article/view/585"),
            ],
        },
        "counters": [
            {
                "against": "Muslim 'appearance' escape",
                "claim": "Historians only have appearances, which the Qur'an already grants.",
                "reply": "Then you concede the historical evidence. The remaining claim is a miracle of illusion against every early source. Say that openly; don't pretend 4:157 is what Tacitus thought.",
            },
        ],
        "live": {
            "if_they_say": "The crucifixion is just what Christians believe.",
            "you_say": "Name a 1st–2nd c. source that has Jesus dying another way. Ehrman (not a Christian) calls the crucifixion rock-bottom certain. Then read 4:157 aloud and choose: deny the event, or reread the verse.",
            "dont_overclaim": "Don't pretend 4:157 is unambiguous. Don't pretend historians treat the Qur'an as a Jesus source.",
        },
    },
    "jewish-monotheist": {
        "why_it_matters": "Best Muslim 'historical Jesus' case: a Torah-loyal Jewish prophet looks more like Qur'anic Isa than like Nicene God-the-Son.",
        "christian": {
            "quotes": [
                Q(
                    "Jesus was a Jew. To know him, one must know the Judaism of his day.",
                    "E. P. Sanders (standard formulation of his project)",
                    "Jesus and Judaism / later summaries",
                    "https://www.fortresspress.com/store/product/9780800621445/Jesus-and-Judaism",
                ),
            ],
            "data_points": [
                D("Hurtado/Bauckham: earliest devotion to Jesus sits inside Jewish monotheism rather than abandoning it.", "Hurtado, Lord Jesus Christ"),
                D("Phil 2 and 1 Cor 8:6 apply Shema-shaped language to Jesus remarkably early.", "1 Cor 8:6"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "He said, 'Indeed, I am the servant of Allah. He has given me the Scripture and made me a prophet.'",
                    "Qur'an 19:30",
                    "Cradle speech as Islamic portrait of Isa",
                    "https://quran.com/19/30",
                ),
            ],
            "data_points": [
                D("Sanders, Vermes, Dunn: Jesus is a Jew among Jews, not a fourth-century council father.", "Historical Jesus consensus stream"),
                D("Mark 12:29: Jesus recites the Shema. That is Muslim-usable data.", "Mark 12:29"),
            ],
        },
        "live": {
            "if_they_say": "The historical Jesus was just a unitarian prophet like Islam says.",
            "you_say": "He was a Jew who recited the Shema — granted. The live question is whether the earliest sources also show him receiving devotion and going to a cross. Don't freeze the film at Mark 12:29 and cut Mark 14–15.",
            "dont_overclaim": "Don't baptize Sanders as a Nicene Christian. Don't baptize him as a Muslim either.",
        },
    },
    "resurrection-claim": {
        "why_it_matters": "Christianity's historical engine. Islam can grant empty-tomb rumors without granting atonement theology.",
        "christian": {
            "quotes": [
                Q(
                    "For I handed on to you as of first importance what I in turn had received: that Christ died for our sins… that he was buried, and that he was raised on the third day… and that he appeared to Cephas, then to the twelve.",
                    "1 Corinthians 15:3–5",
                    "Early creed embedded in Paul",
                    "https://www.biblegateway.com/passage/?search=1%20Corinthians%2015%3A3-8&version=NRSVUE",
                ),
            ],
            "data_points": [
                D("Most scholars date the 1 Cor 15 tradition to within a few years of the crucifixion.", "Standard Pauline chronology (Habermas / Dunn / Allison discussions)"),
                D("Enemy attestation angle: Paul was a former persecutor claiming an appearance.", "Gal 1; 1 Cor 15:8"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Rather, Allah raised him to Himself. And ever is Allah Exalted in Might and Wise.",
                    "Qur'an 4:158",
                    "Raising as the Qur'anic alternative ending",
                    "https://quran.com/4/158",
                ),
            ],
            "data_points": [
                D("Appearances can be visions; empty tomb is not as multiply attested as death.", "Lüdemann / Crossan-type critiques"),
                D("If Jesus did not die, 'resurrection' is a category error — raising a living prophet is not Easter.", "Islamic logic given 4:157"),
            ],
        },
        "live": {
            "if_they_say": "Resurrection is a later legend.",
            "you_say": "Paul's received formula in 1 Cor 15 is early, not Nicea. You can still reject it as vision/legend — but then say why that method doesn't also dissolve other miracle reports you like.",
            "dont_overclaim": "Don't claim 500 eyewitness affidavits in a modern court sense. Don't pretend Paul is late medieval.",
        },
    },
    "source-proximity": {
        "why_it_matters": "Chronology hammer: 1st-century Christian texts vs 7th-century Qur'an on a 30s-CE Jew.",
        "christian": {
            "data_points": [
                D("Paul writes in the 50s; Mark commonly dated ~70; all within living memory windows of a sort the Qur'an cannot match for Jesus.", "Standard NT dating ranges"),
                D("Ehrman: the Qur'an is not an independent 1st-century Jesus source.", "Ehrman blog on Qur'an/Jesus"),
            ],
            "manuscripts": [
                M("P52 — early John fragment", "https://manuscripts.csntm.org/Manuscript/View/GA_P52", "Text circulating by 2nd c."),
            ],
        },
        "muslim": {
            "data_points": [
                D("Proximity of copies ≠ truth of content; a close false report beats a distant true one only if you already trust the reporters.", "Method"),
                D("The Qur'an claims to correct a corrupted memory, so lateness is expected on the Islamic model.", "Revelation-correction thesis"),
            ],
        },
        "live": {
            "if_they_say": "The Gospels are late fan-fiction.",
            "you_say": "Late compared to what? Paul is within ~20–25 years. The Qur'an is ~600 years later. If 'late' kills the Gospels, it does not help Isa-in-the-Qur'an as history.",
            "dont_overclaim": "Don't claim we have Jesus' diaries. Don't claim 7th-century revelation is a 30s-CE archive.",
        },
    },
    "law-torah": {
        "why_it_matters": "Matthew 5 vs Paul vs Qur'anic Jesus-as-Torah-confirmer is a three-way trap.",
        "christian": {
            "quotes": [
                Q(
                    "Do not think that I have come to abolish the law or the prophets; I have come not to abolish but to fulfill.",
                    "Matthew 5:17",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Matthew%205%3A17&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "And [I have come] confirming what was before me of the Torah and to make lawful for you some of what was forbidden to you.",
                    "Qur'an 3:50",
                    "Isa's Torah stance in the Qur'an",
                    "https://quran.com/3/50",
                ),
            ],
            "data_points": [
                D("James and Matthew look more Torah-affirming than later Gentile Christianity's pork/Sabbath practice — Muslims use this as 'Paul vs Jesus.'", "Galatians / Acts 15 debates"),
            ],
        },
        "live": {
            "if_they_say": "Paul invented a law-free religion Jesus never taught.",
            "you_say": "Grant tension: Matthew 5, Mark 7, and Galatians 2 are not the same voice. Then ask whether Qur'anic Isa's infancy miracles and crucifixion denial are closer to 30s-CE Judaism than Paul is.",
            "dont_overclaim": "Don't flatten Paul into antinomian cartoon. Don't flatten Jesus into a later rabbi.",
        },
    },
    "titles": {
        "why_it_matters": "Messiah, Son of Man, Son of God, Lord — each title is a battlefield of meaning.",
        "christian": {
            "quotes": [
                Q(
                    "…yet for us there is one God, the Father… and one Lord, Jesus Christ…",
                    "1 Corinthians 8:6",
                    "Shema-split used in early worship",
                    "https://www.biblegateway.com/passage/?search=1%20Corinthians%208%3A6&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "The Messiah, Jesus, the son of Mary, was but a messenger of Allah…",
                    "Qur'an 4:171",
                    "Messiah as human messenger",
                    "https://quran.com/4/171",
                ),
            ],
            "data_points": [
                D("'Son of God' in Jewish idiom can be king/Israel/righteous one — not automatically second person of the Trinity.", "Psalm 2; 2 Sam 7"),
            ],
        },
        "live": {
            "if_they_say": "Jesus never said 'I am God.'",
            "you_say": "Ask what would count: John 8:58? Mark 14:62? Being called Lord in a Shema-shaped formula? Then ask whether Qur'anic titles (word, spirit, messiah) are being read equally strictly.",
            "dont_overclaim": "Don't pretend John and Mark are the same Christology. Don't pretend 'son of God' always means Nicene Son.",
        },
    },
    "sayings-authenticity": {
        "why_it_matters": "Whoever controls the authentic-sayings list controls 'what Jesus was.'",
        "christian": {
            "data_points": [
                D("Multiple attestation and embarrassment still used in debates even after method critique (Allison, Keith, Le Donne).", "Historical Jesus method wars"),
            ],
        },
        "muslim": {
            "data_points": [
                D("Infancy clay-birds and cradle speech have late antique Christian parallels; using 'late legend' on Gospels while keeping Q 3:49/19:29 needs a rule.", "Method symmetry"),
            ],
        },
        "live": {
            "if_they_say": "Historians proved Jesus didn't say most of the Gospels.",
            "you_say": "Which list — Jesus Seminar? Sanders? Dunn? Then apply the same list to Qur'anic Jesus sayings, which those scholars do not treat as 30s-CE transcripts.",
            "dont_overclaim": "Don't pretend criteria are a machine. Don't pretend there is no recoverable Jesus.",
        },
    },
    "james-jerusalem": {
        "why_it_matters": "James is a Christian-usable 'Jewish Jesus movement' witness and a Muslim-usable 'not Pauline Trinity' witness.",
        "christian": {
            "quotes": [
                Q(
                    "Then after three years I did go up to Jerusalem to visit Cephas… But I did not see any other apostle except James the Lord's brother.",
                    "Galatians 1:18–19",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Galatians%201%3A18-19&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("James 2 emphasizes deeds; Muslims contrast that with later faith-alone slogans.", "James 2:14–26"),
            ],
        },
        "live": {
            "if_they_say": "The real Jesus movement was James, and Paul hijacked it.",
            "you_say": "James is early and Jewish — granted. Galatians still has James in fellowship with Paul, not as a Qur'anic unitarian. 'Not Nicene yet' ≠ 'Islamic Isa.'",
            "dont_overclaim": "Don't make James a Trinitarian church father. Don't make him a Muslim.",
        },
    },
    "miracles": {
        "why_it_matters": "Both books have a miracle-working Jesus. The fight is which miracles and what they mean.",
        "christian": {
            "data_points": [
                D("Even skeptical historians often grant Jesus was known as an exorcist/healer (Sanders, Meier's 'marginal Jew' project).", "Consensus-leaning summaries"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "I heal the blind and the leper, and I give life to the dead — by permission of Allah.",
                    "Qur'an 3:49",
                    "Miracles as signs, not deity",
                    "https://quran.com/3/49",
                ),
            ],
            "data_points": [
                D("Clay birds: Infancy Gospel of Thomas parallel to Q 3:49 / 5:110.", "Standard parallel lists"),
            ],
        },
        "live": {
            "if_they_say": "Jesus' miracles prove he is God.",
            "you_say": "Elisha and Moses do wonders too in both canons. In the Qur'an the refrain is bi-idhnillāh. Miracle ≠ hypostatic union unless you add a philosophy step.",
            "dont_overclaim": "Don't deny the signs. Don't treat every sign as incarnation.",
        },
    },
    "following-today": {
        "why_it_matters": "Tie-breaker when history is messy: what does 'follow Jesus' mean as a life?",
        "christian": {
            "data_points": [
                D("Christian claim: following includes trusting the crucified-and-risen one, not only imitating a teacher.", "Pauline / canonical"),
            ],
        },
        "muslim": {
            "data_points": [
                D("Islamic claim: following Jesus means tawhid, prayer, and accepting the prophet who comes after — not Nicene worship.", "Q 61:6 used in this slot"),
            ],
        },
        "live": {
            "if_they_say": "We follow Jesus more because we don't worship him.",
            "you_say": "Define follow: imitate ethics, obey Torah, accept his self-claim, or accept later revelation about him? Those yield four different winners.",
            "dont_overclaim": "Don't let 'follow' stay undefined. That's how this round is stolen.",
        },
    },
    "ally-white-jesus": {
        "live": {
            "if_they_say": "The Ally–White debates already showed the Islamic Jesus wins historically.",
            "you_say": "Steal White's method-symmetry and Ally's critical-NT questions. Then put crucifixion and 1 Cor 15 on the table. A debate is a map, not a verdict.",
            "dont_overclaim": "Don't outsource your case to a YouTube comment section.",
        },
    },
}

VISION = {
    "portrait-fit-history": {
        "why_it_matters": "This topic's engine: not 'which religion is nicer,' but which Jesus-picture is better motivated by early data plus reason.",
        "christian": {
            "data_points": [
                D("Cross + early devotion + 1 Cor 15 appearances are the Christian portrait's historical spine.", "See historical-jesus topic"),
            ],
        },
        "muslim": {
            "data_points": [
                D("Jewish monotheism + prophet-within-Israel is the Islamic portrait's historical spine; incarnation is the extra.", "Sanders / Qur'anic tawhid"),
            ],
        },
        "live": {
            "if_they_say": "Our Jesus is obviously the real one.",
            "you_say": "Split the scorecard: (1) 1st-century sources, (2) Jewish monotheism, (3) moral meaning, (4) worship practice. Don't let one category bully the rest.",
            "dont_overclaim": "Don't call the other portrait 'a different Jesus' as a slur until you show contradiction, not just emphasis.",
        },
    },
    "monotheism-fit": {
        "why_it_matters": "Same fork as Trinity topic; here it is applied to Jesus' identity rather than abstract God.",
        "christian": {
            "quotes": [
                Q(
                    "Hear, O Israel: the Lord our God, the Lord is one… and one Lord, Jesus Christ…",
                    "Mark 12:29 + 1 Cor 8:6 (combined Christian reading)",
                    "Shema affirmed; Lord-title applied",
                    "https://www.biblegateway.com/passage/?search=1%20Corinthians%208%3A6&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "They have certainly disbelieved who say, 'Allah is the Messiah, son of Mary.'",
                    "Qur'an 5:17",
                    "Primary text",
                    "https://quran.com/5/17",
                ),
            ],
        },
        "live": {
            "if_they_say": "Worshiping Jesus is polytheism, period.",
            "you_say": "If Jesus is the incarnate Word of the one God, it is not a second god. If he is only a prophet, it is shirk. The identity claim is the whole debate — don't smuggle the conclusion into the definition.",
            "dont_overclaim": "Don't pretend the grammar is intuitive to a 7th-century Arabian polemic. Don't pretend 5:17 doesn't exist.",
        },
    },
    "moral-meaning-cross": {
        "why_it_matters": "Even if 4:157 can be reread, the cross as saving event is still the Christian vision's heart.",
        "christian": {
            "quotes": [
                Q(
                    "But God proves his love for us in that while we still were sinners Christ died for us.",
                    "Romans 5:8",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Romans%205%3A8&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "No bearer of burdens will bear the burden of another.",
                    "Qur'an 6:164",
                    "Anti-vicarious-punishment prooftext (as used in debates)",
                    "https://quran.com/6/164",
                ),
            ],
            "data_points": [
                D("Islam: God forgives by tawba and mercy without a blood payment; a crucified God looks unnecessary or unjust.", "Q 39:53"),
            ],
        },
        "live": {
            "if_they_say": "Atonement is divine child-abuse.",
            "you_say": "If the Son freely offers himself and is one with the Father, it is not a third-party child. If you reject that identity, the moral objection follows. Identity again.",
            "dont_overclaim": "Don't mock Jewish/Christian sacrifice language. Don't pretend 6:164 was written as a commentary on Anselm.",
        },
    },
    "word-spirit-titles": {
        "why_it_matters": "Shared high titles are a trap: each side thinks the other is inches from converting.",
        "christian": {
            "quotes": [
                Q(
                    "The Messiah, Jesus, son of Mary, was a messenger of Allah and His word… and a spirit from Him.",
                    "Qur'an 4:171",
                    "Muslim-usable and Christian-usable in different ways",
                    "https://quran.com/4/171",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("Kalimah and rūḥ are honors that still sit under 'do not say Three.'", "Same verse 4:171"),
            ],
        },
        "live": {
            "if_they_say": "The Qur'an already calls Jesus the Word, so he is God.",
            "you_say": "Read the rest of 4:171: messenger, do not say Three, Allah is one God. Title-sharing is not hypostatic union.",
            "dont_overclaim": "Don't strip 4:171 of its tawhid ending. Don't strip it of 'word' and 'spirit' either.",
        },
    },
    "virgin-birth": {
        "why_it_matters": "Rare agreement. Use it as a control: shared miracle, divergent meaning.",
        "christian": {
            "quotes": [
                Q(
                    "The angel said to her, 'The Holy Spirit will come upon you… therefore the child to be born will be holy; he will be called Son of God.'",
                    "Luke 1:35",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Luke%201%3A35&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "The likeness of Jesus with Allah is as the likeness of Adam: He created him from dust, then said to him, 'Be,' and he was.",
                    "Qur'an 3:59",
                    "Virgin birth as creation sign, not deity",
                    "https://quran.com/3/59",
                ),
            ],
        },
        "live": {
            "if_they_say": "Virgin birth proves Jesus is the Son of God.",
            "you_say": "Luke connects it to 'Son of God.' The Qur'an connects it to Adam. Same sign, two interpretations — don't treat the miracle as a unique Christian possession.",
            "dont_overclaim": "Don't deny the Muslim virgin birth. Don't pretend 3:59 is Johannine Logos.",
        },
    },
    "second-coming": {
        "why_it_matters": "Eschatology overlap that still splits: Jesus returns as judge-Messiah vs as Muslim who breaks the cross.",
        "christian": {
            "quotes": [
                Q(
                    "This Jesus, who has been taken up from you into heaven, will come in the same way as you saw him go into heaven.",
                    "Acts 1:11",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Acts%201%3A11&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("Hadith: Jesus returns, breaks the cross, kills the swine, abolishes jizya — a distinctly Islamic future Jesus.", "Sahih Bukhari 2476 / Muslim 155 (standard citations in this debate)", "https://sunnah.com/bukhari:2476"),
            ],
        },
        "live": {
            "if_they_say": "We both believe Jesus is coming back, so we're close.",
            "you_say": "Close on the return, far on who he is when he returns. Ask whether he comes to be worshiped or to correct those who worshiped him.",
            "dont_overclaim": "Don't treat all second-coming hadith as Qur'an. Don't treat Acts 1 as Qur'an either.",
        },
    },
    "prayer-worship": {
        "why_it_matters": "The practice test from the Trinity topic, aimed at Jesus personally.",
        "christian": {
            "quotes": [
                Q(
                    "Stephen prayed, 'Lord Jesus, receive my spirit.'",
                    "Acts 7:59",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Acts%207%3A59&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Indeed, those who say, 'Our Lord is Allah,' and then remain steadfast — the angels descend upon them…",
                    "Qur'an 41:30",
                    "Worship directed to Allah alone as the safe pattern",
                    "https://quran.com/41/30",
                ),
            ],
        },
        "live": {
            "if_they_say": "We only pray through Jesus, not to Jesus.",
            "you_say": "Acts 7:59 looks like prayer to Jesus. Many liturgies address the Son directly. If that's still not 'to,' define worship so the audience can test it.",
            "dont_overclaim": "Don't ignore 'through Christ' language. Don't let it hide the addressee.",
        },
    },
    "salvation-role": {
        "why_it_matters": "Soteriology is why the portraits cannot be merged by goodwill.",
        "christian": {
            "quotes": [
                Q(
                    "There is salvation in no one else, for there is no other name under heaven given among mortals by which we must be saved.",
                    "Acts 4:12",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Acts%204%3A12&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Say, 'If you love Allah, then follow me; Allah will love you and forgive you your sins.'",
                    "Qur'an 3:31",
                    "Forgiveness via following the Prophet, not via Calvary",
                    "https://quran.com/3/31",
                ),
            ],
        },
        "live": {
            "if_they_say": "Jesus is just a prophet in both religions.",
            "you_say": "Not in Christianity: he is savior. In Islam he is messenger and messiah without atonement. 'Just a prophet' is already picking Islam's portrait.",
            "dont_overclaim": "Don't erase Islamic honor of Jesus. Don't shrink Christian claims to 'great teacher.'",
        },
    },
    "injeel-content": {
        "why_it_matters": "If Injil ≠ four Gospels, the Islamic Jesus can float free of Mark. If it ≈ the Gospel Christians had in 632, collision returns.",
        "christian": {
            "data_points": [
                D("4th-c. complete-ish Greek Bibles predate Islam; crucifixion and high Christology are already in them.", "Sinaiticus / Vaticanus"),
            ],
            "manuscripts": [
                M("Codex Sinaiticus", "https://codexsinaiticus.org/en/", "Pre-Islamic Greek Bible"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Since the 'authorized' scriptures of Jews and Christians remain very much today as they existed at the time of the Prophet, it is difficult to argue that the Qur'anic references to Tawrat and Injil were only to the 'pure' Tawrat and Injil as existed at the time of Moses and Jesus.",
                    "Abdullah Saeed",
                    "The Charge of Distortion of Jewish and Christian Scriptures",
                    "https://bible-quran-video.s3.amazonaws.com/Documents/The-Charge-of-Distortion-of-Jewish-and-Christian-Scriptures_Abdullah+Saeed.pdf",
                ),
            ],
            "data_points": [
                D("Muslim reply still: Injil is a revelation to Jesus, not a later four-fold canon; tahrif can be of meaning.", "Ally / classical tahrif maʿnawī"),
            ],
        },
        "live": {
            "if_they_say": "Show me the Injil of Jesus.",
            "you_say": "If you mean a lost single book, neither of us can table it. If you mean what Christians were reading in the 7th century, we can: it already had a crucified, worshiped Jesus.",
            "dont_overclaim": "Don't invent a reconstructed Injil. Don't pretend 5:47 doesn't exist.",
        },
    },
    "prophet-succession": {
        "why_it_matters": "Ahmad/Paraclete fights try to make Jesus a pointer to Muhammad.",
        "christian": {
            "quotes": [
                Q(
                    "And I will ask the Father, and he will give you another Advocate, to be with you forever. This is the Spirit of truth…",
                    "John 14:16–17",
                    "Paraclete as Spirit, not a later Arabian prophet (Christian reading)",
                    "https://www.biblegateway.com/passage/?search=John%2014%3A16-17&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "And [mention] when Jesus, the son of Mary, said, 'O Children of Israel, indeed I am the messenger of Allah to you… giving good tidings of a messenger to come after me, whose name is Ahmad.'",
                    "Qur'an 61:6",
                    "Primary text",
                    "https://quran.com/61/6",
                ),
            ],
        },
        "live": {
            "if_they_say": "Jesus predicted Muhammad (Ahmad / Paraclete).",
            "you_say": "Q 61:6 is the Islamic claim. John 14's paraklētos is the Spirit in Christian reading. Don't bounce Greek periklytos memes without a manuscript. Fight the identity of the promised one with texts on the table.",
            "dont_overclaim": "Don't claim a Greek manuscript of periklytos unless you can show it. Don't claim 61:6 is quoting John.",
        },
    },
    "humanity-full": {
        "why_it_matters": "Docetism accusation: if Jesus only seemed to die, his humanity is at risk both in some tafsīr and in some Christian heresies.",
        "live": {
            "if_they_say": "Islam honors Jesus' humanity more because he is only a man.",
            "you_say": "A prophet who does not truly die can become less human, not more — that's the docetism warning. Chalcedon insists he is fully human. Score the claim against substitution tafsīr and against Apollinarianism, not against a slogan.",
            "dont_overclaim": "Don't say all Muslims are docetists. Don't say all Christians have a credible Jesus of Nazareth.",
        },
    },
    "transformative-power": {
        "why_it_matters": "Existential tie-breaker audiences feel: which portrait actually changes people?",
        "live": {
            "if_they_say": "Our Jesus changes lives, so he is the real one.",
            "you_say": "Transformation is data about communities, not a manuscript. Saints and sinners exist in both. Use it as a closing illustration after history and coherence, not as a proof that skips 4:157 or John 1.",
            "dont_overclaim": "Don't weaponize anecdotes. Don't sneer at the other community's piety.",
        },
    },
    "ally-vs-christian-jesus-nature": {
        "live": {
            "if_they_say": "Ally already showed the Christian Jesus is later theology.",
            "you_say": "Steal the method-symmetry demand. Then put 1 Cor 8:6 and 1 Cor 15 next to Q 4:171. A debate clip is not a stemma.",
            "dont_overclaim": "Don't treat Ally as Ehrman. Don't treat White as Hurtado.",
        },
    },
}
