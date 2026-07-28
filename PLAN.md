# cofferdam — plan

Revised 2026-07-27 (turn 13). History is the record; this file is rewritten.

## Where we are — **[22, 456]; X ≥ 3 AT THE FLOOR; THE WINDOW NONLINEAR ALMOST EVERYWHERE**

| cert | result |
| --- | --- |
| **0001** (22 + 0) | degree-cap ladder; g(1..4) = 1,3,5,8 → m ≥ 18 citing nothing |
| **0002** (22 + 1) | **(L4)** Σ deg ≥ m+5 per edge |
| **0003** (10 + 2) | **(L5)** low-incidence bound |
| **0005** (49 + 5) | **minimum-degree ladder**: m ≥ 19 citing nothing; (A)(B)(C); corrected AKP 2.8 |
| **0006** (22 + 0) | **(L8) excess-concentration**: m = 20 impossible (cited ladder) |
| **0007** (18 + 1) | (L8) on the weak ladder kills every m ≤ 20 → **m ≥ 21 citing nothing** |
| **0008** (43 + 4) | **(D2)** degree-two cap kills m = 21 → **m ≥ 22 citing nothing** |
| **0009** (38 + 13) | **g(5) = N(5) = 13 citing nothing**; the free ladder EQUALS the cited ladder |
| **0010** (24 + 3) | **N(4) = 9 BY HAND** — the hinge is a theorem |
| **0011** (61 + 12) | **Δ = 4 for 13-edge τ ≥ 5 objects**; the (8,4) census proven complete twice |
| **0012** (12 + 5) | **(L10) saturation floor — the δ-budget retires**; m = 21 dies at margin ≥ 6 |
| **0013** (32 + 8) | **THE WINDOW [22, 462]**; ceiling ledger EMPTY; Ryser r=6 ⟺ no critical core in the window |
| **0014** (13 + 4) | **(L11) part-confinement → [22, 456]**; the peer-claimed 456 is an in-house theorem |
| **0015** (19 + 3) | **(CC)** + **X ≥ 2 at m = 22**; margin one unit (231 vs 232). Erratum 2026-07-27: its "floor lands exactly at 2" label overclaimed; reworded, check untouched |
| **0016** (45 + 8) | **(T) the triangle lemma** (a ≥ 2 ⟹ X ≥ 3, self-contained) + **(CC+)** I_e ≤ X − x_e at X ≤ 2 (3/2 sharper) + **X ≥ 3 FOR EVERY CRITICAL CORE AT m = 22** — the 9,224-config X = 2 "frontier field" of turn 11 is EMPTY; margin ONE UNIT of (D2). Erratum 2026-07-27 (turn 13): its "(CC+) unavailable at X=3" notes were false as written; reworded, checks untouched |
| **0017** (61 + 12) | **THE EXCESS-GROWTH LAWS**, window-wide: the corner ladder (**(CC+) holds through X ≤ 4**; dies at X = 5, witness; end-to-end at X = 5 OPEN) · the unconditional pair-sum (complement to (CC)) · linear law 2m + 5x_e ≤ 52 + 3X → lifted **X ≥ 3/3/4 at m = 27/28/29, 290 at 456** · coupling **X ≤ 2 ⟹ m ≤ 26, X ≤ 4 ⟹ m ≤ 28** · **(G) second-moment law: X ≥ 2259 at m = 456**, crossover m = 67 · combined profile: forced X ≥ 1 on 431/435 m-values — **the only arithmetic-free rungs are m ∈ {23,24,25,26}** |

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).
0016 was built through three fleet phases (derive → adversarial ×3 → draft +
hostile audit with 20 sabotages), every consumed step desk-re-derived; the
margin-coordinate and weakened-enactment catches are D-034/D-035 material.

**The chain, one paragraph.** (A)(B)(C) → the pinned ladder N(1..5) =
2,4,6,9,13 → m ≥ 22 (0012's ledger transitively). Criticality → private
5-covers → Katona-style disjoint events → m ≤ 462 (0013) → part-confinement
→ **m ≤ 456** (0014). At the floor: (CC) → X ≥ 2 (0015); the triangle lemma
kills the 3/2 corner at X ≤ 2 → (CC+) → per-edge budgets 2/1/0 → the
λ-trichotomy prices the excess-carrying vertices → W ≤ 24 vs field minimum
27 under (D2) → **X ≥ 3** (0016).

## Where to attack — reranked after turn 13

1. **The λ4-pair rung at X = 3, m = 22.** Turn-13 census (fleet-verified,
   banked in the t13 notebook §3, NOT yet certified): shape-blind W ≤ 48
   leaves 1,580 of 186,086, and **1,549 are consistent only with the
   λ = 4 pair** — two edges with x = 3, all twelve degrees ≤ 6, row sums
   exactly 30, shared 4-set across 4 parts. That is transversal-level
   structure the degree field cannot see: build the two-edge local judge
   (the L1 degree-array machinery is written down) and certify the
   census + star kill (bound 24 < floor 27, Claim-B-free) on the way.
   Joint per-shape bounds need vertex-identification enumeration to be
   cert-grade (census lane's loud flag). X = 3 already impossible at
   m ≥ 28 (0017's coupling).
2. **The m ∈ {23,24,25,26} thin rungs.** 0017 names them: the only sizes
   in the window with NO forced excess. 0016's lemmas ((T), (CC+),
   W-bounds) are m-free; only the field scan was m = 22. Re-run the
   X ≤ 2 field machinery at m = 23..26 (cheap; X ≤ 2 cores are confined
   to exactly these m by 0017) — a kill there would make **X ≥ 3
   universal on the whole window**.
3. **(G)'s successors at the ceiling.** The Jensen step is now certified
   machinery: (a) the b-aware hybrid Φ ≥ max(ψ(d), d−6+b) to smooth the
   m = 67 crossover; (b) an UPPER bound on X — with X ≳ m²/90 forced
   from below, any sub-quadratic upper bound caps m outright (the
   window would shrink from 456); candidates: the intersecting-ness
   axiom lane, C(2r−2, r−1) → 252 (abstract r = 4 open in [17, 35],
   settle it first, D-033 style).
4. **Mine the field's complementary finite framings** (unchanged): DeBiasio
   Table 2 (173 signatures) × the window; Pokrovskiy 2507.05842; Barát's
   18×18 PG(2,5) incidence matrix vs our truncated-plane machinery.
5. **Re-derive the stronger per-part hand claim** (unchanged from turn 9):
   every part of an 8-edge τ ≥ 4 object carries a degree-1 vertex.
6. **Conditioned-class equality scans** (unchanged).

**Closed levers (do not reopen silently):** turn 10's list, plus:
**the growth-law verification (turn 13: DONE, cert 0017 — the spin-off,
its integrality lift, and (G) all certified; the m²/90 asymptote is a
note, never a bound)** · **OPEN flag on file: whether (CC+)'s end-to-end
conclusion survives at X = 5 (the corner dies there; the witness kills
only the middle step)** ·
**PLAN-11 rung (b) — per-edge (CC) with real b-profiles — CLOSED NEGATIVE
(turn 12, lane B's B5)**: the min-over-b equals the Φ(·,5) relaxation
whenever Σ(6−dᵢ)⁺ ≥ 5, which (L4) forces at m = 22 for every X ≤ 4; first
bites at Σdᵢ = 32. · The X = 2 stratification campaign (mooted: the layer
is empty, cert 0016). · Hall/rearrangement and L² column-balance filters
(proven equivalent to the row-sum identity locally; 0 kills).

## Novelty ledger — unchanged from turn 10 re-measure

Floor comparator: Sivashankar arXiv:2606.24878 gives m ≥ 14; ours 22 → 22
with X ≥ 3 structure on top. Ceiling: the two-sided window remains ours;
456 has no published counterpart. Name the function always (D-031).
Publication timing is JD's call — `awaiting_jd` stands.

## Risk decomposition — updated for turn 12

| step | what stands under it now |
| --- | --- |
| m ≥ 22 | unchanged (0012's row) |
| m ≤ 456 | unchanged (0013/0014's rows) |
| X ≥ 2 at m = 22 | 0015, adversarial ×2, margin one unit (231/232) |
| **X ≥ 3 at m = 22 (0016)** | (T) exhausted over 5⁶ patterns; (CC+) on 0015's certified steps; field kill reproduced by 4 independent implementations; adversarial ×3 + hostile audit (20 sabotages); **margin ONE UNIT of (D2)** — if 0008 is ever weakened, recompute before re-quoting |
| the λ-trichotomy | complete by arithmetic (2 = 2 or 1+1); the case bounds exhausted in-cert |

## Machinery — lessons that earned their line (turn-12 additions)

- **State the margin in every consumed cap's coordinate; the binding one
  may not be the headline's** (D-035): 0016 looked 4-units comfortable in
  W and is 1-unit tight in (D2). A D-017 statement is complete only when
  the binding coordinate is identified.
- **An enactment weaker than its label is a red-team finding even when
  the theorem is true** (D-035): covers of size < 5 fed to 5-class Φ
  understated the left side systematically; pad to the hypothesis, then
  re-pin.
- **Green certificates can carry label drift; errata are same-commit,
  dated, condition-untouched, re-verified** (D-034).
- Prior lessons stand: tiny-r calibration (D-033) · measure before
  theorising · a guessed constant is a lie waiting to be caught (twice
  more this turn: Φ(8,5), and the draft's unpinned counts) · transitive
  ledgers (D-032) · diff design sets, not headline counts.

## Standing

- Sixteen certificates, each green ×2. External-input ledger: EMPTY —
  floor, ceiling, refinement, and now the excess floor.
- No solver in the trust chain. Fleet outputs entered no chain until
  desk-re-derived (Certificate Law); the adversarial records live in each
  certificate's NOTES.
- Attribution recorded, not consumed (D-031). The banked lane-B theorems
  (B1–B7) live in the turn-12 notebook §5 with per-item verification
  status; only desk-verified items may be consumed without re-derivation.
