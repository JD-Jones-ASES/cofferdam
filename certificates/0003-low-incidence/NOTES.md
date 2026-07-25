# Certificate 0003 — the low-incidence bound; m = 20, Δ = 5 dies

**Status: GREEN.** 12 checks, 0.6 s, `python3 verify.py`, stdlib only, no solver.

| claim | label |
| --- | --- |
| (L5) Σ_i L_i(θ) ≤ m·⌊B/θ⌋, where B = 6Δ − (m+5) | PROVEN-BY-CERTIFICATE |
| **m = 20 with Δ = 5 is impossible** | **PROVEN-MODULO-CITATION** (needs f(6)=13) |
| m = 20 now has Δ ∈ {6,7}; m = 19 still only Δ = 6 | same |
| the floor is unchanged at m ≥ 19 | — a reduction, not an improvement |

## The lemma

For an edge E and part i, the **deficiency** d_i(E) = Δ − deg(v), v being E's
vertex in part i. Cert 0002's (L4) says Σ_{v∈E} deg(v) ≥ m+5, so

  Σ_i d_i(E) ≤ B := 6Δ − (m+5)   for every edge.

So no edge has more than ⌊B/θ⌋ parts of deficiency ≥ θ, and counting incidences
over all edges gives **Σ_i L_i(θ) ≤ m·⌊B/θ⌋**, where L_i(θ) is the number of edges
whose part-i vertex has degree ≤ Δ−θ.

**Why this is not already in (L4).** (L2) is the average of (L4); (L4) is the
per-edge fact. (L5) is about the *distribution*: the shortfall cannot be
concentrated, because one edge cannot be deficient in two parts when the budget is
below 2θ. The pair count wants a few very popular vertices; (L4) pointwise says
every edge needs popular vertices in nearly every part; (L5) turns the tension
into a counting contradiction whenever B is small.

## The kill

At m = 20, Δ = 5: B = 30 − 25 = **5**. With θ = 3, ⌊5/3⌋ = 1 — every edge has at
most **one** part where its vertex has degree ≤ 2, so at most 20 such incidences
across all six parts. But supplying the C(20,2) = 190 agreements that
"intersecting" demands forces at least **28**. Contradiction.

Computed two independent ways, both in the certificate: a primal DP (maximise
agreements subject to the incidence budget → 184 < 190) and a dual DP (minimise
incidences subject to reaching 190 agreements → 28 > 20).

(L5) is not a universal solvent, and the certificate checks that too: at m=19 Δ=6
and m=20 Δ∈{6,7} the best θ is the trivial one and nothing is gained. The kill
lands exactly where the budget is tight.

## Where the frontier stands after 0001–0003

| m | surviving Δ | how it was cut |
| --- | --- | --- |
| ≤ 18 | none | cert 0001 — the floor |
| 19 | **6 only** | 0002: Δ=4 by counting *and* parity, Δ=5 by counting |
| 20 | **6, 7** | 0002 window; 0003 removes Δ=5 |

Two rungs, three cases. That is the whole unverified remainder of m ≥ 21.
