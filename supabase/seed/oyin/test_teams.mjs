// node supabase/seed/oyin/test_teams.mjs
import { drawTeams, pickTeamForLate, teamCount, lateAllowed, TEAM_MAX } from "../../../api/_oyin/teams.js";
let bad = 0; const ok = (c, m) => { if (!c) { bad++; console.log("XATO:", m); } };
for (const n of [2, 3, 7, 10, 23, 40, 101]) {
  const players = Array.from({ length: n }, (_, i) => ({ user_id: "u" + i, xp: Math.floor(Math.random() * 400) }));
  const teams = drawTeams(players, { seed: 7 });
  const all = teams.flatMap((t) => t.members);
  ok(all.length === n && new Set(all).size === n, `n=${n}: har o'quvchi bitta jamoada bo'lishi kerak`);
  const sizes = teams.map((t) => t.members.length);
  ok(Math.max(...sizes) - Math.min(...sizes) <= 1, `n=${n}: hajm farqi 1 dan oshmasin ${sizes}`);
  ok(new Set(teams.map((t) => t.name)).size === teams.length, `n=${n}: nomlar takrorlanmasin`);
  const again = drawTeams(players, { seed: 7 });
  ok(JSON.stringify(again) === JSON.stringify(teams), `n=${n}: bir xil seed bir xil natija`);
  const other = drawTeams(players, { seed: 8 });
  if (n >= 10) ok(JSON.stringify(other) !== JSON.stringify(teams), `n=${n}: boshqa seed boshqa natija`);
  // kuch muvozanati: jamoalarning o'rtacha XP si bir-biridan juda farq qilmasin
  if (n >= 20) { const xp = Object.fromEntries(players.map((p) => [p.user_id, p.xp])); const avg = teams.map((t) => t.members.reduce((s, u) => s + xp[u], 0) / t.members.length);
    ok(Math.max(...avg) - Math.min(...avg) < 55, `n=${n}: jamoa o'rtachalari yaqin bo'lsin ${avg.map((x) => Math.round(x))}`); }
}
ok(teamCount(1) === 0 && teamCount(4) === 1 && teamCount(10) === 2 && teamCount(23) === 5, "teamCount");
ok(pickTeamForLate([{ id: 1, size: 5 }, { id: 2, size: 4 }, { id: 3, size: 6 }]) === 2, "eng kichik jamoa");
ok(pickTeamForLate([{ id: 1, size: TEAM_MAX }, { id: 2, size: TEAM_MAX }]) === null, "hammasi to'lsa null");
ok(lateAllowed(18) && !lateAllowed(19), "18-kun chegarasi");
// qatlamlilik: 20 o'quvchi, 4 jamoa: eng kuchli 4 tasi har xil jamoalarda
const strong = Array.from({ length: 20 }, (_, i) => ({ user_id: "s" + i, xp: 1000 - i }));
const t = drawTeams(strong, { seed: 3 });
const top4 = new Set(["s0", "s1", "s2", "s3"]);
ok(t.every((x) => x.members.filter((u) => top4.has(u)).length === 1), "eng kuchli to'rtlik har xil jamoaga tushsin");
console.log(bad ? `${bad} ta xato` : "HAMMASI TO'G'RI");
