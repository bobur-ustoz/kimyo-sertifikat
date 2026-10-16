-- Topic lessons: one topic video + a set of up to 20 worked-example videos,
-- each example with a text analog. Every video can carry a transcript that an
-- AI assistant answers student questions from.

create table topics (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  sort_order integer not null default 0,
  bunny_video_id text,
  created_at timestamptz not null default now()
);

create table topic_examples (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid not null references topics(id) on delete cascade,
  example_number integer not null check (example_number between 1 and 20),
  bunny_video_id text,
  analog_savol text,
  analog_yechim text,
  analog_javob text,
  created_at timestamptz not null default now(),
  unique (topic_id, example_number)
);

-- Transcripts live in their own table so students can never read them
-- directly; only admins (RLS) and the server (service role) can.
create table video_transcripts (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid references topics(id) on delete cascade,
  example_id uuid references topic_examples(id) on delete cascade,
  content text not null,
  updated_at timestamptz not null default now(),
  check ((topic_id is not null)::int + (example_id is not null)::int = 1)
);
create unique index video_transcripts_topic_uq on video_transcripts (topic_id) where topic_id is not null;
create unique index video_transcripts_example_uq on video_transcripts (example_id) where example_id is not null;

-- Student questions to the AI assistant, written by the server only.
create table video_questions (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  topic_id uuid references topics(id) on delete cascade,
  example_id uuid references topic_examples(id) on delete cascade,
  question text not null,
  answer text not null,
  created_at timestamptz not null default now()
);

alter table topics enable row level security;
alter table topic_examples enable row level security;
alter table video_transcripts enable row level security;
alter table video_questions enable row level security;

create policy "Public read topics" on topics for select using (true);
create policy "Admin write topics" on topics for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

create policy "Public read topic_examples" on topic_examples for select using (true);
create policy "Admin write topic_examples" on topic_examples for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

create policy "Admin all transcripts" on video_transcripts for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

create policy "Students read own video questions" on video_questions for select using (auth.uid() = student_id);
create policy "Admin read all video questions" on video_questions for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));

-- Seed topics from the free-text questions.topic values already in use.
insert into topics (name, sort_order)
select name, row_number() over (order by name) from (
  select distinct trim(topic) as name from questions where trim(coalesce(topic, '')) <> ''
) t;
