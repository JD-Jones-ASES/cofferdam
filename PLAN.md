# cofferdam — plan

Revised 2026-08-03 (turn 18). History is the record; this file is rewritten.

## Where we are — **[22, 456]; X ≥ 7 EVERYWHERE; X ≥ 8/9/10 from m = 25/29/30; X ≥ 5173 at the ceiling**

| what | where |
| --- | --- |
| the floor **m ≥ 22**, citing nothing | 0001–0012 |
| the window **m ∈ [22, 456]** | 0013, 0014 |
| the per-edge budgets and growth laws — (CC) 3/2 · corner ladder · C3 · (G) | 0015, 0017 |
| the floor-local excess chain X ≥ 2/3/4 at m = 22 | 0015, 0016, 0018 |
| star-collision: **X ≥ 5**, then **X ≥ 6** + the quadratic law (5173 at 456) | 0019, 0020 |
| **X ≥ 7 everywhere**; staircase 26/28/29 | 0021 |
| **X = 7 ⟹ m ≤ 24; the staircase squares off to 24/28/29** | 0022 |

**0022, the live edge, in four lines:**

- **Machinery.** Raw (LD) sieve over all 15 partitions of 7, generated
  in-cert → quotient classification (which shared-set overlaps force closing
  pairs — every completeness claim a finite enumeration) → J-debits → exact
  censuses (the identity pinned, low-cell profiles solved to emptiness).
- **Kills.** (7,26): four raw survivors — (3,3,1) J ≥ 21; (2,2,1,1,1) J ≥ 8;
  (2,2,2,1) nontriangle J ≥ 10, triangle by census at 74 vs 73; (1⁷) by
  trichotomy on |U|, the decisive subcase twice (capacity + census).
  (7,25): six raw survivors; three die only by equality forcing at 70 vs 68
  (s-profiles (7,7,2,2,2) / all-q₁-sets-equal-T / forced K₄), all landing on
  the census's single degree-3 cell.
- **Margins.** One-unit optimizer cell ((2,2,2,1) triangle @ 25, 67 vs 68);
  zero-gap census cells at 26; M-RG reopens the 25-triangle outright.
- **Provenance.** Fifth outside audit proposed the theorem and both rung
  proofs; zero errors found in our chain; its 0021 defect confirmed
  (erratum filed, numbers stood); **its own repair lemma was incomplete**
  — desk + all three refuters found the apex hole, one refuter found the
  C3 rescue; the honest case law is 0022 §3.

All green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O` (D-015).

**The chain, one paragraph.** (A)(B)(C) → ladder → m ≥ 22. Criticality →
Katona → part-confinement → **m ≤ 456**. Excess: (CC) → X ≥ 2 → (T) → X ≥ 3 →
eight shapes → X ≥ 4 → star-collision → X ≥ 5 → strict star-collision →
X ≥ 6 + the quadratic law → the q_max debit → X ≥ 7 everywhere → **shared-set
quotients → X ≥ 8 from m = 25, X ≥ 9 from 29, X ≥ 10 from 30;
X ≥ ⌈m(m−25)/38⌉ window-wide**.

## Where to attack — reranked after turn 18

1. **The (7,24) wall — zero margin, structure required.** The (2,2,2,1)
   triangle ties Λ₇(24) = 62 exactly at (10,9,6); census pinned at
   (12,5,0,16); **the adjacent-apex pattern is LIVE there (c₃ = 5)** — 0022
   §3 carries its witness. Counting alone cannot breach it (the tie IS the
   counting schema's own limit statement). New levers, banked turn 18:
   **the 6-partite tiling test** (n = 36 ⟹ the 36 degrees tile into six
   6-blocks summing to m; strictly stronger than the census; the (7,24)
   template survives it — measured, honest negative) and **(EC)
   admissible-quotient completeness** (enumerate every quotient of the
   free shape template; the apex escape becomes generated, not
   remembered). Plus: per-part confinement of the (10,9,6) stars; the
   banked adjacency-aware J-bound, certified before imposed. Then 23, 22.
2. **Promote the banked bonus rungs** (unchanged: X = 9 ⟹ m ≤ 28,
   X = 10, 11 ⟹ m ≤ 29, X = 12 ⟹ m ≤ 31 — single-route, unaudited).
3. **The ceiling is soft** (unchanged from turn 17: (Q) at X = 5172 forces
   degree collapse; the J-conjunction is the unspent strengthening).
4. **(G)'s successors + the b-aware hybrid** (unchanged from 0017).
5. **Field mining — turn-18 harvest (see notebook § Research).** No
   shortcut to the frontier found; four method imports banked: (EC)
   quotient completeness (item 1) · the forced-equality mechanism and
   bounded-exceptional-set pattern (proofs Ch 9) · the certificate-class-
   limit discipline (Ch 1 — applied: the (7,24) tie is our schema's limit)
   · the Möbius injectivity conversion (Ch 5, candidate for straddling-
   part configurations). Named non-transfers recorded so no turn is spent
   re-deriving them.
6. **Per-part hand claim · conditioned-class equality scans** (unchanged).

**Closed levers (do not reopen silently):** turns 10/13/14/15/16/17 lists,
plus: the X = 7 band above m = 24 (turn 18: DONE — 0022 emptied 25 and 26;
0021's 27/28 stand) · the 0021 triangle-prose defect (erratum filed;
honest case law in 0022 §3 — do not re-litigate the numbers, they were
measured equal) · banked-not-consumed: the adjacency-aware J-bound · the
bonus rungs · 0019/0020-banked items.

## Novelty ledger — updated 2026-08-03 (turn 18)

Floor comparator unchanged (Sivashankar m ≥ 14; ours 22) — now with X ≥ 8
from m = 25 and the frontier at three edge counts. The two-sided window
remains ours; 456 and the excess profile have no published counterpart.
Publication is JD's call — `awaiting_jd` stands, now with five
outside-verified theorems. The outside-audit lane has produced a theorem on
each of its five turns; the intake ledger now records defects caught in
both directions on three consecutive turns.

## Risk decomposition — updated for turn 18

| step | what stands under it now |
| --- | --- |
| m ≥ 22 / m ≤ 456 | unchanged (0012 / 0013–0014) |
| X ≥ 5 / X ≥ 6 / X ≥ 7 + staircase (0019/0020/0021) | unchanged; 0022 consumes 0021's T-A21/T-B21 and re-verifies both frontier rungs by its own sweep |
| **X = 7 ⟹ m ≤ 24 (0022)** | 15-partition sweeps ×2 rungs; tightest: (2,2,2,1)-triangle@25 at ONE unit (M-RG reopens it, 67 → 74); (1⁷)@26 at ZERO gap (census + capacity, both enacted); three equality-forced kills@25 at 70 vs 68; M-D2E flips the two profile kills; M-T5 flips the capacity kill; M-f flips the decisive wall 73 → 83 |
| **the (7,24) preview** | NOT a claim — the tie is exact, the apex pattern live, the census pinned; treat as the next campaign's wall, not as progress |
| (Q)/(Q0)/5173 | unchanged (0020) |

## Machinery — the working lessons (the law itself lives in DECISIONS.md)

- **Verify the frame before the number, and the repair before the story.**
  The fifth audit's defect-find was real and its numbers all held, but its
  repair lemma was itself incomplete — and the missing case turned out to
  be C3-dead at the audited rungs and LIVE at the next wall. Three intakes
  running, the numerical answer survived while a stated support needed
  repair. Enact the case law; never inherit the sentence.
- **A dominated branch is still a branch.** The apex pattern maxes at 54
  against walls of 67+ — and carrying it anyway is what makes the (7,24)
  preview number already correct for the next campaign.
- **Sweep completeness is itself a check** (turn 16's M9; 0022's M-SWEEP).
- **Measurement over expectation** (D-035); peer intake D-036.

## Standing

- Twenty-one green certificates, each ×2 (bare 3.9.6 and `-O`), plus 0004
  never-green scaffolding. External-input ledger: EMPTY.
- No solver in the trust chain. Fleet outputs entered no chain until
  desk-re-derived (Certificate Law); adversarial records in each NOTES.
- Attribution recorded, not consumed (D-031, D-036): five outside reviews
  credited in provenance; no proof step cites any of them.
