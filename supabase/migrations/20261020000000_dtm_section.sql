-- Two sections on the student site: "Milliy Sertifikat" (teacher collections) and
-- "DTM" (state exam base questions by year). A DTM year reuses the teachers table
-- (name = "2019 yil"), so variants, questions, videos and purchases work unchanged.
alter table teachers add column if not exists section text not null default 'milliy'
  check (section in ('milliy', 'dtm'));
