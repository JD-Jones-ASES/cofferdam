# cofferdam — plan

Revised 2026-07-27 (turn 9). History is the record; this file is rewritten.

## Where we are — **floor m ≥ 22, citing nothing, on a pinned ladder**

| cert | result |
| --- | --- |
| **0001** (22 + 0) | degree-cap ladder; g(1..4) = 1,3,5,8 → m ≥ 18 citing nothing |
| **0002** (22 + 1) | **(L4)** Σ deg ≥ m+5 per edge |
| **0003** (10 + 2) | **(L5)** low-incidence bound |
| **0005** (49 + 5) | **minimum-degree ladder**: m ≥ 19 citing nothing; corrected AKP Lemma 2.8 |
| **0006** (22 + 0) | **(L8) excess-concentration**: m = 20 impossible (cited ladder) |
| **0007** (18 + 1) | (L8) on the weak ladder kills every m ≤ 20 → **m ≥ 21 citing nothing** |
| **0008** (43 + 4) | **(D2)** degree-two cap kills m = 21 → **m ≥ 22 citing nothing** |
| **0009** (38 + 13) | **g(5) = N(5) = 13 citing nothing**; Q13 answered YES; the free ladder now EQUALS the cited ladder |
| **0010** (24 + 3) | **N(4) = 9 BY HAND** — the hinge is a theorem, not a search |
| **0011** (61 + 12) | **Δ = 4 for 13-edge τ ≥ 5 objects** — the last uncertified turn-4 result, closed; the (8,4) census proven complete twice over |
| **0012** (12 + 5) | **(L10) saturation floor — the δ-budget retires**: m = 21 dies on floors + convexity, margin ≥ 6 (median 24) |

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).

**The chain, one paragraph.** (A) no active degree-1 vertex · (B) every part
has ≥ 6 active vertices · (C) deleting k same-part stars leaves a residual
witnessing N(6−k), with the ladder now **pinned exactly**: N(1..5) =
2, 4, 6, 9, 13 — N(4) by a hand theorem with two agreeing searches (0010),
N(5) by the m = 12 dead-heat forcing + an 11,520-design exhaustion, thrice
implemented (0009). Then the pair count, (L7), (L8) — whose internals now
carry names: the excess budget X, and **(L9)** the water-filling floor for B
(proved + audited over 262,729 instances, zero mismatches). (D2) caps
2·D₂ ≤ m, and **(L10)** the saturation floor (a cap-saturating vertex's
13-edge complement is certificate 0011's class, so its degrees cap at 4).
**No rung consumes the δ-budget, the level system, qmin, or U** (0012):
m ≤ 19 admits nothing on the pinned ladder, m = 20 dies on the cap, m = 21
on (L7)+(L10) floors + (L9) convexity + B ≤ ⌊5X/2⌋ at margin ≥ 6.
Certificates 0006/0007 stay green as the weak-ladder record.

## Where to attack — reranked after turn 9

1. **QUEUED — NEXT SESSION, part A: certificate 0013, the finite window
   [22, 462] CITING NOTHING.** The ceiling is not astronomical and needs no
   literature: any counterexample contains an edge-minimal critical core K
   (still a counterexample, so m(K) ≥ 22); criticality hands every edge a
   private 5-cover T_e with e ∩ T_e = ∅ and e ∩ T_f ≠ ∅, and the permutation
   count (events "e wholly precedes T_e" are pairwise disjoint, each of
   probability 6!·5!/11! = 1/462) gives **m(K) ≤ C(11,6) = 462**. Hand proof
   re-derived at the desk, arithmetic verified — turn-9 notebook §13. Scope
   with care: the window quantifies over critical cores; the floor
   quantifies over all counterexamples. **Ryser r = 6 intersecting ⟺ no
   critical core in [22, 462].**
   **Part B: the narrowed literature list** (seal-clean; the seal covered
   the chain, not the field): (a) attribution for the set-pair bound
   (Bollobás 1965) and for τ-criticality bounds generally — cite, don't
   consume; (b) is the **456 = C(11,6) − 6 partite refinement** (peer-claimed,
   exterior algebra, desk-read plausible) already in the literature
   (partite/subspace skew-Bollobás variants), and audit it in-house either
   way; (c) what the REAL fractional theorem says — "τ* ≤ r/2 for
   intersecting 6-partite" is **FALSE**, killed firsthand by truncated
   PG(2,5) with τ* = ν* = 5 (notebook §13); (d) FHMW's linear-Ryser scope;
   (e) the claimed March-2026 survey (arXiv 2603.04704) stating intersecting
   r ≥ 6 still open. Done at turn 9: the hand-kill of m = 21's 567
   (cert 0012 — was item 1 here).
2. **Re-derive the stronger per-part claim at the desk**: every part of an
   8-edge τ ≥ 4 object carries a degree-1 vertex (fleet-claimed complete
   proof, turn 9). Lands the corrected AKP 2.8 consequence by hand and
   makes 0010's theorem per-part rather than full-part.
3. **The equality-regime scan — RUN (turn 9), and the answer is sobering.**
   Gap = (6 × capped max) − C(m,2), on the pinned ladders: t = 5 hits **0 at
   m = 12 and nowhere else** (+12 at 13, +29 at 14, growing); t = 6 crosses
   from −9 (m = 19) straight to +8 (m = 20), then +30, +57, +89 — never
   inside [0, 2]. The m = 12 dead heat was the unique free forcing in the
   visible grid; every future rung needs structure, not counting. (Stable
   pattern worth keeping: every t = 6 maximizer is (Δ, 4, 3, 2, 2, 2) with
   Δ saturating the m − 13 cap.) Cheap extensions to *conditioned* classes
   (fixed Δ, fixed D₂ band, full-part subclasses) remain untried.
4. **Lit-check the τ-critical ceiling** (turn-9 notebook §8): a minimum
   counterexample is τ-critical in one line, and τ-critical size bounds
   would make the whole problem a finite window [22, M]. Context, not
   chain — but it reframes the grail.
5. **The m = 23 frontier** — only behind a new lemma. Measured today: no
   counting-shaped lever in-house reaches m = 22 (cap sharpening needs
   2·D₂ ≤ m − 14; ladder pinned; 30,436 (L8) survivors on the pinned
   ladder). Do not spend rung effort here without new structure.

**Closed levers, so nobody reopens them silently:** the (D2) cap sharpening
at m = 22 (priced by full-field sensitivity, two implementations: survivors
down to D₂ = 5 on every ladder; **declined**) · Q13 (answered YES — 0009;
its 232-slice search is retired unrun) · N(5) ≥ 14 (impossible — N(5) = 13
exactly) · the N(4) = 9 tightening of (L7) (D-022, turn 8) · AKP 2.9 as an
attack surface (demoted turn 7) · **the δ-budget, the level system, qmin and U as load-bearing steps** (retired from the minimal chain by 0012; green in 0006/0007 as the weak-ladder record).

**Peer-claimed leads on file (outside review via JD, turn 9 — re-derive
before any use; notebook §13 has the full triage):** the critical-cover
inequality (CC)/(GCC) for cores (desk-checked sound, uncertified) · an
(L8)-free third m = 21 kill via exact Farkas certificates (its ladder
reconstruction independently matched our 45 profiles / 567 systems) ·
**X ≥ 2 for critical cores at m = 22** (would start the m = 22 frontier in
the nonlinear regime; unverified) · Farkas-dual clustering into human
lemmas · split-and-repair construction seeded at truncated PG(2,5)
(BRIEF §5's rigidity warning stands; solvers scout, never ship).

## Risk decomposition — updated for turn 9

| step | what stands under it now |
| --- | --- |
| **X + (L9) + A ≥ S−m** | still the m = 21 kill's engine — **the turn-9 prediction that the hand-kill would retire this row was WRONG**: cert 0012's kill consumes A ≥ S−m, (L9) and X's B-cap exactly as before; what left was the δ-budget/levels/qmin/U. (L9) proved + audited (262,729 comparisons); X's identities brute-forced over 1.86M audits (turn 8) |
| **N(4) = 9** | a hand theorem (0010) + two agreeing searches. No longer a single point of failure. The theorem's inputs: g(2) ≥ 3, g(3) ≥ 5 only |
| **N(5) = 13** | dead-heat forcing (margin one, all four caps load-bearing) + 11,520-design census, three implementations + the witness. Rung closed permanently |
| **g(4) = 8** | margin one, and turn 9 found its "two proofs" were ONE argument in two code forms (the 0001 absence search never branches — the waste-budget root prune IS the counting kill, D-028). A genuinely independent definitions-only brute force closed m ≤ 6 but hit its 200M-node ceiling per quarter at (7,4) — **UNDECIDED, priced at > 800M nodes for this engine**. The counting proof itself is three lines from g(3) = 5, machine-checked in certs 0009/0010/0011 §1, and is not in doubt; what was wrong was the *bookkeeping of independence* |
| the δ-budget | **RETIRED from the minimal chain (0012)** — replaced by (L10)+(L9) at margin ≥ 6 where its margin was one. Stays green inside 0006/0007 |
| the cap ⌊m/2⌋ | m = 20 (105 all fail it) and the D₂ ≤ 10 gate at m = 21; margin one, odd-m rounding (0008) |
| **(L10) via 0011's Δ ≤ 4** | the new m = 21 load-bearer beside (L9): weaken 0011 to Δ ≤ 5 and 65 of 567 revive (0012's sensitivity). 0011's own weight sits on its twice-built (8,4) census |

## Machinery — lessons that earned their line

- **Measure before theorising**: turn 9's cap matrix killed the r-dependent
  (D2) sharpening in an hour, and the classification of the 567 found the
  δ-budget's true load (43 configs, all cap-saturated) before any theory was
  attempted — (L10) fell out of the saturation structure (D-030).
- **Diff design sets, not headline counts** — the blind C reproduction's
  over-strong prune produced 6,912 of 11,520, a flattering subset that
  headline comparison would have blessed (D-005 in the wild, caught).
- **Inventory your own witnesses** (D-026): Q13 sat answered in the repo for
  a full turn while a search for its object was being priced.
- **A dead heat is a forcing, not a failure** (D-029): equality pins every
  profile and X = 0; the search space collapses from hopeless to 553 s.
- Precompute admissible columns when they fit; lazy generation for ρ ≥ 11
  (turn 5). Never repeat an expensive search for bookkeeping (turn 5).
  Weaken deliberately when the conclusion survives (D-009).

## Standing

- Every certificate names its external dependencies; for the floor the
  ledger is **empty**, and after 0009 the cited/free distinction is gone —
  there is one ladder and it is ours.
- No solver in the trust chain. No isomorphism census in the trust chain
  (0009's 11,520 is a count of search outputs, each individually verified;
  no class structure is consumed).
- Every "empty" ships completeness arguments and known-answer controls
  (415,800 closed form; AG(2,3) = 12; W-recovery on all seven peels).
- **A result that lands on the expected answer gets a not-too-strong
  control** — 0009 checks m = 13 survives; 0011 checks W exists with Δ = 4.
