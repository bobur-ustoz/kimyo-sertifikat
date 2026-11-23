// Uyga vazifaning dizaynli PDF'i (platformaning test PDF'i bilan bir xil ko'rinish: ko'k-sariq shapka, ikki ustun,
// moddalar va raqamlar qiya). Serverda yasaladi va yordamchi bot orqali o'quvchiga fayl qilib yuboriladi.
// Chizish kodi brauzerdagi bilan bitta: src/testPdf.js. Shriftlar saytning o'zidan (/fonts) olinadi.
import * as JSPDF from "jspdf";
import { buildTestPdf } from "../src/testPdf.js";

const jsPDF = JSPDF.jsPDF || JSPDF.default?.jsPDF;
const SHRIFTLAR = [["LMRoman-Regular.ttf", "normal", "LM"], ["LMRoman-Bold.ttf", "bold", "LM"], ["LMRoman-Slanted.ttf", "normal", "LMSl"], ["DejaVuSans.ttf", "normal", "DejaVu"]];
let kesh = null;      // bitta ishga tushishda shriftlar bir marta olinadi

// Shriftlarni base64 qilib qaytaradi. olib = (fayl nomi) => Promise<ArrayBuffer | Buffer> (sinovda diskdan o'qiladi).
export async function shriftlar(olib) {
  if (!kesh) kesh = Promise.all(SHRIFTLAR.map(async ([fayl, uslub, oila]) => ({ fayl, uslub, oila, b64: Buffer.from(await olib(fayl)).toString("base64") }))).catch((e) => { kesh = null; throw e; });
  return kesh;
}
export const saytdanOlib = (site) => async (fayl) => {
  const r = await fetch(`${site}/fonts/${fayl}`);
  if (!r.ok) throw new Error(`shrift olinmadi: ${fayl} (${r.status})`);
  return r.arrayBuffer();
};

const kun = (t) => new Date(new Date(t).getTime() + 5 * 3600e3).toISOString().slice(0, 10).split("-").reverse().join(".");

// -> Buffer (PDF). savollar: { question_text, formula, option_a..d } (to'g'ri javobsiz ham bo'ladi: PDF'ga javob chiqmaydi).
export async function vazifaPdf(vazifa, savollar, { olib }) {
  const doc = new jsPDF();
  for (const s of await shriftlar(olib)) { doc.addFileToVFS(s.fayl, s.b64); doc.addFont(s.fayl, s.oila, s.uslub); }
  buildTestPdf(doc, { questions: savollar, label: vazifa.tur === "imtihon" ? "Imtihon" : "Uyga vazifa",
    subtitle: `${vazifa.nom} · ${savollar.length} ta savol${vazifa.muddat ? ` · ${kun(vazifa.muddat)} gacha` : ""}` });
  return Buffer.from(doc.output("arraybuffer"));
}
