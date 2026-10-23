-- Paid live-lesson recordings: a lesson has a price (0 = free), and a purchase row may point
-- at a lesson instead of a variant. The Telegram approve/reject flow and the admin panel work
-- on variant_purchases rows, so recordings reuse that table rather than a parallel one.
alter table live_lessons add column if not exists price integer not null default 0;

alter table variant_purchases alter column variant_id drop not null;
alter table variant_purchases add column if not exists live_lesson_id uuid references live_lessons(id) on delete cascade;
alter table variant_purchases drop constraint if exists variant_purchases_one_target;
alter table variant_purchases add constraint variant_purchases_one_target
  check ((variant_id is not null)::int + (live_lesson_id is not null)::int = 1);
create unique index if not exists variant_purchases_lesson_uq
  on variant_purchases (student_id, live_lesson_id) where live_lesson_id is not null;
