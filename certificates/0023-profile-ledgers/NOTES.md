# 0023 — profile ledgers and the parity sieve: X ≥ 8 everywhere

**Theorems.** (T-A23) The X = 7 layer is empty at every m — **X ≥ 8 for
every critical core in the window**. (T-B23) Staircase: X ≥ 8 on [22, 28] ·
X ≥ 9 at 29 · X ≥ 10 from 30. **The live minimum-excess frontier is X = 8
on m ∈ [22, 28].** An entire excess layer cleared in one certificate.

37 checks, green under bare `/usr/bin/python3` 3.9.6 **and** `python3 -O`.
External-input ledger: **empty**. Billed in-chain: 0005, 0008 (both (D2)
readings), 0017 ((C3), here at c = 5), 0020 ((SSC+)), 0021 ((SJ)/(LD)/(KC)/
(RG), T-B21), 0022 (T-A22, T-B22, the corrected triangle optimizer).

## Provenance

**In-house, desk turn 19.** No peer text was received this turn. 0022 left
(7,24) as "a wall counting alone cannot breach" — the moment/knapsack engine
ties Λ exactly there. The desk worked the tie, found everything at it
FORCED, and the forcing collapsed to two new instruments:

- **(P2) the parity sieve.** At the tie the census pins n₂ = 12 = m/2, so
  (D2) puts exactly one degree-2 cell on every edge; a plain (x = 0) edge
  through the forced degree-10 cell must then fill 17 from four {3,5}
  cells — four odds summing odd. No such edge; five are required. The apex
  variant dies first by (S5) arithmetic (two {3,5} cells summing 7). The
  zero-margin wall falls to a *different invariant*, not a sharper count.
- **(LG) the incidence ledger.** Every low cell of degree d lies in d
  edges, so over all m edges the chosen per-edge degree profiles must hit
  2n₂/3n₃/4n₄/5n₅ exactly. The forced K4 configurations of (2,1⁵) and
  (1⁷) hand each census row a small exhaustive feasibility instance —
  **every one is infeasible**. Highlights: at m = 22 the x = 3 support
  profile does not exist (sum 10 < 11 minimum — one unit); at m = 23 the
  2-count strands the rows the 3-count spares.

Adversarial coverage before certification: three hostile refuter lanes
(the (7,24) parity chain; the profile-exhaustion kills; a sixth-audit
simulation of the whole repo) and one blind computational sweep, all Opus,
launched on the desk derivation. Outcomes recorded below at reconcile.

## Reconciliation — four adversarial lanes, outcomes in full

- **Parity refuter (the (7,24) chain):** every desk step CONFIRMED; found
  the **pigeonhole shortening** (adopted as the primary gate); named the
  tie's single-pillar structure ((SJ) slack, (RG) alone holds 62 — without
  it the branch reaches 83) and the shared-fragility fact (gap ≥ 3 breaks
  every gate at once). Both now stated in-cert (CK_PILLAR).
- **Audit simulation (the whole repo, as the sixth audit will read it):**
  caught the draft's missing (1⁷) multiset family — **(10,8,8) on
  μ = {3,3,1}** — now generated, host-tested, and killed in §5b; caught
  the front-page 5172/5173 drift (fixed, README + 0020 NOTES, dated);
  caught three 0022 prose defects (erratum filed there); confirmed every
  numerical probe P1–P12 it ran.
- **Profile refuter (the ledger kills):** shipped file CONFIRMED
  structurally sound — three defects it found live in the desk's informal
  narrative and are *sidestepped by the ledger's incidence counting*
  (shared ordinary cells double-count correctly as incidences); one cert
  prose overclaim repaired (the (2,1⁵)-(10,9) branch admits J = 7; the
  sub-branch is now enumerated in CK_215 and dies on the same
  non-triangular count). **And it found (PC) — see below.**
- **Blind computational sweep (arrived post-ship; reconciled 2026-08-03):**
  every raw sieve row, census table, and profile enumeration MATCHES this
  file exactly (626 (m, shape, D) cells; the (4,3)@22 survivor and its
  unique census; the sum ≤ 10 emptiness; the rigid (2,3,3,3) at 11).  Its
  independent (2,1⁵) K4-forcing derivation matches 0022/0023's.  Two
  discrepancy classes, both adjudicated at the desk:
  (1) its "(2,1⁵) SURVIVES" rows are SUPPORT-STAGE verdicts (its stated
  scope) — the full-edge incidence ledger closes each, and the profile
  refuter's independent exhaustive check confirmed those exact rows dead;
  (2) its claim that (1⁷)-(10,10)@24 reopens via a k = 3 link is REFUTED:
  two degree-10 cells need s ≥ 6 each, 12 total against the all-ones
  pair-budget of 7 — impossible without a shared link pair, which IS the
  K4 (in its own k = 3 configurations the second cell caps at s = 4,
  d ≤ 8: the (10,8,8) family §5b kills).  Its lasting contributions,
  BANKED: **(RG2)**, the supply/demand sieve — Σ_{cell pairs} C(k_ab, 2)
  = Σ_{parts} C(q+1, 2) =: SUPPLY, against DEMAND from (RG) at |U| = 2
  (k_ab ≥ d(a) + d(b) − m + 7) — desk-re-derived, validated against
  0021's X = 6 table, kills every two-degree-10 multiset at m = 22 in one
  line; and the parity SCOPE law (at maximal n₂ with n = 36, n₄ = Ψ − Λ,
  so the sieve bites exactly on zero-margin rows).  Neither is consumed
  by this file.

## (PC), banked — the part-collision law (NOT consumed by this file)

The profile refuter, working the K4 structures, produced a three-line
lemma the desk has re-derived and verified: for a cell u in part i,

    s(u) = Σ_{pairs e,f ∈ E(u)} (|e∩f| − 1) = Σ_{j≠i} #(pairs of E(u)
    agreeing in part j) ≥ Σ_{j≠i} Φ(d(u), n_j),  and  s(u) ≤ X.

At n = 36 every part has exactly six cells, so **X ≤ 9 forces every degree
≤ 7** (a degree-8 cell needs s ≥ 5·Φ(8,6) = 10). The lane swept X = 7 with
only raw + (KC) + (PC): zero survivors at every rung, ceilings 40–48
against Λ ≥ 59 — every configuration this certificate kills would be
vacuous under (PC). Per Certificate Law the lemma is **banked, not
consumed**: this file's proofs stand on certified inputs only; (PC) is
desk-re-derived but not yet certified or mutation-priced. It opens the
next certificate, where it guts the X = 8 campaign (d ≤ 7 caps persist
through X ≤ 9; the lane measured m = 27, 28 dying outright and 22
partitions cutting to 5).

## The proof surface, compact

| layer | kills |
| --- | --- |
| raw sieve (×3 rungs) | 8 partitions at 23/24, 7 at 22 ((4,3) survives raw at 22 alone) |
| m-independent walls | (4,3) J≥29 · (3,3,1) J≥21 · (3,2,2) J≥16 **rebuilt c=5-clean** · (2,2,2,1)-nontriangle s-hosting → both tops in every support edge → C(4,2) > 4 · (2,2,1,1,1) → C(r,2) = 5 / μ = 2 walls · (2,1⁵)-(10,9,6) → 5-pairs wall · (1⁷) capacity |
| the triangle | dead raw at 22/23 (54/59); at 24: unique tie → census → apex (S5) → **(P2)** |
| the K4 ledgers | (2,1⁵) + (1⁷), all rungs, all rows, **all seven** seventh-pair postures — infeasible throughout |

## Margins

- The (7,24) triangle dies at **zero numeric slack through three gates**
  (optimizer tie 62 = Λ; census unique; parity). M-P2 names the sieve as
  the sole standing gate — there is no backup count behind it.
- m = 22 ledgers close by **one unit** of profile sum (10 vs 11 minimum).
- M-RG (residual pairing 5 → 4): triangle maxima rise 54/59/62 →
  59/62/67 — **all three rungs would reopen**; (RG) is load-bearing
  everywhere here.
- M-D2E ((D2) per-edge withdrawn): the m = 22 instant kill AND the parity
  sieve fall together — (D2) is the single most load-bearing input.
- The 6-partite tiling test (banked turn 18) was measured at the (7,24)
  template: **it tiles** — the tiling does not kill what parity kills.
  Recorded so the lever ledger stays honest.

## What this certificate does **not** claim

- **No core is claimed to exist.** X = 8 on [22, 28] is the new frontier,
  untouched here.
- The X = 8 layer's own structure (partitions of 8, c₃ = ⌊(76−2m)/5⌋)
  is not swept; 0021's T-B21 remains the authority above m = 28.
- The ledger engine proves emptiness only through INFEASIBILITY; a
  feasible ledger would prove nothing (honesty note 3 in the header).

## Run

```
cd certificates/0023-profile-ledgers
python3 verify.py                     # <1 s, exit 0
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 verify.py     # bare 3.9.6
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 -O verify.py  # asserts off
```

Stdlib only. No installs, no venv, no imports from `lib/`, nothing read
from disk.
