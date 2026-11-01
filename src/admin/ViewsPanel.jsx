import { useEffect, useState } from "react";
import { supabase } from "../lib/supabaseClient";
import { C, card, pageTitle } from "./ui";

const mins = (s) => (s < 60 ? `${s} s` : `${Math.round(s / 60)} daq`);
const when = (t) => new Date(t).toLocaleString("uz-UZ", { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" });
const tab = (on) => ({ padding: "7px 14px", borderRadius: 8, border: `1px solid ${on ? C.primary : C.border}`, background: on ? C.primary : "#fff", color: on ? "#fff" : C.textMid, fontSize: 12.5, fontWeight: 700, cursor: "pointer", fontFamily: "inherit" });

// Admin view of who watched what: by video (which ones are watched, by how many students) and
// by student (what each one has watched). Rows come from video_views, written by track_video_view().
export default function ViewsPanel() {
  const [data, setData] = useState(null);
  const [by, setBy] = useState("video");
  const [open, setOpen] = useState(null);

  useEffect(() => {
    (async () => {
      const [v, q, vr, t, tp, ex, ll] = await Promise.all([
        supabase.from("video_views").select("*").order("last_at", { ascending: false }).limit(20000),
        supabase.from("questions").select("id,question_number,variant_id,bunny_video_id").limit(5000),
        supabase.from("variants").select("id,variant_number,teacher_id"),
        supabase.from("teachers").select("id,name"),
        supabase.from("topics").select("id,name"),
        supabase.from("topic_examples").select("id,example_number,topic_id"),
        supabase.from("live_lessons").select("id,title"),
      ]);
      const teacher = Object.fromEntries((t.data || []).map((x) => [x.id, x.name]));
      const variant = Object.fromEntries((vr.data || []).map((x) => [x.id, x]));
      const topic = Object.fromEntries((tp.data || []).map((x) => [x.id, x.name]));
      const label = {};
      (q.data || []).forEach((x) => { const va = variant[x.variant_id]; label["question:" + x.id] = `${teacher[va?.teacher_id] || "?"} · ${va?.variant_number}-variant · ${x.question_number}-savol`; });
      (ex.data || []).forEach((x) => { label["example:" + x.id] = `Mavzu: ${topic[x.topic_id] || "?"} · ${x.example_number}-misol`; });
      (tp.data || []).forEach((x) => { label["topic:" + x.id] = `Mavzu darsi: ${x.name}`; });
      (ll.data || []).forEach((x) => { label["live:" + x.id] = `Jonli dars: ${x.title || ""}`; });
      const rows = v.data || [];
      const seen = new Set(rows.map((r) => r.kind + ":" + r.ref_id));
      const unseen = (q.data || []).filter((x) => x.bunny_video_id && !seen.has("question:" + x.id)).length;
      setData({ rows, label, unseen, error: v.error?.message });
    })();
  }, []);

  if (!data) return <div style={{ fontSize: 13, color: C.textMid }}>Yuklanmoqda...</div>;
  if (data.error) return <div style={{ ...card, color: C.danger, fontSize: 13 }}>Ko'rishlar jadvali topilmadi ({data.error}). Migratsiya (video_views) hali ishga tushirilmagan.</div>;

  const { rows, label, unseen } = data;
  const group = (keyOf, nameOf) => {
    const m = {};
    rows.forEach((r) => {
      const k = keyOf(r);
      const g = (m[k] ||= { key: k, name: nameOf(r), people: [], opens: 0, seconds: 0, last: r.last_at });
      g.people.push(r); g.opens += r.opens; g.seconds += r.seconds;
      if (r.last_at > g.last) g.last = r.last_at;
    });
    return Object.values(m);
  };
  const list = by === "video"
    ? group((r) => r.kind + ":" + r.ref_id, (r) => label[r.kind + ":" + r.ref_id] || "(o'chirilgan video)").sort((a, b) => b.people.length - a.people.length || b.seconds - a.seconds)
    : group((r) => r.student_id, (r) => r.student_name || r.student_email || r.student_id.slice(0, 8)).sort((a, b) => b.seconds - a.seconds);
  const students = new Set(rows.map((r) => r.student_id)).size;

  return (
    <div>
      <div style={pageTitle}>Ko'rishlar</div>
      <div style={{ fontSize: 12.5, color: C.textMid, marginBottom: 14 }}>
        {rows.length ? `${students} ta o'quvchi · ${rows.length} ta video ko'rilgan · variant savollaridan ${unseen} tasini hech kim ko'rmagan` : "Hali ko'rish yozuvlari yo'q. Yangi kod deploy bo'lgach, o'quvchilar video ochganda shu yerda paydo bo'ladi."}
      </div>
      <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
        <button style={tab(by === "video")} onClick={() => { setBy("video"); setOpen(null); }}>Videolar bo'yicha</button>
        <button style={tab(by === "student")} onClick={() => { setBy("student"); setOpen(null); }}>O'quvchilar bo'yicha</button>
      </div>
      <div style={card}>
        {list.map((g) => (
          <div key={g.key} style={{ borderBottom: `1px solid ${C.border}` }}>
            <div onClick={() => setOpen(open === g.key ? null : g.key)} style={{ display: "flex", alignItems: "center", gap: 12, padding: "9px 0", cursor: "pointer" }}>
              <div style={{ flex: 1, fontSize: 13, fontWeight: 700, color: C.text }}>{g.name}</div>
              <div style={{ fontSize: 12, color: C.textMid, width: 110, textAlign: "right" }}>{by === "video" ? `${g.people.length} o'quvchi` : `${g.people.length} video`}</div>
              <div style={{ fontSize: 12, color: C.textMid, width: 70, textAlign: "right" }}>{g.opens} marta</div>
              <div style={{ fontSize: 12, fontWeight: 800, color: C.primary, width: 70, textAlign: "right" }}>{mins(g.seconds)}</div>
              <div style={{ fontSize: 11, color: C.textLight, width: 90, textAlign: "right" }}>{when(g.last)}</div>
            </div>
            {open === g.key && (
              <div style={{ background: C.bgSoft, borderRadius: 8, padding: "6px 12px", marginBottom: 8 }}>
                {g.people.sort((a, b) => b.seconds - a.seconds).map((r) => (
                  <div key={r.student_id + r.video_id} style={{ display: "flex", gap: 12, padding: "4px 0", fontSize: 12, color: C.textMid }}>
                    <div style={{ flex: 1, color: C.text }}>{by === "video" ? (r.student_name || r.student_email || r.student_id.slice(0, 8)) : (label[r.kind + ":" + r.ref_id] || "(o'chirilgan video)")}</div>
                    <div style={{ width: 70, textAlign: "right" }}>{r.opens} marta</div>
                    <div style={{ width: 70, textAlign: "right", fontWeight: 700 }}>{mins(r.seconds)}</div>
                    <div style={{ width: 90, textAlign: "right" }}>{when(r.last_at)}</div>
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
