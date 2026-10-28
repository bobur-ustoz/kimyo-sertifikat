// Who may use the AI assistant / saved answers of a variant question: the same people
// who may watch its video (a free variant, a paid purchase, or an admin). The teacher's
// explanation is the paid content, so the assistant must not hand it out to everyone.
// A Premium plan that has not run out unlocks every variant (a null expiry = legacy, no end date).
export const premiumActive = (profile) =>
  profile?.plan === "premium" && (!profile.plan_expires_at || new Date(profile.plan_expires_at) > new Date());

// Any paid plan that has not run out (Premium, or a legacy Standart account).
export const paidPlanActive = (profile) =>
  !!profile?.plan && profile.plan !== "free" && (!profile.plan_expires_at || new Date(profile.plan_expires_at) > new Date());

export async function canUseQuestion(admin, userId, questionId) {
  const { data: q } = await admin.from("questions").select("variant_id, variants(is_free)").eq("id", questionId).maybeSingle();
  if (!q) return { ok: false, status: 404, error: "Savol topilmadi" };
  if (q.variants?.is_free) return { ok: true };
  const [{ data: profile }, { data: purchase }] = await Promise.all([
    admin.from("profiles").select("is_admin, plan, plan_expires_at").eq("id", userId).maybeSingle(),
    admin.from("variant_purchases").select("status").eq("student_id", userId).eq("variant_id", q.variant_id).maybeSingle(),
  ]);
  if (profile?.is_admin || premiumActive(profile) || purchase?.status === "paid") return { ok: true };
  return { ok: false, status: 403, error: "Bu variant hali sotib olinmagan" };
}
