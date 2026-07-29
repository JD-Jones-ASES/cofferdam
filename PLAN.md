# cofferdam — plan

Revised 2026-07-29 (turn 17). History is the record; this file is rewritten.

## Where we are — **[22, 456]; X ≥ 7 EVERYWHERE; X ≥ 8/9/10 from m = 27/29/30; X ≥ 5173 at the ceiling**

| what | where |
| --- | --- |
| the floor **m ≥ 22**, citing nothing | 0001–0012 |
| the window **m ∈ [22, 456]** | 0013, 0014 |
| the per-edge budgets and growth laws — (CC) 3/2 · corner ladder · C3 · (G) | 0015, 0017 |
| the floor-local excess chain X ≥ 2/3/4 at m = 22 | 0015, 0016, 0018 |
| star-collision: **X ≥ 5**, then **X ≥ 6** + the quadratic law (5173 at 456) | 0019, 0020 |
| **X ≥ 7 everywhere; the staircase sharpens to 26 / 28 / 29** | 0021 |

**0021, the live edge**, in four lines:

- **Lemmas.** (SJ) P + Σ q_max(v) ≤ R — 0020's own un-weakened line, promoted ·
  (LD) the largest-pair debit P ≤ R − q₁(q₁+1) · (DM) d² ≤ 8d − 15 + 3[d=2] +
  f(f+2) for every d ≥ 2, summed to the exact identity Ψ = m² − 43m + 2X +
  15n − 3n₂ + n₄ · (RG) residual pairing |K_U| ≥ 2(6−k) − 1.
- **Engines.** 45-cell X = 6 elimination (nine partitions × five rungs, the
  parts-4 rows carried and killed) · five staircase rungs + a 142-cell belt ·
  the knapsack is cost-F/value-ψ, exhaustive — the f-for-F swap flips 15 raw
  cells and is a named mutant.
- **Margins.** Three one-unit cells; one ZERO-margin cell ((23,(10,9)) clears
  its moment requirement exactly and dies only by census counting); (D2)+1
  reopens 6 cells — measured after three intake lanes disagreed.
- **Provenance.** The fourth outside review proposed all of it — zero errors
  found in our chain, zero retractions owed either way; its stated-step
  defects (the f/F cost trap; a missing disjointness-by-C3 step that would
  have tied a kill at exactly Λ) were repaired in-house before certification.

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).

**The chain, one paragraph.** (A)(B)(C) → ladder → m ≥ 22. Criticality →
Katona → part-confinement → **m ≤ 456**. Excess: (CC) → X ≥ 2 → (T) → X ≥ 3 →
eight shapes → X ≥ 4 → star-collision → X ≥ 5 → strict star-collision →
X ≥ 6 + the quadratic law → **the q_max debit → X ≥ 7 everywhere, X ≥ 8 from
m = 27, X ≥ 9 from m = 29, X ≥ 10 from m = 30; X ≥ ⌈m(m−25)/38⌉ window-wide**.

## Where to attack — reranked after turn 16

1. **X = 7 on m ∈ {22, 23, 24, 25, 26} — the minimum-excess band.** At m = 26
   the measured sieve leaves **two shapes under the sharp bound, three under
   the conservative one**: (2,2,2,1) — alive only through its triangle, at one
   unit (74 vs Λ = 73) — (1⁷), and conservatively (2,2,1,1,1). The 0021
   engine one rung up plus the adjacency-aware J-bound (derived in 0021,
   printed, deliberately not imposed) is the opening move.
2. **Promote the banked bonus rungs.** One guarded lane measured X = 9 ⟹
   m ≤ 28, X = 10, 11 ⟹ m ≤ 29, X = 12 ⟹ m ≤ 31 — single-route, unaudited.
   An independent derivation certifies them cheaply.
3. **The ceiling is soft and knows it.** (Q) at X = 5172 forces H = 0 and all
   degrees ≤ 5, capping Σd² at 13,680 against a required 220,560 — the true
   ceiling floor is FAR above 5173. Levers: lower bounds on H and Σ₅; the
   J-conjunction (debit + per-high-vertex charge together — 0021 banked it);
   any sub-quadratic upper bound on X still caps m outright.
4. **(G)'s successors + the b-aware hybrid** (unchanged from 0017).
5. **Mine the field's complementary finite framings** (unchanged).
6. **Per-part hand claim · conditioned-class equality scans** (unchanged).

**Closed levers (do not reopen silently):** turns 10/13/14/15/16 lists, plus:
the X = 6 campaign (turn 17: DONE — cert 0021 emptied the layer; the m ≤ 25
by-product is absorbed, superseded by the full kill) · banked-not-consumed:
the adjacency-aware J-bound (kills (2,2,1,1,1)@(7,26) at 70 < 73 and would
dissolve one one-unit margin — certify before imposing) · the bonus rungs
(item 2) · 0019/0020-banked items.

## Novelty ledger — updated 2026-07-29 (turn 17)

Floor comparator unchanged (Sivashankar m ≥ 14; ours 22) — now with **X ≥ 7
window-wide, the staircase at 26/28/29, and the quadratic law** on top. The
two-sided window remains ours; 456 and the excess profile have no published
counterpart at any rung. Publication is JD's call — `awaiting_jd` stands,
now with four outside-verified theorems. The outside-audit lane has produced
a theorem on each of its four turns.

## Risk decomposition — updated for turn 17

| step | what stands under it now |
| --- | --- |
| m ≥ 22 / m ≤ 456 | unchanged (0012 / 0013–0014) |
| X ≥ 5 / X ≥ 6 + staircase ceilings (0019/0020) | unchanged; 0021 consumes 0020's claim rows and re-verifies the band interiors by its own belt |
| **X ≥ 7 everywhere (0021 §3)** | 45 cells; **three one-unit cells** ((2,2,1,1)@22 56 vs 57 · (1⁶) no-f5 56 vs 57 · (1⁶) K4@26 70 vs 71 — the band-closing cell) and **one zero-margin cell** ((23,(10,9)): Ψ = Λ exactly, dies only by census counting); (D2)+1 reopens **6 cells** (measured; three intake lanes disagreed, the cert settled it); n ≥ 35 reopens 24; the f-for-F cost swap flips 15 raw cells — all named mutants |
| **the sharpened staircase (0021 §4)** | five rungs + a 142-cell belt; (D2) and (RG) load-bearing (RG 5→4 reopens (2,2,2)@24,25); the (7,27) kill needs the C3 triangle exclusion — without it the cell TIES at Λ = 83 (M-tri) |
| **(Q)/(Q0)/5173** | unchanged (0020); the J-conjunction is the unspent strengthening |

## Machinery — the working lessons (the law itself lives in DECISIONS.md)

- **A stated step and a computed step can differ silently.** The fourth
  review computed its knapsacks under cost F but stated them under cost f —
  the literal reading flips 15 cells alive. The convention is now a named
  mutant (M-f) and a margin coordinate in 0021.
- **Sweep completeness is itself a check** (turn 16's lesson, re-earned: a
  truncated partition list produces a false all-clear — M9 then, the carried
  parts-4 rows now).
- **A withdrawn charge is cheaper than a wrong one.** 0021's draft charged
  the review with a deflation over a number that was correct for the branch
  as the cert itself defined it; the audit caught it and the charge was
  withdrawn before shipping. Verify the frame before verifying the number.
- **Measurement over expectation** — where three intake lanes disagreed on a
  mutation's reopen set, the certificate measured it and named the
  disagreement. Peer intake: D-036. Margins: D-035.

## Standing

- Twenty green certificates, each ×2 (bare 3.9.6 and `-O`), plus 0004
  never-green scaffolding. External-input ledger: EMPTY.
- No solver in the trust chain. Fleet outputs entered no chain until
  desk-re-derived (Certificate Law); adversarial records in each NOTES.
- Attribution recorded, not consumed (D-031, D-036): four outside reviews
  credited in provenance; no proof step cites any of them.
