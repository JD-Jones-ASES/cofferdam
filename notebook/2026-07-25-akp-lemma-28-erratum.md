# 2026-07-25 · erratum on Abu-Khazneh–Pokrovskiy Lemma 2.8

**Found by independent enumeration, not by reading.** Recorded conservatively: the
slip is arithmetic in the *statement*; the surrounding mathematics and the result
f(6) = 13 are unaffected.

## The published statement

AKP, *Intersecting extremal constructions in Ryser's Conjecture for r-partite
hypergraphs* (arXiv:1409.4938), Lemma 2.8:

> If H′ is an intersecting 6-partite hypergraph with 8 hyperedges and τ(H′) = 4,
> then H′ has one of the following degree structure:
> • In all 6 partitions … one vertex of degree 3, two vertices of degree 2 and one
>   vertex of degree 1, or
> • In 5 partitions … one vertex of degree 3, two vertices of degree 2 and one
>   vertex of degree 1, and in the 6th partition it contains one vertex of degree 3,
>   one vertex of degree 2, and **four** vertices of degree 1.

## The slip

Degrees within one part sum to the number of edges, here 8. The first structure
checks out: 3+2+2+1 = 8. The second does not: 3 + 2 + 4·1 = **9**.

It should read **three** vertices of degree 1, giving the profile (3,2,1,1,1) and
3+2+1+1+1 = 8. Their own proof text derives it correctly — "apart from the vertex
of degree 3 the remaining vertices in that partition will all have degree 1", and
with one degree-2 vertex that leaves 8−3−2 = 3 of them. Only the enumeration in the
statement is off by one.

## How it surfaced

Our census of all 8-edge τ=4 6-partite intersecting hypergraphs returns **5
isomorphism classes** — four with every part (3,2,2,1), one with five parts
(3,2,2,1) and a sixth part (3,2,1,1,1). Checking the census against Lemma 2.8 as
printed flagged the fifth class as impossible. Re-verified firsthand, and it is
perfectly real:

```
(0,0,0,0,0,0) (0,1,1,1,1,1) (0,2,2,2,2,2) (1,0,1,3,2,2)
(2,0,3,2,1,3) (3,1,3,0,3,2) (3,3,0,1,2,3) (4,3,1,2,3,0)
```

8 edges, 6-partite, intersecting, Δ = 3, no 3-cover, explicit 4-cover
{(0,0),(0,1),(2,3),(1,3)} — so τ = 4 exactly. Six degree-3 vertices, one in each
part, so **Lemma 2.1 holds on it**; it is only 2.8's arithmetic that it violates.

## Consequence

None for f(6) = 13, which AKP also prove by other cases and which
Aharoni–Barát–Wanless obtained independently. The corrected Lemma 2.8 reads

  (A) all six parts (3,2,2,1)   — 4 of our 5 classes
  (B) five parts (3,2,2,1), sixth part (3,2,1,1,1)   — 1 of our 5 classes

and our census realises both, so the lemma is *sharp* once corrected.

**The lesson is the method's, not the paper's.** We used AKP only for the constant
f(6)=13 and for the technique behind (L4); had we instead imported Lemma 2.8's
degree structures as a filter — an entirely natural thing to do — the fifth class
would have been silently discarded and the enumeration would have been incomplete
in a way no downstream check could see. Cited structure gets re-derived before it
is used as a constraint.

---

## A second finding from the same census

The peeling chain computes (13,5) — the f(6)-extremal hypergraphs — in two
branches, Δ=5 and Δ=4, those being the maximum degrees certificate 0002 leaves
alive at (13, τ=5). **The Δ=5 branch is empty.**

Diagnosed rather than assumed, since a silent zero is exactly what a broken search
looks like. Each of the five 8-edge τ=4 residuals offers 424–453 star patterns and
carries 185–204 minimum 4-covers; a greedy 5-star escapes 180–198 of them and the
exhaustive search confirms none escapes all. So the branch dies on the set-cover
condition, with the machinery demonstrably working.

Hence **every f(6)-extremal 13-edge hypergraph has maximum degree exactly 4** — a
structural fact about the extremal family that neither AKP nor ABW states, and one
that halves the work at the next rung.
