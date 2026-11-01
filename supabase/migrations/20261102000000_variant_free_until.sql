-- A paid variant can be opened for everyone for a while (e.g. 24 hours). While free_until is in the
-- future the whole variant is open; afterwards it closes by itself, with no scheduled job.
alter table variants add column if not exists free_until timestamptz;
