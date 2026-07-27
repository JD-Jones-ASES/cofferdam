# 2026-07-27 · turn 10 — the finite window, certified twice, and the field mapped

## 0. What this turn set out to do

PLAN attack #1, both halves: **Part A** certify the finite window
(cert 0013, m ∈ [22, 462] for critical cores, ceiling citing nothing);
**Part B** the narrowed literature list. Delivered both, plus one thing
the plan had only queued as an audit: the peer-claimed 456 refinement is
now **certificate 0014**, and the window is **[22, 456]**.

## 1. Certificate 0013 — the window [22, 462], ledger empty on the ceiling

The turn-9 §13 desk proof, machine-checked: any counterexample contains
an edge-critical core K (m(K) ≥ 22 by the floor); criticality hands each
edge a private 5-cover with (3a) e ∩ T_e = ∅ and (3b) e ∩ T_f ≠ ∅; the
permutation argument (disjoint events, probability 6!·5!/11! = 1/462
each) gives m(K) ≤ C(11,6) = 462. **Ryser r = 6 intersecting ⟺ no
critical core with m ∈ [22, 462].** 32 checks + 8 notes, < 1 s, green
under bare 3.9.6 and `-O`.

What the certificate *enacts* rather than asserts: the probability lemma
exhausted through 9! at five shapes; the partition tightness witness at
[5] and [7]; teeth (one broken cross-direction → events overlap in
360/40,320 orders; a non-disjoint pair → probability 0; on a non-critical
family the private cover does not exist); the 462-pair complement witness
(212,982 substantive cross-checks — saturated, so the abstract argument
cannot beat 462); and the machinery end-to-end on two real objects. Fano
is NOT edge-critical (core: 6 lines; 5040-order full enactment, 6 events
× 504 orders each). Truncated PG(2,5) is not critical either — the
greedy strips 11 of 25 edges and lands on a **14-edge τ = 5 core, one
edge above 0009's g(5) = 13** (consistency cross-check, disclosed as
CONTROL-ONLY in the ledger).

**Adversarial record**: six lenses (three proof refuters, two code
auditors, completeness critic) — zero fatal, zero mathematical errors.
Catches, all fixed pre-certification: finiteness stated; T_e ⊆ V(K)
argued (cover-minimality one-liner); τ-monotonicity clause; the floor
ledger made TRANSITIVE (0011 and 0006 enter via 0012's (L10)/(L7) — the
first draft shipped three inconsistent dependency lists); the control
citation corrected from N(5) to **g(5)** (the general-class rung — the
scope lens's genuinely good catch); robustness attribution corrected
((3a) rides on τ(K) = 6, not criticality); arithmetic-only checks
relabeled as such. The reimplementation lens rebuilt the rehearsal from
a Singer difference set ({0,1,3,8,12,18} mod 31, different deleted
point, different greedy) and reproduced every invariant — its core has
**13 edges, exactly on the g(5) floor**: independent corroboration that
the floor is achieved inside truncated PG(2,5).

My own errors this turn, recorded per house law: the first draft pinned
three guessed constants (teeth count, greedy deletions, core size)
before measuring — the first run caught all three (the D-017 shape:
number asserted before taken). Fixed by measurement, not adjustment.

## 2. The r = 2 calibration — the little theorem that kept everyone honest

Proven at the desk, then machine-checked (m = 2 witness verified; m = 3
impossible by brute force to n = 9, and by hand): **the abstract
transversal set-pair maximum at r = 2 is exactly 2 = C(3,2) − (r−1)**,
NOT C(3,2) − r = 1. Consequence: no "minus r" refinement can be a pure
partite set-pair theorem uniform in r; any correct 456 proof must either
break at small r or consume core structure. This single data point,
handed to the audit fleet in its briefing, is what forced the mechanism
below to be located precisely.

## 3. The 456 audit → certificate 0014 — the window tightens to [22, 456]

Two independent lanes converged:

- **Derivation lane (DERIVED)**: the mechanism is **part-confinement**.
  Map each part P_j into a generic 5-dim subspace U_j ⊂ R¹¹; with q_j
  the basis-wedge of U_j, the functional x ↦ x ∧ q_j kills EVERY
  transversal wedge *identically* (e's part-j vector plus q_j's five
  factors are six vectors in a 5-dim space). Six independent
  functionals → all edge-wedges in a 456-dim subspace. Diagonals
  x_e ∧ w_{T_e} survive iff **no T_e is concentrated in one part** —
  hypothesis (*).
- **Measurement lane (MEASURED)**: generic (unconfined) embeddings give
  codim 0 at r = 6 with core-realistic part sizes — certified full-rank
  witnesses — so no refinement exists generically and confinement is
  essential; confining parts to 5-dim subspaces gives codim EXACTLY 6,
  the annihilators being precisely the part-wedges. The diagonal-death
  criterion verified both directions. At r = 2 the lane reproduces the
  calibration exactly.

**(*) from (A), two lines** (desk re-derivation): if T_e ⊆ P_j, every
f ≠ e has its part-j vertex in T_e (T_e covers K − e, one vertex per
part), so e's own part-j vertex v ∉ T_e (3a) would have degree 1 —
against 0005's lemma (A), which holds for every counterexample. So
t_j ≤ 4 for all parts, each part contributes ≤ 5 vectors, diagonals
generic-survive.

**Certificate 0014**: 13 checks + 4 notes, exact integer arithmetic
throughout (Bareiss + Fraction elimination, fixed-seed LCG), green under
bare 3.9.6 and `-O`. Checks include: general-position instance; 300
exact-zero annihilation determinants; Plücker rank EXACTLY 6 (so
dim X = 456); a **rank-sensitivity control** (collapse U₆ := U₁ → rank
drops to exactly 5) added after the adversarial pass proved the original
draft would have passed with a broken rank routine; all 246 admissible
cover patterns witnessed nonzero (246 = C(10,5) − 6); the six excluded
patterns die in 60/60 trials; the r = 2 exhibit; unconfined full-rank at
r = 3, 4. Adversarial pass: five lenses, zero mathematical errors; the
independent reimplementation (different RNG, Fraction elimination,
two-prime cross-checks) reconfirmed rank 6 by a second route and
verified the r = 3 confined analog end-to-end (dim X = C(5,3) − 3 = 7).

**General form, noted not certified**: r-partite cores with (A) satisfy
m ≤ C(2r−1, r) − r for every r ≥ 3; at r = 2 (*) is unsatisfiable and
the bound is false abstractly. Certification of the general form is a
cheap future rung.

Provenance, stated precisely: the outside review (via JD, turn 9)
supplied the number and a one-line sketch; the audit fleet located the
mechanism; the desk re-derived it; the certificate witnesses it. The
sweep (below) found **no published counterpart** — if that absence
holds, the 456 ceiling is new mathematics.

Two audit lanes (combinatorial derivation of the abstract-true bound;
exhaustive r = 3 max search) were still running at entry time — addendum
below when they land.

## 4. Part B — the literature, from fetched sources

**(a) Attribution.** Bollobás 1965 = Acta Math. Acad. Sci. Hungar. 16,
447–452 (DOI 10.1007/BF01904851; original in a different lemma form).
The modern symmetric statement: conjectured by Ehrenfeucht–Mycielski,
proved by **Katona, JCTA 17 (1974) 265–266 — with exactly the
random-permutation argument cert 0013 uses** (Jukna argues for
"Bollobás–Katona"). Independently rediscovered (statement, not method)
by **Jaeger–Payan, C. R. Acad. Sci. Paris 273 (1971) A221–A223 — whose
title is literally the maximum edge count of τ-critical hypergraphs of
rank h**: the ceiling's statement class is theirs. Tuza's JCTB 39 (1985)
134–145 does the *vertex* bounds; his surveys catalogue the method. The
general edge formula C(r+t−1, r) is explicitly Remark 3.3 of Li,
arXiv:2512.24850 (Dec 2025; main theorem = the (3,3) case ≤ 10,
verified from the abstract firsthand). Skew variant: same bound
(Lovász 1977 / Frankl 1982 / Kalai 1984); the weighted skew bound is
NOT 1 but n+1 (Frankl–Hegedüs, EJC 120 (2024) 103983) — we use
symmetric-uniform, unaffected.

**(b) Partite refinement.** Not in the literature. Partite Bollobás
variants exist (Alon 1985; Moshkovitz–Shapira 2015; three 2026 papers)
but all constrain BOTH families per part, and at our parameters the
known intersecting-A-side routes buy nothing (AK(2r−1, r, 1) =
C(2r−1, r)). Closest genre: subspace variations of the weighted skew
Bollobás theorem (Wu–Li–Lu–Feng, arXiv:2603.02698, March 2026).

**(c) The real fractional theorems** (both from primary sources — the
Hungarian original and Füredi's own scan): **Lovász, Mat. Lapok 26
(1975) p. 236, Tétel 3: τ ≤ (R/2)·τ\* for R-partite hypergraphs** —
THIS is where "r/2" lives; the turn-9 false Fact was a garble of it.
**Füredi, Combinatorica 1 (1981): τ\* ≤ (r−1)ν + p/r** (no p+1 disjoint
projective-plane substructures), Corollary 5: **τ\* ≤ (r−1)ν for
r-partite**, sharp exactly on truncated projective planes (our τ\* = 5
object is the equality case, not a paradox); and for intersecting
r-uniform: τ\* ≤ r−1+1/r, equality iff a projective plane of order r−1.
Aharoni's 2001 tripartite proof uses the Aharoni–Haxell topological Hall
theorem (Sperner-based, in a deficiency form suggested by Ziv) plus
Kőnig — confirmed from the author's galley.

**(d) FHMW scope.** Ryser is PROVEN for linear intersecting r-partite
hypergraphs, r ≤ 9 — any r = 6 counterexample is necessarily
non-linear. Their Lemma 2.1/2.2 constraints (degree ≥ 2, ≤ one
degree-2 vertex per line, Δ ≥ 4) are adjacent to our (A)/(D2) family.

**(e) The "March-2026 survey" was mischaracterized by the peer.**
arXiv 2603.04704 exists (5 Mar 2026) but is a 9-page research paper
(Hawranick–Luo, monochromatic component covers) whose single relevant
sentence confirms: intersecting proven r ≤ 5 (citing **Tuza's 1979
UNPUBLISHED manuscripts** — r = 4, 5 intersecting have no published
proof, a fact worth knowing), **r ≥ 6 open**. The actual survey is
**DeBiasio–Kamel–McCourt–Sheats, EJC 28(4) (2021) P4.37**, which
carries: a minimal-counterexample structure theorem (Appendix A, Thm
9.1) and the field's existing finite reformulation of intersecting
r = 6 — a 173-signature enumeration (§3.4, Table 2). Their finite
framing is signature-based; ours is size-based. Complementary, and
their Table 2 is a lead.

## 5. Novelty, re-measured — the floor comparator MOVED mid-session

**Sivashankar, arXiv:2606.24878 (23 June 2026, verified firsthand from
the abstract): g(r) ≥ 3r−4** for r-uniform intersecting with τ = r —
the first improvement on Erdős–Lovász in ~fifty years. Every r = 6
counterexample is a fortiori 6-uniform intersecting with τ = 6, so the
**published-preprint floor for our m is now 14** (was 13). Ours is 22 —
eight clear, but the neighborhood is hot (two papers on this function in
15 months). Also in print: g(6) ≤ 18 via Barát's unique 18-line
PG(2,5) configuration (Corollary 7.5, J. Combin. Des. 29 (2021)) —
adjacent to our rehearsal object; his 18×18 incidence matrix is a lead.

**The zoo of 9s and 13s — name the function, always** (three distinct
13s and three distinct 9s now live in this area):

| value | function | object class | source |
| --- | --- | --- | --- |
| 9 | our g(4) = N(4) | 6-partite 6-uniform, τ ≥ 4 | certs 0005/0010 |
| 9 | q(4) | 4-uniform, τ = 4 | Tripathi 2014 |
| 9 | f(5) | 5-partite 5-uniform, τ ≥ 4 | Mansour–Song–Yuster |
| 13 | our g(5) = N(5) | 6-partite 6-uniform, τ ≥ 5 | cert 0009 |
| 13 | f(6) ≡ our g(5) | same function, published | Abu-Khazneh–Pokrovskiy; Aharoni–Barát–Wanless 2016 |
| 13 | q(5) | 5-uniform, τ = 5 | Barát 2021 (single author — the Erdős Problems site misattributes it) |
| 13 | 8r/3 − 3 at r=6 | floor, 6-uniform τ = 6 | Erdős–Lovász — superseded by Sivashankar's 14 |

0009's g(5) = 13 re-derives the published f(6) = 13 citing nothing —
exactly as the founding intended (f(6) = 13 was the cited constant the
free ladder replaced); no novelty statement is harmed, but every future
writeup must name the function.

**Ceiling novelty, scoped precisely**: the generic formula C(r+t−1, r)
is classical and in recent print (Li's remark); its instantiation at
Ryser r = 6 intersecting appears NOWHERE — three full-text scans found
the set-pair and Ryser literatures completely disjoint, and the Ryser
field's only counterexample ceiling is Erdős–Rado sunflower
r!·cʳ ≈ 3.36×10⁷. The two-sided window (certified floor 22 + ceiling
462/456) is ours; the 456 has no counterpart at all.

**Traps recorded**: arXiv:2509.00619 "On Ryser's Conjecture" is the
OTHER Ryser conjecture (math.NT, circulant Hadamard); the Erdős
Problems #21 page (edited 2025-12-03) is stale on Sivashankar and
misattributes Barát.

## 6. Leads opened (PLAN carries the actionable ones)

DeBiasio Table 2 (173 signatures — extraction pass); Barát §7's 18×18
matrix vs our truncated-plane work; Pokrovskiy arXiv:2507.05842 (Ryser ⟺
bounded-diameter Milicevic form — a different finite-shaped
reformulation); certify the general form C(2r−1, r) − r; the confined
embedding as a NEW attack surface (what else does core structure buy as
annihilators — D2? degree caps?); the two pending audit lanes.

## 7. Addendum — the max-search lane landed: the abstract truth is NEITHER pattern

The r = 3 exhaustive search (fleet, with a hand-proved reduction to
partition triples, 11,536,935 tested, positive control at m = 6 finding
54 solutions through the identical code path) returns: **the abstract
transversal set-pair maximum at r = 3 is EXACTLY 6** — not 7 (the "−r"
pattern) and not 8 ("−(r−1)"). The m = 6 witness — the 2×2×2 cube of
transversals minus an antipodal pair, a Hamming-sphere covering — was
**re-verified at the desk** (all axioms pass); the m = 7 impossibility
is fleet-claimed exhaustive (strong controls, not desk-re-derived).

Data so far: r = 2 → 2 = C(2,1); r = 3 → 6 = C(4,2). Both match
**C(2r−2, r−1)** — which at r = 6 would be **252**. If the abstract
partite maximum follows this pattern, the window ceiling would drop
from 456 toward 252 *without consuming any core structure at all*.
Status: **LEAD, not a claim** — proved only at r = 2, 3; the fleet's
r = 4 probe found a verified 17-witness (max ∈ [17, 35], pattern
predicts 20), and the r = 3 witness's sphere-covering mechanism
provably does NOT generalize naively to r = 4 (hand-checked by the
lane). Consistency note: 6 < 7 = the (*)-conditional analog bound, so
even 0014's mechanism is not tight at r = 3 — there is real room below
456.

**The combinatorial lane landed (PARTIAL), with three more facts:**

- **Theorem A (fleet-claimed hand proof, clean writeup on file): every
  abstract transversal system has m ≤ C(2r−1, r) − 1, no hypotheses at
  all** — a tiling/transposition argument on top of the Katona proof
  (if m = N the disjoint events tile the permutation space; one
  adjacent transposition then forces a second edge to be a
  non-transversal). Exact at r = 2 (max 2 = 3 − 1). At r = 6: 461,
  superseded for cores by 0014's 456, but notable — the "−1" is free.
- **The two lanes DISAGREE on r = 4**, honestly recorded: this lane's
  exhaustive searches on supports up to (3,2,2,2) topped at 14 = 2⁴−2
  and conjectured exponential collapse; the max-search lane's verified
  17-witness (bigger support) kills 2^r − 2 and is consistent with
  C(2r−2, r−1) = 20. Both fleet-claimed; the r = 4 truth sits in
  [17, 35]. The C(2r−2, r−1) lead stands; the exponential one dies.
- **Where core structure bites hardest is an axiom nobody consumed
  yet: the e's of a core are pairwise INTERSECTING**, which the
  abstract system never assumes. The lane reports intersecting-ness
  alone forces m ≤ 2^(r−1) on binary supports (32 at r = 6 — far below
  456, though cores don't live on binary supports). Adding the
  intersecting axiom to the abstract landscape is now the sharpest
  open attack on the ceiling.

Also from the derivation lane's full transcript: the six functionals
are the **complete** annihilator — the transversal-wedge span EQUALS
the 456-dim subspace X (staged-reduction dims [5, 25, 105, 270, 432,
456], fleet-measured) — so no seventh functional exists generically,
and any push below 456 must be combinatorial, not dimensional.
