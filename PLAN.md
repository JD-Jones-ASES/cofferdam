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
   removed the citation, every certificate funnels through one exhaustive search:
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
authors, is **m ≥ 16** (FHMW Lemma 2.2 + Theorem 2.3). So m ≥ 21 is five clear of
the literature. Note also that lemmas (A) and (B) are **not new** — they are FHMW
Lemma 2.1(i)(ii), published 2017; we re-derived them, which is a different thing.

**Demoted, and say so plainly: the literature.** AKP Lemma 2.9 was ranked #1 for
two turns. It now holds up nothing — 0007 reaches the floor without it. It stays
interesting as literature (and ABW Thm 2.7 proves f(6)=13 independently, in
exactly the τ ≥ 5 form the ladder consumes, so even the cited route never rested
on AKP alone). Do not spend attack time there.

## Next, in order

1. **Settle the degree-2 lever, and with it m ≥ 22.** FHMW Lemma 2.1(iii) — each
   line holds at most one degree-2 vertex, so 2·D₂ ≤ m — is a constraint this lab
   never had, and against our own enumeration it kills all 105 multisets at m = 20
   by itself and, with (L8), all of m = 21. See
   [notebook/2026-07-26-fhmw-lemma-21.md](notebook/2026-07-26-fhmw-lemma-21.md).
   **It is not a result yet.** Owing, in this order:
   - ~~the not-too-strong control~~ **DONE and it passes**: six copies of
     (17,3,3,3,2,2) at m = 30 survives (L8) explicitly. The filter is not
     vacuously strong. Note the first attempt at this control was wrong — two
     copies of `l8_kills` with different return types, `not (False, reason)` is
     `False` — and reported no survivors anywhere. m = 20 and m = 21 re-checked
     and unchanged; **m = 22 is not yet correctly computed** (156,797 of 2,079,883
     pass the cap there).
   - **(iii) re-derived here**, so the floor stays citation-free. Two lines: if
     line ℓ holds degree-2 vertices u, v with other lines ℓ_u, ℓ_v, then
     ℓ∖{u,v} ∪ {x} for any x ∈ ℓ_u ∩ ℓ_v is an (r−1)-cover.
   - a positive control: the bound must hold on objects that exist.
2. **Certify Δ = 4 for f(6)-extremal objects** — the turn-4 result, still
   uncertified and used nowhere load-bearing. The cheapest place a real error
   could still be hiding, and independent of item 1.
3. **A third implementation of the N(4) = 9 exhaustion.** Two now agree; a third
   by a different route would close the last single point of failure.
4. **The old push-past-21 levers**, now second-string behind item 1: restoring the
   value-pool ceiling dropped under D-009, or settling Q13.
3. **Q13** — is there a 13-edge τ=5 object with a part of minimum degree 2? NO
   gives N(5) ≥ 14 and the 0005 ladder alone yields m ≥ 21, with 22 in reach when
   combined with (L8). **Open.** Measured: 44 min on 3 cores did not finish 1 of
   232 disjoint slices. The untried route is peeling through the N(3)- and
   N(2)-extremal seeds (6 and 4 edges — both tiny).
4. **Pin g(5) exactly** (derived ≥ 12, published 13). No longer urgent — it was
   only ever wanted to self-contain the floor, and the floor is self-contained.
5. **Certify Δ = 4 for f(6)-extremal objects** (turn-4 result, uncertified).

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

| step | what fails without it |
| --- | --- |
| **(L7)** | everything — 100% of configurations survive at every m tested |
| **the excess budget X** | everything — same |
| **N(4) = 9** | m = 20 revives (1445 of 3664 with N(4) = 8) |
| the δ-budget | **only m = 20** — 12 of the 105 cited configurations, 117 of the 7159 citation-free. Below m = 20 the kills come from (L7) + X alone, with a margin of 16 at m = 19 |
| the concentration ceiling U | **nothing — inert.** 0 survivors with it removed entirely |

Two consequences worth stating plainly. **(L7) and X are the joint load-bearer**,
and neither peer audit named them as such — both worked the δ-budget, which is the
newest and least-checked inequality and also the one that can cost the least. And
**a δ-budget failure would drop the floor from m ≥ 21 to m ≥ 20, still citing
nothing** — it cannot touch the citation-free status, only the top rung. The
inert ceiling is D-009 working as intended: it was deliberately weakened, and it
turns out to be doing no work at all, which is the best possible outcome for a
step you kept only for safety.

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
