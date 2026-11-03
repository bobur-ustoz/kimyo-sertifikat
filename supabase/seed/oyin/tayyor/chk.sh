#!/bin/bash
# usage: chk.sh N [tail_lines] — validates tayyor/kun_NN against all earlier prepared days (1..N-1)
cd /Users/macbook/kimyo-sertifikat
O=supabase/seed/oyin/tayyor; N=$(printf %02d $1); args=("$O/kun_$N.json")
for i in $(seq 1 $(( $1 - 1 ))); do args+=("$O/kun_$(printf %02d $i).json"); done
node supabase/seed/oyin/check.mjs "${args[@]}" 2>&1 | tail -${2:-9}
