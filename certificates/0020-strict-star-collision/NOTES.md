# Certificate 0020 — the strict star-collision inequality: X ≥ 6 everywhere, the staircase, and the m(m−25)/38 law

**Status: GREEN ×2.** 55 checks + 12 notes, ~40 s under a bare
`/usr/bin/python3` (3.9.6) and ~26 s under `python3 -O`, both outputs
byte-identical modulo wall clock; stable across `PYTHONHASHSEED` 0 / 1 / 12345
and from any working directory; exit 1 on red, proved by flipping one pinned
constant on a scratch copy. `python3 verify.py`, stdlib only, no solver, no
imports from `lib/`, reads nothing from disk. Deterministic (hand-rolled LCG,
seed 20260728). Every load-bearing bound is exact integer or `Fraction`
arithmetic.

| claim | label |
| --- | --- |
| **(q3)** distinct edges of a critical core have λ ≤ 4, q ≤ 3; hence **R ≤ 4X** | **PROVEN-BY-CERTIFICATE** (in-house: 0013 for τ = 6; mechanism = the cover lemma; **billed only to the Q law**) |
| **(BDH)** F(d(z)) ≤ s(z) for every vertex some edge avoids, F := Φ(·,5) | **PROVEN-BY-CERTIFICATE** (derived in-cert; enacted on 16,919 vertices) |
| **(SSC+)** F(d(z)) + q<sub>max</sub>(z) ≤ s(z) **for every vertex z with d(z) ≥ 2**, whenever τ ≥ q<sub>max</sub>(z) + 2 — automatic at τ = 6 | **PROVEN-BY-CERTIFICATE** (derived in-cert; enacted on 1,221 guarded vertices, with four τ = q<sub>max</sub>+1 violation witnesses as controls) |
| **(SG)** P + H ≤ R, P = Σ<sub>v</sub> F(d(v)), H = #{v : d(v) ≥ 6} | **PROVEN-BY-CERTIFICATE** (derived in-cert; the exchange identity Σ<sub>v</sub> s(v) = R enacted corpus-wide *and* per family, the inequality non-vacuously on one purpose-built family — see below) |
| **(Q)** m(m−25) + Σ5 + 10H ≤ 38X, and **(Q0)** X ≥ ⌈m(m−25)/38⌉ | **PROVEN-BY-CERTIFICATE** (residue identity + both moments + (SG) + (q3); the identity 10P = m²−25m+2X+Σ5 enacted exactly on 391 families) |
| **(H1)** H ≥ 1 for every core with m ≥ 26; hence **X ≥ 5173 at m = 456** | **PROVEN-BY-CERTIFICATE** |
| **(T-A20)** **X ≥ 6 for every critical core in [22, 456]** | **PROVEN-BY-CERTIFICATE** (0019 T-A + T-B, plus §3's 35-cell census; belt-and-suspenders on m = 27…31) |
| **(T-B20)** the staircase: X = 6 ⟹ m ≤ 26 · X = 7 ⟹ m ≤ 28 · X = 8 ⟹ m ≤ 29 · X = 9 ⟹ m ≤ 31 | **PROVEN-BY-CERTIFICATE** (§4: 92 cells, one arithmetic survivor, killed structurally) |

## Why this certificate exists

0019 proved a *linear* star-collision inequality. Fix a vertex z and an edge f
avoiding it: every edge through z must land in f, f's cell in z's own part can
take none of them, so the d(z) edges crowd into **five** fibres and the
crowding is paid for in pair excess. 0019 read that count as
(d(z) − 5)<sub>+</sub> and threw the rest away.

Keep the whole thing — the balanced-split minimum **Φ(d, 5)** — and two things
happen. First, the bound can be *sharpened at the vertex*: the largest excess a
vertex already owns can be subtracted, because f may be chosen to avoid the
whole shared set of that pair. That is **(SSC+)**, and out of it falls a
per-vertex degree cap **F(d(v)) ≤ X − q₁** that drives every sweep in this file.
Second, Φ is *quadratic*, and quadratic is exactly what the residue identity
5d + 10F(d) − d² = r(5−r) needs: summed against the two moments it produces a
**quadratic law in m and X** that reaches the far end of the window, where every
previous certificate could only reach the near end.

The result is two theorems at opposite ends of the same window. At the near end
the excess floor rises to 6 and a staircase appears; at the far end,
X ≥ ⌈m(m−25)/38⌉ — the bare law reads X ≥ 5172 at the ceiling m = 456
(38·5172 = 196536 = 456·431 exactly), and **(H1)** lifts it to X ≥ 5173,
the unit M8 prices. *(Wording corrected 2026-08-03, turn 19: this line
previously credited the bare law with 5173 — the front-page drift the
lab's own audit simulation caught; §"(H1)" below always had it right.)*

## The ledger, in full

| input | what is consumed | where |
| --- | --- | --- |
| **0019 T-A** | X ≥ 5 for every critical core in [22, 456] | a claim row, not re-proved; the base of T-A20 |
| **0019 T-B** | X = 5 ⟹ m ≤ 26 | a claim row; §3 then empties that band. **Not load-bearing** — §3 independently empties m = 27…31 |
| **0019 (DH)** | d(z) ≤ 5 + X − x_f, hence Δ ≤ 5 + X | §4's sanity intersect on the degree cap |
| **0015 (CC)** | 2 Σᵢ Φ(dᵢ−1, 5−bᵢ) ≤ 3(X − x_e), X-unrestricted — the 3/2 per-edge budget after monotonicity and flooring | **derived, and then NOT IMPOSED** (check 23) |
| **0017 check 9** | the 4/3 per-pair corner at forced excess ≤ 5 | **derived, and then NOT IMPOSED** (check 23) |
| **0017 check 12** | Σ over pairs of K − e of (s−1) = X − x_e | the assembly identity behind both budgets |
| **0017 C3** | 2m + 5x_e ≤ 52 + 3X, X-unrestricted | **load-bearing**: §4's rung ceilings (m ≤ 32, 34, 35, 37) and the per-rung cap c ≤ 3 on the largest part |
| **0013** | criticality, τ = 6, the private e-avoiding 5-covers T_e, (3a) | τ = 6 is what makes (q3) and the (SSC+) guard true at all |
| **0005** | min degree ≥ 2 | every census starts at d = 2 (also re-derived in-cert, note) |
| **0008 (D2)** | n₂ ≤ ⌊m/2⌋ | **imposed in §3 only.** §4's primary sweep runs **(D2)-free by construction** — the engine is called with the cap off — and M3 measures that switching it on moves no cell value and no survivor |
| **external** | **NONE.** No peer sketch, no citation, no published lemma. | — |

**Derived in-certificate:** Φ / F / w and their monotonicity · **the two
moment identities** Σ<sub>v</sub> d(v) = 6m and Σ<sub>v</sub> C(d(v),2) =
C(m,2) + X, both by double counting (§2 note) · the b = 5 covering branch
(§2 note) · both per-edge budgets · **(q3)**, **(BDH)**, **(SSC+)**,
**(SG)**, **(Q)**, **(Q0)**, **(H1)** · the star identity
s(v) = Σ<sub>i : v ∈ Sᵢ</sub> qᵢ · **the key cap F(d(v)) ≤ X − q₁**.

**Re-derived, not cited.** 0019's internal lemmas — (L-a) no universal vertex,
(L-b) n ≥ 36, (L-c) the n₂ reading of 0008, (L-d) w-monotonicity — are *not*
claim rows of 0019, so they are re-derived here rather than imported. They
appear as the three `STATED, NOT TESTED` notes of §2 and as check 3.

**Not consumed:** 0018 · 0017 C2 · any solver.

**Billing.** **(q3) is spent on R ≤ 4X and nowhere else.** Both censuses
enumerate *every* partition — parts ≤ 5 in §3, parts ≤ min(3, c) by **C3** in
§4 — and let the census kill the wide rows itself. Mutant M6 measures the
billing directly: permitting q ≤ 4 in the Q chain costs 1,078 units at the
ceiling and changes **nothing** in §3.

**Two ledger rows are derived and then not imposed, and say so.** 0015 (CC)
and 0017 check 9 are both derived here and **neither is imposed in §3's
engine**. The justification for dropping them is that omitting a constraint
*widens* the census, and a wider census can only *lower* min S — so every kill
in §3 holds **a fortiori** without them. Check 23 additionally tabulates,
branch by branch, that the single-degree reading of each budget (an on-f
degree capped at capF(budget) + 1, which since ⌊(3/2)k⌋ ≥ k with capF
non-decreasing sits at least one degree above capF(X − q₁)) is weaker than the
key cap. That is a *per-vertex* observation and it is kept as the secondary
thing it is: both budgets are **sums** over the six cells of f, and a
per-vertex comparison does not show the sum is slack. The certificate stands
with those two rows removed, and the rows are kept as derived-not-imposed
rather than dropped (D-032).

---

## The analytic proofs

Throughout: K is edge-critical, 6-partite (V₁…V₆), 6-uniform, intersecting,
τ(K) = 6, τ(K − e) = 5, m ∈ [22, 456]. A **vertex** is a cell (part, value).
λ(e,f) = |e ∩ f| ≥ 1, q = λ − 1, X = Σ<sub>pairs</sub> q,
x_e = Σ<sub>f≠e</sub> q(e,f) with Σ_e x_e = 2X. Φ(n,k) is the balanced-split
minimum of Σ C(n_j, 2); **F(d) := Φ(d, 5)**; w(d) := Φ(d−1, 5) = F(d−1).
E(z) is the set of edges through z; **s(z)** := Σ over pairs inside E(z) of q
(the *star excess*); **q<sub>max</sub>(z)** := the largest such q.
**P** := Σ_v F(d(v)), **H** := #{v : d(v) ≥ 6}, **R** := Σ<sub>pairs</sub> q(q+1),
**Σ5** := Σ_v r(5−r) with r = d(v) mod 5.

**The two moment identities**, used everywhere and now billed (§2 note, both
by double counting). *First moment:* count incident (vertex, edge) pairs —
each edge is 6 cells, so the count is 6m, and each vertex lies in d(v) edges,
so it is also Σ_v d(v). Hence **Σ_v d(v) = 6m**. *Second moment:* count
triples (v, {e,f}) with v ∈ e ∩ f, e ≠ f — through each vertex there are
C(d(v),2) such pairs, and each pair is counted |e ∩ f| = q + 1 times. Hence
**Σ_v C(d(v),2) = Σ<sub>pairs</sub>(q+1) = C(m,2) + X**, equivalently
Σ_v d(v)² = m² + 5m + 2X. They are enforced in every cell of both engines and
they pin the definition of X itself, which is why they are in the ledger.

### (q3) λ ≤ 4, q ≤ 3, and R ≤ 4X

Suppose λ(e, f) = 5. Then e and f agree in five parts and differ in one, say
part i. Let h be any edge. If h avoided all five common cells, then h ∩ e ⊆
{part i}, so h_i = e_i; and h ∩ f ⊆ {part i}, so h_i = f_i. But e_i ≠ f_i.
So every edge meets the five common cells: they are a **5-cover**, and
τ(K) ≤ 5 < 6. Contradiction. Hence λ ≤ 4 and q ≤ 3 for every pair.

Then q(q+1) ≤ 4q exactly when q ≤ 3, with equality at q = 3, so
R = Σ q(q+1) ≤ 4 Σ q = 4X. One λ = 5 pair breaks it: the triple
(0,0,0,0,0,0), (0,0,0,0,0,1), (0,0,0,0,1,2) has q = (4,3,3), X = 10 and
R = 44 > 40 (check 20 — and its τ is 1, so it is not a core).

The cover lemma is enacted on **18,566** λ = r−1 pairs across the corpus,
against **380,929** (pair, other-edge) tests, with zero exceptions (check 11).

### (BDH) F(d(z)) ≤ s(z)

Fix a vertex z and an edge f with z ∉ f (one exists unless z is universal, and
a universal vertex is a 1-cover against τ = 6). Every e ∈ E(z) meets f. Put
r_u := |{e ∈ E(z) : u ∈ e}| for u ∈ f, so Σ<sub>u ∈ f</sub> r_u ≥ d(z).

**The part-mate is empty.** Let u* be f's cell in z's own part. No e ∈ E(z)
contains u*, because e's cell in that part is z ≠ u*. So at most **five** of
the six fibres are non-empty, and by definition of Φ as the balanced-split
minimum, together with Φ(·,5) being non-decreasing,

  Σ<sub>u</sub> C(r_u, 2) ≥ Φ(Σ<sub>u</sub> r_u, 5) ≥ Φ(d(z), 5) = F(d(z)).

The left side is *exactly* Σ over pairs {e,g} ⊆ E(z) of |e ∩ g ∩ f| — count,
for each u, the pairs of E(z)-edges through it. And z ∈ e ∩ g while z ∉ f, so
|e ∩ g ∩ f| ≤ λ(e,g) − 1 = q<sub>eg</sub>. Summing, F(d(z)) ≤ s(z). ∎

Two edges in the same fibre share both z and u, so their q is at least 1 —
which is what licenses charging C(r_u, 2) to the excess at all. The mechanism
is enacted on **98,951** (z, f) pairs: part-mate empty every time, the identity
exact every time, Φ-minimality every time (check 12).

### (SSC+) F(d(z)) + q<sub>max</sub>(z) ≤ s(z), under τ ≥ q<sub>max</sub>(z) + 2

Let {e*, g*} ⊆ E(z) realise q<sub>max</sub>(z), so |e* ∩ g*| = q<sub>max</sub> + 1
and z ∈ e* ∩ g*. **If e* ∩ g* is not a cover**, choose f avoiding all of it —
such an f automatically avoids z. Run the (BDH) count with that f. The pair
{e*, g*} now contributes |e* ∩ g* ∩ f| = 0 instead of ≤ q<sub>max</sub>, so

  F(d(z)) ≤ Σ<sub>pairs ⊆ E(z)</sub> |e ∩ g ∩ f| ≤ s(z) − q<sub>max</sub>(z). ∎

**The threshold.** e* ∩ g* is *guaranteed* not to be a cover as soon as
τ > |e* ∩ g*| = q<sub>max</sub> + 1, i.e. **τ ≥ q<sub>max</sub> + 2**. That
direction is the one the proof uses and the whole of the hypothesis, and it is
*τ-relativised*: not τ ≥ 3, not τ ≥ 6. (The converse is *not* claimed — a set
of size q<sub>max</sub>+1 can fail to cover while τ ≤ q<sub>max</sub>+1. What
is claimed about sharpness is what the four witnesses below establish: no
smaller τ-threshold will do.)

**At τ = 6 it is automatic, and free of (q3).** Two *distinct* 6-tuples agree
in at most five coordinates, so λ ≤ 5 and **q ≤ 4** for any two distinct edges
whatever — no criticality, no cover lemma. Hence q<sub>max</sub> + 2 ≤ 6 = τ.
(q3) sharpens q ≤ 4 to q ≤ 3, but (SSC+) never asks for it, and the censuses
below carry the q = 4 and q = 5 rows precisely so that nobody can claim it did.

**The four violation witnesses** (check 19, must-fail control 2). Take
AG(2,q) — the affine plane of order q read as a (q+1)-partite (q+1)-uniform
intersecting family: the edge of a point records, for each of the q slopes,
the label of the line of that slope through it, plus the vertical line. Two
distinct points lie on exactly one common line, so every λ is 1.
Now pick a point x, rename its *vertical* coordinate onto a brand-new twin
edge e′, and delete the other q−1 points of the vertical line through x. Then:

* e′ and T(x) share q cells, so q(e′, T(x)) = q − 1 = q<sub>max</sub>;
* those q cells are a **minimum** cover, so **τ = q = q<sub>max</sub> + 1 exactly**
  (computed exactly in-run by minimum cover, not asserted);
* every shared cell z has d(z) = q + 1 (the q surviving points of its line,
  plus e′), s(z) = q<sub>max</sub> = q − 1, and Φ(d(z), q) = 1;
* so (SSC+) would read 1 + (q−1) ≤ q−1 and **fails by exactly one unit**.

q = 2, 3, 4, 5 give witnesses at q<sub>max</sub> = 1, 2, 3, 4 — every value the
window can carry — with 2, 3, 4, 5 violating vertices respectively. F₄ is built
from an explicit multiplication table. The guard is therefore sharp at every
q<sub>max</sub>, and could not have been weakened to τ ≥ 3.

Corpus-wide the same reading holds: **1,221** guarded vertices, zero failures;
**9,380** unguarded vertices, of which **74 actually violate** (check 14).

### (SG) P + H ≤ R

Sum (SSC+) over every vertex — legitimate in a core, where the guard holds at
every vertex. Σ_v F(d(v)) + Σ_v q<sub>max</sub>(v) ≤ Σ_v s(v).

**The right side is R.** A pair {e,g} lies inside E(v) for exactly the
|e ∩ g| = q + 1 cells it shares, so Σ_v s(v) = Σ<sub>pairs</sub> q(q+1) = R.
(Measured on both sides independently and equal — **corpus-wide and also
family by family**, so compensating errors across families cannot pass:
check 16.)

**The left side dominates P + H.** For any vertex with d(v) ≥ 6 we have
F(d(v)) ≥ 1, hence by (BDH) s(v) ≥ 1, hence *some* pair inside E(v) is
excessive, hence q<sub>max</sub>(v) ≥ 1. Every other vertex contributes
q<sub>max</sub> ≥ 0. So Σ_v q<sub>max</sub>(v) ≥ H and P + H ≤ R. ∎

The one-line step is enacted with (BDH): **2,331** high vertices in the
corpus, none with s(z) = 0 (check 13, where that population is now *pinned*
rather than merely reported non-empty). The +H term is not decoration —
mutant **M1** reopens **17 of §3's 35 cells** when it is dropped.

**The two halves of (SG) are enacted to different depths, and check 16 says
so.** The exchange identity runs non-vacuously, corpus-wide and per family. The
*inequality* P + H ≤ R read **0 ≤ 0 on all 70 guarded families** of the first
draft's corpus — whose only high-τ objects were the affine planes AG(2,q),
degrees all q = r−1, so Φ(d, r−1) = 0 at every vertex and P = H = R = 0. The
corpus therefore gained one purpose-built family that satisfies the guard
**non-vacuously**: `fat_plane(3, …)`, AG(2,3) with a sixth part appended that is
constant on all but three *non-collinear* points. That cell has degree 6 ≥ r = 5,
so Φ(6,4) = 2 and the vertex is high; the three excluded points get private
values and, not being collinear, are covered by no single cell, so τ stays at
**3 = q<sub>max</sub> + 2** and the guard holds. It reads **P + H = 3 ≤ R = 30**,
with τ, q<sub>max</sub> and every count computed in-run. One family is one
family: the inequality's real backing is the proof above plus the mutation
suite, and check 16 says that too.

### The residue identity, (Q), (Q0), (H1)

Write d = 5q + r. Then 10F(d) = 25q² + 10qr − 25q and d² = 25q² + 10qr + r², so

  **5d + 10F(d) − d² = r(5 − r)**, taking the values 0, 4, 6, 6, 4.

Checked exactly on d = 0…600 (check 4); mutating the constant to r(4−r) breaks
it at 480 of those 601 degrees (M7). Summing over the vertices,

  5·6m + 10P − (m² + 5m + 2X) = Σ5,  i.e. **10P = m² − 25m + 2X + Σ5**,

enacted as an *equality* on all 391 r = 6 corpus families (check 17). With
(SG) P + H ≤ R and (q3) R ≤ 4X:

  10P + 10H ≤ 10R ≤ 40X  ⟹  **m(m−25) + Σ5 + 10H ≤ 38X**.  **(Q)**

Σ5 ≥ 0 and H ≥ 0 give **(Q0) X ≥ ⌈m(m−25)/38⌉**: 13 at m = 38, 236 at m = 108,
2310 at m = 309, **5172 at m = 456**. (Q0) overtakes this certificate's X ≥ 6
at **m = 33** — the staircase is a low-m instrument and (Q) owns the rest.

**(H1).** If H = 0 then every degree is ≤ 5, so F(d(v)) = 0 everywhere and
P = 0; the identity then reads m(m−25) + 2X + Σ5 = 0 with all three terms
non-negative at m ≥ 26. Impossible. So 10H ≥ 10 and
X ≥ ⌈(m(m−25) + 10)/38⌉. **At m = 456: 456·431 = 196536 = 38·5172 exactly**, so
the ten units of a single high vertex lift the floor by one — **X ≥ 5173**.

**And that floor is nowhere near tight** (stated, not claimed, §5). Put
X = 5172 back into (Q): it forces Σ5 = 0 *and* H = 0, so every degree is ≤ 5
and Σ d² ≤ 5·6m = 13,680 — against the m² + 5m + 2X = **220,560** the second
moment requires. A factor of sixteen. The true floor at the ceiling is far
above 5173, and the next lever is the joint consistency of H's size with the
degree distribution, not another constant in (Q).

### The key cap: F(d(v)) ≤ X − q₁ for every vertex

Let q₁ be the largest pair excess and P₁ = {e₁, g₁} a pair realising it, with
shared set S₁ = e₁ ∩ g₁.

* **v ∈ S₁.** Then both e₁ and g₁ pass through v, so P₁ ⊆ E(v) and
  q<sub>max</sub>(v) ≥ q₁. (SSC+) gives F(d(v)) ≤ s(v) − q<sub>max</sub>(v)
  ≤ X − q₁, since s(v) ≤ X always.
* **v ∉ S₁.** Then P₁ is *not* inside E(v), so s(v) ≤ X − q₁, and (BDH) gives
  F(d(v)) ≤ s(v) ≤ X − q₁.

Either way **F(d(v)) ≤ X − q₁**, i.e. d(v) ≤ capF(X − q₁), where
capF(b) = max{d : F(d) ≤ b} reads 5, 6, 7, 8, 9, 10 at b = 0…5. This one line
is the degree ceiling of every cell in §3 and §4, and it is what kills the wide
partitions: mutant **M2** relaxes it by one degree and the census-infeasible row
(4,1) at m = 22 becomes both feasible *and* alive.

---

## The engines, exactly as encoded

### §3 — T-A20: the X = 5 field on m = 22…26

For each of the **seven** partitions π of 5 (parts ≤ 5 — the wide rows are
carried, not deleted) and each m = 22…26, enumerate every integer census
(n₂ … n<sub>Δ</sub>) with

* Σ d n_d = 6m and Σ d² n_d = m² + 5m + 10 (both moments, X = 5),
* Σ n_d ≥ 36 (0019 (L-b) re-derived),
* n₂ ≤ ⌊m/2⌋ (0008 (D2)),
* 2 ≤ d ≤ Δ(π) = min(capF(5 − q₁), capF(4)),

and **minimise S = P + H = Σ_d (F(d) + [d ≥ 6]) n_d**. (SG) caps S at R(π), so
`min S > R(π)` kills the cell. The second term of Δ is the (SSC+) ceiling that
holds at any high vertex whatever q₁ is: F(d) + 1 ≤ s ≤ X = 5 ⟹ F ≤ 4 ⟹ d ≤ 9
— and said plainly, that term is just the q₁ = 1 case of the first and **never
binds**, since q₁ ≥ 1 always. It is kept to show the ceiling is free, not
because it does work.

**What the key cap adds to 0019 (DH) is coverage, not tightness.** The off-f
cap 10 − q₁ from (DH) does *not* sit above Δ(π): it **coincides exactly** with
it at every q₁ (9/8/7/6/5 against 9/8/7/6/5), because F(d) = (d−5)₊ on this
range. What (DH) cannot do is apply everywhere — it caps only the vertices
that some q₁-pair edge *avoids*, while the key cap also covers the S₁ vertices,
which no q₁-pair edge avoids, and that is what licenses capping **every**
degree. The two on-f budgets from 0015/0017 are **not imposed at all**;
omitting them is conservative (a wider census can only lower min S, so every
kill holds a fortiori). Check 23 carries all three columns and asserts the
coincidence.

Measured, 35 cells, zero survivors:

| π | Δ | R | min S at m = 22, 23, 24, 25, 26 | margins |
| --- | --- | --- | --- | --- |
| (5) | 5 | 30 | census **infeasible** at every m | — |
| (4,1) | 6 | 22 | census **infeasible** at every m | — |
| (3,2) | 7 | 18 | 21, 23, 23, 24, 27 | 3, 5, 5, 6, 9 |
| (3,1,1) | 7 | 16 | 21, 23, 23, 24, 27 | 5, 7, 7, 8, 11 |
| (2,2,1) | 8 | 14 | 16, 16, 16, 19, 20 | **2, 2, 2**, 5, 6 |
| (2,1,1,1) | 8 | 12 | 16, 16, 16, 19, 20 | 4, 4, 4, 7, 8 |
| (1,1,1,1,1) | 9 | 10 | 13, 14, 14, 15, 15 | 3, 4, 4, 5, 5 |

**Belt and suspenders.** The same census empties X = 5 on m = 27…31 as well
(C3 caps X = 5 at m ≤ 31): min S = 20, 23, 25, 30, 35 on the matching row
against R = 10, and larger on the wider rows. So T-A20 does *not* actually lean
on 0019 T-B — if T-B were withdrawn, X ≥ 6 would survive on §3 alone.

### §4 — T-B20: the staircase

**Rung ceilings first, by C3.** 2m + 5x_e ≤ 52 + 3X with Σ_e x_e = 2X > 0
forcing some edge to carry x_e ≥ 1 kills a rung as soon as
c(X, m) = ⌊(52 + 3X − 2m)/5⌋ ≤ 0 — at m = 33, 35, 36, 38 for X = 6, 7, 8, 9.
Each band is exactly six rungs wide, and **c ≤ 3 on every rung**, which is why
the partition enumerator here uses parts ≤ min(3, c): **C3, not (q3)**.

For each (X, m, π) cell — 92 of them — run the **second-moment maximiser**:
the largest Σ d² n_d any census can reach under

* Σ d n_d = 6m, Σ n_d ≥ 36, 2 ≤ d ≤ min(capF(X − q₁), 5 + X),
* the **per-partition (SG) budget** Σ<sub>d ≥ 6</sub> (F(d) + q<sub>min</sub>) n_d ≤ R(π).

That list is the whole list: **n₂ ≤ ⌊m/2⌋ is not among it.** 0008 is billed to
§3, so this engine is called with the cap off and the staircase is (D2)-free
*by construction*; M3 switches it on and measures that no cell value and no
survivor moves.

The budget is **not** (SG) itself restricted to the high vertices — that would
be Σ(F(d) + 1) n_d ≤ R, and for every π with q<sub>min</sub> ≥ 2 the coded
budget is strictly stronger. What it is, is the **un-weakened line that (SG)'s
own proof passes through**, Σ_v F(d(v)) + Σ_v q<sub>max</sub>(v) ≤ Σ_v s(v) =
R (displayed above), restricted to the high vertices: every high vertex has
q<sub>max</sub>(v) ≥ 1 by (BDH), and q<sub>max</sub>(v) is the excess of an
*actual* pair, hence at least the smallest part q<sub>min</sub> of π. (SG)
drops that q<sub>max</sub> to 1; this engine does not, and for q<sub>min</sub>
≥ 2 that is a real strengthening — which is why it is named here rather than
looked for in the claim table, where only P + H ≤ R appears. The cell dies
when the maximum falls short of the required m² + 5m + 2X.

The maximiser is exact, not a relaxation: it enumerates the high degrees
(each costs ≥ 2 of the budget) and solves the low half in closed form via the
identity Σ d² n_d = 42m − 10n − 2n₃ − 2n₄ + Σ<sub>d≥6</sub> exc(d) n_d, valid
whenever Σ d n_d = 6m, with exc(d) = (d−2)(d−5). Its n₃, n₄ ≤ 6 window is
justified in the docstring by an exchange argument and, because that argument
needs n₂ headroom, also **measured**: widening the window to 0…60 on all 92
cells, with (D2) on and off, moves no value. **Every reported optimum is
re-verified from scratch against all six constraints** (check 30 — six, not
seven: n₂ ≤ ⌊m/2⌋ is deliberately not re-checked, since the sweep never
imposed it).

**And it is cross-asserted** (check 31). The closed form and the early break
could in principle *understate* an optimum, and understating is the dangerous
direction: it would kill cells the lemmas do not kill, and check 30 could not
see it, since a valid-but-suboptimal witness passes every constraint. So eight
cells — **the survivor, the thinnest arithmetic kill in each of the four
bands** ((8,30,(3,2,2,1)), (7,29,(3,3,1)), (6,27,(3,2,1)), (9,32,(3,3,2,1)))
**and the widest partition at three of the four band tops** — are re-maximised
in-run by a **second, deliberately stupid maximiser**: brute recursion over
every degree, no closed form, no early break, no shared code path. All eight
agree exactly. The same comparison was run offline on **all 92 cells, also
with zero disagreements**; that costs about 70 s, so eight are kept in-run for
the clock and the other 84 are recorded as a `STATED, NOT TESTED` note rather
than asserted inside a green check label.

**Result: 92 cells, 91 arithmetic kills, exactly one survivor.**

| band | rungs | cells | thinnest kill |
| --- | --- | --- | --- |
| X = 6 | 27…32 | 21 | 12, at (6, 27, (3,2,1)) |
| X = 7 | 29…34 | 19 | **4**, at (7, 29, (3,3,1)) |
| X = 8 | 30…35 | 27 | **2**, at (8, 30, (3,2,2,1)) — 1064 vs 1066 |
| X = 9 | 32…37 | 25 | 16, at (9, 32, (3,3,2,1)) |

The survivor is **(X, m, π) = (8, 30, (3,3,1,1))**, which reaches 1076 against
the required 1066.

### The exceptional cell, killed structurally

q = (3,3,1,1); shared sets S₁…S₄ of sizes 4, 4, 2, 2; c = 3; required Σ d² =
1066; Δ = capF(5) = 10.

**(i) Which pairs may share an edge.** If Pᵢ and P_j share an edge e then
qᵢ + q_j ≤ x_e ≤ c = 3. Only {P₃, P₄} (1 + 1 = 2) qualifies.

**(ii) |Sᵢ ∩ S_j| ≤ 1 for i ≠ j.** Suppose u, v ∈ Sᵢ ∩ S_j.

* *Pᵢ, P_j edge-disjoint.* Then all four edges contain u and v, so **all six**
  pairs among them are excessive — π would need six parts and it has four.
  **That count is the argument, and it is what the code tests.** (For index
  pairs with qᵢ ≥ 2 there is an independent route — each of eᵢ, gᵢ then lies
  in three excessive pairs, so x ≥ qᵢ + 2 ≥ 4 > 3 = c. At {3,4}, where
  q₃ = q₄ = 1, that route gives only x ≥ 3 = c and does **not** close, which
  is precisely why `licensed_ii`'s Case A conjoins k ≥ 6 rather than leaning
  on the x-bound.)
* *Pᵢ, P_j share an edge* — by (i) only {P₃, P₄}, say P₃ = {e,g}, P₄ = {e,h}.
  Then u, v ∈ g ∩ h, so {g, h} is a fifth excessive pair; it must be P₁ or P₂
  (q = 3), and then g lies in two excessive pairs with x_g ≥ 3 + 1 = 4 > 3.

Both die. **This is the repair** — of the review defect recorded once, in
Provenance below, and priced by mutant M9. `licensed_ii()` re-derives the
exclusion mechanically for any (π, c), and check 33 runs it on all six index
pairs of this cell *and* on the review's (3,3,2), where it confirms that no
index pair may share an edge at all.

**(iii) Every high vertex has |T_v| ≥ 2, and its degree is capped by T_v.**
Write T_v = {i : v ∈ Sᵢ}. All excess sits in the four listed pairs, so the
**star identity** s(v) = Σ<sub>i ∈ T_v</sub> qᵢ holds *exactly*, and
q<sub>max</sub>(v) = max<sub>i ∈ T_v</sub> qᵢ. If |T_v| ≤ 1 then
s(v) = q<sub>max</sub>(v) and (SSC+) forces F(d(v)) ≤ 0, i.e. d(v) ≤ 5 — not
high. Otherwise d(v) ≤ capF(s(T_v) − q<sub>max</sub>(T_v)):

| T_v | s − q<sub>max</sub> | d ≤ | exc(d) |
| --- | --- | --- | --- |
| {1,2} | 3 | 8 | 18 |
| {1,3}, {1,4}, {2,3}, {2,4}, {3,4} | 1 | 6 | 4 |
| {1,2,3}, {1,2,4} | 4 | 9 | 28 |
| {1,3,4}, {2,3,4} | 2 | 7 | 10 |
| {1,2,3,4} | 5 | 10 | **40** |

**(iv) Each index pair hosts at most one high vertex** — immediately from (ii),
since a vertex with {i,j} ⊆ T_v lies in Sᵢ ∩ S_j. So the T_v's form a *linear
system* on the four parts.

**(v) The profile maximiser.** Enumerate every legal profile (a set of index
sets, pairwise sharing at most one index) and maximise Σ (d−2)(d−5).
**MAXHIGH = 40**, attained by one vertex with T_v = {1,2,3,4} at degree 10 —
and also, *within the relaxed profile space the enumerator searches*, by
{1,2,3} at degree 9 plus the three sets containing 4 (28 + 4 + 4 + 4). That
second profile is **not realisable**: it puts three distinct high vertices in
S₄ and |S₄| = q₄ + 1 = 2. The enumerator deliberately omits the
|Sᵢ| ≤ qᵢ + 1 slot cap, which can only *raise* MAXHIGH and therefore only
weaken the bound — the safe direction — and it changes nothing here, since the
{1,2,3,4} witness needs exactly one slot in each Sᵢ. Then, using
Σ d² = 42m − 10n + Σ exc and n ≥ 36 with exc(d) ≤ 0 for d ≤ 5,

  **Σ d² ≤ 42·30 − 360 + 40 = 940 < 1066.**  **DEAD**, by 126.

**(vi) Corroboration.** The same maximiser on the other three heavy cells:
(6,27,(3,3)) MAXHIGH 18, 792 vs 876 · (7,29,(3,3,1)) MAXHIGH 28, 886 vs 1000 ·
(9,32,(3,3,3)) MAXHIGH 54, 1038 vs 1202. All dead, all with (ii) independently
licensed — and all three were already dead arithmetically, so the structural
layer is corroboration there and **load-bearing only at (8,30,(3,3,1,1))**.

### The m ≤ 25 by-product — measured, not claimed

Running the X = 6 machinery one rung lower, at m = 26, kills every partition
except (3,2,1), which survives the arithmetic by 4 (822 against 818) and then
dies to the profile maximiser (MAXHIGH 18, bound 750 against 818). So
**X = 6 ⟹ m ≤ 25 is measured**. It is *not* claimed: single-route, leaning on
the structural layer at a rung nothing else corroborates, and the desk spec's
own expectation for it (a clean arithmetic kill at margin 8) did not reproduce.
This certificate claims X = 6 ⟹ m ≤ 26 and stops.

---

## One model comparison — and which model governs

*Corrected 2026-07-28 under D-036. An earlier version of this section declared
the review's rows "withdrawn", called the disagreement "a spec error rather
than an engine error", and asserted that no plausible cap set reproduces them.
All three statements were wrong, and wrong in the direction that deflates
correct peer work. The retraction is kept here rather than quietly edited out.*

The desk spec carried the outside review's own §3 min-S table —
13,14,14,15,15 / 15,15,16,17,19 (twice) / 19,21,21,24,25 (twice) — and
transcribed it faithfully. **Those rows are correct under the model the review
states**, which is written out in the received text: a **global** Δ ≤ 9 from
(SSC+), the 0019 off-f cap d ≤ 10 − t on the vertices some q₁-pair edge
avoids, and the 0017 4/3 budget Σ<sub>v ∈ f</sub> w(d(v)) ≤ ⌊(4/3)(5−t)⌋ on
the six cells of f. Re-run under that model, they reproduce.

**This file runs a different model** — the per-partition key cap
F(d(v)) ≤ X − q₁ imposed at *every* vertex, with **no on-f budget imposed at
all** — and returns **16,16,16,19,20** on the q₁ = 2 rows and
**21,23,23,24,27** on the q₁ = 3 rows: uniformly larger, i.e. **wider kills**.
The q₁ = 1 row and the whole m = 27…31 extension (20/23/25/30/35) agree with
the review exactly.

Neither table is an error. They price different constraint sets, and **this
certificate is governed by its own**: the spec's "three one-unit cells" do not
exist here — the thinnest §3 margin is **2**, at (2,2,1) on m = 22, 23, 24.
*(The tightness control the spec calls "PG(2,5) minus a point" is built and
named here as its dual, the 6-partite **AG(2,5)** — verified identical
firsthand. The desk spec's other unreproduced numbers are recorded once, in
`verify.py`'s honesty note (2).)*

## The mutation table (§6 — ten mutants in twelve measured readings)

Every **reddens** entry below is a check number *captured from the run*, not a
literal, and check 51 asserts that every check number this document and
`verify.py` cite equals the number the run actually assigned — so a
renumbering reddens rather than silently rotting the prose. The four rows that
formerly carried hardcoded pointers (M6, M7, M8, M10) were **all four wrong**;
the sets below were measured by carrying each mutation into a scratch copy and
recording which checks failed.

| mutant | reddens | measured effect |
| --- | --- | --- |
| **M1** +H dropped from S (S := P) | check 24 | **17 of 35** §3 cells reopen, on every narrow partition and every rung 22…26 |
| **M2** Δ relaxed by one degree | check 24 | **10** cells reopen — (2,2,1), (3,1,1), (3,2) on m = 22…24, **plus the wide row (4,1) at m = 22**, which is census-*infeasible* at the true cap |
| **M3** (D2) relaxed in §3, imposed in §4 | check 24 | §3 +1: **0** reopen. §3 dropped: **11** reopen, all at m = 22 and 23, incl. (4,1). §4 with the cap switched **on**: same 92 cells, same single survivor, **every maximum identical** to the (D2)-free primary run |
| **M4** n ≥ 36 → n ≥ 35 | checks 24, 29 | §3: **13** reopen. §4: survivors **1 → 5**, adding (7,29,(3,3,1)) and three more partitions at (8,30) |
| **M5** six fibres, F := Φ(·,6) | check 24 | **29 of 35** §3 cells reopen; only the (5) row (still infeasible) and (1,1,1,1,1) at m = 26 survive the mutation. Corpus: 62 vertices where the five-fibre bound is tight and the six-fibre one would not be |
| **M6** q ≤ 4 in the Q chain (R ≤ 5X) | checks 9, 38, 39, 40 | ceiling floor **5173 → 4095** (−1,078). **§3 completely inert**, and inert at check 5 too — which is what correct billing looks like from outside |
| **M7** residue r(5−r) → r(4−r) | check 4 | identity fails at **480 of 601** degrees |
| **M8** ceil → floor in (Q0)/(H1) | checks 9, 39, 40 | 5173 → 5172, and **all 435** window rungs report a strictly weaker floor |
| **M9** (8,30) partition list cut to {(3,3,2)} — the review's own §7.2 list | check 29 | sweep returns **0 survivors** — a **false all-clear** (the defect itself is recorded once, in Provenance) |
| **M10** \|T_v\| ≥ 2 dropped | checks 34–37 (and, downstream of the changed MAXHIGH, 50 and 52) | **two readings**, below |

**M10, in full, because the spec asked for a measurement and got two.**
*Literal reading* — delete the |T_v| ≥ 2 filter from the profile enumerator and
keep the (SSC+) cap: **MAXHIGH is unchanged at 40**. The mutant is **inert**,
because a singleton index set has s = q<sub>max</sub> and (SSC+) then caps such
a vertex at d ≤ 5, so it cannot be high at all. |T_v| ≥ 2 is a *derived label*,
not an assumption, and the spec's "≥ 74" does not reproduce under it.

*Faithful reading* — withdraw step (iii) itself, so every vertex is capped only
by (BDH), F(d) ≤ s(T_v): a singleton on a q = 3 pair then reaches d = 8 and
exc = 18, and (iv) does not limit how many such vertices exist, since they
consume no index pair. Nothing bounds the *number* of singletons — but the
certificate's own geometry bounds the slots: |Sᵢ| = qᵢ + 1 gives **4, 4, 2, 2**,
and every vertex occupies one slot in each Sᵢ of its index set. Two numbers,
both measured in-run:

* the enumerator visiting each index set at most once returns **206**;
* the same enumerator with the slot cap, allowing a set to be reused while the
  slots last, returns **190**.

The kill fails as soon as the maximum reaches 1066 − 900 = **166**, and
190 > 166, so **the faithful mutant does break the kill**: the bound becomes
1090 against the required 1066. The run prints the realisable witness —
vertices on {2,3,4}, {1,2}, {1,3}, {1,4} at d = 10, 10, 9, 9 plus three
singletons at d = 8, filling all 4 + 4 + 2 + 2 slots with the six index pairs
distinct. A {1,2,3,4} vertex plus singletons is *not* the maximiser: it leaves
3 + 3 = 6 singleton slots and 40 + 6·18 = **148 < 166**. **The step is
load-bearing; the literal filter is not.**

## Margins — every coordinate, named (D-035)

* **§3, thinnest: 2 units, three times** — π = (2,2,1) at m = 22, 23, 24, with
  min S = 16 against R = 14.
* **§3, wide rows** — (4,1) and (5) are killed by *infeasibility*, not by a
  margin; M2 shows how close (4,1) at m = 22 is to feasible.
* **§4, thinnest arithmetic: 2 units** — (8,30,(3,2,2,1)), 1064 against 1066.
* **§4, the survivor** — (8,30,(3,3,1,1)) has **no arithmetic margin at all**;
  it clears the requirement by 10, and dies only structurally, with 126 to
  spare. This is the certificate's real exposure, and M10 prices it.
* **The Δ cap** — one degree of relaxation reopens **10** §3 cells, including
  the wide row (4,1) at m = 22, which is census-*infeasible* at the true cap.
  Priced at **M2**.
* **(D2)** — §3 only, and **not tight even there** (M3, +1 reopens nothing).
* **n ≥ 36** — exposed on both engines (M4), the widest-reaching single input.
* **(Q0) at the ceiling** — 5173, and demonstrably far from tight (§5).

**No census cell and no structural kill** in this certificate turns on a single
unit, which is a change from 0018 and 0019. The exposure has moved from
arithmetic thinness to the structural step. **The one place a single unit
decides an answer is (H1) at m = 456**: 456·431 = 196536 = 38·5172 exactly, so
the ten units of one high vertex are the whole of the 5172 → 5173 lift, and M8
measures the cost of getting that rounding wrong as exactly 1. §5 shows the
true floor there is far above either number, so the exposure is cosmetic — but
it is named rather than covered by a blanket sentence.

## Provenance — the outside-audit lane's third fruit

**Seven of the eight claim rows were proposed by an outside audit** (GPT 5.6
Sol Pro, third audit, 2026-07-28, reading the public repo), delivered as full
proof text, retained verbatim at
`notebook/raw/2026-07-28-received-turn16-gpt-pro-ryser-2.md` — the first file
kept under D-038's retention clause. Its "suggested claim rows" table lists
seven: **(q3)/R ≤ 4X · (BDH) F ≤ s · (SSC+) F + q<sub>max</sub> ≤ s · (SG)
P + H ≤ R · the (Q) law · X ≥ 6 window-wide · the four rung ceilings.**

**The eighth is this desk's own.** **(H1)** — and hence X ≥ 5173 rather than
the review's X ≥ 5172 at m = 456 — appears nowhere in the received text: its
executive verdict, its §5 comparison table and its final assessment all stop at
⌈m(m−25)/38⌉, and it does not observe that H = 0 forces P = 0 and contradicts
the identity at m ≥ 26. Giving that away would be an attribution error in the
generous direction, and **D-036 makes attribution accuracy symmetric**.

Per **D-036** the received text entered no chain:

* the desk re-derived every step independently;
* the blind lanes received **statements plus one-line mechanisms only** — two
  blind lemma lanes (both proved all six statements), a blind X = 5 lane and a
  blind staircase lane (both proved their theorem, and **the staircase lane
  found and killed the exceptional cell the review missed**), plus numeric and
  dependency lanes;
* three **verbatim-file refuter lanes** were told to break it.

**All three refuters found the same real defect** — **one defect with two
consequences.** The review's §7.2 table names (3+3+2) as the only remaining
excess partition at (8,30), so the list is **incomplete**: it omits
**(3,3,1,1)** — the survivor — and **(3,2,2,1)** — the thinnest kill. And
*because* the list is incomplete, its edge-disjointness sentence becomes false:
that sentence is **true of the partitions it listed** (at (3,3,2) every index
pair has qᵢ + q_j ≥ 5 > 3 = c, so edge-disjointness really is forced) and
fails only at the omitted (3,3,1,1), where {P₃,P₄} may share an edge. Its
two/three-set H-rule likewise has **no four-set row**. The repair — the T_v
profile maximiser of §4 — was found **in-house by three lanes independently**
and is what §4 encodes. Mutant M9 prices the omission directly: truncating the
partition list to the review's single entry produces a false all-clear.

The review's §7.1 X = 6 row also mixes cap conventions (a min-S of 21 read at
t = 2 against a max-R of 18 that includes t = 1). Per-partition scans close
everything, and this file scans per partition throughout, so the confusion does
not propagate.

**Attribution recorded, not consumed.** No step in `verify.py` cites the audit.
Where the desk spec's numbers and this run disagree, the measurement stands —
but see §"One model comparison" above: the §3 min-S disagreement is **not** a
defect in the review, it is two different cap models, and saying otherwise was
a D-036 failure of this desk's own, now retracted in both deliverables.

## What this certificate does **not** claim

* **No core is claimed to exist.** Everything here is conditional on a critical
  core in the window.
* **X = 6 on m ∈ [22, 26] is NOT emptied.** The staircase confines X = 6 to
  those five rungs and stops — exactly as 0019 stopped one rung of excess
  lower. That band is the next field.
* **X = 6 ⟹ m ≤ 25 is measured, not claimed** (see above).
* **Nothing at X ≥ 10 below m = 32.** The staircase has four steps.
* **The ceiling floor 5173 is not tight**, and §5 says by how much (a factor of
  sixteen in the second moment).
* **(BDH) adds nothing to 0019's (DH) inside §3, and one to two degrees on a
  quarter of §4.** F(d) = (d−5)<sub>+</sub> for every d ≤ 10 and every §3 cap
  sits at 9 or below, so there the two are the same pointwise statement. But
  **24 of §4's 92 cells run at Δ = 11** (capF(7) = capF(8) = 11), and at
  d = 11 F(11) = 7 against 6, so on those cells (BDH) is strictly stronger —
  the linear reading would have allowed d ≤ 12 or 13. The gain is real and
  **not load-bearing**: all 24 die by 44 or more. The gains that matter are the
  q<sub>max</sub> subtraction and the +H term; F's quadratic growth earns its
  keep in §5. Check 54 measures all of this.

## Tally

55 checks + 12 notes. Sections: 0 ledger · 0(h) canary (1 check) · 1 tables and
identities (8) · 2 the lemmas enacted (12 checks, 5 notes) · 3 T-A20 (6 checks,
1 note) · 4 T-B20 (10 checks, 3 notes) · 5 the quadratic law (3 checks, 1 note) ·
6 mutations (11 checks) · 7 margins (1 check) · 8 controls (3 checks, 2 notes).

## Reproduce

```sh
cd certificates/0020-strict-star-collision
python3 verify.py                                   # ~26 s on a modern build
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 verify.py    # 3.9.6, ~41 s
python3 -O verify.py                                # -O, byte-identical
```

Exit status is 0 on green and 1 on red; the harness canary at check 1 drives
the failure path itself before any mathematics is claimed.
