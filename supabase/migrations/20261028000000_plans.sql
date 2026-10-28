-- Paid plans (Standart 49 900 / Premium 250 000, 30 days each) bought through the same receipt + Telegram
-- approval flow as variants. A plan purchase is a variant_purchases row with plan_id set; when it turns
-- 'paid' (Telegram button or admin panel) a trigger switches the student's plan on for 30 days.
alter table profiles add column if not exists plan_expires_at timestamptz;

alter table variant_purchases add column if not exists plan_id text check (plan_id in ('standart','premium'));
alter table variant_purchases drop constraint if exists variant_purchases_one_target;
alter table variant_purchases add constraint variant_purchases_one_target
  check ((variant_id is not null)::int + (live_lesson_id is not null)::int + (plan_id is not null)::int = 1);
create unique index if not exists variant_purchases_plan_uq
  on variant_purchases (student_id, plan_id) where plan_id is not null;

create or replace function public.apply_plan_purchase() returns trigger
language plpgsql security definer set search_path = public as $$
declare cur text; cur_exp timestamptz;
begin
  if new.plan_id is null or new.status <> 'paid' or old.status = 'paid' then return new; end if;
  select plan, plan_expires_at into cur, cur_exp from profiles where id = new.student_id;
  -- buying Standart while Premium is still running must not downgrade the student
  if cur = 'premium' and new.plan_id = 'standart' and (cur_exp is null or cur_exp > now()) then return new; end if;
  update profiles set
    plan = new.plan_id,
    plan_expires_at = case when cur = new.plan_id and cur_exp > now() then cur_exp + interval '30 days' else now() + interval '30 days' end
  where id = new.student_id;
  return new;
end $$;

drop trigger if exists variant_purchases_apply_plan on variant_purchases;
create trigger variant_purchases_apply_plan after update of status on variant_purchases
  for each row execute function public.apply_plan_purchase();
