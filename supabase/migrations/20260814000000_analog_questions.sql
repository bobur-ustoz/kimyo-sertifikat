-- AI-generated analog questions must be reviewed by an admin before any
-- student can see them (chemistry/math accuracy can't be auto-guaranteed).
create table analog_questions (
  id uuid primary key default gen_random_uuid(),
  question_id uuid not null references questions(id) on delete cascade,
  savol text not null,
  formula text,
  yechim jsonb not null default '[]',
  javob text not null,
  is_approved boolean not null default false,
  created_at timestamptz not null default now()
);

alter table analog_questions enable row level security;

create policy "Public read approved analogs" on analog_questions for select using (is_approved = true);
create policy "Admin read all analogs" on analog_questions for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admin write analogs" on analog_questions for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));
