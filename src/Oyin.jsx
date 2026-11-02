import { useState, useEffect, useRef, useCallback } from "react";
import { Flame, Zap, X, Lock, CheckCircle2, FlaskConical } from "lucide-react";
import { supabase } from "./lib/supabaseClient";

// Organika: a free 24-day organic chemistry game. All checking happens on the server (api/oyin.js);
// this file only draws the questions it receives and sends the student's answer back.
// Three question types: choice (pick an option), write (type a reaction), build (assemble an alkane).

const G = { bg:"#EAF4EE", card:"#fff", ink:"#0F2F26", muted:"#5B7D70", line:"#D3E4DB", green:"#0C8E5E", greenD:"#086944", greenSoft:"#D8F2E6",
  sun:"#F5A400", sunD:"#B87800", sunSoft:"#FFF0CC", coral:"#E8434B", coralD:"#B02A31", coralSoft:"#FFE0E1", violet:"#6A55E0", violetSoft:"#E6E1FF" };

const CSS = `
.og{--bg:${G.bg};--card:${G.card};--ink:${G.ink};--muted:${G.muted};--line:${G.line};--green:${G.green};--green-d:${G.greenD};--green-soft:${G.greenSoft};--sun:${G.sun};--sun-d:${G.sunD};--sun-soft:${G.sunSoft};--coral:${G.coral};--coral-d:${G.coralD};--coral-soft:${G.coralSoft};--violet:${G.violet};--violet-soft:${G.violetSoft};
 background:var(--bg);color:var(--ink);font-family:'Nunito',system-ui,sans-serif;font-weight:700;font-size:16px;min-height:100%;padding:14px 16px 40px}
.og *{box-sizing:border-box}
.og button{font:inherit;color:inherit;cursor:pointer}
.og .wrap{max-width:460px;margin:0 auto;display:flex;flex-direction:column;gap:14px}
.og sub{font-size:.68em;line-height:0}
.og .top{display:flex;align-items:center;justify-content:space-between;gap:10px}
.og .brand{font:700 22px 'Fredoka',system-ui,sans-serif;display:flex;align-items:center;gap:8px}
.og .chips{display:flex;gap:8px}
.og .chip{display:flex;align-items:center;gap:5px;background:var(--card);border:2px solid var(--line);border-radius:99px;padding:5px 11px;font:600 15px 'Fredoka',system-ui,sans-serif}
.og .card{background:var(--card);border:2px solid var(--line);border-radius:20px;padding:14px}
.og .btn{display:block;width:100%;border:0;border-radius:16px;padding:14px 18px;background:var(--green);color:#fff;font:600 18px 'Fredoka',system-ui,sans-serif;letter-spacing:.3px;box-shadow:0 5px 0 var(--green-d);text-transform:uppercase}
.og .btn:active{transform:translateY(4px);box-shadow:0 1px 0 var(--green-d)}
.og .btn:disabled{opacity:.55}
.og .btn.ghost{background:var(--card);color:var(--ink);box-shadow:0 5px 0 var(--line);border:2px solid var(--line)}
.og .btn.no{background:var(--coral);box-shadow:0 5px 0 var(--coral-d)}
.og .day{display:flex;align-items:center;gap:12px;padding:12px;background:var(--card);border:2px solid var(--line);border-radius:18px;box-shadow:0 3px 0 var(--line);width:100%;text-align:left}
.og .dn{flex:none;width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font:700 18px 'Fredoka',system-ui,sans-serif;background:var(--line);color:var(--muted)}
.og .day.cur{border-color:var(--sun)} .og .day.cur .dn{background:var(--sun);color:#3B2800}
.og .day.done{background:var(--green-soft);border-color:var(--green)} .og .day.done .dn{background:var(--green);color:#fff}
.og .day b{font:600 18px 'Fredoka',system-ui,sans-serif;display:block}
.og .day span.s{font-size:13px;color:var(--muted)}
.og .qtop{display:flex;align-items:center;gap:12px}
.og .x{background:none;border:0;color:var(--muted);width:34px;height:34px;display:grid;place-items:center;border-radius:50%}
.og .segs{flex:1;display:flex;gap:3px}
.og .seg{flex:1;height:10px;border-radius:99px;background:var(--line)}
.og .seg.ok{background:var(--green)} .og .seg.no{background:var(--coral)} .og .seg.cur{background:var(--sun)}
.og .lvl{display:inline-block;font:600 12px 'Fredoka',system-ui,sans-serif;letter-spacing:.6px;text-transform:uppercase;padding:3px 10px;border-radius:99px;margin-right:6px}
.og .l1{background:var(--green-soft);color:var(--green)} .og .l2{background:var(--sun-soft);color:var(--sun-d)} .og .l3{background:var(--violet-soft);color:var(--violet)}
.og .rev{background:var(--violet-soft);color:var(--violet)}
.og .prompt{font:600 23px/1.25 'Fredoka',system-ui,sans-serif;margin:2px 0}
.og .stage{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:12px;display:grid;place-items:center;min-height:150px}
.og .stage svg{width:100%;max-width:340px;height:auto}
.og .opts{display:grid;gap:10px}
.og .opt{text-align:left;background:var(--card);border:2px solid var(--line);border-radius:16px;padding:13px 16px;font:700 17px 'Nunito',system-ui,sans-serif;box-shadow:0 4px 0 var(--line);display:flex;align-items:center;gap:12px}
.og .opt .k{flex:none;width:30px;height:30px;border-radius:9px;border:2px solid var(--line);display:grid;place-items:center;font:600 14px 'Fredoka',system-ui,sans-serif;color:var(--muted)}
.og .opt:active{transform:translateY(3px);box-shadow:0 1px 0 var(--line)}
.og .opt.ok{background:var(--green-soft);border-color:var(--green);box-shadow:0 4px 0 var(--green)}
.og .opt.no{background:var(--coral-soft);border-color:var(--coral);box-shadow:0 4px 0 var(--coral)}
.og .opt.dim{opacity:.55}
.og .stake{display:flex;align-items:center;gap:10px;font:600 15px 'Fredoka',system-ui,sans-serif;background:var(--violet-soft);color:var(--violet);border-radius:14px;padding:8px 12px}
.og .stake input{width:20px;height:20px}
.og .eqval{width:100%;min-height:70px;background:var(--bg);border:2px dashed var(--line);border-radius:14px;padding:12px;font:600 24px 'Fredoka',system-ui,sans-serif;text-align:center;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;overflow-wrap:anywhere;cursor:text}
.og .caret{display:inline-block;width:3px;height:24px;background:var(--green);margin-left:3px;animation:ogblink 1s steps(2) infinite}
@keyframes ogblink{50%{opacity:0}}
.og .kb{display:grid;grid-template-columns:repeat(8,1fr);gap:6px}
.og .key{border:2px solid var(--line);background:var(--card);border-radius:12px;height:44px;min-width:0;padding:0;font:600 16px 'Fredoka',system-ui,sans-serif;box-shadow:0 3px 0 var(--line)}
.og .key:active{transform:translateY(2px);box-shadow:0 1px 0 var(--line)}
.og .key.op{background:var(--green-soft);color:var(--green)} .og .key.del{background:var(--coral-soft);color:var(--coral)}
.og .key.arr{grid-column:span 3;background:var(--violet-soft);color:var(--violet)} .og .key.dot{grid-column:span 2}
.og .chain{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;font:600 15px 'Fredoka',system-ui,sans-serif;margin-bottom:8px}
.og .chain span{padding:3px 10px;border-radius:99px;border:2px solid var(--line)}
.og .chain span.on{background:var(--sun-soft);border-color:var(--sun);color:var(--sun-d)} .og .chain span.done{background:var(--green-soft);border-color:var(--green);color:var(--green)}
.og .sheet{position:sticky;bottom:0;margin:0 -16px;padding:16px;border-radius:24px 24px 0 0}
.og .sheet.ok{background:var(--green-soft);border-top:3px solid var(--green)} .og .sheet.no{background:var(--coral-soft);border-top:3px solid var(--coral)}
.og .sheet h3{margin:0 0 4px;font:600 22px 'Fredoka',system-ui,sans-serif} .og .sheet.ok h3{color:var(--green)} .og .sheet.no h3{color:var(--coral)}
.og .sheet p{margin:0 0 12px;font-size:15px;line-height:1.4}
.og .result{display:grid;gap:14px;justify-items:center;text-align:center;padding-top:20px}
.og .result h2{margin:0;font:700 28px 'Fredoka',system-ui,sans-serif}
.og .stats{display:grid;grid-template-columns:1fr 1fr;gap:10px;width:100%}
.og .stat{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:10px}
.og .stat b{display:block;font:700 26px 'Fredoka',system-ui,sans-serif} .og .stat span{font-size:13px;color:var(--muted)}
.og .hint{font-size:14px;color:var(--muted);text-align:center;line-height:1.4}
`;

// ---------- small renderers
const Lab = ({ s }) => s.split(/(\d+)/).filter(Boolean).map((t, i) =>
  /^\d+$/.test(t) ? <tspan key={i} dy="6" fontSize="15">{t}<tspan dy="-6">​</tspan></tspan> : <tspan key={i}>{t}</tspan>);

function MolSvg({ m }) {
  const r = 24;
  return (
    <svg viewBox="0 0 300 190" role="img" aria-label="Tuzilish formulasi">
      {m.b.map(([i, j], k) => { const A = m.a[i], B = m.a[j], dx = B[0] - A[0], dy = B[1] - A[1], L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
        return <line key={k} x1={A[0] + ux * r * 1.15} y1={A[1] + uy * r} x2={B[0] - ux * r * 1.15} y2={B[1] - uy * r} stroke={G.ink} strokeWidth="4" strokeLinecap="round" />; })}
      {m.a.map(([x, y, l], k) => <text key={k} x={x} y={y + 8} textAnchor="middle" fontFamily="Fredoka,system-ui,sans-serif" fontWeight="600" fontSize="24" fill={G.ink}><Lab s={l} /></text>)}
    </svg>
  );
}

// equation text with subscript digits: "2C3H7Cl+2Na→..." -> nodes
function Eq({ s }) {
  const out = []; let prev = "", sub = false, dec = false;
  [...s].forEach((ch, i) => {
    if (/\d/.test(ch)) { sub = !dec && (/[A-Za-z)]/.test(prev) || (sub && /\d/.test(prev))); out.push(sub ? <sub key={i}>{ch}</sub> : ch); }
    else if (ch === ",") { sub = false; dec = true; out.push(ch); }
    else { sub = false; dec = false; out.push(ch === "+" || ch === "→" ? <span key={i} style={{ color: G.muted }}> {ch} </span> : ch); }
    prev = ch;
  });
  return <>{out}</>;
}

function Tokens({ tk, cp }) {
  const out = []; let prev = "", sub = false, dec = false;
  tk.forEach((t, i) => {
    if (i === cp) out.push(<i key={"c" + i} className="caret" />);
    const isOp = t === "+" || t === "→";
    let h;
    if (/^\d$/.test(t)) { sub = !dec && (/[A-Za-z)]/.test(prev) || (sub && /\d/.test(prev))); h = sub ? <sub>{t}</sub> : t; }
    else if (t === ",") { sub = false; dec = true; h = t; }
    else { sub = false; dec = false; h = isOp ? <span style={{ color: G.muted, margin: "0 6px" }}>{t}</span> : t; }
    out.push(<span key={i} data-i={i}>{h}</span>);
    prev = t.slice(-1);
  });
  if (cp >= tk.length) out.push(<i key="end" className="caret" />);
  return <>{out}</>;
}

const KEYS = ["C","H","O","N","Cl","Br","Na","S","Al","Cu","Ag","Ca","Mg","K","Fe","I","1","2","3","4","5","6","7","8","9","0","+","→","(",")","⌫","✕","◀","▶",","];

function WriteInput({ q, onChange, locked }) {
  const [tk, setTk] = useState([]); const [cp, setCp] = useState(0);
  useEffect(() => { onChange(tk.join("")); }, [tk]);
  const press = (v) => {
    if (locked) return;
    if (v === "⌫") { if (cp > 0) { setTk((a) => a.filter((_, i) => i !== cp - 1)); setCp(cp - 1); } }
    else if (v === "✕") { setTk([]); setCp(0); }
    else if (v === "◀") setCp(Math.max(0, cp - 1));
    else if (v === "▶") setCp(Math.min(tk.length, cp + 1));
    else { setTk((a) => [...a.slice(0, cp), v, ...a.slice(cp)]); setCp(cp + 1); }
  };
  const clickVal = (e) => {
    if (locked) return;
    const t = e.target.closest("span[data-i]");
    if (!t) { setCp(tk.length); return; }
    const i = +t.dataset.i, r = t.getBoundingClientRect();
    setCp(e.clientX < r.left + r.width / 2 ? i : i + 1);
  };
  return (
    <>
      <div className="stage" style={{ display: "block" }}>
        {q.chain && <div className="chain">{q.chain.all.map((f, i) => <span key={i} className={i < q.chain.at ? "done" : i <= q.chain.at + 1 ? "on" : ""}><Eq s={f} /></span>)}</div>}
        <div className="eqval" onClick={clickVal}>{tk.length ? <Tokens tk={tk} cp={cp} /> : <span style={{ color: G.muted, fontSize: 16 }}>Reaksiyani klaviatura bilan yozing</span>}</div>
      </div>
      <div className="kb">{KEYS.map((k) => <button key={k} disabled={locked} onClick={() => press(k)} className={"key " + (/^[+→()]$/.test(k) ? "op" : k === "⌫" || k === "✕" ? "del" : k === "◀" || k === "▶" ? "arr" : k === "," ? "dot" : "")}>{k}</button>)}</div>
      <p className="hint">Raqamni o'rtaga qo'yish uchun yozuvga bosing yoki ◀ ▶ bilan kursorni suring.</p>
    </>
  );
}

// ---------- alkane builder: a chain (yellow +) and methyls on the inner carbons (+ beside a carbon)
const MAXC = 7;
const BP = (i) => [44 + i * 54, i % 2 ? 85 : 125];
function BuildInput({ onChange, locked }) {
  const [st, setSt] = useState({ n: 1, br: Array.from({ length: MAXC }, () => [0, 0]), h: [] });
  useEffect(() => { onChange({ n: st.n, br: st.br }); }, [st]);
  const ext = () => { if (locked || st.n >= MAXC) return; setSt((s) => ({ ...s, n: s.n + 1, h: [...s.h, ["e"]] })); };
  const slot = (i, k) => { if (locked) return; setSt((s) => { const br = s.br.map((r) => r.slice()); br[i][k] = br[i][k] ? 0 : 1; return { ...s, br, h: [...s.h, ["b", i, k]] }; }); };
  const undo = () => { if (locked) return; setSt((s) => { const a = s.h[s.h.length - 1]; if (!a) return s; const h = s.h.slice(0, -1);
    if (a[0] === "e") return { ...s, n: s.n - 1, h }; const br = s.br.map((r) => r.slice()); br[a[1]][a[2]] = br[a[1]][a[2]] ? 0 : 1; return { ...s, br, h }; }); };
  const n = st.n, r = 22, kinds = ["C", "CH", "CH2", "CH3", "CH4"];
  const bond = (A, B, key) => { const dx = B[0] - A[0], dy = B[1] - A[1], L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
    return <line key={key} x1={A[0] + ux * r} y1={A[1] + uy * r} x2={B[0] - ux * r} y2={B[1] - uy * r} stroke={G.ink} strokeWidth="4" strokeLinecap="round" />; };
  const txt = (p, l, col, key) => <text key={key} x={p[0]} y={p[1] + 8} textAnchor="middle" fontFamily="Fredoka,system-ui,sans-serif" fontWeight="600" fontSize="24" fill={col || G.ink}><Lab s={l} /></text>;
  const plus = (p, col, onClick, key) => (
    <g key={key} onClick={onClick} style={{ cursor: "pointer" }}>
      <circle cx={p[0]} cy={p[1]} r="20" fill="none" stroke={col} strokeWidth="2.5" strokeDasharray="4 5" />
      <path d={`M${p[0] - 8} ${p[1]}h16M${p[0]} ${p[1] - 8}v16`} stroke={col} strokeWidth="3" strokeLinecap="round" />
      <circle cx={p[0]} cy={p[1]} r="28" fill="transparent" />
    </g>);
  const els = [];
  for (let i = 0; i < n - 1; i++) els.push(bond(BP(i), BP(i + 1), "b" + i));
  for (let i = 0; i < n; i++) {
    const P = BP(i), deg = (i > 0 ? 1 : 0) + (i < n - 1 ? 1 : 0) + st.br[i][0] + st.br[i][1];
    if (i > 0 && i < n - 1) {
      const sl = i % 2 ? [[P[0] - 28, 34], [P[0] + 28, 34]] : [[P[0] - 28, 180], [P[0] + 28, 180]];
      sl.forEach((s, k) => {
        if (st.br[i][k]) els.push(bond(P, s, `s${i}${k}`), <g key={`m${i}${k}`} onClick={() => slot(i, k)} style={{ cursor: "pointer" }}><circle cx={s[0]} cy={s[1]} r="28" fill="transparent" />{txt(s, "CH3", G.green, "t")}</g>);
        else els.push(plus(s, G.muted, () => slot(i, k), `p${i}${k}`));
      });
    }
    els.push(txt(P, kinds[4 - deg], null, "c" + i));
  }
  if (n < MAXC) els.push(plus(BP(n), G.sunD, ext, "ext"));
  const W = Math.max(300, BP(n < MAXC ? n : n - 1)[0] + 50);
  return (
    <>
      <div className="stage"><svg viewBox={`0 0 ${W} 200`} role="img" aria-label="Molekula yig'ish maydoni">{els}</svg></div>
      <p className="hint">Avval sariq <b>+</b> bilan zanjirni uzaytiring, keyin uglerod yonidagi <b>+</b> bilan metil qo'shing.</p>
      <button className="btn ghost" disabled={locked || !st.h.length} onClick={undo}>Orqaga</button>
    </>
  );
}

// ---------- the question screen
function Question({ item, onAnswer, locked, result }) {
  const q = item.question;
  const [val, setVal] = useState(null);
  const [stake, setStake] = useState(false);
  const t0 = useRef(Date.now());
  useEffect(() => { t0.current = Date.now(); }, [q.id]);
  const send = (a) => onAnswer(a, stake, Date.now() - t0.current);
  const lvl = q.lvl || 1;
  return (
    <>
      <div><span className={"lvl l" + lvl}>{["", "1-daraja", "2-daraja", "3-daraja · qiyin"][lvl]}</span>{item.review && <span className="lvl rev">Takror</span>}</div>
      <div className="prompt" dangerouslySetInnerHTML={{ __html: q.p }} />
      {item.canStake && !locked && (
        <label className="stake"><input type="checkbox" checked={stake} onChange={(e) => setStake(e.target.checked)} /> Stavka: to'g'ri +20, xato −10 reyting</label>
      )}
      {q.type === "choice" && (
        <>
          {q.mol && <div className="stage"><MolSvg m={q.mol} /></div>}
          <div className="opts">
            {q.options.map((o, i) => {
              const cls = result ? (o === result.reveal.correct ? "ok" : o === result.chosen ? "no" : "dim") : "";
              return <button key={i} className={"opt " + cls} disabled={locked} onClick={() => send(o)}><span className="k">{"ABCD"[i]}</span><span dangerouslySetInnerHTML={{ __html: o }} /></button>;
            })}
          </div>
        </>
      )}
      {q.type === "write" && (<><WriteInput key={q.id} q={q} onChange={setVal} locked={locked} />
        <button className="btn" disabled={locked || !val} onClick={() => send(val)}>Tekshirish</button></>)}
      {q.type === "build" && (<><BuildInput key={q.id} onChange={setVal} locked={locked} />
        <button className="btn" disabled={locked || !val} onClick={() => send(val)}>Tekshirish</button></>)}
    </>
  );
}

export default function Oyin({ session, setTab }) {
  const [view, setView] = useState("home");       // home | quiz | result
  const [state, setState] = useState(null);       // { season, player, days }
  const [today, setToday] = useState(null);       // the day's set
  const [pos, setPos] = useState(0);
  const [res, setRes] = useState(null);           // result of the current answer
  const [fin, setFin] = useState(null);           // totals when the day is done
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");

  const call = useCallback(async (action, body = {}) => {
    const { data: { session: s } } = await supabase.auth.getSession();
    const r = await fetch("/api/oyin", { method: "POST", headers: { "Content-Type": "application/json", Authorization: `Bearer ${s?.access_token}` }, body: JSON.stringify({ action, ...body }) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || "Xatolik yuz berdi");
    return j;
  }, []);

  const loadState = useCallback(async () => {
    setErr("");
    try { setState(await call("state")); } catch (e) { setErr(e.message); }
  }, [call]);
  useEffect(() => { if (session) loadState(); }, [session?.user?.id]);

  const open = async (day) => {
    setBusy(true); setErr("");
    try {
      const t = await call("today", { day });
      setToday(t); setRes(null); setFin(null);
      const first = t.items.findIndex((i) => !i.answered);
      if (first === -1) { setFin({ correct: t.items.filter((i) => i.answered.ok).length, total: t.total, bonus: 0, done: true }); setView("result"); }
      else { setPos(first); setView("quiz"); }
    } catch (e) { setErr(e.message); }
    setBusy(false);
  };

  const answer = async (a, stake, ms) => {
    if (busy || res) return;
    setBusy(true);
    try {
      const item = today.items[pos];
      const r = await call("answer", { day: today.day, position: item.position, answer: a, stake, ms });
      setRes({ ...r, chosen: typeof a === "string" ? a : null });
      setToday((t) => ({ ...t, stakesUsed: t.stakesUsed + (stake && item.canStake ? 1 : 0),
        items: t.items.map((it, i) => i === pos ? { ...it, answered: { ok: r.ok, stake: !!(stake && item.canStake), xp: r.xp } } : it) }));
      setState((s) => s && { ...s, player: r.player });
    } catch (e) { setErr(e.message); }
    setBusy(false);
  };

  const next = () => {
    const nxt = today.items.findIndex((it, i) => i > pos && !it.answered);
    if (res.done || nxt === -1) { setFin({ correct: res.correct, total: res.total, bonus: res.bonus, done: true }); setView("result"); loadState(); }
    else { setPos(nxt); setRes(null); }
  };

  const wrap = (children) => <div className="og"><style>{CSS}</style><style>{"@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@600;700;800&display=swap');"}</style><div className="wrap">{children}</div></div>;

  if (!session) return wrap(<>
    <div className="top"><div className="brand"><FlaskConical size={24} /> Organika</div></div>
    <div className="card" style={{ textAlign: "center" }}>
      <div style={{ font: "600 22px Fredoka,system-ui,sans-serif", marginBottom: 6 }}>24 kunda organik kimyo</div>
      <p style={{ margin: "0 0 14px", color: G.muted, lineHeight: 1.5 }}>Har kuni yangi mavzu, 30 ta savol, ball va seriya. O'yin hamma uchun bepul. O'ynash uchun hisobingizga kiring.</p>
      <button className="btn" onClick={() => setTab("profile")}>Kirish / Ro'yxatdan o'tish</button>
    </div></>);

  const chips = state && <div className="chips"><div className="chip" style={{ color: G.coral }}><Flame size={17} />{state.player.streak}</div><div className="chip" style={{ color: G.sun }}><Zap size={17} />{state.player.xp}</div></div>;

  if (view === "quiz" && today) {
    const item = today.items[pos];
    return wrap(<>
      <div className="qtop">
        <button className="x" aria-label="Chiqish" onClick={() => { setView("home"); loadState(); }}><X size={22} /></button>
        <div className="segs">{today.items.map((it, i) => <div key={i} className={"seg " + (it.answered ? (it.answered.ok ? "ok" : "no") : i === pos ? "cur" : "")} />)}</div>
        <div className="chip" style={{ color: G.sun }}><Zap size={16} />{state?.player.xp ?? 0}</div>
      </div>
      {err && <div className="card" style={{ color: G.coral }}>{err}</div>}
      <Question key={item.question.id} item={item} onAnswer={answer} locked={!!res || busy} result={res} />
      {res && (
        <div className={"sheet " + (res.ok ? "ok" : "no")}>
          <h3>{res.ok ? "To'g'ri!" : "Hali emas"}{res.xp > 0 ? ` +${res.xp} XP` : ""}</h3>
          <p>
            {!res.ok && res.reveal.message && <>{res.reveal.message} </>}
            {!res.ok && res.reveal.got && <>Siz yig'gan modda: <b>{res.reveal.got}</b>. </>}
            {!res.ok && item.question.type === "write" && <>To'g'ri tenglama: <b><Eq s={res.reveal.correct} /></b><br /></>}
            {!res.ok && item.question.type === "build" && <>To'g'ri javob: <b>{res.reveal.correct.name}</b> ({res.reveal.correct.formula}).<br /></>}
            {res.stakeLost && <>Stavka yutqazildi: reyting −10. </>}{res.shieldUsed && <>Qalqon stavkani saqladi. </>}
            {res.trapHit && res.reveal.trapWhy && <><b>Tuzoq!</b> <span dangerouslySetInnerHTML={{ __html: res.reveal.trapWhy }} /><br /></>}
            <span dangerouslySetInnerHTML={{ __html: res.reveal.explanation }} />
          </p>
          <button className={"btn " + (res.ok ? "" : "no")} onClick={next}>{res.done ? "Tugatish" : "Davom"}</button>
        </div>
      )}
    </>);
  }

  if (view === "result" && fin) {
    return wrap(<div className="result">
      <CheckCircle2 size={90} color={G.green} />
      <h2>{today?.day}-kun tugadi!</h2>
      <div className="stats">
        <div className="stat"><b>{fin.correct}/{fin.total}</b><span>to'g'ri javob</span></div>
        <div className="stat"><b>{fin.bonus ? "+" + fin.bonus : "0"}</b><span>{fin.bonus ? "kunlik bonus" : "bonus (tuzoqqa tushildi)"}</span></div>
        <div className="stat"><b>{state?.player.xp ?? 0}</b><span>jami XP</span></div>
        <div className="stat"><b>{state?.player.streak ?? 0}</b><span>kun ketma-ket</span></div>
      </div>
      <button className="btn" onClick={() => { setView("home"); loadState(); }}>Kunlar ro'yxati</button>
    </div>);
  }

  return wrap(<>
    <div className="top"><div className="brand"><FlaskConical size={24} /> Organika</div>{chips}</div>
    {err && <div className="card" style={{ color: G.coral }}>{err}{" "}<button className="btn ghost" style={{ marginTop: 10 }} onClick={loadState}>Qayta urinish</button></div>}
    {!state && !err && <div className="hint">Yuklanmoqda…</div>}
    {state && (<>
      <div className="card"><b style={{ font: "600 19px Fredoka,system-ui,sans-serif" }}>24 kunlik mavsum</b>
        <div className="hint" style={{ textAlign: "left", marginTop: 4 }}>Har kuni yangi mavzu: 30 savol, taxminan 15 daqiqa. Bepul.</div></div>
      {state.days.length === 0 && <div className="hint">Savollar tez orada qo'shiladi.</div>}
      {state.days.map((d) => (
        <button key={d.day} className={"day " + (d.status === "done" ? "done" : d.open ? "cur" : "")} disabled={!d.open || busy} onClick={() => open(d.day)}>
          <span className="dn">{d.status === "done" ? <CheckCircle2 size={22} /> : d.open ? d.day : <Lock size={18} />}</span>
          <span><b>{d.day}-kun · {d.topic}</b><span className="s">{d.status === "done" ? "Tugatilgan, qayta ko'rish mumkin" : d.status === "open" ? "Davom ettiring" : d.open ? "30 savol" : "Hali ochilmagan"}</span></span>
        </button>))}
    </>)}
  </>);
}
