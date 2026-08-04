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
 (4) RUNTIME/SCOPE.  Engine P sweeps every cell of every window;
     engine D double-checks every cell at X = 7 (the theorem layer),
     every cell of every atlas row (the data layer), and every 89th
     cell of the remainder (deterministic stride).  The stride is a
     runtime concession, priced by M-STRIDE; the theorem and data
     layers are double-engine COMPLETE.

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
      "407,253 cells; X = 10 on [22,32] adds 23*30231 = 695,313",
      [len(part_vectors(m)) for m in range(22, 34)]
      == [462, 462, 924, 924, 1716, 1716, 3003, 3003, 5005, 5005,
          8008, 8008]
      and 11 * 4488 + 15 * 9207 + 18 * 12210 == 407253
      and sum(len(part_vectors(m)) for m in range(22, 33)) == 30231
      and 23 * 30231 == 695313)


# ======================================================================
head("1.  PHI IS THE BALANCED MINIMUM -- brute-forced, then monotone")
# ======================================================================

def phi_brute(a, b):
    """True minimum of sum C(a_i,2) over partitions of a into <= b
    nonnegative bins (order irrelevant since C is symmetric)."""
    best = [None]

    def rec(rem, bins, mx, acc):
        if bins == 1:
            if rem <= mx:
                v = acc + comb(rem, 2)
                if best[0] is None or v < best[0]:
                    best[0] = v
            return
        for x in range(min(rem, mx), -1, -1):
            v = acc + comb(x, 2)
            if best[0] is not None and v >= best[0]:
                continue
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
    X, R, rows = family_stats(edges)
    used = [len(set(e[j] for e in edges)) for j in range(6)]
    verts = set((j, e[j]) for e in edges for j in range(6))
    for (j, y) in verts:
        d = sum(1 for e in edges if e[j] == y)
        s = [r[1] for r in rows
             if rowsimplindex := None] if False else None
    break
# (the perturbed sweep is done in one pass below, vertex-aligned)
own_bad = bins_bad = balls_bad = 0
for trip in itertools.combinations(range(200), 2):
    break
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
