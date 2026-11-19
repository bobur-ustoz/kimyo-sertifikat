import { test } from "node:test";
import assert from "node:assert/strict";
import { yigish, AGENTLAR } from "../api/_ofis.js";

const NOW = new Date("2026-11-19T14:00:00Z");
const q = (id, agent, tur, holat, soatOldin, extra = {}) => ({ id, agent, tur, holat, sarlavha: `${agent} ${tur} ${id}`, kimga: null, created_at: new Date(NOW.getTime() - soatOldin * 3600e3).toISOString(), ...extra });
const topish = (d, id) => d.agentlar.find((a) => a.id === id);

test("yigish: har agent chiqadi, navbat bo'sh bo'lsa hammasi kutmoqda (qurilmagani alohida)", () => {
  const d = yigish([], NOW);
  assert.equal(d.agentlar.length, AGENTLAR.length);
  assert.equal(topish(d, "izoh").belgi, "yoq");
  assert.ok(d.agentlar.filter((a) => a.id !== "izoh").every((a) => a.belgi === "kutmoqda" && a.oxirgi === null && a.ishlar.length === 0));
  assert.deepEqual(d.ustozga, []);
});

test("yigish: holat belgisi ustuvorligi: xato, sizdan savol, ishlayapti, bugun ishlagan, kutmoqda", () => {
  const d = yigish([
    q(1, "kod", "xato", "yangi", 2, { kimga: "kod" }), q(2, "kod", "ish", "bajarildi", 1),
    q(3, "instagram", "savol", "yangi", 5, { kimga: "ustoz" }),
    q(4, "montaj", "ish", "jarayonda", 0.2),
    q(5, "pdf", "ish", "bajarildi", 3),
    q(6, "sotuv", "ish", "bajarildi", 30),
    q(7, "marketolog", "savol", "bekor", 1, { kimga: "ustoz" }),
  ], NOW);
  assert.deepEqual(["kod", "instagram", "montaj", "pdf", "sotuv", "marketolog"].map((id) => topish(d, id).belgi), ["xato", "savol", "ishlayapti", "faol", "kutmoqda", "kutmoqda"]);
  assert.equal(topish(d, "montaj").hozir, "montaj ish 4");
  assert.deepEqual(d.ustozga.map((r) => [r.agent, r.id]), [["instagram", 3]]);            // bekor qilingan savol sanalmaydi
  assert.deepEqual(topish(d, "kod").soni, { ish: 1, hisobot: 0, xato7: 1, ochiq: 1 });
  assert.equal(topish(d, "kod").oxirgi.id, 2);                                              // eng yangi yozuv
});

test("yigish: ro'yxatda yo'q agent yozuvi yo'qolmaydi, alohida ko'rsatiladi", () => {
  assert.deepEqual(yigish([q(1, "yangilik", "hisobot", "bajarildi", 1)], NOW).tanilmagan, ["yangilik"]);
});
