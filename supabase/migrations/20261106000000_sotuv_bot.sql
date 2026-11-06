-- Sotuv boti (Telegram): lidlar va suhbat jurnali. Bu jadvallarga faqat service_role kiradi
-- (api/organika-webhook.js?bot=sotuv). RLS yoqilgan, policy yo'q: anon va authenticated hech narsani ko'ra olmaydi.

create table if not exists sotuv_leads (
  tg_id          bigint primary key,
  name           text not null default '',
  username       text,
  source         text,                                         -- /start parametri, masalan "ig_valent"
  stage          text not null default 'new'
                 check (stage in ('new','chatting','offered','handoff','stopped')),
  human          boolean not null default false,               -- true: ustoz o'zi javob beradi, AI jim
  handoff_reason text,
  last_update_id bigint not null default 0,                    -- Telegram qayta yuborsa ikki marta javob bermaslik uchun
  msg_day        date,                                         -- Asia/Tashkent bo'yicha kun
  msg_count      integer not null default 0,                   -- shu kundagi xabarlar (xarajatni cheklash)
  linked_user_id uuid references auth.users(id) on delete set null,
  created_at     timestamptz not null default now(),
  last_msg_at    timestamptz not null default now()
);

create table if not exists sotuv_messages (
  id         bigserial primary key,
  tg_id      bigint not null references sotuv_leads(tg_id) on delete cascade,
  role       text not null check (role in ('user','assistant')),
  content    text not null,
  created_at timestamptz not null default now()
);
create index if not exists sotuv_messages_tg_idx on sotuv_messages (tg_id, id desc);

alter table sotuv_leads enable row level security;
alter table sotuv_messages enable row level security;
