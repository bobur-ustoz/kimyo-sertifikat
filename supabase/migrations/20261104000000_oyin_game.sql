-- Organika veb o'yini: 24 kunlik mavsum. Hamma jadval faqat server (service_role) orqali yoziladi.
-- Savollar bankida to'g'ri javoblar `secret` ustunida: u hech qachon mijozga o'qish uchun berilmaydi
-- (RLS yoqilgan, o'quvchilar uchun policy yo'q). O'quvchi o'z progressini ko'ra oladi (og_players, og_daily_sets).
-- Telegram boti jadvallaridan (ob_*) alohida: bular saytdagi hisob (auth.users) bilan ishlaydi.

create table og_days (
  day        smallint primary key check (day between 1 and 24),
  topic      text not null,
  substances text[] not null default '{}'          -- shu kunning majburiy moddalari
);

-- Bitta savol varianti. Bir o'rin (day, slot) ning 2–3 ta varianti bor, o'quvchiga bittasi tushadi.
create table og_questions (
  id           text primary key,                    -- masalan 'd01-ou-3-2'
  day          smallint not null references og_days(day) on delete cascade,
  slot         text not null,
  variant      smallint not null,
  grp          text not null,                       -- bosqich guruhi: 'Olinish: umumiy', ...
  type         text not null check (type in ('choice','build','write')),
  lvl          smallint not null check (lvl between 1 and 3),
  bundle       text,                                -- zanjir to'plami (A, B), bog'langan o'rinlar uchun
  bundle_group text,
  public       jsonb not null,                      -- mijozga boradigan qism: matn, rasm, zanjir ko'rsatkichi
  secret       jsonb not null,                      -- javob kaliti: ok/no, re/pr/ans, build. FAQAT server
  explanation  text not null,
  trap         jsonb,                               -- { opt, why }: tuzoq variant (faqat choice)
  uses         text[] not null default '{}',        -- bu variantda qatnashadigan majburiy moddalar
  active       boolean not null default true,
  unique (day, slot, variant)
);
create index og_questions_day_idx on og_questions (day) where active;

create table og_seasons (
  id         serial primary key,
  name       text not null,
  starts_on  date not null,                         -- 1-kun (Toshkent vaqti bilan)
  days       smallint not null default 24,
  status     text not null default 'planned' check (status in ('planned','active','finished'))
);

-- O'quvchining mavsumdagi holati
create table og_players (
  user_id     uuid not null references auth.users(id) on delete cascade,
  season_id   integer not null references og_seasons(id) on delete cascade,
  joined_on   date not null default current_date,
  xp          integer not null default 0 check (xp >= 0),         -- umumiy XP hech qachon kamaymaydi
  rank_points integer not null default 0 check (rank_points >= 0),-- reyting balli, 0 dan pastga tushmaydi
  streak      integer not null default 0,
  last_day    smallint,
  shields     smallint not null default 0,
  primary key (user_id, season_id)
);

-- O'quvchining kunlik to'plami: server shu kun uchun bir marta tuzadi va saqlaydi (qayta yuklasa ham o'sha)
create table og_daily_sets (
  user_id      uuid not null,
  season_id    integer not null,
  day          smallint not null,
  items        jsonb not null,                      -- [{ id, review, fromDay, order }]
  stakes_used  smallint not null default 0 check (stakes_used between 0 and 2),
  trap_hit     boolean not null default false,
  status       text not null default 'open' check (status in ('open','done')),
  created_at   timestamptz not null default now(),
  completed_at timestamptz,
  primary key (user_id, season_id, day),
  foreign key (user_id, season_id) references og_players(user_id, season_id) on delete cascade
);

-- Har javob. (user, mavsum, kun, pozitsiya) bo'yicha yagona: bir savolga ikki marta hisob yozilmaydi.
create table og_answers (
  id          bigserial primary key,
  user_id     uuid not null,
  season_id   integer not null,
  day         smallint not null,
  position    smallint not null,
  question_id text not null references og_questions(id),
  ok          boolean not null,
  stake       boolean not null default false,
  trap_hit    boolean not null default false,
  xp          integer not null default 0,
  rank        integer not null default 0,
  ms          integer,                               -- javobga ketgan vaqt (gumonli tezlikni aniqlash uchun)
  created_at  timestamptz not null default now(),
  unique (user_id, season_id, day, position),
  foreign key (user_id, season_id, day) references og_daily_sets(user_id, season_id, day) on delete cascade
);
create index og_answers_question_idx on og_answers (question_id);
create index og_answers_user_idx on og_answers (user_id, created_at desc);

alter table og_days       enable row level security;
alter table og_questions  enable row level security;   -- policy yo'q: javoblar mijozga ko'rinmaydi
alter table og_seasons    enable row level security;
alter table og_players    enable row level security;
alter table og_daily_sets enable row level security;
alter table og_answers    enable row level security;

-- O'quvchi faqat o'z holatini o'qiy oladi; yozish faqat server orqali
create policy "O'quvchi o'z holatini ko'radi" on og_players for select using (auth.uid() = user_id);
create policy "O'quvchi o'z to'plamlarini ko'radi" on og_daily_sets for select using (auth.uid() = user_id);
create policy "O'quvchi o'z javoblarini ko'radi" on og_answers for select using (auth.uid() = user_id);
create policy "Mavsumlar hammaga ochiq" on og_seasons for select using (true);
create policy "Kunlar ro'yxati hammaga ochiq" on og_days for select using (true);
-- og_days.substances ham ochiq (bu faqat majburiy moddalar ro'yxati, javob emas)
