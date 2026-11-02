-- Testimonials of the teacher's students. Public read (only published rows), admin writes.
-- Photos and proof images (certificate / message screenshot) live in a public bucket;
-- they are uploaded from the admin panel only.
create table if not exists testimonials (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  result text,                 -- e.g. "Milliy sertifikat 2025, kimyodan B2"
  quote text,
  photo_path text,
  proof_path text,             -- certificate or message screenshot
  video_url text,              -- YouTube / Telegram link
  verified boolean not null default false,   -- the owner has seen the proof
  published boolean not null default false,
  featured boolean not null default false,    -- shown in the home banner (up to 2)
  sort_order integer not null default 0,
  created_at timestamptz not null default now()
);

alter table testimonials enable row level security;

create policy "Public read published testimonials" on testimonials for select
  using (published);
create policy "Admin read all testimonials" on testimonials for select
  using (exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admin write testimonials" on testimonials for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('testimonials', 'testimonials', true, 5242880, array['image/jpeg', 'image/png', 'image/webp'])
on conflict (id) do update
  set public = true, file_size_limit = 5242880, allowed_mime_types = array['image/jpeg', 'image/png', 'image/webp'];

create policy "Admins upload testimonial images" on storage.objects for insert to authenticated
  with check (bucket_id = 'testimonials' and exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admins replace testimonial images" on storage.objects for update to authenticated
  using (bucket_id = 'testimonials' and exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admins delete testimonial images" on storage.objects for delete to authenticated
  using (bucket_id = 'testimonials' and exists (select 1 from profiles where id = auth.uid() and is_admin));
