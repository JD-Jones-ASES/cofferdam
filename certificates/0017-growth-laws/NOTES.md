# Certificate 0017 — the excess-growth laws: the corner ladder, the linear law, and the second-moment law

**Status: GREEN.** 61 checks + 12 notes, ~13 s, `python3 verify.py`, stdlib only,
no solver, no imports from `lib/`. Green under a bare `/usr/bin/python3` (3.9.6)
and under `python3 -O`, and under 3.14.6 with and without `-O` — all four outputs
byte-identical modulo wall clock. Deterministic (verified across `PYTHONHASHSEED`
0 / 1 / 12345, and from any working directory; it reads nothing from disk).

**There is no m = 22 field scan anywhere in this certificate.** Every claim is
window-wide, and the one m = 22 fact it uses is cited from 0016, not re-derived.

| claim | label |
| --- | --- |
| **(C1) the corner ladder** — c = 1 at X ≤ 4, 4/3 at X = 5, 3/2 always (s ≤ 5); hence **(CC4⁺)** Σᵢ Φ(dᵢ−1, 5−bᵢ) ≤ I_e ≤ X − x_e at X ≤ 4 | **PROVEN-BY-CERTIFICATE** (in-house: 0013, 0015 steps (2)–(3), 0016's (T) generalized; external NONE) |
| **(C2) the unconditional pair-sum** — Σ_e I_e ≤ Σ over excessive pairs of (λ−1)·Σ_{u∈f∩g}(deg u − 2), **for any X, no hypothesis on a_e** | **PROVEN-BY-CERTIFICATE** (in-house: 0013 (3a) only; external NONE) |
| **(C3) the linear law, per edge** — 2m + 5x_e ≤ 52 + 3X on **every edge of every critical core, at every m** | **PROVEN-BY-CERTIFICATE** (in-house: 0013, 0015 steps (1)–(5); external NONE) |
| **(C4) the global law + integrality lift** — X ≥ 2m(m−26)/(3m−10), and 2X ≤ m·⌊(52+3X−2m)/5⌋ | **PROVEN-BY-CERTIFICATE** (C3 + integrality; external NONE) |
| **(C5) the coupling** — X ≤ 2 ⟹ m ≤ 26 (C4 alone); X ≤ 4 ⟹ m ≤ 28 (**C4 + C1**) | **PROVEN-BY-CERTIFICATE** |
| **(C6) (G), the second-moment law** — 2·(6m·ψ̂(μ)) ≤ 3(m−2)X; **X ≥ 2259 at m = 456** | **PROVEN-BY-CERTIFICATE** (in-house: 0015's global (CC), two moment identities, convexity of ψ, Jensen; external NONE) |
| **(C7) the combined window profile** — X ≥ 1 on **431 of the 435** m in [22, 456] | **PROVEN-BY-CERTIFICATE** (+ 0016's X ≥ 3 at m = 22, transitively its ledger) |

## Why this certificate exists

Certificates 0015–0016 are **m = 22 statements**: their lemmas are m-free but
their kills are field scans at the window floor (0013/0014 are the window's two
halves — floor consolidation and ceiling — not m = 22 kills; ERRATUM 2026-07-28,
this sentence originally lumped them in as "0013–0016", caught by the outside
audit). 0017 is the opposite shape — it
carries **no field scan at all** and quantifies over the whole window at once.

The mechanism is one relaxation and one convexity argument applied to the same
chain 0015 already certified. Relax Φ(dᵢ−1, 5−bᵢ) **linearly** and the row sum
Σᵢ dᵢ = m + 5 + x_e turns plain (CC) into a per-edge inequality between m, x_e
and X. Relax it by **convexity** instead — keeping ψ(d) = Φ(d−1,5) whole and
pushing it through Jensen at the slot mean — and the same chain becomes
quadratic. The two are branches of one law with a measured crossover:

> the **linear** law owns the bottom (vacuous below m = 27, first bites there),
> the **second-moment** law owns the top (vacuous below m = 32, ties at m = 65
> and 66, takes the lead at **m = 67** and never gives it back).

**The problem was already finite. It is now finite AND nonlinear across its whole
width**: X ≥ 1 on 431 of the 435 admissible m, X ≥ 1000 from m = 309 up, and
X ≥ 2259 at the ceiling — 7.8× what the linear law alone gives there.

## The ledger, in full (transitively)

| input | what is consumed | where |
| --- | --- | --- |
| **0013** | criticality; private minimum 5-covers T_e; **(3a)** e ∩ T_e = ∅ and T_e ⊆ V(K) | C1 (a+b ≤ s), C2, C3 |
| **0015 step (1)** | covering: bᵢ = 5 forces dᵢ = 1 | C3 — **and this is the branch that is load-bearing**, §4 |
| **0015 steps (2)–(3)** | the pigeonhole Σᵢ Φ ≤ I_e and the accounting identity I_e = Σ a·b | C1, C3 |
| **0015 plain (CC)** | 2 Σᵢ Φ ≤ 3(X − x_e), summed to 2W ≤ 3(m−2)X | C3, C6 |
| **0016 (T)** | the three-distinct-pairs excess accounting, **generalized off a = 2** to X ≥ 2(a−1) + (s−1) | C1 |
| **0016's X ≥ 3 at m = 22** | one table entry in C7 — and hence, transitively, 0016's own ledger (field 0005/0009/0012, (D2) 0008, 0015's X ≥ 2) | C7 only |
| **external** | **NONE.** No peer sketch, no citation, no published lemma. | — |

C2 consumes **only** 0013 (3a) — not (T), not intersecting-ness beyond λ ≥ 1, not
the 6-uniform cap s ≤ 5. §9 and §10 (the τ = 5 objects) are **CONTROL-ONLY**:
they can redden this certificate, never green it.

**Lemma (A) of 0005 is deliberately NOT spent.** The bᵢ = 5 branch of C3 is
closed by covering alone (0015 step (1)), so C3 holds for any intersecting family
with private covers, critical or not. The turn-13 census lane flagged this branch
as an unnamed side condition and proposed (A) as the cheapest source; the desk
took the cheaper-still route and says so in check 25 (the 9,015-failure teeth are check 24).

## Margins and teeth (D-035 — every coordinate, one named)

**M2, the relaxation coordinate, is binding, and it is not the headline.**

| coordinate | measured | binding? |
| --- | --- | --- |
| **M1** per-m slack of the summed chain, (3m−10)X − 2m(m−26) | **302** at (456, 289), 1,660 at (456, 290) | no — the headline, and it only measures the *relaxed* law against its own floor |
| **M2** the Φ-vs-linear relaxation, Σᵢ Φ − (Σᵢ dᵢ − Θ − 5) | **7 per edge, uniformly**, on all 14 edges of the τ = 5 core; **483 per vertex** at m = 456 (ψ(78) = 555 vs 78 − 6 = 72) | **YES.** The law's entire distance from truth lives here, and (G) is what recovers it |
| **M3** the corner constant c | the ladder moves m = 27..31 from 3,3,4,5,5 to **3,4,5,5,6** | 1–2 units per rung at the bottom |
| **M4** the consumed cap σ = \|T_e\| | Θ = 5σ + 1, so **±1 in σ is ∓5 in Θ**; at Θ = 31 the whole column 27..31 collapses to 0,0,0,0,0 | σ = 5 is *forced* by criticality, not assumed — but the sensitivity is stated |
| integrality | exactly **one unit** at the ceiling (290 vs 289; 294 vs 293), 1–2 per rung at the bottom (m = 27: 3 vs 1) | — |

**And what enactment can and cannot price, said plainly.** The tightest real
object this lab can build sits at (m, X, x_e) = (14, 0, 0) and needs only
2m + 5x_e = **28**. Replacing the τ = 5 constant 42 by 27 goes red on it; *any*
constant ≥ 28 survives every object available. **Enactment pins the τ = 6 constant
52 only within [28, 52]. The constant rests on the derivation, not on enactment.**

**Enactment cannot price (G) at all.** Everything constructible here has m ≤ 25
and (G) is vacuous below m = 32. Its teeth are therefore three **mutants**, each
asserted in-run:

- **the ψ-index shift** — reading the ψ row as starting at d = 0 rather than
  d = 1 inflates the m = 456 floor from 2259 to **2323**, sixty-four units of pure
  overclaim in the direction that flatters the answer. ψ is *derived* from Φ in
  the checker so it cannot be written by accident; if it were, **four checks**
  redden together.
- **ψ(⌈μ⌉) is unsound** — witness: nine 6s and one 7 have Σψ = **1** while the
  rounded form claims **10**. Coded that way (G) reads a fake 2291.
- **ψ(⌊μ⌋) is sound but weaker** — 2230 against 2259. **The piecewise-linear
  interpolation is worth 29 units**, so the `rem·(ψ(d+1) − ψ(d))` term is
  load-bearing, not decoration.

**And (G) has no criticality tooth.** The 25-edge truncated PG(2,5) violates the
linear law by 8 units per edge and satisfies (G)₅ at **margin exactly zero** (its
slot mean is exactly 5). The linear law's single best tooth is invisible to (G);
that is why (G) carries its own.

**The one genuine margin-zero real object** is the τ = 5 rehearsal core: at X = 0,
(G)₅ forces Δ ≤ 5 and the core has Δ = **exactly 5**. One degree higher and (G)₅
would have killed a genuine edge-critical core.

**Other teeth, each asserted:**

- **criticality is load-bearing, and the mutant is exhibited, not imagined.** The
  un-pruned 25-edge truncated PG(2,5) is 6-partite, 6-uniform, intersecting,
  τ = 5, X = 0, m = 25 — and violates the τ = 5 per-edge law by 8 units on every
  edge. It escapes because, **exhaustively over all C(24,5) = 42,504 five-subsets
  disjoint from each of its 25 edges (1,062,600 subsets), not one edge admits an
  e-avoiding 5-cover.** That is 0013 (3a) read backwards.
- **the bᵢ = 5 branch is not a formality.** On the 27,027 excluded states the
  relaxation step is **false 9,015 times**, worst gap **9**
  (b = (0,0,0,0,0,5), d = (6,6,6,6,6,10): left side 0 against a required 9).
- **the (λ−1) factor in C2 is load-bearing** — dropping it makes the pair-sum
  false on **1,306** of 4,819 codegree-3-triangle systems.
- **the c = 4/3 rung is load-bearing** — with only c = 1 the m = 31 rung reads 5,
  not 6.
- **s ≥ 1 is load-bearing** (at s = 0 the corner reads 0 > −1), and it holds
  because K − e is a subfamily of an intersecting family.
- **seven single-point sabotages** were run against the finished checker at the
  desk — ψ shifted, the excess accounting stripped to (s−1), −31 → −30, 52 → 53,
  Jensen → ⌈μ⌉, Θ 26 → 25, and 42 → 52 at t = 5. **All seven turn the run red**
  and exit 1, reddening 1 to 13 checks each.

## THE OPEN FLAG — and it is the loudest thing in this document

**Whether (CC⁺)'s END-TO-END conclusion survives at X = 5 is OPEN.**

What is proven is that the **c = 1 corner** dies at X = 5 — the 4/3 rung of C1
holds there, and C2/C3 are X-unrestricted — and the certificate exhibits
the repaired witness (§2, check 13–15):

```
e   = (0,0,0,0,0,0)
f   = (0,0,1,1,1,1)
g   = (0,0,1,1,2,2)
T_e = {(2,1),(3,1),(4,1),(4,2),(5,1)}     |T_e| = 5, T_e ∩ e = ∅,
                                           T_e ⊆ V(K), T_e covers K − e
X = 5   x_e = 2   (a,b,s) = (2,2,4)
a·b = 4 > s − 1 = 3          THE CORNER FAILS
I_e = 4 > X − x_e = 3        THE MIDDLE STEP FAILS
2ab = 8 ≤ 3(s−1) = 9         plain (CC) survives
Σᵢ Φ(dᵢ−1, 5−bᵢ) = 0 ≤ 3     THE END-TO-END CONCLUSION HOLDS
```

The witness's left side is **zero**, so it bounds the **proof method** and not the
**statement**. A 120,000-trial hunt by the phase-2 refuter found no end-to-end
counterexample — *and zero enactments with a positive left side*, so that hunt has
no teeth either. **There is no evidence in either direction, and this certificate
claims none.** Saying "the true threshold is X ≤ 4" without saying which of the
two statements is meant would be label drift of exactly the 0015-check-18 / D-034
shape, and it is not said here.

Two further scope facts about the witness, both asserted: it is an **abstract
corner object**, not a critical core (with m = 3 its τ(K−e) is 1, so T_e is a
5-cover but not a minimum one); and the originally circulated T_e used three
cells no edge of K carries — repaired in-house by the phase-2 refuter.

## Addendum against certificate 0016 §6 — an addendum, NOT an erratum

0016 §6 derives the pair-sum under "a_e ≤ 1 by (T)", which at X ≤ 2 **is true**.
That derivation is **correct** — it is merely not minimal. C2 removes the
hypothesis outright: `a_e·b_e ≤ a_e(λ−a_e) ≤ a_e(λ−1)` needs only 0013 (3a), and
`Σ_{e∉{f,g}} a_e = Σ_{u∈f∩g}(deg u − 2)` is an exact swap of two finite sums.
**No 0016 check condition and no 0016 conclusion changes**, so no erratum is owed
and none is filed. The addendum belongs in 0016's NOTES.

(The separate 0016 erratum — §9's "(CC⁺) is UNAVAILABLE at X = 3", false as
written — was applied with this certificate and is recorded in 0016's NOTES. This
certificate supplies the replacement fact: the corner survives through X ≤ 4 and
first fails at X = 5.)

## Adversarial record

**Phase 1 — three derivation lanes, and a desk slip caught.** The growth-law
lane, the census lane and the desk re-derivation. Two findings the desk did not
have: **(CC3⁺) is really (CC4⁺)** (the desk stopped one rung early), and **the
linear law is the wrong law above m ≈ 67** — the same certified ingredients give
a quadratic bound. The census lane also caught **an unnamed side condition**: the
relaxation step is *false* when bᵢ = 5 meets dᵢ ≥ 2, an omission of exactly the
Φ(8,5) shape that turn 12 paid for. Both are now checks (23, 24).

**Phase 2 — refuter with four BREAKs, and a blind numeric re-derivation.**

- **Refuter (SOUND-WITH-REPAIRS), four breaks, none fatal, all repairing the
  spec rather than the mathematics.** (i) **The ψ table circulated at the desk was
  off by one index**, which coded as printed inflates (G) at m = 456 from 2259 to
  2323 — *an error that flatters the expected answer*, the lab's named worst
  failure mode. (ii) **X ≤ 4 ⟹ m ≤ 28 is not a contrapositive of the lift**: the
  lift alone admits (m, X) = (29, 4), and the rung's real ledger is the lift **+
  the c = 1 corner**. Printed in-transcript, both ways, in check 36. (iii) The
  X = 5 witness's T_e **was not inside V(K)** — repaired in-house. (iv) The same
  witness **refutes the middle step, not the statement** — hence the open flag
  above. Also: (G)'s feasible set is an **interval**, not an up-set, so the floor
  must be found by scanning from X = 0 and the upper branch must be shown inert;
  and **C2 is not uniformly stronger than plain (CC)**.
- **Blind numeric re-derivation (independent).** Rebuilt the whole numeric surface
  from the stated definitions without reading the derivation, and reported **two
  models** for ψ — model A (the desk's printed table) and model B (ψ derived from
  Φ). The models disagree at every (G) value: 96/422/984/**2323** against
  83/396/942/**2259**, and on the crossover (m = 26 against m = 67) and on the
  window profile (X ≥ 100 from m = 102 against m = 108). **Resolved to model B**,
  which is the true Φ: ψ(6) = Φ(5,5) = 0 because five singletons collide nowhere.
  Every number in this certificate is model B, and check 44 pins model A as the
  mutant it is. The blind lane reproduced the linear column (3/3/4 at 27/28/29,
  290 at 456, 294 at 462) and the C5 rungs exactly, in model-independent
  arithmetic.

**Every pinned constant in this certificate was reproduced by at least two
independent implementations before it was pinned**, and re-measured by this
checker at run time — with one class of exception, stated: the **§2–§3 enactment
tallies** (family counts, tight counts, mutant-failure counts, comparison
splits) are **single-implementation regression pins**. They are deterministic and
reproduce under 3.9.6 and 3.14.6 and under `-O`, but they were measured by this
generator design alone, and the certificate claims nothing more for them.

**One honest scope limit inside the enactments.** The pair-sum is never tight in
this run — 2,570 systems with T_e chosen **exhaustively to maximise I_e** leave
a minimum slack of **6**. The phase-2 refuter *did* reach equality, in 54 of 350
families under its own adversarial-cover design, so the bound is attainable; that
is recorded as **the refuter's measurement, not this checker's**, and is not
re-quoted as if this run had produced it.

## Two facts about the lifted law that a reader will otherwise get wrong

Both are asserted in-run (checks 32, 33):

1. **The lifted predicate is not upward-closed in X.** At m = 26 the value X = 1
   is *forbidden* while X = 0 and X = 2 pass; at m = 94, X = 48 is forbidden while
   47 and 49 pass. **The minimum must be found by scanning from X = 0** — never by
   bisection.
2. **It is not monotone in m.** The floor at m = 93 is **48** and at m = 94 it is
   **47**. A bigger core can be admitted at a smaller excess.

And a third, on the easy corollary: the **some-edge form** 3X ≥ 2m − 47 ties the
full lift on all of m = 27..92 and again at 94 (67 values), first falls strictly
below at **m = 93**, and is strictly weaker from **m = 95** onward. Quote it for
its one-line proof, never for its strength.

## What this does not claim

Nothing about existence — every law here is conditional on a critical core at
that m. At X = 5, nothing beyond what C1–C3 already state — the c = 1 corner
fails (witness), **the 4/3 corner holds**, and C2/C3 carry no X restriction;
the OPEN item is (CC⁺)'s constant-one end-to-end conclusion, §"THE OPEN FLAG".
(ERRATUM 2026-07-28: this sentence and the OPEN-FLAG opener originally said
"nothing at X = 5 beyond the corner's failure" — a deflation of the
certificate's own C1: the 4/3 rung IS an X = 5 claim, certified. Caught by
the second outside audit. No check touched.) And the laws are **vacuous
on m ∈ [23, 26]**, which is named in check 47 rather than buried: those four
integers are the only m in the whole window where the arithmetic forces
*nothing*, and the field campaign must do that work by hand.

**Never quote m²/90.** The asymptote **overstates** at finite m — 2310.4 against
the true 2259 at m = 456 — and is approached from below, crossing only near
m ≈ 1000. It is a note about the shape of the law, not a bound.

## Tally

61 checks, 12 notes (stated-not-tested facts). Sections: 1 Φ, ψ and the linear
floor (6) · 2 the corner ladder and the X = 5 witness (9 + 2 notes) · 3 the
unconditional pair-sum (6 + 4) · 4 the per-edge linear law (6) · 5 the summed law
and the lift (7) · 6 the coupling (2 + 2) · 7 (G) and its mutants (10 + 2) ·
8 the window profile (2 + 1) · 9 the τ = 5 direction control (4 + 1) ·
10 criticality teeth (3) · 11 the margins (6).
(ERRATUM 2026-07-28: this tally originally read "10 notes" with §3 at 3 and §6
at 1; the transcript prints 12 — §3 has 4 notes and §6 has 2. The header's
"61 + 12" was always correct. Counting drift only; no check or note touched.
Caught by the outside audit.)

Runtime: **~13 s** on a bare `/usr/bin/python3` (3.9.6), **~9 s** on 3.14.6;
`-O` makes no difference to either. Every heavy step reports its own wall clock
in the transcript: the 1,261,260-state relaxation exhaustion **2.6 s**, the
randomized enactments of §2–§3 **0.2 + 1.8 + 0.8 + 2.2 s**, the −31 identity's
200,000 random pairs **1.0 s**, the two floor curves over [22, 462] **0.5 s**,
the (G) moment and Jensen enactments **0.2 + 0.2 s**, the PG(2,5) peel **0.2 s**
and the 1,062,600-subset criticality exhaustion **0.2 s**. The ~3 s balance is
the Φ and 5⁶-pattern exhaustions of §1–§2. No file is read; no network.

## What this opens

**1. The X ≤ 2 box is now four integers wide.** 0016 killed X = 2 at m = 22 and
C5 caps X ≤ 2 at m ≤ 26, so **any hypothetical critical core with X ≤ 2 lives in
m ∈ {23, 24, 25, 26} and nowhere else in [22, 456]**. Those are the same four
rungs where the profile forces nothing. 0016's W ≤ 24 machinery and its per-edge
budgets are m-free — **only the field scan needs re-running at 23, 24, 25, 26.**
That is the cheapest thing on the board.

**2. The X = 3 shape census is banked and points at one shape.** From the turn-13
census and refuter lanes (`t13-census.md`, `t13-refuter.md` — *measured there, not
re-derived here, and deliberately not carried into this certificate, which owns no
field scan*): the eight-shape census at X = 3 is complete, all eight W-bounds
reproduce (48/36/32/30/28/27/27/24), and on the m = 22 field the shape-blind rule
W ≤ 48 cuts 0016's frontier from **15,340 to 1,580 — a 9.7× cut that does not
empty the layer**. The **star is field-dead** (0 survivors). The triangle, the
path P4 and P3+K2 survive on the raw floor with one configuration each and die
only under a **configuration-aware judge that is not yet certificate-grade** —
that distinction matters and is why none of it is claimed here. **1,549 of the
1,580 survivors are consistent with the λ-4 pair alone**: that shape is the whole
frontier, both its edges have x_e = 3 hence budget 0 hence all twelve degrees
≤ 6, and Lemma 1.2 fixes each row sum at exactly 30. That is transversal-level
structure the degree-multiset field cannot see.

**3. (G)'s Jensen step is the new workhorse.** It is the first tool in this
lineage that is *quadratic* in m, and it was built from ingredients already
certified — no new combinatorics. Two immediate extensions: the **b-aware hybrid**
Φ(d−1, 5−b) ≥ max(ψ(d), d−6+b), which would smooth the crossover at m ≈ 67; and,
now that X ≳ m²/90 from below, **any sub-quadratic upper bound on X would cap m
directly** — nothing in the ledger supplies one, and (G)'s own upper branch is
inert by a factor of ten.

## Post-audit repairs (applied at the desk, then re-verified)

The phase-3 hostile audit returned PASS-WITH-FIXES; the desk applied: the M2
slack decomposition now COMPUTES the true Σᵢ Φ on the rehearsal core instead of
hard-coding 0 (the moderate catch); the crossover check asserts a STRICT lead
on all of [67, 462]; two static checks now self-declare; the adversarial-cover
funnel is disclosed in full (75 of 4,000 trials dropped by a near-inert
enumeration cap); the Δ ≤ 9 citation in the complement comparison is marked as
transitive-via-C7; the coupling scan's tail argument (numerator sign for
m ≥ 33) is stated beside the scan; three NOTES cross-references corrected.

## Reproduce

```bash
python3 verify.py
```

~13 s under a bare `python3`, deterministic, exit 0 on green. Runs from any
working directory; reads nothing from disk.
