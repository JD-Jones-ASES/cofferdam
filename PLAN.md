# cofferdam — plan

Revised 2026-07-26 (turn 5). History is the record; this file is rewritten, not
appended.

## Where we are — floor **m ≥ 20**, one case left, one question left

Seal intact (BRIEF §2): no sealed path read by this repo, the main thread, or any
of the seven subagents run in turn 5.

**Cert 0005 GREEN (30 checks, ~5 min):** the minimum-degree ladder.

- **(A)** no active vertex of a counterexample has degree 1 — drop a vertex from
  an edge and the remaining five cannot cover, so some edge meets that edge only
  there. **(B)** every part has ≥ 6 active vertices — a part is itself a cover.
- **(C)** deleting k same-part stars leaves a residual whose *surviving vertices
  of that part keep all their edges*, so it is a witness for **N(6−k)**, where
  N(t) = least edges with τ ≥ t **and a part all of whose degrees are ≥ 2**.
- **N(1..4) = 2, 4, 6, 9**, computed exactly. N(4) ≥ 9 by exhaustion (52.0M
  nodes, 268 s: at 8 edges such a part must be (2,2,2,2), and no such object
  exists); N(4) ≤ 9 by an explicit 9-edge witness built by hand from our own
  (8,4) census, not by search.
- Re-running the pair count over the profiles those permit: **m ≥ 19 citing
  nothing** (was 18) and **m ≥ 20 citing f(6)=13** (was 19). **m = 19 is dead.**
  At m = 20 only Δ = 7 survives; the old Δ=5 and Δ=6 cases die by counting alone.

Certs 0001–0003 stand and are reproduced inside 0005 as a control.

## The entire remaining gap

Δ = 7 at m = 20 saturates the k=1 cap (7 = 20 − 13), so the degree-7 vertex's
complement is a 13-edge τ=5 — f(6)-extremal — object, and by (A)+(B) the relevant
part has every degree ≥ 2. So the whole question is:

> **Q13.** Is there a 6-partite intersecting hypergraph with 13 edges, τ ≥ 5, and
> a part all of whose active vertices have degree ≥ 2?
>
> **NO ⟹ N(5) ≥ 14 ⟹ Δ ≤ m−14 ⟹ m ≥ 21.**  Nothing else is required.

Exactly three profiles are possible for that part, with these waste budgets:
`(4,3,2,2,2)` → 9 · `(3,3,3,2,2)` → 8 · `(3,2,2,2,2,2)` → 5.

## Next, in order

1. **Settle Q13.** Two routes, both live:
   - *direct*: column search with column 0 pinned, 232 disjoint slices for
     parallelism (`scratchpad/q13par.py` shape). Measured ≈35k nodes/s; profile
     (3,2,2,2,2,2) is the tightest and should be run first.
   - *peeling*: (4,3,2,2,2) peels by its 4- and 3-blocks to a **6-edge τ≥3 object
     with part 0 = (2,2,2)** — an N(3)-extremal seed; (3,3,3,2,2) peels by its
     three 3-blocks to a **4-edge τ≥2 object with part 0 = (2,2)** — an
     N(2)-extremal seed. Both seed censuses are tiny; build back up by star
     attachment. (3,2,2,2,2,2) has no tight peel and needs the direct route.
2. **If Q13 is YES**, the m=20 Δ=7 case is not yet dead: seven star edges must
   each restrict to a *rainbow minimum cover* of the 13-edge residual, and
   τ(H) ≥ 6 iff every minimum cover of the residual is escaped by one of them.
   That set-cover test is cheap per residual — the cost is producing them, which
   the Q13 search does anyway.
3. **Pin N(5) exactly** either way; it is the last unknown rung of the N-ladder
   and would also make the floor self-contained (N(5) ≥ N(4)+2 = 11 is all we
   have without citing f(6)=13).
4. **The standing audit question (BRIEF §3)**, gated on JD's seal ruling. The
   localisation has improved again: the unverified remainder is one rung, one Δ,
   one question.

## Machinery

`certificates/0005-min-degree-ladder/verify.py` carries a self-contained copy of
the column engine. Two measured lessons from turn 5:

- **Precompute the admissible partition list when it fits** (2220 at ρ=8, and the
  ρ=8 exhaustion then runs in 268 s); regenerating columns lazily at every node
  cost >7 min on the same instance without finishing. Lazy generation is for
  ρ ≥ 11, where the list cannot be built at all.
- The **per-edge degree lookahead** — edge e meets the other ρ−1 edges only inside
  its own blocks, so Σ_j (|block_j(e)| − 1) ≥ ρ−1, and the columns not yet fixed
  can contribute at most (maxb−1) each — is the prune that makes ρ=8 exhaustion
  feasible at all.

## Dead ends recorded

- **Counting alone will not kill m=20 Δ=7.** The (L4) value-pool bound played
  against the (L7) star-intersection bound kills a fraction of the 105 admissible
  six-part profile multisets, but all-(7,4,3,2,2,2) survives at exactly 30
  against a requirement of exactly 30. A dead heat is not a kill.
- Cert 0002's reading that AKP Lemma 2.1 is "subsumed by the ladder" was **wrong**
  and is superseded: it rested on allowing degree-1 vertices in a counterexample,
  which (A) forbids.

## Standing

- Every certificate names its external dependencies and states the floor it would
  still reach without them.
- No solver in the trust chain. τ ≤ 5 ships as an explicit five-vertex cover.
- A search that under-enumerates fakes a proof: every "empty" result ships with
  its completeness argument and is validated first on g(3)=5, g(4)=8 and the N(4)
  facts.
- Guesses about g- or N-values are computed, not inferred from the shape of the
  expected answer.
