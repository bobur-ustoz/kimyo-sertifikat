-- Survey: a student marks which questions of a variant were hard for them. One row per
-- (student, question); the admin reads all rows to see which questions need a closer look.
create table if not exists question_votes (
  student_id uuid not null references auth.users(id) on delete cascade,
  question_id uuid not null references questions(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (student_id, question_id)
);

alter table question_votes enable row level security;

create policy "Students read own votes" on question_votes for select using (auth.uid() = student_id);
create policy "Students add own votes" on question_votes for insert with check (auth.uid() = student_id);
create policy "Students remove own votes" on question_votes for delete using (auth.uid() = student_id);
create policy "Admins read all votes" on question_votes for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));
