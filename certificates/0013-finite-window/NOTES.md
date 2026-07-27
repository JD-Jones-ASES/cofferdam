# Certificate 0013 — the finite window: every critical core has m ∈ [22, 462]

**Status: GREEN.** 32 checks + 8 notes, ~1 s, `python3 verify.py`, stdlib
only, no solver, no imports from `lib/`. Green under a bare
`/usr/bin/python3` (3.9.6) and under `python3 -O`.

| claim | label |
| --- | --- |
| every edge-critical counterexample ("critical core") has m ≤ C(11,6) = 462 | **PROVEN-BY-CERTIFICATE, ledger empty** — no external inputs, no in-house certificate inputs |
| every critical core has m ∈ [22, 462] | **PROVEN-BY-CERTIFICATE** (floor half in-house: transitively 0005/0006/0008–0012) |
| **Ryser r = 6 intersecting ⟺ no critical core with m ∈ [22, 462]** | **PROVEN-BY-CERTIFICATE** (the [22,·] half inherits the floor's ledger) |

## Why this certificate exists

Until today the conjecture was an infinite question: the floor certificates
kill m ≤ 21, but nothing bounded a counterexample from above. This
certificate closes the top: any counterexample contains an edge-minimal
**critical core** K (still a counterexample, so m(K) ≥ 22); criticality
hands every edge a private 5-cover T_e with e ∩ T_e = ∅ and e ∩ T_f ≠ ∅,
and the permutation argument — the events "all of e precedes all of T_e"
are pairwise disjoint, each of probability exactly 6!·5!/11! = 1/462 —
caps m(K) at C(11,6) = 462. The conjecture is now **one finite check**:
does a critical core live in [22, 462]? Both ends are certified, and every
future rung closes part of a window with 441 values of m remaining.

The hand proof was re-derived at the desk in turn 9 (notebook §13) after an
outside review (commissioned by JD, relayed per house law as peer-claimed)
caught that the ceiling is 462, not "astronomically far" — the same review
whose false τ* ≤ 3 "Fact" died against truncated PG(2,5). Both corrections
were re-derived firsthand before anything here was written; this
certificate is the desk proof, machine-checked.

## Scope, stated with care

The **window quantifies over critical cores**; the floor certificates
quantify over **all counterexamples** — strictly stronger, and exactly what
the floor step consumes (a core is a counterexample a fortiori). The
ceiling is a cores-only statement: a non-critical counterexample is bounded
by nothing here, but every counterexample *contains* a core, which is what
makes the window equivalent to the conjecture. Sections 5–6 exhibit real
non-critical objects (Fano; truncated PG(2,5)) where the private-cover
construction fails outright until the greedy core is extracted (a labeled
TEETH check enacts the failure) — criticality is a working hypothesis, not
a relabeling.

## Margins and teeth

- The abstract set-pair bound is **saturated**: the 462-pair complement
  witness on [11] (§4) satisfies every hypothesis the permutation argument
  uses (212,982 substantive ordered cross-checks). The ceiling argument
  alone cannot be pushed below 462 — any refinement (e.g. the peer-claimed
  456 for 6-partite cores) must consume structure this certificate does
  not. **Not too strong**, abstract side.
- **Teeth**: break ONE cross-direction of one pair and the disjointness
  mechanism dies — the two events overlap in exactly 360 of the 40,320
  orders (§3). A non-disjoint pair has event probability 0 (§3). On a
  non-critical family the promised private cover does not even exist (§5).
- **Not too strong, hypergraph side**: the machinery kills nothing that
  exists — the extracted τ = 5 core of truncated PG(2,5) sits alive inside
  its own window analog [13, 210], the floor end cross-checking
  certificate 0009's g(5) = 13 (its general-class rung; the greedy landed
  on 14, ONE edge above the floor — consistency, not input).
- The whole argument is **enacted by exhaustion twice**: the 10-pair
  system on [5] partitions all 120 orders, the 35-pair system on [7] all
  5040; and at τ = 3 the Fano core's 6 events fire in exactly 504 of the
  5040 orders each, pairwise disjointly (§5) — the theorem run as a
  physical experiment, no step abstract.

## Adversarial record (turn 10)

Six independent lenses attacked the proof and the checker before
certification: three refuters (criticality/extraction, permutation
argument, scope/overclaim), two code auditors, one completeness critic.
**Zero fatal findings; zero mathematical errors.** Every catch was
bookkeeping and was fixed before this went green: finiteness stated,
T_e ⊆ V(K) argued via cover-minimality, τ-monotonicity clause added, the
floor ledger made transitive (0011 and 0006 enter via 0012's (L10)/(L7)),
g(5) vs N(5) precision in the control, robustness attribution corrected
((3a) rides on τ(K) = 6, not criticality), and arithmetic-only checks
relabeled as such. One auditor **reimplemented the §6 rehearsal from
scratch** on a different construction (Singer difference set {0,1,3,8,12,18}
mod 31, different deleted point, different greedy) and reproduced every
invariant — its independent core landed on **13 edges, exactly 0009's
floor**, corroborating that g(5) = 13 is achieved inside truncated
PG(2,5). Core size is greedy-dependent (ours 14, theirs 13); no claim
rides on it.

## Attribution (recorded, not consumed)

The ceiling's machinery is classical, and the turn-10 literature sweep
pinned it exactly (fetched sources; details in the turn-10 notebook entry):

- **The set-pair inequality**: Bollobás 1965 (Acta Math. Acad. Sci.
  Hungar. 16, 447–452) — stated there in a different lemma form; the
  modern symmetric statement was conjectured by Ehrenfeucht–Mycielski and
  proved by **Katona (JCTA 17 (1974) 265–266) with exactly the
  random-permutation argument used here** (Jukna argues for
  "Bollobás–Katona"); the uniform statement was independently
  rediscovered by Jaeger–Payan (1971).
- **The application to τ-critical hypergraphs**: Jaeger–Payan (C. R.
  Acad. Sci. Paris 273 (1971) A221–A223 — their title *is* the maximum
  edge count of τ-critical hypergraphs of rank h); the set-pair method
  for critical systems is Tuza's school (JCTB 39 (1985) 134–145 gives
  the *vertex* bounds; his surveys catalogue the method). The general
  edge formula C(r+t−1, r) appears explicitly as Remark 3.3 of Li,
  arXiv:2512.24850 (Dec 2025), whose main theorem is the (3,3) case
  ≤ 10 = C(5,3).
- **Nobody instantiates the formula at Ryser r = 6 intersecting**: the
  sweep found the set-pair and Ryser literatures disjoint (zero
  cross-hits across the DeBiasio–Kamel–McCourt–Sheats survey, FHMW, and
  2026 full texts); the Ryser literature's only counterexample ceiling
  is the Erdős–Rado sunflower bound r!·cʳ ≈ 3.36×10⁷ at r = 6. The
  window [22, 462] — a certified floor paired with the 462 ceiling —
  appears nowhere.
- **The skew variant** (one cross direction only): same C(a+b, a) bound,
  by exterior algebra (Lovász 1977; Frankl 1982; Kalai 1984) — not used
  here; the weighted skew bound is NOT 1 (Frankl–Hegedüs, EJC 120
  (2024) 103983). Our use is symmetric-uniform and unaffected.

The proof here is re-derived from first principles and machine-checked,
so the certificate stands without any citation — but a result must never
look more novel than it is: **the argument is classical machinery
re-derived; what is ours is the window.** (Floor context moved during
this session: Sivashankar, arXiv:2606.24878, June 2026, proves
g(r) ≥ 3r−4 for r-uniform intersecting with τ = r, so every
counterexample has m ≥ 14 by one-line specialization — verified
firsthand from the abstract; the in-house floor stands 8 above it.)

## Annex (context, not chain)

The truncated PG(2,5) built in §6 carries the machine record of the τ*
kill: every vertex has degree exactly 5; edge weights 1/5 (value 5 exactly)
and vertex weights 1/6 (value 5 exactly) are both feasible in exact
rationals; one prose line of weak LP duality squeezes **τ* = ν* = 5** —
so "τ* ≤ r/2 for r-partite intersecting hypergraphs" (asserted as Fact in
the turn-9 notebook §8) is FALSE, and its killer lives in a green
certificate.

## Reproduce

```bash
python3 verify.py
```

~1 s, deterministic. The heavy steps are the 212,982 ordered cross-checks
on the 462-pair witness, the 9! exhaustions in §2, and the
C(30,4) = 27,405-subset cover scans in the truncated-plane rehearsal.
