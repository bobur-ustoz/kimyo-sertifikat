-- O'quvchi hisobini Telegram bilan ulash (eslatmalar uchun). O'quvchi saytda "Telegramni ulash" tugmasini bosadi,
-- server bir martalik kod yaratadi, bot esa /start ulash_KOD orqali Telegram ID ni hisobga bog'laydi.
-- Jadvallarga faqat service_role kiradi (RLS yoqilgan, policy yo'q).

create table if not exists tg_link_codes (
  code       text primary key,
  user_id    uuid not null references auth.users(id) on delete cascade,
  expires_at timestamptz not null,
  used       boolean not null default false,
  created_at timestamptz not null default now()
);
alter table tg_link_codes enable row level security;

-- Ulangan lidga eslatmalar: remind=false bo'lsa /stop qilgan; last_nudge_at ko'p eslatma yubormaslik uchun.
alter table sotuv_leads add column if not exists remind boolean not null default true;
alter table sotuv_leads add column if not exists last_nudge_at timestamptz;

-- Bitta hisobga bitta Telegram.
create unique index if not exists sotuv_leads_linked_user_uq on sotuv_leads (linked_user_id) where linked_user_id is not null;
