-- Variant purchases confirmed from Telegram: the student uploads a receipt photo,
-- the admin gets it in the bot chat with Approve / Reject buttons.
--
-- Requests are now created only by api/purchase-request.js (service role), which
-- demands the receipt. That is why the student insert policy is dropped: with it
-- in place a student could still file a request straight from the browser and
-- skip the receipt.

alter table variant_purchases
  add column if not exists proof_path text,
  add column if not exists reject_reason text,
  add column if not exists reviewed_by text,
  add column if not exists reviewed_at timestamptz,
  add column if not exists tg_chat_id bigint,
  add column if not exists tg_message_id bigint;

alter table variant_purchases drop constraint if exists variant_purchases_status_check;
alter table variant_purchases add constraint variant_purchases_status_check
  check (status in ('pending', 'paid', 'cancelled', 'rejected'));

drop policy if exists "Students request purchase" on variant_purchases;

-- Private bucket for receipts: nothing is public, size and type are enforced by
-- Storage itself.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('payment-proofs', 'payment-proofs', false, 5242880, array['image/jpeg', 'image/png', 'image/webp'])
on conflict (id) do update
  set public = false,
      file_size_limit = 5242880,
      allowed_mime_types = array['image/jpeg', 'image/png', 'image/webp'];

-- A student may upload only into their own folder (<user id>/...) and cannot
-- read, replace or delete anything afterwards.
create policy "Students upload own proofs" on storage.objects for insert to authenticated
  with check (bucket_id = 'payment-proofs' and (storage.foldername(name))[1] = auth.uid()::text);

-- Admins can open receipts from the panel; the Telegram side uses the service role.
create policy "Admins read proofs" on storage.objects for select to authenticated
  using (bucket_id = 'payment-proofs'
         and exists (select 1 from profiles where id = auth.uid() and is_admin));
