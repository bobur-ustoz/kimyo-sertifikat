-- Who watched which video. One row per (student, video): how many times it was opened and how
-- many seconds were actually played. Written only through track_video_view(), which works out
-- what the video belongs to on the server, so a student cannot invent rows.
create table if not exists video_views (
  student_id uuid not null references auth.users(id) on delete cascade,
  video_id text not null,
  kind text not null check (kind in ('question','topic','example','live')),
  ref_id uuid,
  student_email text,
  student_name text,
  opens integer not null default 0,
  seconds integer not null default 0,
  first_at timestamptz not null default now(),
  last_at timestamptz not null default now(),
  primary key (student_id, video_id)
);

create index if not exists video_views_ref_idx on video_views (kind, ref_id);

alter table video_views enable row level security;

create policy "Admins read all video views" on video_views for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));

create or replace function track_video_view(p_video_id text, p_open boolean, p_seconds integer)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_kind text;
  v_ref uuid;
  v_email text;
  v_name text;
begin
  if auth.uid() is null or p_video_id is null then return; end if;

  select 'question', id into v_kind, v_ref from questions where bunny_video_id = p_video_id limit 1;
  if v_kind is null then select 'example', id into v_kind, v_ref from topic_examples where bunny_video_id = p_video_id limit 1; end if;
  if v_kind is null then select 'topic', id into v_kind, v_ref from topics where bunny_video_id = p_video_id limit 1; end if;
  if v_kind is null then select 'live', id into v_kind, v_ref from live_lessons where recording_video_id = p_video_id limit 1; end if;
  if v_kind is null then return; end if;

  select email, full_name into v_email, v_name from profiles where id = auth.uid();

  insert into video_views (student_id, video_id, kind, ref_id, student_email, student_name, opens, seconds)
  values (auth.uid(), p_video_id, v_kind, v_ref, v_email, v_name,
          case when p_open then 1 else 0 end, greatest(0, least(coalesce(p_seconds, 0), 300)))
  on conflict (student_id, video_id) do update set
    opens = video_views.opens + case when p_open then 1 else 0 end,
    seconds = video_views.seconds + greatest(0, least(coalesce(p_seconds, 0), 300)),
    student_email = coalesce(excluded.student_email, video_views.student_email),
    student_name = coalesce(excluded.student_name, video_views.student_name),
    last_at = now();
end;
$$;

revoke all on function track_video_view(text, boolean, integer) from public;
grant execute on function track_video_view(text, boolean, integer) to authenticated;
