-- The analog question/solution/answer of a topic example is a Premium feature, but topic_examples
-- is readable by everyone, so anyone who knew the API could pull the text. The analogs move to
-- their own table that only paid plans and admins can read.
create table if not exists topic_example_analogs (
  example_id uuid primary key references topic_examples(id) on delete cascade,
  analog_savol text,
  analog_yechim text,
  analog_javob text,
  updated_at timestamptz not null default now()
);

alter table topic_example_analogs enable row level security;

create policy "Paid plans and admins read topic analogs" on topic_example_analogs for select
  using (exists (
    select 1 from profiles p
    where p.id = auth.uid()
      and (p.is_admin or (p.plan <> 'free' and (p.plan_expires_at is null or p.plan_expires_at > now())))
  ));

create policy "Admin write topic analogs" on topic_example_analogs for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

-- Copy what is there now. The old columns stay until the new site code is live (step 2 below).
insert into topic_example_analogs (example_id, analog_savol, analog_yechim, analog_javob)
select id, analog_savol, analog_yechim, analog_javob from topic_examples
where analog_savol is not null or analog_yechim is not null or analog_javob is not null
on conflict (example_id) do nothing;
