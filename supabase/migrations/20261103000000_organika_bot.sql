-- Organika bot (Telegram o'yin boti): o'quvchilar, savollar, progress, joriy urinish va javoblar jurnali.
-- Bu jadvallarga faqat service_role kiradi (api/organika-webhook.js). RLS yoqilgan, policy yo'q:
-- anon va authenticated foydalanuvchilar hech narsani ko'ra olmaydi.

create table ob_users (
  tg_id          bigint primary key,
  name           text not null default '',
  username       text,
  level          smallint check (level between 1 and 3),   -- kirish testidan keyin: 1 boshlang'ich, 2 o'rta, 3 kuchli
  xp             integer not null default 0,
  streak         integer not null default 0,
  last_play      date,                                      -- Asia/Tashkent bo'yicha oxirgi o'yin kuni
  linked_user_id uuid references auth.users(id) on delete set null,
  created_at     timestamptz not null default now()
);

create table ob_questions (
  id          serial primary key,
  chapter     smallint not null,                            -- 0 = kirish testi, 1..11 = boblar
  part        text not null check (part in ('intro','nomlanish','olinishi','xossa','boss','zanjir')),
  difficulty  smallint not null check (difficulty between 1 and 3),
  text        text not null,
  options     jsonb not null,                               -- 4 ta variant, tartibi tayyor
  correct     smallint not null check (correct between 0 and 3),
  explanation text not null default '',
  active      boolean not null default true,
  created_at  timestamptz not null default now()
);
create index ob_questions_part_idx on ob_questions (chapter, part) where active;
-- Seed qayta ishga tushirilsa savollar ko'payib ketmasligi uchun.
create unique index ob_questions_chapter_text_key on ob_questions (chapter, text);

create table ob_progress (
  tg_id      bigint not null references ob_users(tg_id) on delete cascade,
  chapter    smallint not null,
  stage      smallint not null,
  done       boolean not null default false,
  best_score smallint not null default 0,
  updated_at timestamptz not null default now(),
  primary key (tg_id, chapter, stage)
);

-- Har o'quvchining bitta faol urinishi. idx bo'yicha "compare-and-set" qilinadi,
-- shuning uchun Telegram update'ni qayta yuborsa ham javob ikki marta hisoblanmaydi.
create table ob_runs (
  tg_id      bigint primary key references ob_users(tg_id) on delete cascade,
  chapter    smallint not null,
  stage      smallint not null,
  q_ids      integer[] not null,
  idx        smallint not null default 0,
  correct    smallint not null default 0,
  hearts     smallint not null default 0,
  max_hearts smallint not null default 0,                   -- 0 = jon yo'q (kirish testi)
  started_at timestamptz not null default now()
);

-- Zaif mavzular va noto'g'ri savollarni aniqlash uchun.
create table ob_answers (
  id          bigserial primary key,
  tg_id       bigint not null references ob_users(tg_id) on delete cascade,
  question_id integer not null references ob_questions(id) on delete cascade,
  ok          boolean not null,
  created_at  timestamptz not null default now()
);
create index ob_answers_question_idx on ob_answers (question_id);
create index ob_answers_user_idx on ob_answers (tg_id, created_at desc);

alter table ob_users     enable row level security;
alter table ob_questions enable row level security;
alter table ob_progress  enable row level security;
alter table ob_runs      enable row level security;
alter table ob_answers   enable row level security;

-- XP atomik qo'shiladi (ikki so'rov bir vaqtda kelsa ham yo'qolmaydi).
create function public.ob_add_xp(p_tg bigint, p_xp integer)
returns integer
language sql security definer set search_path = public as $$
  update ob_users set xp = xp + p_xp where tg_id = p_tg returning xp;
$$;
revoke all on function public.ob_add_xp(bigint, integer) from public, anon, authenticated;
