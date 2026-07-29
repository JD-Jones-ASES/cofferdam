# Turn 17 — the q_max debit: X ≥ 7 everywhere, the staircase sharpens to 26/28/29

The fourth Sol Pro review (retained: `raw/2026-07-29-received-turn17-gpt-pro-
ryser-3.md`) found zero errors in our chain, owed and claimed no retractions in
either direction, and named a **large underclaim**: 0020's (SG) proof passes
through P + J ≤ R (J = Σ q_max(v)) before weakening J to H — our own turn-16
audit had flagged the same line. Mining it: (LD) P ≤ R − q₁(q₁+1); (DM)
d² ≤ 8d − 15 + 3[d=2] + f(f+2), an identity at d ≥ 5, summed to the EXACT
Ψ = m² − 43m + 2X + 15n − 3n₂ + n₄; (RG) |K_U| ≥ 2(6−k) − 1.

## Cert 0021 (63 + 5, green ×2): X ≥ 7 everywhere; X = 7/8/9 ⟹ m ≤ 26/28/29

45-cell X = 6 elimination (nine partitions × five rungs — parts-4 rows carried
so (q3) stays unconsumed) + five staircase rungs + a 142-cell belt. The
knapsack is cost-F/value-ψ, exhaustive: the f-for-F swap flips 15 raw cells
(named mutant), greedy-at-cap provably understates at C ≥ 7. Margins regress
honestly: three one-unit cells, and ONE ZERO-MARGIN cell — (23,(10,9)) clears
its moment requirement at exactly Ψ = Λ = 59 and dies only by the census-and-
profile count. (D2)+1 reopens 6 cells (measured after three intake lanes
returned three different answers); n ≥ 35 reopens 24; RG 5→4 reopens 2.

## Fleet record (9 + 5 lanes)

Both blind lemma lanes PROVED all five statements; the blind staircase lane's
GIVEN pack failed to load and it **rebuilt the whole chain from scratch** — an
unplanned fully-independent proof — and self-caught an unguarded shared-set
lemma that would have "proven" X = 6 ⟹ m ≤ 25 (the flattering direction,
guarded in-lane). Review defects, all stated-step not conclusion: the f/F cost
trap (§2 states f, §6 computes F — 15 cells flip under the literal reading);
the missing disjointness-by-C3 at (7,27) (the triangle ties at Ψ = Λ = 83
exactly — M-tri); the missing (SSC+) line in §4.2's high-cell step; the
missing K4 star-union proof; min-degree-2 unlisted though (DM) is false at
d ≤ 1; a greedy claim that is not a proof; one deflated row maximum (42 vs
48 — but see below). Cert audits ×3 PASS-WITH-FIXES, 29 findings, 0 refusals.

## Scars kept

The 0021 draft charged the review with a deflation over 42 — and 42 was
CORRECT for the branch as the cert itself defines it; the audit caught the
false charge and it was withdrawn before shipping (verify the frame before
the number). The spec's "15 flips" and the draft's "10" were BOTH right —
different layers of the same engine; the shipped cert measures and asserts
both. The (7,26) preview's survivor count is bound-dependent (two sharp,
three conservative) and is stated as such, not rounded to the review's two.

## Banked, not consumed

The adjacency-aware J-bound (kills (2,2,1,1,1)@(7,26) at 70 < 73; would
dissolve the (2,2,1,1) one-unit margin — certify before imposing) · the
guarded engine's bonus rungs (X = 9 ⟹ m ≤ 28; X = 10,11 ⟹ m ≤ 29; X = 12 ⟹
m ≤ 31 — one lane, unaudited) · the J-conjunction (debit + per-vertex charge
together).

## State after turn 17

**X ≥ 7 on every rung; X ≥ 8/9/10 from m = 27/29/30; X ≥ ⌈m(m−25)/38⌉;
5173 at the ceiling.** Twenty-one certs (twenty green ×2). Frontier: X = 7 on
m ∈ {22..26}, two-to-three shapes at m = 26. Four reviews, four theorems.
