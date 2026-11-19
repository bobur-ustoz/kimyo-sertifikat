-- O'quvchi murabbiyi: reja muddati haqidagi eslatma shu muddat uchun bir marta yuborilishi uchun belgi.
-- Qiymat: eslatma yuborilgan paytdagi profiles.plan_expires_at. O'quvchi rejani uzaytirsa muddat o'zgaradi va
-- keyingi safar yana bir marta eslatiladi.
alter table sotuv_leads add column if not exists reja_eslatma timestamptz;
