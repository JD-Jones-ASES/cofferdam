# 2026-07-26 · turn 8 — the degree-two cap closes m = 21, and the risk table was wrong

Append-only. Technical. Failure recorded as failure.

## 0. What this turn set out to do

Two things, both named in PLAN.md: **(1)** settle the FHMW 2.1(iii) degree-2
lever and with it m ≥ 22; **(2)** attack **(L7)** and the **excess budget X**,
which PLAN's own risk decomposition called the joint load-bearer and which
PLAN's own attack list did not mention.

Both are done. Item 1 produced certificate 0008. Item 2 produced a correction to
the risk decomposition itself, and a dead end closed.

## 1. The scope error that would have undone certificate 0007

The notebook's original cap table (105 → 0 at m = 20, 43875 → 567 → 0 at m = 21)
was computed **on the cited ladder**, N(5) = 13. It says so, and nobody noticed
what that meant: a floor built on those numbers would have silently re-imported
f(6) = 13 and undone 0007's whole point.

The citation-free run is a different and ~7× larger problem:

| ladder | m | admissible | pass D₂ ≤ ⌊m/2⌋ | survive (L8) |
| --- | --- | --- | --- | --- |
| cited | 21 | 43,875 | 567 | 0 |
| **free** | **21** | **316,591** | **2,478** | **0** |
| free | 22 | 6,499,005 | 307,420 | 56,592 |
| cited | 22 | 2,079,883 | 156,797 | 30,436 |

**m = 21 dies on the weak ladder too.** The floor is m ≥ 22 citing nothing.

The decisive cell was reproduced by a second implementation that read no
`verify.py` anywhere, no `lib/`, and none of the exploratory scripts — working
from the prose derivation in 0006's NOTES. A third reproduced the enumeration by
**full brute force** over all 185,250,786 and 156,238,908 six-multisets at m = 22.

## 2. Two prunes, and why the enumeration stopped being the bottleneck

0007 enumerates by flat `combinations_with_replacement` over all profile
6-multisets. Two exact prunes collapse it — a score bound (the profile list is
sorted by score, so the tail is cuttable) and, for the capped sweep, pushing D₂
into the recursion since a partial D₂ sum only grows:

| m | admissible | flat combos | pruned nodes |
| --- | --- | --- | --- |
| 20 | 7,159 | 3.3M | 8,078 |
| 21 | 316,591 | 20.4M | 341,155 |
| 22 | 6,499,005 | 185.3M | 6,830,764 |
| 23 | 77,063,429 | 988M | 79.9M |
| 24 | 809,106,366 | 7.5B | 830M |

Counts agree exactly with the unpruned enumeration where both were run. With the
D₂ cap in the recursion, m = 21 drops to **4,285 nodes**. Both prunes are checked
against unpruned enumeration inside certificate 0008.

**Consequence for the machine question**: the wall at m ≥ 23 was a missing prune,
not missing cores. Measured leverage on this box, in order: prunes (25–59×) >
PyPy (~10×, not installed) > 8-core `multiprocessing` (~5×) > a rented VM.

## 3. (L8) is load-bearing at exactly one rung

Read 0008's sweep table: at every m from 12 to 20 the number of configurations
**surviving the cap is zero**, so those rungs die on (A)+(B)+(C)+the pair
count+(D2) alone and (L8) is never consulted. Only m = 21 leaves anything.

Both peer audits went after the δ-budget inside (L8). With (D2) in hand that
machinery is load-bearing at one rung. The hinge does not move: m = 20 still
funnels through **N(4) = 9**, still with a margin of one.

## 4. Item 2 — the risk decomposition was wrong, and the real load-bearer is unnamed

PLAN.md and D-019 both said: remove (L7) and 100% of configurations survive at
every m. **False.** Measured firsthand with 0007's own `l8_kills`, one line
changed to zero the floors:

    m = 20 cited     3 of   105 survive  (2.9%)
    m = 20 free   1,616 of 7,159 survive (22.6%)
    m = 19 free       1 of    33 survive  (3.0%)

Five implementations agree, one keeping 0007's loop structure verbatim.

**And the step that carries the other 77.4% is in no table, ledger or label.**
100% reproduces only when **B_min(A)** — the convexity lower bound on
B = Σ C(c_ij,2) given Σ c_ij = A — is zeroed *as well*. With floors and B_min
both zeroed: 105/105 and 7159/7159 survive. Every no-(L7) survivor sits at
exactly D = 0, because D = A − S + m ≥ 0 still forces A ≥ S − m even with (L7)
gone. Recorded as **D-023**.

Also found in the same pass, and each now on the record:

- **N(4) = 8 understates.** m = 19 revives too, so that failure drops the floor
  to 19, not 20.
- **g(4) = 8 carries a margin of exactly one** (weaken to 7 → 649 of 7,159
  survive at m = 20 free) and appears on no attack list.
- **`B ≤ ⌊5X/2⌋` is a second inert step** beside U: it is implied by the level
  budget, and removing it changes nothing anywhere.

## 5. What the attack could NOT break, which is most of the chain

(L2), X's definition, (C2), (C3), B_cap, (C5) in its corrected form, δ(k),
`need`, `qmin` — brute-forced over **1,859,176 audits** on explicit objects, zero
failures, each also run under two deliberately wrong choices of u_j so the
identities are tested as identities rather than as artefacts of the max-degree
choice. The intersecting hypothesis was *priced*: drop it and Σ(t_ef−1)⁺ ≤ X
fails 5,167 times in 39,721 non-intersecting families, with an explicit witness.

And the relaxation property itself — no real object's true point falls outside
any guard — was checked directly: **1,924 instances from real objects with τ
computed rather than assumed, all 16 guards inside `l8_kills` pass**.

(L7)'s own derivation is sound. Worth recording that the direct argument is
cleaner than the one NOTES.md gives: if R = H ∖ (E(u_i) ∪ E(u_j)) had a cover C
with |C| ≤ 3, then C ∪ {u_i, u_j} covers H with size ≤ 5 < 6. No appeal to the
peeling lemma is needed.

## 6. Dead end: the (L7) tightening to N(4) = 9

Recorded as **D-022**. The only ρ = |R| where the +1 changes a floor is ρ = 8,
and there R is g(4)-extremal — where certificate 0005's corrected AKP Lemma 2.8
says every part is (3,2,2,1) or (3,2,1,1,1), each carrying a degree-1 vertex. So
at the only ρ that matters the residual provably has **no** part of minimum
degree 2. Machine-checked: 15 of 15 two-star residuals of W8, 15 of 15 of W9.

The mechanism is the general lesson: lemma (C) works because deleting k vertices
of **one** part never touches that part's survivors' degrees. A **cross-part**
peel destroys exactly that guarantee.

It would not have sufficed anyway — (L7) with g(4) = 9 still leaves 950 survivors
at m = 21 citation-free.

## 7. The positive control that cannot exist, and a bug in `lib/ryser.py`

PLAN owed "a positive control: the bound must hold on objects that exist." **It
cannot be discharged** (D-024): τ(H) = r *is* the counterexample condition, so
the hypothesis class is conjecturally empty, and 0 of 67,463 census objects have
τ = r. My own specification of this control was also wrong — I had conflated the
lab's g(3)=5 and g(4)=8 objects (6-partite, τ = 3 and 4) with "r-partite, τ = r".

Replaced by testing the **construction**, which runs regardless of τ: 248,460
constructed covers in 0008, zero failures, with a mutant failing 3,780 of 3,780
to show the test has teeth.

Separately (D-025): `extension_edges` returns edges **already in H**, since such
an edge trivially meets every edge of H. `generate(3,3,1)` returned
`((0,0,0),(0,0,0))`. Fixed. Extremal counts re-verified unchanged —
`enumerate(5,3) = 12`, `enumerate(8,4) = 5`, both now with zero non-simple
objects — so **N(4) = 9 and the ladder do not move**. Non-extremal censuses do:
`enumerate(6,3)` is 53,871, not 53,906.

## 8. What did not get done

- m = 23 and m = 24 not-too-strong controls: started, killed to free cores. m = 22
  suffices to show the filter stops.
- The memo-key soundness check in 0008 covers m = 20 (all admissible) and m = 21
  (all cap-passing), **not** the full 316,591-configuration m = 21 set.
- Δ = 4 certification: untouched, still PLAN item 1.
- Q13: untouched, and its payoff has fallen again — it reaches m ≥ 21, now two
  rungs below the floor.

## 9. Errors of mine this turn, recorded

1. Claimed all m = 22 survivors saturate the cap, generalising from the first
   five seen. Measured: 159 of 200. Caught by my own certificate.
2. Specified a positive control on objects that cannot satisfy the hypothesis.
3. Hardcoded a "non-intersecting witness" with τ = 2 and one degree-2 vertex,
   which the check caught; it is now searched rather than asserted.
4. Wrote a code comment claiming a full-range memo run had been made; it had been
   killed before finishing. Removed.
5. Left a self-withdrawing `check(..., True, ...)` in a draft — the exact D-015
   pattern — and removed it before the first green run.
