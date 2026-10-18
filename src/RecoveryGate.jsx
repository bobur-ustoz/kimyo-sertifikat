import { useEffect, useState } from "react";
import { supabase } from "./lib/supabaseClient";
import ResetPassword, { RESET_PATH } from "./ResetPassword";

// Supabase only redirects a recovery mail to an address that is on the
// project's allow-list; anything else silently falls back to the project's
// Site URL. That made the mailed link land on the home page and appear to do
// nothing. So instead of trusting one path, watch for the recovery token
// wherever it arrives -- the form then works with no dashboard setup at all.
const looksLikeRecovery = () =>
  window.location.pathname.startsWith(RESET_PATH) ||
  /type=recovery/.test(window.location.hash) ||
  new URLSearchParams(window.location.search).get("type") === "recovery";

export default function RecoveryGate({ children }) {
  const [recovering, setRecovering] = useState(looksLikeRecovery);

  useEffect(() => {
    // The PKCE flow hands over a ?code= instead of a marker we can read, so the
    // event is what confirms it in that case.
    const { data: sub } = supabase.auth.onAuthStateChange((event) => {
      if (event === "PASSWORD_RECOVERY") setRecovering(true);
    });
    return () => sub.subscription.unsubscribe();
  }, []);

  return recovering ? <ResetPassword/> : children;
}
