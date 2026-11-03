import { createClient } from "@supabase/supabase-js";
const a = createClient(process.env.VITE_SUPABASE_URL||process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, {auth:{persistSession:false}});
const { data:v } = await a.from("variants").select("id,variant_number").eq("teacher_id","a0905cf4-7164-4381-b3d1-750faa9307ae");
const vm=Object.fromEntries(v.map(x=>[x.id,x.variant_number]));
const { data:p } = await a.from("variant_purchases").select("*").order("created_at",{ascending:false}).limit(15);
const off=5*3600e3, f=d=>d?new Date(new Date(d).getTime()+off).toISOString().slice(5,16).replace("T"," "):"-";
for (const x of p) {
  const { data:u } = await a.from("profiles").select("email").eq("id",x.student_id).maybeSingle();
  console.log(f(x.created_at), x.status, x.amount, x.variant_id?("2019 "+(vm[x.variant_id]||"?")+"-variant"):(x.plan_id||"live"), (u?.email||"").slice(0,28), "tg_msg", x.tg_message_id, "paid", f(x.paid_at));
}
