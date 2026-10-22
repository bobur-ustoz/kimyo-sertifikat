-- Text of the teacher's video for a variant question (DTM / Milliy Sertifikat).
-- Students never read it directly; it exists so the AI assistant can answer from
-- what the teacher actually said (same idea as video_transcripts for Mavzular).
create table if not exists question_transcripts (
  id uuid primary key default gen_random_uuid(),
  question_id uuid not null unique references questions(id) on delete cascade,
  content text not null,
  updated_at timestamptz not null default now()
);

alter table question_transcripts enable row level security;

create policy "Admin read question transcripts" on question_transcripts for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admin write question transcripts" on question_transcripts for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));
