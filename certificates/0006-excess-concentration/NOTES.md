# Certificate 0006 — (L8), the excess-concentration incompatibility: **m ≥ 21**

**Status: GREEN.** 22 checks, 0 notes, 166 s, `python3 verify.py`, stdlib only,
no solver. Green under `python3 -O` as well as plain `python3`. Every `check` is
machine-tested and there are no `note`s; the closing Result block, like any
summary, states conclusions rather than testing them.

| claim | label |
| --- | --- |
| (L7) for x,y in different parts, \|E(x) ∩ E(y)\| ≥ d(x)+d(y)−(m−g(4)) | PROVEN-BY-CERTIFICATE |
| (L8) the excess-concentration incompatibility | PROVEN-BY-CERTIFICATE |
| **m = 20 is impossible** | **PROVEN-MODULO-CITATION** (f(6)=13) |
| **a Ryser r=6 counterexample has m ≥ 21** | **PROVEN-MODULO-CITATION** (f(6)=13) |

Certificate 0005 excluded m ≤ 19 and left Δ = 7 at m = 20 as its sole survivor.
This certificate excludes m = 20 outright. Together: **m ≥ 21** — the statement
this lab was seeded with.

> **Superseded in strength, not in content.** [Certificate 0007](../0007-citation-free-floor)
> runs this same machinery on the weaker rung N(5) ≥ 11 — which is ours — and
> still kills every m ≤ 20, so **the floor does not depend on f(6) = 13** and is
> PROVEN-BY-CERTIFICATE citing nothing. The labels above are left as they stand
> because they are accurate about what *this* file proves. Read this certificate
> as the cited-input route to a result 0007 reaches with no citation at all.

## Origin

The seed is Codex's, and it arrived as exact algebra:

> *Let x,y be the forced degree-7 vertices and put c = |E(x) ∩ E(y)| ≥ 2. Feed that
> overlap back into the pair-intersection count. The c common-star edges contribute
> at least C(c,2) ≥ 1 units of excess, because every pair among them meets at both x
> and y. Therefore Σ_v C(d(v),2) ≥ 191, not merely 190.* Then: re-open the equality
> case of the 30-against-30 squeeze.

Ours: the setting it applies to (the 105 configurations, the forced pair of degree-7
vertices, (L7), the dead heat), t_ef ≤ 5, the B ≤ ⌊5X/2⌋ form, the δ-budget that does
the actual killing — a different mechanism from the one suggested — the W_t argument,
the sweep, and every control.

It is the hinge. The pair count is not just a *lower* bound to
be met — the amount by which it is exceeded is a **budget**, and overlapping
high-degree stars spend it. Certificate 0005 had used the pair count only as
"≥ C(m,2)"; reading the surplus as a resource is what closes m = 20.

Carried through, one refinement is needed beyond the ≥191: the same overlap that
costs excess *also* forces edges rich in maximum-degree vertices, and those have
their own budget. The two budgets together are (L8).

## The argument

Choose one maximum-degree vertex u_j per part; U = {u_1..u_6}, M_j = d(u_j), and

    k_e  = |e ∩ U|          c_ij = |E(u_i) ∩ E(u_j)|
    t_ef = #{j : u_j ∈ e ∩ f}    X = Σ_v C(d(v),2) − C(m,2)

Four identities, each a double count (all four verified by brute force on
explicit objects, each with its own check):

| | |
| --- | --- |
| (I1) | Σ_e k_e = Σ_j M_j |
| (I2) | Σ_e C(k_e,2) = Σ_{i<j} c_ij =: **A** |
| (I3) | Σ_{e<f} C(t_ef,2) = Σ_{i<j} C(c_ij,2) =: **B** |
| (I4) | Σ_{e<f} t_ef = Σ_j C(M_j,2) |

and four facts:

- **(L2)** Σ_v C(d,2) = Σ_{e<f} |e∩f|, so **X = Σ_{e<f}(|e∩f| − 1)**.
- **(L7)** c_ij ≥ M_i + M_j − (m − g(4)): delete both stars, τ ≥ 4 survives on
  m − |E(u_i) ∪ E(u_j)| edges, so that count is ≥ g(4) = 8.
- **(C2)** |e∩f| ≥ t_ef, hence Σ_{e<f}(t_ef − 1)⁺ ≤ X.
- **(C3)** t_ef ≤ 5 for distinct edges — agreeing in all six parts means e = f.

Now put δ(k) = C(k,2) − (k−1) ≥ 0, so **δ(0)=1**, δ(1)=δ(2)=0, δ(3)=1, δ(4)=3,
δ(5)=6, δ(6)=10. By (I1)+(I2), **Σ_e δ(k_e) = A − Σ_j M_j + m =: D.** And since
t_ef ≤ min(k_e,k_f), every edge-pair at level ≥ t lies inside W_t = {e : k_e ≥ t},
so the number of such pairs is at most C(|W_t|,2), i.e. |W_t| ≥ q_t.

δ is *not* increasing — it **dips at k = 0 → 1** (δ(0)=1 > δ(1)=0) and is only
nondecreasing on k ≥ 1 — so the layer cake cannot be started at t = 3. In full,
D = m·δ(0) + Σ_{t≥1}(δ(t) − δ(t−1))·|W_t|, where δ(1)−δ(0) = −1 collapses the
base and t=1 layers to n₀ := #{e : k_e = 0} = m − |W₁|, and δ(2)−δ(1) = 0 kills
the t=2 layer:

  **(C5)  D = n₀ + |W₃| + 2|W₄| + 3|W₅| + 4|W₆| ≥ q₃ + 2q₄ + 3q₅**, q_t = least q with C(q,2) ≥ #{pairs at level ≥ t}.

Both dropped terms are ≥ 0, so the sweep's bound can only **understate** D — the
direction that makes a kill harder, never easier.

> **Erratum, ours.** Through 2026-07-26 this note and the certificate docstring
> printed (C5) as `D = Σ_{t≥3}(δ(t)−δ(t−1))·|W_t|`, omitting n₀. That equality is
> false, and it is falsified by a witness *this certificate already ships*: the
> 5-edge g(3) witness has n₀ = 1, so the printed form reads 3 where D = 4. The
> code was never affected — `l8_kills` computes D exactly from (C4), `A − S + m`,
> and never forms |W_t| at all — so no result moves. Found by Codex in the
> adversarial pass; the failure mode is that **an identity which is displayed but
> never asserted is an identity nobody has tested**, which is why (C5) is now a
> check rather than prose. Raised by the same reading: had the omission gone the
> other way it would have *overstated* D and could have manufactured a false kill.

**(L8) is the collision of three demands.** (L7) forces A, hence B, to be large.
Since C(t,2)/(t−1) = t/2 ≤ 5/2, (C2)+(C3) give **B ≤ ⌊5X/2⌋** — so B can only be
carried by *many shallow* pairs, which X forbids, or by *deep* ones, which D
forbids. At m = 20 every admissible configuration fails one of the two.

## Why m = 20 dies and m = 21 does not

The numbers are interpretable, which is the reassuring part. At m = 20 the best
per-part profile scores 33, so reaching C(20,2) = 190 leaves an excess of at most
**X = 8** — while (L7), in the six-copies-of-(7,4,3,2,2,2) case, demands
**B ≥ 15**. (B ≥ 15 is that configuration's floor, not a bound holding across all
105; the general statement is just that (L7) forces B large.)
Fifteen units of pair-depth cannot be bought with eight units of excess unless the
pairs are deep, and deep pairs need high-k edges, whose budget is also only 8.

The dead heat certificate 0005 recorded — all six parts (7,4,3,2,2,2), where the
(L4)/(L7) squeeze ended 30 against exactly 30 — is now decided: equality forces
every c_ij = 2, hence B = 15 exactly, and with X = 8 and t ≤ 5 only two level
structures reach 15: {5,3,2,2} and {4,4,3}. They need δ-budgets of 13 and 9
against D = 8. Both bust.

**The margin, stated because "conservative" hides it.** 91 of the 105 die on the
excess bound before the δ-budget is consulted at all; 14 reach it. The tightest
point in the whole kill is that dead heat at A = 30 under level structure {4,4,3}:
**D = 8 against need = 9 — a margin of exactly one**, and the need is exact, not a
bound. Three inputs (g(4) = 8, X, the δ-budget) each flip m = 20 if moved by a
single unit. Five other quantities were loosened by large amounts in an
adversarial pass with no survivors appearing — Pc, U, B_cap, the loop bounds and
the omitted t = 6 level. (**L is binding**, and a later pass found it the tightest
thing in the file; an earlier version of this note wrongly listed it as inert.) A certificate that says
"conservative" without saying "margin 1" has told the reader the safe half.

At m = 21 the same arithmetic leaves room: the analogous X is 30, not 8. That is
what the not-too-strong control exploits.

## Controls — the reason to believe a negative result

This result lands exactly on the number the lab was asked to check, which by
D-005 is the most dangerous direction for an error to point. So:

1. **Positive control.** The δ-budget inequality is the one that does
   the killing, so it is checked on objects that *exist*: on all four witnesses
   (3, 5, 8 and 9 edges) it holds with room — D = 12, 4, 6, 12 against needs of
   6, 0, 0, 7.
2. **Not-too-strong control.** An argument that killed every m
   would be proving Ryser at r = 6, an open problem, and would therefore be
   wrong. The identical machinery at m = 21 leaves **6198 of 43875** multisets
   alive. (L8) discriminates.
3. **Identity audit.** All four identities and both inequalities were also
   verified by brute force on 420 random intersecting objects at seven sizes
   during development; the shipped identity checks keep four deterministic
   instances.
4. **Which direction each half runs — and where a false kill could hide.**
   Everything *inside* `l8_kills` is a **relaxation**: it permits configurations
   reality forbids, so a total kill under it is conservative, and an adversarial
   pass confirmed no off-by-one in any loop bound, that the greedy B_min equals the
   exact DP minimum, and that the δ-budget never exceeds the true requirement. But
   `profiles()` runs the *other* way — it is a **restriction**, forbidding
   configurations via the N-caps and lemmas (A)/(B)/(C). **That is the only place a
   false kill could live**, and the blanket claim that "every relaxation makes
   survival easier" does not reach it. Measured: N(4) = 8 instead of 9 turns 0
   survivors into 1445 of 3664. So the weakest step in the chain is N(4) = 9, not
   anything in this file.
5. **Conservative ceiling.** The bound on A uses only "Σ_e k_e = Σ_j M_j over m
   edges with k_e ≤ 6", i.e. maximum concentration — **no value pool and no (L4)
   input at all.** An earlier version used an exact pool DP; dropping it makes the
   ceiling weaker, hence the test strictly more permissive, and it still kills all
   105. That removes a whole layer of machinery from the trust chain. (On the dead heat the *floor* L is 30
   and the shipped weak ceiling U is 105; an earlier version of this note said the
   two ceiling implementations "agree at 30", which confused the floor with the
   ceiling. The claim that matters is unaffected: the weak ceiling is higher, so
   the test is more permissive, and it still kills all 105.)
6. **Overlap with 0005.** m ≤ 19 has no admissible configuration at
   all here, consistent with 0005 rather than in tension with it.

## Cited-input discipline — the citation, read firsthand

The only external input is **f(6) ≥ 13**, entering at exactly one place: the k=1
cap Δ ≤ m − 13. Without it the floor is **m ≥ 19** (certificate 0005).

It has now been checked in the source (Abu-Khazneh–Pokrovskiy, arXiv:1409.4938 —
published literature, which the seal does not cover). It is **proved, not inferred
from the 13-edge construction**:

- **Theorem 1.1: f(6) = 13**, "also proved independently by Aharoni, Barat and
  Wanless".
- §2: "we will first show that f(6) > 12, by proving that f(6) ≠ 12 and then
  combine it with the result f(6) > 11 established in [11]" — [11] being
  Mansour–Song–Yuster.
- **Lemma 2.9 (f(6) ≠ 12)** proceeds by case analysis on Δ(H), and its hard case
  is stated plainly: "The case Δ(H) = 4 turns out to be more difficult … to settle
  it we will require some facts concerning the degree structure of intersecting
  6-partite hypergraphs with 8 hyperedges and a covering number equal to 4."

**That is Lemma 2.8 — the lemma this lab found an arithmetic erratum in, and whose
corrected form certificate 0005 proves outright.** So the loop closes:

| piece of f(6) ≥ 13 | status here |
| --- | --- |
| f(6) ≥ 12 (MSY, f(6) > 11) | **independently ours** — cert 0001 derives g(5) ≥ 12 |
| Lemma 2.8, the structural input to the hard case | **independently ours** — cert 0005 proves the corrected statement by exhaustion, and re-derives Lemma 2.1's degree-3 clause |
| **Lemma 2.9 (f(6) ≠ 12), the case analysis itself** | **cited, not reproduced** |

So the external exposure of m ≥ 21 *for this certificate* is not a constant but
**one lemma: AKP 2.9** — (certificate 0007 has no external exposure at all) —
whose main structural input, **Lemma 2.8**, we have proven ourselves and in whose
printed statement we found and corrected an error. (The erratum is in 2.8, not in
2.9; an earlier phrasing here attached it to the wrong lemma.) The ledger: three lemmas of ours, one
exhaustive search of ours (N(4) = 9, 52.0M nodes), two counting lemmas of ours,
one peer-seeded reframing (Codex, re-derived here), one cited lemma.

## What is NOT claimed

- Nothing says a counterexample exists at 21 or above. The floor localises; it
  does not construct.
- **Q13 is not answered** — the question of whether a 13-edge τ=5 object can have
  a part of minimum degree 2. It became *unnecessary*, not settled. It remains the
  natural next lever — though answering it NO gives N(5) ≥ 14, which on the 0005
  ladder reaches exactly 21 rather than past it, and FHMW Lemma 2.1(iii) now looks
  like the cheaper route (notebook/2026-07-26-fhmw-lemma-21.md).
- f(6) ≥ 13 is not verified here, and at the time this certificate was written it
  was the whole difference between m ≥ 19 and m ≥ 21. **Certificate 0007 removed
  that dependence**: the floor of 21 holds citing nothing.

## Reproduce

```bash
python3 verify.py
```

166 s, deterministic, green under `python3 -O` as well. The m = 21 control now
**sweeps the full 43875 and reports 6198 survivors** — it used to stop at the first
one while this section quoted a number the certificate never computed.

> Caught in the same adversarial pass that produced the (C5) erratum, and it is the
> same defect one layer out: **prose no check tests.** The status line was updated
> and the Reproduce block was not. If a certificate's own README can drift from its
> code inside a single session, assume every unasserted sentence in it has.
