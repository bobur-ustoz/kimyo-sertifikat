-- Live lessons: a schedule the admin manages, hosted in a Daily.co room that the
-- server creates on demand. Students get a short-lived meeting token from
-- /api/live-token only while the host has started the lesson.
create table live_lessons (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  description text,
  starts_at timestamptz not null,
  duration_min integer not null default 90,
  for_all boolean not null default false,          -- true: free plan may join too
  room_name text,
  status text not null default 'scheduled' check (status in ('scheduled','live','ended')),
  created_at timestamptz not null default now()
);

alter table live_lessons enable row level security;

create policy "Signed-in users read live lessons" on live_lessons for select
  using (auth.role() = 'authenticated');
create policy "Admins write live lessons" on live_lessons for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));
