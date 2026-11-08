-- Mavzuga biriktiriladigan qo'shimcha materiallar: vizual video (Bunny) yoki PDF (saytdagi fayl).
-- Hamma o'qiy oladi (mavzu darsi kabi ochiq); yozish faqat service_role orqali.
create table if not exists topic_materials (
  id             uuid primary key default gen_random_uuid(),
  topic_id       uuid not null references topics(id) on delete cascade,
  kind           text not null check (kind in ('video','pdf')),
  title          text not null,
  bunny_video_id text,
  file_url       text,
  sort_order     integer not null default 0,
  created_at     timestamptz not null default now(),
  check ((kind = 'video' and bunny_video_id is not null) or (kind = 'pdf' and file_url is not null))
);
create index if not exists topic_materials_topic_idx on topic_materials (topic_id, sort_order);
alter table topic_materials enable row level security;
create policy "Public read topic_materials" on topic_materials for select using (true);

-- Alkanlar mavzusi: olinish sxemasi (3D vizual + PDF).
insert into topic_materials (topic_id, kind, title, bunny_video_id, file_url, sort_order)
select t.id, v.kind, v.title, v.vid, v.url, v.so
from topics t,
     (values ('video', 'Alkanlar olinish sxemasi (3D vizual)', '825ee954-b51c-418b-80cf-4ed4393c5e78', null, 1),
             ('pdf',   'Alkanlar olinish sxemasi (PDF)',        null, '/materiallar/alkan_olinishi_sxema.pdf', 2)) as v(kind, title, vid, url, so)
where t.name = 'Alkanlar';
