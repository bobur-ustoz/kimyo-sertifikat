-- Per-variant paid access for videos.
--
-- Access rule (enforced server-side in api/bunny-token.js, mirrored in the UI):
--   1. the variant is marked free  -> anyone, guests included, may watch;
--   2. the student's plan is 'premium' -> everything is open;
--   3. the student has a 'paid' row in variant_purchases for that variant.
-- Everything else is locked.

alter table variants add column is_free boolean not null default false;
alter table variants add column price integer not null default 5000;

-- Every teacher keeps one full free variant: the lowest-numbered one.
update variants v set is_free = true
where v.variant_number = (
  select min(v2.variant_number) from variants v2 where v2.teacher_id = v.teacher_id
);

create table variant_purchases (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  variant_id uuid not null references variants(id) on delete cascade,
  amount integer not null default 5000,
  status text not null default 'pending' check (status in ('pending','paid','cancelled')),
  provider text not null default 'manual' check (provider in ('manual','click','payme')),
  provider_txn_id text,
  contact text,
  created_at timestamptz not null default now(),
  paid_at timestamptz,
  unique(student_id, variant_id)
);

create index variant_purchases_pending_idx on variant_purchases (status, created_at desc);

alter table variant_purchases enable row level security;

create policy "Students read own purchases" on variant_purchases for select
  using (auth.uid() = student_id);

-- A student may only ever file a *request*: pending, manual, no transaction id,
-- and at the variant's real price. Marking it paid is an admin or payment-webhook
-- action -- never something the browser can do on its own.
create policy "Students request purchase" on variant_purchases for insert
  with check (
    auth.uid() = student_id
    and status = 'pending'
    and provider = 'manual'
    and provider_txn_id is null
    and amount = (select price from variants where id = variant_id)
  );

-- Students may withdraw a request they have not paid for yet, nothing else.
create policy "Students cancel own pending" on variant_purchases for delete
  using (auth.uid() = student_id and status = 'pending');

create policy "Admin read purchases" on variant_purchases for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admin write purchases" on variant_purchases for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

-- Keep the rule true for teachers added later: the first variant a teacher gets
-- becomes their free one automatically, so no teacher is ever fully locked.
create function public.first_variant_is_free()
returns trigger as $$
begin
  if not exists (select 1 from variants where teacher_id = new.teacher_id and is_free) then
    new.is_free := true;
  end if;
  return new;
end;
$$ language plpgsql security definer set search_path = public;

create trigger variants_first_is_free
  before insert on variants
  for each row execute procedure public.first_variant_is_free();
