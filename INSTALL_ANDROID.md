# تنصيب تطبيق «موسوعة» على Android Studio
# Building "Encyclopedia" (موسوعة) on Android Studio

التطبيق: **موسوعة / Encyclopedia** · المعرّف `com.encymawsuah.app` · قاعدة البيانات `EncymawsuahDB` · Capacitor 8 · مجلّد الويب `dist`.
(versionName حرّ — يقبل `0.0.0` في جوجل بلاي؛ المهمّ `versionCode` يتزايد.)

## المتطلّبات
- Node.js (LTS) + npm
- Android Studio (SDK + Platform Tools)

## البناء أوّل مرّة (الهويّة الجديدة — يتطلّب توليد android من جديد)
1. احذفي مجلّد `android/` القديم إن وُجد.
2. `npm install`
3. `npm run build`
4. `npx cap add android`  ← يولّد مشروع أندرويد بـ`com.encymawsuah.app`.
5. الصقي **MainActivity.java** (المرفق) في:
   `android/app/src/main/java/com/encymawsuah/app/MainActivity.java`
   (يضبط edge-to-edge + شريطين شفّافين + إلغاء القناع الغامق لأندرويد 15.)
6. `npx cap sync android`
7. `npx capacitor-assets generate --android`  ← يولّد الأيقونة/السبلاش من `assets/icon.png` (لوقو الموسوعة).
   - **لا تشغّلي** `npm run icons:android` إلا إن أردتِ أيقونات `android-icons/` الجاهزة (هي أيضاً لوقو الموسوعة).
8. `npx cap open android`  ← Build > Clean Project ← Rebuild Project ← Build APK.

## كلّ بناء بعدها (روتين)
1. `npm run build`
2. `npx cap sync android`
3. Android Studio ← Build APK.
(لا حذف، لا `cap add`، MainActivity يبقى ثابتاً.)

## ملاحظات
- `appId: com.encymawsuah.app` — لا تغيّريه بعد النشر (يحفظ بيانات القاعدة). معزول تماماً عن أي تطبيق قديم على نفس الجهاز.
- `EncymawsuahDB` تُنشأ فارغة أوّل فتح و تُبذر كاملةً (لا بيانات حيّة) — قد تأخذ الفهرسة لحظات («index building %»).
- لون الثيم الافتراضيّ أخضر · اسم العرض «موسوعة».

---
# English
App: **Encyclopedia / موسوعة** · id `com.encymawsuah.app` · DB `EncymawsuahDB` · Capacitor 8 · web dir `dist`. versionName is free (Google Play accepts `0.0.0`; versionCode must increase).

First build (new identity): delete old `android/` → `npm install` → `npm run build` → `npx cap add android` → paste MainActivity.java at `android/app/src/main/java/com/encymawsuah/app/MainActivity.java` → `npx cap sync android` → `npx capacitor-assets generate --android` (icon from `assets/icon.png`) → open → Clean → Rebuild → Build APK.
Routine: `npm run build` → `npx cap sync android` → Build APK.
Notes: don't change appId after publishing; DB seeds fresh on first open; default theme is green; do NOT run `icons:android` unless you want the prepared `android-icons/` set (also the encyclopedia logo).
