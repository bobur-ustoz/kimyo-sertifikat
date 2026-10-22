-- AI questions can now also be asked about a variant question's video (DTM / Milliy
-- Sertifikat), so the saved answers need to point at the question they belong to.
alter table video_questions
  add column if not exists question_id uuid references questions(id) on delete cascade;

create index if not exists video_questions_question_cache_idx
  on video_questions (question_id, question_norm);
