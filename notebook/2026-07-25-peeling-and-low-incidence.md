# 2026-07-25 · turn 2 — peeling, the low-incidence bound, and what did not finish

Append-only. Technical. Failure is recorded as failure.

## 0. Seal check

Intact. Nothing sealed was read, by this lab or by any subagent. The only external
reading was the published literature (AKP arXiv:1409.4938, ABW abstract), which the
BRIEF explicitly permits — the seal covers the *chain*, not the field.

## 1. (L5), and m = 20 Δ = 5

Cert 0002's (L4) is per-edge: Σ_{v∈E} deg(v) ≥ m+5. Write the deficiency of E in
part i as Δ − deg, so Σ_i d_i(E) ≤ B = 6Δ − (m+5). Then no edge has more than
⌊B/θ⌋ parts of deficiency ≥ θ, so Σ_i L_i(θ) ≤ m⌊B/θ⌋. **Cert 0003 GREEN.**

At m=20, Δ=5 the budget is 5, so θ=3 gives at most one low part per edge — 20
incidences available against 28 required. **m=20, Δ=5 is dead.** Primal and dual
DPs agree. m=20 is now Δ ∈ {6,7}.

This is the third distinct consequence squeezed out of the same pigeonhole that
AKP run once, at m=8, inside their Claim 2.3.

## 2. The peeling engine

`lib/peel.py`. H with max degree Δ splits as star(v) ∪ R with τ(R) ≥ t−1, so
enumeration at (m,t) reduces to (m−Δ, t−1). Attaching a star is cheap: every star
edge must meet all of R using its five coordinates outside v's part, so its
restriction there is a **minimum cover of R**. And τ(H) ≥ t reduces to a set-cover
condition — the star must escape every minimum cover of R.

`canonical_fast` added to `ryser.py`: restrict part permutations to those sorting an
iso-invariant part signature. Verified to induce the same classes as the slow form
on every r=3 level. **21× on the case measured** (generate(5,3): 187 s → 8.7 s).

**Validation:** enumerate(5,3) = **12 classes** by peeling, matching the edge-wise
census exactly. Two algorithms sharing no code path. enumerate(4,3) = 0, matching
g(3)=5.

## 3. The m = 19 reduction, sharpened

Let H be a 19-edge counterexample. Cert 0002 forces Δ=6; let v have degree 6 in
part p and R = H − star(v), so |R| = 13 and τ(R) = 5 (f(6)-extremal).

(a) Each star edge f must meet all 13 edges of R, and v does no work, so f's
restriction C_f to the five parts ≠ p is itself a **minimum cover of R**.

(b) A 5-set C covering H cannot contain v (else C∖{v} is a 4-cover of R, against
τ(R)=5), so C is a minimum cover of R that meets every C_f. Hence

  **τ(H) ≥ 6 ⟺ every minimum cover of R is disjoint from some C_f.**

So m = 19 is exactly: *does some f(6)-extremal 13-edge object admit six of its own
minimum covers, all rainbow across one common set of five parts, that dominate all
its minimum covers by disjointness?* Taking C = C_{f_i} shows the six must contain
disjoint pairs. Cheap to test per R — the cost is producing R.

## 4. What did not finish, and why

The chain to enumerate(13,5) did **not** complete. Measured, not guessed:

- the peeling recursion drops through τ≥2 levels, where classes proliferate
  (enumerate(4,2) alone = 49 classes and climbing) — the wrong tool down there;
- routing the base cases through the edge-wise generator is better but its
  intermediate levels are unpruned until the τ-prune bites: level sizes
  1, 6, 48, 508, 12 for (5,3), and (6,3) did not finish inside the budget;
- the star attachment allows up to Δ fresh symbols per part with no canonical
  ordering, so isomorphic stars are generated many times over and deduped after
  the fact. This is the real defect.

**The fix, for next turn:** attach stars *column-wise*. What matters in part q is
only the partition the star induces on its Δ edges (which edges share a symbol,
and whether that symbol is old or new) — not which fresh label is used. Enumerating
set partitions of the star kills the redundancy at source instead of by dedup.

Budget honoured: the 90-minute pre-registration held, the run was killed rather
than pushed through, and the manifest records it.

## 5. Verdict

Floor unchanged: **m ≥ 19**. The remainder is now three cases — m=19 Δ=6, m=20
Δ∈{6,7} — and m=19 has a crisp finite reduction. Nothing here confirms m ≥ 21.
