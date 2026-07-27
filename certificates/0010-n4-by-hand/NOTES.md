# Certificate 0010 — N(4) = 9 by hand

**Status: GREEN.** 24 checks + 3 notes, ~33 s, `python3 verify.py`, stdlib
only, no solver, no imports from `lib/`. Green under a bare `/usr/bin/python3`
(3.9.6) and under `python3 -O`.

| claim | label |
| --- | --- |
| no 8-edge 6-partite intersecting τ ≥ 4 object has a full part | **PROVEN-BY-CERTIFICATE** (hand proof; finite enumerations machine-checked) |
| **N(4) = 9** | **PROVEN-BY-CERTIFICATE, citing nothing** |

## Why this certificate exists

N(4) = 9 is the hinge of the floor. Certificate 0007's own closing words:
"the load-bearing step is no longer a citation. It is N(4) = 9, one
exhaustive search of ours at 52.0M nodes... A third independent
implementation of that search is now the single most valuable thing anyone
could contribute." PLAN item 3 (as of turn 8) asked for that third implementation — and
warned that it should match "the verdict and a structurally different route,
not the node count."

This certificate is the third leg, and it is better than a third search: it
is a **proof with no search in it**. The route: reduce to partition systems;
pin the full part to (2,2,2,2) (four married pairs); cap all degrees at 3 and
same-part degree pairs at 5; the pair count then admits exactly three profile
cases (X ≤ 1); any two size-3 blocks intersect (else their complement-pair's
common vertex completes a 3-cover); the excess budget prices every
coincidence; every edge lies in some triple (Σ b_i = 11 + ε); a double count
funnels each case into an r-vector with a 2–3 line kill. Case A-η1 ends the
way this lab likes: the married-pair structure the *hypothesis* forces is
exactly what the excess budget cannot afford.

Every finite claim the proof invokes is machine-checked in §§2–3, and then
§4 kills every case a second time at the structure level (exhaustive sweeps
over triple systems in C(8,3) = 56), independent of the r-vector arithmetic.
Either route alone closes the theorem.

## Margins and teeth

- The case split has **no slack**: 24 of a maximum 25 pair-units are required
  from five parts, which is what pins ≥ 4 parts to (3,2,2,1). This is the
  same margin-one geometry as everything else at the bottom of the ladder —
  stated, not hidden (D-017).
- **Teeth**: relaxing the excess budget by one unit (one married pair allowed
  inside a triple) floods the A-η1 sweep with 12,500 passes on the first 500
  systems alone. The budget is what kills; the sweep can tell the difference
  (check 21).
- The 9-edge witness is re-verified from scratch: intersecting, τ = 4 exactly
  (explicit 4-cover, no 3-cover in all 2,300 subsets), part 1 = (3,2,2,2)
  full (checks 22–24).

## Relation to the searches

The 52.0M-node exhaustion (certificate 0005) and the turn-7 second
implementation (5,713,053 nodes, 8,648 exhibited near-misses) agree with the
theorem and now stand as corroboration, not foundation. The risk class of the
floor's hinge changes today: from "two searches agree" to "a theorem a human
can read in an afternoon, plus two searches that agree with it."

## Provenance

The proof was found by this lab's subagent fleet (turn 9; three independent
angles briefed adversarially — and **all three returned complete proofs**).
The certificate ships the pairs-angle proof, which was re-derived line by
line at the desk before certification — fleet output is fleet-claimed until
re-derived (Certificate Law), and only this one has been. The other two are
recorded as fleet-claimed corroboration; notably the third proves the
*stronger* per-part statement (every part of an 8-edge τ ≥ 4 object carries a
degree-1 vertex — the corrected-AKP-2.8 consequence) and is the natural next
re-derivation target. The finding agent also corrected two errors in its own
briefing: the pair-sum of (2,2,2,1,1) is 3 (not 4), and (3,2,1,1,1) was
missing from the briefed fifth-part list (it is Case C here).

## Reproduce

```bash
python3 verify.py
```

~33 s, deterministic. The heavy step is the C(56,5) triple-system sweep.
