# Erratum: Abu-Khazneh–Pokrovskiy Lemma 2.8, in both published editions

**Scope of the claim, stated before anything else.** The slip is present in **both**
editions, each read firsthand:

- **arXiv:1409.4938v1** (submitted 17 Sep 2014), the only version on arXiv — there
  is no v2, and the arXiv record carries no journal reference.
- **the version of record**: *J. Combin. Math. Combin. Comput.* **103** (2017)
  81–104, publisher-hosted at combinatorialpress.com, Diamond Open Access and
  freely downloadable (sha256 `b4da4cd8…f86bec81`).

> **Scope widened 2026-07-26 (turn 7).** Until this revision the note read "we have
> not seen the journal text, so nothing here is a claim about it", and inferred that
> the arXiv PDF was the copy in circulation. Both statements are now superseded: the
> journal PDF is freely available, and it carries the error. The reason it read as
> unreachable is a detail worth recording — **it is a 400-dpi bilevel scan with no
> text layer**, so `pdftotext` returns 24 bytes of form feeds and a text-based check
> comes back empty. An empty grep on a scan is not evidence of absence. Raised in the
> adversarial pass by Codex, verified here by rendering the pages.

**The date.** Every publisher-side and article-side surface says **2017**: the
publisher page states "Published: 20/03/2017" (and `citation_online_date`
20/03/2017), the title page is dated March 20 2017, and the p.81 footer reads
"JCMCC 103 (2017), pp. 81–104". The second author's publication list labels it 2018;
that is the outlier.

**The journal text is a re-typeset, not a photo-reprint** — arXiv's "8 hyperedges"
reads "8 edges" in the journal — so the arithmetic survived a copy-editing pass into
the version of record rather than merely being reprinted. Which settles what the
earlier version of this note could only speculate about: no referee caught it.

The slip is **arithmetic, in the statement only**: the surrounding proof derives the
correct structure, and **f(6) = 13 is unaffected**. Nothing in our floor would move
if the published version reads correctly; the reason to record it at all is the
dependency check in the last section.

Found by independent enumeration, not by reading.

## The printed statement

It appears **twice in each edition** — once as the Lemma 2.8 statement, once as the
"Type B" definition that names the same profile:

| | arXiv v1 | journal (JCMCC 103) |
| --- | --- | --- |
| Lemma 2.8 statement | §2, pp. 7–8 | printed p. 89 |
| proof sentence implying **three** | §2 | printed p. 90 |
| "Type B" definition, repeating **four** | §2 | printed p. 91 |

Lemma 2.8 (arXiv:1409.4938v1, §2; journal p. 89):

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

The printed lemma has **two halves**, and until turn 7 this note restated only the
first — which was an overclaim, caught by Codex in the adversarial pass. Both are now
certified (cert 0005):

> **Per-part.** Every part of an 8-edge τ=4 intersecting 6-partite hypergraph has
> degree profile A = (3,2,2,1) or B = (3,2,1,1,1).
>
> **Global.** At most one part is B. So the object is all-A, or five A and one B —
> the disjunction the lemma actually prints.

*Per-part.* A part is a cover, so it has ≥ 4 active vertices, leaving eight
conceivable profiles. Three die on the pair count alone (six parts cover at most that
part's pairs plus 5 × 5, against C(8,2) = 28). Three more die by exhaustive column
search: (2,2,2,2) at 52.0M nodes, (3,1,1,1,1,1) at 2.8M nodes / 31 s, (2,2,2,1,1) at
7.0M nodes / 72 s — the last two with waste budget 0. Exactly A and B survive, so the
per-part half is **sharp**.

*Global.* cov(A) = 5 and cov(B) = 4, so six parts cover 30 − b pairs with b parts of
type B; intersecting forces 30 − b ≥ C(8,2) = 28, so **b ≤ 2**, and b = 2 forces the
excess to be exactly **0**. One search settles it: with column 0 pinned to B and the
waste budget forced to 0 the engine returns nothing. Its positive control — the
identical call at waste budget 1 — *does* find a 5A+1B object, so the zero
discriminates rather than being systematic.

**Why the distinction is not pedantic.** The global half is the one AKP's Lemma 2.9
actually consumes: its Δ=4 case bounds the intersections by 7 + 6·4 = **31** against
**32** required — a margin of one, which a second B part erases. So the half we had
*not* proven was precisely the load-bearing half of the citation we lean on.

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
