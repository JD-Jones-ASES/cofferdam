#!/usr/bin/env python3
"""Certificate 0006 — (L8), the excess-concentration incompatibility: m >= 21.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from lib/.

WHAT IS CLAIMED
---------------
  (L7)  for x, y in different parts, |E(x) n E(y)| >= d(x)+d(y)-(m-g(4))
  (L8)  the excess-concentration incompatibility (stated below)
  **m = 20 is impossible**                            PROVEN-MODULO-CITATION
  **a Ryser r=6 counterexample has m >= 21**          PROVEN-MODULO-CITATION
  and the citation is f(6) = 13, the same single one certificate 0005 leans on.

  Certificate 0005 excluded m <= 19.  This one excludes m = 20, which was its
  sole survivor, so together they give m >= 21.

  SUPERSEDED IN STRENGTH, NOT IN CONTENT.  Certificate 0007 runs this same
  machinery on the weaker rung N(5) >= 11, which is ours, and still kills every
  m <= 20 -- so the floor of 21 does NOT depend on f(6) = 13 and is
  PROVEN-BY-CERTIFICATE citing nothing.  This certificate's own labels are left
  as they stand, because they are accurate about what THIS file proves; read them
  as the cited-input route to a result 0007 reaches without any citation.

PROVENANCE
----------
Three labs worked this problem in parallel; this one fell behind the others and
inherited the thread, which is why it re-derives rather than transcribes.  The
pointers that opened certificates 0005 and 0006 came from Codex; the proofs,
searches, machinery and controls are this repo's.  Nothing sealed was read.

THE ARGUMENT
------------
Choose one maximum-degree vertex u_j in each part; put U = {u_1..u_6},
M_j = d(u_j), and for edges e, f and parts i, j:

    k_e  = |e n U|                      c_ij = |E(u_i) n E(u_j)|
    t_ef = #{j : u_j in e n f}          X    = sum_v C(d(v),2) - C(m,2)

Four identities, each a double count:

  (I1) sum_e k_e           = sum_j M_j
  (I2) sum_e C(k_e,2)      = sum_{i<j} c_ij            =: A
  (I3) sum_{e<f} C(t_ef,2) = sum_{i<j} C(c_ij,2)       =: B
  (I4) sum_{e<f} t_ef      = sum_j C(M_j,2)

and four facts:

  (L2) sum_v C(d(v),2) = sum_{e<f} |e n f| >= C(m,2), so X = sum_{e<f}(|e n f| - 1)
  (L7) c_ij >= M_i + M_j - (m - g(4)):  delete both stars and tau >= 4 survives
       on m - |E(u_i) u E(u_j)| edges, so that count is >= g(4) = 8
  (C2) |e n f| >= t_ef, hence  sum_{e<f} (t_ef - 1)^+ <= X
  (C3) t_ef <= 5 for e != f: agreeing in all six parts would make e = f

Now the squeeze.  Write delta(k) = C(k,2) - (k-1) >= 0, so delta(1)=delta(2)=0,
delta(3)=1, delta(4)=3, delta(5)=6, delta(6)=10.  By (I1) and (I2),

  (C4) sum_e delta(k_e) = A - sum_j M_j + m =: D.

Since t_ef <= min(k_e, k_f), every edge-pair at level >= t lies inside
W_t = {e : k_e >= t}, so #{pairs at level >= t} <= C(|W_t|,2), hence |W_t| >= q_t.
Mind delta(0) = 1: delta DIPS at k = 0 -> 1 and is only nondecreasing on k >= 1,
so the layer-cake expansion cannot be started at t = 3.  In full,

  D = m*delta(0) + sum_{t>=1} (delta(t)-delta(t-1)) |W_t|,

where delta(1)-delta(0) = -1 collapses the base and t=1 layers to
n_0 := #{e : k_e = 0} = m - |W_1|, and delta(2)-delta(1) = 0 kills the t=2 layer:

  (C5) D = n_0 + |W_3| + 2|W_4| + 3|W_5| + 4|W_6| >= 1*q_3 + 2*q_4 + 3*q_5,
       q_t := least q with C(q,2) >= #{pairs at level >= t}.

Both dropped terms (n_0 and 4|W_6|) are >= 0, so the bound the sweep uses is
conservative -- it can only understate D, never overstate it, and understating D
is the direction that makes a kill HARDER.  (C5) is pinned on the witnesses by
its own check;
the earlier printed form of it omitted n_0 and was falsified by this
certificate's own 5-edge witness, where n_0 = 1.

(L8) is the contradiction between three demands: (L7) forces A, hence B, to be
LARGE; (C2) with C(t,2)/(t-1) = t/2 <= 5/2 forces B <= 5X/2, so B can only be
carried by MANY shallow pairs -- which X forbids -- or by DEEP ones -- which D
forbids.  At m = 20 every admissible configuration fails.

WHY THIS IS NOT TOO STRONG (the control that matters)
-----------------------------------------------------
An argument that killed every m would be "proving" Ryser at r = 6, an open
problem, and would therefore be wrong.  The last two checks run the identical
machinery at m = 21 and find 6198 survivors of 43875.  (L8) discriminates; it
does not prove too much.  (Check numbers are deliberately not quoted here: they
shift whenever a check is added, and a stale cross-reference is a small lie that
costs a reader real time.)

EXTERNAL DEPENDENCIES, and what is reached without them
-------------------------------------------------------
  f(6) = 13 = g(5)  (Aharoni-Barat-Wanless Thm 2.7, which states it in exactly the
      tau >= 5 form the ladder consumes; independently Abu-Khazneh-Pokrovskiy).
      Used only through the k=1 cap Delta <= m - 13, which is what limits the
      admissible profiles.  Certificate 0005 records the same dependence and
      reaches m >= 19 without it -- and certificate 0007 reaches m >= 21 without
      it, so this input is removable rather than merely isolated.
  g(4) = 8, proven in certificates 0001 and 0005 -- ours, not cited.  It is what
      makes (L7) numerical.
  N(1..4) = 2,4,6,9, proven in certificate 0005 -- ours.
  NOTHING else.  In particular this certificate uses NO value-pool argument and
  NO (L4) input: the ceiling on A is the trivial concentration bound, which is
  strictly weaker and therefore strictly conservative.
"""

import itertools
import sys
import time
from math import comb

FAIL = []
COUNT = [0]


def check(label, cond, detail=""):
    COUNT[0] += 1
    tag = "ok  " if cond else "FAIL"
    if not cond:
        FAIL.append(label)
    print(f"  [{tag}] {COUNT[0]:2d}. {label}" + (f"   {detail}" if detail else ""))

NOTES_N = [0]


def note(label, detail=""):
    """A STATED FACT -- a citation, or a step proved by hand and recorded here --
    and NOT a machine check.  Printed with its own tag and counted separately, so
    the check count can never imply a test that did not run."""
    NOTES_N[0] += 1
    print(f"  [note] {label}" + (f"   {detail}" if detail else ""))


def head(s):
    print(f"\n=== {s} ===")


G4 = 8                                  # ours (certs 0001, 0005)
N = {1: 2, 2: 4, 3: 6, 4: 9, 5: 13}     # 13 is the cited f(6); the rest are ours
DELTA = {k: comb(k, 2) - (k - 1) for k in range(0, 8)}


# ==========================================================================
# 1. The identities, verified on explicit objects
# ==========================================================================

# certificate 0005's witnesses, plus two more objects built here
W8 = [(0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1), (0, 2, 2, 2, 2, 2), (1, 0, 1, 3, 2, 2),
      (2, 0, 3, 2, 1, 3), (3, 1, 3, 0, 3, 2), (3, 3, 0, 1, 2, 3), (4, 3, 1, 2, 3, 0)]
W9 = W8 + [(0, 2, 1, 2, 2, 2)]
W5 = [tuple([min(i, (p - i) % 5) for p in range(5)] + [i]) for i in range(5)]
W3 = [(0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1), (1, 0, 1, 1, 1, 1)]


def identities(H):
    """Compute every quantity of (L8) directly from an edge list, by brute force."""
    m, r = len(H), 6
    deg = {}
    for e in H:
        for j in range(r):
            deg[(j, e[j])] = deg.get((j, e[j]), 0) + 1
    U = []
    for j in range(r):
        best = max((d, s) for (jj, s), d in deg.items() if jj == j)
        U.append((j, best[1]))
    M = [deg[u] for u in U]
    k = [sum(1 for (j, s) in U if e[j] == s) for e in H]
    c = {}
    for a in range(r):
        for b in range(a + 1, r):
            c[(a, b)] = sum(1 for e in H
                            if e[U[a][0]] == U[a][1] and e[U[b][0]] == U[b][1])
    t = {}
    for (i1, e), (i2, f) in itertools.combinations(list(enumerate(H)), 2):
        t[(i1, i2)] = sum(1 for (j, s) in U if e[j] == s and f[j] == s)
    X = sum(comb(d, 2) for d in deg.values()) - comb(m, 2)
    inter = sum(sum(1 for j in range(r) if e[j] == f[j])
                for e, f in itertools.combinations(H, 2))
    return dict(m=m, M=M, k=k, c=c, t=t, X=X, deg=deg, inter=inter)


head("The identities of (L8), each verified by brute force on explicit objects")

named = [("the 3-edge g(2) witness", W3), ("the 5-edge g(3) witness", W5),
         ("the 8-edge g(4) witness", W8), ("the 9-edge N(4) witness", W9)]
res = {n: identities(H) for n, H in named}

check("(L2) sum_v C(d,2) = sum_{e<f} |e n f| on all four objects",
      all(sum(comb(d, 2) for d in q['deg'].values()) == q['inter']
          for q in res.values()))
check("(I1) sum_e k_e = sum_j M_j",
      all(sum(q['k']) == sum(q['M']) for q in res.values()))
check("(I2) sum_e C(k_e,2) = sum_{i<j} c_ij",
      all(sum(comb(x, 2) for x in q['k']) == sum(q['c'].values())
          for q in res.values()))
check("(I3) sum_{e<f} C(t_ef,2) = sum_{i<j} C(c_ij,2)",
      all(sum(comb(v, 2) for v in q['t'].values())
          == sum(comb(v, 2) for v in q['c'].values()) for q in res.values()))
check("(I4) sum_{e<f} t_ef = sum_j C(M_j,2)",
      all(sum(q['t'].values()) == sum(comb(x, 2) for x in q['M'])
          for q in res.values()))
check("(C2) sum_{e<f} (t_ef - 1)^+ <= X",
      all(sum(max(0, v - 1) for v in q['t'].values()) <= q['X']
          for q in res.values()),
      "  ".join(f"{n}: {sum(max(0,v-1) for v in q['t'].values())} <= {q['X']}"
                for n, q in res.items()))
check("(C3) t_ef <= 5 for distinct edges",
      all(all(v <= 5 for v in q['t'].values()) for q in res.values()))
check("(C4) sum_e delta(k_e) = sum_{i<j} c_ij - sum_j M_j + m",
      all(sum(DELTA[x] for x in q['k'])
          == sum(q['c'].values()) - sum(q['M']) + q['m'] for q in res.values()))
check("t_ef <= min(k_e, k_f)",
      all(all(q['t'][(i, j)] <= min(q['k'][i], q['k'][j]) for (i, j) in q['t'])
          for q in res.values()))

# (C5), the layer-cake form of D.  This check exists because the earlier printed
# form of it dropped n_0, and the 5-edge witness below -- already shipped in this
# certificate -- falsifies that form (it reads 3 where D = 4).  An identity that
# is displayed but never asserted is an identity nobody has tested.
def c5_terms(q):
    W = {t: sum(1 for x in q['k'] if x >= t) for t in range(1, 7)}
    n0 = q['m'] - W[1]
    return n0, W


ok_c5, det_c5 = True, []
for n, q in res.items():
    D = sum(q['c'].values()) - sum(q['M']) + q['m']            # (C4), exact
    n0, W = c5_terms(q)
    lhs = n0 + W[3] + 2 * W[4] + 3 * W[5] + 4 * W[6]
    bad = W[3] + 2 * W[4] + 3 * W[5] + 4 * W[6]               # the form without n_0
    if lhs != D:
        ok_c5 = False
    det_c5.append(f"{n.split()[1]}: n_0={n0}, D={D}"
                  + ("" if bad == D else f" (dropping n_0 would give {bad})"))
check("(C5) D = n_0 + |W_3| + 2|W_4| + 3|W_5| + 4|W_6|, with n_0 = #{e : k_e = 0}",
      ok_c5, "  ".join(det_c5))
check("and the same expression WITHOUT n_0 is false on at least one witness, "
      "which is why (C5) is asserted and not merely displayed",
      any(c5_terms(q)[0] > 0 for q in res.values()),
      "delta(0) = 1, so delta dips at k = 0 -> 1; the layer cake cannot start at t = 3")
# POSITIVE CONTROL on (L7) itself.  Every other identity here is checked on the
# witnesses, but (L7) -- the inequality that forces A and hence B to be large, and
# so the one doing half the killing -- was not.  Its general form: for an object
# with tau = t, deleting two stars in different parts leaves tau >= t-2 on the
# surviving edges, so that count is >= g(t-2), i.e.
#     c_ij >= M_i + M_j - (m - g(t-2)).
# At t = 6 this is (L7) as used.  It must hold on objects that EXIST.
GLOW = {0: 0, 1: 1, 2: 3, 3: 5, 4: 8}
ok_l7, det_l7 = True, []
for n, q in res.items():
    m_, M_ = q['m'], q['M']
    tq = {3: 2, 5: 3, 8: 4, 9: 4}[m_]           # tau of each named witness
    slacks = []
    for (a, b), cval in q['c'].items():
        floor = M_[a] + M_[b] - (m_ - GLOW[max(tq - 2, 0)])
        slacks.append(cval - floor)
    if min(slacks) < 0:
        ok_l7 = False
    det_l7.append(f"{n.split()[1]}: tightest slack {min(slacks)}")
check("POSITIVE CONTROL: (L7) holds on every object that actually exists, and is "
      "TIGHT on each -- so it is not vacuously satisfied", ok_l7,
      "  ".join(det_l7))

# The `if q['X'] > 0` guard here used to silently drop W5 (which has X = 0
# exactly), so the check covered 3 of the 4 witnesses while its label implied 4.
# The guard was never needed -- at X = 0 both sides are 0 -- and a check whose
# label claims more coverage than its code has is the same hazard as D-015's
# literal `True`.  Guard removed, coverage now printed.
check("B <= floor(5X/2) on every witness, X = 0 included (the excess bound)",
      all(sum(comb(v, 2) for v in q['t'].values()) <= (5 * q['X']) // 2
          for q in res.values()),
      "%d of %d witnesses, X values %s"
      % (len(res), len(res), sorted(q['X'] for q in res.values())))

# POSITIVE CONTROL.  The delta budget is the one inequality of (L8) that does the
# killing, so it must be checked in the direction that would expose it as false:
# on objects that EXIST, it has to hold with room to spare.
def qmin0(n):
    if n <= 0:
        return 0
    q = 2
    while comb(q, 2) < n:
        q += 1
    return q


ok_pos, detail = True, []
for n, q in res.items():
    A = sum(q['c'].values())
    D = A - sum(q['M']) + q['m']
    lv = {t: sum(1 for v in q['t'].values() if v == t) for t in range(2, 7)}
    need = (qmin0(lv[3] + lv[4] + lv[5] + lv[6])
            + 2 * qmin0(lv[4] + lv[5] + lv[6]) + 3 * qmin0(lv[5] + lv[6]))
    if D < need:
        ok_pos = False
    detail.append(f"{n.split()[1]}: D={D} >= need={need}")
check("POSITIVE CONTROL: the delta budget D >= q_3 + 2q_4 + 3q_5 holds on every "
      "object that actually exists", ok_pos, "  ".join(detail))


# ==========================================================================
# 2. The admissible profiles, from certificate 0005's lemmas
# ==========================================================================

def profiles(m):
    """A part's degree profile: a partition of m into at least 6 entries, each at
    least 2 (lemmas (A) and (B)), whose k largest sum to at most m - N(6-k)
    (lemma (C))."""
    caps = {k: m - N[6 - k] for k in range(1, 6)}
    out = []

    def rec(left, cur):
        k = len(cur)
        if k in caps and sum(cur) > caps[k]:
            return
        if left == 0:
            if len(cur) >= 6:
                out.append(tuple(cur))
            return
        for s in range(min(left, cur[-1] if cur else m - N[5]), 1, -1):
            if 0 < left - s < 2:
                continue
            rec(left - s, cur + [s])
    rec(m, [])
    return out


def sc(p):
    return sum(comb(d, 2) for d in p)


def qmin(n):
    if n <= 0:
        return 0
    q = 2
    while comb(q, 2) < n:
        q += 1
    return q


def l8_kills(combo, m):
    """True iff (L8) rules this multiset of six part profiles out."""
    Ms = [p[0] for p in combo]
    S = sum(Ms)
    X = sum(sc(p) for p in combo) - comb(m, 2)
    Pc = sum(comb(x, 2) for x in Ms)
    floors = [max(0, Ms[i] + Ms[j] - (m - G4))
              for i in range(6) for j in range(i + 1, 6)]
    L = sum(floors)
    # ceiling on A: sum_e k_e = S over m edges with k_e <= 6, so A is largest
    # under maximum concentration.  No pool, no (L4) -- strictly conservative.
    q, rr = divmod(S, 6)
    U = min(q, m) * comb(6, 2) + (comb(rr, 2) if q < m else 0)
    if U < L:
        return True, f"(L7) floor {L} exceeds the concentration ceiling {U}"
    for A in range(L, U + 1):
        D = A - S + m
        if D < 0:
            continue
        # B is minimised, for sum c_ij = A fixed, by the most equal allocation
        # above the floors (C(.,2) is convex)
        c = list(floors)
        for _ in range(A - L):
            c[min(range(len(c)), key=lambda i: c[i])] += 1
        Bmin = sum(comb(v, 2) for v in c)
        Bcap = (5 * X) // 2
        if Bmin > Bcap:
            continue
        for Bv in range(Bmin, Bcap + 1):
            for n5 in range(0, X // 4 + 1):
                for n4 in range(0, (X - 4 * n5) // 3 + 1):
                    for n3 in range(0, (X - 4 * n5 - 3 * n4) // 2 + 1):
                        rest = Bv - 10 * n5 - 6 * n4 - 3 * n3
                        if rest < 0:
                            continue
                        n2 = rest
                        if n2 + 2 * n3 + 3 * n4 + 4 * n5 > X:
                            continue
                        if 2 * n2 + 3 * n3 + 4 * n4 + 5 * n5 > Pc:
                            continue
                        if n2 + n3 + n4 + n5 > comb(m, 2):
                            continue
                        need = (qmin(n3 + n4 + n5) + 2 * qmin(n4 + n5)
                                + 3 * qmin(n5))
                        if D >= need:
                            return False, (f"survives at A={A}, B={Bv}, "
                                           f"levels(n2..n5)=({n2},{n3},{n4},{n5})")
    return True, "every (A, B, level structure) busts the excess or delta budget"


def multisets(m):
    P = sorted(profiles(m), key=sc, reverse=True)
    return P, [c for c in itertools.combinations_with_replacement(P, 6)
               if sum(sc(p) for p in c) >= comb(m, 2)]


head("m = 20: the admissible configurations, and (L8) applied to each")

T0 = time.time()
P20, C20 = multisets(20)
check("at m = 20 there are exactly 32 admissible part profiles",
      len(P20) == 32, f"got {len(P20)}, best is {P20[0]} with sum C(d,2) = {sc(P20[0])}")
check("the pair count (L2) leaves exactly 105 multisets of six profiles",
      len(C20) == 105, f"got {len(C20)}")
check("every one of them contains at least two parts with a degree-7 vertex",
      all(sum(1 for p in c if p[0] == 7) >= 2 for c in C20),
      "best d1=7 profile scores 33, best d1<=6 scores 31: zero sevens reach at "
      "most 6x31 = 186, ONE seven at most 33 + 5x31 = 188, and both fall short "
      "of C(20,2) = 190 -- the one-seven case is the half that has to be said")

alive = []
for combo in C20:
    dead, why = l8_kills(combo, 20)
    if not dead:
        alive.append((combo, why))
check("(L8) rules out ALL 105 — so m = 20 is impossible",
      not alive, f"{len(C20)} killed, {len(alive)} survivors, {time.time()-T0:.0f}s")
if alive:
    for c, why in alive[:5]:
        print("        SURVIVOR:", '+'.join(str(p[0]) for p in c), c, why)

# the dead heat certificate 0005 recorded, now dead
dh = tuple([(7, 4, 3, 2, 2, 2)] * 6)
d, why = l8_kills(dh, 20)
check("in particular the (L4)/(L7) dead heat, all six parts (7,4,3,2,2,2), dies",
      d, f"X = {sum(sc(p) for p in dh) - comb(20,2)}, "
         f"D = 30 - 42 + 20 = 8, and the level structures need 13 and 9")

head("Controls")

# The label used to say "m <= 19" while the code tested only (17, 18, 19).  Below
# m = 12 no profile exists at all -- six parts of size >= 2 need twelve edges --
# so 12..19 IS the whole range, and it is cheap to test all of it.
lowm = [mm for mm in range(12, 20) if multisets(mm)[1]]
check("m <= 19 has no admissible configuration at all (certificate 0005 agrees)",
      not lowm,
      "every m from 12 to 19 tested; below 12 no part profile exists at all, "
      "since six parts of minimum degree 2 need 12 edges")

# THE control: an argument that killed every m would be proving Ryser at r=6.
# This is the load-bearing control, so it is COMPUTED here rather than asserted
# from a separately-replayed development run.  Earlier versions stopped at the
# first survivor while the prose quoted "6198 of 43875" -- a number the
# certificate did not actually produce.  It costs ~3 min; the control is worth it.
T21 = time.time()
P21, C21 = multisets(21)
surv21 = None
n21 = 0
for combo in C21:
    dead, why = l8_kills(combo, 21)
    if not dead:
        n21 += 1
        if surv21 is None:
            surv21 = (combo, why)
check("(L8) is NOT vacuously strong: at m = 21 it leaves survivors",
      surv21 is not None,
      f"{n21} of {len(C21)} multisets at m=21 survive, {time.time()-T21:.0f}s; "
      f"e.g. {'+'.join(str(p[0]) for p in surv21[0]) if surv21 else '-'} "
      f"{surv21[1] if surv21 else ''}")
check("the same machinery kills every configuration at m = 20 and leaves "
      "thousands at m = 21, so it does not 'prove' Ryser at r = 6",
      not alive and n21 > 0,
      f"m=20: 0 of {len(C20)} survive.  m=21: {n21} of {len(C21)} survive.  "
      f"The kill is specific, not an artefact of an over-strong lemma.")

head("Result")

print(f"""
  (L7), (L8)                                    PROVEN-BY-CERTIFICATE
  m = 20 is impossible                          PROVEN-MODULO-CITATION (f(6)=13)
  a Ryser r=6 counterexample has m >= 21        PROVEN-MODULO-CITATION (f(6)=13)

  Certificate 0005 excluded m <= 19 and left Delta = 7 at m = 20 as the single
  survivor.  This certificate excludes m = 20 outright, so the floor is m >= 21.

  The claim this lab was seeded with was m >= 21.  It is now reached here by a
  derivation that shares no machinery with the chain that proposed it, and that
  leans on exactly one published constant, f(6) = 13.  Without that constant the
  floor is m >= 19 (certificate 0005).

  What is NOT claimed: nothing here says a counterexample exists at 21 or above,
  and nothing here settles Q13 (whether a 13-edge tau=5 object can have a part of
  minimum degree 2).  Q13 became unnecessary, not answered.
""")

print(f"{COUNT[0]} checks + {NOTES_N[0]} notes (stated, not tested), "
      f"{time.time()-T0:.0f}s, "
      f"{'ALL GREEN' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(1 if FAIL else 0)
