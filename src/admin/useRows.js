import { useCallback, useEffect, useState } from "react";

// Every panel here did the same three things: run a Supabase query, hold the
// rows, and re-run it after a write. This is that pattern, written once.
//
//   const [teachers, reload] = useRows(() => supabase.from("teachers").select("*"));
//
// `deps` are the values the query reads (a variant id, a filter); pass them so
// the query re-runs when they change.
export function useRows(query, deps = []) {
  const [rows, setRows] = useState([]);
  const reload = useCallback(async () => {
    const { data } = await query();
    setRows(data || []);
  }, deps);
  useEffect(() => { reload(); }, [reload]);
  return [rows, reload];
}
