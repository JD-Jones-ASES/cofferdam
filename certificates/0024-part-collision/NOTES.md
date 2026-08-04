# 0024 — part-collision: the laws, the engines, the atlases

**Theorems.** (L-PC24)/(L-GPC24) The part-collision laws: g(u) ≤ s(u) ≤ X
pointwise and Σg ≤ R globally — proved above an **exact identity**
(s(u) = Σ_{j≠i} Σ_y C(c_u(y),2); the law is its balanced relaxation).
(T-A24) **X ≠ 7 → X ≥ 8 everywhere, independently**: the chain is
0021 → 0024 alone — 0022/0023 are NOT consumed, so X ≥ 8 now stands on
**two disjoint proof stacks**. (T-B24) **X = 10 ⟹ m ≤ 28**, with exact
survivor **atlases**: X = 8 (8 cells), X = 9 (23 cells), X = 10 high
(22 cells at m = 26/27/28) + the 74-cell X = 10 low-rung frontier list.

25 checks + 9 priced mutations, green under bare `/usr/bin/python3` 3.9.6
**and** `python3 -O` (~7 min each: 1,286,681 cells × two engines behind a
priced prefilter). External inputs: 0005, 0008, 0021 ((SJ)/(LD)/(KC),
T-A21/T-B21), 0013/0014. **No peer text cited** (D-036).

## Provenance

The pointwise law was found by a turn-19 refuter lane and banked (0023
NOTES §(PC)). The global form, exact sweep, and two-theorem shape were
**proposed by the sixth outside audit** (GPT 5.6 Sol Pro, Ryser-5,
retained in `notebook/raw/`). Per D-036, before any enactment:

- **Desk**: re-derived (GPC) (three lines), (DM), Σs = R, (KC) for every
  vertex, all ten Λ values, partition counts 11/15/18/23, the 407,253
  cell count, and the tail knapsack max 179 — by hand.
- **Blind lane B1**: proved both laws from the bare statement; ~8.7M
  numeric checks with equality attained at both ends; hypothesis
  inventory (intersecting-ness needed ONLY for s ≤ X — explicit
  witness, now enacted in section 2); harness-sensitivity controls
  (adopted as this file's must-fail controls).
- **Refuter R2**: reimplemented the sweep four ways (Pareto DP,
  uncompressed, raw product, DFS-with-witness); exhaustive A/B and A/D
  cross-checks at X = 7/8 with zero mismatches; explicit degree
  witnesses for the three positive controls; every Λ and knapsack
  constant reconfirmed.
- **Refuter R3**: independent engine, tables identical; corroborated
  against 0023's published raw-sieve row.

Three independent engine families agreed cell-for-cell with the desk
table before the atlas assertions here were written. The audit's §5
attribution of the X = 7 kill to (GPC) was **refuted** (R2/R3): the
attribution check + M-PC/M-GPC now measure both directions in-cert —
pointwise (PC) alone empties X = 7; (GPC) bites at X = 9 m = 27 (6
cells) and X = 10 m = 26 (47 vs 15).

## Margins and mutation highlights

- **M-PC**: X = 7 reopens without the pointwise law (witness
  (22,(3,3,1),6⁶)) — the floor stands on (PC).
- **M-D2R / M-KC — both NULL at the floor, load-bearing in the tail**:
  X = 7 stays empty under (D2)+1 and without (KC) (the (PC) cap
  dominates at floor part sizes) — but (D2)'s withdrawal drops
  Λ′₁₀(33) to 122 < 179, and (KC)'s admits degree-17 knapsack items
  (max Ψ → 203 ≥ 182): **either withdrawal kills T-B24's tail**. The
  two proof stacks (0023 | 0024) have honestly different dependency
  profiles: (D2) is 0023's most load-bearing input and this file's
  least, at the floor.
- **M-DOM**: corrupting engine P's frontier to one max state per moment
  value falsely kills 2 of the 8 X = 8 atlas cells — the Pareto rule's
  minimal corner is what survives later caps.
- **M-PRE**: prefilter off on every m ≤ 26 window → identical atlases
  (an optimization with a proof, not a filter with an opinion).
- **M-DM**: witness (22,(4,3),6⁶) — matches 0023's raw-sieve fact that
  (4,3) survives raw at 22; exactness of (DM) is load-bearing.

## What this certificate does **not** claim

- **No atlas cell is claimed realizable.** The atlases are relaxation
  survivors, certified as DATA; 0025 kills them structurally.
- X = 10 low rungs (m ≤ 25, 74 cells) are certified in count and left
  ALIVE — they are the next campaign, not a defect.
- The two-engine agreement is a soundness belt for the DP compression,
  not a proof of the constraint laws (those are sections 1–3).

## Reconcile notes (turn 20)

- The X = 10 low-rung count was mis-asserted 66 in a draft after a
  truncated read of the desk log; the engines said 74 and a fresh
  desk/cert diff agreed (10/17/25/22). A hostile lane's side remark of
  15 at m = 22 did not reproduce (three engine implementations: 10)
  and was outside its audited scope.
- R2's declared-unverified scope: its A/D exhaustive cross-check
  covered X = 7/8 (X = 9 pass unfinished at its write-up); this file's
  own engine-D-vs-P diff covers every cell of every window.

## Run

```
cd certificates/0024-part-collision
python3 verify.py                     # ~7 min, exit 0
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 verify.py     # bare 3.9.6
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 -O verify.py  # asserts off
```

Stdlib only. No installs, no venv, no imports from `lib/`, nothing read
from disk.
