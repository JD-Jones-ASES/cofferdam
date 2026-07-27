#!/usr/bin/env python3
"""Certificate 0010 -- N(4) = 9 BY HAND: the load-bearing exhaustion gets a
search-free third leg.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from lib/.
Runs in seconds under a bare /usr/bin/python3 (3.9) and under python3 -O.

WHAT IS CLAIMED
---------------
  THEOREM: no 6-partite 6-uniform intersecting hypergraph has m = 8 edges,
  tau >= 4, and a part all of whose active vertices have degree >= 2
                                                PROVEN-BY-CERTIFICATE
                                                (a hand proof; the machine
                                                checks below are finite case
                                                enumerations, each transparent)
  N(4) = 9, citing nothing                      PROVEN-BY-CERTIFICATE

N(4) = 9 is the hinge of the floor: certificate 0007 says every m <= 20 kill
funnels through it, certificate 0008 the same for m <= 20 under the cap, and
until today its lower bound rested on exhaustive search alone -- 52.0M nodes
(certificate 0005) and a structurally different 5.7M-node second
implementation (turn 7).  Searches can under-enumerate, and an
under-enumerating search fakes exactly this kind of proof.  This certificate
replaces the risk class entirely: a human can read the argument below in an
afternoon, and every finite claim it leans on is machine-checked here in
seconds.  The two searches stand as corroboration; nothing rests on them.

PROVENANCE.  The proof was produced by this lab's subagent fleet (turn 9,
three independent angles briefed adversarially) and re-derived line by line
at the desk before being written here.  Fleet output is fleet-claimed until
re-derived (Certificate Law); this one has been.

THE PROOF
---------
Suppose H is 6-partite, 6-uniform, intersecting, with 8 edges E, tau(H) >= 4,
and a part p0 whose active vertices all have degree >= 2.

SEC 0 (column form).  In each part the stars of its active vertices partition
E; identify a vertex with its block.  A pair {e,f} of edges is covered at a
part iff e,f share that part's vertex; mult{e,f} = number of parts covering
the pair.  Intersecting <=> mult >= 1 for all 28 pairs.  A vertex set covers
H iff its blocks' union is E; tau >= 4 <=> no 3 blocks union to E.

SEC 1 (profiles).  (1.1) A part's blocks partition E, so every part is a
cover: every part has >= 4 blocks.  (1.2) Deleting a degree-d vertex's star
leaves 8-d edges with tau >= 3 (a cover of the residual plus the vertex
covers H; an empty residual would make the vertex a 1-cover), so
8 - d >= g(3) = 5: every degree is <= 3.  (1.3) Two same-part vertices have
disjoint stars; deleting both leaves tau >= 2, so d1 + d2 <= 8 - g(2) = 5:
no part has two degree-3 vertices.  (1.4) p0 has >= 4 blocks, all >= 2,
summing to 8: p0 is EXACTLY (2,2,2,2), a perfect matching of E into four
"married pairs".  (1.5) Pair count: sum over parts of sum_B C(|B|,2)
= sum over pairs of mult = 28 + X with excess X >= 0.  (1.6) The admissible
non-p0 profiles (partitions of 8, >= 4 entries, entries <= 3, top two <= 5)
and their pair-sums are exactly: (3,2,2,1)->5, (3,2,1,1,1)->4, (2,2,2,2)->4,
(2,2,2,1,1)->3, (3,1,1,1,1,1)->3, (2,2,1,1,1,1)->2, (2,1,1,1,1,1,1)->1,
(1x8)->0.  (1.7) p0 contributes 4, so the other five parts sum to >= 24 with
each <= 5; at most one falls short of 5, and only three cases reach 24:
    CASE A: five (3,2,2,1)                     total 29, X = 1
    CASE B: four (3,2,2,1) + one (2,2,2,2)     total 28, X = 0
    CASE C: four (3,2,2,1) + one (3,2,1,1,1)   total 28, X = 0

SEC 2 (triples).  Each non-p0 part carries at most one size-3 block; call
these the triples -- four in case B, five in A and C, all in distinct parts.
  LEMMA 2.1: any two triples intersect.  Otherwise E minus their 6 edges is a
  pair {a,b}; intersecting-ness hands us a vertex w covering both, and the
  two triples' vertices plus w are a 3-cover.  Contradiction with tau >= 4.
  LEMMA 2.2 (excess accounting): a pair of triples sharing 2 edges puts a
  pair at mult >= 2 and spends 1 of X; a married pair inside a triple spends
  1; two identical triples would spend 3.  So in B and C (X = 0) every two
  triples share EXACTLY one edge and no triple contains a married pair; in A
  (X = 1) at most one triple-pair shares 2 edges (eta in {0,1}).

SEC 3 (every edge lies in a triple).  Fix an edge e and let b_1..b_5 be its
block sizes in the non-p0 parts.  Counting the 7 pairs at e:
sum_parts (size at e - 1) = 7 + eps_e, and p0 gives 1, so
sum b_i = 11 + eps_e >= 11; all b_i <= 2 would give <= 10.  So every edge
lies in at least one triple (r_e >= 1).

SEC 4 (double count).  sum_e r_e = 3 (number of triples) and
sum_e C(r_e,2) = sum over triple-pairs |Ti n Tj|.  So the vector r over the
8 edges satisfies: case B (12, 6); case C and A-eta0 (15, 10);
case A-eta1 (15, 11).

SEC 5 (case B dies).  With entries in 1..4, sum 12 and sum-C 6 force
r = (3,3,1,1,1,1,1,1).  Two edges of r = 3 have triple-sets that are
3-subsets of the 4 triples, hence share >= 2 triples -- and any two shared
triples share those TWO edges, against |Ti n Tj| = 1.

SEC 6 (cases C and A-eta0 die).  (15,10) forces r = (4,2,2,2,2,1,1,1) or
(3,3,3,2,1,1,1,1).  For the first: the r=4 edge x pins Ti n Tj = {x} among
its four triples; the fifth triple must meet all four in four DISTINCT edges
(a repeat would be a second edge in some Ti n Tj) -- impossible in a 3-set.
For the second: the three r=3 edges' triple-sets are 3-subsets of the 5
triples, pairwise sharing <= 1 (two common triples would share two edges);
but any two 3-subsets of a 5-set share >= 1, so both intersections are
exactly 1 and their union is all 5 triples; the third set, inside that
union, meets one of the two in >= 2.  Contradiction.

SEC 7 (case A-eta1 dies).  (15,11) forces r = (4,3,2,2,1,1,1,1).  The unique
2-share of triples spends all of X: every other triple-pair shares exactly
one edge and NO married pair lies inside any triple.  Let x be the r=4 edge
(in triples T1..T4, not T5) and y the r=3 edge.  y in three of T1..T4 would
make three triple-pairs share {x,y} -- three units of excess.  So y is in T5
and exactly two x-triples, say T1, T2, making T1 n T2 = {x,y} the unique
2-share; T5 then meets T1 and T2 only at y, and meets T3, T4 in distinct
edges u, v (a common one would be a second r=3 edge).  Up to labels:
T1 = {x,y,a}, T2 = {x,y,b}, T3 = {x,u,c}, T4 = {x,v,d}, T5 = {y,u,v}, and
the eight edges are x,y,u,v,a,b,c,d.  Now p0 marries x to SOMETHING -- but
y, a, b, u, c, v, d is everything, and each shares a triple with x, so the
married pair {x, w} sits inside a triple (w != y), or {x,y} reaches mult 3
(w = y).  Either way X >= 2 > 1.  Contradiction.

Cases A, B, C are exhaustive, so no such H exists.  QED.

With m <= 7 impossible outright (g(4) >= 8, re-derived in section 1 below by
the same counting that needs no search), N(4) >= 9; the 9-edge witness of
certificate 0005, re-verified here, gives N(4) = 9.

WHAT THE MACHINE CHECKS ARE, AND ARE NOT
----------------------------------------
Sections 2-4 of the checks below verify every finite enumeration the proof
invokes (the profile case split, the r-vector solution sets, two set-system
facts), and then INDEPENDENTLY kill each case at the structure level: an
exhaustive sweep over triple systems inside C(8,3) = 56 with the stated
intersection pattern and coverage.  The proof does not depend on the sweeps;
the sweeps do not depend on the r-vectors.  Either alone closes the cases.

THE LEDGER, in full
-------------------
  g(2) >= 3, g(3) >= 5, g(4) >= 8    re-derived here by counting (section 1)
  the case analysis                   sections 2-4 below, plus the docstring
  the 9-edge witness                  re-verified here (section 5)
  EXTERNAL INPUTS -- NONE.  The 52M-node and 5.7M-node searches are
  corroboration, cited as history, load-bearing for nothing here.
"""

import itertools
import sys
import time
from math import comb

FAIL = []
COUNT = [0]
NOTES_N = [0]


def check(label, cond, detail=""):
    COUNT[0] += 1
    tag = "ok  " if cond else "FAIL"
    if not cond:
        FAIL.append(label)
    print("  [%s] %2d. %s%s" % (tag, COUNT[0], label,
                                ("   " + detail) if detail else ""), flush=True)


def note(label, detail=""):
    NOTES_N[0] += 1
    print("  [note] %s%s" % (label, ("   " + detail) if detail else ""),
          flush=True)


def head(s):
    print("\n=== %s ===" % s, flush=True)


T0 = time.time()

# ==========================================================================
# 1.  The counting ladder this proof consumes: g(2) >= 3, g(3) >= 5,
#     g(4) >= 8 -- re-derived, so the certificate stands alone
# ==========================================================================

head("1.  g(2) >= 3, g(3) >= 5, g(4) >= 8 by (L1) caps + (L2) pair count")


def capped_profiles(m, caps):
    out = []

    def rec(left, cur):
        k = len(cur)
        if k in caps and m - left > caps[k]:
            return
        if left == 0:
            out.append(tuple(cur))
            return
        top = cur[-1] if cur else left
        for d in range(min(left, top), 0, -1):
            rec(left - d, cur + [d])
    rec(m, [])
    return out


def sc(p):
    return sum(comb(d, 2) for d in p)


G = {1: 1}
for t, ms, rung in ((2, (1, 2), 3), (3, (3, 4), 5), (4, (5, 6, 7), 8)):
    for m in ms:
        caps = {k: m - G[t - k] for k in range(1, min(5, t))}
        profs = capped_profiles(m, caps)
        if not profs:
            dead, why = True, "no profile satisfies the caps"
        else:
            best = max(sc(p) for p in profs)
            dead = 6 * best < comb(m, 2)
            why = "max pair count %d, 6 x %d = %d < %d" % (
                best, best, 6 * best, comb(m, 2))
        check("t=%d, m=%d impossible under caps %s" % (t, m, caps), dead, why)
    G[t] = rung
note("hence g(2) >= 3, g(3) >= 5, g(4) >= 8; smaller m per rung die by "
     "monotonicity (tau >= t => tau >= t-1).  Witnesses at 3, 5, 8 live in "
     "certificate 0001 and are not needed here: the proof consumes only "
     "lower bounds")

# ==========================================================================
# 2.  CHECK 1 -- the profile case split
# ==========================================================================

head("2.  The case split: profiles and the three cases")

parts8 = [p for p in capped_profiles(8, {1: 3, 2: 5}) if len(p) >= 4]
PAIRSUMS = {p: sc(p) for p in parts8}
EXPECT = {(3, 2, 2, 1): 5, (3, 2, 1, 1, 1): 4, (2, 2, 2, 2): 4,
          (2, 2, 2, 1, 1): 3, (3, 1, 1, 1, 1, 1): 3, (2, 2, 1, 1, 1, 1): 2,
          (2, 1, 1, 1, 1, 1, 1): 1, (1, 1, 1, 1, 1, 1, 1, 1): 0}
check("the admissible non-p0 profiles (>= 4 entries, max <= 3, top two <= 5) "
      "are exactly the eight of (1.6), with exactly these pair-sums",
      PAIRSUMS == EXPECT)

full8 = [p for p in capped_profiles(8, {1: 3, 2: 5})
         if len(p) >= 4 and min(p) >= 2]
check("a full part at m = 8 is exactly (2,2,2,2) -- the perfect matching",
      full8 == [(2, 2, 2, 2)])

cases = []
for combo in itertools.combinations_with_replacement(sorted(PAIRSUMS), 5):
    tot = sum(PAIRSUMS[p] for p in combo)
    if 4 + tot >= comb(8, 2):
        cases.append((combo, 4 + tot))
check("exactly three 5-multisets of admissible profiles reach the pair "
      "count 28: cases A (X=1), B (X=0), C (X=0) of the proof",
      sorted(c[1] for c in cases) == [28, 28, 29] and len(cases) == 3
      and all(c[0].count((3, 2, 2, 1)) >= 4 for c in cases),
      "totals %s" % sorted(c[1] for c in cases))

# ==========================================================================
# 3.  CHECK 2 -- the r-vector solution sets and two set-system facts
# ==========================================================================

head("3.  The double-count funnels")


def rvectors(total, pairsum, maxr):
    sols = []
    for r in itertools.combinations_with_replacement(range(1, maxr + 1), 8):
        if sum(r) == total and sum(comb(x, 2) for x in r) == pairsum:
            sols.append(tuple(sorted(r, reverse=True)))
    return sorted(set(sols))


check("case B: (sum 12, pair-sum 6, entries <= 4) forces r = (3,3,1,...,1)",
      rvectors(12, 6, 4) == [(3, 3, 1, 1, 1, 1, 1, 1)])
check("cases C, A-eta0: (15, 10, <= 5) forces (4,2,2,2,2,1,1,1) or "
      "(3,3,3,2,1,1,1,1)",
      rvectors(15, 10, 5) == [(3, 3, 3, 2, 1, 1, 1, 1),
                              (4, 2, 2, 2, 2, 1, 1, 1)])
check("case A-eta1: (15, 11, <= 5) forces (4,3,2,2,1,1,1,1)",
      rvectors(15, 11, 5) == [(4, 3, 2, 2, 1, 1, 1, 1)])

bad_b = [(a, b) for a in itertools.combinations(range(4), 3)
         for b in itertools.combinations(range(4), 3)
         if a != b and len(set(a) & set(b)) < 2]
check("SEC 5's set fact: two distinct 3-subsets of a 4-set always share "
      ">= 2 elements", not bad_b)

trip5 = list(itertools.combinations(range(5), 3))
bad_c = [t for t in itertools.combinations(trip5, 3)
         if all(len(set(a) & set(b)) <= 1
                for a, b in itertools.combinations(t, 2))]
check("SEC 6's set fact: no three 3-subsets of a 5-set are pairwise "
      "<= 1-intersecting", not bad_c)

# ==========================================================================
# 4.  CHECK 3 -- independent structure-level kills of every case
# ==========================================================================

head("4.  Structure sweeps: each case killed again, without the r-vectors")

TRIPLES = list(itertools.combinations(range(8), 3))          # C(8,3) = 56


def inter(a, b):
    return len(set(a) & set(b))


def cover_all(sys_):
    return set().union(*(set(t) for t in sys_)) == set(range(8))


t_s = time.time()
b_sys = [s for s in itertools.combinations(TRIPLES, 4)
         if all(inter(a, b) == 1 for a, b in itertools.combinations(s, 2))
         and cover_all(s)]
check("case B at the structure level: ZERO systems of 4 triples, pairwise "
      "sharing exactly one edge, covering all 8 edges", not b_sys)

c_sys = [s for s in itertools.combinations(TRIPLES, 5)
         if all(inter(a, b) == 1 for a, b in itertools.combinations(s, 2))
         and cover_all(s)]
check("cases C and A-eta0 at the structure level: ZERO such 5-triple "
      "systems", not c_sys)

a1_sys = []
for s in itertools.combinations(TRIPLES, 5):
    ints = [inter(a, b) for a, b in itertools.combinations(s, 2)]
    if sorted(ints) == [1] * 9 + [2] and cover_all(s):
        a1_sys.append(s)
rv = set()
for s in a1_sys:
    r = [sum(1 for t in s if e in t) for e in range(8)]
    rv.add(tuple(sorted(r, reverse=True)))
check("case A-eta1: exactly 10,080 systems with one 2-share, nine 1-shares "
      "and full coverage, every one with r-vector (4,3,2,2,1,1,1,1)",
      len(a1_sys) == 10080 and rv == {(4, 3, 2, 2, 1, 1, 1, 1)},
      "%.1fs so far" % (time.time() - t_s))

MATCHINGS = []
def all_matchings(rest, cur):
    if not rest:
        MATCHINGS.append(tuple(cur))
        return
    a = rest[0]
    for b in rest[1:]:
        all_matchings([x for x in rest if x != a and x != b],
                      cur + [(a, b)])
all_matchings(list(range(8)), [])
check("there are 105 perfect matchings of the 8 edges", len(MATCHINGS) == 105)


def pair_in_triple(pr, s):
    return any(pr[0] in t and pr[1] in t for t in s)


alive = 0
for s in a1_sys:
    for mm in MATCHINGS:
        if all(not pair_in_triple(pr, s) for pr in mm):
            alive += 1
check("and across all 10,080 x 105 (system, matching) pairs, ZERO matchings "
      "avoid every triple -- p0's marriage always overspends X: case A-eta1 "
      "is dead", alive == 0, "%.1fs" % (time.time() - t_s))

relaxed = 0
for s in a1_sys[:500]:
    for mm in MATCHINGS:
        if sum(1 for pr in mm if pair_in_triple(pr, s)) <= 1:
            relaxed += 1
check("TEETH: relax the budget by one unit (allow a single married pair "
      "inside a triple) and structures pass by the thousand on the first "
      "500 systems alone -- the X-budget is what kills, and the sweep can "
      "tell the difference", relaxed > 0, "%d relaxed passes" % relaxed)

# ==========================================================================
# 5.  The witness: N(4) <= 9, so N(4) = 9
# ==========================================================================

head("5.  The 9-edge witness (certificate 0005's, re-verified)")

W_N4 = [(0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1), (0, 2, 2, 2, 2, 2),
        (1, 0, 1, 3, 2, 2), (2, 0, 3, 2, 1, 3), (3, 1, 3, 0, 3, 2),
        (3, 3, 0, 1, 2, 3), (4, 3, 1, 2, 3, 0), (0, 2, 1, 2, 2, 2)]
Wsets = [frozenset((i, e[i]) for i in range(6)) for e in W_N4]
Wv = sorted(set().union(*Wsets))
check("the witness has 9 distinct edges and is intersecting",
      len(set(W_N4)) == 9
      and all(a & b for a, b in itertools.combinations(Wsets, 2)))
has3 = any(all(set(S) & s for s in Wsets)
           for S in itertools.combinations(Wv, 3))
c4 = None
for S in itertools.combinations(Wv, 4):
    if all(set(S) & s for s in Wsets):
        c4 = S
        break
check("tau = 4 exactly: an explicit 4-cover, and no 3-cover among all "
      "C(%d,3) = %d subsets" % (len(Wv), comb(len(Wv), 3)),
      c4 is not None and not has3, "cover %s" % (c4,))
deg1 = {}
for e in W_N4:
    deg1[e[1]] = deg1.get(e[1], 0) + 1
prof1 = tuple(sorted(deg1.values(), reverse=True))
check("part 1 is (3,2,2,2): full, every active vertex of degree >= 2",
      prof1 == (3, 2, 2, 2))
note("N(4) <= 9 by the witness; the theorem gives no qualifying object at "
     "m = 8, and g(4) >= 8 (section 1) kills m <= 7 outright.  N(4) = 9, "
     "citing nothing")
note("the 52.0M-node exhaustion (certificate 0005) and the turn-7 "
     "5.7M-node second implementation now stand as CORROBORATION of a "
     "theorem, not as the theorem's only support.  The hinge of the floor "
     "is no longer a search")

head("Result")

print("""
  THEOREM: no 8-edge 6-partite intersecting tau >= 4     PROVEN-BY-CERTIFICATE
           object has a full part                        (hand proof + finite
                                                          machine checks)
  N(4) = 9                                               PROVEN-BY-CERTIFICATE,
                                                         citing NOTHING

  The floor's hinge -- the one step certificates 0007 and 0008 both funnel
  through below m = 21 -- is now a readable proof with three independent
  legs: this argument, and two exhaustive searches that agree with it.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (COUNT[0], NOTES_N[0], time.time() - T0,
         "ALL GREEN" if not FAIL else "FAILURES: " + ", ".join(FAIL)),
      flush=True)
sys.exit(1 if FAIL else 0)
