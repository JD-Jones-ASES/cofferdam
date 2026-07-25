# 2026-07-25 · founding — the degree-cap ladder

Append-only. Technical. Failure is recorded as failure.

## 0. Seal check

Founded under the blind-verification protocol (BRIEF §2). No sealed path read by
this repo, by any subagent, or by the quarry dead-region sweep, which was
explicitly contained to `~/Documents/repos/quarry` with web access forbidden. The
seed was the statement m ≥ 21 and the problem setup.

## 1. Setup

H is 6-partite 6-uniform intersecting; edges are length-6 words over per-part
alphabets, pairwise agreeing in at least one coordinate; a vertex is a
(part, symbol) pair; τ is the least number of vertices meeting every edge. Any
single edge is a cover, so τ ≤ 6 and a counterexample has τ exactly 6.

g(t) := least edge count of such an H with τ ≥ t. The minimum counterexample size
**is** g(6). This reframing is the whole reason the ladder exists: it turns one
hard question into a recursion in t, and the small values of t are computable.

## 2. The two lemmas

(L1) cap: for any k < t vertices S, the edges avoiding S have τ ≥ t−k, hence
number ≥ g(t−k). Same-part S ⟹ disjoint stars ⟹ prefix caps on the sorted degree
profile. (L2) pair count: Σ_parts Σ_v C(deg v, 2) ≥ C(m,2).

Both are one-liners. The content is that (L1) makes the recursion, and that the
small g values are cheap enough to compute exactly.

## 3. What was computed

Two engines, both stdlib, both exact.

*Edge-wise* (`lib/ryser.py`): build by edges, dedupe by canonical form (lex-least
flattening over all part orders and edge orders, symbols renamed by first
appearance). Calibration: reproduced f(3)=3, and settled **Ryser at r=3** —
exhaustive generation to m=10 found zero τ≥3 classes in 26 s, and a τ-critical
family with τ=t has at most C(t+r−1, r) = C(5,3) = 10 edges.

Honesty on that last step, per the cited-input discipline: what is derived *here*
is the reduction — for each edge e_i of a τ-critical family there is a
(τ−1)-cover C_i of H−e_i with C_i ∩ e_i = ∅ (else τ would drop), and C_i meets
every e_j with j ≠ i, so the pairs (e_i, C_i) form a cross-intersecting set-pair
system with |e_i| = r, |C_i| = τ−1. The bound |E| ≤ C(r+τ−1, r) on such a system
is **Bollobás's set-pair inequality**, cited, not proved here. So r=3 is settled
modulo that citation. It is a calibration of the machinery, not a result of this
lab, and nothing in cert 0001 depends on it. Class counts 3, 8, 25, 64, 193, 550, 1714, 263, 0 at m=2..10.
Too slow at r=6: 187 s to reach m=5.

*Column-wise* (`lib/columns.py`): H as 6 partitions of the edge set. Block =
vertex, block size = degree, intersecting = the partitions jointly cover all
C(m,2) pairs, τ = least number of blocks covering [m]. Branch on the least
uncovered pair. Prunes: cap ladder on block profiles; τ monotone non-increasing in
columns fixed so far; cross-part union bound at k=2; waste budget on duplicated
pair-coverings. Milliseconds where the edge-wise engine took minutes.

Results, each proven in both directions:

| | value | witness | exhaustion |
| --- | --- | --- | --- |
| g(2) | 3 | explicit | m=2 empty |
| g(3) | 5 | K₅ edge-colouring | m=3,4 empty |
| g(4) | 8 | search output, re-verified edge-wise | m=6,7 empty |

The g(3) witness: columns 0–4 realise a proper 5-edge-colouring of K₅ (pair {i,j}
↦ colour i+j mod 5), so each is a matching on the five edges, every pair agrees
exactly once, max degree 2, hence two vertices cover ≤ 4 < 5 edges and τ ≥ 3.
Bounded degree forcing τ from below is the cheapest τ-raising mechanism available.

Ladder from these: g(5) ≥ 12, **g(6) ≥ 18** citing nothing; with f(6)=13 cited,
**g(6) ≥ 19**. Cert 0001, GREEN, 22 checks, 96 s.

## 4. Two wrong guesses, recorded

Before computing, this lab guessed g(3)=6 and g(4)=9, reasoning from the valid
embedding g₆(t) ≤ f(t+1). Upper bounds only; both loose. The truth is 5 and 8.

With the guessed values the ladder returns **20**. That is one rung below the
claim under verification and would have been reported as a near-total independent
confirmation of it. The error flattered the expected answer, which is the most
dangerous direction for a verifier's error to point. Recorded as D-005.

## 5. Cost data

- edge-wise r=6: 187 s to m=5. Not viable past that without better canonicalisation.
- g(4) at m=8, 2220 admissible partitions: **576 s** with cap + τ prunes; **88 s**
  after adding the cross-part union prune. Same witness both times — an accidental
  but welcome soundness check on the prune.
- cert 0001 end to end: 96 s, dominated by the m=7 τ≥4 exhaustion.

## 6. Where it stops

Slack (= 6·max-per-part − C(m,2), which equals the total permitted excess
X = Σ_pairs (λ−1)): m=18 → −3 dead; m=19 → +9; m=20 → +26. The method dies at 19
and the slack grows fast, so no tightening of constants reaches 21.

The maximiser at m=19 is (6,5,3,2,2,1), saturating all five caps at once — so the
degree-6 vertex's 13-edge complement must be an *extremal* f(6)=13 object, in
every part. Combined with slack 9 forcing near-linearity, against FHMW forbidding
actual linearity, that is a vice worth closing. Not attempted this turn.

## 7. Verdict against the seed

Independently reached m ≥ 19. Corroborates the exclusion of m ≤ 18 by machinery
the existing chain does not share. Does **not** confirm m = 19 or m = 20 — the
entire unverified remainder of the claim m ≥ 21, and m = 20 is where the
predecessor residual was left undecided.
