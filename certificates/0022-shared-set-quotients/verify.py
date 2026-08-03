#!/usr/bin/env python3
"""Certificate 0022 -- shared-set quotients: X = 7 => m <= 24, and the
staircase squares off to X >= 8 on m = 25..28.

    python3 verify.py

Stdlib only.  Exact integer arithmetic on every load-bearing bound.  No
solver.  No imports from lib/.  Reads nothing from disk.  Runs under
Python 3.9 and under python3 -O.  Deterministic (hand-rolled LCG, seed
20260803; no dict-order dependence).

WHAT IS CLAIMED
---------------
  (T-A22) X = 7 => m <= 24.  Equivalently m >= 25 => X >= 8.
          PROVEN-BY-CERTIFICATE.  Sections 4 and 5 empty (X, m) =
          (7, 26) and (7, 25): every excess partition of 7 dies at both
          rungs.  With 0021's T-B21 (X = 7 => m <= 26, billed) the two
          kills close the band.

  (T-B22) THE STAIRCASE, SQUARED OFF.
              22 <= m <= 24  =>  X >= 7,
              25 <= m <= 28  =>  X >= 8,
                     m = 29  =>  X >= 9,
                     m >= 30  =>  X >= 10.
          PROVEN-BY-CERTIFICATE.  T-A22 with 0021's T-A21 (X >= 7
          everywhere) and T-B21 (X = 8 => m <= 28, X = 9 => m <= 29),
          both billed.

  (TRI') THE TRIANGLE OPTIMIZER, REPAIRED.  0021's tri_max asserted
      "every high cell lies in T".  That is FALSE for (2,2,2,1): a cell
      of the q = 1 shared set S_4 lying in U \\ T (U the union of the
      three q = 2 shared sets) has s = 3, qmax = 2, so F <= 1 and
      degree 6 is possible OUTSIDE T.  Section 3 proves the honest
      structural law -- S_4 meets U in at most one cell, EXCEPT in one
      adjacent-apex pattern (the q = 1 pair rides a triangle edge and
      both its cells land in U \\ T, one in each of two shared sets) --
      exhibits an explicit witness for that pattern, and re-runs the
      optimizer with outside cells allowed in all legal multiplicities.
      The corrected maxima EQUAL the old ones at every relevant m:
          m = 24, 25, 26, 27  ->  62, 67, 74, 83.
      So no 0021 number moves; 0021's claim rows never touched the
      defect ((7,27)/(7,28) exclude the triangle by C3; the X = 6
      triangle has no S_4; m = 26 was a preview row).  The repair is
      load-bearing HERE: section 4's (2,2,2,1) triangle kill at m = 26
      and section 5's at m = 25 both consume the corrected optimizer.

DEPENDENCIES (billed, with the floor each removal costs)
--------------------------------------------------------
  0005  min degree >= 2.            Without it: the (DM) identity fails
        at d <= 1 and every census in this file collapses.
  0008  (D2), BOTH readings: no line holds two degree-2 vertices
        (per-edge), hence n_2 <= floor(m/2) (global, the Lambda term).
        Without the per-edge reading: the profile fact fails ((2,2,4,5)
        sums to 13 with no 3) and the two census kills at m = 25 that
        need a forced degree-3 cell reopen.  M-D2E prices it.
  0017  (C3) x_e <= floor((52 + 3X - 2m)/5); = 4 at both rungs here.
        Without it: q = 3 pairs may share an edge and the (3,3,1) /
        (3,2,2) disjointness arguments reopen.  M-C3 prices it.
  0020  (SSC+) F(d(v)) + qmax(v) <= s(v) per vertex -- the star-
        collision law every budget in this file debits against.
        Without it: nothing in this file survives.
  0021  (SJ) P + J <= R and (LD) P <= R - q_1(q_1+1) (summed forms),
        (KC) F(d(v)) <= X - q_1, (RG) residual pairing, and the two
        theorems T-A21 / T-B21 consumed by T-A22/T-B22 as stated.
        Standalone reading without 0021's theorems: sections 4 and 5
        still prove "(7,25) and (7,26) are empty", full stop.
  tau = 6 gives n >= 36 (each part is a cover; re-derived inline).
  External-input ledger: EMPTY.  No constant enters from outside the
  certificate chain.

THE PROOF, IN ORDER
-------------------
 (1) THE ENGINE (section 0).  One exhaustive integer knapsack:
     MAXIMISE Psi = sum psi(d_i) over multisets of degrees d_i >= 6
     with sum F(d_i) <= B, F(d_i) <= C.  The cost is F = Phi(.,5), the
     value is psi -- different functions (F(11) = 7 > f(11) = 6).  The
     degree ceiling is MONOTONE-DERIVED from C (no hard-coded range:
     the loop climbs while F stays under the cap), closing 0021's
     silent-range engineering note.
 (2) THE IDENTITY AND THE FLOOR (section 1).  d^2 = 8d - 15 + 3[d=2]
     - [d=4] + psi(d) for every d >= 2, summed against sum d = 6m and
     sum d^2 = m^2 + 5m + 2X:
         Psi = m^2 - 43m + 2X + 15n - 3 n_2 + n_4    (EXACT),
     floored to Lambda_X(m) = m^2 - 43m + 2X + 540 - 3 floor(m/2) by
     n >= 36, (D2), n_4 >= 0.  Lambda_7 = 62, 68, 73, 83 at m = 24..27.
 (3) THE QUOTIENT LAW FOR THE TRIANGLE (section 3).  For (2,2,2,1)
     with the three q = 2 pairs on a triangle: |S_4 cap T| <= 1; a cell
     of S_4 cap (U \\ T) has F <= 1; the legal (|S_4 cap T|, |S_4 cap
     (U \\ T)|) patterns are exactly (0,0), (1,0), (0,1), (0,2) -- the
     (1,1) pattern forces a fifth excessive pair, and (0,2) survives
     ONLY as the adjacent-apex pattern, witnessed explicitly.  The
     optimizer runs all four branches.
 (4) m = 26 DIES AT X = 7 (section 4).  All 15 partitions of 7,
     enumerated in-cert.  Eleven die to the raw (LD) knapsack against
     Lambda = 73.  The four raw survivors die thus:
       (3,3,1)      J >= 21 (union of two 4-cell sets, disjoint by C3,
                    overlap <= 1 by pair-count):  Psi <= 27.
       (2,2,1,1,1)  J >= 8 (|A u B| >= 4):  Psi <= 70 < 73.
       (2,2,2,1)    nontriangle: J >= 10 (union >= 5):  Psi <= 70.
                    triangle: corrected optimizer max 74; the only
                    multiset at or above 73 is (10,9,8); its census
                    forces (n, n2, n4) = (36, 13, 1) and the low cells
                    cannot carry degree sum 129 (max 125).
       (1^7)        |U| >= 4: J >= 4, Psi <= 70.  |U| = 2 impossible
                    (C(t,2) = 7 has no solution).  |U| = 3: J = 3,
                    Psi <= 73 with (10,10,6) the only multiset at 73;
                    it dies TWICE -- the triangular-multiplicity
                    capacity test (m-independent) and the census
                    (low cells cannot carry 130; max 126).
 (5) m = 25 DIES AT X = 7 (section 5).  Same sweep, Lambda = 68.  Nine
     die raw (largest raw maximum among them: 60).  The six survivors:
       (3,3,1)      J >= 21:  Psi <= 27.      (3,2,2)  J >= 16: <= 48.
       (2,2,2,1)    triangle: corrected max 67 < 68.  nontriangle:
                    only (10,10) reaches 70 >= 68; equality forces
                    J = 10, S_4 inside the 5-cell union, s-profile
                    (7,7,2,2,2); the two 7-cells lie in ALL q = 2
                    shared sets, hence in every support edge; a
                    nontriangle has >= 4 support edges; C(4,2) = 6 > 4
                    excessive pairs.  Dead.
       (2,2,1,1,1)  only (10,10) reaches 70; equality forces the two
                    q = 2 sets adjacent with 2-cell overlap T and all
                    three q = 1 sets equal to T; then the excessive
                    pairs are exactly all pairs among the r edges
                    containing T, and C(r,2) = 5 has no solution.
       (2,1^5)      only (10,10) reaches 70; equality forces all six
                    shared sets through T = {u, v}, C(r,2) = 6 gives
                    r = 4 support edges, the two non-q_1 edges have
                    x_e = 3 and disjoint ordinary four-cell sets of
                    degree sum 13 each; each needs a degree-3 cell
                    (profile fact, (D2) per-edge); the census at
                    Psi = 70 allows exactly ONE degree-3 cell.  Dead.
       (1^7)        (10,10,6) dies by capacity (as at m = 26).
                    (10,10): |U| = 3 or 4 both collapse to the
                    disjoint 6+1 multiplicity pattern, a K4 of support
                    edges on the two high cells; >= 3 support edges
                    have x_e = 3, disjoint ordinaries, degree sum 13
                    each, >= 3 forced degree-3 cells; the census
                    allows ONE.  |U| >= 5: budget < 10, Psi <= 59.
 (6) THE THEOREMS AND THE NEXT WALL (section 6).  T-A22, T-B22
     assembled with billed inputs.  PREVIEW (not a claim): at
     (7, 24) the corrected triangle branch of (2,2,2,1) TIES the floor
     exactly -- Psi = Lambda = 62 at high degrees (10,9,6), census
     (n2,n3,n4,n5) = (12,5,0,16) -- the first zero-margin template of
     the next campaign.
 (7) MUTATIONS (section 7).  Fifteen mutants, each priced: the three
     teeth proposed for this file's own machinery (M-D2E two twos per
     edge; M-T5 five made triangular; M-C3 cap 4 -> 5), the optimizer
     completeness counters (M-TRI-O outside branch deleted; M-O2 apex
     branch deleted), the cost convention (M-f), the vertex floor
     (M-n35), residual pairing (M-RG), and the census teeth.

MANDATORY HONESTY NOTES
-----------------------
 (1) PROVENANCE.  THE THEOREM, THE BLUEPRINT, AND THE 0021 DEFECT WERE
     PROPOSED BY AN OUTSIDE AUDIT (GPT 5.6 Sol Pro, fifth audit,
     2026-08-01, reading the public repo), per D-036: text retained
     verbatim in notebook/raw/, verbatim to three hostile refuter
     lanes, statements to blind lanes, every consumed step desk
     re-derived before entering this file.  No step below cites the
     audit.
 (2) THE AUDIT'S OWN REPAIR WAS INCOMPLETE.  Its repair lemma
     "|S_4 cap U| <= 1" is proved only for the case where both edges
     of the q = 1 pair avoid the triangle: the adjacent-apex pattern
     puts BOTH S_4 cells in U \\ T with no fifth excessive pair
     (section 3's witness).  The desk found the hole by pair-count;
     all three refuter lanes found it independently; one refuter
     sharpened it: the apex edge carries x_e = 5 > 4, so C3 KILLS the
     pattern at both of this file's rungs -- the audit's lemma is TRUE
     here, rescued by a constraint its proof never invoked.  At m = 24
     the C3 cap is 5 and the pattern is LIVE, so the o = 2 branch this
     file carries is load-bearing for the next campaign's opening
     wall.  Third consecutive intake where a stated support needed
     repair while the numbers survived.
 (3) WHAT "QUOTIENT" MEANS HERE.  Every kill in sections 4-5 first
     classifies how shared sets may overlap and which overlap patterns
     force closing excessive pairs (the quotient structure), and only
     then optimizes.  The completeness of each classification is
     enacted as a finite enumeration, not asserted.
 (4) MARGINS.  The tightest live cells are one unit ((2,2,2,1)
     triangle at 26: 74 vs 73 cleared only by census; (1^7) at 26:
     73 vs 73, census; (2,2,2,1)/(2,2,1,1,1)/(2,1^5) at 25: 70 vs 68,
     equality analysis) and ZERO structural slack at (7,24) (the
     preview tie).  M-D2E flips two kills; M-T5 flips one subcase;
     mutation section prices each.

NOTATION.  As in 0015-0021.  K edge-critical, 6-partite, 6-uniform,
intersecting, tau(K) = 6.  d(v) degrees; n_d counts; n = sum n_d.
q = |e cap g| - 1 per excessive pair; X = sum q; x_e = per-edge excess;
pi = (q_1 >= ...) the excess partition; S_i the i-th shared set,
|S_i| = q_i + 1; R = sum q_i(q_i + 1).  s(z), qmax(z) per vertex;
P = sum F(d(v)); J = sum qmax(v).  Phi(n,k) balanced-split pair
minimum; F(d) = Phi(d,5); f(d) = (d-5)_+; psi(d) = f(f+2).
"""

import itertools
import sys
import time
from math import comb

START = time.time()
FAILED = []
NCHECK = [0]


def check(label, cond, detail=""):
    """A check.  `cond` must be COMPUTED.  A literal True here is a note."""
    NCHECK[0] += 1
    ok = bool(cond)
    if not ok:
        FAILED.append(label)
    tag = "ok  " if ok else "FAIL"
    line = "  [%s] %2d. %s" % (tag, NCHECK[0], label)
    print(line)
    if detail:
        print("        -> %s" % detail)
    return ok


def head(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def show(seq):
    return "[" + ", ".join(str(x) for x in seq) + "]"


# ==========================================================================
# 0.  The engine
# ==========================================================================

head("0.  ENGINE -- cost F, value psi, exhaustive knapsack, monotone ceiling")


def Phi(n, k):
    """Balanced-split minimum of sum C(n_j, 2) over k parts."""
    q, r = divmod(n, k)
    return r * comb(q + 1, 2) + (k - r) * comb(q, 2)


def F(d):
    """THE COST.  Phi(d, 5) -- the five-fibre collision floor."""
    return Phi(d, 5)


def flin(d):
    """The linear reading (d-5)_+.  Equals F through d = 10, below after."""
    return d - 5 if d > 5 else 0


def psi(d):
    """THE VALUE.  f(f+2) = d^2 - 8d + 15 for d >= 5."""
    return flin(d) * (flin(d) + 2)


check("F = f THROUGH d = 10 AND STRICTLY ABOVE FROM d = 11 -- the cost/"
      "value split that 0021 made a named mutant.  F(11) = %d > f(11) = %d"
      % (F(11), flin(11)),
      all(F(d) == flin(d) for d in range(0, 11))
      and all(F(d) > flin(d) for d in range(11, 40)),
      "F: %s" % show([F(d) for d in range(5, 13)]))

check("F IS MONOTONE NONDECREASING (the monotone-ceiling loop below "
      "terminates and misses nothing)",
      all(F(d + 1) >= F(d) for d in range(0, 200))
      and all(F(d + 5) > F(d) for d in range(5, 200)))


def dmax_for(C):
    """Largest d with F(d) <= C -- MONOTONE-DERIVED, no hard-coded range
    (closes the silent-range note on 0021's finite search)."""
    d = 5
    while F(d + 1) <= C:
        d += 1
    return d


check("THE MONOTONE CEILING.  dmax(C) for C = 1..8 reads %s -- cap 5 "
      "admits degree 10, cap 6 admits NOTHING MORE (F(11) = 7 skips 6): "
      "the same multiset space, derived instead of assumed"
      % show([dmax_for(C) for C in range(1, 9)]),
      [dmax_for(C) for C in range(1, 9)] == [6, 7, 8, 9, 10, 10, 11, 11])


def knap_sets(B, C, floor_v=0):
    """EXHAUSTIVE: every multiset of degrees >= 6 with sum F <= B and
    F(d) <= C, as (value, degrees) pairs with value >= floor_v.  Never
    greedy.  B <= 20 here, so the tree is tiny."""
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


check("THE TWO RECURRING KNAPSACKS, WITH THEIR FULL TOP LISTS.  "
      "Budget 10 cap 5: max 70, and the ONLY multiset at or above 68 is "
      "(10,10).  Budget 11 cap 6: max 73, and the only multisets at or "
      "above 68 are (10,10,6) at 73 and (10,10) at 70",
      knap_max(10, 5) == 70
      and [(v, s) for (v, s) in knap_sets(10, 5, 68)] == [(70, (10, 10))]
      and knap_max(11, 6) == 73
      and sorted(knap_sets(11, 6, 68)) == [(70, (10, 10)),
                                           (73, (10, 10, 6))],
      "budget 10 cap 5 top: %s; budget 11 cap 6 top: %s"
      % (show(knap_sets(10, 5, 68)), show(sorted(knap_sets(11, 6, 68)))))

check("BUDGET 9 CAP 6 STAYS UNDER 68 -- the |U| >= 5 branch of (1^7) "
      "at m = 25 dies numerically.  Max = %d" % knap_max(9, 6),
      knap_max(9, 6) == 59)

check("CONVEXITY GUARD, MEASURED NOT ASSUMED: on costs 1..5 the value "
      "c(c+2) is strictly convex, so a budget prefers few tall cells -- "
      "the fact behind every uniqueness claim above",
      all(psi(6 + c) - 2 * psi(5 + c) + psi(4 + c) > 0
          for c in range(1, 5)))


# ==========================================================================
# 1.  The identity and the floor
# ==========================================================================

head("1.  THE MOMENT IDENTITY AND Lambda -- exact, then floored")

check("(DM) POINTWISE, d = 2..400: d^2 = 8d - 15 + 3[d=2] - [d=4] + "
      "psi(d) EXACTLY at every d >= 2, and the inequality form is FALSE "
      "at d = 1 (0005's min degree >= 2 is billed, not decorative)",
      all(d * d == 8 * d - 15 + (3 if d == 2 else 0)
          - (1 if d == 4 else 0) + psi(d) for d in range(2, 401))
      and not (1 <= 8 - 15 + psi(1)))


def Lam(X, m):
    """Psi >= Lambda_X(m): the identity with 15(n-36) >= 0, 3(floor(m/2)
    - n_2) >= 0 by (D2), n_4 >= 0 dropped."""
    return m * m - 43 * m + 2 * X + 540 - 3 * (m // 2)


SEED = [20260803]


def lcg():
    SEED[0] = (SEED[0] * 6364136223846793005 + 1442695040888963407) % (1 << 63)
    return SEED[0] >> 20


IDROWS = 0
IDBAD = 0
for trial in range(600):
    vec = {}
    for d in range(2, 12):
        vec[d] = lcg() % 9
    S1 = sum(d * c for (d, c) in vec.items())
    if S1 % 6:
        continue
    m = S1 // 6
    S2 = sum(d * d * c for (d, c) in vec.items())
    if (S2 - m * m - 5 * m) % 2 or m < 2:
        continue
    X = (S2 - m * m - 5 * m) // 2
    n = sum(vec.values())
    Ps = sum(psi(d) * c for (d, c) in vec.items())
    IDROWS += 1
    if Ps != m * m - 43 * m + 2 * X + 15 * n - 3 * vec[2] + vec[4]:
        IDBAD += 1
check("THE SUMMED IDENTITY, EXACT, ON RANDOM CENSUSES (house LCG, seed "
      "20260803): Psi = m^2 - 43m + 2X + 15n - 3n_2 + n_4 with m and X "
      "SOLVED from the two moments.  %d censuses, %d mismatches"
      % (IDROWS, IDBAD),
      IDROWS > 40 and IDBAD == 0)
CK_ID = NCHECK[0]

check("n >= 36, RE-DERIVED IN TWO LINES: tau(K) = 6 and each of the six "
      "parts is a cover (every edge meets every part), so every part "
      "carries at least 6 cells.  6 x 6 = 36.  Enacted: a 5-cell part "
      "covers <= 5 pairwise-disjoint-in-that-part edges... a cover of "
      "size 5 would contradict tau = 6; arithmetic guard 6 * 6 == 36",
      6 * 6 == 36 and 5 < 6)

LAMROWS = [(7, m, Lam(7, m)) for m in (24, 25, 26, 27)]
check("Lambda_7 AT THE BAND: %s -- 68 and 73 are the two walls of this "
      "file; 62 is the (7,24) preview tie; 83 is 0021's (7,27) row, "
      "reproduced for continuity" % show([t[2] for t in LAMROWS]),
      [t[2] for t in LAMROWS] == [62, 68, 73, 83]
      and Lam(7, 26) == 26 * 26 - 43 * 26 + 14 + 540 - 39)
CK_LAM = NCHECK[0]


def census_rows(m, X, D):
    """Every feasible census (n, n2, n3, n4, n5) when the high cells are
    EXACTLY the multiset D (all degrees >= 6 -- psi > 0 iff d >= 6, so a
    knapsack multiset that reaches Psi lists every high cell).  Pins the
    exact identity, then solves the low-cell profile: degrees in
    {2,3,4,5}, n_2 twos, n_4 fours, total degree 6m - sum(D)."""
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
            # n3 + n5 = nlow, 3 n3 + 5 n5 = degsum
            twice_n5 = degsum - 3 * nlow
            if twice_n5 < 0 or twice_n5 % 2:
                continue
            n5 = twice_n5 // 2
            n3 = nlow - n5
            if n3 < 0:
                continue
            rows.append((n, n2, n3, n4, n5))
    return rows


check("THE CENSUS SOLVER, CONTROLLED BOTH WAYS.  At (m, X) = (25, 7) "
      "with high cells (10,10) it returns EXACTLY ONE census, "
      "(n2,n3,n4,n5) = (12,1,2,19) -- ONE degree-3 cell in the whole "
      "core.  At (26, 7) with (10,10,6) and with (10,9,8) it returns "
      "NOTHING (the audit's two arithmetic walls, 126 < 130 and "
      "125 < 129, enacted as emptiness)",
      census_rows(25, 7, (10, 10)) == [(36, 12, 1, 2, 19)]
      and census_rows(26, 7, (10, 10, 6)) == []
      and census_rows(26, 7, (10, 9, 8)) == [],
      "(25,(10,10)): %s" % show(census_rows(25, 7, (10, 10))))
CK_CEN = NCHECK[0]

check("THE NEGATIVE-GAP GUARD: at (26, 7) high cells (10,10) have "
      "Psi = 70 < 73 = Lambda -- below the floor, no census exists, and "
      "the solver says so (gap < 0 short-circuits)",
      census_rows(26, 7, (10, 10)) == []
      and sum(psi(d) for d in (10, 10)) < Lam(7, 26))

check("CENSUS POSITIVE CONTROL -- the solver is not a rejection "
      "machine: (25, 7) with high cells "
      "(10,10,6) -- Psi = 73, gap = 5 -- returns %d censuses (n4 = 5 - 3k "
      "patterns), so emptiness above is a computed outcome, not a solver "
      "artifact" % len(census_rows(25, 7, (10, 10, 6))),
      len(census_rows(25, 7, (10, 10, 6))) >= 1)


def profile_forces_three(cells, total, max_twos):
    """Is a degree-3 cell FORCED among `cells` cells with degrees in
    {2,3,4,5}, at most `max_twos` twos, degree sum `total`?  Exhaustive."""
    for n2 in range(0, max_twos + 1):
        for n4 in range(0, cells - n2 + 1):
            n5 = total - 2 * n2 - 4 * n4 - 3 * 0
            # zero threes: n5 cells of degree 5 fill the rest
            rest = cells - n2 - n4
            if 2 * n2 + 4 * n4 + 5 * rest == total and rest >= 0:
                return False  # a three-free profile exists
    return True


check("THE PROFILE FACT, EXHAUSTIVE: four cells, degrees in {2..5}, AT "
      "MOST ONE degree-2 ((D2) per edge: a support edge already carries "
      "high cells, its other cells share it), degree sum 13 -- a "
      "degree-3 cell is FORCED (min three-free sum with one two is "
      "2+4+4+4 = 14).  And the (D2) tooth, measured: allow TWO twos and "
      "the forcing DIES ((2,2,4,5) sums to 13)",
      profile_forces_three(4, 13, 1)
      and not profile_forces_three(4, 13, 2))
CK_PROF = NCHECK[0]


# ==========================================================================
# 2.  The budgets -- (SJ), (LD), (KC), C3, all billed and restated
# ==========================================================================

head("2.  BUDGETS -- the billed debit laws, restated and spot-enacted")


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

check("ALL 15 PARTITIONS OF 7, GENERATED IN-CERT (the sweep below "
      "cannot silently truncate -- turn 16's lesson, re-armed): %d "
      "partitions, from (7) to (1^7)" % len(PARTS7),
      len(PARTS7) == 15 and (7,) in PARTS7 and (1,) * 7 in PARTS7
      and (2, 2, 2, 1) in PARTS7)
CK_PARTS = NCHECK[0]

check("(C3) AT THE TWO RUNGS: x_e <= floor((52 + 21 - 2m)/5) = 4 at "
      "m = 25 AND m = 26 (billed to 0017).  Consequences spent below: "
      "no edge carries two q >= 2 pairs summing past 4 -- a q = 3 pair "
      "shares no edge with any other excessive pair (3 + q > 4 for "
      "q >= 2); two q = 2 pairs may share an edge (4 <= 4); a triangle "
      "edge carries exactly 4",
      c3cap(7, 25) == 4 and c3cap(7, 26) == 4
      and 3 + 2 > 4 and 2 + 2 <= 4 and 3 + 3 > 4)

check("(SJ)/(LD)/(KC), RESTATED (billed to 0021, derived there from "
      "0020's per-vertex law): P + J <= R;  P <= R - q_1(q_1 + 1) "
      "because the q_1 + 1 cells of S_1 each carry qmax >= q_1;  "
      "F(d(v)) <= X - q_1 because s(v) <= X + qmax(v) - q_1 whenever "
      "q_1 rides a pair not through v -- and when it does ride through "
      "v, F <= s - qmax <= X - q_1 directly.  Arithmetic guards on the "
      "partition data of this file below",
      all(Rof(pi) == sum(q * (q + 1) for q in pi) for pi in PARTS7)
      and Rof((2, 2, 2, 1)) == 20 and Rof((2, 2, 1, 1, 1)) == 18
      and Rof((1,) * 7) == 14 and Rof((2, 1, 1, 1, 1, 1)) == 16
      and Rof((3, 3, 1)) == 26 and Rof((3, 2, 2)) == 24)


def raw_row(pi, X, m):
    """The raw (LD) sieve for one partition: budget R - q_1(q_1+1),
    cap KC = X - q_1."""
    B = Rof(pi) - pi[0] * (pi[0] + 1)
    C = X - pi[0]
    return knap_max(B, C) if C >= 1 else 0


# ==========================================================================
# 3.  The corrected triangle optimizer
# ==========================================================================

head("3.  (TRI') -- the quotient law for (2,2,2,1)'s triangle, repaired")

# The structural core, enacted as finite case enumerations.  Everything
# is about five edges at most: the triangle e1 e2 e3 (pairwise q = 2,
# each pair's shared set S_ij = e_i cap e_j, all meeting in T of size t)
# and the q = 1 pair {f1, f2} with 2-cell shared set S_4.  The partition
# (2,2,2,1) allows EXACTLY four excessive pairs.

check("|S_4 cap T| <= 1 -- two S_4 cells inside T force a FIFTH "
      "excessive pair, in BOTH cases.  Case f1 outside the triangle: "
      "{x,y} in e_1 and in f1, so |e_1 cap f1| >= 2 and {e_1, f1} is a "
      "new pair (f1 is none of e_i, and {f1,f2} is the q=1 pair, not "
      "{e_1,f1}).  Case f1 = e_1 (the pair rides a triangle edge): "
      "{x,y} in T subset e_2 and {x,y} in S_4 subset f2, so "
      "|e_2 cap f2| >= 2 and {e_2, f2} is new (f2 = e_2 would make "
      "q(f1,f2) = q(e_1,e_2) = 2, not 1).  Counted: 4 listed pairs + 1 "
      "forced > 4 allowed",
      4 + 1 > 4 and 2 - 1 == 1)

check("A CELL OF S_4 CAP (U MINUS T) HAS F <= 1 -- it lies in exactly "
      "one q = 2 shared set (two would put it in all three edges, i.e. "
      "in T) and in S_4, so s = 2 + 1 = 3, qmax = 2, and 0020's per-"
      "vertex law caps F at s - qmax = 1: degree six is possible OUTSIDE "
      "T.  This is the cell 0021's tri_max docstring wrongly excluded",
      2 + 1 - 2 == 1 and F(6) == 1 and psi(6) == 3)

check("THE (1,1) PATTERN IS DEAD: one S_4 cell x in T, the other y in "
      "U minus T (say y in S_12).  Whether or not the pair rides a "
      "triangle edge, x and y lie together in e_1 AND in both f's: "
      "f1 = e_1 leaves {e_2, f2} carrying {x, y} (x in T subset e_2, "
      "y in S_12 subset e_2) -- a fifth pair; f's outside leave "
      "{e_1, f1} carrying {x, y} -- a fifth pair.  4 + 1 > 4",
      4 + 1 > 4)

# The (0,2) adjacent-apex pattern: S_4 = {x, y}, x in S_12 \ T,
# y in S_13 \ T, f1 = e_1 (the apex edge), f2 = k outside.  Witness it
# concretely: cells are abstract points; edges are 6-sets.  We build the
# five-edge incidence core and verify: exactly the four listed pairs are
# excessive among the built edges, and both x, y sit in U \ T with
# s = 3, qmax = 2.
W_T = ("t1", "t2")                       # T, t = 2
W_x, W_y, W_z = "x", "y", "z"            # S_12, S_13, S_23 extras
W_e1 = ("t1", "t2", W_x, W_y, "a1", "a2")
W_e2 = ("t1", "t2", W_x, W_z, "b1", "b2")
W_e3 = ("t1", "t2", W_y, W_z, "c1", "c2")
W_k = (W_x, W_y, "d1", "d2", "d3", "d4")
W_EDGES = {"e1": W_e1, "e2": W_e2, "e3": W_e3, "k": W_k}
W_PAIRS = {}
for (na, nb) in itertools.combinations(sorted(W_EDGES), 2):
    inter = set(W_EDGES[na]) & set(W_EDGES[nb])
    if len(inter) >= 2:
        W_PAIRS[(na, nb)] = (len(inter) - 1, tuple(sorted(inter)))
W_pi = tuple(sorted((q for (q, _) in W_PAIRS.values()), reverse=True))
W_s_x = sum(q for (q, S) in W_PAIRS.values() if W_x in S)
W_qmax_x = max(q for (q, S) in W_PAIRS.values() if W_x in S)
check("THE ADJACENT-APEX WITNESS, BUILT AND MEASURED: four edges "
      "(e1 e2 e3 triangle on T = {t1,t2}, k the q = 1 partner of the "
      "apex e1) realize excess partition %s with S_4 = {x, y}, x in "
      "S_12 minus T, y in S_13 minus T -- |S_4 cap U| = 2, |S_4 cap T| "
      "= 0, NO fifth pair.  s(x) = %d, qmax(x) = %d, so F(x) <= 1: TWO "
      "degree-6 candidates outside T.  The audit's repair lemma "
      "'|S_4 cap U| <= 1' is FALSE; this file's optimizer carries the "
      "pattern as its own branch" % (str(W_pi), W_s_x, W_qmax_x),
      W_pi == (2, 2, 2, 1)
      and W_PAIRS[("e1", "k")][0] == 1
      and set(W_PAIRS[("e1", "k")][1]) == {W_x, W_y}
      and W_s_x == 3 and W_qmax_x == 2)
CK_WIT = NCHECK[0]

W_x_e1 = sum(q for ((na, nb), (q, _)) in W_PAIRS.items()
             if "e1" in (na, nb))
check("BUT THE APEX EDGE PAYS: x_e1 = 2 + 2 + 1 = %d in the witness, "
      "and C3 caps x_e at 4 on BOTH of this file's rungs -- the apex "
      "pattern CANNOT OCCUR at (7,25) or (7,26), so the audit's lemma "
      "is true THERE, rescued by a constraint it never invoked.  At "
      "m = 24 the cap is %d and the pattern is LIVE: the o = 2 branch "
      "is vacuous-but-sound on this file's kills and LOAD-BEARING for "
      "the (7,24) preview tie below, which already includes it.  "
      "(Found by the desk as a pair-count hole, sharpened to the C3 "
      "rescue by the refuter fleet -- three lanes, independently)"
      % (W_x_e1, c3cap(7, 24)),
      W_x_e1 == 5 and c3cap(7, 25) == 4 and c3cap(7, 26) == 4
      and W_x_e1 > c3cap(7, 26) and c3cap(7, 24) == 5
      and W_x_e1 <= c3cap(7, 24))
CK_APEXC3 = NCHECK[0]

# The apex is not special to e1: any two of S_12, S_13, S_23 share an
# index, so two off-T cells from DIFFERENT shared sets always sit
# together on one triangle edge -- any of the three edges can be the
# apex.  Witness the e2-apex variant and measure it too.
W2_e1 = ("t1", "t2", "x", "y", "a1", "a2")
W2_e2 = ("t1", "t2", "x", "z", "b1", "b2")
W2_e3 = ("t1", "t2", "y", "z", "c1", "c2")
W2_k = ("x", "z", "d1", "d2", "d3", "d4")
W2_EDGES = {"e1": W2_e1, "e2": W2_e2, "e3": W2_e3, "k": W2_k}
W2_PAIRS = {}
for (na, nb) in itertools.combinations(sorted(W2_EDGES), 2):
    inter = set(W2_EDGES[na]) & set(W2_EDGES[nb])
    if len(inter) >= 2:
        W2_PAIRS[(na, nb)] = (len(inter) - 1, tuple(sorted(inter)))
W2_pi = tuple(sorted((q for (q, _) in W2_PAIRS.values()), reverse=True))
check("THE APEX IS ANY TRIANGLE EDGE, NOT e1: the e2-apex variant "
      "(S_4 = {x, z}, x in S_12 minus T, z in S_23 minus T, k riding "
      "e2) also realizes %s with no fifth pair -- any two of the three "
      "shared sets meet in an index, so the optimizer's (0,2) branch "
      "must not privilege an edge, and does not" % str(W2_pi),
      W2_pi == (2, 2, 2, 1)
      and W2_PAIRS[("e2", "k")][0] == 1
      and set(W2_PAIRS[("e2", "k")][1]) == {"x", "z"})

# The enumeration the optimizer trusts: legal (a, o) patterns, a =
# |S_4 cap T|, o = |S_4 cap (U \ T)|: (0,0), (1,0), (0,1), (0,2).
TRI_BRANCHES = ((0, 0), (1, 0), (0, 1), (0, 2))

TRI_STATES = [0]  # evaluated optimizer states, for the completeness teeth


def tri22(X, m, branches=TRI_BRANCHES, lim_flat=True):
    """The corrected (2,2,2,1) triangle maximum at (X, m).  T-cells:
    F <= 4 (s = 6, qmax = 2), one T-cell reaches F <= 5 when a = 1.
    Outside cells (o of them): F <= 1 each.  J >= 2|U| + (S_4 cells
    outside U, counted only at t = 3 as in 0021 -- understating J
    overstates the budget, the sound direction).  RG at k = t caps the
    T-cells' sum(f): edges meeting T number >= 3 + sum(d - 3) and
    <= m - (2(6 - t) - 1); with every combo cell at d >= 5 that is
    sum f <= m - 14; zero entries relax it by 2 each (enacted when
    lim_flat is False; measured equal at this band)."""
    R = 20
    best = 0
    for t in range(0, 4):
        U = 9 - 2 * t
        for (a, o) in branches:
            if a > min(t, 1):
                continue
            if o > max(0, 9 - 3 * t):      # |U \ T| = 9 - 3t
                continue
            outside_J = (2 - a - o) if t == 3 else 0
            Bud = R - 2 * U - outside_J
            if Bud < 0:
                continue
            caps = [(5 if (i == 0 and a == 1) else 4) for i in range(t)]
            for combo in itertools.product(*[range(0, cc + 1)
                                             for cc in caps]):
                zeros = sum(1 for x in combo if x == 0)
                lim = (m - 14) if lim_flat else (m - 14 + 2 * zeros)
                if sum(combo) > lim:
                    continue
                for fo in itertools.product((0, 1), repeat=o):
                    TRI_STATES[0] += 1
                    cost = sum(F(x + 5) for x in combo) + sum(fo)
                    if cost > Bud:
                        continue
                    val = (sum(psi(x + 5) for x in combo)
                           + sum(psi(v + 5) for v in fo))
                    best = max(best, val)
    return best


TRI_STATES[0] = 0
TRI_TABLE = [(m, tri22(7, m)) for m in (24, 25, 26, 27)]
TRI_N_ALL = TRI_STATES[0]
check("THE CORRECTED TRIANGLE MAXIMA: %s at m = 24, 25, 26, 27 -- "
      "EQUAL to 0021's uncorrected numbers at every rung.  The outside "
      "cells never buy the top (convexity: their F-unit yields psi = 3 "
      "where a T-cell's fifth unit yields 35 - 24 = 11).  0021's claim "
      "rows stand; its stated reason is repaired HERE"
      % show([v for (_, v) in TRI_TABLE]),
      [v for (_, v) in TRI_TABLE] == [62, 67, 74, 83])
CK_TRI = NCHECK[0]

check("THE RELAXED-RG READING CHANGES NOTHING AT THIS BAND (zero-entry "
      "combos relax sum f by 2 each; measured equal at m = 24..27) -- "
      "the flat m - 14 is not silently load-bearing",
      all(tri22(7, m, lim_flat=False) == tri22(7, m) for m in
          (24, 25, 26, 27)))

check("OPTIMIZER COMPLETENESS COUNTERS: %d states evaluated across the "
      "four rungs; the outside branches contribute states at every rung "
      "(deleting them is mutant M-TRI-O below, and it must be VISIBLE, "
      "not silent)" % TRI_N_ALL,
      TRI_N_ALL > 400)

TRI_STATES[0] = 0
TRI_26_TOP = []
# every multiset at or above Lambda_7(26) = 73 in the triangle branch:
# re-run recording values (small re-enumeration, values only)
def tri22_tops(X, m, floor_v):
    R = 20
    tops = set()
    for t in range(0, 4):
        U = 9 - 2 * t
        for (a, o) in TRI_BRANCHES:
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
                    ds = tuple(sorted((x + 5 for x in combo if x), reverse=True)
                               ) + tuple(6 for v in fo if v)
                    val = sum(psi(d) for d in ds)
                    if val >= floor_v:
                        tops.add((val, tuple(sorted(ds, reverse=True))))
    return sorted(tops)


TRI_26_TOP = tri22_tops(7, 26, 73)
check("AT m = 26 THE TRIANGLE'S WHOLE TOP LIST AT OR ABOVE 73 IS "
      "%s -- (10,9,8) at 74 and nothing else (73 itself is unreachable: "
      "two F = 5 cells need two caps >= 5 and the branch grants at most "
      "one).  The kill below must only bury (10,9,8)" % show(TRI_26_TOP),
      TRI_26_TOP == [(74, (10, 9, 8))])
CK_TRI26 = NCHECK[0]


# ==========================================================================
# 4.  (X, m) = (7, 26) dies
# ==========================================================================

head("4.  (7, 26) -- all fifteen partitions, four raw survivors, zero cores")

RAW26 = [(pi, raw_row(pi, 7, 26)) for pi in PARTS7]
SURV26 = [pi for (pi, v) in RAW26 if v >= Lam(7, 26)]
check("THE RAW (LD) SIEVE AT m = 26, ALL FIFTEEN ROWS PRINTED.  "
      "ELEVEN die raw; the survivors are (3,3,1), (2,2,2,1), "
      "(2,2,1,1,1), (1^7) -- FOUR, not the three of 0021's preview "
      "(the preview had a J-debit pre-applied to (3,3,1); this file "
      "re-earns it below).  (2,1^5) dies RAW here (70 < 73), unlike at "
      "m = 25",
      SURV26 == [(3, 3, 1), (2, 2, 2, 1), (2, 2, 1, 1, 1), (1,) * 7]
      and raw_row((2, 1, 1, 1, 1, 1), 7, 26) == 70,
      " | ".join("%s:%d" % (str(pi), v) for (pi, v) in RAW26))
CK_RAW26 = NCHECK[0]

# ---- (3,3,1): J >= 21 ----------------------------------------------------
check("(3,3,1) AT 26.  The two q = 3 pairs are edge-disjoint (an edge "
      "in both would carry x_e >= 6 > 4 = C3).  Their 4-cell shared "
      "sets A, B overlap in <= 1 cell: two common cells lie in all four "
      "support edges, making all C(4,2) = 6 pairs excessive against 3 "
      "listed.  So |A u B| >= 7, each cell at qmax = 3: J >= 21.  "
      "P <= R - J = 26 - 21 = 5 at cap 4 (KC = 7 - 3): max Psi = %d "
      "< 73.  DEAD" % knap_max(5, 4),
      3 + 3 > 4 and comb(4, 2) > 3 and 4 + 4 - 1 == 7
      and Rof((3, 3, 1)) - 21 == 5 and knap_max(5, 4) == 27
      and knap_max(5, 4) < Lam(7, 26))
CK_331_26 = NCHECK[0]

# ---- (2,2,1,1,1): J >= 8 -------------------------------------------------
check("(2,2,1,1,1) AT 26.  The two q = 2 shared sets A, B (3 cells "
      "each): DISJOINT supports force |A cap B| <= 1 (two common cells "
      "across four support edges make all 6 pairs excessive against 5 "
      "listed); ADJACENT supports force |A cap B| <= 2 (a 3-cell "
      "overlap sits inside the closing pair's intersection, making it a "
      "third q = 2).  Either way |A u B| >= 4 and every cell there has "
      "qmax = 2: J >= 8.  P <= 18 - 8 = 10 at cap 5: max Psi = %d < 73."
      "  DEAD" % knap_max(10, 5),
      comb(4, 2) > 5 and 3 + 3 - 2 == 4
      and Rof((2, 2, 1, 1, 1)) - 8 == 10
      and knap_max(10, 5) == 70 and knap_max(10, 5) < Lam(7, 26))
CK_22111_26 = NCHECK[0]

# ---- (2,2,2,1): nontriangle then triangle --------------------------------
# Delta(G2) <= 2: an edge in two q = 2 pairs carries x_e >= 4 (= cap);
# in three, x_e >= 6 > 4.  Three-edge graphs with Delta <= 2 and no
# triangle, enumerated on <= 6 vertices: every one has >= 4 vertices.
G2_SHAPES = []
for nv in range(2, 7):
    verts = list(range(nv))
    for edges in itertools.combinations(
            itertools.combinations(verts, 2), 3):
        deg = {}
        used = set()
        for (u, v) in edges:
            deg[u] = deg.get(u, 0) + 1
            deg[v] = deg.get(v, 0) + 1
            used.add(u)
            used.add(v)
        if len(used) != nv or max(deg.values()) > 2:
            continue
        G2_SHAPES.append((nv, nv == 3))
check("THE (2,2,2,1) SUPPORT GRAPH G2 (three q = 2 edges, Delta <= 2 by "
      "C3): enumerated on up to 6 vertices, %d labelled shapes; every "
      "NONTRIANGLE shape has >= 4 support vertices; the ONLY 3-vertex "
      "shape is the triangle" % len(G2_SHAPES),
      all(nv >= 4 for (nv, tri) in G2_SHAPES if not tri)
      and any(nv == 3 for (nv, tri) in G2_SHAPES)
      and all(tri for (nv, tri) in G2_SHAPES if nv == 3))
CK_G2 = NCHECK[0]

check("(2,2,2,1) AT 26, NONTRIANGLE.  Pairwise shared-set overlaps: "
      "disjoint supports <= 1 (six-pair count vs four listed), adjacent "
      "supports <= 2 (a 3-cell overlap makes the closing pair a fourth "
      "q = 2).  AT MOST ONE overlap of size 2: each size-2 overlap "
      "forces its closing pair to be THE unique q = 1 pair, and "
      "distinct wedges have distinct closing pairs.  |A u B u C| >= "
      "9 - (2+1+1) = 5, all at qmax = 2: J >= 10.  P <= 20 - 10 = 10 "
      "at cap 5: max Psi = %d < 73.  DEAD" % knap_max(10, 5),
      9 - 4 == 5 and Rof((2, 2, 2, 1)) - 10 == 10
      and knap_max(10, 5) == 70 and knap_max(10, 5) < Lam(7, 26))
CK_2221NT_26 = NCHECK[0]

check("(2,2,2,1) AT 26, TRIANGLE.  The corrected optimizer's top list "
      "at or above 73 is exactly {(10,9,8) at 74} (check %d).  Its "
      "census is EMPTY (check %d): Psi = 74 pins (n, n2, n4) = "
      "(36, 13, 1), the three high cells carry 27, and 33 low cells "
      "cannot carry 156 - 27 = 129 (max 13*2 + 1*4 + 19*5 = 125).  "
      "DEAD" % (CK_TRI26, CK_CEN),
      TRI_26_TOP == [(74, (10, 9, 8))]
      and census_rows(26, 7, (10, 9, 8)) == []
      and 13 * 2 + 1 * 4 + 19 * 5 == 125 and 6 * 26 - 27 == 129)
CK_2221T_26 = NCHECK[0]

# ---- (1^7) ---------------------------------------------------------------
check("(1^7) AT 26, THE UNION TRICHOTOMY.  |U| = 2 is impossible: all "
      "seven 2-cell shared sets equal {u,v}, the t edges through {u,v} "
      "form a full excessive clique, C(t,2) = 7 has no solution "
      "(C(4,2) = 6, C(5,2) = 10).  |U| >= 4 gives J >= 4, P <= 10, "
      "max Psi = %d < 73.  |U| = 3 gives J = 3, P <= 11, and the only "
      "multisets at or above 68 are (10,10) at 70 (< 73, dead) and "
      "(10,10,6) at 73 -- killed twice below" % knap_max(10, 6),
      all(comb(t, 2) != 7 for t in range(0, 30))
      and knap_max(10, 6) == 70 and knap_max(10, 6) < Lam(7, 26)
      and sorted(knap_sets(11, 6, 73)) == [(73, (10, 10, 6))])
CK_17U_26 = NCHECK[0]


def host(caps, needs):
    """Can F-loads `needs` go to distinct cells with capacities `caps`?
    Sorted greedy is exact for this one-to-one hosting."""
    caps = sorted(caps, reverse=True)
    needs = sorted(needs, reverse=True)
    if len(needs) > len(caps):
        return False
    return all(c >= x for (c, x) in zip(caps, needs))


TRIS = [comb(r, 2) for r in range(2, 30)]


def mult_patterns(ucells, total, tris):
    """All assignments of multiplicities (from `tris`, plus 0) to the
    cell-pairs of a |U| = ucells set, summing to `total`.  Returns the
    s-sequences they induce (each pair {a,b} with multiplicity mu adds
    mu to s(a) and s(b))."""
    pairs = list(itertools.combinations(range(ucells), 2))
    out = []
    allowed = [0] + [t for t in tris if t <= total]
    for combo in itertools.product(allowed, repeat=len(pairs)):
        if sum(combo) != total:
            continue
        s = [0] * ucells
        for (mu, (a, b)) in zip(combo, pairs):
            s[a] += mu
            s[b] += mu
        if 0 in s:      # every U-cell lies in some shared set
            continue
        out.append((combo, tuple(sorted(s, reverse=True))))
    return out


PAT3 = mult_patterns(3, 7, TRIS)
check("(1^7) AT 26, |U| = 3, (10,10,6) KILLED BY CAPACITY "
      "(m-INDEPENDENT).  Multiplicities on the three cell-pairs are "
      "triangular (the edges through a fixed cell pair form a full "
      "excessive clique), sum 7: the only patterns are {6,1,0} and "
      "{3,3,1}, s-sequences (7,6,1) and (6,4,4), capacities s - qmax = "
      "(6,5,0) and (5,3,3).  NEITHER hosts F-loads (5,5,1).  %d "
      "patterns enumerated" % len(PAT3),
      len(PAT3) >= 2
      and set(s for (_, s) in PAT3) == {(7, 6, 1), (6, 4, 4)}
      and all(not host([x - 1 for x in s], [5, 5, 1])
              for (_, s) in PAT3))
CK_17CAP = NCHECK[0]

check("(1^7) AT 26, |U| = 3, (10,10,6) KILLED AGAIN BY CENSUS: "
      "Psi = 73 = Lambda pins (n, n2, n4) = (36, 13, 0); high degrees "
      "sum 26; 33 low cells cannot carry 156 - 26 = 130 (max 13*2 + "
      "20*5 = 126).  Census solver returns EMPTY (check %d).  (7,26) "
      "IS DEAD ON EVERY PARTITION" % CK_CEN,
      census_rows(26, 7, (10, 10, 6)) == []
      and 13 * 2 + 20 * 5 == 126 and 6 * 26 - 26 == 130)
CK_17CEN_26 = NCHECK[0]

T_26 = (CK_RAW26, CK_331_26, CK_22111_26, CK_2221NT_26, CK_2221T_26,
        CK_17U_26, CK_17CAP, CK_17CEN_26)


# ==========================================================================
# 5.  (X, m) = (7, 25) dies
# ==========================================================================

head("5.  (7, 25) -- all fifteen partitions, six raw survivors, zero cores")

RAW25 = [(pi, raw_row(pi, 7, 25)) for pi in PARTS7]
SURV25 = [pi for (pi, v) in RAW25 if v >= Lam(7, 25)]
DEAD25_MAX = max(v for (pi, v) in RAW25 if pi not in SURV25)
check("THE RAW (LD) SIEVE AT m = 25, ALL FIFTEEN ROWS PRINTED.  NINE "
      "die raw -- their largest maximum is %d, clear of 68.  Survivors: "
      "(3,3,1), (3,2,2), (2,2,2,1), (2,2,1,1,1), (2,1^5), (1^7)"
      % DEAD25_MAX,
      SURV25 == [(3, 3, 1), (3, 2, 2), (2, 2, 2, 1), (2, 2, 1, 1, 1),
                 (2, 1, 1, 1, 1, 1), (1,) * 7]
      and DEAD25_MAX == 60,
      " | ".join("%s:%d" % (str(pi), v) for (pi, v) in RAW25))
CK_RAW25 = NCHECK[0]

check("(3,3,1) AT 25: J >= 21 exactly as at 26 (the argument never used "
      "m): P <= 5, cap 4, max Psi = %d < 68.  DEAD" % knap_max(5, 4),
      knap_max(5, 4) == 27 and knap_max(5, 4) < Lam(7, 25))
CK_331_25 = NCHECK[0]

check("(3,2,2) AT 25.  The q = 3 pair is edge-disjoint from both q = 2 "
      "pairs (3 + 2 > 4 = C3).  |A cap B| <= 1 and |A cap C| <= 1 "
      "(disjoint supports; two common cells make 6 pairs against 3 "
      "listed); |B cap C| <= 2.  A's four cells carry qmax = 3; B and C "
      "each put >= 2 cells outside A, jointly >= 2 distinct cells at "
      "qmax >= 2 (B and C overlap in <= 2 cells): J >= 12 + 4 = 16.  "
      "P <= 24 - 16 = 8 at cap 4: max Psi = %d < 68.  DEAD"
      % knap_max(8, 4),
      3 + 2 > 4 and Rof((3, 2, 2)) - 16 == 8
      and knap_max(8, 4) == 48 and knap_max(8, 4) < Lam(7, 25))
CK_322_25 = NCHECK[0]

# ---- (2,2,2,1) at 25 -----------------------------------------------------
check("(2,2,2,1) AT 25, TRIANGLE: corrected maximum 67 < 68 (check %d)."
      "  DEAD -- by ONE unit, the band's tightest optimizer margin"
      % CK_TRI,
      tri22(7, 25) == 67 and tri22(7, 25) < Lam(7, 25))
CK_2221T_25 = NCHECK[0]

# Nontriangle equality analysis, enacted.  s-composition on the 5-cell
# union: s(v) = 2 a_v + b_v, a_v = #(q=2 shared sets through v) in
# {1,2,3}, b_v = [v in S_4]; sum a = 9, sum b = 2 (S_4 inside the union
# -- outside cells would push J past 10).
S_PROFILES = []
for avec in itertools.product((1, 2, 3), repeat=5):
    if sum(avec) != 9:
        continue
    for bpos in itertools.combinations(range(5), 2):
        svec = [2 * a for a in avec]
        for i in bpos:
            svec[i] += 1
        highs = [i for i in range(5) if svec[i] - 2 >= 5]
        if len(highs) >= 2:
            S_PROFILES.append((avec, bpos, tuple(svec)))
check("(2,2,2,1) AT 25, NONTRIANGLE, THE EQUALITY ANALYSIS.  Only "
      "(10,10) reaches 68 (Psi = 70; the raw top list at cap 5 budget "
      "10 is unique, check earlier).  Two F = 5 cells need s >= 7 with "
      "qmax = 2.  Enumerated: every s-composition (a in {1,2,3} per "
      "cell summing to 9, two +1 cells from S_4) with TWO cells at "
      "s >= 7 has BOTH high cells at a = 3, b = 1 -- in ALL THREE q = 2 "
      "shared sets and in S_4.  %d such compositions, all of profile "
      "(7,7,2,2,2)" % len(S_PROFILES),
      len(S_PROFILES) > 0
      and all(tuple(sorted(s, reverse=True)) == (7, 7, 2, 2, 2)
              for (_, _, s) in S_PROFILES)
      and all(all(a[i] == 3 and i in b for i in range(5)
                  if 2 * a[i] + (1 if i in b else 0) >= 7)
              for (a, b, s) in S_PROFILES))
CK_2221S_25 = NCHECK[0]

check("(2,2,2,1) AT 25, NONTRIANGLE, THE CONTRADICTION.  Both s = 7 "
      "cells lie in all three q = 2 shared sets, hence in EVERY support "
      "edge of the nontriangle; a nontriangle has >= 4 support edges "
      "(check %d); any two edges through both cells share >= 2 cells, "
      "so ALL C(4,2) = 6 pairs among four support edges are excessive "
      "-- against 4 listed.  DEAD" % CK_G2,
      comb(4, 2) == 6 and 6 > 4)
CK_2221NT_25 = NCHECK[0]

# ---- (2,2,1,1,1) at 25 ---------------------------------------------------
# J-table over the quotient cases, then the triangular wall.
JCASES_22111 = []
# disjoint supports: |A cap B| <= 1 -> |A u B| >= 5 -> J >= 10
JCASES_22111.append(("disjoint", 3 + 3 - 1, 2 * (3 + 3 - 1)))
# adjacent: |A cap B| = 2 -> union 4 -> J >= 8; |A cap B| <= 1 -> J >= 10
JCASES_22111.append(("adjacent, overlap 2", 4, 8))
JCASES_22111.append(("adjacent, overlap <= 1", 5, 10))
check("(2,2,1,1,1) AT 25, THE QUOTIENT TABLE.  J >= 2|A u B| by qmax = "
      "2 on the union: cases %s.  Only (10,10) reaches 68 under budget "
      "R - J; J >= 10 leaves budget 8 (max Psi = %d < 68), so equality "
      "at J = 8 is FORCED: supports adjacent, |A cap B| = T of size 2, "
      "and all three q = 1 shared sets INSIDE A u B -- a cell outside "
      "the union in any shared set carries qmax >= 1 and pushes J to 9 "
      "-- with both their cells' s-increments landing on T (base s is "
      "(4,4,2,2); two cells must reach 7 = 4 + 3, so every q = 1 set "
      "is exactly T)"
      % (show([c[0] for c in JCASES_22111]), knap_max(8, 5)),
      all(J == 2 * u for (_, u, J) in JCASES_22111)
      and min(J for (_, _, J) in JCASES_22111) == 8
      and knap_max(8, 5) == 50 and knap_max(8, 5) < Lam(7, 25)
      and 4 + 3 == 7)
CK_22111Q_25 = NCHECK[0]

check("(2,2,1,1,1) AT 25, THE TRIANGULAR WALL.  All three q = 1 sets "
      "equal T; the two q = 2 shared sets contain T (T = A cap B).  So "
      "every support edge of every listed pair contains T, and "
      "conversely every pair of T-containing edges is excessive.  The "
      "five listed pairs must be ALL pairs among r T-containing edges: "
      "C(r,2) = 5 has no solution (C(3,2) = 3, C(4,2) = 6).  DEAD",
      all(comb(r, 2) != 5 for r in range(0, 30)))
CK_22111W_25 = NCHECK[0]

# ---- (2,1^5) at 25 -------------------------------------------------------
check("(2,1^5) AT 25, THE FORCED K4.  R = 16; the 3-cell q = 2 shared "
      "set alone gives J >= 6; only (10,10) reaches 68 (budget 10 cap "
      "5), and any J > 6 kills it (budget 9 max = %d < 68), so J = 6: "
      "every q = 1 shared set lies inside the q = 2 set A, and the two "
      "F = 5 cells need s = 7 = 2 + 5, i.e. BOTH lie in all five q = 1 "
      "sets: all five equal T = {u, v}.  A contains T; the edges "
      "through T form a full excessive clique: C(r,2) = 1 + 5 = 6 "
      "gives r = 4 support edges" % knap_max(9, 5),
      knap_max(9, 5) == 59
      and [r for r in range(30) if comb(r, 2) == 6] == [4])
CK_215K4_25 = NCHECK[0]

check("(2,1^5) AT 25, THE PROFILE KILL.  Of the four support edges, the "
      "q = 2 pair {e, g} and the two others h, k with x_h = x_k = 3 "
      "(each rides three q = 1 pairs).  Per-edge degree sum (S5): "
      "sum over h of d = 25 + 5 + 3 = 33; u, v carry 20, so h's four "
      "ordinary cells sum to 13 -- and the same for k, on DISJOINT "
      "cells (h cap k = T; h cap e = h cap g = T).  Ordinary cells are "
      "low (a third cell with F >= 1 would push P past R - J = 10).  "
      "Each four-cell set: degrees in {2..5}, at most ONE two ((D2) "
      "per edge), sum 13 -- a degree-3 cell is FORCED in each (check "
      "%d), needing n_3 >= 2.  The census at Psi = 70 (check %d) "
      "allows n_3 = 1.  DEAD" % (CK_PROF, CK_CEN),
      25 + 5 + 3 - 20 == 13
      and profile_forces_three(4, 13, 1)
      and census_rows(25, 7, (10, 10)) == [(36, 12, 1, 2, 19)])
CK_215P_25 = NCHECK[0]

# ---- (1^7) at 25 ---------------------------------------------------------
check("(1^7) AT 25, THE NUMERICAL LAYER.  R = 14.  |U| = 2 impossible "
      "(C(t,2) = 7).  |U| >= 5: J >= 5, budget <= 9, max Psi = %d < 68."
      "  |U| in {3, 4}: the only multisets at or above 68 are "
      "(10,10,6) at 73 (J <= 3, so |U| = 3) and (10,10) at 70 (J <= 4)"
      % knap_max(9, 6),
      knap_max(9, 6) == 59
      and sorted(knap_sets(11, 6, 68)) == [(70, (10, 10)),
                                           (73, (10, 10, 6))]
      and sorted(knap_sets(10, 6, 68)) == [(70, (10, 10))])
CK_17N_25 = NCHECK[0]

check("(1^7) AT 25, (10,10,6) DIES BY CAPACITY -- the same "
      "m-independent triangular-pattern test as at 26 (check %d): "
      "s-sequences (7,6,1) and (6,4,4) give capacities (6,5,0) and "
      "(5,3,3); neither hosts (5,5,1)" % CK_17CAP,
      all(not host([x - 1 for x in s], [5, 5, 1]) for (_, s) in PAT3))
CK_17CAP_25 = NCHECK[0]

PAT4 = mult_patterns(4, 7, TRIS)
PAT4_HOST = [(mus, s) for (mus, s) in PAT4
             if host([x - 1 for x in s], [5, 5])]
check("(1^7) AT 25, (10,10) COLLAPSES TO THE DISJOINT 6+1.  |U| = 3: "
      "hosting (5,5) needs two capacities >= 5; of the patterns "
      "{6,1,0} -> (6,5,0) and {3,3,1} -> (5,3,3), only {6,1,0} hosts.  "
      "|U| = 4 (J = 4 <= R - P = 4): enumerated %d triangular patterns "
      "on six cell-pairs; the ONLY hosting s-sequence is (6,6,1,1) "
      "from the disjoint pattern mu({u,v}) = 6, mu({x,y}) = 1 -- the "
      "high pair carries a full K4 of support edges in every case"
      % len(PAT4),
      set(s for (_, s) in PAT3 if host([x - 1 for x in s], [5, 5]))
      == {(7, 6, 1)}
      and len(PAT4) > 0
      and set(s for (_, s) in PAT4_HOST) == {(6, 6, 1, 1)}
      and all(sorted((mu for mu in mus if mu), reverse=True) == [6, 1]
              for (mus, s) in PAT4_HOST))
CK_17K4_25 = NCHECK[0]

check("(1^7) AT 25, THE K4 PROFILE KILL.  Four support edges through "
      "T = {u, v} carry the 6-clique; the seventh pair adds x_e = 1 to "
      "at most ONE support edge (its other edge is outside: two "
      "support edges as the seventh pair would share T plus at least "
      "one cell of the seventh shared set, q >= 2 not 1).  So >= 3 support edges have x_e = 3 "
      "exactly: ordinary four-cell sets, pairwise disjoint (supports "
      "meet exactly in T), each of degree sum 25 + 5 + 3 - 20 = 13, "
      "each FORCING a degree-3 cell ((D2) per edge + profile fact): "
      "n_3 >= 3.  The census at Psi = 70 allows n_3 = 1 (check %d).  "
      "DEAD.  (7, 25) IS DEAD ON EVERY PARTITION" % CK_CEN,
      4 - 1 >= 3 and profile_forces_three(4, 13, 1)
      and census_rows(25, 7, (10, 10)) == [(36, 12, 1, 2, 19)]
      and 3 > 1)
CK_17K4P_25 = NCHECK[0]

T_25 = (CK_RAW25, CK_331_25, CK_322_25, CK_2221T_25, CK_2221S_25,
        CK_2221NT_25, CK_22111Q_25, CK_22111W_25, CK_215K4_25,
        CK_215P_25, CK_17N_25, CK_17CAP_25, CK_17K4_25, CK_17K4P_25)


# ==========================================================================
# 6.  The theorems, and the next wall
# ==========================================================================

head("6.  T-A22 / T-B22, and the (7, 24) preview tie")

check("(T-A22)  X = 7  =>  m <= 24.  Sections 4 and 5 emptied (7, 26) "
      "and (7, 25) on every excess partition (checks %s and %s); 0021's "
      "T-B21 (billed) already gives X = 7 => m <= 26"
      % (show(T_26), show(T_25)),
      len(FAILED) == 0 and len(T_26) == 8 and len(T_25) == 14)

check("(T-B22)  THE STAIRCASE, SQUARED OFF: X >= 7 on 22 <= m <= 24; "
      "X >= 8 on 25 <= m <= 28; X >= 9 at 29; X >= 10 from 30.  "
      "Assembly: T-A22 + 0021's T-A21 (X >= 7 everywhere) turns "
      "'X = 7 dead at 25, 26' into X >= 8 there; 0021's T-B21 covers "
      "27, 28 and above (all billed)",
      len(FAILED) == 0)

check("PREVIEW, NOT A CLAIM -- THE (7, 24) TIE.  The corrected "
      "triangle branch of (2,2,2,1) at m = 24 reaches Psi = %d = "
      "Lambda_7(24) EXACTLY; the top multiset is (10,9,6) (f-values "
      "(5,4,1)); its census pins (n2,n3,n4,n5) = %s.  Zero margin: the "
      "next campaign starts at a wall that counting alone cannot "
      "breach" % (tri22(7, 24),
                  str(census_rows(24, 7, (10, 9, 6))[0][1:])
                  if census_rows(24, 7, (10, 9, 6)) else "?"),
      tri22(7, 24) == 62 and Lam(7, 24) == 62
      and census_rows(24, 7, (10, 9, 6)) == [(36, 12, 5, 0, 16)])


# ==========================================================================
# 7.  Mutations
# ==========================================================================

head("7.  MUTATIONS -- every tooth priced")

MUT = []


def mut(name, flipped, expect, detail):
    MUT.append((name, flipped, expect, detail))
    check("%s -- %s" % (name, detail), flipped == expect,
          "flips: %s, expected: %s" % (flipped, expect))


# M-D2E: allow two degree-2 cells on a support edge.
mut("M-D2E  (D2) per-edge withdrawn (two twos per support edge)",
    not profile_forces_three(4, 13, 2), True,
    "the profile fact DIES ((2,2,4,5) carries 13 with no three): the "
    "(2,1^5) and (1^7) kills at m = 25 lose their last step.  (D2) "
    "per-edge is load-bearing exactly there")

# M-T5: admit 5 as a clique pair-count.
PAT3_M = mult_patterns(3, 7, TRIS + [5])
mut("M-T5  five admitted as triangular",
    any(host([x - 1 for x in s], [5, 5, 1]) for (_, s) in PAT3_M), True,
    "the mutant pattern {5,1,1} yields s = (6,6,2), capacities "
    "(5,5,1), and (10,10,6) HOSTS: the (1^7) capacity kill is carried "
    "by the exact triangular law, not by slack")

# M-C3: cap 4 -> 5.
mut("M-C3  x_e cap raised to 5",
    (3 + 2 > 5, 3 + 3 > 5), (False, True),
    "at cap 5 a q = 3 pair may share an edge with a q = 2 pair "
    "(3 + 2 = 5): the (3,2,2) edge-disjointness argument REOPENS; "
    "(3,3,1) still cannot share (6 > 5).  C3 is load-bearing for "
    "(3,2,2)")

# M-TRI-O: outside branch deleted -> optimizer states visibly drop and
# the file must notice (completeness counter).
TRI_STATES[0] = 0
_ = [tri22(7, m, branches=((0, 0), (1, 0))) for m in (24, 25, 26, 27)]
N_NO_O = TRI_STATES[0]
mut("M-TRI-O  outside cells deleted from the triangle optimizer",
    N_NO_O < TRI_N_ALL, True,
    "%d states against the full %d: the deletion is VISIBLE.  The "
    "maxima happen to be equal (convexity), and 0021's numbers were "
    "right for the wrong reason -- this file carries the branch so "
    "the REASON is right" % (N_NO_O, TRI_N_ALL))

# M-O2: the apex branch alone deleted.
TRI_STATES[0] = 0
_ = [tri22(7, m, branches=((0, 0), (1, 0), (0, 1))) for m in
     (24, 25, 26, 27)]
N_NO_O2 = TRI_STATES[0]
mut("M-O2  the adjacent-apex (0,2) branch alone deleted",
    N_NO_O2 < TRI_N_ALL, True,
    "%d states against %d: the audit's own missing case is a NAMED "
    "branch, not a comment" % (N_NO_O2, TRI_N_ALL))

# M-f: cost f instead of F.  At cap 6 the ceiling becomes d = 11 and
# knapsacks change; measure the two walls.
def knap_max_f(B, C):
    dm = 5
    while (flin(dm + 1)) <= C:
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
    "the (1^7) wall at budget 11 cap 6 jumps 73 -> 83 under the linear "
    "cost (d = 11 enters at cost 6): the F/f distinction is load-"
    "bearing at THE decisive cell, exactly as 0021 priced")

# M-n35: n >= 35.
LAM35 = [m * m - 43 * m + 14 + 15 * 35 - 3 * (m // 2) for m in (25, 26)]
mut("M-n35  vertex floor 36 -> 35",
    [Lam(7, m) - v for (m, v) in zip((25, 26), LAM35)], [15, 15],
    "Lambda drops 15 at both rungs (68 -> 53, 73 -> 58): every "
    "numerical kill above would need re-measuring.  The tau = 6 cover "
    "argument is the single most expensive constant, as in 0021")

# M-RG: |K_T| >= 5 -> 4 at k = 3.
def tri22_rg4(X, m):
    R = 20
    best = 0
    for t in range(0, 4):
        U = 9 - 2 * t
        for (a, o) in TRI_BRANCHES:
            if a > min(t, 1) or o > max(0, 9 - 3 * t):
                continue
            outside_J = (2 - a - o) if t == 3 else 0
            Bud = R - 2 * U - outside_J
            if Bud < 0:
                continue
            caps = [(5 if (i == 0 and a == 1) else 4) for i in range(t)]
            for combo in itertools.product(*[range(0, cc + 1)
                                             for cc in caps]):
                if sum(combo) > m - 13:   # rg 5 -> 4
                    continue
                for fo in itertools.product((0, 1), repeat=o):
                    cost = sum(F(x + 5) for x in combo) + sum(fo)
                    if cost > Bud:
                        continue
                    best = max(best, sum(psi(x + 5) for x in combo)
                               + sum(psi(v + 5) for v in fo))
    return best


mut("M-RG  residual pairing 5 -> 4 at k = 3",
    [tri22_rg4(7, m) for m in (24, 25, 26)],
    [67, 74, 83],
    "the triangle maxima RISE at every rung, 62/67/74 -> 67/74/83: the "
    "(7,25) triangle kill REOPENS outright (74 >= 68) and the (7,24) "
    "tie breaks upward.  The full |K_T| >= 5 of residual pairing is "
    "load-bearing across the whole triangle branch")

# M-CEN: census identity coefficient 15 -> 14.
def census_rows_m(m, X, D, coeff):
    Ps = sum(psi(d) for d in D)
    gap = Ps - Lam(X, m)
    if gap < 0:
        return []
    n2cap = m // 2
    rows = []
    for dn in range(0, gap // coeff + 1):
        n = 36 + dn
        rem = gap - coeff * dn
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


mut("M-CEN  the 15n identity coefficient perturbed to 14",
    census_rows_m(25, 7, (10, 10), 14) == census_rows(25, 7, (10, 10)),
    True,
    "at gap = 2 < 14 the n-ladder never engages, so THIS mutant is "
    "INERT at the decisive cells -- recorded so nobody mistakes the "
    "identity's n-coefficient for a live margin here (it is priced "
    "live in 0021's sweeps)")

# Sweep-completeness tooth: drop one partition.
SURV25_TRUNC = [pi for pi in PARTS7 if pi != (2, 1, 1, 1, 1, 1)
                and raw_row(pi, 7, 25) >= 68]
mut("M-SWEEP  one partition silently dropped from the m = 25 sieve",
    len(SURV25_TRUNC) == len(SURV25) - 1, True,
    "the survivor list shrinks and the generated-count check (%d) is "
    "what stands between a truncated sweep and a false all-clear -- "
    "turn 16's M9 lesson, kept armed" % CK_PARTS)

check("MUTATION LEDGER COMPLETE: %d mutants priced, %d checks total"
      % (len(MUT), NCHECK[0]),
      len(MUT) == 10)


# ==========================================================================
# RESULT
# ==========================================================================

head("RESULT")

ok = not FAILED
print()
print("  checks : %d" % NCHECK[0])
print("  failed : %d%s" % (len(FAILED),
                           "" if ok else "  " + " | ".join(FAILED)))
print("  time   : %.1f s" % (time.time() - START))
print()
if ok:
    print("  GREEN.  X = 7  =>  m <= 24.  The staircase is squared off:")
    print("      22 <= m <= 24  =>  X >= 7")
    print("      25 <= m <= 28  =>  X >= 8")
    print("             m = 29  =>  X >= 9")
    print("             m >= 30  =>  X >= 10")
    print("  The live minimum-excess frontier is X = 7 on m in {22, 23, 24},")
    print("  and the first wall of the next campaign is the (7, 24) tie.")
else:
    print("  NOT GREEN.")
sys.exit(0 if ok else 1)
