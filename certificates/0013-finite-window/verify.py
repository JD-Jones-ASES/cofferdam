#!/usr/bin/env python3
"""Certificate 0013 -- the finite window: every critical core has m in [22, 462].

    python3 verify.py

Stdlib only.  Exact integer/rational arithmetic.  No solver.  No imports
from lib/.  Runs under Python 3.9 and under python3 -O.  Deterministic.

WHAT IS CLAIMED
---------------
  THE CEILING: every edge-critical counterexample ("critical core") to
  Ryser r = 6 intersecting has                            PROVEN-BY-CERTIFICATE;
      m(K) <= C(11,6) = 462                               ledger EMPTY -- no
                                                          external inputs, and no
                                                          in-house certificate
                                                          inputs either
  THE WINDOW: with the in-house floor (m >= 22 for ALL
  counterexamples, certificates 0005/0008/0009/0010/0012):
      every critical core has m(K) in [22, 462], and
      Ryser r = 6 intersecting  <=>  no critical core     PROVEN-BY-CERTIFICATE
      with m in [22, 462]                                 (floor half in-house)

  ANNEX (context, not chain): the truncated PG(2,5) built in section 6 has
  tau* = nu* = 5 -- the machine record of the turn-9 kill of the false
  claim "tau* <= r/2 for r-partite intersecting hypergraphs".

THE PROOF
---------
Throughout, a counterexample is a FINITE 6-partite 6-uniform intersecting
hypergraph H with tau(H) > 5, taken as a set of edges (no multi-edges);
covers may use any vertices of H.  (Ryser's conjecture is a statement
about finite hypergraphs; every floor certificate quantifies over m.)

  (0) tau(H) <= 6 always: the six vertices of any single edge form a
      cover, because H is intersecting.  So a counterexample has
      tau(H) = 6 exactly.
  (1) CORE EXTRACTION.  Delete edges one at a time as long as tau stays 6;
      m is finite and strictly decreasing, so this terminates at an
      edge-minimal K with tau(K) = 6.  K is 6-partite 6-uniform on the
      same parts and intersecting (a subfamily), so K is itself a
      counterexample; and K is edge-critical: deleting an edge cannot
      RAISE tau (any cover of K covers K - e), so at termination
      tau(K - e) < 6 for every e.
  (2) FLOOR.  K is a counterexample, and the in-house floor quantifies
      over ALL counterexamples: m(K) >= 22.
  (3) PRIVATE COVERS.  Fix e in K.  tau(K - e) <= 5 by criticality, and
      tau(K - e) >= tau(K) - 1 = 5, because a cover of K - e together
      with any one vertex of e covers K.  So tau(K - e) = 5 exactly; fix
      a minimum cover T_e of K - e, |T_e| = 5.  Minimality also puts T_e
      inside V(K): a vertex of T_e meeting no edge of K - e could be
      dropped, leaving a 4-cover of K - e -- so T_e is contained in
      V(K - e), a subset of V(K), and step (4)'s ground set holds every
      T_e.
      (3a) e cap T_e = empty: otherwise T_e meets e as well as every edge
           of K - e, i.e. T_e is a 5-cover of K -- contradicting
           tau(K) = 6.
      (3b) for f != e: e cap T_f != empty, because e is an edge of K - f
           and T_f covers K - f.
  (4) THE PERMUTATION BOUND.  Order the vertices of K uniformly at
      random.  For e in K let A_e be the event that every vertex of e
      precedes every vertex of T_e.  The 11 vertices of e cup T_e are
      distinct (an edge has 6 distinct vertices, one per part; |T_e| = 5;
      (3a)), and the relative order of 11 fixed distinct elements is
      uniform over 11! arrangements, of which 6!*5! put all of e first:
          P(A_e) = 6!*5!/11! = 1/C(11,6) = 1/462.
      The events are PAIRWISE DISJOINT: for e != f pick x in f cap T_e
      and y in e cap T_f (nonempty by (3b)); x != y, since x in T_e,
      y in e, and e cap T_e = empty (3a); if A_e and A_f both held, A_e
      forces y < x (y in e, x in T_e) while A_f forces x < y (x in f,
      y in T_f) -- impossible.  Disjoint events' probabilities sum to at
      most 1:  m(K) / 462 <= 1,  so  m(K) <= 462.
  (5) THE EQUIVALENCE.  If Ryser r = 6 intersecting fails, (1)-(4)
      produce a critical core with m in [22, 462].  Conversely, a
      critical core is itself a counterexample.  So the conjecture is
      EQUIVALENT to: no edge-critical counterexample has m in [22, 462].

  ROBUSTNESS.  The ceiling is not knife-edge in the cover size: with
  b_e := |T_e| <= 5 the same argument gives P(A_e) = 1/C(6+b_e, 6)
  >= 1/462 (the table C(6+b, 6) = 1, 7, 28, 84, 210, 462 for b = 0..5 is
  increasing -- checked in section 7), and the disjointness proof uses
  only (3a)/(3b), never the sizes, so mixed b_e are fine.  What the
  bound cannot survive is losing the ambient structure: the size cap
  b_e <= 5 comes from criticality (tau(K - e) < tau(K)), and (3a)'s
  disjointness from tau(K) = 6 -- the counterexample status itself.  For
  a non-critical counterexample nothing here bounds m -- see SCOPE.

SCOPE, STATED WITH CARE
-----------------------
The window quantifies over CRITICAL CORES.  The floor certificates
quantify over ALL counterexamples -- strictly stronger, and exactly what
step (2) consumes; the ceiling is a cores-only statement, and section 5/6
below exhibit real objects (one rung down) that are NOT critical and
where the private-cover construction has no purchase until the greedy
core is extracted.  Finite-search consequence: a critical core has at
most 462 edges and (dropping vertices of degree 0) at most 6*462 = 2772
vertices, so Ryser r = 6 intersecting is equivalent to one finite --
astronomically large, but finite -- check.

ATTRIBUTION (recorded, not consumed)
------------------------------------
The set-pair inequality behind (4) is classical (Bollobas 1965); bounding
tau-critical hypergraphs by set-pair systems is also classical (Tuza).
The proof above is re-derived from first principles and machine-checked
below, so the certificate stands without any citation; the attribution is
recorded in NOTES.md and the turn-10 notebook entry (the literature
sweep), because a result must never look more novel than it is.  What is
ours is the WINDOW: the composition with the in-house floor, both ends
now certified.

THE LEDGER, in full
-------------------
  CEILING m(K) <= 462          EXTERNAL INPUTS -- NONE.
                               IN-HOUSE CERTIFICATE INPUTS -- NONE.
  FLOOR m(K) >= 22             in-house, the pinned-ladder chain stated
                               TRANSITIVELY (0012's ledger is the
                               authority): certificates 0005 (ladder +
                               (A)(B)(C)), 0006 ((L7)), 0008 ((D2)),
                               0009 (N(5)), 0010 (N(4) by hand), 0011
                               ((L10)'s Delta <= 4), 0012 (the m = 21
                               kill).  0007 remains the weak-ladder
                               record, not consumed here.
                               EXTERNAL INPUTS -- NONE.
  CONTROL-ONLY                 0009's g(5) = 13 -- its GENERAL-class rung
                               (g, not the full-part N; 0009 proves
                               g(5) = N(5) = 13) -- is consumed by ONE
                               consistency check in section 6: the
                               extracted tau = 5 rehearsal core must have
                               >= 13 edges.  A cross-check on a rehearsal
                               object, fail-safe by construction: an
                               error there could only redden this
                               certificate, never wrongly green the
                               ceiling.  (0009 is separately a floor
                               input via the pinned ladder, listed
                               above.)
"""

import itertools
import sys
import time
from fractions import Fraction
from math import comb, factorial

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


# ==========================================================================
# 1.  The number 462
# ==========================================================================

head("1.  the number 462")

check("C(11,6) = 462", comb(11, 6) == 462)
check("6! * 5! * 462 = 11! exactly -- the probability computation is an "
      "identity, not an estimate",
      factorial(6) * factorial(5) * 462 == factorial(11))
check("the event probability 6!5!/11! is exactly 1/462 (exact rational)",
      Fraction(factorial(6) * factorial(5), factorial(11)) == Fraction(1, 462))
check("a!b!/(a+b)! = 1/C(a+b,a) -- the two forms of the bound agree at "
      "(a,b) = (6,5)",
      Fraction(factorial(6) * factorial(5), factorial(11))
      == Fraction(1, comb(11, 6)))

# ==========================================================================
# 2.  The probability lemma, exhaustively at small scale
# ==========================================================================

head("2.  P(all of A before all of B) = a!b!/(a+b)!, by exhaustion")


def event_count(n, A, B):
    """Number of the n! orders of range(n) with all of A before all of B."""
    cnt = 0
    for perm in itertools.permutations(range(n)):
        pos = {}
        for i, v in enumerate(perm):
            pos[v] = i
        if max(pos[a] for a in A) < min(pos[b] for b in B):
            cnt += 1
    return cnt


ok_all = True
detail = []
for (a, b, extra) in ((2, 1, 2), (2, 2, 2), (3, 2, 2), (4, 3, 2), (5, 4, 0)):
    n = a + b + extra
    got = event_count(n, tuple(range(a)), tuple(range(a, a + b)))
    want = factorial(n) * Fraction(factorial(a) * factorial(b),
                                   factorial(a + b))
    detail.append("(%d,%d) in %d! -> %d" % (a, b, n, got))
    if Fraction(got) != want:
        ok_all = False
check("the event count is exactly n! * a!b!/(a+b)! -- five shapes "
      "exhausted, through all 9! = 362,880 orders, three of them on "
      "STRICTLY LARGER ground sets",
      ok_all, "; ".join(detail))
note("the (6,5) instance the theorem consumes is the same one-line "
     "formula; its arithmetic 6!*5!*462 = 11! is check 2, and exhausting "
     "11! = 39.9M orders adds nothing the five shapes above do not "
     "already test")
check("embedding independence: (a,b) = (3,2) gives the same fraction 1/10 "
      "of orders on 5 elements and on 7 -- only the RELATIVE order of the "
      "a+b elements matters",
      Fraction(event_count(5, (0, 1, 2), (3, 4)), factorial(5))
      == Fraction(event_count(7, (0, 1, 2), (3, 4)), factorial(7))
      == Fraction(1, 10))

# ==========================================================================
# 3.  Disjointness, exhaustively -- and its teeth
# ==========================================================================

head("3.  disjoint events: the mechanism, enacted and then broken")

# The complement witness on [5], (a,b) = (3,2): all C(5,3) = 10 pairs
# (A, [5] \ A).  Cross-intersecting both ways: A_i cap B_j != empty for
# i != j because two distinct 3-subsets of a 5-set cannot be disjoint from
# each other's complement (that would force A_i inside A_j).
W5 = []
for A in itertools.combinations(range(5), 3):
    W5.append((frozenset(A), frozenset(range(5)) - frozenset(A)))
cond = len(W5) == 10
for i, (A, B) in enumerate(W5):
    if A & B:
        cond = False
    for j, (A2, B2) in enumerate(W5):
        if i != j and not (A & B2):
            cond = False
check("the 10-pair complement system on [5] satisfies every hypothesis: "
      "own-pair disjoint, cross-pairs meeting in BOTH directions", cond)

counts = [0] * len(W5)
overlap = 0
for perm in itertools.permutations(range(5)):
    pos = {}
    for i, v in enumerate(perm):
        pos[v] = i
    fired = []
    for i, (A, B) in enumerate(W5):
        if max(pos[x] for x in A) < min(pos[y] for y in B):
            fired.append(i)
    if len(fired) > 1:
        overlap += 1
    for i in fired:
        counts[i] += 1
check("over all 120 orders of [5], NO order lies in two events, and every "
      "event fires in exactly 120 * (1/10) = 12 orders -- the events "
      "PARTITION the space: the bound C(5,3) = 10 is met with equality",
      overlap == 0 and counts == [12] * 10,
      "this is the tightness witness in miniature")

# The same full enactment one scale up: all C(7,4) = 35 complement pairs
# on [7], all 5040 orders.
W7 = []
for A in itertools.combinations(range(7), 4):
    W7.append((frozenset(A), frozenset(range(7)) - frozenset(A)))
counts7 = [0] * len(W7)
overlap7 = 0
for perm in itertools.permutations(range(7)):
    pos = {}
    for i, v in enumerate(perm):
        pos[v] = i
    fired = []
    for i, (A, B) in enumerate(W7):
        if max(pos[x] for x in A) < min(pos[y] for y in B):
            fired.append(i)
    if len(fired) > 1:
        overlap7 += 1
    for i in fired:
        counts7[i] += 1
check("the same, one scale up: the 35-pair complement system on [7] "
      "((a,b) = (4,3)) partitions all 5040 orders into 35 events of "
      "exactly 4!3! = 144 orders each",
      overlap7 == 0 and counts7 == [144] * 35 and 35 * 144 == 5040)

# TEETH 1: break ONE cross-direction of ONE pair and the disjointness
# mechanism dies.  e1 = {1,2,3}, T1 = {4,5}; e2 = {4,6,7}, T2 = {5,8}:
# own-pairs disjoint, e2 cap T1 = {4} != empty, but e1 cap T2 = empty.
E1, T1 = frozenset((1, 2, 3)), frozenset((4, 5))
E2, T2 = frozenset((4, 6, 7)), frozenset((5, 8))
both = 0
for perm in itertools.permutations(range(1, 9)):
    pos = {}
    for i, v in enumerate(perm):
        pos[v] = i
    if (max(pos[x] for x in E1) < min(pos[y] for y in T1)
            and max(pos[x] for x in E2) < min(pos[y] for y in T2)):
        both += 1
check("TEETH: with e1 cap T2 empty (one broken cross-direction; the other "
      "direction intact) the two events OVERLAP -- in exactly 360 of the "
      "40320 orders of [8]",
      not (E1 & T1) and not (E2 & T2) and (E2 & T1) and not (E1 & T2)
      and both == 360,
      "the SYMMETRIC cross-intersection our cores provide is precisely "
      "what the disjointness argument consumes")
note("the skew set-pair bound (one direction only) is still a true theorem "
     "in the literature, by other means (exterior algebra); this "
     "certificate neither uses nor certifies it -- our cores give both "
     "directions and the elementary argument closes alone")

# TEETH 2: the probability formula needs the pair itself disjoint.
both2 = 0
for perm in itertools.permutations(range(1, 4)):
    pos = {}
    for i, v in enumerate(perm):
        pos[v] = i
    if max(pos[x] for x in (1, 2)) < min(pos[y] for y in (2, 3)):
        both2 += 1
check("TEETH: a pair with e cap T != empty has event probability 0, not "
      "a!b!/(a+b)! -- an element cannot precede itself", both2 == 0)

# ==========================================================================
# 4.  The tight witness at full scale: 462 pairs on 11 points
# ==========================================================================

head("4.  the 462-pair complement witness on [11]")

FULL11 = (1 << 11) - 1
SETS = [sum(1 << i for i in c) for c in itertools.combinations(range(11), 6)]
check("there are exactly C(11,6) = 462 six-subsets of [11]",
      len(SETS) == 462)

t0 = time.time()
cond = True
for i, S in enumerate(SETS):
    if S & (FULL11 & ~S):
        cond = False
    for j, S2 in enumerate(SETS):
        if i != j and not (S & (FULL11 & ~S2)):
            cond = False
check("every ordered cross pair meets: S_i cap complement(S_j) != empty "
      "for all i != j -- 212,982 cross checks, the substantive content "
      "(the 462 own-pair disjointness checks also run, but are "
      "definitional for complement pairs)",
      cond, "%.1fs" % (time.time() - t0))
check("closing arithmetic: 462 events, each of probability exactly 1/462 "
      "by the section-2 lemma, pairwise disjoint by the section-3 "
      "mechanism applied to check 13's cross conditions, sum to EXACTLY "
      "1 -- saturation.  (This condition is the arithmetic step only; "
      "the mechanism's load is carried by sections 2-3 and check 13)",
      sum((Fraction(1, 462) for _ in SETS), Fraction(0)) == 1)
note("NOT TOO STRONG: the ceiling argument alone cannot be pushed below "
     "462 -- this witness satisfies every hypothesis the permutation "
     "argument uses.  Any refinement (e.g. the peer-claimed 456 for "
     "6-partite cores) must consume structure this certificate does not: "
     "the partite transversal shape of the edges and the cover structure "
     "of the T_e.  Recorded in NOTES.md; not consumed here")

# ==========================================================================
# 5.  The machinery end-to-end, small: the Fano plane at tau = 3
# ==========================================================================

head("5.  Fano: extract the critical core, build the covers, enact the "
     "bound by full enumeration")

FANO = [frozenset(e) for e in
        ((0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5),
         (1, 4, 6), (2, 3, 6), (2, 4, 5))]
check("the seven Fano lines are pairwise intersecting",
      all(a & b for a, b in itertools.combinations(FANO, 2)))


def small_cover(family, k, npts):
    """Lex-first k-subset of range(npts) covering every edge, else None."""
    for c in itertools.combinations(range(npts), k):
        cs = frozenset(c)
        if all(e & cs for e in family):
            return cs
    return None


check("tau(Fano) = 3: line {0,1,2} is a 3-cover (any edge of an "
      "intersecting family is a cover) and no 2-cover exists among all "
      "C(7,2) = 21",
      all(e & FANO[0] for e in FANO) and small_cover(FANO, 2, 7) is None)

fano_core = list(FANO)
changed = True
fano_deleted = 0
while changed:
    changed = False
    for i in range(len(fano_core)):
        trial = fano_core[:i] + fano_core[i + 1:]
        if small_cover(trial, 2, 7) is None:          # tau stays 3
            fano_core = trial
            fano_deleted += 1
            changed = True
            break
check("Fano is NOT edge-critical -- the greedy (first deletable edge, "
      "rescan) removes exactly 1 edge before every remaining deletion "
      "drops tau; the critical core has 6 edges",
      fano_deleted == 1 and len(fano_core) == 6,
      "criticality is a real hypothesis, not a relabeling")
check("TEETH for criticality: on the FULL plane the private-cover "
      "construction fails outright -- deleting the greedy's first edge "
      "leaves tau = 3, so the size-2 private cover T_e that step (3) "
      "promises for a CRITICAL family does not exist here",
      small_cover(FANO[1:], 2, 7) is None,
      "the theorem's step (3) is unavailable before core extraction")

fano_pairs = []
cond = True
for i, e in enumerate(fano_core):
    rest = fano_core[:i] + fano_core[i + 1:]
    T = small_cover(rest, 2, 7)
    if T is None or small_cover(rest, 1, 7) is not None:
        cond = False                                   # tau(core - e) != 2
    if T is None or (e & T):
        cond = False                                   # (3a) fails
    fano_pairs.append((e, T))
for i, (e, _) in enumerate(fano_pairs):
    for j, (_, T2) in enumerate(fano_pairs):
        if i != j and not (e & T2):
            cond = False                               # (3b) fails
check("on the core, the theorem's steps all hold: tau(core - e) = 2 "
      "EXACTLY for every e (a 2-cover exists, no 1-cover), e cap T_e "
      "empty, and every cross pair e cap T_f nonempty",
      cond)
check("the bound: 6 = m(core) <= C(3+2, 3) = 10",
      len(fano_core) == 6 and len(fano_core) <= comb(5, 3))

counts = [0] * len(fano_pairs)
overlap = 0
for perm in itertools.permutations(range(7)):
    pos = {}
    for i, v in enumerate(perm):
        pos[v] = i
    fired = []
    for i, (e, T) in enumerate(fano_pairs):
        if max(pos[x] for x in e) < min(pos[y] for y in T):
            fired.append(i)
    if len(fired) > 1:
        overlap += 1
    for i in fired:
        counts[i] += 1
check("the WHOLE argument, enacted by brute force over all 7! = 5040 "
      "orders: no order lies in two events, and each of the 6 events "
      "fires in exactly 5040 * (3!2!/5!) = 504 orders",
      overlap == 0 and counts == [504] * 6,
      "6 disjoint events of probability 1/10: the bound m <= 10, live")

# ==========================================================================
# 6.  The machinery end-to-end, large: truncated PG(2,5) at tau = 5
# ==========================================================================

head("6.  truncated PG(2,5): a 6-partite rehearsal one rung down")


def norm(v):
    """Normalize a nonzero GF(5)^3 vector: first nonzero coordinate 1."""
    for x in v:
        if x % 5:
            inv = pow(x, 3, 5)                         # x^-1 mod 5
            return tuple((inv * y) % 5 for y in v)
    return None


PTS = sorted(set(n for n in (norm(v) for v in
                             itertools.product(range(5), repeat=3))
                 if n is not None))
LINES = list(PTS)                                      # self-dual coordinates


def on(line, pt):
    return (line[0] * pt[0] + line[1] * pt[1] + line[2] * pt[2]) % 5 == 0


check("PG(2,5) from GF(5): 31 points, 31 lines, 6 points on every line, "
      "6 lines through every point, and every two lines meet in EXACTLY "
      "one point",
      len(PTS) == 31 and len(LINES) == 31
      and all(sum(1 for q in PTS if on(l, q)) == 6 for l in LINES)
      and all(sum(1 for l in LINES if on(l, q)) == 6 for q in PTS)
      and all(sum(1 for q in PTS if on(l1, q) and on(l2, q)) == 1
              for l1, l2 in itertools.combinations(LINES, 2)))

P_DEL = (0, 0, 1)
PENCIL = [l for l in LINES if on(l, P_DEL)]
SURV = [l for l in LINES if not on(l, P_DEL)]
VERTS = sorted(q for q in PTS if q != P_DEL)
VIDX = {}
for i, q in enumerate(VERTS):
    VIDX[q] = i
EDGES = [frozenset(VIDX[q] for q in PTS if q != P_DEL and on(l, q))
         for l in SURV]
PARTS = [frozenset(VIDX[q] for q in PTS if q != P_DEL and on(l, q))
         for l in PENCIL]

check("delete the point (0,0,1) and its pencil of 6 lines: 30 vertices, "
      "25 surviving edges of 6 vertices each; the 6 pencil traces "
      "partition the vertices into parts of 5",
      len(PENCIL) == 6 and len(EDGES) == 25 and len(VERTS) == 30
      and all(len(e) == 6 for e in EDGES)
      and sorted(v for p in PARTS for v in p) == list(range(30))
      and all(len(p) == 5 for p in PARTS))
check("the truncation is 6-partite (every edge meets every part exactly "
      "once) and intersecting (every two edges share exactly one vertex)",
      all(len(e & p) == 1 for e in EDGES for p in PARTS)
      and all(len(a & b) == 1 for a, b in itertools.combinations(EDGES, 2)))

VMASK = [0] * 30
for ei, e in enumerate(EDGES):
    for v in e:
        VMASK[v] |= (1 << ei)
FULL = (1 << 25) - 1


def kcover(E, k):
    """Lex-first k-subset of vertices covering edge-mask E, else None."""
    for c in itertools.combinations(range(30), k):
        m = 0
        for v in c:
            m |= VMASK[v]
        if m & E == E:
            return c
    return None


t0 = time.time()
part0 = 0
for v in sorted(PARTS[0]):
    part0 |= VMASK[v]
check("tau = 5: any part is a 5-cover (edges are transversals), and no "
      "4-cover exists among all C(30,4) = 27,405",
      part0 & FULL == FULL and kcover(FULL, 4) is None,
      "%.1fs" % (time.time() - t0))

# --- annex: the tau* kill, machine-recorded ------------------------------
check("ANNEX: every vertex lies on exactly 5 surviving edges, so edge "
      "weights 1/5 are a feasible fractional matching of value "
      "25 * (1/5) = 5 exactly, and vertex weights 1/6 a feasible "
      "fractional cover of value 30 * (1/6) = 5 exactly, and 5 > 3 = r/2 "
      "(all in exact rationals)",
      all(bin(VMASK[v]).count("1") == 5 for v in range(30))
      and all(sum((Fraction(1, 5) for _ in range(bin(VMASK[v]).count("1"))),
                  Fraction(0)) == 1 for v in range(30))
      and all(sum((Fraction(1, 6) for _ in e), Fraction(0)) == 1
              for e in EDGES)
      and sum((Fraction(1, 5) for _ in EDGES), Fraction(0)) == 5
      and sum((Fraction(1, 6) for _ in range(30)), Fraction(0)) == 5
      and Fraction(5) > Fraction(3))
note("ANNEX (context, not chain): the machine records the two feasible "
     "LP solutions and their exact values; the last step is one line of "
     "prose -- weak LP duality (any fractional matching's value <= any "
     "fractional cover's value, by summing constraints) squeezes "
     "nu* = tau* = 5 for this 6-partite intersecting object.  The claim "
     "'tau* <= r/2 for r-partite intersecting hypergraphs' -- asserted "
     "as Fact in the turn-9 notebook section 8 -- is therefore FALSE, "
     "and its killer now lives in a green certificate")

# --- greedy critical core ------------------------------------------------
t0 = time.time()
active = list(range(25))
E = FULL
pg_deleted = 0
changed = True
while changed:
    changed = False
    for ei in list(active):
        E2 = E & ~(1 << ei)
        if kcover(E2, 4) is None:                      # tau stays 5
            active.remove(ei)
            E = E2
            pg_deleted += 1
            changed = True
            break
core = list(active)
check("the truncation is NOT edge-critical either: the greedy removes "
      "fully 11 of the 25 edges; the tau = 5 core has 14 edges, and "
      "tau(core) = 5 is re-verified from scratch (a part still covers; "
      "no 4-cover)",
      pg_deleted == 11 and len(core) == 14
      and part0 & E == E and kcover(E, 4) is None,
      "%.1fs" % (time.time() - t0))

t0 = time.time()
cond = True
TCOV = {}
for ei in core:
    E2 = E & ~(1 << ei)
    T = kcover(E2, 4)
    if T is None or kcover(E2, 3) is not None:
        cond = False                                   # tau(core - e) != 4
    TCOV[ei] = frozenset(T) if T is not None else frozenset()
    if TCOV[ei] & EDGES[ei]:
        cond = False                                   # (3a) fails
for ei in core:
    for fj in core:
        if ei != fj and not (EDGES[ei] & TCOV[fj]):
            cond = False                               # (3b) fails
check("on the 14-edge core, every step of the theorem holds: "
      "tau(core - e) = 4 EXACTLY for all 14 edges (4-cover exists, no "
      "3-cover in all C(30,3) = 4,060), e cap T_e empty, and all 182 "
      "ordered cross pairs meet",
      cond, "%.1fs" % (time.time() - t0))
check("the window analog, both ends live: 13 <= 14 = m(core) <= "
      "C(6+4, 6) = 210 -- the LOWER end is certificate 0009's "
      "g(5) = 13, its GENERAL-class rung (0009 proves g(5) = N(5) = 13; "
      "a tau >= 5 6-partite intersecting object cannot have fewer "
      "edges): consistency cross-check, not an input; the greedy landed "
      "ONE edge above that floor.  The UPPER end is this certificate's "
      "argument at (a,b) = (6,4)",
      len(core) == 14 and 13 <= len(core) <= comb(10, 6))
check("the 14 disjoint events sum to 14/210 = 1/15 <= 1 (exact "
      "rationals) -- unlike the abstract witness of section 4, a real "
      "core sits far from the ceiling",
      sum((Fraction(1, comb(10, 6)) for _ in core), Fraction(0))
      == Fraction(1, 15) <= 1)
note("NOT TOO STRONG, hypergraph side: the machinery kills nothing that "
     "exists -- the tau = 5 critical core is alive and well inside its "
     "own window [13, 210].  A ceiling that emptied its window would be "
     "proving too much")

# ==========================================================================
# 7.  Composition and scope
# ==========================================================================

head("7.  the window, composed")

check("the window [22, 462] is nonempty and its ceiling is the section-1 "
      "constant: nothing in this certificate constrains the interior "
      "(honest redundancy: this pins constants, it cannot fail alone)",
      22 <= 462 and comb(11, 6) == 462)
check("the ROBUSTNESS table: C(6+b, 6) for b = 0..5 is exactly "
      "(1, 7, 28, 84, 210, 462), strictly increasing -- so "
      "P(A_e) = 1/C(6+b_e, 6) >= 1/462 for every cover size b_e <= 5",
      tuple(comb(6 + b, 6) for b in range(6)) == (1, 7, 28, 84, 210, 462)
      and all(comb(6 + b, 6) < comb(7 + b, 6) for b in range(5)))
note("FLOOR (in-house): m >= 22 for ALL counterexamples -- the "
     "pinned-ladder chain stated transitively per 0012's ledger: "
     "0005/0006/0008/0009/0010/0011/0012 ((L7) from 0006, (L10) "
     "standing on 0011); 0007 remains the weak-ladder record.  A "
     "critical core is a counterexample, so the floor covers it a "
     "fortiori")
note("SCOPE: the ceiling quantifies over critical cores ONLY.  A "
     "non-critical counterexample is bounded by nothing here -- but every "
     "counterexample CONTAINS a core (step 1), which is what makes the "
     "window equivalent to the conjecture")
note("ROBUSTNESS: with |T_e| = b <= 5 the bound per pair is "
     "1/C(6+b, 6) >= 1/462 -- the ceiling does not ride on the exactness "
     "of tau(K - e) = 5, only on criticality itself (sizes AND "
     "disjointness both flow from tau(K - e) < 6)")

head("Result")

print("""
  every critical core K has m(K) <= C(11,6) = 462       PROVEN-BY-CERTIFICATE
                                                        (ledger EMPTY: no
                                                        external, no in-house
                                                        inputs)
  every critical core K has m(K) in [22, 462]           PROVEN-BY-CERTIFICATE
                                                        (floor: in-house,
                                                        transitively
                                                        0005/0006/0008-0012)
  Ryser r = 6 intersecting <=> no critical core         PROVEN-BY-CERTIFICATE
  with m in [22, 462]                                   (the [22,...] half
                                                        inherits the floor's
                                                        in-house ledger)

  The conjecture is now a FINITE question.  Every future rung (m = 23,
  24, ...) closes part of a window whose two ends are both certified:
  441 values of m remain.  The ceiling's bound rides on criticality --
  the cover-size cap and, via tau(K) = 6, the private covers' (3a)/(3b)
  -- yielding m(K) <= 462 pairwise-disjoint events of probability at
  least 1/462 each (the written proof also pins tau(K - e) = 5 exactly,
  which the bound survives without).  It does NOT consume: the ladder,
  the pair count, (D2), (L7)-(L10), any budget, or any citation.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(1 if FAILED else 0)
