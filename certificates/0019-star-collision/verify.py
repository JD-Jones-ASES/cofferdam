#!/usr/bin/env python3
"""Certificate 0019 -- the star-collision inequality: X >= 5 everywhere in
the window, and X = 5 confined to m <= 26.

    python3 verify.py

Stdlib only.  Exact Fraction arithmetic on every load-bearing bound.  No
solver.  No imports from lib/.  Reads nothing from disk.  Runs under
Python 3.9 and under python3 -O.  Deterministic (hand-rolled LCG, seed
20260728; no dict-order dependence).

WHAT IS CLAIMED
---------------
  (T-A) X >= 5 FOR EVERY CRITICAL CORE in the window: every
      edge-critical 6-partite 6-uniform intersecting counterexample
      core with tau = 6 and m in [22, 456] has X >= 5.
          PROVEN-BY-CERTIFICATE.  In-house: 0013 (criticality, the
          private 5-covers), 0015 (2)-(3), 0017 C1 (check 8) + c12 +
          C3, 0005, 0008 (D2), 0012/0013/0014 transitively.  0016 (T)
          as generalized by 0017 c7 enters only THROUGH C1, not as a
          step of its own.  NOT 0017 c9 -- the 4/3 corner is spent at
          X = 5 only, i.e. in T-B.  External NONE.

  (T-B) X = 5 FORCES m <= 26.
      Corollary, with T-A: m >= 27 forces X >= 6.
          PROVEN-BY-CERTIFICATE.  In-house: 0013, 0015 (2)-(3),
          0017 c9 (the 4/3 per-pair corner) + c12 + C3, 0005,
          0012/0013/0014 transitively.  NOT 0008 (D2) -- measured,
          mutants M3/M3'.  External NONE.

  (SC) THE STAR-COLLISION INEQUALITY.
      For an intersecting r-partite r-uniform family
      with NO universal vertex,
          D := sum_v (d(v) - (r-1))_+  <=  R := sum_{pairs} q(q+1),
      q = lambda - 1 the pair excess.  At r = 6:
      D = sum_v (d(v) - 5)_+ <= sum over excessive pairs of q(q+1).

  (DH) THE DEFECT-HUB BOUND.  For z not in f,
          d(z) <= (r-1) + sum_{{e,g} in E(z)} q_eg <= (r-1) + X - x_f,
      and hence GLOBALLY Delta <= 5 + X at r = 6.  This is the repair
      of the outside audit's 16/3-circularity: the degree cap is now
      derived from X alone, with no appeal to the bound it feeds.

NOTATION.  As in 0015-0018.  K edge-critical, 6-partite (V_1..V_6),
6-uniform, intersecting, tau(K) = 6, tau(K - e) = 5.  A VERTEX is a cell
(part, value); d(v) its degree; n_d the number of vertices of degree d;
n = sum_d n_d.  lambda(f,g) = |f cap g| >= 1; q = lambda - 1;
X = sum over pairs of q = sum_v C(d(v),2) - C(m,2);
x_e = sum_{f != e} q(e,f), sum_e x_e = 2X.  Phi(n,k) = balanced-split
minimum of sum C(n_j,2); w(d) := Phi(d-1,5), the cover-free per-vertex
weight, DERIVED from Phi and never tabulated by hand.  E(z) = the edges
through z; star_excess(z) = sum over pairs inside E(z) of q.
D := sum_v (d(v)-5)_+ ; R := sum over pairs of q(q+1).

THE PROOF, IN ORDER
-------------------
 (1) THE TWO NEW LEMMAS (section 2, enacted; proofs in NOTES.md).
     Fix z not in f.  Every e in E(z) meets f (intersecting), so with
     r_u := |{e in E(z) : u in e}| we have sum_{u in f} r_u >= d(z).
     THE PART-MATE IS EMPTY: f's cell in z's own part is not on any
     e in E(z), because e's cell there is z.  So at most r - 1 of the
     r_u are positive, and
         sum_u C(r_u,2) >= sum_u (r_u - 1)_+ >= d(z) - (r-1).
     The left side is EXACTLY sum over pairs {e,g} inside E(z) of
     |e cap g cap f| (count the pairs through each u), and z lies in
     e cap g but not in f, so |e cap g cap f| <= q_eg.  That is (DH).
     Summing (DH) over all vertices with d(v) > r-1, and using
         sum_v star_excess(v) = sum over pairs q_eg * |e cap g|
                              = sum over pairs q(q+1) = R
     (each pair {e,g} is counted once per shared cell), gives (SC).
     PARTITENESS IS LOAD-BEARING (the -1) and NO UNIVERSAL VERTEX is
     load-bearing (there must exist an f avoiding z); both are shown by
     must-fail controls in section 2.  D <= X is FALSE -- the q(q+1)
     factor is not decoration -- also by control.

 (2) THE CAPS (sections 1, 3).  Per branch, choose f as stated and read
     two caps off the two lemmas:
       OFF f:  d(z) <= 5 + (X - x_f)                          [(DH)]
       ON  f:  sum_{v in f} w(d(v)) <= X - x_f   at X <= 4    [(CC4+),
               sum_{v in f} w(d(v)) <= (4/3)(5 - x_f) at X = 5  0017 C1]
     and the global Delta <= 5 + X closes degree 11 at X = 5 without
     any (Dq) machinery.  R is capped by the partition maxima of X
     under the branch's cap on q (section 1's partition-maximum
     check).  The thirteen branch cap-triples are LITERALS in
     BRANCH_A/BRANCH_B, and section 4 re-derives every one of them
     from capof[] and RTAB[] so that no transcription slip can hide.

 (3) THE CENSUS (sections 3, 4).  With those caps the two moment
     identities
         sum_d d * n_d = 6m,   sum_d C(d,2) * n_d = C(m,2) + X
     (equivalently sum_d d^2 n_d = m^2 + 5m + 2X), the vertex count
     n >= 36 (six blocks per part, tau = 6), the (D2) cap
     n_2 <= floor(m/2) and the star-collision cap D <= R leave NO
     integer solution, at any m in the window, in any branch.  That is
     T-A.  At X = 5, C3 (0017) caps m <= 31 and the same census empties
     m = 27..31.  That is T-B.

 (4) THE ANALYTIC MIRROR (sections 1, 3, 4).  Every branch is also
     killed by hand, by summing one of five pointwise inequalities
     (A),(B),(C),(E),(F) over the vertices and using the same two
     moments.  (A) gives L_X(m) = -7m + (C(m,2)+X)/3 + 90 -
     floor(m/2)/2 <= D; (B) gives the (U)-difference G(m) > 0 except at
     m = 26; (C) gives R4(m) <= D on the X = 4 max-2 branch; (E) and
     (F) carry the two X = 5 rungs m = 28, 27 through an exact
     slack-budget analysis.  The census is the primary kill; the
     analytic route is the cross-assertion.

MANDATORY HONESTY NOTES
-----------------------
 (1) PROVENANCE.  BOTH THEOREMS AND A COMPLETE ANALYTIC ROUTE WERE
     PROPOSED BY AN OUTSIDE AUDIT (GPT 5.6 Sol Pro, second audit,
     2026-07-28, reading the public repo at 079539c), delivered as
     FULL PROOF TEXT.  Per D-036 that proof text entered no chain:
     the desk read it and re-derived every step independently, the
     blind fleet lanes received STATEMENTS plus one-line mechanisms
     only, and the received text itself went only to three hostile
     refuter lanes whose job was to break it.  Two refuters flagged
     its one defect -- the floor(16/3) = 5 => Delta <= 11 step is
     circular as written, since integrality of the w-sum presupposes
     the degree cap it is deriving -- and the desk repaired it with
     the strictly stronger free cap Delta <= 5 + X read directly off
     (DH).  Attribution recorded, not consumed: no step cites the
     audit.  NOTES.md carries the full intake record.
 (2) (D2) IS CONSUMED, AND THE MUTATION SUITE SAYS SO.  Section 5
     measures it rather than assuming it: relax 0008's cap to
     floor(m/2) + 1 and THREE configurations survive (X = 4 max-2 at
     m = 22; X = 4 some-x>=3 at m = 24 and 25); drop it entirely and
     279 survive across four branches.  Theorem B is a different story
     -- every X = 5 census run is empty with the cap dropped, so T-B is
     (D2)-FREE while T-A is not.  The ledger records exactly that.
 (3) THE MARGIN IS ONE UNIT, TWICE, AND ZERO UNITS TWICE.  X = 4
     matching closes 9 against 8; X = 4 max-2 closes 13 against 12; the
     (U)-difference is exactly 1 at m = 24 and 25 and exactly 0 at
     m = 26 (where three redundant teeth take over); and at m = 27 and
     m = 28 the star-collision bound is EXACTLY tight -- D is forced to
     equal R = 14 and the kill is a divisibility argument, not a
     margin.  Section 6 names every one of them.
 (4) WHAT ENACTMENT DOES AND DOES NOT PRICE.  Section 2 enacts (DH) and
     (SC) on 1,000+ constructed families, which prices the LEMMAS.  It
     cannot price the census layers: nothing this lab can build has
     m >= 22.  The census layers are priced by the mutation suite
     (section 5), which is why every cap carries a mutant.
 (5) WHAT THIS DOES NOT CLAIM.  No core is claimed to exist.  Nothing
     is claimed at X >= 6.  The X = 5 field on m in [22, 26] is NOT
     emptied -- T-B confines X = 5 to those five rungs and stops.  The
     thin rungs m in {23..26} remain the window's arithmetic-free
     stretch for X = 5.

THE LEDGER, in full
-------------------
  CONSUMES.  0013 (criticality; the private minimum 5-covers T_e --
  tau(K - e) = 5 is what puts the 5 in Phi(d_i - 1, 5 - b_i)); 0015
  steps (2)-(3) (the pigeonhole sum_i Phi(d_i-1, 5-b_i) <= I_e and the
  accounting I_e = sum a*b) -- c-free; 0017 C1 (check 8), the c = 1
  per-pair corner a*b <= s - 1 at forced excess <= 4 -- this is (L-e)
  at X <= 4, i.e. EVERY on-f budget of Theorem A; 0017 check 9 (the
  4/3 per-pair corner at forced excess <= 5) -- T-B only; 0017 check
  12's identity (sum over pairs of K - e of (s-1) = X - x_e); 0017 C3
  (2m + 5x_e <= 52 + 3X, X-unrestricted); 0005 (min degree >= 2; (A)
  on active vertices); 0008 (D2) -- CONSUMED BY T-A, measured in
  section 5, NOT consumed by T-B; 0012/0013/0014 transitively for the
  window [22, 456].  0016's (T) as generalized by 0017 c7, and 0013's
  (3a), are inputs to C1 and reach this file only THROUGH it -- they
  are not separately consumed here (the L1.2 discipline: cite the
  conclusion or its ingredients, never both).
  DERIVES IN-CERT: (L-a) no universal vertex; (L-b) n >= 36 and the
  per-part structure; (L-c) n_2 <= floor(m/2); (L-d) w-monotonicity and
  the w-table; (L-e) the X = 5 per-edge budget; (L-f) (DH), (SC),
  Delta <= 5 + X.
  DOES NOT CONSUME: 0018 (independent corroboration -- T-A implies its
  theorem, section 7); 0017 C2; any solver.
  EXTERNAL INPUTS -- NONE.
"""

import itertools
import sys
import time
from fractions import Fraction as Fr
from math import comb

START = time.time()
FAILED = []
NCHECK = [0]
NNOTE = [0]
INTERNAL = []
NODES = [0]
LEAVES = [0]
RAW = []


def record(label, cond, sink):
    """The ONE place a verdict becomes a failure.  Split out of check()
    so that section 0's canary can drive this exact code path on a
    deliberately false condition, against a private sink, without
    reddening the run."""
    ok = bool(cond)
    if not ok:
        sink.append(label)
    return ok


def exit_code(sink):
    """The ONE place a failure becomes an exit status."""
    return 1 if sink else 0


def check(label, cond, detail=""):
    NCHECK[0] += 1
    ok = record(label, cond, FAILED)
    print("  [%s] %2d. %s%s" % ("ok  " if ok else "FAIL", NCHECK[0], label,
                                ("   " + detail) if detail else ""),
          flush=True)


def note(label, detail=""):
    NNOTE[0] += 1
    print("  [note] %s%s" % (label, ("   " + detail) if detail else ""),
          flush=True)


def head(s):
    print("\n=== %s ===" % s, flush=True)


def show(seq):
    return ", ".join(str(x) for x in seq)


def ceil_fr(x):
    """Ceiling of an exact Fraction, by integer arithmetic only."""
    return -((-x.numerator) // x.denominator)


def phi(n, k):
    """Balanced-split minimum of sum C(n_j, 2) over k classes totalling n."""
    if n <= 0:
        return 0
    q, r = divmod(n, k)
    return r * comb(q + 1, 2) + (k - r) * comb(q, 2)


def w(d):
    """The cover-free per-vertex weight Phi(d-1, 5)."""
    return phi(d - 1, 5)


def pos(d):
    """(d - 5)_+ , the star-collision defect of one vertex."""
    return d - 5 if d > 5 else 0


class LCG(object):
    """The house LCG.  Deterministic; identical on every interpreter."""

    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFF

    def next(self):
        self.s = (25214903917 * self.s + 11) & 0xFFFFFFFFFFFF
        return self.s >> 16

    def below(self, k):
        return self.next() % k


def lam(e, f):
    return sum(1 for i in range(len(e)) if e[i] == f[i])


# ==========================================================================
# S0.  The census enumerator
# ==========================================================================

def census(m, X, dmax, count_caps, Rmax, use_n2cap=True, nmin=36):
    """EVERY integer vector (n_2, ..., n_dmax) satisfying

        sum_d d * n_d      = 6m                     (first moment)
        sum_d C(d,2) * n_d = C(m,2) + X             (second moment)
        sum_d n_d          >= nmin                  (n >= 36, (L-b))
        n_2 <= floor(m/2)                           ((D2)/(L-c), optional)
        n_d <= count_caps.get(d, inf)               (branch caps)
        D := sum_d (d-5)_+ n_d <= Rmax              ((SC))

    TERMINATION IS PROVEN, not hoped: degrees are capped at dmax by
    hypothesis, and the first moment caps each n_d <= floor(6m/d) with
    all terms non-negative (degrees start at 2 by 0005), so the search
    tree is finite.  The recursion descends d = dmax..3 and SOLVES for
    n_2 from the first moment at the leaf, so no solution can be missed
    by the leaf step.  Two exact prunes, both one-line consequences of
    2 <= d' <= d on the remaining degrees:
        sum d'^2 n_d' >= 2 * sum d' n_d'  and  <= d * sum d' n_d' .
    ONE internal invariant is recorded into INTERNAL (checked in
    section 3, and again after the mutants) rather than by a bare
    assert, which -O strips: EVERY emitted vector is re-verified
    against all seven constraints from scratch before it leaves the
    leaf -- including the first-moment bound n_d <= floor(6m/d)
    RECOMPUTED FROM m, not read off the caps the recursion threads.
    (An earlier draft also guarded the values OFFERED inside rec()
    against that same bound.  That guard was unreachable by
    construction -- caps[d] <= 6m/d and the remaining first-moment
    budget only shrinks -- so it measured nothing, and it has been
    deleted rather than left standing as decoration.)
    """
    S1 = 6 * m
    S2 = m * m + 5 * m + 2 * X          # sum d^2 n_d
    caps = {}
    for d in range(2, dmax + 1):
        c = S1 // d                      # the first-moment bound
        if d in count_caps:
            c = min(c, count_caps[d])
        if d == 2 and use_n2cap:
            c = min(c, m // 2)
        caps[d] = c
    out = []
    vec = [0] * (dmax + 1)

    def rec(d, r1, r2, cnt, Drem):
        NODES[0] += 1
        if d == 2:
            if r1 < 0 or r1 % 2:
                return
            n2 = r1 // 2
            if n2 > caps[2] or 4 * n2 != r2 or cnt + n2 < nmin:
                return
            vec[2] = n2
            sol = tuple(vec[2:dmax + 1])
            if (sum((i + 2) * sol[i] for i in range(len(sol))) != S1
                or sum(comb(i + 2, 2) * sol[i]
                       for i in range(len(sol))) != comb(m, 2) + X
                or sum(sol) < nmin
                or any(sol[i] > caps[i + 2] for i in range(len(sol)))
                or any(sol[i] > 6 * m // (i + 2) for i in range(len(sol)))
                or sum(max(i - 3, 0) * sol[i]
                       for i in range(len(sol))) > Rmax):
                INTERNAL.append(("leaf", m, X, sol))
            LEAVES[0] += 1
            out.append(sol)
            return
        if r2 < 2 * r1 or r2 > d * r1:
            return
        if cnt + r1 // 2 < nmin:
            return
        wgt = d - 5 if d > 5 else 0
        mx = min(caps[d], r1 // d)
        if wgt:
            mx = min(mx, Drem // wgt)
        for k in range(mx + 1):
            vec[d] = k
            rec(d - 1, r1 - d * k, r2 - d * d * k, cnt + k, Drem - wgt * k)
        vec[d] = 0

    if dmax >= 2:
        rec(dmax, S1, S2, 0, Rmax)
    return out


head("0.  the dependency ledger, printed in-run")

print("""    CONSUMES   0013 criticality + the private minimum 5-covers T_e
                                    (tau(K-e) = 5 -- the 5 in Phi(d-1, 5-b))
               0015 steps (2)-(3)   pigeonhole + I_e accounting (c-free)
               0017 C1 (check 8)    the c = 1 per-pair corner a*b <= s-1 at
                                    forced excess <= 4 -- (L-e) at X <= 4,
                                    EVERY on-f budget of Theorem A
               0017 check 9         the 4/3 per-pair corner at X = 5 -- T-B
               0017 check 12        sum over pairs of K-e of (s-1) = X - x_e
               0017 C3              2m + 5x_e <= 52 + 3X, X-unrestricted
               0005                 min degree >= 2; (A) on active vertices
               0008 (D2)            2*D_2 <= m -- CONSUMED BY T-A ONLY
               0012/0013/0014       the window [22, 456], transitively
    THROUGH C1 0016 (T) via 0017 c7, and 0013's (3a): inputs to C1, NOT
               separately consumed here -- cite the conclusion or its
               ingredients, never both
    DERIVES    (L-a) no universal vertex   (L-b) n >= 36 + per-part
               (L-c) n_2 <= floor(m/2)     (L-d) w-monotonicity + table
               (L-e) the X = 5 budget      (L-f) (DH), (SC), Delta <= 5+X
    NOT USED   0018 (T-A implies its theorem), 0017 C2, any solver
    EXTERNAL   NONE""", flush=True)

head("0(h).  the harness canary -- the failure path itself, exercised")

_probe = []
_ok_false = record("CANARY: a deliberately false condition", False, _probe)
_ok_true = record("CANARY: a true condition", True, _probe)
check("THE HARNESS REDDENS.  Before a single mathematical claim is "
      "made, the machinery that turns a verdict into a failure is "
      "driven on a deliberately FALSE condition -- against a private "
      "sink, so the run itself stays green.  record() returned False, "
      "appended exactly that one label, and exit_code() reads 1 on the "
      "sink; a true condition returns True, appends nothing, and reads "
      "0.  check() and the final sys.exit() call these same two "
      "functions, so 'ALL GREEN' below is a measurement and not a "
      "printing convention.  (Without this, deleting the failure "
      "recording would leave every check printing [ok] and the file "
      "exiting 0 -- the one mutation no other check in this file can "
      "see)",
      _ok_false is False and _ok_true is True
      and _probe == ["CANARY: a deliberately false condition"]
      and exit_code(_probe) == 1 and exit_code([]) == 0
      and FAILED == [],
      "private sink: " + show(_probe))

# ==========================================================================
# 1.  Tables and identities
# ==========================================================================

head("1.  Phi, w, the five pointwise inequalities, and the summed laws")

ok_min = True
for n in range(0, 13):
    for k in range(1, 7):
        best = None
        for compo in itertools.product(range(n + 1), repeat=k):
            if sum(compo) == n:
                v = sum(comb(c, 2) for c in compo)
                if best is None or v < best:
                    best = v
        if best != phi(n, k):
            ok_min = False
WTAB = [w(d) for d in range(2, 12)]
check("Phi(n,k) is the EXHAUSTIVE minimum of sum C(n_j,2) over every "
      "composition of n into k classes (n <= 12, k <= 6), and the "
      "w-table it produces at d = 2..11 is 0,0,0,0,0,1,2,3,4,5 -- "
      "DERIVED, never hand-tabulated (the 0017 lesson).  Also "
      "w(d) = Phi(d-1,5) >= d - 6 for every d <= 120, the relaxation "
      "the linear laws below read at b_i = 0",
      ok_min and WTAB == [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
      and all(w(d) >= d - 6 for d in range(2, 121)),
      "w(2..11) = " + show(WTAB))
check("(L-d) MONOTONICITY: Phi(n, 5-b) >= Phi(n, 5) for every n <= 60 and "
      "b = 0..4 -- the step that turns the private cover's unknown "
      "b_i-profile into the b-free weight w(d), so every budget below "
      "is valid whatever T_e does with its five cells",
      all(phi(n, 5 - b) >= phi(n, 5)
          for n in range(0, 61) for b in range(0, 5)))


def ineq_A(d):
    return (Fr(-7, 6) * d + Fr(1, 3) * comb(d, 2) + Fr(5, 2)
            - (Fr(1, 2) if d == 2 else 0))


def ineq_B(d):
    return 4 * d - 9 + (2 if d == 2 else 0) + (2 if d == 7 else 0)


def ineq_C(d):
    return (Fr(-7, 4) * d + Fr(1, 2) * comb(d, 2) + Fr(15, 4)
            - (Fr(3, 4) if d == 2 else 0) - (Fr(3, 4) if d == 8 else 0))


def ineq_E(d):
    return ineq_A(d) - (Fr(5, 6) if d == 10 else 0)


def ineq_F(d):
    return (Fr(-6, 7) * d + Fr(2, 7) * comb(d, 2) + Fr(10, 7)
            - (Fr(5, 7) if d == 10 else 0))


SLACK = {}
for nm, fn, top in (("A", ineq_A, 9), ("C", ineq_C, 8),
                    ("E", ineq_E, 10), ("F", ineq_F, 10)):
    SLACK[nm] = [pos(d) - fn(d) for d in range(2, top + 1)]
SLACK["B"] = [ineq_B(d) - comb(d, 2) for d in range(2, 8)]
check("(A) on [2,9]: (d-5)_+ >= -(7/6)d + (1/3)C(d,2) + 5/2 - (1/2)[d=2], "
      "EXACT slacks 0, 0, 1/6, 0, 1/2, 2/3, 1/2, 0 -- and it FAILS at "
      "d = 10 (by exactly 5/6), so the range cap is load-bearing and "
      "(E) exists only to buy that one degree back",
      SLACK["A"] == [Fr(0), Fr(0), Fr(1, 6), Fr(0), Fr(1, 2), Fr(2, 3),
                     Fr(1, 2), Fr(0)]
      and pos(10) - ineq_A(10) == Fr(-5, 6),
      "slacks " + show(SLACK["A"]))
check("(B) on [2,7]: C(d,2) <= 4d - 9 + 2[d=2] + 2[d=7], slacks 1 at "
      "d = 4 and d = 5 ONLY -- and it FAILS at d = 8 (28 > 23).  This "
      "is the inequality behind the (U)-difference, and its range top "
      "is exactly why (U) is quoted only on dmax = 7 branches",
      SLACK["B"] == [0, 0, 1, 1, 0, 0] and comb(8, 2) > ineq_B(8),
      "slacks " + show(SLACK["B"]))
check("(C) on [2,8]: (d-5)_+ >= -(7/4)d + (1/2)C(d,2) + 15/4 - (3/4)[d=2] "
      "- (3/4)[d=8], slacks 0, 0, 1/4, 0, 1/4, 0, 0 -- FAILS at d = 9",
      SLACK["C"] == [Fr(0), Fr(0), Fr(1, 4), Fr(0), Fr(1, 4), Fr(0), Fr(0)]
      and pos(9) - ineq_C(9) < 0,
      "slacks " + show(SLACK["C"]))
check("(E) on [2,10] = (A)'s right side minus (5/6)[d=10]: slacks "
      "0, 0, 1/6, 0, 1/2, 2/3, 1/2, 0, 0 -- ZERO at d = 9 AND d = 10, "
      "which is what makes the m = 28 slack budget as tight as it is; "
      "FAILS at d = 11",
      SLACK["E"] == [Fr(0), Fr(0), Fr(1, 6), Fr(0), Fr(1, 2), Fr(2, 3),
                     Fr(1, 2), Fr(0), Fr(0)]
      and pos(11) - ineq_E(11) < 0,
      "slacks " + show(SLACK["E"]))
check("(F) on [2,10]: (d-5)_+ >= -(6/7)d + (2/7)C(d,2) + 10/7 - "
      "(5/7)[d=10], slacks 0, 2/7, 2/7, 0, 3/7, 4/7, 3/7, 0, 0 -- FAILS "
      "at d = 11.  (F) carries NO n_2 correction, which is why the "
      "m = 27 analytic route below spends no (D2) at all",
      SLACK["F"] == [Fr(0), Fr(2, 7), Fr(2, 7), Fr(0), Fr(3, 7), Fr(4, 7),
                     Fr(3, 7), Fr(0), Fr(0)]
      and pos(11) - ineq_F(11) < 0,
      "slacks " + show(SLACK["F"]))
note("STATED, NOT TESTED (and deliberately absent): the (Dq) machinery "
     "and the degree-11 analysis of the audit's route are NOT needed "
     "anywhere in this certificate.  Delta <= 5 + X (section 2) caps "
     "degrees at 10 for every X <= 5, so d = 11 never arises and no "
     "inequality here is ever read past its certified range")

WINDOW = list(range(22, 457))


def L(m, X):
    """(A) summed: -7m + (C(m,2)+X)/3 + 90 - floor(m/2)/2 <= D."""
    return Fr(-7) * m + Fr(comb(m, 2) + X, 3) + 90 - Fr(1, 2) * (m // 2)


LX22 = [L(22, x) for x in range(6)]
check("L_X(m) := -7m + (C(m,2)+X)/3 + 90 - (1/2)floor(m/2) is (A) summed "
      "over the vertices under n >= 36 and n_2 <= floor(m/2), and it is "
      "a LOWER BOUND ON D.  At m = 22 it reads 15/2, 47/6, 49/6, 17/2, "
      "53/6, 55/6 for X = 0..5; L_5 reads 79/6, 44/3, 17 at m = 27, 28, "
      "29; and it is STRICTLY INCREASING in m on the whole window for "
      "every X <= 5, so the m = 22 value is the window minimum",
      LX22 == [Fr(15, 2), Fr(47, 6), Fr(49, 6), Fr(17, 2), Fr(53, 6),
               Fr(55, 6)]
      and L(27, 5) == Fr(79, 6) and L(28, 5) == Fr(44, 3) and L(29, 5) == 17
      and all(L(m + 1, x) > L(m, x) for m in range(22, 456)
              for x in range(6)),
      "L_X(22) = " + show(LX22))


def G(m):
    """(B) summed at X = 3, as a difference: > 0 is a contradiction."""
    return (comb(m, 2) + 3) - (24 * m - 324 + 2 * (m // 2) + 2)


gid = all(G(m) == ((m - 25) * (m - 26) // 2 if m % 2 == 0
                   else (m * m - 51 * m + 652) // 2) for m in WINDOW)
gzero = [m for m in WINDOW if G(m) <= 0]
check("THE (U)-DIFFERENCE.  G(m) := (C(m,2)+3) - (24m - 324 + "
      "2 floor(m/2) + 2) equals (m-25)(m-26)/2 at even m and "
      "(m^2 - 51m + 652)/2 at odd m, exactly, on the whole window.  It "
      "is POSITIVE everywhere except m = 26, where it is ZERO -- the "
      "odd branch never vanishes because m^2 - 51m + 652 has "
      "discriminant 2601 - 2608 = -7 < 0",
      gid and gzero == [26] and G(26) == 0 and 51 * 51 - 4 * 652 == -7)
g4 = [G(m) + 1 for m in WINDOW]
check("AND AT X = 4 THE SAME DIFFERENCE IS G(m) + 1 > 0 EVERYWHERE, with "
      "MINIMUM EXACTLY 1, attained only at m = 26.  That single unit is "
      "the entire margin of the X = 4 some-x>=3 branch across 435 rungs "
      "-- named here, measured again in section 6",
      min(g4) == 1 and [m for m in WINDOW if G(m) + 1 == 1] == [26]
      and all(v > 0 for v in g4))


def R4(m):
    """(C) summed at X = 4 with n_8 <= 1: a lower bound on D."""
    return (Fr(-21, 2) * m + Fr(comb(m, 2) + 4, 2) + 135
            - Fr(3, 4) * (m // 2) - Fr(3, 4))


check("R4(m) := -(21/2)m + (1/2)(C(m,2)+4) + 135 - (3/4)floor(m/2) - 3/4 "
      "is (C) summed at X = 4 under n >= 36, n_2 <= floor(m/2), n_8 <= 1. "
      "R4(22) = 25/2, and R4 is strictly increasing on the window, so "
      "D >= 13 by integrality at every m -- against the branch's "
      "R = 12.  ONE UNIT",
      R4(22) == Fr(25, 2) and ceil_fr(R4(22)) == 13
      and all(R4(m + 1) > R4(m) for m in range(22, 456)))


def part_max(X, cap):
    """max sum q(q+1) over partitions of X into parts <= cap."""
    best = [0]
    plist = []

    def rec(left, mx, cur, acc):
        if left == 0:
            best[0] = max(best[0], acc)
            plist.append((tuple(cur), acc))
            return
        for p in range(min(left, mx), 0, -1):
            rec(left - p, p, cur + [p], acc + p * (p + 1))

    rec(X, min(cap, X) if X else 0, [], 0)
    return best[0], plist


RTAB = {}
for (X, cap) in ((0, 0), (1, 1), (2, 2), (3, 1), (3, 3), (4, 1), (4, 2),
                 (4, 4), (5, 1), (5, 2), (5, 5)):
    RTAB[(X, cap)] = part_max(X, cap)[0]
p52 = part_max(5, 2)[1]
check("R IS A PARTITION MAXIMUM, exhausted: over partitions of X into "
      "pair-excesses q with q <= cap, max sum q(q+1) is "
      "(2,any) 6 · (3,cap1) 6 · (3,any) 12 · (4,cap1) 8 · (4,cap2) 12 · "
      "(4,any) 20 · (5,cap1) 10 · (5,cap2) 14 · (5,any) 30.  These are "
      "the Rmax of every branch below, and at X = 5 with q <= 2 the "
      "maximum 14 is attained ONLY by (2,2,1)",
      RTAB[(2, 2)] == 6 and RTAB[(3, 1)] == 6 and RTAB[(3, 3)] == 12
      and RTAB[(4, 1)] == 8 and RTAB[(4, 2)] == 12 and RTAB[(4, 4)] == 20
      and RTAB[(5, 1)] == 10 and RTAB[(5, 2)] == 14 and RTAB[(5, 5)] == 30
      and RTAB[(0, 0)] == 0 and RTAB[(1, 1)] == 2
      and [p for (p, v) in p52 if v == 14] == [(2, 2, 1)])

BUDGET5 = [int(Fr(4, 3) * (5 - x)) for x in range(6)]
capof = {}
for b in range(0, 7):
    capof[b] = max([d for d in range(2, 13) if w(d) <= b] or [1])
check("(L-e) THE X = 5 BUDGETS, floored: floor((4/3)(5 - x_e)) = "
      "6, 5, 4, 2, 1, 0 for x_e = 0..5.  Read against the w-table: "
      "budget 2 admits d <= 8 with at most ONE 8; budget 3 admits "
      "d <= 9; budget 4 admits d <= 10 with n_10 <= 1 and n_9 + n_10 "
      "<= 1; budget 5 admits at most one d >= 10 (4 + 4 > 5).  Budget "
      "5 would also admit d = 11 (w(11) = 5) -- and DELTA <= 5 + X = 10 "
      "is what closes it, not the budget",
      BUDGET5 == [6, 5, 4, 2, 1, 0]
      and capof[2] == 8 and 2 * w(8) > 2
      and capof[3] == 9 and capof[4] == 10 and 2 * w(10) > 4
      and w(9) + w(10) > 4 and 2 * w(9) > 4
      and capof[5] == 11 and 2 * w(10) > 5)
check("and the X <= 4 budgets, the (CC4+) form sum_{v in e} w(d(v)) <= "
      "X - x_e: budget 0 caps d at 6, budget 1 at 7 with n_7 <= 1, "
      "budget 2 at 8 with n_8 <= 1, budget 3 at 9 with n_9 <= 1.  Every "
      "on-f cap in sections 3 and 4 is one of these five lines",
      capof[0] == 6 and capof[1] == 7 and 2 * w(7) > 1
      and capof[2] == 8 and capof[3] == 9 and 2 * w(9) > 3)

# ==========================================================================
# 2.  (DH) and (SC), enacted
# ==========================================================================

head("2.  the defect-hub bound and the star-collision inequality, enacted")


def famstats(fam):
    r = len(fam[0])
    m = len(fam)
    deg = {}
    for e in fam:
        for i in range(r):
            deg[(i, e[i])] = deg.get((i, e[i]), 0) + 1
    X = sum(lam(p, q) - 1 for p, q in itertools.combinations(fam, 2))
    R = sum((lam(p, q) - 1) * lam(p, q)
            for p, q in itertools.combinations(fam, 2))
    D = sum(max(d - (r - 1), 0) for d in deg.values())
    return r, m, deg, X, R, D


ACC = {"fams": 0, "pairs": 0, "dh_n": 0, "dh_bad": 0, "mate_bad": 0,
       "id_bad": 0, "id_nz": 0, "local_bad": 0, "glob_bad": 0, "sc_n": 0,
       "sc_bad": 0, "sc_tight": 0, "dgtx": 0, "univ": 0, "univ_break": 0,
       "univ_z": 0, "univ_z_break": 0, "gen_bad": 0, "m2_bad": 0,
       "dh_tight": 0, "local_tight": 0, "glob_tight": 0,
       "star_sum": 0, "Rsum": 0, "short": 0}
BYR = {}


def audit(fam):
    """Every (DH)/(SC) claim, on one family."""
    if len(fam) < 3:
        ACC["short"] += 1            # below 3 edges every claim is vacuous
        return
    r, m, deg, X, R, D = famstats(fam)
    if (any(len(e) != r for e in fam) or len(set(fam)) != m
            or any(lam(p, q) < 1 for p, q in itertools.combinations(fam, 2))):
        ACC["gen_bad"] += 1          # the generator's own hypothesis guard
        return
    ACC["fams"] += 1
    ACC["Rsum"] += R                 # (SC)'s right side, family by family
    BYR[r] = BYR.get(r, 0) + 1
    universal = any(d == m for d in deg.values())
    for z in sorted(deg):
        Ez = [e for e in fam if e[z[0]] == z[1]]
        dz = len(Ez)
        star = sum(lam(p, q) - 1 for p, q in itertools.combinations(Ez, 2))
        ACC["star_sum"] += star      # the exchange-of-summation left side
        if dz == m:
            ACC["univ_z"] += 1
            if dz > (r - 1) + star:
                ACC["univ_z_break"] += 1
            continue
        ACC["dh_n"] += 1
        if dz > (r - 1) + star:
            ACC["dh_bad"] += 1
        if dz == (r - 1) + star:
            ACC["dh_tight"] += 1     # the constant r-1 attained: sharpness
        for f in fam:
            if f[z[0]] == z[1]:
                continue                       # z lies in f
            ACC["pairs"] += 1
            ru = [sum(1 for e in Ez if e[i] == f[i]) for i in range(r)]
            if ru[z[0]] != 0:
                ACC["mate_bad"] += 1
            lhs = sum(comb(k, 2) for k in ru)
            rhs = sum(sum(1 for i in range(r) if p[i] == q[i] == f[i])
                      for p, q in itertools.combinations(Ez, 2))
            if lhs != rhs:
                ACC["id_bad"] += 1
            if lhs > 0:
                ACC["id_nz"] += 1
            if dz > (r - 1) + lhs:
                ACC["local_bad"] += 1
            if dz == (r - 1) + lhs:
                ACC["local_tight"] += 1
            xf = sum(lam(f, g) - 1 for g in fam if g != f)
            if dz > (r - 1) + X - xf:
                ACC["glob_bad"] += 1
            if dz == (r - 1) + X - xf:
                ACC["glob_tight"] += 1
    if universal:
        ACC["univ"] += 1
        if D > R:
            ACC["univ_break"] += 1
    else:
        ACC["sc_n"] += 1
        if D > R:
            ACC["sc_bad"] += 1
        if D == R:
            ACC["sc_tight"] += 1
        if D > X:
            ACC["dgtx"] += 1
        if D > sum((lam(p, q) - 1) ** 2
                   for p, q in itertools.combinations(fam, 2)):
            ACC["m2_bad"] += 1          # mutant M2, measured corpus-wide


def rand_family(r, rng, nv, target):
    fam = []
    for _ in range(400):
        if len(fam) >= target:
            break
        c = tuple(rng.below(nv) for _ in range(r))
        if c in fam:
            continue
        if all(lam(c, f) >= 1 for f in fam):
            fam.append(c)
    return fam


def greedy_family(r, nv, skip, cap):
    """Deterministic lexicographic greedy maximal intersecting family."""
    fam = []
    i = 0
    for c in itertools.product(range(nv), repeat=r):
        i += 1
        if i % skip:
            continue
        if all(lam(c, f) >= 1 for f in fam):
            fam.append(c)
        if len(fam) >= cap:
            break
    return fam


def pencil(r, k):
    """k edges through one cell -- a universal vertex by construction."""
    return [tuple([0] + [i + 1 if j == 0 else i for j in range(r - 1)])
            for i in range(k)]


def sunflower2(r, k):
    """Core of size 2."""
    return [tuple([0, 0] + [i] * (r - 2)) for i in range(k)]


def nearpencil(r, k):
    """A pencil in one part plus one edge off the hub, meeting all."""
    return ([tuple([0, i] + [0] * (r - 2)) for i in range(k)]
            + [tuple([1, k] + [0] * (r - 2))])


def rehearsal(r):
    """The tau-heavy rehearsal shape: the all-zero edge and the r edges
    with a single 1 -- pairwise intersecting for r >= 3."""
    return [c for c in itertools.product((0, 1), repeat=r) if sum(c) <= 1]


t0 = time.time()
RNG = LCG(20260728)
for r in (3, 4, 5, 6):
    built = 0
    for _ in range(6000):
        if built >= 300:
            break
        fam = rand_family(r, RNG, 2 + RNG.below(3), 3 + RNG.below(8))
        if len(fam) >= 3:
            audit(fam)
            built += 1
    for nv in (2, 3):
        for skip in (1, 2, 3, 5, 7):
            for cap in (4, 6, 8, 10, 12):
                audit(greedy_family(r, nv, skip, cap))
    for k in (3, 5, 7, 9):
        audit(pencil(r, k))
        audit(sunflower2(r, k))
        audit(nearpencil(r, k))
    audit(rehearsal(r))
CTRL3 = [(1, 1, 1), (2, 1, 2), (0, 1, 1), (2, 1, 0), (2, 0, 1)]
audit(CTRL3)
S2TIME = time.time() - t0

check("THE GENERATOR'S OWN HYPOTHESES FIRST: every family of >= 3 edges "
      "handed to the audit is checked r-partite (r-tuples), "
      "duplicate-free and PAIRWISE INTERSECTING before any claim is "
      "read off it -- 0 rejects.  (Families below 3 edges are dropped "
      "before the guard and counted separately: every claim here is "
      "vacuous on them, and there are 30.)  This guard earned its "
      "place: the first draft of this very generator emitted a "
      "NON-INTERSECTING 'near-pencil', which produced 12 spurious "
      "(DH) failures and 1,088 spurious failures of its global form.  "
      "The lemma was fine; the family was not.  An enactment that does "
      "not verify its own hypotheses is not evidence",
      ACC["gen_bad"] == 0 and ACC["fams"] == 1423 and ACC["short"] == 30
      and sorted(BYR.items()) == [(3, 339), (4, 358), (5, 363), (6, 363)]
      and all(BYR[r] >= 200 for r in (3, 4, 5, 6)),
      "families %d = %s by r; %d short families dropped"
      % (ACC["fams"], show(sorted(BYR.items())), ACC["short"]))
check("(DH) LOCAL FORM AND THE DERIVATION-MIRROR IDENTITY, on 60,416 "
      "(z, f) pairs with z not in f: the part-mate f-cell in z's own "
      "part carries r_u = 0 EVERY time (0 exceptions); the identity "
      "sum_{u in f} C(r_u,2) = sum over pairs {e,g} inside E(z) of "
      "|e cap g cap f| holds EVERY time; and d(z) <= (r-1) + "
      "sum_u C(r_u,2) every time.  31,619 of the pairs have a "
      "STRICTLY POSITIVE identity, so the mirror is exercised "
      "nonvacuously, not vacuously satisfied.  439 of the pairs sit at "
      "EQUALITY d(z) = (r-1) + sum_u C(r_u,2), so the local form is "
      "attained and its constant cannot be lowered",
      ACC["pairs"] == 60416 and ACC["pairs"] >= 50000
      and ACC["mate_bad"] == 0 and ACC["id_bad"] == 0
      and ACC["local_bad"] == 0 and ACC["id_nz"] == 31619
      and ACC["local_tight"] == 439,
      "%.1fs, %d tight" % (S2TIME, ACC["local_tight"]))
check("(DH) IN BOTH PUBLISHED FORMS, AND THE CONSTANT r-1 IS PINNED BY "
      "WITNESSES, NOT ONLY BY ABSENCE OF FAILURES: d(z) <= (r-1) + "
      "star_excess(z) on all 14,730 non-universal vertices and the "
      "global d(z) <= (r-1) + X - x_f on all 60,416 pairs -- zero "
      "failures, and 201 of the vertices sit at EQUALITY in the star "
      "form while 344 of the pairs sit at equality in the global form "
      "(439 in the local form, above).  Those equalities are what a "
      "weaker constant could not survive: (DH) with r-2 in place of "
      "r-1 is FALSE on every one of them, so the enactment tells the "
      "sharp bound from the bound-minus-one-unit -- the same job "
      "sc_tight does for (SC).  The global form is the one the caps "
      "spend, and it is what makes DELTA <= 5 + X at r = 6 a theorem "
      "about X alone: no degree cap is assumed anywhere in its "
      "derivation, which is exactly the circularity the outside "
      "audit's own write-up contained",
      ACC["dh_n"] == 14730 and ACC["dh_bad"] == 0 and ACC["glob_bad"] == 0
      and ACC["dh_tight"] == 201 and ACC["glob_tight"] == 344
      and ACC["dh_tight"] > 0 and ACC["glob_tight"] > 0,
      "tight: star %d, local %d, global %d"
      % (ACC["dh_tight"], ACC["local_tight"], ACC["glob_tight"]))
check("(SC) ENACTED: on all 849 generated families with NO universal "
      "vertex, D = sum_v (d(v)-(r-1))_+ <= R = sum over pairs of "
      "q(q+1).  Zero failures -- and 62 instances hit EQUALITY, so the "
      "inequality is SHARP and not a slack bound.  Two DISTINCT "
      "predicates are also counted here, and they must not be read as "
      "one measurement made twice: 24 families have D > X (the first "
      "must-fail control below) and 24 families have D > sum q^2 (the "
      "corpus-wide reading of mutant M2).  sum q^2 >= X always, so the "
      "second set is contained in the first; they are equal in this "
      "corpus and that is a fact, not a definition",
      ACC["sc_n"] == 849 and ACC["sc_bad"] == 0 and ACC["sc_tight"] == 62
      and ACC["sc_tight"] > 0 and ACC["dgtx"] == 24
      and ACC["m2_bad"] == 24,
      "D > X: %d;  D > sum q^2 (M2): %d -- distinct predicates, equal "
      "here" % (ACC["dgtx"], ACC["m2_bad"]))
CK_SC = NCHECK[0]
check("(SC)'s EXCHANGE OF SUMMATION, ENACTED -- the step where the "
      "q(q+1) weight is actually born.  Section 2's other checks price "
      "(DH) and the final inequality D <= R; this one prices the "
      "identity that carries one to the other.  Summed over all 1,423 "
      "families and every vertex in them, universal vertices included, "
      "sum_v star_excess(v) = sum over pairs q_eg * |e cap g| = sum "
      "over pairs q(q+1) = R, because a pair {e,g} lies inside E(v) "
      "for exactly the |e cap g| = q+1 vertices it shares.  Measured "
      "on both sides independently and equal, and strictly positive so "
      "the identity is not satisfied by two zeros",
      ACC["star_sum"] == ACC["Rsum"] and ACC["star_sum"] > 0,
      "sum_v star_excess = %d = sum_pairs q(q+1)" % ACC["star_sum"])

r3, m3, deg3, X3, R3, D3 = famstats(CTRL3)
q2sum = sum((lam(p, q) - 1) ** 2 for p, q in itertools.combinations(CTRL3, 2))
check("MUST-FAIL CONTROL 1 -- D <= X IS FALSE, and the q(q+1) factor is "
      "why.  The r = 3, m = 5 family (1,1,1), (2,1,2), (0,1,1), "
      "(2,1,0), (2,0,1) has X = 2 but D = 4: TWICE X.  It satisfies "
      "(SC) at exact equality D = R = 4.  MUTANT M2, on the same "
      "object: replace q(q+1) by q^2 and the mutated bound reads "
      "4 <= 2 and IS VIOLATED -- the lambda factor is load-bearing, "
      "not decoration",
      (X3, R3, D3) == (2, 4, 4) and D3 > X3 and q2sum == 2 and D3 > q2sum,
      "X=%d R=%d D=%d sum q^2=%d" % (X3, R3, D3, q2sum))

PEN6 = [tuple([0] + [i] * 5) for i in range(9)]
r6, m6, deg6, X6, R6, D6 = famstats(PEN6)
check("MUST-FAIL CONTROL 2 -- (SC) NEEDS 'NO UNIVERSAL VERTEX'.  The "
      "r = 6, m = 9 pencil through one cell has X = 0, hence R = 0, "
      "but D = 4 > 0.  (SC) is FALSE on it, exactly because no edge "
      "avoids the hub and (DH) has no f to spend.  In a critical core "
      "the hypothesis is free: a universal vertex is a 1-cover and "
      "tau = 6 (lemma L-a).  Across the whole generated corpus, 574 "
      "families have a universal vertex and 14 of them break (SC), and "
      "18 universal vertices break (DH) itself, so the control is not "
      "a one-off",
      (m6, X6, R6, D6) == (9, 0, 0, 4) and max(deg6.values()) == m6
      and D6 > R6 and ACC["univ"] == 574 and ACC["univ_break"] == 14
      and ACC["univ_z"] == 764 and ACC["univ_z_break"] == 18)

NP = [(1, 2, 3), (0, 1, 7), (0, 2, 8), (0, 3, 9)]
np_f = NP[0]
np_Ez = NP[1:]
np_star = sum(len(set(p) & set(q)) - 1
              for p, q in itertools.combinations(np_Ez, 2))
np_ru = [sum(1 for e in np_Ez if u in e) for u in np_f]
check("MUST-FAIL CONTROL 3 -- PARTITENESS IS LOAD-BEARING, and it is "
      "load-bearing for exactly one unit.  The NON-partite 3-uniform "
      "family f = {1,2,3}, {0,1,7}, {0,2,8}, {0,3,9} at z = 0 has "
      "d(z) = 3 while (r-1) + star_excess = 2 + 0 = 2: (DH) FAILS.  "
      "The reason is visible in the r_u vector (1,1,1): with no "
      "part-mate forced empty, the d(z) edges spread over ALL r "
      "vertices of f instead of r-1, and the -1 in the bound is gone",
      len(np_Ez) == 3 and np_star == 0 and len(np_Ez) > 2 + np_star
      and np_ru == [1, 1, 1] and sum(np_ru) == len(np_Ez))
note("STATED, NOT TESTED (lemma L-a, one line): a universal vertex is a "
     "1-cover of K, so tau(K) = 1 < 6.  Every critical core therefore "
     "satisfies (SC)'s hypothesis, and every vertex z has some edge f "
     "avoiding it -- which is all (DH) ever needs")
note("STATED, NOT TESTED (lemma L-b): each part's blocks partition the "
     "edge set, so they COVER it; a part with <= 5 blocks would be a "
     "5-cover against tau = 6.  Hence >= 6 vertices per part, "
     "n >= 36, and each part's degrees sum to m.  Both facts are "
     "consumed by every census below -- n >= 36 as a constraint, the "
     "per-part sums as the m = 26 tooth of section 3")

# ==========================================================================
# 3.  Theorem A: X <= 4 is empty across the window
# ==========================================================================

head("3.  THEOREM A -- every branch of X <= 4 is empty, at every m in "
     "[22, 456]")

BRANCH_A = [
    ("X=0, any f (x_f = 0)", 0, 6, {6: 6}, 0, WINDOW),
    ("X=1, f in the unique pair", 1, 6, {6: 6}, 2, WINDOW),
    ("X=2, f with x_f >= 1", 2, 7, {7: 1}, 6, WINDOW),
    ("X=3, all x_e <= 1", 3, 8, {8: 1}, 6, WINDOW),
    ("X=3, some x_f >= 2", 3, 7, {7: 1}, 12, list(range(22, 26))),
    ("X=4, all x_e <= 1", 4, 9, {9: 1}, 8, WINDOW),
    ("X=4, max x_e = 2", 4, 8, {8: 1}, 12, WINDOW),
    ("X=4, some x_e >= 3", 4, 7, {7: 1}, 20, WINDOW),
]


def run_branches(branches, dbump=0, capmod=None, rbump=0, nmin=36,
                 n2mode="on", only=None, capdrop=None):
    """Every (branch, m) cell; returns (cells, survivors, where).

    The number of vectors the enumerator EMITTED on this call, before
    any post-filter, is appended to RAW -- so section 5 can tie the
    module-global leaf counter LEAVES to per-run totals assembled out
    here, instead of pinning a magic constant.
    """
    cells = 0
    tot = 0
    raw = 0
    where = []
    for (lab, X, dmax, caps, Rmax, ms) in branches:
        if only is not None and lab not in only:
            continue
        cc = dict(caps)
        if capmod and lab in capmod:
            cc.update(capmod[lab])
        if capdrop and lab in capdrop:
            cc = {d: c for (d, c) in cc.items() if d > capdrop[lab]}
        for m in ms:
            cells += 1
            s = census(m, X, dmax + dbump, cc, Rmax + rbump,
                       use_n2cap=(n2mode == "on"), nmin=nmin)
            raw += len(s)
            if n2mode == "plus1":
                s = [v for v in s if v[0] <= m // 2 + 1]
            if s:
                tot += len(s)
                where.append((lab, m, len(s)))
    RAW.append(raw)
    return cells, tot, sorted(where)


t0 = time.time()
n0 = NODES[0]
cellsA, survA, whereA = run_branches(BRANCH_A)
nodesA = NODES[0] - n0
check("THE ENGINE: 3,049 (branch, m) cells -- seven branches across all "
      "435 rungs of [22, 456] plus the four rungs C3 leaves to the "
      "X = 3 heavy branch -- and ZERO configurations survive.  Every cell "
      "enforces both moment identities, n >= 36, n_2 <= floor(m/2), "
      "the branch's degree caps and D <= R.  This is Theorem A",
      cellsA == 3049 and survA == 0 and whereA == [],
      "%d search nodes, %.1fs" % (nodesA, time.time() - t0))
CK_A = NCHECK[0]
check("and the enumerator's LEAF RE-VERIFICATION held: every vector the "
      "census emits is re-checked from scratch against all seven "
      "constraints -- both moments, n >= nmin, the branch count caps, "
      "the first-moment bound n_d <= floor(6m/d) RECOMPUTED FROM m "
      "rather than read off the threaded caps, and D <= Rmax -- a "
      "guard that is vacuous here (nothing survives, so it has nothing "
      "to re-verify) and NOT vacuous in section 5, where the mutants "
      "emit thousands of vectors and every one of them is re-verified. "
      "(Recorded into a list and checked here, NOT by a bare assert -- "
      "this file must stay green under python3 -O.  An earlier draft "
      "advertised a second invariant, a guard on the values OFFERED "
      "inside the recursion; it was unreachable by construction and "
      "has been deleted rather than counted as evidence)",
      INTERNAL == [])

note("STATED, NOT TESTED -- the branch caps, one line each, all read off "
     "(DH) and (L-e).  X=0: x_f = 0, off-f d <= 5, on-f budget 0 so "
     "d <= 6 (dmax 6, n_6 <= 6), R = 0.  X=1: the unique pair gives "
     "x_f = 1, off-f <= 5, budget 0, R = 2.  X=2: sum_e x_e = 2X = 4 > 0 "
     "so some f has x_f >= 1; off-f <= 6, budget 1 (dmax 7, n_7 <= 1), "
     "R = 6.  X=3 matching: x_f = 1, off-f <= 7, budget 2 (dmax 8, "
     "n_8 <= 1), R = 6.  X=3 heavy: x_f >= 2, off-f <= 6, budget 1 "
     "(dmax 7, n_7 <= 1), R = 12.  X=4 matching: x_f = 1, off-f <= 8, "
     "budget 3 (dmax 9, n_9 <= 1), R = 8.  X=4 max-2: x_f = 2, off-f "
     "<= 7, budget 2 (dmax 8, n_8 <= 1), R = 12.  X=4 heavy: x_f >= 3, "
     "off-f <= 6, budget 1 (dmax 7, n_7 <= 1), R = 20")
note("STATED, NOT TESTED -- EXISTENCE OF f, per branch.  sum_e x_e = 2X, "
     "so at X >= 1 some edge has x_e >= 1; the branch splits are on "
     "max_e x_e, which is exhaustive by trichotomy (<= 1, = 2, >= 3 at "
     "X = 4; <= 1, >= 2 at X = 3).  At X = 0 any edge serves.  No "
     "branch assumes an f it has not produced")

c3_bound = [(x, (52 + 3 * 3 - 5 * x) // 2) for x in (2, 3)]
check("THE X = 3 HEAVY BRANCH IS CAPPED BY C3 BEFORE ANY CENSUS RUNS: "
      "0017's per-edge linear law 2m + 5x_e <= 52 + 3X reads "
      "2m <= 61 - 5x_e at X = 3, so x_e >= 2 forces 2m <= 51, m <= 25.  "
      "The census above therefore only has to cover m = 22..25 -- and "
      "the (U)-difference of section 1 independently kills every m in "
      "the window except 26, which C3 has already taken",
      c3_bound == [(2, 25), (3, 23)] and (61 - 10) // 2 == 25
      and all(G(m) > 0 for m in WINDOW if m != 26))

# ---- the m = 26 redundant tooth, three ways
head("3(t).  m = 26 on the X = 3 heavy branch -- dead already by C3, "
     "and killed again three ways, all three of them reading off "
     "tooth (a)'s pinned vector")

forced = []
for n6 in range(0, 37):
    for n3 in range(0, 37):
        for n2 in range(0, 37):
            if n2 + n3 + n6 + 1 != 36:
                continue
            if 2 * n2 + 3 * n3 + 6 * n6 + 7 != 156:
                continue
            forced.append((n2, n3, n6, 1))
forced = sorted(forced)
pinned = (13, 3, 19, 1)
check("TOOTH (a), THE (U)-EQUALITY PIN.  G(26) = 0 means (B) summed is "
      "EXACTLY tight at m = 26, so every slack source vanishes: "
      "n_4 = n_5 = 0 (slack 1 each), n = 36 exactly, n_2 = floor(26/2) "
      "= 13 exactly, n_7 = 1 exactly.  Degrees are confined to "
      "{2,3,6,7} and the first moment 2n_2+3n_3+6n_6+7n_7 = 156 then "
      "has the UNIQUE solution (n_2,n_3,n_6,n_7) = (13,3,19,1), whose "
      "second moment is 328 = C(26,2)+3 exactly -- a consistent "
      "arithmetic survivor, which is why it needs killing",
      [f for f in forced if f[0] == 13] == [pinned]
      and pinned[0] + 3 * pinned[1] + 15 * pinned[2] + 21 * pinned[3]
      == comb(26, 2) + 3
      and 2 * 13 + 3 * 3 + 6 * 19 + 7 == 156)
check("AND WHAT THE n_2 = 13 PIN ACTUALLY BUYS: drop it and the FIRST "
      "MOMENT ALONE has FIVE solutions -- (1,19,15,1), (4,15,16,1), "
      "(7,11,17,1), (10,7,18,1), (13,3,19,1).  They are first-moment "
      "solutions and nothing more: their second moments are 304, 310, "
      "316, 322 and 328 against the required C(26,2) + 3 = 328, so "
      "only the pinned one is even arithmetically admissible.  The pin "
      "shortens the argument; it does not supply the kill -- the next "
      "check measures who does",
      len(forced) == 5
      and forced == [(1, 19, 15, 1), (4, 15, 16, 1), (7, 11, 17, 1),
                     (10, 7, 18, 1), (13, 3, 19, 1)]
      and [f[0] + 3 * f[1] + 15 * f[2] + 21 * f[3] for f in forced]
      == [304, 310, 316, 322, 328]
      and comb(26, 2) + 3 == 328,
      show(forced))

BIG = 10 ** 9
c26 = census(26, 3, 7, {7: 1}, 12)
c26_nod2 = census(26, 3, 7, {7: 1}, 12, use_n2cap=False)
c26_nosc = census(26, 3, 7, {7: 1}, BIG)
c26_bare = census(26, 3, 7, {7: 1}, BIG, use_n2cap=False)
check("AND THE CENSUS KILLS m = 26 OUTRIGHT -- MEASURED WITH THIS "
      "FILE'S OWN ENUMERATOR, not asserted about it.  The branch's own "
      "census at m = 26 (X = 3, dmax 7, n_7 <= 1, R = 12) is EMPTY, "
      "with the (D2) cap on AND with it dropped.  Drop (SC) instead "
      "(R unbounded) and keep both moments, and EXACTLY ONE vector "
      "survives -- the pinned (n_2..n_7) = (13,3,0,0,19,1) -- with n_2 "
      "not pinned to 13 at all, merely capped by (D2).  Drop (D2) too "
      "and a second appears, (14,1,0,2,18,1), which (SC) kills at "
      "D = 20 > 12.  So the (U)-equality is NOT what kills this rung "
      "and the census is not standing by: what the equality buys is "
      "that the target vector is selected WITHOUT the moment argument, "
      "which is the only reason teeth (b) and (c) can be read as teeth "
      "at all",
      c26 == [] and c26_nod2 == []
      and c26_nosc == [(13, 3, 0, 0, 19, 1)]
      and sorted(c26_bare) == [(13, 3, 0, 0, 19, 1), (14, 1, 0, 2, 18, 1)]
      and 18 + 2 * 1 == 20 and 20 > 12,
      "R=12: %d survivors; R free: %s; R free, (D2) off: %s"
      % (len(c26), show(c26_nosc), show(sorted(c26_bare))))
check("TOOTH (b), THE STAR-COLLISION ONE-LINER.  The pinned census has "
      "D = n_6 + 2 n_7 = 19 + 2 = 21, against R <= 12 for X = 3 (the "
      "partition maximum of section 1).  21 > 12: dead, with no "
      "structure used at all.  Note what it runs on: tooth (a)'s "
      "pinned vector.  (b) is not independent of (a)",
      pinned[2] + 2 * pinned[3] == 21 and 21 > RTAB[(3, 3)])

msets = sorted(t for t in itertools.combinations_with_replacement(
    (2, 3, 6, 7), 6) if sum(t) == 26)
msets1 = [t for t in msets if t.count(7) <= 1]
asm = set()
for combo in itertools.combinations_with_replacement(msets1, 6):
    if sum(t.count(7) for t in combo) > 1:
        continue
    asm.add(tuple(sum(t.count(d) for t in combo) for d in (2, 3, 6, 7)))
asm_free = set()
for combo in itertools.combinations_with_replacement(msets, 6):
    asm_free.add(tuple(sum(t.count(d) for t in combo) for d in (2, 3, 6, 7)))
check("TOOTH (c), THE PER-PART CLASH.  Each part carries exactly 6 "
      "blocks (lemma L-b, at n = 36) whose degrees sum to m = 26 -- "
      "and BOTH of those, the confinement of degrees to {2,3,6,7} and "
      "n = 36 exactly, are imported from tooth (a)'s (U)-equality, so "
      "(c) is not independent of (a) either.  EXHAUSTIVELY, the size-6 "
      "multisets from {2,3,6,7} summing to 26 are exactly FOUR: "
      "{2,2,2,6,7,7}, {2,2,3,6,6,7}, {2,3,3,6,6,6}, {3,3,3,3,7,7}.  "
      "The (U)-equality pins n_7 = 1 exactly; the enumeration "
      "DELIBERATELY INVOKES ONLY THE WEAKER n_7 <= 1, both per part "
      "and globally, so the clash is established on a SUPERSET of what "
      "the pin allows.  That removes the two double-7 multisets, "
      "leaving two; the six parts then assemble into exactly two "
      "global vectors, (6,12,18,0) -- a vector the pin itself already "
      "excludes -- and (7,11,17,1).  NEITHER is (13,3,19,1).  "
      "Contradiction",
      len(msets) == 4 and msets == [(2, 2, 2, 6, 7, 7), (2, 2, 3, 6, 6, 7),
                                    (2, 3, 3, 6, 6, 6), (3, 3, 3, 3, 7, 7)]
      and len(msets1) == 2
      and sorted(asm) == [(6, 12, 18, 0), (7, 11, 17, 1)]
      and pinned not in asm)
CK_TC = NCHECK[0]
note("STATED, NOT TESTED: the three teeth are REDUNDANT by construction "
     "-- C3 already caps this branch at m <= 25, so m = 26 is dead "
     "before any of them speaks, and the census of the previous check "
     "empties it independently of all three.  Nor are the teeth "
     "independent OF EACH OTHER: (b) and (c) both run on (a)'s pinned "
     "vector, and (c) borrows (a)'s degree confinement and n = 36 as "
     "well.  The independent kill is C3.  They are kept because the "
     "desk's first pass reached m = 26 through the (U) route alone, "
     "where the difference is exactly zero and one wrong slack would "
     "have been fatal.  Redundancy at a zero-margin rung is not "
     "padding -- but it should be labelled as redundancy, not as "
     "independence")

# ---- the analytic mirror, branch by branch
head("3(x).  the analytic cross-assertions -- every branch killed twice")

XA = []
for (lab, X, Rm, bound, val) in (
        ("X=0", 0, 0, ceil_fr(L(22, 0)), 8),
        ("X=1", 1, 2, ceil_fr(L(22, 1)), 8),
        ("X=2", 2, 6, ceil_fr(L(22, 2)), 9),
        ("X=3 matching", 3, 6, ceil_fr(L(22, 3)), 9),
        ("X=4 matching", 4, 8, ceil_fr(L(22, 4)), 9)):
    XA.append((lab, bound, Rm, bound == val and bound > Rm))
check("(A) SUMMED, WITH INTEGRALITY, KILLS FIVE BRANCHES ON ITS OWN: D "
      "is an integer and D >= L_X(22) at the window's minimum, so "
      "D >= 8, 8, 9, 9, 9 at X = 0, 1, 2, 3-matching, 4-matching "
      "against R = 0, 2, 6, 6, 8.  L_X is increasing in m, so the "
      "m = 22 reading covers all 435 rungs at once",
      all(t[3] for t in XA),
      show(["%s: %d > %d" % (t[0], t[1], t[2]) for t in XA]))
check("(C) SUMMED KILLS THE X = 4 MAX-2 BRANCH: D >= R4(22) = 25/2, so "
      "D >= 13 by integrality, against R = 12.  ONE UNIT -- and it is "
      "the smallest margin in Theorem A's analytic mirror",
      ceil_fr(R4(22)) == 13 and 13 > RTAB[(4, 2)]
      and RTAB[(4, 2)] == 12)
check("(B) SUMMED KILLS THE X = 4 HEAVY BRANCH ACROSS THE WHOLE WINDOW: "
      "at dmax 7 with n_7 <= 1 the (U)-difference reads G(m) + 1 > 0 "
      "at EVERY m in [22, 456], minimum exactly 1 at m = 26.  No "
      "census needed anywhere on that branch -- though the census ran "
      "on all 435 rungs anyway and agreed",
      all(G(m) + 1 > 0 for m in WINDOW) and min(G(m) + 1 for m in WINDOW) == 1)

# ==========================================================================
# 4.  Theorem B: X = 5 forces m <= 26
# ==========================================================================

head("4.  THEOREM B -- X = 5 forces m <= 26")

rungs = [(m, (67 - 2 * m) // 5) for m in range(27, 32)]
check("C3 AT X = 5: 2m + 5 x_e <= 52 + 15 = 67.  sum_e x_e = 2X = 10 > 0 "
      "so SOME edge has x_e >= 1, whence 2m <= 62 and m <= 31 -- the "
      "whole of X = 5 above m = 26 is five rungs wide.  The per-rung "
      "caps floor((67-2m)/5) are 2, 2, 1, 1, 1 at m = 27..31, so "
      "m >= 29 admits only x_e <= 1: a 5-MATCHING of lambda-2 pairs, "
      "R = 10 exactly",
      rungs == [(27, 2), (28, 2), (29, 1), (30, 1), (31, 1)]
      and (67 - 5) // 2 == 31 and RTAB[(5, 1)] == 10)

BRANCH_B = [
    ("X=5, m>=29, 5-matching", 5, 10, {10: 1}, 10, [29, 30, 31]),
    ("X=5, m=28, 5-matching", 5, 10, {10: 1}, 10, [28]),
    ("X=5, m=28, some x_f=2", 5, 10, {10: 1}, 14, [28]),
    ("X=5, m=27, 5-matching", 5, 10, {10: 1}, 10, [27]),
    ("X=5, m=27, some x_f=2", 5, 10, {10: 1}, 14, [27]),
]

# ---- the thirteen branch cap-triples, re-derived rather than trusted
BSPEC = [
    ("X=0, any f (x_f = 0)", 0, 0, 0),
    ("X=1, f in the unique pair", 1, 1, 1),
    ("X=2, f with x_f >= 1", 2, 1, 2),
    ("X=3, all x_e <= 1", 3, 1, 1),
    ("X=3, some x_f >= 2", 3, 2, 3),
    ("X=4, all x_e <= 1", 4, 1, 1),
    ("X=4, max x_e = 2", 4, 2, 2),
    ("X=4, some x_e >= 3", 4, 3, 4),
    ("X=5, m>=29, 5-matching", 5, 1, 1),
    ("X=5, m=28, 5-matching", 5, 1, 1),
    ("X=5, m=28, some x_f=2", 5, 2, 2),
    ("X=5, m=27, 5-matching", 5, 1, 1),
    ("X=5, m=27, some x_f=2", 5, 2, 2),
]
DERIVED = []
for (lab, X, xf, qcap) in BSPEC:
    b = BUDGET5[xf] if X == 5 else X - xf
    dm = min(capof[b], 5 + X) if X == 5 else capof[b]
    DERIVED.append((lab, X, dm, {dm: 6 if b == 0 else 1}, RTAB[(X, qcap)]))
LITERAL = [(lab, X, dmax, caps, Rmax)
           for (lab, X, dmax, caps, Rmax, ms) in BRANCH_A + BRANCH_B]
OFFF = [(BUDGET5[xf] if X == 5 else X - xf, 5 + (X - xf), X)
        for (lab, X, xf, qcap) in BSPEC]
check("THE BRANCH TABLES ARE HAND-TRANSCRIBED LITERALS, SO THEY ARE "
      "RE-DERIVED HERE: every one of the 13 (dmax, count cap, Rmax) "
      "triples in BRANCH_A and BRANCH_B is recomputed from the tables "
      "section 1 exhausted -- dmax = capof[budget] (and at X = 5 also "
      "min'd against DELTA <= 5 + X = 10), the count cap sitting at "
      "dmax and reading 6 at budget 0 (f has six vertices, every one "
      "of weight 0) and 1 at budget >= 1 (because 2 w(dmax) > budget), "
      "and Rmax = RTAB[(X, cap on q)] -- and every literal MATCHES.  "
      "The dangerous direction is TIGHTNESS: a literal stronger than "
      "its derivation would empty a layer that the lemmas do not "
      "empty, and nothing else in this file would notice, since an "
      "over-tight cap produces exactly what a correct one does -- "
      "nothing.  A literal looser than licensed is merely "
      "conservative, and this check reports that too.  "
      "Also verified: in every branch the on-f cap dominates the off-f "
      "cap 5 + (X - x_f), which is why dmax is read off (L-e) and the "
      "count cap off f's six vertices",
      LITERAL == DERIVED and len(LITERAL) == 13
      and all(w(t[2]) == 0 if OFFF[i][0] == 0 else 2 * w(t[2]) > OFFF[i][0]
              for i, t in enumerate(DERIVED))
      and all(t[2] >= OFFF[i][1] for i, t in enumerate(DERIVED)),
      "13 triples re-derived from capof[] and RTAB[], 0 mismatches")

t0 = time.time()
n0 = NODES[0]
cellsB, survB, whereB = run_branches(BRANCH_B)
nodesB = NODES[0] - n0
tight = []
for m in (27, 28):
    base = census(m, 5, 10, {10: 1}, 14)
    tight.append((m, len(base), len([v for v in base if v[7] + v[8] <= 1])))
check("THE X = 5 ENGINE: seven (branch, m) cells over m = 27..31 -- the "
      "5-matching branch at every rung, plus the max-x=2 branch at "
      "m = 27 and 28 where C3 still allows it -- and ZERO configurations "
      "survive.  Caps: off-f d <= 9 (or 8 at x_f = 2) by (DH), on-f by "
      "the floored 4/3 budget, dmax 10 by DELTA <= 5 + X, n_10 <= 1.  "
      "The SECOND, tighter run of the max-2 branch with n_9 + n_10 <= 1 "
      "(the budget-4 reading) is empty too, necessarily so -- it is a "
      "filter over an enumeration that is already empty, and it buys "
      "nothing that the conservative run has not already bought",
      cellsB == 7 and survB == 0 and whereB == []
      and tight == [(27, 0, 0), (28, 0, 0)],
      "%d search nodes, %.1fs; tighter run at m = 27, 28: base 0 -> "
      "filtered 0 both times" % (nodesB, time.time() - t0))
CK_B = NCHECK[0]

ceil29 = ceil_fr(L(29, 5) - Fr(5, 6))
check("CROSS-ASSERTION AT m = 29..31, the (E) route: D >= L_5(29) - 5/6 "
      "= 97/6 (the 5/6 is (E)'s single correction, spent on n_10 <= 1), "
      "so D >= 17 by integrality against R = 10.  Seven units of "
      "slack: the top of Theorem B's range is not where it is thin",
      L(29, 5) == 17 and ceil29 == 17 and 17 > 10)

SRC28 = {"n4": Fr(1, 6), "n6": Fr(1, 2), "n7": Fr(2, 3), "n8": Fr(1, 2),
         "extra-n": Fr(5, 2), "n2-deficit": Fr(1, 2), "n10-missing": Fr(5, 6)}
SRC27 = {"n3": Fr(2, 7), "n4": Fr(2, 7), "n6": Fr(3, 7), "n7": Fr(4, 7),
         "n8": Fr(3, 7), "extra-n": Fr(10, 7), "n10-missing": Fr(5, 7)}


def slack_multisets(src, budget):
    """EVERY multiset of slack sources whose total cost fits the budget."""
    keys = sorted(src)
    out = []

    def rec(i, left, cur):
        if i == len(keys):
            out.append(tuple(cur))
            return
        j = 0
        while src[keys[i]] * j <= left:
            rec(i + 1, left - src[keys[i]] * j,
                cur + [(keys[i], j)] if j else cur)
            j += 1

    rec(0, budget, [])
    return sorted(out)


def slack_cases(src, base, R, use_ceil=True):
    """For each admissible slack multiset: the forced D-form c + 4 n_9,
    and whether an integer D in [bound, R] of that form exists."""
    lo = ceil_fr(base) if use_ceil else base.numerator // base.denominator
    out = []
    for c in slack_multisets(src, R - base):
        dd = dict(c)
        cD = (dd.get("n6", 0) + 2 * dd.get("n7", 0) + 3 * dd.get("n8", 0)
              + (0 if "n10-missing" in dd else 5))
        sol = [D for D in range(lo, R + 1) if D >= cD and (D - cD) % 4 == 0]
        out.append((c, cD, sol))
    return out


case28 = slack_cases(SRC28, Fr(83, 6), 14)
check("m = 28, THE MAX-2 BRANCH, WHERE THE STAR-COLLISION BOUND IS "
      "EXACTLY TIGHT.  (E) summed gives D >= 44/3 - 5/6 = 83/6, so "
      "D = 14 = R exactly, and the whole kill is a divisibility "
      "argument on a ZERO margin.  Slack budget 14 - 83/6 = 1/6, and "
      "EXHAUSTIVELY over the seven slack sources the ONLY admissible "
      "non-empty multiset is {n_4: 1} (every other source costs >= "
      "1/2).  Both admissible cases force n_6 = n_7 = n_8 = 0 and "
      "n_10 = 1, hence D = 5 + 4 n_9 = 14 -- INSOLUBLE in integers",
      len(case28) == 2
      and sorted(tuple(sorted(dict(c).items())) for c, _, _ in case28)
      == [(), (("n4", 1),)]
      and all(cD == 5 and sol == [] for _, cD, sol in case28),
      "budget " + str(14 - Fr(83, 6)))
CK_28 = NCHECK[0]

case27 = slack_cases(SRC27, Fr(95, 7), 14)
live27 = [c for c in case27 if c[2]]
check("m = 27, THE SAME SHAPE ONE RUNG DOWN, VIA (F).  (F) summed gives "
      "D >= 95/7 (and (F) spends NO n_2 correction -- this rung is "
      "(D2)-free), so again D = 14 = R and the slack budget is 3/7.  "
      "Five multisets fit; the only ones that move D are {n_6: 1} and "
      "{n_8: 1}.  Case 8 gives D = 8 + 4 n_9 = 14, insoluble; the "
      "three D = 5 + 4 n_9 cases are insoluble; case 6 gives "
      "D = 6 + 4 n_9 = 14 with n_9 = 2 and is the ONLY survivor of "
      "this step",
      len(case27) == 5 and len(live27) == 1
      and dict(live27[0][0]) == {"n6": 1} and live27[0][2] == [14])
CK_27 = NCHECK[0]

# case 6 residual system: n3 = n4 = 0, n = 36, n2 free, n5 free,
# n6 = 1, n7 = n8 = 0, n9 = 2, n10 = 1
n_rest = 36 - 1 - 2 - 1
lhs_slots = 6 * 27 - (6 * 1 + 9 * 2 + 10 * 1)
n5_sol = Fr(lhs_slots - 2 * n_rest, 3)
check("AND CASE 6 DIES ON ITS RESIDUAL LINEAR SYSTEM.  The 3/7 budget "
      "is fully spent by n_6 = 1, so n_3 = n_4 = 0 (2/7 each), n = 36 "
      "exactly and n_10 = 1.  Then n_2 + n_5 = 32 and 2 n_2 + 5 n_5 = "
      "128, giving 3 n_5 = 64: n_5 = 64/3, NOT AN INTEGER.  m = 27 is "
      "dead, and with it Theorem B",
      n_rest == 32 and lhs_slots == 128 and n5_sol == Fr(64, 3)
      and n5_sol.denominator != 1,
      "n_5 = " + str(n5_sol))
check("THEOREM B ASSEMBLED -- A RESTATEMENT, NOT A FIFTH KILL.  Every "
      "conjunct below is already asserted above (the seven cells and "
      "zero survivors in the engine check, the m <= 31 rung list in "
      "the C3 check, the m = 28 slack cases, the single live m = 27 "
      "case, and its 64/3): this line assembles them and says what "
      "they add up to.  X = 5 forces m <= 26.  With Theorem A "
      "(X >= 5 everywhere), m >= 27 forces X >= 6 -- the window's low "
      "end now carries a strictly higher excess floor than its floor "
      "rung does",
      cellsB == 7 and survB == 0 and rungs[-1] == (31, 1)
      and all(sol == [] for _, _, sol in case28)
      and len(live27) == 1 and n5_sol.denominator == 3)

# ==========================================================================
# 5.  The mutation suite -- every cap carries a tooth
# ==========================================================================

head("5.  the mutation suite: nine mutants in eleven measured readings")

MUT = []
leaves0 = LEAVES[0]
raw0 = len(RAW)
CAPDROP = {lab: 6 + X - xf for (lab, X, xf, qcap) in BSPEC}

t0 = time.time()
_, m1a, w1a = run_branches(BRANCH_A, dbump=1)
_, m1b, w1b = run_branches(BRANCH_B, dbump=1)
MUT.append(("M1  dmax + 1 (a RELAXATION of DH 5 -> 6)",
            "%d, %d" % (CK_A, CK_B), m1a + m1b,
            "S3 %d in 3 branches (m 22..28), S4 %d at m=27 max-2"
            % (m1a, m1b)))
check("M1 -- THE DEGREE CAPS, RAISED BY ONE, AND IT IS A STRICT "
      "RELAXATION OF '(DH) 5 -> 6' RATHER THAN THAT MUTATION ITSELF.  "
      "This run bumps every dmax by one while leaving the count caps "
      "KEYED AT THE OLD DEGREES, so it admits configurations no "
      "reading of the (DH) constant permits -- a degree-9 vertex on "
      "the X = 4 max-2 branch, say, which neither a mutated off-f cap "
      "of 8 nor a budget-2 on-f cap would allow.  Stated as what it "
      "is: 971 configurations revive, 947 in Theorem A (X=3 heavy at "
      "m = 22..25, X=4 max-2 at m = 22..25, X=4 heavy at m = 22..28) "
      "and 24 in Theorem B (m = 27, max-2).  The faithful mutation is "
      "the next check; both say the same thing about the wall",
      m1a == 947 and m1b == 24 and m1a + m1b == 971
      and sorted(set(t[0] for t in w1a)) == ["X=3, some x_f >= 2",
                                             "X=4, max x_e = 2",
                                             "X=4, some x_e >= 3"]
      and sorted(set(t[0] for t in w1b)) == ["X=5, m=27, some x_f=2"])

_, m1pa, w1pa = run_branches(BRANCH_A, capdrop=CAPDROP)
_, m1pb, w1pb = run_branches(BRANCH_B, capdrop=CAPDROP)
MUT.append(("M1' off-f cap +1 (faithful DH 5 -> 6)",
            str(CK_A), m1pa + m1pb,
            "S3 %d (X=4 max-2 m 22..24, X=4 heavy m 22..27), S4 %d"
            % (m1pa, m1pb)))
check("M1' -- THE (DH) CONSTANT, MUTATED FAITHFULLY.  Raising 5 to 6 "
      "moves the OFF-f cap 5 + (X - x_f) by one and leaves (L-e)'s "
      "on-f budget alone; since the on-f cap already sits exactly one "
      "above the off-f cap in every branch, the effect is precise: "
      "dmax is unchanged and the count cap at dmax is VOIDED, because "
      "the degree that used to be forced onto f no longer is.  Only "
      "where the on-f cap sits TWO above -- the X = 5 max-2 branches, "
      "off-f 8 against dmax 10 -- does n_10 <= 1 survive the mutation, "
      "and it does.  Measured: 193 configurations revive in Theorem A "
      "(X=4 max-2 at m = 22..24, X=4 heavy at m = 22..27) and ZERO in "
      "Theorem B.  So the wall is real in T-A, and T-B does not lean "
      "on the constant at all",
      m1pa == 193 and m1pb == 0 and w1pb == []
      and sorted(set(t[0] for t in w1pa)) == ["X=4, max x_e = 2",
                                              "X=4, some x_e >= 3"]
      and sorted(set(t[1] for t in w1pa)) == [22, 23, 24, 25, 26, 27],
      "T-A %d, T-B %d" % (m1pa, m1pb))

_, m3a, w3a = run_branches(BRANCH_A, n2mode="plus1")
_, m3b, w3b = run_branches(BRANCH_B, n2mode="plus1")
_, m3c, w3c = run_branches(BRANCH_A, n2mode="off")
_, m3d, w3d = run_branches(BRANCH_B, n2mode="off")
MUT.append(("M3  (D2) cap floor(m/2) -> floor(m/2)+1",
            str(CK_A), m3a + m3b,
            "S3 %d, S4 %d -- (D2) IS consumed by T-A, NOT by T-B"
            % (m3a, m3b)))
MUT.append(("M3' (D2) dropped entirely",
            str(CK_A), m3c + m3d,
            "S3 %d in four branches, S4 %d" % (m3c, m3d)))
check("M3 -- AND IT IS THE LEDGER-DECIDING MEASUREMENT.  The spec asked "
      "whether ANY branch of EITHER engine needs 0008's (D2) cap.  "
      "Measured, both ways: relax n_2 <= floor(m/2) to floor(m/2)+1 and "
      "THREE configurations survive -- X=4 max-2 at m = 22, X=4 heavy "
      "at m = 24 and m = 25.  Drop the cap entirely and 279 survive "
      "across FOUR branches of Theorem A.  So (D2) STAYS CONSUMED, and the "
      "branches that need it are named.  This certificate does NOT hold "
      "without (D2)",
      m3a == 3 and m3c == 279
      and [(t[0], t[1]) for t in w3a] == [("X=4, max x_e = 2", 22),
                                          ("X=4, some x_e >= 3", 24),
                                          ("X=4, some x_e >= 3", 25)]
      and sorted(set(t[0] for t in w3c)) == ["X=3, some x_f >= 2",
                                             "X=4, all x_e <= 1",
                                             "X=4, max x_e = 2",
                                             "X=4, some x_e >= 3"])
check("M3, THE OTHER HALF OF THE SAME MEASUREMENT, AND IT IS A FINDING: "
      "THEOREM B IS (D2)-FREE.  Every X = 5 census run at m = 27..31 "
      "is empty with the cap relaxed by one AND with it dropped "
      "entirely -- 0 survivors both ways.  The m = 27 analytic route is (D2)-free "
      "too, by (F)'s missing n_2 term; only the m = 28 route spends it, "
      "and there the census carries the kill regardless.  X = 5 forces "
      "m <= 26 WITHOUT certificate 0008",
      m3b == 0 and m3d == 0 and w3b == [] and w3d == [])

_, m4, w4 = run_branches(BRANCH_A, capmod={"X=4, max x_e = 2": {8: 2}},
                         only={"X=4, max x_e = 2"})
MUT.append(("M4  n_8 cap 1 -> 2, X=4 max-2 branch",
            str(CK_A), m4, "1 survivor, m = 22 only (spec expected 22..25)"))
check("M4 -- THE n_8 CAP.  Allow a second degree-8 vertex on the X = 4 "
      "max-2 branch and ONE configuration survives, at m = 22.  MEASURED "
      "AGAINST THE SPEC'S EXPECTATION, which predicted survivors "
      "across m = 22..25: only the floor rung revives, and it revives "
      "by a single configuration.  The cap is a tooth, but a narrow "
      "one -- said plainly rather than rounded up",
      m4 == 1 and [(t[1], t[2]) for t in w4] == [(22, 1)])

_, m5, w5 = run_branches(BRANCH_B,
                         capmod={"X=5, m=27, 5-matching": {10: 2},
                                 "X=5, m=27, some x_f=2": {10: 2}},
                         only={"X=5, m=27, 5-matching",
                               "X=5, m=27, some x_f=2"})
MUT.append(("M5  n_10 cap 1 -> 2 at m = 27",
            str(CK_B), m5, "3 survivors, m = 27 max-2 branch"))
check("M5 -- THE n_10 CAP AT THE THIN RUNG.  Allow two degree-10 "
      "vertices at m = 27 and three configurations survive, all on the max-2 "
      "branch.  n_10 <= 1 comes from the floored 4/3 budget (two tens "
      "cost 8 > 5), so this mutant prices 0017 check 9's corner "
      "directly: without the 4/3 rung, Theorem B's bottom rung is open",
      m5 == 3 and sorted(set(t[0] for t in w5)) == ["X=5, m=27, some x_f=2"])

_, m6, w6 = run_branches(BRANCH_A, rbump=1, only={"X=4, max x_e = 2"})
MUT.append(("M6  R -> R + 1 on the X=4 max-2 branch",
            str(CK_A), m6, "2 at m=22, 1 at m=23"))
check("M6 -- THE R VALUE ITSELF.  Add ONE unit to the X = 4 max-2 "
      "branch's R = 12 and three configurations survive, at m = 22 and "
      "23.  R = 12 is section 1's partition maximum; this "
      "mutant is what makes that check load-bearing rather than "
      "decorative",
      m6 == 3 and [(t[1], t[2]) for t in w6] == [(22, 2), (23, 1)])

MUT.append(("M7  drop n_7 <= 1 in tooth (c)",
            str(CK_TC), len(asm_free),
            "4 per-part multisets not 2; 49 assembled vectors not 2"))
check("M7 -- THE EXPLICIT n_7 <= 1 IN THE PER-PART TOOTH, AND IT IS "
      "NOT LOAD-BEARING.  Skip it and the per-part enumeration keeps "
      "all FOUR multisets instead of two, and the six parts assemble "
      "into 49 global vectors instead of 2.  MEASURED, AND IT IS THE "
      "OPPOSITE OF WHAT THE DRAFT ASSERTED: (13,3,19,1) is absent from "
      "ALL 49, so tooth (c)'s actual contradiction -- assembled != "
      "pinned -- SURVIVES the relaxation untouched.  The invocation "
      "sharpens the tooth and shrinks the enumeration; it does not "
      "carry it.  What the pin does buy is visible elsewhere: THREE of "
      "the 49 -- (4,18,4,10), (7,13,9,7), (10,8,14,4) -- satisfy the "
      "second moment 328 and would be live vectors without the (U)-pin "
      "context, and each carries n_7 in {4,7,10}",
      len(msets) == 4 and len(msets1) == 2 and len(asm_free) == 49
      and len(asm) == 2 and pinned not in asm_free
      and sorted(v for v in asm_free
                 if v[0] + 3 * v[1] + 15 * v[2] + 21 * v[3] == 328)
      == [(4, 18, 4, 10), (7, 13, 9, 7), (10, 8, 14, 4)],
      "pinned in the 49? %s" % (pinned in asm_free))

case27f = slack_cases(SRC27, Fr(95, 7), 14, use_ceil=False)
case28f = slack_cases(SRC28, Fr(83, 6), 14, use_ceil=False)
live27f = [c for c in case27f if c[2]]
live28f = [c for c in case28f if c[2]]
MUT.append(("M8  floor not ceil on 95/7 and 83/6",
            "%d, %d" % (CK_28, CK_27), len(live27f) + len(live28f),
            "soluble slack cases 1 -> 4 at m=27, 0 -> 2 at m=28"))
check("M8 -- INTEGRALITY, AND IT IS NOT A ROUNDING PREFERENCE.  D >= "
      "95/7 with D an integer means D >= 14, not 13; read it with "
      "floor instead of ceil and the m = 27 slack analysis goes from "
      "ONE soluble case to FOUR, and m = 28 from ZERO to TWO -- every "
      "new case being D = 13, a value the exact bound forbids.  The "
      "mutant reads differently, and it reads WEAKER",
      len(live27) == 1 and len(live27f) == 4
      and len(case28) == 2 and len(live28f) == 2
      and all(13 in sol for _, _, sol in live28f))

_, m9a, w9a = run_branches(BRANCH_A, nmin=35)
_, m9b, w9b = run_branches(BRANCH_B, nmin=35)
MUT.append(("M9  n >= 36 -> n >= 35",
            "%d, %d" % (CK_A, CK_B), m9a + m9b,
            "S3 %d (55 at m=22, X=4 max-2), S4 %d at m=27" % (m9a, m9b)))
check("M9 -- THE VERTEX COUNT.  Lower n >= 36 to n >= 35 -- one block "
      "short in one part -- and 183 configurations come alive (173 in "
      "Theorem A, led by X = 4 max-2 with 55 at m = 22; 10 in Theorem "
      "B at m = 27).  n >= 36 is lemma L-b, a two-line consequence of "
      "tau = 6, and it is doing as much work as any cap in the file",
      m9a == 173 and m9b == 10
      and sorted(set(t[0] for t in w9a)) == ["X=3, some x_f >= 2",
                                             "X=4, all x_e <= 1",
                                             "X=4, max x_e = 2",
                                             "X=4, some x_e >= 3"])
MUT.append(("M2  R's q(q+1) -> q^2",
            str(CK_SC), ACC["m2_bad"],
            "families in the corpus that VIOLATE the mutant (D = 4 > 2 "
            "on control 1)"))
MUTS = sorted(MUT)
print("\n      MUTANT                                   REDDENS       COUNT"
      "   MEASURED WHERE", flush=True)
for (nm, wh, n, det) in MUTS:
    print("      %-40s %-13s %5d   %s"
          % (nm, "check " + wh, n, det), flush=True)
check("THE MUTATION TABLE, printed above, is COMPLETE over the "
      "certificate's parameters (and the enumerator's leaf "
      "re-verification held across every mutant run too): the (DH) "
      "constant (M1 as a relaxation, M1' faithfully), the (SC) "
      "weight (M2), the (D2) cap (M3, both readings), the two count "
      "caps n_8 and n_10 (M4, M5), the R value (M6), the n_7 <= 1 "
      "invocation (M7), the integrality step (M8) and the vertex "
      "floor (M9).  Every one of them reddens something except M7, "
      "which is recorded as inert rather than quietly dropped, and "
      "each count above is a MEASUREMENT made in this run, not a "
      "prediction.  The leaf counter is tied to the runs rather than "
      "pinned to a constant: the vectors emitted since section 5 began "
      "equal the sum of the per-run emission totals assembled at the "
      "caller, so adding, removing or reordering a census call cannot "
      "silently break this line",
      len(MUTS) == 11 and all(isinstance(t[2], int) for t in MUTS)
      and m1a + m1b > 0 and m1pa > 0 and m3a > 0 and m4 > 0 and m5 > 0
      and m6 > 0 and m9a + m9b > 0 and len(asm_free) > len(asm)
      and len(live27f) > len(live27) and ACC["m2_bad"] == 24
      and INTERNAL == []
      and LEAVES[0] - leaves0 == sum(RAW[raw0:])
      and sum(RAW[raw0:]) > 0,
      "%d mutant vectors emitted in section 5 (= the sum of %d per-run "
      "totals), every one re-verified against all seven census "
      "constraints at the leaf; 0 internal violations, %.1fs"
      % (LEAVES[0] - leaves0, len(RAW) - raw0, time.time() - t0))

# ==========================================================================
# 6.  Margins -- measured and named (D-035)
# ==========================================================================

head("6.  the margins, every one named")

check("ONE UNIT, TWICE, in Theorem A's analytic mirror: the X = 4 "
      "matching branch closes 9 against 8, and the X = 4 max-2 branch "
      "closes 13 against 12.  Both are ceilings of exact Fractions "
      "(53/6 and 25/2) -- lose one unit of either and the branch needs "
      "its census alone",
      ceil_fr(L(22, 4)) == 9 and RTAB[(4, 1)] == 8
      and ceil_fr(R4(22)) == 13 and RTAB[(4, 2)] == 12)
check("ONE UNIT AGAIN in the (U)-difference: G(24) = G(25) = 1 exactly, "
      "and G(m) + 1 has minimum exactly 1 at m = 26.  Two rungs of the "
      "X = 3 heavy branch and the entire X = 4 heavy branch sit one "
      "unit from open",
      G(24) == 1 and G(25) == 1 and min(G(m) + 1 for m in WINDOW) == 1)
check("ZERO UNITS AT m = 27 AND m = 28: there D is FORCED to equal "
      "R = 14 exactly, the star-collision bound is tight, and nothing "
      "is killed by size.  The DIVISIBILITY kills are 5 + 4 n_9 = 14 "
      "and 8 + 4 n_9 = 14; the cD = 6 case SURVIVES divisibility "
      "(6 + 4 n_9 = 14 gives n_9 = 2) and dies one step later on the "
      "non-integrality of n_5 = 64/3.  A certificate whose thinnest "
      "rung has zero slack should say so in its headline, and this one "
      "does",
      ceil_fr(Fr(83, 6)) == 14 and ceil_fr(Fr(95, 7)) == 14
      and RTAB[(5, 2)] == 14 and n5_sol == Fr(64, 3))
check("THE DEGREE-CAP SENSITIVITY, from M1/M1' and M9: +1 on every "
      "degree cap revives 971 configurations, the faithful (DH) 5 -> 6 "
      "revives 193, and -1 on the vertex floor revives 183.  Those two "
      "coordinates are worth more than every other margin in this file "
      "combined, and both are theorems (DH, L-b) rather than "
      "assumptions.  AND ONE CELL CARRIES MORE OF THEM THAN ANY OTHER: "
      "X = 4 max-2 at m = 22 revives under five of the nine mutants -- "
      "M1 (both readings), M3 (both readings), M4, M6, M9, seven of "
      "the eleven measured rows.  No other cell revives under more "
      "than three.  It is the single thinnest configuration here, and "
      "it is exactly the rung certificate 0018's frontier sat on",
      m1a + m1b == 971 and m1pa == 193 and m9a + m9b == 183
      and [len([t for t in wh
                if t[0] == "X=4, max x_e = 2" and t[1] == 22]) == 1
           for wh in (w1a, w1pa, w3a, w3c, w4, w6, w9a)] == [True] * 7)
note("STATED, NOT TESTED, and it is the honest shape of the (D2) "
     "margin: Theorem A's dependence on 0008 is now MEASURED at three "
     "configurations (M3) rather than asserted.  If 0008 is ever "
     "weakened, the three named cells -- X=4 max-2 at m=22, X=4 heavy at m=24 "
     "and m=25 -- are exactly what must be redone.  Theorem B needs no "
     "such maintenance clause")

# ==========================================================================
# 7.  Controls
# ==========================================================================

head("7.  controls -- what this certificate must NOT contradict")

t0 = time.time()
_, s22, _ = run_branches([b for b in BRANCH_A if b[1] == 3],
                         only={"X=3, all x_e <= 1", "X=3, some x_f >= 2"})
check("CONTROL-ONLY COROLLARY: Theorem A implies certificate 0018's "
      "theorem.  0018 emptied the X = 3 layer at m = 22 by an "
      "eight-shape structural argument; the engine here empties X = 3 "
      "at every rung of the window, m = 22 included, by an entirely "
      "different route (star-collision plus moments, no shape census "
      "at all).  Two independent proofs of the same statement -- and "
      "0018 is NOT consumed anywhere above.  The X = 3 layer at m = 22 "
      "is re-run explicitly here; the X <= 2 layers it also needs were "
      "emptied by the engine check of section 3, and that is asserted "
      "again alongside it so this corollary stands on both halves",
      s22 == 0 and survA == 0)
W_E = (0, 0, 0, 0, 0, 0)
W_F = (0, 0, 1, 1, 1, 1)
W_G = (0, 0, 1, 1, 2, 2)
WIT = [W_E, W_F, W_G]
wX = sum(lam(p, q) - 1 for p, q in itertools.combinations(WIT, 2))
check("NO TENSION WITH 0017's X = 5 CORNER WITNESS: that object has "
      "X = 5 and m = 3.  Theorem A quantifies over critical cores in "
      "[22, 456]; a 3-edge abstract corner is not one (0017 says so "
      "itself -- its tau(K-e) is 1).  X >= 5 and 'X = 5 exists at "
      "m = 3' are compatible statements about different objects",
      wX == 5 and len(WIT) == 3 and 3 < 22)
check("AND THE COUPLING IS SUPERSEDED, NOT CONTRADICTED: 0017 C5 said "
      "X <= 2 forces m <= 26.  T-A says X <= 4 is empty outright, so "
      "the hypothesis of C5 is now never satisfied by a core -- the "
      "coupling survives as a true implication with an empty "
      "antecedent.  Nothing in 0017 changes; one of its corollaries "
      "simply stops being reachable.  What is TESTED here is the "
      "antecedent's emptiness and the layer it lives in: all 3,049 "
      "cells of Theorem A ran with zero survivors, X <= 2 among them, "
      "and the X = 2 branch's R = 6 is the partition maximum section 1 "
      "exhausted",
      survA == 0 and cellsA == 3049 and RTAB[(2, 2)] == 6,
      "X <= 2 emptied by T-A: %d survivors in %d cells" % (survA, cellsA))
note("STATED, NOT TESTED: certificate 0018 remains the authority for "
     "its own theorem and its shape census; this file re-derives the "
     "STATEMENT, not 0018's structure.  Its 12,171-configuration X = 4 "
     "frontier at m = 22 is closed by Theorem A -- by counting, "
     "without ever enumerating a shape")
note("STATED, NOT TESTED -- WHAT REMAINS OPEN.  X = 5 on m in [22, 26] "
     "is NOT emptied by this certificate: T-B confines X = 5 to those "
     "five rungs and stops there.  Nothing here bears on X >= 6, on "
     "existence, or on the arithmetic-free stretch m in {23..26}, "
     "which is now the only place a critical core could hide with "
     "X = 5")

# ==========================================================================

head("Result")

print("""
  (T-A) X >= 5 FOR EVERY CRITICAL CORE, m in [22, 456]  PROVEN-BY-CERT
        (0013 covers; 0015 (2)-(3); 0017 C1 (check 8) + c12 + C3;
         0005; 0008 (D2); 0012/0013/0014 window; external NONE.
         0016 (T) via 0017 c7 and 0013's (3a) enter through C1 only)
  (T-B) X = 5 FORCES m <= 26; hence m >= 27 => X >= 6   PROVEN-BY-CERT
        (0013; 0015 (2)-(3); 0017 c9 -- the 4/3 corner, T-B's alone --
         + c12 + C3; 0005; 0012/0013/0014 window; NOT 0008 (D2),
         measured at mutants M3/M3'; external NONE)

  Two lemmas do the whole job.  A vertex z outside an edge f must send
  every one of its edges into f, and f's cell in z's own part can take
  none of them -- so d(z) beyond r-1 is paid for in collisions, and the
  collisions are excess: DELTA <= 5 + X, with no circularity.  Summed
  over all vertices, the same count says the total defect D cannot
  exceed R = sum q(q+1).  After that the problem is arithmetic: two
  moments, 36 vertices, a degree-2 cap, and eight branches of X <= 4
  plus five rungs of X = 5 -- 3,056 census runs, every one empty.

  THE MARGINS: one unit at X = 4 (twice), one unit at the (U)-difference
  (m = 24, 25, 26), and ZERO at m = 27 and 28, where D is forced to
  equal R = 14 and only divisibility kills.  (D2) is consumed by T-A at
  three measured configurations -- and NOT consumed by T-B at all.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(exit_code(FAILED))
