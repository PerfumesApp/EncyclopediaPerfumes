# EncyclopediaPerfumes
تطبيق لا يحتاج اتصال انترنت لتتبع العطور ومرفق إدارة موسوعة

# موسوعة  Encyclopedia
A local-first, offline, bilingual (English / Arabic) encyclopedia app for Android,
built with React + Vite + Capacitor. All data lives on the device (IndexedDB) —
no server, no account, no tracking.

This is a **clean template**: it ships with no catalog data, so you can build your
own content on top of it.

## What's included
- Bilingual (EN / AR), RTL-aware UI with a configurable theme colour.
- Encyclopedia with a **Stories** section (one example entry) and a **Perfumes Era** timeline.
- A **notes** reference list (text only).
- Offline-first storage via IndexedDB.

## What's intentionally empty (clean template)
- No perfumes, brands, or perfumers seed data.
- Notes ship as text only (no images or image links).
- Stories contain a single example entry — add your own.

## Tech stack
- React + Vite (web)
- Capacitor 8 (Android)
- IndexedDB (offline storage)

## Build (Android)
See `INSTALL_ANDROID.md` for full steps. In short:

```
npm install
npm run build
npx cap add android
npx cap sync android
npx @capacitor/assets generate --android
```

Then open the `android/` project in Android Studio and build the APK.

## License
Open source. Use, modify, and contribute freely.
