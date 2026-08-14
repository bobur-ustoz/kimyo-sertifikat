-- Answers to AI-generated Adaptive Test Generator questions. These have no
-- fixed question_id (they're generated fresh each time), so topic is stored
-- directly; analytics combines this with the regular `answers` table.
create table adaptive_answers (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  topic text not null,
  question_text text not null,
  is_correct boolean not null,
  created_at timestamptz not null default now()
);

alter table adaptive_answers enable row level security;

create policy "Students read own adaptive answers" on adaptive_answers for select using (auth.uid() = student_id);
create policy "Students insert own adaptive answers" on adaptive_answers for insert with check (auth.uid() = student_id);
