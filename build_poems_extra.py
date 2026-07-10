# -*- coding: utf-8 -*-
# إضافة خمس قصائد للموسوعة (sec_poems): بانت سعاد، بردة البوصيري، نهج البردة، واحر قلباه، حتام نحن.
# يُلحقها بـ public/seed/enc/poems.json بنفس قواعد تنظيف build_poems.py.
import json, re, os

def clean(s):
    s = s.replace("\u0640", "")
    s = re.sub(r"[\u064B-\u0652\u0670]", "", s)
    s = s.replace("؟", "").replace("!", "").replace("?", "")
    s = s.replace("«", "").replace("»", "").replace("\u201c", "").replace("\u201d", "")
    s = s.replace("(", "").replace(")", "")
    s = s.replace("\u2019", "'")
    return s

def verses(block):
    return clean("\n".join(l.strip() for l in block.strip("\n").split("\n") if l.strip()))

def readf(name):
    return open(f"/tmp/poems/{name}", encoding="utf-8").read()

def first_hemistich(block):
    line = [l for l in block.strip("\n").split("\n") if l.strip()][0]
    return clean(line.split(" .. ")[0].strip())

def poem(poet, ar_block, en_block, title_en, meter_ar, meter_en, rawi_ar, rawi_en,
         purpose_ar, purpose_en, year, sharh, era, nat, timeline,
         tags="sub_pt_fasih, sub_st_qafiya",
         poemtype_ar="فصيح", poemtype_en="Classical",
         structure_ar="قافية", structure_en="Single rhyme",
         form_ar="عمودية", form_en="Classical ode"):
    return {
        "section": "sec_poems", "subclass": era, "subclass2": nat,
        "timeline": timeline, "year": str(year), "tags": tags,
        "titles": {"ar": first_hemistich(ar_block), "en": clean(title_en)},
        "texts": {"ar": verses(ar_block), "en": verses(en_block)},
        "source": f"{poet['poet_ar']} — {poet['poet_en']}",
        "explain": "", "refs": "",
        "poem": {
            "poet_key": poet["poet_key"], "poet_ar": poet["poet_ar"], "poet_en": poet["poet_en"],
            "gender": poet["gender"], "period": poet["period"], "period_en": poet["period_en"],
            "homeland_ar": poet["homeland_ar"], "homeland_en": poet["homeland_en"],
            "laqab_ar": poet["laqab_ar"], "laqab_en": poet["laqab_en"],
            "bio_ar": clean(poet["bio_ar"]), "bio_en": poet["bio_en"],
            "poemtype_ar": poemtype_ar, "poemtype_en": poemtype_en,
            "structure_ar": structure_ar, "structure_en": structure_en,
            "meter_ar": clean(meter_ar), "meter_en": meter_en,
            "rawi_ar": clean(rawi_ar), "rawi_en": rawi_en,
            "form_ar": form_ar, "form_en": form_en,
            "purpose_ar": purpose_ar, "purpose_en": purpose_en,
            "sharh": [{"t_ar": clean(s.get("t_ar", "")), "b_ar": clean(s.get("b_ar", "")),
                       "t_en": s.get("t_en", ""), "b_en": s.get("b_en", "")} for s in sharh],
        },
    }

# ── الشعراء ──
KAAB = dict(poet_key="kaab_bin_zuhayr", poet_ar="كعب بن زهير", poet_en="Ka'b ibn Zuhayr",
    gender="male", period="صدر الإسلام", period_en="Early Islamic era",
    homeland_ar="جزيرة العرب", homeland_en="Arabian Peninsula",
    laqab_ar="صاحب البردة", laqab_en="Author of the original Al-Burda",
    bio_ar="شاعر مخضرم أدرك عصري الجاهلية و صدر الإسلام. اشتهر في الجاهلية، و لما ظهر الإسلام هجا النبي محمد فأهدر دمه، فجاءه كعب مستأمنا و قد أسلم و أنشده لاميته المشهورة التي مطلعها: بانت سعاد فقلبي اليوم متبول، فعفا عنه النبي و خلع عليه بردته. و من حكمته في القصيدة: من هاب أسباب المنايا ينلنه .. و إن يرق أسباب السماء بسلم — و من يك ذا فضل فيبخل بفضله .. على قومه يستغن عنه و يذمم.",
    bio_en="Ka'b ibn Zuhayr was an Arabian poet of the 7th century and a contemporary of the Prophet Muhammad. He wrote Banat Su'ad, a qasida in praise of the Prophet, considered the first na'at in Arabic and the original Al-Burda, which he recited before Muhammad after embracing Islam.")

BUSIRI = dict(poet_key="al_busiri", poet_ar="البوصيري", poet_en="Al-Busiri",
    gender="male", period="العصور المظلمة", period_en="Mamluk era",
    homeland_ar="مصر", homeland_en="Egypt",
    laqab_ar="صاحب البردة", laqab_en="Author of the Mantle Ode",
    bio_ar="محمد الصنهاجي البوصيري، شاعر صنهاجي صوفي شاذلي اشتهر بمدائحه النبوية. أشهر أعماله البردة المسماة الكواكب الدرية في مدح خير البرية، و هي من أشهر القصائد الإسلامية في بابها، و له كذلك الهمزية.",
    bio_en="Al-Busiri was a Sanhaji Sufi Sunni poet of the Shadhili order and a disciple of Abu al-Abbas al-Mursi. His magnum opus, the Qasida al-Burda (Poem of the Mantle) in praise of the Prophet Muhammad, is one of the most popular Islamic poems of its genre, written in Arabic, as is his other ode Al-Hamziyya.")

SHAWQI = dict(poet_key="ahmad_shawqi", poet_ar="أحمد شوقي", poet_en="Ahmed Shawqi",
    gender="male", period="العصر الحديث", period_en="Modern era",
    homeland_ar="مصر", homeland_en="Egypt",
    laqab_ar="أمير الشعراء", laqab_en="Prince of Poets",
    bio_ar="أحمد شوقي بن علي أحمد شوقي، شاعر و كاتب مسرحي مصري، يعد من أشهر شعراء العربية في العصر الحديث، لقب بأمير الشعراء. من روائعه نهج البردة معارضا بها بردة البوصيري.",
    bio_en="Ahmed Shawqi, nicknamed the Prince of Poets, was an Egyptian poet laureate, linguist, and one of the most famous Arabic literary writers of the modern era in the Arab world. His Nahj al-Burda echoes Al-Busiri's Burda.")

MUTANABBI = dict(poet_key="al_mutanabbi", poet_ar="أبو الطيب المتنبي", poet_en="Al-Mutanabbi",
    gender="male", period="العصر العباسي", period_en="Abbasid era",
    homeland_ar="الكوفة، العراق", homeland_en="Kufa, Iraq",
    laqab_ar="شاعر العرب - مالئ الدنيا و شاغل الناس", laqab_en="Poet of the Arabs",
    bio_ar="أبو الطيب أحمد بن الحسين الجعفي الكندي، شاعر مجيد لقب بشاعر العرب و مالئ الدنيا و شاغل الناس، له مكانة سامية لم تتح لغيره من شعراء العرب بعد الإسلام. شاعر حكيم و أحد مفاخر الأدب العربي، تدور معظم قصائده حول نفسه و مدح الملوك. ظهرت موهبته مبكرا فقال الشعر صبيا و نظم أول أشعاره و عمره تسع سنوات. كان ذا كبرياء و شجاعة و طموح و محبا للمغامرات، يعتز بعروبته و يفخر بنفسه، و أفضل شعره في الحكمة و فلسفة الحياة و وصف المعارك. عاش أفضل أيامه و أكثرها عطاء في بلاط سيف الدولة الحمداني في حلب.",
    bio_en="Abu al-Tayyib Ahmad ibn al-Husayn al-Mutanabbi al-Kindi, known as al-Mutanabbi, was an Abbasid-era Arab poet at the court of the Hamdanid emir Sayf al-Dawla in Aleppo, for whom he composed 300 folios of poetry. Regarded among the greatest poets of the Arabic language, he is renowned for his wisdom, self-pride, and vivid battle descriptions; he spent his most productive years in Aleppo.")

# ── الشروح ──
SHARH_KAAB = [{
    "t_ar": "البردة", "t_en": "Al-Burda (The Mantle)",
    "b_ar": "تعرف هذه القصيدة باسم البردة، و هي من عيون الشعر العربي و من أشهر قصائد المدح النبوي. نظمها كعب بعد أن أهدر دمه فجاء المدينة مستخفيا و أعلن إسلامه بين يدي الرسول و أنشدها يستعطفه و يعتذر إليه. تبدأ على عادة العرب بالمقدمة الغزلية و وصف الرحيل و الناقة، ثم تنتقل إلى الخوف من وعيد الرسول و وشاية الأعداء، لتنتهي بالاعتذار و المدح الخالد للرسول و المهاجرين من قريش. و قد أعجب بها النبي فخلع عليه بردته تكريما له.",
    "b_en": "Famously known as Al-Burda (The Mantle), this is one of the masterpieces of classical Arabic poetry and of prophetic praise. Ka'b composed it after his execution was ordered; he entered Medina in secret, embraced Islam before the Prophet, and recited it to seek pardon. It opens with the customary amatory prelude and a description of the journey and the she-camel, moves to his fear of the Prophet's warning and his enemies' slander, and culminates in an immortal eulogy of the Prophet and the Emigrants of Quraysh. Moved, the Prophet draped his own mantle over Ka'b as a sign of forgiveness."
}]
SHARH_MUT1 = [{
    "t_ar": "واحر قلباه", "t_en": "Wa Harra Qalbah",
    "b_ar": "تعد هذه القصيدة، المعروفة باسم واحر قلباه، واحدة من روائع الشعر العربي و من أشهر قصائد المتنبي في عتاب سيف الدولة الحمداني أمير حلب. نظمها عام 347 هجرية بعد أن نجح حساده في إفساد علاقته بالأمير. تتميز بمزيج فريد من العتاب الصادق و الفخر الذاتي و الحكمة البليغة؛ يعبر فيها عن ألمه من جفاء سيف الدولة، و في الوقت ذاته يعيد تأكيد مكانته كشاعر لا يتكرر و خير من تمشي به قدم.",
    "b_en": "Known as Wa Harra Qalbah (How Burning is My Heart), this is one of the masterpieces of Arabic literature. Al-Mutanabbi composed it in 958 CE as a poignant reproach to his patron and friend Sayf al-Dawla, ruler of Aleppo, after court rivals sowed discord between them. It blends sincere admonition, unmatched self-pride, and profound wisdom, voicing his sorrow over the prince's coldness while reaffirming his standing as a peerless poet and a man of unmatched honor."
}]
SHARH_MUT2 = [{
    "t_ar": "مأساة المتنبي في مصر", "t_en": "Al-Mutanabbi's Egyptian Tragedy",
    "b_ar": "تعرف هذه القصيدة بمأساة المتنبي في مصر أو مرثية فاتك الكبير. نظمها بعد خروجه غاضبا فارا من مصر و هجائه كافورا الإخشيدي. يستهل بمناجاة الليل و الشكوى من عناء السفر، ثم ينتقل إلى مدح و رثاء صديقه المخلص فاتك الكبير أبي شجاع الذي توفي في مصر، معبرا عن صدمته بفقده و ضياع آماله هناك. تحمل روحا فلسفية عميقة تذم قلة إنصاف الناس و تعلي من شأن السيف على القلم، و تنتهي بأبيات شهيرة تلخص نظرته المتشائمة للزمن.",
    "b_en": "Known as Al-Mutanabbi's Egyptian Tragedy or the Elegy of Fatik al-Kabir, composed after he fled Egypt following his bitter falling-out with its ruler Kafur al-Ikhshidi. It opens with a lamentation on the night and the grueling journey, then turns to a moving elegy for his loyal friend Abu Shuja' Fatik, whose death shattered the poet's hopes. It carries a deeply philosophical spirit critiquing human unfairness, exalts the sword over the pen, and ends with legendary verses on the cruelty of Time."
}]

entries = [
    poem(KAAB, readf("kaab_ar.txt"), readf("kaab_en.txt"),
         "Su'ad has departed, so my heart today is lovesick",
         "البسيط", "Al-Basit", "لامية ل", "Lam (ل)", "عامة", "General",
         630, SHARH_KAAB, "sub_era_sadr", "sub_nat_jazira", "tl_poem_sadr"),
    poem(BUSIRI, readf("busiri_ar.txt"), readf("busiri_en.txt"),
         "Is it from remembering the neighbors at Dhu Salam",
         "البسيط", "Al-Basit", "الميم م", "Mim (م)", "مدح", "Praise",
         1292, [], "sub_era_dark", "sub_nat_misr_yaman_sudan", "tl_poem_dark"),
    poem(SHAWQI, readf("shawqi_ar.txt"), readf("shawqi_en.txt"),
         "A gazelle on the lowlands between the willow and the landmark",
         "البسيط", "Al-Basit", "الميم م", "Mim (م)", "مدح", "Praise",
         1909, [], "sub_era_hadith", "sub_nat_misr_yaman_sudan", "tl_poem_hadith"),
    poem(MUTANABBI, readf("mut1_ar.txt"), readf("mut1_en.txt"),
         "How burning is my heart for him whose heart is cold",
         "البسيط", "Al-Basit", "الميم م", "Mim (م)", "عتاب", "Reproach",
         958, SHARH_MUT1, "sub_era_abbasi", "sub_nat_iraq_sham", "tl_poem_abbasi"),
    poem(MUTANABBI, readf("mut2_ar.txt"), readf("mut2_en.txt"),
         "Until when shall we travel by night with the stars in the darkness",
         "البسيط", "Al-Basit", "الميم م", "Mim (م)", "عامة", "General",
         961, SHARH_MUT2, "sub_era_abbasi", "sub_nat_misr_yaman_sudan", "tl_poem_abbasi"),
]

path = "public/seed/enc/poems.json"
data = json.load(open(path, encoding="utf-8"))
before = len(data)
# تفادي التكرار: احذف أي مدخل سابق بنفس مطلع العنوان
titles_new = {e["titles"]["ar"] for e in entries}
data = [d for d in data if d.get("titles", {}).get("ar") not in titles_new]
data.extend(entries)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"poems.json: {before} -> {len(data)} (+{len(entries)} added)")
for e in entries:
    print("  +", e["titles"]["ar"], "|", e["subclass"], e["subclass2"], "| ar verses:",
          e["texts"]["ar"].count("\n")+1, "| en verses:", e["texts"]["en"].count("\n")+1)
