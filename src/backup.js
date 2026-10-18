import { supabase } from "./lib/supabaseClient";

// Tables worth keeping a copy of. Student-owned data (profiles, answers) is left
// out on purpose: the backup is for the content the team builds by hand.
const TABLES = ["teachers", "variants", "questions", "option_groups", "analog_questions",
  "topics", "topic_examples", "video_transcripts", "video_questions", "variant_purchases"];

// Downloads every table as one JSON file. Reads as the signed-in admin, so
// row-level security decides what is included; failures are listed, not hidden.
export async function downloadBackup() {
  const out = { exportedAt: new Date().toISOString(), tables: {}, errors: {} };
  for (const t of TABLES) {
    const rows = [];
    for (let from = 0; ; from += 1000) {
      const { data, error } = await supabase.from(t).select("*").range(from, from + 999);
      if (error) { out.errors[t] = error.message; break; }
      rows.push(...data);
      if (data.length < 1000) break;
    }
    out.tables[t] = rows;
  }
  const blob = new Blob([JSON.stringify(out, null, 2)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `kimyo-zaxira-${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(a.href);
  const counts = Object.entries(out.tables).map(([k, v]) => `${k}: ${v.length}`).join("\n");
  const errs = Object.keys(out.errors).length ? "\n\nXatolar: " + JSON.stringify(out.errors) : "";
  alert("Zaxira nusxa yuklandi.\n\n" + counts + errs);
}
