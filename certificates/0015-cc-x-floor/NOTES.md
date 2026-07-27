# Certificate 0015 — (CC), the critical-cover inequality, and X ≥ 2 at the window floor

**Status: GREEN.** 19 checks + 3 notes, ~15 s, `python3 verify.py`, stdlib
only, no solver, no imports from `lib/`. Green under a bare
`/usr/bin/python3` (3.9.6) and under `python3 -O`. Deterministic.

| claim | label |
| --- | --- |
| **(CC)** 2·Σᵢ Φ(dᵢ−1, 5−bᵢ) ≤ 3(X − x_e) for every edge of a critical core, any m; global form 2·Σ_e Σᵢ Φ ≤ 3(m−2)X | **PROVEN-BY-CERTIFICATE** (in-house: 0013; external NONE) |
| **X ≥ 2 for every critical core at m = 22** | **PROVEN-BY-CERTIFICATE** (field: 0005/0009/0012; (D2): 0008; external NONE) |

## Why this certificate exists

The window [22, 456] (certs 0013/0014) made the bottom rung a real
place; this certificate is the first structural statement about what
must live there. (CC) converts criticality's private covers into a
pair-excess floor: the d_i − 1 sibling edges through each vertex of e
must funnel through the 5 − b_i cover vertices outside that part, every
same-cell pair is a double-meet, the funnel count charges each pair
{f, f′} exactly a·b times, and the corner a·b ≤ (3/2)(s−1) (tight
exactly at (2,3), s = 5 — the 6-uniform cap s ≤ 5 is load-bearing;
at s = 6 the corner is FALSE) converts the charge into excess. At
m = 22 the corollaries bite hard: X = 0 forbids degree 7, X = 1 forbids
degree 8 and makes the 7-stars pairwise edge-disjoint (≤ 3 of them fit
in 22 edges). Over the full pinned-ladder field: 506,204 X ≤ 1
configurations, all dead — 504,478 on the per-edge cap, 1,150 on
star-disjointness, 576 on (D2). **A minimum core must carry excess
X ≥ 2: it is in the nonlinear regime the moment it exists.**

## Margins and teeth

- **Not too strong**: at X = 2 the same judge leaves 9,224 of 210,713
  configurations alive — this judge's evidence stops at X ≥ 2 (see the
  erratum below). And the τ = 5
  rehearsal core (rebuilt from 0013) *realizes* X = 0 — (CC) does not
  forbid low excess in general; the m = 22 kill is that rung's
  pair-count tension.
- **Enactment at margin zero**: the t = 5 analog of (CC) holds on all
  14 edges of the real core with the actual lex-first covers, with
  margin EXACTLY 0 on every edge (X = 0, every Φ vanishes) — a sign
  error anywhere in the derivation would fail loudly there. Both
  accounting identities (I_e = Σ a·b; Σ x_e = 2X) are exact on the
  real object.
- **Teeth**: the corner fails at s = 6 ((3,3) gives 9 > 7.5); drop the
  star rule → exactly 6 configurations revive (all X = 1 with four
  degree-7s); drop (D2) → exactly its 576 victims revive (none caught
  downstream).
- Φ verified as the true exhaustive minimum (all n ≤ 10, k ≤ 6) and
  monotone in the class count — Φ(·, 5) is a safe bound whatever the
  covers do.

## Provenance — audited, repaired, stronger than claimed

The outside review (via JD, turn 9) claimed (CC) with exactly this
Φ/corner shape and claimed "X ∈ {0,1} excluded via (CC) + the D₂ cap".
(CC) re-derived from scratch at the desk this turn: correct as claimed.
The exclusion as sketched does **not** close — measured first: the
global form + (D2) leaves 52 survivors. What closes it are the
per-edge corollaries and the star-disjointness count, which the sketch
did not contain. Recorded per house law: claim audited, mechanism
repaired, result delivered stronger than the sketch.

## Adversarial record (turn 11)

Two independent attackers before certification, both returning
**zero fatal findings and zero gaps**:

- **Proof refuter (SOUND)**: hand-rederived every step; 16,578
  randomized instance checks of the exact identities (5,996 pairs at
  the tight (2,3, s=5) corner); a fully independent re-implementation
  reproduced all five machine counts; and an independent knapsack
  computation delivered **the margin: the maximum degree-pair total
  under the X = 1 rules is exactly 231, one short of the 232 that
  X = 1 requires** (225 at X = 0) — promoted into the certificate as
  check 19. Catches applied: the corner's binding hypothesis is
  a + b ≤ s (misquantified in one docstring line); the b_i = 5 case
  is vacuous from covering alone, so (CC) needs no lemma (A);
  "X ≤ 1" means 0 ≤ X ≤ 1.
- **Code auditor (SOUND-WITH-NITS)**: independent reimplementation
  matched every number (67 / 506,204 / 504,478 / 1,150 / 576 / 0;
  X = 2: 210,713 / 9,224; revivals 6 and 576; and the honesty note's
  unasserted 52 — confirmed exactly, now check 18); the §4 rebuild
  diffs byte-identical against 0013's construction; sabotage tests
  confirmed teeth; determinism verified across 3.9.6/3.14 and hash
  seeds. Catches applied: the real-core a·b identity is vacuous there
  (all terms 0 = 0 — label now says so) and gained a nonvacuous
  transversal-synthetic check (292 nonzero terms, pinned); the
  six-revival parenthetical is now asserted, not stated; dead code
  removed.

Two guessed constants in drafts (the D2-drop revival count; the
"thousands" nonvacuity threshold) were caught by the run itself and
replaced by measured values — the D-017 shape, caught twice more by
the machinery built to catch it.

## Erratum (2026-07-27, applied with certificate 0016)

The original not-too-strong label read "the floor lands exactly at 2" —
a claim about the **floor**, where only a claim about **this judge**
was proven (the judge leaves 9,224 X = 2 configurations alive; that
count is true and still asserted). Certificate 0016, same commit,
closes the X = 2 layer by a sharper corner (the triangle lemma):
**X ≥ 3 for every critical core at m = 22**. Every mathematical claim
of this certificate — (CC) and X ≥ 2 — is unaffected. The verify.py
label was reworded the same day; the check's condition is untouched;
re-verified green under bare 3.9.6 and `-O` after the edit. Caught by
the turn-12 adversarial fleet (refuter lens).

## Reproduce

```bash
python3 verify.py
```

~10 s, deterministic. The heavy steps are the two pruned field scans at
m = 22 (X ≤ 1 and X = 2 layers) and the C(30,4) cover searches in the
rehearsal rebuild.
