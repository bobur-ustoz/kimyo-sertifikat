-- Distinguish casual per-video answers ("practice") from answers given
-- during a formal mixed-variant Test session ("test"). Analytics is
-- computed only from the "test" source, per product decision: the video
-- explains the solution, so answering right under it isn't a fair signal.
alter table answers add column source text not null default 'practice' check (source in ('practice','test'));

-- Superseded by the real variant-mixing Test Generator; drop the unused
-- AI-freeform-question tracking table from the earlier design.
drop table if exists adaptive_answers;
