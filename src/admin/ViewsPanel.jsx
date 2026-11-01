import { useEffect, useState } from "react";
import { supabase } from "../lib/supabaseClient";
import { C, card, pageTitle } from "./ui";

const mins = (s) => (s < 60 ? `${s} s` : `${Math.round(s / 60)} daq`);
const MONTHS = ["yan", "fev", "mar", "apr", "may", "iyn", "iyl", "avg", "sen", "okt", "noy", "dek"];
// "1-noy 14:03", in Uzbekistan time whatever the admin's computer clock says.
const when = (t) => {
  const d = new Date(new Date(t).getTime() + 5 * 3600 * 1000);
  const pad = (n) => String(n).padStart(2, "0");
  return `${d.getUTCDate()}-${MONTHS[d.getUTCMonth()]} ${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}`;
};
// How much was actually watched: opening a video is not the same as watching it.
const status = (sec) => sec >= 60 ? { t: "Ko'rdi", bg: "#DCFCE7", fg: "#166534" } : sec >= 10 ? { t: "Qisman", bg: "#FEF3C7", fg: "#92400E" } : { t: "Faqat ochdi", bg: "#F1F5F9", fg: "#64748B" };
const Badge = ({ sec }) => { const st = status(sec); return <span style={{ background: st.bg, color: st.fg, borderRadius: 20, padding: "2px 9px", fontSize: 11, fontWeight: 800, whiteSpace: "nowrap" }}>{st.t}</span>; };
const tab = (on) => ({ padding: "7px 14px", borderRadius: 8, border: `1px solid ${on ? C.primary : C.border}`, background: on ? C.primary : "#fff", color: on ? "#fff" : C.textMid, fontSize: 12.5, fontWeight: 700, cursor: "pointer", fontFamily: "inherit" });

// Admin view of who watched what: by video (which ones are watched, by how many students) and
// by student (what each one has watched). Rows come from video_views, written by track_video_view().
export default function ViewsPanel() {
  const [data, setData] = useState(null);
  const [by, setBy] = useState("video");
  const [open, setOpen] = useState(null);
  const [work, setWork] = useState(null);   // variant answers per student (admin_variant_activity)

  useEffect(() => {
    (async () => {
      const [v, q, vr, t, tp, ex, ll, gv] = await Promise.all([
        supabase.from("video_views").select("*").order("last_at", { ascending: false }).limit(20000),
        supabase.from("questions").select("id,question_number,variant_id,bunny_video_id").limit(5000),
        supabase.from("variants").select("id,variant_number,teacher_id"),
        supabase.from("teachers").select("id,name"),
        supabase.from("topics").select("id,name"),
        supabase.from("topic_examples").select("id,example_number,topic_id"),
        supabase.from("live_lessons").select("id,title"),
        supabase.from("guest_views").select("*").order("last_at", { ascending: false }).limit(20000),
      ]);
      const teacher = Object.fromEntries((t.data || []).map((x) => [x.id, x.name]));
      const variant = Object.fromEntries((vr.data || []).map((x) => [x.id, x]));
      const topic = Object.fromEntries((tp.data || []).map((x) => [x.id, x.name]));
      const label = {};
      (q.data || []).forEach((x) => { const va = variant[x.variant_id]; label["question:" + x.id] = `${teacher[va?.teacher_id] || "?"} · ${va?.variant_number}-variant · ${x.question_number}-savol`; });
      (ex.data || []).forEach((x) => { label["example:" + x.id] = `Mavzu: ${topic[x.topic_id] || "?"} · ${x.example_number}-misol`; });
      (tp.data || []).forEach((x) => { label["topic:" + x.id] = `Mavzu darsi: ${x.name}`; });
      (ll.data || []).forEach((x) => { label["live:" + x.id] = `Jonli dars: ${x.title || ""}`; });
      // Guests (not signed in) are anonymous: one pseudo-student per browser.
      const guests = (gv.data || []).map((g) => ({ ...g, student_id: "g:" + g.device_id, student_name: `Mehmon ${g.device_id.slice(0, 4)} (${g.device_kind || "?"})`, student_email: null, guest: true }));
      const rows = [...(v.data || []), ...guests];
      const seen = new Set(rows.map((r) => r.kind + ":" + r.ref_id));
      const unseen = (q.data || []).filter((x) => x.bunny_video_id && !seen.has("question:" + x.id)).length;
      setData({ rows, label, unseen, error: v.error?.message });
    })();
  }, []);

  useEffect(() => {
    supabase.rpc("admin_variant_activity").then(({ data: d, error }) => setWork(error ? { error: error.message } : d || []));
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
  const students = new Set(rows.filter((r) => !r.guest).map((r) => r.student_id)).size;
  const guestCount = new Set(rows.filter((r) => r.guest).map((r) => r.student_id)).size;

  return (
    <div>
      <div style={pageTitle}>Ko'rishlar</div>
      <div style={{ fontSize: 12.5, color: C.textMid, marginBottom: 14 }}>
        {rows.length ? `${students} ta o'quvchi${guestCount ? ` + ${guestCount} ta mehmon (kirmagan)` : ""} · ${rows.length} ta ko'rish yozuvi · variant savollaridan ${unseen} tasini hech kim ko'rmagan` : "Hali ko'rish yozuvlari yo'q. Yangi kod deploy bo'lgach, o'quvchilar video ochganda shu yerda paydo bo'ladi."}
      </div>
      <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
        <button style={tab(by === "video")} onClick={() => { setBy("video"); setOpen(null); }}>Videolar bo'yicha</button>
        <button style={tab(by === "student")} onClick={() => { setBy("student"); setOpen(null); }}>O'quvchilar bo'yicha</button>
        <button style={tab(by === "work")} onClick={() => { setBy("work"); setOpen(null); }}>Variant ishlaganlar</button>
      </div>
      {by === "work" ? <WorkList work={work} open={open} setOpen={setOpen}/> : (
      <div style={card}>
        {list.map((g) => (
          <div key={g.key} style={{ borderBottom: `1px solid ${C.border}` }}>
            <div onClick={() => setOpen(open === g.key ? null : g.key)} style={{ display: "flex", alignItems: "center", gap: 12, padding: "9px 0", cursor: "pointer" }}>
              <div style={{ flex: 1, fontSize: 13, fontWeight: 700, color: C.text }}>{g.name}</div>
              <div style={{ fontSize: 12, color: C.textMid, width: 170, textAlign: "right" }}>{by === "video" ? `${g.people.length} o'quvchi · ${g.people.filter((r) => r.seconds >= 60).length} ko'rdi` : `${g.people.length} video · ${g.people.filter((r) => r.seconds >= 60).length} ko'rdi`}</div>
              <div style={{ fontSize: 12, color: C.textMid, width: 70, textAlign: "right" }}>{g.opens} marta</div>
              <div style={{ fontSize: 12, fontWeight: 800, color: C.primary, width: 70, textAlign: "right" }}>{mins(g.seconds)}</div>
              <div style={{ fontSize: 11, color: C.textLight, width: 90, textAlign: "right" }}>{when(g.last)}</div>
            </div>
            {open === g.key && (
              <div style={{ background: C.bgSoft, borderRadius: 8, padding: "6px 12px", marginBottom: 8 }}>
                {g.people.sort((a, b) => b.seconds - a.seconds).map((r) => (
                  <div key={r.student_id + r.video_id} style={{ display: "flex", gap: 12, padding: "4px 0", fontSize: 12, color: C.textMid }}>
                    <div style={{ flex: 1, color: C.text }}>{by === "video" ? (r.student_name || r.student_email || r.student_id.slice(0, 8)) : (label[r.kind + ":" + r.ref_id] || "(o'chirilgan video)")}</div>
                    <div style={{ width: 90, textAlign: "right" }}><Badge sec={r.seconds}/></div>
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
      )}
    </div>
  );
}

// Variants the students actually worked on (answered questions), with when they started / last answered.
function WorkList({ work, open, setOpen }) {
  if (!work) return <div style={{ fontSize: 13, color: C.textMid }}>Yuklanmoqda...</div>;
  if (work.error) return <div style={{ ...card, color: C.danger, fontSize: 13 }}>Ma'lumot olinmadi ({work.error}). Migratsiya (admin_variant_activity) hali ishga tushirilmagan.</div>;
  if (!work.length) return <div style={{ ...card, fontSize: 13, color: C.textMid }}>Hali hech kim variant savollariga javob bermagan.</div>;
  const m = {};
  work.forEach((r) => {
    const g = (m[r.variant_id] ||= { key: r.variant_id, name: `${r.teacher_name} · ${r.variant_number}-variant`, people: [], answered: 0, last: r.last_at });
    g.people.push(r); g.answered += r.answered;
    if (r.last_at > g.last) g.last = r.last_at;
  });
  const list = Object.values(m).sort((a, b) => b.people.length - a.people.length);
  return (
    <div style={card}>
      {list.map((g) => (
        <div key={g.key} style={{ borderBottom: `1px solid ${C.border}` }}>
          <div onClick={() => setOpen(open === g.key ? null : g.key)} style={{ display: "flex", alignItems: "center", gap: 12, padding: "9px 0", cursor: "pointer" }}>
            <div style={{ flex: 1, fontSize: 13, fontWeight: 700, color: C.text }}>{g.name}</div>
            <div style={{ fontSize: 12, color: C.textMid, width: 110, textAlign: "right" }}>{g.people.length} o'quvchi</div>
            <div style={{ fontSize: 12, color: C.textMid, width: 90, textAlign: "right" }}>{g.answered} javob</div>
            <div style={{ fontSize: 11, color: C.textLight, width: 90, textAlign: "right" }}>{when(g.last)}</div>
          </div>
          {open === g.key && (
            <div style={{ background: C.bgSoft, borderRadius: 8, padding: "6px 12px", marginBottom: 8 }}>
              {g.people.sort((a, b) => b.answered - a.answered).map((r) => (
                <div key={r.student_id} style={{ display: "flex", gap: 12, padding: "4px 0", fontSize: 12, color: C.textMid }}>
                  <div style={{ flex: 1, color: C.text }}>{r.student_name || r.student_email || r.student_id.slice(0, 8)}</div>
                  <div style={{ width: 110, textAlign: "right", fontWeight: 700 }}>{r.correct}/{r.answered} to'g'ri</div>
                  <div style={{ width: 170, textAlign: "right" }}>{when(r.first_at)} → {when(r.last_at)}</div>
                </div>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
