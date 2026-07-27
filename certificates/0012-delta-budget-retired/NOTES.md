# Certificate 0012 — the δ-budget retires: m = 21 dies on floors and convexity

**Status: GREEN.** 12 checks + 5 notes, ~80 s, `python3 verify.py`, stdlib
only, no solver, no imports from `lib/`. Green under a bare
`/usr/bin/python3` (3.9.6) and under `python3 -O`.

| claim | label |
| --- | --- |
| **(L10)**, the saturation floor: deg(v) = m − 13 forces \|E(v)∩E(u)\| ≥ deg(u) − 4 for u outside v's part | **PROVEN-BY-CERTIFICATE** (three lines, standing on 0011) |
| m = 21 impossible via profiles + (D2) cap + (L7)+(L10) + A ≥ S−m + (L9) + B ≤ ⌊5X/2⌋ | **PROVEN-BY-CERTIFICATE** |
| the pinned-ladder floor m ≥ 22 consumes **no δ-budget, no level system, no qmin, no U** — at any rung | corollary, stated precisely below |

## What happened

PLAN attack #1 asked for a hand-kill of the 567 configurations that (L8)
carries at m = 21 — the one rung where the δ-budget machinery (the
narrowest-margin code in the repo, the target of both peer audits) was still
load-bearing. Measurement came first: under the old guards the 567 split
**502** dead on (L9)+B_cap+A≥S−m alone, **22** on level feasibility, **43**
on the δ-budget proper. Every one of the 43 has at least two parts whose
maximum degree **saturates** the k=1 cap Δ ≤ m − N(5) = 8.

Saturation is structure. A degree-8 vertex at m = 21 leaves a 13-edge
complement with τ ≥ 5 — **exactly certificate 0011's hypothesis class** — so
the complement has Δ ≤ 4, and the saturating vertex must share
≥ deg(u) − 4 edges with every other-part vertex u. That is **(L10)**, and it
beats (L7) by one unit on every saturated pair. One unit per pair compounds
across pairs at A₀, (L9) is convex, and **all 567 configurations die on a
single convexity evaluation each**: B_min(A₀) > ⌊5X/2⌋, margin ≥ 6
everywhere, median 24 — against the δ-budget's margin of exactly one.

Certificate 0011 was shipped hours earlier as "used nowhere load-bearing."
It was load-bearing the same afternoon.

## The minimal chain, after this certificate

On the pinned ladder N(1..5) = 2,4,6,9,13: m ≤ 11 dies on (A)+(B); m ≤ 19
admits **no configuration at all** (the pair count under the pinned caps);
m = 20's 105 all fail the (D2) cap; m = 21 dies here; m ≥ 22 is the floor.
Nothing in that chain evaluates a δ-budget, a level structure, `qmin`, or
the ceiling U. Certificates 0006/0007 stay green as the weak-ladder record —
retired from the minimal chain, not refuted.

## Controls

- **Not too strong**: the identical reduced test at m = 22 (saturating
  degree 9) leaves survivors — the 12th cap-passer scanned already lives.
- **Sensitivity**: weaken 0011's theorem to Δ ≤ 5 and **65 of 567 revive**.
  The new input is load-bearing, with the 22 + 43 pre-(L10) stragglers as
  exactly the exposure.
- **Monotonicity of B_min** proved (decrement an above-floor entry) and
  machine-checked on 81 sampled configurations × 6 consecutive A values.
- The B_cap concentration inequality C(t,2) ≤ (5/2)(t−1), t ≤ 5, checked at
  every t with its t = 5 equality; the underlying identities carry turn 8's
  1.86M-audit history.

## Margins (D-017)

| step | margin |
| --- | --- |
| the kill itself | **≥ 6** at the tightest configuration; median 24; max 46 |
| (L10) vs (L7) per saturated pair | exactly 1 — but it compounds across pairs |
| the sensitivity direction | Δ ≤ 5 revives 65; Δ ≤ 4 revives 0 |

## Reproduce

```bash
python3 certificates/0012-delta-budget-retired/verify.py
```

~80 s. Deterministic. Green under bare 3.9.6 and `-O`.
