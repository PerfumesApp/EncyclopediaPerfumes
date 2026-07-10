import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.encymawsuah.app',
  appName: 'موسوعة',
  webDir: 'dist',
  android: {
    // Capacitor 8: مثبّت صراحةً على القيمة الفعّالة منذ Cap 6 (https) — يمنع أي تغيّر صامت للنطاق
    // فلا تفقد بيانات IndexedDB/localStorage عند الترقية. لا تغيّر هذه القيمة على نسخة منشورة.
    androidScheme: 'https',
    backgroundColor: '#C8A02E', // مطابق لشاشة البداية الذهبية — يلغي الومضة البيضاء في فجوة الرسم بين إخفاء السبلاش وأول رسم للمحتوى
    allowMixedContent: false, // لا محتوى مختلطا — تطبيق بلا شبكة أصلا (CSP في index.html يقطع كل الطلبات الخارجية)
  },
  plugins: {
    StatusBar: {
      // شريط شفّاف (overlay): تظهر خلفية التطبيق تحته. يضبطه main.jsx أيضًا حسب الثيم.
      backgroundColor: '#00000000',
      style: 'DARK',
      overlaysWebView: true,
    },
    SplashScreen: {
      launchShowDuration: 1500,
      backgroundColor: '#C8A02E',
      androidScaleType: 'FIT_CENTER',
      showSpinner: false,
      splashFullScreen: true,
      splashImmersive: true,
      launchAutoHide: true,
    },
    Keyboard: {
      resize: 'body',
    },
  },
};

export default config;
