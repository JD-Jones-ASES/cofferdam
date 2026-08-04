# 2026-08-03 — turn 20: the sixth audit, part-collision certified, X ≥ 10

Peer text: GPT 5.6 Sol Pro ("Ryser-5"), retained verbatim at
`notebook/raw/2026-08-03-received-turn20-gpt-pro-ryser-5.md` before anything
else happened (D-036). Contents: an audit of 0023 (agrees; four minor
defects) and a proposal — the global part-collision law, an exact
degree/part sweep, X ≥ 10 everywhere, X = 10 ⟹ m ≤ 25.

## Intake, by the law

Three hostile refuters (verbatim text) + two blind lanes (statements only),
all Opus, plus full desk re-derivation before any enactment.

- **Desk:** all four 0023 defect claims verified against source and
  repaired same-day. (GPC) re-derived in three lines; (DM), Σs = R,
  (KC)-for-every-vertex, all ten Λ values, partition counts 11/15/18/23,
  the 407,253 cell count, the tail knapsack max 179 — all by hand before
  any lane returned. **Desk find:** the peer's §7.2/§9.2 "edge-disjoint"
  claim is FALSE as written — the (4,3,2)/(4,3,3) support triangles are
  set-realizable; the kill is T-confinement + (PC), not the union bound.
- **R3:** every sweep table reproduced by an independent engine; §5's
  attribution of the X = 7 kill to (GPC) REFUTED (pointwise (PC) does it
  alone — in-house, banked turn 19); the same posture gap found
  independently + (4,3,2,1) at m = 26; **the audit's §2.2 mechanism
  REFUTED — 0023's parity gate is APEX-FREE** (the desk's first repair
  had over-retracted on the audit's faulty reasoning; re-corrected, both
  versions dated); a new 0023 typo (deg-6 residual 21, not 13).
- **R2:** four engine variants, exhaustive A/B and A/D cross-checks at
  X = 7/8 (0 mismatches), explicit witnesses for the positive controls;
  every Λ, knapsack constant, incidence total confirmed; an exhaustive
  support-realizability audit (k ≤ 6) with explicit 3-edge witness for
  the (4,3,2) triangle (min J = 23, the union bound genuinely fails);
  **found the second repair route: (C3) from 0017 kills every q4+q3
  adjacency** (x_e ≥ 7 > c₃). Its side remark of 15 X = 10 cells at
  m = 22 did not reproduce (three engines + blind: 10) — outside its
  audited scope, recorded here.
- **B1 (blind):** proved (PC)/(GPC) from the bare statement over an
  exact identity; ~8.7M checks, equality attained both ends; hypothesis
  inventory (intersecting-ness load-bearing ONLY for s ≤ X, witness);
  harness-sensitivity controls. Banked design laws: the codegree
  identity outranks (PC); **(PC)/(SJ) are incomparable — never add**.
- **B2 (blind):** independent exact sweep, three procedures, zero
  mismatches over 97,214 DP-decided cells; **tables identical to the
  desk's cell-for-cell** (X=7: 0 of 49,368; X=8: 8; X=9: 23; X=10: 96
  over [22,33], none above 28, m = 33 anchor zero row); explicit
  re-verified degree witness for every one of the 127 survivors.
- **R1 (lemma refuter):** died on an API error mid-run (connection
  closed; 9 tool calls, no report) and was NOT re-run — its assigned
  scope, hostile refutation of the lemma and the §4 constraint
  equivalences, was already covered four independent ways (desk; B1's
  blind proof; R2 §8; R3 A2) plus 0024's own corpus enactments.
  Recorded so the lane count stays honest: five launched, four
  returned.

## Shipped

- **0023 erratum, twice-corrected** (commits 0888b6d, b0f27eb): four
  audit finds + one desk find (37→39) + one lane find (21, not 13);
  checker strengthened (`len(H_1010) == 1`, exact hosting). The first
  "three ways" repair over-retracted on the audit's faulty mechanism;
  the refuter lane restored parity's independence, desk re-derived
  (excess edges ≤ 5 in either posture; T-meeting posture-free; census
  pins upstream). Honest form: TWO complete independent proofs.
- **Cert 0024 — part-collision** (587238a): (L-PC24)/(L-GPC24) above
  the exact codegree identity; **(T-A24) X ≠ 7 independently — X ≥ 8
  everywhere now on TWO disjoint stacks** (0021→0023 | 0021→0024);
  **(T-B24) X = 10 ⟹ m ≤ 28** + the survivor atlases (8/23/22 cells,
  + 74 low-rung X = 10 cells as the next campaign's certified list).
  25 checks + 9 mutations, green ×2, 1,286,681 cells × two engines
  behind a priced prefilter (~7 min). Mutation highlights: M-D2R and
  M-KC are NULLS at the floor and load-bearing in the tail — the two
  stacks have honestly different dependency profiles.
- **Cert 0025 — support postures**: postures from graphs, not prose
  (the cure for the three-audits-running posture-gap failure mode).
  Canonical-growth enumeration → closure → derived pairwise caps →
  kills C3 (0017) / J-budget / capacity-ILP with the triangle-
  coincidence law. **(T-A25) X ≥ 10 everywhere; (T-B25) X = 10 ⟹
  m ≤ 25.** The audit's missed triangles are generated and killed by
  law; M-CAPS/M-PCCAP pin the load-bearing spine (the posture caps and
  0024's (PC)); C3/J/coincidence measured as belts. Green ×2.

## The lessons

- **Verify the deflation like the claim — it happened to us, inward.**
  The audit correctly caught an overclaim, mis-diagnosed the mechanism,
  and the desk's first repair imported the mis-diagnosis into three
  files. A refuter lane caught it in-session. D-036 clause appended.
- **The posture gap is cured by generation, not vigilance.** Sixth
  audit, third instance of the same failure shape. 0025's enumeration
  is the standing fix; its class counts are the completeness anchor.
- Peer's arXiv citation (2505.05339, Clow–Haxell–Mohar) verified
  firsthand: Ryser open for all r ≥ 4 as of May 2025 — the neighborhood
  citation for the novelty ledger.
