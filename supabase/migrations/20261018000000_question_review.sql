-- Reviewed answer cache for the video assistant, plus a "moderator" role that may
-- only review those questions (not touch teachers, videos or payments).

alter table profiles add column if not exists is_moderator boolean not null default false;

alter table video_questions
  add column if not exists question_norm text,
  add column if not exists status text not null default 'auto'
    check (status in ('auto', 'approved', 'flagged')),
  add column if not exists hits integer not null default 0,
  add column if not exists reviewed_at timestamptz;

create index if not exists video_questions_cache_idx
  on video_questions (topic_id, example_id, question_norm);

create or replace function is_reviewer() returns boolean
  language sql stable security definer set search_path = public as $$
  select exists (select 1 from profiles where id = auth.uid() and (is_admin or is_moderator));
$$;

create policy "Reviewers read all video questions" on video_questions
  for select using (is_reviewer());
create policy "Reviewers update video questions" on video_questions
  for update using (is_reviewer()) with check (is_reviewer());
create policy "Reviewers delete video questions" on video_questions
  for delete using (is_reviewer());
