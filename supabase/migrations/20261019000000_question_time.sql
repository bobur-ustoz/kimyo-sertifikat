-- Where in the video a reviewed question belongs (seconds), so the student page
-- can offer the questions that match the minute they are watching.
alter table video_questions add column if not exists video_seconds integer;
