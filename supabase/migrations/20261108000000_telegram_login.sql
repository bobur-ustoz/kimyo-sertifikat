-- Telegram orqali ro'yxatdan o'tish va kirish. Oqim:
--   1) sayt tg-login-start chaqiradi: kod (botga havolada) va brauzer sirining xeshi saqlanadi;
--   2) o'quvchi botda /start kirish_KOD bosadi va telefon raqamini ulashadi (Telegram raqamni tasdiqlaydi);
--   3) bot hisobni topadi yoki yaratadi va qatorga user_id yozadi;
--   4) sayt tg-login-poll bilan sir orqali bir martalik kirish tokenini oladi.
-- Faqat service_role kiradi (RLS yoqilgan, policy yo'q).

create table if not exists tg_logins (
  code        text primary key,                 -- botga havoladagi kod
  secret_hash text not null,                    -- brauzerdagi sirning sha256 si (havolani olgan begona kira olmasligi uchun)
  tg_id       bigint,                           -- bot kodni ochgan Telegram
  user_id     uuid references auth.users(id) on delete cascade,
  consumed    boolean not null default false,   -- kirish tokeni olingan
  expires_at  timestamptz not null,
  created_at  timestamptz not null default now()
);
create index if not exists tg_logins_tg_idx on tg_logins (tg_id) where consumed = false;
alter table tg_logins enable row level security;

-- Tasdiqlangan telefon raqami (ustoz bog'lanishi uchun). O'quvchi o'z profilini o'qiy oladi, yozishni faqat server qiladi.
alter table profiles add column if not exists phone text;
