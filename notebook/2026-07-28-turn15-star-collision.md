# Turn 15 — the star-collision inequality: X ≥ 5 everywhere, X = 5 confined to m ≤ 26

2026-07-28, same day as turn 14. The second Sol Pro review of the public repo
arrived through JD with **full proof text**: two proposed theorems (every core
has X ≥ 5; X = 5 forces m ≤ 26), a new structural lemma pair, and three
doc-defect claims. Intake per D-036, extended to the full-text case (now D-037).

## The two lemmas (derived in-cert, 0019 (L-f))

**(DH)** For z ∉ f: every z-edge meets f but not f's cell in z's own part
(part-mate exclusion), so d(z) edges land in ≤ 5 fibres; a ≤ 1 + C(a,2) per
fibre; the fibre-pair count equals Σ_pairs |e∩g∩f| ≤ Σ_pairs q (drop z). Hence
d(z) ≤ 5 + star_excess(z) ≤ 5 + X − x_f, and globally **Δ ≤ 5 + X**.

**(SC)** Summing over vertices and exchanging summation (a pair {e,g} is seen by
its λ = q+1 shared vertices): **D := Σ(d−5)₊ ≤ R := Σ q(q+1)**. Sharp (62/849
corpus equalities). D ≤ X is FALSE (r=3 witness, D = 2X); the λ factor is the
lemma.

## The engine

Moments Σd = 6m, ΣC(d,2) = C(m,2)+X; n ≥ 36; n₂ ≤ ⌊m/2⌋; branch degree caps
from (DH) off-f + (L-e) budgets on-f; D ≤ R with R capped by partition maxima.
Eight branches of X ≤ 4 across [22,456] + five rungs of X = 5: **3,056 census
runs, all empty.** X = 3's heavy branch is cut to m ≤ 25 by C3 before the old
m = 26 equality rung is ever reached (the audit's census argument was dead code;
kept as a triple-redundant tooth). Thin kills: m = 27/28 at D = R = 14 exactly,
dead by 14−5, 14−8 ∤ 4 and n₅ = 64/3 ∉ ℤ.

## Verification record (the largest fleet to date: 11 + 4 + 1 lanes, all Opus)

Desk first: full re-derivation + a 35-check exact-rational script, green before
any lane launched. Then: 2 blind lemma lanes (PROVED ×2, 1M+ enactments, sharp);
3 blind layer lanes (PROVED ×3 — **two returned independent alternative proofs**:
X ≤ 3 by a single negative-discriminant quadratic, valid for every real m;
X = 4 by the shifted second moment Σ(d−3)(d−5), four branch quadratics with
discriminants −559/−143/−47/−175 — both **banked here, not consumed**);
1 numeric lane (15/15 confirmed); 2 dependency audits (the X = 5 budget
Σw ≤ (4/3)(5−x_e) is TRUE but NOT a labeled 0017 claim — 0019 derives it from
the c-free links + the 4/3 per-pair corner; "no universal vertex" and n ≥ 36
were NOT-IN-REPO → derived-in-cert); 3 hostile refuters (SOUND ×3, zero fatal:
caught the audit text's one defect — ⌊16/3⌋ = 5 ⟹ Δ ≤ 11 is circular, repaired
by Δ ≤ 5 + X — plus the C3 dead-code find and the n₇-invocation explicitness).
Then the build: drafter (green ×2 first try on the mathematics) + 3-lens cert
audit (PASS-WITH-FIXES ×3: a deflation in check 26's headline — the census DOES
kill m = 26 outright — an inert mutant M7 advertised as load-bearing, a
mislabeled M1, ledger drift on (L-e), ~25 fixes total, all applied and
re-measured). Final: **60 checks + 9 notes, green ×2, 3.5 s.**

## Banked, not consumed

- The negative-discriminant X ≤ 3 route (window-free; also derives Δ ≤ 5+X
  independently and re-proves no-universal-vertex).
- The (d−3)(d−5) route to X = 4 (branch t=4 closes by confinement n₆ ≤ 6, not
  by D ≤ R — the D ≤ R version of that branch SURVIVES; remember that).
- (SC) strengthening S2′: only vertices of degree ≥ r count on the right —
  R* ≤ R, strict on 10,253/13,986 tested families. May matter at one-unit margins.
- (DH) sharper forms S1+/S1++ (fibre-level; the balanced-split convex bound
  F_r(d) > d−5 from d = 11 up).
- l5's alternative T-B route via the census identity 5n = 4D + 18m − C(m,2) − X − Σ
  (kills m = 28 coarse, no equality analysis).

## Doc errata this turn (all D-034: same-commit, condition-untouched)

Audit's three claims, all real: 0018 NOTES claim-row still carried struck L1.2;
PLAN's "Eighteen certificates, each green ×2" vs 0004 never-green; 0017's
"nothing at X = 5 beyond the corner's failure" (a deflation of its own C1 — the
4/3 rung IS a certified X = 5 claim). Desk found three more: the same deflation
in 0017 verify.py's docstring (caught by a dependency lane; comments fixed,
re-verified green ×2), the same over-broad line in README, and AGENTS.md's
green-cert list stale at 0012. Issue: none open.

## Scars kept (D-017)

The desk's spec parenthetical claimed the m = 26 no-(D2) census run has exactly
one survivor — false, it has two (the second dies by (SC) at D = 20 > 12); the
fixer measured and enacted the truth instead of the instruction. And the desk's
first read of the audit text missed the ⌊16/3⌋ circularity that two refuter
lanes caught. Both recorded in 0019's NOTES.

## State after turn 15

**X ≥ 5 on every rung of [22, 456]; X = 5 only on m ∈ [22, 26]; X ≥ 6 on
m ∈ [27, 456].** The 12,171-configuration X = 4 frontier is closed without
enumerating a single configuration. The thin rungs m ∈ {23..26} are no longer
arithmetic-free — every rung now carries forced excess ≥ 5. The next field is
X = 5 on five rungs, five excess partitions.
