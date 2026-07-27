# Certificate 0009 — the g(5) rung pinned: g(5) = N(5) = 13, citing nothing

**Status: GREEN.** Checks + notes and runtime in the run log; `python3
verify.py`, stdlib only, no solver, no imports from `lib/`. Green under a
bare `/usr/bin/python3` (3.9.6) and under `python3 -O`.

| claim | label |
| --- | --- |
| **g(5) = 13** | **PROVEN-BY-CERTIFICATE, citing nothing** |
| **N(5) = 13** | **PROVEN-BY-CERTIFICATE, citing nothing** |
| Q13 answered **YES** | corollary — the witness is Q13's object |
| the citation-free ladder = the cited ladder | corollary — N = {2,4,6,9,13} |

## The two findings under this certificate

**1. The dead heat nobody named.** Certificate 0001's counting ladder kills
m = 10 and m = 11 at t = 5 but lands on exact equality at m = 12: per-part
maximum 11 pairs, uniquely at (4,3,2,2,1), and 6 × 11 = 66 = C(12,2). The
arithmetic has been printed in 0001's check-18 output since turn 1; no
document ever read it back. Equality is not a failure of the method — it is
the method handing over a **forced shape**: every part exactly (4,3,2,2,1),
excess X = 0 (every pair of edges meets in exactly one part), no repeated
edges. In column form: six partitions of [12], shape (4,3,2,2,1), tiling the
66 edge-pairs exactly once. That design space is small: with the first part
pinned (WLOG, edge relabelling), **11,520 complete designs exist and every
one has an explicit 4-cover**. m = 12 is dead, and g(5) ≥ 13.

**2. The witness that was already in the building.** Certificate 0008 ships a
13-edge τ = 5 object — as the *falsifier* of (D2) one rung below the floor.
Nobody asked it any other question. Its part 1 is (4,3,2,2,2): a **full
part**, every active vertex of degree ≥ 2. So the same object is: the g(5) ≤
13 witness, the N(5) ≤ 13 witness, and the **YES answer to Q13** — the open
question certificate 0005 posed and PLAN item 5 priced at a 232-slice search
(44 min on 3 cores unfinished). The search was for an object the repo already
shipped. With N(5) ≥ g(5) = 13: **N(5) = 13 exactly**, and the rung can never
be raised — the 'Q13 NO ⟹ N(5) ≥ 14' lever is not open, it is dead.

## What moves and what does not

- The **floor does not move**: m ≥ 22 stands exactly as certificate 0008 left
  it. What changes is what stands under it: the citation-free ladder rises
  from N(5) = 11 to N(5) = 13 and **equals** the cited ladder, so every
  cited-ladder sweep in certificates 0006–0008 is citation-free as of today
  (m = 21: 43,875 admissible / 567 cap-passers / 0 survivors — the (L8)
  surface at the last live rung shrinks 4.4× from the 2,478 the weak ladder
  carried).
- The k = 1 degree cap on a counterexample tightens to **Δ ≤ m − 13**.
- Measured beforehand (turn 9 sensitivity, two independent implementations):
  at m = 22 the rise from 11 to 13 cuts the admissible field 3.13× and (L8)
  survivors 1.86× (56,592 → 30,436) — it thins, it does not kill. Nobody
  should read this certificate as progress on m = 22.

## Completeness, margins, controls

- The **forcing has margin one**: the runner-up profile scores 10, and each
  of the four (L1) caps is individually load-bearing (drop any one and the
  maximum rises to ≥ 12; checks 17–21). Weakening g(3) to 4 admits
  (4,4,1,1,1,1) at 12 pairs and the whole route fails — the ladder inputs
  are consumed, not decorative.
- The partition enumerator is validated against the closed form
  12!/(4!·3!·2!·2!·1!)/2! = 415,800 (check 23); the exact-cover census
  visits each unordered completion exactly once (the branching pair is a
  function of the covered set); the first 100 designs are re-verified
  independently (shapes, exact tiling); every 4-cover claimed is verified as
  a cover.
- **Not too strong**: at m = 13 the same counting leaves slack (90 ≥ 78) and
  the witness lives there; the argument cannot kill 13 (check on the maxima),
  which is exactly right.
- 11,520 = 1152 × 10 — the stabiliser of the pinned partition times ten —
  stated as arithmetic context; **no isomorphism claim is made or needed**.
- Independent reproduction: the same census (11,520 / zero τ ≥ 5) was
  reproduced blind this turn by two subagents working from a spec, one by
  design-enumeration (415,800 control included), one by a column-by-column
  route with a τ-prune cut proving the emptiness claim without a full census.

## The dependency picture after this certificate

Everything below m = 21 now runs through: lemmas (A), (B), (C) + the pair
count + **N(4) = 9** (certificate 0010's theorem, plus two searches) +
**N(5) = 13** (this certificate) + (D2). (L8) is consulted at exactly one
rung, m = 21, now on the 567-configuration cited-equals-free set. The
external-input ledger for the entire floor remains **empty**.

## Reproduce

```bash
python3 verify.py
```

Deterministic. The heavy step is the exact-cover census.
