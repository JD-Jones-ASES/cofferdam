# Certificate 0006 — (L8), the excess-concentration incompatibility: **m ≥ 21**

**Status: GREEN.** 19 checks, 66 s, `python3 verify.py`, stdlib only, no solver.

| claim | label |
| --- | --- |
| (L7) for x,y in different parts, \|E(x) ∩ E(y)\| ≥ d(x)+d(y)−(m−g(4)) | PROVEN-BY-CERTIFICATE |
| (L8) the excess-concentration incompatibility | PROVEN-BY-CERTIFICATE |
| **m = 20 is impossible** | **PROVEN-MODULO-CITATION** (f(6)=13) |
| **a Ryser r=6 counterexample has m ≥ 21** | **PROVEN-MODULO-CITATION** (f(6)=13) |

Certificate 0005 excluded m ≤ 19 and left Δ = 7 at m = 20 as its sole survivor.
This certificate excludes m = 20 outright. Together: **m ≥ 21** — the statement
this lab was seeded with. **But see the attribution section: the seeds of both
certificates came from Codex, so the result is partially independent, not blind.**

## Origin: Codex — and what that costs the claim

> *Let x,y be the forced degree-7 vertices and put c = |E(x) ∩ E(y)| ≥ 2. Feed
> that overlap back into the pair-intersection count. The c common-star edges
> contribute at least C(c,2) ≥ 1 units of excess, because every pair among them
> meets at both x and y. Therefore Σ_v C(d(v),2) ≥ 191, not merely 190.*

**This is Codex's, not ours, and it arrived as exact algebra rather than a
heuristic** — every identity above is exact. No sealed path was read; the
statements were passed to this lab in conversation. But a station of the
correlated chain seeded the final step, so **m ≥ 21 as reached here is partially
independent, not blind**, and must not be called an independent confirmation of
that chain's m ≥ 21. See D-010.

Ours: the setting (the 105 configurations, the forced pair of degree-7 vertices,
(L7), the dead heat), t_ef ≤ 5, the B ≤ ⌊5X/2⌋ form, the **δ-budget that does the
actual killing** — a different mechanism from the one Codex proposed ("every
counted obligation used exactly once — or equivalently linearity in the relevant
trace") — the W_t argument, the sweep, and every control.

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
explicit objects in checks 2–5):

| | |
| --- | --- |
| (I1) | Σ_e k_e = Σ_j M_j |
| (I2) | Σ_e C(k_e,2) = Σ_{i<j} c_ij =: **A** |
| (I3) | Σ_{e<f} C(t_ef,2) = Σ_{i<j} C(c_ij,2) =: **B** |
| (I4) | Σ_{e<f} t_ef = Σ_j C(M_j,2) |

and four facts:

- **(L2)** Σ_v C(d,2) = Σ_{e<f} |e∩f|, so **X = Σ_{e<f}(|e∩f| − 1)** — Codex's identity.
- **(L7)** c_ij ≥ M_i + M_j − (m − g(4)): delete both stars, τ ≥ 4 survives on
  m − |E(u_i) ∪ E(u_j)| edges, so that count is ≥ g(4) = 8.
- **(C2)** |e∩f| ≥ t_ef, hence Σ_{e<f}(t_ef − 1)⁺ ≤ X.
- **(C3)** t_ef ≤ 5 for distinct edges — agreeing in all six parts means e = f.

Now put δ(k) = C(k,2) − (k−1) ≥ 0, so δ(1)=δ(2)=0, δ(3)=1, δ(4)=3, δ(5)=6. By
(I1)+(I2), **Σ_e δ(k_e) = A − Σ_j M_j + m =: D.** And since t_ef ≤ min(k_e,k_f),
every edge-pair at level ≥ t lies inside W_t = {e : k_e ≥ t}, so the number of
such pairs is at most C(|W_t|,2); δ increasing then gives

  **D = Σ_{t≥3}(δ(t) − δ(t−1))·|W_t| ≥ q₃ + 2q₄ + 3q₅**, q_t = least q with C(q,2) ≥ #{pairs at level ≥ t}.

**(L8) is the collision of three demands.** (L7) forces A, hence B, to be large.
Since C(t,2)/(t−1) = t/2 ≤ 5/2, (C2)+(C3) give **B ≤ ⌊5X/2⌋** — so B can only be
carried by *many shallow* pairs, which X forbids, or by *deep* ones, which D
forbids. At m = 20 every admissible configuration fails one of the two.

## Why m = 20 dies and m = 21 does not

The numbers are interpretable, which is the reassuring part. At m = 20 the best
per-part profile scores 33, so reaching C(20,2) = 190 leaves an excess of at most
**X = 8** — while (L7) with two forced degree-7 vertices demands **B ≥ 15**.
Fifteen units of pair-depth cannot be bought with eight units of excess unless the
pairs are deep, and deep pairs need high-k edges, whose budget is also only 8.

The dead heat certificate 0005 recorded — all six parts (7,4,3,2,2,2), where the
(L4)/(L7) squeeze ended 30 against exactly 30 — is now decided: equality forces
every c_ij = 2, hence B = 15 exactly, and with X = 8 and t ≤ 5 only two level
structures reach 15: {5,3,2,2} and {4,4,3}. They need δ-budgets of 13 and 9
against D = 8. Both bust.

At m = 21 the same arithmetic leaves room: the analogous X is 30, not 8. Hence
check 18.

## Controls — the reason to believe a negative result

This result lands exactly on the number the lab was asked to check, which by
D-005 is the most dangerous direction for an error to point. So:

1. **Positive control (check 11).** The δ-budget inequality is the one that does
   the killing, so it is checked on objects that *exist*: on all four witnesses
   (3, 5, 8 and 9 edges) it holds with room — D = 12, 4, 6, 12 against needs of
   6, 0, 0, 7.
2. **Not-too-strong control (checks 18–19).** An argument that killed every m
   would be proving Ryser at r = 6, an open problem, and would therefore be
   wrong. The identical machinery at m = 21 leaves **6198 of 43875** multisets
   alive. (L8) discriminates.
3. **Identity audit.** All four identities and both inequalities were also
   verified by brute force on 420 random intersecting objects at seven sizes
   during development; checks 1–10 keep four deterministic instances.
4. **Conservative ceiling.** The bound on A uses only "Σ_e k_e = Σ_j M_j over m
   edges with k_e ≤ 6", i.e. maximum concentration — **no value pool and no (L4)
   input at all.** An earlier version used an exact pool DP; dropping it makes the
   ceiling weaker, hence the test strictly more permissive, and it still kills all
   105. That removes a whole layer of machinery from the trust chain. (The pool DP
   and the weak bound were separately cross-checked to agree at 30 on the dead-heat
   case, by two independent implementations.)
5. **Overlap with 0005 (check 17).** m ≤ 19 has no admissible configuration at
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

So the external exposure of m ≥ 21 is not a constant but **one lemma: AKP 2.9** —
whose main structural input we have proven ourselves, and in whose printed
statement we found (and corrected) an error. The ledger: three lemmas of ours, one
exhaustive search of ours (N(4) = 9, 52.0M nodes), two counting lemmas of ours,
one peer-seeded reframing (Codex, re-derived here), one cited lemma.

## What is NOT claimed

- Nothing says a counterexample exists at 21 or above. The floor localises; it
  does not construct.
- **Q13 is not answered** — the question of whether a 13-edge τ=5 object can have
  a part of minimum degree 2. It became *unnecessary*, not settled. It remains the
  natural next lever, since answering it NO would push the floor past 21 by the
  0005 ladder alone.
- f(6) ≥ 13 is still unverified here, and it is the whole difference between
  m ≥ 19 and m ≥ 21.

## Reproduce

```bash
python3 verify.py
```

66 s, deterministic. The m = 21 control is stopped at the first survivor; the full
sweep there (43875 multisets, 6198 survivors) takes a few minutes.
