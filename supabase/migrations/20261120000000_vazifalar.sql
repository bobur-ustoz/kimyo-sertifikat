-- Uyga vazifa va imtihon (api/_vazifa.js). Ustoz tayinlaydi, o'quvchi platformada ishlaydi.
-- Jadvallarga faqat server (service role) kiradi: RLS yoqilgan, siyosat yo'q. Shunda o'quvchi natijani o'zi
-- yozolmaydi va boshqa o'quvchining vazifasini ko'rmaydi.
create table if not exists vazifalar (
  id         bigserial primary key,
  tur        text not null default 'uyga' check (tur in ('uyga','imtihon')),
  nom        text not null check (char_length(nom) between 2 and 120),
  mavzu      text not null default '',
  savollar   uuid[] not null,                       -- questions.id, o'quvchi ko'radigan tartibda
  muddat     timestamptz,
  created_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now()
);

create table if not exists vazifa_topshiriq (
  id              bigserial primary key,
  vazifa_id       bigint not null references vazifalar(id) on delete cascade,
  student_id      uuid not null references auth.users(id) on delete cascade,
  holat           text not null default 'berilgan' check (holat in ('berilgan','boshlangan','topshirilgan')),
  javoblar        jsonb not null default '{}'::jsonb,   -- { "<question_id>": "A" }
  togri           integer,
  jami            integer,
  tg_xabar_at     timestamptz,                          -- Telegramga xabar ketgan vaqt
  eslatma_at      timestamptz,                          -- muddat eslatmasi ketgan vaqt
  boshlangan_at   timestamptz,
  topshirilgan_at timestamptz,
  created_at      timestamptz not null default now(),
  unique (vazifa_id, student_id)
);
create index if not exists vazifa_topshiriq_student_idx on vazifa_topshiriq (student_id);
create index if not exists vazifalar_muddat_idx on vazifalar (muddat);

alter table vazifalar enable row level security;
alter table vazifa_topshiriq enable row level security;
