# 0022 — shared-set quotients: X = 7 ⟹ m ≤ 24

**Theorems.** (T-A22) X = 7 ⟹ m ≤ 24 — equivalently m ≥ 25 ⟹ X ≥ 8.
(T-B22) The staircase, squared off: X ≥ 7 on [22, 24] · X ≥ 8 on [25, 28] ·
X ≥ 9 at 29 · X ≥ 10 from 30. The live minimum-excess frontier shrinks from
five edge counts to three: **X = 7 on m ∈ {22, 23, 24}**.

64 checks, green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O`.
External-input ledger: **empty**. Billed in-chain: 0005 (min degree ≥ 2),
0008 ((D2), both readings), 0017 ((C3)), 0020 ((SSC+)), 0021 ((SJ)/(LD)/(KC)/
(RG), T-A21, T-B21). Standalone reading without 0021's theorems: "(7,25) and
(7,26) are empty," full stop.

## Provenance (D-036)

The theorem, the blueprint, and the 0021 tri_max defect were proposed by the
**fifth outside audit** (GPT 5.6 Sol Pro, 2026-08-01, reading the public
repo). Received text retained verbatim at
`notebook/raw/2026-08-03-received-turn18-gpt-pro-ryser-4.md`; three hostile
refuter lanes got the file verbatim; blind lanes got statements only; every
consumed step desk-re-derived before entering this file. No step cites the
audit. The audit found **zero errors** in the lab's certified chain — and
one real, non-load-bearing defect in 0021's triangle prose (erratum filed
there, numbers unchanged).

## The intake, both directions (the running ledger of who caught what)

- **The audit's repair was itself incomplete.** Its lemma |S₄ ∩ U| ≤ 1
  assumes both edges of the q = 1 pair avoid the triangle. The desk found
  the adjacent-apex escape (both S₄ cells in U ∖ T, no fifth pair) by
  pair-count; **all three refuter lanes found the same hole independently**;
  one refuter sharpened it: the apex edge carries x_e = 5 > 4, so **C3 kills
  the pattern at both of this file's rungs** — the audit's lemma is true
  here for a reason its proof never invoked — and c₃ = 5 at m = 24 makes the
  pattern **live exactly at the next campaign's opening wall**. The (0,2)
  branch is carried, measured dominated here (max 54), and the (7,24)
  preview tie (62 = Λ) already includes it.
- **Refuter finds, written into the checks:** the §4.4 implicit step (a cell
  outside A ∪ B in any shared set pushes J to 9) and the honest reason a
  seventh pair touches at most one K₄ support edge (q ≥ 2, not 1).
- **The audit's knapsack claims are correct only under cost F** — its table
  stops at d = 10 and never states F(11) = 7 > 6; under the linear cost the
  decisive (1⁷) wall jumps 73 → 83 and the census kill is never reached.
  0021's M-f trap, still armed; priced here again as M-f.
- **Blind lane (m = 25) proved the full rung independently** — all 15
  partitions, no peer text. Blind sieve lane reproduced every raw table
  (four raw survivors at 26, six at 25, the 60-max for the raw-dead) and
  independently rediscovered the d ≤ 10 ceiling's load-bearing role.

## The shape of the proof

Raw (LD) sieve over all 15 partitions of 7 (generated in-cert, M-SWEEP armed)
→ survivors classified by **quotient structure** (how shared sets overlap,
which overlaps force closing pairs — each completeness claim a finite
enumeration, not an assertion) → J-debits → the exact census when Ψ pins.
The census solver enacts the audit's arithmetic walls as emptiness: at
(26, (10,9,8)) and (26, (10,10,6)) no feasible low-cell profile exists; at
(25, (10,10)) the unique census (12,1,2,19) carries **exactly one degree-3
cell**, against which the (2,1⁵) and (1⁷) kills need two and three disjoint
forced degree-3 cells ((S5) sum-13 four-sets + profile fact + (D2) per-edge).
The (1⁷) (10,10,6) subcase dies **twice** — triangular-multiplicity capacity
(m-independent) and census.

## Margins

| cell | margin |
| --- | --- |
| (2,2,2,1) triangle @ 26 | 74 vs 73 — cleared only by census emptiness |
| (1⁷) |U| = 3 @ 26 | 73 vs 73 — census + capacity, both enacted |
| (2,2,2,1)/(2,2,1,1,1)/(2,1⁵) @ 25 | 70 vs 68 — equality analyses |
| (2,2,2,1) triangle @ 25 | 67 vs 68 — **one unit**, optimizer only |
| (7,24) preview | 62 = 62 — **zero margin**, the next wall |

Ten mutants priced. Load-bearing where it matters: M-D2E (profile fact dies),
M-T5 ((10,10,6) hosts), M-C3 ((3,2,2) reopens), M-f (73 → 83 at THE decisive
cell), M-RG (the (7,25) triangle kill **reopens outright**, 67 → 74), M-n35
(Λ − 15 everywhere). Inert-and-said-so: M-CEN at gap < 14. Completeness
counters: M-TRI-O, M-O2, M-SWEEP.

## What this certificate does **not** claim

- **No core is claimed to exist.**
- **X = 7 on m ∈ [22, 24] is not emptied.** That is the new frontier. Its
  first wall is exact: the (7,24) triangle ties Λ at (10,9,6), census
  (12,5,0,16), with the apex pattern live (c = 5). Counting alone will not
  breach it.
- **The bonus rungs stay banked** (0021's list), and 0020's (Q)/(Q0) remain
  the authority at the far end of the window.

## Run

```
cd certificates/0022-shared-set-quotients
python3 verify.py                     # <1 s, exit 0
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 verify.py     # bare 3.9.6
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 -O verify.py  # asserts off
```

Stdlib only. No installs, no venv, no imports from `lib/`, nothing read from
disk.
