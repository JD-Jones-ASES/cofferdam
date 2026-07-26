# 2026-07-26 · turn 5 — the minimum-degree ladder; m ≥ 20; the gap is one question

Append-only. Technical. Failure recorded as failure.

## 0. Seal check

Intact. No sealed path read by this repo, by the main thread, or by any of the
seven subagents run this turn — each carried the seal verbatim in its prompt and
none had web access. Published literature (AKP arXiv:1409.4938) is referenced
only as an *agreement*, never as an input.

## 1. Where the turn started, and JD's pointer

Certs 0001–0003 left three cases: (19, Δ=6), (20, Δ=6), (20, Δ=7). JD's pointer:

> You used Lemma 2.1. Inspect the equality case when deleting the stars of two
> vertices in the same part. Every part of a τ=6 example has at least 6 active
> vertices. No active vertex can have degree one. What must that part look like
> in an eight-edge residual.

Cert 0002 had folded AKP Lemma 2.1 into the ladder as a saturation condition and
concluded it "moves the floor by nothing" — because it assumed the residual's
tail profile could be (3,2,1,1,1)-like. **That was the error the pointer names:
a τ=6 counterexample has no degree-1 vertices at all**, so the tail cannot look
like that, and the equality case is not merely constrained — it is impossible.

## 2. The two elementary lemmas

**(A) minimum degree 2.** Let E ∈ H and x ∈ E. |E\{x}| = 5 < 6 = τ, so E\{x} is
not a cover: some F ∈ H misses it. H intersecting ⟹ F ∩ E ≠ ∅ ⟹ F ∩ E = {x},
so x ∈ F, F ≠ E, deg(x) ≥ 2. No minimality needed; it holds for every vertex of
every edge.

**(B) six vertices per part.** A part's active vertices meet every edge, so they
are a cover: |V_i| ≥ τ = 6.

Both are one-liners. What they buy is that **every part's degree profile is a
partition of m into ≥ 6 entries each ≥ 2** — which on its own already drops
m=19's slack from 9 to 3 and kills (20, Δ=5) a second time.

## 3. The N-ladder — the actual lever

Define **N(t)** = least edges of a 6-partite intersecting object with τ ≥ t
*having some part all of whose active vertices have degree ≥ 2*.

**(C) Deletion.** Delete k same-part vertices from a counterexample. The residual
has m − Σdeg edges and τ ≥ 6−k, *and every remaining vertex of that part keeps
all of its edges* (an edge has exactly one vertex per part) — so by (A) and (B)
the residual has ≥ 6−k vertices of degree ≥ 2 in that part. The residual is
therefore a witness for **N(6−k), not merely g(6−k)**:

  the k largest degrees of any part sum to at most **m − N(6−k)**.

Computed exactly this turn: **N(1)=2, N(2)=4, N(3)=6, N(4)=9**.

- N(t) ≥ 2t is forced (≥ t blocks, each ≥ 2). N(1..3) meet it; witnesses found.
- **N(4) ≥ 9** is the pointer's question answered: at 8 edges a full part must be
  exactly (2,2,2,2) — four vertices minimum since a part is a cover, each ≥ 2,
  summing to 8 — and no such object exists. Exhaustive column search, **52.0M
  nodes, 268 s**. Two independent agreements, neither used as input: AKP Lemma
  2.1 (a degree-3 vertex in every part forces a part sum ≥ 3+2+2+2 = 9 > 8), and
  this lab's own 5-class census at (8,4), every part (3,2,2,1) or (3,2,1,1,1).
- **N(4) ≤ 9** by construction, not search: take our (8,4) census class whose
  part 1 is (3,2,2,1) and add one edge whose part-1 vertex is that part's
  degree-1 vertex, choosing the other five coordinates to meet all eight old
  edges. `(0,2,1,2,2,2)` does it. τ can only rise, so τ = 4 still, and part 1
  becomes (3,2,2,2).

## 4. What the ladder now returns

Maximising (L2) — Σ_parts Σ_v C(deg v,2) ≥ C(m,2) — over profiles admissible
under (A), (B), (C):

| caps | floor | note |
| --- | --- | --- |
| cert 0001's (g, degree ≥ 1) | 18 / 19 | reproduced exactly as a control |
| (A)+(B) only, g-caps | 19 | m=19 slack falls 9 → 3 |
| N-caps, N(5) ≥ N(4)+2 = 11 | **19** | **cites nothing** |
| N-caps, N(5) = 13 (f(6) cited) | **20** | **m = 19 dies outright** |
| N-caps, N(5) ≥ 14 | 21 | *the remaining question* |

At m = 20 exactly one maximum degree survives: **Δ = 7**, maximiser
(7,4,3,2,2,2), slack 8. Both m=20 Δ=5 and Δ=6 die by counting alone here — Δ=5
had needed cert 0003's separate low-incidence argument.

Certificate 0005, 30 checks, ~5 min, stdlib, no solver.

## 5. The gap is now a single well-posed question

Δ = 7 at m = 20 saturates the k=1 cap (7 = 20 − 13), so the degree-7 vertex's
complement R has exactly 13 edges; τ(R) ≥ 5 by peeling and τ(R) = 6 is excluded
(that would be a 13-edge counterexample), so R is **f(6)-extremal**; and by
(A)+(B) its part-i profile is a partition of 13 into ≥5 entries each ≥ 2. So:

> **Q13.** Is there a 6-partite intersecting hypergraph with 13 edges, τ ≥ 5,
> and a part all of whose vertices have degree ≥ 2?
>
> **NO ⟹ N(5) ≥ 14 ⟹ Δ ≤ m−14 ⟹ m ≥ 21.** Nothing else is needed.

Under the N-caps the distinguished part has one of exactly three profiles:
(4,3,2,2,2) · (3,3,3,2,2) · (3,2,2,2,2,2), with waste budgets 9, 8 and 5.
This is what replaces the "broad (13,5) run" of turn 4: not a census of every
f(6)-extremal object, but one existence question with column 0 pinned.

## 6. Q13 — measured, not settled

Direct column search, the same engine as N(4) with lazy column generation and a
disjoint 232-way split at the first free column's block. Rate ≈ 35k nodes/s
against 194k/s at ρ=8; profile (3,2,2,2,2,2) ran 42M nodes single-threaded
without exhausting.

**Honest status: Q13 is open.** The floor stands at **m ≥ 20**.

## 7. A fallback that does not work, and how close it came

m=20 Δ=7 can also be attacked by counting alone: pick each part's maximum-degree
vertex u_j, put k_E = |E ∩ {u_j}|, and play (L7) against (L4).

- (L7): deleting two stars leaves τ ≥ 4, so |star(u_i) ∪ star(u_j)| ≤ m−g(4) = 12
  and Σ_E C(k_E,2) = Σ_{i<j}|star(u_i) ∩ star(u_j)| ≥ Σ max(0, M_i+M_j−12).
- (L4) + the value pool bound Σ_E C(k_E,2) from above: an edge missing u_j gets
  at most the *second* degree of part j, so edges poor in maximum-degree vertices
  are expensive in high-degree slots, and the slots are a fixed pool.

105 profile multisets pass the pair count; 10 die on the concentration bound
alone. The exact pool DP then kills more — 13 of the first 59 checked, at ~15–30 s
each — but **all six parts (7,4,3,2,2,2) survives with maximum 30 against a
requirement of exactly 30.** Dead heat, and it is case 1, so the verdict does not
depend on finishing the sweep (stopped at 59/95: 46 alive, 13 dead). The route
does not close m = 20 and is recorded as a measured near-miss, not a lever.

**The unused lever the same enumeration hands over:** every one of the 105
multisets contains **at least two parts with a degree-7 vertex** — the best d1=7
profile scores 33 and the best d1≤6 scores 31, so reaching 190 forces it. Two
degree-7 vertices in different parts then satisfy |star(u) ∩ star(w)| ≥ 2 by (L7).
That does not go through Q13 at all, and is the obvious next thing to push.

## 8. Cost data

- N(4) ≥ 9 exhaustion at ρ=8: 52.0M nodes, 268 s, 2220 admissible columns.
- Same engine with columns regenerated lazily rather than precomputed: >7 min and
  unfinished on the same instance. **Precompute when the partition list fits;
  the lazy generator is for ρ ≥ 11 only.**
- Q13 ρ=13: ≈35k nodes/s; 232 disjoint slices available for parallelism.
- The (L4)+(L7) pool DP: ~15 s per profile multiset, 95 to check.

## 9. What would have gone wrong

The tail-profile slip in cert 0002 is the lesson of the turn: **a cited structure
theorem was combined with an unstated and false assumption of our own** — that a
counterexample may contain degree-1 vertices. The lemma was cited correctly; the
error was in what we let it sit next to. Lemma 2.1 was not subsumed by the
ladder, as cert 0002 recorded; it was *underused*, and the two-line lemma (A) is
what unlocks it.

---

# 2026-07-26 · turn 6 (same session) — (L8) closes m = 20; the floor is **m ≥ 21**

## 10. Codex's hint (relayed by JD), and what it turned out to be

**Attribution corrected after the fact — this was recorded as JD's own and it is
not.** The hint below is **Codex's**, passed on by JD in conversation; no sealed
path was read. It matters, because a station of the correlated chain seeded the
final step, and the honest label on m ≥ 21 is therefore **partially independent,
not blind**. See D-010.

> *Let x,y be the forced degree-7 vertices, c = |E(x) ∩ E(y)| ≥ 2. Feed that
> overlap back into the pair-intersection count. The c common-star edges
> contribute at least C(c,2) ≥ 1 units of excess, because every pair among them
> meets at both x and y. So Σ_v C(d(v),2) ≥ 191, not merely 190.*

The move is to stop reading the pair count as a bound to be *met* and read the
surplus as a **budget to be spent**. Section 7 above had the (L4)/(L7) squeeze end
at 30 against exactly 30 and filed it as a dead heat. It is not a dead heat: the
equality forces every c_ij = 2, and the budget then cannot pay for the
consequences.

One refinement was needed past the ≥191. The overlap costs excess *and* forces
edges rich in maximum-degree vertices, and those cost a second budget:

  δ(k) := C(k,2) − (k−1) ≥ 0, and Σ_e δ(k_e) = A − Σ_j M_j + m =: D.

Since t_ef ≤ min(k_e,k_f), pairs at level ≥ t live inside W_t = {e : k_e ≥ t}, so
D ≥ q₃ + 2q₄ + 3q₅ with q_t the least q with C(q,2) ≥ #{pairs at level ≥ t}.

**(L8)**: (L7) forces B = Σ_{i<j}C(c_ij,2) large; C(t,2)/(t−1) = t/2 ≤ 5/2 with
t ≤ 5 forces B ≤ ⌊5X/2⌋; so B must be carried by many shallow pairs (X forbids) or
deep ones (D forbids). At m = 20, every one of the 105 admissible configurations
fails. **Cert 0006 GREEN, 19 checks, 66 s.**

For the dead-heat case concretely: c_ij = 2 for all 15 part-pairs → B = 15; with
X = 8 and t ≤ 5 only {5,3,2,2} and {4,4,3} reach 15; they need δ-budgets 13 and 9
against D = 8.

## 11. Why it does not prove too much

The result lands exactly on the number under verification — D-005's most
dangerous direction. Four controls:

- **Positive control**: the δ-budget inequality holds with room on all four real
  witnesses (D = 12, 4, 6, 12 against needs 6, 0, 0, 7).
- **Not-too-strong**: the identical machinery at m = 21 leaves **6198 of 43875**
  multisets alive. Had it killed every m it would be proving Ryser at r=6 and
  would therefore be wrong.
- **Identity audit**: all four identities and both inequalities brute-forced on
  420 random intersecting objects across seven sizes.
- **Conservative ceiling**: the final version uses *no* value pool and *no* (L4) —
  only "Σ k_e = Σ M_j over m edges with k ≤ 6", i.e. maximum concentration. That is
  strictly weaker than the pool DP, so strictly more permissive, and it still kills
  all 105. A whole layer left the trust chain. (Two independent implementations of
  the pool DP had agreed at 30 first.)

**Why 20 dies and 21 doesn't, in one line:** at m=20 the best profile scores 33, so
reaching 190 leaves excess X ≤ 8 while (L7) demands B ≥ 15; at m=21 the same
arithmetic leaves X = 30.

## 12. Ledger for m ≥ 21

Three lemmas of ours ((A),(B),(C)), one exhaustive search of ours (N(4)=9, 52.0M
nodes), two counting lemmas of ours ((L7),(L8) — the latter **seeded by Codex and
re-derived here**), and **one cited lemma**. No solver anywhere; no
isomorphism-class census anywhere.

**The citation, now read firsthand** (published literature, which the seal does not
cover — AKP arXiv:1409.4938): f(6) ≥ 13 is *proved*, not inferred from the 13-edge
construction. Theorem 1.1 gives f(6) = 13, independently obtained by ABW; §2 splits
it as "f(6) ≠ 12" (Lemma 2.9, a case analysis on Δ) plus MSY's f(6) > 11. And
Lemma 2.9's hard case is Δ(H) = 4, which the paper says outright "will require some
facts concerning the degree structure of intersecting 6-partite hypergraphs with 8
hyperedges and a covering number equal to 4" — **that is Lemma 2.8, the lemma we
found the erratum in and whose corrected form cert 0005 proves outright.**

So the exposure is not a constant but one lemma:

| piece of f(6) ≥ 13 | status here |
| --- | --- |
| f(6) ≥ 12 (MSY) | **independently ours** — cert 0001's g(5) ≥ 12 |
| Lemma 2.8 (the hard case's structural input) | **independently ours** — cert 0005 |
| Lemma 2.9's case analysis itself | **cited, not reproduced** |

Our erratum work therefore *shores up* the citation rather than undermining it: we
have proven the corrected form of the lemma its hardest case depends on.

**Q13 was not answered — it became unnecessary.** It stays the natural next lever:
NO there would push the floor past 21 through the 0005 ladder alone.
