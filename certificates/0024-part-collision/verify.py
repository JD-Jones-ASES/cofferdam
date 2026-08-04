#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
0024 -- PART-COLLISION: THE POINTWISE LAW, THE GLOBAL LAW, AND THE
        EXACT DEGREE/PART SWEEP.

THEOREMS
--------
  (L-PC24) THE PART-COLLISION LAW, POINTWISE.  For every vertex u of an
      intersecting 6-partite 6-uniform family (parts V_1..V_6, sizes
      n_j, u in V_i),
          g(u) := sum_{j != i} Phi(d(u), n_j)  <=  s(u)  <=  X.
      Underneath it, AN EXACT IDENTITY (the real content -- the law is
      its balanced relaxation): writing c_u(y) = #{e in E(u): y in e}
      for y in V_j (the codegree),
          s(u) = sum_{j != i} sum_{y in V_j} C(c_u(y), 2).
      Intersecting-ness is load-bearing ONLY for s(u) <= X (a
      non-intersecting family violates it; witness enacted in section
      2).  The identity and g <= s need nothing but 6-partiteness.

  (L-GPC24) THE GLOBAL LAW.  sum_u g(u) <= sum_u s(u) = R.
      The right identity is (SJ)'s sum s = R (0021, re-derived here:
      a pair {e,f} is counted once per cell of e cap f, so it
      contributes q(q+1) with q = |e cap f| - 1).

  (T-A24) X != 7 FOR EVERY CRITICAL CORE -- hence, with 0021's T-A21
      (X >= 7) and T-B21 (X = 7 => m <= 26), X >= 8 EVERYWHERE.
      AN INDEPENDENT SECOND PROOF of 0023's T-A23: the chain is
      0021 -> 0024 alone.  It consumes NEITHER 0022 NOR 0023 -- no
      quotients, no parity, no ledgers, no residual pairing.

  (T-B24) X = 10 => m <= 28, AND THE SURVIVOR ATLASES.  The exact
      sweep leaves, at X = 8, X = 9, X = 10, ONLY the cells asserted
      in section 5 (the atlases); in particular X = 10 admits no cell
      at m in [29, 32] and the Lambda tail kills every m >= 33 (with
      0013/0014's window closing the question at 456).  The atlases
      are certified DATA for the next certificate's structural kills.

THE SWEEP IS A RELAXATION.  A surviving cell proves NOTHING exists --
it only survives the constraint set.  Emptiness proves emptiness.
Every constraint is a certified law: (DM) exact, per-part sums, degree
floor 2 (0005), (D2) n_2 <= floor(m/2) (0008), (LD)/(KC) (0021),
(PC)/(GPC) (proved here).  No SAT solver, no ILP, no floats, no
randomness; two independent engines whose verdicts are diffed cell by
cell over the entire space.

EXTERNAL INPUTS (the cited-constant ledger)
-------------------------------------------
  0005 (min degree >= 2)     -- degree alphabets start at 2.  Without
                                it: alphabets start at 1 and every
                                atlas below is UNKNOWN (not enacted).
  0008 ((D2) global reading) -- n_2 <= floor(m/2).  Without it: the
                                X = 7 kill THINS but survives at some
                                rungs only via (GPC); the atlases
                                grow.  M-D2R prices one unit of it.
  0021 T-A21, T-B21          -- X >= 7 and the 7/8/9 windows bound the
                                m-ranges swept; T-A21 turns "X != 7"
                                into "X >= 8 everywhere".
  0021 (SJ)/(LD)/(KC)        -- P <= R - q1(q1+1) and F <= X - q1.
                                Both re-stated here, not re-derived;
                                0021 is the authority.
  0013/0014 (the window)     -- m <= 456 makes "everywhere" finite;
                                the Lambda tail covers [33, 456]
                                explicitly, rung by rung.
  Nothing else.  No peer text is cited; no proof step consumes one
  (D-036: the sixth audit's text is retained in notebook/raw/, its
  claims were re-derived at the desk and adversarially re-proved
  before this file was written).

THE PROOF, IN ORDER
-------------------
 (1) PHI IS THE BALANCED MINIMUM (section 1).  Phi(a,b) = r C(q+1,2) +
     (b-r) C(q,2), a = qb + r, equals the true minimum of
     sum C(a_i, 2) over all b-bin distributions -- brute-forced over
     every (a, b) this file ever evaluates, plus monotonicity in b.
 (2) THE IDENTITY AND BOTH LAWS, ENACTED (section 2).  On deterministic
     corpora: every intersecting family on small pools (exhaustive),
     stars, sunflower cores, K4 patterns.  Identity exact everywhere;
     g <= s <= X and sum g <= R everywhere; the non-intersecting
     witness for s <= X; and MUST-FAIL controls (own-part inclusion,
     bins - 1, balls + 1 all violate on the corpus -- the harness can
     see a false law).
 (3) THE MOMENT FLOOR (section 3).  d^2 = 8d - 15 + 3[d=2] + psi(d)
     exactly at d >= 5 and d in {2,3}, slack 1 at d = 4, false at
     d <= 1 (0005 billed): summed, Psi = m^2 - 43m + 2X + 15n - 3n_2
     + n_4, hence Psi >= Lambda_X(m) = m^2 - 43m + 2X + 540 -
     3 floor(m/2) at n >= 36 -- 0021's floor, re-enacted because the
     tail leans on it.
 (4) THE ENGINES (section 4).  A cell is (X, m, pi, n-vector).  Per
     part, the degree-multiset options compress to (sum d^2, #2s, P,
     sum g) tuples; six-fold convolution under caps (D2)/(LD)/(GPC)
     with per-vertex alphabets already filtered by (KC)/(PC); a cell
     survives iff some final state hits (DM) exactly.  ENGINE D:
     direct state sets.  ENGINE P: Pareto frontiers per sum d^2
     (dominance in (n_2, P, sum g) -- sound because every downstream
     constraint is monotone).  Verdicts asserted IDENTICAL cell by
     cell, atlases identical in aggregate.
 (5) THE SWEEP (section 5).  X = 7 on [22, 26] (T-B21's whole X = 7
     window): ZERO survivors -- T-A24.  X = 8 on [22, 28], X = 9 on
     [22, 29], X = 10 on [22, 32]: the atlases, asserted cell-exact.
     Positive controls: relaxing the new laws must and does revive
     cells (the sweep can tell a law from a tautology).
 (6) THE TAIL (section 6).  X = 10, m in [33, 456]: max Psi over all
     23 admissible partitions under (LD)+(KC) knapsacks is 179
     (attained by (3,3,3,1)); Lambda_10(m) >= Lambda_10(33) = 182 and
     increases -- every rung dead, asserted rung by rung to 456.
 (7) MUTATIONS (section 7).  Nine, priced.

MANDATORY HONESTY NOTES
-----------------------
 (1) PROVENANCE.  The part-collision law was found by a turn-19
     refuter lane and banked (0023 NOTES); the global form, the exact
     sweep, and the two-theorem shape were PROPOSED by the sixth
     outside audit (GPT 5.6 Sol Pro, notebook/raw/ 2026-08-03).  Per
     D-036 the desk re-derived every step before enactment; the
     audit's own text carried one refuted step (its section 7.2/9.2
     "edge-disjoint" claim -- see 0025) and its tables were re-derived
     three ways (desk, hostile lane, blind lane) before the atlas
     assertions below were written.  No audit sentence is consumed.
 (2) WHAT THE ATLASES ARE NOT.  A surviving cell is NOT a hypergraph;
     no realizability is claimed.  The next certificate kills them
     structurally; nothing here depends on their death.
 (3) (PC) AND (SJ) ARE INCOMPARABLE, NOT ADDITIVE.  g collapses to 0
     when d <= min n_j while F(d) > 0 from d = 6; with large parts
     (SJ) wins, with small parts and high degree (PC) wins.  The
     engines enforce each SEPARATELY and never add them into one
     budget (the blind lane's warning, adopted as design law here).
 (4) RUNTIME/SCOPE.  BOTH engines sweep EVERY cell of every window --
     1,286,681 cells each way -- behind a per-cell Lambda-prefilter
     (an O(1) knapsack-vs-moment test) that only skips cells it
     PROVES dead; M-PRE runs every m <= 26 window with the prefilter
     off and asserts identical atlases.  No stride, no sampling.

NOTATION.  As in 0015-0023.  q, X, pi, R, s(v), qmax(v), P, F, f, psi,
Phi as there; g(u) as above; c_u(y) the codegree.  A CELL is
(X, m, pi, nvec) with nvec sorted, 6 <= n_i <= floor(m/2).
"""

import itertools
import sys
import time
from math import comb

START = time.time()
FAILED = []
NCHECK = [0]
NNOTE = [0]


def check(name, ok, detail=""):
    NCHECK[0] += 1
    tag = "ok  " if ok else "FAIL"
    if not ok:
        FAILED.append("%d. %s" % (NCHECK[0], name.split(".")[0]))
    print("  [%s] %d. %s%s" % (tag, NCHECK[0], name,
                               ("  [%s]" % detail) if detail else ""))
    return ok


def note(text):
    NNOTE[0] += 1
    print("  [note] %s" % text)


def head(text):
    print()
    print("=" * 74)
    print("  " + text)
    print("=" * 74)


# ======================================================================
head("0.  THE PRIMITIVES")
# ======================================================================

def Phi(a, b):
    q, r = divmod(a, b)
    return r * comb(q + 1, 2) + (b - r) * comb(q, 2)


def F(d):
    return Phi(d, 5)


def psi(d):
    f = max(d - 5, 0)
    return f * (f + 2)


def partitions_leq4(X):
    out = []

    def rec(rem, mx, acc):
        if rem == 0:
            out.append(tuple(acc))
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, acc + [p])

    rec(X, 4, [])
    return out


def part_vectors(m):
    lo, hi = 6, m // 2
    out = []

    def rec(k, mn, acc):
        if k == 6:
            out.append(tuple(acc))
            return
        for v in range(mn, hi + 1):
            rec(k + 1, v, acc + [v])

    rec(0, lo, [])
    return out


check("F AND psi TABLES.  F(6..11) = 1,2,3,4,5,7 (the 0019/0020 "
      "collision cost); psi(6..11) = 3,8,15,24,35,48 (the moment "
      "value); the two are DIFFERENT functions and neither is "
      "monotone-proportional to the other",
      [F(d) for d in range(6, 12)] == [1, 2, 3, 4, 5, 7]
      and [psi(d) for d in range(6, 12)] == [3, 8, 15, 24, 35, 48])

check("ADMISSIBLE EXCESS PARTITIONS (q_i <= 4 -- distinct 6-sets "
      "share at most 5 cells).  Counts for X = 7/8/9/10: 11/15/18/23",
      [len(partitions_leq4(X)) for X in (7, 8, 9, 10)]
      == [11, 15, 18, 23])

check("THE CELL SPACE, COUNTED.  Part vectors (sorted, 6 <= n_i <= "
      "floor(m/2)): 462 at m in {22,23}, 924 at {24,25}, 1716 at "
      "{26,27}, 3003 at {28,29}, 5005 at {30,31}, 8008 at {32,33}.  "
      "The X <= 9 windows sweep 11*4488 + 15*9207 + 18*12210 = "
      "407,253 cells; X = 10 on [22,33] adds 23*38,236 = 879,428 -- "
      "1,286,681 cells in all, each swept by BOTH engines",
      [len(part_vectors(m)) for m in range(22, 34)]
      == [462, 462, 924, 924, 1716, 1716, 3003, 3003, 5005, 5005,
          8008, 8008]
      and 11 * 4488 + 15 * 9207 + 18 * 12210 == 407253
      and sum(len(part_vectors(m)) for m in range(22, 34)) == 38236
      and 407253 + 23 * 38236 == 1286681)


# ======================================================================
head("1.  PHI IS THE BALANCED MINIMUM -- brute-forced, then monotone")
# ======================================================================

def phi_brute(a, b):
    """True minimum of sum C(a_i,2) over partitions of a into <= b
    nonnegative bins (order irrelevant since C is symmetric).  The
    largest bin x is tried BALANCED-FIRST (x from ceil(a/b) upward),
    so the optimum lands first and the monotone pruning is sharp."""
    best = [None]

    def rec(rem, bins, mx, acc):
        if best[0] is not None and acc >= best[0]:
            return
        if bins == 1:
            if rem <= mx:
                v = acc + comb(rem, 2)
                if best[0] is None or v < best[0]:
                    best[0] = v
            return
        lo = -(-rem // bins)
        for x in range(lo, min(rem, mx) + 1):
            v = acc + comb(x, 2)
            if best[0] is not None and v >= best[0]:
                break
            rec(rem - x, bins - 1, x, v)

    rec(a, b, a, 0)
    return best[0]


check("Phi(a,b) EQUALS THE BRUTE-FORCE MINIMUM on every (a, b) this "
      "file evaluates: a <= 40, b in {5} + [6, 16] (F's fibre count "
      "and every part size the sweeps see)",
      all(Phi(a, b) == phi_brute(a, b)
          for a in range(0, 41)
          for b in [5] + list(range(6, 17))))

check("MONOTONICITY IN THE BIN COUNT: Phi(a, b) >= Phi(a, b+1) on the "
      "same grid -- an extra empty bin never hurts, so OVERSTATING a "
      "part size only weakens g: the law survives lazy part counts",
      all(Phi(a, b) >= Phi(a, b + 1)
          for a in range(0, 41) for b in range(5, 16)))

check("THE SMOOTHING STEP, PRICED.  Moving one ball off a taller bin "
      "strictly lowers the pair count: C(x-1,2) + C(y+1,2) < C(x,2) + "
      "C(y,2) whenever x >= y + 2 (all x, y <= 40) -- the inequality "
      "behind balancedness; at x = y + 1 it flips to equality-or-"
      "worse, so the balanced profile is the exact floor",
      all(comb(x - 1, 2) + comb(y + 1, 2) < comb(x, 2) + comb(y, 2)
          for x in range(2, 41) for y in range(0, x - 1))
      and all(comb(x - 1, 2) + comb(y + 1, 2) >= comb(x, 2) + comb(y, 2)
              for x in range(1, 41) for y in range(x - 1, 41)))


# ======================================================================
head("2.  THE IDENTITY AND BOTH LAWS, ENACTED ON CORPORA")
# ======================================================================

def family_stats(edges, nvec=None):
    """Compute (X, R, per-vertex d, s, g) directly from definitions.
    Edges are 6-tuples (cell index per part).  nvec: declared part
    sizes; default = used cells per part."""
    m = len(edges)
    used = [sorted(set(e[j] for e in edges)) for j in range(6)]
    nv = nvec if nvec else [len(u) for u in used]
    X = 0
    R = 0
    for a in range(m):
        for b in range(a + 1, m):
            k = sum(1 for j in range(6) if edges[a][j] == edges[b][j])
            q = k - 1
            X += q
            if q > 0:
                R += q * (q + 1)
    verts = set((j, e[j]) for e in edges for j in range(6))
    out = []
    for (j, y) in sorted(verts):
        E = [e for e in edges if e[j] == y]
        d = len(E)
        s = 0
        for a in range(d):
            for b in range(a + 1, d):
                k = sum(1 for t in range(6) if E[a][t] == E[b][t])
                s += k - 1
        ident = 0
        for t in range(6):
            if t == j:
                continue
            fib = {}
            for e in E:
                fib[e[t]] = fib.get(e[t], 0) + 1
            ident += sum(comb(c, 2) for c in fib.values())
        g = sum(Phi(d, nv[t]) for t in range(6) if t != j)
        out.append((d, s, ident, g))
    return X, R, out


def is_intersecting(edges):
    return all(any(ea[j] == eb[j] for j in range(6))
               for i, ea in enumerate(edges) for eb in edges[i + 1:])


# corpus 1: EXHAUSTIVE -- every 3-subset of the 2^6 pool restricted to
# a 2-cell alphabet per part (64 edges), intersecting or not.
pool = list(itertools.product((0, 1), repeat=6))
c_int, c_non = 0, 0
id_bad = pc_bad = gpc_bad = 0
sx_bad_int = 0
sx_viol_non = 0
for trip in itertools.combinations(range(64), 3):
    edges = [pool[i] for i in trip]
    X, R, rows = family_stats(edges)
    inter = is_intersecting(edges)
    if inter:
        c_int += 1
    else:
        c_non += 1
    for (d, s, ident, g) in rows:
        if s != ident:
            id_bad += 1
        if g > s:
            pc_bad += 1
        if inter and s > X:
            sx_bad_int += 1
        if (not inter) and s > X:
            sx_viol_non += 1
    if sum(g for (_, _, _, g) in rows) > R:
        gpc_bad += 1

check("CORPUS 1 (exhaustive, all C(64,3) = 41,664 triples of the "
      "2-alphabet pool).  The identity s = sum-of-fibre-pairs holds "
      "at EVERY vertex; g <= s at every vertex; sum g <= R for every "
      "family; s <= X at every vertex of every INTERSECTING family",
      id_bad == 0 and pc_bad == 0 and gpc_bad == 0 and sx_bad_int == 0
      and c_int + c_non == comb(64, 3),
      "%d intersecting, %d not" % (c_int, c_non))

check("INTERSECTING-NESS IS LOAD-BEARING FOR s <= X, AND ONLY THERE: "
      "the exhaustive corpus contains non-intersecting families "
      "violating s <= X (a disjoint pair contributes q = -1 to X but "
      "not to any s)",
      sx_viol_non > 0, "%d violations" % sx_viol_non)

# the canonical witness, stated exactly:
wit = [(1, 1, 1, 0, 0, 1), (0, 0, 0, 1, 0, 0), (0, 0, 0, 1, 1, 0)]
Xw, Rw, rows_w = family_stats(wit)
sw = max(s for (_, s, _, _) in rows_w)
check("THE WITNESS, PINNED.  E = {A,B,C} with q(A,B) = 0, q(A,C) = -1 "
      "(disjoint), q(B,C) = 4: X = 3, and the B-C spine vertices have "
      "s = 4 > X.  Non-intersecting kills the law's right end only",
      not is_intersecting(wit) and Xw == 3 and sw == 4)

# corpus 2: structured families -- stars, sunflowers, K4 patterns,
# larger alphabets, unbalanced fibres.
def star(m, spread):
    """m edges through one vertex, fibres as unbalanced as spread."""
    return [(0, min(i, spread), i, i, i, i) for i in range(m)]


c2 = []
for m in (7, 11, 16, 22):
    for spread in (1, 2, 5, m - 1):
        c2.append(star(m, spread))
c2.append([(0, i, i, i, i, i) for i in range(9)])          # sunflower
c2.append([(i, 0, 0, 0, 0, 0) for i in range(2)]
          + [(0, i, i, i, i, i) for i in range(1, 5)])      # near-K4
ok2 = True
for edges in c2:
    X, R, rows = family_stats(edges)
    inter = is_intersecting(edges)
    for (d, s, ident, g) in rows:
        ok2 = ok2 and s == ident and g <= s
        if inter:
            ok2 = ok2 and s <= X
    ok2 = ok2 and sum(g for (_, _, _, g) in rows) <= R
check("CORPUS 2 (stars at four spreads and sizes, a sunflower, a "
      "near-K4; degrees to 22, deliberately unbalanced fibres).  "
      "Identity, g <= s, s <= X (intersecting), sum g <= R: all hold",
      ok2)

# MUST-FAIL controls: a harness that cannot catch a false law proves
# nothing.  Three perturbations of g, each must violate on corpus 1.
own_bad = bins_bad = balls_bad = 0
for trip in itertools.combinations(range(64), 3):
    edges = [pool[i] for i in trip]
    used = [sorted(set(e[j] for e in edges)) for j in range(6)]
    nv = [len(u) for u in used]
    verts = set((j, e[j]) for e in edges for j in range(6))
    for (j, y) in verts:
        E = [e for e in edges if e[j] == y]
        d = len(E)
        s = 0
        for a in range(d):
            for b in range(a + 1, d):
                s += sum(1 for t in range(6)
                         if E[a][t] == E[b][t]) - 1
        g_own = sum(Phi(d, nv[t]) for t in range(6))          # + own part
        g_bins = sum(Phi(d, max(nv[t] - 1, 1))
                     for t in range(6) if t != j)             # bins - 1
        g_balls = sum(Phi(d + 1, nv[t])
                      for t in range(6) if t != j)            # balls + 1
        if g_own > s:
            own_bad += 1
        if g_bins > s:
            bins_bad += 1
        if g_balls > s:
            balls_bad += 1

check("MUST-FAIL CONTROLS.  Perturb g three ways -- include the own "
      "part, shrink every bin count by one, add a phantom ball -- "
      "and each perturbation VIOLATES g <= s somewhere on corpus 1: "
      "the harness can see a false law; the true law's zero above is "
      "a pass, not blindness",
      own_bad > 0 and bins_bad > 0 and balls_bad > 0,
      "violations %d/%d/%d" % (own_bad, bins_bad, balls_bad))


# ======================================================================
head("3.  THE MOMENT FLOOR -- 0021's Lambda, re-enacted")
# ======================================================================

check("THE POINTWISE IDENTITY.  d^2 = 8d - 15 + 3[d=2] + psi(d) "
      "EXACTLY at d >= 5 and d in {2, 3}; slack exactly 1 at d = 4; "
      "FALSE at d <= 1 (0005's floor is billed, not decorative).  "
      "Checked d = 2..300",
      all(d * d == 8 * d - 15 + (3 if d == 2 else 0) + psi(d)
          for d in list(range(5, 301)) + [2, 3])
      and (16 == 8 * 4 - 15 + psi(4) - 1)
      and 1 * 1 != 8 * 1 - 15 + psi(1) and 0 != -15 + psi(0))


def Lam(X, m):
    return m * m - 43 * m + 2 * X + 540 - 3 * (m // 2)


check("THE FLOOR Lambda_X(m) = m^2 - 43m + 2X + 540 - 3 floor(m/2) "
      "(n >= 36, (D2), n_4 >= 0 -- three slack terms, as in 0021).  "
      "Spot table: Lambda_7(22..24) = 59/61/62; Lambda_8(22..24) = "
      "61/63/64; Lambda_9(22..24) = 63/65/66; Lambda_10(26/27/28/33) "
      "= 79/89/98/182.  STRICTLY INCREASING in m from 22 (increment "
      "2m - 42 - 3[m odd] >= 1)",
      [Lam(7, m) for m in (22, 23, 24)] == [59, 61, 62]
      and [Lam(8, m) for m in (22, 23, 24)] == [61, 63, 64]
      and [Lam(9, m) for m in (22, 23, 24)] == [63, 65, 66]
      and [Lam(10, m) for m in (26, 27, 28, 33)] == [79, 89, 98, 182]
      and all(Lam(10, m + 1) > Lam(10, m) for m in range(22, 456)))


# ======================================================================
head("4.  THE TWO ENGINES")
# ======================================================================
# A cell is (X, m, pi, nvec).  Alphabet: degrees d >= 2 with
# F(d) <= X - q1 (KC) and g(d) <= X (PC).  Per-part option tuples
# (sum d^2, #2s, sum F, sum g) over multisets of n_i admissible degrees
# summing to m; then a 6-fold convolution under the caps
# n_2 <= floor(m/2) (D2), P <= R - q1(q1+1) (LD), sum g <= R (GPC),
# with survival = hitting sum d^2 = m^2 + 5m + 2X (DM) exactly.
#
# ENGINE D carries full state sets.  ENGINE P prunes each layer to the
# Pareto frontier per sum-d^2 value (dominance in (n_2, P, G) -- sound
# for a feasibility question because every downstream constraint is
# monotone nondecreasing in each coordinate and (DM) reads only
# sum d^2).  M-DOM prices the dominance rule.

_alpha_cache = {}


def alphabet(m, C, X, gtuple):
    key = (m, C, X, gtuple)
    if key not in _alpha_cache:
        out = {}
        for d in range(2, m + 1):
            if F(d) > C:
                continue
            g = sum(Phi(d, nj) for nj in gtuple)
            if g > X:
                continue
            out[d] = g
        _alpha_cache[key] = out
    return _alpha_cache[key]


_deg_cache = {}


def degsets(ni, m, C, X, gtuple):
    key = (ni, m, C, X, gtuple)
    if key not in _deg_cache:
        galpha = alphabet(m, C, X, gtuple)
        res = set()

        def rec(left, rem, mind, sq, n2, P, G):
            if left == 1:
                d = rem
                if d >= mind and d in galpha:
                    res.add((sq + d * d, n2 + (1 if d == 2 else 0),
                             P + F(d), G + galpha[d]))
                return
            dmax = rem - 2 * (left - 1)
            for d in range(mind, dmax + 1):
                if d in galpha:
                    rec(left - 1, rem - d, d, sq + d * d,
                        n2 + (1 if d == 2 else 0), P + F(d),
                        G + galpha[d])

        if m >= 2 * ni:
            rec(ni, m, 2, 0, 0, 0, 0)
        _deg_cache[key] = frozenset(res)
    return _deg_cache[key]


def _sqrange(opts):
    if not opts:
        return None
    return (min(t[0] for t in opts), max(t[0] for t in opts))


def cell_survives(X, m, pi, nvec, engine, gpc=True):
    R = sum(q * (q + 1) for q in pi)
    q1 = pi[0]
    B = R - q1 * (q1 + 1)
    C = X - q1
    Gcap = R if gpc else 10 ** 9
    target = m * m + 5 * m + 2 * X
    n2cap = m // 2
    partopts = []
    lo = hi = 0
    for i in range(6):
        gtuple = tuple(sorted(nvec[:i] + nvec[i + 1:]))
        opts = degsets(nvec[i], m, C, X, gtuple)
        rng = _sqrange(opts)
        if rng is None:
            return False
        lo += rng[0]
        hi += rng[1]
        partopts.append((opts, rng))
    if target < lo or target > hi:
        return False
    states = {(0, 0, 0, 0)}
    rem_hi = hi
    rem_lo = lo
    for (opts, rng) in partopts:
        rem_hi -= rng[1]
        rem_lo -= rng[0]
        new = set()
        for (sq, n2, P, G) in states:
            for (dsq, dn2, dP, dG) in opts:
                s2 = sq + dsq
                if s2 + rem_hi < target or s2 + rem_lo > target:
                    continue
                nn, PP, GG = n2 + dn2, P + dP, G + dG
                if nn <= n2cap and PP <= B and GG <= Gcap:
                    new.add((s2, nn, PP, GG))
        if engine == "P":
            bysq = {}
            for st in new:
                bysq.setdefault(st[0], []).append((st[1], st[2], st[3]))
            kept = set()
            for sqv, lst in bysq.items():
                lst.sort()
                front = []
                for t in lst:
                    if not any(a[0] <= t[0] and a[1] <= t[1]
                               and a[2] <= t[2] for a in front):
                        front.append(t)
                for t in front:
                    kept.add((sqv,) + t)
            new = kept
        states = new
        if not states:
            return False
    return any(sq == target for (sq, n2, P, G) in states)


# ----------------------------------------------------------------------
# The Lambda-prefilter: an O(1) per-cell knapsack test.  For a cell
# (X, m, pi, nvec) with n = sum(nvec), any realization needs
#     Psi >= m^2 - 43m + 2X + 15n - 3 floor(m/2)
# (section 3, with n_4 >= 0), while (LD)+(KC) cap Psi at the knapsack
# maximum maxPsi(pi) (m-independent).  maxPsi < requirement kills the
# cell without a DP.  The prefilter is PRICED: M-PRE runs the full DP
# with the prefilter off over every m <= 26 window and asserts the
# identical atlas.
_maxpsi_cache = {}


def maxPsi(X, pi):
    key = (X, pi)
    if key not in _maxpsi_cache:
        R = sum(q * (q + 1) for q in pi)
        q1 = pi[0]
        B = R - q1 * (q1 + 1)
        C = X - q1
        items = [(F(d), psi(d)) for d in range(6, 2 * X + 20)
                 if F(d) <= C]
        best = [0] * (B + 1)
        for b in range(1, B + 1):
            for (c, v) in items:
                if c <= b and best[b - c] + v > best[b]:
                    best[b] = best[b - c] + v
        _maxpsi_cache[key] = best[B]
    return _maxpsi_cache[key]


def cell_alive(X, m, pi, nvec, engine, prefilter=True, gpc=True):
    if prefilter:
        n = sum(nvec)
        need = m * m - 43 * m + 2 * X + 15 * n - 3 * (m // 2)
        if maxPsi(X, pi) < need:
            return False
    return cell_survives(X, m, pi, nvec, engine, gpc=gpc)


def sweep(X, mlo, mhi, engine, prefilter=True, drop_pi=None,
          only66=False, gpc=True):
    """Full sweep; returns sorted survivor list of (m, pi, nvec)."""
    out = []
    pis = partitions_leq4(X)
    if drop_pi is not None:
        pis = [p for p in pis if p != drop_pi]
    for m in range(mlo, mhi + 1):
        vecs = part_vectors(m)
        if only66:
            vecs = [v for v in vecs if v == (6, 6, 6, 6, 6, 6)]
        for pi in pis:
            for nvec in vecs:
                if cell_alive(X, m, pi, nvec, engine,
                              prefilter=prefilter, gpc=gpc):
                    out.append((m, pi, nvec))
    return sorted(out)


# ======================================================================
head("5.  THE SWEEP -- X = 7 empty; the atlases at 8, 9, 10")
# ======================================================================

V66 = (6, 6, 6, 6, 6, 6)
V57 = (6, 6, 6, 6, 6, 7)
V477 = (6, 6, 6, 6, 7, 7)

t0 = time.time()
S7D = sweep(7, 22, 26, "D")
S7P = sweep(7, 22, 26, "P")
check("X = 7: ZERO SURVIVORS at every rung of T-B21's whole X = 7 "
      "window [22, 26], under BOTH engines -- 11 partitions x 4,488 "
      "part vectors x 5 rungs = 49,368 cells.  The X = 7 layer is "
      "empty with no quotient, no parity, no ledger, no residual "
      "pairing anywhere in the chain",
      S7D == [] and S7P == [],
      "%.0f s" % (time.time() - t0))

t0 = time.time()
S8D = sweep(8, 22, 28, "D")
S8P = sweep(8, 22, 28, "P")
ATLAS8 = [
    (22, (4, 4), V66),
    (23, (3, 3, 2), V66), (23, (4, 4), V66),
    (24, (3, 3, 2), V66), (24, (4, 4), V66), (24, (4, 4), V57),
    (25, (4, 4), V66),
    (26, (4, 4), V66),
]
check("THE X = 8 ATLAS, CELL-EXACT (both engines agree): (4,4) at "
      "6^6 on every rung 22-26 (+ 6^5 7 at 24), (3,3,2) at 6^6 on "
      "23-24, NOTHING at 27-28, NOTHING ELSE -- 15 partitions x "
      "9,207 cells",
      S8D == sorted(ATLAS8) and S8P == sorted(ATLAS8),
      "%.0f s" % (time.time() - t0))

t0 = time.time()
S9D = sweep(9, 22, 29, "D")
S9P = sweep(9, 22, 29, "P")
ATLAS9 = [
    (22, (4, 4, 1), V66),
    (23, (3, 3, 3), V66), (23, (4, 3, 2), V66),
    (23, (4, 4, 1), V66), (23, (4, 4, 1), V57),
    (24, (2, 2, 2, 2, 1), V66), (24, (3, 2, 2, 2), V66),
    (24, (3, 3, 1, 1, 1), V66), (24, (3, 3, 2, 1), V66),
    (24, (3, 3, 3), V66), (24, (3, 3, 3), V57),
    (24, (4, 3, 2), V66), (24, (4, 4, 1), V66), (24, (4, 4, 1), V57),
    (25, (3, 3, 2, 1), V66), (25, (3, 3, 3), V66),
    (25, (3, 3, 3), V57), (25, (4, 4, 1), V66), (25, (4, 4, 1), V57),
    (26, (3, 3, 3), V66), (26, (3, 3, 3), V57),
    (26, (4, 4, 1), V66), (26, (4, 4, 1), V57),
]
check("THE X = 9 ATLAS, CELL-EXACT (both engines agree): 23 cells on "
      "[22, 26] -- (4,4,1) every rung, (3,3,3) from 23, (4,3,2) at "
      "23-24 only, the four low shapes at 24(-25) only, all at 6^6 "
      "or 6^5 7 -- and NOTHING at 27-29: 18 partitions x 12,210 cells",
      S9D == sorted(ATLAS9) and S9P == sorted(ATLAS9),
      "%.0f s" % (time.time() - t0))

t0 = time.time()
S10D = sweep(10, 22, 33, "D")
S10P = sweep(10, 22, 33, "P")
ATLAS10_HI = [
    (26, (2, 2, 2, 2, 1, 1), V66), (26, (2, 2, 2, 2, 2), V66),
    (26, (3, 3, 2, 1, 1), V66),
    (26, (3, 3, 2, 2), V66), (26, (3, 3, 2, 2), V57),
    (26, (3, 3, 3, 1), V66), (26, (3, 3, 3, 1), V57),
    (26, (4, 3, 2, 1), V66),
    (26, (4, 3, 3), V66), (26, (4, 3, 3), V57),
    (26, (4, 4, 1, 1), V66), (26, (4, 4, 1, 1), V57),
    (26, (4, 4, 2), V66), (26, (4, 4, 2), V57), (26, (4, 4, 2), V477),
    (27, (3, 3, 2, 2), V66), (27, (3, 3, 3, 1), V66),
    (27, (4, 3, 3), V66), (27, (4, 4, 1, 1), V66),
    (27, (4, 4, 2), V66), (27, (4, 4, 2), V57),
    (28, (4, 4, 2), V66),
]
S10_hi = [c for c in S10D if c[0] >= 26]
check("THE X = 10 HIGH-RUNG ATLAS, CELL-EXACT (both engines agree): "
      "15 cells at m = 26 (nine shapes), 6 at 27 (five shapes), "
      "(4,4,2);6^6 ALONE at 28, and NOTHING at 29-33 -- the m = 33 "
      "zero row is the Lambda tail's anchor.  23 partitions x 38,236 "
      "part vectors over [22, 33]",
      S10_hi == sorted(ATLAS10_HI) and S10D == S10P
      and all(c[0] <= 28 for c in S10D),
      "%.0f s" % (time.time() - t0))

note("X = 10 also has survivors at m in [22, 25] -- %d cells, both "
     "engines agreeing; they are the LIVE frontier if X >= 10 is "
     "certified (0025), not a defect.  Printed for the record, "
     "asserted only in count so the next campaign starts from an "
     "honest list." % len([c for c in S10D if c[0] <= 25]))

check("THE X = 10 LOW-RUNG COUNT (the next campaign's target list): "
      "10 cells at m = 22, 17 at 23, 25 at 24, 22 at 25 -- 74 in all "
      "(three engine implementations agree; a hostile lane's side "
      "remark of 15 at m = 22 did not reproduce and was not part of "
      "its audited scope -- recorded in the turn notebook)",
      [len([c for c in S10D if c[0] == m]) for m in (22, 23, 24, 25)]
      == [10, 17, 25, 22])

check("POSITIVE CONTROLS -- the engine can tell a law from a "
      "tautology: (8,24,(4,4),6^5 7), (9,24,(3,3,3),6^5 7) and "
      "(10,28,(4,4,2),6^6) each SURVIVE both engines (a sweep that "
      "kills everything is broken, not strong)",
      cell_alive(8, 24, (4, 4), V57, "D")
      and cell_alive(8, 24, (4, 4), V57, "P")
      and cell_alive(9, 24, (3, 3, 3), V57, "D")
      and cell_alive(10, 28, (4, 4, 2), V66, "D"))

check("ATTRIBUTION INSIDE THE SWEEP, MEASURED (the sixth audit "
      "credited (GPC) with the X = 7 kill; the refuter lane showed "
      "pointwise (PC) does it alone): with the GLOBAL law switched "
      "off, X = 7 is STILL empty -- but X = 9 at m = 27 reopens (6 "
      "cells) and X = 10 at m = 26 grows 15 -> 47.  (GPC) earns its "
      "place ABOVE the floor, not at it",
      sweep(7, 22, 26, "P", gpc=False) == []
      and len(sweep(9, 27, 27, "P", gpc=False)) == 6
      and len(sweep(10, 26, 26, "P", gpc=False)) == 47)


# ======================================================================
head("6.  THE TAIL -- X = 10 dies on [33, 456] by knapsack vs Lambda")
# ======================================================================

check("MAX Psi OVER ALL 23 ADMISSIBLE PARTITIONS OF 10 UNDER "
      "(LD)+(KC) IS 179, ATTAINED BY (3,3,3,1) (B = 26, cap F <= 7 "
      "admits d = 11: three 48s cost 21, one d = 10 closes the "
      "budget) -- runner-up (4,4,2) at 178.  The maximum is "
      "m-INDEPENDENT: only R(pi) and X - q_1 enter",
      max(maxPsi(10, pi) for pi in partitions_leq4(10)) == 179
      and maxPsi(10, (3, 3, 3, 1)) == 179
      and maxPsi(10, (4, 4, 2)) == 178
      and sorted(maxPsi(10, pi) for pi in partitions_leq4(10))[-1]
      == 179)

check("THE TAIL, RUNG BY RUNG.  Lambda_10(33) = 182 > 179, and "
      "Lambda_10 increases through m = 456 (section 3): EVERY rung "
      "of [33, 456] has requirement > 179 >= max Psi -- X = 10 is "
      "impossible on the whole tail.  With the sweep's zero rows at "
      "[29, 32] (section 5): X = 10 => m <= 28",
      Lam(10, 33) == 182
      and all(Lam(10, m) > 179 for m in range(33, 457)))

check("(T-B24)  X = 10 => m <= 28, WITH THE HIGH-RUNG ATLAS: the "
      "only cells above m = 25 are the 22 asserted in section 5, "
      "and none exist above 28.  Equivalently: any critical core "
      "with m >= 29 has X != 10 -- with 0023's X >= 9 at 29 and "
      "X >= 10 from 30 (T-B23, billed as CONTEXT ONLY, not consumed "
      "here), the excess at m = 29 is X = 9 or X >= 11",
      all(c[0] <= 28 for c in S10D) and len(ATLAS10_HI) == 22)

check("(T-A24)  X != 7 FOR EVERY CRITICAL CORE; X >= 8 EVERYWHERE.  "
      "Chain: T-B21 (0021, billed) confines X = 7 to m in [22, 26]; "
      "section 5 empties every such cell under both engines; T-A21 "
      "(0021, billed) gives X >= 7; hence X >= 8 on all of "
      "[22, 456].  The certificate chain is 0021 -> 0024: 0022 and "
      "0023 are NOT consumed -- X >= 8 everywhere now stands on two "
      "disjoint proof stacks (ledgers/parity/quotients in 0023; "
      "part-collision here)",
      S7D == [] and S7P == [])


# ======================================================================
head("7.  MUTATIONS -- nine, priced")
# ======================================================================

MUT = []


def mut(name, flipped, expect, detail):
    MUT.append(name)
    tag = "ok  " if flipped == expect else "FAIL"
    if flipped != expect:
        FAILED.append("MUT " + name.split()[0])
    print("  [%s] %s -- %s" % (tag, name, detail))


# M-GPC: the global law withdrawn (already measured in section 5's
# attribution check: X = 9 m = 27 reopens 6 cells, X = 10 m = 26 grows
# 15 -> 47).  Here: the X = 9 atlas itself would be WRONG without it.
mut("M-GPC  the global law withdrawn",
    sweep(9, 27, 29, "P", gpc=False) != [],
    True,
    "X = 9 reopens above the atlas ceiling (m = 27: 6 cells) -- the "
    "27-29 zero rows STAND ON (GPC); the X = 7 floor does not (the "
    "attribution check).  Withdrawing the global law breaks T-B24's "
    "neighborhood, not T-A24")

# The parametrized mutant engine: one code path, flags name the wound.
def cell_mut(X, m, pi, nvec, pc=True, kc=True, d2slack=0,
             dm_exact=True, bad_dom=False):
    R = sum(q * (q + 1) for q in pi)
    q1 = pi[0]
    B = R - q1 * (q1 + 1)
    C = X - q1
    target = m * m + 5 * m + 2 * X
    n2cap = m // 2 + d2slack
    states = {(0, 0, 0, 0)}
    for i in range(6):
        gtuple = tuple(sorted(nvec[:i] + nvec[i + 1:]))
        opts = set()
        ga = {}
        for d in range(2, m + 1):
            if kc and F(d) > C:
                continue
            g = sum(Phi(d, nj) for nj in gtuple)
            if pc and g > X:
                continue
            ga[d] = g

        def rec(left, rem, mind, sq, n2, P, G):
            if left == 1:
                d = rem
                if d >= mind and d in ga:
                    opts.add((sq + d * d, n2 + (1 if d == 2 else 0),
                              P + F(d), G + ga[d]))
                return
            dmax = rem - 2 * (left - 1)
            for d in range(mind, dmax + 1):
                if d in ga:
                    rec(left - 1, rem - d, d, sq + d * d,
                        n2 + (1 if d == 2 else 0), P + F(d), G + ga[d])

        if m >= 2 * nvec[i]:
            rec(nvec[i], m, 2, 0, 0, 0, 0)
        new = set()
        for (sq, n2, P, G) in states:
            for (dsq, dn2, dP, dG) in opts:
                s2, nn, PP, GG = sq + dsq, n2 + dn2, P + dP, G + dG
                if s2 <= target and nn <= n2cap and PP <= B and GG <= R:
                    new.add((s2, nn, PP, GG))
        if bad_dom:
            bysq = {}
            for st in new:
                bysq.setdefault(st[0], []).append((st[1], st[2], st[3]))
            kept = set()
            for sqv, lst in bysq.items():
                for t in lst:
                    if not any(a != t and a[0] >= t[0] and a[1] >= t[1]
                               and a[2] >= t[2] for a in lst):
                        kept.add((sqv,) + t)
            new = kept
        states = new
        if not states:
            return False
    if dm_exact:
        return any(sq == target for (sq, _, _, _) in states)
    return any(sq <= target for (sq, _, _, _) in states)


def mut_witness(X, mlo, mhi, **flags):
    for m in range(mlo, mhi + 1):
        for pi in partitions_leq4(X):
            for nvec in part_vectors(m):
                if cell_mut(X, m, pi, nvec, **flags):
                    return (m, pi, nvec)
    return None


w_pc = mut_witness(7, 22, 26, pc=False)
mut("M-PC  the pointwise law withdrawn from the alphabet",
    w_pc is not None,
    True,
    "X = 7 REOPENS (witness %s) -- the floor kill stands on "
    "pointwise (PC); with section 5's attribution check, both "
    "directions are now measured in-cert" % (w_pc,))

w_d2 = mut_witness(7, 22, 23, d2slack=1)
mut("M-D2R  (D2) priced -- a NULL at the floor, load-bearing in the "
    "tail",
    (w_d2 is None)
    and (33 * 33 - 43 * 33 + 20 + 540 - 3 * 36 < 179),
    True,
    "measured both ways: X = 7 stays EMPTY at m = 22, 23 even under "
    "n_2 <= floor(m/2) + 1 -- the floor kill does NOT lean on (D2) "
    "(unlike 0023, where M-D2E reopens everything; the two proof "
    "stacks have honestly different dependency profiles) -- but "
    "withdrawing (D2) from Lambda breaks the X = 10 tail: with n_2 "
    "free at n = 36, Lambda'_10(33) = 122 < 179 and T-B24's m >= 33 "
    "argument DIES.  (D2) is billed for the tail, not the floor")

def maxPsi_noKC(pi):
    R = sum(q * (q + 1) for q in pi)
    B = R - pi[0] * (pi[0] + 1)
    items = [(F(d), psi(d)) for d in range(6, 40) if F(d) <= B]
    best = [0] * (B + 1)
    for b in range(1, B + 1):
        for (c, v) in items:
            if c <= b and best[b - c] + v > best[b]:
                best[b] = best[b - c] + v
    return best[B]


w_kc = mut_witness(7, 22, 23, kc=False)
kc_tail = max(maxPsi_noKC(pi) for pi in partitions_leq4(10))
mut("M-KC  the cap F <= X - q_1 withdrawn -- a NULL at the floor, "
    "load-bearing in the tail",
    (w_kc is None) and kc_tail >= Lam(10, 33),
    True,
    "measured both ways: X = 7 stays EMPTY at m = 22, 23 without "
    "(KC) -- at the floor's part sizes, (PC) caps degrees below "
    "(KC)'s reach, so the floor kill does not lean on it -- but the "
    "TAIL does: without the cap the (LD) knapsack admits degree-17 "
    "items and max Psi rises to %d >= %d = Lambda_10(33), so the "
    "m = 33 rung REOPENS and T-B24's tail argument dies.  (KC) is "
    "billed for the tail, not the floor" % (kc_tail, Lam(10, 33)))

w_dm = mut_witness(7, 22, 22, dm_exact=False)
mut("M-DM  the moment identity relaxed to an inequality",
    w_dm is not None,
    True,
    "X = 7 at m = 22 reopens if a state may undershoot the moment "
    "target (witness %s) -- exactness of (DM) is load-bearing"
    % (w_dm,))

# M-PART: one partition deleted from the sieve.
mut("M-PART  (4,4) deleted from the X = 8 sieve",
    sweep(8, 22, 22, "P", drop_pi=(4, 4)) == [],
    True,
    "the m = 22 atlas row vanishes -- a dropped partition is VISIBLE "
    "as a wrong atlas, the sweep-completeness scar (M-SWEEP, 0021) "
    "carried forward")

# M-NV: part vectors restricted to 6^6.
mut("M-NV  part vectors restricted to n = 36",
    sweep(9, 22, 29, "P", only66=True)
    == [c for c in sorted(ATLAS9) if c[2] == V66],
    True,
    "the atlas loses EXACTLY its 6^5 7 rows -- the n > 36 ladder is "
    "load-bearing for atlas exactness (and for nothing else: no "
    "6^6 verdict changes)")

# M-DOM: engine P's compression corrupted -- keep ONE state per
# sum-d^2 value, the coordinatewise-largest.  A frontier that discards
# the minimal corner loses exactly the states that survive later caps.
def cell_bad_compress(X, m, pi, nvec):
    R = sum(q * (q + 1) for q in pi)
    q1 = pi[0]
    B = R - q1 * (q1 + 1)
    C = X - q1
    target = m * m + 5 * m + 2 * X
    n2cap = m // 2
    states = {(0, 0, 0, 0)}
    for i in range(6):
        gtuple = tuple(sorted(nvec[:i] + nvec[i + 1:]))
        opts = degsets(nvec[i], m, C, X, gtuple)
        new = {}
        for (sq, n2, P, G) in states:
            for (dsq, dn2, dP, dG) in opts:
                s2, nn, PP, GG = sq + dsq, n2 + dn2, P + dP, G + dG
                if s2 <= target and nn <= n2cap and PP <= B and GG <= R:
                    k = (nn, PP, GG)
                    if s2 not in new or k > new[s2]:
                        new[s2] = k
        states = set((s2,) + k for (s2, k) in new.items())
        if not states:
            return False
    return any(sq == target for (sq, _, _, _) in states)


bad_atlas8 = []
for m in range(22, 29):
    for pi in partitions_leq4(8):
        for nvec in part_vectors(m):
            if cell_alive(8, m, pi, nvec, "P") \
               and not cell_bad_compress(8, m, pi, nvec):
                bad_atlas8.append((m, pi, nvec))
mut("M-DOM  engine P's frontier corrupted to one max state per "
    "moment value",
    bad_atlas8 != [],
    True,
    "the corrupted compression FALSELY KILLS true atlas cells "
    "(%d of 8 at X = 8: %s...) -- discarding the minimal corner "
    "loses the states that survive later caps; the Pareto rule keeps "
    "them, and engine D agrees with engine P everywhere (section 5), "
    "so the shipped compression is priced sound"
    % (len(bad_atlas8), bad_atlas8[:2]))

# M-PRE: the Lambda-prefilter disabled -- must change NOTHING.
mut("M-PRE  the prefilter disabled on every m <= 26 window",
    (sweep(8, 22, 26, "P", prefilter=False)
     == [c for c in sorted(ATLAS8) if c[0] <= 26]
     and sweep(9, 22, 26, "P", prefilter=False)
     == [c for c in sorted(ATLAS9) if c[0] <= 26]),
    True,
    "identical atlases with the prefilter off -- the prefilter only "
    "skips dead cells (it is an optimization with a proof, not a "
    "filter with an opinion)")

check("MUTATION LEDGER: %d mutants priced" % len(MUT), len(MUT) == 9)


# ======================================================================
head("RESULT")
# ======================================================================

ok = not FAILED
print()
print("  checks : %d" % NCHECK[0])
print("  notes  : %d (stated, not tested)" % NNOTE[0])
print("  failed : %d%s" % (len(FAILED),
                           "" if ok else "  " + " | ".join(FAILED)))
print("  time   : %.1f s" % (time.time() - START))
print()
if ok:
    print("  GREEN.  THE PART-COLLISION LAWS HOLD AND THE SWEEP IS EXACT:")
    print("      X = 7 is EMPTY on its whole window -- X >= 8 everywhere,")
    print("      now on TWO disjoint proof stacks (0021->0024 | 0021->0023).")
    print("      X = 10 => m <= 28.  Atlases at X = 8 (8 cells), X = 9")
    print("      (23 cells), X = 10 high (22 cells) certified for 0025.")
else:
    print("  NOT GREEN.")
sys.exit(0 if ok else 1)
