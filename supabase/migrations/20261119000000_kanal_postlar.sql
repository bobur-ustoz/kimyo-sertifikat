-- Kanal postchisi: Telegram kanalga (t.me/KimyogarBobur) chiqadigan postlar navbati.
-- Post avval "qoralama" bo'ladi, ustoz tasdiqlagach "tasdiqlangan"; kron (keepalive?job=kanal) kuniga bitta
-- tasdiqlangan postni reja kuni kelganda yuboradi. Bu jadvalga faqat service_role kiradi. RLS yoqilgan, policy yo'q.

create table if not exists kanal_postlar (
  id         bigserial primary key,
  matn       text not null check (char_length(matn) between 1 and 4000),   -- Telegram HTML (b, i, a ...)
  rasm_url   text,                                                         -- bo'lsa rasm bilan yuboriladi
  imzo       boolean not null default true,                                -- oxiriga "Yordamchi bot | Telegram | Instagram" bloki
  reja_kuni  date not null,                                                -- Asia/Tashkent bo'yicha kun
  holat      text not null default 'qoralama'
             check (holat in ('qoralama','tasdiqlangan','yuborilmoqda','yuborildi','xato','bekor')),
  message_id bigint,                                                       -- kanaldagi xabar raqami
  xato       text,
  created_at timestamptz not null default now(),
  sent_at    timestamptz
);

create index if not exists kanal_postlar_navbat_idx on kanal_postlar (reja_kuni, id) where holat = 'tasdiqlangan';

alter table kanal_postlar enable row level security;
