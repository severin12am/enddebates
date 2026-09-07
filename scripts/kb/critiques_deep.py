# -*- coding: utf-8 -*-
from .deepen_lib import D, Q, S

OVERLAYS = {
    "crucifixion": {
        "importance": "Top 10",
        "why_it_matters": "Highest-frequency Christian historical critique of the Qur'an. If 4:157 denies the event, Islam vs the 1st-century record; if it denies the boast, the theology still diverges.",
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
                D("Q 4:157 is the collision text.", "https://quran.com/4/157"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "The point is that tafsir, not the Qur'an, denies the Crucifixion.",
                    "Todd Lawson",
                    "The Crucifixion and the Qur'an",
                    "https://almuslih.org/wp-content/uploads/2024/12/Lawson-T-%E2%80%93-The-Crucifixion-and-the-Quran.pdf",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam denies the crucifixion so it is historically false.",
            "you_say": "State the consensus, then ask whether 4:157 denies the event or the boast. Cite Lawson/AJIS diversity. Don't pretend Muslim views are one ḥadīth.",
            "dont_overclaim": "Don't hide majority tafsīr substitution. Don't hide Tacitus/Paul.",
        },
    },
    "islamic-dilemma": {
        "why_it_matters": "Best Christian logical-theological squeeze from Qur'anic verses that honor prior scripture.",
        "christian": {
            "quotes": [
                Q(
                    "Let the People of the Gospel judge by what Allah has revealed therein.",
                    "Qur'an 5:47",
                    "Primary text",
                    "https://quran.com/5/47",
                ),
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
                D("Q 5:48: Qur'an as muhaymin (guardian/criterion) over previous scripture.", "https://quran.com/5/48"),
            ],
        },
        "live": {
            "if_they_say": "The Qur'an confirms the Bible, so Muslims must accept the Gospels.",
            "you_say": "Define Injil. Affirmation of guidance therein is not a blank check for Nicene doctrine. Then argue crucifixion/deity as separate questions.",
            "dont_overclaim": "Don't invent a lost Injil you cannot describe. Don't pretend 5:47 doesn't exist.",
        },
    },
    "trinity": {
        "why_it_matters": "If the Qur'an misses the actual Christian doctrine, the polemic misfires; if it hits worship of Jesus, it still lands.",
        "christian": {
            "quotes": [
                Q(
                    "And [beware the Day] when Allah will say, 'O Jesus, Son of Mary, did you say to the people, \"Take me and my mother as deities besides Allah?\"'",
                    "Qur'an 5:116",
                    "Primary text",
                    "https://quran.com/5/116",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "And do not say, 'Three'; desist — it is better for you. Allah is but one God.",
                    "Qur'an 4:171",
                    "Primary text",
                    "https://quran.com/4/171",
                ),
            ],
        },
        "live": {
            "if_they_say": "The Qur'an thinks the Trinity is Father, Mother, Son.",
            "you_say": "5:116 is that picture. 4:171 and 5:73 still hit 'Three' and sonship without Mary. Don't collapse the file into one verse either way.",
            "dont_overclaim": "Don't pretend 5:116 is Cappadocian theology. Don't pretend 4:171 isn't aimed at Christians.",
        },
    },
    "deity-of-christ": {
        "why_it_matters": "Even unitarian-leaning historical Jesus scholars rarely become Muslims; this is about identity, not only councils.",
        "christian": {
            "quotes": [
                Q(
                    "In the beginning was the Word, and the Word was with God, and the Word was God.",
                    "John 1:1",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=John%201%3A1&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "They have certainly disbelieved who say that Allah is the Messiah, son of Mary.",
                    "Qur'an 5:17",
                    "Primary text",
                    "https://quran.com/5/17",
                ),
            ],
        },
        "live": {
            "if_they_say": "Jesus never claimed to be God, so Islam is right.",
            "you_say": "Define claim: explicit 'I am God,' or receiving worship, or John 8:58, or Mark 14:62, or 1 Cor 8:6. Then apply the same strictness to Qur'anic titles (word, spirit, messiah).",
            "dont_overclaim": "Don't pretend Mark is John. Don't pretend 5:17 is a commentary on Chalcedon.",
        },
    },
    "false-prophet": {
        "why_it_matters": "Deut 13/18 tests vs Qur'anic self-claim. Easy to do as insult; hard to do as criteria.",
        "christian": {
            "quotes": [
                Q(
                    "If a prophet… says, 'Let us follow other gods'… you must not heed the words of that prophet…",
                    "Deuteronomy 13:1–3 (abridged)",
                    "OT test as used in critiques",
                    "https://www.biblegateway.com/passage/?search=Deuteronomy%2013%3A1-5&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Muhammad is not the father of any one of your men, but he is the Messenger of Allah and last of the prophets.",
                    "Qur'an 33:40",
                    "Primary text",
                    "https://quran.com/33/40",
                ),
            ],
            "data_points": [
                D("Muslim reply: Deut tests assume Israel's covenant; a later prophet to the nations is not 'other gods' if he preaches tawhid.", "Q 21:25"),
            ],
        },
        "live": {
            "if_they_say": "Deuteronomy proves Muhammad is a false prophet.",
            "you_say": "State the test: other gods vs signs. Islam claims continuity of tawhid, not Baal. Then you must argue that Jesus' identity is the true God-test, or that moral/war files fail a prophet-test. Don't treat Deut 13 as a magic word.",
            "dont_overclaim": "Don't skip Jesus' own conflicts with Deut-reading opponents. Don't skip 33:40.",
        },
    },
    "quran-preservation": {
        "why_it_matters": "Folk dawah vs manuscripts. Same file as historicity Top 10.",
        "christian": {
            "quotes": [
                Q(
                    "It's very clear that the standard narrative has holes in it.",
                    "Yasir Qadhi",
                    "Interview with Mohammed Hijab, 8 June 2020",
                    "https://en.wikipedia.org/wiki/Yasir_Qadhi",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "All Quranic manuscripts, with one exception, belong to the same Uthmanic text type.",
                    "Marijn van Putten",
                    "BSOAS 82 (2019)",
                    "https://doi.org/10.1017/s0041977x19000338",
                ),
                Q(
                    "The Qur'an has never been a uniformic text, but rather a multiformic text.",
                    "Ali Ataie",
                    "The Sound Narrative (~8:04)",
                    "https://www.youtube.com/watch?v=5XuiZLfEb64",
                ),
                Q(
                    "By all indications, the manuscript evidence is consistent with the traditional narrative regarding the ʿUthmānic standardization.",
                    "Hythem Sidky",
                    "Al-ʿUṣūr al-Wusṭā 27 (2019), review of Brubaker",
                    "https://www.middleeastmedievalists.com/wp-content/uploads/2019/11/UW-27-Sidky.pdf",
                ),
            ],
        },
        "live": {
            "if_they_say": "Every letter of the Qur'an is identical worldwide.",
            "you_say": "Identical rasm, identical Hafs print, or all ten qira'at? Sidky: four ancestral regional copies, consistent with ʿUthmān. Ataie: the uniformic slogan is the own-goal. Pin the thesis, then Sanaa/Qadhi become relevant.",
            "dont_overclaim": "Don't turn qira'at into 93,000 Qur'ans. Don't deny companion reports. Don't treat a stemma as a miracle.",
        },
    },
    "violence-jihad": {
        "why_it_matters": "Audience magnet. Requires 2:190 and 9:5 in the same minute.",
        "christian": {
            "quotes": [
                Q(
                    "And when the sacred months have passed, then kill the polytheists wherever you find them…",
                    "Qur'an 9:5",
                    "Primary text",
                    "https://quran.com/9/5",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Fight in the way of Allah those who fight you but do not transgress.",
                    "Qur'an 2:190",
                    "Primary text",
                    "https://quran.com/2/190",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam is a violent religion because of 9:5.",
            "you_say": "Read 9:4–7 with it. Compare Joshua 6. Then specify: founding wars, classical fiqh, or modern terrorism. Those are three debates.",
            "dont_overclaim": "Don't abrogate 2:256 with a YouTube clip. Don't hide 9:29.",
        },
    },
    "apostasy": {
        "why_it_matters": "Liberty of conscience vs classical ḥadd. One of the hardest live-audience files for Muslim debaters.",
        "christian": {
            "data_points": [
                D("Bukhari 6922: 'Whoever changed his Islamic religion, then kill him' — staple citation (evaluate isnād/fiqh scope in good faith).", "https://sunnah.com/bukhari:6922"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "There is no compulsion in religion.",
                    "Qur'an 2:256",
                    "Primary text used against a simple ḥadd slogan",
                    "https://quran.com/2/256",
                ),
            ],
            "data_points": [
                D("Reform argument: Qur'an mentions apostasy without an earthly death penalty (e.g. 4:137); ḥadd is extra-Qur'anic hadith/fiqh.", "Q 4:137"),
            ],
        },
        "live": {
            "if_they_say": "Islam kills apostates; therefore it is false or evil.",
            "you_say": "Classical fiqh often does. 2:256 and 4:137 are the internal tension. Christianity's Deut 13 and heresy executions are the tu quoque. Then: which view is still taught as God's law today?",
            "dont_overclaim": "Don't say no Muslim scholar ever mandated death. Don't say Jesus ran the Inquisition.",
        },
    },
    "women": {
        "why_it_matters": "4:34 and polygyny will be asked. Prepare the verse, not a vibe.",
        "christian": {
            "quotes": [
                Q(
                    "…and [finally], strike them…",
                    "Qur'an 4:34",
                    "Critique rendering of ḍaraba",
                    "https://quran.com/4/34",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Never will I allow to be lost the work of [any] worker among you, whether male or female; you are of one another.",
                    "Qur'an 3:195",
                    "Spiritual equality",
                    "https://quran.com/3/195",
                ),
            ],
        },
        "live": {
            "if_they_say": "The Qur'an tells men to beat their wives.",
            "you_say": "4:34 is the verse. Grant ḍaraba's classical reading, then restriction reports, Wadud-style rereadings, and 1 Tim 2 / Eph 5. Don't debate a meme vs a greeting card.",
            "dont_overclaim": "Don't pretend ḍaraba never meant strike. Don't pretend the NT has no household codes.",
        },
    },
    "salvation": {
        "why_it_matters": "Endgame of many critiques: how are sins actually dealt with?",
        "christian": {
            "quotes": [
                Q(
                    "For by grace you have been saved through faith… not the result of works.",
                    "Ephesians 2:8–9",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Ephesians%202%3A8-9&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Do not despair of the mercy of Allah. Indeed, Allah forgives all sins.",
                    "Qur'an 39:53",
                    "Primary text",
                    "https://quran.com/39/53",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam has no atonement, so God is unjust or sins aren't serious.",
            "you_say": "Islam: tawba + mercy + deeds + possibly intercession. Christianity: cross as satisfaction/victory. Both take sin seriously. The crux is whether blood is required, not whether God 'just shrugs.'",
            "dont_overclaim": "Don't turn 39:53 into cheap grace. Don't turn the cross into divine child-abuse without answering the identity claim.",
        },
    },
}
