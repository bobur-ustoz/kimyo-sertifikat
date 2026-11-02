// Kunlik savol fayli (v2) ni dvigatel o'qiydigan shaklga keltiradi.
//
// Fayl: { version: 2, day, topic, substances: [...majburiy moddalar], slots: [ { slot, group, type, lvl,
//   bundleGroup?, variants: [ ...savol variantlari ] } ] }
// Har "o'rin" (slot) uchun 2–3 ta teng qiyinlikdagi variant bor; o'quvchiga bittasi tushadi.

export function loadDay(json) {
  if (json.version !== 2) throw new Error("fayl versiyasi 2 bo'lishi kerak");
  const slots = json.slots.map((s) => ({
    slot: s.slot, group: s.group, type: s.type, lvl: s.lvl, bundleGroup: s.bundleGroup || null,
    variants: s.variants.map((v, i) => ({
      ...v,
      id: `d${String(json.day).padStart(2, "0")}-${s.slot}-${i + 1}`,
      day: json.day, topic: json.topic, slot: s.slot, group: s.group, type: s.type, lvl: s.lvl,
      bundleGroup: s.bundleGroup || null, uses: v.uses || [],
    })),
  }));
  return { day: json.day, topic: json.topic, substances: json.substances || [], slots };
}

export const allQuestions = (days) => days.flatMap((d) => d.slots.flatMap((s) => s.variants));
export const byId = (days) => new Map(allQuestions(days).map((q) => [q.id, q]));
