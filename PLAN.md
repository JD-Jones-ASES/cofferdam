# cofferdam — plan

Revised 2026-07-26 (turn 7). History is the record; this file is rewritten.

## Where we are — **floor m ≥ 21, citing nothing**

| cert | result |
| --- | --- |
| **0001** (22 + 0 notes) | degree-cap ladder; g(1..4) = 1,3,5,8 twice over → m ≥ 18 citing nothing |
| **0002** (22 + 1 note) | **(L4)** Σ deg ≥ m+5 per edge. Its "AKP 2.1 is subsumed" reading is **superseded** (D-006) |
| **0003** (10 + 2 notes) | **(L5)** low-incidence bound |
| **0005** (49 + 5 notes) | **minimum-degree ladder**: m ≥ 19 citing nothing · m ≥ 20 citing f(6)=13; **the corrected AKP Lemma 2.8, now BOTH halves** |
| **0006** (22 + 0 notes) | **(L8) excess-concentration**: m = 20 impossible → m ≥ 21 citing f(6)=13 |
| **0007** (18 + 1 note) | **the citation is unnecessary**: (L8) on the weaker rung N(5) ≥ 11 kills every m ≤ 20 → **m ≥ 21 citing NOTHING** |

All six green under `python3` **and** `python3 -O` (D-015).

**The chain, in one paragraph.** (A) no active vertex has degree 1; (B) every part
has ≥ 6 active vertices; so (C) deleting k same-part stars leaves a residual
witnessing **N(6−k)** — least edges with τ ≥ t *and a part of minimum degree 2*.
N(1..4) = 2,4,6,9, the last by exhaustion (52.0M nodes). Peeling gives N(5) ≥ 11
citing nothing. Then (L7): two maximum-degree vertices in different parts satisfy
|E(u)∩E(w)| ≥ M+M′−(m−g(4)); and (L8): the pair count's **surplus is a budget**,
spent both by those overlaps and by the high-k edges they force. Run over the
citation-free ladder, (L8) kills every m from 12 to 20 and leaves m = 21 alive.

## Where to attack this — reranked, and it is now one target

1. **N(4) = 9's lower bound — still #1, but no longer unchecked.** Since 0007
   removed the citation, the floor of 21 funnels through one exhaustive search
   (certificates 0001–0003 predate the N-ladder and do not use it):
   ρ=8 pinned to (2,2,2,2), 52,023,309 nodes, 2220 admissible columns, result
   *empty*. 0007's sensitivity check prices it: set N(4) = 8 and m = 20 comes back
   to life among 180,480 configurations.

   **A second, structurally different search now agrees** (turn 7, completeness
   pass): 1505 candidate columns, 5,713,053 nodes, same verdict — and it is a
   *better* control than ours, because it exhibits what it rejects: **8648 full
   pair-covers built, every one at τ = 3**. A search that returns empty tells you
   nothing about whether it looked; one that hands you 8648 near-misses does. The
   least-uncovered-pair reduction the two searches share was closed by brute force
   separately.

   Beware a trap. It is tempting to treat our corrected Lemma 2.8 as a further leg
   — it is not. **Lemma 2.8's derivation consumes that same search**, so it is
   downstream of N(4) ≥ 9 and can never corroborate it. AKP Lemma 2.1 *would* be a
   genuine independent leg, but we cite it and mark it not-used.

   **What a third implementation should match is the verdict and a structurally
   different route — not the node count.** Matching 52,023,309 nodes would only
   prove someone reimplemented our prunes.

2. **(L8)'s δ-budget step** — hunted for a false kill in the turn-7 pass and none
   found: no off-by-one in any loop bound (ranges widened by 12, zero admissible
   tuples outside them), the greedy B_min equals the exact DP minimum, U is a
   genuine ceiling, and the δ-budget never exceeds the true requirement. **But note
   the margin: exactly one.** The tightest point is the (7,…,7) dead heat at A = 30
   under level structure {4,4,3}, D = 8 against need = 9, and the need is exact.
   Three inputs flip m = 20 if moved a single unit.

   And note *which half* is safe. Everything inside `l8_kills` is a **relaxation**
   — it permits what reality forbids, so a total kill under it is conservative.
   `profiles()` is a **restriction** and runs the other way. **A false kill could
   only live there**, which is another way of saying it could only live in N(4) = 9.

3. **The profile and multiset enumeration** — a single missing admissible part
   profile would hole the kill. Three implementations now agree at 32/105 (cited)
   and 34/7159 (citation-free); a fourth would still be worth having, because all
   three descend from the same written description of lemmas (A)(B)(C).

4. **Δ = 4 for f(6)-extremal objects** — a turn-4 peel-chain result, still
   **uncertified**, used nowhere load-bearing. Cheapest place to find a real error.

**Novelty, checked 2026-07-26.** Six independent literature sweeps plus own
reading: **no published lower bound on the size of an r = 6 Ryser counterexample
exists.** The strongest published *statement* bearing on it is m ≥ 13 (f(6) = 13,
which does cover τ ≥ 6, since MSY defined f on τ ≥ r−1 precisely so it survives
Ryser failing). The strongest published *consequence*, never stated by its
authors, is **m ≥ 19** — FHMW's Theorem 2.3 as stated gives Δ ≥ 6 and hence
m ≥ 16, but the quadratic *inside* its proof, optimised over Δ, reaches 19 (the
bottleneck is Δ = 9). So m ≥ 21 is **two** clear of what the literature already
implies, not five. Worth knowing rather than glossing: our m ≥ 19 rung is
independently reachable from FHMW by a completely different route, which
corroborates that rung rather than scooping it. The new ground is 20 and 21. Note also that lemmas (A) and (B) are **not new** — they are FHMW
Lemma 2.1(i)(ii), published 2017; we re-derived them, which is a different thing.

**Demoted, and say so plainly: the literature.** AKP Lemma 2.9 was ranked #1 for
two turns. It now holds up nothing — 0007 reaches the floor without it. It stays
interesting as literature (and ABW Thm 2.7 proves f(6)=13 independently, in
exactly the τ ≥ 5 form the ladder consumes, so even the cited route never rested
on AKP alone). Do not spend attack time there.

## Next, in order

**Item 1 is DONE — certificate 0008, `m ≥ 22` citing nothing.** (D2) re-derived
here via a strictly more general constructive lemma, the sweep run on the
**citation-free** ladder (the notebook's table had been computed on the cited
one, which would have silently re-imported f(6)=13), and reproduced by a blind
second implementation. The lever buys **one rung and stops**: m = 22 survives,
56,592 of 307,420 cap-passers citation-free. The positive control this file
asked for was **impossible as written** and has been replaced — see D-024.

1. **Certify Δ = 4 for f(6)-extremal objects** — the turn-4 result, still
   uncertified and used nowhere load-bearing. The cheapest place a real error
   could still be hiding.
2. **Attack X, the sole total load-bearer**, and **g(4) = 8** with it. The
   corrected risk table above says X is the only step whose removal leaves 100%
   surviving, and g(4) = 8 carries a margin of exactly one while appearing on no
   attack list. Neither peer audit touched either.
3. **A third implementation of the N(4) = 9 exhaustion.** Two agree; a third by a
   different route would close the last single point of failure. It is now the
   hinge for m ≤ 20 under (D2) as well, since (L8) is not consulted there.
4. **Fix `lib/ryser.py`'s duplicate-edge bug** (D-025) and recount anything that
   used the non-extremal censuses. `enumerate(6,3)` is 53,871, not 53,906. The
   extremal counts 12 and 5 are unaffected, so the ladder does not move.
5. **The old push-past-22 levers.** Q13 — is there a 13-edge τ=5 object with a
   part of minimum degree 2? Measured: 44 min on 3 cores did not finish 1 of 232
   disjoint slices; the untried route peels through the N(3)- and N(2)-extremal
   seeds (6 and 4 edges, both tiny). Note its payoff has fallen further: it
   reaches m ≥ 21, which is now two rungs below the floor.
6. **Pin g(5) exactly** (derived ≥ 12, published 13). Not urgent.

**Dead end, closed this turn (D-022): the (L7) tightening to N(4) = 9.** The only
ρ = |R| where the +1 changes a floor is ρ = 8, and there R is g(4)-extremal — and
certificate 0005's corrected AKP Lemma 2.8 says every part of an 8-edge τ ≥ 4
object is (3,2,2,1) or (3,2,1,1,1), each carrying a degree-1 vertex. **So at the
only ρ that matters the residual provably has no part of minimum degree 2.** The
property is strictly stronger than the conclusion it would buy. Machine-checked
too: 15 of 15 two-star residuals of W8 and 15 of 15 of W9 have no such part. And
it would not have been enough anyway — running (L7) with g(4) = 9 still leaves
950 survivors at m = 21 citation-free.

## Machinery

`certificates/000{5,6,7}/verify.py` each carry a self-contained copy of what they
need. Measured lessons:

- **Precompute the admissible partition list when it fits** (2220 at ρ=8 → the
  exhaustion runs in ~5 min); regenerating columns lazily cost >7 min unfinished
  on the same instance. Lazy generation is for ρ ≥ 11.
- The **per-edge degree lookahead** is what makes ρ=8 exhaustion feasible at all.
- **Weaken a bound deliberately when the conclusion survives it** (D-009). Cert
  0006's ceiling dropped the value-pool DP for the crudest concentration bound;
  the kill survived, and a whole layer left the trust chain. 0007 is the same move
  applied to an *input*: weaken N(5) from 13 to 11 and the kill still lands.
- **Never repeat an expensive search for bookkeeping.** 0005 ran its 52M-node
  exhaustion twice for no extra assurance; reusing the verdict saved ~5 min.

## Dead ends recorded, with the assumptions under which they died

- **The (L4)/(L7) pool squeeze alone** ends at 30 against exactly 30 at m=20 — a
  dead heat, and *not* a kill. It became one only after the surplus was read as a
  budget and the δ-cost of high-k edges was added. **Assumption under which it was
  dead: that the pair count is only a lower bound.** (D-006 in action.)
- Cert 0002's reading that AKP Lemma 2.1 is "subsumed by the ladder" was wrong; it
  assumed a counterexample may hold degree-1 vertices.
- **"The citation is load-bearing"** — believed for two turns, recorded in four
  files, and false. It died when the sweep was rerun on the weaker rung. The
  assumption under which it was true: that the *pair count* was the only thing
  consuming N(5). (L8) consumes it far more cheaply.

## Risk decomposition — what each step actually carries

Measured by ablation in the turn-7 completeness pass, and it relocates the risk:

**Corrected 2026-07-26 turn 8. The (L7) row published here was false**, and it
was the row this table existed to get right. Measured firsthand with certificate
0007's own `l8_kills`, one line changed:

| step | what fails without it |
| --- | --- |
| **the excess budget X** | everything — **exactly 100%** survive at every m with a non-empty configuration set. The sole total load-bearer |
| **(L7)** | the floor breaks (21 → 20 cited, 21 → 19 free) but **most configurations still die**: 3 of 105 survive at m=20 cited (2.9%), 1,616 of 7,159 at m=20 free (22.6%), 1 of 33 at m=19 free |
| **N(4) = 9** | m = 20 revives (1445 of 3664 with N(4) = 8) — **and m = 19 revives too**, so the floor drops 21 → **19**, not 21 → 20 |
| **g(4) = 8** | (L7) goes with it. Weaken to 7 and 649 of 7,159 survive at m = 20 free — the same margin of exactly one, on a constant nobody lists |
| the δ-budget | **only m = 20** — 12 of the 105 cited, 117 of the 7159 citation-free |
| the ceiling U | **nothing — inert**, at m = 21 as well as below |
| B ≤ ⌊5X/2⌋ inside X | **nothing — inert.** A second dead step: it is implied by the level budget, which already does the work |

**And the real load-bearer has no name.** 100% survival is reproducible only if
you *also* zero **B_min(A)** — the convexity lower bound on B = Σ C(c_ij,2) given
Σ c_ij = A — which is no part of (L7). With floors *and* B_min zeroed: 105/105
and 7159/7159 survive. So the step carrying the other 77.4% of the m = 20
citation-free kills is **the convexity bound on B_min, together with A ≥ S − m
(from (C4) and δ ≥ 0) and B_cap (from X)**. That step appears in no risk table,
no ledger line and no certificate label. Five implementations agree, one keeping
0007's loop structure verbatim.

Three consequences. **The convexity bound and X are what to defend** — not the
pair (L7)+X. **g(4) = 8 belongs on the attack list above and is not on it** — it
carries the same single-unit margin D-017 prices for the δ-budget, and unlike the
δ-budget (whose failure only drops the floor to 20) a failure of g(4) takes (L7)
with it. And **a table published to direct attack, that misstates one step's load
by a factor of 35 and omits the step doing the work, sends the attack to the
wrong place** — D-019 failing on its own terms (D-023).

**What did survive the attack, and it is most of the chain.** (L2), X's
definition, (C2), (C3), B_cap = ⌊5X/2⌋, (C5) in its corrected form, δ(k), `need`
and `qmin` were each brute-forced over **1,859,176 audits on explicit objects,
zero failures** — each also run under two deliberately wrong choices of u_j, so
the identities are tested as identities. The intersecting hypothesis was *priced*
rather than assumed: drop it and Σ(t_ef−1)⁺ ≤ X fails 5,167 times in 39,721
non-intersecting families, with an explicit witness. And the relaxation property
itself — that no real object's true point falls outside any guard — was checked
directly: **1,924 instances from real objects with τ computed, all 16 guards
inside `l8_kills` pass at the object's true (A, B, n₂..n₅, D)**.

## Standing

- Every certificate names its external dependencies and states the floor it would
  still reach without them. For m ≥ 21 that ledger is now **empty**.
- No solver in the trust chain. No isomorphism-class census in the trust chain.
- A search that under-enumerates fakes a proof: every "empty" result ships with a
  completeness argument and is validated on known-answer targets first. The b=2
  search in 0005 ships with a positive control at excess 1 for exactly this reason.
- **A result that lands on the expected answer gets a not-too-strong control.**
  (L8) is run at m = 21 in both 0006 and 0007 precisely to check it does not prove
  Ryser at r = 6.
- **A displayed identity is an untested identity** (D-013), **a loop's range is
  part of its claim** (D-016), and **a `check` whose condition is a literal `True`
  is a note, not a check** (D-015).
