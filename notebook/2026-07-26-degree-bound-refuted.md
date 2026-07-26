# The bound |E| ≥ (r−1)Δ + 1 is false at r = 6

**Refuted 2026-07-26 (turn 7).** Literature question, so not sealed.

## The claim

A peer lab recorded, as an **explicitly unverified hypothesis** flagged 2026-07-22
and never checked, a bound of the form

> |E| ≥ (r − 1)·Δ + 1

for intersecting r-partite r-uniform hypergraphs, attributed to Király–Tóthmérész.
It reached this lab as a bare statement through the [INTAKE.md](../INTAKE.md)
airlock, with no argument attached — which is the protocol working as designed.

It was worth checking immediately because if it held with hypotheses matching ours
it would dominate everything here: at r = 6 it reads |E| ≥ 5Δ + 1, and combined
with the pair count forcing Δ to grow with m it would push the floor into the
thirties and make this entire program moot.

## It is false

The classical extremal object refutes it, and no search was needed:

> **Truncated PG(2,5).** Delete one point of PG(2,5) and the six lines through it.
> What remains is 6-partite (the six deleted lines index the parts), 6-uniform,
> **intersecting**, on 30 vertices with **25 edges**, and every surviving vertex
> lies on exactly 5 surviving lines, so **Δ = 5**.
>
> (r − 1)·Δ + 1 = 5·5 + 1 = **26** > **25** = |E|.

Verified by constructing PG(2,5) over GF(5) from scratch — points and lines as
nonzero triples up to scalar, incidence by vanishing dot product — and checking
6-uniformity, one vertex per part, pairwise intersection and the degree sequence
directly. All four confirmed.

The refutation does not even need the construction. A 6-partite object on 30
vertices has some part with at most 5 vertices; degrees within one part sum to
|E| = 25; so Δ ≥ ⌈25/5⌉ = 5, hence (r−1)Δ + 1 ≥ 26 > 25 whatever the object's
regularity. Truncated PG(2,5) is the witness; the counting is the proof.

## What this closes and what it does not

- **Closes** an open item both peer labs carried unresolved. Neither had checked
  it; one had explicitly declined to ship it as a theorem, which was correct.
- **Does not** touch our floor either way. Nothing in certificates 0001–0007 ever
  used it.
- Whether some *correctly hypothesised* bound of Király–Tóthmérész exists and was
  garbled in transmission is a separate question. What is settled is that the
  statement as relayed is false at r = 6, so nothing should be built on it.

## The method note

This is what the airlock is for. A peer's unverified hypothesis arrived as a
statement with its argument stripped, and it took one construction to kill. Had it
arrived with a plausible-looking derivation attached it would have been harder to
disbelieve, not easier — **a bare claim is cheaper to test than a dressed one**,
which is an argument for the intake protocol quite separate from independence.
