# cofferdam — plan

Revised 2026-07-25 (founding). History is the record; this file is rewritten, not
appended.

## Where we are

Founded and seeded per [BRIEF.md](BRIEF.md): the statement **m ≥ 21**, the problem
setup, and nothing else. The seal (BRIEF §2) is intact — no sealed path has been
read by this repo or by any subagent it has run.

**Cert 0003 GREEN (12 checks):** the low-incidence bound (L5). Deficiency
Δ−deg summed over an edge is ≤ B = 6Δ−(m+5) by (L4), so no edge has more than
⌊B/θ⌋ parts of deficiency ≥ θ, giving Σ_i L_i(θ) ≤ m⌊B/θ⌋. At m=20, Δ=5 the
budget is 5: at most 20 low incidences available against 28 required.
**m = 20, Δ = 5 is dead** (primal and dual DPs agree). m=20 is now Δ ∈ {6,7}.

**Cert 0002 GREEN (23 checks):** the maximum-degree window. The per-edge
pigeonhole (L4) — Σ_{v∈E} deg(v) ≥ m+5, of which cert 0001's (L2) is exactly the
average — gives Δ ≥ 1+⌈(m−1)/6⌉ against Δ ≤ m−13. Re-running the pair count per Δ
collapses **m = 19 to the single case Δ = 6**, where the degree-6 vertex's
complement is an f(6)-extremal 13-edge object. Δ=4 there dies twice over, the
second time by parity. m = 20 keeps Δ ∈ {5,6,7}, the Δ=5 case on a slack of 2.
The floor is unchanged — this is a reduction, not an improvement.

**Cert 0001 GREEN (22 checks):** the degree-cap ladder. A Ryser r=6 intersecting
counterexample has **m ≥ 18** citing nothing, and **m ≥ 19** citing the single
published constant f(6)=13. Exact values g(1)=1, g(2)=3, g(3)=5, g(4)=8 each
proven twice over — explicit witness plus exhaustive absence — and g(5) ≥ 12
derived.

**Against the claim under verification:** every rung up to the exclusion of m ≤ 18
is now independently corroborated by a route sharing no machinery with the
existing chain. The rungs m = 19 and m = 20 are **not** confirmed here. That is
the whole unverified remainder, and it is worth noting that m = 20 is precisely
where quarry's predecessor residual (179 classes at R ≥ 8) was left undecided,
and that quarry's own record flagged the deep clean-room of that residual chain as
never performed.

## Machinery

`lib/ryser.py` — edge-wise: canonical form, exact τ by depth-bounded branching,
isomorph-free layer generation. Validated: reproduces **f(3)=3**, and settles
Ryser at r=3 (zero τ≥3 classes on ≤10 edges, 26 s) **modulo the cited Bollobás
set-pair inequality**, which caps a τ-critical family at C(τ+r−1, r) = 10 edges —
the reduction to a set-pair system is ours, the inequality is not. Calibration
only; cert 0001 does not depend on it. Slow at r=6 — ~3 min by m=5.

`lib/columns.py` — column-wise: r partitions of the edge set. Prunes by the cap
ladder, by τ-monotonicity in the columns fixed so far, by the cross-part union
bound at k=2, and by a waste budget on duplicated pair-coverings. This is the
engine that settled g(4).

Cost data, measured: g(4) at m=8 took **576 s** with cap + τ prunes, **88 s** once
the cross-part union prune was added; both runs returned the same witness.

## Next, in order

1. **Lazy partition generation in `columns.py`** — the single change that opens
   m = 19. Attack (13,5) *directly* rather than bottom-up: there Δ = 4 exactly
   (proved — the Δ=5 branch is empty), the caps are {1:4, 2:8, 3:10, 4:12}, the
   best per-part profile (4,4,2,2,1) gives 84 pair-coverings against the 78
   required, so the **waste budget is 6** — the tightest constraint in the lab and
   exactly the regime the column engine exploits. It currently materialises the
   admissible partition list before searching (fine at m=8's 2220, hopeless at
   m=13's millions); generate them lazily, indexed by the pair they must join.

   *Why not bottom-up:* measured. One 5-edge residual at Δ=4 yields **6457
   classes in 142 s** — the search terminates fine; the level is simply enormous.
   Twelve residuals feed the Δ=4 branch and 53,906 feed the Δ=3 branch, putting
   (9,4) at perhaps 10⁵–10⁶ classes, all of which the next pass would sweep. The
   intermediate level is far larger than the target: (13,5) is *extremal*, so it
   is small, while (9,4) sits in the loose middle where objects proliferate.

2. **Old item, superseded:** column-wise star attachment — the one engineering blocker.** `peel.py`
   attaches stars by assigning symbols, allowing up to Δ fresh labels per part
   with no canonical ordering, so isomorphic stars are generated repeatedly and
   deduped afterwards. What actually matters in part q is only the *partition* the
   star induces on its Δ edges, and whether each class takes an old symbol or a
   new one. Enumerate those partitions instead and the redundancy vanishes at
   source. Everything below is gated on this.

2. **Close m = 19.** One case (cert 0002): Δ = 6, residual an f(6)-extremal
   13-edge object R. Sharpened to a finite question — each star edge restricts to
   a *minimum cover of R*, and τ(H) ≥ 6 iff every minimum cover of R is disjoint
   from one of the six. So: does some extremal R admit six of its own minimum
   covers, rainbow across one common five parts, dominating all its minimum covers
   by disjointness? Cheap per R; the cost is producing R. ABW caveat: f(6) is
   *not* achieved only by linear hypergraphs, so linearity may not be assumed.

3. **m = 20, Δ ∈ {6,7}.** Δ=5 is closed by cert 0003. The remaining two have
   slack 20 and 26, so counting will not do it — they need the same structural
   route as m=19 (residual 14 and 13 edges respectively; the Δ=7 residual is again
   f(6)-extremal, so it reuses whatever (2) builds).

4. **Squeeze the linearity vice.** Slack bounds the total excess
   X = Σ_pairs(λ−1), so a counterexample is forced nearly linear, while
   Francetić–Herke–McKay–Wanless forbid it from being linear outright. Quantify
   the minimum non-linearity and compare against the slack.

5. **The standing audit question (BRIEF §3).** Unblocked since cert 0001 was
   committed, and gated only on JD's seal ruling. Note that the localisation has
   improved since that ruling was framed: the unverified remainder is now m = 19
   in one case, plus m = 20 in three.

6. **Pin g(5) exactly** (derived ≥ 12, published 13) to make the floor fully
   self-contained. Pre-register cost first, per the No-Noise Law.

## Standing

- Every certificate names its external dependencies and states the floor it would
  still reach without them.
- No solver in the trust chain. τ ≤ 5 ships as an explicit five-vertex cover.
- Do not seed searches from truncated PG(2,5) — rigid, and τ breaks before it
  rises. Seed from the sparse side; f(6)=13 shows τ=5 is reachable far below 25.
- Guesses about g-values are to be computed, not inferred from the shape of the
  expected answer. Two were wrong at founding, and both errors pointed *toward*
  the number under verification.
