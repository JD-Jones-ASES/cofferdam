#!/usr/bin/env python3
"""Certificate 0015 -- (CC), the critical-cover inequality, and the excess
floor X >= 2 at the bottom of the window.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from
lib/.  Runs under Python 3.9 and under python3 -O.  Deterministic.

WHAT IS CLAIMED
---------------
  (CC) for every edge e of a critical core K (any m):
      2 * sum_i Phi(d_i - 1, 5 - b_i)  <=  3 (X - x_e)      PROVEN-BY-CERTIFICATE
  where d_i = degree of e's part-i vertex, b_i = |T_e cap V_i|
  for e's private 5-cover T_e (certificate 0013), Phi(n, k) =
  the balanced-split minimum of sum C(n_j, 2) over k classes
  totalling n, X = sum_v C(deg v, 2) - C(m, 2) the excess,
  x_e = sum_i d_i - (m + 5) the edge excess.  Globally
  (sum_e x_e = 2X is an identity):
      2 * sum_e sum_i Phi(d_i - 1, 5 - b_i) <= 3 (m-2) X     PROVEN-BY-CERTIFICATE

  X >= 2 FOR EVERY CRITICAL CORE AT m = 22                   PROVEN-BY-CERTIFICATE
  (the bottom rung of the window [22, 456] enters the         (in-house: 0005,
  nonlinear regime: the first structural statement about      0008, 0009, 0012
  a minimum core beyond existence)                            field + 0013 covers;
                                                              external NONE)

THE PROOF OF (CC)
-----------------
Fix a critical core K (edge-critical counterexample, tau = 6; finite,
6-partite, 6-uniform, intersecting) and an edge e with private minimum
5-cover T_e: e cap T_e = empty, T_e covers K - e, T_e inside V(K) --
all from certificate 0013, steps (1)-(3).  Write v_i for e's part-i
vertex, d_i = deg(v_i), b_i = |T_e cap V_i|, sum_i b_i = 5.

  (1) CLASSES.  Every edge f != e with v_i in f meets T_e (T_e covers
      K - e), and NOT in part i: a vertex of f in V_i is f's unique
      part-i vertex v_i, and v_i is not in T_e.  So each of the
      d_i - 1 edges through v_i other than e hits T_e \\ V_i, a set of
      5 - b_i cover vertices.  (If d_i >= 2 this forces b_i <= 4 --
      the concentration lemma (*) of certificate 0014, re-proven
      pointwise; with lemma (A), d_i >= 2 always.)
  (2) PIGEONHOLE.  For u in T_e \\ V_i let n_iu = #{f != e : v_i in f,
      u in f}.  Then sum_u n_iu >= d_i - 1, and by convexity
      sum_u C(n_iu, 2) >= Phi(d_i - 1, 5 - b_i)  (the balanced split
      minimizes; section 1 checks this exhaustively).  Well-defined:
      b_i = 5 would leave d_i - 1 edges with no cell, so covering
      alone forces d_i = 1 there and the Phi term is 0 -- (CC) itself
      needs no lemma (A); the class count is only ever 0 when n is.
  (3) ACCOUNTING.  I_e := sum_i sum_{u in T_e \\ V_i} C(n_iu, 2)
      counts, for each unordered pair {f, f'} of edges != e, exactly
      a * b incidences, where a = |f cap f' cap e| and
      b = |f cap f' cap T_e|:  the pair is counted once per shared
      (v_i, u) combination, u never lies in V_i automatically.
      (Section 3 verifies the identity exactly, on synthetic systems
      and on a real core.)
  (4) THE CORNER.  a + b <= s := |f cap f'| <= 5 (distinct 6-uniform
      edges share at most 5 vertices; e-vertices and cover vertices
      are disjoint, so no shared vertex is counted in both a and b).
      For integers a, b >= 0 with a + b <= s <= 5  (the binding
      hypothesis is a + b <= s, established by the first clause):
          a * b <= (3/2)(s - 1),
      with equality exactly at (a, b) = (2, 3), s = 5.  (Exhaustive in
      section 2; at s = 6 the inequality would FAIL at (3,3) -- the
      6-uniform distinctness cap is load-bearing.)
  (5) SUM.  Every pair of edges of an intersecting family has s >= 1,
      so summing (4) over all pairs {f, f'} inside K - e:
          I_e <= (3/2) * sum_pairs (s - 1) = (3/2)(X - x_e),
      because X = sum over ALL pairs of (lambda - 1) and x_e is
      exactly the part contributed by pairs involving e
      (x_e = sum_{f != e} (|e cap f| - 1) >= 0 by (L4)).  With (2):
          sum_i Phi(d_i - 1, 5 - b_i) <= I_e <= (3/2)(X - x_e).  QED.
  (6) GLOBAL.  sum_e x_e = sum over ordered pairs of (lambda - 1)
      = 2X (an identity, checked on a real core), so summing (CC)
      over the m edges gives 2 sum_e sum_i Phi <= 3(mX - 2X).

  The derivation is uniform in tau: for a tau = t edge-critical
  6-partite intersecting object, the same argument gives
  2 sum_i Phi(d_i - 1, (t-1) - b_i) <= 3(X - x_e) -- section 4 enacts
  the t = 5 instance on a real core, where it holds with margin
  exactly ZERO on every edge (X = 0 there: inside a projective plane
  every two lines meet exactly once).

THE m = 22 KILL (X <= 1 impossible for cores)
---------------------------------------------
Corollaries of (CC), per edge, using Phi(n, 5 - b) >= Phi(n, 5):
  - a vertex of degree d forces, via any edge through it,
    2 Phi(d-1, 5) <= 3(X - x_e) <= 3X.  So X = 0 forces Delta <= 6,
    and X <= 1 forces Delta <= 7  (d = 8 gives LHS 4 > 3).
  - at X <= 1 no edge holds TWO degree->=7 vertices (LHS >= 4 > 3),
    and same-part vertices never share an edge, so the stars of
    degree->=7 vertices are pairwise edge-disjoint:
    7 * (#degree->=7 vertices) <= m = 22, i.e. at most 3 of them.
  - the (D2) cap 2*D2 <= m (certificate 0008) and the global form.
Over the pinned-ladder configuration field at m = 22 (the profile
machinery of certificates 0005/0009/0012, which quantifies over ALL
counterexamples, cores a fortiori): 506,204 configurations have
0 <= X <= 1 (X >= 0 is (L2); the field totals are {231, 232}), and
the four rules kill every one -- 504,478 on the per-edge degree cap,
1,150 on star-disjointness, 576 on (D2), none surviving.  Hence
X >= 2 for every critical core at m = 22.  THE MARGIN, stated per
D-017: under the X = 1 rules (Delta <= 7, at most three 7s, D2 <= 11)
the maximum achievable degree-pair total is EXACTLY 231, one short of
the 232 that X = 1 requires -- the kill closes by exactly one unit;
at X = 0 the maximum is 225, margin six (section 6 computes both).

HONESTY NOTE ON PROVENANCE.  The outside review (via JD, turn 9)
claimed (CC) with exactly this Phi/corner shape, and claimed "X in
{0,1} excluded via (CC) + the D2 cap".  (CC) re-derived here from
scratch checks out.  The exclusion AS SKETCHED does not close: the
global form plus (D2) leaves 52 surviving configurations (measured
first, section 5's sensitivity).  Closing needed the per-edge
corollaries and the star-disjointness count above, which the sketch
did not contain.  Claim audited, mechanism repaired, result stronger
than the sketch.

THE LEDGER, in full
-------------------
  (CC), per-edge and global      EXTERNAL INPUTS -- NONE.  In-house:
                                 certificate 0013 (criticality, private
                                 covers, (3a)/(3b), T_e in V(K)).
  X >= 2 at m = 22               additionally: the configuration field
                                 (0005 (A)(B) + pinned ladder caps
                                 0009/0012) and the (D2) cap (0008).
                                 EXTERNAL INPUTS -- NONE.
  the tau = 5 enactment          CONTROL-ONLY: rebuilds 0013's
                                 rehearsal core deterministically; an
                                 error there reddens this certificate,
                                 never greens it.
"""

import itertools
import sys
import time
from math import comb

START = time.time()
FAILED = []
NCHECK = [0]
NNOTE = [0]


def check(label, cond, detail=""):
    NCHECK[0] += 1
    ok = bool(cond)
    if not ok:
        FAILED.append(label)
    print("  [%s] %2d. %s%s" % ("ok  " if ok else "FAIL", NCHECK[0], label,
                                ("   " + detail) if detail else ""),
          flush=True)


def note(label, detail=""):
    NNOTE[0] += 1
    print("  [note] %s%s" % (label, ("   " + detail) if detail else ""),
          flush=True)


def head(s):
    print("\n=== %s ===" % s, flush=True)


def phi(n, k):
    """Balanced-split minimum of sum C(n_j, 2) over k classes totalling n."""
    if n <= 0:
        return 0
    q, r = divmod(n, k)
    return r * comb(q + 1, 2) + (k - r) * comb(q, 2)


# ==========================================================================
# 1.  Phi is the true minimum, exhaustively
# ==========================================================================

head("1.  Phi: balanced splits minimize sum C(., 2)")

ok_min = True
for n in range(0, 11):
    for k in range(1, 7):
        best = None
        for compo in itertools.product(range(n + 1), repeat=k):
            if sum(compo) == n:
                v = sum(comb(c, 2) for c in compo)
                if best is None or v < best:
                    best = v
        if best != phi(n, k):
            ok_min = False
check("Phi(n, k) equals the exhaustive minimum over ALL compositions of n "
      "into k classes, for every n <= 10, k <= 6",
      ok_min)
check("Phi is nonincreasing in the class count k (fewer classes, more "
      "forced pairs): Phi(n, k) >= Phi(n, k') for k <= k', all n <= 10, "
      "k' <= 6 -- so Phi(., 5) is a SAFE lower bound whatever b_i is",
      all(phi(n, k) >= phi(n, kk)
          for n in range(11) for k in range(1, 7) for kk in range(k, 7)))
check("the values the kill leans on: Phi(5,5) = 0, Phi(6,5) = 1, "
      "Phi(7,5) = 2 -- degree 6 is free, degree 7 costs 1, degree 8 "
      "costs 2",
      (phi(5, 5), phi(6, 5), phi(7, 5)) == (0, 1, 2))

# ==========================================================================
# 2.  The corner: a*b <= (3/2)(s-1) for a+b <= s <= 5
# ==========================================================================

head("2.  the corner inequality")

corner_ok = True
tight = []
for s in range(1, 6):
    for a in range(0, s + 1):
        for b in range(0, s + 1 - a):
            if 2 * a * b > 3 * (s - 1):
                corner_ok = False
            if 2 * a * b == 3 * (s - 1) and a * b > 0:
                tight.append((a, b, s))
check("a*b <= (3/2)(s-1) for ALL integers a, b >= 0 with a + b <= s <= 5 "
      "(exhaustive)", corner_ok)
check("tight EXACTLY at (a,b,s) = (2,3,5) and (3,2,5) -- the corner the "
      "turn-9 note recorded", sorted(tight) == [(2, 3, 5), (3, 2, 5)])
check("TEETH: at s = 6 the corner FAILS -- (3,3) gives 9 > 7.5 -- so the "
      "6-uniform distinctness cap s <= 5 is load-bearing (static "
      "arithmetic: this check documents the boundary, it cannot fail "
      "on its own)",
      2 * 3 * 3 > 3 * (6 - 1))

# ==========================================================================
# 3.  The accounting identity on synthetic systems
# ==========================================================================

head("3.  I_e = sum over pairs of a*b, exactly")


class LCG(object):
    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFF

    def next(self):
        self.s = (25214903917 * self.s + 11) & 0xFFFFFFFFFFFF
        return self.s >> 16


RNG = LCG(20260727)
id_ok = True
pig_ok = True
for trial in range(200):
    # a synthetic 'edge neighbourhood': 6 e-vertices, 5 cover vertices
    # spread over parts, and a bundle of other 'edges' as random subsets
    # containing at least one e-vertex and one cover vertex or not.
    parts_of = {}
    evs = list(range(6))
    for i, v in enumerate(evs):
        parts_of[v] = i
    tvs = list(range(6, 11))
    for u in tvs:
        parts_of[u] = RNG.next() % 6
    edges = []
    for _ in range(3 + RNG.next() % 8):
        f = set()
        for v in evs:
            if RNG.next() % 3 == 0:
                f.add(v)
        for u in tvs:
            if RNG.next() % 3 == 0:
                f.add(u)
        edges.append(frozenset(f))
    I = 0
    for v in evs:
        i = parts_of[v]
        for u in tvs:
            if parts_of[u] == i:
                continue
            n_iu = sum(1 for f in edges if v in f and u in f)
            I += comb(n_iu, 2)
    Ip = 0
    for f, g in itertools.combinations(edges, 2):
        cnt = 0
        for v in evs:
            if v in f and v in g:
                for u in tvs:
                    if u in f and u in g and parts_of[u] != parts_of[v]:
                        cnt += 1
        Ip += cnt
    if I != Ip:
        id_ok = False
check("on 200 random synthetic systems the incidence sum "
      "sum_i sum_u C(n_iu, 2) equals the per-pair count of shared "
      "(e-vertex, cover-vertex) combinations, exactly",
      id_ok)

# The a*b SPECIALIZATION, nonvacuously: random TRANSVERSAL systems (the
# real-core shape, where a shared cover vertex is automatically outside
# every shared e-vertex's part), with genuine double-meets.
ab_ok = True
ab_nonzero = 0
for trial in range(200):
    nv = 4                                             # vertices per part
    def vid(part, idx):
        return part * nv + idx
    e = [vid(i, 0) for i in range(6)]
    T = []
    while len(T) < 5:
        cand = vid(RNG.next() % 6, 1 + RNG.next() % (nv - 1))
        if cand not in T:
            T.append(cand)
    others = []
    for _ in range(4 + RNG.next() % 6):
        f = frozenset(vid(i, RNG.next() % nv) for i in range(6))
        others.append(f)
    I = 0
    for v in e:
        i = v // nv
        for u in T:
            if u // nv == i:
                continue
            n_iu = sum(1 for f in others if v in f and u in f)
            I += comb(n_iu, 2)
    Ip = 0
    for f, g in itertools.combinations(others, 2):
        a = sum(1 for v in e if v in f and v in g)
        b = sum(1 for u in T if u in f and u in g)
        Ip += a * b
        if a * b:
            ab_nonzero += 1
    if I != Ip:
        ab_ok = False
check("the a*b FORM of the identity, on 200 random TRANSVERSAL systems "
      "(the real-core shape, where the u-outside-V_i guarantee holds "
      "structurally): incidence sum == sum of a*b exactly, and the test "
      "is NONVACUOUS -- exactly 292 pair terms with a*b > 0 exercised "
      "(deterministic LCG)",
      ab_ok and ab_nonzero == 292,
      "%d nonzero a*b pair terms" % ab_nonzero)
note("in a real core the pairwise count IS a*b (a shared e-vertices "
     "times b shared cover vertices) because a shared cover vertex is "
     "automatically outside the part of every shared e-vertex: u in "
     "V_i cap f would be f's unique part-i vertex v_i, and v_i is "
     "never in T_e.  The synthetic systems above drop that guarantee, "
     "so they test the raw incidence identity; section 4 tests the "
     "a*b form on a real core")

# ==========================================================================
# 4.  Enactment on a real core: 0013's 14-edge tau = 5 rehearsal
# ==========================================================================

head("4.  (CC) enacted on the rehearsal core (t = 5 analog)")


def norm(v):
    for x in v:
        if x % 5:
            inv = pow(x, 3, 5)
            return tuple((inv * y) % 5 for y in v)
    return None


PTS = sorted(set(n for n in (norm(v) for v in
                             itertools.product(range(5), repeat=3))
                 if n is not None))


def on(l, p):
    return (l[0] * p[0] + l[1] * p[1] + l[2] * p[2]) % 5 == 0


P_DEL = (0, 0, 1)
VERTS = sorted(q for q in PTS if q != P_DEL)
VIDX = {}
for i, q in enumerate(VERTS):
    VIDX[q] = i
EDGES = [frozenset(VIDX[q] for q in PTS if q != P_DEL and on(l, q))
         for l in PTS if not on(l, P_DEL)]
PARTS = [frozenset(VIDX[q] for q in PTS if q != P_DEL and on(l, q))
         for l in PTS if on(l, P_DEL)]
PARTOF = {}
for i, p in enumerate(PARTS):
    for v in p:
        PARTOF[v] = i
VMASK = [0] * 30
for ei, e in enumerate(EDGES):
    for v in e:
        VMASK[v] |= (1 << ei)
FULL = (1 << 25) - 1


def kcover(E, k):
    for c in itertools.combinations(range(30), k):
        m = 0
        for v in c:
            m |= VMASK[v]
        if m & E == E:
            return c
    return None


active = list(range(25))
E = FULL
changed = True
while changed:
    changed = False
    for ei in list(active):
        E2 = E & ~(1 << ei)
        if kcover(E2, 4) is None:
            active.remove(ei)
            E = E2
            changed = True
            break
CE = [EDGES[i] for i in active]
mr = len(CE)
TC = []
for k, ei in enumerate(active):
    TC.append(frozenset(kcover(E & ~(1 << ei), 4)))

deg = {}
for e in CE:
    for v in e:
        deg[v] = deg.get(v, 0) + 1
Xr = sum(comb(d, 2) for d in deg.values()) - comb(mr, 2)
check("the deterministic rebuild reproduces certificate 0013's rehearsal "
      "core: 14 edges, and its excess is X = 0 -- inside a projective "
      "plane every two lines meet exactly once",
      mr == 14 and Xr == 0)

margins = []
ok_cc = True
for k, (e, T) in enumerate(zip(CE, TC)):
    x_e = sum(len(e & f) for j, f in enumerate(CE) if j != k) - (mr - 1)
    b = [len(T & PARTS[i]) for i in range(6)]
    lhs = 0
    for v in sorted(e):
        i = PARTOF[v]
        cls = 4 - b[i]
        n = deg[v] - 1
        if n > 0 and cls <= 0:
            ok_cc = False
        lhs += phi(n, cls if cls > 0 else 1)
    rhs = 3 * (Xr - x_e)
    margins.append(rhs - 2 * lhs)
    if 2 * lhs > rhs:
        ok_cc = False
check("the t = 5 analog of (CC) holds on ALL 14 edges of the real core "
      "with the actual lex-first private covers -- and the margin is "
      "EXACTLY ZERO on every edge: X = 0 forces both sides to 0 "
      "(every Phi term vanishes -- mostly by class count, twice by "
      "n = 0 at a b_i = 4 concentration, which this tau = 5 object may "
      "carry because lemma (A) binds only tau = 6 counterexamples).  A "
      "DIRECTION error in the derivation would fail loudly here; scale "
      "factors are caught by section 5's exact counts instead",
      ok_cc and margins == [0] * 14)

id2_ok = True
for k, (e, T) in enumerate(zip(CE, TC)):
    others = [f for j, f in enumerate(CE) if j != k]
    I = 0
    for v in e:
        i = PARTOF[v]
        for u in T:
            if PARTOF[u] == i:
                continue
            n_iu = sum(1 for f in others if v in f and u in f)
            I += comb(n_iu, 2)
    Ip = 0
    for f, g in itertools.combinations(others, 2):
        Ip += len(f & g & e) * len(f & g & T)
    if I != Ip:
        id2_ok = False
sum_x = sum(sum(len(e & f) for j, f in enumerate(CE) if j != k) - (mr - 1)
            for k, e in enumerate(CE))
check("on the real core the a*b form of the accounting identity is exact "
      "for all 14 edges (vacuously so -- two projective-plane lines "
      "never share both an e-vertex and a cover vertex, so every term "
      "is 0 = 0; the NONVACUOUS test of the a*b form is check 8's "
      "transversal synthetics), and sum_e x_e = 2X holds (0 = 0)",
      id2_ok and sum_x == 2 * Xr)
note("NOT TOO STRONG: X = 0 is REALIZED by this real tau = 5 core -- "
     "(CC) does not forbid low excess in general; the m = 22 exclusion "
     "below is about that rung's pair-count tension, not about (CC) "
     "alone")

# ==========================================================================
# 5.  The m = 22 kill: X <= 1 leaves nothing
# ==========================================================================

head("5.  m = 22, pinned ladder: every X <= 1 configuration dies")

N = {1: 2, 2: 4, 3: 6, 4: 9, 5: 13}
M = 22
TARGET = comb(M, 2)


def profiles(m, ladder):
    caps = {k: m - ladder[6 - k] for k in range(1, 6)}
    out = []

    def rec(left, cur):
        k = len(cur)
        if k in caps and sum(cur) > caps[k]:
            return
        if left == 0:
            if len(cur) >= 6:
                out.append(tuple(cur))
            return
        for s in range(min(left, cur[-1] if cur else m - ladder[5]), 1, -1):
            if 0 < left - s < 2:
                continue
            rec(left - s, cur + [s])
    rec(m, [])
    return out


def sc(p):
    return sum(comb(d, 2) for d in p)


P22 = sorted(profiles(M, N), key=sc)
S22 = [sc(p) for p in P22]
check("the pinned-ladder profile list at m = 22 has 67 members "
      "(entries >= 2 by (A), >= 6 entries by (B), prefix caps from the "
      "ladder)", len(P22) == 67)


def scan(xmax):
    found = []
    n = len(P22)

    def rec(start, k, tot, cur):
        if k == 6:
            if TARGET <= tot <= TARGET + xmax:
                found.append(tuple(cur))
            return
        rem = 6 - k
        for i in range(start, n):
            t2 = tot + S22[i]
            if t2 + (rem - 1) * S22[i] > TARGET + xmax:
                break
            if t2 + (rem - 1) * S22[-1] < TARGET:
                continue
            cur.append(i)
            rec(i, k + 1, t2, cur)
            cur.pop()
    rec(0, 0, 0, [])
    return found


def judge(cfg_idx, use_stars=True, use_d2=True):
    c = [P22[i] for i in cfg_idx]
    X = sum(sc(p) for p in c) - TARGET
    Dmax = max(d for p in c for d in p)
    if 2 * phi(Dmax - 1, 5) > 3 * X:
        return "CCedge"
    if use_stars and X <= 1:
        n7 = sum(1 for p in c for d in p if d >= 7)
        if 7 * n7 > M:
            return "stars"
    if use_d2:
        D2 = sum(1 for p in c for d in p if d == 2)
        if 2 * D2 > M:
            return "D2"
    lhs = 2 * sum(d * phi(d - 1, 5) for p in c for d in p)
    if lhs > 3 * (M - 2) * X:
        return "CCglobal"
    return "ALIVE"


t0 = time.time()
CF1 = scan(1)
check("506,204 configurations have X <= 1 (total degree-pair sum 231 or "
      "232)", len(CF1) == 506204, "%.1fs" % (time.time() - t0))

t0 = time.time()
tally = {}
for c in CF1:
    v = judge(c)
    tally[v] = tally.get(v, 0) + 1
check("ALL of them die: 504,478 on the per-edge degree cap "
      "(2 Phi(Delta-1,5) > 3X), 1,150 on star-disjointness (four or "
      "more degree-7 vertices need 28 > 22 edges), 576 on the (D2) "
      "cap, ZERO alive",
      tally == {"CCedge": 504478, "stars": 1150, "D2": 576},
      "%.1fs -- X >= 2 for every critical core at m = 22"
      % (time.time() - t0))
note("the per-edge corollaries, spelled out: X = 0 kills any degree >= 7 "
     "(2*Phi(6,5) = 2 > 0); X = 1 kills any degree >= 8 (2*Phi(7,5) = "
     "4 > 3) and forbids two degree->=7 vertices in one edge (2+2 = 4 "
     "> 3), which with same-part disjointness makes 7-stars pairwise "
     "edge-disjoint")

# ==========================================================================
# 6.  Controls and teeth
# ==========================================================================

head("6.  controls")

t0 = time.time()
CF2 = [c for c in scan(2) if sum(S22[i] for i in c) == TARGET + 2]
alive2 = sum(1 for c in CF2 if judge(c) == "ALIVE")
check("NOT TOO STRONG: at X = 2 the same judge leaves 9,224 of 210,713 "
      "configurations alive -- THIS certificate's rules do not decide "
      "the X = 2 layer, and its claim stops at X >= 2 (the layer is "
      "certificate 0016's claim, by a sharper corner unavailable to "
      "this judge; NOTES erratum 2026-07-27)",
      len(CF2) == 210713 and alive2 == 9224, "%.1fs" % (time.time() - t0))

revlist = [c for c in CF1 if judge(c, use_stars=False) == "ALIVE"]
check("SENSITIVITY: drop the star-disjointness rule and exactly 6 "
      "configurations revive, every one with X = 1 and exactly four "
      "degree-7 vertices (both properties asserted, not just stated) "
      "-- the rule is load-bearing, and by exactly this much",
      len(revlist) == 6
      and all(sum(sc(p) for p in (P22[i] for i in c)) - TARGET == 1
              for c in revlist)
      and all(sum(1 for i in c for d in P22[i] if d >= 7) == 4
              for c in revlist))
revived_d2 = sum(1 for c in CF1 if judge(c, use_d2=False) == "ALIVE")
check("SENSITIVITY: drop the (D2) cap instead and exactly the 576 "
      "configurations it killed revive -- none of them is caught by "
      "the global form downstream, so 0008's cap is independently "
      "load-bearing here",
      revived_d2 == 576)
def judge_sketch(cfg_idx):
    """The outside review's sketch, literally: global (CC) + (D2) only."""
    c = [P22[i] for i in cfg_idx]
    X = sum(sc(p) for p in c) - TARGET
    D2 = sum(1 for p in c for d in p if d == 2)
    if 2 * D2 > M:
        return "D2"
    if 2 * sum(d * phi(d - 1, 5) for p in c for d in p) > 3 * (M - 2) * X:
        return "CCglobal"
    return "ALIVE"


sketch_alive = sum(1 for c in CF1 if judge_sketch(c) == "ALIVE")
check("HONESTY, provenance -- now measured IN-TRANSCRIPT: the outside "
      "review's sketch ('(CC) global + the D2 cap') leaves exactly 52 "
      "survivors and does NOT close the kill; the per-edge corollaries "
      "and the star count -- not in the sketch -- are what close it.  "
      "Audited, repaired, and stronger than claimed",
      sketch_alive == 52)


def max_total(dmax, n7cap, d2cap):
    """DP: max sum of sc over 6-profile multisets under a max-degree cap,
    a cap on the count of degree-(>= 7) vertices, and a (D2) cap."""
    pool = [p for p in P22 if max(p) <= dmax]
    stats = [(sc(p), sum(1 for d in p if d >= 7), sum(1 for d in p if d == 2))
             for p in pool]
    best = {(0, 0): 0}
    for _ in range(6):
        nxt = {}
        for (n7, d2), tot in best.items():
            for (s, s7, s2) in stats:
                k = (n7 + s7, d2 + s2)
                if k[0] > n7cap or k[1] > d2cap:
                    continue
                if nxt.get(k, -1) < tot + s:
                    nxt[k] = tot + s
        best = nxt
    return max(best.values())


check("THE MARGIN, computed: under the X = 1 rules (Delta <= 7, at most "
      "three degree-7 vertices, D2 <= 11) the maximum achievable "
      "degree-pair total over the field is EXACTLY 231 -- one short of "
      "the 232 that X = 1 requires; under the X = 0 rules (Delta <= 6, "
      "D2 <= 11) it is 225, six short of 231.  The kill closes by one "
      "unit, and says so",
      max_total(7, 3, 11) == 231 and max_total(6, 99, 11) == 225)

head("Result")

print("""
  (CC)  2 sum_i Phi(d_i - 1, 5 - b_i) <= 3(X - x_e)   PROVEN-BY-CERTIFICATE
        per edge, and its global form                  (in-house: 0013)
  X >= 2 for every critical core at m = 22             PROVEN-BY-CERTIFICATE
                                                       (field: 0005/0009/0012;
                                                       (D2): 0008)

  The bottom of the window is no longer smooth: a minimum counterexample
  core at m = 22 must carry excess at least 2 -- at least two extra
  edge-meets beyond the one-per-pair minimum, i.e. the structure is
  forced into the nonlinear regime the moment it exists.  The m = 23
  frontier now has a lever that did not exist this morning.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(1 if FAILED else 0)
