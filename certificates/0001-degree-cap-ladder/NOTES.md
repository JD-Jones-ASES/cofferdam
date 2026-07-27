# Certificate 0001 — the degree-cap ladder and the Ryser r=6 floor

**Status: GREEN.** 22 checks, ~96 s, `python3 verify.py`, stdlib only, no solver.

| claim | label |
| --- | --- |
| g(1)=1, g(2)=3, g(3)=5, g(4)=8 | PROVEN-BY-CERTIFICATE (T1) |
| g(5) ≥ 12 | PROVEN-BY-CERTIFICATE (T1) |
| **a Ryser r=6 intersecting counterexample has m ≥ 18** | **PROVEN-BY-CERTIFICATE (T1), citing nothing** |
| **…has m ≥ 19** | **PROVEN-MODULO-CITATION**, the citation being f(6)=13 |

g(t) is the least number of edges in a 6-partite 6-uniform intersecting
hypergraph with τ ≥ t. A counterexample to Ryser at r=6 in the intersecting case
is exactly an object counted by g(6), so the minimum counterexample size **is**
g(6).

## The argument in two lemmas

**(L1) Cap lemma.** If τ(H) ≥ t and S is any set of k < t vertices, the edges
avoiding S form a 6-partite intersecting family with τ ≥ t−k — because a cover of
*those* of size t−1−k, together with S, would cover H with t−1 vertices. Hence
they number at least g(t−k). When the k vertices share a part their stars are
disjoint, so degrees add and this becomes a prefix cap on that part's sorted
degree profile: the k largest degrees sum to at most m − g(t−k).

**(L2) Pair count.** Every pair of edges agrees in some part; in part i such a
pair shares a vertex v and is counted once in C(deg v, 2). So
Σ_parts Σ_v C(deg v, 2) ≥ C(m,2).

Cap the profiles with (L1), maximise (L2)'s left side over admissible profiles,
and if the maximum falls short of C(m,2) no such H exists. Walk m upward for
g(t); walk t upward from g(1)=1 for the ladder.

## Where the numbers come from

g(2), g(3), g(4) are settled by **absence search plus an explicit witness** —
both directions, in the certificate. The engine represents the hypergraph as 6
partitions of the edge set: a block is a vertex, its size is that vertex's
degree, intersecting means the partitions jointly cover all C(m,2) pairs, and
τ is the least number of blocks covering [m].

> **Corrected 2026-07-27 (turn 9).** This file used to open the paragraph with
> "counting alone is not tight at the bottom". That is **false** — the
> (L1)+(L2) counting ladder walked from g(1)=1 returns exactly 3, 5, 8, 12,
> tight through g(5) — and worse, instrumented replay shows the absence
> searches **never branch**: at every sub-threshold m the root waste-budget
> prune (6·maxcov < C(m,2)) kills in one node, and that prune *is* the
> counting argument. So the two "directions" are real (witness vs absence),
> but the two *lower-bound routes* this lab believed it had were one argument
> in two code forms (D-028). The genuinely independent second route — a
> definitions-only brute force with no (L1)/(L2) — is recorded in the turn-9
> notebook. A hand-readable statement of the counting kills now lives in
> certificates 0009 §1 and 0010 §1.

The g(3)=5 witness is worth keeping: columns 0–4 realise a proper 5-edge-colouring
of K₅ (pair {i,j} takes colour i+j mod 5), so each is a matching on the five
edges and every pair of edges agrees exactly once; column 5 is all-distinct. Max
degree 2, so any two vertices cover at most 4 of the 5 edges and τ ≥ 3 comes for
free. **Bounded degree forcing τ from below is the cheapest τ-raising trick there
is**, and it is what makes these small extremal objects sparse rather than dense.

### Two wrong guesses, both caught by computing

Before searching, this lab guessed g(3)=6 and g(4)=9, reasoning from the
embedding g₆(t) ≤ f(t+1) (pad an extremal (t+1)-partite family with all-distinct
columns). Those are upper bounds only, and both were loose: the truth is 5 and 8.
The guesses were not idle — with g(3)=6 and g(4)=9 the ladder returns a floor of
**20**, one rung short of the chain's claim. Believing them would have produced a
much stronger and entirely false result, and it would have agreed suspiciously
well with the number this lab is supposed to be checking. Compute the rungs; do
not infer them from the shape of the answer you expect.

## Where this stops, and why

With the proven values (g(4)=8) and the cited f(6)=13:

| m | per-part maximum | 6 × max | C(m,2) | slack |
| --- | --- | --- | --- | --- |
| 18 | 25 at (5,5,3,2,2,1) | 150 | 153 | **−3 → dead** |
| 19 | 30 at (6,5,3,2,2,1) | 180 | 171 | +9 |
| 20 | 36 at (7,5,3,2,2,1) | 216 | 190 | +26 |

So the counting ladder dies at m=19 and the method's reach ends there. Note how
fast the slack grows: this is not a bound that will be nudged to 21 by tightening
constants.

**The slack is the excess.** Σ_parts Σ_v C(d,2) = C(m,2) + X where
X = Σ_pairs (λ−1), λ being the number of parts in which that pair of edges agrees.
So "slack 9" at m=19 says an object there has at most 9 units of repeated
agreement across all 171 pairs — it is forced to be nearly *linear*. That matters,
because Ryser is proven for linear intersecting hypergraphs at r ≤ 9 (Francetić,
Herke, McKay, Wanless), so a counterexample must be non-linear (X ≥ 1) while the
counting forces it to be barely non-linear. Squeezing that vice is the obvious
next move and it is not attempted here.

## The lever that was built before it was used — it is now (L7)

(L1) was applied only in its **same-part** form, where stars are disjoint and
degrees add. The general form is stronger and cross-part: for *any* k vertices,

  | union of their stars | ≤ m − g(t−k).

`lib/columns.py` implements this at k=2 as a search prune (`union_bound_violated`)
and it is what made the g(4) search tractable — 88 s with it against 576 s
without, both runs returning the same witness. It is **not** in the counting
ladder, because the ladder optimises each part independently and a cross-part
constraint couples them. Folding it in means optimising over the whole 6-part
structure at once. That is the first thing to try against m=19, where the slack
is only 9 and where the maximising profile (6,5,3,2,2,1) saturates every one of
the five caps simultaneously — which forces the degree-6 vertex's 13-edge
complement to be an *extremal* f(6)=13 object, a very rigid thing to have to
contain six times over.

## Relation to the claim under verification

The claim this lab was seeded with is **m ≥ 21**. This certificate independently
reaches **m ≥ 19** by a route that is closed-form counting rather than per-class
case elimination. It therefore:

- **corroborates** every rung of the chain up to and including the exclusion of
  m ≤ 18, by an argument that shares no machinery with it;
- **did not, at turn 1, confirm** the exclusion of m = 19 or m = 20. Those two
  rungs were the entire unverified remainder of the claim, and m = 20 is exactly
  where the predecessor lab's residual (179 classes at R ≥ 8) was left undecided.
  Both are now closed — m = 19 by certificate 0005 citing nothing, m = 20 by
  certificates 0006 and 0007.

Nothing here should be read as evidence for or against m ≥ 21. It narrows what
would have to be wrong for the claim to fail.

## Reproduce

```bash
python3 verify.py
```

Runtime ~96 s on an idle box (~227 s measured under load, turn 9).
**Corrected 2026-07-27:** the runtime is dominated by the section [C] witness
re-finding at m = 8 (3,702,067 nodes), **not** by the m=7 absence check — that
one is a single node (its root prune is the counting kill; see the correction
above). Deterministic.
