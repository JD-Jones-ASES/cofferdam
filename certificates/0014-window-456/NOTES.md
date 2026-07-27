# Certificate 0014 — the window tightens: every critical core has m ∈ [22, 456]

**Status: GREEN.** 13 checks + 4 notes, ~1 s, `python3 verify.py`, stdlib
only, exact integer/rational arithmetic throughout (Bareiss determinants,
Fraction row reduction; no floats, no modular shortcuts, no solver), no
imports from `lib/`. Green under a bare `/usr/bin/python3` (3.9.6) and
under `python3 -O`. Deterministic (fixed-seed hand-rolled LCG).

| claim | label |
| --- | --- |
| **(L11)** six part-functionals annihilate the transversal-wedge span; dim X = 456 | **PROVEN-BY-CERTIFICATE** |
| **(\*)** no private cover of a critical core is concentrated in one part | **PROVEN** (from (A) in 0005, via 0013's (3a)/(3b)) |
| every critical core has m ≤ C(11,6) − 6 = 456 | **PROVEN-BY-CERTIFICATE** (in-house: 0005, 0013; external NONE) |
| **the window tightens: m ∈ [22, 456]**; Ryser r = 6 intersecting ⟺ no critical core with m ∈ [22, 456] | **PROVEN-BY-CERTIFICATE** (floor: 0013's floor half, transitively 0005/0006/0008–0012) |

## Why this certificate exists

Certificate 0013 closed the window at C(11,6) = 462 with classical,
self-contained machinery. This certificate spends core structure to buy
six more units. The mechanism — located by the turn-10 audit fleet and
re-derived at the desk — is **part-confinement**: map each part into a
generic 5-dimensional subspace U_j of R¹¹. Then the six functionals
x ↦ x ∧ q_j (q_j the basis-wedge of U_j) annihilate *every* transversal
wedge **identically** — e's part-j vector plus q_j's five factors are six
vectors in a 5-dimensional space — so all edge-wedges live in a
456-dimensional subspace; and the Bollobás-style diagonal pairing
survives confinement precisely because **no private cover T_e can sit
inside a single part**: a concentrated T_e would force e's own part-j
vertex to degree 1, against 0005's lemma (A). Two lines of hypergraph
theory unlock six units of linear algebra.

## Scope, and the r = 2 boundary

Cores only, exactly as 0013; this certificate consumes MORE than 0013
(lemma (A) and the confined embedding) and stands on it — 0013's ceiling
remains the empty-ledger record. The general form (r-partite cores:
m ≤ C(2r−1, r) − r for every r ≥ 3) is noted, not separately certified.
At r = 2 the hypothesis (*) is **unsatisfiable** (|T| = 1 always sits in
one part) and the refinement is **false** abstractly: the in-house
calibration system has m = 2 > C(3,2) − 2 = 1. That calibration, proven
before the derivation was attempted, is what forced the mechanism to
consume core structure — the peer sketch omitted this entirely.

## Margins and teeth

- **Teeth (\*)**: the six excluded patterns (T_e concentrated) give
  determinant exactly 0 in all 60 trials — the diagonal dies, and with
  it the bound. The r = 2 exhibit shows the refinement false without (*).
- **Not too strong**: with parts UNCONFINED the transversal wedges span
  *everything* — rank 10/10 at r = 3 and 35/35 at r = 4, exact over Q
  (the audit's measurement lane witnessed the same at r = 6: rank 462;
  fleet-measured, recorded in the turn-10 notebook, not a check here).
  No refinement exists generically; confinement is essential.
- **Sensitivity**: collapse U₆ := U₁ and the annihilator rank drops to
  exactly 5 — the rank computation is falsifiable in both directions
  (a rank routine that always reports full rank fails this check), and
  the bound would weaken to 462 − rank if the rank fell short.
- All 246 admissible cover-patterns carry exact nonzero witness
  determinants; the annihilation identity is spot-verified by 300 exact
  zero determinants; the off-diagonal identity by 20 more.

## Adversarial record (turn 10)

Five lenses attacked the certificate before it went green in this form:
exterior-algebra core, concentration lemma/composition, code audit
(det_bareiss differential-tested on 5,800 adversarial matrices, zero
mismatches; full shadow-run of all 12,608 determinant calls against a
Fraction reference), independent reimplementation (different RNG,
Fraction Gaussian elimination + two-prime modular cross-checks: rank 6
reconfirmed by a second route — the signed 6×462 functional matrix —
all 246 patterns re-witnessed, the r = 3 confined analog verified
end-to-end with dim X = C(5,3) − 3 = 7), and a completeness critic.
**Zero fatal findings; zero mathematical errors.** The one genuine gap —
no degenerate-instance control on the rank routine — became the
sensitivity check above; the wording catches (a garbled clause in the
(*) proof, an "empty-ledger" conflation, two label overclaims) were all
fixed before certification.

## Provenance and novelty

The 456 mechanism was claimed by an outside review (relayed via JD,
turn 9) as a one-line sketch, desk-read plausible, unverified. Turn 10
ran two independent in-house audit lanes; both converged on the
part-confinement mechanism, the measurement lane additionally proving
generic embeddings give codimension 0. The proof was re-derived at the
desk line by line before this certificate was written. The turn-10
literature sweep found **no published counterpart** of this partite
refinement (closest genre: subspace variations of the weighted skew
Bollobás theorem, Wu–Li–Lu–Feng, arXiv:2603.02698, March 2026); if that
absence holds, the 456 ceiling is new mathematics. Attribution for the
exterior-algebra set-pair method (Lovász 1977 / Frankl 1982 / Kalai
1984): recorded, not consumed.

## Reproduce

```bash
python3 verify.py
```

~1 s, deterministic. The heavy steps are the 2,772 Plücker minors and
the ~600 exact 11×11 Bareiss determinants.
