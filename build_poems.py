# -*- coding: utf-8 -*-
"""يبني public/seed/enc/poems.json من جديد: عصر الجاهلي — امرؤ القيس (5) + عفيرة بنت عباد (1)."""
import json, re

def clean(s):
    s = s.replace("\u0640", "")                       # تطويل
    s = re.sub(r"[\u064B-\u0652\u0670]", "", s)        # تشكيل
    s = s.replace("؟", "").replace("!", "").replace("?", "")
    s = s.replace("«", "").replace("»", "").replace("\u201c", "").replace("\u201d", "")
    s = s.replace("(", "").replace(")", "")
    s = s.replace("\u2019", "'")
    return s

def verses(block):
    return clean("\n".join(l.strip() for l in block.strip("\n").split("\n") if l.strip()))

IMRU = dict(poet_key="imru_alqais", poet_ar="امرؤ القيس", poet_en="Imru' al-Qais",
            gender="male", period="أواخر العصر الجاهلي", period_en="Late pre-Islamic era",
            homeland_ar="نجد، جزيرة العرب", homeland_en="Najd, Arabian Peninsula",
            laqab_ar="الملك الضليل", laqab_en="The Wandering King",
            bio_ar="امرؤ القيس بن حجر الكندي، من ملوك كندة و أشهر شعراء الجاهلية، يعد رائد القصيدة العربية و صاحب أشهر المعلقات. شرد بعد مقتل أبيه يطلب الثأر و استرداد ملكه حتى مات في طريق عودته من بلاد الروم.",
            bio_en="Imru' al-Qais ibn Hujr al-Kindi, a prince of Kinda and the most celebrated poet of pre-Islamic Arabia, author of the most famous Mu'allaqah. After his father's killing he wandered seeking vengeance and his lost kingdom, dying on his way back from Byzantium.")

AFIRA = dict(poet_key="afira_bint_abbad", poet_ar="عفيرة بنت عباد", poet_en="Afira Bint Abbad",
             gender="female", period="العصر الجاهلي", period_en="Pre-Islamic era",
             homeland_ar="جزيرة العرب", homeland_en="Arabian Peninsula",
             laqab_ar="الشموس - عفار", laqab_en="Al-Shumus - Affar",
             bio_ar="شاعرة جاهلية من جديس، اشتهرت بأبياتها التحريضية حين دنس حاكم طسم عرض عروس قومها ليلة زفافها، فحرضت قومها على الثأر و كسر حال الذل، حتى صارت أبياتها من عيون شعر الحماسة و نموذجا لقيادة المرأة للرأي العام في الجاهلية.",
             bio_en="A pre-Islamic poetess of Jadis, famed for her inciting verses after a Tasm ruler violated a bride of her people on her wedding night. She goaded her tribe to vengeance against humiliation, and her lines became a model of war-poetry and of a woman steering tribal will.")

def poem(poet, title_ar, title_en, ar, en, meter_ar, meter_en, rawi_ar, rawi_en,
         purpose_ar, purpose_en, year, sharh,
         era="sub_era_jahili", nat="sub_nat_jazira", timeline="tl_poem_jahili",
         tags="sub_pt_fasih, sub_st_qafiya",
         poemtype_ar="فصيح", poemtype_en="Classical",
         structure_ar="قافية", structure_en="Single rhyme",
         form_ar="عمودية", form_en="Classical ode"):
    return {
        "section": "sec_poems", "subclass": era, "subclass2": nat,
        "timeline": timeline, "year": str(year),
        "tags": tags,
        "titles": {"ar": clean(title_ar), "en": clean(title_en)},
        "texts": {"ar": verses(ar), "en": verses(en)},
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

entries = []

# ── عفيرة بنت عباد — لا أحد أذل من جديس (قصيدة واحدة) ──
afira_ar = """
لا أحد أذل من جديس .. أهكذا يفعل بالعروس
يرضى بذا يا قوم بعل حر .. أهدى و قد أعطى و سيق المهر
أيجمل ما يؤتى إلى فتياتكم .. و أنتم رجال فيكم عدد النمل
و تصبح عفيرا في الدماء غريقة .. جهارا و زفت في النساء إلى بعل
و لو أننا كنا رجالا و كنتم .. نساء لكنا لا نقر بذا الفعل
فموتوا كراما أو أميتوا عدوكم .. و دبوا لنار الحرب بالحطب الجزل
و إلا فخلوا بطنها و تحملوا .. إلى بلد قفر و موتوا من الهزل
فللبين خير من تماد على أذى .. و للموت خير من مقام على الذل
و إن أنتم لم تغضبوا بعد هذه .. فكونوا نساء لا يعبن من الكحل
و دونكم طيب العروس فإنما .. خلقتم لأثواب العروس و للنسل
فبعدا و سخفا للذي ليس دافعا .. و يختال يمشي بيننا مشية الفحل
"""
afira_en = """
No one is more humiliated than Jadis .. is this how one acts with a bride
Does a free husband accept this, O people .. while he has sent gifts and paid the dowry
Is it fitting what is done to your young women .. while you are men, in number like ants
And Afira becomes drowned in blood .. openly, and she was led among women to a husband
And if we had been men and you had been .. women, we would not have accepted this deed
So die with honor or kill your enemy .. and stir the fire of war with thick firewood
Otherwise vacate its belly and depart .. to a barren land and die of weakness
For departure is better than persisting in harm .. and death is better than staying in humiliation
And if you do not feel anger after this .. then be women, not blamed for using kohl
And take the bride's perfume, for you were only .. created for the bride's garments and for offspring
So distance and shame to him who does not defend .. while he walks among us with the gait of a stallion
"""
afira_sharh = [{
 "t_ar":"الشرح و الإشارات",
 "b_ar":"تجسد هذه الأبيات قمة التحدي و التحريض في الشعر الجاهلي، حيث تندد الشاعرة عفيرة بموقف قومها من جديس الذين قبلوا الهوان بعد أن دنس حاكم طسم عرض عروستهم ليلة زفافها. تستعمل لغة قاسية مباشرة تمزق حجاب الصمت، فتقارن عجز الرجال عن الثأر بشجاعة النساء لو كن مكانهم، حتى تبلغ السخرية بدعوتهم لارتداء الحلي و الكحل ما داموا رضوا بالذل، و تضعهم بين خيارين لا ثالث لهما: الثأر أو الفناء.",
 "t_en":"Explanation and Indications",
 "b_en":"These lines embody the peak of challenge and incitement in pre-Islamic verse. Afira condemns her people of Jadis for accepting disgrace after a Tasm ruler violated their bride on her wedding night. With stark, direct language she contrasts the men's failure to avenge with the courage women would have shown, mocking them to wear jewelry and kohl since they accepted humiliation, and setting them between two choices only: vengeance or annihilation."
}]
entries.append(poem(AFIRA,
  "لا أحد أذل من جديس ..", "No one is more humiliated than Jadis ..",
  afira_ar, afira_en, "الطويل — و رجز في المطلع", "Al-Tawil (rajaz opening)",
  "اللام (ل)", "Lam (ل)", "ثأر و نخوة و حماسة", "Vengeance, honor and zeal", 524, afira_sharh))

# ── امرؤ القيس — المعلقة: قفا نبك ──
mu_ar = """
قفا نبك من ذكرى حبيب ومنزل .. بسقط اللوى بين الدخول فحومل
فتوضح فالمقراة لم يعف رسمها .. لما نسجتها من جنوب وشمأل
ترى بعر الأرآم في عرصاتها .. و قيعانها كأنه حب فلفل
كأني غداة البين يوم تحملوا .. لدى سمرات الحي ناقف حنظل
وقوفا بها صحبي علي مطيهم .. يقولون لا تهلك أسى وتجمل
و إن شفائي عبرة مهراقة .. فهل عند رسم دارس من معول
كدأبك من أم الحويرث قبلها .. وجارتها أم الرباب بمأسل
إذا قامتا تضوع المسك منهما .. نسيم الصبا جاءت بريا القرنفل
ففاضت دموع العين مني صبابة .. على النحر حتى بل دمعي محملي
ألا رب يوم لك منهن صالح .. و لا سيما يوم بدارة جلجل
و يوم عقرت للعذارى مطيتي .. فيا عجبا من كورها المتحمل
فظل العذارى يرتمين بلحمها .. و شحم كهداب الدمقس المفتل
ويوم دخلت الخدر خدر عنيزة .. فقالت لك الويلات إنك مرجلي
تقول وقد مال الغبيط بنا معا .. عقرت بعيري يا امرأ القيس فانزل
فقلت لها سيري وأرخي زمامه .. و لا تبعديني من جناك المعلل
فمثلك حبلى قد طرقت ومرضع .. فألهيتها عن ذي تمائم محول
إذا ما بكى من خلفها انصرفت له .. بشق وتحتي شقها لم يحول
ويوما على ظهر الكثيب تعذرت .. علي وآلت حلفة لم تحلل
أفاطم مهلا بعض هذا التدلل .. و إن كنت قد أزمعت صرمي فأجملي
و إن تك قد ساءتك مني خليقة .. فسلي ثيابي من ثيابك تنسل
أغرك مني أن حبك قاتلي .. و أنك مهما تأمري القلب يفعل
و ما ذرفت عيناك إلا لتضربي .. بسهميك في أعشار قلب مقتل
وبيضة خدر لا يرام خباؤها .. تمتعت من لهو بها غير معجل
تجاوزت أحراسا إليها ومعشرا .. علي حراصا لو يسرون مقتلي
إذا ما الثريا في السماء تعرضت .. تعرض أثناء الوشاح المفصل
فجئت وقد نضت لنوم ثيابها .. لدى الستر إلا لبسة المتفضل
فقالت يمين الله ما لك حيلة .. و ما إن أرى عنك الغواية تنجلي
خرجت بها تمشي تجر وراءنا .. على أثرينا ذيل مرط مرحل
فلما أجزنا ساحة الحي وانتحى .. بنا بطن خبت ذي حقاف عقنقل
هصرت بفودي رأسها فتمايلت .. علي هضيم الكشح ريا المخلخل
إذا التفتت نحوي تضوع ريحها .. نسيم الصبا جاءت بريا القرنفل
مهفهفة بيضاء غير مفاضة .. ترائبها مصقولة كالسجنجل
كبكر المقاناة البياض بصفرة .. غذاها نمير الماء غير محلل
تصد وتبدي عن أسيل وتتقي .. بناظرة من وحش وجرة مطفل
وجيد كجيد الريم ليس بفاحش .. إذا هي نصته ولا بمعطل
و فرع يزين المتن أسود فاحم .. أثيث كقنو النخلة المتعثكل
غدائره مستشزرات إلى العلا .. تضل العقاص في مثنى ومرسل
و كشح لطيف كالجديل مخصر .. و ساق كأنبوب السقي المذلل
و تضحي فتيت المسك فوق فراشها .. نؤوم الضحى لم تنتطق عن تفضل
و تعطو برخص غير ششن كأنه .. أساريع ظبي أو مساويك إسحل
تضيء الظلام بالعشاء كأنها .. منارة ممسى راهب متبتل
إلى مثلها يرنو الحليم صبابة .. إذا ما اسبكرت بين درع ومجول
تسلت عمايات الرجال عن الصبا .. و ليس فؤادي عن هواك بمنسل
ألا رب خصم فيك ألوى رددته .. نصيح على تعذاله غير مؤتل
و ليل كموج البحر أرخى سدوله .. علي بأنواع الهموم ليبتلي
فقلت له لما تمطى بصلبه .. و أردف أعجازا وناء بكلكل
ألا أيها الليل الطويل ألا انجلي .. بصبح وما الإصباح منك بأمثل
فيا لك من ليل كأن نجومه .. بكل مغار الفتل شدت بيذبل
كأن الثريا علقت في مصامها .. بأمراس كتان إلى صم جندل
وقد أغتدي والطير في وكناتها .. بمنجرد قيد الأوابد هيكل
مكر مفر مقبل مدبر معا .. كجلمود صخر حطه السيل من عل
كميت يزل اللبد عن حال متنه .. كما زلت الصفواء بالمتنزل
مسح إذا ما السابحات على الونى .. أثرن الغبار بالكديد المركل
على الذبل جياش كأن اهتزامه .. إذا جاش فيه حميه غلي مرجل
يزل الغلام الخف عن صهواته .. و يلوي بأثواب العنيف المثقل
درير كخذروف الوليد أمره .. تقلب كفيه بخيط موصل
له أيطلا ظبي وساقا نعامة .. و إرخاء سرحان وتقريب تتفل
كأن على الكتفين منه إذا انتحى .. مداك عروس أو صلاية حنظل
و بات عليه سرجه ولجامه .. و بات بعيني قائما غير مرسل
فعن لنا سرب كأن نعاجه .. عذارى دوار في ملاء مذيل
فأدبرن كالجزع المفصل بينه .. بجيد معم في العشيرة مخول
فألحقنا بالهاديات ودونه .. جواحرها في صرة لم تزيل
فعادى عداء بين ثور ونعجة .. دراكا ولم ينضح بماء فيغسل
و ظل طهاة اللحم من بين منضج .. صفيف شواء أو قدير معجل
و رحنا وراح الطرف ينفض رأسه .. متى ترق العين فيه تسفل
كأن دماء الهاديات بنحره .. عصارة حناء بشيب مرجل
و أنت إذا استدبرته سد فرجه .. بضاف فويق الأرض ليس بأعزل
أحار ترى برقا أريك وميضه .. كلمع اليدين في حبي مكلل
يضيء سناه أو مصابيح راهب .. أمال السليط بالذبال المفتل
قعدت له وصحبتي بين حامر .. وبين إكام بعدما متأملي
فأضحى يسح الماء عن كل فيقة .. يكب على الأذقان دوح الكنهبل
و تيماء لم يترك بها جذع نخلة .. و لا أطما إلا مشيدا بجندل
كأن ذرى رأس المجيمر غدوة .. من السيل والغثاء فلكة مغزل
كأن أبانا في أفانين ودقه .. كبير أناس في بجاد مزمل
و ألقى بصحراء الغبيط بعاعه .. نزول اليماني ذي العياب المحمل
كأن سباعا فيه غرقى غدية .. بأرجائه القصوى أنابيش عنصل
على قطن بالشيم أيمن صوبه .. و أيسره على الستار فيذبل
و ألقى ببيسان مع الليل بركه .. فأنزل منه العصم من كل منزل
"""
mu_en = """
Halt both of you and let us weep remembering a beloved and a home .. at the edge of the winding sands between Al-Dakhool and Hawmal
Thence to Tuwdih and Al-Miqrat where her camp's traces have not faded .. despite the shifting winds from north and south
You can see the dung of white deer in its courtyards .. and its lowlands looking like peppercorns
On the morning of separation the day they packed to leave .. I stood by the tribe's desert trees like one cutting bitter colocynth
My companions halted their mounts beside me .. saying do not destroy yourself with grief and bear it
Yet my only cure is a shedding of tears .. but is there any hope left at a fading ruin
This grief is like your old habit with Umm al-Huwayrith before her .. and her neighbor Umm al-Rabab at Masil
When they stood up the scent of musk wafted from them .. like a morning breeze bearing the fragrance of cloves
So the tears of love flowed from my eyes .. onto my chest until they soaked my sword-belt
Ah many a good day you enjoyed with them .. and most notably that day at Darat Juljul
And the day I slaughtered my mount for the maidens .. how wondrous was the lifting of its heavy saddle
The maidens spent the day tossing its meat to one another .. and its fat like the fringed tassels of twisted silk
And the day I entered the litter the litter of Unaizah .. and she cried woe to you you will make me walk
She said as the saddle tilted with both of us .. you have wounded my camel O Imru al-Qais so dismount
I said to her ride on and loosen his reins .. and do not banish me from your sweet repeated fruits
Many a pregnant woman like you have I visited by night and a nursing mother .. and distracted her from her amuleted infant
Whenever he cried behind her she turned half her body to him .. while the half beneath me remained unmoved
And one day on the crest of the dune she grew distant .. and swore an oath that could not be broken
O Fatima hold on and ease some of this disdain .. and if you have resolved to cut me off then do it gently
And if any of my habits have displeased you .. then draw my garments from yours and they will slip away
Did it deceive you that your love is my killer .. and that whatever you command my heart will perform
Your eyes did not shed those tears except to strike .. with your two arrows into a slain heart
And many a hidden maiden whose tent none dares approach .. have I enjoyed in unhurried pleasure
I passed by guards to reach her and a whole tribe .. eager and longing to secretly plot my death
That was when the Pleiades appeared across the sky .. like the gems of a detailed sash
I came to her when she had stripped her clothes for sleep .. by the curtain leaving only her light night-dress
She said by God you have no way out of this .. and I do not see your wandering passion clearing
I walked out with her as she dragged behind us .. over our footprints the train of an embroidered gown
When we crossed the open ground and turned .. into the belly of a wide valley of winding sand
I gently drew her head by her sidelocks and she leaned .. over me slender-waisted and full-ankled
Whenever she turned toward me her fragrance wafted .. like a morning breeze bearing the scent of cloves
Slender-waisted white-skinned and not fleshy .. her breastbone polished as a mirror
Like the first egg of an ostrich a blend of white and yellow .. nourished by pure water of an undisturbed spring
She turns away to show a smooth cheek and guards herself .. with the eyes of a wild doe of Wajrah with her fawn
And a neck like a white deer's not excessive .. when she lifts it nor left without adornment
And jet-black heavy hair adorning her back .. thick like the clustered branches of a date palm
Its braids are lifted to the crown .. and the knots hide both twisted and loosened strands
And a slender waist like a twisted leather strap .. and a leg like a well-watered smooth reed
She wakes with crushed musk scattered on her bed .. sleeping late into the forenoon ungirded
She reaches with delicate fingers not coarse .. like the soft worms of the sand or twigs of an Iskhir
She lights the darkness in the evening as if she were .. the evening lamp of a secluded monk
Upon her like a wise man gazes with longing .. when she stands tall between a maiden's dress and a gown
The distractions of other men have cleared from youth .. but my heart will never be detached from your love
Many a persistent adversary in your matter have I turned back .. who advised but was unyielding in blame
And a night like the waves of the sea let down its curtains .. over me with all kinds of cares to test my endurance
I said to it when it stretched out its spine .. and followed with its hindquarters and weighed down with its chest
O you long night will you not clear away .. to morning though the morning is no better than you
O what a night you are as if its stars .. were tied to Mount Yadhbul with tightly twisted ropes
As if the Pleiades were fixed in their place .. bound by linen cords to solid rocks
And I go out at dawn while the birds are in their nests .. on a short-haired steed that traps wild beasts
A master of charge and flight advance and retreat at once .. like a boulder hurled down by a torrent
A bay whose glossy back makes the saddle-felt slip .. as smooth stones make falling rain slide away
He runs hard even when other horses are weary .. raising the dust on the hard pounded ground
Lean yet he boils with energy as if his neighing .. when his fervor rages is the boiling of a pot
The lightweight boy slips off his back .. and he tosses the garments of the heavy rider into the air
He is swift like a child's spinning top .. whose string two rotating hands pull rapidly
He has the flanks of a gazelle and legs of an ostrich .. the gallop of a wolf and the spring of a fox
As if upon his shoulders when he runs .. is the grinding stone of a bride or crushed colocynth
His saddle and bridle remained on him through the night .. and he stood before my eyes all night untied
Then a herd of wild cows appeared as if its females .. were maidens circling an idol in trailing gowns
They turned back like a necklace of divided onyx .. on the neck of a boy well-born among his kin
He caught up with the leaders while behind him .. the rest stayed in a tight bunch undispersed
He ran on striking down a bull and a cow .. in quick succession without sweating to be washed
The cooks of the meat spent the day either boiling it .. or roasting it in strips or a quick stew
We returned in the evening while the steed shook his head .. whenever the eye rose to his top it fell back in awe
As if the blood of the leading cows on his chest .. was henna smeared on combed gray hair
And if you look at him from behind his thighs close the gap .. with a thick tail near the ground not crooked
O my companion do you see the lightning whose flash I show you .. like the movement of hands in a crowned cloud
Its light shines or looks like a monk's lamps .. who poured plenty of oil on twisted wicks
I sat to watch it with my companions between Hamir .. and Ikam after my sight had stretched far
It poured down its water from every cloud .. overturning the great Kanahbal trees on their faces
It did not leave a date palm trunk standing in Taima .. nor any fortress except those built firmly with stone
As if the summit of Mount Mujaymir in the morning .. with torrent and debris was a spindle's whorl
As if Mount Aban amid its downpour .. was an old chief wrapped in a striped cloak
It cast its heavy rain onto the desert of Al-Ghabeet .. like a Yemeni merchant unloading his packed bags
As if the wild beasts drowned in it at dawn .. at its furthest edges were uprooted wild onions
On Mount Qatan the right side of the storm poured .. while its left fell on Al-Sittar and Yadhbul
And it cast its clouds over Baisan by night .. bringing down the mountain goats from every peak
"""
mu_sharh = [
 {"t_ar":"مطلع القصيدة و البكاء على الأطلال","t_en":"The Prelude and Weeping Over the Ruins",
  "b_ar":"يبدأ الشاعر بالوقوف التقليدي على أطلال ديار محبوبته عنيزة، يستوقف رفيقيه ليبكيا معه ذكريات المواضع التي سكنتها، و يصف خلو الديار حتى لم يبق إلا بعر الغزلان كحب الفلفل، و يشبه حاله يوم الفراق بمن يقطع الحنظل المر، يبكي بحرقة رغم لوم أصحابه و دعوتهم إياه للصبر.",
  "b_en":"The poet begins with the pre-Islamic standing before the abandoned campsite of his beloved Unaizah, calling his two companions to weep over named places, describing the desolation where only deer droppings remain like peppercorns, equating his grief to a man cutting bitter colocynth, finding his only cure in tears despite his friends urging patience."},
 {"t_ar":"تذكر عهود الحب و قصة دارة جلجل","t_en":"Memories of Past Loves and the Day of Darat Juljul",
  "b_ar":"ينتقل بتذكر مغامراته العاطفية ليعزي نفسه، فيذكر أم الحويرث و أم الرباب و كيف فاحت منهما رائحة المسك كنسيم الصبا، ثم يستحضر مغامرته في دارة جلجل حين غافل العذارى و هن يسبحن فأخذ ثيابهن، و عقر لهن ناقته ليأكلن، ثم ركب الهودج مع عنيزة حتى مال و شكت من ثقله.",
  "b_en":"To console himself he recalls past loves, Umm al-Huwayrith and Umm al-Rabab, their scent like a breeze of cloves, then the day at Darat Juljul, catching maidens bathing and withholding their clothes, slaughtering his camel for them, then forcing his way into Unaizah's litter as it tilted under their weight."},
 {"t_ar":"مغازلة عشيقاته و حواره مع فاطم","t_en":"Flirtation and the Dialogue with Fatima",
  "b_ar":"يتفاخر بقدرته على الوصول الى النساء حتى الحوامل و المرضعات و إلهائهن عن أطفالهن، ثم يخاطب فاطم يرجوها أن تخفف دلالها، و يعلن استسلامه لسطوة حبها، موضحا أن دموعها سهام تصيب مقتل قلبه و تزيده تعلقا.",
  "b_en":"He boasts he could win even pregnant and nursing women, then pleads with Fatima to ease her cruelty, declaring his heart wholly obedient to her, realizing her tears are arrows aimed at his already-slain heart."},
 {"t_ar":"التسلل الى الخدر و وصف المحبوبة","t_en":"Infiltrating the Tent and the Beloved",
  "b_ar":"يصف مغامرة جريئة تسلل فيها ليلا الى خدر امرأة مصونة متجاوزا الحراس و الأهل الراغبين في قتله، حين تعرضت الثريا كوشاح مفصل، فوجدها قد خلعت ثيابها للنوم، ثم خرج بها و هي تجر ذيل مرطها لتعمي آثار أقدامهما، حتى بلغا واديا آمنا فضمها و وصف بياضها كالمرآة و جيدها كجيد الريم و شعرها الأسود الفاحم.",
  "b_en":"He recounts a daring night, slipping past guards and a tribe eager to kill him when the Pleiades hung like a jeweled sash, finding her undressed for sleep, leading her out as she dragged her gown to erase their tracks, and in a safe valley praising her mirror-bright skin, her gazelle neck and jet-black hair."},
 {"t_ar":"صفات المرأة المثالية","t_en":"Attributes of the Idealized Woman",
  "b_ar":"يستطرد في وصف مفاتنها: خصرها اللطيف، و ساقها الناعمة كأنبوب السقي، و ترفها إذ تنام الضحى، و رائحة المسك تفوح من فراشها، و أصابعها الرقيقة، و وجهها المشرق كمنارة راهب متبتل، و أنها محط أنظار الحكماء إذا بلغت النضج.",
  "b_en":"He continues the idealization: a slender waist, smooth legs like watered reeds, a luxurious life sleeping late, musk on her bed, delicate fingers, a face that lights the dark like a monk's lamp, the longing of every wise man when she comes of age."},
 {"t_ar":"وصف الليل الطويل و همومه","t_en":"The Eternal Night and its Sorrows",
  "b_ar":"ينتقل الى مقطع وجداني فلسفي يصف الليل كموج البحر يرخي سدوله محملا بالهموم ليختبر صبره، يخاطب الليل الطويل يطلب منه أن ينجلي عن الصبح رغم علمه أن الصبح لن يغير من همومه، و يشبه ثبات النجوم بأنها مشدودة بأمراس كتان الى صخر، أو مربوطة الى جبل يذبل.",
  "b_en":"A famous melancholic passage: the night like sea waves lets down its curtains of cares to test him. He begs it to yield to morning, knowing morning brings no relief, likening the static stars to linen ropes tied to solid rock and chained to Mount Yadhbul."},
 {"t_ar":"وصف الخيل المضمر و الصيد","t_en":"The Splendor of the Stallion and the Hunt",
  "b_ar":"يستعرض فروسيته فيصف خروجه باكرا و الطير في أعشاشها على فرس قوي سريع قيد الأوابد، و يأتي ببيته المعجز: مكر مفر مقبل مدبر معا كجلمود صخر حطه السيل من عل، و له صفات الظبي و النعامة و الذئب و الثعلب، يطارد قطيعا من بقر الوحش فيسقط ثورا و نعجة دون أن يعرق، و ينتهي المشهد بطهي اللحم و عودته يقطر صدره دما كأنه خضب بالحناء.",
  "b_en":"He displays his chivalry on a short-haired stallion that traps wild beasts, with the famous line, charging fleeing advancing retreating at once like a boulder hurled by a torrent. With the traits of gazelle ostrich wolf and fox it downs a bull and a cow without sweating, ending with cooking the game, its chest stained red like henna."},
 {"t_ar":"وصف البرق و المطر و السيول","t_en":"The Tempest, Lightning and the Torrent",
  "b_ar":"يختم بلوحة طبيعية مهيبة، يستوقف صاحبه ليريه برقا يلمع كحركة اليدين وسط سحاب كمصابيح الراهب، يصف المطر الغزير يقتلع شجر الكنهبل و لم يترك في تيماء نخلة و لا حصنا إلا المشيد بالصخر، و يشبه قمم الجبال بفلكة المغزل و جبل أبان كشيخ ملتف بكساء مخطط، و أثر السيل و ما خلفه من حيوانات غارقة كأصول البصل البري المقتلع، قوة مدمرة و خصب لاحق.",
  "b_en":"He closes with a roaring desert storm: lightning like moving hands within a crowned cloud, a torrent uprooting great trees, sparing in Taima only stone-built forts. He likens peaks to a spindle's whorl, Mount Aban to a chief in a striped cloak, and the drowned beasts to uprooted wild-onion bulbs, destruction and the fertility that follows."},
]
entries.append(poem(IMRU,
  "قفا نبك من ذكرى حبيب ومنزل ..", "Halt both of you and let us weep ..",
  mu_ar, mu_en, "الطويل", "Al-Tawil", "اللام (ل) - لامية", "Lam (ل)",
  "عامة - معلقة", "General - Mu'allaqah", 520, mu_sharh))
print("after muallaqa:", len(entries))

# ── امرؤ القيس — سما لك شوق (رحلة قيصر) ──
sb_ar = """
سما لك شوق بعدما كان أقصر .. و حلت سليمي بطن قو فعرعرا
كنانية بانت وفي الصدر ودها .. و جاورة غسان والحي يعمرا
بعيني ظعن الحي لما تحملوا .. لدى جانب الأفلاج من جنب تيمرا
فشبهتهم في الآل لما تكمشوا .. حدائق دوم أو سفينا مقيرا
أو المكراعات من نخيل ابن يامن .. دوين الصفا اللائي يلين المشقرا
سوامق جبار أثيث فروعه .. و عالين قنوانا من البسر أحمرا
حمته بنوا الربداء من آل يامن .. بأسيافهم حتى أقر وأوقرا
و أرضى بني الربداء واعتم زهوه .. و أكمامه حتى إذا ما تهصرا
أطافت به جيلان عند قطاعه .. تردد فيه العين حتى تحيرا
كأن دمى سقف على ظهر مرمر .. كسا مزبد الساجوم وشيا مصورا
غرائر في كن وصون ونعمة .. يحلين ياقوتا و شذرا مفقرا
و ريح سنا في حقة حميرية .. تخص بمفروك من المسك أذفرا
و بانا و ألويا من الهند داكيا .. و رندا و لبنى و الكباء المقترا
غلقن برهن من حبيب به ادعت .. سليمى فأمسى حبلها قد تبترا
و كان لها في سالف الدهر خلة .. يسارق بالطرف الخباء المسترا
إذا نال منها نظرة ريع قلبه .. كما ذرعت كأس الصبوح المخمرا
نزيف إذا قامت لوجه تمايلت .. تراشي الفؤاد الرخص ألا تخترا
أأسماء أمسى ودها قد تغيرا .. سنبدل إن أبدلت بالود آخرا
تذكرت أهلي الصالحين و قد أتت .. على خملى خوص الركاب و أوجرا
فلما بدت حوران في الآل دونها .. نظرت فلم تنظر بعينيك منظرا
تقطع أسباب اللبانة و الهوى .. عشية جاوزنا حماة و شيزرا
بسير يضج العود منه يمنه .. أخوا لجهد لا يلوى على من تعذرا
و لم ينسني ما قد لقيت ظعائنا .. و خملا لها كالقر يوما مخدرا
كأثل من الأعراض من دون بيشة .. و دون الغمير عامدات لغضورا
فدع ذا و سل الهم عنك بجسرة .. ذمول إذا صام النهار و هجرا
تقطع غيطانا كأن متونها .. إذا أظهرت تكسي ملاء منشرا
بعيدة بين المنكبين كأنها .. ترى عند مجرى الظفر هرا مشجرا
تطاير ظران الحصى بمناسم .. صلاب العجى ملثومها غير أمعرا
كأن الحصى من خلفها و أمامها .. إذا نجلته رحلها خذف أعسرا
كأن صليل المرو حين تطيره .. صليل زيوف ينتقدن بعبقرا
عليها فتى لم تحمل الأرض مثله .. أبر بميثاق و أوفى و أصبرا
هو المنزل الآلاف من جو ناعط .. بني أسد حزنا من الأرض أوعرا
ولو شاء كان الغزو من أرض حمير .. و لكنه عمدا إلى الروم أنفرا
بكى صاحبي لما رأى الدرب دونه .. و أيقن أنا لاحقان بقيصرا
فقلت له لا تبك عينك إنما .. نحاول ملكا أو نموت فنعذرا
و إني زعيم إن رجعت مملكا .. بسير ترى منه الفرانق أزورا
على لاحب لا يهتدي بمناره .. إذا سافه العود النباطي جرجرا
على كل مقصوص الذنابي معاود .. بريد السرى بالليل من خيل بربرا
أقب كسرحان الغضا متمطر .. ترى الماء من أعطافه قد تحدرا
إذا زعته من جانبيه كليهما .. مشي الهيدبى في دفه ثم فرفرا
إذا قلت روحنا أرن فرانق .. على جعلد واهي الأباجل أبترا
لقد أنكرتني بعلبك و أهلها .. و لابن جريج في قرى حمص أنكرا
نشيم بروق المزن أين مصابه .. و لا شيء يشفي منك يا ابنة عفزرا
من القاصرات الطرف لو دب محول .. من الذر فوق الإتب منها لأثرا
له الويل إن أمسى و لا أم هاشم .. قريب و لا البسباسة ابنة يشكرا
أرى أم عمرو دمعها قد تحدرا .. بكاء على عمرو و ما كان أصبرا
إذا نحن سرنا خمس عشرة ليلة .. وراء الحساء من مدافع قيصرا
إذا قلت هذا صاحب قد رضيته .. و قرت به العينان بدلت آخرا
كذلك جدي ما أصاحب صاحبا .. من الناس إلا خانني و تغيرا
و كنا أناسا قبل غزوة قرمل .. ورثنا الغنى و المجد أكبر أكبرا
و ما جبنت خيلي و لكن تذكرت .. مرابطها من بربعيص و ميسرا
ألا رب يوم صالح قد شهدته .. بتأذف ذات التل من فوق طرطرا
و لا مثل يوم في قذاران ظلته .. كأني و أصحابي على قرن أعفرا
و نشرب حتى نحسب الخيل حولنا .. نقادا و حتى نحسب الجون أشقرا
"""
sb_en = """
High longing came to you after it had abated .. and Sulayma descended in the heart of Qu and Ar'ar
A Kinani woman departed while her love remained in the breast .. neighboring Ghassan and the tribe of Ya'mur
With my own eyes I saw the tribe's caravan when they loaded .. by the side of Al-Aflaj from the side of Taymar
I likened them in the mirage when they hastened .. to gardens of dom trees or pitch-covered ships
Or the irrigated palm groves of Ibn Yamin .. below the Safa that border the Mashqar
Rising high, mighty, with thick branches .. and tall clusters of red dates
The sons of Ar-Rabda from the house of Yamin protected it .. with their swords until it was firm and weighed down
And it pleased the sons of Ar-Rabda, its beauty grew .. and its spathes until it bent under the weight
Jilan surrounded it when it was harvested .. the eye wanders through it until it is bewildered
As if statues of a ceiling on a marble back .. covered with the frothy fabric of the Sajum, patterned
Virginal girls in shielding, protection and luxury .. adorned with jewels and scattered gold
And the scent of senna in a Himyarite box .. enriched with rubbed musk, the most fragrant
And aloe wood and dark incense from India .. and randa, labdanum, and the burnt incense
They were barred by a promise from a lover whom .. Sulayma claimed, so her rope was severed
And she had in the past of time a friend .. stealing glances at the veiled tent
If he won a look from her his heart was shaken .. as if he had drunk the morning cup of wine
He is faint, if she rose before him she would sway .. coaxing the tender heart not to fear
O Asma, has your love for me changed .. We shall replace you if you replace love with another
I remembered my righteous family when they arrived .. at Khamla, the camels' hooves moving quickly
When Hauran appeared in the mirage before it .. you looked, but your eyes saw no sight
The ties of longing and desire were severed .. the evening we passed Hamah and Shayzar
With a journey that makes the wooden saddle groan .. both suffering fatigue, not turning to the failing
And my parting from the travelers did not make me forget .. Khamla, like the cold of a curtained day
Like Athal trees of the Arad away from Bisha .. and beyond the Ghamir, heading for Ghadur
So leave this and dispel the worry with a sturdy she-camel .. that trots when the day is hot and the noon blazes
Crossing valleys as if their backs .. when exposed were covered with a spread garment
Wide between the shoulders as if she .. sees at the hoof-strike an arch-backed cat
The hard pebbles fly from her hooves .. solid of sole, its surface unworn
As if the pebbles behind and before her .. when her saddle kicks them are a difficult throw
As if the clatter of flint when she flings it .. is the clatter of counterfeit coins tested in Abqar
Upon her is a youth whose like the earth has not borne .. more faithful to a pact, more fulfilling, more patient
He settled the thousands from the valley of Na'it .. the sons of Asad, in the roughest of lands
Had he wished the raid would be from the land of Himyar .. but he deliberately marched against the Romans
My companion wept when he saw the pass before him .. certain that we two would reach Caesar
So I said to him do not let your eye weep .. we seek a kingdom or we die and are excused
And I am a guarantor if I return a king .. with a march from which the swift courier turns aside
On a clear road whose beacon gives no guidance .. when the Nabataean wood treads it, it rattles
On every short-tailed, seasoned horse .. courier of the night journey, of the steeds of Barbar
Lean like a desert wolf, rain-drenched .. you see the water flowing down its flanks
If you urge it from both its sides .. it sways on its flank then bursts into gallop
If I say let us rest, the courier brays .. on a firm, weak-jointed, stump-tailed one
Baalbek and its people have denied me .. and Ibn Jurayj in the villages of Homs denied me
We watch the lightning of the clouds, where it strikes .. and nothing heals the pain of you, O daughter of Afzar
One who lowers her gaze, if a young ant crawled .. over her shift it would leave a mark
Woe to him at evening without Umm Hashim .. near, nor Al-Basbasa the daughter of Yashkur
I see Umm Amr, her tears already flowing .. weeping for Amr, and how patient she was
When we have traveled fifteen nights .. beyond the Hasa from the floodplains of Caesar
If I say this is a companion I am pleased with .. and my eyes are cooled by him, he is replaced
Such is my fortune, I befriend no companion .. among people but he betrays me and changes
We were a people before the raid of Qarmal .. we inherited wealth and ever-greater glory
My horses were not cowardly, but I recalled .. their tethering grounds at Rabi'is and Maysara
Many a good day have I witnessed .. at Ta'dhuf of the hill, above Tartar
And no day like the day at Qadhara I spent .. as if I and my companions were on a dusty horn
And we drink until we reckon the horses around us .. to be noble, and reckon the dark one to be reddish
"""
sb_sharh = [{
 "t_ar":"الشرح و الإشارات",
 "b_ar":"قصيدة من رحلة امرئ القيس نحو بلاد الروم يطلب نصرة قيصر على من قتل أباه و استرداد ملكه. تبدأ بالنسيب و وصف الظعائن و العطور، ثم تنقلب الى وصف الناقة الجسرة و الطريق الطويل، فيبلغ بيته الذائع حين يبكي صاحبه عند الدرب فيجيبه: نحاول ملكا أو نموت فنعذرا. تختم بالشكوى من خيانة الأصحاب و الحنين الى أيام المجد قبل النوائب.",
 "t_en":"Explanation and Indications",
 "b_en":"A poem of Imru' al-Qais's journey toward Byzantium to seek Caesar's aid against his father's killers and reclaim his kingdom. It opens with love-prelude, departing women and perfumes, then turns to the sturdy she-camel and the long road, reaching its famous line as his companion weeps at the pass and he answers, we seek a kingdom or we die and are excused. It closes lamenting the betrayal of friends and longing for days of glory before misfortune."
}]
entries.append(poem(IMRU,
  "سما لك شوق بعدما كان أقصر ..", "High longing came to you after it had abated ..",
  sb_ar, sb_en, "الطويل", "Al-Tawil", "الراء (ر) - رائية", "Ra (ر)",
  "عامة - رحلة و فخر", "General - journey and pride", 540, sb_sharh))
print("after B:", len(entries))

# ── امرؤ القيس — ألا عم صباحا أيها الطلل البالي ──
ta_ar = """
ألا عم صباحا أيها الطلل البالي .. و هل يعمن من كان في العصر الخالي
و هل يعمن إلا سعيد مخلد .. قليل الهموم ما يبيت بأوجال
و هل يعمن من كان أحدث عهده .. ثلاثين شهرا في ثلاثة أحوال
ديار لسلمى عافيات بذي خال .. ألح عليها كل أسحم هطال
و تحسب سلمى لا تزال ترى طلا .. من الوحش أو بيضا بميثاء محلال
و تحسب سلمى لا نزال كعهدنا .. بوادي الخزامى أو على رس أوعال
ليالي سلمى إذ تريك منصبا .. و جيدا كجيد الرئم ليس بمعطال
ألا زعمت بسباسة اليوم أنني .. كبرت و أن لا يحسن اللهو أمثالي
كذبت لقد أصبى على المرء عرسه .. و أمنع عرسي أن يزن بها الخالي
و يا رب يوم قد لهوت و ليلة .. بآنسة كأنها خط تمثال
يضيء الفراش وجهها لضجيعها .. كمصباح زيت في قناديل ذبال
كأن على لباتها جمر مصطل .. أصاب غضا جزلا و كف بأجزال
و هبت له ريح بمختلف الصوا .. صبا و شمال في منازل قفال
و مثلك بيضاء العوارض طفلة .. لعوب تنسيني إذا قمت سربالي
إذا ما الضجيع ابتزها من ثيابها .. تميل عليه هونة غير مجبال
كحقف النقا يمشي الوليدان فوقه .. بما احتسبا من لين مس و تسهال
لطيفة طي الكشح غير مفاضة .. إذا انفلتت مرتجة غير متفال
تنورتها من أذرعات و أهلها .. بيثرب أدنى دارها نظر عال
نظرت إليها و النجوم كأنها .. مصابيح رهبان تشب لقفال
سموت إليها بعد ما نام أهلها .. سمو حباب الماء حالا على حال
فقالت سباك الله إنك فاضحي .. ألست ترى السمار و الناس أحوالي
فقلت يمين الله أبرح قاعدا .. و لو قطعوا رأسي لديك و أوصالي
حلفت لها بالله حلفة فاجر .. لناموا فما إن من حديث و لا صال
فلما تنازعنا الحديث و أسمحت .. هصرت بغصن ذي شماريخ ميال
و صرنا إلى الحسنى و رق كلامنا .. و رضت فذلت صعبة أي إذلال
فأصبحت معشوقا و أصبح بعلها .. عليه القتام سيئ الظن و البال
يغط غطيط البكر شد خناقه .. ليقتلني و المرء ليس بقتال
أيقتلني و المشرفي مضاجعي .. و مسنونة زرق كأنياب أغوال
و ليس بذي رمح فيطعنني به .. و ليس بذي سيف و ليس بنبال
أيقتلني و قد شغفت فؤادها .. كما شغف المهنوءة الرجل الطالي
و قد علمت سلمى و إن كان بعلها .. بأن الفتى يهذي و ليس بفعال
و ماذا عليه إن ذكرت أوانسا .. كغزلان رمل في محاريب أقيال
و بيت عذارى يوم دجن ولجته .. يطفن بجباء المرافق مكسال
سباط البنان و العرانين و القنا .. لطاف الخصور في تمام و إكمال
نواعم يتبعن الهوى سبل الردى .. يقلن لأهل الحلم ضل بتضلال
صرفت الهوى عنهن من خشية الردى .. و لست بمقلي الخلال و لا قال
كأني لم أركب جوادا للذة .. و لم أتبطن كاعبا ذات خلخال
و لم أسبإ الزق الروي و لم أقل .. لخيلي كري كرة بعد إجفال
و لم أشهد الخيل المغيرة بالضحى .. على هيكل عبل الجزارة جوال
سليم الشظى عبل الشوى شنج النسا .. له حجبات مشرفات على الفال
وصم صلاب ما يقين من الوجى .. كأن مكان الردف منه على رأل
و قد أغتدي و الطير في وكناتها .. لغيث من الوسمي رائده خال
تحاماه أطراف الرماح تحاميا .. و جاد عليه كل أسحم هطال
بعجلزة قد أترز الجري لحمها .. كميت كأنها هراوة منوال
ذعرت بها سربا نقيا جلوده .. و أكرعه وشي البرود من الخال
كأن الصوار إذ تجهد عدوه .. على جمزى خيل تجول بأجلال
فجال الصوار و اتقين بقرهب .. طويل الفرا و الروق أخنس ذيال
فعادى عداء بين ثور و نعجة .. و كان عداء الوحش مني على بال
كأني بفتخاء الجناحين لقوة .. صيود من العقبان طأطأت شملالي
تخطف خزان الشرية بالضحى .. و قد حجرت منها ثعالب أورال
كأن قلوب الطير رطبا و يابسا .. لدى وكرها العناب و الحشف البالي
فلو أن ما أسعى لأدنى معيشة .. كفاني و لم أطلب قليل من المال
و لكنما أسعى لمجد مؤثل .. و قد يدرك المجد المؤثل أمثالي
و ما المرء ما دامت حشاشة نفسه .. بمدرك أطراف الخطوب و لا آلي
"""
ta_en = """
May you be greeted with morning, O worn-out ruin .. and can one of the bygone age be greeted
And can any be greeted except a happy, lasting one .. of few cares, who does not pass the night in terror
And can one be greeted whose latest bond .. was thirty months ago across three seasons
The abodes of Sulayma are effaced at Dhu Khal .. lashed by every dark, pouring cloud
Sulayma fancies she still sees a fawn .. of the wild, or white ones in the level land
Sulayma fancies we are as in our day .. at Wadi al-Khuzama or at Rass U'al
The nights of Sulayma when she showed you a slender waist .. and a neck like a wild deer's, unadorned
Babasa claimed today that I .. have aged, and that men like me cannot enjoy mirth
She lied, for a man's wife rekindles his passion .. and I guard my wife from the empty-hearted
And many a day I spent in mirth, and a night .. with a graceful woman like a carved image
Her face lights the bed for her companion .. like an oil lamp in the wicks of lanterns
As if on her throat were glowing embers .. that caught thick wood and a handful of kindling
And a wind blew for it from varied quarters .. east and north among the abandoned camps
And like you, a fair-cheeked, youthful girl .. playful, who makes me forget my cloak when I rise
When her companion strips her garments .. she leans on him, gently, not stiffly
Like a curved dune two children walk upon .. for the soft yielding touch they reckon
Slender of waist, not bulging .. if she slips free she is lively, not sluggish
I beheld her from Adhru'at, her people .. in Yathrib, her nearest abode a distant glance
I gazed at her while the stars were as if .. monks' lamps lit for travelers
I rose toward her after her people slept .. like the rising of water bubbles, state on state
She said may God ruin you, you will expose me .. do you not see the night-talkers and people around
I said by God's oath I will not cease to sit .. even if they cut off my head and limbs before you
I swore to her by God a sinner's oath .. that they slept, so there was no talk nor assault
When we contended in talk and she relented .. I bent a branch of swaying clusters
And we turned to kindness, our speech grew soft .. and she was tamed, the hard one wholly subdued
So I became beloved, and her husband became .. dust-covered, of ill thought and mind
He gasps like a young camel whose halter is drawn .. to kill me, yet the man is no killer
Does he kill me while the Musharafi sword is my bedfellow .. and sharp, blue blades like ghouls' fangs
He has no spear to thrust at me .. nor sword, nor arrows
Does he kill me when I have smitten her heart .. as the salve-man smites the treated camel
Sulayma knew, even if her husband did not .. that the youth raves but is no man of deeds
And what is it to him if I name graceful women .. like sand gazelles in the niches of kings
And a house of maidens on a cloudy day I entered .. they move with lovely forearms, languid
Slender of fingers, noses and stature .. thin of waist, in perfection and completion
Soft ones who follow desire down the paths of ruin .. saying to the prudent he is lost in delusion
I turned passion from them for fear of ruin .. and I am no despiser of virtues, nor a slanderer
As if I never rode a steed for pleasure .. and never embraced an anklet-wearing maiden
And never broached the full wineskin, nor said .. to my horses charge, a charge after retreat
And never witnessed the raiding horses at forenoon .. on a thick-muscled, roving stallion
Sound of bone, thick of legs, taut of sinew .. with hips raised high
Firm, hard hooves not spared from bruising .. as if the place of the croup were on an ostrich chick
And I go out at dawn while the birds are in their nests .. for a spring rain whose herald is green
The spear-tips shunned it, shunning indeed .. and every dark pouring cloud bestowed on it
On a sturdy mare whose flesh running has built .. dark bay as if she were a weaver's club
With her I startled a herd of pure-skinned ones .. their legs patterned like striped garments
As if the wild cattle, when they strained their run .. on hard ground, were horses roaming in majesty
The cattle roamed and shielded themselves with a strong bull .. long of horn, retreating, dragging
He coursed, a contest between a bull and a cow .. and the wild ones' contest was on my mind
As if I were a curved-winged predator .. a hunting eagle that lowered my wing
Snatching the lizards of the highland at forenoon .. while the foxes of Awral were denned away
As if the hearts of the birds, wet and dry .. at its nest, were jujube and shriveled dates
If what I strive for were a lowly living .. a little wealth would suffice, and I would not seek more
But I strive for a rooted glory .. and such as I may attain rooted glory
And a man, while a breath of soul remains .. attains the ends of fortune, and is never idle
"""
ta_sharh = [{
 "t_ar":"الشرح و الإشارات",
 "b_ar":"قصيدة لامرئ القيس يستهلها بالوقوف على الأطلال و التحية للديار البالية، ثم يتذكر سلمى و ليالي اللهو، و يرد على من زعم أنه شاخ عن الصبا. تتنقل بين الغزل و وصف المرأة، ثم وصف الفرس و رحلة الصيد، لتختم بنبرة الطموح: أنه لا يسعى لعيش زهيد بل لمجد مؤثل لا يبلغه إلا أمثاله.",
 "t_en":"Explanation and Indications",
 "b_en":"A poem of Imru' al-Qais opening with the standing over the ruins and a greeting to the worn abodes, recalling Sulayma and nights of mirth, answering those who claim he has aged past youth. It moves between love and the woman's portrait, then the horse and the hunt, closing on a note of ambition, that he seeks not a lowly life but a rooted glory only his like can reach."
}]
entries.append(poem(IMRU,
  "ألا عم صباحا أيها الطلل البالي ..", "May you be greeted with morning, O worn-out ruin ..",
  ta_ar, ta_en, "الطويل", "Al-Tawil", "الياء (ي) - يائية", "Ya (ي)",
  "غزل - فخر", "Love and pride", 523, ta_sharh))
print("after C:", len(entries))

# ── امرؤ القيس — ألا انعم صباحا أيها الربع و انطق ──
rb_ar = """
ألا انعم صباحا أيها الربع و انطق .. و حدث حديث الركب إن شئت و اصدق
و حدث بأن زالت بليل حمولهم .. كنخل من الأعراض غير منبق
جعلن حوايا و اقتعدن قعائدا .. و خففن من حوك العراق المنمق
و فوق الحوايا غزلة و جآذر .. تضمخن من مسك ذكي و زنبق
فأتبعتهم طرفي و قد حال دونهم .. غوارب رمل ذي ألاء و شبرق
على إثر حي عامدين لنية .. فحلوا العقيق أو ثنية مطرق
فعزيت نفسي حين بانوا بحسرة .. أمون كبنيان اليهودي خيفق
إذا زجرت ألفيتها مشمعلة .. تنيف بعذق من غروس ابن معنق
تروح إذا راحت رواح جهامة .. بإثر جهام رائح متفرق
كأن بها هرا جنيبا تجره .. بكل طريق صادفته و مأزق
كأني و رحلي و القراب و نمرقي .. على يرفئي ذي زوائد نقنق
تروح من أرض لأرض نطية .. لذكرة قيض حول بيض مفلق
يجول بآفاق البلاد مغربا .. و تسحقه ريح الصبا كل مسحق
و بيت يفوح المسك في حجراته .. بعيد من الآفات غير مروق
دخلت على بيضاء جم عظامها .. تعفي بذيل الدرع إذ جئت مودقي
و قد ركدت وسط السماء نجومها .. ركود نوادي الربرب المتورق
و قد أغتدي قبل العطاس بهيكل .. شديد مشك الجنب فعم المنطق
بعثنا ربيئا قبل ذاك محملا .. كذئب الغضى يمشي الضراء و يتقي
فظل كمثل الخشف يرفع رأسه .. و سائره مثل التراب المدقق
فجاء خفيا يسفن الأرض بطنه .. ترى الترب منه لاصقا كل ملصق
و قال ألا هذا صوار و عانة .. و خيط نعام يرتعي متفرق
فقمنا بأشلاء اللجام و لم نقد .. إلى غصن بان ناضر لم يحرق
نزاوله حتى حملنا غلامنا .. على ظهر ساط كالصليف المعرق
كأن غلامي إذ علا حال متنه .. على ظهر باز في السماء محلق
رأى أرنبا فانقض يهوي أمامه .. إليها و جلاها بطرف ملقلق
فقلت له صوب و لا تجهدنه .. فيدرك من أعلى القطاة فتزلق
فأدبرن كالجزع المفصل بينه .. بجيد الغلام ذي القميص المطوق
و أدركهن ثانيا من عنانه .. كغيث العشي الأقهب المتودق
فصاد لنا عيرا و ثورا و خاضبا .. عداء و لم ينضح بماء فيعرق
و ظل غلامي يضجع الرمح حوله .. لكل مهاة أو لأحقب سهوق
و قام طوال الشخص إذ يخضبونه .. قيام العزيز الفارسي المنطق
فقلنا ألا قد كان صيد لقانص .. فخبوا علينا كل بيت مزوق
و ظل صحابي يشتوون بنعمة .. يصفون غارا باللكيك الموشق
و رحنا كأن من جؤاثى عشية .. نعالي النعاج بين عدل و مشنق
و رحنا بكابن الماء يجنب وسطنا .. تصوب فيه العين طورا و ترتقي
و أصبح زهلولا يزل غلامنا .. كفدح النضي باليدين المفوق
كأن دماء الهاديات بنحره .. عصارة حناء بشيب مفرق
"""
rb_en = """
May you be greeted with morning, O quarter, and speak .. and tell the riders' tale if you wish, and be truthful
And tell that their baggage departed by night .. like palm trees of the Arad, not uprooted
They made them litters and sat upon them .. and lightened them of the patterned Iraqi weave
And upon the litters were gazelles and fawns .. perfumed with keen musk and lilies
So I followed them with my gaze, and between us .. rose the summits of a dune of A'la and Shabraq
Following a tribe bound for a goal .. they alighted at Al-Aqiq or the pass of Matraq
So I consoled my soul when they left, in regret .. on a sturdy mount, restless, like a Jew's structure
When I urged her I found her brisk .. towering like a palm-branch of Ibn Ma'naq's grafts
She goes at evening when a thin cloud goes .. following a dark cloud, scattered at dusk
As if a strange cat clung to her, dragged .. on every road and narrow pass she met
As if I and my saddle, sheath and cushion .. were on a long-bodied, rattling ostrich
She journeys from land to far land .. for the memory of a dry nest among split eggs
He roams the horizons of the land westward .. and the east wind wears him utterly down
And a house where musk wafts in its chambers .. far from blights, not refined away
I entered upon a fair one, full-boned .. who wiped with her shift's hem as I came at dusk
And her stars stood still in mid-sky .. like the stillness of the grazing wild herd
And I go out before the sneeze on a sturdy steed .. tight of flank, ample of frame
We sent a scout ahead, well-equipped .. like the Ghadah wolf walking the thickets, wary
He stayed like a fawn raising its head .. the rest of him like pulverized dust
He came stealthily, his belly sweeping the earth .. you see the soil clinging to all of him
And he said behold, here is a herd and wild asses .. and a string of ostriches grazing, scattered
So we rose with the reins' remnants and led not .. to a fresh, unburnt branch of Ban
We worked at it until we mounted our boy .. on the back of a swift, cross-bred, veined one
As if my boy, when he topped its back .. were on the back of a falcon soaring the sky
He saw a hare and swooped, plunging before it .. toward it, fixing it with a darting eye
So I said aim and do not exhaust him .. lest he reach from above the rump and slip
So they fled like onyx beads strung apart .. on the neck of the boy in the collared shirt
And he overtook them, turning from his rein .. like the evening rain, dusky and pouring
He hunted us a wild ass, a bull and a stained one .. in a race, not wetted with sweat to tire
And my boy kept laying the spear about him .. for every oryx or dark-backed, tall one
And he stood tall of frame as they daubed him .. the standing of a noble, eloquent Persian
So we said behold there was a hunt for the hunter .. so pitch for us every adorned tent
And my companions roasted in plenty .. dressing a cut with the well-mixed seasoning
And we went at evening as if from Juatha .. carrying the ewes between load and hanger
And we went with the son of water in our midst .. the eye descends upon it then rises
And it grew smooth, our boy slipping off .. like the felling of the fletched shaft by hand
As if the blood of the leading ones on his throat .. were the juice of henna on parted hair
"""
rb_sharh = [{
 "t_ar":"الشرح و الإشارات",
 "b_ar":"من مفاخر الشعر الجاهلي، تصور رحلة صيد ممتعة تبرز فروسية الشاعر و دقة وصفه للطبيعة. يبدأ بالوقوف على الربع و سؤاله عن رحيل الأحبة، ثم يصف الناقة الأمون التي تعينه على لوعة الفراق، و يفصل في أدوات الصيد و مهارة الغلام في ملاحقة الوحوش بصور تشبيهية دقيقة للخيل و الطرائد، و يختم بوصف الوليمة التي تلت الصيد في صورة تجمع القوة و النعمة.",
 "t_en":"Explanation and Indications",
 "b_en":"A celebrated pre-Islamic ode depicting a vivid hunt that showcases the poet's horsemanship and precise nature-painting. It opens at the abode, asking after the departed, then describes the sturdy she-camel that eases his grief, detailing the hunt and the boy's skill chasing the beasts with exact similes of horses and quarry, closing with the post-hunt feast in an image joining power and bounty."
}]
entries.append(poem(IMRU,
  "ألا انعم صباحا أيها الربع و انطق ..", "May you be greeted with morning, O quarter ..",
  rb_ar, rb_en, "الطويل", "Al-Tawil", "الياء (ي) - يائية", "Ya (ي)",
  "عامة - صيد و فروسية", "General - hunt and chivalry", 527, rb_sharh))
print("after D:", len(entries))

# ── امرؤ القيس — خليلي مرا بي على أم جندب ──
uj_ar = """
خليلي مرا بي على أم جندب .. ونقض لبانات الفؤاد المعذب
فإنكما إن تنظراني ساعة .. من الدهر تنفعني لدى أم جندب
ألم ترياني كلما جئت طارقا .. وجدت بها طيبا وإن لم تطيب
عقيلة أتراب لها لا ذميمة .. ولا ذات خلق إن تأملت جأنب
ألا ليت شعري كيف حادث وصلها .. وكيف تراعي وصلة المتغيب
أقامت على ما بيننا من مودة .. أميمة أم صارت لقول المخبب
فإن تنأ عنها حقبة لا تلاقها .. فإنك مما أحدثت بالمجرب
وقالت متى يبخل عليك ويعتلل .. يسؤك وإن يكشف غرامك تدرب
تبصر خليلي هل ترى من ظعائن .. سوالك نقبا بين حزمي شعبعب
علون بأنطاكية فوق عقمة .. كجرمة نخل أو كجنة يثرب
ولله عينا من رأى من تفرق .. أشت وأنأى من فراق المحصب
فريقان منهم جازع بطن نخلة .. وآخر منهم قاطع نجد كبكب
فعيناك غربا جدول في مفاضة .. كمر الخليج في صفيح مصوب
وإنك لم يفخر عليك كفاخر .. ضعيف ولم يغلبك مثل مغلب
وإنك لم تقطع لبانة عاشق .. بمثل غدو أو رواح مؤوب
بأدماء حرجوج كأن قتودها .. على أبلق الكشحين ليس بمغرب
يغرد بالأسحار في كل سدفة .. تغرد مياح الندامى المطرب
أقب رباع من حمير عماية .. يمج لعاع البقل في كل مشرب
بمحنية قد آزر الضال نبتها .. مجر جيوش غانمين وخيب
وقد أغتدي والطير في وكناتها .. وماء الندى يجري على كل مذنب
بمنجرد قيد الأوابد لاحه .. طراد الهوادي كل شأو مغرب
على الأين جياش كأن سراته .. على الضمر والتعداء سرحة مرقب
يباري الخنوف المستقل زماعه .. ترى شخصه كأنه عود مشجب
له أيطلا ظبي وساقا نعامة .. وصهوة عير قائم فوق مرقب
ويخطو على صم صلاب كأنها .. حجارة غيل وارسات بطحلب
له كفل كالدعص لبده الندى .. إلى حارك مثل الغبيط المذأب
وعين كمرآة الصناع تديرها .. لمحجرها من النصيف المنقب
له أذنان تعرف العتق فيهما .. كسامعتي مذعورة وسط ربرب
ومستفلك الذفرى كأن عنانه .. ومثناته في رأس جذع مشذب
وأسحم ريان العسيب كأنه .. عثاكيل قنو من سميحة مرطب
إذا ما جرى شأوين وابتل عطفه .. تقول هزير الريح مرت بأثأب
يدير قطاة كالمحالة أشرفت .. إلى سند مثل الغبيط المذأب
ويخضد في الآري حتى كأنما .. به عرة من طائف غير معقب
فيوما على سرب نقي جلوده .. ويوما على بيدانة أم تولب
فبينا نعاج يرتعين خميلة .. كمشي العذارى في الملاء المهدب
فكان تنادينا وعقد عذاره .. وقال صحابي قد شأونك فاطلب
فلأيا بلأي ما حملنا غلامنا .. على ظهر محبوك السراة محنب
وولى كشؤبوب العشي بوابل .. ويخرجن من جعد ثراه منصب
فللساق ألهوب وللسوط درة .. وللزجر منه وقع أهوج متعب
فأدرك لم يجهد ولم يثن شأوه .. يمر كخذروف الوليد المثقب
ترى الفار في مستنقع القاع لاحبا .. على جدد الصحراء من شد ملهب
خفاهن من أنفاقهن كأنما .. خفاهن ودق من عشي مجلب
فعادى عداء بين ثور ونعجة .. وبين شبوب كالقضيمة قرهب
وظل لثيران الصريم غماغم .. يداعسها بالسمهري المعلب
فكاب على حر الجبين ومتق .. بمدرية كأنها ذلق مشعب
وقلنا لفتيان كرام ألا انزلوا .. فعالوا علينا فضل ثوب مطنب
وأوتاده ماذية وعماده .. ردينية بها أسنة قعضب
وأطنابه أشطان خوص نجائب .. وصهوته من أتحمي مشرعب
فلما دخلناه أضفنا ظهورنا .. إلى كل حاري جديد مشطب
كأن عيون الوحش حول خبائنا .. وأرجلنا الجزع الذي لم يثقب
نمش بأعراف الجياد أكفنا .. إذا نحن قمنا عن شواء مضهب
ورحنا كأنا من جؤاثى عشية .. نعالي النعاج بين عدل ومحقب
وراح كتيس الربل ينفض رأسه .. أذاة به من صائك متحلب
كأن دماء الهاديات بنحره .. عصارة حناء بشيب مخضب
و أنت إذا استدبرته سد فرجه .. بضاف فويق الأرض ليس بأصهب
"""
uj_en = """
My two friends, take me by Umm Jundub .. and settle the needs of the tormented heart
And if you wait for me a moment .. of time, it will profit me before Umm Jundub
Do you not see me, whenever I come a night-visitor .. I find her sweet, even when unperfumed
A choicest of her peers, not despicable .. nor of ill form if you ponder her aspect
Alas I wish I knew how her bond fares .. and how she keeps the tie of the absent one
Did Ummayma stay true to our affection .. or did she heed the slanderer's word
And if you are long absent and do not meet her .. you become, by what you wrought, an experienced one
She said when he is stingy and makes excuses .. it grieves you, and if your love shows you are tamed
Look, my friend, do you see any travelers .. roaming a pass between the two ridges of Sha'ba'ab
They climbed at Antioch above barren ground .. like a cluster of palms or the garden of Yathrib
To God belong the eyes of one who saw a parting .. more scattered, more distant than Al-Muhassab's
Two parties, one crossing the valley of Nakhla .. another cutting the highland of Kabkab
So your two eyes are a stream in a wide basin .. like the canal's flow on a slanted plate
And no weak boaster has boasted over you .. nor has any overcomer overcome you
And you have not cut a lover's need .. with the like of an early or a returning ride
On a dark, lean, sturdy mare whose saddle-bows .. were as on a piebald of flanks, no stranger
She sings at the dawns in every darkness .. like the singing of swaying, merry companions
Lean and young of the best Himyarite breed .. spitting the fields' fresh herbage at each spring
In a bend where lotus shelters its growth .. a passage of armies, victors and the failed
And I go out at dawn while the birds are in their nests .. and the dew-water runs on every branch
On a smooth-backed restrainer of wild beasts .. polished by chasing every distant quarry
In fatigue he surges, as if his withers .. lean and racing, were a watchtower's stem
He rivals the swift one of his own resolve .. you see his form like a wooden clothes-rack
He has the flanks of a gazelle, an ostrich's legs .. and the croup of an ass on a lookout
And he steps on firm hard hooves as if they were .. stones of a stream rooted with moss
He has a haunch like a dune the dew has packed .. up to a withers like a leather saddle
And an eye like the artisan's mirror she turns .. for its socket from the lifted veil
He has two ears in which you know nobility .. like the ears of a startled one amid a herd
And a rounded nape, as if his rein .. and neck-knots were at a pruned branch's head
And a dark, full-stalked tail as if it were .. the ripening clusters of a Samiha palm
When he runs two reaches and his side grows wet .. you say a gust of wind passed by a fig tree
He turns a croup like a risen millstone .. up to a support like a leather saddle
And he champs in the stable as if upon him .. were a mark of a night-spirit, unrelenting
So one day on a herd of pure skins .. and one day on a wild cow, mother of a calf
While ewes were grazing a thicket .. like maidens walking in fringed robes
And it was our calling out and his rein's tying .. my friend said they have outrun you, pursue
With much toil we mounted our boy .. on the back of a firm-built, curved one
And he turned away like the evening shower in a downpour .. and they burst from the tangled, poured-out ground
For the leg a burst, for the whip a flow .. and for the urging a heavy, tiring blow
He overtook untired, his reach unbent .. passing like a child's pierced spinning-top
You see the mouse in the valley pool, coursing .. on the desert's surface from the burning speed
He drew them from their burrows, as if .. he drew them with the rain of a gathered dusk
He coursed, a contest between a bull and a cow .. and a raging one, strong-backed like a biting ass
And the bulls of the thicket kept groaning .. as he gored them with the seasoned spear
He fell on the heat of the brow, on guard .. with a point like the sharp tip of a cluster
And we said to noble youths will you not alight .. so they raised above us the spare of a tied tent
Its pegs of Mazi wood, its pole .. of Rudayni wood bearing sharp spear-points
Its ropes the cords of choice palm-fiber .. its seat of a tanned, lofty hide
When we entered it we leaned our backs .. against every new, carved support
As if the wild beasts' eyes around our tent .. and our feet were unpierced carnelian
We wipe our palms on the horses' manes .. when we rise from the spread-out roast
And we went at evening as if from Juatha .. carrying the ewes between load and strapped bag
And he went like the Rabl buck shaking his head .. an annoyance on him from the dripping sweat
As if the blood of the leading ones on his throat .. were the juice of henna on dyed hair
And you, if you are behind him, his gap is closed .. by a full tail above the earth, not reddish
"""
uj_sharh = [{
 "t_ar":"الشرح و الإشارات",
 "b_ar":"من روائع الشعر الجاهلي، يستهلها الشاعر بالغزل بأم جندب و التحسر على الفراق، ثم ينتقل ببراعة الى وصف دقيق للفرس و رحلة الصيد. القصيدة مليئة بالصور البيانية، تجسد مهارة الشاعر في وصف الخيل و تشريح كل جزء فيها، و تبرز الاعتزاز بالفروسية و الكرم، بجزالة ألفاظ و قوة تراكيب تعكس روح البادية الجاهلية و جسارة أهلها.",
 "t_en":"Explanation and Indications",
 "b_en":"One of the masterpieces of pre-Islamic verse. The poet opens with a love-song to Umm Jundub and grief at parting, then turns with great skill to a precise portrait of his horse and a hunt. The poem teems with imagery, embodying his mastery in describing the steed limb by limb, and his pride in chivalry and generosity, with sonorous diction and powerful structures reflecting the spirit of the desert and the boldness of its people."
}]
entries.append(poem(IMRU,
  "خليلي مرا بي على أم جندب ..", "My two friends, take me by Umm Jundub ..",
  uj_ar, uj_en, "الطويل", "Al-Tawil", "الباء (ب) - بائية", "Ba (ب)",
  "عامة - غزل و فروسية", "General - love and chivalry", 530, uj_sharh))

# ── الأمير بدر بن عبد المحسن — رذاذ (نبطي، حديث، سعودي) ──
BADR = dict(poet_key="badr_bin_abdulmohsen", poet_ar="الأمير بدر بن عبد المحسن", poet_en="Badr bin Abdul Mohsen Al Saud",
            gender="male", period="العصر الحديث", period_en="Modern era",
            homeland_ar="المملكة العربية السعودية", homeland_en="Saudi Arabia",
            laqab_ar="فارس الكلمة", laqab_en="The Knight of the Word",
            bio_ar="الأمير بدر بن عبد المحسن بن عبد العزيز آل سعود، شاعر و رسام سعودي يعد من أبرز رواد الحداثة الشعرية في الجزيرة العربية. كتب القصيدة الغنائية الرفيعة في أغراض فنية مختلفة، و صور الواقع الاجتماعي و السياسي، و جمع بين الأسلوبين التقليدي و الحداثي. لقب فارس الكلمة، و كرمه الملك سلمان بوشاح عبد العزيز آل سعود.",
            bio_en="Prince Badr bin Abdul Mohsen Al Saud, a Saudi poet and painter, one of the foremost pioneers of poetic modernism in the Arabian Peninsula. He wrote refined lyric poetry across varied themes and portrayed social and political life, blending traditional and modernist styles. Titled the Knight of the Word, he was decorated by King Salman with the King Abdulaziz Medal.")
badr_ar = """
رذاذ ما سقى خدك .. و عنقود العنب ما ابيه
و تين ما حضن يدك .. و لو طاب و نضج ما اشريه
دخيل الله من صدك .. و من طول الجفا و طاريه
أنا اللي لو صفا ودك .. بطير من الفرح و التيه
في وادي وج و الردف .. هواك يدوزن أوتاره
بين الطار و بين الكف .. حديث معرف أسراره
قصيدة حبرها ما جف .. من أول يوم شفتك فيه
أنا اللي لو صفا ودك .. بطير من الفرح و التيه
أجي متولع و خايف .. يشاركني الجبل وصلك
و ألقى اليوم يالطايف .. سبقني للوعد رملك
تأمل حالي وش شايف .. نحولي و التعب يكفيه
أنا اللي لو صفا ودك .. أبيع العمر و أشتريه
أنا اللي لو صفا ودك .. بطير من الفرح و التيه
"""
badr_en = """
A drizzle that did not water your cheek .. and the grape cluster, I want it not
And a fig your hand has not cradled .. I will not buy it, ripe and sweet as it is
I seek refuge in God from your rejection .. and from the long estrangement and its mention
I am the one who, if your love runs pure .. would fly away with joy and rapture
In Wadi Wajj and Ar-Ruddaf .. your love tunes its strings
And between the tambourine and the palm .. a talk whose secrets I know
And a poem whose ink has not dried .. since the first day I saw you
I am the one who, if your love runs pure .. would fly away with joy and rapture
I come passionate and afraid .. that the mountain might share your nearness
And today I find, O Taif .. your sands have beaten me to the tryst
Look at my state, what do you see .. my frailty and weariness say enough
I am the one who, if your love runs pure .. would sell my life and buy it anew
I am the one who, if your love runs pure .. would fly away with joy and rapture
"""
badr_sharh = [{
 "t_ar":"الشرح و الإشارات",
 "b_ar":"القصيدة على بحر الهجيني النبطي، تتوزع تفعيلاته القريبة من البسيط أو الرجز في الفصيح لتناسب الشيلات و الغناء. لوحة غزلية وجدانية مرتبطة بمكان محدد هو مدينة الطائف، يذكر معالمها وادي وج و الردف و الجبل. يفضل الشاعر رذاذ المطر الذي يلامس خد المحبوب على أطيب الثمار العنب و التين، و يصور الوجد و الخوف من الفقد، و كيف تشاركه طبيعة الطائف و جبالها هذا الحب.",
 "t_en":"Explanation and Indications",
 "b_en":"The poem rides the Nabati Hajini meter, its feet close to the classical Basit or Rajaz, suited to chant and song. A tender love-tableau bound to the city of Taif, naming Wadi Wajj, Ar-Ruddaf and its mountain. The poet prizes the rain-drizzle that touches the beloved's cheek over the finest fruits, grapes and figs, picturing yearning and the fear of loss, and how the nature and mountains of Taif share his love."
}]
entries.append(poem(BADR,
  "رذاذ ما سقى خدك ..", "A drizzle that did not water your cheek ..",
  badr_ar, badr_en, "الهجيني", "Al-Hajini (Nabati)", "", "",
  "مدن و غزل", "Cities and love", 2017, badr_sharh,
  era="sub_era_hadith", nat="sub_nat_saudi", timeline="tl_poem_hadith",
  tags="sub_pt_nabati, sub_st_qafiyatayn",
  poemtype_ar="نبطي", poemtype_en="Nabati",
  structure_ar="قافيتين", structure_en="Two rhymes",
  form_ar="نبطية غنائية - شيلة", form_en="Nabati lyric"))

# ── الإخراج ──
import json
json.dump(entries, open("public/seed/enc/poems.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("TOTAL poems:", len(entries))
for e in entries:
    print(" -", e["poem"]["poet_key"], "|", e["titles"]["ar"][:34], "| year", e["year"], "| rawi", e["poem"]["rawi_ar"])
