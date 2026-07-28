# Certificate 0018 — the X = 3 layer at the window floor is empty: X ≥ 4 at m = 22

**Status: GREEN.** 33 checks + 10 notes, ~44 s, `python3 verify.py`, stdlib only,
no solver, no imports from `lib/`. Green under a bare `/usr/bin/python3` (3.9.6)
and under `python3 -O`. Deterministic (fixed-seed hand-rolled LCG, seed 20260728).

| claim | label |
| --- | --- |
| the eight-shape census of X = 3 (one λ4 · λ3+λ2 adjacent/disjoint · five 3-edge pair-graphs) is complete | **PROVEN-BY-CERTIFICATE** (X-identity + exhaustive graph classification) |
| shape λ4 forces m ≤ 20; shape λ3+adjacent forces m ≤ 21 | **PROVEN-BY-CERTIFICATE** (channel counts; relation spaces exhausted 144/216) |
| shape λ3+disjoint forces W ≤ 23 (heavy confinement to U ∪ V, \|U ∪ V\| = 5 < 7) | **PROVEN-BY-CERTIFICATE** |
| pair-sum maxima: star 24 · triangle 27 · path 27 · P3+K2 28 · 3K2 30 (all identification patterns × degrees exhausted) | **PROVEN-BY-CERTIFICATE** |
| the (0,0,1) field survivor dies for every shape (all-light shared sets cap the pair-sum at 24 < 27) | **PROVEN-BY-CERTIFICATE** |
| 3K2 at W = 30: splits forced to {7,7}/{8,6}; subcase A dies 2 > 1, subcase B dies 7 > 4 | **PROVEN-BY-CERTIFICATE** |
| **X ≥ 4 for every critical core at m = 22** | **PROVEN-BY-CERTIFICATE** (in-house: 0005/0008/0009/0012/0013, 0015 (2)–(3), 0016 (T) + X ≥ 3, 0017 C1 + C2; **external NONE**) |

(ERRATUM 2026-07-28: this row originally read "0015 (2)–(3) + L1.2" — the same
inflated dependency the phase-3 outside reader struck from the header, banner
and ledger; the claim table missed the strike. Caught by the second outside
audit. No check touched.)

## Provenance — the outside-audit lane's first fruit, and the law it ran under

The theorem and the eight-case attack plan were **proposed by GPT 5.6 Sol Pro**
(2026-07-28), the first outside audit of the repo since JD made it public at
`baed4d1` (turn 13). The audit's field numbers matched this lab's banked and
certified values to the last digit — six in-house implementations agree (desk +
two blind spec-only fleet lanes + three refuter re-implementations). Its
**proofs were not ingested**: the audit arrived as a statement list with
one-line mechanisms; every proof consumed here was derived in-house — desk
derivation first, then nine **blind** fleet lanes re-deriving each shape kill
from the definitions pack alone, then five hostile refuters attacking the desk
versions, then a three-lens hostile audit of this verify.py itself. Attribution
recorded, not consumed (D-031): no step cites the outside audit.

Two scars, kept on purpose (D-017):

- **The desk "corrected" the audit's path bound 27 to 26 — and was wrong.**
  The desk's identification exhaustion missed the triple identification (one
  degree-7 vertex serving all three shared 2-sets). Three refuter lanes
  restored 27 by independent exhaustive enumeration; the audit had it right
  all along. The correction of a correction is pinned as a tooth in check 23.
- **Both the audit's summarized 3K2 equality route AND the desk's first
  write-up missed the all-(8,6) subcase** (the single degree-8 vertex serving
  all three pairs). The desk caught it in self-review mid-turn; three refuter
  lanes caught it independently minutes later; two blind lanes' proofs covered
  it unprompted. It dies by the 7 ≤ 4 injection (subcase B, check 29).

## Adversarial record (three fleet phases + this file's own audit)

- **Phase 1 (11 lanes):** 2 field lanes (Opus, spec-only, blind to the repo)
  reproduced every field number including the five survivor configurations;
  9 blind derivation lanes (one per shape + a Δ-lemma lane) each returned
  proved-dead with tool-cited proofs. The Δ-lane went beyond its brief and
  proved the whole theorem a second way (Δ ≤ 8 field-free → no degree-8 vertex
  → the all-7 censuses die) — banked in the turn-14 notebook, not consumed.
- **Phase 2 (5 refuters):** shapes 1–3 ruled **sound** (23-check exhaustive
  attack script); the two majors above; the triangle-equality prose fix
  (the \|∩\| = 1 partial identification also attains 27); the W ≤ Σ I_e
  citation re-pointed at 0015 step (2) + Φ-monotonicity (X-free), where it
  belongs.
- **Phase 3 (3 auditors on this verify.py): pass-with-fixes ×3, zero fatal,
  zero major; the outside reader signs PROVEN-BY-CERTIFICATE.** Sabotage
  red-team: 19 targeted mutations, **13 red with on-point localization**
  (budgets, w-table, (D2), TARGET, ladder, T_e-disjointness, the X ≤ 4 corner
  gate — which genuinely breaks at X = 5, matching 0017's witness — the
  equality split, the dfs prune, the shape_max budget, the light-run filter);
  the 6 green mutants root-caused as safe-direction redundancies. Notable:
  the same-pair-slots filter and the set-collapse in `hosts` are **mutually
  masking** (dropping either alone stays green; dropping both reddens —
  M19); the two spent-ledger legality filters were proven **inert** — which
  the fixed cert now certifies as a feature (see below). Spec audit:
  independent re-implementations of the field AND the shape maxima from
  first principles, all numbers reproduced; found one silently-implied
  premise (per-pair cap 14) and two cond=True checks. Outside reader: walked
  all eight kills end to end, re-derived the tool hypotheses against
  0013/0015/0016/0017, independently reproduced every field number and all
  ten maxima, and caught an **inflated ledger** — 0015's Lemma 1.2 was cited
  but consumed nowhere ("an inflated ledger is the flattering direction for
  a dependency audit").

  **Fixes applied, all same-commit, re-verified green ×2:** Lemma 1.2 struck
  from header/banner/ledger with a note · the per-pair-14 premise enacted
  (check 26) · check 6 demoted to a note and the ASSEMBLY check given a real
  conjunction of the run's own results · a **robustness check added**: both
  ledger legality filters disabled re-runs the whole exhaustion over the
  unconditional superset and every maximum is unchanged — the budgets alone
  pin the maxima, closing the fatal direction (a filter wrongly excluding a
  real core) unconditionally · the dead degree-9 bar and the never-firing
  size guard removed with comments · needs_heavy check marked corroborative
  and given a falsifiable case (star's flag is False) · the m ≤ 27 scope
  note re-pointed at 0017's margins row, not C5 · the six-vs-seven pencil
  discrepancy with the turn-14 notebook fixed (six is correct).

  **Mutation-surface honesty (the sabotage lane's ask):** the reddening
  surface covers sections 1–3, 7–8 and the enumerations; the prose-structural
  steps of sections 4–6 and 9 (channel caps, confinement injection, subcase
  kills) are defended by desk + nine blind lanes + five refuters, not by this
  script's checks — their finite content (relation exhaustions, pattern
  lists, split census) is what the script pins.

## The margins (D-035: name the binding coordinate)

- **Field side: one unit of (D2), again.** All five W ≤ 30 survivors sit ON
  the boundary at D2 = 11; relax 0008's cap by one degree-2 vertex and the
  list grows 5 → 46 (check 32). Sections 7–9 must be redone before re-quoting
  if (D2) ever weakens — same maintenance law as 0016.
- **Triangle and path close with ZERO units of W** (maxima = floor = 27); the
  binding fact is the census clash — every maximizer needs a heavy shared
  vertex, the (0,0,1) survivor has none (checks 24–25).
- 3K2 subcase A closes by **one unit** (2 vs 1); subcase B by three (7 vs 4);
  shape 1 by two rungs of m; shape 2 by one rung; shape 3 by two units of the
  confinement injection; star by three units of W.

## What this does not claim

Nothing about m ≥ 23 — the thin rungs m ∈ {23, 24, 25, 26} remain the
window's arithmetic-free stretch (0017 C7), and X = 3 was already impossible
at m ≥ 28 by 0017's coupling; this certificate empties the one rung where
X = 3 met a live field. No core is claimed to exist. Lemma D9 (X = 3 ⟹
Δ ≤ 8, window-wide, m > 9) is fleet-proven and desk-verified but **not
consumed** here; it and the degree-descent alternative proof live in the
turn-14 notebook, cited not consumed.

## Tally

33 checks, 10 notes (stated-not-tested facts), the breakdown measured from
the transcript, not hand-counted (the 0017-tally lesson). Sections: 1
budgets (4 + 1 note) · 2 the shape census (2 + 2) · 3 localization enacted
(2 + 1) · 4 shape 1 (2 + 1) · 5 shape 2 (3 + 1) · 6 shape 3 (2 + 1) · 7 the
field (5) · 8 the (1,1,1) maxima + light run + robustness (5) · 9 3K2
equality (4 + 1) · 10 assembly, controls, margins (4 + 2). Heavy steps report their own wall
clock: the 20,000-trial localization enactment ~5–9 s, the X ≤ 3 field scan
~0.5 s (inside the ~7 s section), the shape_max exhaustions ~8 s + ~3 s
(light) + ~21 s (the double robustness run), the X = 4 control scan ~1 s.

Runtime: ~44 s on bare 3.9.6; `-O` identical.
