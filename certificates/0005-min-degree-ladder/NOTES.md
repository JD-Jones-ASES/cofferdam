# Certificate 0005 — the minimum-degree ladder; m ≥ 20, and the gap becomes one question

**Status: GREEN.** 40 checks, `python3 verify.py`, stdlib only, no solver.
Measured runtime **~8 min on Python 3.10+**, **~42 min on Python 3.9** (which is what
macOS ships as `/usr/bin/python3`; the fallback popcount is ~5x slower). Green either
way — it is slow, not hung.

| claim | label |
| --- | --- |
| (A) no active vertex has degree 1 · (B) every part has ≥ 6 active vertices | PROVEN (two-line arguments, stated below) |
| N(1), N(2), N(3), N(4) = 2, 4, 6, 9 | PROVEN-BY-CERTIFICATE |
| **a Ryser r=6 counterexample has m ≥ 19** | **PROVEN-BY-CERTIFICATE, citing nothing** |
| **…has m ≥ 20** | **PROVEN-MODULO-CITATION**, the citation being f(6)=13 |
| m = 20 leaves exactly Δ = 7, whose 13-edge complement is f(6)-extremal with a full part | same |
| Q13 answered NO would give m ≥ 21 | the whole remaining gap |

Certificate 0001 reached m ≥ 18 / m ≥ 19. This moves both rungs by one, using the
*same* counting argument over a strictly smaller set of admissible profiles.
Certs 0001–0003 are reproduced inside this one as a control (checks 29–31).

## Provenance

Three labs worked this in parallel; this one fell behind and inherited the thread.
The pointer that opened this certificate came from Codex — *inspect the equality case
when deleting the stars of two vertices in the same part; every part of a τ=6 example
has at least 6 active vertices; no active vertex can have degree one; what must that
part look like in an eight-edge residual?* — so (A) and (B) below are given
statements and the proofs, the N-ladder, the searches and the controls are this
repo's. Nothing sealed was read.

## The two lemmas, and why they were missed

**(A)** Let E be an edge and x ∈ E. Then |E \ {x}| = 5 < 6 = τ, so E \ {x} is not
a cover: some edge F misses all of it. F must still meet E, so F ∩ E = {x}. Hence
x lies in a second edge: **deg(x) ≥ 2**. No minimality hypothesis is used.

**(B)** The active vertices of one part meet every edge — each edge has exactly
one — so a part is itself a cover: **|V_i| ≥ τ = 6**.

Both are immediate once stated — and being *stated* is what we were missing. The
ladder was being read as a statement about *degrees*; these are statements about
*parts*. Certificate 0002 in fact ran the relevant equality case, and got it wrong: it inferred that
the residual tail must be (3,2,1,1,1) and that the existing caps already forced
that, concluding AKP Lemma 2.1 was "subsumed — moves the floor by nothing". With
(A) in hand, a tail containing a degree-1 vertex is impossible, and the equality
case is not constrained but **empty**. That correction is this certificate.

## N(t), and why it is the right object

  **N(t)** = least edges of a 6-partite intersecting object with τ ≥ t that has
  **some part all of whose active vertices have degree ≥ 2**.

The point is the deletion lemma **(C)**: delete k vertices of one part of a
counterexample. The residual has τ ≥ 6−k, and the *surviving* vertices of that
part keep every one of their edges — an edge has exactly one vertex per part, so
nothing they carry can pass through a deleted vertex. By (A) each still has degree
≥ 2, and by (B) there are ≥ 6−k of them. So the residual witnesses N(6−k), not
merely g(6−k), and the k largest degrees of any part sum to at most **m − N(6−k)**.

Since N(t) ≥ g(t) always, every cap can only tighten. The gain is entirely in
N(4) = 9 > g(4) = 8.

## N(4) = 9

**Lower.** A full part at 8 edges has ≥ 4 vertices (a part is a cover and τ = 4),
each of degree ≥ 2, summing to 8 — so it is exactly (2,2,2,2). Exhaustive column
search with column 0 pinned to that profile: **none exists**. 52.0M nodes, 268 s,
2220 admissible columns.

Two independent agreements, *neither used as an input*:
- Abu-Khazneh–Pokrovskiy Lemma 2.1 — an 8-edge τ=4 object has a degree-3 vertex in
  every part; with three more vertices of degree ≥ 2 that part would sum to ≥ 9 > 8.
- This lab's own census of the five (8,4) classes: every part is (3,2,2,1) or
  (3,2,1,1,1), so every part has a degree-1 vertex.

**Upper.** Built, not searched. Take our census class 5, whose part 1 is
(3,2,2,1), and add one edge whose part-1 vertex is that part's degree-1 vertex,
with its other five coordinates chosen to meet all eight old edges:
`(0,2,1,2,2,2)`. τ can only rise, so it is still 4, and part 1 becomes (3,2,2,2).

## Corollary at almost no extra cost: AKP Lemma 2.8, corrected and certified

A part of an (8, τ=4) object is a cover, so it has ≥ 4 vertices; that leaves
eight conceivable profiles. Three die on the pair count alone, (2,2,2,2) died
above, and (3,1,1,1,1,1) and (2,2,2,1,1) die by exhaustive search here — 2.8M
nodes / 31 s and 7.0M nodes / 72 s, both with waste budget 0. What survives is
exactly **(3,2,2,1) and (3,2,1,1,1)**.

That is Abu-Khazneh–Pokrovskiy Lemma 2.8 with its arithmetic corrected (as
printed, its second structure sums to 9, not 8 — see the erratum note), now
**proven here**, and it reproduces the part profiles of this lab's own 5-class
(8,4) census by a route sharing no machinery with it. It also re-derives AKP
Lemma 2.1's "a degree-3 vertex in every part" clause as a consequence rather
than a citation.

## Reading the witness — one trap worth naming

"Part 1" of the 9-edge N(4) witness means **0-indexed coordinate 1**, the second
coordinate. Coordinate 0 is (4,2,1,1,1) and is *not* full. A checker who reads
"part 1" as the first coordinate will wrongly reject a good witness. (Caught by
the adversarial re-derivation, which cost itself time on exactly this.)

## What the ladder returns

| caps | least surviving m |
| --- | --- |
| cert 0001's (g-caps, degree ≥ 1, no minimum part size) | 19 — reproduced exactly, as a control |
| (A)+(B) with g-caps | 19, but m=19's slack falls 9 → 3 |
| N-caps with N(5) ≥ N(4)+2 = 11 (**cites nothing**) | **19** |
| N-caps with N(5) = 13 (**cites f(6)=13**) | **20** |
| N-caps with N(5) ≥ 14 | 21 |

At m = 20 the survivors go from {Δ=5,6,7} to **Δ=7 alone**; Δ=5 had previously
needed certificate 0003's separate low-incidence argument, and now dies by
counting.

## The single remaining question

Δ = 7 at m = 20 saturates the k=1 cap (7 = 20 − 13). So the degree-7 vertex's
complement R has exactly 13 edges; τ(R) ≥ 5 by peeling, and τ(R) = 6 would make R
a 13-edge counterexample, which the floor already excludes — so R is
**f(6)-extremal**, and by (A)+(B) its part-i profile is a partition of 13 into
≥ 5 entries each ≥ 2.

> **Q13.** Is there a 6-partite intersecting hypergraph with 13 edges, τ ≥ 5, and
> a part all of whose active vertices have degree ≥ 2?
>
> **NO ⟹ N(5) ≥ 14 ⟹ Δ ≤ m−14 ⟹ m ≥ 21.**

Only three profiles are possible for that part: (4,3,2,2,2), (3,3,3,2,2),
(3,2,2,2,2,2), with waste budgets 9, 8, 5. **Q13 is open**; see the notebook entry
for the measured search cost and for the counting-only fallback that came to a
dead heat (max 30 against a requirement of exactly 30) and therefore fails.

## Independent re-derivation, and what it flagged

The chain was handed to an adversarial re-derivation with instructions to break
it. It confirmed every step and **re-proved N(4) ≥ 9 by a search of a different
design** (50.75M nodes, 48 s, zero solutions) whose positive control — the same
machinery with the full-part requirement dropped — recovers exactly the two
part-profile multisets the corollary above predicts. Three findings worth
keeping:

- **Sensitivity.** m ≥ 20 rests on exactly three things: (A)+(B)+(C), N(4) = 9
  (now ours twice, by two unrelated searches), and the citation f(6) ≥ 13.
  Perturb any one and the floor falls back to 19 (or to 16 with no N-ladder).
  **f(6) ≥ 13 is now the single largest unverified load in this lab** — and it
  is the *lower* bound that is needed, whereas extremal constants are often
  reported as best-known constructions. Our own citation-free bound is g(5) ≥ 12,
  and the entire distance from m ≥ 19 to m ≥ 20 lives in 12 versus 13.
- **No circularity.** Excluding τ(R) = 6 uses cert 0001's m ≥ 18, which cites
  nothing — not the f(6) figure the same argument is deriving from.
- **A second lever on m = 20, unused here.** Every one of the 105 profile
  multisets that reach C(20,2) contains **at least two parts with a degree-7
  vertex**. So an m=20 counterexample has two degree-7 vertices in different
  parts, and (L7) forces their stars to share ≥ 2 edges. That does not go through
  Q13 and is the obvious next thing to push.

Strictly, the 13-edge complement is a witness for **N(5) ≤ 13**; equality needs
N(5) ≥ g(5) = 13, the cited constant. And "Q13 NO ⟹ N(5) ≥ 14" also uses g(5)=13
to dispose of the ≤ 12-edge case.

## Cited-input discipline

The only external input is **f(6) = 13**, used solely as the k=1 cap. Without it
the certificate still derives N(5) ≥ N(4) + 2 = 11 from its own machinery and
still reaches **m ≥ 19** — one better than certificate 0001's citation-free
bound. Certificate 0001's g-values are not taken on trust: g(1..4) = 1,3,5,8 are
re-derived here, the lower bounds by counting and the upper bounds by explicit
witnesses.

## Reproduce

```bash
python3 verify.py
```

Deterministic, and dominated by the ρ=8 exhaustion — which visits exactly
**52,023,309 nodes**, a figure worth checking against if you modify the engine, since
any change to the traversal moves it. ~8 min on 3.10+, ~42 min on 3.9.
