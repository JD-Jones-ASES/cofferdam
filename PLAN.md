# cofferdam — plan

Revised 2026-07-28 (turn 14). History is the record; this file is rewritten.

## Where we are — **[22, 456]; X ≥ 4 AT THE FLOOR; the λ4 frontier is gone**

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
| **0014** (13 + 4) | **(L11) part-confinement → [22, 456]**. Erratum 2026-07-28: closing prose "5 notes" → 4 (hand count included the helper def; outside-audit catch) |
| **0015** (19 + 3) | **(CC)** + **X ≥ 2 at m = 22**; margin one unit (231 vs 232). Erratum 2026-07-27 (D-034) |
| **0016** (45 + 8) | **(T) + (CC+) → X ≥ 3 AT m = 22**; margin ONE UNIT of (D2). Errata 2026-07-27 (D-034) |
| **0017** (61 + 12) | **THE EXCESS-GROWTH LAWS**, window-wide: (CC4+) through X ≤ 4 · linear law + lift (X ≥ 3/3/4 at m = 27/28/29, 290 at 456) · coupling (X ≤ 2 ⟹ m ≤ 26; X ≤ 4 ⟹ m ≤ 28) · (G) Jensen (X ≥ 2259 at 456) · forced X ≥ 1 on 431/435 rungs. NOTES errata 2026-07-28 (tally; 0013/0014 mischaracterization; outside-audit catches) |
| **0018** (33 + 10) | **THE X = 3 LAYER AT m = 22 IS EMPTY → X ≥ 4 AT THE FLOOR.** Eight-shape census; λ4 → m ≤ 20 · λ3+adj → m ≤ 21 · λ3+disj → heavy confinement W ≤ 23 · pair-sum maxima 24/27/27/28/30 by identification-pattern exhaustion · the (0,0,1) survivor dies all-shapes · 3K2 at forced equality dies twice. Margin: one unit of (D2) (5 → 46 survivors on relax); triangle/path at ZERO W-slack (census clash is binding). Theorem proposed by the outside audit (GPT 5.6 Sol Pro, 2026-07-28); every proof in-house (D-031/D-036) |

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).
0018 went through three fleet phases (2 field + 9 blind derivation lanes →
5 hostile refuters → 3-lens cert audit); the desk's own wrong "correction"
(path 27 → 26) and the missed all-(8,6) subcase are D-036 material.

**The chain, one paragraph.** (A)(B)(C) → pinned ladder → m ≥ 22 (0012's
ledger). Criticality → private 5-covers → Katona-style disjoint events →
m ≤ 462 (0013) → part-confinement → **m ≤ 456** (0014). At the floor:
(CC) → X ≥ 2 (0015) → (T) + (CC+) → X ≥ 3 (0016) → the eight-shape kill
→ **X ≥ 4** (0018). Window-wide: (CC4+) through X ≤ 4, the linear law and
its lift, the coupling, (G) (0017).

## Where to attack — reranked after turn 14

1. **The X = 4 layer at m = 22 — the new frontier.** 12,171 configs alive
   under (D2) + the shape-blind W ≤ 80 (0018 §10). The machinery that just
   won is still valid there: (CC4+) holds through X ≤ 4 (budgets 4 − x_e),
   the pair-sum is unconditional, and the shape census of 4 has five
   partitions — (4), (3,1), (2,2), (2,1,1), (1,1,1,1) — turn-13 banked
   23 shapes, field floor 32. Two cautions from 0017: the corner dies at
   X = 5, so a win here is the LAST rung this corner ladder climbs without
   new mathematics; and every equality analysis must redo its census
   bookkeeping (the all-(8,6) lesson). A kill gives X ≥ 5 and, with the
   coupling (X ≤ 4 ⟹ m ≤ 28), starts squeezing the window's low end.
2. **The thin rungs m ∈ {23, 24, 25, 26}.** Still the only sizes with NO
   forced excess (0017 C7). New leverage from 0018: the λ4 and λ3+adjacent
   kills are m-free counts (m ≤ 20/21), so X = 3 on the thin rungs already
   reduces to six shapes; the field scans re-run cheaply at each m. And
   0016's X ≤ 2 machinery re-runs there too (X ≤ 2 lives only on m ≤ 26 by
   0017's coupling). Killing X ≤ 2 there makes **X ≥ 3 window-universal**.
3. **(G)'s successors at the ceiling** (unchanged from turn 13): b-aware
   hybrid; any sub-quadratic UPPER bound on X caps m outright; the
   intersecting-ness axiom lane; C(2r−2, r−1) → 252 (abstract r = 4 in
   [17, 35] first, D-033 style).
4. **Mine the field's complementary finite framings** (unchanged): DeBiasio
   Table 2 × the window; Pokrovskiy 2507.05842; Barát's PG(2,5) matrix.
5. **Re-derive the stronger per-part hand claim** (unchanged from turn 9).
6. **Conditioned-class equality scans** (unchanged).

**Closed levers (do not reopen silently):** turn 10's and turn 13's lists,
plus: **the X = 3 campaign (turn 14: DONE, cert 0018 — census, kills,
equality analysis all certified; the λ4 two-edge-transversal judge PLAN
rank #1 of turn 13 is MOOT: the shape died by counting, no judge built)** ·
banked-not-consumed in the t14 notebook: Lemma D9 (X = 3 ⟹ Δ ≤ 8
window-wide) · the degree-descent alternative proof of 0018's theorem ·
shape-2's m-free Δ ≤ 6 · shape-3's counting kill.

## Novelty ledger — updated 2026-07-28

Floor comparator unchanged (Sivashankar m ≥ 14; ours 22) — now with
**X ≥ 4 structure at the floor** on top. The two-sided window remains ours;
456 has no published counterpart. Name the function always (D-031).
Publication timing is JD's call — `awaiting_jd` stands. **The outside-audit
lane is live and productive: first outside review found zero mathematical
errors and proposed the turn's theorem (D-036).**

## Risk decomposition — updated for turn 14

| step | what stands under it now |
| --- | --- |
| m ≥ 22 | unchanged (0012's row) |
| m ≤ 456 | unchanged (0013/0014's rows) |
| X ≥ 2 / X ≥ 3 at m = 22 | unchanged (0015/0016's rows) |
| **X ≥ 4 at m = 22 (0018)** | census complete by enumeration; kills verified by 9 blind lanes + 5 refuters + 3 cert auditors; field six-way agreed; **margins: one unit of (D2); zero W-slack on triangle/path (census clash binding); one unit in 3K2's subcase A** — if 0008 weakens, redo §7–9 before re-quoting |
| the corner ladder at X = 4 | 0017 C1; **dies at X = 5** — attack #1 is its last free rung |

## Machinery — lessons that earned their line (turn-14 additions)

- **A deflation is an error too (D-036):** the desk shaved a peer's correct
  bound (27 → 26) inside a "correction" and nearly consumed it. Skepticism
  toward a peer's numbers must be symmetric — enumerate, don't re-derive by
  hand and trust the smaller answer because it is yours.
- **Equality analyses must enumerate their census assignments** (the
  all-(8,6) lesson): "at most one" plus "at least one exists" was silently
  conflated with "exactly one". Three independent lanes caught it; the cert
  now enumerates the assignment dichotomy explicitly (check 27).
- **Statement-level peer intake works** (D-036): theorem in, proofs never;
  blind lanes re-derive; refuters attack; attribution recorded not
  consumed. The audit's numbers agreeing with six in-house implementations
  is corroboration, not authority — the cert cites only the implementations.
- Prior lessons stand: margins in every consumed coordinate (D-035) ·
  errata same-commit, condition-untouched (D-034) · a guessed constant is a
  lie waiting to be caught (three more this turn: two pinned counts and an
  uncertified-cap enactment, all caught by the cert's own first red run).

## Standing

- Eighteen certificates, each green ×2 (0004 never-green scaffolding).
  External-input ledger: EMPTY — floor, ceiling, refinement, excess floor.
- No solver in the trust chain. Fleet outputs entered no chain until
  desk-re-derived (Certificate Law); adversarial records live in each
  certificate's NOTES.
- Attribution recorded, not consumed (D-031/D-036): the outside audit's
  role is in 0018's NOTES provenance section; no step cites it.
