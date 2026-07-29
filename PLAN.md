# cofferdam — plan

Revised 2026-07-28 (turn 16). History is the record; this file is rewritten.

## Where we are — **[22, 456]; X ≥ 6 EVERYWHERE; the staircase X ≥ 7/8/9/10 from m = 27/29/30/32; X ≥ 5173 at the ceiling**

| cert | result |
| --- | --- |
| **0001–0012** | the floor: **m ≥ 22 citing nothing** (pinned ladder; N(4) = 9 by hand; (D2); saturation) |
| **0013** (32 + 8) | **THE WINDOW [22, 462]**; ceiling ledger EMPTY; Ryser r=6 ⟺ no critical core in the window |
| **0014** (13 + 4) | **(L11) part-confinement → [22, 456]** |
| **0015** (19 + 3) | **(CC)** — the 3/2 per-edge Φ-budget, X-unrestricted — + X ≥ 2 at m = 22 |
| **0016** (45 + 8) | **(T) + (CC+) → X ≥ 3 at m = 22** |
| **0017** (61 + 12) | **THE EXCESS-GROWTH LAWS**: corner ladder (c = 1 ≤ 4 · 4/3 at 5 · 3/2 always) · C3 · C4/C5 · (G) Jensen |
| **0018** (33 + 10) | **X = 3 EMPTY at m = 22 → X ≥ 4 at the floor** (eight-shape census; now doubly a corollary) |
| **0019** (60 + 9) | **(DH) + (SC) → X ≥ 5 everywhere; X = 5 ⟹ m ≤ 26** (3,056 census runs; errata 2026-07-28: the turn-15 circularity charge retracted, D-038) |
| **0020** (55 + 12) | **(BDH)/(SSC+)/(SG) — the strict star-collision family → X ≥ 6 EVERYWHERE; the staircase X = 6/7/8/9 ⟹ m ≤ 26/28/29/31; (Q) m(m−25) + Σ5 + 10H ≤ 38X; X ≥ 5173 at m = 456.** New lemmas: q ≤ 3 (the λ = 5 five-cover obstruction) · F(d) ≤ s(z) balanced · F + q_max ≤ s strict (τ ≥ q_max + 2) · P + H ≤ R · the key cap F(d(v)) ≤ X − q₁. Engines: 35-cell X = 5 census (+ m = 27..31 belt) · 92-cell staircase sweep, ONE arithmetic survivor (8,30,(3,3,1,1)) killed by the T_v profile maximizer (MAXHIGH 40 → 940 < 1066). Staircase (D2)-free by construction; (q3) billed only to the Q law. Theorems + route proposed by the third outside audit; **its §7.2 partition list was incomplete at (8,30) — found by three refuter lanes independently, repaired in-house**; (H1)/5173 is the desk's own step past the review's 5172 |

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).
Turn-16 intake: 9 verification lanes (2 blind lemma provers — all six statements
PROVED twice — blind X = 5 + staircase lanes, numeric, dependency+record, 3
verbatim-file refuters per D-038), then drafter + 3 cert auditors + a fix lane.
The turn also RETRACTED the turn-15 circularity charge against the second
audit (D-038: the circle was in the desk's transcription; received texts now
go to refuters verbatim and are retained in notebook/raw/).

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
strengthened. **The outside-audit lane: three reviews, three turns, three
theorems** — and turn 16 both consumed a review's theorems AND retracted the
lab's own false charge against the previous one (D-038).

## Risk decomposition — updated for turn 16

| step | what stands under it now |
| --- | --- |
| m ≥ 22 / m ≤ 456 | unchanged (0012 / 0013–0014) |
| X ≥ 5, X = 5 ⟹ m ≤ 26 (0019) | unchanged; 0020 consumes both claim rows (T-B measured not-load-bearing — §3's belt covers m = 27..31) |
| **X ≥ 6 everywhere (0020 §3)** | 35 cells, margins ≥ 2 (thinnest: (2,2,1) at m = 22..24); needs (D2) at m = 22, 23 (11 cells reopen without it — M3); needs n ≥ 36 (M4) and Δ ≤ 9 via (SSC+) (M2); +H load-bearing on 17 cells (M1) |
| **the staircase (0020 §4)** | 92 cells (D2)-free; one structural kill at (8,30,(3,3,1,1)) — the T_v maximizer with \|T_v\| ≥ 2 (M10: dropping it breaks the kill, 1090 > 1066 — genuinely load-bearing); thinnest arithmetic kill 2 units at (8,30,(3,2,2,1)) |
| **(Q)/(Q0)/5173** | q ≤ 3 is its only (q3) consumer (M6: at q ≤ 4 the ceiling drops to ~4095); the 5172→5173 lift rides on ONE high vertex (H1) — and §5 shows the true floor is far higher |

## Machinery — lessons that earned their line (turn-16 additions)

- **A transcription is a claim (D-038).** The turn-15 refuters broke the
  desk's restatement of the peer's proof, and the desk recorded the break as
  the peer's defect. Received texts now go to refuters verbatim, are retained
  in `notebook/raw/`, and a defect found in restated material is re-checked
  against the original before it is recorded. The erratum runs through every
  turn-15 document, inline.
- **The third audit's one real defect was an incomplete case list** — (8,30)
  admits three partitions, its text named one — found independently by all
  three verbatim-file refuters, repaired in-house three ways before the cert
  encoded the strongest. An audit lane that only checks the listed cases
  inherits the listing's blindness: **sweep completeness is itself a check**
  (M9: truncating the partition list produces a false all-clear).
- **Attribution symmetry cuts both ways (audit catch, applied):** the draft
  credited all eight claim rows to the review; (H1)/5173 is the desk's own.
  Giving credit away is the same bookkeeping failure as taking it.
- Prior lessons stand: measurement over expectation (three spec numbers
  refused to reproduce and the measurements shipped) · an inert mutant is
  table inflation · margins in every consumed coordinate (D-035).

## Standing

- Nineteen green certificates, each ×2 (bare 3.9.6 and `-O`), plus 0004
  never-green scaffolding. External-input ledger: EMPTY.
- No solver in the trust chain. Fleet outputs entered no chain until
  desk-re-derived (Certificate Law); adversarial records in each NOTES.
- Attribution recorded, not consumed (D-031/D-036/D-037/D-038): three outside
  reviews credited in provenance; no proof step cites any of them.
