// Mijozga boradigan ko'rinish. To'g'ri javob, tenglama kaliti va tuzoq belgisi bu yerdan CHIQMAYDI:
// o'quvchi ularni sahifa kodidan ko'ra olmasligi kerak. Javob faqat tekshirilgandan keyin ochiladi.
import { gradeEquation, gradeBuild, condensed } from "./chem.js";

export function publicQuestion(q, order) {
  const base = { id: q.id, type: q.type, lvl: q.lvl, group: q.group, p: q.p };
  if (q.type === "choice") {
    const all = [q.ok, ...q.no];
    return { ...base, ...(q.mol ? { mol: q.mol } : {}), options: (order || [0, 1, 2, 3]).map((i) => all[i]) };
  }
  if (q.type === "write") return { ...base, ...(q.chain ? { chain: q.chain } : {}) };
  return base;   // build: nom savol matnida, javob tuzilishi
}

// answer: choice -> tanlangan variant matni; write -> tenglama matni; build -> { n, br }
// -> { ok, trapHit, reveal: {...} }  reveal faqat javobdan keyin mijozga qaytariladi
export function check(q, answer) {
  let ok = false, msg = "", got;
  if (q.type === "choice") ok = answer === q.ok;
  else if (q.type === "write") { const r = gradeEquation(answer, q); ok = r.ok; msg = r.msg || ""; }
  else { const r = gradeBuild(answer, q); ok = r.ok; got = r.got; msg = r.msg || ""; }
  const trapHit = q.type === "choice" && !!q.trap && answer === q.trap.opt;
  const correct = q.type === "choice" ? q.ok : q.type === "write" ? q.ans : { name: q.build, formula: condensed(q.build) };
  return {
    ok, trapHit,
    reveal: { explanation: q.w, correct, ...(msg ? { message: msg } : {}), ...(got ? { got } : {}), ...(trapHit ? { trapWhy: q.trap.why } : {}) },
  };
}
