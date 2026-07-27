# 2026-07-27 · turn 9 — two rungs pinned by hand, and the lever that measurement killed

Append-only. Technical. Failure recorded as failure.

## 0. What this turn set out to do

JD's brief: follow the PLAN, check the work, push the math; the floor moving
is not the goal. Ultracode on, several hours of silicon. The turn opened with
the PLAN queue (Δ = 4 certification; attack X, B_min, g(4) = 8; third N(4)
route) and closed having done some of that and three things not on any list.

## 1. Baseline

All seven certificates replayed GREEN under bare `/usr/bin/python3` 3.9.6 and
under `-O` — 14 runs, 14 exits 0 — before anything was touched.

## 2. Q13 was answered the day it was priced, by an object already shipped

Certificate 0008 ships a 13-edge τ = 5 object W to show (D2) fails one rung
down. Its part 1 is **(4,3,2,2,2) — a full part**. So W is exactly the object
Q13 asks for: **Q13 = YES, N(5) ≤ 13**, and PLAN item 5's 232-slice search
was pricing a hunt for something the repo already possessed. Fresh-code
verification (15 checks): 13 distinct transversal edges, all 78 pairs meet,
τ = 5 exactly by three routes (explicit 5-cover; no 4-cover in C(30,4); an
independent branch-and-bound hitting-set), part 1 the sole full part. A grep
sweep confirmed no document had ever connected W to Q13 — 0008's own turn-8
notebook entry says "Q13: untouched" in the same file that ships the answer.

**Lesson recorded (D-026): inventory your own witnesses.** An object built to
answer one question does not announce what else it answers.

## 3. The m = 12 dead heat, named at last → certificate 0009: g(5) = N(5) = 13

Certificate 0001's counting ladder at t = 5 dies at 10 and 11 and lands on
**exact equality at m = 12**: caps (4,7,9,11), unique maximizing profile
(4,3,2,2,1) at 11 pairs, 6 × 11 = 66 = C(12,2). The arithmetic sat in
0001's check-18 output since turn 1; nothing ever read it back (grep: the
repo's every "dead heat" is 0005's A = 30 one). Equality forces: every part
exactly (4,3,2,2,1), X = 0, no repeated edges. Column form: six shape-
(4,3,2,2,1) partitions of [12] tiling all 66 pairs exactly once.

That space was exhausted three times today:
- **here**: exact-cover census, first part pinned WLOG — 35,424 compatible
  candidate partitions (enumerator validated against the closed form
  415,800), **11,520 complete designs, every one with an explicit 4-cover**;
- **blind agent 1 (C)**: two structurally different enumerators (exact cover;
  pair-colouring with restricted growth + bin-packing invariant) —
  bit-identical design sets, 11,520; alternate pin gives 11,520 again; all
  11,520 validated by a third-party script; τ = 4 exactly for every design by
  exhaustive ≤ 3 refutation; 10 free Stab-orbits of 1152;
- **blind agent 2 (Python, different route)**: column-by-column with a
  τ-prune (decides the claim without a census) + Stab(P0) orbit reduction —
  zero τ ≥ 5; prune-off control reaches 58 reduced designs whose
  orbit-weighted count is 57,600 = 5 × 11,520 exactly; **AG(2,3) positive
  control** (12 resolutions of K9 into triple classes, the theory number).

So **m = 12 admits no τ ≥ 5 object: g(5) ≥ 13**, and W gives ≤. With N ≥ g:
**g(5) = N(5) = 13, citing nothing** — certificate 0009 (forcing checks,
census, witness, drop-a-cap sensitivities, m = 13 not-too-strong control).

Consequences: the citation-free ladder **equals** the cited ladder; every
cited-ladder sweep in 0006–0008 is citation-free as of today; (L8)'s surface
at m = 21 shrinks 2,478 → 567; the counterexample degree cap tightens to
Δ ≤ m − 13. The floor does not move.

The near-misses were real: blind agent 1's first partition generator produced
332,640 of 415,800 (a canonical-form bug caught by the required closed-form
control before any search ran), and its first second-enumerator prune was
over-strong — 6,912 designs, a flattering subset that would have "confirmed"
the verdict — caught only by diffing design sets rather than headline counts
(D-005 in the wild, twice).

## 4. N(4) = 9 BY HAND → certificate 0010: the hinge is no longer a search

PLAN item 3 asked for a third implementation of the N(4) exhaustion. What
landed is better: a **search-free proof**, found by a three-angle subagent
panel (all three angles returned complete proofs; the shipped one re-derived
line by line at the desk). Route: full part = (2,2,2,2) (four married
pairs) · degrees ≤ 3, same-part top two ≤ 5 · pair count admits exactly
three cases (X ≤ 1) · any two triples intersect (else the complement pair's
common vertex completes a 3-cover) · every edge lies in a triple
(Σ b_i = 11 + ε) · a double count funnels each case to an r-vector killed in
2–3 lines. The prettiest kill is the last: the marriage the *hypothesis*
forces on the r = 4 edge is exactly what the excess budget cannot afford.

Certificate 0010: 24 checks + 3 notes, 33 s — the finite enumerations, plus
**independent structure-level sweeps killing every case again** (zero
qualifying 4- and 5-triple systems in C(8,3); the 10,080 A-η1 systems all
die on the matching step), a budget-relaxation teeth control (12,500 passes
appear the moment one unit of slack is allowed), and the 9-edge witness
re-verified (τ = 4 exactly, part 1 = (3,2,2,2)). N(4) = 9 now has three
independent legs: theorem + two searches. The third angle's stronger claim —
every part of an 8-edge τ ≥ 4 object carries a degree-1 vertex, i.e. the
corrected-AKP-2.8 consequence by hand — is recorded as fleet-claimed, next
in the re-derivation queue.

## 5. What measurement killed before theory wasted a week: the cap at m = 22

Two independent implementations (one from the code, one from prose alone —
which caught that 0006's prose never states the implicit D ≥ 0 constraint)
agree on every cell of the m = 22 sensitivity matrix:

| ladder N(5) | cap 11 | cap 10 | cap 9 | ... cap 4 |
| --- | --- | --- | --- | --- |
| 11 ≡ 12 | 56,592 | 20,585 | 5,565 | 0 |
| 13 | 30,436 | 11,337 | 3,334 | 0 |

- **N(5) = 11 and 12 are byte-identical at m = 22** (the k = 2 cap already
  forbids a largest entry of 11), so the peeling-vs-g(5) distinction never
  mattered at this rung; 13 bites, killing exactly two profiles.
- **Survivors exist down to D₂ = 5.** Emptying m = 22 by a cap needs
  2·D₂ ≤ 8 = m − 14 — no (D2)-shaped lemma reaches that. 0008's "one unit of
  the cap is worth the whole rung" is an m = 21 statement only. **PLAN item
  1b (the r-dependent sharpening) is hereby priced and declined as a floor
  lever**; the matching structure stays unconsumed for future per-class work.
- Full-field D₂ bands also correct a narrative drift: 0008's "survivors crowd
  the ceiling" holds of its exhibited first-200 only; the full field spans
  D₂ = 5..32.

## 6. (L9) named, proved, audited — D-023's unnamed load-bearer has a name

The water-filling floor for B: over integer c ≥ floors with Σc = A, the
greedy that increments a current minimum attains min Σ C(c_i,2) exactly
(exchange argument; minimizers = levelled-above-floors vectors; value
tie-break-free). Audited: 253,890 exhaustive small instances + 2,000 seeded
n = 15 instances vs an independent DP + **all 6,839 distinct (floors, A)
pairs the certificates actually consult** — 262,729 comparisons, zero
mismatches. Directionality stated: the greedy value sits at a feasible
vector, so the only possible failure mode is the dangerous one (too-high
B_min = false kills); exactness is the entire safety margin, which is why
the audit matters. (L8) survives sound: Bmin enters only as a scan floor.

## 7. The g-ladder's "proven twice" was one proof in two costumes

Instrumented replay of certificate 0001: its "exhaustive absence" searches at
every sub-threshold m execute **exactly one recursive call** — the root
waste-budget prune (6·maxcov < C(m,2)) IS the (L1)+(L2) counting kill. So
the two lower-bound routes were one argument in two code forms, and two 0001
doc claims are false: "counting alone is not tight there" (it is tight
through g(5) — the cert's own ladder_floor returns 3, 5, 8, 12) and "~96 s
dominated by the m = 7 absence check" (that check is 1 node / 0.003 s; the
runtime is the m = 8 witness re-find at 3.7M nodes). Also: g(4) = 8's m = 5
rung lives in section [E] labelled "smoke test" while being load-bearing.

The genuine second leg — a definitions-only brute force (no (L1), no (L2),
Bell-partition columns, only the τ-monotone prune) — confirmed m = 1..6 dead
by real search. **(7,4) did not close: all four root-split quarters hit
their 200M-node limit (800M+ nodes, ~95 min of engine time, no verdict and
no witness).** It stays UNDECIDED and is recorded as such. Perspective for
the risk table: g(4) ≥ 8's *counting proof* is three lines from g(3) = 5,
machine-checked in three certificates today, and is not in doubt — what
D-028 corrects is the claim that a second independent argument existed. The
definitions-only exhaustion remains optional insurance, now priced: this
engine needs either symmetry quotienting or a smarter independent route.

## 8. The grail question, answered honestly: can the floor rise without bound?

JD's brief asked. Three facts, one lead, one verdict.

**Fact 1 — every rung so far is a fixed-m finite argument**, and the base
counting's slack grows against us (0001's table: −3 at m = 18, +9 at 19, +26
at 20). Each rung past 19 has needed a NEW structural lemma ((L7), (L8),
(D2)), and today's sensitivity matrix says no counting-shaped lever visible
in-house reaches m = 22: the cap route needs 2·D₂ ≤ m − 14, the ladder is
pinned at N(5) = 13 forever, and 30,436 configurations survive (L8) there.
Rung-climbing is not converging to a proof; it is buying localisation at
increasing marginal cost — exactly the BRIEF's scope discipline (structure,
not the scalar).

**Fact 2 — the problem is finite in principle, and half the argument is
in-house for free.** A minimum counterexample is **τ-critical**: deleting any
edge of a minimum-m counterexample leaves τ ≤ 5, else a smaller
counterexample. τ-critical hypergraphs carry classical size bounds (Lovász-
style; for r-uniform τ-critical with τ = r the literature has explicit
ceilings). If such a ceiling M were verified, "Ryser r = 6 intersecting" IS
the finite statement "no counterexample in the window [22, M]" — the grail
reframes from 'raise the floor without bound' to 'floor meets ceiling'.
**Lit-check task for a future turn: pull the exact τ-critical bound and its
proof; the constant is expected astronomically far from 22.** Until checked,
this paragraph is literature-context, consumed by nothing.

**Fact 3 — the fractional gap says counting alone can never finish.** For
intersecting 6-partite families the fractional cover number stays small
(literature: τ* ≤ r/2), while a counterexample needs τ = 6; every counting
argument in this repo lower-bounds an integral quantity by fractional-style
budgets, and that gap is exactly where the per-rung structural lemmas have
had to do their work. A uniform-in-m kill would need a lemma whose strength
grows with m — nothing in-house has that shape.

**The lead worth keeping — measured before this entry closed:** the m = 12
dead heat forced an exact tiling structure and the space collapsed, so the
scan for other forcing regimes was run the same day. Answer: **there are
none.** On the pinned ladders the gap (6 × capped max) − C(m,2) is 0 at
(12, 5) and only there — t = 5 jumps to +12 at m = 13; t = 6 crosses from
−9 (m = 19) to +8 (m = 20) without touching [0, 2], then +30, +57, +89
through m = 28, every maximizer of shape (Δ, 4, 3, 2, 2, 2) with Δ
saturating the m − 13 cap. The one free rung has been harvested; what
remains costs structure. Conditioned-class variants (fixed Δ, fixed D₂
band) remain cheap and untried.

**Verdict:** no route visible, here or (to our knowledge, unverified) in the
literature, raises the floor without bound. The floor's value stays what the
BRIEF said: localisation and reusable structure. The finite-window framing
(Fact 2) is the one genuinely new thing this question surfaced.

## 9. Certificate 0011 — Δ = 4 exactly, and a control that fired live

PLAN item 1 closed the same day it was scouted. The scout measured every
piece first (the empirical answer was in before assembly began: the Δ = 5
branch dies at all 30 (residual, part) pairs); an assembly agent built the
certificate from the design; the desk review demoted one literal-arithmetic
check to a note (the D-015 pattern, caught in our own new file — again) and
gates ran clean: **61 checks + 12 notes, 176 s bare / 170 s under `-O`**.

Structure worth remembering: the (8, τ ≥ 4) census (5 classes) is built by
two routes sharing no enumeration — edge-wise growth under an excess prune,
and peel-to-(5,3)-then-reattach through the escape machinery — and **the
A = B control fired during assembly**: a prototype's global index-ordering
bug returned 4 classes, a silently flattering census, caught by nothing
except the second route. The mask-level reduction proves an *iff*, so the
seven recovery controls (peel each degree-4 vertex of W; the same code must
say SOLVABLE) test the direction the kill uses. max_fresh = 1 is derived by
uncapped enumeration at all 30 pairs, not imposed. The three-profile
corollary is stated at its true size: the list was already derivable from
the N(4) cap; the new route consumes g(4) ≥ 8 and g(5) ≥ 12 only and bounds
all six parts. Nothing in 0011 consumes 0009 or 0010 — it re-derives its own
ladder, deliberately, so it does not sit downstream of the hinge.

## 10. What did not get done

- The m = 23 frontier: untouched, deliberately — nothing measured today says
  a counting-shaped lever reaches it.
- The stronger per-part hand claim (§4) not yet re-derived at the desk.
- X and the convexity bound were *audited* (1.86M + 262k zero-failure
  comparisons now stand behind them) but no new attack on X's definition was
  mounted; g(4) = 8 kept its margin-one status and gained the §7 finding
  that its two "independent" proofs were one.
- The definitions-only (7,4) brute force: see §7 status.

## 11. Errors of mine this turn, recorded

1. My first m = 12 enumerator forced the smallest leftover edge into a
   2-block — the singleton case was unreachable. Caught in review before any
   run; the blind C agent independently made (and caught) the same class of
   bug, which says something about the shape.
2. I drafted certificate 0009 with a literal-True check and two "hence"
   checks whose condition was `True` — the exact D-015 pattern this repo
   outlaws — and caught it re-reading the draft before first run.
3. Cert 0009's NOTES were drafted citing the blind reproductions before they
   had returned; had they disagreed, the file was wrong at write time. They
   agreed; the order of operations was still backwards.
