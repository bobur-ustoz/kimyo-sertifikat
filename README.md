# 🧪 Kimyo Sertifikat — Milliy Sertifikat Platformasi

AI-powered kimyo sertifikat tayyorlanish platformasi. Claude AI analog savol generatori va adaptiv test tizimi bilan.

---

## 🚀 Deploy qilish (5 daqiqa)

### 1-qadam — Node.js o'rnating
https://nodejs.org → LTS versiyani yuklab o'rnating

### 2-qadam — Loyihani o'rnating

```bash
cd kimyo-sertifikat
npm install
```

### 3-qadam — Lokal sinab ko'ring

```bash
npm run dev
```
Brauzer avtomatik ochilib `http://localhost:3000` da ishlaydi.

---

## 🌐 Vercel ga deploy (bepul)

### Usul 1 — Vercel CLI (tez)

```bash
# Vercel o'rnating (bir marta)
npm install -g vercel

# Deploy
vercel --prod
```
Email kiriting → link tayyor! `kimyo-sertifikat.vercel.app`

### Usul 2 — GitHub + Vercel (tavsiya)

1. **GitHub** da yangi repo yarating: `kimyo-sertifikat`
2. Terminalda:
```bash
git init
git add .
git commit -m "Kimyo Sertifikat - birinchi versiya"
git remote add origin https://github.com/SIZNING_USERNAME/kimyo-sertifikat.git
git push -u origin main
```
3. **vercel.com** ga kiring → "Add New Project" → GitHub repo tanlang → Deploy

✅ Har safar `git push` qilsangiz — avtomatik yangilanadi!

---

## 📁 Loyiha tuzilmasi

```
kimyo-sertifikat/
├── public/
│   └── favicon.svg          # Logo ikonka
├── src/
│   ├── main.jsx             # React kirish nuqtasi
│   └── App.jsx              # Asosiy ilova (barcha kod)
├── index.html               # HTML shablon
├── package.json             # Kutubxonalar
├── vite.config.js           # Vite sozlamalari
├── vercel.json              # Vercel deploy sozlamalari
└── .gitignore
```

---

## ✨ Funksiyalar

- 📚 **6 ta o'qituvchi** kolleksiyasi
- 🎬 **20 ta variant**, har birida 43 ta masala video tahlili
- 🏷️ **Mavzular bo'yicha** filtrlash
- 📊 **Tahlil grafiklari** (Bar chart + Radar chart)
- 🤖 **AI Analog Savol Generator** (Claude AI)
- 🧠 **AI Adaptive Test Generator** (Zaif mavzularga moslashtirilgan)
- 💳 **3 ta obuna rejasi** (Bepul / Standart / Premium)

---

## 💰 Video kirish qoidasi (pullik qism)

| Kim | Nimani ko'radi |
|-----|----------------|
| Mehmon (login yo'q) | Har o'qituvchining **bitta bepul varianti** — to'liq, 43 ta video |
| Ro'yxatdan o'tgan | Bepul variant + o'zi sotib olgan variantlar |
| Premium obunachi | **Barcha variantlar**, to'lovsiz |

Qolgan variantlar **variantiga 5 000 so'mdan** (narx admin panelda o'zgartiriladi) —
bir marta to'lanadi, umrbod ochiq qoladi.

Bu qoida `api/bunny-token.js` da **serverda** tekshiriladi: to'lamagan odam video
tokenini umuman ololmaydi. Brauzerdagi qulf belgilari faqat ko'rsatma.

### Sotib olish oqimi (hozircha qo'lda)

1. O'quvchi variant ustiga bosadi → telefon raqamini qoldiradi → `pending` so'rov tushadi
2. Siz `/admin` → **To'lovlar** bo'limida so'rovni ko'rasiz, pulni qabul qilasiz
3. **"To'landi"** tugmasini bosasiz → variant o'sha zahoti ochiladi

O'quvchi o'ziga o'zi variant ocholmaydi — buni RLS qat'iy taqiqlaydi
(`status='paid'` yozish, narxni pasaytirish, boshqa nom bilan so'rov — hammasi bloklangan).

### Click / Payme ulash (keyinroq)

`api/grant-variant.js` — avtomatik to'lov uchun tayyor ulanish nuqtasi. Provayder
adapteri o'z imzosini tekshirgach shu endpointga POST qiladi. Ishga tushishi uchun
Vercel'da ikkita o'zgaruvchi kerak:

```
PAYMENT_WEBHOOK_SECRET=<uzun tasodifiy satr>
SUPABASE_SERVICE_ROLE_KEY=<Supabase service_role kaliti>
```

Ular qo'yilmaguncha endpoint `503` qaytaradi — ya'ni tasodifan ochilib qolmaydi.

---

## 🔧 Sozlamalar

### Claude API
`src/App.jsx` faylida `callClaude` funksiyasi Anthropic API ga murojaat qiladi.
Hozircha API kalit shart emas (Claude.ai artifacts orqali ishlaydi).
Production uchun `.env` fayliga qo'shing:
```
VITE_ANTHROPIC_API_KEY=sk-ant-...
```

---

## 🛠️ Texnologiyalar

| Kutubxona | Versiya | Maqsad |
|-----------|---------|--------|
| React | 18.3 | UI framework |
| Vite | 5.3 | Build tool |
| Recharts | 2.12 | Grafiklar |
| Lucide React | 0.383 | Ikonkalar |
| Claude AI | claude-sonnet-4-6 | AI funksiyalar |

---

## 📞 Muammo bo'lsa

1. `node_modules` papkasini o'chirib, `npm install` qayta ishlatib ko'ring
2. Node.js versiyasi 18+ bo'lishi kerak: `node --version`
3. Port band bo'lsa: `npm run dev -- --port 3001`

---

*Kimyo Sertifikat · Milliy Sertifikat 2026*

