-- A finished live lesson can carry its recording (a Bunny Stream video the admin uploads).
alter table live_lessons add column if not exists recording_video_id text;
