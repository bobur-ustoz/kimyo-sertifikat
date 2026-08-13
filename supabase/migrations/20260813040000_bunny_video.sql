-- Bunny.net Stream video id per question, used with a signed embed-view
-- token so only paying/logged-in access is required (not a bare public URL).
alter table questions add column bunny_video_id text;
