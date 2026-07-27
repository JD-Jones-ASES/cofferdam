# Certificate 0011 — **Δ = 4 exactly**, for 13 edges at τ ≥ 5

**Status: GREEN.** 61 checks + 12 notes, **176 s** bare / **170 s** under `-O`
on the iMac, `python3 verify.py`, stdlib only, no solver, no imports from
`lib/`. Green under a bare `/usr/bin/python3` (3.9.6) **and** under
`python3 -O`; the two runs' check lines are byte-identical apart from
elapsed-seconds figures. (An earlier assembly had 62 checks; one of them —
`5 − 4 == 1` — was a literal-arithmetic tautology, the exact D-015 pattern,
and was demoted to a note at desk review. Its real content is §5's check
that the uncapped enumeration never produces a 2-fresh covering pattern.)

| claim | label |
| --- | --- |
| g(2) ≥ 3, g(3) ≥ 5, g(4) ≥ 8, g(5) ≥ 12 | **PROVEN-BY-CERTIFICATE** (§1, re-derived here) |
| the (8, τ ≥ 4) census is exactly **5 classes** | **PROVEN-BY-CERTIFICATE** (§4, two routes) |
| Δ ≥ 4 at m = 13, **any τ** | **PROVEN-BY-CERTIFICATE** (§2) |
| Δ ≤ 4 at m = 13, τ ≥ 5 | **PROVEN-BY-CERTIFICATE** (§5) |
| **every 6-partite 6-uniform intersecting hypergraph with 13 edges and τ ≥ 5 has Δ = 4 exactly** | **PROVEN-BY-CERTIFICATE, CITING NOTHING** |

**EXTERNAL INPUTS — NONE.** Nothing to remove, so no fallback statement to
make. In particular **f(6) = 13 is not used**: "13 edges" is a hypothesis of the
theorem, not a borrowed constant, and a reader who disbelieves f(6) = 13 loses
nothing here.

## Why this exists

It is **PLAN item 1** — the turn-4 peel-chain result that was still
uncertified, and that PLAN itself named "the cheapest place a real error could
still be hiding." Nothing downstream moves if it is wrong; that is exactly why
it was worth writing down properly instead of carrying as a remembered fact.

It is also deliberately *not* wired into the floor. §1 re-derives its own
ladder rather than importing certificate 0001's, so this file does not sit
downstream of N(4) = 9 — the hinge that carried the floor alone for two turns.

## The argument in one paragraph

**Δ ≥ 4** is pure counting and needs no hypothesis on τ: with every degree ≤ 3 a
part contributes at most 12 agreeing pairs (maximiser (3,3,3,3,1)), and
6 × 12 = 72 < 78 = C(13,2). **Δ ≤ 4** peels. If deg(v) = D ≥ 5 then
R = H \ star(v) has 13 − D edges and τ(R) ≥ 4, so 13 − D ≥ g(4) ≥ 8 forces
D = 5 and |R| = 8; and τ(R) ≥ 5 would need |R| ≥ g(5) ≥ 12, so **τ(R) = 4
exactly**. There are exactly **five** such R up to isomorphism. Each star edge
must cover R with its five non-p coordinates, so at most one of them is fresh;
and τ(H) ≥ 5 **iff** every 4-cover of R is avoided by some star edge — a
condition depending on the edge only through its *pattern*, hence through an
escape mask over the 4-cover list. At all 5 × 6 = 30 (residual, part) pairs, no
≤ 5 masks OR to all-ones. So no vertex of degree 5, and none above it.

## Margins — where this is tight and where it is not

| step | margin |
| --- | --- |
| Δ ≥ 4 (the pair count at m = 13) | **6 pairs** — 72 against 78 |
| Δ(R) = 3 for the residual (kills Δ ≤ 2) | **4 pairs** — 24 against 28 |
| X ≤ 2, the census excess prune | 30 against 28 — **two units of slack**, and the prune cuts the level-7 tree hard |
| (m = 7, τ ≥ 4) — the rung giving g(4) ≥ 8 | **3 pairs** — 18 against 21 |
| (m = 11, τ ≥ 5) — the rung giving g(5) ≥ 12 | **7 pairs** — 48 against 55 |
| max_fresh = 1 | **zero** — τ(R) = 4 out of 5 coordinates. One more free coordinate and the pattern space explodes; §5 and §6 both check this cap rather than assume it |
| the (L1) caps {1:3, 2:5, 3:7} | attained — every census class has Δ = 3 exactly, so the cap is not silently over-tight |

The one place with **no** margin is `max_fresh`, and it is the one place the
certificate refuses to take on trust: at all 30 pairs (and all 72 pairs of the
path-B rung) the pattern product is enumerated with **no cap at all** and the
cap is read off the result.

## The live tooth — a real bug, caught by a control, in this session

The A = B control is not decorative; it fired.

Path B's first prototype grouped patterns by escape mask, enumerated
distinct-mask triples, and then imposed an index ordering `ii ≤ jj ≤ kk`
**globally** while expanding each triple back into patterns. That is correct
*within* a repeated mask group and wrong *across* distinct groups. It returned
**4 classes, not 5** — a silently incomplete census, in the direction that
flatters the conclusion (fewer residuals to refute). Path A's 5 was what caught
it. Nothing else in the pipeline would have.

The shipped file does not fix that bug; it **removes the shape of it**. There is
no index arithmetic anywhere in path B: mask multisets come out of the same
element-driven search §5 uses, and patterns are drawn from each mask's group
with `combinations_with_replacement`, which is what "a star's patterns grouped
by their mask" literally *is*. Two further traps were designed out of the same
routine:

- `full_or_multisets` enumerates multisets of **exactly** three masks, not
  minimal ones. Stopping at a minimal full-OR subset would have dropped every
  object whose first two star edges already escape every 3-cover — the third
  edge still exists and still has to be built.
- The **TOOTH** control in §6 simulates the whole under-enumeration bug family
  in one line: set `max_fresh = 0` and re-run the seven positive controls. All
  seven fail, at the membership clause *and* at the search — a false
  "UNSOLVABLE" of exactly the shape §5 reports 30 times. An emptiness result is
  only as good as its enumeration, so the enumeration is the thing checked
  twice.

## What was checked twice on purpose

- **The census, by two routes with no shared enumeration.** Path A grows edge by
  edge from a single edge (Δ ≤ 3, prefix caps, τ lookahead, excess X ≤ 2). Path
  B peels a maximum-degree vertex to the (5, τ ≥ 3) census (12 classes) and
  re-attaches 3-stars through the escape machinery. Same 5 classes.
- **Canonical form, twice.** The census dedups by an invariant-restricted
  canonical form; the five finals are then re-canonicalised over all
  **720** part orders with no shortcut, and A and B agree there too.
- **Both directions of the escape equivalence §3(d), one rung below where §5
  spends them.** Path B checks τ ≥ 4 on all 46 objects it builds from full-OR
  mask triples — 0 failures: *sufficiency*. And path B enumerates **only**
  full-OR triples, so it can be complete just when every (8, τ ≥ 4) object's own
  3-star ORs to all-ones — so **A = B is a test of *necessity***, which is the
  direction §5 actually uses to kill. Path A never mentions a mask.
- **The machinery saying yes.** §6 peels each of W's seven degree-4 vertices and
  requires the *same* §5 code to return SOLVABLE, with W's own star patterns
  present in the enumerated list and their masks ORing to all-ones.
- **τ, in both directions, by brute force.** No 3-subset of V(R) covers R and
  4-subsets do, at every residual; and τ(W) = 5 by exhaustion over all
  C(30,4) = 27,405 vertex 4-sets.
- **The set-cover search, in two element orders.** Lowest-index-uncovered and
  static rarest-first. Both UNSOLVABLE at all 30 pairs. The node counts differ
  by ~64,000× (≈3.1 × 10⁸ against 4,832), which is worth knowing: the fast order
  is the one to use, and the slow one is the one that proves the fast one's
  ordering heuristic is not doing the deciding.

## What §7 adds, stated at its true size

A 13-edge τ ≥ 5 witness's **full** part (every active vertex of degree ≥ 2) has
one of exactly four degree profiles: (5,2,2,2,2), (4,3,2,2,2), (3,3,3,2,2),
(3,2,2,2,2,2). Δ ≤ 4 kills the first.

**That three-profile list is not new.** The turn-5 notebook already has it, from
the ladder cap d₁ ≤ 13 − N(4) = 4 — i.e. standing on N(4) = 9. What is new is
the **second route**: this one consumes g(4) ≥ 8 and g(5) ≥ 12 (eleven lines of
counting in §1) and never touches the hinge, and it bounds **all six** parts
rather than the distinguished one. Certificate 0008's witness W realises the
list: its part 1 is (4,3,2,2,2), one of the three survivors.

## What this does **not** do

- It does **not** move the floor. A Ryser counterexample has τ = 6; this is a
  statement about τ ≥ 5 at exactly 13 edges.
- It does **not** say a 13-edge τ ≥ 5 object exists. W says that, and W is
  carried as a control precisely so the theorem is not vacuously true — and so
  that Δ = 4 is exhibited as *attained*, at seven vertices.
- It does **not** license Δ ≤ 4 anywhere else. §5 consumes |R| = 8 and
  τ(R) = 4, which are consequences of m = 13 and of nothing more general. The
  same discipline certificate 0008 records for (D2): a cap proved at one rung is
  a false kill one rung down.

## Where a reviewer should push

1. **§1.** Both census routes consume the same ladder, so an error in g(3) ≥ 5
   or g(4) ≥ 8 moves both together — the A = B control cannot see it. It is
   eleven lines of counting and it is the widest target in the file.
2. **The census's completeness**, not its correctness. Every class it *found* is
   verified to be a genuine (8, τ = 4) object; the claim at risk is that there
   is no sixth. Both routes prune with (L1) caps and (for path A) the excess
   bound X ≤ 2 — the monotonicity argument for X is stated in a note and is
   the least machine-checked step in §4.
3. **`covering_patterns`.** Everything in §5 is downstream of it. It is checked
   for the cap it derives and for membership on a real object, but a systematic
   omission that also affected W's own patterns would pass both.

## Run log — the numbers a re-implementation should match

| quantity | value |
| --- | --- |
| path A level sizes, 1→8 edges | 1, 3, 8, 41, 272, 1725, 4501, **5** |
| path B (5, τ ≥ 3) level sizes | 1, 3, 4, 21, **12** |
| path B candidate objects built | 46, of which **0** fail τ ≥ 4 |
| residual vertex counts \|V(R)\| | 24, 24, 24, 24, 25 |
| 4-covers per residual (K) | 196, 196, 194, 204, 185 |
| part profiles over all 30 parts | only (3,2,2,1) and (3,2,1,1,1) |
| pairs swept | 30 = 5 × 6; **5** die at the all-OR precheck |
| search nodes, lowest-index order | 310,483,691 |
| search nodes, rarest-first order | 4,832 |
| recovery control (§6) | 7 peels × {membership, full-OR, SOLVABLE ×2 orders}, 1,230 nodes |
| tooth control | 7/7 fail at `max_fresh = 0`, membership *and* search |

Node counts are **representative-dependent** — they depend on which labelling of
each class the census happens to emit, so a different implementation that agrees
on everything else may well report different node totals. The level sizes, the
class counts, K, and the verdicts are the invariants.

## Reproduce

```sh
cd certificates/0011-extremal-delta
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 verify.py     # ~3 min, 3.9.6
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 -O verify.py  # same, asserts off
```

Deterministic. Both runs must end `ALL GREEN` and exit 0. Roughly half the wall
clock is the lowest-index-order set-cover search, which is kept only so that the
rarest-first order has something to be checked against.
