-- Admin paneldan mavzu materiallarini (vizual video, PDF) yuklash va o'chirish.
-- PDF fayllar ochiq "materiallar" bucket'ida saqlanadi (o'qish hamma uchun, yozish faqat admin).
create policy "Admin write topic_materials" on topic_materials for all
  using (exists (select 1 from profiles where id = auth.uid() and is_admin))
  with check (exists (select 1 from profiles where id = auth.uid() and is_admin));

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('materiallar', 'materiallar', true, 20971520, array['application/pdf'])
on conflict (id) do update set public = true, file_size_limit = 20971520, allowed_mime_types = array['application/pdf'];

create policy "Admin upload materiallar" on storage.objects for insert to authenticated
  with check (bucket_id = 'materiallar' and exists (select 1 from profiles where id = auth.uid() and is_admin));
create policy "Admin delete materiallar" on storage.objects for delete to authenticated
  using (bucket_id = 'materiallar' and exists (select 1 from profiles where id = auth.uid() and is_admin));
