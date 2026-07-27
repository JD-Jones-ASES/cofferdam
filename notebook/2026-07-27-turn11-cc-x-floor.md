# 2026-07-27 · turn 11 — (CC) certified, and the window floor goes nonlinear

## 0. Scope

PLAN attack #1's first rung: certify the critical-cover inequality (CC),
then price the peer-claimed X ∈ {0,1} exclusion at m = 22. Both landed —
the second only after a repair the sketch did not contain.

## 1. (CC), re-derived at the desk

For a core edge e with private 5-cover T_e (0013), part-degrees d_i,
b_i = |T_e ∩ V_i|: every sibling edge through v_i meets T_e outside
part i (its part-i vertex IS v_i ∉ T_e), so the d_i − 1 siblings funnel
through 5 − b_i cover vertices; same-cell pairs are double-meets. The
incidence sum Σᵢ Σᵤ C(n_iu, 2) ≥ Σᵢ Φ(dᵢ−1, 5−bᵢ) (balanced-split
convexity) and counts each pair {f, f′} exactly a·b times (a shared
e-vertices, b shared cover vertices; a shared cover vertex is
automatically outside every shared e-vertex's part). With a + b ≤ s =
|f ∩ f′| ≤ 5: **a·b ≤ (3/2)(s−1)**, tight exactly at (2,3), s = 5 —
the corner the turn-9 triage recorded, now with its proof. Summing over
pairs inside K − e (their excess is exactly X − x_e):

**2·Σᵢ Φ(dᵢ−1, 5−bᵢ) ≤ 3(X − x_e)**, and globally (Σ_e x_e = 2X):
2·Σ_e Σᵢ Φ ≤ 3(m−2)X.

Well-definedness note found by the refuter: b_i = 5 forces d_i = 1 from
covering alone — **(CC) itself needs no lemma (A)**; its ledger is 0013
only. The derivation is uniform in τ: the t = 5 analog was enacted on
the real 14-edge rehearsal core with **margin exactly zero on all 14
edges** (X = 0 there — projective-plane lines pairwise meet once), both
accounting identities exact.

## 2. Measure first: the sketch does not close

The outside review claimed "X ∈ {0,1} excluded via (CC) + the D₂ cap."
Measured before theorising: the global form + (D2) over the m = 22
field leaves **52 survivors** (now check 18, in-transcript). The
repair — corollaries the sketch did not contain:

- per-edge, via Φ(·, 5−b) ≥ Φ(·, 5): **X = 0 ⟹ Δ ≤ 6; X ≤ 1 ⟹ Δ ≤ 7**
  (a degree-8 vertex makes LHS 4 > 3);
- at X ≤ 1 **no edge carries two degree-7 vertices** (4 > 3 again), so
  7-stars are pairwise edge-disjoint: **at most three degree-7 vertices
  fit in 22 edges** (four need 28).

## 3. Certificate 0015 — X ≥ 2 for every critical core at m = 22

Over the pinned-ladder field: 506,204 configurations with 0 ≤ X ≤ 1;
verdicts 504,478 per-edge cap / 1,150 star-disjointness / 576 (D2) /
**zero alive**. The margin, computed in-transcript (check 19): the
maximum degree-pair total under the X = 1 rules is **exactly 231, one
unit short** of the 232 that X = 1 requires (225 at X = 0, margin six).
Not too strong: at X = 2 the same judge leaves 9,224 of 210,713 alive —
the floor lands exactly at 2. Sensitivity: drop stars → exactly 6
revive (asserted: all X = 1 with four 7s); drop (D2) → exactly its 576
victims revive. 19 checks + 3 notes, ~15 s, green under bare 3.9.6 and
`-O`.

**What it says**: a minimum counterexample core is in the nonlinear
regime the moment it exists — at least two extra edge-meets beyond
one-per-pair. The m = 23 frontier now has a structural lever: any
argument that prices X ≥ 2 structure (two λ = 2 pairs, or one λ = 3
pair) can spend it.

## 4. Adversarial record

Two independent attackers (Agent-tool lenses; ultracode off this turn):

- **Proof refuter — SOUND, no gap**: hand-rederivation of every step;
  16,578 randomized instance checks (5,996 at the tight corner); full
  independent re-enumeration matching all five counts; the knapsack
  margin computation (231/225) — promoted into the certificate.
  Catches: the corner's binding hypothesis is a + b ≤ s (docstring
  phrasing); b_i = 5 vacuous from covering; "X ≤ 1" = "0 ≤ X ≤ 1".
- **Code auditor — SOUND-WITH-NITS**: independent reimplementation
  matched every number including the then-unasserted 52; §4 rebuild
  byte-identical to 0013's construction; sabotage tests red as
  expected; determinism across 3.9.6/3.14 and hash seeds. Catches:
  the real-core a·b identity is vacuous there (0 = 0 — label now says
  so) and gained a nonvacuous transversal-synthetic check (292 nonzero
  terms, pinned); the six-revival shape is now asserted.

## 5. Errors of mine, recorded

Two guessed constants in drafts (the D2-drop revival count 528→576;
the "thousands" nonvacuity threshold →292) — both caught by the run
itself, both replaced by measurement. The D-017 shape, twice more.

## 6. What this opens

The X = 2 layer's 9,224 survivors are the new frontier field — small
enough to stratify. Next levers, in rough order: (a) the per-edge (CC)
with real b-profiles (the cover-free min over b was not needed at
X ≤ 1; at X = 2 it may bite); (b) the second-moment structure of X = 2
(exactly two λ = 2 pairs or one λ = 3 pair — both very rigid); (c) the
peer's (GCC) global form with cover structure, still uncertified. The
ceiling lanes (intersecting-ness axiom, abstract r = 4, Theorem A) are
untouched this turn and remain queued.
