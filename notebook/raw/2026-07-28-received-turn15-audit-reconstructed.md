# RETENTION NOTE (D-038 clause 4, applied one turn late)

This is the turn-15 received text (GPT 5.6 Sol Pro's second review), reconstructed
2026-07-28 from the session transcript in which JD relayed it. The original was never
saved as a file; this copy is desk-mediated and retained to substantiate the turn-16
erratum (the received text defines w(d) := Φ(d−1,5), an integer at every d — see the
"Write w(d) := Phi(d-1,5)" line in §2 below). The turn-16 review and all future received
texts are retained verbatim on arrival. Formulas appear as relayed (plain-text LaTeX).

---

Cofferdam audit and a new excess theorem

Executive verdict: I agree with the current certified state of the project. I found no
fatal mathematical error in the chain establishing m >= 22, 22 <= m(K) <= 456 for an
edge-critical counterexample core K, nor in the current conclusion that a core with
m = 22 has X >= 4. The latest public commit is 079539c, synchronizing the repository
around Certificate 0018 and the X >= 4 result. The finite-window reduction, degree-two
cap, private-cover machinery, corner inequalities, growth laws, and Certificate 0018's
X = 3 elimination all survive this audit. The repository's public summary accurately
describes the certified standing. My substantive disagreement is not that the current
state is wrong. It is that it is now too weak.

Proposed new standing: Let K be an edge-critical counterexample core for intersecting
Ryser at r = 6. Then X(K) >= 5. Moreover, X(K) = 5 ==> 22 <= m(K) <= 26. Consequently,
m(K) >= 27 ==> X(K) >= 6. The proof below is analytic. It uses no solver, no m = 22
degree-profile enumeration, no eight-shape census, and no pair-sum inequality (C2).
Certificate 0018 remains correct, but its X = 3 case analysis becomes independent
corroboration rather than a necessary dependency. I regard the argument as
mathematically complete and ready for hostile certification. In the repository's
terminology, however, it should be treated as PROPOSED-PROVEN, not yet GREEN, until
independently reimplemented and attacked.

§1. Audit of the existing project. [Claim-by-claim table: floor m >= 22 — agree (the
degree-two cap especially clean); critical cores — agree; m <= 462 sharpened to 456 —
agree; X >= 4 at m = 22 — agree; the 163,682 -> 12,171 X = 4 reduction — agree as an
enumeration statement; the 12,171 configurations as frontier — superseded by the theorem
below. Also independently reconstructed the part-profile field and matched the decisive
published counts, including the 67 admissible part profiles.]

Minor documentation errors (none affecting theorems): (1) Certificate 0018's dependency
table still lists "0015 (2)–(3) + L1.2" in its X >= 4 row although its own audit later
says Lemma 1.2 was an inflated, unused dependency struck from the ledger — remove
"+ L1.2" from that table entry. (2) PLAN.md says "Eighteen certificates, each green ×2"
and immediately says 0004 is never-green scaffolding; the accurate wording is "seventeen
green certificates plus 0004 never-green scaffolding". (3) Certificate 0017 correctly
proves the 4/3 corner at X <= 5, but two honesty notes say, too broadly, that nothing is
claimed at X = 5 beyond the corner's failure; what is open is the constant-one/end-to-end
CC+ conclusion at X = 5 — the 4/3 corner is already certified.

§2. Notation and certified inputs. Let K be an edge-critical core with m edges. Write
d(v) = deg_K(v), lambda(e,f) = |e ∩ f|, pair excess q_ef := lambda(e,f) − 1 >= 0. Then
X = Σ_{{e,f}} q_ef, x_e = Σ_{f≠e} q_ef, Σ_e x_e = 2X. Let D := Σ_v (d(v)−5)_+ be the
total degree mass above five, and define R := Σ_{{e,f}} lambda(lambda−1) = Σ q(q+1).
Certified inputs used: m >= 22, d(v) >= 2, n := |V(K)| >= 36, n_2 <= floor(m/2), and the
moment identities Σ d(v) = 6m, Σ C(d(v),2) = C(m,2) + X. (M)

**Write w(d) := Φ(d−1, 5).** Thus w(d) = 0 (d <= 6), w(7) = 1, w(8) = 2, w(9) = 3,
w(10) = 4, w(11) = 5. Certificate 0017 gives, for X <= 4: Σ_{v∈e} w(d(v)) <= X − x_e for
every edge e (CC4). This is the only critical-cover inequality needed for the X >= 5
theorem.

§3. The star–edge collision lemma. Lemma 1 (local defect–hub bound): in an intersecting
r-partite r-uniform hypergraph, for z ∉ f: d(z) <= (r−1) + Σ_{{e,g}⊆E(z)} (lambda(e,g)−1)
(DH); at r = 6, d(z) <= 5 + X − x_f (DH6). Proof: every edge through z meets f; z's part
excludes f's vertex in that part, so only the other r−1 cells of f are available; with
r_u = #z-edges containing u: d(z) <= Σ_u r_u; at most r−1 nonzero; a <= 1 + C(a,2);
Σ_u C(r_u,2) = Σ_{{e,g}⊆E(z)} |e ∩ g ∩ f| <= Σ (lambda−1). ∎
Lemma 2 (global star-collision): D <= R (SC). Proof: no vertex is universal (tau = 6);
for each z choose an edge avoiding it; (d(z)−5)_+ <= Q_z := Σ_{{e,g}⊆E(z)} q_eg; summing,
Σ_z Q_z = Σ q·lambda = Σ q(q+1) = R. ∎ In rank r: Σ_v (d(v)−(r−1))_+ <= Σ lambda(lambda−1).

§4. Three elementary degree inequalities. (A) for 2 <= d <= 9:
(d−5)_+ >= −(7/6)d + (1/3)C(d,2) + 5/2 − (1/2)[d=2]; slacks 0, 0, 1/6, 0, 1/2, 2/3, 1/2, 0.
Whenever all degrees <= 9, summing (A) with (M): D >= L_X(m) := −7m + (C(m,2)+X)/3 + 90
− (1/2)floor(m/2) (L), increasing for m >= 22. (B) for 2 <= d <= 7:
C(d,2) <= 4d − 9 + 2[d=2] + 2[d=7]; positive slack one unit at d = 4, 5 only. If all
degrees <= 7 and n_7 <= 1: C(m,2) + X <= 24m − 324 + 2 floor(m/2) + 2 (U). (C) for
2 <= d <= 8: (d−5)_+ >= −(7/4)d + (1/2)C(d,2) + 15/4 − (3/4)[d=2] − (3/4)[d=8]; slacks
0, 0, 1/4, 0, 1/4, 0, 0. If all degrees <= 8 and n_8 <= 1, at X = 4:
D >= −(21/2)m + (1/2)(C(m,2)+4) + 135 − (3/4)floor(m/2) − 3/4 (R4); at m = 22 the right
side is 25/2, increasing; hence D >= 13 (R4').

§5. Excluding X = 0, 1, 2, 3, 4.
5.1 (X = 0, 1, 2): X = 0: any f has x_f = 0, so DH6 and CC4 give every degree <= 6.
X = 1: f an endpoint of the unique excessive pair: x_f = 1, again every degree <= 6.
X = 2: f with x_f >= 1: X − x_f <= 1; outside degrees <= 6, at most one degree-7 on f.
L gives L_0(22) = 15/2, L_1(22) = 47/6, L_2(22) = 49/6; D lower bounds 8, 8, 9 against R
upper bounds 0, 2, 6 (partitions of X). Each row contradicts D <= R. Hence X >= 3 — this
already fills the old arithmetic-free rungs m = 23..26: no core anywhere in the window
has X <= 2.
5.2 (X = 3): if every x_e <= 1, the excessive pairs form a 3-matching, R = 6; a positive
edge f has X − x_f = 2, Delta <= 8, and D >= ceil(17/2) = 9 > 6. Else some x_f >= 2:
X − x_f <= 1, every degree <= 7, n_7 <= 1; (U) with X = 3 is impossible for all
m >= 22 except equality at m = 26 (even-m difference (m−25)(m−26)/2; odd-m
(m²−51m+652)/2, discriminant −7). The m = 26 equality case: equality forces n = 36,
n_2 = 13, n_7 = 1, n_4 = n_5 = 0, census (13, 3, 19, 1); per-part (six active vertices
per part, degree sums 26): profiles (6,6,6,3,3,2) ×5 and (7,6,6,3,2,2) ×1 assemble to
(7, 11, 17, 1) ≠ (13, 3, 19, 1). Dead. X = 3 impossible at every m >= 22.
5.3 (X = 4): all x_e <= 1: 4-matching, R = 8; positive f gives Delta <= 9;
D >= ceil(53/6) = 9 > 8. Some x_e >= 3: X − x_e <= 1, (U) with the left side one larger —
even the m = 26 equality disappears. Remaining: max x_e = 2: f with x_f = 2: Delta <= 8,
n_8 <= 1; all q <= 2 so R <= 2·(2·3) = 12; (R4') D >= 13 > 12. Dead.
THEOREM A: every critical core with m >= 22 has X >= 5. Dependency ledger: the floor,
minimum degree 2, six active vertices per part, the degree-two cap, the moment
identities, 0017's constant-one corner/CC4 at X <= 4. NOT used: 0018, the eight-shape
census, the 12,171 field, C2, the pinned Delta <= 9 ladder, a solver.

§6. The X = 5 layer is confined to 22 <= m <= 26. Certificate 0017 proves at X <= 5 the
corner a·b <= (4/3)(s−1); combining with the already-certified pigeonhole and accounting
steps gives Σ_{v∈e} w(d(v)) <= I_e <= (4/3)(5 − x_e) (CC5-4/3) — this does not assume the
open constant-one CC+ at X = 5. The linear law gives at X = 5: 2m + 5x_e <= 67 (C3-5);
Σ x_e = 10 forces m <= 31; m = 29, 30, 31 give x_e <= 1; m = 27, 28 give x_e <= 2.
6.1 (m = 29..31): every x_e <= 1: 5-matching, R = 10. Positive f: outside-degree bound 9;
edge budget Σ w <= floor(16/3) = 5, so every degree at most eleven and globally at most
one vertex of degree >= 10. (D) for 2 <= d <= 11: (A)'s bound − 2[d>=10]; summing:
D >= L_5(m) − 2; at m = 29: 17 − 2 = 15 > 10. Dead (30, 31 larger).
6.2 (m = 28): all <= 1: D >= ceil(38/3) = 13 > 10. So some x_e = 2: outside <= 8, budget
(4/3)(3) = 4: Delta <= 10, n_10 <= 1; q <= 2 so R <= 14, equality only at (2,2,1). (E)
for 2 <= d <= 10: (A)'s bound − (5/6)[d=10]; summing at (28, 5): D >= 83/6; D = 14 = R
forced, slack exactly 1/6, realized only by one degree-4 vertex, n = 36, n_2 = 14,
n_10 = 1, n_6 = n_7 = n_8 = 0; then D = 5 + 4n_9 = 14 insoluble. Dead.
6.3 (m = 27): all <= 1: D >= ceil(67/6) = 12 > 10. So some x_e = 2: Delta <= 10,
n_10 <= 1, R <= 14. (F) for 2 <= d <= 10: (d−5)_+ >= −(6/7)d + (2/7)C(d,2) + 10/7
− (5/7)[d=10]; slacks 0, 2/7, 2/7, 0, 3/7, 4/7, 3/7, 0, 0. Summing at (27, 5):
D >= 95/7; D = 14 forced, slack exactly 3/7: one degree-6 XOR one degree-8 vertex, no
3/4/7, n = 36, n_10 = 1. Case 8: D = 5 + 3 + 4n_9 = 14 insoluble. Case 6: n_9 = 2;
remaining degrees {2, 5}: n_2 + n_5 = 32, 2n_2 + 5n_5 = 128, n_5 = 64/3 impossible. Dead.
THEOREM B: X = 5 ==> 22 <= m <= 26. Combined: 22 <= m <= 26 ==> X >= 5;
27 <= m <= 456 ==> X >= 6.

§7. Margins and likely certificate teeth. The X = 4, x_e = 2 branch closes by one unit
after integrality; both the degree-two cap and the one-degree-8 local cap are
independently load-bearing (n_2 relaxation lowers 12.5 to 11.75; two degree-8s the same).
The X = 3, m = 26 branch has zero slack in the moment bound; the contradiction arrives
only through the six-part census. The X = 5, m = 28 and m = 27 branches land at
D = R = 14 exactly and die by equality-census obstructions (5 + 4n_9 ≠ 14; degree-sum
divisibility). Mutation targets: five cells -> six in Lemma 1; q(q+1) -> q²; the
degree-two cap relaxed by one; the n_8 <= 1 / n_10 <= 1 local caps relaxed; integrality
removed; the m = 26 per-part equality check skipped.

§8. Recommended Certificate 0019: "the star-collision inequality: every critical core
has X >= 5, and X = 5 is confined to m <= 26". Trust chain: derive and synthetically
test the defect–hub construction; prove the global star-collision identity D <= R;
exhaustively verify pointwise inequalities (A)–(F); eliminate X = 0, 1, 2; eliminate
X = 3 including the m = 26 equality profile; eliminate X = 4; use the certified 4/3
corner and C3 to confine X = 5; controls reproducing the existing m = 22 field counts
(control-only); mutation/margin suite. The dependency ledger should say: consumes the
floor, (A), (B), (D2), private covers, C1, C3; does not consume 0018; does not consume
C2; uses no solver or exterior algebra; the X = 5 argument consumes the 4/3 corner, not
the open constant-one CC+ claim.

§9. The new practical frontier: no longer m = 22, X = 4 (12,171 configurations) but
22 <= m <= 26, X = 5. The excess multiset has total weight five: partitions (3,2),
(3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1) after the x_e >= 4 branch is eliminated by the
same degree-moment argument. Suggested order: classify the weighted excess multigraphs;
apply the defect–hub bound per edge class; apply the 4/3 per-edge budgets; use D <= R to
force heavy vertices into shared sets; only then intersect with the part-profile field.

§10. Holy Grail status: no counterexample or complete proof of Ryser r = 6 here; the
public status remains unresolved (the standard survey records the intersecting case
known through r <= 5). But: the finite window remains sound; the old four
arithmetic-free rungs are no longer excess-free; every possible core has X >= 5; every
core above m = 26 has X >= 6; the entire X <= 4 universe disappears without a field
scan; the only remaining minimum-excess campaign is X = 5 on five edge counts.
Recommendation: make the star-collision argument Certificate 0019 before spending more
effort on the 12,171 X = 4 configurations. Those configurations are no longer the
frontier.
