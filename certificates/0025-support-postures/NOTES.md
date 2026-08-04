# 0025 — support postures: X ≥ 10 everywhere; X = 10 ⟹ m ≤ 25

**Theorems.** (T-A25) **X ≥ 10 for every critical core in [22, 456]** —
chain 0021 → 0024 → 0025: the X = 8 and X = 9 atlases are 0024's only
surviving cells and every one is posture-impossible here. (T-B25)
**X = 10 ⟹ m ≤ 25**: the 22 high-rung atlas cells at m = 26/27/28 all
die. **The live minimum-excess frontier is X = 10 on m ∈ [22, 25]** —
0024's 74-cell low-rung atlas is the entire next campaign.

9 checks + 5 priced mutations, green under bare `/usr/bin/python3` 3.9.6
**and** `python3 -O` (~4.5 min). External inputs: 0024 (atlases, (PC),
the moment floor), 0021 ((SJ)/(LD)/(KC)), 0017 ((C3)), 0005/0008
inherited, 0013/0014. No peer text cited (D-036).

## The method — generation, not narration

Three audits in a row lost a support posture to prose (third: one
partition of three; fifth: adjacent-apex; sixth: "edge-disjoint" asserted
where the (4,3,2)/(4,3,3)/(4,3,2,1) triangles are realizable — refuted at
the desk and by two hostile lanes independently, one with an explicit
3-edge witness and an exhaustive k ≤ 6 realizability audit). The cure:
**postures are enumerated as simple graphs with labeled edges**
(canonical growth, signature-deduped to iso-classes, counts asserted —
the completeness anchor), **closed** under forced cross-excesses, and
killed by the first law that reaches them: (C3) edge-load, J-budget
knapsack, or the capacity ILP over membership patterns with the
triangle-coincidence law. The audit's missed triangles are *generated*
here and die by law — pinned forever in check 3.

## Kill profile and mutation story

Baseline tally over the 53 atlas cells (C3/BUD/CAP posture-kills):
X = 8: 1/11/0 · X = 9: 52/124/20 · X = 10: 259/166/245.

- **M-C3, M-J — two measured BELTS**: every atlas cell still dies with
  (C3) withdrawn and with the J-credit zeroed. The redundancy is real
  and now priced, not presumed.
- **M-COIN — SPINE, and a same-day correction**: a full-atlas
  measurement (5,424 s) showed the triangle-coincidence law carries
  three cells — (9,24,(3,3,3),6⁵7) and two X = 10 cells REOPEN without
  it. An earlier draft scoped the mutation to six 6⁶ rows and called
  the law a belt; wrong, caught by the measurement before push settled,
  repaired in-cert with the three flips pinned. (Belt-vs-spine
  misclassification flatters the chain — same failure family as the
  audit's attribution error, now measured instead of narrated.)
- **M-CAPS — the load-bearing spine, part 2**: posture-blind caps
  (min(q)+1 everywhere) REOPEN (10,26,(3,3,2,1,1),6⁶) — the capacity
  ILP reaches 84 ≥ 79 and the budget dies with it. The derived posture
  caps ARE the proof.
- **M-PCCAP — the load-bearing spine, part 3**: without 0024's (PC)
  degree cap, (9,23,(3,3,3),6⁶) REOPENS (the triangle's T carries
  d ≤ 10 under (KC) alone: 140 ≥ 65; (PC)'s d ≤ 7 closes it at 32).
  The peer's own §7.2 gap had the same shape: its union-bound "kill"
  of (4,3,2) needed exactly this cap and never invoked it.

## Provenance

Desk turn 20. The posture-generation design and the two kill engines are
desk-derived; the (C3) repair route was found by refuter lane R2 and
desk-verified against 0017's exact statement; the greedy-J soundness
argument, the pattern-ILP exactness argument, and the coincidence law
(S_a ∩ S_b = e∩f∩g ⊆ S_c) were desk-derived before enactment. A hostile
lane's exhaustive realizability audit (min J = 36/23/27/23/20/23 for the
six contested shapes) brackets this file's greedy bounds from above, in
the sound direction.

## What this certificate does **not** claim

- Nothing about m ∈ [22, 25] at X = 10: those 74 cells are ALIVE and are
  the next campaign.
- No posture is claimed realizable — kills are one-directional.
- The class counts assert completeness of the *enumeration*, not of
  nature: the completeness argument is that t pairs span ≤ 2t core-edges
  and distinct pairs cannot share two core-edges (header, note 2).

## Run

```
cd certificates/0025-support-postures
python3 verify.py                     # ~4.5 min, exit 0
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 verify.py     # bare 3.9.6
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 -O verify.py  # asserts off
```

Stdlib only. No installs, no venv, no imports from `lib/`, nothing read
from disk.
