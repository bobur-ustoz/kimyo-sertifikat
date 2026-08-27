-- The parts of the paid-access work that were deferred while the first
-- migration was being typed into the SQL editor by hand. None of them change
-- who can see what; they close smaller gaps and keep the rule true over time.

-- Free-variant rule for teachers whose numbering does not start at 1.
update variants v set is_free = true
where not exists (select 1 from variants w where w.teacher_id = v.teacher_id and w.is_free)
  and v.variant_number = (select min(variant_number) from variants w where w.teacher_id = v.teacher_id);

-- ...and for teachers added later: their first variant becomes the free one,
-- so no teacher is ever fully locked.
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

-- The admin panel lists pending requests newest first.
create index variant_purchases_pending_idx on variant_purchases (status, created_at desc);

-- Keep provider values to the ones the code knows about.
alter table variant_purchases add constraint variant_purchases_provider_check
  check (provider in ('manual','click','payme'));

-- A student may withdraw a request they have not paid for yet, nothing else.
create policy "Students cancel own pending" on variant_purchases for delete
  using (auth.uid() = student_id and status = 'pending');
