# cofferdam — turn 5 digest, 2026-07-26

Plain language. For JD.

> **Superseded, same day.** The floor is m ≥ 21 citing nothing (certificates
> 0006 and 0007); Q13 was never answered and turned out not to be needed. Runtimes
> and check counts below have moved. Kept as the record of what turn 5 concluded.

## The headline

**The floor moved: m ≥ 20.** The first of the two unverified rungs — m = 19 — is
gone, killed by an argument this lab derived itself, and the whole remaining gap
between us and the claim m ≥ 21 is now **one finite question about 13-edge
objects**, stated below. The seal is intact.

## What your pointer did

You wrote: *inspect the equality case when deleting two same-part stars; every
part has at least 6 active vertices; no active vertex can have degree one; what
must that part look like in an eight-edge residual.*

That is exactly right, and it exposed an error of ours. Certificate 0002 had
tried the same equality case, concluded the residual's tail had to look like
(3,2,1,1,1), found the existing ladder already forced that, and recorded Lemma
2.1 as "subsumed — moves the floor by nothing". **But a counterexample has no
degree-1 vertices at all**, so that tail is impossible and the equality case does
not merely get constrained, it dies. Lemma 2.1 was not subsumed; it was underused.

The two facts your pointer names are both one-liners:

- **No degree-1 vertex.** Take an edge E and a vertex x in it. Drop x: five
  vertices are left, and five is fewer than τ = 6, so those five do not cover —
  some edge F avoids all of them. F still has to meet E, so it meets it exactly
  at x. That is a second edge through x.
- **Six vertices per part.** The vertices of one part already meet every edge, so
  a part is itself a cover, so it has at least τ = 6 of them.

Together: **every part's degrees are at least 6 numbers, each at least 2, adding
to m.** That alone drops m=19's margin from 9 to 3.

## The lever they unlock

Deleting k vertices of one part leaves a residual, and the residual's *surviving
vertices in that part keep every one of their edges* — because an edge has
exactly one vertex per part. So the residual is not just "some object with τ at
least 6−k"; it is one with a part whose every degree is at least 2. Call the
least size of such an object N(t). We computed:

| | N(1) | N(2) | N(3) | N(4) |
| --- | --- | --- | --- | --- |
| value | 2 | 4 | 6 | **9** |

N(4) = 9 is your eight-edge question answered. At eight edges such a part would
have to be exactly four vertices of degree 2, and **no eight-edge object has
that** — exhaustive search, 52 million nodes, 268 seconds. Two independent things
agree and neither was used as input: the published Abu-Khazneh–Pokrovskiy Lemma
2.1, and our own census of the five 8-edge classes. For the other direction we
built a 9-edge object by hand from our own census class, adding one edge on the
degree-1 vertex — no search needed.

Feed those into the old counting ladder and:

| what it cites | floor |
| --- | --- |
| nothing at all | **19** (was 18) |
| the one published constant f(6)=13 | **20** (was 19) |

At m = 20 exactly one case survives, Δ = 7 — the previous m=20 Δ=5 and Δ=6 cases
both die by counting now.

## The whole remaining gap, in one sentence

At m = 20 with Δ = 7, deleting the degree-7 vertex leaves exactly 13 edges, which
must be an f(6)-extremal object whose relevant part has every degree ≥ 2. So:

> **Is there a 13-edge 6-partite intersecting hypergraph with τ = 5 and a part
> all of whose vertices have degree ≥ 2?**
>
> If **no**, then m ≥ 21 and the claim is confirmed. If yes, the case stays open.

Three possible profiles for that part, no more: (4,3,2,2,2), (3,3,3,2,2),
(3,2,2,2,2,2). This is what turn 4 called "the broad (13,5) run", now shrunk from
a census of every extremal object to one existence question with a column pinned.

## Honest status of that question: open, and measured

The search is running and has not finished. Rate ≈35k nodes/s against 194k/s at
the eight-edge level; the tightest of the three profiles ran 42 million nodes
without exhausting. It is split into 232 disjoint slices for parallelism.

A second, counting-only route to the same case was tried and **does not work**: a
pool argument played against a star-intersection bound kills a good fraction of
the 105 admissible profile combinations, but the all-(7,4,3,2,2,2) case survives
with maximum 30 against a requirement of exactly 30 — a dead heat. Recorded as a
near-miss, not a lever.

## What this says about the claim under verification

Unchanged in kind, better in degree. This lab now **independently corroborates
every rung up to and including the exclusion of m = 19**, by machinery the
existing chain does not share. It still **does not confirm m = 20**. The
unverified remainder has gone from two rungs and three cases to one rung, one
case, one question.

## One command

```bash
cd ~/Documents/repos/cofferdam/certificates/0005-min-degree-ladder && python3 verify.py
```

~5 minutes, stdlib only, no solver, 30 checks.
