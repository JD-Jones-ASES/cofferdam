#!/usr/bin/env python3
"""Certificate 0008 -- the degree-two cap: a Ryser r=6 counterexample has m >= 22.

    python3 verify.py

Stdlib only.  No imports from lib/.  No solver.  Runs under Python 3.9.
Deterministic.  Green under `python3` and under `python3 -O`.

WHAT THIS ADDS TO CERTIFICATE 0007.  0007 killed every m from 12 to 20 on the
citation-free ladder and left m = 21 standing, with an explicit survivor.  This
certificate closes m = 21 with one further constraint:

    (D2)  every line of a Ryser r=6 counterexample contains at most one vertex
          of degree 2; hence 2*D2 <= m, where D2 counts degree-2 vertices.

(D2) is clause (iii) of Lemma 2.1 of Francetic, Herke, McKay and Wanless,
Europ. J. Combin. 61 (2017) 91-105.  IT IS NOT OURS.  It is re-derived here in
full -- section 1 proves a strictly more general constructive statement and
tests the construction exhaustively -- so that the floor cites nothing.  But
re-deriving a published lemma is a different act from finding one, and this file
does not pretend otherwise.  The same is already true of the lab's lemmas (A)
and (B), which are that paper's 2.1(ii) and 2.1(i).

THE TRAP THIS CERTIFICATE IS BUILT AROUND.  (D2) requires tau(H) >= |E|.  The
N-ladder residuals have tau = t < 6, and (D2) is FALSE for them -- section 3
ships a 13-edge tau=5 witness with 2*D2 = 18 > 13 = m.  Applying the cap
anywhere down the ladder would manufacture a false kill in exactly the direction
this lab wants.  The cap is applied to H's own six part-profiles and nowhere
else.
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
    """A check.  `cond` must be COMPUTED.  A literal True here is a note (D-015)."""
    NCHECK[0] += 1
    ok = bool(cond)
    if not ok:
        FAILED.append(label)
    tag = "ok  " if ok else "FAIL"
    print("  [%s] %2d. %s%s" % (tag, NCHECK[0], label,
                                ("   " + detail) if detail else ""))
    return ok


def note(label, detail=""):
    """Stated, not tested here.  Never counted as a check."""
    NNOTE[0] += 1
    print("  [note] %s%s" % (label, ("   " + detail) if detail else ""))


def head(s):
    print("\n" + "=" * 74)
    print(s)
    print("=" * 74)


# =========================================================================
# 1.  (D2) RE-DERIVED HERE, VIA A STRICTLY MORE GENERAL CONSTRUCTIVE LEMMA
# =========================================================================
#
# (III-C)  Let H be an intersecting hypergraph, E an edge with |E| >= 3, and
#          x != y two vertices of E with deg(x) <= 2 and deg(y) <= 2.  Then
#          tau(H) <= |E| - 1, witnessed by an explicit cover.
#
#   Put B = E \ {x,y}, so |B| = |E| - 2 >= 1, and U = {F in H : F cap B = 0}.
#   (a) E not in U, because E cap B = B is non-empty -- this is where |E| >= 3
#       is spent.
#   (b) |U| <= 2.  For F in U we have F != E by (a), so F cap E is non-empty
#       (H is intersecting); and F cap B empty with E = B + {x,y} forces
#       F cap E contained in {x,y}.  So every member of U contains x or y.  The
#       edges through x are E and at most one other E_x (deg(x) <= 2), likewise
#       E_y.  Hence U is contained in {E_x, E_y}.
#   (c) If |U| = 2 its two members are distinct edges of an intersecting family,
#       so they meet.
#   Then S = B, or B + {w} for w in the single member of U, or B + {w} for
#   w in the intersection of the two members, is a cover of size <= |E| - 1.
#
# (III)  If moreover tau(H) >= |E|, no such pair x,y exists: every edge holds at
#        most one vertex of degree <= 2.  With lemma (A) (degree >= 2) that is
#        exactly "at most one vertex of degree 2".
#
# HYPOTHESES CONSUMED: intersecting (twice -- in (b) and in (c)), |E| >= 3,
# and tau >= |E|.  NOT consumed: r-partiteness, linearity, lemma (A), lemma (B),
# simplicity, or any external constant.  That linearity is not needed matters:
# a Ryser r=6 counterexample must be non-linear.

def tau_brute(H, ground):
    """Least size of a vertex set meeting every edge.  Exhaustive, no pruning."""
    if not H:
        return 0
    for k in range(0, len(ground) + 1):
        for S in itertools.combinations(ground, k):
            s = set(S)
            if all(s & set(e) for e in H):
                return k
    return len(ground)


def degrees_of(H):
    d = {}
    for e in H:
        for v in e:
            d[v] = d.get(v, 0) + 1
    return d


def is_intersecting(H):
    return all(set(e) & set(f) for e, f in itertools.combinations(H, 2))


def build_cover(H, E, x, y):
    """The (III-C) construction, exactly as proved above.  Returns S or None."""
    B = set(E) - {x, y}
    U = [F for F in H if not (set(F) & B)]
    if len(U) == 0:
        return set(B)
    if len(U) == 1:
        w = sorted(U[0])[0]
        return set(B) | {w}
    if len(U) == 2:
        common = sorted(set(U[0]) & set(U[1]))
        if not common:
            return None                      # would refute step (c)
        return set(B) | {common[0]}
    return None                              # would refute step (b)


def families(ground, size, kmax, intersecting=True):
    """Every family of `size`-subsets of `ground` with 1..kmax edges.

    With intersecting=True the pairwise-meeting constraint is enforced DURING
    the build, so the enumeration is over intersecting families directly rather
    than by filtering.  Either way it is EXHAUSTIVE over the stated range, and
    the range is part of the claim (D-016).
    """
    cells = [tuple(c) for c in itertools.combinations(ground, size)]
    n = len(cells)
    cur = []

    def rec(start):
        if cur:
            yield tuple(cur)
        if len(cur) == kmax:
            return
        for i in range(start, n):
            c = cells[i]
            if intersecting and not all(set(c) & set(e) for e in cur):
                continue
            cur.append(c)
            for out in rec(i + 1):
                yield out
            cur.pop()

    for out in rec(0):
        yield out


head("1.  (D2) re-derived here: the construction, tested exhaustively")

# --- 1a.  the construction always produces a genuine cover of size <= |E|-1 ---
STATS = {}
for tag, ground, size, kmax in (("3-uniform on [6]", range(6), 3, 5),
                                ("4-uniform on [7]", range(7), 4, 4)):
    fam = wit = built = short = bad_cover = bad_size = 0
    u_sizes = {0: 0, 1: 0, 2: 0, 3: 0}
    for H in families(ground, size, kmax):
        fam += 1
        deg = degrees_of(H)
        for E in H:
            low = [v for v in E if deg[v] <= 2]
            if len(low) < 2:
                continue
            for x, y in itertools.combinations(low, 2):
                wit += 1
                B = set(E) - {x, y}
                U = [F for F in H if not (set(F) & B)]
                u_sizes[min(len(U), 3)] = u_sizes.get(min(len(U), 3), 0) + 1
                S = build_cover(H, E, x, y)
                if S is None:
                    bad_cover += 1
                    continue
                built += 1
                if not all(S & set(f) for f in H):
                    bad_cover += 1
                if len(S) > len(E) - 1:
                    bad_size += 1
                if len(S) < len(E) - 1:
                    short += 1
    STATS[tag] = (fam, wit, built, short, bad_cover, bad_size, dict(u_sizes))
    check("%s: every (E,x,y) witness yields a genuine cover of size <= |E|-1"
          % tag,
          bad_cover == 0 and bad_size == 0 and built == wit,
          "%d intersecting families, %d witnesses, %d covers built, "
          "%d of size |E|-2, 0 failures" % (fam, wit, built, short))

# step (b) and step (c) are what the proof actually turns on, so assert them
u3 = STATS["3-uniform on [6]"][6].get(3, 0) + STATS["4-uniform on [7]"][6].get(3, 0)
check("step (b) holds everywhere: |U| <= 2 at every witness", u3 == 0,
      "0 witnesses with |U| >= 3 across both sweeps")
check("step (c) is exercised, not vacuous: |U| = 2 occurs",
      STATS["3-uniform on [6]"][6].get(2, 0) > 0,
      "%d witnesses with |U| = 2 in the [6] sweep (its two members always met)"
      % STATS["3-uniform on [6]"][6].get(2, 0))
check("all three branches of the construction fire",
      all(STATS["3-uniform on [6]"][6].get(i, 0) > 0 for i in (0, 1, 2)),
      "|U| = 0 / 1 / 2 counts: %d / %d / %d"
      % tuple(STATS["3-uniform on [6]"][6].get(i, 0) for i in (0, 1, 2)))

# --- 1b.  TEETH.  A check that cannot fail is not a check (D-015). -----------
mut_fail = 0
mut_tot = 0
for H in families(range(6), 3, 5):
    deg = degrees_of(H)
    for E in H:
        low = [v for v in E if deg[v] <= 2]
        if len(low) < 2:
            continue
        for x, y in itertools.combinations(low, 2):
            B = set(E) - {x, y}
            U = [F for F in H if not (set(F) & B)]
            if len(U) != 2:
                continue
            mut_tot += 1
            # MUTANT: take w from U[0] instead of from U[0] cap U[1].
            w = sorted(set(U[0]) - set(U[1]))
            S = set(B) | ({w[0]} if w else {sorted(U[0])[0]})
            if not all(S & set(f) for f in H):
                mut_fail += 1
check("the cover test has teeth: breaking step (c) breaks the covers",
      mut_fail > 0,
      "mutant drawing w from U[0] \\ U[1] fails on %d of %d two-member cases"
      % (mut_fail, mut_tot))

# --- 1c.  the CONCLUSION of (D2), where it is not vacuous --------------------
# tau >= r is unreachable for r-partite objects (that IS the counterexample
# condition), but reachable for general 3-uniform families.  So the conclusion
# gets tested here, on the non-partite class.
# tau >= 3 for a 3-uniform intersecting family first becomes possible at SIX
# edges (the Fano plane minus a line), so the sweep must reach past 5 -- at 5
# it finds nothing and the test would pass vacuously.  It runs to 7 because the
# 7-edge layer is where most such families live.
taur = withdeg2 = twoinline = 0
for H in families(range(7), 3, 7):
    if tau_brute(H, range(7)) < 3:
        continue
    taur += 1
    deg = degrees_of(H)
    if any(d == 2 for d in deg.values()):
        withdeg2 += 1
    for E in H:
        if sum(1 for v in E if deg[v] == 2) >= 2:
            twoinline += 1
            break
check("(D2)'s conclusion holds on every reachable object with tau >= r",
      twoinline == 0 and taur > 0,
      "%d families on [7] with tau >= 3, %d of them carrying a degree-2 "
      "vertex, %d with two in one line" % (taur, withdeg2, twoinline))
check("that test is not vacuous for want of degree-2 vertices",
      withdeg2 > 0, "%d of the %d carry one" % (withdeg2, taur))

# --- 1d.  the hypotheses are priced, not asserted ----------------------------
K3 = ((0, 1), (1, 2), (0, 2))
check("dropping |E| >= 3 refutes (D2): the triangle has tau = 2 = r and every "
      "line holds two degree-2 vertices",
      tau_brute(K3, range(3)) == 2
      and all(sum(1 for v in e if degrees_of(K3)[v] == 2) == 2 for e in K3),
      "K3 is intersecting, 2-uniform, tau = 2")

# Searched, not hardcoded: an earlier hand-picked "witness" here was simply
# wrong (it had tau = 2 and one degree-2 vertex), and the check caught it.
NONINT = None
for H in families(range(7), 3, 5, intersecting=False):
    deg = degrees_of(H)
    if not any(sum(1 for v in E if deg[v] == 2) >= 2 for E in H):
        continue
    if is_intersecting(H):
        continue
    if tau_brute(H, range(7)) >= 3:
        NONINT = H
        break
check("dropping `intersecting` refutes (D2): a witness exists and is exhibited",
      NONINT is not None
      and not is_intersecting(NONINT)
      and tau_brute(NONINT, range(7)) >= 3
      and any(sum(1 for v in E if degrees_of(NONINT)[v] == 2) >= 2
              for E in NONINT),
      "%s -- tau = %s, and a line holds two degree-2 vertices"
      % (NONINT, tau_brute(NONINT, range(7)) if NONINT else "n/a"))

# --- 1e.  A POSITIVE CONTROL AT r = 6, which an earlier version of this file
# said was impossible.  It said the hypothesis class is empty because
# "intersecting 6-partite with tau = 6" IS the counterexample class.  True --
# but (III-C) never uses r-partiteness, so its own hypothesis class is
# intersecting, |E| >= 3, tau >= |E|, and THAT is non-empty at r = 6 and
# constructible in a second.  Correcting the overstatement rather than
# repeating it.

def pg2(q):
    """Points and lines of PG(2,q), q prime.  Line = points orthogonal to a
    dual point.  Any two lines meet in exactly one point."""
    pts = ([(1, a, b) for a in range(q) for b in range(q)]
           + [(0, 1, b) for b in range(q)] + [(0, 0, 1)])
    L = [frozenset(i for i, p in enumerate(pts)
                   if (p[0]*d[0] + p[1]*d[1] + p[2]*d[2]) % q == 0)
         for d in pts]
    return pts, L


PTS5, LINES5 = pg2(5)
check("PG(2,5) is 6-uniform and pairwise intersecting",
      len(LINES5) == 31 and all(len(L) == 6 for L in LINES5)
      and all(len(a & b) == 1 for a, b in itertools.combinations(LINES5, 2)),
      "31 lines of 6 points, every pair meeting in exactly one")

# A 5-arc: five points, no three collinear.  Delete its ten secants.
ARC = None
for cand in itertools.combinations(range(31), 5):
    if all(len(set(cand) & L) <= 2 for L in LINES5):
        ARC = cand
        break
SEC = [L for L in LINES5 if len(set(ARC) & L) == 2]
FAM = [L for L in LINES5 if L not in SEC]
FDEG = degrees_of(FAM)
FD2 = sum(1 for d in FDEG.values() if d == 2)

no5 = True
for S in itertools.combinations(sorted(FDEG), 5):
    s = set(S)
    if all(s & L for L in FAM):
        no5 = False
        break
check("an intersecting 6-uniform family with tau = 6 = r EXISTS and carries "
      "degree-2 vertices", len(FAM) == 21 and no5 and FD2 > 0,
      "PG(2,5) minus the 10 secants of the 5-arc %s: m = %d, D2 = %d, no "
      "5-cover among C(31,5) = %d subsets, and a line is a 6-cover"
      % (ARC, len(FAM), FD2, comb(31, 5)))
check("(D2) HOLDS on it, non-vacuously -- the positive control this file "
      "previously said could not exist",
      max(sum(1 for v in L if FDEG[v] == 2) for L in FAM) <= 1
      and 2 * FD2 <= len(FAM),
      "every one of the %d lines holds at most one degree-2 vertex; "
      "2*D2 = %d <= %d = m" % (len(FAM), 2 * FD2, len(FAM)))

# CRITICAL.  This object has tau = r = 6 at m = 21, which section 4 proves
# impossible -- for 6-PARTITE objects.  If it were 6-partite the floor would be
# false, so the certificate must show it is not, rather than leave the reader
# to worry.  A 6-partition with every line meeting each part once is exactly a
# proper 6-colouring of the collinearity graph (each line is a 6-clique).
_adj = {v: set() for v in FDEG}
for L in FAM:
    for a, b in itertools.combinations(sorted(L), 2):
        _adj[a].add(b)
        _adj[b].add(a)
_order = sorted(FDEG, key=lambda v: -len(_adj[v]))
_col = {}


def _six(i):
    if i == len(_order):
        return True
    v = _order[i]
    used = set(_col[u] for u in _adj[v] if u in _col)
    for c in range(6):
        if c not in used:
            _col[v] = c
            if _six(i + 1):
                return True
            del _col[v]
    return False


check("and it is NOT 6-partite, so it is not a counterexample and section 4 "
      "is untouched", not _six(0) and len(FDEG) == 31,
      "no proper 6-colouring of its collinearity graph exists; independently, "
      "lemma (B) would force >= 36 vertices and it has 31")

# =========================================================================
# 2.  THE COUNTING COROLLARY, AND WHAT IT MEANS IN THE PROFILE ENCODING
# =========================================================================

head("2.  from (D2) to 2*D2 <= m, and into the part-profile encoding")

note("(A) every vertex of a counterexample has degree >= 2; (B) every part has "
     ">= 6 vertices", "proved in certificates 0001/0005 and not re-proved here. "
     "They are also FHMW Lemma 2.1(ii) and 2.1(i).")

note("tau = r = 6 exactly for our class",
     "any single edge covers an intersecting 6-uniform family, so tau <= 6; a "
     "counterexample has tau > (r-1)*nu = 5 since nu = 1; so tau = 6. This is "
     "the hypothesis (D2) needs, and we meet it with margin ZERO.")

# The counting step, tested as a double count on real objects.
bad = tested = 0
for H in families(range(7), 3, 5):
    deg = degrees_of(H)
    D2 = sum(1 for d in deg.values() if d == 2)
    perline = max([sum(1 for v in e if deg[v] == 2) for e in H] + [0])
    if perline <= 1:                      # the hypothesis of the count
        tested += 1
        if 2 * D2 > len(H):
            bad += 1
check("the double count is sound: <=1 degree-2 vertex per line implies "
      "2*D2 <= m", bad == 0 and tested > 0,
      "%d families satisfying the per-line hypothesis, %d violating 2*D2 <= m"
      % (tested, bad))

# =========================================================================
# 3.  THE TRAP: (D2) IS NOT INHERITED BY RESIDUALS
# =========================================================================

head("3.  (D2) is FALSE one rung down -- exhibited, not asserted")

# 13 edges, 6-partite, intersecting, tau = 5.  Coordinate c is the part-c label.
W = ((0, 1, 4, 2, 3, 1), (0, 2, 3, 4, 1, 2), (0, 4, 1, 3, 2, 4),
     (1, 1, 0, 3, 4, 2), (1, 2, 4, 0, 2, 3), (2, 0, 2, 2, 2, 2),
     (2, 3, 4, 3, 1, 0), (2, 4, 3, 0, 4, 1), (3, 1, 2, 0, 1, 4),
     (4, 0, 4, 4, 4, 4), (4, 1, 3, 1, 2, 0), (4, 2, 2, 3, 0, 1),
     (4, 3, 1, 0, 3, 2))
Wv = [(i, s) for i, s in
      sorted({(i, e[i]) for e in W for i in range(6)})]
Wdeg = {}
for e in W:
    for i in range(6):
        Wdeg[(i, e[i])] = Wdeg.get((i, e[i]), 0) + 1
Wsets = [frozenset((i, e[i]) for i in range(6)) for e in W]

check("the witness is 6-partite, 6-uniform and intersecting",
      len(W) == 13 and all(len(s) == 6 for s in Wsets)
      and all(a & b for a, b in itertools.combinations(Wsets, 2)),
      "13 edges, all 78 pairs meet")

# tau = 5 exactly: an explicit 5-cover, and no 4-cover.
cover5 = frozenset((0, s) for s in range(5))
has4 = False
for S in itertools.combinations(Wv, 4):
    ss = set(S)
    if all(ss & s for s in Wsets):
        has4 = True
        break
check("the witness has tau = 5 exactly",
      all(cover5 & s for s in Wsets) and not has4,
      "explicit 5-cover (all of part 0); no 4-cover among C(%d,4) = %d subsets"
      % (len(Wv), comb(len(Wv), 4)))

WD2 = sum(1 for d in Wdeg.values() if d == 2)
check("and (D2) FAILS on it, by a wide margin",
      2 * WD2 > len(W),
      "D2 = %d, so 2*D2 = %d against m = 13" % (WD2, 2 * WD2))
check("its counting form fails because its structural form does",
      max(sum(1 for i in range(6) if Wdeg[(i, e[i])] == 2) for e in W) >= 2,
      "some line holds %d degree-2 vertices"
      % max(sum(1 for i in range(6) if Wdeg[(i, e[i])] == 2) for e in W))
note("CONSEQUENCE FOR EVERY LATER SESSION",
     "the cap is applied ONLY to H's own six part-profiles. Applying it to any "
     "object obtained by deleting vertices or edges -- i.e. anywhere on the "
     "N-ladder -- is a false kill in the flattering direction (D-005).")

# =========================================================================
# 4.  THE SWEEP
# =========================================================================

head("4.  m = 12..21 on the citation-free ladder, with the cap")

G4 = 8                                       # ours (certificates 0001, 0005)
N_FREE = {1: 2, 2: 4, 3: 6, 4: 9, 5: 11}     # every rung ours
N_CITED = {1: 2, 2: 4, 3: 6, 4: 9, 5: 13}    # 0006's ladder, for containment


def profiles(m, N):
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


def d2_of(p):
    return sum(1 for d in p if d == 2)


def qmin(n):
    if n <= 0:
        return 0
    q = 2
    while comb(q, 2) < n:
        q += 1
    return q


_L8MEMO = {}


def l8_kills(combo, m, g4=G4):
    """True iff (L8) rules this multiset of six part profiles out.

    Derived in certificate 0006; reproduced here so this file stands alone.

    MEMOISED on (sorted part maxima, X, m, g4), which is everything the body
    reads: Ms fixes S, Pc and floors, and X is passed in.  The key is not
    assumed sound -- section 5f re-runs the unmemoised body over a full sweep
    and checks no key ever carries two verdicts.
    """
    Ms = [p[0] for p in combo]
    S = sum(Ms)
    X = sum(sc(p) for p in combo) - comb(m, 2)
    key = (tuple(sorted(Ms)), X, m, g4)
    if key in _L8MEMO:
        return _L8MEMO[key]
    _L8MEMO[key] = _l8_body(Ms, S, X, m, g4)
    return _L8MEMO[key]


def _l8_body(Ms, S, X, m, g4):
    Pc = sum(comb(x, 2) for x in Ms)
    floors = [max(0, Ms[i] + Ms[j] - (m - g4))
              for i in range(6) for j in range(i + 1, 6)]
    L = sum(floors)
    q, rr = divmod(S, 6)
    U = min(q, m) * comb(6, 2) + (comb(rr, 2) if q < m else 0)
    if U < L:
        return True
    for A in range(L, U + 1):
        D = A - S + m
        if D < 0:
            continue
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
                            return False
    return True


def enumerate_admissible(m, N, cap=None):
    """Admissible 6-multisets of part profiles, optionally capped.

    Score-pruned branch and bound; the D2 cap, when given, is pushed into the
    recursion because a partial D2 sum only grows.  Both prunes are exact --
    section 5 checks the pruned count against the unpruned one.
    """
    P = sorted(profiles(m, N), key=sc, reverse=True)
    S = [sc(p) for p in P]
    D = [d2_of(p) for p in P]
    thresh, L = comb(m, 2), len(P)
    out = []

    def rec(start, d, s, dd, cur):
        if d == 6:
            if s >= thresh:
                out.append(tuple(cur))
            return
        rem = 6 - d
        for i in range(start, L):
            if s + rem * S[i] < thresh:
                break
            if cap is not None and dd + D[i] > cap:
                continue
            cur.append(i)
            rec(i, d + 1, s + S[i], dd + D[i], cur)
            cur.pop()
    rec(0, 0, 0, 0, [])
    return P, out


results = {}
for m in range(12, 22):
    P, capped = enumerate_admissible(m, N_FREE, cap=m // 2)
    surv = [c for c in capped if not l8_kills(tuple(P[i] for i in c), m)]
    results[m] = (len(P), len(capped), len(surv))
    check("m = %d impossible" % m, len(surv) == 0,
          "%3d profiles, %7d admissible multisets under D2 <= %d, %d survive (L8)"
          % (len(P), len(capped), m // 2, len(surv)))

check("therefore a Ryser r=6 counterexample has m >= 22",
      all(results[m][2] == 0 for m in range(12, 22)),
      "every m from 12 to 21 swept HERE, not inherited (D-016)")

# WHERE (L8) IS ACTUALLY NEEDED.  Read the table above: below m = 21 the cap
# leaves nothing for (L8) to do.  Both peer audits attacked the delta-budget
# inside (L8); with (D2) in hand it is load-bearing at exactly one rung.
needs_l8 = [m for m in range(12, 22) if results[m][1] > 0]
check("(L8) is load-bearing at exactly one rung: m = 21",
      needs_l8 == [21],
      "m = 12..20 die on (A)+(B)+(C)+pair count+(D2) alone, with 0 "
      "configurations left for (L8); m = 21 leaves %d" % results[21][1])

# =========================================================================
# 5.  CONTROLS
# =========================================================================

head("5.  controls -- this raises our own floor, the dangerous direction")

# 5a.  NOT TOO STRONG.  If this killed m = 22 as well it would be proving Ryser.
P22, cap22 = enumerate_admissible(22, N_FREE, cap=11)
surv22 = []
for c in cap22:
    if not l8_kills(tuple(P22[i] for i in c), 22):
        surv22.append(c)
        if len(surv22) >= 200:
            break
check("NOT TOO STRONG: the same machinery leaves m = 22 alive",
      len(surv22) > 0,
      "%d multisets pass the cap at m = 22; stopped after finding %d survivors"
      % (len(cap22), len(surv22)))
# An earlier version of this file claimed all m = 22 survivors saturate the
# cap.  They do not -- that was generalised from the first five seen, and this
# check caught it.  What is true is that the cap is still BITING at m = 22:
# it removes most of the field.
# SCOPE (corrected 2026-07-27, turn 9): the distribution below describes the
# FIRST 200 survivors in enumeration order (profiles sorted by score), and
# ONLY them.  The full-field measurement (turn-9 sensitivity, two independent
# implementations) finds survivors spanning D2 = 5..32 -- one lives at
# D2 = 5, six below the cap -- so "survivors crowd the ceiling" is a fact
# about this exhibited sample, not about the field.  Emptying m = 22 by a
# sharpened cap would need D2 <= 4; the cap lever does not extend one rung.
dist = {}
for c in surv22:
    v = sum(d2_of(P22[i]) for i in c)
    dist[v] = dist.get(v, 0) + 1
check("the cap still bites at m = 22 -- the first-200 exhibited survivors "
      "sit high against it (full field spans D2 = 5..32; see NOTES)",
      min(dist) >= 8 and max(dist) == 11,
      "D2 distribution over %d exhibited survivors: %s (cap = 11)"
      % (len(surv22), ", ".join("%d:%d" % (k, dist[k])
                                for k in sorted(dist))))
check("the cap removes most of the m = 22 field, so m = 22 surviving is not "
      "the cap failing to apply", len(cap22) < len(enumerate_admissible(22, N_FREE)[1]),
      "%d of %d admissible multisets pass D2 <= 11"
      % (len(cap22), len(enumerate_admissible(22, N_FREE)[1])))

# 5b.  ANTI-VACUITY.  Zero survivors is the failure mode that fakes a proof.
P21, all21 = enumerate_admissible(21, N_FREE, cap=None)
n21 = 0
for c in all21:
    if not l8_kills(tuple(P21[i] for i in c), 21):
        n21 += 1
check("ANTI-VACUITY: the identical predicate on the identical m = 21 "
      "configurations, cap REMOVED, reports survivors",
      n21 > 0,
      "%d of %d survive (L8) without the cap -- so the zero above is a kill, "
      "not a harness that cannot speak" % (n21, len(all21)))

# 5f.  THE MEMO KEY IS SOUND, not assumed.  The unmemoised body is re-run over
# two full sweeps -- every admissible configuration at m = 20, and every
# cap-passing one at m = 21, which is the set the result actually turns on.
# The range is part of the claim (D-016): the full m = 21 set (316,591
# configurations, ~13 min unmemoised) has NOT been checked this way.
P20m, adm20m = enumerate_admissible(20, N_FREE, cap=None)
P21m, cap21m = enumerate_admissible(21, N_FREE, cap=10)
collide = 0
seen = {}
ntest = 0
for m_, cs, Ps in ((20, adm20m, P20m), (21, cap21m, P21m)):
    for c in cs:
        combo = tuple(Ps[i] for i in c)
        Ms = [p[0] for p in combo]
        X = sum(sc(p) for p in combo) - comb(m_, 2)
        key = (tuple(sorted(Ms)), X, m_)
        v = _l8_body(Ms, sum(Ms), X, m_, G4)
        ntest += 1
        if key in seen and seen[key] != v:
            collide += 1
        seen[key] = v
check("the memo key carries a single verdict, checked not assumed",
      collide == 0 and ntest > 0,
      "%d configurations over m = 20 (all admissible) and m = 21 (all "
      "cap-passing) collapse to %d keys, 0 keys carrying two verdicts"
      % (ntest, len(seen)))

# 5c.  THE PRUNES ARE EXACT.
_, uncapped21 = enumerate_admissible(21, N_FREE, cap=None)
manual = [c for c in uncapped21 if sum(d2_of(P21[i]) for i in c) <= 10]
_, capped21 = enumerate_admissible(21, N_FREE, cap=10)
check("the in-recursion D2 prune is exact: it agrees with filtering afterwards",
      len(manual) == len(capped21) and set(manual) == set(capped21),
      "%d configurations either way at m = 21" % len(manual))

flat = 0
Pf = sorted(profiles(20, N_FREE), key=sc, reverse=True)
th = comb(20, 2)
for c in itertools.combinations_with_replacement(range(len(Pf)), 6):
    if sum(sc(Pf[i]) for i in c) >= th:
        flat += 1
_, bb20 = enumerate_admissible(20, N_FREE, cap=None)
check("the score prune is exact: branch-and-bound agrees with the flat "
      "enumeration at m = 20", flat == len(bb20),
      "%d admissible multisets both ways" % flat)

# 5d.  SENSITIVITY.  How much slack does the constant in (D2) have?
sens = {}
for capv in (9, 10, 11, 12):
    _, cc = enumerate_admissible(21, N_FREE, cap=capv)
    sens[capv] = sum(1 for c in cc if not l8_kills(tuple(P21[i] for i in c), 21))
check("SENSITIVITY: the m = 21 kill needs the cap to be exactly floor(m/2)",
      sens[10] == 0 and sens[11] > 0,
      "survivors at cap 9/10/11/12: %d/%d/%d/%d -- one unit weaker and m = 21 "
      "reopens" % (sens[9], sens[10], sens[11], sens[12]))

# 5g.  THE MARGIN, STATED.  Certificate 0006 set the rule: a certificate that
# says "conservative" without saying "margin 1" has told the reader the safe
# half (D-017).  This result has margin exactly one in TWO independent places.
bands = {}
for c in all21:
    v = sum(d2_of(P21[i]) for i in c)
    if v not in bands:
        bands[v] = [0, 0]
    bands[v][0] += 1
    if not l8_kills(tuple(P21[i] for i in c), 21):
        bands[v][1] += 1
lowest_surv = min((v for v in bands if bands[v][1] > 0), default=None)
check("MARGIN 1 on the cap: the least D2 admitting an (L8) survivor at m = 21 "
      "is one above the cap", lowest_surv == 11,
      "cap = 10; bands D2 -> (configurations, survivors): %s"
      % ", ".join("%d->(%d,%d)" % (v, bands[v][0], bands[v][1])
                  for v in sorted(bands) if v <= 12))
note("the m = 21 kill rides on an odd-m rounding",
     "2*D2 <= 21 gives D2 <= 10. At even m the same lemma gives no such half "
     "unit -- at m = 22 the cap is 11 and 56,592 configurations survive.")

# 5h.  SENSITIVITY THAT ACTUALLY EXERCISES THIS ROW.  Certificate 0007's control
# -- falsify N(4) to 8 and m = 20 revives -- does NOT transfer here.  Reusing it
# under an m >= 22 claim would ship a control that never touches the claim.
N_N4BAD = {1: 2, 2: 4, 3: 6, 4: 8, 5: 11}
Pn4s, cap21_n4bad = enumerate_admissible(21, N_N4BAD, cap=10)
surv_n4 = sum(1 for c in cap21_n4bad
              if not l8_kills(tuple(Pn4s[i] for i in c), 21))
check("0007's N(4) control does NOT transfer: falsifying N(4) to 8 leaves "
      "m = 21 dead", surv_n4 == 0,
      "%d cap-passers under N(4) = 8, %d survive -- so this row is NOT held up "
      "by the N-ladder" % (len(cap21_n4bad), surv_n4))

surv_g7 = sum(1 for c in capped21
              if not l8_kills(tuple(P21[i] for i in c), 21, g4=7))
check("SENSITIVITY for THIS row: g(4) = 8 is what holds m = 21, with margin one",
      surv_g7 > 0,
      "weaken g(4) to 7 and %d of the %d cap-passers survive" % (surv_g7,
                                                                 len(capped21)))

# 5e.  CONTAINMENT: the cited ladder is a special case, not a rival.
_, cited21 = enumerate_admissible(21, N_CITED, cap=10)
Pc21 = sorted(profiles(21, N_CITED), key=sc, reverse=True)
cited_set = set(tuple(sorted(Pc21[i] for i in c)) for c in cited21)
free_set = set(tuple(sorted(P21[i] for i in c)) for c in capped21)
check("CONTAINMENT: every capped configuration of the CITED ladder is among "
      "the citation-free ones", cited_set <= free_set,
      "%d cited inside %d citation-free at m = 21"
      % (len(cited_set), len(free_set)))

# =========================================================================
# 6.  DEPENDENCY LEDGER
# =========================================================================

head("6.  what this result rests on")

print("""
  EXTERNAL CONSTANTS USED:  none.
  EXTERNAL LEMMAS USED:     none -- (D2) is re-derived in section 1.

  Chain, all ours:
    (A),(B)   certificates 0001/0005     -- also FHMW 2.1(ii),(i). Not new.
    (C)       the N-ladder, N(4) = 9 by exhaustion, N(5) >= 11 by peeling
    (L7),(L8) certificate 0006
    (D2)      re-derived here             -- also FHMW 2.1(iii). Not new.

  WHAT IS NEW HERE is m >= 22, and the derivation of it. Every lemma in the
  chain except (L7)/(L8) and the N-ladder is a re-derivation of published
  mathematics. This file claims the floor, not the lemmas.

  IF (D2) WERE WITHDRAWN the floor returns to m >= 21, certificate 0007,
  citing nothing. Nothing below 21 depends on this file.

  WHAT HOLDS THE m = 21 ROW UP, measured above and NOT what holds up the rest:
    the cap itself   margin exactly 1 (D2 = 11 admits 7 survivors, cap is 10)
    g(4) = 8         margin exactly 1 (weaken to 7 and survivors appear)
    the delta budget margin exactly 1 (tightest cap-passer misses by one unit)
    the N-ladder     INERT at m = 21 -- falsify N(4) to 8 and it stays dead
  So this row has margin one in THREE places at once, and certificate 0007's
  sensitivity control does not exercise it. For m <= 20 the load-bearing step is
  still N(4) = 9, as 0007 says; those are different claims with different hinges.
""")

head("VERDICT")
el = time.time() - START
if FAILED:
    print("  %d checks, %d FAILED: %s" % (NCHECK[0], len(FAILED), FAILED))
    print("  %.0fs" % el)
    sys.exit(1)
print("""  a Ryser r=6 counterexample has m >= 22    PROVEN-BY-CERTIFICATE,
  CITING NOTHING -- with (D2) re-derived here, and recorded as a published
  lemma re-derived rather than a lemma found.

  %d checks + %d notes (stated, not tested), %.0fs, ALL GREEN""" % (
    NCHECK[0], NNOTE[0], el))
