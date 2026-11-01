-- Admin-only: who worked on which variant (answered its questions), how many answers were right,
-- and when they started and last answered. Students can only read their own answers, so the
-- admin gets this through a function that checks is_admin itself.
create or replace function admin_variant_activity()
returns table (
  student_id uuid, student_email text, student_name text,
  variant_id uuid, teacher_name text, variant_number integer,
  answered integer, correct integer, first_at timestamptz, last_at timestamptz
)
language plpgsql
security definer
set search_path = public
as $$
begin
  if not exists (select 1 from profiles pr where pr.id = auth.uid() and pr.is_admin) then
    return;
  end if;
  return query
    select a.student_id, p.email, p.full_name, v.id, t.name, v.variant_number,
           count(*)::integer, (count(*) filter (where a.is_correct))::integer,
           min(a.answered_at), max(a.answered_at)
    from answers a
    join questions q on q.id = a.question_id
    join variants v on v.id = q.variant_id
    join teachers t on t.id = v.teacher_id
    left join profiles p on p.id = a.student_id
    group by a.student_id, p.email, p.full_name, v.id, t.name, v.variant_number;
end;
$$;

revoke all on function admin_variant_activity() from public;
grant execute on function admin_variant_activity() to authenticated;
