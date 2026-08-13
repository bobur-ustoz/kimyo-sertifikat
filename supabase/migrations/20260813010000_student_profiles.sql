-- Student accounts: one profile row per authenticated user, holding their subscription plan.
create table profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  full_name text,
  plan text not null default 'free' check (plan in ('free','standart','premium')),
  created_at timestamptz not null default now()
);

alter table profiles enable row level security;

create policy "Users read own profile" on profiles for select using (auth.uid() = id);
-- No client-side update policy: plan changes only happen via trusted server-side code
-- (e.g. a payment webhook using the service_role key), never directly from the browser.

-- Auto-create a profile row (defaulting to the free plan) whenever a new user signs up.
create function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, email) values (new.id, new.email);
  return new;
end;
$$ language plpgsql security definer set search_path = public;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
