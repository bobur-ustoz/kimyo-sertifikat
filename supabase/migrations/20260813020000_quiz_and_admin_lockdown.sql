-- 1) Lock down content writes to admins only (previously any authenticated user,
--    including regular students, could write teachers/variants/questions).
alter table profiles add column is_admin boolean not null default false;

update profiles set is_admin = true
where id = (select id from auth.users where email = 'boburvaydiev853@gmail.com');

drop policy "Admin write teachers" on teachers;
drop policy "Admin write variants" on variants;
drop policy "Admin write questions" on questions;

create policy "Admin write teachers" on teachers for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admin write variants" on variants for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admin write questions" on questions for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

-- 2) Multiple-choice answers per question.
alter table questions add column option_a text;
alter table questions add column option_b text;
alter table questions add column option_c text;
alter table questions add column option_d text;
alter table questions add column correct_option text check (correct_option in ('A','B','C','D'));

-- 3) Student answers, one row per student per question (re-answering overwrites).
create table answers (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  question_id uuid not null references questions(id) on delete cascade,
  selected_option text not null check (selected_option in ('A','B','C','D')),
  is_correct boolean not null,
  answered_at timestamptz not null default now(),
  unique(student_id, question_id)
);

alter table answers enable row level security;

create policy "Students read own answers" on answers for select using (auth.uid() = student_id);
create policy "Students insert own answers" on answers for insert with check (auth.uid() = student_id);
create policy "Students update own answers" on answers for update using (auth.uid() = student_id) with check (auth.uid() = student_id);
