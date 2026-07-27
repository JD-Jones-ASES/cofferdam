# Turn 10 — the problem is now finite: [22, 456]

*2026-07-27 · for JD · plain language*

## What happened

Two new certificates, both adversarially attacked by independent fleets
before going green, both green under the bare system Python and `-O`.

**Certificate 0013 — the finite window.** Until today we could only push
the floor up: no counterexample below 22 edges. Nothing said a
counterexample couldn't be enormous. Now it can't be: any counterexample
contains a minimal "critical core," and a critical core has **at most
462 edges** — proven with a beautiful classical argument (random
orderings, disjoint events) that consumes *no* outside literature and
*no* other certificate. So the whole conjecture collapsed from an
infinite question to one finite check: **Ryser r = 6 intersecting is
true if and only if no critical core exists with between 22 and 462
edges.** Every rung we climb from here closes a measurable part of a
window with two certified ends.

**Certificate 0014 — the window tightens to [22, 456].** The outside
review you commissioned claimed the ceiling improves to 456 via exterior
algebra, in one cryptic line. We audited it in-house: first a
twenty-minute calibration at the smallest case proved any naive reading
FALSE (that honesty check mattered — it forced the real mechanism into
the open), then two independent derivation fleets converged on what the
sketch actually meant, I re-derived it at the desk, and it's now a
certified theorem. The literature sweep found **no published counterpart
anywhere** — if that holds, the 456 ceiling is new mathematics.

## What the literature sweep settled (the other half of the plan)

- The ceiling's *generic* formula is classical (1971, and restated in a
  Dec 2025 preprint) — but nobody has ever applied it to Ryser. The
  set-pair world and the Ryser world literally do not cite each other.
  The Ryser field's only previous ceiling was ~33.6 million edges; ours
  is 456.
- The false "τ* ≤ 3" claim from the review is fully diagnosed: it was a
  garble of a real 1975 Lovász theorem (verified from the Hungarian
  original). Our truncated-plane object isn't a paradox — it's the
  *equality case* of the real Füredi theorem.
- The "March 2026 survey" the review cited isn't a survey (it's a 9-page
  research paper), but it does confirm in one sentence: intersecting
  Ryser is open for r ≥ 6. The actual survey (2021) contains a
  complementary finite reformulation — a lead we've filed.
- **The floor's published comparator moved mid-session**: a June 2026
  Princeton preprint proves every counterexample has ≥ 14 edges (the
  first improvement on the 1975 bound in fifty years). Ours is 22 —
  still eight clear, but this neighborhood is suddenly active: two
  papers in fifteen months, right next to our floor.

## What opened up (next sessions)

The audit measured *exactly* where the 456 proof's power ends — its six
"annihilators" are provably all of them — so further tightening must
come from combinatorics. Two live routes: small-case exhaustion suggests
the true abstract ceiling may be as low as **252**, and one big
hypothesis (that a counterexample's edges pairwise intersect) hasn't
been spent on the ceiling at all yet. Both are queued in the plan.

## One thing for you (no action needed today)

Publishing is your line, always. I've flagged in the project note that
the neighborhood heated up. If a partite-specialized note from that
direction ever lands, our floor and window are the natural response —
worth a strategy conversation whenever you want one.

## Reproduce

Every certificate replays in about a second:

```bash
cd ~/Documents/repos/cofferdam/certificates/0014-window-456 && python3 verify.py
```
