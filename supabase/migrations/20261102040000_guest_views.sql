-- Views by people who are not signed in (free videos are open to guests). They are anonymous:
-- one row per (browser id, video). Only the admin can read them.
create table if not exists guest_views (
  device_id text not null,
  video_id text not null,
  kind text not null check (kind in ('question','topic','example','live')),
  ref_id uuid,
  device_kind text,
  opens integer not null default 0,
  seconds integer not null default 0,
  first_at timestamptz not null default now(),
  last_at timestamptz not null default now(),
  primary key (device_id, video_id)
);

alter table guest_views enable row level security;

create policy "Admins read guest views" on guest_views for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));

create or replace function track_guest_view(p_device text, p_video_id text, p_open boolean, p_seconds integer, p_ua text)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_kind text;
  v_ref uuid;
begin
  if p_device is null or length(p_device) < 8 or length(p_device) > 64 or p_video_id is null then return; end if;

  select 'question', id into v_kind, v_ref from questions where bunny_video_id = p_video_id limit 1;
  if v_kind is null then select 'example', id into v_kind, v_ref from topic_examples where bunny_video_id = p_video_id limit 1; end if;
  if v_kind is null then select 'topic', id into v_kind, v_ref from topics where bunny_video_id = p_video_id limit 1; end if;
  if v_kind is null then select 'live', id into v_kind, v_ref from live_lessons where recording_video_id = p_video_id limit 1; end if;
  if v_kind is null then return; end if;

  insert into guest_views (device_id, video_id, kind, ref_id, device_kind, opens, seconds)
  values (p_device, p_video_id, v_kind, v_ref, left(coalesce(p_ua, ''), 20),
          case when p_open then 1 else 0 end, greatest(0, least(coalesce(p_seconds, 0), 300)))
  on conflict (device_id, video_id) do update set
    opens = guest_views.opens + case when p_open then 1 else 0 end,
    seconds = guest_views.seconds + greatest(0, least(coalesce(p_seconds, 0), 300)),
    last_at = now();
end;
$$;

revoke all on function track_guest_view(text, text, boolean, integer, text) from public;
grant execute on function track_guest_view(text, text, boolean, integer, text) to anon, authenticated;
