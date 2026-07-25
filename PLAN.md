# cofferdam — plan

Revised 2026-07-25 (founding). History is the record; this file is rewritten, not
appended.

## Where we are

Founded and seeded per [BRIEF.md](BRIEF.md): the statement **m ≥ 21**, the problem
setup, and nothing else. The seal (BRIEF §2) is intact — no sealed path has been
read by this repo or by any subagent it has run.

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

1. **Answer the standing audit question (BRIEF §3) — highest priority.** The seal
   lifts only for the diff. Locate the step in the existing chain that does the
   work the Open Lemma was meant to do, and check it on its own terms. Do this
   *after* cert 0001 is committed, which it now is, so this is unblocked.

2. **Fold the cross-part cap into the counting ladder.** (L1) is currently used
   only in its same-part form. The general form couples the six parts, so the
   per-part optimisation becomes a joint one. Target: m = 19, where the slack is
   only 9 and the maximising profile (6,5,3,2,2,1) saturates all five caps at
   once — which forces the degree-6 vertex's complement to be an extremal
   f(6)=13 object, six times over. Cheap to attempt, high information either way.

3. **Squeeze the linearity vice at m = 19.** Slack 9 means at most 9 units of
   repeated agreement across 171 pairs, so the object is forced nearly linear;
   Francetić–Herke–McKay–Wanless forbid it from being linear. Quantify how far
   from linear a counterexample must be and compare against the slack.

4. **Pin g(5) exactly.** Derived ≥ 12, published value 13. Deciding m = 12 at
   τ ≥ 5 by the column engine would make the m ≥ 19 floor fully self-contained.
   Pre-register before running: partition count and a measured cost estimate
   first, budget and kill criterion written down, per the No-Noise Law.

5. **Only then, m = 20.** Not before 2–4 have been tried; the counting slack there
   is 26 and growing, so the method that reached 19 will not reach 21 by
   tightening. A different idea is required, which is exactly what the audit in
   step 1 is looking for in the existing chain.

## Standing

- Every certificate names its external dependencies and states the floor it would
  still reach without them.
- No solver in the trust chain. τ ≤ 5 ships as an explicit five-vertex cover.
- Do not seed searches from truncated PG(2,5) — rigid, and τ breaks before it
  rises. Seed from the sparse side; f(6)=13 shows τ=5 is reachable far below 25.
- Guesses about g-values are to be computed, not inferred from the shape of the
  expected answer. Two were wrong at founding, and both errors pointed *toward*
  the number under verification.
