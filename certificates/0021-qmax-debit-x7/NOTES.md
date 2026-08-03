# Certificate 0021 — the q<sub>max</sub> debit: **X ≥ 7 everywhere**, and the staircase sharpens to 26 / 28 / 29

**Status: GREEN ×2.** 63 checks + 5 notes, **3 s** under a bare
`/usr/bin/python3` (3.9.6) and **3 s** under `python3 -O`, the two outputs
**byte-identical modulo the five wall-clock fields** — the `%.1f s` timings in
checks 11, 38, 45 and 57 and the `%.0f s` in the final tally, which are the only
lines a slow machine can move. Everything else is stable across
`PYTHONHASHSEED` 0 / 1 / 12345, across repeated runs, and from any working
directory (no dict- or set-order dependence anywhere: every set is printed
through `sorted`). **Exit 1 on red**, proved twice on scratch copies — lowering
`Lambda` by one unit reddens **22** checks, and mutating `f` to (d−4)<sub>+</sub>
reddens **39**, both exiting 1.
`python3 verify.py`, stdlib only, no solver, no imports from `lib/`, reads
nothing from disk. Deterministic (hand-rolled LCG, seed 20260728). Every
load-bearing bound is exact integer arithmetic.

| claim | label |
| --- | --- |
| **(SJ)** P + J ≤ R, with **J = Σ<sub>v</sub> q<sub>max</sub>(v) over ALL vertices** | **PROVEN-BY-CERTIFICATE** (derived in-cert by summing 0020's (SSC+); enacted on 27 guarded families, 22 of them non-vacuously) |
| **(LD)** P ≤ R − q₁(q₁+1) | **PROVEN-BY-CERTIFICATE** (derived in-cert from (SJ); enacted) |
| **(DM)** d² ≤ 8d − 15 + 3[d = 2] + f(d)(f(d)+2) **for every d ≥ 2**, and summed exactly to Ψ = m² − 43m + 2X + 15n − 3n₂ + n₄ | **PROVEN-BY-CERTIFICATE** (identity at d ≥ 5 and at d = 2, 3; slack 1 at d = 4 only; **FALSE at d ≤ 1**, must-fail controls exhibited) |
| **(RG)** an intersecting r-edge family has a cover ≤ ⌈r/2⌉; τ(K<sub>U</sub>) ≥ 6 − k for \|U\| = k ≤ 5, hence \|K<sub>U</sub>\| ≥ 2(6−k) − 1 | **PROVEN-BY-CERTIFICATE** (cover *constructed*; enacted on 2,827 (family, U) pairs, 20 of them tight) |
| **(S5)** Σ<sub>z ∈ e</sub> d(z) = m + 5 + x<sub>e</sub> | **PROVEN-BY-CERTIFICATE** (enacted on 1,299 edges, 1,054 with x<sub>e</sub> > 0) |
| **(T-A21)** **X ≥ 7 for every critical core in [22, 456]** | **PROVEN-BY-CERTIFICATE** (0020 T-A20 + T-B20, plus §3's 45-cell elimination; belt-and-suspenders on m = 27…32) |
| **(T-B21)** **X = 7 ⟹ m ≤ 26 · X = 8 ⟹ m ≤ 28 · X = 9 ⟹ m ≤ 29** | **PROVEN-BY-CERTIFICATE** (§4: five rungs killed, plus a belt over all 142 cells of the four bands) |

## Why this certificate exists

0020 proved **(SSC+)**: for every vertex z of a critical core,
F(d(z)) + q<sub>max</sub>(z) ≤ s(z). It then summed that line over all vertices,
used Σ<sub>v</sub> s(v) = R, and arrived at

> Σ<sub>v</sub> F(d(v)) + Σ<sub>v</sub> q<sub>max</sub>(v) ≤ R,

whereupon it **threw the second sum away**, keeping only
Σ<sub>v</sub> q<sub>max</sub>(v) ≥ H = #{v : d(v) ≥ 6}. That weakening is the
whole gap this certificate closes. Write **J := Σ<sub>v</sub> q<sub>max</sub>(v)**
and keep it: **(SJ) P + J ≤ R**. It is 0020's own sentence, one clause earlier.

Two things fall straight out.

**The debit.** The largest excessive pair has a shared set S₁ with
\|S₁\| = q₁ + 1 cells, and every one of them has that pair inside its own star,
so q<sub>max</sub> ≥ q₁ there. Hence J ≥ q₁(q₁+1) and **(LD) P ≤ R − q₁(q₁+1)**
— a budget cut that costs nothing and is available on every partition.

**The moment inequality.** With f(d) := (d−5)<sub>+</sub> and ψ(d) := f(f+2),
the identity d² = 8d − 15 + ψ(d) holds for every d ≥ 5 — and, remarkably, also
at d = 3, and at d = 2 once 3[d = 2] is added. The only degree with slack is
d = 4, and it gives back exactly one unit. Summed against Σd = 6m and
Σd² = m² + 5m + 2X this is an **exact identity**, and dropping n ≥ 36,
0008's n₂ ≤ ⌊m/2⌋ and n₄ ≥ 0 leaves the floor **Λ<sub>X</sub>(m)** that every
sweep in the file compares against.

Together they turn each cell of the field into **one integer knapsack**:
maximise Ψ = Σ ψ(dᵢ) over degrees ≥ 6 subject to Σ F(dᵢ) ≤ B and F(dᵢ) ≤ C.
**The cost is F and the value is ψ, and they are different functions.**

## The knapsack convention — pin it or die by it

F(d) = Φ(d, 5) is the collision *cost*; f(d) = (d−5)<sub>+</sub> is its linear
reading; ψ(d) = f(f+2) is the *value*. F and f agree on every d ≤ 10 and
separate at **d = 11**, where F = 7 and f = 6.

| d | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **F** (cost) | 1 | 2 | 3 | 4 | 5 | **7** | 9 | 11 |
| f (linear) | 1 | 2 | 3 | 4 | 5 | **6** | 7 | 8 |
| **ψ** (value) | 3 | 8 | 15 | 24 | 35 | 48 | 63 | 80 |

capF(C) is 6, 7, 8, 9, 10, 10, 11, 11 at C = 1…8: the cap sticks at d = 10 for
every C ≤ 6 and admits d = 11 only at C = 7 and C = 8. The ratio ψ/F is
3, 4, 5, 6, 7 at d = 6…10 and drops to 48/7 at d = 11 — so **greedy-at-cap
understates** once C ≥ 7, and understating a maximum is the *false-kill*
direction. The knapsack here is exhaustive (a budget DP, cross-asserted against
a table-free recursion on all 248 (B, C) pairs with B ≤ 30, C ≤ 8).

Two mutants price the convention, and both are measurements:

- **M-f** swaps the cost to f: caps widen to capf(6) = 11, and the run reports
  **both layers**. At the **raw (LD) sieve** — before any union bound —
  **15 cells flip alive**. After the union bounds re-kill six of those fifteen,
  and one further cell, (9,30,(2,2,2,2,1)), flips at the **J layer** instead,
  **10 cells of the two sweeps lose their kill**. The two sets are not nested.
  The flip the desk spec named reproduces exactly: (1⁷) at (7, 27) climbs from
  **78 to 96** against Λ = 83.
- **M-greedy** swaps the engine to greedy-at-cap: **6 of the 50 staircase cells
  get a strictly smaller maximum, by up to 4 units.** On these rungs no
  understatement spans Λ, so no kill in this file rests on the convention —
  said plainly rather than dressed up.

> **Spec number that did not reproduce.** The desk spec pinned the
> exhaustive-vs-greedy shortfall at "up to 9". **Measured: 10**, at
> (C, B) = (7, 30), (7, 37), (8, 30), (8, 37) — 210 against 200 and 258 against
> 248. The measurement stands.
>
> **And a spec number that DID reproduce, against an earlier reading of it by
> this desk.** The spec's **"15" M-f flips is the raw-sieve count and this run
> measures exactly 15 there.** An earlier draft of this file described the 15 as
> a transcription the run replaced with its own 10 — which would have been a
> **deflation of a correct count**, the mirror of the failure mode D-036 exists
> to catch. Both numbers are real, they measure different layers, and check 48
> prints and asserts each.

## The ledger, in full

| input | what is consumed | where |
| --- | --- | --- |
| **0020 (SSC+)** | F(d(z)) + q<sub>max</sub>(z) ≤ s(z) at every vertex | **the line this file sums.** Claim row |
| **0020 (BDH)** | F(d(z)) ≤ s(z) | claim row; the fallback reading |
| **0020 T-A20** | X ≥ 6 on the whole window | claim row; the base of T-A21 |
| **0020 T-B20** | X = 6 ⟹ m ≤ 26, and the rung ceilings | claim row — **and not load-bearing**: §4's belt re-derives every ceiling |
| **0017 C3** | 2m + 5x<sub>e</sub> ≤ 52 + 3X, X-unrestricted | **LOAD-BEARING**: the per-rung cap c, the parts ≤ 3 bound, the triangle exclusion, and every edge-disjointness licence |
| **0008 (D2)** | ≤ 1 degree-2 cell per edge, hence n₂ ≤ ⌊m/2⌋ | **LOAD-BEARING TWICE**: the n₂ term of Λ, *and* the at-most-one-2 clause of the support-edge profile lists. M-D2 prices both at once |
| **0005** | min degree ≥ 2 | **LOAD-BEARING**: (DM) is *false* at d ≤ 1, and the must-fail controls are exhibited |
| **external** | **NONE** | — |

**Derived in-certificate, and claim rows nowhere:** the key cap
F(d(v)) ≤ X − q₁ (two-case proof) · the exchange identity Σ<sub>v</sub> s(v) = R
· both moment identities · n ≥ 36 and the per-part degree sum m · the
42m − 10n identity · **(SJ)**, **(LD)**, **(DM)**, **(RG)**, **(S5)**.

**(q3) is spent nowhere.** The partition enumeration needs only q ≤ 4, which is
free from 6-partiteness (distinct 6-tuples share at most 5 cells). The two
parts-4 rows (4,2) and (4,1,1) are **carried and killed** — at 24 and 16 on the
(LD) debit alone, against Λ = 57 — rather than deleted by citation. That is what
keeps the billing honest.

**Not consumed:** 0018, 0019 internals, 0017 C2, 0015 (CC), any solver, any
(RG) alternative.

## The analytic proofs

### (SJ) P + J ≤ R

Sum (SSC+) over every vertex. The guard τ ≥ q<sub>max</sub>(v) + 2 is automatic
in a core: distinct 6-tuples of a 6-partite family share at most 5 cells, so
q ≤ 4 and q<sub>max</sub> + 2 ≤ 6 = τ. Every vertex has d ≥ 2 by 0005, so
q<sub>max</sub>(v) is defined everywhere, and no vertex is universal (a
universal vertex is a 1-cover and τ = 6), so the avoiding edge f the mechanism
needs always exists. The right-hand side is R by the exchange identity: a pair
{e, g} lies inside E(v) for exactly the λ = q + 1 cells it shares. ∎

Enacted on **27 guarded families** of the built corpus (177 families in all),
zero violations, **non-vacuously on 22** — the fat planes, where P + J > 0 and
R > 0 together. The **86 universal-vertex families are the must-fail control**:
**10 of them break P + J ≤ R**, which is what makes the hypothesis a hypothesis.

> **Spec number that did not reproduce.** The spec named an "r = 3, m = 4
> equality witness". It reproduces — AG(2,2) is guarded and has P + J = R — but
> the equality is **vacuous**: P = J = R = 0. It *cannot* be otherwise at r = 3.
> Ryser's conjecture is a theorem there, so a 3-partite intersecting family has
> τ ≤ 2; the guard τ ≥ q<sub>max</sub> + 2 then forces q<sub>max</sub> = 0 and
> R = 0. An exhaustive anchored search over 3-, 4- and 5-partite guarded
> families on 4 and 5 edges found **no guarded family with R > 0 at all** in
> that range. Measured on the corpus: **5 vacuous equalities, 0 non-vacuous**.
> The non-vacuous enactment therefore rests on the fat planes, where the
> inequality is strict.

### (LD) P ≤ R − q₁(q₁+1)

Every cell of S₁ has the q₁-pair inside its star, so q<sub>max</sub> ≥ q₁ on all
q₁ + 1 of them; J, being a sum over **all** vertices, already contains those
q₁(q₁+1) units. ∎

**Why "all vertices" is not a detail.** If J were restricted to the *high*
vertices — the ones that contribute to P — the debit would not follow, because
the cells of S₁ need not be high. Measured: of **22 guarded corpus families with
R > 0, all 22** have the restricted J strictly below q₁(q₁+1). The fat planes
are the clean case: one high cell with q<sub>max</sub> = 1, against a debit of 2.

### (DM), pointwise and summed

For d ≥ 5, ψ(d) = (d−5)(d−3) = d² − 8d + 15, so d² = 8d − 15 + ψ(d) **exactly**.
At d = 3, 8·3 − 15 = 9 = 3². At d = 2, 8·2 − 15 = 1 and the 3[d = 2] term makes
it 4 = 2². At d = 4 the right side is 17 against 16 — **slack exactly 1, and
nowhere else on 2…60**. At d = 1 it is −7 against 1 and at d = 0 it is −15
against 0: **both fail**, which is where 0005 is spent.

Summing with Σ<sub>v</sub> d = 6m and Σ<sub>v</sub> d² = m² + 5m + 2X, and
accounting the slack exactly (one unit per degree-4 vertex):

> **Ψ = m² − 43m + 2X + 15n − 3n₂ + n₄** (an identity)

Enacted on 64 random integer censuses with m and X *solved from the two
moments*, and on the 8 six-partite six-uniform corpus families with min degree
≥ 2 — zero mismatches either way. Dropping 15(n − 36) ≥ 0, then
3(⌊m/2⌋ − n₂) ≥ 0 by (D2), then n₄ ≥ 0 — **a pure loss, nothing recovers it** —
gives

> **Ψ ≥ Λ<sub>X</sub>(m) := m² − 43m + 2X + 540 − 3⌊m/2⌋**

which reads **57, 59, 60, 66, 71** at X = 6 on m = 22…26 and **83, 92, 108, 123,
141** on the five staircase rungs.

### The key cap F(d(v)) ≤ X − q₁

Two cases. If v ∈ S₁ then the q₁-pair is inside E(v), so q<sub>max</sub>(v) ≥ q₁
and (SSC+) gives F(d(v)) ≤ s(v) − q<sub>max</sub>(v) ≤ X − q₁. If v ∉ S₁ then
that pair is not inside E(v) at all, so s(v) ≤ X − q₁ already. ∎ Enacted at
**460 vertices** of the guarded corpus, zero violations.

### (RG) residual pairing

*Step one, constructed.* Pair the edges of an intersecting family up; each pair
shares a cell; take one such cell per pair, plus any cell of the odd edge. That
set is **exhibited and then verified to cover**, on all 177 corpus families.
Hence τ ≤ ⌈r/2⌉.

*Step two.* If C covers K<sub>U</sub> then C ∪ U covers all of K, since every
edge either meets U or lies in K<sub>U</sub>; so \|C\| + k ≥ τ, i.e.
τ(K<sub>U</sub>) ≥ τ − k. Combining, ⌈\|K<sub>U</sub>\|/2⌉ ≥ τ − k gives
\|K<sub>U</sub>\| ≥ 2(τ − k) − 1. ∎ The edge case k ≥ τ, where the bound reads
negative and K<sub>U</sub> may be empty, is stated and never used: this file
uses only k = 2 (≥ 7 edges avoid a pair of cells) and k = 3 (≥ 5 avoid a triple).
Enacted on 2,827 (family, U) pairs, zero failures, **tight on 20**.

### (S5) Σ<sub>z ∈ e</sub> d(z) = m + 5 + x<sub>e</sub>

One double count: summing d(z) over the six cells of e counts each other edge g
once per shared cell, i.e. λ(e, g) = 1 + q(e, g) times, plus 6 for e itself. ∎

## §3 — T-A21: the X = 6 field on m = 22…26 is empty

**Nine excess partitions**, not seven: the seven with parts ≤ 3, plus (4,2) and
(4,1,1). Carrying the parts-4 rows is what keeps (q3) unspent.

| partition | R | route | max Ψ, m = 22…26 |
| --- | --- | --- | --- |
| (4,2) | 26 | (LD) 24, union bound 8 | 8 |
| (4,1,1) | 24 | (LD) 16 | 16 |
| (3,3) | 24 | union: J ≥ 21 | 15 |
| (3,2,1) | 20 | knapsack | 38, then 18 |
| (3,1,1,1) | 18 | knapsack | 30 |
| (2,2,2) | 18 | trichotomy | 48, 51, 56, 63, 32 |
| **(2,2,1,1)** | 16 | knapsack | **56**, 56, 56, 56, 32 |
| (2,1⁴) | 14 | knapsack | 48 |
| **(1⁶)** † | 12 | three branches | **56**, then census |

† The 56 is the **knapsack branches only**. The row's **K₄ branch** reaches
59, 59/70, 70, 70 on m = 22…25 — *above* Λ on four of the five rungs, by up to
11 — and is killed by the census-and-profile count below, not by the floor.
This is the certificate's thinnest row, not a comfortable one; the run's §3
table carries the same footnote.

**(3,3).** The two 4-cell shared sets cannot share an edge (x<sub>e</sub> ≥ 6
against c ≤ 5), and being edge-disjoint they cannot share two cells either: two
common cells would sit in all four edges, making all **six** pairs among them
excessive, and this partition has two parts. So the union is ≥ 7 cells, each
with q<sub>max</sub> ≥ 3: **J ≥ 21**, B = 3, max Ψ = **15**.

**(2,2,2) — the excess-graph trichotomy.** Read the three pairs as edges of a
graph on the edges of K.

- *Not a triangle.* Then \|Sᵢ ∩ S<sub>j</sub>\| ≤ 1 always. Edge-disjoint: the
  six-pairs count against three parts. **Sharing an edge e:** with
  Pᵢ = {e,g}, P<sub>j</sub> = {e,h}, two common cells lie in e, g *and* h, so
  \|g ∩ h\| ≥ 2 and {g,h} is a third excessive pair — **the closing edge**, and
  the three pairs are a triangle after all. (This argument is valid at *any* c,
  which is why the non-triangle branch does not need C3.) Union ≥ 6,
  **J ≥ 12**, B = 6, max Ψ = **32**.
- *A triangle on {e,f,g}.* Each triangle edge carries x<sub>e</sub> = 2 + 2 = 4,
  so **C3 kills the whole branch at m = 26**, where c = 3. That one-liner is
  carried first.
- *The triangle at m = 22…25.* By (SSC+) a cell in at most one shared set has
  s = q<sub>max</sub> and F(d) ≤ 0, so **every high cell lies in the triple
  intersection T**. Split by the number of high cells, not by \|T\|. **At most
  two:** each has s = 6, q<sub>max</sub> = 2, so F ≤ 4, d ≤ 9, ψ ≤ 24 — at most
  **48**. **Three:** no outside edge may hold two T-cells (it would meet e, f
  and g twice each, adding three excessive pairs and pushing X to 9), so the
  stars overlap only in {e,f,g} and the star-union is 9 + Σfᵢ; **(RG) at k = 3**
  leaves ≥ 5 edges avoiding all of T, so **Σfᵢ ≤ m − 14**. **Every fᵢ ≥ 1 in
  this branch** — a T-cell at f = 0 has d = 5 and is *not high*, so that
  configuration belongs to the ≤ 2 branch, already bounded at 48. Per-rung
  maxima **42, 51, 56, 63** against 57, 59, 60, 66; the **row** maximum at
  m = 22 is the other branch's 48, so the kill is unchanged either way.

  > **A retraction owed outward, and paid.** An earlier draft charged the
  > outside audit with a **deflation** over the value 42 at m = 22 and
  > substituted 48. The charge was **wrong**. 42 is the correct maximum of the
  > branch *as this file labels it* (three high cells, every fᵢ ≥ 1); the 48
  > came from an enumeration that admitted fᵢ = 0 — i.e. from the *other*
  > branch, computed under this branch's name. The audit's number was right,
  > the enumeration has been restricted to `range(1, 5)` so the branch computes
  > what it says, and the charge is withdrawn. **A deflation of a correct
  > number is an error in the mirror direction, and the lab owes the same
  > retraction outward that it demands inward (D-036).**
- *A redundant tooth at m = 26.* Identically
  Σd² = 42m − 10n − 2n₃ − 2n₄ + Σ<sub>d≥6</sub>(d−2)(d−5)n<sub>d</sub>; with
  ≤ 3 high cells at d ≤ 9 that is 42·26 − 360 + 3·28 = **816** against the
  **818** the second moment requires. Two independent routes close the branch.

**(1⁶) — three branches.**

1. *No cell at f = 5.* B = 10, cap drops to d ≤ 9, exhaustive maximum **56**
   against 57 — **one unit**.
2. *A cell u at f(u) = 5, no K₄.* (SSC+) gives 5 + 1 ≤ s(u) ≤ X = 6, so
   s(u) = 6 and **u lies in all six shared sets**. Any other high cell w then has
   Sᵢ = {u, w} for every i ∈ T<sub>w</sub>, so the edges through both carry all
   of T<sub>w</sub>: with k such edges, \|T<sub>w</sub>\| = C(k,2), and
   (SSC+) caps F(d(w)) at C(k,2) − 1. k = 2 gives d ≤ 5 (not high), k = 3 gives
   d ≤ 7, and k ≥ 5 is impossible (C(5,2) = 10 > 6). Maximum
   35 + 8 + 8 + 3 = **54**.
3. *The K₄.* If some high w has k = 4 then C(4,2) = 6 exhausts X, Sᵢ = {u,w} for
   all six pairs, and **u, w are the only high cells**. A **fifth** edge through
   {u,w} would make ten excessive pairs and X ≥ 10, so exactly four carry it; the
   star-union is 4 + (d(u)−4) + (d(w)−4) = 6 + p with p = f(u) + f(w), and
   **(RG) at k = 2** leaves ≥ 7 edges avoiding both, so **p ≤ m − 13**.

The arithmetic survivors of branch 3:

| m | Λ | p ≤ | survivors (d<sub>u</sub>, d<sub>v</sub>) | Ψ |
| --- | --- | --- | --- | --- |
| 22 | 57 | 9 | (10, 9) | 59 |
| 23 | 59 | 10 | (10, 9) · (10, 10) | **59 = Λ** · 70 |
| 24 | 60 | 11 | (10, 10) | 70 |
| 25 | 66 | 12 | (10, 10) | 70 |
| 26 | 71 | 13 | **none** | 70 vs 71 — **one unit** |

### The five survivors die by census and profile

**n = 36 is forced, and (D2) is what forces it.** n ≥ 36 because each part is a
cover and τ = 6. Running the census enumerator with n free returns solutions at
n = 36 *and at no other n* on all five survivors — **checked computationally per
case**. Drop the n₂ cap and the same enumerator returns solutions above n = 36
on **four of the five** — n = 37 on four of them and n = 38 on two — and only
m = 25 stays at 36. (The count is now computed per survivor and asserted, not
narrated from one case.) With n = 36 every part holds **exactly six cells**,
which is what licenses the two-special-parts count.

**The support edges.** A support edge meets the other three in exactly {u, v} at
q = 1, so x<sub>e</sub> = 3 and (S5) pins its six degrees at m + 8. Subtracting
d(u) + d(v) leaves the four **ordinary** cells summing to m + 8 − d<sub>u</sub> −
d<sub>v</sub>; each is ≥ 2 (0005) and ≤ 5 (only u, v are high), and **(D2) allows
at most one degree-2 cell per edge**. And **no ordinary cell serves two support
edges** — a third common cell would give λ ≥ 3, q ≥ 2, which (1⁶) forbids — so
the four edges need four *disjoint* copies of their profiles.

| case | census(es) | profiles | how it dies |
| --- | --- | --- | --- |
| m = 22, (10,9) | (11,11,2,10) | {2,3,3,3} | needs 12 degree-3 cells; n₃ = 11 |
| m = 23, (10,9) | (11,9,0,14) | {3,3,3,3}, {2,3,3,4} | **n₄ = 0** removes {2,3,3,4}; 16 needed, n₃ = 9 |
| m = 23, (10,10) | four, incl. (8,13,2,11) | {2,3,3,3} | three fail on n₃ < 12; the fourth needs the **two special parts** |
| m = 24, (10,10) | four | {3,3,3,3}, {2,3,3,4} | 16 − 2t degree-3 and t degree-4; only t = 4 clears n₃, and wants 4 degree-4 where n₄ ≤ 1 |
| m = 25, (10,10) | two | {2,3,3,5}, {2,3,4,4}, {3,3,3,4} | every profile needs a degree-3; ≥ 4 demanded, n₃ ≤ 3 |

**The two special parts.** u and v lie in **different** parts, since a support
edge holds one cell per part. At n = 36 each special part is its degree-10 cell
plus five low cells summing to m − 10, which at m = 23 allows exactly
(5,2,2,2,2), (4,3,2,2,2), (3,3,3,2,2). The support demand — twelve degree-3 and
four degree-2 cells — lives entirely in the *other four* parts. All six unordered
pairs of special profiles are enumerated:

| special parts | n₃ left of 13 | n₂ left of 8 |
| --- | --- | --- |
| (5,2,2,2,2) + (5,2,2,2,2) | 13 | **0** |
| (5,2,2,2,2) + (4,3,2,2,2) | 12 | **1** |
| (5,2,2,2,2) + (3,3,3,2,2) | **10** | 2 |
| (4,3,2,2,2) + (4,3,2,2,2) | **11** | 2 |
| (4,3,2,2,2) + (3,3,3,2,2) | **9** | 3 |
| (3,3,3,2,2) + (3,3,3,2,2) | **7** | 4 |

Every row fails on twelve degree-3 or on four degree-2. Dead.

**T-A21 assembled.** 45 cells, 0 survivors, so X ≥ 7 on the whole window.

## §4 — T-B21: the staircase

Five rungs, c = ⌊(52 + 3X − 2m)/5⌋ = **3** on every one, so parts ≤ 3 by C3.
The raw (LD) knapsack leaves **ten** survivors:

| rung | Λ | raw survivors (max Ψ) |
| --- | --- | --- |
| (7, 27) | 83 | (2,2,2,1) 94 |
| (7, 28) | 92 | (2,2,2,1) 94 |
| (8, 29) | 108 | (3,3,2) 120 · (3,3,1,1) 108 · (2,2,2,2) 120 · (2,2,2,1,1) 108 |
| (9, 30) | 123 | (3,3,3) 164 · (3,3,2,1) 140 · (2,2,2,2,1) 140 |
| (9, 31) | 141 | (3,3,3) 164 |

Note **(1⁸) at (8,29)**: its cap C = 7 admits d = 11 and the cost-F knapsack
gives **96** against 108. Read with cost f the cap widens to d = 12 and the same
budget of 14 buys **two** degree-12 cells, reaching **126** against 108 — it
would have lived. That 126 is measured in-run and pinned, not transcribed.

**(7,27) and (7,28), partition (2,2,2,1) — where the kill lives.** Two q = 2
pairs sharing an edge would put x<sub>e</sub> ≥ 4 on it, and c = 3, so the three
pairs are **pairwise edge-disjoint** — which also rules out the triangle
outright. Edge-disjointness gives \|Sᵢ ∩ S<sub>j</sub>\| ≤ 1 by the six-pairs
count against four parts; three 3-cell sets meeting pairwise in at most a point
have union ≥ 6; every such cell carries q<sub>max</sub> ≥ 2, so **J ≥ 12**,
B = 8, max Ψ = **50** against 83 and 92.

> **M-tri.** Withdraw that exclusion and the cell climbs from 50 to **exactly
> 83 = Λ — a tie, so the kill is lost.** The tying configuration is fully
> determined: \|T\| = 3 with one T-cell also in S₄, giving J ≥ 7, B = 13,
> caps f ≤ 5, 4, 4 and Σfᵢ ≤ 13 from (RG) at k = 3, hence
> ψ(10) + ψ(9) + ψ(9) = 35 + 24 + 24 = 83. **This is the thinnest structural
> step in the certificate.**

**(8,29) — four union bounds, all derived.** (3,3,2): the two 4-cell sets give
union ≥ 7 and J ≥ 21; the 3-cell set meets each in at most a point
(q<sub>i</sub> + q<sub>j</sub> = 5 > 3 licenses edge-disjointness), so one of its
cells is new and **J ≥ 23** — B = 7, max Ψ = 43 (against 59 at the weaker
J ≥ 21; **both kill, and the file uses the derived 23**). (3,3,1,1): J ≥ 21,
B = 7, 43. (2,2,2,2) and (2,2,2,1,1): union ≥ 6, J ≥ 12, B = 12 and 10, giving
78 and 70.

**The four-set union bound is enumerated, not asserted.** Four 3-cell sets
pairwise meeting in ≤ 1 cell place twelve incidences on their union; a cell in j
of them accounts for C(j,2) of the C(4,2) = 6 index pairs. Every multiplicity
vector summing to 12 is enumerated: **no union of five or fewer cells admits
one**, and six does (all multiplicities 2).

**(9,30) and (9,31) — the two one-unit cells do not rest on one unit.** At
m = 31 the raw knapsack kills (3,3,2,1) at 140 vs 141 and (2,2,2,2,1) at 140 vs
141. **Both are killed again by their geometry:** (3,3,2,1) at J ≥ 23, B = 9,
Ψ ≤ **59**; (2,2,2,2,1) at J ≥ 12, B = 14, C = 7 (d = 11 admitted),
Ψ ≤ **96**. (3,3,3) has J ≥ 27, B = 9, Ψ ≤ **59**.

**The belt.** The same engine runs on **all 142 cells** from each band's first
live rung to its C3 ceiling — X = 6 on m = 27…32, X = 7 on 27…34, X = 8 on
29…35, X = 9 on 30…37 — and every one is dead. **X = 6 on m = 27…32 dies to the
raw knapsack with no union bound at all.** So T-A21 and T-B21 do not lean on
0020's T-B20; if it were withdrawn tomorrow both would survive on §4 alone.

## Derived and then not imposed — the sharper union bound

`Jlb` withdraws entirely the moment C3 stops forcing edge-disjointness
(q<sub>i</sub> + q<sub>j</sub> ≤ c). It need not: two shared sets meeting in
z ≥ 2 cells force a **closing edge** of excess ≥ z − 1, so the partition itself
limits the overlap. That reading is **computed for all 45 §3 cells and imposed
nowhere** — omitting a constraint widens the field, and a wider field can only
make a kill harder, so every kill holds a fortiori.

It would tighten **5 of the 45 cells** — (2,2,1,1) on all of m = 22…25, from
**56 down to 48**, and (3,2,1) at m = 22, from 38 down to 30. **That matters for
honesty about margins:** this file's first named one-unit margin exists under the
bound the file actually runs, and evaporates under a bound it declines to run.
Both are stated.

## The mutation table (§5 — nine mutants in ten measured readings)

| mutant | reddens | count | measured effect |
| --- | --- | --- | --- |
| **M-f** cost read as f, not F | check 2 | **10** | **15 raw-sieve flips**, 10 of them still open after the union bounds; (1⁷)@27 climbs 78 → 96 against 83 |
| **M-D2** n₂ cap +1 (Λ − 3) | checks 6, 34 | **6** | see below — this run settles a three-way disagreement |
| **M-n35** n ≥ 36 → n ≥ 35 (Λ − 15) | check 6 | **24** | reopens at every m from 22 to 26, incl. (2,1⁴) and (2,2,1,1) |
| **M-RG** \|K<sub>U</sub>\| ≥ 7 → 6 at k = 2 | check 22 | **0** | **INERT, with the reason** |
| **M-RG′** \|K<sub>U</sub>\| ≥ 5 → 4 at k = 3 | check 22 | **2** | (2,2,2) lives at m = 24 (63 vs 60) and m = 25 (72 vs 66) |
| **M-debit** (LD) dropped, P ≤ R kept | check 16 | **29** | (3,2,1) climbs 38 → 98; the union-bound rows are unmoved |
| **M-tri** C3 triangle exclusion skipped | checks 28, 40 | **2** | (7,27) **ties at 83 = Λ**; at (7,26) the branch is 74 vs 73. **A lower bound on C3's exposure, not its price** — see M-C3disj |
| **M-C3disj** C3 edge-disjointness licence withdrawn | checks 27, 41 | **15** | every union bound falls: all five (3,3) cells and all ten staircase cells that die by a debit. (2,2,2) is **untouched** — its J ≥ 12 is the trichotomy, valid at any c |
| **M-greedy** greedy-at-cap engine | check 9 | **6** | 6 cells understated by up to 4; **0 false kills visible** |
| **M-2sup** ordinary cells may serve two support edges | check 36 | **3** | demand halves; the (1⁶) row at m = 22, 23, 24. **Not m = 25**, although a K₄ survivor exists there: halving still leaves every profile at tot = 13 wanting more degree-3 cells than n₃ ≤ 3 supplies |

Every REDDENS entry is a **captured check number**, asserted equal to the number
the run actually assigned, so a renumbering reddens check 57 instead of silently
making this table wrong. **And every capture is now pinned, not only the fifteen
the prose cites:** check 63 asserts all 59 `CK_*` bindings against literals,
checks they are distinct and increasing, and names the four checks that carry no
capture. An unread capture is a variable that cannot fail, and a table claiming
captured numbers should not advertise more coverage than it has.

### M-D2 — the fleet disagreed, and this run settles it

Three intake lanes returned three different reopen sets: **nothing at all** /
**m = 22 and 23** / **only the m = 25 zero-margin cell**. Measured here over all
95 cells of both sweeps, **six cells reopen**:

> (1⁶) and (2,2,1,1) at **m = 22**; (1⁶) and (2,2,1,1) at **m = 23**;
> (2,2,2) at **m = 25**; and one staircase cell, **(9, 30, (2,2,2,1,1,1))**,
> which clears the lowered floor at 121 against 120.

So the second lane was right about m = 22 and 23 and missed three cells; the
third lane was right that m = 25 moves but named the wrong cell — **the
zero-margin cell is (23, (10,9)) and it does not reopen**, because its kill is a
counting kill and nothing about Λ touches it; the first lane was simply wrong.

### M-RG — one arm is not load-bearing, and that is a measurement

Weakening the k = 2 bound to 6 does make (10,10) an arithmetic survivor at
m = 22, with **five** censuses instead of the primary run's one — the desk spec's
expectation, reproduced exactly. **But the cell still dies, and not by census:**
at (22, 10, 10) a support edge's four ordinary cells must sum to 10, and *every*
partition of 10 into four parts ≥ 2 contains at least two 2s, which (D2) forbids
on one edge. The profile list is **empty** — no support edge exists at all.
Withdrawing the k = 2 bound **entirely** still reopens **zero** cells. So this
file's use of (RG) is load-bearing at k = 3 and slack at k = 2, and the ledger
should be read that way.

## Margins — every coordinate, named (D-035)

- **Three one-unit cells.** (2,2,1,1) at m = 22 and the no-f = 5 branch of (1⁶),
  both **56 against 57 at m = 22**; and the K₄ branch of (1⁶) at m = 26,
  **70 against 71** — and that last one is what **closes the X = 6 band**, so
  the band's top rung is decided by a single unit. For (1⁶) the *branch value*
  56 holds on every rung; the *margin* does not — it is **1, 3, 4, 10, 15**
  across m = 22…26.
- **One zero-margin cell.** At m = 23 the degree pair **(10,9) reaches Ψ = 59
  against Λ = 59 exactly**. It clears the moment requirement with nothing to
  spare and is killed **only** by the census-and-profile count.
- **Two further one-unit cells** at (9,31), both re-killed by geometry (59 and
  96), so no staircase cell rests on a single unit.
- **The f/F cost/value convention** — **one unit at d = 11**, where F = 7 and
  f = 6. M-f flips **15** cells at the raw sieve, **10** still open after the
  union bounds, including (1⁸)@29 at **126 against 108** under cost f.
- **Among the knapsack branches**, the thinnest surviving margins are **1** (at
  m = 22, (1⁶)) in §3 and **2** (at (9, 30, (2,2,2,1,1,1))) in §4 — both
  measured in-run. **The K₄ branch of (1⁶) is deliberately not in that number**,
  because it is not a knapsack branch: it stands *above* Λ on four of the five
  survivors, by up to **11**, and is killed by counting cells. Calling a number
  that excludes the most exposed row "after every bound" would be the flattering
  direction, so the quantity is named for what it measures.
- **The structural exposure** is 0017's C3, in both of the uses that bound a
  cell: the triangle exclusion, which M-tri turns into a tie, and the
  edge-disjointness licence behind every union bound, which **M-C3disj** prices
  at **15 cells**. C3's third use — the per-rung part bound and the band
  ceilings — defines the *field* rather than a bound and is not mutated; that
  is stated, not skipped.
- **(D2)** is load-bearing twice; **n ≥ 36** is worth 15 units of Λ; **(RG)** is
  load-bearing at k = 3 and inert at k = 2. The support-edge profiles' **≤ 5
  ordinary-cell ceiling is measured INERT** the same way the k = 2 arm is:
  recomputing every list at a ceiling of 6 returns the same lists on all five
  survivors, because (D2)'s at-most-one-2 clause has already removed the
  profiles that would use a degree-6 cell.
- **(RG)'s enactment cannot reach the instances the proof spends.** The largest
  τ any family this lab can build is **5**, so the (τ, k) = (6, 2) and (6, 3)
  readings §3 and §4 use are carried by the *proof*; the 2,827 enacted pairs
  price the general statement, at τ − k up to **4**.

This certificate is **thinner than 0020**, whose thinnest census margin was 2.
That is stated rather than covered by a blanket sentence.

## Provenance — the outside-audit lane's fourth fruit

**Every claim row and the whole blueprint were proposed by an outside audit**
(GPT 5.6 Sol Pro, fourth audit, 2026-07-28/29, reading the public repo), which
also found **zero errors** in the lab's existing chain.

Per **D-036** the received text entered no chain: it is retained verbatim at
`notebook/raw/2026-07-29-received-turn17-gpt-pro-ryser-3.md` on arrival, the
desk re-derived every step, blind derivation lanes received statements plus
one-line mechanisms only, and hostile refuter lanes were given the file verbatim
and told to break it. **No step in `verify.py` cites the audit.**

### The fleet, and the one thing it is most worth recording

* **2 blind lemma lanes** — statements plus one-line mechanisms only. Both
  proved every statement.
* **2 blind layer lanes.** One of them **rebuilt the chain from scratch** after
  a defect in its own prompt — an unplanned fully-independent proof — and in
  doing so **caught an unguarded lemma of its own that would have flattered the
  result to m ≤ 25**, and guarded it in-lane. *An error that flatters the
  expected answer is the worst kind a verifier can make;* a lane that catches
  one of its own before it leaves the lane is the single most valuable line in
  this record, and it is written down rather than absorbed into a green tick.
* **numeric and dependency lanes** — the (RG) arms, the M-D2 reopen set, and the
  per-rung budget vectors.
* **3 verbatim-file refuter lanes**, told to break the finished file.
* **A post-freeze audit round of three more lanes** read the frozen file: a
  **sabotage lane** (66 single-point mutations on scratch copies, 59 reddening),
  an **independent reimplementation lane** (built from the spec's mathematics
  without reading the draft), and an **outside-reader lane**. Their catches are
  attributed below.

### What the post-freeze round caught, and who caught it

| defect | lane |
| --- | --- |
| the (7,26) preview printed **(2,2,2,1) at 78** where the file's own table says **94** | all three, independently |
| the M-f "15" framed as a mis-transcription when it is the **correct raw-sieve count** | reimplementation |
| the **deflation charge over 42** — the charge was ours and it was wrong | outside reader |
| "n = 37 and 38 on **three** of the five" — measured **four** | reimplementation and outside reader |
| "(1⁸)@29 would have reached **108**" — measured **126** | outside reader |
| the per-part degree sum **unpinned** in the executed path (both directions of a one-unit error stayed green) | sabotage |
| the (3,3) floor literal **21 inert**; the case-combination conventions pinned only inside mutants | sabotage |
| five **computed-and-dropped** diagnostics, and 48 unread `CK_*` captures | sabotage |
| the §3 table's **B column** read at c = 3 for every rung; the (1⁶) row's K₄ exposure missing from it | reimplementation and outside reader |
| "after every bound" said of a margin that **excludes the K₄ branch** | reimplementation |
| the determinism claim stated without the wall-clock qualifier | sabotage and outside reader |
| the docstring's "**eight** survivors" against the run's asserted ten | outside reader |
| M-2sup's gloss ("wherever a K₄ survivor exists") against its measured three | outside reader |
| M-tri's 2 read as C3's price rather than a floor | reimplementation |
| (RG)'s enactment never reaching τ = 6; the profile ceiling inert; `psi(10)` hardcoded where `du` was bound | sabotage |

All are repaired above. **None touched a kill**: every one was a stated number,
a scope word, or an unpinned measurement, and the mathematics reproduced
number-for-number in the reimplementation lane.

### The audit's stated-step defects — and one retraction owed outward

The audit's own stated-step defects, all repaired in-cert and none fatal: the
f/F cost/value trap; the claim that greedy suffices; the missing
disjointness-by-C3 at (7,27); the missing (SSC+) line in its §4.2; the missing
star-union proof in the K₄ branch; the J ≥ 23 gap at (3,3,2); and a heading that
said five where the content said four.

**An earlier draft listed an eighth — "a deflated 42 where the correct value is
48" — and that charge is WITHDRAWN.** 42 is the correct maximum of the branch as
this file labels it; the 48 came from this desk's own enumeration admitting
fᵢ = 0, i.e. from a different branch. So it is **not** true that no retraction
was owed in either direction this time: **one was owed outward, and it is paid
here and in §3.** Deflating a peer's correct number is the mirror of inflating
one's own, and D-036 makes attribution accuracy symmetric.

**Three spec numbers did not reproduce**, and in each case the measurement
stands and is printed by the run: the greedy shortfall (**10**, not 9); the
"r = 3, m = 4 equality witness" (**vacuous**, and provably so at r = 3); and the
(7,26) preview's J-layer, read by the spec as two shapes with (2,2,2,1) alive
only through its triangle (see below). **One spec number that DID reproduce and
was briefly mis-framed as not reproducing** is the M-f "15" — see the knapsack
convention section.

## The (7,26) frontier — a preview, measured, not claimed

c = 4 there, so parts ≤ 4. The raw (LD) sieve leaves **four** shapes alive
against Λ = 73: (3,3,1) at 80, (2,2,2,1) at 94, (2,2,1,1,1) at 78, (1⁷) at 78 —
exactly as the spec pinned them.

**The J-layer is where the readings part.** Under *this file's* conservative
`Jlb`, (3,3,1) dies at 27 and **three** shapes survive: **(2,2,2,1) at 94**,
(2,2,1,1,1) at 78, (1⁷) at 78. The 94 is not a typo for 78: at c = 4 the licence
q<sub>i</sub> + q<sub>j</sub> > c fails (2 + 2 = 4), `Jlb` withdraws entirely,
nothing is debited, and the raw value stands — **twenty-one units clear of 73**.

The spec read this rung as **two** shapes with (2,2,2,1) "alive only through its
triangle at one unit"; that does not reproduce under the bound this file runs.
Under the **sharper adjacency-aware reading** (derived above, not imposed),
(2,2,1,1,1) drops to **70** and dies, and **two** shapes survive — the spec's
answer, reached by a bound this file declines to impose. The **one unit** is
real but belongs to (2,2,2,1)'s **triangle sub-branch** alone, 74 against 73,
and that is the shape of the frontier.

**Not claimed.** This rung is stated open, and the adjacent-but-not-triangle
configurations at c = 4 are not separated here.

## What this certificate does **not** claim

- **No core is claimed to exist.**
- **X = 7 on m ∈ [22, 26] is not emptied.** That is the new frontier; the
  preview above measures **three** shapes alive at m = 26 under this file's own
  `Jlb`, two under the sharper bound it declines to impose.
- **Nothing at X ≥ 10 below m = 30.**
- **The banked leads are leads.** One unaudited lane reported that a *guarded*
  engine (imposing the (SSC+) ceiling F(d) + q<sub>max</sub> ≤ X at every high
  vertex simultaneously with the key cap) yields bonus rungs — X = 9 ⟹ m ≤ 28,
  X = 10 and 11 ⟹ m ≤ 29, X = 12 ⟹ m ≤ 31. Single-lane, unaudited, **not
  re-derived here**, and claimed nowhere. Named so they are not lost.
- **The far end of the window is untouched.** 0020's (Q) and (Q0) remain the
  authority there.
- **0018, 0019 and 0020 remain the authorities for their own theorems.** This
  file consumes four of 0020's rows and re-derives everything else it uses; it
  supersedes their *bands*, not their statements.

## Tally

63 checks + 5 notes. A **note** is a stated fact — a citation, a measurement
carried for the record, or a step proved by hand — and is *not* machine-tested.
The two tallies are kept apart so the check count can never imply a test that
did not run.

## Reproduce

```sh
cd certificates/0021-qmax-debit-x7
python3 verify.py                     # ~3 s, exit 0
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 verify.py     # bare 3.9.6
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 -O verify.py  # asserts off
```

Stdlib only. No installs, no venv, no imports from `lib/`, nothing read from
disk.

## Erratum 2026-08-03 — the triangle optimizer's stated support (turn 18)

`tri_max`'s docstring asserted **"every high cell lies in T"**. False for
(2,2,2,1): a cell of S₄ ∩ (U ∖ T) has s = 2 + 1 = 3, q_max = 2, so F ≤ 1 and a
degree-6 cell can sit **outside T**. The optimizer never searched that cell.

**No number in this file moves.** At the rungs where this file runs the branch,
c = 4, and an S₄ cell in U needs the q = 1 pair riding a triangle edge — which
then carries x_e = 2 + 2 + 1 = 5 > 4 — or forces a fifth excessive pair. Both
of this file's uses were therefore sound as run: the claim rows (7,27)/(7,28)
exclude the triangle by C3 outright, and the (7,26) preview's 74 is confirmed
by the corrected optimizer. 0022 §3 proves the honest case law ((0,0), (1,0),
(0,1), (0,2) for (|S₄ ∩ T|, |S₄ ∩ (U ∖ T)|), with the (0,2) adjacent-apex
pattern witnessed and shown **live at m = 24**, where c = 5), carries the
outside-cell branches, and measures the corrected maxima **equal**:
62/67/74/83 at m = 24..27.

Found by the fifth outside audit (which also supplied an incomplete repair —
its lemma |S₄ ∩ U| ≤ 1 is true at c = 4 but not in general; 0022's honesty
note 2 records both directions). Docstring reworded in place; **no check
touched; re-verified green ×2** (bare 3.9.6 and `-O`) after the rewording.
The engineering note from the same audit — the finite search's hard-coded
degree ceiling — is closed in 0022's engine (monotone-derived ceiling), left
as-is here.
