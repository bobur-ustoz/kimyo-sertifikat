// AI ofis: agentlar jamoasini ko'rsatadigan mahalliy sahifa uchun kichik server.
//
//   node agentlar/ofis.mjs [port=5183]        keyin brauzerda http://localhost:5183
//   node agentlar/ofis.mjs --malumot          serversiz: ma'lumotni JSON qilib chiqaradi (tekshirish uchun)
//
// Sahifa (public/ofis/index.html, saytda admin panel ichida ham shu fayl) har ochilganda /malumot.json ni so'raydi:
// agentlar ro'yxati (api/_ofis.js dan) va ularning ishlari (agent_navbat jadvalidan, oxirgi 30 kun). Faqat o'qiydi, hech narsa yozmaydi va yubormaydi.
// Kalit (.env dagi SUPABASE_SERVICE_ROLE_KEY) shu jarayon ichida qoladi: sahifaga chiqmaydi. Server faqat shu kompyuterda (127.0.0.1) tinglaydi.
import { readFileSync, existsSync, statSync } from "fs";
import { createServer } from "http";
import { fileURLToPath } from "url";
import { join, normalize, extname } from "path";
import { createClient } from "@supabase/supabase-js";
import { yigish, ofisMalumot } from "../api/_ofis.js";

const ILDIZ = fileURLToPath(new URL("../public/ofis/", import.meta.url));     // sahifa saytdagi bilan bitta fayl
const env = Object.fromEntries(readFileSync(new URL("../.env", import.meta.url), "utf8").split("\n")
  .map((l) => l.match(/^([A-Z0-9_]+)=(.*)$/)).filter(Boolean).map((m) => [m[1], m[2].trim().replace(/^["']|["']$/g, "")]));
const db = env.VITE_SUPABASE_URL && env.SUPABASE_SERVICE_ROLE_KEY ? createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } }) : null;

export async function malumot(now = new Date()) {
  if (!db) return { ...yigish([], now), ogohlantirish: ".env da baza kalitlari yo'q: ishlar ko'rsatilmaydi" };
  return ofisMalumot(db, now);
}

const TUR = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".json": "application/json; charset=utf-8", ".css": "text/css; charset=utf-8", ".png": "image/png", ".jpg": "image/jpeg", ".svg": "image/svg+xml" };

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  if (process.argv.includes("--malumot")) { console.log(JSON.stringify(await malumot(), null, 1)); process.exit(0); }
  const port = Number(process.argv[2]) || 5183;
  let kesh = null, keshVaqt = 0;
  createServer(async (req, res) => {
    try {
      const yol = decodeURIComponent(new URL(req.url, "http://x").pathname);
      if (req.method !== "GET") { res.writeHead(405).end(); return; }
      if (yol === "/malumot.json") {
        if (!kesh || Date.now() - keshVaqt > 15000) { kesh = await malumot(); keshVaqt = Date.now(); }
        res.writeHead(200, { "Content-Type": TUR[".json"], "Cache-Control": "no-store" }).end(JSON.stringify(kesh)); return;
      }
      const fayl = normalize(join(ILDIZ, yol === "/" ? "index.html" : yol));
      if (!fayl.startsWith(ILDIZ) || !existsSync(fayl) || !statSync(fayl).isFile()) { res.writeHead(404).end("Topilmadi"); return; }
      res.writeHead(200, { "Content-Type": TUR[extname(fayl)] || "application/octet-stream", "Cache-Control": "no-store" }).end(readFileSync(fayl));
    } catch (e) { res.writeHead(500).end("Xato: " + e.message); }
  }).on("error", (e) => {
    // Port band: odatda ofis allaqachon ochiq (boshqa oynada yoki brauzer panelida). Bu xato emas.
    if (e.code === "EADDRINUSE") { console.log(`AI ofis allaqachon ishlab turibdi: http://localhost:${port}\nBoshqa portda ochish uchun: node agentlar/ofis.mjs ${port + 1}`); process.exit(0); }
    console.error("Server ishga tushmadi:", e.message); process.exit(1);
  }).listen(port, "127.0.0.1", () => console.log(`AI ofis: http://localhost:${port}`));
}
