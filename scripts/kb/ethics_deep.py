# -*- coding: utf-8 -*-
from .deepen_lib import D, Q, S

WARFARE = {
    "jesus-enemy-love": {
        "why_it_matters": "Highest Christian moral altitude claim. If it is the ethic, armed prophethood looks like a downgrade. If it is interim pacifism, the NT church's later just war is the real comparator.",
        "christian": {
            "quotes": [
                Q(
                    "But I say to you, Love your enemies and pray for those who persecute you.",
                    "Matthew 5:44",
                    "Sermon on the Mount",
                    "https://www.biblegateway.com/passage/?search=Matthew%205%3A44&version=NRSVUE",
                ),
                Q(
                    "Put your sword back into its place; for all who take the sword will perish by the sword.",
                    "Matthew 26:52",
                    "Gethsemane",
                    "https://www.biblegateway.com/passage/?search=Matthew%2026%3A52&version=NRSVUE",
                ),
            ],
            "data_points": [
                D("Jesus' kingdom is 'not from this world' (John 18:36) — Christian readings split on whether that bans all state violence.", "John 18:36"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Permission [to fight] has been given to those who are being fought, because they were wronged.",
                    "Qur'an 22:39",
                    "Permission verse",
                    "https://quran.com/22/39",
                ),
            ],
            "data_points": [
                D("Romans 13 and Luke 22:36 are used to show the NT is not simple pacifism.", "Rom 13:1–4; Luke 22:36"),
                D("A prophet with political authority faces questions Jesus, in the Gospels, does not — apples to oranges unless you compare Constantine/just war to siyar.", "Genre/office argument"),
            ],
        },
        "live": {
            "if_they_say": "Jesus never fought, so Christianity is the peace religion.",
            "you_say": "Jesus' personal nonviolence is real. Then ask what Christians did with armies for 1700 years, and whether the fair Islamic comparator is Muhammad in Medina or a village Sufi. Match offices: preacher vs statesman, or church vs umma.",
            "dont_overclaim": "Don't erase Crusades. Don't erase Maghāzī.",
        },
    },
    "defensive-jihad": {
        "why_it_matters": "Street slogan vs 9:5/9:29. Definitions of 'defensive' decide the round.",
        "christian": {
            "quotes": [
                Q(
                    "And when the sacred months have passed, then kill the polytheists wherever you find them…",
                    "Qur'an 9:5",
                    "Sword verse (as cited in critiques)",
                    "https://quran.com/9/5",
                ),
                Q(
                    "Fight those who do not believe in Allah or in the Last Day… from those who were given the Book, until they give the jizya willingly while they are humbled.",
                    "Qur'an 9:29",
                    "People of the Book fighting verse",
                    "https://quran.com/9/29",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Fight in the way of Allah those who fight you but do not transgress. Indeed, Allah does not like transgressors.",
                    "Qur'an 2:190",
                    "Limitation verse",
                    "https://quran.com/2/190",
                ),
                Q(
                    "There is no compulsion in religion.",
                    "Qur'an 2:256",
                    "Prooftext against forced conversion",
                    "https://quran.com/2/256",
                ),
            ],
            "data_points": [
                D("Asbāb al-nuzūl for 9:5 typically tie it to treaty-breaking pagans, not a timeless 'kill all unbelievers' license — fight the tafsīr, don't ignore 9:5.", "Classical tafsīr of Sūrat al-Tawba"),
                D("Reuven Firestone and others: Qur'anic war verses are historically layered, not a single slogan.", "Firestone, Jihad: The Origin of Holy War in Islam"),
            ],
            "sources": [
                S("Firestone, Jihad (OUP)", "https://global.oup.com/academic/product/jihad-9780195125805"),
            ],
        },
        "counters": [
            {
                "against": "Christian 9:5 isolated",
                "claim": "Islam's last word is 'kill the polytheists.'",
                "reply": "Read 9:4–7 (treaty-keepers excepted) and 2:190. Then compare herem texts in Joshua. Isolation is a method both sides abuse.",
            },
        ],
        "live": {
            "if_they_say": "9:5 abrogates all peaceful verses.",
            "you_say": "Abrogation is a real classical theory — don't deny it. Then ask which legal school, whether 9:5 is bound to ḥudaybiya-breakers, and what 9:6 (granting asylum) is doing in the same passage.",
            "dont_overclaim": "Don't pretend 9:5 is a greeting-card. Don't pretend 2:256 deleted 9:29 from fiqh.",
        },
    },
    "noncombatants": {
        "why_it_matters": "Conduct of war is where both traditions have usable law and ugly history.",
        "christian": {
            "quotes": [
                Q(
                    "Augustine and later Aquinas distinguish just cause from right conduct (jus ad bellum / jus in bello).",
                    "Just-war tradition (summary)",
                    "Aquinas, ST II-II q.40",
                    "https://www.newadvent.org/summa/3040.htm",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Do not kill a woman, nor a child, nor an old man, nor cut down fruit trees…",
                    "Abū Bakr's reported instructions to armies (standard siyar citation)",
                    "Transmitted in siyar / tārīkh collections; wording varies by report",
                    "https://shamela.ws/",
                ),
            ],
            "data_points": [
                D("Prophetic hadith against killing women and children in combat is a mainstream siyar building block.", "Bukhari 3014–3015 area; Muslim 1744"),
            ],
            "sources": [
                S("Sahih Bukhari — killing women/children", "https://sunnah.com/bukhari:3014"),
            ],
        },
        "live": {
            "if_they_say": "Islam has no civilian protection.",
            "you_say": "Siyar texts do. Then both of you have to survive your own history: Maghāzī raids, Crusader massacres, 20th-c. bombing. Law on the page vs practice is the shared human problem.",
            "dont_overclaim": "Don't cite ISIS as 'the' fiqh. Don't cite a just-war manual as 'the' Crusades.",
        },
    },
    "just-war-tradition": {
        "why_it_matters": "Adult comparison: Aquinas vs Shaybānī, not Jesus-the-pacifist vs a YouTube clip of 9:5.",
        "christian": {
            "sources": [
                S("Aquinas ST II-II 40", "https://www.newadvent.org/summa/3040.htm"),
            ],
        },
        "muslim": {
            "data_points": [
                D("Majid Khadduri's translation of Shaybānī is the usual English gateway to classical siyar.", "The Islamic Law of Nations"),
            ],
            "sources": [
                S("Khadduri, The Islamic Law of Nations", "https://press.jhu.edu/books/title/1671/islamic-law-nations"),
            ],
        },
        "live": {
            "if_they_say": "Only Christians invented just war.",
            "you_say": "Just-war vocabulary is Latin-Christian. Limitation-of-war as law is not unique. Compare Shaybānī and Aquinas on cause, authority, and noncombatants — then score.",
            "dont_overclaim": "Don't baptize either tradition as the Geneva Conventions.",
        },
    },
    "ot-holy-war": {
        "why_it_matters": "Best Muslim tu quoque. Christians must have a theology of herem, not a memory-hole.",
        "christian": {
            "quotes": [
                Q(
                    "They devoted to destruction by the edge of the sword all in the city, both men and women, young and old, oxen, sheep, and donkeys.",
                    "Joshua 6:21",
                    "Jericho ḥērem",
                    "https://www.biblegateway.com/passage/?search=Joshua%206%3A21&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("If OT ḥērem is 'old covenant,' say what moral rule makes Qur'anic jihad still live while Joshua is dead.", "Hermeneutics demand"),
            ],
        },
        "live": {
            "if_they_say": "The Qur'an is uniquely violent.",
            "you_say": "Open Joshua 6 and 1 Samuel 15. Then discuss covenant, typology, and whether Muhammad's wars look more like Joshua, like David, or like Augustine. Isolation is not a method.",
            "dont_overclaim": "Don't say Joshua didn't happen as a moral free pass. Don't say 9:5 is just like a psalm of lament.",
        },
    },
    "crusades-colonialism": {
        "why_it_matters": "History dump round. Force a metric: founding texts vs later empires.",
        "live": {
            "if_they_say": "Christianity is Crusades and colonialism.",
            "you_say": "Those are Christian-world crimes. Maghāzī, ridda, futūḥ, and later sultanates are Muslim-world wars. Score founders, classical law, and modern outcomes separately or you are just trading body counts.",
            "dont_overclaim": "Don't excuse atrocity as 'context' only for your side.",
        },
    },
    "apostasy-blasphemy-war": {
        "why_it_matters": "Where warfare ethics bleeds into liberty of conscience.",
        "christian": {
            "data_points": [
                D("Deut 13 and later Christendom's heresy laws are the Christian skeleton in this closet.", "Deut 13"),
            ],
        },
        "muslim": {
            "data_points": [
                D("Classical ridda/hiraba and sabb al-rasūl rulings are the Islamic skeleton.", "Fiqh manuals; Bukhari 6922 area"),
            ],
        },
        "live": {
            "if_they_say": "Islam kills apostates, Christianity doesn't.",
            "you_say": "Classical fiqh often does prescribe death for apostasy. Christian history often did too. The live question is which scriptures still authorize it as a religious good, and who reformed.",
            "dont_overclaim": "Don't pretend all Muslim states apply hudud. Don't pretend the Inquisition is a cartoon with no bodies.",
        },
    },
    "prisoners-spoils": {
        "why_it_matters": "Q 47:4, 8:41, 33:50 vs NT silence / later church practice.",
        "muslim": {
            "quotes": [
                Q(
                    "So when you meet those who disbelieve [in battle], strike [their] necks until, when you have inflicted slaughter upon them, then secure their bonds, and either [confer] favor afterwards or ransom [them]…",
                    "Qur'an 47:4",
                    "Prisoners: grace or ransom",
                    "https://quran.com/47/4",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam legalized war-booty and concubinage.",
            "you_say": "8:41 and 4:24 are in the book — grant the texts. Then compare OT spoils (Num 31) and Christian just-war ransom practice. The distinctive Islamic fight is whether those rules remain exemplary.",
            "dont_overclaim": "Don't deny the verses. Don't pretend medieval Christians had clean hands on captives.",
        },
    },
    "terrorism-takfir": {
        "why_it_matters": "Modern audiences start here. You still need a text-to-practice map.",
        "christian": {
            "data_points": [
                D("Graeme Wood's ISIS analysis: they were following a coherent extreme reading, not 'no Islam.'", "Wood, What ISIS Really Wants / The Way of the Strangers"),
            ],
        },
        "muslim": {
            "data_points": [
                D("Mainstream fiqh: targeting civilians, breaking oaths, and indiscriminate takfir are ḥarām; Khawārij are the classical warning tale.", "Classical ḥudūd / siyar + modern marājiʿ statements"),
            ],
        },
        "live": {
            "if_they_say": "ISIS is true Islam.",
            "you_say": "They cited Islamic texts. So did their Muslim enemies. The adult move is: which reading is central vs extreme, and what does the same method do to Christian Reconstructionist violence.",
            "dont_overclaim": "Don't say 'nothing to do with Islam.' Don't say 'this is all Muslims.'",
        },
    },
    "proportionality-treaties": {
        "why_it_matters": "Where both can sound like Geneva — and both can be accused of bad faith.",
        "muslim": {
            "quotes": [
                Q(
                    "Excepted are those with whom you made a treaty among the polytheists and they have not been deficient toward you… so fulfill their treaty to its term.",
                    "Qur'an 9:4",
                    "Treaty-keeping beside 9:5",
                    "https://quran.com/9/4",
                ),
            ],
        },
        "christian": {
            "data_points": [
                D("Pacta sunt servanda in just-war and in Grotius sits in a Christian-European legal story.", "Grotius, De jure belli"),
            ],
        },
        "live": {
            "if_they_say": "Muslims may break any treaty with unbelievers.",
            "you_say": "9:4 and 8:72 and the Constitution of Medina tradition cut against that slogan. Then discuss Hudaybiyyah and whether 'no compulsion' survives conquest. Slogans both ways are lazy.",
            "dont_overclaim": "Don't ignore 9:1–15's treaty-break frame. Don't ignore Christian colonial treaty-breaking.",
        },
    },
}

WOMEN = {
    "jesus-and-women": {
        "why_it_matters": "Christian opening: Jesus' practice as paradigm vs later church and vs fiqh.",
        "christian": {
            "quotes": [
                Q(
                    "There is no longer Jew or Greek, there is no longer slave or free, there is no longer male and female; for all of you are one in Christ Jesus.",
                    "Galatians 3:28",
                    "Baptismal equality text",
                    "https://www.biblegateway.com/passage/?search=Galatians%203%3A28&version=NRSVUE",
                ),
            ],
            "data_points": [
                D("Gospels: women as first resurrection witnesses; Jesus speaking with the Samaritan woman; Mary of Bethany as disciple.", "John 4; John 20; Luke 10"),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "And their Lord responded to them, 'Never will I allow to be lost the work of [any] worker among you, whether male or female; you are of one another.'",
                    "Qur'an 3:195",
                    "Spiritual equality text",
                    "https://quran.com/3/195",
                ),
            ],
            "data_points": [
                D("1 Tim 2:12 and 1 Cor 14:34 are the Christian counter-texts Muslims will read aloud.", "Pastoral epistles"),
            ],
        },
        "live": {
            "if_they_say": "Jesus was a feminist; Muhammad was not.",
            "you_say": "Jesus' counter-cultural honor of women is real. Then put 1 Timothy 2 and Q 4:34 on the same table, plus each community's law after the founder. Founder-anecdote vs legal system is the honest split.",
            "dont_overclaim": "Don't hide Paul. Don't hide Khadīja/Āʿisha either.",
        },
    },
    "polygyny": {
        "why_it_matters": "Clear legal difference. Christians usually win the modern audience unless Muslims reframe as regulated vs hypocritical serial monogamy.",
        "christian": {
            "quotes": [
                Q(
                    "Each man [should have] his own wife and each woman her own husband.",
                    "1 Corinthians 7:2",
                    "As used against polygyny",
                    "https://www.biblegateway.com/passage/?search=1%20Corinthians%207%3A2&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "…marry those that please you of [other] women, two or three or four. But if you fear that you will not be just, then [marry only] one…",
                    "Qur'an 4:3",
                    "Polygyny with justice condition",
                    "https://quran.com/4/3",
                ),
                Q(
                    "And you will never be able to be equal [in feeling] between wives, even if you should strive [to do so].",
                    "Qur'an 4:129",
                    "Used by some as near-ban via impossibility of justice",
                    "https://quran.com/4/129",
                ),
            ],
            "data_points": [
                D("OT patriarchs are polygynous; Christian argument needs a covenant-change story, not amnesia.", "Abraham, Jacob, David"),
            ],
        },
        "live": {
            "if_they_say": "Islam lets men have four wives, so it oppresses women.",
            "you_say": "4:3 is in the book. Grant it. Then: justice condition, 4:129, historical OT, and whether Western serial marriage plus infidelity is the actual comparator. Still a live inequality if only men get the extra license.",
            "dont_overclaim": "Don't say Islam mandates four wives. Don't say the NT is a modern egalitarian charter.",
        },
    },
    "quran-4-34": {
        "why_it_matters": "The verse. If you cannot steelman nushūz, ḍaraba, and reform readings, you will look like a slogan machine.",
        "christian": {
            "quotes": [
                Q(
                    "…But those [wives] from whom you fear arrogance — [first] advise them; [then if they persist], forsake them in bed; and [finally], strike them…",
                    "Qur'an 4:34",
                    "Saheeh International-type rendering used in critiques",
                    "https://quran.com/4/34",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("Classical tafsīr generally allows a (disputed-degree) strike; many moderns (Wadud, others) reread ḍaraba as 'separate' or as a failed 7th-c. concession.", "Amina Wadud; Kecia Ali, Sexual Ethics and Islam"),
                D("Hadith: 'The best of you are the best to their wives' is the pastoral counter-weight Muslims will quote.", "Tirmidhi 1162 area"),
            ],
            "sources": [
                S("Kecia Ali, Sexual Ethics and Islam", "https://oneworld-publications.com/work/sexual-ethics-and-islam/"),
            ],
        },
        "live": {
            "if_they_say": "The Qur'an tells men to beat their wives.",
            "you_say": "4:34 is the verse; ḍaraba is the verb; three-step sequence is the grammar. Don't deny the text. Then: prophetic 'do not beat' reports, legal restrictions, and Christian household codes (Eph 5 / 1 Pet 3). Fight translation and whether the verse is timeless law.",
            "dont_overclaim": "Don't pretend ḍaraba never meant strike. Don't pretend Ephesians 5 is a UN convention.",
        },
    },
    "inheritance-testimony": {
        "why_it_matters": "Quantifiable legal inequality vs a financial-structure defense.",
        "muslim": {
            "quotes": [
                Q(
                    "Allah instructs you concerning your children: for the male, what is equal to the share of two females.",
                    "Qur'an 4:11",
                    "Inheritance ratio",
                    "https://quran.com/4/11",
                ),
                Q(
                    "And bring to witness two witnesses from among your men. And if there are not two men [available], then a man and two women from those whom you accept as witnesses…",
                    "Qur'an 2:282",
                    "Debt-contract testimony",
                    "https://quran.com/2/282",
                ),
            ],
            "data_points": [
                D("Muslim defense: men owed nafaqa/mahr; shares are a system, not a one-verse insult. Critics: testimony still looks like a competence slight, and modern women also earn.", "Fiqh of nafaqa vs modern labor"),
            ],
        },
        "christian": {
            "data_points": [
                D("Num 27 (daughters of Zelophehad) and later Christian civil law are the usual Christian counters — mixed historical record on property.", "Numbers 27"),
            ],
        },
        "live": {
            "if_they_say": "A woman's testimony is worth half.",
            "you_say": "2:282 is a debt-document rule, not a universal IQ claim — grant that nuance. Then ask why the verse's reason ('that if one of the women errs, the other can remind her') isn't still a competence hierarchy, and how courts work today.",
            "dont_overclaim": "Don't extend 2:282 to all testimony if fiqh doesn't. Don't pretend the verse is about parking tickets in Oslo.",
        },
    },
    "divorce-mahr": {
        "why_it_matters": "Islamic family law's best 'protection' card vs ṭalāq asymmetry.",
        "muslim": {
            "quotes": [
                Q(
                    "And give the women [upon marriage] their [bridal] gifts graciously.",
                    "Qur'an 4:4",
                    "Mahr as her property",
                    "https://quran.com/4/4",
                ),
            ],
        },
        "christian": {
            "quotes": [
                Q(
                    "Whoever divorces his wife, except for sexual immorality, and marries another, commits adultery.",
                    "Matthew 19:9",
                    "Jesus on divorce (as Christian high bar)",
                    "https://www.biblegateway.com/passage/?search=Matthew%2019%3A9&version=NRSVUE",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam makes divorce easy for men and traps women.",
            "you_say": "Ṭalāq is historically easier for the husband; khulʿ and mahr are the counter-institutions. Jesus' divorce ethic is stricter for both — then look at Christian civil divorce rates. Law vs culture, again.",
            "dont_overclaim": "Don't say Muslim women cannot divorce. Don't say Matthew 19 is how all churches operate.",
        },
    },
    "modesty-veiling": {
        "why_it_matters": "Visual politics. Need 24:31, 33:59, 1 Cor 11 on the table.",
        "muslim": {
            "quotes": [
                Q(
                    "…tell your wives and your daughters and the women of the believers to bring down over themselves [part] of their outer garments.",
                    "Qur'an 33:59",
                    "Jilbāb verse",
                    "https://quran.com/33/59",
                ),
            ],
        },
        "christian": {
            "quotes": [
                Q(
                    "…if a woman will not veil herself, then she should cut off her hair…",
                    "1 Corinthians 11:6",
                    "Pauline head-covering (as tu quoque / shared modesty)",
                    "https://www.biblegateway.com/passage/?search=1%20Corinthians%2011%3A6&version=NRSVUE",
                ),
            ],
        },
        "live": {
            "if_they_say": "Hijab is oppression unique to Islam.",
            "you_say": "33:31/33:59 are the texts. 1 Cor 11 is the Christian cousin. The distinctive fight is state compulsion vs voluntary piety, and whether covering is a salvation issue.",
            "dont_overclaim": "Don't say the Qur'an requires a specific Saudi niqab. Don't say Paul is irrelevant because your church skipped it.",
        },
    },
    "leadership": {
        "why_it_matters": "Imamate, priesthood, and 1 Tim 2 vs female monarchs and ʿĀʾisha at the Camel.",
        "christian": {
            "quotes": [
                Q(
                    "I permit no woman to teach or to have authority over a man; she is to keep silent.",
                    "1 Timothy 2:12",
                    "Restriction text",
                    "https://www.biblegateway.com/passage/?search=1%20Timothy%202%3A12&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("Hadith 'a people who appoint a woman as their leader will never succeed' is the staple restriction text (Bukhari 7099).", "https://sunnah.com/bukhari:7099"),
            ],
        },
        "live": {
            "if_they_say": "Islam forbids female leaders; Christianity doesn't.",
            "you_say": "Bukhari 7099 vs 1 Timothy 2: both traditions have restriction texts and exception histories (Deborah, ʿĀʾisha, Elizabeth I, Benazir). Score texts, majority fiqh/canon law, and present practice separately.",
            "dont_overclaim": "Don't erase Deborah. Don't erase female heads of Muslim-majority states as if fiqh vanished.",
        },
    },
    "sexual-ethics": {
        "why_it_matters": "Zina, consent, and double standards. Overlaps slavery's concubinage fight.",
        "live": {
            "if_they_say": "Islam is obsessed with controlling female sexuality.",
            "you_say": "Both canons police sex. Put zina ḥadd, John 8, and 1 Cor 6 on the table. The distinctive Islamic texts are 24:2, 4:15–16, and slave-concubinage. Distinctive Christian fights are later purity culture vs Jesus and the accused woman.",
            "dont_overclaim": "Don't make John 8 the whole NT ethic if your tradition also ran Magdalene asylums.",
        },
    },
    "mary-maryam": {
        "why_it_matters": "Honor overlap. Muslims will quote 3:42; Christians will say honor ≠ legal equality.",
        "muslim": {
            "quotes": [
                Q(
                    "O Mary, indeed Allah has chosen you and purified you and chosen you above the women of the worlds.",
                    "Qur'an 3:42",
                    "Maryam's election",
                    "https://quran.com/3/42",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam honors Mary more than Christians do.",
            "you_say": "3:42 is extraordinary honor. Catholic/Orthodox Marian piety is also extraordinary. Neither automatically yields inheritance law or courtroom standing. Don't confuse liturgical honor with rights.",
            "dont_overclaim": "Don't say Muslims worship Mary (5:116 is a polemic, not a self-description). Don't say Protestants have no Mary.",
        },
    },
    "modern-outcomes": {
        "why_it_matters": "Indices, not verses — easy to abuse, still part of public debate.",
        "live": {
            "if_they_say": "Look at women's rights indices: Christian countries win.",
            "you_say": "Many high-scoring states are post-Christian liberal, not Sermon-on-the-Mount jurisdictions. Many low-scoring states mix oil autocracy, custom, and fiqh. Use data, then ask which texts still resist reform.",
            "dont_overclaim": "Don't treat UNDP as a tafsīr. Don't treat a pious village as Sweden.",
        },
    },
}

SLAVERY = {
    "both-regulate": {
        "why_it_matters": "Kills the cartoon that one religion is abolitionist in the modern sense from page one.",
        "christian": {
            "quotes": [
                Q(
                    "Let all who are under the yoke of slavery regard their masters as worthy of all honor…",
                    "1 Timothy 6:1",
                    "Household code",
                    "https://www.biblegateway.com/passage/?search=1%20Timothy%206%3A1&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "And those who seek a contract [for eventual emancipation] from among whom your right hands possess — then make a contract with them if you know there is within them goodness and give them from the wealth of Allah which He has given you.",
                    "Qur'an 24:33",
                    "Mukātaba encouragement",
                    "https://quran.com/24/33",
                ),
            ],
        },
        "live": {
            "if_they_say": "My book abolished slavery; yours didn't.",
            "you_say": "Neither Testament nor Qur'an is the 13th Amendment. Both regulate. The fight is trajectory, manumission incentives, concubinage, and who actually abolished when.",
            "dont_overclaim": "Don't baptize either founder as William Wilberforce.",
        },
    },
    "philemon-trajectory": {
        "why_it_matters": "Best Christian 'seed of abolition' text. Needs honesty that it is a seed, not a statute.",
        "christian": {
            "quotes": [
                Q(
                    "Perhaps this is the reason he was separated from you for a while, so that you might have him back forever, no longer as a slave but more than a slave, a beloved brother…",
                    "Philemon 15–16",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Philemon%201-25&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("Q 90:13 and 9:60 make freeing slaves a pious good — a parallel 'seed' Muslims will claim.", "https://quran.com/90/13"),
            ],
        },
        "live": {
            "if_they_say": "Philemon proves Christianity ended slavery.",
            "you_say": "It relativizes the master-slave relation in Christ. It does not command manumission in verse 1. Trajectory arguments must survive 1800 years of Christian slaveholding.",
            "dont_overclaim": "Don't call Paul an abolitionist. Don't call the Qur'an one either.",
        },
    },
    "manumission-incentives": {
        "why_it_matters": "Islam's strongest structural claim: kaffāra, zakāt, mukātaba.",
        "muslim": {
            "quotes": [
                Q(
                    "It is the freeing of a slave…",
                    "Qur'an 90:13",
                    "Steep path includes manumission",
                    "https://quran.com/90/13",
                ),
            ],
            "data_points": [
                D("Expiation for certain oaths/sins includes freeing a slave (Q 5:89; 58:3).", "Kaffāra verses"),
            ],
        },
        "live": {
            "if_they_say": "Islam wanted slavery to fade.",
            "you_say": "Incentives to free are real. So is an ongoing lawful status for captives and those born into slavery. A system can both manumit and replenish. Ask whether the replenishment path (war captives) is still moral.",
            "dont_overclaim": "Don't deny 90:13. Don't treat it as a sunset clause with a date.",
        },
    },
    "war-captives-sex": {
        "why_it_matters": "Usually the sharpest ethical collision in this topic. 4:24 / 23:5–6 / 33:50.",
        "christian": {
            "quotes": [
                Q(
                    "And [also prohibited to you are] all married women except those your right hands possess.",
                    "Qur'an 4:24",
                    "As read in critiques of concubinage",
                    "https://quran.com/4/24",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("Jonathan A.C. Brown's Slavery and Islam is the book-length Muslim-academic attempt to face this file.", "Brown, Slavery and Islam"),
                D("OT: Numbers 31 and Deut 21:10–14 are the tu quoque texts.", "Deut 21:10–14"),
            ],
            "sources": [
                S("Brown, Slavery and Islam", "https://oneworld-publications.com/work/slavery-and-islam/"),
                S("Deut 21:10–14", "https://www.biblegateway.com/passage/?search=Deuteronomy%2021%3A10-14&version=NRSVUE"),
            ],
        },
        "live": {
            "if_they_say": "The Qur'an permits sex with slaves.",
            "you_say": "Mā malakat aymānukum is in the Qur'an. Grant the institution. Then: consent, marriage-to-slave, OT captive-wife law, and whether 'historical regulation' is still a defense after abolition. Don't euphemize.",
            "dont_overclaim": "Don't say it was 'just like employment.' Don't say no Christian ever baptized a slave-society.",
        },
    },
    "atlantic-vs-islamic-trades": {
        "why_it_matters": "Body-count and race-structure fight. Easy to do badly.",
        "live": {
            "if_they_say": "The transatlantic trade was uniquely Christian and uniquely evil.",
            "you_say": "Scale, race-making, and New World chattel are historically specific. The Islamic world's slave trades (including East African and Caucasian) are also historically specific. Unique ≠ only. Use historians (Davis, Lewis, Lovejoy), not memes.",
            "dont_overclaim": "Don't erase the transatlantic horror. Don't erase Zanj, Crimean, or Barbary trades.",
        },
    },
    "jesus-paul-silence": {
        "why_it_matters": "Why didn't the NT ban it? Honest Christian answer needed.",
        "live": {
            "if_they_say": "If Jesus is God, why didn't he abolish slavery?",
            "you_say": "Same form of question Muslims get about 4:24. Answers available: eschatological delay, household-code gradualism, spiritual equality first. None of those is a modern abolition statute. Admit it.",
            "dont_overclaim": "Don't say Jesus secretly published the 13th Amendment.",
        },
    },
    "race": {
        "why_it_matters": "Curse of Ham vs no racial slave caste in fiqh vs actual racist practice both ways.",
        "live": {
            "if_they_say": "Christianity invented racial slavery.",
            "you_say": "Early Christian slavery was not a color line. Later Atlantic Christianity often racialized it. Islamic law is typically color-blind on paper and was not always so in markets. Score doctrine vs practice.",
            "dont_overclaim": "Don't hang the curse of Ham on Jesus. Don't hang every racist market on fiqh.",
        },
    },
    "abolition-timing": {
        "why_it_matters": "Who actually passed statutes, and whether that was because of the religion or Enlightenment/secular pressure.",
        "live": {
            "if_they_say": "Christians abolished slavery; Muslims lagged.",
            "you_say": "British/American abolition had Christian activists (Woolman, Wilberforce, Equiano's public) and economic/imperial politics. Ottoman and later Muslim-state abolitions are late and often under European pressure. Also: Christian states ran the trade first. Sequence is not a sermon.",
            "dont_overclaim": "Don't make Wilberforce the whole church. Don't make 1962 Saudi abolition the whole umma.",
        },
    },
    "concubinage-vs-household": {
        "why_it_matters": "Different textures of the same sin-structure.",
        "live": {
            "if_they_say": "At least Christians didn't have concubines.",
            "you_say": "Christian household slavery included sexual abuse in practice even when canon law frowned. Islam made concubinage a named legal category. Named vs hypocritical is a real distinction — neither is abolition.",
            "dont_overclaim": "Don't sanitize plantations. Don't sanitize harems.",
        },
    },
    "today": {
        "why_it_matters": "ISIS, kafala, and trafficking: the residual file.",
        "live": {
            "if_they_say": "Islam still has slavery.",
            "you_say": "Mainstream states abolished it. Extremists revived a reading of siyar. Christian-world trafficking exists too. The textual question is whether anyone can still cite scripture as license. That's the live danger.",
            "dont_overclaim": "Don't smear 1.8 billion people with ISIS. Don't pretend Western trafficking is 'not our religion.'",
        },
    },
}

NONBELIEVERS = {
    "no-compulsion": {
        "why_it_matters": "2:256 vs later fiqh and vs NT persuasion. Definitions of compulsion decide it.",
        "muslim": {
            "quotes": [
                Q(
                    "There is no compulsion in religion. The right course has become clear from the wrong.",
                    "Qur'an 2:256",
                    "Primary text",
                    "https://quran.com/2/256",
                ),
            ],
        },
        "christian": {
            "quotes": [
                Q(
                    "Go therefore and make disciples of all nations…",
                    "Matthew 28:19",
                    "Mission without a jizya structure (as Christian claim)",
                    "https://www.biblegateway.com/passage/?search=Matthew%2028%3A19&version=NRSVUE",
                ),
            ],
            "data_points": [
                D("Christendom's coerced conversions (Visigothic Spain, colonial missions) are the Christian counter-file.", "History"),
            ],
        },
        "live": {
            "if_they_say": "Islam is conversion by the sword.",
            "you_say": "2:256 exists. So do 9:29 and ridda laws. The adult question is how classical fiqh limited 2:256 to pre-conquest Arabs or 'don't force the heart after conquest.' Then compare baptism-or-exile episodes in Christian history.",
            "dont_overclaim": "Don't delete 2:256. Don't delete 9:29.",
        },
    },
    "jizya-dhimma": {
        "why_it_matters": "The institutional difference most non-Muslims actually feel in the classical model.",
        "muslim": {
            "quotes": [
                Q(
                    "Fight those who do not believe in Allah… from those who were given the Book, until they give the jizya willingly while they are humbled.",
                    "Qur'an 9:29",
                    "Jizya verse",
                    "https://quran.com/9/29",
                ),
            ],
            "data_points": [
                D("Pact of ʿUmar traditions (later compilation) describe dress, building, and weapons restrictions — historicity debated, social memory real.", "Tritton / Cohen on Pact of Umar"),
            ],
        },
        "christian": {
            "data_points": [
                D("Jizya as poll-tax-for-protection vs ṣaghār (humiliation) is the interpretation split; 9:29's wa-hum ṣāghirūn is the problem word.", "Exegetical crux"),
            ],
        },
        "live": {
            "if_they_say": "Dhimma was tolerant multiculturalism.",
            "you_say": "Compared with some medieval alternatives, protected People of the Book could live and worship. Compared with equal citizenship, 9:29's 'humbled' and later sumptuary rules are second-class. Both sentences can be true.",
            "dont_overclaim": "Don't call dhimma liberal democracy. Don't call it 24/7 genocide.",
        },
    },
    "love-neighbor-enemy": {
        "why_it_matters": "Christian uniqueness claim vs Islamic justice/ihsan claim.",
        "christian": {
            "quotes": [
                Q(
                    "You shall love your neighbor as yourself.",
                    "Mark 12:31",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Mark%2012%3A31&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Allah does not forbid you from those who do not fight you because of religion and do not expel you from your homes — from being righteous toward them and acting justly toward them.",
                    "Qur'an 60:8",
                    "Kindness to peaceful non-Muslims",
                    "https://quran.com/60/8",
                ),
            ],
        },
        "live": {
            "if_they_say": "Only Jesus said love your enemies.",
            "you_say": "Matthew 5:44 is distinctive. 60:8 is the Islamic near-neighbor. 60:9 and 5:51 pull the other way. Don't let one verse impersonate a whole legal system.",
            "dont_overclaim": "Don't say Muslims have no ethic of kindness to outsiders. Don't say 5:44 ran Christendom's policy.",
        },
    },
    "salvation-exclusivism": {
        "why_it_matters": "Hell for the other is a shared scandal or a shared seriousness.",
        "christian": {
            "quotes": [
                Q(
                    "I am the way, and the truth, and the life. No one comes to the Father except through me.",
                    "John 14:6",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=John%2014%3A6&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "And whoever desires other than Islam as religion — never will it be accepted from him, and he, in the Hereafter, will be among the losers.",
                    "Qur'an 3:85",
                    "Primary text",
                    "https://quran.com/3/85",
                ),
                Q(
                    "Indeed, those who believed and those who were Jews or Christians or Sabeans — those who believed in Allah and the Last Day and did righteousness — will have their reward with their Lord.",
                    "Qur'an 2:62",
                    "Inclusivist-used verse (tension with 3:85)",
                    "https://quran.com/2/62",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam sends all Christians to hell.",
            "you_say": "3:85 is exclusivist; 2:62 is the tension verse; 5:72 is aimed at deity-of-Christ. Christianity has John 14:6 and extra ecclesiam. Score honesty about hell, not who smiles more in interfaith week.",
            "dont_overclaim": "Don't hide 3:85. Don't hide extra ecclesiam / John 14:6.",
        },
    },
    "blasphemy": {
        "why_it_matters": "Modern flashpoint: cartoons, apostasy, and sacred honor.",
        "muslim": {
            "data_points": [
                D("Classical sabb al-rasūl / ridda penalties are the legal backbone of blasphemy politics.", "Fiqh; modern Pakistan 295-C as a case study"),
            ],
        },
        "christian": {
            "data_points": [
                D("Leviticus 24:16 and medieval heresy law; also modern Christian-majority blasphemy leftovers.", "Lev 24:16"),
            ],
        },
        "live": {
            "if_they_say": "Islam cannot tolerate satire; Christianity can.",
            "you_say": "Today many Christian-majority states do. Classical both did not. The question is which texts still generate death-for-insult as piety. That's a live Islamic-law fight more than a live Catholic-canon fight in 2026.",
            "dont_overclaim": "Don't forget Servetus. Don't forget that most Muslims are not a ḥadd court.",
        },
    },
    "friendship-loyalty": {
        "why_it_matters": "5:51 / 9:23 vs 'do not be unequally yoked' and church discipline.",
        "muslim": {
            "quotes": [
                Q(
                    "O you who have believed, do not take the Jews and the Christians as allies…",
                    "Qur'an 5:51",
                    "Walāya verse (translation fights: allies vs friends)",
                    "https://quran.com/5/51",
                ),
            ],
        },
        "live": {
            "if_they_say": "Muslims are forbidden to be friends with us.",
            "you_say": "Awliyāʾ is the word; 'allies in a war-context' vs 'friends' is the tafsīr fight. 60:8 is the counter-verse. Then put 2 Cor 6:14 beside it. Don't let one English gloss end the round.",
            "dont_overclaim": "Don't say 5:51 is only about a schoolyard friendship. Don't say it mandates hatred of all Christians.",
        },
    },
    "polytheists-atheists": {
        "why_it_matters": "People of the Book get a box; others often don't.",
        "live": {
            "if_they_say": "Islam only has a problem with pagans, not with us.",
            "you_say": "9:5's mushrikūn and 9:29's People of the Book are different files. Atheists are usually assimilated to unbelief without a dhimma kit. Christianity historically had its own 'no salvation outside' for pagans. Specify the out-group.",
            "dont_overclaim": "Don't collapse 9:5 and 9:29. Don't pretend medieval baptism of Lithuania was a seminar.",
        },
    },
    "people-of-book-honor": {
        "why_it_matters": "5:82 vs 5:51; nearest in affection vs not taking allies.",
        "muslim": {
            "quotes": [
                Q(
                    "…and you will find the nearest of them in affection to the believers those who say, 'We are Christians.'",
                    "Qur'an 5:82",
                    "Affection verse",
                    "https://quran.com/5/82",
                ),
            ],
        },
        "live": {
            "if_they_say": "The Qur'an honors Christians uniquely.",
            "you_say": "5:82 is real. So is 5:14, 5:72, and 9:30. Honor plus polemic is the pattern. Don't quote only the compliment verse.",
            "dont_overclaim": "Don't erase 5:82. Don't make it a blank check for Nicene doctrine.",
        },
    },
    "missionary-ethics": {
        "why_it_matters": "Power plus preaching. Colonial missions vs daʿwa-and-conquest.",
        "live": {
            "if_they_say": "Christian missions are imperialism.",
            "you_say": "Sometimes they were. Daʿwa sometimes rode futūḥ. Score coercion, education, and whether conversion is reversible without death. That's the liberty test.",
            "dont_overclaim": "Don't make every clinic a plot. Don't make every mosque a garrison.",
        },
    },
    "modern-pluralism": {
        "why_it_matters": "Who can actually live the other's minority life today.",
        "christian": {
            "data_points": [
                D("Dignitatis Humanae (Vatican II) is the Catholic landmark shift toward religious liberty as a right.", "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_decl_19651207_dignitatis-humanae_en.html"),
            ],
        },
        "live": {
            "if_they_say": "You can build a church in our country; we can't build a mosque in yours.",
            "you_say": "That's an empirical claim — test it by country, not by religion-name. Gulf vs Western Europe vs rural Pakistan vs rural Alabama are four files. Then ask which theology still forbids the church or the mosque.",
            "dont_overclaim": "Don't pick the worst village as the whole religion. Don't pick Dubai as the whole fiqh.",
        },
    },
}

MORALITY = {
    "golden-rule": {
        "why_it_matters": "Shared moral core. Difference is often scope (enemy vs in-group) and enforcement.",
        "christian": {
            "quotes": [
                Q(
                    "In everything do to others as you would have them do to you; for this is the law and the prophets.",
                    "Matthew 7:12",
                    "Golden Rule",
                    "https://www.biblegateway.com/passage/?search=Matthew%207%3A12&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "None of you [truly] believes until he loves for his brother what he loves for himself.",
                    "Hadith (Bukhari 13 / Muslim 45)",
                    "An-Nawawi's 40 hadith #13 tradition",
                    "https://sunnah.com/bukhari:13",
                ),
            ],
            "data_points": [
                D("Debate: does 'brother' mean fellow Muslim or any human? That scope fight is the round.", "Commentarial split"),
            ],
        },
        "live": {
            "if_they_say": "Only Jesus taught the Golden Rule.",
            "you_say": "The form is in Hillel, in Matthew 7, and in the īmān hadith. Fight scope (enemy, stranger, co-religionist) and whether law later narrows it.",
            "dont_overclaim": "Don't claim unique copyright on reciprocity. Don't claim the hadith obviously includes enemies.",
        },
    },
    "grace-vs-deeds": {
        "why_it_matters": "The salvation-moral psychology fight.",
        "christian": {
            "quotes": [
                Q(
                    "For by grace you have been saved through faith, and this is not your own doing; it is the gift of God — not the result of works, so that no one may boast.",
                    "Ephesians 2:8–9",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Ephesians%202%3A8-9&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "Then whoever does an atom's weight of good will see it, and whoever does an atom's weight of evil will see it.",
                    "Qur'an 99:7–8",
                    "Deeds matter",
                    "https://quran.com/99",
                ),
                Q(
                    "Say, 'O My servants who have transgressed against themselves [by sinning], do not despair of the mercy of Allah. Indeed, Allah forgives all sins.'",
                    "Qur'an 39:53",
                    "Mercy without Calvary (Islamic reading)",
                    "https://quran.com/39/53",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam is works-righteousness; Christianity is grace.",
            "you_say": "Eph 2 is grace. James 2 is deeds. 99:7–8 is deeds. 39:53 is mercy. Both have grace-and-demand. The distinctive Christian claim is that grace is purchased at the cross; the distinctive Islamic claim is that it is not.",
            "dont_overclaim": "Don't turn Muslims into Pelagians. Don't turn Christians into antinomians.",
        },
    },
    "original-sin": {
        "why_it_matters": "Anthropology fork: inherited guilt vs fitrah.",
        "christian": {
            "quotes": [
                Q(
                    "Therefore, just as sin came into the world through one man, and death came through sin, and so death spread to all because all have sinned…",
                    "Romans 5:12",
                    "Pauline Adam",
                    "https://www.biblegateway.com/passage/?search=Romans%205%3A12&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "So it is no sin on you… And no bearer of burdens will bear the burden of another.",
                    "Qur'an 53:38 (with 6:164)",
                    "Anti-inherited-guilt prooftexts",
                    "https://quran.com/53/38",
                ),
            ],
            "data_points": [
                D("Fitrah hadith: every child is born on fitrah; parents judaize/christianize/magianize.", "Bukhari 1358", "https://sunnah.com/bukhari:1358"),
            ],
        },
        "live": {
            "if_they_say": "Islam denies sin, so it is naïve.",
            "you_say": "Islam denies inherited guilt, not sin. 99:8 and the whole tawba system assume real evil. The fight is Adam's leak into babies, not whether people do wrong.",
            "dont_overclaim": "Don't say Muslims think humans are angels. Don't say every Christian holds Augustinian mass damnation of infants.",
        },
    },
    "divine-command": {
        "why_it_matters": "Euthyphro: is the good God's will or God's nature? Both get hit.",
        "live": {
            "if_they_say": "Your God could command evil and it would be good.",
            "you_say": "That's Euthyphro for both. Ashʿarī voluntarism is the Islamic version critics name; DCT is the Christian version. Alternatives: Māturīdī/Muʿtazilī ʿadl; Thomist eternal law. Don't pretend only the other side has a raw-will God.",
            "dont_overclaim": "Don't hang all of Islam on the most voluntarist kalam. Don't hang all of Christianity on the most voluntarist Protestant.",
        },
    },
    "prophet-example": {
        "why_it_matters": "Jesus vs Muhammad as moral exemplar — the personal file that audiences remember.",
        "christian": {
            "data_points": [
                D("Christian critique cluster: marriages (Zaynab, Aisha age debates), Banū Qurayza, enemies killed.", "Sīra/hadith file — handle with primary citations, not memes"),
            ],
        },
        "muslim": {
            "data_points": [
                D("Muslim critique cluster: temple incident, 'I came not to bring peace but a sword' (Matt 10:34), later church violence in Jesus' name.", "Matt 10:34"),
                D("Q 33:21: Muhammad as uswa ḥasana — the Islamic claim that his life is the pattern.", "https://quran.com/33/21"),
            ],
        },
        "live": {
            "if_they_say": "Muhammad's life is immoral; Jesus' is perfect.",
            "you_say": "Split offices: itinerant preacher vs statesman. Then take one concrete file (e.g. treatment of enemies, marriage, wealth) with primary texts. Don't debate a cartoon vs a stained-glass window.",
            "dont_overclaim": "Don't use unsourced Aisha-age slogans as if the isnād debate didn't exist. Don't pretend Matthew 10:34 is a pacifist fridge magnet.",
        },
    },
    "justice-mercy": {
        "why_it_matters": "Both claim the balance; they locate it differently (cross vs sharīʿa ḥudūd + tawba).",
        "muslim": {
            "quotes": [
                Q(
                    "Indeed, Allah commands justice and good conduct and giving to relatives and forbids immorality and bad conduct and oppression.",
                    "Qur'an 16:90",
                    "Often called the most comprehensive ethics verse",
                    "https://quran.com/16/90",
                ),
            ],
        },
        "christian": {
            "quotes": [
                Q(
                    "He has told you, O mortal, what is good; and what does the Lord require of you but to do justice, and to love kindness, and to walk humbly with your God?",
                    "Micah 6:8",
                    "OT ethics summary Christians still claim",
                    "https://www.biblegateway.com/passage/?search=Micah%206%3A8&version=NRSVUE",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam is justice without mercy; Christianity is mercy without justice.",
            "you_say": "16:90 commands both. The cross claims both. Ḥudūd and hell doctrines are where each is accused of excess. Pick a concrete penalty, not a vibe.",
            "dont_overclaim": "Don't erase rahma. Don't erase judgment in the NT.",
        },
    },
    "truthfulness": {
        "why_it_matters": "Taqiyya polemic vs NT 'let your yes be yes.'",
        "christian": {
            "quotes": [
                Q(
                    "Let your word be 'Yes, Yes' or 'No, No'; anything more than this comes from the evil one.",
                    "Matthew 5:37",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Matthew%205%3A37&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "data_points": [
                D("Taqiyya in classical usage is primarily a Shīʿī survival doctrine under persecution, not a Sunni license to lie in daʿwa.", "Standard academic correction"),
                D("Q 16:106: exception under compulsion. Q 2:225 / oaths. Lying is generally ḥarām.", "https://quran.com/16/106"),
            ],
        },
        "live": {
            "if_they_say": "Muslims are allowed to lie to infidels (taqiyya).",
            "you_say": "That's usually a category error: taqiyya ≠ 'Islam means lying.' Ask for a Sunni usūl text that licenses daʿwa fraud. Then admit war-ruses exist in every tradition, including Joshua's spies.",
            "dont_overclaim": "Don't say no Muslim ever lied in religion's name. Don't say taqiyya is the fifth pillar.",
        },
    },
    "sexual-ethics": {
        "why_it_matters": "Modern audience test; overlaps women/slavery.",
        "live": {
            "if_they_say": "Islam is sexually regressive; Christianity is not.",
            "you_say": "Both restrict zina/fornication. Distinctive files: polygyny, concubinage, divorce, and LGBT. Distinctive Christian files: later church discipline and contemporary schism. Be specific or you're doing culture war, not ethics.",
            "dont_overclaim": "Don't pretend all churches match 2026 campus norms. Don't pretend all fiqh matches Taliban policy.",
        },
    },
    "forgiveness-practice": {
        "why_it_matters": "Seventy times seven vs qiṣāṣ and pardon (2:178).",
        "christian": {
            "quotes": [
                Q(
                    "Then Peter came and said to him, 'Lord, if another member of the church sins against me, how often should I forgive? As many as seven times?' Jesus said to him, 'Not seven times, but, I tell you, seventy-seven times.'",
                    "Matthew 18:21–22",
                    "NT primary",
                    "https://www.biblegateway.com/passage/?search=Matthew%2018%3A21-22&version=NRSVUE",
                ),
            ],
        },
        "muslim": {
            "quotes": [
                Q(
                    "But whoever pardons and makes reconciliation — his reward is [due] from Allah.",
                    "Qur'an 42:40",
                    "Pardon preferred",
                    "https://quran.com/42/40",
                ),
            ],
        },
        "live": {
            "if_they_say": "Islam is revenge religion; Christianity is forgiveness.",
            "you_say": "Matthew 18 is radical. 42:40 and 2:178's pardon option are also real. Then look at qiṣāṣ and at Christian history's vendettas. Ideal vs institution.",
            "dont_overclaim": "Don't turn qiṣāṣ into bloodlust. Don't turn 'forgive' into 'no criminal law.'",
        },
    },
    "universalizability": {
        "why_it_matters": "Kantian test both fail if in-group ethics is the real operating system.",
        "live": {
            "if_they_say": "My ethic is universal; yours is tribal.",
            "you_say": "Test it: would you accept this rule if you were born in the other umma/church? Then inspect war, apostasy, and salvation of the outsider. That's Kant plus scripture, not a vibe.",
            "dont_overclaim": "Don't call every boundary 'tribal.' Don't call every mission 'universal love.'",
        },
    },
    "hypocrisy-test": {
        "why_it_matters": "Audiences punish hypocrisy more than they reward metaphysics.",
        "live": {
            "if_they_say": "Look at how your people actually live.",
            "you_say": "Granted: practice is evidence. Then sample fairly — not the worst atrocity vs the best saint. And ask which texts still authorize the worst. Hypocrisy can indict a community without settling which book is true.",
            "dont_overclaim": "Don't do atrocity ping-pong as if body count were tafsīr.",
        },
    },
    "summum-bonum": {
        "why_it_matters": "What is the highest good — beatific love or worshipful obedience — shapes every other moral argument.",
        "live": {
            "if_they_say": "The highest good is obvious.",
            "you_say": "Name it in one sentence: union with God, the vision of God, ʿubūdiyyah, the pleasure of Allah, human flourishing. Then ask whether that good requires the cross, the sharīʿa, both, or neither. This is the last fork, not the first slogan.",
            "dont_overclaim": "Don't pretend the other side has no love of God. Don't pretend your side has no law.",
        },
    },
    "qureshi-style-salvation": {
        "live": {
            "if_they_say": "Nabeel Qureshi settled the salvation contrast.",
            "you_say": "Use his contrast as a map of felt difference (assurance vs scales), then go back to Eph 2, James 2, 39:53, and 99:7–8. Memoir is not a systematic theology.",
            "dont_overclaim": "Don't psychologize 1.8 billion people from one convert's story. Don't dismiss convert testimony as fake.",
        },
    },
}
