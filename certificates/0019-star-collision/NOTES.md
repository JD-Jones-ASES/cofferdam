# Certificate 0019 — the star-collision inequality: X ≥ 5 everywhere, X = 5 confined to m ≤ 26

**Status: GREEN ×2.** 60 checks + 9 notes, ~3 s,
`python3 verify.py`, stdlib only, no solver, no imports from `lib/`, reads nothing
from disk. Green under a bare `/usr/bin/python3` (3.9.6) **and** under `python3 -O`,
both outputs byte-identical modulo wall clock; stable across `PYTHONHASHSEED`
0 / 1 / 12345 and from any working directory. Deterministic (hand-rolled LCG,
seed 20260728). Every load-bearing bound is exact `Fraction` arithmetic.

| claim | label |
| --- | --- |
| **(T-A) X ≥ 5 for every critical core in the window** — every edge-critical 6-partite 6-uniform intersecting counterexample core with τ = 6 and m ∈ [22, 456] has X ≥ 5 | **PROVEN-BY-CERTIFICATE** (in-house: 0013, 0015 (2)–(3), **0017 C1 (check 8)**/c12/C3, 0005, **0008 (D2)**, 0012/0013/0014 transitively; 0016 (T) via 0017 c7 only *through* C1; **not 0017 c9** — the 4/3 corner is T-B's; external NONE) |
| **(T-B) X = 5 forces m ≤ 26** — corollary with T-A: **m ≥ 27 ⟹ X ≥ 6** | **PROVEN-BY-CERTIFICATE** (in-house: 0013, 0015 (2)–(3), **0017 c9** (the 4/3 corner) + c12 + C3, 0005, 0012/0013/0014 transitively; **NOT 0008 (D2)** — measured, mutants M3/M3′, §5; external NONE) |
| **(SC) the star-collision inequality** — for an intersecting r-partite r-uniform family with no universal vertex, D := Σ_v (d(v)−(r−1))₊ ≤ R := Σ_pairs q(q+1) | **PROVEN-BY-CERTIFICATE** (derived in-cert; enacted on 849 families, 62 at equality) |
| **(DH) the defect-hub bound** — for z ∉ f, d(z) ≤ (r−1) + Σ_{{e,g}⊆E(z)} q_eg ≤ (r−1) + X − x_f; **globally Δ ≤ 5 + X** at r = 6 | **PROVEN-BY-CERTIFICATE** (derived in-cert; enacted on 60,416 (z,f) pairs) |
| the R partition maxima and the five pointwise inequalities (A)(B)(C)(E)(F) with their exact slack vectors and range tops | **PROVEN-BY-CERTIFICATE** (exhaustive, exact — checks 4–8, 13) |
| the **thirteen branch cap-triples** (dmax, count cap, R) | **PROVEN-BY-CERTIFICATE** (derived in §layers from (DH) and (L-e); the budget→cap readings are exhaustive at checks 14–15, and the per-branch assignment — hand-derived, then hard-coded as literals in `BRANCH_A`/`BRANCH_B` — is re-derived from `capof[]` and `RTAB[]` and matched literal by literal at check 36) |

## Why this certificate exists

Turn 14 left the lab at **X ≥ 4 at m = 22** (0018) and a 12,171-configuration
X = 4 frontier at the floor, with the rest of the window carrying only 0017's
window-wide profile. The obvious next move was to attack X = 4 at m = 22 the way
0018 attacked X = 3: enumerate the shapes of the excess and kill them one at a
time. That path was open, and it was going to be long — 23 shapes were already
banked from turn 13.

This certificate does not take it. It replaces the whole shape-census method
with **two counting lemmas and one arithmetic engine**, and gets a strictly
stronger result across the entire window instead of one rung of it:

> A vertex z outside an edge f must send **every one of its edges** into f, and
> f's cell in z's own part can take **none** of them. So d(z) beyond r−1 is paid
> for in collisions between z's own edges, and every collision is excess.
> That is Δ ≤ 5 + X. Summed over all vertices, the same count says the total
> degree defect D cannot exceed R = Σ q(q+1). After that the problem is
> arithmetic: two moments, 36 vertices, a degree-2 cap, and eight branches of
> X ≤ 4 plus five rungs of X = 5 — **3,056 census runs, every one
> empty**.

Three things change with it. **0018's theorem becomes a corollary** (§7,
control-only — 0018 is not consumed anywhere here), **the X = 4 frontier at
m = 22 closes without a single shape being enumerated**, and the excess floor
becomes *window-wide* rather than floor-local, which is what T-B then exploits:
above m = 26 the floor is X ≥ 6.

## The ledger, in full

| input | what is consumed | where |
| --- | --- | --- |
| **0013** | criticality; the private minimum 5-covers T_e (τ(K−e) = 5) | supplies T_e, hence the 5 in Φ(dᵢ−1, 5−bᵢ) and the whole w-table |
| **0015 steps (2)–(3)** | the pigeonhole Σᵢ Φ(dᵢ−1, 5−bᵢ) ≤ I_e and the accounting I_e = Σ a·b — **c-free** | (L-e), all on-f caps |
| **0017 C1 (check 8)** | the **c = 1 per-pair corner** a·b ≤ s−1 at forced excess ≤ 4 | (L-e) at X ≤ 4 — **every on-f budget of Theorem A** |
| **0017 check 9** | the **4/3 per-pair corner** at forced excess ≤ 5 | (L-e) at X = 5 — priced by mutant M5 |
| **0017 check 12** | the identity Σ over pairs of K−e of (s−1) = X − x_e | (L-e) |
| **0017 C3** | 2m + 5x_e ≤ 52 + 3X, X-unrestricted | X = 3 heavy branch (m ≤ 25); **all of Theorem B** (m ≤ 31, per-rung caps) |
| **0005** | min degree ≥ 2; (A) on active vertices (deg ≤ 2 ⟺ deg = 2) | (L-c); the census's degree floor |
| **0008 (D2)** | 2·D₂ ≤ m | (L-c) — **consumed by T-A, measured at 3 configurations (M3); NOT consumed by T-B** |
| **0012/0013/0014** | the window [22, 456] | transitively, the quantifier |
| **external** | **NONE.** No peer sketch, no citation, no published lemma. | — |

**Cited through C1, not separately consumed.** 0016's (T) as generalized by
0017 **check 7**, and 0013's **(3a)**, are inputs to 0017 **C1** — they reach
this file only through C1's own ledger. An earlier draft billed both directly
to (L-e) *and* cited C1's conclusion in the same proof, which is the L1.2
disease: cite the conclusion or its ingredients, never both. Rows dropped.

**Derived in-certificate** (proofs below, enacted in-run): (L-a) no universal
vertex · (L-b) n ≥ 36 and the per-part structure · (L-c) n₂ ≤ ⌊m/2⌋ · (L-d)
w-monotonicity and the w-table · (L-e) the X = 5 per-edge budget · (L-f) (DH),
(SC), Δ ≤ 5 + X.

**Not consumed:** certificate **0018** (T-A implies its theorem — independent
corroboration, §7), 0017 **C2**, and any solver.

---

## The analytic proof

Throughout: K is edge-critical, 6-partite, 6-uniform, intersecting, τ(K) = 6,
and — this is what "edge-critical" unpacks to, and it is load-bearing —
**τ(K − e) = 5 for every e ∈ K**, which is what supplies each edge its own
private minimum 5-cover T_e (0013), and hence the **5** in Φ(dᵢ−1, 5−bᵢ), hence
w(d) = Φ(d−1,5), hence the w-table, (L-d), (L-e) and every on-f budget in both
theorems. m = |K|. A **vertex** is a cell (part, value); d(v) its degree; n_d the
number of vertices of degree d; n = Σ n_d. λ(f,g) = |f ∩ g| ≥ 1, q = λ − 1,
X = Σ_pairs q, x_e = Σ_{f≠e} q(e,f), Σ_e x_e = 2X. Φ(n,k) is the balanced-split
minimum of Σ C(n_j,2); **w(d) := Φ(d−1, 5)**, derived from Φ and never
hand-tabulated. E(z) = the edges through z;
**star_excess(z) := Σ over pairs inside E(z) of q**.
**D := Σ_v (d(v)−5)₊** and **R := Σ_pairs q(q+1)**.

**The per-edge notation, imported verbatim from 0015/0017** so that (L-e) is
walkable from this file alone. Fix an edge e. **T_e** is a private minimum
5-cover of K − e (it exists because τ(K − e) = 5). Number e's six slots
i = 1..6; **dᵢ** is the degree of e's i-th vertex and **bᵢ** = |T_e ∩ {that
vertex's block}|, the part of T_e's five cells that lands in slot i, so
Σᵢ bᵢ ≤ 5. For a pair {f,g} ⊆ K − e: **s := λ(f,g)**, **a := |e ∩ f ∩ g|**,
**b := |T_e ∩ f ∩ g|**, and **I_e := Σ over those pairs of a·b**.

### (L-a) No universal vertex

If a vertex z lies in every edge, {z} is a 1-cover of K and τ(K) = 1 ≠ 6. ∎

Consequence: **every vertex has some edge avoiding it**, which is the only
hypothesis (DH) ever needs. The hypothesis is not free in general — §2's control
2 exhibits an r = 6, m = 9 pencil where (SC) is flatly false — it is free *for a
critical core*.

### (L-b) n ≥ 36, and the per-part structure

Fix a part V_i. Every edge has exactly one cell in V_i, so the nonempty blocks
of V_i **partition** E — in particular they **cover** E. A cover of size ≤ 5
contradicts τ = 6, so V_i carries **≥ 6 vertices**, and Σ_{v ∈ V_i} d(v) = m. ∎

Consequence: **n ≥ 36**, a constraint in every census below; and at n = 36
exactly, each part carries *exactly* six blocks whose degrees sum to m — the
fact tooth (c) of §3 spends at m = 26. Mutant M9 prices it: relax to n ≥ 35 and
**183 configurations revive**.

### (L-c) n₂ ≤ ⌊m/2⌋

0008's (D2) is 2·D₂ ≤ m with D₂ the number of degree-≤-2 vertices; 0005 (A)
makes minimum degree 2 on active vertices, so D₂ = n₂. Integrality gives
n₂ ≤ ⌊m/2⌋. ∎ (This is the one place 0008 enters, and §5 measures exactly what
it buys.)

### (L-d) The weight w and its monotonicity

C(j,2) ≥ j − 1 for every integer j ≥ 0, so Φ(n,k) ≥ n − k; Φ is nonincreasing in
the class count k. Hence **Φ(d−1, 5−b) ≥ Φ(d−1, 5) = w(d)** for 0 ≤ b ≤ 4 —
whatever the private cover T_e does with its five cells; **if bᵢ = 5**,
monotonicity is not invoked: the inherited covering branch (0015 step (1))
forces dᵢ = 1, so the term and its w-relaxation are both zero. (Scope
clarification 2026-07-28, third outside audit: the sentence originally said
"for every b ≥ 0", though the check runs b = 0..4.) The table at d = 2..11
is **0, 0, 0, 0, 0, 1, 2, 3, 4, 5**, and w(d) ≥ d − 6 for all d — w is an
**integer at every d** (Φ is a count; w(12) = 7). ∎

### (L-e) The per-edge budget

0015 steps (2)–(3) give Σᵢ Φ(dᵢ−1, 5−bᵢ) ≤ I_e = Σ over pairs {f,g} ⊆ K−e of
a·b, and 0017 check 12 gives Σ over those pairs of (s−1) = X − x_e. Apply the
corner pairwise:

- **at X ≤ 4** (0017 **C1**, its check 8: c = 1 is valid at X ≤ 4, the first
  violator (a,b,s) = (2,2,4) forcing exactly 5): a·b ≤ s − 1, so I_e ≤ X − x_e;
- **at X = 5** (0017 check 9, c = 4/3): a·b ≤ (4/3)(s−1), so I_e ≤ (4/3)(X − x_e);
- the a ≤ 1 branch is trivial in both cases: a = 0 gives a·b = 0 ≤ c(s−1) since
  s ≥ 1; a = 1 puts a vertex of e inside f ∩ g, and **T_e avoids e** (that is
  what "private" means, 0013), so b = |T_e ∩ f ∩ g| ≤ s − 1, i.e. a·b ≤ s−1.

With (L-d) on the left, **Σ_{v∈e} w(d(v)) ≤ X − x_e** at X ≤ 4, and
**Σ_{v∈e} w(d(v)) ≤ (4/3)(5 − x_e)** at X = 5. Floored, the X = 5 budgets read
**6, 5, 4, 2, 1, 0** at x_e = 0..5. ∎

Read against the w-table: budget 0 ⟹ d ≤ 6; budget 1 ⟹ d ≤ 7 with n₇ ≤ 1;
budget 2 ⟹ d ≤ 8 with n₈ ≤ 1; budget 3 ⟹ d ≤ 9 with n₉ ≤ 1; budget 4 ⟹ d ≤ 10
with n₁₀ ≤ 1 **and** n₉ + n₁₀ ≤ 1; budget 5 ⟹ at most one d ≥ 10.

> Budget 5 would also admit **d = 11** (w(11) = 5). It is **Δ ≤ 5 + X = 10** that
> closes degree 11, not the budget — which is why no (Dq) machinery and no
> degree-11 analysis appears anywhere in this certificate.

### (L-f) (DH), (SC), and Δ ≤ 5 + X — the two new lemmas

**(DH).** Fix a vertex z and an edge f with z ∉ f. For u ∈ f put
r_u := |{e ∈ E(z) : u ∈ e}|.

1. **Every z-edge meets f** (K is intersecting), so Σ_{u∈f} r_u ≥ d(z).
2. **The part-mate is empty.** Let p be z's part and u_p = f's cell in p. Every
   e ∈ E(z) has z as its part-p cell, and z ≠ u_p, so no e ∈ E(z) contains u_p:
   **r_{u_p} = 0**. At most r − 1 of the r fibres are nonempty. *(This is the
   whole content of partiteness here, and it is worth exactly one unit — §2's
   control 3 exhibits a non-partite family where (DH) fails by that unit.)*
3. **Fibre pigeonhole.** For every integer a ≥ 0, a ≤ 1 + C(a,2). Applied
   fibre by fibre over the ≤ r−1 nonempty fibres:
   Σ_{u∈f} C(r_u,2) ≥ Σ_u (r_u − 1)₊ ≥ Σ_u r_u − (r−1) ≥ d(z) − (r−1).
4. **The mirror identity.** Σ_{u∈f} C(r_u,2) = Σ over pairs {e,g} ⊆ E(z) of
   |e ∩ g ∩ f| — count, for each u ∈ f, the C(r_u,2) pairs of z-edges through u.
5. **The drop-z step.** z ∈ e ∩ g but z ∉ f, so |e ∩ g ∩ f| ≤ |e ∩ g| − 1 = q_eg.

Chaining 3–5: **d(z) ≤ (r−1) + Σ_{{e,g}⊆E(z)} q_eg = (r−1) + star_excess(z)**.
And no pair inside E(z) involves f, so star_excess(z) ≤ X − x_f, giving
**d(z) ≤ (r−1) + X − x_f**. With (L-a) supplying an f for every z, at r = 6:
**Δ ≤ 5 + X**. ∎

**(SC).** Sum (DH) over the vertices with d(v) > r−1 (all others contribute 0 to
D), then exchange the order of summation:

  Σ_v star_excess(v) = Σ over pairs {e,g} of q_eg · |e ∩ g| = Σ_pairs q(q+1) = R,

because a pair {e,g} appears in E(v) exactly for the |e ∩ g| = q+1 vertices it
shares. Hence **D ≤ R**. ∎ *(That exchange is the step where the q(q+1) weight
is born, so it is enacted separately in §2 — both sides accumulated
independently over every family and every vertex, universal ones included, and
equal.)*

Three facts about (SC), each a must-fail control in §2 rather than a remark:

- **D ≤ X is FALSE.** The r = 3, m = 5 family (1,1,1), (2,1,2), (0,1,1), (2,1,0),
  (2,0,1) has X = 2 and **D = 4** — twice X — and sits at (SC) equality D = R = 4.
  The λ factor in q(q+1) is load-bearing (**mutant M2**: with q² the bound reads
  4 ≤ 2 and is violated by **24 families** in the corpus).
- **"No universal vertex" is load-bearing.** The r = 6, m = 9 pencil has R = 0
  and D = 4. In the corpus, 574 families have a universal vertex and 14 break
  (SC); 18 universal vertices break (DH) itself.
- **The bound is sharp**: 62 of the 849 hypothesis-satisfying families hit
  equality.

### The Δ ≤ 5 + X strengthening — and an erratum owed to the audit (2026-07-28)

**ERRATUM (caught by the third outside audit, same day).** This section
originally stated that the received proof's degree-cap step — w-sum ≤ 16/3,
⌊16/3⌋ = 5, therefore Δ ≤ 11 — "was circular as written: reading the w-sum as
an integer presupposes that the degrees are already capped." **That charge is
false of the received text.** There, w(d) := Φ(d−1, 5), and Φ is a count — an
integer at *every* d (w(12) = 7, not "≥ 6") — so the w-sum is a sum of
integers and the flooring is valid with no cap presupposed anywhere. The
circularity was real only in the **desk's transcription** handed to the
refuter lanes, which restated w as the d ≤ 11 table plus the inequality
w(d) ≥ d − 6 above it; under that weakened spec integrality genuinely fails to
follow, and the two refuters who flagged it were **correct about their
input** — though even there the step was unjustified-but-**inert**: the pack's
own w(d) ≥ d − 6 closes d ≥ 12 against 16/3 directly, so no downstream
conclusion depended on the flooring (fourth-audit-lane refinement, same day).
The desk then recorded their finding as the peer's defect without
re-checking it against the original — a deflation of a peer's correct *step*,
the same failure D-036 names for numbers, now committed one level up. D-038
is the law this bought: refuters read the verbatim received text, and a
defect found in transcribed material is checked against the original before
it is recorded as the peer's.

What stands unchanged: **(DH) is independently derived** — partiteness,
intersecting-ness, and the definition of X, no flooring at any step — and it
is **strictly stronger** (Δ ≤ 5 + X = 10 at X = 5, against the received
text's 11). It is an improvement over a valid argument, not a repair of a
broken one. This paragraph exists so that no reader mistakes either direction:
agreement-on-the-statement is not agreement-on-the-proof, and *disagreement
with a transcription is not a defect in the source*.

---

## The layers, exactly as the engines encode them

For each branch: pick f as stated (existence from Σ_e x_e = 2X), read the
**off-f** cap d ≤ 5 + (X − x_f) from (DH), the **on-f** cap from (L-e), and
**R** from the partition maximum of X under the branch's cap on q. A vertex of
degree above the off-f cap must lie on f, and f has six vertices — that is where
every count cap (n₆ ≤ 6, n₇ ≤ 1, n₈ ≤ 1, n₉ ≤ 1, n₁₀ ≤ 1) comes from.

### Theorem A — X ≤ 4 (§3): 3,049 (branch, m) cells, zero survivors

| branch | f | off-f | on-f budget | caps | R |
| --- | --- | --- | --- | --- | --- |
| X = 0 | any (x_f = 0) | ≤ 5 | 0 | dmax 6, n₆ ≤ 6 | 0 |
| X = 1 | in the unique pair | ≤ 5 | 0 | dmax 6, n₆ ≤ 6 | 2 |
| X = 2, x_f ≥ 1 | Σx_e = 4 > 0 | ≤ 6 | 1 | dmax 7, n₇ ≤ 1 | 6 |
| X = 3, all x_e ≤ 1 | x_f = 1 | ≤ 7 | 2 | dmax 8, n₈ ≤ 1 | 6 |
| X = 3, some x_f ≥ 2 | x_f ≥ 2 | ≤ 6 | 1 | dmax 7, n₇ ≤ 1 | 12 |
| X = 4, all x_e ≤ 1 | x_f = 1 | ≤ 8 | 3 | dmax 9, n₉ ≤ 1 | 8 |
| X = 4, max x_e = 2 | x_f = 2 | ≤ 7 | 2 | dmax 8, n₈ ≤ 1 | 12 |
| X = 4, some x_e ≥ 3 | x_f ≥ 3 | ≤ 6 | 1 | dmax 7, n₇ ≤ 1 | 20 |

The census then asks for integer (n₂ … n_dmax) with Σ d·n_d = 6m,
Σ C(d,2)·n_d = C(m,2) + X, Σ n_d ≥ 36, n₂ ≤ ⌊m/2⌋, the count caps, and D ≤ R.
**There are none, at any m in [22, 456], in any branch** (253,529 search nodes).

**The analytic mirror.** (A) summed under n ≥ 36 and n₂ ≤ ⌊m/2⌋ gives
L_X(m) = −7m + (C(m,2)+X)/3 + 90 − ⌊m/2⌋/2 ≤ D, strictly increasing in m, so the
m = 22 reading covers all 435 rungs: **D ≥ 8, 8, 9, 9, 9** against R = 0, 2, 6,
6, 8 for the five "light" branches. (C) summed gives R4(22) = 25/2, so **D ≥ 13
> 12** on the X = 4 max-2 branch. (B) summed gives the (U)-difference
**G(m) + 1 > 0 everywhere** on the X = 4 heavy branch.

**The C3 shortcut at X = 3, x_f ≥ 2 — and why the census is kept anyway.**
0017's C3 reads 2m ≤ 61 − 5x_e at X = 3, so x_e ≥ 2 forces **m ≤ 25**; the census
therefore only has to cover m = 22..25, and the (U)-difference independently
kills every rung except **m = 26**, which C3 has already taken. The desk's first
pass reached m = 26 through the (U) route alone, where G(26) = **0** — a
zero-margin rung where one wrong slack term would have been fatal. So m = 26 is
killed **three more times**, all redundant, all kept — and the redundancy runs
deeper than it looks: **the independent kill is C3, not the teeth from each
other.** (b) and (c) both read off (a)'s pinned vector, and (c) additionally
imports (a)'s degree confinement and n = 36. Three teeth, one root.

- **(a) the (U)-equality pin.** G(26) = 0 means (B) summed is *exactly* tight, so
  every slack source vanishes: n₄ = n₅ = 0 (slack 1 each), n = 36, n₂ = 13, n₇ = 1.
  Degrees confine to {2,3,6,7} and the first moment 2n₂+3n₃+6n₆+7n₇ = 156 has the
  **unique** solution **(13,3,19,1)** — whose second moment is 328 = C(26,2)+3
  exactly, i.e. a fully consistent arithmetic survivor. Drop the n₂ = 13 pin and
  the same system has **five** solutions (1,19,15,1), (4,15,16,1), (7,11,17,1),
  (10,7,18,1), (13,3,19,1) — but those are solutions of the **first moment
  alone**: their second moments are 304, 310, 316, 322, 328 against the required
  328, so four of the five are not census-admissible at all. **The census kills
  m = 26 outright**, measured with this file's own enumerator: census(26, X = 3,
  dmax 7, n₇ ≤ 1, R = 12) is **empty**, with (D2) on and with it dropped. Drop
  (SC) instead (R unbounded), keep both moments, and **exactly one** vector
  survives — the pinned (n₂..n₇) = (13,3,0,0,19,1) — with n₂ *not* pinned to 13,
  merely capped by (D2); drop (D2) as well and a second appears, (14,1,0,2,18,1),
  which (SC) kills at D = 20 > 12. So what the (U)-equality buys here is **not**
  the kill: it is that the target vector is selected *without* the moment
  argument, which is the only reason (b) and (c) can be read as teeth at all.
- **(b) star-collision, one line.** That vector has D = n₆ + 2n₇ = **21 > 12** = R.
  It runs on (a)'s pin.
- **(c) the per-part clash.** At n = 36 each part carries six blocks summing to
  26 — both of those facts imported from (a). The size-6 multisets from {2,3,6,7}
  summing to 26 are exactly **four**: {2,2,2,6,7,7}, {2,2,3,6,6,7},
  {2,3,3,6,6,6}, {3,3,3,3,7,7}. The pin is n₇ = 1 exactly; the enactment
  **deliberately invokes only the weaker n₇ ≤ 1**, per part and globally, so the
  clash is established on a *superset* of what the pin allows. That removes the
  two double-7 multisets; the six parts then assemble into exactly two global
  vectors, (6,12,18,0) — which the pin itself already excludes — and
  **(7,11,17,1)**. Neither is (13,3,19,1). *The invocation is written out for
  explicitness, and it is **not** load-bearing:* **mutant M7** drops it, the
  assembly grows from 2 vectors to **49**, and (13,3,19,1) is absent from all 49,
  so the clash survives the relaxation untouched.

### Theorem B — X = 5 (§4): five rungs, seven cells, zero survivors

C3 at X = 5 reads 2m + 5x_e ≤ 67, and Σ_e x_e = 10 > 0 forces some x_e ≥ 1, so
**m ≤ 31**. The per-rung caps ⌊(67−2m)/5⌋ are **2, 2, 1, 1, 1** at m = 27..31, so
m ≥ 29 admits only x_e ≤ 1 — a **5-matching** of λ2 pairs, R = 10 exactly. Caps:
off-f ≤ 9 (or ≤ 8 at x_f = 2), on-f by the floored 4/3 budget, dmax 10 by
Δ ≤ 5 + X, n₁₀ ≤ 1. Every census run is empty; the tighter max-2 run with
n₉ + n₁₀ ≤ 1 is empty too — **necessarily so, since it is a filter over an
already-empty enumeration** (the budget-4 reading buys nothing once the
conservative run is empty). Base 0 → filtered 0, at both m = 27 and m = 28.

The analytic mirror at the two thin rungs is where this certificate is thinnest,
and it is worth reading in full:

- **m = 29..31:** (E) summed gives D ≥ L₅(29) − 5/6 = 97/6, so **D ≥ 17 > 10**.
  Seven units of slack — the top of the range is not the problem.
- **m = 28, max-2:** (E) gives D ≥ 44/3 − 5/6 = **83/6**, so D = 14 = R **exactly**.
  Slack budget 14 − 83/6 = **1/6**; over the seven slack sources
  {n₄: 1/6, n₆: 1/2, n₇: 2/3, n₈: 1/2, extra-n: 5/2, n₂-deficit: 1/2,
  n₁₀-missing: 5/6} the only admissible non-empty multiset is **{n₄: 1}**. Both
  admissible cases force n₆ = n₇ = n₈ = 0 and n₁₀ = 1, hence D = 5 + 4n₉ = 14 —
  **insoluble in integers**.
- **m = 27, max-2:** (F) gives D ≥ **95/7** (and **(F) carries no n₂ correction,
  so this rung is (D2)-free**), so again D = 14 = R and the budget is **3/7**.
  Five multisets fit; only {n₆: 1} and {n₈: 1} move D. Case 8: D = 8 + 4n₉ = 14,
  insoluble. The three D = 5 + 4n₉ cases: insoluble. Case 6: D = 6 + 4n₉ = 14
  gives n₉ = 2 and survives *this* step — then the budget is fully spent, so
  n₃ = n₄ = 0, n = 36, n₁₀ = 1, and the residual system n₂ + n₅ = 32,
  2n₂ + 5n₅ = 128 gives **n₅ = 64/3**, not an integer. Dead.

**T-B assembled:** X = 5 ⟹ m ≤ 26. With T-A: **m ≥ 27 ⟹ X ≥ 6**.

---

## Provenance — the outside-audit lane's second fruit

The second outside audit (**GPT 5.6 Sol Pro**, 2026-07-28, reading the public
repo at `079539c`) proposed **both theorems AND a complete analytic route**,
delivered as **full proof text**. Per **D-036** the proof text entered no
chain: the desk read it and **re-derived every step independently** (a 35-check
exact-rational desk script ran before any fleet lane); the **blind fleet lanes
received STATEMENTS plus one-line mechanisms only** — two lemma lanes re-proved
(DH)/(SC) from the definitions with over a million enactment instances; three
layer lanes re-derived the eliminations, two of them by **independent routes
the audit text does not contain** (a negative-discriminant quadratic for X ≤ 3;
a (d−3)(d−5) second-moment functional for X = 4); the received text itself went
only to **three hostile refuter lanes**, whose job was to break it. Two
refuters flagged a circularity in the ⌊16/3⌋ degree-cap step **as it appeared
in the desk's transcription** (ERRATUM 2026-07-28: originally recorded here as
"its one defect", i.e. the received proof's — false; the received text's
Φ-defined w is integer at every d and its flooring was valid; see "The
Δ ≤ 5 + X strengthening" above and D-038). The desk's (DH) supplies the
strictly stronger free cap Δ ≤ 5 + X independently. **Attribution recorded,
not consumed: no step cites the audit.** The lanes, in full:

- **2 blind lemma lanes** on (DH)/(SC) from the definitions pack alone, with
  1M+ enactments between them;
- **3 blind layer lanes**, two of which returned **independent alternative
  proofs** — the *negative-discriminant* route to X ≤ 3 and the *(d−3)(d−5)*
  route to X = 4. Both are **banked in the turn-15 notebook, not consumed**;
- a **numeric lane** re-deriving the tables and the two summed laws;
- **2 dependency audits** on the ledger;
- **3 hostile refuters** — the only lanes to receive the argument;
  **zero fatal, zero major**; two flagged the transcription's circularity
  (see the erratum above);
- a desk re-derivation with its own 35-check script, then this file.

### The catches, kept on the record (D-017/D-036)

- **The ⌊16/3⌋ misattribution** (ERRATUM 2026-07-28): the desk transcribed w
  into a weaker spec, the refuters correctly broke the transcription, and the
  desk recorded the break as the peer's defect. The received step was valid;
  (DH) is a strengthening, not a repair. Caught by the third outside audit.
- **The m = 26 census was dead code** — C3 already caps that branch at m ≤ 25.
  Kept anyway, as a triple-redundant tooth, because it is a zero-margin rung.
- **The n₇ = 1 invocation in tooth (c) was implicit** in the desk's first
  write-up. Made explicit — and then measured, which is how mutant **M7 turned
  out to be inert**: dropping it grows the assembly from 2 to 49 and the clash
  survives anyway. Recorded as inert rather than quietly withdrawn.
- **Drafting scars, this file's own — two of them, both caught by the enactment
  rather than by reading.** The §2 audit's first run reported **31 (DH)
  violations**, which is exactly the shape of a broken lemma. It was not one.
  **Twelve** came from a **non-intersecting "near-pencil"** the generator was
  emitting (it also produced 1,088 spurious failures of (DH)'s global form);
  **nineteen** came from the draft checking (DH) at **universal vertices**,
  where the lemma has no hypothesis to stand on — an error in the *checker's
  scoping*, not in the generator or the lemma. Both were fixed at the source:
  a **hypothesis guard** that re-checks r-partiteness, distinctness and pairwise
  intersection on every family of ≥ 3 edges before any claim is read off it
  (check 16), and an explicit universal-vertex branch that **re-counts them as
  evidence for control 2** instead of failures — **eighteen** survive the
  generator fix (the nineteenth lived on the broken near-pencil), and check 22
  pins exactly those eighteen. *An enactment that does not
  verify its own hypotheses is not evidence — and a violation count is a
  question, not an answer.*

---

## Margins — every coordinate, named (D-035)

| coordinate | measured | binding? |
| --- | --- | --- |
| **X = 4 matching** | ⌈53/6⌉ = **9** against R = 8 | **one unit** |
| **X = 4 max-2** | ⌈25/2⌉ = **13** against R = 12 | **one unit** |
| **(U) at m = 24, 25** | G = **1** exactly | **one unit** |
| **(U) + 1 at X = 4** | minimum **1**, at m = 26 | **one unit**, across all 435 rungs |
| **m = 27 and m = 28** | D forced **= R = 14**: ZERO slack; the kills are 5+4n₉ = 14, 8+4n₉ = 14 and n₅ = 64/3 | **zero units** — divisibility, not size |
| **m = 29..31** | ⌈97/6⌉ = 17 against 10 | seven units |
| **the degree caps (DH)** | dmax +1 everywhere ⟹ **971** configurations revive; the faithful off-f +1 ⟹ **193** | the largest single coordinate |
| **the vertex floor (L-b)** | n ≥ 35 ⟹ **183** revive | second largest |
| **(D2)** | +1 ⟹ **3** revive (T-A only); dropped ⟹ **279** (T-A only), **0** in T-B | consumed by T-A, **not** by T-B |
| **n₈ ≤ 1** (L-e, budget 2) | 1→2 ⟹ **1** revives (m = 22) | one configuration |
| **n₁₀ ≤ 1** (L-e, 0017 c9's 4/3 corner) | 1→2 ⟹ **3** revive (m = 27) | the only coordinate pricing c9 |
| **R = 12** (partition maximum, X = 4 max-2) | R+1 ⟹ **3** revive (m = 22, 23) | one unit |

**Where this certificate is thin, in one sentence:** at m = 27 and m = 28 the
star-collision bound is *exactly tight* — D must equal R = 14 — and nothing is
killed by size; the kills are the non-divisibility of 14 − 5 and 14 − 8 by 4 and
the non-integrality of 64/3. If any of the three inputs to those two rungs moves
by one unit, those rungs reopen. **And one cell carries more coordinates than
any other: X = 4 max-2 at m = 22 revives under five of the nine mutants — M1
(both readings), M3 (both readings), M4, M6 and M9, seven of the eleven measured
rows.** No other cell revives under more than three. It is the single thinnest
configuration in the certificate, and it is exactly the rung 0018's frontier sat
on.

## The mutation table (§5 — nine mutants in eleven measured readings, every count in-run)

| mutant | reddens | surviving configurations | measured where |
| --- | --- | --- | --- |
| **M1** every dmax +1 — a **strict relaxation** of (DH) 5 → 6, with the count caps left keyed at the old degrees | checks 24, 37 | **971** | S3 947 (X=3 heavy m 22–25, X=4 max-2 m 22–25, X=4 heavy m 22–28); S4 24 (m = 27 max-2) |
| **M1′** off-f cap +1 — **the faithful** (DH) 5 → 6, (L-e)'s on-f budget untouched | check 24 | **193** | S3 193 (X=4 max-2 m 22–24, X=4 heavy m 22–27); **S4: 0** |
| **M2** R's q(q+1) → q² | check 19 | **24** families falsify the mutant | control 1 (r=3, m=5): D = 4 > Σq² = 2 |
| **M3** (D2) ⌊m/2⌋ → ⌊m/2⌋+1 | check 24 | **3** | X=4 max-2 at m=22; X=4 heavy at m=24, 25. **S4: 0** |
| **M3′** (D2) dropped entirely | check 24 | **279** | four branches of T-A. **S4: 0** |
| **M4** n₈ cap 1 → 2 (X=4 max-2) | check 24 | **1** | m = 22 only — **the spec expected m = 22..25** |
| **M5** n₁₀ cap 1 → 2 at m = 27 | check 37 | **3** | m = 27 max-2; prices 0017 check 9's 4/3 corner directly |
| **M6** R → R+1 (X=4 max-2) | check 24 | **3** | 2 at m = 22, 1 at m = 23 |
| **M7** drop n₇ ≤ 1 in tooth (c) | check 31 | **49** assembled vectors (vs 2) — **and the tooth survives it** | 4 per-part multisets instead of 2 |
| **M8** floor instead of ceil on 95/7, 83/6 | checks 39, 40 | **6** soluble slack cases (vs 1) | m = 27: 1 → 4; m = 28: 0 → 2, every new case D = 13 |
| **M9** n ≥ 36 → n ≥ 35 | checks 24, 37 | **183** | S3 173 (55 at m = 22, X=4 max-2); S4 10 at m = 27 |

**M1 is two readings of one coordinate, and only the second is the mutation the
prose names.** M1 bumps every `dmax` by one while the count caps stay keyed at
the old degrees, so it admits configurations no reading of "(DH) 5 → 6"
permits — all 971 of them, in fact, sit outside the mutant the name describes.
**M1′ is the faithful one:** the off-f cap 5 + (X − x_f) moves by one and
(L-e)'s on-f budget is left alone. Because the on-f cap already sits exactly one
above the off-f cap in every branch, the effect is exact — `dmax` unchanged, the
count cap at `dmax` voided — except on the X = 5 max-2 branches, where the on-f
cap sits *two* above and n₁₀ ≤ 1 survives the mutation. Measured: **193** in
T-A, **0** in T-B. Both rows are kept: the loose one because 971 is the number
the margins table quotes for the coordinate, the faithful one because it is the
number the *lemma* is worth.

**M7 is inert, and it is kept because it is inert.** Dropping n₇ ≤ 1 grows the
per-part assembly from 2 vectors to 49 — but **(13,3,19,1) is absent from all
49**, so tooth (c)'s actual contradiction, *assembled ≠ pinned*, survives the
relaxation completely. The invocation is **explicitness and sharpening, not a
tooth**. What the pin *does* buy is visible elsewhere: three of the 49 —
(4,18,4,10), (7,13,9,7), (10,8,14,4) — satisfy the second moment 328 and would
be live vectors without the (U)-pin context, and each carries n₇ ∈ {4,7,10}.

**M3 is the ledger-deciding measurement, and it came out the harder way.** The
spec asked whether *any* branch of *either* engine needs (D2), and instructed
that if nothing anywhere needed it, (D2) be demoted to corroborative. It is
needed: three configurations survive at ⌊m/2⌋+1, 279 with the cap gone. So **(D2) stays
CONSUMED for T-A**, and the three cells that need it are named above — they are
exactly what must be redone if 0008 is ever weakened (the same maintenance law
as 0016/0018, D-017). **T-B carries no such clause: it is (D2)-free both ways.**

**M4 came out weaker than the spec predicted** — one survivor at m = 22, not a
spread over m = 22..25. Recorded as measured rather than rounded up to the
expectation. A cap with one tooth is still a tooth, but it should be described
as one.

## What this certificate does **not** claim

- **No core is claimed to exist.** Every statement is conditional on a critical
  core at that m.
- **Nothing at X ≥ 6.** T-B says X = 5 ⟹ m ≤ 26; it says nothing about what
  happens at X = 6 anywhere.
- **X = 5 on m ∈ [22, 26] is NOT emptied.** T-B confines X = 5 to those five
  rungs and stops. That band — with m ∈ {23..26} still the window's
  arithmetic-free stretch — is now the only place a critical core can sit with
  X = 5, and it is the next field.
- **The banked alternative proofs are not consumed.** The negative-discriminant
  X ≤ 3 route and the (d−3)(d−5) X = 4 route live in the turn-15 notebook.
- **Enactment prices the lemmas, not the layers.** §2's 1,423 families price
  (DH) and (SC); nothing this lab can build has m ≥ 22, so the census layers are
  priced by the mutation suite instead — which is why every cap carries a mutant.

## Tally

**60 checks + 9 notes (stated, not tested).** 3.5 s under a bare 3.9.6, 2.6 s
under `-O`. 3,056 census runs across Theorems A and B (253,529 + 18,291 search
nodes), 1,423 enacted families, 60,416 (z,f) pairs, and **1,912 vectors emitted
in §5** — every one re-verified against all seven census constraints at the
leaf, 0 internal violations.

The reconciliation, since the two numbers count different things. The **eight
census-emitting rows** of the mutation table — M1, M1′, M3, M3′, M4, M5, M6,
M9 — account for **1,636 surviving configurations** (1,443 of them without
M1′'s 193). M2, M7 and M8 count corpus *families*, per-part *assemblies* and
*slack cases* respectively, never census leaves, which is why they contribute
nothing here. The remaining **276** are M3's pre-filter emissions: the ⌊m/2⌋+1
reading is computed as a filter over the uncapped run, which emits 279 and
keeps 3. 1,636 + 276 = **1,912**, and §5's check ties that figure to the sum of
the thirteen per-run emission totals rather than to a literal, so a future edit
that adds or reorders a census call cannot break it silently.

## Reproduce

```sh
cd certificates/0019-star-collision
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 verify.py   # bare 3.9.6
python3 -O verify.py                                       # asserts stripped
```

Both must print `60 checks + 9 notes (stated, not tested), …, ALL GREEN` and
exit 0, byte-identical modulo wall clock.
