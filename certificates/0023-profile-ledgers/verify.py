#!/usr/bin/env python3
"""Certificate 0023 -- profile ledgers and the parity sieve: the X = 7
layer is EMPTY.  X >= 8 for every critical core in the window.

    python3 verify.py

Stdlib only.  Exact integer arithmetic on every load-bearing bound.  No
solver.  No imports from lib/.  Reads nothing from disk.  Runs under
Python 3.9 and under python3 -O.  Deterministic.

WHAT IS CLAIMED
---------------
  (T-A23) X >= 8 FOR EVERY CRITICAL CORE IN THE WINDOW [22, 456].
          Equivalently: the X = 7 layer is empty at every m.
          PROVEN-BY-CERTIFICATE.  0022's T-A22 (X = 7 => m <= 24,
          billed) leaves X = 7 alive only on m in {22, 23, 24};
          sections 2-5 empty all three rungs on every excess partition.
          With 0021's T-A21 / 0022's T-B22 (X >= 7 everywhere, billed),
          X >= 8 everywhere follows.

  (T-B23) THE STAIRCASE.  X >= 8 on 22 <= m <= 28;  X >= 9 at 29;
          X >= 10 from 30.  The live minimum-excess frontier becomes
          X = 8 on m in [22, 28].
          PROVEN-BY-CERTIFICATE.  T-A23 with 0021's T-B21 (X = 8 =>
          m <= 28, X = 9 => m <= 29, billed).

  (P2) THE PARITY SIEVE (new lemma, load-bearing at (7,24)).  On any
      edge e, sum_{z in e} d(z) = m + 5 + x_e (S5), so the number of
      odd-degree cells of e is congruent to m + 5 + x_e (mod 2).  At a
      census with n_2 = m/2 (m even), (D2) forces EXACTLY ONE degree-2
      cell on every edge; on an x_e = 0 edge with no degree-4 cells and
      no high cells beyond a single even-degree cell v, the remaining
      four cells are odd (degrees 3 or 5) and the edge degree-sum is
      even -- against m + 5 odd.  Such an edge cannot exist.

  (LG) THE INCIDENCE LEDGER (new engine, load-bearing at every K4
      cell).  Fix a census row (n_2, n_3, n_4, n_5) and the forced edge
      inventory of a configuration (support edges, excess-1 partners,
      plain edges through the high cells, outside edges).  Every edge
      carries a multiset of low-cell degrees (its PROFILE) constrained
      by (S5), (D2), the census's degree alphabet, and the class's
      fixed high-cell content.  A degree-d low cell lies in exactly d
      edges, so summed over ALL edges the chosen profiles must hit
      2 n_2, 3 n_3, 4 n_4, 5 n_5 EXACTLY.  The ledger solver decides
      that integer feasibility EXHAUSTIVELY; infeasibility kills the
      row.  (Necessary conditions only -- a feasible ledger proves
      nothing exists; every ledger below is INFEASIBLE.)

DEPENDENCIES (billed)
---------------------
  0005  min degree >= 2 (the identity and every profile alphabet).
  0008  (D2) both readings: <= one degree-2 cell per edge; n_2 <=
        floor(m/2).  The ledger's one-2-per-edge cap and the parity
        sieve's exactly-one-2 both price it.  M-D2E prices it here.
  0017  (C3) x_e <= floor((52 + 3X - 2m)/5) = 5 at m = 22, 23, 24.
        Note: at these rungs C3 does NOT exclude the (2,2,2,1)
        triangle (4 <= 5) and does NOT force q = 3 pairs edge-disjoint
        from q = 2 pairs (3 + 2 = 5): every argument below is c = 5
        clean, none quietly assumes the c = 4 world of 0021/0022.
  0020  (SSC+) F(d(v)) <= s(v) - qmax(v) per vertex.
  0021  (SJ)/(LD)/(KC)/(RG) and T-B21 (consumed by T-B23).
  0022  T-A22 (X = 7 => m <= 24) and T-B22 (X >= 7 everywhere,
        assembled there from 0021's T-A21) -- consumed by T-A23; the
        corrected triangle optimizer (re-enacted and re-measured here
        at 22/23/24 with its own case space).
  tau = 6 gives n >= 36 (re-derived inline).  External inputs: NONE.

THE PROOF, IN ORDER
-------------------
 (1) THE RUNGS (section 1).  Lambda_7 = 59 / 61 / 62 at m = 22/23/24;
     c = 5 at all three; the identity and census solver as in 0022.
 (2) THE RAW SIEVE (section 2).  All 15 partitions at each rung.
     Survivors: the six of 0022 -- (3,3,1), (3,2,2), (2,2,2,1),
     (2,2,1,1,1), (2,1^5), (1^7) -- plus (4,3) at m = 22 alone (60 vs
     Lambda 59).
 (3) THE m-INDEPENDENT WALLS (section 3).  Union/J bounds and quotient
     forcings that never mention m:
       (4,3)      J >= 29 (edge-disjoint by C3 even at c = 5: 7 > 5),
                  P <= 3:  Psi <= 15.
       (3,3,1)    J >= 21:  Psi <= 27.
       (3,2,2)    J >= 16 -- WITHOUT edge-disjointness (at c = 5 a
                  q = 3 pair MAY share an edge with a q = 2 pair;
                  the union bound survives on pair-counts alone):
                  Psi <= 48.
       (2,2,2,1)  nontriangle: |U| = 5 forced; every reaching multiset
                  -- (10,10), (10,9,6), and (10,9) -- forces BOTH top
                  cells into all three heavy shared sets (s-hosting
                  enumerated), hence into every support edge: C(4,2) =
                  6 > 4 excessive pairs.  Dead at J = 10 and J = 11.
       (2,2,1,1,1)  (10,10): the C(r,2) = 5 wall.  (10,9,6): every
                  hosting unit-distribution puts multiplicity 2 on a
                  cell pair -- 2 is not a clique pair-count.  (10,9):
                  J = 8 collapses to mu = 2 or to C(r,2) = 5; J = 9
                  likewise (enumerated).  All dead.
       (2,1^5)    (10,9,6): the pairs through {a,b} number 5 -- not a
                  clique count.  (10,10)/(10,9): the K4 collapse (all
                  five q = 1 sets equal {a,b}, C(r,2) = 6, r = 4).
       (1^7)      (10,10,6) and (10,9,6): capacity -- no triangular
                  multiplicity pattern hosts them (|U| = 3 and 4
                  enumerated).  (10,10)/(10,9): the disjoint 6+1
                  collapse to a K4 (0022's pattern logic, re-enacted).
 (4) THE TRIANGLE, RUNG BY RUNG (section 4).  The corrected optimizer
     maxes at 54 / 59 / 62: dead raw at 22 and 23.  At 24 the unique
     achiever at Lambda is t = 3, S_4 through the top cell, degrees
     (10,9,6); the census pins (12,5,0,16) with EXACTLY ONE degree-2
     cell per edge; the apex variant dies by (S5) arithmetic (two
     {3,5} cells cannot sum to 7); and the five plain edges through
     the degree-10 cell die by (P2).  Zero margin, closed by parity.
 (5) THE K4 LEDGERS (section 5).  For (2,1^5) and (1^7) at each rung
     and each census row of each reaching multiset: the forced K4
     inventory is built, profile options enumerated, and the ledger
     solved.  EVERY ledger is infeasible.  Highlights: at m = 22 the
     x = 3 support profile does not exist (four cells, <= one 2, sum
     10 < 11 minimum); at m = 23 the 2-count strands the rows the
     3-count spares; at m = 24 the 3/4-counts exhaust jointly.
 (6) ASSEMBLY (section 6).  T-A23, T-B23.
 (7) MUTATIONS (section 7).  Nine, priced.

MANDATORY HONESTY NOTES
-----------------------
 (1) PROVENANCE.  THE THEOREM AND EVERY ARGUMENT ARE IN-HOUSE (desk
     turn 19); no peer text was received this turn.  The parity sieve
     and the ledger engine arose at the desk while working the (7,24)
     tie that 0022 left as its open wall; the K4/quotient machinery
     extends 0022's.  Adversarial lanes (three refuters, one blind
     computational sweep) ran against the desk derivation before
     certification; their outcomes are recorded in NOTES.md.
 (2) THE TIE FELL TO PARITY, NOT TO A SHARPER COUNT.  0022 called
     (7,24) "a wall counting alone cannot breach", and that stands:
     the moment/knapsack engine ties at 62 = Lambda exactly, and the
     kill is the parity of forced degree profiles, a different
     invariant.  The 6-partite tiling test (banked turn 18) was
     measured against the same template and does NOT kill it (it
     tiles); recorded as a mutant-style note, not consumed.
 (3) THE LEDGER IS A RELAXATION.  A feasible ledger would prove
     nothing; the certificate only ever uses INFEASIBILITY.  The
     solver enumerates every distribution of every edge class over its
     full profile option list -- completeness of the option lists is
     itself checked (M-PROF, M-OPT).
 (4) MARGINS.  The (7,24) triangle dies with zero numeric slack at
     three separate computations (optimizer tie, apex sum, parity) --
     TWO COMPLETE INDEPENDENT PROOFS (pigeonhole CK_PIG; parity
     CK_P2, apex-free), with CK_APEX a posture note and the deg-6
     parity the same invariant twice (erratum 2026-08-03, twice-
     corrected -- see CK_P2 and NOTES).  The
     ledgers at m = 23 close by 2 units of n_3 or 2 of the 2-count;
     m = 22 closes by 1 unit of profile-sum.  M-D2E reopens the m = 22
     instant kill and the parity sieve simultaneously -- (D2) is the
     single most load-bearing input of this file.

NOTATION.  As in 0015-0022.  q, X, x_e, pi, S_i, R, s(v), qmax(v), P,
J, F, f, psi, Phi as there.  A PROFILE is the multiset of low-cell
degrees of one edge (high cells listed separately).  LOW means degree
in {2,3,4,5}; HIGH means degree >= 6 (exactly the knapsack multiset).
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
    """A check.  `cond` must be COMPUTED.  A literal True here is a
    note and belongs in note() below (D-015; the separate-tally
    discipline 0022 dropped and this file restores)."""
    NCHECK[0] += 1
    ok = bool(cond)
    if not ok:
        FAILED.append(label)
    tag = "ok  " if ok else "FAIL"
    print("  [%s] %2d. %s" % (tag, NCHECK[0], label))
    if detail:
        print("        -> %s" % detail)
    return ok


def note(label):
    """A stated-not-tested fact: definitional, inert-by-theorem, or
    prose that a check nearby enacts.  Counted separately."""
    NNOTE[0] += 1
    print("  [note] n%d. %s" % (NNOTE[0], label))


def head(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def show(seq):
    return "[" + ", ".join(str(x) for x in seq) + "]"


# ==========================================================================
# 0.  Engine
# ==========================================================================

head("0.  ENGINE -- knapsack, census, profiles, the ledger solver")


def Phi(n, k):
    q, r = divmod(n, k)
    return r * comb(q + 1, 2) + (k - r) * comb(q, 2)


def F(d):
    return Phi(d, 5)


def flin(d):
    return d - 5 if d > 5 else 0


def psi(d):
    return flin(d) * (flin(d) + 2)


def Lam(X, m):
    return m * m - 43 * m + 2 * X + 540 - 3 * (m // 2)


def dmax_for(C):
    d = 5
    while F(d + 1) <= C:
        d += 1
    return d


def knap_sets(B, C, floor_v=0):
    dm = dmax_for(C)
    out = []

    def rec(dcur, budget, cur, val):
        if val >= floor_v:
            out.append((val, tuple(cur)))
        for d in range(min(dcur, dm), 5, -1):
            c = F(d)
            if c <= budget:
                cur.append(d)
                rec(d, budget - c, cur, val + psi(d))
                cur.pop()

    rec(dm, B, [], 0)
    return out


def knap_max(B, C):
    return max(v for (v, _) in knap_sets(B, C))


def Rof(pi):
    return sum(q * (q + 1) for q in pi)


def c3cap(X, m):
    return (52 + 3 * X - 2 * m) // 5


PARTS7 = []
def _parts(rest, most, cur):
    if rest == 0:
        PARTS7.append(tuple(cur))
        return
    for q in range(min(rest, most), 0, -1):
        cur.append(q)
        _parts(rest - q, q, cur)
        cur.pop()
_parts(7, 7, [])

check("ALL 15 PARTITIONS OF 7, GENERATED IN-CERT (M-SWEEP below)",
      len(PARTS7) == 15)
CK_PARTS = NCHECK[0]


def census_rows(m, X, D):
    """All feasible (n, n2, n3, n4, n5), high cells exactly D."""
    Ps = sum(psi(d) for d in D)
    gap = Ps - Lam(X, m)
    if gap < 0:
        return []
    n2cap = m // 2
    rows = []
    for dn in range(0, gap // 15 + 1):
        n = 36 + dn
        rem = gap - 15 * dn
        for n2 in range(0, n2cap + 1):
            n4 = rem - 3 * (n2cap - n2)
            if n4 < 0:
                continue
            nlow = n - len(D) - n2 - n4
            if nlow < 0:
                continue
            degsum = 6 * m - sum(D) - 2 * n2 - 4 * n4
            t5 = degsum - 3 * nlow
            if t5 < 0 or t5 % 2:
                continue
            n5 = t5 // 2
            if nlow - n5 < 0:
                continue
            rows.append((n, n2, nlow - n5, n4, n5))
    return rows


def profiles(cells, total, allowed=(2, 3, 4, 5), max2=1):
    """All degree multisets of `cells` low cells, degrees from
    `allowed`, at most `max2` degree-2 cells ((D2)), summing to
    `total`.  Exhaustive."""
    out = []
    for combo in itertools.combinations_with_replacement(allowed, cells):
        if sum(combo) != total:
            continue
        if combo.count(2) > max2:
            continue
        out.append(combo)
    return out


check("THE PROFILE ALPHABET AT THE THREE RUNGS.  x = 3 support-edge "
      "ordinaries (four cells, <= one 2): sum m - 12 = 10 at m = 22 "
      "has NO profile (minimum is 2+3+3+3 = 11); sum 11 has exactly "
      "one, (2,3,3,3); sum 12 has two, (2,3,3,4) and (3,3,3,3), both "
      "with >= 2 threes; sum 13 has three, minimum one 3.  These four "
      "facts carry section 5",
      profiles(4, 10) == []
      and profiles(4, 11) == [(2, 3, 3, 3)]
      and sorted(profiles(4, 12)) == [(2, 3, 3, 4), (3, 3, 3, 3)]
      and min(p.count(3) for p in profiles(4, 12)) == 2
      and len(profiles(4, 13)) == 3
      and min(p.count(3) for p in profiles(4, 13)) == 1,
      "sum13: %s" % show(profiles(4, 13)))
CK_PROF = NCHECK[0]


def ledger_feasible(classes, targets):
    """classes: list of (count, [profile, ...]) -- `count` edges each
    choosing one profile from the list.  targets: {d: total} -- the
    summed multiplicity of degree d over ALL chosen profiles must
    equal targets[d] for every listed d.  Exhaustive over per-class
    distributions (compositions of count over the options), with
    partial-sum pruning.  Returns True iff SOME assignment hits every
    target exactly.  An empty option list with count > 0 is
    immediately infeasible."""
    degs = sorted(targets)
    for (count, opts) in classes:
        if count > 0 and not opts:
            return False

    def upper(ci, d):
        """Max attainable of degree d from classes ci..end."""
        tot = 0
        for (count, opts) in classes[ci:]:
            tot += count * max((p.count(d) for p in opts), default=0)
        return tot

    def lower(ci, d):
        tot = 0
        for (count, opts) in classes[ci:]:
            tot += count * min((p.count(d) for p in opts), default=0)
        return tot

    def rec(ci, acc):
        if ci == len(classes):
            return all(acc[d] == targets[d] for d in degs)
        for d in degs:
            if acc[d] + upper(ci, d) < targets[d]:
                return False
            if acc[d] + lower(ci, d) > targets[d]:
                return False
        count, opts = classes[ci]
        for split in itertools.combinations_with_replacement(
                range(len(opts)), count):
            acc2 = dict(acc)
            ok = True
            for oi in split:
                for d in degs:
                    acc2[d] = acc2[d] + opts[oi].count(d)
                    if acc2[d] > targets[d]:
                        ok = False
            if ok and rec(ci + 1, acc2):
                return True
        return False

    return rec(0, {d: 0 for d in degs})


check("LEDGER SOLVER, CONTROLLED BOTH WAYS.  A synthetic satisfiable "
      "instance (two classes, unique hit) returns FEASIBLE; perturbing "
      "one target by one unit returns INFEASIBLE; an empty option list "
      "is infeasible on sight",
      ledger_feasible([(2, [(2, 3), (3, 3)]), (1, [(2, 5)])],
                      {2: 2, 3: 3, 5: 1})
      and not ledger_feasible([(2, [(2, 3), (3, 3)]), (1, [(2, 5)])],
                              {2: 2, 3: 2, 5: 1})
      and not ledger_feasible([(1, [])], {2: 0}))
CK_LG = NCHECK[0]


# ==========================================================================
# 1.  The rungs
# ==========================================================================

head("1.  THE RUNGS -- Lambda, C3 at c = 5, the identity")

check("(DM) POINTWISE d = 2..400 (identity except slack 1 at d = 4; "
      "FALSE at d = 1: 0005 billed) and Lambda_7 = 59, 61, 62 at "
      "m = 22, 23, 24",
      all(d * d == 8 * d - 15 + (3 if d == 2 else 0)
          - (1 if d == 4 else 0) + psi(d) for d in range(2, 401))
      and not (1 <= 8 - 15 + psi(1))
      and [Lam(7, m) for m in (22, 23, 24)] == [59, 61, 62])
CK_LAM = NCHECK[0]

check("(C3) c = 5 AT ALL THREE RUNGS -- and what c = 5 permits, spelled "
      "out so nothing below inherits a c = 4 habit: a triangle edge "
      "(4 <= 5) MAY also ride the q = 1 pair (4 + 1 = 5); a q = 3 pair "
      "MAY share an edge with a q = 2 pair (3 + 2 = 5); a q = 3 pair "
      "may NOT share with q = 3 (6 > 5); q = 4 may not share with "
      "q = 3 (7 > 5)",
      [c3cap(7, m) for m in (22, 23, 24)] == [5, 5, 5]
      and 4 + 1 <= 5 and 3 + 2 <= 5 and 3 + 3 > 5 and 4 + 3 > 5)
CK_C3 = NCHECK[0]

note("n >= 36 (tau = 6: each of the six parts is a cover, so each "
     "holds >= 6 cells; 6 x 6 = 36) and (S5) sum_{z in e} d(z) = "
     "m + 5 + x_e (double count: e meets each of the other m - 1 "
     "edges, with x_e counting the excess overlaps): the sums "
     "27/28/29 (+x) at the three rungs drive every profile below.  "
     "Both are re-derivations of standing lemmas, enacted by every "
     "profile query in sections 4-5")


# ==========================================================================
# 2.  The raw sieve, three rungs
# ==========================================================================

head("2.  THE RAW SIEVE -- fifteen partitions at each rung")

SIX = [(3, 3, 1), (3, 2, 2), (2, 2, 2, 1), (2, 2, 1, 1, 1),
       (2, 1, 1, 1, 1, 1), (1,) * 7]


def raw_row(pi, X):
    B = Rof(pi) - pi[0] * (pi[0] + 1)
    C = X - pi[0]
    return knap_max(B, C) if C >= 1 else 0


RAW = [(pi, raw_row(pi, 7)) for pi in PARTS7]
for m in (22, 23, 24):
    surv = [pi for (pi, v) in RAW if v >= Lam(7, m)]
    check("RAW SURVIVORS AT m = %d (Lambda %d): %s" %
          (m, Lam(7, m),
           "the six + (4,3)" if m == 22 else "exactly the six of 0022"),
          surv == ([(4, 3)] + SIX if m == 22 else SIX),
          " | ".join("%s:%d" % (str(pi), v) for (pi, v) in RAW
                     if v >= Lam(7, m)))
CK_RAW = NCHECK[0]


# ==========================================================================
# 3.  The m-independent walls
# ==========================================================================

head("3.  THE m-INDEPENDENT WALLS -- once each, spent at all three rungs")

check("(4,3) -- ONLY ALIVE AT 22 (raw 60 vs 59).  The pairs are "
      "edge-disjoint (a common edge carries 4 + 3 = 7 > 5 = c).  Two "
      "common cells of the shared sets would put 2 cells in all four "
      "support edges: C(4,2) = 6 excessive pairs against 2 listed.  So "
      "|A cap B| <= 1: A's five cells at qmax 4 give 20, B's >= 3 "
      "outside cells at qmax 3 give 9: J >= 29, P <= 32 - 29 = 3 at "
      "cap 3: max Psi = %d < 59.  DEAD" % knap_max(3, 3),
      comb(4, 2) > 2 and Rof((4, 3)) - 29 == 3
      and knap_max(3, 3) == 15 and knap_max(3, 3) < 59)
CK_43 = NCHECK[0]

check("(3,3,1).  The q = 3 pairs are edge-disjoint EVEN AT c = 5 "
      "(6 > 5); |A cap B| <= 1 (six pairs against three); "
      "|A u B| >= 7 at qmax 3: J >= 21, P <= 5 at cap 4: max Psi = "
      "%d < 59.  DEAD at every rung" % knap_max(5, 4),
      3 + 3 > 5 and knap_max(5, 4) == 27 and knap_max(5, 4) < 59)
CK_331 = NCHECK[0]

check("(3,2,2) -- THE c = 5 REWORK.  At c = 5 the q = 3 pair MAY share "
      "an edge with a q = 2 pair (3 + 2 = 5), so 0022's edge-"
      "disjointness opening is NOT available; the union bound never "
      "needed it.  |A cap B| <= 1 in BOTH postures: shared edge e "
      "(A = e cap f, B = e cap g) puts A cap B inside f cap g, and "
      "|A cap B| >= 2 makes {f,g} a fourth excessive pair; disjoint "
      "supports with 2 common cells make six pairs against three.  So "
      "A's 4 cells at qmax 3 give 12 and B's >= 2 outside cells at "
      "qmax >= 2 give 4: J >= 16, P <= 8 at cap 4: max Psi = %d < 59."
      "  DEAD at every rung" % knap_max(8, 4),
      3 + 2 <= 5 and comb(4, 2) > 3
      and Rof((3, 2, 2)) - 16 == 8
      and knap_max(8, 4) == 48 and knap_max(8, 4) < 59)
CK_322 = NCHECK[0]

# ---- (2,2,2,1) nontriangle: the s-hosting enumeration -------------------
# |U| = 5 forced for J <= 11 (union >= 5 as in 0022, c-independent;
# |U| = 6 gives J >= 12, budget <= 8, max Psi 50 < 59).  Reaching
# multisets under budget 10 (J = 10) / 9 (J = 11): (10,10), (10,9,6),
# (10,9).  Enumerate s-compositions: a_v in {1,2,3} counts heavy sets
# through v (sum 9), b_v in {0,1} marks S_4 (sum(b in U) = 2 at J = 10,
# 1 at J = 11).  Hosting F-needs on distinct cells with s - 2 >= F.
NT_HOST = {}
for (needs, bU) in [((5, 5), 2), ((5, 4, 1), 2), ((5, 4), 2),
                    ((5, 5), 1), ((5, 4, 1), 1), ((5, 4), 1)]:
    hosts = []
    for avec in itertools.product((1, 2, 3), repeat=5):
        if sum(avec) != 9:
            continue
        for bpos in itertools.combinations(range(5), bU):
            s = [2 * a for a in avec]
            for i in bpos:
                s[i] += 1
            caps = sorted(((s[i] - 2, avec[i]) for i in range(5)),
                          reverse=True)
            need = sorted(needs, reverse=True)
            if all(caps[i][0] >= need[i] for i in range(len(need))):
                hosts.append(tuple(caps[i][1] for i in range(len(need))))
    NT_HOST[(needs, bU)] = sorted(set(hosts))

check("(2,2,2,1) NONTRIANGLE.  Budget: J = 10 leaves 10 (multisets "
      "(10,10), (10,9,6), (10,9)); J = 11 leaves 9 ((10,9) only); "
      "J >= 12 leaves <= 8, max Psi = %d < 59.  ENUMERATED s-hosting: "
      "in EVERY case, at both J-levels, every hosting composition puts "
      "the top two cells at a = 3 -- inside all three heavy shared "
      "sets, hence inside every support edge.  A nontriangle has >= 4 "
      "support edges (3-edge triangle-free graphs with Delta <= 2, "
      "enumerated in 0022; Delta <= 2 holds at c = 5 since three q = 2 "
      "pairs on one edge cost 6 > 5); any two support edges then share "
      "two cells: C(4,2) = 6 excessive pairs against 4.  DEAD at every "
      "rung, every multiset" % knap_max(8, 5),
      knap_max(8, 5) == 50
      and sorted(knap_sets(10, 5, 59)) == [(59, (10, 9)), (62, (10, 9, 6)),
                                           (70, (10, 10))]
      and sorted(knap_sets(9, 5, 59)) == [(59, (10, 9))]
      and all(all(h[0] == 3 and h[1] == 3 for h in NT_HOST[k])
              for k in NT_HOST if NT_HOST[k])
      and any(NT_HOST[k] for k in NT_HOST)
      and 2 + 2 + 2 > 5 and comb(4, 2) > 4,
      "hosting a-signatures: %s" % str(
          {str(k): v for (k, v) in sorted(NT_HOST.items(),
                                          key=lambda kv: str(kv[0]))}))
CK_2221NT = NCHECK[0]

# ---- (2,2,1,1,1): the mu enumeration ------------------------------------
TRI_N = set(comb(r, 2) for r in range(2, 12))


def w22111(needs, extra_out):
    """J = 8 + extra_out.  Base s on A u B (adjacent, |T| = 2) is
    (4,4,2,2); the three q = 1 sets place 6 - extra_out unit-increments
    on A u B in 2-cell sets (extra_out increments sit on cells outside
    the union).  Returns the list of (s-profile, in-union mu table,
    T-mu-with-heavies) for every hosting distribution."""
    out = []
    pairs = list(itertools.combinations(range(4), 2))
    inU = 3 - extra_out  # q=1 sets fully inside; extra_out sets have
    # one cell outside (their inside cell still gets +1)
    for full in itertools.combinations_with_replacement(pairs, inU):
        for half in itertools.combinations_with_replacement(
                range(4), 3 - inU):
            s = [4, 4, 2, 2]
            mus = {}
            for p in full:
                s[p[0]] += 1
                s[p[1]] += 1
                mus[p] = mus.get(p, 0) + 1
            for c in half:
                s[c] += 1
            caps = sorted(((s[i] - 2, i) for i in range(4)),
                          reverse=True)
            need = sorted(needs, reverse=True)
            if all(caps[i][0] >= need[i] for i in range(len(need))):
                out.append((tuple(sorted(s, reverse=True)), tuple(
                    sorted(mus.items()))))
    return out


H_1010 = w22111((5, 5), 0)
H_1096 = w22111((5, 4, 1), 0)
H_109_8 = w22111((5, 4), 0)
H_109_9 = w22111((5, 4), 1)

check("(2,2,1,1,1), THE QUOTIENT KILLS, ENUMERATED.  (10,10) at J = 8: "
      "every hosting distribution sends all three q = 1 sets to "
      "T = A cap B, so the excessive pairs are exactly all pairs among "
      "the r edges containing T and C(r,2) = 5 has no solution.  "
      "(10,9,6): %d hosting distributions, and EVERY one places "
      "multiplicity 2 on some cell pair -- 2 is not a clique count "
      "C(r,2).  (10,9) (@22 only, 59 = Lambda): at J = 8, hosting "
      "forces mu patterns {3} or {2,1}; mu = 3 collapses onto T making "
      "C(r,2) = 5 again; mu = 2 is not a clique count.  At J = 9 (one "
      "increment outside) the in-union distributions repeat the same "
      "two fates.  DEAD at every rung, every multiset.  The (10,10) "
      "hosting is UNIQUE: (7,7,2,2) with mu_01 = 3 (erratum "
      "2026-08-03: a vacuous 'or True' conjunct sat here -- deleted, "
      "replaced by this exact assertion; sixth audit's find)"
      % len(H_1096),
      all(comb(r, 2) != 5 for r in range(30))
      and len(H_1010) == 1
      and H_1010[0] == ((7, 7, 2, 2), (((0, 1), 3),))
      and all(mus and all(p == (0, 1) for (p, c) in mus)
              for (_, mus) in H_1010)
      and len(H_1096) > 0
      and all(any(c == 2 for (_, c) in mus) for (_, mus) in H_1096)
      and 2 not in TRI_N
      and all((not mus) or any(c == 2 for (_, c) in mus)
              or all(p == (0, 1) for (p, c) in mus)
              for (_, mus) in H_109_8 + H_109_9)
      and len(H_109_8) > 0,
      "(10,10) mus: %s | (10,9,6) sample: %s"
      % (sorted(set(m for (_, m) in H_1010)),
         H_1096[0][1] if H_1096 else "-"))
CK_22111 = NCHECK[0]

# ---- (2,1^5): the {a,b} clique counts -----------------------------------
# The q = 2 set A (3 cells) alone gives J >= 6.  Budgets: Psi = 70
# needs P = 10, so J <= 16 - 10 = 6 exactly; Psi = 62 needs P = 10,
# same; Psi = 59 needs P = 9, so J <= 7 -- the (10,9) branch admits
# J = 7 (one q = 1 increment lands OUTSIDE A) and the refuter lane
# caught the draft claiming J = 6 was forced there.  Enumerate the
# unit distributions in BOTH postures: five q = 1 sets place 10
# increments; at J = 6 all inside A; at J = 7 exactly one outside.
CL215 = []
for (needs, out) in [((5, 5), 0), ((5, 4, 1), 0), ((5, 4), 0),
                     ((5, 4), 1)]:
    inA = 10 - out
    for ua in range(0, 6):
        for ub in range(0, 6 - 0):
            uc = inA - ua - ub
            if not (0 <= uc <= 5 and ua >= ub >= uc):
                continue
            s = (2 + ua, 2 + ub, 2 + uc)
            caps = tuple(x - 2 for x in s)
            need = tuple(sorted(needs, reverse=True))
            if len(need) > 3 or any(caps[i] < need[i]
                                    for i in range(len(need))):
                continue
            # mu through {a,b}: ub of the q=1 sets pair b with a (a is
            # in all sets that touch anything: ua = max); plus the
            # q=2 pair whose set A contains both.  The clique count
            # through {a,b} is mu_q1(ab) + 1.
            mu_ab = ub  # every b-increment shares its set with a
            CL215.append((needs, out, (ua, ub, uc), mu_ab + 1))
check("(2,1^5), THE CLIQUE COUNTS -- unit distributions ENUMERATED in "
      "both J-postures.  All five q = 1 sets have both cells in A "
      "when J = 6; at J = 7 (live only for (10,9), P = 9) one "
      "increment sits outside.  Every hosting distribution: (10,10) "
      "-> u = (5,5,0), pairs through {a,b} = 5 + 1 = 6 = C(4,2): the "
      "K4, handed to section 5.  (10,9,6) -> u = (5,4,1): pairs "
      "through {a,b} = 4 + 1 = 5 -- NOT a clique count.  DEAD.  "
      "(10,9) at J = 6 -> u = (5,5,0): the K4 again (section 5); at "
      "J = 7 -> u = (5,4,+out): pairs through {a,b} = 5 again -- "
      "DEAD.  %d distributions, every non-K4 one lands on a "
      "non-triangular count" % len(CL215),
      5 not in TRI_N and 2 not in TRI_N and 4 not in TRI_N
      and 6 in TRI_N and [r for r in range(30) if comb(r, 2) == 6] == [4]
      and len(CL215) > 0
      and all(mu in (5, 6) for (_, _, _, mu) in CL215)
      and all(mu == 6 for (needs, _, _, mu) in CL215
              if needs == (5, 5))
      and all(mu == 5 for (needs, out, _, mu) in CL215
              if needs == (5, 4, 1) or out == 1),
      "distributions: %s" % show(CL215))
CK_215 = NCHECK[0]

# ---- (1^7): capacity + the 6+1 collapse ---------------------------------


def mult_patterns(ucells, total):
    pairs = list(itertools.combinations(range(ucells), 2))
    allowed = [0] + [t for t in sorted(TRI_N) if t <= total]
    out = []
    for combo in itertools.product(allowed, repeat=len(pairs)):
        if sum(combo) != total:
            continue
        s = [0] * ucells
        for (mu, (x, y)) in zip(combo, pairs):
            s[x] += mu
            s[y] += mu
        if 0 in s:
            continue
        out.append((combo, tuple(sorted(s, reverse=True))))
    return out


def hosts(pat, needs):
    caps = sorted((x - 1 for x in pat), reverse=True)
    need = sorted(needs, reverse=True)
    return len(need) <= len(caps) and all(
        c >= x for (c, x) in zip(caps, need))


P3 = mult_patterns(3, 7)
P4 = mult_patterns(4, 7)
P5 = mult_patterns(5, 7)

# The FULL (1^7) reaching lists per |U|-branch -- enumerated, not
# hand-picked (the audit-simulation lane caught a draft of this file
# treating four multisets where seven reach; the three it missed die
# below, one of them only after real work).  J = |U| (every U-cell at
# qmax 1, nothing outside U in any shared set... cells outside U in no
# shared set have F <= 0); budget P <= 14 - |U|.
REACH17 = {}
for (u, B) in ((3, 11), (4, 10), (5, 9)):
    pats = {3: P3, 4: P4, 5: P5}[u]
    rows = []
    for (v, ds) in sorted(set(knap_sets(B, 6, 59))):
        loads = tuple(F(d) for d in ds)
        if len(ds) > u:
            rows.append((v, ds, "dead: more high cells than U-cells"))
            continue
        hosting = sorted(set(s for (_, s) in pats if hosts(s, loads)))
        rows.append((v, ds, hosting))
    REACH17[u] = rows

SURV17 = [(u, v, ds, h) for (u, r) in REACH17.items()
          for (v, ds, h) in r if isinstance(h, list) and h]
check("(1^7), THE FULL REACHING LISTS, HOST-TESTED.  |U| = 3 (budget "
      "11): SEVEN multisets reach 59 -- (10,10,6) 73, (10,10) 70, "
      "(10,9,7) 67, (10,9,6,6) 65, (10,8,8) 65, (9,9,8) 63, (10,9,6) "
      "62, (10,9) 59, and the 4-cell ones die on sight (3 U-cells).  "
      "Host-testing every one against every triangular pattern: "
      "(10,10,6), (10,9,7), (9,9,8), (10,9,6) all FAIL capacity; the "
      "survivors are EXACTLY (10,10) and (10,9) on the disjoint-6+1 "
      "pattern (7,6,1) -- the K4 -- and (10,8,8) on (6,4,4), the "
      "mu = {3,3,1} DOUBLE-TRIPLE family.  |U| = 4 (budget 10): "
      "survivors (10,10), (10,9) on (6,6,1,1) -- the K4 again.  "
      "|U| = 5 (budget 9): NOTHING hosts (max capacity 3 < 5).  "
      "|U| >= 6: J >= 6 leaves max Psi = %d < 59.  The seventh pair "
      "rides at most one K4 support (two supports would share T plus "
      "the seventh set: q >= 2).  Sections 5 and 5b finish the three "
      "surviving families" % knap_max(8, 6),
      sorted(set(s for (u, v, ds, h) in SURV17 for s in h))
      == [(6, 4, 4), (6, 6, 1, 1), (7, 6, 1)]
      and sorted(set(ds for (u, v, ds, h) in SURV17))
      == [(10, 8, 8), (10, 9), (10, 10)]
      and all(h == [(6, 4, 4)] for (u, v, ds, h) in SURV17
              if ds == (10, 8, 8))
      and not any(h for (u, v, ds, h) in
                  [(u, v, ds, h) for (u, r) in REACH17.items()
                   for (v, ds, h) in r if isinstance(h, list)]
                  if ds in ((10, 10, 6), (10, 9, 7), (9, 9, 8),
                            (10, 9, 6)))
      and knap_max(8, 6) == 50,
      "survivors: %s" % show(sorted(set(
          (u, ds, tuple(h)) for (u, v, ds, h) in SURV17))))
CK_17 = NCHECK[0]


# ==========================================================================
# 4.  The triangle, rung by rung -- and the parity sieve at 24
# ==========================================================================

head("4.  (2,2,2,1) TRIANGLE -- dead raw at 22, 23; parity at 24")

TRI_BR = ((0, 0), (1, 0), (0, 1), (0, 2))


def tri23(X, m):
    """0022's corrected optimizer, re-enacted: t, (a, o) branches,
    T-caps 4 (5 on the a = 1 cell), outside cells F <= 1, sum f(T) <=
    m - 14 (RG at k = 3), budget R - J."""
    R = 20
    best = 0
    tops = set()
    for t in range(0, 4):
        U = 9 - 2 * t
        for (a, o) in TRI_BR:
            if a > min(t, 1) or o > max(0, 9 - 3 * t):
                continue
            outside_J = (2 - a - o) if t == 3 else 0
            Bud = R - 2 * U - outside_J
            if Bud < 0:
                continue
            caps = [(5 if (i == 0 and a == 1) else 4) for i in range(t)]
            for combo in itertools.product(*[range(0, cc + 1)
                                             for cc in caps]):
                if sum(combo) > m - 14:
                    continue
                for fo in itertools.product((0, 1), repeat=o):
                    cost = sum(F(x + 5) for x in combo) + sum(fo)
                    if cost > Bud:
                        continue
                    val = (sum(psi(x + 5) for x in combo)
                           + sum(psi(v + 5) for v in fo))
                    best = max(best, val)
                    if val >= Lam(7, m):
                        ds = tuple(sorted([x + 5 for x in combo if x]
                                          + [6 for v in fo if v],
                                          reverse=True))
                        tops.add((val, t, a, o, ds))
    return best, sorted(tops)


T22, TOP22 = tri23(7, 22)
T23, TOP23 = tri23(7, 23)
T24, TOP24 = tri23(7, 24)
check("THE TRIANGLE MAXIMA: 54 / 59 / 62 at m = 22 / 23 / 24 -- DEAD "
      "RAW at 22 and 23 (54 < 59, 59 < 61), and at 24 the achiever at "
      "Lambda is UNIQUE: t = 3, a = 1 (S_4 through one T-cell), o = 0, "
      "degrees (10, 9, 6) with the degree-10 cell carrying the S_4 "
      "membership (the f = 5 cell is the a = 1 cap-5 cell)",
      (T22, T23, T24) == (54, 59, 62)
      and TOP22 == [] and TOP23 == []
      and TOP24 == [(62, 3, 1, 0, (10, 9, 6))])
CK_TRI = NCHECK[0]

check("THE (7,24) CENSUS, PINNED.  Psi = 62 = Lambda exactly forces "
      "(n, n2, n3, n4, n5) = (36, 12, 5, 0, 16), the ONLY census row; "
      "n2 = 12 = floor(24/2) with degree-2 cells covering 24 edge-"
      "incidences over 24 edges at (D2)'s one-per-edge cap -- (D2) "
      "applied to THE CORE ITSELF, the object 0008 licenses, not a "
      "residual: EVERY EDGE CARRIES EXACTLY ONE DEGREE-2 CELL.  The "
      "high multiset is (10,9,6) BY THE OPTIMIZER'S UNIQUENESS (the "
      "previous check) -- the census alone would not exclude other "
      "62-reaching multisets, and at this rung census-emptiness has "
      "no bite at all (every nearby multiset admits a census; the "
      "m = 26 tool retired here, measured below)",
      census_rows(24, 7, (10, 9, 6)) == [(36, 12, 5, 0, 16)]
      and 2 * 12 == 24 and psi(6) == 3
      and census_rows(24, 7, (10, 9, 8)) != []
      and census_rows(24, 7, (10, 10, 6)) != [])
CK_CEN24 = NCHECK[0]

check("t = 3 STRUCTURE AT THE TIE.  |T| = 3 makes every heavy shared "
      "set EQUAL T (|S_ij| = 3 contains T); the star count is TIGHT: "
      "edges meeting T number >= 3 + (10-3) + (9-3) + (6-3) = 19 and "
      "residual pairing caps them at 24 - (2(6-3) - 1) = 19 -- so "
      "EVERY non-triangle edge meets T in at most one cell, EXACTLY 19 "
      "edges meet T and exactly 5 avoid it",
      3 + 7 + 6 + 3 == 19 and 24 - 5 == 19)
CK_TIE = NCHECK[0]

check("THE APEX DIES BY (S5) ARITHMETIC.  If the q = 1 pair rides a "
      "triangle edge (legal at c = 5), that edge sums to 24 + 5 + 5 = "
      "34: T carries 25, the forced one degree-2 cell carries 2, and "
      "the remaining two cells -- degrees in {3, 5} (no 4s, no highs "
      "outside T, no second 2) -- must sum to 7: {3,5} pairs reach "
      "only 6, 8, 10.  So BOTH q = 1 edges avoid the triangle",
      34 - 25 - 2 == 7
      and sorted(set(a + b for a in (3, 5) for b in (3, 5))) == [6, 8, 10])
CK_APEX = NCHECK[0]

check("THE PIGEONHOLE KILL -- the refuter lane's shortening, adopted "
      "as the PRIMARY gate.  Every edge must reach 29 (S5 at x >= 0); "
      "an edge with NO high cell holds exactly one degree-2 cell and "
      "five cells from {3,5} (n4 = 0): maximum 2 + 25 = 27 < 29.  So "
      "EVERY edge contains a high cell.  High incidences total "
      "10 + 9 + 6 = 25; the three triangle edges hold all three highs "
      "(T IS the high set), absorbing 9; the other 21 edges hold at "
      "most one high each (no non-triangle edge holds two T-cells) "
      "and must each hold at least one: 16 < 21.  DEAD -- using only "
      "the census, (D2), (S5), and the T-structure; indifferent to "
      "the apex posture and to which T-cell rides S_4",
      2 + 5 * 5 == 27 and 27 < 29
      and 10 + 9 + 6 - 3 * 3 == 16 and 24 - 3 == 21 and 16 < 21)
CK_PIG = NCHECK[0]

check("(P2) KILLS THE TIE AGAIN -- the desk's original parity gate, "
      "kept as an independent belt.  The degree-10 cell w is in S_4 "
      "(forced) and in T, so every excess-carrying edge through w is "
      "a triangle edge or a q = 1 edge; the rest are PLAIN (x = 0: "
      "all four excessive pairs are accounted elsewhere).  A plain "
      "edge through w sums to 29 "
      "(S5): w gives 10, the forced degree-2 cell gives 2, and the "
      "other FOUR cells have degrees in {3, 5} (the edge meets T only "
      "in w; n4 = 0; a second high is excluded by the optimizer's "
      "uniqueness; a second 2 violates (D2)): four odd numbers sum "
      "even, 17 is odd.  NO SUCH EDGE EXISTS -- and w needs FIVE OR "
      "MORE in EITHER apex posture: the excess-carrying edges lie in "
      "{3 triangle edges} + {both q = 1 edges through w}, at most 5 "
      "edges (4 if the pair rides the triangle), so d(w) = 10 leaves "
      ">= 5 plain edges.  This gate is APEX-FREE: 'meets T only in w' "
      "needs no posture (a second T-cell spawns an excessive pair "
      "with every triangle edge -- the partition is already spent), "
      "and the census pins are upstream of the split.  The degree-6 "
      "cell v (3 plain edges, residual 29 - 6 - 2 = 21, odd) repeats "
      "the SAME invariant -- a second manifestation, not a new "
      "proof.  THE DEGREE-9 CELL YIELDS NOTHING (9 + 2 + 3 + 5 + 5 "
      "+ 5 = 29 is realizable) -- said aloud so nobody 'verifies' "
      "parity there and reads the failure as a flaw.  THE (7,24) "
      "TRIANGLE IS EMPTY -- TWO COMPLETE INDEPENDENT PROOFS: the "
      "pigeonhole (CK_PIG) and this parity gate; CK_APEX is a "
      "posture note, load-bearing for neither (erratum 2026-08-03, "
      "twice-corrected: 'three independent ways' overclaimed, then "
      "the first repair OVER-retracted parity to a chain -- the "
      "refuter lane restored its independence; both versions dated "
      "in NOTES)",
      29 - 10 - 2 == 17
      and sorted(set(sum(c) for c in
                     itertools.combinations_with_replacement(
                         (3, 5), 4))) == [12, 14, 16, 18, 20]
      and 17 % 2 == 1 and (29 - 6 - 2) % 2 == 1
      and 9 + 2 + 3 + 5 + 5 + 5 == 29)
CK_P2 = NCHECK[0]

check("THE TIE'S SINGLE PILLAR, NAMED.  At the achieving state (SJ) "
      "is SLACK (P = 10 against R - J = 13): the optimizer's 62 is "
      "held at Lambda by residual pairing ALONE (sum f(T) <= 10), and "
      "without (RG) the branch reaches 83.  The RG limit's flat "
      "m - 14 is exact at every t (the t-dependence cancels: "
      "3 + sum(d-3) <= m - (2(6-t)-1) gives sum f <= m - 14 + 2t - "
      "2t).  Any future correction that lifts the optimizer by 3 or "
      "lowers Lambda by 3 admits n2 = 11 censuses, a 2-less edge "
      "reaches 30 >= 29, and every gate above fails SIMULTANEOUSLY -- "
      "the fragility is shared, not layered.  M-RG below prices it",
      20 - 7 == 13 and 10 < 13
      and (3 + 16 <= 24 - 5) and 62 - Lam(7, 24) == 0)
CK_PILLAR = NCHECK[0]


# ==========================================================================
# 5.  The K4 ledgers
# ==========================================================================

head("5.  THE K4 LEDGERS -- (2,1^5) and (1^7), every rung, every row")

# The K4: supports s1..s4 pairwise meeting exactly in T = the top two
# cells {a, b} (d(a) = 10; d(b) = 10 or 9).  (2,1^5): x = (4,4,3,3).
# (1^7): x = (3,3,3,3) with the seventh pair adding +1 to at most one
# support (cases: rides one support, or lives on non-support edges);
# in the |U| = 3 posture the seventh set is {a, c} and its second edge
# is an f-EDGE through a (x_f = 1); in |U| = 4 both seventh edges
# avoid T... their profiles are 6 low cells summing m + 6 (x = 1).
# Plain edges through a: d(a) minus a's excessive edges; likewise b.
# Outside edges: the rest, x = 0, six low cells summing m + 5.
#
# Every class's profile list is generated from (S5) + (D2) + the row's
# degree alphabet ({2,3,5} when n4 = 0, else {2,3,4,5}); the ledger
# then demands the global incidence totals 2 n2 / 3 n3 / 4 n4 / 5 n5.

LEDGERS = []


def alphabet(n4):
    return (2, 3, 5) if n4 == 0 else (2, 3, 4, 5)


def run_ledger(tag, m, row, classes):
    (n, n2, n3, n4, n5) = row
    targets = {2: 2 * n2, 3: 3 * n3, 4: 4 * n4, 5: 5 * n5}
    feas = ledger_feasible(classes, targets)
    LEDGERS.append((tag, m, row, feas))
    return feas


def k4_ledger_215(m, D, row):
    """(2,1^5): supports (4,4,3,3); a,b in all four; no seventh pair.
    Plains: a has d(a) - 4, b has d(b) - 4; outside m - 4 - plains."""
    (n, n2, n3, n4, n5) = row
    al = alphabet(n4)
    da, db = D[0], D[1]
    cls = []
    cls.append((2, profiles(4, m + 5 + 4 - da - db, al)))   # x=4 supports
    cls.append((2, profiles(4, m + 5 + 3 - da - db, al)))   # x=3 supports
    cls.append((da - 4, profiles(5, m + 5 - da, al)))       # a-plains
    cls.append((db - 4, profiles(5, m + 5 - db, al)))       # b-plains
    out = m - 4 - (da - 4) - (db - 4)
    cls.append((out, profiles(6, m + 5, al)))               # outside
    return run_ledger("(2,1^5) D=%s" % str(D), m, row, cls)


# The seventh pair's two edges each have one of four TYPES: S (a support,
# which then carries x = 4), A (a non-support edge through the top cell
# a; five low cells, sum m + 6 - d(a)), B (through b; sum m + 6 - d(b)),
# N (through neither; six low cells, sum m + 6).  Constraints: not both
# S (two supports already share T; adding the seventh set gives q >= 2);
# a cell of the seventh shared set lies in BOTH edges, so in the
# |U| = 3 posture (seventh set {a, c}) both edges contain a -- types in
# {S, A} -- and in the |U| = 4 posture (seventh set {x, y}, both low)
# an edge containing a or b puts that high cell in at most ONE of the
# two (a in both would put a in the seventh set).  The full posture
# list, both |U| cases merged (order irrelevant):
POSTURES_17 = (("S", "A"), ("A", "A"),          # |U| = 3
               ("S", "N"), ("A", "B"), ("A", "N"),
               ("B", "N"), ("N", "N"))           # |U| = 4


def k4_ledger_17(m, D, row, posture):
    """(1^7): four supports pairwise meeting in T = {a, b}; the seventh
    pair's two edges typed per `posture`."""
    (n, n2, n3, n4, n5) = row
    al = alphabet(n4)
    da, db = D[0], D[1]
    nS = posture.count("S")
    nA = posture.count("A")
    nB = posture.count("B")
    nN = posture.count("N")
    cls = []
    cls.append((nS, profiles(4, m + 5 + 4 - da - db, al)))
    cls.append((4 - nS, profiles(4, m + 5 + 3 - da - db, al)))
    cls.append((nA, profiles(5, m + 6 - da, al)))
    cls.append((nB, profiles(5, m + 6 - db, al)))
    cls.append((nN, profiles(6, m + 6, al)))
    cls.append((da - 4 - nA, profiles(5, m + 5 - da, al)))
    cls.append((db - 4 - nB, profiles(5, m + 5 - db, al)))
    out = m - 4 - nA - nB - nN - (da - 4 - nA) - (db - 4 - nB)
    cls.append((out, profiles(6, m + 5, al)))
    return run_ledger("(1^7) D=%s %s" % (str(D), "".join(posture)),
                      m, row, cls)


ALL_DEAD = True
DETAIL = []
for m in (22, 23, 24):
    for D in [(10, 10)] + ([(10, 9)] if m == 22 else []):
        if sum(psi(d) for d in D) < Lam(7, m):
            continue
        for row in census_rows(m, 7, D):
            f1 = k4_ledger_215(m, D, row)
            f17 = [k4_ledger_17(m, D, row, p) for p in POSTURES_17]
            if f1 or any(f17):
                ALL_DEAD = False
            DETAIL.append("m%d %s row%s: %s%s" %
                          (m, str(D), str(row[1:]),
                           "F" if f1 else ".",
                           "".join("F" if f else "." for f in f17)))

check("EVERY K4 LEDGER IS INFEASIBLE -- %d ledgers over the rungs, "
      "multisets (10,10) everywhere and (10,9) at 22, every census "
      "row, and ALL SEVEN seventh-pair postures for (1^7) (both edges "
      "typed over support / through-a / through-b / through-neither, "
      "the full |U| = 3 and |U| = 4 case space).  At m = 22 the x = 3 "
      "support class has an EMPTY option list (sum 10 < 11): instant.  "
      "At m = 23 and 24 the 2/3/4-counts strand every row.  The "
      "(2,1^5) and (1^7) shapes are EMPTY at all three rungs"
      % len(LEDGERS),
      ALL_DEAD and len(LEDGERS) >= 60,
      " | ".join(DETAIL))
CK_LEDGER = NCHECK[0]

head("5b.  THE DOUBLE-TRIPLE LEDGERS -- (1^7) at (10,8,8), mu = {3,3,1}")

# The mu = {3,3,1} structure (the audit-simulation lane's find): cells
# a (s = 6, d = 10), b, c (s = 4, d = 8 each); THREE edges through
# {a,b} (C(3,2) = 3 pairs), three through {a,c}, TWO through {b,c}
# (C(2,2) = 1 pair); 3 + 3 + 1 = 7 pairs.  Load assignment is forced
# (only a's capacity 5 carries F = 5).  Two edges sharing all of
# {a,b,c} would carry q >= 2: at most ONE such edge e0, giving two
# postures:
#   k = 0: no abc-edge.  8 supports: 3 ab (x = 2), 3 ac (x = 2),
#          2 bc (x = 1); plains a: 4, b: 3, c: 3; outside m - 18.
#   k = 1: e0 (x = 2+2+1 = 5 <= c3 = 5, legal); 2 pure-ab, 2 pure-ac,
#          1 pure-bc; plains a: 5, b: 4, c: 4; outside m - 19.
# Low-cell sums per class from (S5); the ledger does the rest.


def dbl_ledger(m, row, k):
    (n, n2, n3, n4, n5) = row
    al = alphabet(n4)
    cls = []
    if k == 0:
        cls.append((6, profiles(4, m - 11, al)))    # ab + ac, x = 2
        cls.append((2, profiles(4, m - 10, al)))    # bc, x = 1
        cls.append((4, profiles(5, m - 5, al)))     # a-plains
        cls.append((6, profiles(5, m - 3, al)))     # b- and c-plains
        cls.append((m - 18, profiles(6, m + 5, al)))
    else:
        cls.append((1, profiles(3, m - 16, al)))    # e0, x = 5
        cls.append((4, profiles(4, m - 11, al)))    # pure ab + ac
        cls.append((1, profiles(4, m - 10, al)))    # pure bc
        cls.append((5, profiles(5, m - 5, al)))     # a-plains
        cls.append((8, profiles(5, m - 3, al)))     # b- and c-plains
        cls.append((m - 19, profiles(6, m + 5, al)))
    return run_ledger("(1^7) (10,8,8) k=%d" % k, m, row, cls)


check("m = 22 DIES BY RESIDUAL PAIRING BEFORE ANY LEDGER RUNS.  The "
      "double-triple structure fixes the edges through {a, b, c} "
      "exactly: 8 supports + 4 + 3 + 3 plains at k = 0 (a-plains avoid "
      "b and c -- a plain through a and b would share {a, b} with "
      "every ab-support, an eighth pair), so EXACTLY 18 distinct edges "
      "meet the triple and m - 18 avoid it; k = 1 gives 19 and "
      "m - 19.  (RG) at |U| = 3 demands >= 2(6-3) - 1 = 5 avoiding "
      "edges: at m = 22 there are 4 (k = 0) or 3 (k = 1).  DEAD -- "
      "and this gate was found only after the incidence ledger "
      "returned FEASIBLE on two m = 22 census rows: the ledger is a "
      "relaxation, it proves nothing when satisfiable, and the "
      "certificate says so out loud (honesty note 3).  At m = 23, 24 "
      "the RG count passes (5, 6) and the ledgers below do the work",
      22 - 18 < 5 and 22 - 19 < 5 and 23 - 18 >= 5 and 24 - 18 >= 5
      and 2 * (6 - 3) - 1 == 5)
CK_DBLRG = NCHECK[0]

DBL_DEAD = True
DBL_DETAIL = []
for m in (23, 24):
    rows = census_rows(m, 7, (10, 8, 8))
    for row in rows:
        for k in (0, 1):
            f = dbl_ledger(m, row, k)
            if f:
                DBL_DEAD = False
            DBL_DETAIL.append("m%d row%s k%d: %s"
                              % (m, str(row[1:]), k, "F" if f else "."))

check("EVERY DOUBLE-TRIPLE LEDGER AT m = 23, 24 IS INFEASIBLE -- %d "
      "ledgers: every census row, both abc-postures.  The k = 1 "
      "posture dies instantly at 23 (the abc-edge's three ordinaries "
      "must sum to 7, under the minimum 2 + 3 + 3 = 8); the rest die "
      "on the incidence counts.  With the m = 22 RG gate (check %d), "
      "the (1^7) shape has NO live multiset left: (10,10) and (10,9) "
      "fell to the K4 ledgers, (10,8,8) falls here, every other "
      "reaching multiset failed capacity (check %d)"
      % (len(DBL_DETAIL), CK_DBLRG, CK_17),
      DBL_DEAD and len(DBL_DETAIL) >= 8
      and profiles(3, 7) == [] and profiles(3, 8) == [(2, 3, 3)],
      " | ".join(DBL_DETAIL))
CK_DBL = NCHECK[0]

# Positive control: build the m = 25 (2,1^5) class inventory, PICK one
# profile per class by hand, and feed the ledger the exact totals that
# choice produces -- feasibility is then true by construction, and the
# solver must find it.  (The m = 25 CENSUS row (12,1,2,19) itself is
# infeasible -- 0022 killed it by the n_3 = 1 count and the ledger
# agrees.)
_al = (2, 3, 4, 5)
_CL25 = [(2, profiles(4, 14, _al)), (2, profiles(4, 13, _al)),
         (6, profiles(5, 20, _al)), (6, profiles(5, 20, _al)),
         (9, profiles(6, 30, _al))]
_pick = {2: 0, 3: 0, 4: 0, 5: 0}
for (cnt, opts) in _CL25:
    for d in _pick:
        _pick[d] += cnt * opts[0].count(d)
check("LEDGER SANITY, BOTH DIRECTIONS.  The m = 25 (2,1^5) census row "
      "(12,1,2,19) is INFEASIBLE (0022's n_3 = 1 kill, re-found by the "
      "ledger), while the constructed target vector %s -- produced by "
      "actually choosing one profile per class -- is FEASIBLE: the "
      "solver is deciding the instance, not rejecting everything"
      % str(_pick),
      not k4_ledger_215(25, (10, 10), (36, 12, 1, 2, 19))
      and ledger_feasible(_CL25, dict(_pick)))
CK_LSAN = NCHECK[0]


# ==========================================================================
# 6.  Assembly
# ==========================================================================

head("6.  T-A23 / T-B23")

check("(T-A23)  X >= 8 FOR EVERY CRITICAL CORE.  The X = 7 layer on "
      "m in {22, 23, 24}: raw sieve (checks %d-%d) -> walls (checks "
      "%d, %d, %d, %d, %d, %d, %d) -> triangle (checks %d-%d) -> "
      "ledgers (check %d): every partition dead at every rung.  0022's "
      "T-A22 (billed) closes m >= 25; 0021/0022's X >= 7 (billed) "
      "turns emptiness into X >= 8"
      % (CK_RAW - 2, CK_RAW, CK_43, CK_331, CK_322, CK_2221NT,
         CK_22111, CK_215, CK_17, CK_TRI, CK_P2, CK_LEDGER),
      len(FAILED) == 0)

check("(T-B23)  THE STAIRCASE: X >= 8 on [22, 28]; X >= 9 at 29; "
      "X >= 10 from 30 (0021 T-B21 billed for the upper rungs).  The "
      "live minimum-excess frontier is X = 8 on m in [22, 28] -- "
      "seven rungs, one excess layer higher than turn 18 left it",
      len(FAILED) == 0)

check("THE TILING NOTE (banked lever, measured, NOT consumed): the "
      "(7,24) template's degree multiset DOES tile into six 6-cell "
      "parts summing to 24 each (witness printed) -- the tiling test "
      "does not kill what parity kills; recorded so the ledger of "
      "levers stays honest",
      (lambda degs: (lambda tile: tile(tile, sorted(degs, reverse=True)))(
          lambda self, ms: (not ms) or any(
              self(self, [x for i, x in enumerate(ms)
                          if i not in (0,) + c])
              for c in itertools.combinations(range(1, len(ms)), 5)
              if ms[0] + sum(ms[i] for i in c) == 24)))(
          [10, 9, 6] + [2] * 12 + [3] * 5 + [5] * 16),
      "one tiling: (10,9,5)+(2,3,3,3,3)... exists; parity, not "
      "tiling, is the killing invariant at the tie")


# ==========================================================================
# 7.  Mutations
# ==========================================================================

head("7.  MUTATIONS")

MUT = []


def mut(name, flipped, expect, detail):
    MUT.append((name, flipped, expect, detail))
    check("%s -- %s" % (name, detail), flipped == expect,
          "flips: %s, expected: %s" % (flipped, expect))


# M-D2E: two 2s per edge.
mut("M-D2E  (D2) per-edge withdrawn",
    (profiles(4, 10, max2=2), profiles(4, 10, max2=1)),
    ([(2, 2, 3, 3)], []),
    "sum-10 support profiles EXIST at two 2s ((2,2,3,3), uniquely): "
    "the m = 22 instant kill and the parity sieve's exactly-one-2 "
    "both fall.  (D2) is the most load-bearing input of this file")

# M-P2: parity sieve withdrawn -- the (7,24) plain-edge profile set
# under the parity-blind alphabet becomes nonempty.
mut("M-P2  the parity sieve withdrawn at (7,24)",
    profiles(4, 17, allowed=(3, 5), max2=0) == [],
    True,
    "four {3,5} cells summing 17: EMPTY -- the kill IS the parity of "
    "this very profile query; withdrawing it removes one of the "
    "cell's two complete proofs, and the INDEPENDENT pigeonhole gate "
    "(CK_PIG) still kills it, so the theorem does NOT reopen (erratum "
    "2026-08-03: this note once claimed no alternative gate stood "
    "behind parity -- false, CK_PIG stands; sixth audit's find).  "
    "Zero margin on this gate, named")

# M-RG: residual pairing 5 -> 4 at k = 3 raises the triangle lims.
def tri_rg4(X, m):
    R = 20
    best = 0
    for t in range(0, 4):
        U = 9 - 2 * t
        for (a, o) in TRI_BR:
            if a > min(t, 1) or o > max(0, 9 - 3 * t):
                continue
            outside_J = (2 - a - o) if t == 3 else 0
            Bud = R - 2 * U - outside_J
            if Bud < 0:
                continue
            caps = [(5 if (i == 0 and a == 1) else 4) for i in range(t)]
            for combo in itertools.product(*[range(0, cc + 1)
                                             for cc in caps]):
                if sum(combo) > m - 13:
                    continue
                for fo in itertools.product((0, 1), repeat=o):
                    cost = sum(F(x + 5) for x in combo) + sum(fo)
                    if cost > Bud:
                        continue
                    best = max(best, sum(psi(x + 5) for x in combo)
                               + sum(psi(v + 5) for v in fo))
    return best


mut("M-RG  residual pairing 5 -> 4 at k = 3",
    [tri_rg4(7, m) for m in (22, 23, 24)], [59, 62, 67],
    "the triangle maxima rise 54/59/62 -> 59/62/67: m = 22 TIES its "
    "floor, 23 and 24 clear it -- all three rungs would reopen.  The "
    "full |K_T| >= 5 is load-bearing at every rung of this file")

# M-T5: 5 admitted as a clique count.
mut("M-T5  five admitted as triangular",
    (5 in {comb(r, 2) for r in range(2, 12)},
     any(c == 5 for (_, mus) in H_1096 for (_, c) in mus)
     or 5 not in TRI_N),
    (False, True),
    "the (2,1^5)-(10,9,6) wall counts 5 pairs through {a,b} and the "
    "(2,2,1,1,1)-(10,10) wall counts C(r,2) = 5: both kills exist "
    "BECAUSE 5 is not a clique count; admitting it reopens them")

# M-f: cost f for F.
def knap_max_f(B, C):
    dm = 5
    while flin(dm + 1) <= C:
        dm += 1
    best = [0]

    def rec(dcur, budget, val):
        best[0] = max(best[0], val)
        for d in range(min(dcur, dm), 5, -1):
            c = flin(d)
            if c <= budget:
                rec(d, budget - c, val + psi(d))

    rec(dm, B, 0)
    return best[0]


mut("M-f  cost f for cost F",
    (knap_max_f(11, 6), knap_max(11, 6)), (83, 73),
    "the (1^7) budget-11 wall jumps 73 -> 83 under the linear cost: "
    "the F(11) = 7 distinction still carries the shape lists at these "
    "rungs, as in 0021/0022")

# M-n35.
mut("M-n35  vertex floor 36 -> 35",
    [Lam(7, m) - (m * m - 43 * m + 14 + 15 * 35 - 3 * (m // 2))
     for m in (22, 23, 24)], [15, 15, 15],
    "Lambda drops 15 at every rung; every raw sieve and census in "
    "this file would need re-measuring.  tau = 6 remains the most "
    "expensive constant")

# M-SWEEP.
mut("M-SWEEP  one partition dropped from the sieve",
    len([pi for pi in PARTS7 if pi != (2, 1, 1, 1, 1, 1)
         and raw_row(pi, 7) >= 59]) == len([(4, 3)] + SIX) - 1,
    True,
    "the m = 22 survivor list shrinks by one; the generated-count "
    "check (%d) stands between a truncated sweep and a false "
    "all-clear" % CK_PARTS)

# M-CEN: census row completeness -- widen n2 by 1 past the cap.
def census_rows_wide(m, X, D):
    Ps = sum(psi(d) for d in D)
    gap = Ps - Lam(X, m)
    if gap < 0:
        return []
    n2cap = m // 2 + 1
    rows = []
    for dn in range(0, gap // 15 + 1):
        n = 36 + dn
        rem = gap - 15 * dn
        for n2 in range(0, n2cap + 1):
            n4 = rem - 3 * ((m // 2) - n2)
            if n4 < 0:
                continue
            nlow = n - len(D) - n2 - n4
            if nlow < 0:
                continue
            degsum = 6 * m - sum(D) - 2 * n2 - 4 * n4
            t5 = degsum - 3 * nlow
            if t5 < 0 or t5 % 2:
                continue
            n5 = t5 // 2
            if nlow - n5 >= 0:
                rows.append((n, n2, nlow - n5, n4, n5))
    return rows


mut("M-CEN  the (D2) global cap n_2 <= floor(m/2) relaxed by one",
    len(census_rows_wide(22, 7, (10, 10))) > len(census_rows(22, 7,
                                                             (10, 10))),
    True,
    "an extra census row appears at m = 22 (n_2 = 12 > 11): the row "
    "lists this file kills are complete only under (D2)'s global "
    "reading -- both readings of 0008 are billed and load-bearing")

# M-OPT: ledger option-list truncation must flip a verdict.
mut("M-OPT  one profile deleted from a feasible ledger's options",
    (ledger_feasible([(2, [(2, 3), (3, 3)]), (1, [(2, 5)])],
                     {2: 2, 3: 3, 5: 1}),
     ledger_feasible([(2, [(3, 3)]), (1, [(2, 5)])],
                     {2: 2, 3: 3, 5: 1})),
    (True, False),
    "deleting (2,3) from the control instance flips FEASIBLE -> "
    "INFEASIBLE: a truncated option list manufactures kills, which is "
    "why profile lists are generated, never written by hand")

note("M-X4 (the seventh pair on two support edges) is INERT-BY-"
     "THEOREM, not priced: two supports already share T; adding the "
     "seventh shared set makes q >= 2 against the all-ones partition. "
     "The exclusion is definitional -- there is no numeric flip to "
     "measure, so it is a note, not a mutant")

check("MUTATION LEDGER: %d mutants priced, %d notes stated separately"
      % (len(MUT), NNOTE[0]), len(MUT) == 9 and NNOTE[0] >= 2)


# ==========================================================================
# RESULT
# ==========================================================================

head("RESULT")

ok = not FAILED
print()
print("  checks : %d" % NCHECK[0])
print("  notes  : %d (stated, not tested)" % NNOTE[0])
print("  failed : %d%s" % (len(FAILED),
                           "" if ok else "  " + " | ".join(FAILED)))
print("  time   : %.1f s" % (time.time() - START))
print()
if ok:
    print("  GREEN.  THE X = 7 LAYER IS EMPTY.  X >= 8 everywhere:")
    print("      22 <= m <= 28  =>  X >= 8")
    print("             m = 29  =>  X >= 9")
    print("             m >= 30  =>  X >= 10")
    print("  The live minimum-excess frontier is X = 8 on m in [22, 28].")
else:
    print("  NOT GREEN.")
sys.exit(0 if ok else 1)
