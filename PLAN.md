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

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).

**The chain, one paragraph.** (A) no active degree-1 vertex · (B) every part
has ≥ 6 active vertices · (C) deleting k same-part stars leaves a residual
witnessing N(6−k), with the ladder now **pinned exactly**: N(1..5) =
2, 4, 6, 9, 13 — N(4) by a hand theorem with two agreeing searches (0010),
N(5) by the m = 12 dead-heat forcing + an 11,520-design exhaustion, thrice
implemented (0009). Then the pair count, (L7), (L8) — whose internals now
carry names: the excess budget X, and **(L9)** the water-filling floor for B
(proved + audited over 262,729 instances, zero mismatches). (D2) caps
2·D₂ ≤ m. Under the pinned ladder every m ≤ 20 dies before (L8) is
consulted; **(L8) is load-bearing at exactly one rung, m = 21, on exactly
567 configurations.**

## Where to attack — reranked after turn 9

1. **Hand-kill m = 21's 567 configurations.** (L8) is consulted at one rung.
   The triple-method that hand-proved N(4) = 9 (0010) and the forcing
   geometry that collapsed m = 12 (0009) are both built for exactly this
   shape of problem. If the 567 fall to structure, the δ-budget machinery —
   the narrowest-margin code in the repo, the target of both peer audits —
   **leaves the trust chain entirely**. Highest value per unit work.
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
attack surface (demoted turn 7).

## Risk decomposition — updated for turn 9

| step | what stands under it now |
| --- | --- |
| **X + (L9) + A ≥ S−m** | the m = 21 kill's engine. (L9) proved + audited (262,729 comparisons, incl. every (floors,A) pair the certs consult); X's identities brute-forced over 1.86M audits (turn 8). Attack #1 above would retire the whole row |
| **N(4) = 9** | a hand theorem (0010) + two agreeing searches. No longer a single point of failure. The theorem's inputs: g(2) ≥ 3, g(3) ≥ 5 only |
| **N(5) = 13** | dead-heat forcing (margin one, all four caps load-bearing) + 11,520-design census, three implementations + the witness. Rung closed permanently |
| **g(4) = 8** | margin one, and turn 9 found its "two proofs" were ONE argument in two code forms (the 0001 absence search never branches — the waste-budget root prune IS the counting kill, D-028). A genuinely independent definitions-only brute force closed m ≤ 6 but hit its 200M-node ceiling per quarter at (7,4) — **UNDECIDED, priced at > 800M nodes for this engine**. The counting proof itself is three lines from g(3) = 5, machine-checked in certs 0009/0010/0011 §1, and is not in doubt; what was wrong was the *bookkeeping of independence* |
| the δ-budget | m = 21 only, margin one (0008's table). Attack #1 would retire it |
| the cap ⌊m/2⌋ | m = 21 only, margin one, odd-m rounding. Same |

## Machinery — lessons that earned their line

- **Measure before theorising** (turn 9's cap matrix killed PLAN item 1b in
  an hour; the alternative was a week of matching theory for nothing).
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
