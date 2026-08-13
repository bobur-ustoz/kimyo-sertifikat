-- Shared answer-option pools for "matching" questions (e.g. 33-35 all pick
-- from the same A-F list).
create table option_groups (
  id uuid primary key default gen_random_uuid(),
  variant_id uuid not null references variants(id) on delete cascade,
  label text not null default '',
  options jsonb not null default '[]', -- [{"letter":"A","text":"364"}, ...]
  created_at timestamptz not null default now()
);

alter table option_groups enable row level security;
create policy "Public read option_groups" on option_groups for select using (true);
create policy "Admin write option_groups" on option_groups for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

-- Question types: 'mcq' (own A-D options, existing behaviour), 'open' (free
-- text, graded by AI against correct_answer_text), 'match' (points at a
-- shared option_group, correct_option is one of that group's letters).
alter table questions add column question_type text not null default 'mcq' check (question_type in ('mcq','open','match'));
alter table questions add column correct_answer_text text;
alter table questions add column option_group_id uuid references option_groups(id) on delete set null;

alter table questions drop constraint questions_correct_option_check;
alter table questions add constraint questions_correct_option_check check (correct_option is null or correct_option in ('A','B','C','D','E','F'));

-- Answers: allow a free-text response (open questions) alongside the
-- existing lettered one, and widen letters to A-F for matching questions.
alter table answers alter column selected_option drop not null;
alter table answers drop constraint answers_selected_option_check;
alter table answers add constraint answers_selected_option_check check (selected_option is null or selected_option in ('A','B','C','D','E','F'));
alter table answers add column selected_text text;
alter table answers add constraint answers_has_selection check (selected_option is not null or selected_text is not null);
