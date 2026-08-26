-- Per-variant paid access for videos.
--
-- Access rule (enforced server-side in api/bunny-token.js, mirrored in the UI):
--   1. the variant is marked free  -> anyone, guests included, may watch;
--   2. the student's plan is 'premium' -> everything is open;
--   3. the student has a 'paid' row in variant_purchases for that variant.
-- Everything else is locked.
--
-- This file records what was actually applied to the project database, typed in
-- by hand through the SQL editor. The extra hardening that was left out to keep
-- that typing manageable lives in the next migration.

alter table variants add column is_free boolean not null default false;
alter table variants add column price integer not null default 5000;

-- Open one variant per teacher. Applied as `where variant_number = 1`, which is
-- the same thing for the current data; the next migration generalises it.
update variants set is_free = true where variant_number = 1;

create table variant_purchases (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  variant_id uuid not null references variants(id) on delete cascade,
  amount integer not null default 5000,
  status text not null default 'pending' check (status in ('pending','paid','cancelled')),
  provider text not null default 'manual',
  provider_txn_id text,
  contact text,
  created_at timestamptz not null default now(),
  paid_at timestamptz,
  unique(student_id, variant_id)
);

alter table variant_purchases enable row level security;

create policy "Students read own purchases" on variant_purchases for select
  using (auth.uid() = student_id);

-- A student may only ever file a *request*: pending, at the variant's real
-- price. Marking it paid is an admin or payment-webhook action -- never
-- something the browser can do on its own, since there is no update policy.
create policy "Students request purchase" on variant_purchases for insert
  with check (
    auth.uid() = student_id
    and status = 'pending'
    and amount = (select price from variants where id = variant_id)
  );

create policy "Admin read purchases" on variant_purchases for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));

create policy "Admin write purchases" on variant_purchases for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));
