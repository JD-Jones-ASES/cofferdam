# cofferdam — plan

Revised 2026-07-27 (turn 11). History is the record; this file is rewritten.

## Where we are — **THE FINITE WINDOW: every critical core has m ∈ [22, 456]**

| cert | result |
| --- | --- |
| **0001** (22 + 0) | degree-cap ladder; g(1..4) = 1,3,5,8 → m ≥ 18 citing nothing |
| **0002** (22 + 1) | **(L4)** Σ deg ≥ m+5 per edge |
| **0003** (10 + 2) | **(L5)** low-incidence bound |
| **0005** (49 + 5) | **minimum-degree ladder**: m ≥ 19 citing nothing; (A)(B)(C); corrected AKP 2.8 |
| **0006** (22 + 0) | **(L8) excess-concentration**: m = 20 impossible (cited ladder) |
| **0007** (18 + 1) | (L8) on the weak ladder kills every m ≤ 20 → **m ≥ 21 citing nothing** |
| **0008** (43 + 4) | **(D2)** degree-two cap kills m = 21 → **m ≥ 22 citing nothing** |
| **0009** (38 + 13) | **g(5) = N(5) = 13 citing nothing** (≡ published f(6) = 13); the free ladder EQUALS the cited ladder |
| **0010** (24 + 3) | **N(4) = 9 BY HAND** — the hinge is a theorem |
| **0011** (61 + 12) | **Δ = 4 for 13-edge τ ≥ 5 objects**; the (8,4) census proven complete twice |
| **0012** (12 + 5) | **(L10) saturation floor — the δ-budget retires**; m = 21 dies at margin ≥ 6 |
| **0013** (32 + 8) | **THE WINDOW [22, 462]**: every critical core has m ≤ C(11,6) = 462, **ceiling ledger EMPTY**; Ryser r=6 intersecting ⟺ no critical core in the window |
| **0014** (13 + 4) | **(L11) part-confinement annihilator → THE WINDOW TIGHTENS TO [22, 456]**; the peer-claimed 456 is an in-house theorem (consumes (A) + 0013) |
| **0015** (19 + 3) | **(CC) the critical-cover inequality** (per-edge + global, ledger: 0013 only) **→ X ≥ 2 for every critical core at m = 22** — the floor rung is in the nonlinear regime; kill margin exactly one unit, computed in-transcript |

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).
Both 0013 and 0014 were adversarially fleet-verified before certification
(six and five lenses; zero mathematical errors either time; every catch
fixed pre-green — D-031/D-032 record the policy outcomes).

**The problem is now finite.** A counterexample exists iff an
edge-critical one exists with m ∈ [22, 456] and ≤ 6·456 active vertices.
The floor certificates quantify over ALL counterexamples; the ceiling
quantifies over critical cores — which suffices, because every
counterexample contains one. 435 values of m remain.

**The chain, one paragraph.** (A) no degree-1 active vertex · (B) every
part ≥ 6 active · (C) same-part star deletion → the pinned ladder
N(1..5) = 2, 4, 6, 9, 13. Then the pair count, (L7)+(L10) floors, (L9)
convexity, B ≤ ⌊5X/2⌋, (D2) → **m ≥ 22** (0012's ledger is the
transitive authority: 0005/0006/0008–0012; 0007 the weak-ladder record).
Criticality → private disjoint covers → Katona-style disjoint events →
**m ≤ 462 citing nothing** (0013). Part-confinement in Λ⁶(R¹¹) + (A) →
**m ≤ 456** (0014).

## Where to attack — reranked after turn 10

1. **The m = 22 frontier — the X = 2 stratum.** DONE at turn 11: (CC)
   certified (0015; ledger 0013 only) and **X ≥ 2 proven at m = 22**
   (the peer sketch did NOT close — 52 survivors measured; repaired
   with the per-edge corollaries + star-disjointness). Next rungs on
   this lane: (a) the **9,224 X = 2 survivors** are the frontier field
   — stratify them (X = 2 means exactly two λ = 2 pairs or one λ = 3
   pair: very rigid); (b) per-edge (CC) with real b-profiles (the
   cover-free min over b was not needed at X ≤ 1; at X = 2 it may
   bite); (c) the peer's (GCC) global-with-cover-structure form, still
   uncertified · Farkas-dual clustering still on file.
2. **Squeeze the ceiling — combinatorially, not dimensionally.** The
   audit's derivation lane measured the six functionals as the
   COMPLETE annihilator (the transversal-wedge span EQUALS the 456-dim
   subspace; no seventh exists generically), so more linear algebra on
   the same embedding buys nothing. The live routes below 456:
   (a) **consume intersecting-ness of the e's** — the one core axiom
   the abstract system never uses (fleet-claimed: it alone forces
   m ≤ 2^(r−1) on binary supports); (b) the **C(2r−2, r−1) abstract
   conjecture** (truth at r = 2, 3; would give 252 at r = 6; r = 4
   open in [17, 35] — settle r = 4 first, D-033 style); (c) desk
   re-derivation of the fleet-claimed **Theorem A** (m ≤ C(2r−1,r)−1
   free of hypotheses) and its tiling method, which may compose with
   (*). Also: certify the general form m ≤ C(2r−1, r) − r for r ≥ 3
   (cheap; the r = 3 analog is already fleet-verified end-to-end).
3. **Mine the field's complementary finite framings** (turn-10 sweep):
   extract DeBiasio–Kamel–McCourt–Sheats Table 2 (the 173 surviving
   r = 6 signatures) and cross it with the window; read Pokrovskiy
   arXiv:2507.05842 (Ryser ⟺ bounded-diameter); fetch Barát's 18×18
   PG(2,5) incidence matrix (§7) against our truncated-plane machinery.
4. **Re-derive the stronger per-part claim at the desk** (unchanged from
   turn 9): every part of an 8-edge τ ≥ 4 object carries a degree-1
   vertex (fleet-claimed complete). Lands corrected AKP 2.8 by hand.
5. **Conditioned-class equality scans** (unchanged): fixed Δ, D₂ bands,
   full-part subclasses. The m = 12 dead heat remains the only free
   forcing in the visible grid.
6. **The abstract partite set-pair maximum — answered at r = 3, open
   at r = 4.** Turn-10 audit: r = 2 → 2, r = 3 → 6 (exhaustive; the
   cube-minus-antipodal witness desk-verified), r = 4 ∈ [17, 35]
   (fleet-claimed 17-witness kills the exponential pattern; the
   C(2r−2, r−1) pattern predicts 20). Settling r = 4 exactly is the
   cheapest decisive measurement on the ceiling's true shape — folds
   into attack #2(b).

**Closed levers (do not reopen silently):** everything from turn 9's
list, plus: **the 456 audit (RESOLVED — cert 0014)** · the "τ* ≤ r/2"
attribution question (RESOLVED: it is Lovász's τ ≤ (R/2)τ*, Mat. Lapok
1975; Füredi 1981 gives τ* ≤ (r−1)ν for r-partite, sharp at truncated
planes) · the 2603.04704 "survey" characterization (it is a research
paper; the survey is DeBiasio et al. 2021).

## Novelty ledger — re-measured 2026-07-27 (turn 10)

- **Floor**: best published-preprint comparator is now **m ≥ 14**
  (Sivashankar arXiv:2606.24878, June 2026: g(r) ≥ 3r−4, one-line
  specialization; verified firsthand). Ours: **m ≥ 22, eight clear** —
  but the neighborhood is HOT (first Erdős–Lovász improvement in ~50
  years; two papers in 15 months). Publication timing is JD's call —
  flagged in `awaiting_jd`.
- **Ceiling**: the generic formula C(r+t−1, r) is classical
  (Jaeger–Payan 1971; Tuza's school; Li arXiv:2512.24850 Remark 3.3).
  Its Ryser instantiation appears NOWHERE (set-pair and Ryser
  literatures fully disjoint across three full-text scans); the field's
  only ceiling is Erdős–Rado ≈ 3.36×10⁷. **The two-sided window is
  ours; the 456 has no published counterpart at all.**
- **Name the function** (D-031): three distinct published 13s and three
  9s live near our ladder — the disambiguation table is in the turn-10
  notebook §5. Our g(5) ≡ published f(6); our g(4)/N(4) is NOT
  Tripathi's q(4).

## Risk decomposition — updated for turn 10

| step | what stands under it now |
| --- | --- |
| the floor m ≥ 22 | unchanged from turn 9 (0012's row); nothing in turn 10 touched it |
| **m ≤ 462 (0013)** | criticality + drop-by-one + private covers + Katona argument; adversarially verified ×6; enacted by exhaustion at two scales; saturated witness shows the abstract argument is tight |
| **m ≤ 456 (0014)** | 0013's construction + (A) + exact rank-6 witness (sensitivity-controlled) + 246 pattern witnesses; adversarially verified ×5; independently reimplemented; the r = 2 calibration guards the shape |
| g(5) = 13 | now ALSO the published f(6) = 13 (two independent published proofs) — the rung's risk class improves again |
| the ladder coincidences | the 9s/13s zoo is a documented confusion hazard, not a math risk — D-031 |

## Machinery — lessons that earned their line (turn-10 additions)

- **Calibrate a claimed refinement at the smallest r before deriving**
  (D-033): the r = 2 truth (max = 2, not 1) cost twenty minutes, killed
  the naive "−r" reading, and forced the audit to locate exactly which
  hypothesis buys the six units. Tiny-r truth tables before proof
  attempts.
- **A guessed constant in a check is a lie waiting to be caught** — 0013
  draft 1 pinned three; the run caught them (D-017's shape, again).
- **State ledgers transitively** (D-032): 0013 draft 1 shipped three
  mutually inconsistent floor-dependency lists; the authority is the
  consumed certificate's OWN ledger, followed transitively.
- Prior lessons (turn 9 and earlier) stand: measure before theorising ·
  diff design sets, not headline counts · inventory your own witnesses ·
  a dead heat is a forcing · weaken deliberately when the conclusion
  survives.

## Standing

- Every certificate names its dependencies; the ceiling of 0013 has
  **none** (external or in-house); 0014's are 0005 + 0013, external
  NONE. The floor's ledger is empty of external inputs, as before.
- No solver in the trust chain. Both fleets' outputs entered no chain
  until re-derived at the desk (Certificate Law); the adversarial
  records live in each certificate's NOTES.
- Attribution is recorded, not consumed (D-031): 0013 stands without
  citations while NOTES/notebook carry Bollobás 1965 · Katona 1974 ·
  Jaeger–Payan 1971 · Tuza 1985 · Li 2025 exactly.
