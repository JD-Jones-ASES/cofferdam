# Certificate 0007 — the floor needs no citation: **m ≥ 21**, citing nothing

**Status: GREEN.** 18 checks + 1 note, ~2 min, `python3 verify.py`, stdlib only,
no solver. Green under `python3 -O` as well.

> The note is the peeling lemma (P), which is **proved by hand in certificate
> 0005 and not tested here** — `9 + 2 == 11` would be a tautology, not a test of
> the lemma. An earlier version of this file shipped it as a check and claimed
> "nothing stated-but-untested in this certificate", which was exactly the
> inflation D-015 was written about, committed in the certificate that records
> D-015. Caught by the completeness pass.

| claim | label |
| --- | --- |
| (P) N(5) ≥ N(4) + 2 = 11, by peeling | PROVEN-BY-CERTIFICATE (0005) |
| m = 19 impossible, citing nothing | **PROVEN-BY-CERTIFICATE** |
| m = 20 impossible, citing nothing | **PROVEN-BY-CERTIFICATE** |
| **a Ryser r=6 counterexample has m ≥ 21** | **PROVEN-BY-CERTIFICATE, CITING NOTHING** |

Certificates 0005 and 0006 reached m ≥ 21 as PROVEN-MODULO-CITATION. The number
does not change. What changes is that **nothing external stands behind it.**

> **Superseded upward, 2026-07-27 (turn 9).** Certificate 0009 pins
> **N(5) = 13 citing nothing** (and g(5) = 13), so the weak rung (P) this
> certificate deliberately ran on is no longer the best citation-free input —
> the free ladder now *equals* the old cited one. Everything here stands
> a fortiori (this certificate solved a strictly harder problem than it had
> to: 7,159 multisets at m = 20 where 105 now suffice). Two footnotes from
> the turn-9 measurements: N(5) ≥ g(5) ≥ 12 was already available
> citation-free from certificate 0001 when this was written — one free unit
> nobody used — and, measured at m = 21/22, the rung value 11 vs 12 changes
> **nothing** (the k = 2 cap dominates; the profile sets are identical), so
> the conservatism was real but cost-free. The closing plea below for "a
> third independent implementation of N(4) = 9" was answered by certificate
> 0010 — with a hand proof rather than a third search.

## Where the citation was, and why it was never needed

f(6) = 13 entered at exactly one place — the k=1 rung of the (C) ladder, as the
cap Δ ≤ m − N(5) with N(5) = 13. Certificate 0005 already derives a weaker rung
citing nothing:

> **(P)** peel the smallest block of an N(5) witness's full part. The residual has
> τ ≥ 4, and the surviving vertices of that part keep every edge they had, so
> their degrees are unchanged and the part is still full — an N(4) witness. The
> block removed had size ≥ 2. Hence **N(5) ≥ N(4) + 2 = 11.**

Under (P) the *pair count* no longer closes m = 19, which is precisely why
certificate 0005's citation-free floor stopped there. But (L8) is far stronger
than the pair count, and (L8) closes it:

| ladder | m = 19 | m = 20 |
| --- | --- | --- |
| N(5) = 13 (cited) | 0 admissible multisets | 105 admissible, **0 survive** |
| **N(5) = 11 (ours)** | **33 admissible, 0 survive** | **7159 admissible, 0 survive** |

**The whole range is swept here, not inherited.** m ≤ 11 dies on lemmas (A)+(B)
before any search — six parts of ≥ 6 active vertices of degree ≥ 2 force m ≥ 12 —
and m = 12..18 are swept and empty. Certificate 0005's floor would have covered
m ≤ 18, but its ladder loop *used to* run `range(14, 24)` and so never tested
m = 12 or 13 (D-016; 0005 now starts at 12). Inheriting a floor means inheriting
another file's loop bounds, so this one sweeps its own. So m ≥ 21.

## The direction, which is the whole point

Weakening N(5) from 13 to 11 **admits more** configurations — 34 profiles rather
than 32 at m = 20, 7159 multisets rather than 105. This is a *strictly harder*
problem than certificate 0006 solved, not a different one: the containment check verifies that
0006's 105 multisets are a proper subset of the 7159 killed here. A citation-free
result obtained by *loosening* an input and still killing everything cannot be an
artefact of the input.

## Controls — this result raises our own claim, which is the dangerous direction

D-005 says an error that flatters the expected answer is a verifier's worst kind.
This one flatters harder than m ≥ 21 did: it upgrades the label. So:

1. **Not-too-strong.** At m = 21 the identical machinery on the
   identical weak ladder still leaves survivors. Had it killed m = 21 as well, it
   would be "proving" Ryser at r = 6 and would therefore be wrong. *The full
   m = 21 count is not swept here* — the check stops at the first survivor and
   says so. What the control needs is existence, and that is what it asserts.
2. **Sensitivity on the real hinge.** Set N(4) = 8 — the value the
   52.0M-node search would have produced had it under-enumerated — and m = 20
   comes back to life among 180,480 multisets. So the kill genuinely rests on
   N(4) = 9 and is not reachable without it.
3. **Containment.** 105 ⊂ 7159, so this subsumes 0006 rather than
   sitting beside it.
4. **Three implementations, one of them blind.** The m = 19 and m = 20 sweeps were run through an
   independently written checker — level structures enumerated directly from the
   (C2) budget instead of swept through B, and B_min by exact dynamic programming
   instead of the greedy most-equal allocation — reproducing 33/0, 7159/0, and
   survivors at m = 21 in every regime. Agreement between two implementations of
   the same relaxation does not prove the relaxation sound; it rules out a coding
   slip in one of them, which is a different and smaller claim. A third
   reproduction came from a subagent auditing an unrelated question, which had
   not been told this result was being pursued and reported 33/0 and 7159/0
   independently.

## What this retires, and what it does not

**Retired:** the dependence. Every question that hung on the citation — whether
AKP Lemma 2.9 holds, whether its printed definition of f(6) (τ = r−1 in the
abstract, τ ≥ r−1 in the introduction) matches the τ ≥ 5 form the ladder actually
consumes, whether the erratum in Lemma 2.8 touches the constant — is **moot for
the floor**. Those remain live as literature questions and for any push past 21.

**Not retired:** the reading itself. f(6) = 13 is true, proved twice
independently (ABW Thm 2.7 under exactly the τ ≥ r−1 form the ladder needs; AKP
Thm 1.1), and remains the cheaper route to the same rung. Certificates 0005 and
0006 keep it and keep their labels — this certificate does not rewrite them, it
stands over them.

**The exposure moved rather than vanished.** The load-bearing step is now
**N(4) = 9**, one exhaustive search of ours at 52.0M nodes. A search that
under-enumerates fakes a proof, and the sensitivity check prices exactly what rests on this
one. A third independent implementation is now the single most valuable
contribution anyone could make to this repo.

## Origin

The sensitivity that pointed here was raised by **Grok's Witness-Lab** in the
adversarial pass: it observed that (L8) still reported no survivors at m = 20
under the weakened caps, and suggested the citation might be unnecessary. Its
stated inference did not follow — it tested m = 20 only, and concluded "combined
with 0005's citation-free m ≥ 19, that would give m ≥ 21", but m ≥ 19 leaves
m = 19 *standing*, so killing m = 20 alone leaves the floor at 19. The missing
rung is the m = 19 sweep, which is the first line of this certificate's table and
had not been run anywhere. Pointer theirs; the rung, the controls, the
containment argument and this certificate are this repo's.

Worth recording as a method note rather than a scoring one: the useful part of an
adversarial pass was not a defect it found in our work. It was a **sensitivity it
ran on ours that we had not thought to run** — and its value survived its own
conclusion being wrong.

## Reproduce

```bash
python3 verify.py
```

~2 min (111 s measured under `python3 -O`), deterministic. Green under both
`python3` and `python3 -O`.
