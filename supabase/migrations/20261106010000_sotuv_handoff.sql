-- Sotuv boti: to'liq uzatishdan keyin AI o'zi qaytishi va "yetkazildi" xabarini takrorlamaslik uchun.
alter table sotuv_leads add column if not exists handoff_at timestamptz;   -- to'liq uzatilgan payt
alter table sotuv_leads add column if not exists ack_at timestamptz;       -- oxirgi "yetkazildi" xabari
