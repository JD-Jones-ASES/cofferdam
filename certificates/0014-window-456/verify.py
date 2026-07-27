#!/usr/bin/env python3
"""Certificate 0014 -- the window tightens: every critical core has
m in [22, 456].

    python3 verify.py

Stdlib only.  Exact integer/rational arithmetic throughout (Bareiss
determinants, Fraction row reduction; no floats, no modular shortcuts,
no solver).  No imports from lib/.  Runs under Python 3.9 and under
python3 -O.  Deterministic (all "random" draws come from a hand-rolled
LCG with fixed seed).

WHAT IS CLAIMED
---------------
  (L11) the part-confinement annihilator: map each part
  P_j of a 6-partition into a 5-dimensional subspace
  U_j of R^11; the six functionals x -> x ^ q_j, with
  q_j the basis-wedge of U_j, annihilate EVERY
  transversal wedge; for generic U_j they are
  independent, so all transversal wedges lie in a
  456-dimensional subspace of Lambda^6(R^11)            PROVEN-BY-CERTIFICATE

  (*) no private cover T_e of a critical core is
  contained in a single part                            PROVEN (two lines from
                                                        (A), certificate 0005,
                                                        via 0013's (3a)/(3b))

  every critical core has m(K) <= C(11,6) - 6 = 456,
  and THE WINDOW TIGHTENS: m(K) in [22, 456];
  Ryser r = 6 intersecting <=> no critical core with
  m in [22, 456]                                        PROVEN-BY-CERTIFICATE
                                                        (in-house: 0005, 0013)

THE PROOF
---------
Setting as in certificate 0013: K is an edge-critical counterexample
(finite, 6-partite, 6-uniform, intersecting, tau(K) = 6), with, for each
edge e, a private minimum 5-cover T_e of K - e satisfying (3a)
e cap T_e = empty and (3b) e cap T_f != empty for f != e, and
T_e inside V(K).  All from certificate 0013, steps (1)-(3).

  (5*) THE CONCENTRATION LEMMA (*).  No T_e lies inside a single part.
       Suppose T_e is contained in part P_j.  Every f != e is an edge
       of K - e, which T_e covers, so f cap T_e != empty; and f has
       exactly ONE vertex in P_j, so f's part-j vertex is in T_e.  Let v be e's own
       part-j vertex; v is not in T_e by (3a).  By lemma (A) (certificate
       0005: every active vertex of a counterexample has degree >= 2 --
       for x in an edge E, E minus x has 5 < 6 = tau vertices, so some
       edge F meets E exactly in x), some f != e contains v; f's part-j
       vertex is then v, forcing v in T_e -- contradiction.  QED (*).
  (6) THE EMBEDDING.  Choose six 5-dimensional subspaces U_1..U_6 of
      R^11 and map each vertex of P_j to a vector in U_j, all choices
      generic.  For an edge e let x_e in Lambda^6(R^11) be the wedge of
      its six vectors; for a cover T let w_T in Lambda^5(R^11) be the
      wedge of its five vectors.
  (7) ANNIHILATION -- an identity, not a genericity fact.  Let q_j be
      the wedge of a basis of U_j and phi_j(x) = x ^ q_j in
      Lambda^11(R^11) = R.  For EVERY transversal e: phi_j(x_e) = 0,
      because x_e ^ q_j wedges 11 vectors of which six -- e's part-j
      vector and q_j's five factors -- lie in the 5-dimensional U_j.
      Six vectors in a 5-dimensional space are dependent; the wedge is
      0.  (Over the generating set of the transversal-wedge span --
      basis-vector products, by multilinearity in each slot -- the
      matrix even has a literally repeated column.)
  (8) INDEPENDENCE OF THE SIX FUNCTIONALS.  The pairing
      Lambda^6 x Lambda^5 -> Lambda^11 is perfect, so the phi_j are
      independent iff the q_j are independent in Lambda^5(R^11).
      Witnessed below by an exact rank-6 computation on an explicit
      integer instance (section 3); a nonzero minor at one instance
      proves the generic rank is 6.  Hence
      X := intersection of the six kernels has dim 462 - 6 = 456, and
      every x_e lies in X by (7).
  (9) DIAGONALS SURVIVE.  x_e ^ w_{T_f} = 0 for f != e identically: by
      (3b) the two vertex sets share a vertex, so the wedge repeats a
      vector.  x_e ^ w_{T_e} is, for each multiplicity pattern
      (t_1..t_6) of T_e over the parts (sum 5), a polynomial in the
      free coordinates; by (*) every t_j <= 4, so each part contributes
      1 + t_j <= 5 <= dim U_j vectors, and the pattern's polynomial is
      NOT identically zero -- witnessed below by one exact nonzero
      determinant per pattern, all 246 patterns (section 4).  A single
      core presents finitely many polynomial conditions (the rank minor
      and one diagonal per edge -- finitely many, since K is finite),
      each nonzero somewhere, so over the infinite field Q a common
      generic choice satisfies all simultaneously.
 (10) THE BOUND.  Fix such a choice.  If sum c_e x_e = 0, wedging with
      w_{T_f} kills every term but c_f (x_f ^ w_{T_f}) with nonzero
      coefficient factor, so c_f = 0: the x_e are linearly independent
      members of X.  Hence m(K) <= dim X = 456.  With certificate
      0013's floor half: m(K) in [22, 456], and the equivalence
      restates as: Ryser r = 6 intersecting <=> no critical core with
      m in [22, 456].

  GENERAL FORM (noted, not separately certified): the same argument
  gives, for every r >= 3, that an r-partite critical core (with (A))
  has m <= C(2r-1, r) - r.  At r = 2 hypothesis (*) is UNSATISFIABLE
  (|T_e| = 1 always lies in one part) and the refinement is FALSE
  abstractly: the section-5 exhibit has m = 2 > C(3,2) - 2 = 1.  The
  r = 2 calibration is what forced the mechanism to consume core
  structure -- exactly the audit trail the peer sketch omitted.

SCOPE
-----
Everything quantifies over critical cores, exactly as in certificate
0013; the ceiling here consumes MORE structure than 0013's (namely (A)
and (*)), buys 6 more units, and is NOT self-contained -- 0013's
CEILING remains the empty-ledger record (its window's floor half
transits the pinned chain, per 0013's own ledger).  This certificate
never replaces 0013; it stands on it.

PROVENANCE
----------
The 456 mechanism was claimed by an outside review (relayed via JD,
turn 9) as a one-line sketch ("six functionals q_i ^ . annihilate the
transversal-wedge span"), desk-read plausible, unverified.  Turn 10's
audit ran two independent in-house lanes (a derivation lane and a
rank-measurement lane); both converged on the part-confinement
mechanism above, the measurement lane additionally proving generic
embeddings give codimension 0 (so confinement is essential, and no
refinement of this kind is available without (*)).  The proof was then
re-derived at the desk line by line before this certificate was
written.  The turn-10 literature sweep found NO published statement of
this partite refinement (closest genre: subspace variations of the
weighted skew Bollobas theorem, Wu-Li-Lu-Feng, arXiv:2603.02698, March
2026); if that absence holds, the 456 ceiling is new mathematics.

THE LEDGER, in full
-------------------
  (L11) + the 456 ceiling      EXTERNAL INPUTS -- NONE.  In-house:
                               certificate 0013 (criticality, private
                               covers, (3a)/(3b), T_e in V(K)) and
                               certificate 0005 (lemma (A)) via (*).
  the window [22, 456]         additionally the floor: 0013's floor half
                               (transitively 0005/0006/0008-0012).
  ATTRIBUTION                  exterior-algebra set-pair method: Lovasz
                               1977 / Frankl 1982 / Kalai 1984
                               (recorded, not consumed -- the argument
                               is re-derived and witnessed exactly
                               here).  The 456 statement itself: no
                               published counterpart found (turn-10
                               sweep).
"""

import itertools
import sys
import time
from fractions import Fraction
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


# --- deterministic pseudo-randomness: a hand-rolled LCG ------------------
class LCG(object):
    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFF

    def next(self):
        self.s = (25214903917 * self.s + 11) & 0xFFFFFFFFFFFF
        return self.s >> 16

    def small(self):
        """An integer in [-9, 9], never 0 (keeps combos honest)."""
        v = self.next() % 19 - 9
        return v if v != 0 else 1


RNG = LCG(462456)


def det_bareiss(M):
    """Exact integer determinant, fraction-free Bareiss.  M is a list of
    lists of ints; M is consumed."""
    n = len(M)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for i in range(k + 1, n):
                if M[i][k]:
                    M[k], M[i] = M[i], M[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def rank_fraction(rows):
    """Exact rank over Q of a list of integer row vectors."""
    rows = [[Fraction(x) for x in r] for r in rows]
    ncols = len(rows[0]) if rows else 0
    rank = 0
    col = 0
    r = 0
    while r < len(rows) and col < ncols:
        piv = None
        for i in range(r, len(rows)):
            if rows[i][col] != 0:
                piv = i
                break
        if piv is None:
            col += 1
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][col]
        for i in range(r + 1, len(rows)):
            if rows[i][col] != 0:
                f = rows[i][col] / pv
                for j in range(col, ncols):
                    rows[i][j] -= f * rows[r][j]
        rank += 1
        r += 1
        col += 1
    return rank


# ==========================================================================
# 1.  The instance: six 5x11 integer bases, in general position
# ==========================================================================

head("1.  the instance -- six part-subspaces U_j of R^11")

U = [[[RNG.small() for _ in range(11)] for _ in range(5)] for _ in range(6)]

check("each U_j has rank exactly 5 (exact rational row reduction)",
      all(rank_fraction(U[j]) == 5 for j in range(6)))
check("every pair U_i + U_j has rank 10 and every triple has rank 11 -- "
      "the instance is in general position",
      all(rank_fraction(U[i] + U[j]) == 10
          for i, j in itertools.combinations(range(6), 2))
      and all(rank_fraction(U[i] + U[j] + U[k]) == 11
              for i, j, k in itertools.combinations(range(6), 3)))


def combo(j):
    """A generic integer vector in U_j: an LCG combination of its basis."""
    cs = [RNG.small() for _ in range(5)]
    return [sum(cs[b] * U[j][b][c] for b in range(5)) for c in range(11)]


# ==========================================================================
# 2.  (L11) annihilation -- the identity, exactly spot-verified
# ==========================================================================

head("2.  six functionals annihilate every transversal wedge")

note("phi_j(x_e) = det[ e's six vectors | U_j's five basis vectors ]: the "
     "matrix holds six vectors of the 5-dimensional U_j (e's part-j "
     "vector plus q_j's five factors), so the determinant is 0 -- an "
     "identity over ANY field, no genericity.  Over the span's generating "
     "set (basis-vector products, by multilinearity in each slot) the "
     "matrix even repeats a column literally")

t0 = time.time()
bad = 0
for trial in range(50):
    evecs = [combo(j) for j in range(6)]
    for j in range(6):
        M = [list(v) for v in evecs] + [list(b) for b in U[j]]
        if det_bareiss([row[:] for row in M]) != 0:
            bad += 1
check("50 random transversal wedges (LCG combinations, one generic vector "
      "per part) against all six functionals: 300 exact integer "
      "determinants, every one exactly 0",
      bad == 0, "%.1fs" % (time.time() - t0))

# ==========================================================================
# 3.  The six functionals are independent: dim X = 456
# ==========================================================================

head("3.  rank of the annihilators")

t0 = time.time()
COLS5 = list(itertools.combinations(range(11), 5))     # 462 basis 5-sets
QROWS = []
for j in range(6):
    row = []
    for S in COLS5:
        M = [[U[j][r][c] for c in S] for r in range(5)]
        row.append(det_bareiss(M))
    QROWS.append(row)
check("the six q_j (Plucker coordinates: 5x5 minors over all "
      "C(11,5) = 462 column sets) have rank EXACTLY 6 over Q",
      rank_fraction(QROWS) == 6, "%.1fs" % (time.time() - t0))

# SENSITIVITY: the rank routine must have failure power in BOTH
# directions -- a collapsed instance must DROP the rank.
t0 = time.time()
QROWS2 = list(QROWS[:5])
row2 = []
for S in COLS5:
    M = [[U[0][r][c] for c in S] for r in range(5)]    # U_6 := U_1
    row2.append(det_bareiss(M))
QROWS2.append(row2)
check("SENSITIVITY: collapse U_6 := U_1 and the annihilator rank drops "
      "to EXACTLY 5, and the bound this certificate could then prove "
      "would weaken to 462 - 5 = 457 -- the rank computation is "
      "falsifiable in both directions (a rank routine that always "
      "reports full rank fails here)",
      rank_fraction(QROWS2) == 5 and QROWS2[5] == QROWS[0],
      "%.1fs" % (time.time() - t0))
check("therefore dim X = 462 - 6 = 456, and C(11,6) - 6 = 456",
      462 - 6 == 456 and comb(11, 6) - 6 == 456)

# ==========================================================================
# 4.  Diagonals survive: all 246 admissible patterns witnessed nonzero
# ==========================================================================

head("4.  diagonal survival under (*)")

patterns = [t for t in itertools.product(range(5), repeat=6) if sum(t) == 5]
check("the multiplicity patterns of a 5-cover over six parts with every "
      "t_j <= 4 number exactly 246 = C(10,5) - 6",
      len(patterns) == 246 and comb(10, 5) - 6 == 246)

t0 = time.time()
witnessed = 0
max_tries = 0
for t in patterns:
    tries = 0
    while True:
        tries += 1
        cols = []
        for j in range(6):
            cols.append(combo(j))                      # e's part-j vector
        for j in range(6):
            for _ in range(t[j]):
                cols.append(combo(j))                  # T_e's vectors
        if det_bareiss([row[:] for row in cols]) != 0:
            witnessed += 1
            break
        if tries >= 20:
            break
    max_tries = max(max_tries, tries)
check("every one of the 246 patterns has an exact nonzero witness "
      "determinant -- each diagonal polynomial is NOT identically zero, "
      "so a generic embedding keeps every diagonal of a finite core "
      "alive simultaneously",
      witnessed == len(patterns) and len(patterns) == 246,
      "%.1fs, max retries %d" % (time.time() - t0, max_tries))

offdiag_zero = True
for trial in range(20):
    shared = combo(0)                                  # one shared vertex
    cols = [list(shared)] + [combo(j) for j in range(1, 6)]
    cols.append(list(shared))                          # T_f repeats it
    for j in (1, 2, 3, 4):
        cols.append(combo(j))
    if det_bareiss([row[:] for row in cols]) != 0:
        offdiag_zero = False
check("the off-diagonal identity, spot-witnessed: when e and T_f share "
      "a vertex ((3b)) the 11-column matrix repeats that vertex's "
      "vector and the determinant is exactly 0 -- 20 trials, all zero",
      offdiag_zero)

# ==========================================================================
# 5.  Teeth
# ==========================================================================

head("5.  teeth: (*) is load-bearing, and r = 2 is the honest boundary")

t0 = time.time()
allzero = True
for j in range(6):                                     # concentrated: t_j = 5
    for trial in range(10):
        cols = [combo(k) for k in range(6)]
        for _ in range(5):
            cols.append(combo(j))
        if det_bareiss([row[:] for row in cols]) != 0:
            allzero = False
check("TEETH: the six EXCLUDED patterns (T_e concentrated in one part, "
      "t_j = 5) give determinant exactly 0 in every one of 60 trials -- "
      "T_e's five vectors plus e's own part-j vector are six vectors in "
      "the 5-dimensional U_j; the diagonal DIES, and with "
      "it the bound.  (*) is what keeps the argument alive",
      allzero, "%.1fs" % (time.time() - t0))

# r = 2: (*) unsatisfiable, refinement false -- the calibration exhibit.
# Parts {a},{b,d}; e1 = {a,b}, T1 = {d}; e2 = {a,d}, T2 = {b}.
part = {"a": 0, "b": 1, "d": 1}
e1, T1 = frozenset("ab"), frozenset("d")
e2, T2 = frozenset("ad"), frozenset("b")
check("TEETH, r = 2: the calibration system (parts {a},{b,d}; e1 = ab, "
      "T1 = d; e2 = ad, T2 = b) passes the axioms tested here "
      "(own-disjointness, both cross directions, transversality; sizes "
      "|e| = 2, |T| = 1 by construction), has m = 2 > C(3,2) - 2 = 1, "
      "and BOTH its T's are concentrated (|T| = 1 always is) -- the "
      "minus-r refinement is FALSE without (*), and (*) is "
      "unsatisfiable at r = 2",
      (not e1 & T1) and (not e2 & T2) and bool(e1 & T2) and bool(e2 & T1)
      and len({part[v] for v in e1}) == 2
      and len({part[v] for v in e2}) == 2
      and 2 > comb(3, 2) - 2)

# ==========================================================================
# 6.  Not too strong: generic embeddings see NOTHING
# ==========================================================================

head("6.  not too strong -- without confinement the span is everything")

t0 = time.time()
ok_generic = True
for (r, npart) in ((3, 3), (4, 4)):
    N = 2 * r - 1
    dimL = comb(N, r)
    parts = [[[RNG.small() for _ in range(N)] for _ in range(r)]
             for _ in range(r)]                        # r vectors per part, UNCONFINED in R^N
    rows = []
    for choice in itertools.product(range(r), repeat=r):
        vecs = [parts[j][choice[j]] for j in range(r)]
        row = []
        for S in itertools.combinations(range(N), r):
            row.append(det_bareiss([[vecs[i][c] for c in S]
                                    for i in range(r)]))
        rows.append(row)
    if rank_fraction(rows) != dimL:
        ok_generic = False
check("NOT TOO STRONG: with parts UNCONFINED (generic in the full space) "
      "the transversal wedges span ALL of Lambda^r at r = 3 (rank "
      "10/10) and r = 4 (rank 35/35, exact over Q) -- at these r, no "
      "functional annihilates the span and no refinement exists "
      "generically; the confined embedding, and with it (*), is "
      "essential (r = 6 essentiality rests on the adjacent "
      "fleet-measured note, not on this check)",
      ok_generic, "%.1fs" % (time.time() - t0))
note("the audit's measurement lane witnessed the same at r = 6: rank "
     "462 = C(11,6) for unconfined parts of core-realistic size "
     "(fleet-measured, recorded in the turn-10 notebook; not a check "
     "here)")

# ==========================================================================
# 7.  The window, composed
# ==========================================================================

head("7.  composition")

note("(*) stands on certificate 0005's lemma (A), which holds for EVERY "
     "counterexample (for x in edge E, E minus x has 5 < 6 = tau "
     "vertices, so some edge F meets E exactly in x): a concentrated "
     "T_e would make e's part-j vertex degree-1.  Two lines, no new "
     "machinery")
note("SCOPE: cores only, exactly as 0013; this certificate consumes MORE "
     "than 0013 (namely (A) and the confined embedding) and buys 6 more "
     "units.  0013's CEILING remains the empty-ledger record; this one "
     "stands on 0013, never replaces it")
check("closing arithmetic (the theorem itself is the composition above): "
      "22 <= 456, and 456 = C(11,6) - 6 -- every critical core has "
      "m in [22, 456]",
      22 <= 456 and comb(11, 6) - 6 == 456)

head("Result")

print("""
  (L11) six part-functionals annihilate the            PROVEN-BY-CERTIFICATE
  transversal-wedge span; dim X = 456
  (*) no private cover is concentrated in a part       PROVEN (from (A) in 0005,
                                                       via 0013's (3a)/(3b))
  every critical core has m(K) <= 456                  PROVEN-BY-CERTIFICATE
                                                       (in-house: 0005, 0013)
  THE WINDOW TIGHTENS: m(K) in [22, 456];              PROVEN-BY-CERTIFICATE
  Ryser r = 6 intersecting <=> no critical core        (floor: 0013's, in-house
  with m in [22, 456]                                  transitively)

  The peer-claimed 456 is now an in-house theorem: mechanism located
  (part-confinement), r = 2 boundary understood ((*) unsatisfiable, bound
  false abstractly -- the calibration that forced honesty), generic
  impossibility proven in-transcript at r = 3, 4 (r = 6 fleet-measured,
  notebook).  Every identity and witness THIS transcript relies on is
  exact integer arithmetic; the 5 notes are stated, not tested, and say
  so.  435 values of m remain.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(1 if FAILED else 0)
