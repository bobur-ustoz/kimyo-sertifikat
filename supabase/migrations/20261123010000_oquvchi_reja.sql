-- Shaxsiy reja: har pullik o'quvchi mavzular ketma-ketligida qayerda turgani (api/_reja.js).
-- Murabbiy har ertalab shu jadvalga qarab ishlaydi: kirish testi, keyin har mavzuda dars, uyga vazifa, imtihon, keyingi mavzu.
-- Jadvalga faqat server (service role) kiradi: RLS yoqilgan, siyosat yo'q.
create table if not exists oquvchi_reja (
  student_id    uuid primary key references auth.users(id) on delete cascade,
  topic_id      uuid references topics(id) on delete set null,          -- joriy mavzu (reja tugagan bo'lsa bo'sh)
  bosqich       text not null default 'dars' check (bosqich in ('kirish','dars','vazifa','imtihon','tugadi')),
  vazifa_id     bigint references vazifalar(id) on delete set null,     -- joriy uyga vazifa yoki imtihon
  tugagan       uuid[] not null default '{}',                           -- tugatilgan mavzular (bilganlari ham shu yerda)
  bilgan        uuid[] not null default '{}',                           -- kirish testida bilgani aniqlangan mavzular
  kirish        jsonb,                                                  -- kirish testi natijasi: { "<topic_id>": [to'g'ri, jami] }
  boshlangan_at timestamptz not null default now(),                     -- joriy mavzu boshlangan vaqt
  eslatma_at    timestamptz,                                            -- "darsni ko'ring" eslatmasi ketgan vaqt
  updated_at    timestamptz not null default now()
);
alter table oquvchi_reja enable row level security;
