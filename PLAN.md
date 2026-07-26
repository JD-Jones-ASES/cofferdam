# cofferdam — plan

Revised 2026-07-26 (turn 6). History is the record; this file is rewritten.

## Where we are — **floor m ≥ 21**

Seal intact (BRIEF §2): no sealed path read by this repo, the main thread, or any
of the eight subagents run this session.

| cert | result |
| --- | --- |
| **0001** (22) | degree-cap ladder; g(1..4) = 1,3,5,8 twice over → m ≥ 18 citing nothing |
| **0002** (23) | **(L4)** Σ deg ≥ m+5 per edge. Its "AKP 2.1 is subsumed" reading is **superseded** (D-006) |
| **0003** (12) | **(L5)** low-incidence bound (0005 now kills its case by counting alone) |
| **0005** (40) | **minimum-degree ladder**: m ≥ 19 citing nothing · **m ≥ 20** citing f(6)=13; corrected AKP 2.8 proven |
| **0006** (19) | **(L8) excess-concentration**: **m = 20 impossible → m ≥ 21** citing f(6)=13 |

**The chain, in one paragraph.** (A) no active vertex has degree 1; (B) every part
has ≥ 6 active vertices; so (C) deleting k same-part stars leaves a residual
witnessing **N(6−k)** — least edges with τ ≥ t *and a part of minimum degree 2* —
not merely g(6−k). N(1..4) = 2,4,6,9, the last by exhaustion (52.0M nodes) plus a
built witness. That kills m ≤ 19 and leaves Δ=7 at m=20. Then (L7): two
maximum-degree vertices in different parts have |E(u)∩E(w)| ≥ M+M′−(m−g(4)); and
(L8): the pair count's **surplus is a budget**, spent both by those overlaps and
by the high-k edges they force, and at m = 20 the two budgets cannot both be paid.

## Next, in order

1. **DONE — f(6) ≥ 13 checked in the source** (AKP arXiv:1409.4938, read firsthand;
   published literature is not sealed). It is *proved*, not inferred from the 13-edge
   construction: Theorem 1.1, split in §2 as Lemma 2.9 ("f(6) ≠ 12", a Δ case
   analysis) plus MSY's f(6) > 11, and independently obtained by ABW. **The hard case
   of Lemma 2.9 is Δ = 4, which the paper settles using Lemma 2.8 — the lemma we
   found the erratum in and whose corrected form cert 0005 proves outright.** So the
   exposure is one lemma, not a constant: f(6) ≥ 12 is independently ours (g(5) ≥ 12)
   and Lemma 2.8 is independently ours; only Lemma 2.9's case analysis is cited and
   unreproduced. Reproducing it is now a well-scoped target (a 12-edge τ=5 exhaustion
   is the same order of work as Q13).
2. **Push the floor above 21.** Two levers, both live:
   - *(L8) upward*: it leaves 6198 of 43875 configurations alive at m = 21. Adding
     the value-pool ceiling back (deliberately dropped for safety at m=20) and the
     (L4) pointwise bound would cut that set; the question is by how much.
   - *Q13*: is there a 13-edge τ=5 object with a part of minimum degree 2? NO gives
     N(5) ≥ 14, hence Δ ≤ m−14, and the 0005 ladder alone then yields m ≥ 21 with
     the floor moving to 22 when combined with (L8). **Open.** Measured: 44 min on
     3 cores did not finish 1 of 232 disjoint slices. The untried route is peeling
     through the N(3)- and N(2)-extremal seeds (6 and 4 edges — both tiny).
3. **Self-contain the floor.** Pin g(5) exactly (derived ≥ 12, published 13). A
   ρ=12 exhaustion is the same order of work as Q13.
4. **Certify Δ = 4 for f(6)-extremal objects** (turn-4 result, still uncertified);
   it tightens Q13's waste budgets from 9/8/5 to 4/3/0.
5. **The standing audit question (BRIEF §3).** Gated on the owner's seal ruling.

## Machinery

`certificates/000{5,6}/verify.py` each carry a self-contained copy of what they
need. Measured lessons:

- **Precompute the admissible partition list when it fits** (2220 at ρ=8 → the
  exhaustion runs in 268 s); regenerating columns lazily cost >7 min unfinished on
  the same instance. Lazy generation is for ρ ≥ 11, where the list cannot be built.
- The **per-edge degree lookahead** is what makes ρ=8 exhaustion feasible at all.
- **Weaken a bound deliberately when the conclusion survives it.** Cert 0006's
  ceiling on A dropped the value-pool DP for the crudest concentration bound; the
  kill survived, and a whole layer left the trust chain.

## Dead ends recorded, with the assumptions under which they died

- **The (L4)/(L7) pool squeeze alone** ends at 30 against exactly 30 at m=20 — a
  dead heat, and *not* a kill. It became one only after the surplus was read as a
  budget and the δ-cost of high-k edges was added. **Assumption under which it was
  dead: that the pair count is only a lower bound.** (D-006 in action.)
- Cert 0002's reading that AKP Lemma 2.1 is "subsumed by the ladder" was wrong;
  it assumed a counterexample may hold degree-1 vertices.

## Where to attack this (for the other two labs)

Ranked by how much rests on it and how little has been checked twice:

1. **AKP Lemma 2.9** (f(6) ≠ 12) — the single cited step, not reproduced here. If it
   fails, the floor drops to 19. A 12-edge τ=5 exhaustion settles it independently.
2. **N(4) = 9's lower bound** — one exhaustive search, 52.0M nodes, ρ=8 pinned to
   (2,2,2,2). Re-derived once on different machinery; a third implementation is worth
   having, since an under-enumerating search fakes a proof.
3. **(L8)'s δ-budget step** — D ≥ q₃ + 2q₄ + 3q₅ from t_ef ≤ min(k_e,k_f). The
   identities are brute-forced on 420 objects and the m=21 control shows the lemma is
   not vacuous, but the inequality chain is the newest thing here.
4. **Δ = 4 for f(6)-extremal objects** — a turn-4 peel-chain result, **uncertified**,
   and used nowhere load-bearing. Cheapest place to find a real error.
5. **The 105-multiset enumeration** — if a single admissible part profile at m=20 is
   missing, the m=20 kill has a hole. Two independent enumerators agreed; a third
   would close it.

## Standing

- Every certificate names its external dependencies and states the floor it would
  still reach without them. For m ≥ 21 the ledger is: three lemmas of ours, one
  exhaustive search of ours, two counting lemmas of ours, one published constant.
- No solver in the trust chain. No isomorphism-class census in the trust chain.
- A search that under-enumerates fakes a proof: every "empty" result ships with a
  completeness argument and is validated on known-answer targets first.
- **A result that lands on the expected answer gets a not-too-strong control.**
  (L8) was run at m = 21 precisely to check it does not prove Ryser at r = 6.
