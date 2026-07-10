import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'
import path from 'path'
import { readFileSync } from 'fs'

// نقرأ النسخة من package.json وقت البناء فتصبح ثابتة داخل الحزمة (A 1.812):
// كانت تظهر «من» versionName في gradle، و إعادة توليد android/ من الصفر تفقدها —
// الآن النسخة تأتي من مصدر واحد (package.json) و تظهر داخل التطبيق فلا تضيع أبدا.
const pkg = JSON.parse(readFileSync(path.resolve(__dirname, 'package.json'), 'utf-8'));

// Encyclopedia — offline-friendly Vite config
// لا ملحق بناء خارجيّ — التطبيق أوفلاين بالكامل
export default defineConfig({
  define: {
    __APP_VERSION__: JSON.stringify(pkg.version),
  },
  logLevel: 'warn',
  // تجريد console.log/info/debug من حزمة الإنتاج: تُعلَّم «نقيّة» فيحذفها المصغّر
  // لأن قيمتها غير مستعملة. نُبقي console.warn و console.error للتشخيص (وحارس الأداء).
  esbuild: { pure: ['console.log', 'console.info', 'console.debug', 'console.trace'] },
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    port: 5173,
    open: true,
    host: true,
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
    rollupOptions: {
      output: {
        // Function form matches sub-paths (react-dom/client, react/jsx-runtime)
        // so the react vendor chunk is no longer empty. Other libs (charts,
        // jspdf, html2canvas, …) are left to Vite's default code-splitting so
        // they stay in their on-demand lazy chunks.
        manualChunks(id) {
          if (id.includes('node_modules/react-router')) return 'router';
          if (id.includes('node_modules/react-dom') || id.includes('node_modules/react/') || id.includes('node_modules/scheduler')) return 'react';
          if (id.includes('node_modules/@radix-ui')) return 'ui';
        }
      }
    }
  }
})
