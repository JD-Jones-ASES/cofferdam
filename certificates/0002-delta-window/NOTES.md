# Certificate 0002 — the maximum-degree window; m = 19 reduced to one case

**Status: GREEN.** 22 checks + 1 note, instant, `python3 verify.py`, stdlib only,
no solver. Green under `python3 -O` too. (It advertised 23 checks until the
literal-`True` one was reclassified as a note — a stated fact, not a machine test.)

| claim | label |
| --- | --- |
| (L4) every edge E has Σ_{v∈E} deg(v) ≥ m+5, hence Δ ≥ 1+⌈(m−1)/6⌉ | PROVEN-BY-CERTIFICATE |
| the Δ-refined pair count, case by case | PROVEN-BY-CERTIFICATE, given cert 0001's g-values |
| **an m=19 counterexample has Δ = 6 exactly** | **PROVEN-MODULO-CITATION** (needs f(6)=13) |
| **its degree-6 vertex's complement is an f(6)-extremal 13-edge object** | same |
| the floor is unchanged at m ≥ 19 | — this is a reduction, not an improvement |

## Origin: what the pointer to AKP Lemma 2.1 actually bought

Abu-Khazneh–Pokrovskiy Lemma 2.1 (arXiv:1409.4938): *an intersecting 6-partite
hypergraph with 8 edges and τ = 4 contains a degree-3 vertex in each partition,
and two of its edges share at least two degree-3 vertices.*

That is a structure theorem for **exactly** the object cert 0001's g₆(4) = 8 search
produced, so the first thing done was a two-way check. Our independently-found
8-edge witness satisfies every clause: Δ = 3, exactly six degree-3 vertices, one
per part, every pair of them in a common edge (their Claim 2.4), and edges 1 and 2
sharing two of them. Their lemma is confirmed on an object found without it; our
search is confirmed against published structure.

**Then the honest negative result.** Folding Lemma 2.1 into the ladder as a
saturation condition gives: if two vertices u,v of one part have deg(u)+deg(v) =
m−8, the residual is an 8-edge τ=4 object, so by Lemma 2.1 every *other* vertex of
that part has degree ≤ 3 with at least one equal to 3 — forcing the tail profile to
(3,2,2,1). But cert 0001's 3-, 4- and 5-caps **already force exactly that tail**.
So Lemma 2.1's content is subsumed by the existing ladder and moves the floor by
nothing. Worth recording: the ladder turns out to already encode this structure.

> **This paragraph is WRONG and is kept only as the record of the error.** See
> D-006. The caps do not force that tail uniquely; the reading rested on an
> unstated assumption of our own — that a counterexample may hold degree-1
> vertices, which lemma (A) forbids. With (A), the equality case is not
> constrained but *empty*, and the same lemma moves the floor by a full rung.
> The failure mode was accepting a *negative* result without auditing the
> assumptions around it, which is why D-006 now requires a recorded dead end to
> name the assumptions under which it is dead.

**What did move was the proof technique, not the lemma.** Their Claim 2.3 runs a
pigeonhole at m = 8 — an edge has 6 vertices and must meet 7 others, so one vertex
has degree 3. Run the same count at general m and it becomes (L4).

## (L4) and why it is strictly stronger than (L2)

For any edge E, the other m−1 edges each meet E at one of its 6 vertices, so
Σ_{v∈E}(deg v − 1) ≥ m−1, i.e. **Σ_{v∈E} deg(v) ≥ m+5**.

Summing over all edges gives Σ_v deg(v)² ≥ m(m+5), which rearranges to
Σ_v C(deg v, 2) ≥ C(m,2) — cert 0001's (L2), exactly. The certificate checks this
identity for m = 14..24. So **(L2) is the average of (L4)**, and (L4) is the
pointwise refinement. That is the whole gain: the ladder was using an averaged
consequence of a per-edge fact.

Immediate consequence: some vertex of every edge has degree ≥ 1+⌈(m−1)/6⌉, so
**Δ ≥ 1+⌈(m−1)/6⌉**. Against cert 0001's **Δ ≤ m − 13**, that is a window.

## The Δ-refined counting

Re-run the pair count with the degree cap tightened to a hypothesised Δ:

| m | Δ | max/part | 6·max vs C(m,2) | |
| --- | --- | --- | --- | --- |
| 19 | 4 | 25 at (4,4,4,4,2,1) | 150 vs 171 | **dead** |
| 19 | 5 | 28 at (5,5,4,2,2,1) | 168 vs 171 | **dead** |
| 19 | 6 | 30 at (6,5,3,2,2,1) | 180 vs 171 | survives, slack 9 |
| 20 | 5 | 32 at (5,5,5,2,2,1) | 192 vs 190 | survives, **slack 2** |
| 20 | 6 | 35 at (6,6,3,2,2,1) | 210 vs 190 | survives, slack 20 |
| 20 | 7 | 36 at (7,5,3,2,2,1) | 216 vs 190 | survives, slack 26 |
| 21 | 5 | 34 at (5,5,5,3,2,1) | 204 vs 210 | **dead** |

Δ = 4 at m = 19 dies a second, independent way. 6·4 = 24 = m+5 exactly, so (L4)
holds with equality on every edge — which forces *every* vertex to have degree
exactly 4, and then the total degree 6m = 114 would have to be divisible by 4.
It is not. Two kills of one case by unrelated arguments is the kind of redundancy
worth having in a verification.

## The consequence, and why it matters

**An m = 19 counterexample has a vertex of degree exactly 6, and deleting it leaves
exactly 13 edges with τ ≥ 5 — an f(6)-extremal hypergraph.**

So the first unconfirmed rung is no longer an open search. It is a single extension
question: *can an f(6)-extremal 13-edge object be extended by six edges through one
new common vertex so that τ reaches 6?* That is finite and well-posed, and it is
precisely the "seed from the sparse family and grow by edge addition" route the
status note recommended over perturbing PG(2,5).

Note from Aharoni–Barát–Wanless: f(r) is achieved only by linear hypergraphs for
r ≤ 5, **but not for r ∈ {6,7}** — so the 13-edge extremal family includes
non-linear members and cannot be assumed linear when this is attempted.

## What is needed to finish m = 19, and the measured obstacle

Either the classification of f(6)-extremal 13-edge hypergraphs from the literature,
or generating them here. Generating them was attempted and is **out of reach with
the current engine**: `partitions_bounded(13, 5, caps)` did not finish enumerating
even the admissible partition list. The engine materialises the full partition list
before searching, which is fine at m = 8 (2220 partitions) and hopeless at m = 13.
The fix is engineering, not mathematics — generate partitions lazily, indexed by
the pair they must join, so the list is never built. That is the next build task.

## m = 20

Three cases survive, and Δ = 5 survives on a slack of 2 — the tightest number at turn 2 (the m = 20 kill's margin of 1, D-017, is tighter)
anywhere in this lab. It also forces near-uniform structure: essentially every part
must carry profile (5,5,5,2,2,1). That is the natural next target, and unlike
m = 19 it needs no classification input.
