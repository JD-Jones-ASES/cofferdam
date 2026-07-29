# cofferdam — plan

Revised 2026-07-28 (turn 16). History is the record; this file is rewritten.

## Where we are — **[22, 456]; X ≥ 6 EVERYWHERE; the staircase X ≥ 7/8/9/10 from m = 27/29/30/32; X ≥ 5173 at the ceiling**

| what | where |
| --- | --- |
| the floor **m ≥ 22**, citing nothing | 0001–0012 |
| the window **m ∈ [22, 456]** | 0013, 0014 |
| the per-edge budgets and growth laws — (CC) 3/2 · corner ladder · C3 · (G) | 0015, 0017 |
| the floor-local excess chain X ≥ 2/3/4 at m = 22 | 0015, 0016, 0018 |
| **X ≥ 5 everywhere; X = 5 ⟹ m ≤ 26** | 0019 |
| **X ≥ 6 everywhere; the staircase; the quadratic law** | 0020 |

**0020, the live edge**, in four lines:

- **Lemmas.** q ≤ 3 (the λ = 5 five-cover obstruction) · F(d) ≤ s(z) balanced ·
  **F + q_max ≤ s** strict (needs τ ≥ q_max + 2) · P + H ≤ R · the key cap
  F(d(v)) ≤ X − q₁, which drives every sweep.
- **Engines.** 35-cell X = 5 census (+ a m = 27..31 belt) · 92-cell staircase
  sweep with ONE arithmetic survivor, (8,30,(3,3,1,1)), killed by the T_v
  profile maximizer (MAXHIGH 40 → 940 < 1066).
- **Billing.** Staircase is (D2)-free by construction; (q3) is spent on the
  Q law and nowhere else.
- **Provenance.** Theorems and route proposed by the third outside audit,
  whose §7.2 partition list was incomplete at (8,30) — found by three refuter
  lanes independently and repaired in-house; (H1)/5173 is this desk's own step
  past the review's 5172.

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).
Turn-16 intake ran 9 verification lanes, a drafter, 3 cert auditors and a fix
lane, and retracted the turn-15 circularity charge (D-036).

**The chain, one paragraph.** (A)(B)(C) → ladder → m ≥ 22. Criticality →
Katona → part-confinement → **m ≤ 456**. Excess: (CC) → X ≥ 2 → (T) → X ≥ 3 →
eight shapes → X ≥ 4 → (DH)/(SC) census → X ≥ 5, X = 5 ⟹ m ≤ 26 →
(BDH)/(SSC+)/(SG) → **X ≥ 6 everywhere, the staircase, and the quadratic law
X ≥ ⌈m(m−25)/38⌉ window-wide (5173 at the ceiling)**.

## Where to attack — reranked after turn 16

1. **X = 6 on m ∈ {22, 23, 24, 25, 26} — the minimum-excess band.** The same
   engine one rung up: partitions of 6 with parts ≤ 3 (seven of them), the key
   cap F ≤ 6 − q₁, per-partition (SG) budgets, the T_v profile maximizer for
   heavy shapes. Measured warm start: the X = 6 sweep already kills m = 26 via
   the maximizer (822 vs 818, MAXHIGH 18 — the m ≤ 25 by-product, measured
   NOT claimed; an independent derivation promotes it). A kill of the whole
   band gives X ≥ 7 everywhere and re-runs the staircase from above.
2. **The ceiling is soft and knows it.** (Q) at X = 5172 forces H = 0 and all
   degrees ≤ 5, capping Σd² at 13,680 against a required 220,560 — the true
   ceiling floor is FAR above 5173. Levers: a lower bound on H (per-part
   structure forces high degrees at large m: Σ_part d = m over ≤ m/2 …
   measure); carrying Σ5; iterating (Q) against the (G) Jensen law's moment
   machinery. Any sub-quadratic upper bound on X still caps m outright.
3. **(G)'s successors + the b-aware hybrid** (unchanged from 0017).
4. **Mine the field's complementary finite framings** (unchanged).
5. **Re-derive the stronger per-part hand claim** (unchanged from turn 9).
6. **Conditioned-class equality scans** (unchanged).

**Closed levers (do not reopen silently):** turns 10/13/14/15 lists, plus:
the X = 5 campaign (turn 16: MOOT — 0020 emptied the layer; the five-partition
shape plan of turn 15 was never needed) · the X = 6 horizon scan (ANSWERED —
the staircase) · banked-not-consumed: the m ≤ 25 by-product at X = 6 · the
review's two-tier §6.2 cap model (correct, weaker than the key cap — the
model-comparison note in 0020) · 0019-banked items (S2′, the alternative
layer proofs, the 5n identity).

## Novelty ledger — updated 2026-07-28 (turn 16)

Floor comparator unchanged (Sivashankar m ≥ 14; ours 22) — now with **X ≥ 6
window-wide, a four-step staircase, and a quadratic excess law** on top. The
two-sided window remains ours; 456 has no published counterpart; the excess
profile (X ≥ ⌈m(m−25)/38⌉, 5173 at the ceiling) has no published counterpart
at any rung. Publication timing is JD's call — `awaiting_jd` stands, again
strengthened. The outside-audit lane has produced a theorem on each of its
three turns.

## Risk decomposition — updated for turn 16

| step | what stands under it now |
| --- | --- |
| m ≥ 22 / m ≤ 456 | unchanged (0012 / 0013–0014) |
| X ≥ 5, X = 5 ⟹ m ≤ 26 (0019) | unchanged; 0020 consumes both claim rows (T-B measured not-load-bearing — §3's belt covers m = 27..31) |
| **X ≥ 6 everywhere (0020 §3)** | 35 cells, margins ≥ 2 (thinnest: (2,2,1) at m = 22..24); needs (D2) at m = 22, 23 (11 cells reopen without it — M3); needs n ≥ 36 (M4) and Δ ≤ 9 via (SSC+) (M2); +H load-bearing on 17 cells (M1) |
| **the staircase (0020 §4)** | 92 cells (D2)-free; one structural kill at (8,30,(3,3,1,1)) — the T_v maximizer with \|T_v\| ≥ 2 (M10: dropping it breaks the kill, 1090 > 1066 — genuinely load-bearing); thinnest arithmetic kill 2 units at (8,30,(3,2,2,1)) |
| **(Q)/(Q0)/5173** | q ≤ 3 is its only (q3) consumer (M6: at q ≤ 4 the ceiling drops to ~4095); the 5172→5173 lift rides on ONE high vertex (H1) — and §5 shows the true floor is far higher |

## Machinery — the working lessons (the law itself lives in DECISIONS.md)

- **Sweep completeness is itself a check.** The third audit's one real defect
  was an incomplete case list — (8,30) admits three partitions, its text named
  one. An audit lane that only checks the listed cases inherits the listing's
  blindness (M9: truncating the partition list produces a false all-clear).
- **Attribution symmetry cuts both ways.** The 0020 draft credited all eight
  claim rows to the review; (H1)/5173 is this desk's. Giving credit away is
  the same bookkeeping failure as taking it.
- **Measurement over expectation** — three spec numbers refused to reproduce
  and the measurements shipped; an inert mutant is table inflation.
- Peer-intake law: D-036. Margins in every consumed coordinate: D-035.

## Standing

- Nineteen green certificates, each ×2 (bare 3.9.6 and `-O`), plus 0004
  never-green scaffolding. External-input ledger: EMPTY.
- No solver in the trust chain. Fleet outputs entered no chain until
  desk-re-derived (Certificate Law); adversarial records in each NOTES.
- Attribution recorded, not consumed (D-031, D-036): three outside reviews
  credited in provenance; no proof step cites any of them.
