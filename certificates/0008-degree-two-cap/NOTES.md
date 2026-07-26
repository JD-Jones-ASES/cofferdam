# Certificate 0008 — the degree-two cap: **m ≥ 22**, citing nothing

**Status: GREEN.** 36 checks + 3 notes, ~2 min, `python3 verify.py`, stdlib only,
no solver, no imports from `lib/`. Measured on this box: 130 s under Homebrew
3.14, **123 s under a bare `/usr/bin/python3` (3.9.6)**, 124 s under `-O`.

| claim | label |
| --- | --- |
| **(D2)** each line holds ≤ 1 degree-2 vertex, hence 2·D₂ ≤ m | **PROVEN-BY-CERTIFICATE** (re-derived here) |
| m = 21 impossible | **PROVEN-BY-CERTIFICATE** |
| **a Ryser r=6 counterexample has m ≥ 22** | **PROVEN-BY-CERTIFICATE, CITING NOTHING** |

## What is new, and what is not

**The floor is new. The lemma is not.** (D2) is clause (iii) of Lemma 2.1 of
Francetić, Herke, McKay and Wanless, *Europ. J. Combin.* **61** (2017) 91–105.
This certificate re-derives it in full so that the floor cites nothing — but
re-deriving a published lemma is a different act from finding one, and nothing
here should be read as the latter. The lab's lemmas (A) and (B) are already in
that same position: they are that paper's 2.1(ii) and 2.1(i).

What §1 proves is *strictly more general* than the published clause:

> **(III-C)** Let H be intersecting, E an edge with |E| ≥ 3, and x ≠ y vertices
> of E with deg(x) ≤ 2 and deg(y) ≤ 2. Then τ(H) ≤ |E| − 1, by an explicit
> cover.

with (iii) following by contradiction when τ(H) ≥ |E|. The generalisation matters
in one specific way: **the proof never uses linearity**, and a Ryser r=6
counterexample must be non-linear. It also never uses r-partiteness, lemma (A),
or any external constant. It consumes exactly: *intersecting* (twice — to bound
|U| and to supply the common vertex), *|E| ≥ 3*, and *τ ≥ |E|*.

Our class meets the last of these with **margin zero**. Any single edge covers an
intersecting 6-uniform family, so τ ≤ 6; a counterexample has τ > (r−1)ν = 5
since ν = 1; hence **τ = 6 = r exactly**.

## (L8) is needed at exactly one rung

Read the sweep table in §4: at every m from 12 to 20 the number of admissible
configurations **surviving the cap is zero**, so those rungs die on
(A)+(B)+(C)+the pair count+(D2) alone, with (L8) never consulted. Only m = 21
leaves anything — 2,478 configurations — and those are what (L8) kills.

This is worth stating plainly because of where the lab's attention has been.
Both peer audits went after the δ-budget inside (L8), whose tightest margin is
exactly one. **With (D2) in hand, none of that machinery is load-bearing below
m = 21.** The hinge does not move, though: the m = 20 rung still funnels through
**N(4) = 9**, and still with a margin of one.

## The trap this certificate is built around

**(D2) is false one rung down**, and §3 exhibits the witness rather than
asserting it: a 13-edge 6-partite intersecting object with τ = 5 exactly (no
4-cover among all C(30,4) = 27,405 subsets) whose D₂ = 9, so 2·D₂ = 18 against
m = 13 — and one of whose lines holds three degree-2 vertices.

So the cap has no validity off τ(H) = r. The N-ladder residuals all have
τ = t < 6. **Applying the cap anywhere on the ladder is a false kill with no
visible symptom**, in exactly the direction this lab wants to go (D-005). It is
applied here to H's own six part-profiles and nowhere else.

Independently corroborated on real objects: truncated PG(2,2) is intersecting,
3-partite, τ = 2 = r−1, and has 2·D₂ = 12 > 4 = m.

## The positive control PLAN asked for cannot be run — and what replaces it

PLAN.md owed "a positive control: the bound must hold on objects that exist."
**That item cannot be discharged, by anyone.** An intersecting 6-partite object
with τ = 6 *is* a Ryser counterexample, so the hypothesis class is conjecturally
empty; and for r ≤ 5 it is empty by theorem. Measured: **0 of 67,463** census
objects have τ = r, and direct exhaustive searches found none at r = 3 (m ≤ 8),
r = 4 (m ≤ 11), r = 5 (m ≤ 8). More compute does not fix this. The proof carries
the weight; computation can only rule out a slip in it.

What *is* testable is the lemma's **construction**, which runs on objects
regardless of τ. §1 does this exhaustively over two bounded classes:

- 12,584 intersecting 3-uniform families on [6] (≤ 5 edges) → 19,560 witnesses
- 59,535 intersecting 4-uniform families on [7] (≤ 4 edges) → 228,900 witnesses

**Every one of the 248,460 constructed sets is a genuine cover of size ≤ |E|−1.**
Zero failures, and |U| never exceeded 2.

The conclusion of (D2) is then tested where it is *not* vacuous — on the
non-partite class, where τ ≥ r is reachable at 7 edges (the Fano plane): **6,330
families on [7] with τ ≥ 3, of which 3,570 carry a degree-2 vertex, and 0 have
two in one line.**

## Controls

1. **Teeth** (D-015). A mutant drawing w from U[0] ∖ U[1] instead of U[0] ∩ U[1]
   — i.e. breaking step (c) — fails on **3,780 of 3,780** two-member cases. The
   passing checks demonstrably can fail.
2. **Hypotheses priced, not asserted.** Drop |E| ≥ 3 → K₃ is intersecting with
   τ = 2 = r and every line holding two degree-2 vertices. Drop *intersecting* →
   a searched witness with τ = 3 and a line holding two degree-2 vertices. An
   earlier hand-picked witness here was simply **wrong** (τ = 2, one degree-2
   vertex) and the check caught it; it is now searched, not hardcoded.
3. **Not too strong.** m = 22 survives. If it did not, this would be "proving"
   Ryser at r = 6 and would therefore be wrong.
4. **Anti-vacuity.** The identical predicate on the identical m = 21
   configurations with the cap removed reports **20,638 survivors**. The zero at
   m = 21 is a kill, not a harness that cannot speak.
5. **Both prunes are exact.** The in-recursion D₂ prune agrees with filtering
   afterwards (2,478 either way at m = 21); the score prune agrees with the flat
   `combinations_with_replacement` enumeration (7,159 both ways at m = 20).
6. **The memo key carries a single verdict**, checked rather than assumed —
   9,637 configurations over two full sweeps collapse to 1,484 keys, none
   carrying two verdicts. *Range stated because it is part of the claim
   (D-016): the full 316,591-configuration m = 21 set was not checked this way.*
7. **Sensitivity.** Survivors at cap 9/10/11/12 are **0 / 0 / 7 / 114**. One unit
   of slack and m = 21 reopens — the cap is needed at exactly ⌊m/2⌋.
8. **Containment.** All 567 capped configurations of the cited ladder sit inside
   the 2,478 citation-free ones, so this subsumes the cited route rather than
   rivalling it.

## Independent reproduction

The decisive cell — m = 21, citation-free ladder, cap + (L8) → 0 — was
reproduced by a **second implementation that read no `verify.py` anywhere, no
`lib/`, and none of the exploratory scripts**, working from the prose derivation
in certificate 0006's NOTES. It agrees on every cell:

| ladder | m | admissible | pass cap | survive (L8) |
| --- | --- | --- | --- | --- |
| free | 20 | 7,159 | 0 | 0 |
| **free** | **21** | **316,591** | **2,478** | **0** |
| free | 22 | 6,499,005 | 307,420 | 56,592 |
| cited | 21 | 43,875 | 567 | 0 |
| cited | 22 | 2,079,883 | 156,797 | 30,436 |

A third implementation, written independently again, reproduced the profile and
admissibility counts and additionally ran the **full brute force** over all
185,250,786 and 156,238,908 six-multisets at m = 22 to completion, agreeing
exactly. Agreement between implementations of the same relaxation rules out a
coding slip; it does not prove the relaxation sound.

**Scope warning that nearly bit us.** The notebook's original cap table and
PLAN.md's summary of it were computed on the **cited** ladder (N(5) = 13). A
floor built on those numbers would have silently re-imported f(6) = 13 and undone
certificate 0007. The citation-free run is a different and ~7× larger problem —
316,591 admissible at m = 21, not 43,875; 2,478 cap-passers, not 567.

## What this buys, exactly

**One rung, and it stops.** m = 22 does not die: 56,592 of the 307,420
cap-passing configurations survive on the citation-free ladder (30,436 of 156,797
cited). Reported as the negative result it is — the temptation to publish only
the m = 21 kill is precisely the rounding-up the No-Noise Law forbids.

## Reproduce

```bash
python3 certificates/0008-degree-two-cap/verify.py
```

Deterministic. Green under `python3` and `python3 -O`.
