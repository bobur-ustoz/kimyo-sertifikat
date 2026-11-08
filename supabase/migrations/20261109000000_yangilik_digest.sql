-- Premium o'quvchilarga kunlik "yangi narsalar" xabari (Telegram, sotuv boti orqali).
-- Har ishga tushish shu yerga yoziladi: keyingi xabar oxirgi yuborilgan paytdan keyingi yangiliklarni oladi,
-- shuning uchun bir narsa ikki marta yuborilmaydi. Faqat service_role kiradi (RLS yoqilgan, policy yo'q).
create table if not exists digest_runs (
  id         bigserial primary key,
  run_at     timestamptz not null default now(),
  items      jsonb not null default '[]',
  sent       integer not null default 0,
  failed     integer not null default 0
);
alter table digest_runs enable row level security;
