-- Organika jamoalari: qur'a (tasodifiy, kuchlari teng) bilan tuziladi. Hamma yozuv faqat server (service_role) orqali.
create table og_teams (
  id         serial primary key,
  season_id  integer not null references og_seasons(id) on delete cascade,
  name       text not null,
  created_at timestamptz not null default now(),
  unique (season_id, name)
);
alter table og_teams enable row level security;   -- policy yo'q: mijoz to'g'ridan-to'g'ri o'qiy olmaydi

alter table og_players add column if not exists team_id integer references og_teams(id) on delete set null;
create index if not exists og_players_team_idx on og_players (team_id);

-- Qur'a bir marta o'tkaziladi; natija o'zgartirilmaydi
alter table og_seasons add column if not exists teams_drawn_at timestamptz;
