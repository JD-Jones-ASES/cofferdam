# Certificate 0016 — the triangle lemma, (CC⁺), and X ≥ 3 at the window floor

**Status: GREEN.** 45 checks + 8 notes, ~14 s, `python3 verify.py`, stdlib only,
no solver, no imports from `lib/`. Green under a bare `/usr/bin/python3` (3.9.6)
and under `python3 -O`, both with byte-identical output modulo wall-clock.
Deterministic (verified across `PYTHONHASHSEED` 0 / 1 / 12345).

| claim | label |
| --- | --- |
| **(T) the triangle lemma** — distinct e, f, g in an intersecting family with \|f ∩ g ∩ e\| ≥ 2 force **X ≥ 3** | **PROVEN-BY-CERTIFICATE** (external NONE; in-house NONE — self-contained) |
| **(CC⁺)** Σᵢ Φ(dᵢ−1, 5−bᵢ) ≤ I_e ≤ X − x_e for every edge of a critical core with X ≤ 2 | **PROVEN-BY-CERTIFICATE** (in-house: 0013 private covers, 0015 steps (2)–(3), and (T); external NONE) |
| **X ≥ 3 for every critical core at m = 22** | **PROVEN-BY-CERTIFICATE** (field 0005/0009/0012; (D2) 0008; 0015's X ≥ 2; external NONE) |

## Why this certificate exists

Certificate 0015 put a floor under the bottom of the window — a minimum core at
m = 22 must carry excess X ≥ 2 — and left 9,224 X = 2 configurations standing as
the field for the next campaign. This certificate removes that field entirely.

The mechanism is a hypothesis 0015 did not have. 0015's corner
`a·b ≤ (3/2)(s−1)` is tight at (a, b, s) = (2, 3, 5), and that corner **needs
a = 2** — three edges sharing two vertices. By (T) an a = 2 triple by itself
forces X ≥ 3, so at X ≤ 2 the tight corner is unreachable and the true corner is

    a·b ≤ s − 1        (a ≤ 1, a + b ≤ s, s ≥ 1)

proved in **two cases**, never as the one-line chain `a·b ≤ b ≤ s−a ≤ s−1`,
which is false at a = 0. That kills the factor 3/2 in every budget. The budgets
then cap the degrees of exactly the vertices the excess runs through: at X = 2
the excess lives on one λ = 3 pair or two λ = 2 pairs, the edges carrying it have
x_e ∈ {1, 2}, and their whole-edge budgets 2 − x_e force those shared vertices
light. Case arithmetic gives **W ≤ 24** where the un-shaped global form gives
only 40. The field's minimum W under (D2) is **27**. Nothing survives.

**X ≥ 3 for every critical core at m = 22.** Every critical core at the window
floor is nonlinear, with excess at least three.

## The ledger, in full (transitively)

| input | what is consumed | where |
| --- | --- | --- |
| **0005 (A)** | every active vertex has degree ≥ 2 | field profiles; b_i ≤ 4 |
| **0005 (B)** | ≥ 6 active vertices per part | field profiles |
| **0008 (D2)** | 2·#{degree-2 vertices} ≤ m | the kill, §6 — **and it is where the margin is** |
| **0009 / 0012** | the pinned ladder N = 2,4,6,9,13 → prefix caps 9,13,16,18,20 | field profiles |
| **0013** | criticality; private minimum 5-covers T_e; (3a) e ∩ T_e = ∅; T_e ⊆ V(K) | (CC⁺) |
| **0015** | steps (2) pigeonhole and (3) the accounting identity I_e = Σ a·b — **and its certified X ≥ 2**, which is what turns "the X = 2 layer is empty" into "X ≥ 3" | (CC⁺); the conclusion |
| **external** | **NONE.** No peer sketch, no citation, no published lemma. | — |

(T) itself consumes nothing at all: intersecting-ness and counting.
§10, the τ = 5 rehearsal-core enactment, is **CONTROL-ONLY** — it can redden this
certificate, never green it.

## Margins and teeth

- **THE MARGIN IS ONE UNIT OF (D2)**, and it is not where it looks — see below.
- **Not too strong**: at X = 3 the rules that survive — (D2), the ladder's own
  Δ ≤ 9, and *plain* (CC)'s global form W ≤ 90 — leave **15,340** of the 186,086
  X = 3 configurations alive (measured, asserted `> 0`). The theorem stops where
  its evidence stops. The min W over Δ ≤ 8 + (D2) moves from **28** at X = 2 to
  **30** at X = 3.
- **Not too weak**: replace W ≤ 24 by the un-shaped W ≤ (m−2)X = 40 and **286**
  configurations survive. The λ-shape analysis of §5 is worth 16 units of W and
  is the difference between a kill and no kill.
- **The mutant fails, as it must**: drop the (λ−1) factor from the pair-sum and
  the inequality is **false on 119** of the 1,446 random systems that satisfy its
  a_e ≤ 1 hypothesis. The check can go red.
- **(T) has teeth**: 636 intersecting patterns with a = 1 violate the conclusion,
  so a ≥ 2 is load-bearing; and the sharpened corner **fails at a = 2**
  ((2,3,5) gives 6 > 4) while 0015's plain corner still holds there — (CC⁺) is
  *false* without (T).
- **s ≥ 1 is load-bearing**: at s = 0 the corner reads 0 > −1. It holds because
  K − e is a subfamily of an intersecting family. Intersecting-ness is spent
  exactly on the a = 0 branch.
- **The τ = 5 falsification opportunity, taken**: 0013's rehearsal core has max
  degree **5**, one below the degree 6 that would have broken the analog chain
  (at X = 0 the analog budget forces every Φ(dᵢ−1, 4−bᵢ) = 0, hence d ≤ 5), and
  max |f ∩ g ∩ e| over all **364** triples is 1, and W′ = 0.
- **The b_i = 5 well-definedness guard, honestly scoped**: across all 59,276
  padded-cover enactments the largest b_i ever seen is **4** (measured,
  asserted) — the guard is *unexercised* and supplies no evidence. The
  well-definedness of (CC⁺) at b_i = 5 rests on the covering argument alone
  (five cover cells in one part leave the dᵢ − 1 siblings no cell, forcing
  dᵢ = 1), which needs no lemma beyond 0013. The phase-3 audit caught the
  draft presenting this guard as evidence; it no longer does.

## THE MARGIN (D-017): one unit of the (D2) cap

The comfortable reading is *four units of W* — the bound is 24, the field
minimum under Δ ≤ 8 + (D2) is 28. **That is the wrong coordinate to quote.**
Measured in-transcript, §7:

| (D2) cap as `2·D₂ ≤` | 22 (true) | 23 | **24** | 26 | 28 |
| --- | --- | --- | --- | --- | --- |
| configurations with W ≤ 24 surviving | **0** | 0 | **9** | 66 | 218 |

**One additional degree-2 vertex and the theorem does not close.** Equivalently:
W ≤ 24 alone leaves 843 configurations, and the minimum D₂ among them is exactly
**12** — one above the cap of 11. The named near-miss, printed in full by the
checker:

```
(8,5,3,2,2,2) (7,6,3,2,2,2) (6,6,3,3,2,2) (6,6,3,3,2,2) (6,6,3,3,2,2) (6,4,3,3,3,3)
    X = 2   Delta = 8   D2 = 12   W = 23  <=  24
```

It satisfies every other rule this certificate proves. Only 2·D₂ ≤ 22 stops it.

And the maintenance instruction that goes with it: **all three W-minimizers sit
exactly ON the (D2) boundary**, D₂ = 11 = ⌊m/2⌋. If certificate 0008's cap is
ever weakened, the minimum must be recomputed *before* this kill is re-quoted.
The same knife edge 0008 documented at m = 21 has re-appeared one rung up, in a
different argument.

## Erratum against certificate 0015 (same commit)

0015's check-18 **label** originally read "the floor lands at exactly X ≥ 2, not
higher" — a claim about the **floor** where only a claim about **that judge** was
proven. This certificate disbelieves that sentence, so the label is reworded and
an erratum is added to 0015's NOTES, applied in the same commit (verified present
in the working tree: `certificates/0015-cc-x-floor/NOTES.md` "## Erratum
(2026-07-27, applied with certificate 0016)", and the reworded check-18 label in
its `verify.py`). The **check** is untouched and remains true: `alive2 == 9224`
is a fact about 0015's own judge, and that judge at X = 2 reduces to (D2) plus
the global form W ≤ 60 — it simply does not decide the layer. §6 here re-measures
the same field and shows W ≤ 24 empties it.

## Provenance — in-house, and no sketch was consumed

The sharpening is **in-house**. It was found by this turn's derivation fleet and
re-derived at the desk before any of it was written down as a claim. No external
sketch, note or paper contains (T), (CC⁺), the pair-sum, or the constant 24. The
only outside object anywhere in this lineage is the turn-9 review that seeded
*plain* (CC) — already audited, repaired and superseded inside 0015.

## Adversarial record

**Phase 1 — three independent derivation lanes.** The transversal lane, the
cover lane and the desk re-derivation. The lane work caught the desk's own first
sketch of this certificate: it used **Φ(8,5) = 4** and drew the right conclusion
(Δ ≤ 8) from the wrong number. Φ(8,5) is **3**, plain (CC) therefore permits
Δ = 9, and Δ ≤ 8 needs the *sharpened* budget, not the miscomputed Φ. Check 2
pins all four values.

**Phase 2 — three independent attackers, zero fatal findings.**

- **Refuter (SOUND-WITH-REPAIRS)** — reproduced fourteen counts on code written
  without reading the derivation lane's scripts; exhausted (T) over all 15,625
  agreement patterns; found the serious repair: **the stated margin was in the
  wrong coordinate** (4 units of W, when the binding margin is 1 unit of (D2)) —
  precisely the failure mode the lab named at quarry retirement, *an error that
  flatters the expected answer*. Also: the draft's teeth for the pair-sum were
  vacuous on the left (W = 0 in every X ≤ 2 random family), and supplied the
  heavy-star design that fixes it — now checks 13–15. Also corrected a sabotage
  suggestion inherited from 0015: an s = 6 teeth-test guards *plain* (CC), not
  (CC⁺), whose only breaking points are a = 2 and s = 0.
- **Blind re-deriver (SOUND)** — worked from the two axioms alone, never opening
  the derivation. Reached **W ≤ 24** independently, with the same case split
  (24 / 16 / 18), and reproduced 67 / 210,713 / 9,224 / 506,204 / min W = 28 /
  3 minimizers / 0 survivors. Zero disagreements. Also supplied the rung-down
  controls, which reprove 0015's X ≥ 2 by a different route — a real cross-check
  that would have gone red on a sign or factor error.
- **Reimplementation (SOUND-WITH-REPAIRS)** — fresh code from the stated
  definitions; every published count exact, by three separate computations (DFS,
  multiset-counting DP, and a (size, score, D₂, W) DP). Found the **Δ ≤ 8
  redundancy**: W ≤ 24 implies Δ ≤ 8 on its own (a degree-9 vertex contributes
  27 > 24), so presenting Δ ≤ 8 as a stage of the kill inflates the apparent
  work and mis-prices the budget derivation. Check 21 and check 36 now state the
  redundancy plainly instead of leaning on it.

**Phase 3 — hostile audit of the drafted checker (PASS-WITH-FIXES, no
fatal).** The draft was written to a binding desk spec and then audited by an
independent agent: label-drift hunt over all 45 checks, pin audit against the
phase-2 reports, style/determinism verification, and **20 single-point
sabotage mutations — 17 turned the run red, and each of the 3 inert ones was
proven inert by theorem** (e.g. tightening W ≤ 90 to 89 at X = 3 changes
nothing because the maximum W among survivors is 88). Fixes applied at the
desk after the audit:

- **The enactment was quietly weaker than its label** — the substantive catch.
  The draft's cover search returns covers of size ≤ 5 (mostly 1–3), while the
  Φ terms were computed against 5 − bᵢ classes regardless, systematically
  *understating* the pigeonhole's left side. Repaired by **padding every
  cover to exactly five cells** (a superset of a cover is a cover), making
  the enactment literally (CC⁺); re-pinned honestly: 175 tight enactments
  (was 104 under the weak form), 5,980 heavy-star systems (19 skipped as
  unpaddable, said so), 56,584 enactments, 54,119 with positive left side.
  The audit verified zero failures survive the honest strengthening.
- The vacuous b₁ = 5 guard demoted to a measured-scope statement (above).
- The inert Δ ≤ 9 clause at X = 3 asserted inert rather than priced as a rule.
- The Δ-free minimum's "single degree-9 vertex" now asserted (3 minimizers,
  census (0, 0, 1)), not just stated; the X = 1 case bound W ≤ 8 exhausted by
  loop rather than prose; generator funnels disclosed (40,000 / 6,000 /
  20,000 LCG trials); "byte-for-byte" softened to what is literally true.

**Every field constant in this certificate was reproduced by at least two
independent implementations before it was pinned**, and re-measured by this
checker at run time. The §3 *enactment* counts (tight/positive/system tallies)
are single-implementation regression pins: deterministic, reproduced under
3.9.6 and 3.14.6 and under `-O`, but measured by this generator design alone —
the certificate does not claim more for them.

### One honest discrepancy, carried rather than smoothed

The desk's spec pinned **5,384** as the count of "intersecting patterns with
distinct edges and a ≥ 2", and glossed distinctness as "e ≠ f iff some coordinate
separates them". Those two do not agree. 5,384 is the count of intersecting a ≥ 2
patterns **minus the single fully degenerate e = f = g**; applying the stated
distinctness rule to all three pairs gives **5,216**, the other 168 having exactly
two of the three edges equal. Both numbers are asserted (checks 8 and 9), the
pinned 5,384 is not adjusted, and the difference is stated in the label: **(T)'s
hypothesis is pairwise distinctness, so 5,216 is the count that matches the
lemma** — the bound holds on all 5,384 anyway, with minimum exactly 3 in both
readings, and the 636-pattern teeth count is the same either way.

## Tally

45 checks, 8 notes (stated-not-tested facts). Sections: 1 Φ and the corner (6) ·
2 (T), exhaustive (4) · 3 randomized enactments (8) · 4 per-edge budgets (3) ·
5 the λ-trichotomy and W ≤ 24 (5) · 6 the field kill (6) · 7 the margin (4) ·
8 rung-down controls (3) · 9 not-too-strong at X = 3 (2) · 10 the τ = 5 control
(4).

Runtime: **~10 s** on Python 3.14.6, **~14 s** on a bare `/usr/bin/python3`
(3.9.6); `-O` makes no difference to either. Peak RSS ≈ 167 MB. The heavy steps
are the single pruned field scan of the X ≤ 3 layers at m = 22 (903,003
configurations in one pass, ~3.3 s) and the randomized enactments of §3 (~6 s).

## What this opens

**The X = 3 frontier — and it is a different world.** The 9,224 configurations
the turn-11 notebook queued as the m = 23 campaign's field do not exist as an
X = 2 frontier; the real frontier is the **186,086-configuration X = 3 layer**,
of which **15,340** survive everything currently available.

> **ERRATUM 2026-07-29 (internal doc sweep) — that frontier is closed, and so
> is the layer above it.** All of it: the m = 22 rung by certificate **0018**
> (the eight-shape census — the λ4 pair, which carried 1,549 of the 1,580
> shape-cut survivors, dies at m ≤ 20); the X = 3 layer window-wide by **0019**
> (T-A: X ≥ 5 for every critical core in [22, 456], reached by counting with no
> shape enumerated at all); and the rung above that by **0020** (T-A20: X ≥ 6
> everywhere in the window). The 15,340 configurations are **not** a field to
> scan — **no critical core has X = 3 at any m**, so every X = 3 statement in
> this section is now vacuous for cores and is kept as the shape-space record
> it was, not as a work list. No check condition changes.

Three things change at X = 3, and none of them is cosmetic:

1. **a = 2 becomes legal.** (T) no longer forbids a triple sharing two vertices —
   in fact the codegree-3 triangle consumes exactly X = 3. *(Erratum
   2026-07-27: this item originally concluded "(CC⁺) is unavailable" — false
   as written. a = 2 at X ≤ 4 forces b = 0 or s = 3, never a corner
   violation, so (CC⁺) survives through X ≤ 4 — certificate 0017.)*
2. **The constant 24 does not transfer.** It is built from the X = 2
   trichotomy. The X = 3 shape space additionally contains a λ = 4 pair and the
   codegree-3 triangle. The whole λ-case analysis of §5 must be redone.
3. **The λ-shape lever weakens where a = 2 is realised**, because on the
   triangle's three edges x_e = 2, where (CC⁺)'s bound X − x_e = 1 and plain
   (CC)'s ⌊3(X−x_e)/2⌋ = 1 coincide.
   *(This item is unaffected by the erratum: on the triangle's edges the two
   bounds coincide, so there the sharpening genuinely buys nothing.)*

Both leads this section opened are **retired, unproven and unneeded** — the
a = 2 rigidity lemma (that the a = 2 world at X = 3 is *exactly* the codegree-3
triangle) and the induced degree-array judge (L1): 0018/0019/0020 leave no
X = 3 core for either to act on. Neither was ever consumed by any certificate.

## Erratum against this certificate (2026-07-27, applied with certificate 0017)

Section 9's warning note and one docstring line said **"(CC⁺) is UNAVAILABLE"**
at X = 3. False as written: only the *naive* a ≤ 1 argument dies there. An
a = 2 triple at X ≤ 4 forces (a, b, s) ∈ {(2,0,2), (2,0,3), (2,1,3)}, never a
corner violation, so the sharpened corner — hence (CC⁺) — survives through
X ≤ 4 and first fails at X = 5 (certificate 0017 exhausts the ladder). The two
companion statements were and remain true: the constant 24 does not transfer,
and the λ-case analysis must be redone at X = 3. No check condition changes;
the reworded note and docstring line are marked in place; re-verified green
under bare 3.9.6 and `-O` after the edit. Caught by the turn-13 fleet
(both derivation lanes independently).

## Reproduce

```bash
python3 verify.py
```

~13 s under a bare `python3`, deterministic, exit 0 on green. Runs from any
working directory; reads nothing from disk.
