-- Umumiy navbat: har bir agent (sotuv, nazoratchi, montaj, instagram, platforma ...) qilgan ishini,
-- topgan xatosini va ustozga savolini shu jadvalga yozadi. CEO hisoboti shu yerdan yig'iladi,
-- kod agenti esa o'ziga atalgan xatolarni shu yerdan oladi.
-- Bu jadvalga faqat service_role kiradi (api/_navbat.js va agentlar/navbat.mjs). RLS yoqilgan, policy yo'q.

create table if not exists agent_navbat (
  id         bigserial primary key,
  agent      text not null check (char_length(agent) between 2 and 40),      -- kim yozdi: "sotuv", "montaj" ...
  tur        text not null check (tur in ('ish','xato','savol','hisobot')),
  holat      text not null default 'yangi' check (holat in ('yangi','jarayonda','bajarildi','bekor')),
  sarlavha   text not null check (char_length(sarlavha) between 1 and 300),
  tafsilot   jsonb not null default '{}'::jsonb,
  kimga      text check (kimga is null or char_length(kimga) between 2 and 40), -- kim bajarishi kerak: "kod", "ustoz" ...
  kalit      text unique,                                                      -- bir xil yozuv ikki marta tushmasligi uchun
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists agent_navbat_vaqt_idx on agent_navbat (created_at desc);
create index if not exists agent_navbat_ochiq_idx on agent_navbat (kimga, holat) where holat in ('yangi','jarayonda');

alter table agent_navbat enable row level security;
