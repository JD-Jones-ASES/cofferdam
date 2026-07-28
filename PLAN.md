# cofferdam — plan

Revised 2026-07-28 (turn 15). History is the record; this file is rewritten.

## Where we are — **[22, 456]; X ≥ 5 EVERYWHERE; X = 5 only on m ≤ 26; X ≥ 6 from 27 up**

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
| **0014** (13 + 4) | **(L11) part-confinement → [22, 456]**. Erratum 2026-07-28 (outside-audit catch) |
| **0015** (19 + 3) | **(CC)** + **X ≥ 2 at m = 22**; margin one unit. Erratum 2026-07-27 (D-034) |
| **0016** (45 + 8) | **(T) + (CC+) → X ≥ 3 AT m = 22**; margin ONE UNIT of (D2). Errata 2026-07-27 |
| **0017** (61 + 12) | **THE EXCESS-GROWTH LAWS**, window-wide: (CC4+) at X ≤ 4 · the 4/3 per-pair corner at X = 5 · C3 (X-unrestricted) · C4/C5 · (G) Jensen (X ≥ 2259 at 456). NOTES + docstring errata 2026-07-28 (the X = 5 deflation; comments only, re-verified ×2) |
| **0018** (33 + 10) | **X = 3 EMPTY AT m = 22 → X ≥ 4 at the floor** — eight-shape census. Now a **corollary of 0019** (kept; not consumed by it). Erratum 2026-07-28: struck L1.2 removed from claim row |
| **0019** (60 + 9) | **(DH) + (SC) → X ≥ 5 ON EVERY RUNG; X = 5 ⟹ m ≤ 26; m ≥ 27 ⟹ X ≥ 6.** Two counting lemmas (part-mate exclusion → fibre pigeonhole; star-collision D ≤ R) + one census engine: 3,056 runs, all empty. Theorem + route proposed by the second outside audit (full text; D-037 routing); one circular step in the received proof repaired by the stronger Δ ≤ 5 + X. The 12,171-config X = 4 frontier closed WITHOUT enumeration |

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).
0019's record: desk re-derivation + 35-check script first; 11 verification
lanes (2 blind lemma provers, 3 blind layer lanes — two independent alternative
proofs, banked in the turn-15 notebook — numeric, 2 dependency audits, 3
refuters, zero fatal); then drafter + 3-lens cert audit (~25 fixes, all
measured); green ×2.

**The chain, one paragraph.** (A)(B)(C) → pinned ladder → m ≥ 22 (0012's
ledger). Criticality → private 5-covers → Katona-style disjoint events →
m ≤ 462 (0013) → part-confinement → **m ≤ 456** (0014). Excess: (CC) → X ≥ 2
(0015) → (T)+(CC+) → X ≥ 3 (0016) → eight-shape census → X ≥ 4 at the floor
(0018) → **(DH)+(SC) census engine → X ≥ 5 window-wide, X = 5 ⟹ m ≤ 26**
(0019). Window-wide laws: C1–C7, (G) (0017).

## Where to attack — reranked after turn 15

1. **X = 5 on m ∈ {22, 23, 24, 25, 26} — the only place a core can sit at
   minimum excess.** Five excess partitions: (3,2), (3,1,1), (2,2,1),
   (2,1,1,1), (1,1,1,1,1). Attack order per the audit's §9 (statement adopted,
   worth following): classify the weighted excess multigraphs of total weight
   5 → (DH) per edge class → the floored 4/3 budgets (6,5,4,2,1,0 at
   x_e = 0..5) → (SC) to force heavy vertices into the shared sets → only then
   the part-profile field. New tools banked for it: S2′ (R counts only
   degree-≥6 shared vertices), the fibre-level (DH) forms, l5's census
   identity. A kill gives **X ≥ 6 everywhere** and re-opens the same ladder at
   the next rung.
2. **The X = 6 horizon.** Before campaigning: measure whether the 0019 engine
   alone (with c = 3/2 budgets, the only corner above X = 5) already confines
   X = 6. Cheap scan, same machinery, honest chance of a free rung.
3. **(G)'s successors at the ceiling** (unchanged): b-aware hybrid; any
   sub-quadratic upper bound on X caps m outright; intersecting-ness axiom
   lane; C(2r−2, r−1) → 252 (abstract r = 4 in [17, 35] first).
4. **Mine the field's complementary finite framings** (unchanged): DeBiasio
   Table 2 × the window; Pokrovskiy 2507.05842; Barát's PG(2,5) matrix.
5. **Re-derive the stronger per-part hand claim** (unchanged from turn 9).
6. **Conditioned-class equality scans** (unchanged).

**Closed levers (do not reopen silently):** turn 10/13/14 lists, plus: **the
X = 4 campaign (turn 15: MOOT — 0019 closed the layer window-wide without
enumeration; the 23 banked shapes and the 12,171-config field are historical)**
· the thin-rung X ≤ 2 / X = 3 rescans (MOOT — X ≥ 5 covers them) · banked-not-
consumed in the turn-15 notebook: the negative-discriminant X ≤ 3 route · the
(d−3)(d−5) X = 4 route (its t=4 branch NEEDS confinement, not D ≤ R) · S2′ ·
S1+/S1++ · the 5n census identity.

## Novelty ledger — updated 2026-07-28 (turn 15)

Floor comparator unchanged (Sivashankar m ≥ 14; ours 22) — now with **X ≥ 5
window-wide structure** and a **two-theorem excess profile** on top. The
two-sided window remains ours; 456 has no published counterpart. Name the
function always (D-031). Publication timing is JD's call — `awaiting_jd`
stands, strengthened. **The outside-audit lane has now produced two theorems
in two days** (0018's and 0019's); the lane's laws are D-036 + D-037.

## Risk decomposition — updated for turn 15

| step | what stands under it now |
| --- | --- |
| m ≥ 22 | unchanged (0012's row) |
| m ≤ 456 | unchanged (0013/0014's rows) |
| X ≥ 2/3/4 at m = 22 | unchanged (0015/0016/0018) — 0018 now also a 0019 corollary |
| **X ≥ 5 everywhere; X = 5 ⟹ m ≤ 26 (0019)** | (DH)/(SC) derived in-cert + enacted; 3,056 census runs; margins: **X = 4 max-2 at m = 22 revives under five of nine mutants** (the certificate's named pressure point); m = 27/28 kills at ZERO D-slack (divisibility only); (D2) consumed by T-A at exactly 3 configurations, NOT by T-B — if 0008 weakens, redo those three cells |
| the corner ladder | C1 (c = 1, X ≤ 4) + check 9 (4/3, X = 5) both spent by 0019; **above X = 5 only c = 3/2 exists** — attack #2's question |

## Machinery — lessons that earned their line (turn-15 additions)

- **Agreement on a statement is not agreement on a proof (D-037).** The second
  audit's theorems were true and its route sound in outline — and its one
  degree-cap step was circular as written. Full received proof text goes ONLY
  to refuter lanes; blind lanes get statements + one-line mechanisms; the desk
  re-derives before the fleet flies. The desk's first read missed the circle;
  two refuters caught it.
- **A false "exactly one" in a spec is the same disease as a false census
  split** (the fixer's catch: the desk's no-(D2) parenthetical claimed one
  survivor; measurement says two, the second dying by (SC)). Instructions to a
  drafter are claims; measure them like claims.
- **An inert mutant advertised as load-bearing is table inflation** (M7): a
  mutation suite is itself a set of claims, and each row must be measured in
  the direction it advertises. Kept, relabeled inert, because the measurement
  is the value.
- Prior lessons stand: a deflation is an error too (D-036) · equality analyses
  enumerate their assignments · margins in every consumed coordinate (D-035) ·
  errata same-commit, condition-untouched (D-034).

## Standing

- Eighteen green certificates, each ×2 (bare 3.9.6 and `-O`), plus 0004
  never-green scaffolding. External-input ledger: EMPTY — floor, ceiling,
  refinement, excess profile.
- No solver in the trust chain. Fleet outputs entered no chain until
  desk-re-derived (Certificate Law); adversarial records live in each
  certificate's NOTES.
- Attribution recorded, not consumed (D-031/D-036/D-037): the outside audit's
  role is in 0019's NOTES provenance; no step cites it.
