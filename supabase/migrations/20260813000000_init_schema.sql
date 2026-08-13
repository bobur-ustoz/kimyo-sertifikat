-- Teachers, variants and questions for the Kimyo Sertifikat platform.
create table teachers (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  subject text not null,
  initials text not null,
  color text not null default '#0F5132',
  bg_color text not null default '#F0FDF4',
  rating numeric(2,1) not null default 5.0,
  students integer not null default 0,
  badge text,
  is_free boolean not null default true,
  description text not null default '',
  sort_order integer not null default 0,
  created_at timestamptz not null default now()
);

create table variants (
  id uuid primary key default gen_random_uuid(),
  teacher_id uuid not null references teachers(id) on delete cascade,
  variant_number integer not null,
  total_questions integer not null default 43,
  created_at timestamptz not null default now(),
  unique(teacher_id, variant_number)
);

create table questions (
  id uuid primary key default gen_random_uuid(),
  variant_id uuid not null references variants(id) on delete cascade,
  question_number integer not null,
  topic text not null default '',
  formula text not null default '',
  question_text text not null default '',
  video_url text,
  video_ready boolean not null default false,
  created_at timestamptz not null default now(),
  unique(variant_id, question_number)
);

alter table teachers enable row level security;
alter table variants enable row level security;
alter table questions enable row level security;

-- Public (anon) read access so the main site can display data.
create policy "Public read teachers" on teachers for select using (true);
create policy "Public read variants" on variants for select using (true);
create policy "Public read questions" on questions for select using (true);

-- Only authenticated (admin) users can write.
create policy "Admin write teachers" on teachers for all using (auth.role() = 'authenticated') with check (auth.role() = 'authenticated');
create policy "Admin write variants" on variants for all using (auth.role() = 'authenticated') with check (auth.role() = 'authenticated');
create policy "Admin write questions" on questions for all using (auth.role() = 'authenticated') with check (auth.role() = 'authenticated');
