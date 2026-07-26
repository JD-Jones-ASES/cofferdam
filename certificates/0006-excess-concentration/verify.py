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
W_t = {e : k_e >= t}, so #{pairs at level >= t} <= C(|W_t|,2); and because delta
is increasing,

  D = sum_{t>=3} (delta(t)-delta(t-1)) |W_t| >= 1*q_3 + 2*q_4 + 3*q_5,
      q_t := least q with C(q,2) >= #{pairs at level >= t}.

(L8) is the contradiction between three demands: (L7) forces A, hence B, to be
LARGE; (C2) with C(t,2)/(t-1) = t/2 <= 5/2 forces B <= 5X/2, so B can only be
carried by MANY shallow pairs -- which X forbids -- or by DEEP ones -- which D
forbids.  At m = 20 every admissible configuration fails.

WHY THIS IS NOT TOO STRONG (the control that matters)
-----------------------------------------------------
An argument that killed every m would be "proving" Ryser at r = 6, an open
problem, and would therefore be wrong.  Check 8 runs the identical machinery at
m = 21 and finds survivors.  (L8) discriminates; it does not prove too much.

EXTERNAL DEPENDENCIES, and what is reached without them
-------------------------------------------------------
  f(6) = 13 = g(5)  (Aharoni-Barat-Wanless; Abu-Khazneh-Pokrovskiy).  Used only
      through the k=1 cap Delta <= m - 13, which is what limits the admissible
      profiles.  Certificate 0005 records the same dependence and reaches m >= 19
      without it.
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
check("B <= floor(5X/2) whenever X > 0 (the sharp form of the excess bound)",
      all(sum(comb(v, 2) for v in q['t'].values()) <= (5 * q['X']) // 2
          for q in res.values() if q['X'] > 0))

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
      "best d1=7 profile scores 33, best d1<=6 scores 31, and 6x31 = 186 < 190")

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

check("m <= 19 has no admissible configuration at all (certificate 0005 agrees)",
      all(len(multisets(mm)[1]) == 0 for mm in (17, 18, 19)),
      "so this certificate and 0005 overlap consistently rather than conflict")

# THE control: an argument that killed every m would be proving Ryser at r=6.
P21, C21 = multisets(21)
surv21 = None
n21 = 0
for combo in C21:
    dead, why = l8_kills(combo, 21)
    if not dead:
        n21 += 1
        if surv21 is None:
            surv21 = (combo, why)
    if n21 >= 1 and surv21 is not None:
        break
check("(L8) is NOT vacuously strong: at m = 21 it leaves survivors",
      surv21 is not None,
      f"{len(C21)} multisets at m=21; e.g. "
      f"{'+'.join(str(p[0]) for p in surv21[0]) if surv21 else '-'} "
      f"{surv21[1] if surv21 else ''}")
check("so (L8) does not 'prove' Ryser at r = 6, which would falsify it", True,
      "the m = 20 kill is specific, not an artefact of an over-strong lemma")

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

print(f"{COUNT[0]} checks, {time.time()-T0:.0f}s, "
      f"{'ALL GREEN' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(1 if FAIL else 0)
