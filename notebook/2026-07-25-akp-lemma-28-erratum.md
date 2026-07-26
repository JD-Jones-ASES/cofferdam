# Erratum: Abu-Khazneh–Pokrovskiy Lemma 2.8, as posted on arXiv

**Scope of the claim, stated before anything else.** This concerns
**arXiv:1409.4938v1** (submitted 17 Sep 2014), which is the **only version on
arXiv** — checked 2026-07-26; there is no v2, and the arXiv record carries no
journal reference. A journal version is reported by a secondary source as *J.
Combin. Math. Combin. Comput.* **103** (2017) 81–104; **we have not seen it**, so
nothing here is a claim about the published text. The slip is **arithmetic, in the
statement only**: the surrounding proof derives the correct structure, and
**f(6) = 13 is unaffected**.

Found by independent enumeration, not by reading.

## The printed statement

Lemma 2.8 (arXiv:1409.4938v1, §2):

> If H′ is an intersecting 6-partite hypergraph with 8 hyperedges and τ(H′) = 4,
> then H′ has one of the following degree structure:
> • In all 6 partitions … one vertex of degree 3, two vertices of degree 2 and one
>   vertex of degree 1, or
> • In 5 partitions … one vertex of degree 3, two vertices of degree 2, and one
>   vertex of degree 1, and in the 6th partition it contains one vertex of degree 3,
>   one vertex of degree 2, and **four** vertices of degree 1.

## The arithmetic

Degrees within one part sum to the number of edges — here 8 — because every edge has
exactly one vertex in each part.

- First structure: 3 + 2 + 2 + 1 = **8** ✓
- Second structure: 3 + 2 + 4·1 = **9** ✗

It should read **three** vertices of degree 1, giving profile (3,2,1,1,1) and
3 + 2 + 1 + 1 + 1 = 8.

**Their own proof text gets this right.** The proof concludes: "If one of the
partitions of H′ contains exactly one vertex of degree 2, then apart from the vertex
of degree 3 the remaining vertices in that partition will all have degree 1." With 8
edges, one vertex of degree 3 and one of degree 2, that leaves 8 − 3 − 2 = 3 vertices
of degree 1. The derivation is correct; only the enumeration in the statement is off
by one.

## The corrected statement, proven here

Certificate 0005 proves it rather than observing it:

> **Every part of an 8-edge τ=4 intersecting 6-partite hypergraph has degree profile
> (3,2,2,1) or (3,2,1,1,1).**

A part is a cover, so it has ≥ 4 active vertices, leaving eight conceivable profiles.
Three die on the pair count alone (six parts cover at most that part's pairs plus
5 × 5, against C(8,2) = 28). Three more die by exhaustive column search: (2,2,2,2) at
52.0M nodes, (3,1,1,1,1,1) at 2.8M nodes / 31 s, (2,2,2,1,1) at 7.0M nodes / 72 s —
the last two with waste budget 0. Exactly (3,2,2,1) and (3,2,1,1,1) survive, so the
corrected lemma is **sharp**.

Two independent confirmations, neither used as an input:

- This lab's census of the five (8,4) isomorphism classes — four with every part
  (3,2,2,1), one with five parts (3,2,2,1) and a sixth part (3,2,1,1,1) — realises
  **both** corrected structures, so the corrected lemma is exactly attained. That
  census is how the discrepancy surfaced: checked against Lemma 2.8 as printed, the
  fifth class read as impossible.
- An adversarial re-derivation on different machinery, whose positive control at
  (8,4) recovers exactly those two part-profile multisets.

The fifth class, re-verified firsthand — 8 edges, 6-partite, intersecting, Δ = 3, no
3-cover, explicit 4-cover {(0,0),(0,1),(2,3),(1,3)}, so τ = 4 exactly:

```
(0,0,0,0,0,0) (0,1,1,1,1,1) (0,2,2,2,2,2) (1,0,1,3,2,2)
(2,0,3,2,1,3) (3,1,3,0,3,2) (3,3,0,1,2,3) (4,3,1,2,3,0)
```

Six degree-3 vertices, one per part, so **Lemma 2.1 holds on it**; only 2.8's
arithmetic fails. Certificate 0005 also re-derives Lemma 2.1's "a degree-3 vertex in
every part" clause as a consequence of the corrected 2.8 rather than as a citation.

## Why this matters to our own floor

Not as a criticism of the paper — as a dependency check. Our floor cites exactly one
external result, f(6) ≥ 13, and that citation runs:

    f(6) = 13   (AKP Theorem 1.1; independently Aharoni–Barát–Wanless)
      = f(6) ≠ 12   (AKP Lemma 2.9, a case analysis on Δ(H))
      + f(6) > 11   (Mansour–Song–Yuster)

and AKP say plainly that Lemma 2.9's hard case, Δ(H) = 4, "will require some facts
concerning the degree structure of intersecting 6-partite hypergraphs with 8
hyperedges and a covering number equal to 4" — that is Lemma 2.8. So the lemma with
the slip is the structural input to the hard case of the result we depend on, and we
have now proven its corrected form independently. The dependency is in better shape
than an uninspected citation, not worse.

## The other f(6)-extremal finding from the same census

The peeling chain computes (13,5) — the f(6)-extremal hypergraphs — in two branches,
Δ=5 and Δ=4, those being the maximum degrees certificate 0002 leaves alive. **The Δ=5
branch is empty**, diagnosed rather than assumed: each of the five 8-edge τ=4
residuals offers 424–453 star patterns and carries 185–204 minimum 4-covers, a greedy
5-star escapes 180–198 of them, and the exhaustive search confirms none escapes all.
So the branch dies on the set-cover condition with the machinery demonstrably
working, giving **every f(6)-extremal 13-edge hypergraph maximum degree exactly 4** —
stated by neither AKP nor ABW. **Still uncertified**, and one of the first things an
attacker should hit.

## The method lesson

We used AKP for the constant f(6)=13 and for the technique behind (L4), not for
structure. Had we imported Lemma 2.8's degree structures **as an enumeration filter**
— an entirely natural move — the fifth class would have been silently discarded and
the census would have been incomplete in a way no downstream check could see.
**Cited structure gets re-derived before it is used as a constraint.**
