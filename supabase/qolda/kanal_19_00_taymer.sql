-- Kanal postini har kuni aniq 19:00 da (Toshkent) chiqarish: Supabase taymeri saytni chaqiradi.
-- Hech narsa almashtirilmaydi, shu holatda ishga tushiriladi. Kalit bazaning o'zida yaratiladi va ko'rsatilmaydi;
-- uni faqat server o'qiydi (RLS yoqilgan, siyosat yo'q). Bu kalit faqat kunlik kanal postini ochadi (api/keepalive.js).
-- Vercel'ning 20:00 dagi kechki ishi zaxira bo'lib qoladi: post kuniga bir marta chiqadi (api/_kanal.js o'zi tekshiradi).

create extension if not exists pg_cron;
create extension if not exists pg_net;

create table if not exists ichki_kalit (
  nom    text primary key,
  qiymat text not null default replace(gen_random_uuid()::text || gen_random_uuid()::text, '-', '')
);
alter table ichki_kalit enable row level security;
insert into ichki_kalit (nom) values ('kanal') on conflict (nom) do nothing;

select cron.schedule(
  'kanal-19-00',
  '0 14 * * *',            -- 14:00 UTC = 19:00 Toshkent
  $$
  select net.http_get(
    url := 'https://kimyo-sertifikat.vercel.app/api/keepalive?job=kanal',
    headers := jsonb_build_object('Authorization', 'Bearer ' || (select qiymat from ichki_kalit where nom = 'kanal')),
    timeout_milliseconds := 30000
  );
  $$
);

-- Tekshirish:   select jobname, schedule, active from cron.job;
-- Natijalar:    select status_code, content, created from net._http_response order by created desc limit 5;
-- O'chirish:    select cron.unschedule('kanal-19-00');
