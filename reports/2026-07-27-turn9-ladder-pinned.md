# Turn 9 — the ladder is pinned, the hinge is a theorem, and a search you almost paid for was already answered

*For JD. Plain language. Ends with the one command.*

## The headline

The floor did not move, exactly as you said it needn't. What moved is
everything underneath it. Four new certificates today (0012 landed after
this digest's first draft — its section is below):

**Certificate 0009 — g(5) = N(5) = 13, citing nothing.** The last daylight
between "our ladder" and "the ladder that cited the literature" is closed.
There is now one ladder, it is entirely ours, and the machinery that both
peer labs attacked is load-bearing at exactly one edge count (m = 21), on
567 configurations instead of 2,478.

**Certificate 0010 — N(4) = 9 by hand.** This was the single most exposed
step in the whole proof — the one our own certificate 0007 called "the
single most valuable thing anyone could contribute," resting on one big
search (then two). It is now a **theorem a person can read in an
afternoon**, with the two searches demoted to corroboration. Three separate
subagent angles each produced a complete proof; I re-derived the best one
line by line before certifying it.

**Certificate 0011 — every 13-edge τ≥5 object has max degree exactly 4.**
The last result from turn 4 that had never been certified. 61 checks, ~3
minutes, its central census built twice by routes sharing no code — and
that double-build control earned its keep **live**: a prototype bug
produced a silently smaller census (4 classes instead of 5, the flattering
direction), and only the second route caught it.

## Certificate 0012 — the machinery both peer labs attacked now holds up nothing

Your PLAN's new attack #1 (hand-kill the 567 configurations at m = 21)
closed the same session it was ranked. Measurement said 43 of the 567
genuinely needed the delta-budget — and every one of the 43 saturates the
degree cap in at least two parts. A saturating vertex's complement is
exactly the class certificate 0011 just bounded, which yields a three-line
lemma — (L10), the saturation floor — strong enough that **all 567 die on a
single convexity evaluation each, margin at least six, median 24**, where
the old machinery's margin was exactly one. The floor's minimal chain now
contains no delta-budget, no level system, none of the code the audits went
after. Certificate 0011, shipped this morning as "used nowhere
load-bearing," was load-bearing by the afternoon.

## The free gift

Your open question Q13 — "is there a 13-edge τ≥5 object with a part of
minimum degree 2?", the one PLAN priced at a 232-slice search — was already
answered **YES** by an object we shipped yesterday for a different purpose.
Certificate 0008's 13-edge witness has exactly such a part. Nobody had asked
it. That closes the N(5) rung permanently (it can never be raised to 14) and
retires the search unrun. New house rule (D-026): when a new object enters
the repo, run it against the standing open questions once.

## What measurement killed before theory wasted a week

The next lever PLAN wanted to try — sharpening the degree-two cap to push
past 22 — is **dead as a floor-mover, and we know it in numbers**: even
forbidding five times more than the lemma forbids leaves survivors at
m = 22. Two independent implementations agree on every cell. An hour of
measurement replaced a week of doomed theory.

## Checks on our own work (the part you asked for first)

- All seven existing certificates replayed green, twice each, before
  anything was touched. All eleven now green under both interpreters.
- The B_min convexity bound — the step our corrected risk table said was
  carrying the load with no name — is now **(L9)**: stated, proved, and
  audited at every point the certificates actually use it. Zero mismatches
  in 262,729 comparisons.
- One embarrassment found and recorded (D-028): certificate 0001's
  "proven twice" lower bounds were **one proof in two costumes** — its
  exhaustive searches never actually branch; their root prune is the
  counting argument. To be clear about what this does and does not mean:
  the counting proof itself is three lines and machine-checked in three
  places — the constant is not in doubt; what was wrong was our claim of
  having two independent arguments. The honest second argument (a
  from-definitions brute force using none of our lemmas) closed every case
  through 6 edges but hit its node ceiling at 7 (800M+ nodes, no verdict) —
  recorded as undecided, priced for a future attempt.
- Blind reproductions: the m = 12 exhaustion behind certificate 0009 was
  reproduced by two agents who never saw my code — one in C by two different
  methods, one in Python by a third route — all landing on the same 11,520
  designs, every one with an explicit 4-cover. Two of their own bugs were
  caught by the mandatory controls, including one that would have produced
  a *flattering* wrong answer. The controls are earning their keep.

## The grail question

You asked whether the floor can rise without bound. Honest answer: no route
visible, here or in the literature we've read. But one reframing surfaced
that I think you'll like: a minimum counterexample is **τ-critical** (one
line: deleting any edge of a minimum one must drop τ), and τ-critical
hypergraphs have classical *size ceilings*. If that constant checks out in
the literature, the whole problem becomes a finite window — floor 22,
ceiling M — and "prove Ryser at r = 6" becomes "empty a finite list". The
constant is expected to be astronomically far away; the point is the shape,
not the number. Queued as a literature check, consumed by nothing yet.

## Owner items

- The turn-8 open question to you — commission a peer lab for a third
  N(4) = 9 search? — has changed shape: the third leg now exists in-house
  and is search-free (certificate 0010). My read: the commissioning
  question is moot, but a cheap peer replay of the certificates (one
  command each) is still worth something whenever a peer lab is idle.
  Your call; the note is updated.
- Nothing was published, posted, or pushed outside the private repos.

## The one command

```bash
cd ~/Documents/repos/cofferdam && for c in certificates/00*/verify.py; do case "$c" in *0004*) continue;; esac; python3 "$c" || break; done
```

Every certificate in order (0004 is never-green scaffolding and is skipped),
each ending ALL GREEN.
