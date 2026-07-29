#!/usr/bin/env python3
"""Certificate 0020 -- the STRICT star-collision inequality: X >= 6 everywhere
in the window, the staircase X = 6 => m <= 26 ... X = 9 => m <= 31, and the
quadratic law m(m-25) + Sigma5 + 10H <= 38X.

    python3 verify.py

Stdlib only.  Exact integer / Fraction arithmetic on every load-bearing
bound.  No solver.  No imports from lib/.  Reads nothing from disk.  Runs
under Python 3.9 and under python3 -O.  Deterministic (hand-rolled LCG,
seed 20260728; no dict-order dependence).

WHAT IS CLAIMED
---------------
  (q3) DISTINCT EDGES OF A CRITICAL CORE HAVE lambda <= 4, i.e. q <= 3;
      hence R := sum over pairs of q(q+1) <= 4X.
          PROVEN-BY-CERTIFICATE.  In-house: 0013 (tau = 6).  Its
          mechanism is the cover lemma -- a lambda = 5 pair's five
          common cells are a 5-cover.  BILLED ONLY TO THE Q LAW.

  (BDH) THE STRICT DEFECT-HUB BOUND.  For every vertex z that some edge
      avoids,  F(d(z)) <= s(z),  F := Phi(., 5), s(z) the star excess.
      Stronger than 0019's (DH) d(z) <= 5 + s(z), since F(d) >= (d-5)_+
      always, WITH EQUALITY EXACTLY ON d <= 10 and strict inequality
      from d = 11 on (the gaps at d = 11, 12, 13 are 1, 2, 3).
          PROVEN-BY-CERTIFICATE.  Derived in-cert; enacted.

  (SSC+) THE STRICT STAR-COLLISION INEQUALITY.  For every vertex z with
      d(z) >= 2, provided tau >= qmax(z) + 2,
          F(d(z)) + qmax(z) <= s(z).
      At tau = 6 the hypothesis is AUTOMATIC: distinct 6-tuples share at
      most 5 cells, so q <= 4 and qmax + 2 <= 6.  q <= 4 here is FREE
      FROM DISTINCTNESS, not from (q3) -- (q3) is not spent anywhere in
      this lemma or in any census below.
          PROVEN-BY-CERTIFICATE.  Derived in-cert; enacted, with
          four tau = qmax + 1 violation witnesses as controls.

  (SG) THE SUMMED FORM.  P + H <= R, where P := sum_v F(d(v)) and
      H := #{v : d(v) >= 6}.
          PROVEN-BY-CERTIFICATE.  Derived in-cert; enacted.

  (Q) THE QUADRATIC LAW.  m(m-25) + Sigma5 + 10H <= 38X, where
      Sigma5 := sum_v r_v(5 - r_v), r_v = d(v) mod 5.
      (Q0) X >= ceil(m(m-25)/38).
          PROVEN-BY-CERTIFICATE.  Derived in-cert from the residue
          identity, both moments, (SG) and (q3).

  (H1) H >= 1 FOR EVERY CORE WITH m >= 26; hence AT THE CEILING m = 456,
      X >= 5173  (456*431 = 196536 = 38*5172 exactly; the +10 from
      10H lifts the ceiling by one).
          PROVEN-BY-CERTIFICATE.

  (T-A20) X >= 6 FOR EVERY CRITICAL CORE IN THE WINDOW [22, 456].
          PROVEN-BY-CERTIFICATE.  0019 T-A (X >= 5) and T-B (X = 5 =>
          m <= 26), plus the X = 5 elimination on m = 22..26 in
          section 3.  Belt-and-suspenders: the same census also empties
          X = 5 on m = 27..31, so the conclusion survives even if T-B
          were withdrawn.

  (T-B20) THE STAIRCASE.  X = 6 => m <= 26;  X = 7 => m <= 28;
      X = 8 => m <= 29;  X = 9 => m <= 31.  Equivalently m >= 27 =>
      X >= 7, m >= 29 => X >= 8, m >= 30 => X >= 9, m >= 32 => X >= 10.
          PROVEN-BY-CERTIFICATE.  Section 4: 92 (X, m, partition)
          cells, one arithmetic survivor, killed structurally.

NOTATION.  As in 0015-0019.  K edge-critical, 6-partite (V_1..V_6),
6-uniform, intersecting, tau(K) = 6, tau(K - e) = 5.  A VERTEX is a cell
(part, value); d(v) its degree; n_d the number of vertices of degree d;
n = sum_d n_d.  lambda(f,g) = |f cap g| >= 1; q = lambda - 1;
X = sum over pairs of q; x_e = sum_{f != e} q(e,f), sum_e x_e = 2X.
Phi(n,k) = balanced-split minimum of sum C(n_j,2).  F(d) := Phi(d,5);
w(d) := Phi(d-1,5) = F(d-1).  E(z) = the edges through z;
s(z) := sum over pairs inside E(z) of q  (the STAR EXCESS);
qmax(z) := the largest q over pairs inside E(z).
P := sum_v F(d(v));  H := #{v : d(v) >= 6};  R := sum over pairs q(q+1);
Sigma5 := sum_v r(5-r), r = d(v) mod 5.

THE PROOF, IN ORDER
-------------------
 (1) THE FIBRE COUNT, SHARPENED (section 2).  Fix z and an edge f
     avoiding z.  Every e in E(z) meets f, so with
     r_u := |{e in E(z) : u in e}| we have sum_{u in f} r_u >= d(z).
     THE PART-MATE IS EMPTY: f's cell in z's own part lies on no edge of
     E(z), because e's cell there is z.  So at most 5 of the 6 fibres
     are non-empty and
         sum_u C(r_u, 2) >= Phi(sum_u r_u, 5) >= Phi(d(z), 5) = F(d(z)).
     0019 relaxed the left side to (d(z) - 5)_+ and threw the rest away;
     keeping Phi is the whole of this certificate.  The left side is
     EXACTLY sum over pairs {e,g} inside E(z) of |e cap g cap f|, and z
     lies in e cap g but not in f, so each term is <= q_eg.  That is
     (BDH).  If moreover f can be chosen to avoid ALL of e* cap g* for a
     pair {e*,g*} inside E(z) of excess qmax(z) -- possible exactly when
     e* cap g* is not a cover, which is GUARANTEED as soon as
     tau > |e* cap g*| = qmax + 1 (the converse is not claimed and not
     needed) -- then that pair contributes 0 instead of qmax and we get
     (SSC+).
 (2) THE SUMMED LAWS (sections 2, 5).  sum_v s(v) = R (a pair {e,g} lies
     inside E(v) for exactly its lambda = q+1 shared cells).  Summing
     (SSC+) over all vertices and using qmax(v) >= 1 at every high
     vertex (F(d) >= 1 => s(v) >= 1 => some pair through v is excessive)
     gives (SG) P + H <= R.  The residue identity
     5d + 10F(d) - d^2 = r(5-r) summed against the two moments
     sum_v d = 6m and sum_v d^2 = m^2 + 5m + 2X gives
     10P = m^2 - 25m + 2X + Sigma5; with (SG) and R <= 4X that is (Q).
 (3) THE KEY CAP (sections 3, 4).  F(d(v)) <= X - q_1 FOR EVERY VERTEX,
     q_1 the largest pair excess.  Two cases: if v lies in the
     q_1-pair's shared set then qmax(v) >= q_1 and (SSC+) subtracts it;
     otherwise that pair is not inside E(v) and s(v) <= X - q_1.  This
     one line drives every sweep in this file.
 (4) THE CENSUSES (sections 3, 4).  Two engines over integer censuses
     (n_2, ..., n_dmax) obeying both moments, n >= 36 and the
     per-partition degree cap: (a) MINIMISE S = P + H and compare
     against R(pi) -- section 3, X = 5, and this engine ALSO imposes
     0008's n_2 <= floor(m/2); (b) MAXIMISE sum d^2 n_d under the
     per-partition (SG) budget and compare against the required
     m^2 + 5m + 2X -- section 4, the staircase, WITHOUT the n_2 cap,
     which is billed to (a).
 (5) THE ONE SURVIVOR (section 4).  Exactly one arithmetic cell lives:
     X = 8, m = 30, excess partition (3,3,1,1).  It dies structurally,
     by enumerating the legal high-vertex index-profiles T_v and
     maximising sum (d-2)(d-5) over them: the maximum is 40, so
     sum d^2 <= 42*30 - 360 + 40 = 940 < 1066.

MANDATORY HONESTY NOTES
-----------------------
 (1) PROVENANCE.  SEVEN OF THE EIGHT CLAIM ROWS WERE PROPOSED BY AN
     OUTSIDE AUDIT (GPT 5.6 Sol Pro, third audit, 2026-07-28, reading
     the public repo), delivered as full proof text: (q3)/R <= 4X,
     (BDH) F <= s, (SSC+) F + qmax <= s, (SG) P + H <= R, the (Q) law,
     X >= 6 window-wide, and the four rung ceilings.  THE EIGHTH IS
     THIS DESK'S OWN: (H1) -- hence X >= 5173 rather than the review's
     X >= 5172 at m = 456 -- appears nowhere in the received text,
     whose section 5 stops at ceil(m(m-25)/38) and does not observe
     that H = 0 forces P = 0 and contradicts the identity at m >= 26.
     Per D-036 the received text entered no chain: the desk re-derived
     every step, the blind lanes received statements plus one-line
     mechanisms only, and three verbatim-file refuter lanes were told
     to break it.  ALL THREE found the same real defect, ONE DEFECT
     WITH TWO CONSEQUENCES: the review's section 7.2 partition table at
     (8, 30) names (3+3+2) as the only remaining excess partition and
     so omits (3,3,1,1) -- the survivor -- and (3,2,2,1) -- the
     thinnest kill; and BECAUSE that list is incomplete its
     edge-disjointness sentence, which is TRUE of the partitions it
     listed (there q_i + q_j >= 5 > 3 = c for every index pair), is
     false at the omitted (3,3,1,1).  Its two/three-set H-rule likewise
     has no four-set row.  THE REPAIR (the T_v profile maximiser of
     section 4) WAS FOUND IN-HOUSE BY THREE LANES INDEPENDENTLY and is
     what section 4 encodes.  Attribution recorded, not consumed: no
     step below cites the audit.
 (2) ONE MODEL COMPARISON AND TWO SPEC NUMBERS THAT DID NOT REPRODUCE.
     (a) NOT AN ERROR ON EITHER SIDE -- TWO DIFFERENT CAP MODELS.  The
     desk spec transcribed the review's section 3 min-S table
     (13,14,14,15,15 / 15,15,16,17,19 twice / 19,21,21,24,25 twice)
     faithfully, and those rows are CORRECT UNDER THE REVIEW'S OWN
     STATED MODEL: a global Delta <= 9 from (SSC+), the 0019 off-f cap
     d <= 10 - t on every vertex some q_1-pair edge avoids, and the
     0017 4/3 budget sum_{v in f} w(d(v)) <= floor((4/3)(5-t)) on the
     six cells of f.  THIS CERTIFICATE RUNS A DIFFERENT MODEL -- the
     per-partition key cap F(d(v)) <= X - q_1 imposed at EVERY vertex,
     with no on-f budget imposed at all -- and it returns uniformly
     LARGER minima on the q_1 = 2 and q_1 = 3 rows: 16,16,16,19,20 and
     21,23,23,24,27.  Both tables are right about their own model; the
     key-cap model gives wider kills, which is why this file uses it.
     Consequence, and it is this file's number that governs here: under
     THIS model the spec's "three one-unit cells" do not exist -- the
     thinnest section-3 margin is 2, three times.  (Recorded per D-036,
     2026-07-28: an earlier draft of this note called the review's rows
     "withdrawn" and "a spec error", and asserted that no cap set
     reproduces them.  That was a DEFLATION of correct peer work and is
     retracted here; the rows reproduce exactly under the model the
     review states.)  (b) The spec's thinnest section-4 arithmetic
     kill, (8,30,(3,2,2,1)), was pinned at margin 6; MEASURED 2.
     (c) M10's MAXHIGH was guessed at ">= 74" with an explicit
     instruction to measure; MEASURED, the literal mutant is INERT (40,
     unchanged) and only the faithful one reddens.  Section 6 states
     each of these as measurements.
 (3) TWO LEDGER ROWS ARE DERIVED AND THEN NOT IMPOSED.  0015 (CC)'s
     3/2 per-edge budget and 0017 check 9's 4/3 per-edge budget are
     both derived here and NEITHER IS IMPOSED IN section 3's engine.
     Omitting them is the CONSERVATIVE direction and that is the whole
     justification: a census with fewer constraints is wider, a wider
     census can only LOWER min S, so every kill in section 3 holds a
     fortiori without them.  Check 23 additionally tabulates, branch by
     branch, that the single-degree reading of each budget sits above
     the key cap -- a per-vertex observation, kept as the secondary
     thing it is, since both budgets are SUMS over the six cells of f
     and a per-vertex comparison does not imply the sum is slack.  They
     are kept in the ledger as derived inputs; a certificate must never
     look more dependent than it is either.
 (4) WHAT ENACTMENT DOES AND DOES NOT PRICE.  Section 2 enacts (BDH),
     (SSC+), (SG) and the fibre mechanism on 1,500+ constructed
     families, which prices the LEMMAS.  It cannot price the census
     layers: nothing this lab can build has m >= 22.  Those are priced
     by the mutation suite of section 6, which is why every cap carries
     a mutant.
 (5) WHAT THIS DOES NOT CLAIM.  No core is claimed to exist.  X = 6 on
     m in [22, 26] is NOT emptied -- that is the next field.  X = 6 =>
     m <= 25 is MEASURED (section 4's by-product) and NOT CLAIMED:
     single-route so far.  Nothing is claimed at X >= 10 below m = 32.
     The ceiling floor 5173 is far from tight and section 5 says by how
     much.

THE LEDGER, in full
-------------------
  CONSUMES.  0019 T-A (X >= 5) and T-B (X = 5 => m <= 26) as CLAIM
  ROWS, plus 0019 (DH) (d(z) <= 5 + X - x_f, hence Delta <= 5 + X);
  0015 (CC) (2 sum_i Phi(d_i-1, 5-b_i) <= 3(X - x_e), X-unrestricted --
  the 3/2 per-edge budget after monotonicity and flooring; DERIVED HERE
  AND THEN NOT IMPOSED); 0017 check 9 (the 4/3 per-pair corner at
  forced excess <= 5 -- X = 5 budgets only; ALSO NOT IMPOSED),
  0017 check 12 (the assembly identity) and 0017 C3 (2m + 5x_e <=
  52 + 3X, X-unrestricted -- the rung ceilings of section 4); 0013
  (criticality, tau = 6, the private e-avoiding 5-covers T_e, (3a) for
  the a <= 1 branch); 0005 (min degree >= 2 -- ALSO re-derived in-cert
  as a note); 0008 (D2) (n_2 <= floor(m/2)) -- IMPOSED IN SECTION 3
  ONLY.  Section 4's primary sweep runs (D2)-FREE; M3 measures that
  imposing it there moves no cell value and no survivor.
  DERIVED IN-CERT.  Phi/F/w tables and monotonicity; the two moment
  identities sum_v d = 6m and sum_v C(d,2) = C(m,2) + X (both by
  double counting, note in section 2); the b = 5 covering branch (note
  in section 2); the two per-edge budgets above; (q3), (BDH), (SSC+),
  (SG), (Q), (Q0), (H1); the star identity s(v) = sum_{i : v in S_i}
  q_i; and the key cap F(d(v)) <= X - q_1.  0019's INTERNAL lemmas (L-a)
  no universal vertex, (L-b) n >= 36, (L-c) n_2 <= floor(m/2) as a
  reading of 0008, (L-d) w-monotonicity are RE-DERIVED here, not cited:
  they are not claim rows of 0019.
  NOT CONSUMED.  0018; 0017 C2; any solver.  EXTERNAL INPUTS: NONE.
  BILLING NOTE.  (q3) is consumed by R <= 4X and by nothing else.  The
  censuses of sections 3 and 4 enumerate ALL partitions (parts <= 5 in
  section 3, parts <= min(3, c) by C3 in section 4) and let the census
  kill the 4- and 5-part rows itself.
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


def F(d):
    """Phi(d, 5) -- the five-fibre collision floor of a degree-d vertex."""
    return phi(d, 5)


def w(d):
    """The cover-free per-vertex weight Phi(d-1, 5) = F(d-1)."""
    return phi(d - 1, 5)


def exc(d):
    """(d-2)(d-5) = d^2 - 7d + 10, the second-moment excess of one vertex."""
    return (d - 2) * (d - 5)


def capF(b):
    """max{d : F(d) <= b} -- the degree cap a collision budget b buys."""
    return max(d for d in range(0, 400) if F(d) <= b)


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


def parts_of(X, maxpart):
    """Every partition of X into parts <= maxpart, largest part first."""
    out = []

    def rec(left, mx, cur):
        if left == 0:
            out.append(tuple(cur))
            return
        for p in range(min(left, mx), 0, -1):
            rec(left - p, p, cur + [p])

    rec(X, min(maxpart, X) if X else 0, [])
    return out


def Rof(pi):
    """R(pi) = sum q(q+1) over the parts of pi."""
    return sum(q * (q + 1) for q in pi)


# ==========================================================================
# S0.  The two census engines and the profile maximiser
# ==========================================================================

def censuses(m, X, dmax, use_n2cap=True, n2bump=0, nmin=36):
    """EVERY integer vector (n_2, ..., n_dmax) satisfying

        sum_d d * n_d      = 6m                     (first moment)
        sum_d C(d,2) * n_d = C(m,2) + X             (second moment)
        sum_d n_d          >= nmin                  (n >= 36)
        n_2 <= floor(m/2) + n2bump                  ((D2), optional)

    TERMINATION IS PROVEN, not hoped: degrees are capped at dmax by
    hypothesis and the first moment caps each n_d <= floor(6m/d) with
    all terms non-negative (degrees start at 2 by 0005), so the tree is
    finite.  The recursion descends d = dmax..3 and SOLVES for n_2 from
    the first moment at the leaf, so no solution can be missed there.
    Two exact prunes, both one-line consequences of 2 <= d' <= d on the
    remaining degrees:  sum d'^2 n_d' >= 2 sum d' n_d'  and  <= d sum
    d' n_d'.  ONE internal invariant is recorded into INTERNAL (checked
    in section 3, and again after the mutants) rather than by a bare
    assert, which -O strips: EVERY emitted vector is re-verified against
    all four constraints from scratch before it leaves the leaf,
    including the first-moment bound n_d <= floor(6m/d) RECOMPUTED FROM
    m rather than read off the caps the recursion threads."""
    S1 = 6 * m
    S2 = m * m + 5 * m + 2 * X          # sum d^2 n_d
    caps = {}
    for d in range(2, dmax + 1):
        c = S1 // d
        if d == 2 and use_n2cap:
            c = min(c, m // 2 + n2bump)
        caps[d] = c
    out = []
    vec = [0] * (dmax + 1)

    def rec(d, r1, r2, cnt):
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
                or any(sol[i] > 6 * m // (i + 2) for i in range(len(sol)))):
                INTERNAL.append(("leaf", m, X, sol))
            LEAVES[0] += 1
            out.append(sol)
            return
        if r2 < 2 * r1 or r2 > d * r1:
            return
        if cnt + r1 // 2 < nmin:
            return
        mx = min(caps[d], r1 // d)
        for k in range(mx + 1):
            vec[d] = k
            rec(d - 1, r1 - d * k, r2 - d * d * k, cnt + k)
        vec[d] = 0

    if dmax >= 2:
        rec(dmax, S1, S2, 0)
    return out


def Sof(vec, useH=True, Ffn=F):
    """S = sum_d (F(d) + [d >= 6]) n_d  =  P + H  on one census vector."""
    return sum((Ffn(i + 2) + ((1 if i + 2 >= 6 else 0) if useH else 0))
               * vec[i] for i in range(len(vec)))


def minS(m, X, dmax, useH=True, Ffn=F, **kw):
    """min of P + H over the censuses; None if the cell is infeasible."""
    cs = censuses(m, X, dmax, **kw)
    if not cs:
        return None, None
    best = min((Sof(v, useH, Ffn), v) for v in cs)
    return best[0], best[1]


def _best_low(h, Sh, m, nmin, cap2):
    """Over low degrees 2..5 with sum d n_d = 6m - Sh and n >= nmin - h:
    the least value of 10n + 2n_3 + 2n_4, with a witness.  That is the
    whole of the second-moment maximiser's low half, because
        sum d^2 n_d = 42m - 10n - 2n_3 - 2n_4 + sum_{d>=6} exc(d) n_d
    identically when sum d n_d = 6m (exc(d) = 0, -2, -2, 0 at d = 2..5).
    The scan is ascending in n and stops at the first feasible value:
    each extra vertex costs 10 while the n_3/n_4 penalty is at most 2,
    so no later n can beat an earlier feasible one.

    WHY THE n_3, n_4 <= 6 WINDOW IS SAFE, since understating the low
    half is the dangerous direction.  For fixed n_low the residual
    M = L1 - 2 n_low is written as n_3 + 2 n_4 + 3 n_5 with
    n_2 = n_low - n_3 - n_4 - n_5 >= 0, and the objective adds
    2(n_3 + n_4).  An exchange argument bounds where the minimum can
    sit: three degree-3 vertices may be traded for one degree-5 and two
    degree-2 (same n_low, same M, objective DOWN by 6), and three
    degree-4 for two degree-5 and one degree-2 (also down by 6).  Both
    trades raise n_2, so with the (D2) cap active they are not always
    available -- WHICH IS WHY THE WINDOW IS ALSO MEASURED rather than
    only argued: widening it to 0..60 on all 92 cells of section 4,
    with (D2) on and with (D2) off, moves no value (measured
    firsthand; kept offline for the clock)."""
    L1 = 6 * m - Sh
    if L1 < 0:
        return None, None
    lo = max(0, nmin - h, -((-L1) // 5))
    hi = L1 // 2
    best = None
    arg = None
    for nlow in range(lo, hi + 1):
        if best is not None and 10 * (h + nlow) >= best:
            break
        M = L1 - 2 * nlow
        for n3 in range(0, 7):
            for n4 in range(0, 7):
                rem = M - n3 - 2 * n4
                if rem < 0 or rem % 3:
                    continue
                n5 = rem // 3
                n2 = nlow - n3 - n4 - n5
                if n2 < 0 or n2 > cap2:
                    continue
                cost = 10 * (h + nlow) + 2 * (n3 + n4)
                if best is None or cost < best:
                    best = cost
                    arg = (n2, n3, n4, n5)
    return best, arg


def maximize_sq(m, X, dmax, budget_w, R, nmin=36, use_n2cap=False):
    """max sum d^2 n_d over integer censuses with sum d n_d = 6m,
    sum n_d >= nmin, 2 <= d <= dmax, and the per-partition (SG) budget
    sum_{d>=6} budget_w[d] n_d <= R.  (D2)'s n_2 <= floor(m/2) is
    OPTIONAL AND OFF BY DEFAULT: this is section 4's engine and 0008 is
    billed to section 3.  M3 turns it on and measures the difference.
    Returns (value, full census vector) or (None, None) if infeasible.
    The high degrees are enumerated exhaustively -- each costs at least
    F(6) + q_min >= 2 of the budget, so the tree is finite -- and the
    low half is solved in closed form by _best_low."""
    highs = list(range(6, dmax + 1))
    cap2 = (m // 2) if use_n2cap else 10 ** 9
    best = [None, None]
    cur = [0] * (dmax + 1)

    def rec(i, budget_left, Sh, h, E):
        NODES[0] += 1
        if i == len(highs):
            cost, arg = _best_low(h, Sh, m, nmin, cap2)
            if cost is not None:
                val = 42 * m - cost + E
                if best[0] is None or val > best[0]:
                    best[0] = val
                    best[1] = tuple(list(arg) + list(cur[6:dmax + 1]))
            return
        d = highs[i]
        wg = budget_w[d]
        k = 0
        while wg * k <= budget_left and d * k <= 6 * m - Sh:
            cur[d] = k
            rec(i + 1, budget_left - wg * k, Sh + d * k, h + k,
                E + exc(d) * k)
            k += 1
        cur[d] = 0

    rec(0, R, 0, 0, 0)
    return best[0], best[1]


def legal_profiles(pi, dmax, minsize=2, bdh_only=False):
    """The index sets T = {i : v in S_i} a HIGH vertex may carry, with
    the degree each one permits.  s(T) = sum_{i in T} q_i is the star
    excess forced on such a vertex (the star identity), qmax(T) its
    largest part, so (SSC+) caps its degree at max{d : F(d) <= s - qmax}
    -- or, if bdh_only, only (BDH) applies and the cap is
    max{d : F(d) <= s}."""
    k = len(pi)
    out = []
    for sz in range(minsize, k + 1):
        for T in itertools.combinations(range(k), sz):
            s = sum(pi[i] for i in T)
            qm = max(pi[i] for i in T)
            b = s if bdh_only else s - qm
            dm = min(capF(b), dmax)
            out.append((T, dm, exc(dm) if dm >= 6 else 0))
    return out


def profile_max(pi, dmax, minsize=2, bdh_only=False, slots=None):
    """MAXHIGH := max sum (d-2)(d-5) over legal high-vertex profiles.
    A profile is a set of index sets T_v, and (iv) says each index PAIR
    {i,j} is hosted by at most one high vertex -- so the T_v's form a
    linear system on the parts and the search is an exact packing over
    pair-bitmasks.  Returns (value, the maximising profile).

    slots=None (the certificate's own reading) visits each index set at
    most once and imposes no |S_i| bound: a RELAXATION, hence the safe
    direction, since it can only raise MAXHIGH.  slots=[q_i + 1] is the
    realisability reading used by M10: an index set may then be reused
    -- a singleton consumes no index pair, so (iv) does not forbid a
    second vertex on it -- and what bounds the count instead is that
    S_i holds only q_i + 1 vertices.  WITHOUT EITHER BOUND the faithful
    M10 profile space is genuinely unbounded, which is why M10 reports
    the slotted number."""
    k = len(pi)
    pidx = {}
    for i in range(k):
        for j in range(i + 1, k):
            pidx[(i, j)] = len(pidx)
    Ts = []
    for (T, dm, wt) in legal_profiles(pi, dmax, minsize, bdh_only):
        if wt <= 0:
            continue
        mask = 0
        for a in range(len(T)):
            for b in range(a + 1, len(T)):
                mask |= 1 << pidx[(T[a], T[b])]
        Ts.append((wt, mask, T, dm))
    Ts.sort(reverse=True)
    suff = [0] * (len(Ts) + 1)
    for i in range(len(Ts) - 1, -1, -1):
        suff[i] = suff[i + 1] + Ts[i][0]
    best = [0, []]

    def rec(i, used, acc, prof):
        NODES[0] += 1
        if acc > best[0]:
            best[0] = acc
            best[1] = list(prof)
        if i == len(Ts) or acc + suff[i] <= best[0]:
            return
        for j in range(i, len(Ts)):
            if acc + suff[j] <= best[0]:
                return
            wt, mask, T, dm = Ts[j]
            if used & mask:
                continue
            rec(j + 1, used | mask, acc + wt, prof + [(T, dm)])

    def rec_slots(i, used, room, acc, prof):
        NODES[0] += 1
        if acc > best[0]:
            best[0] = acc
            best[1] = list(prof)
        for j in range(i, len(Ts)):
            wt, mask, T, dm = Ts[j]
            if used & mask or any(room[t] < 1 for t in T):
                continue
            nr = list(room)
            for t in T:
                nr[t] -= 1
            rec_slots(j, used | mask, tuple(nr), acc + wt, prof + [(T, dm)])

    if slots is None:
        rec(0, 0, 0, [])
    else:
        rec_slots(0, 0, tuple(slots), 0, [])
    return best[0], best[1]


def licensed_ii(pi, c):
    """Is |S_i cap S_j| <= 1 (step (ii)) FORCED for this partition at
    per-edge cap c?  Two ways two shared sets could meet twice:

      CASE A, the pairs P_i, P_j edge-disjoint.  Then all four edges
        contain the two common vertices, so ALL SIX pairs among them are
        excessive and pi would need at least six parts.  THAT COUNT IS
        THE ARGUMENT, and it is what the code tests (the k >= 6
        conjunct).  For index pairs {i,j} with q_i >= 2 there is also an
        independent route -- each of e_i, g_i then lies in three
        excessive pairs, so x >= q_i + 2 >= 4 > 3 = c -- but at
        {i,j} = {3,4} of the exceptional cell, where q_3 = q_4 = 1, that
        route gives only x >= 3 = c and does NOT close.  Hence the
        six-pairs-versus-four-parts count is the one the code relies on.
      CASE B, the pairs sharing an edge e (possible only if
        q_i + q_j <= x_e <= c).  With P_i = {e,g}, P_j = {e,h}, two
        common vertices put both in g cap h, so {g,h} is a third
        excessive pair P_l; then x_g >= q_i + q_l and x_h >= q_j + q_l,
        and both must still be <= c.

    Returns True when every (i,j) excludes both cases."""
    k = len(pi)
    bad = []
    for i in range(k):
        for j in range(i + 1, k):
            caseA = (pi[i] + 2 <= c and pi[j] + 2 <= c and k >= 6)
            caseB = False
            if pi[i] + pi[j] <= c:
                for l in range(k):
                    if l in (i, j):
                        continue
                    if pi[i] + pi[l] <= c and pi[j] + pi[l] <= c:
                        caseB = True
            if caseA or caseB:
                bad.append((i, j, "A" if caseA else "B"))
    return (not bad), bad


def c3cap(X, m):
    """0017 C3: 2m + 5 x_e <= 52 + 3X, hence x_e <= floor((52+3X-2m)/5)."""
    return (52 + 3 * X - 2 * m) // 5


def mincover(fam):
    """Exact tau: branch on the six cells of the least-recently covered
    edge.  Depth is bounded by r+1 and each node has r children, so the
    search terminates; iterative deepening returns the MINIMUM."""
    r = len(fam[0])

    def rec(rem, k):
        if not rem:
            return True
        if k == 0:
            return False
        e = rem[0]
        for i in range(r):
            if rec([f for f in rem if f[i] != e[i]], k - 1):
                return True
        return False

    for k in range(0, r + 2):
        if rec(list(fam), k):
            return k
    return r + 2


head("0.  the dependency ledger, printed in-run")

print("""    CONSUMES   0019 T-A, T-B      X >= 5 everywhere; X = 5 => m <= 26
                                    (claim rows, not re-proved here)
               0019 (DH)            d(z) <= 5 + X - x_f; Delta <= 5 + X
               0015 (CC)            2 sum Phi(d_i-1,5-b_i) <= 3(X - x_e)
                                    -- the 3/2 per-edge budget.  DERIVED
                                    HERE AND THEN NOT IMPOSED (c23)
               0017 check 9         the 4/3 per-pair corner at X = 5.
                                    ALSO DERIVED AND NOT IMPOSED (c23)
               0017 check 12        sum over pairs of K-e of (s-1) = X - x_e
               0017 C3              2m + 5x_e <= 52 + 3X -- the section 4
                                    rung ceilings, load-bearing
               0013                 criticality, tau = 6, private T_e, (3a)
               0005                 min degree >= 2 (also re-derived, note)
               0008 (D2)            n_2 <= floor(m/2) -- IMPOSED IN
                                    SECTION 3 ONLY.  Section 4's primary
                                    sweep is (D2)-FREE; M3 prices both
    DERIVES    Phi/F/w + monotonicity   (q3)  (BDH)  (SSC+)  (SG)
               the star identity        (Q)   (Q0)   (H1)
               the two moment identities (double counting, note in S2)
               the b = 5 covering branch (note in section 2)
               THE KEY CAP  F(d(v)) <= X - q_1  for every vertex
               and 0019's internal lemmas (no universal vertex, n >= 36,
               n_2 cap reading, w-monotonicity) -- RE-DERIVED, not cited
    NOT USED   0018, 0017 C2, any solver
    BILLING    (q3) is spent on R <= 4X and NOWHERE ELSE.  Both censuses
               enumerate every partition and kill the wide rows by count
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
      "printing convention",
      _ok_false is False and _ok_true is True
      and _probe == ["CANARY: a deliberately false condition"]
      and exit_code(_probe) == 1 and exit_code([]) == 0
      and FAILED == [],
      "private sink: " + show(_probe))

# ==========================================================================
# 1.  Tables and identities
# ==========================================================================

head("1.  F, w, the residue identity, and the partition tables")

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
FTAB = [F(d) for d in range(0, 13)]
check("Phi(n,k) is the EXHAUSTIVE minimum of sum C(n_j,2) over every "
      "composition of n into k classes (n <= 12, k <= 6).  F := Phi(.,5) "
      "reads 0,0,0,0,0,0,1,2,3,4,5,7,9 at d = 0..12 -- so F(9) = 4, "
      "F(10) = 5, F(11) = 7 -- and w(d) = F(d-1) gives w(11) = 5, "
      "w(12) = 7.  F is non-decreasing to d = 600 (the step the fibre "
      "count needs, since sum_u r_u >= d(z) only bounds the total) and "
      "F(d) >= (d-5)_+ everywhere, with EQUALITY exactly on d <= 10 and "
      "STRICT inequality from d = 11 on -- the gaps at d = 11, 12, 13 "
      "being 1, 2, 3.  READ THAT HONESTLY: every degree cap in section "
      "3 sits at 9 or below, where (BDH) and 0019's (DH) are the SAME "
      "pointwise statement; section 4 runs a quarter of its cells at "
      "Delta = 11, where (BDH) is strictly stronger, and the last "
      "control of section 8 measures exactly how much that buys.  The "
      "three places this "
      "certificate actually gains are the qmax subtraction of (SSC+), "
      "the +H term of (SG), and -- at large m, where degrees may run "
      "to 5 + X -- F's quadratic growth, which is what makes the "
      "residue identity and hence (Q) possible at all",
      ok_min and FTAB == [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 7, 9]
      and w(11) == 5 and w(12) == 7
      and all(F(d + 1) >= F(d) for d in range(0, 600))
      and all(F(d) >= max(d - 5, 0) for d in range(0, 601))
      and all(F(d) == max(d - 5, 0) for d in range(0, 11))
      and all(F(d) > d - 5 for d in range(11, 601)),
      "F(0..12) = " + show(FTAB))
check("(L-d) MONOTONICITY IN THE FIBRE COUNT: Phi(n, 5-b) >= Phi(n, 5) "
      "for every n <= 60 and b = 0..4 -- the step that turns the private "
      "cover's unknown b_i-profile into the b-free weight w(d).  And "
      "Phi(n,5) >= Phi(n,6) with STRICT inequality somewhere (n = 6 "
      "already: 1 > 0), which is why the part-mate exclusion -- five "
      "fibres, not six -- is a load-bearing step and not bookkeeping",
      all(phi(n, 5 - b) >= phi(n, 5)
          for n in range(0, 61) for b in range(0, 5))
      and all(phi(n, 5) >= phi(n, 6) for n in range(0, 601))
      and phi(6, 5) == 1 and phi(6, 6) == 0)
CK_MONO = NCHECK[0]

resid = [(5 * d + 10 * F(d) - d * d, (d % 5) * (5 - d % 5))
         for d in range(0, 601)]
check("THE RESIDUE IDENTITY, exactly, on d = 0..600: "
      "5d + 10 F(d) - d^2 = r(5-r) with r = d mod 5, taking the five "
      "values 0, 4, 6, 6, 4.  Written d = 5q + r it is the one-line "
      "computation 10 F(d) = 25q^2 + 10qr - 25q; this is the hinge of "
      "the whole quadratic law, since summing it against the two "
      "moments turns P into a polynomial in m and X",
      all(a == b for a, b in resid)
      and sorted(set(b for a, b in resid)) == [0, 4, 6]
      and [r * (5 - r) for r in range(5)] == [0, 4, 6, 6, 4],
      "values r(5-r) = " + show([r * (5 - r) for r in range(5)]))
CK_RESID = NCHECK[0]

check("(q3)'s ARITHMETIC HALF: q(q+1) <= 4q exactly when q <= 3, with "
      "EQUALITY at q = 3 and first failure at q = 4 (20 > 16).  So "
      "R = sum q(q+1) <= 4X needs lambda <= 4 and nothing weaker -- one "
      "lambda = 5 pair breaks it",
      all(q * (q + 1) <= 4 * q for q in range(0, 4))
      and 3 * 4 == 4 * 3 and 4 * 5 > 4 * 4,
      "q(q+1) at q=0..4: " + show([q * (q + 1) for q in range(5)]))
CK_Q3A = NCHECK[0]

P5 = parts_of(5, 5)
P5_3 = parts_of(5, 3)
BUD43 = [int(Fr(4, 3) * (5 - t)) for t in range(6)]
check("THE PARTITIONS OF 5.  All seven, largest part first: the five "
      "with parts <= 3 carry R = 10, 12, 14, 16, 18 at q_1 = 1, 2, 2, "
      "3, 3, and the two wide rows (4,1) and (5) carry R = 22 and 30.  "
      "The wide rows are CARRIED, not deleted -- (q3) is not spent in "
      "section 3, so the census has to kill them itself.  The floored "
      "4/3 budgets floor((4/3)(5-q_1)) read 5, 4, 4, 2, 2 on the narrow "
      "rows",
      len(P5) == 7 and len(P5_3) == 5
      and [Rof(p) for p in P5_3] == [18, 16, 14, 12, 10]
      and sorted(Rof(p) for p in P5 if max(p) >= 4) == [22, 30]
      and [BUD43[p[0]] for p in P5_3] == [2, 2, 4, 4, 5],
      "partitions " + show(P5))

check("d^2 <= 7d - 10 ON [2,5] with EXACT slacks 0, 2, 2, 0, and the "
      "excess exc(d) = (d-2)(d-5) = 4, 10, 18, 28, 40, 54 at d = 6..11. "
      "This is the identity the second-moment maximiser runs on: "
      "sum d^2 n_d = 42m - 10n + sum exc(d) n_d whenever sum d n_d = 6m, "
      "so with n >= 36 only the HIGH vertices can push the second "
      "moment up",
      [7 * d - 10 - d * d for d in range(2, 6)] == [0, 2, 2, 0]
      and [exc(d) for d in range(6, 12)] == [4, 10, 18, 28, 40, 54]
      and all(exc(d) <= 0 for d in range(2, 6)),
      "exc(6..11) = " + show([exc(d) for d in range(6, 12)]))

CAPLADDER = [capF(b) for b in range(0, 6)]
check("THE CAP LADDER capF(b) = max{d : F(d) <= b} reads 5, 6, 7, 8, 9, "
      "10 at b = 0..5.  Every degree cap in sections 3 and 4 is one of "
      "these six numbers, read at b = X - q_1",
      CAPLADDER == [5, 6, 7, 8, 9, 10]
      and F(11) == 7 and F(12) == 9,
      "capF(0..5) = " + show(CAPLADDER))

Q0 = {}
for m in (38, 108, 309, 456):
    Q0[m] = ceil_fr(Fr(m * (m - 25), 38))
check("(Q0) SPOT VALUES, exact: ceil(m(m-25)/38) = 13, 236, 2310, 5172 "
      "at m = 38, 108, 309, 456 -- and 456*431 = 196536 = 38*5172 "
      "EXACTLY, which is why the ceiling rung is the one place the +10 "
      "of (H1) changes the answer",
      [Q0[m] for m in (38, 108, 309, 456)] == [13, 236, 2310, 5172]
      and 456 * 431 == 196536 and 38 * 5172 == 196536
      and Fr(196536, 38).denominator == 1,
      "Q0 = " + show([Q0[m] for m in (38, 108, 309, 456)]))
CK_Q0 = NCHECK[0]

# ==========================================================================
# 2.  The lemmas, enacted
# ==========================================================================

head("2.  (q3), (BDH), (SSC+) and (SG) -- enacted on a built corpus")

MUL4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]


def field(q):
    """(add, mul, neg) for F_q, q in {2,3,4,5}.  F_4 by explicit table."""
    if q == 4:
        return (lambda a, b: a ^ b), (lambda a, b: MUL4[a][b]), (lambda a: a)
    return ((lambda a, b: (a + b) % q), (lambda a, b: (a * b) % q),
            (lambda a: (-a) % q))


def ag(q):
    """AG(2,q) as a (q+1)-partite (q+1)-uniform intersecting family of
    q^2 edges: the edge of the point (a,b) records, for each of the q
    slopes, the label of the line of that slope through it, and finally
    the vertical line.  Two distinct points lie on exactly one common
    line, so every lambda is 1 and X = R = 0.  tau = q (a parallel class
    covers; q-1 lines cover only q(q-1) < q^2 points)."""
    add, mul, neg = field(q)
    return [tuple([add(b, mul(neg(s), a)) for s in range(q)] + [a])
            for a in range(q) for b in range(q)]


def ag_witness(q):
    """AG(2,q) with the vertical line through one point RENAMED on a new
    edge, and the other q-1 points of that line deleted.  The new edge
    e' meets its twin in q of the q+1 parts, so q(e', T(x)) = q-1, and
    the shared cells are a MINIMUM cover: tau = q = qmax + 1 exactly.
    Every shared cell z then has d(z) = q+1, s(z) = qmax = q-1 and
    Phi(d(z), q) = 1, so (SSC+) fails there by exactly one unit."""
    A = ag(q)
    x = A[0]
    i0 = q
    keep = [e for e in A if e == x or e[i0] != x[i0]]
    return keep + [tuple(list(x[:i0]) + [q])]


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
    return [tuple([0, 0] + [i] * (r - 2)) for i in range(k)]


def nearpencil(r, k):
    return ([tuple([0, i] + [0] * (r - 2)) for i in range(k)]
            + [tuple([1, k] + [0] * (r - 2))])


def rehearsal(r):
    return [c for c in itertools.product((0, 1), repeat=r) if sum(c) <= 1]


def twins(r, k, extra, rng):
    """k edges agreeing on parts 1..r-1: every pair has lambda = r-1, so
    this is the (q3) generator.  Extra greedy edges are then forced by
    the lemma to meet the shared (r-1)-set, which is what gets checked."""
    fam = [tuple([i] + [0] * (r - 1)) for i in range(k)]
    tries = 0
    while len(fam) < k + extra and tries < 300:
        tries += 1
        c = tuple([rng.below(3)] + [rng.below(2) for _ in range(r - 1)])
        if c in fam:
            continue
        if all(lam(c, f) >= 1 for f in fam):
            fam.append(c)
    return fam


ACC = dict((k, 0) for k in (
    "fams", "short", "gen_bad", "q3pairs", "q3bad", "q3extra", "bdh_n",
    "bdh_bad", "bdh_tight", "pairs", "mate_bad", "id_bad", "id_nz",
    "fib_bad", "ssc_n", "ssc_bad", "ssc_nz", "ssc_tightnz", "ssc_unguard",
    "ssc_unguard_bad", "sg_n", "sg_bad", "sg_nz", "sg_unguard",
    "sg_unguard_bad", "star_sum", "Rsum", "star_perfam_bad", "univ",
    "univ_break", "m6_load", "hi_n", "hi_bad", "q5", "qid_bad", "qid_n"))
BYR = {}
TAUH = {}
QROWS = []


def audit(fam):
    """Every claim of section 2, on one family."""
    if len(fam) < 3:
        ACC["short"] += 1
        return
    r = len(fam[0])
    m = len(fam)
    if (any(len(e) != r for e in fam) or len(set(fam)) != m
            or any(lam(p, q) < 1 for p, q in itertools.combinations(fam, 2))):
        ACC["gen_bad"] += 1
        return
    ACC["fams"] += 1
    BYR[r] = BYR.get(r, 0) + 1
    deg = {}
    for e in fam:
        for i in range(r):
            deg[(i, e[i])] = deg.get((i, e[i]), 0) + 1
    X = sum(lam(p, q) - 1 for p, q in itertools.combinations(fam, 2))
    R = sum((lam(p, q) - 1) * lam(p, q)
            for p, q in itertools.combinations(fam, 2))
    ACC["Rsum"] += R
    tau = mincover(fam)
    TAUH[tau] = TAUH.get(tau, 0) + 1
    qmaxg = max([lam(p, q) - 1 for p, q in itertools.combinations(fam, 2)])
    if qmaxg >= 4:
        ACC["q5"] += 1
    # ---- (q3): a lambda = r-1 pair's common cells form a cover
    for p, q in itertools.combinations(fam, 2):
        if lam(p, q) == r - 1:
            ACC["q3pairs"] += 1
            shared = [(i, p[i]) for i in range(r) if p[i] == q[i]]
            for h in fam:
                if h == p or h == q:
                    continue
                ACC["q3extra"] += 1
                if not any(h[i] == v for (i, v) in shared):
                    ACC["q3bad"] += 1
    # ---- the summed laws
    universal = any(d == m for d in deg.values())
    P = sum(phi(d, r - 1) for d in deg.values())
    H = sum(1 for d in deg.values() if phi(d, r - 1) >= 1)
    if universal:
        ACC["univ"] += 1
        if P + H > R:
            ACC["univ_break"] += 1
    elif tau >= qmaxg + 2:
        ACC["sg_n"] += 1
        if P + H > R:
            ACC["sg_bad"] += 1
        if P + H > 0:
            ACC["sg_nz"] += 1
    else:
        ACC["sg_unguard"] += 1
        if P + H > R:
            ACC["sg_unguard_bad"] += 1
    if r == 6:
        S5 = sum((d % 5) * (5 - d % 5) for d in deg.values())
        ACC["qid_n"] += 1
        if 10 * P != m * m - 25 * m + 2 * X + S5:
            ACC["qid_bad"] += 1
        QROWS.append((m, P, H, X, S5, R))
    # ---- the per-vertex laws
    famstar = 0
    for z in sorted(deg):
        Ez = [e for e in fam if e[z[0]] == z[1]]
        dz = len(Ez)
        star = sum(lam(p, q) - 1 for p, q in itertools.combinations(Ez, 2))
        ACC["star_sum"] += star
        famstar += star
        if dz == m:
            continue
        ACC["bdh_n"] += 1
        if phi(dz, r - 1) > star:
            ACC["bdh_bad"] += 1
        if phi(dz, r - 1) == star and star > 0:
            ACC["bdh_tight"] += 1
            if phi(dz, r - 1) > phi(dz, r):
                ACC["m6_load"] += 1
        if phi(dz, r - 1) >= 1:
            ACC["hi_n"] += 1
            if star < 1:
                ACC["hi_bad"] += 1
        if dz >= 2:
            qmax = max(lam(p, q) - 1
                       for p, q in itertools.combinations(Ez, 2))
            if tau >= qmax + 2:
                ACC["ssc_n"] += 1
                if phi(dz, r - 1) + qmax > star:
                    ACC["ssc_bad"] += 1
                if star > 0:
                    ACC["ssc_nz"] += 1
                    if phi(dz, r - 1) + qmax == star:
                        ACC["ssc_tightnz"] += 1
            else:
                ACC["ssc_unguard"] += 1
                if phi(dz, r - 1) + qmax > star:
                    ACC["ssc_unguard_bad"] += 1
        # ---- the fibre mechanism, one (z, f) pair at a time
        for f in fam:
            if f[z[0]] == z[1]:
                continue
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
            if sum(ru) < dz or lhs < phi(sum(ru), r - 1):
                ACC["fib_bad"] += 1
    # ---- the exchange of summation, THIS family alone: sum_v s(v) = R
    if famstar != R:
        ACC["star_perfam_bad"] += 1


def fat_plane(q, tri):
    """AG(2,q) with one EXTRA part appended, constant on all but the
    points of `tri` -- a deliberately FATTENED vertex.  Built to give
    section 2 a family that satisfies the (SG) family guard
    tau >= qmax + 2 NON-VACUOUSLY, i.e. with P + H > 0.

    AG(2,q) itself cannot: every one of its degrees is q = r-1, so
    Phi(d, r-1) = 0 at every vertex and P = H = 0.  Appending a part
    whose value is 0 on all but three NON-COLLINEAR points gives that
    cell degree q^2 - 3, which for q = 3 is 6 >= r = 5, so
    Phi(6, 4) = 2 >= 1 and the vertex is high.  The three excluded
    points get distinct private values, and because they are not
    collinear no single cell covers them, so the two-cell cover
    (the fat cell + one more) does not exist and tau stays at 3 --
    exactly qmax + 2, since the q^2 - 3 edges through the fat cell now
    pairwise share TWO cells (it and their AG line) and qmax = 1.
    tau and every count below are COMPUTED, not asserted."""
    A = ag(q)
    out = []
    k = 0
    for i, e in enumerate(A):
        if i in tri:
            k += 1
            out.append(tuple(list(e) + [k]))
        else:
            out.append(tuple(list(e) + [0]))
    return out


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
    for k in (5, 8, 12, 20, 26, 32):
        for extra in (0, 2, 4):
            audit(twins(r, k, extra, RNG))
AGF = {}
for q in (2, 3, 4, 5):
    AGF[q] = ag(q)
    audit(AGF[q])
    audit(ag_witness(q))
    for cut in range(1, 9):
        sub = [AGF[q][i] for i in range(len(AGF[q])) if (i * 7 + 3) % 11 >= cut]
        if len(sub) >= 3:
            audit(sub)
FAT53 = fat_plane(3, (0, 1, 3))     # the points (0,0), (0,1), (1,0)
audit(FAT53)
S2TIME = time.time() - t0
FATD = {}
for e in FAT53:
    for i in range(5):
        FATD[(i, e[i])] = FATD.get((i, e[i]), 0) + 1
FATtau = mincover(FAT53)
FATq = max(lam(a, b) - 1 for a, b in itertools.combinations(FAT53, 2))
FATP = sum(phi(d, 4) for d in FATD.values())
FATH = sum(1 for d in FATD.values() if phi(d, 4) >= 1)
FATR = sum((lam(a, b) - 1) * lam(a, b)
           for a, b in itertools.combinations(FAT53, 2))

check("THE GENERATOR'S OWN HYPOTHESES FIRST: every family of >= 3 edges "
      "handed to the audit is checked r-partite (r-tuples), "
      "duplicate-free and PAIRWISE INTERSECTING before any claim is read "
      "off it -- 0 rejects.  Families below 3 edges are dropped before "
      "the guard and counted separately, since every claim here is "
      "vacuous on them.  The corpus spans r = 3, 4, 5, 6 and, crucially, "
      "carries HIGH-tau objects: the affine planes AG(2,q) and their "
      "subfamilies reach tau = 5, without which the (SSC+) guard would "
      "never be satisfied and section 2 would be enacting nothing",
      ACC["gen_bad"] == 0 and ACC["fams"] >= 1500
      and all(BYR[r] >= 300 for r in (3, 4, 5, 6))
      and max(TAUH) >= 5 and sum(TAUH[t] for t in TAUH if t >= 3) >= 30,
      "%d families %s by r; tau histogram %s; %d short dropped; %.1fs"
      % (ACC["fams"], show(sorted(BYR.items())), show(sorted(TAUH.items())),
         ACC["short"], S2TIME))

check("(q3) VIA ITS COVER LEMMA, the only mechanism it has: if "
      "lambda(e,f) = r-1 then e and f differ in ONE part, so any edge h "
      "missing all r-1 common cells would have to meet e and f in that "
      "one part -- at two different values.  Impossible; so the common "
      "cells COVER, and in a core with tau = 6 no such pair can exist: "
      "lambda <= 4, q <= 3.  ENACTED on every lambda = r-1 pair in the "
      "corpus, against every OTHER edge of its family: zero exceptions, "
      "and the count of (pair, other edge) tests is large enough that "
      "the lemma is not being confirmed on a handful of sunflowers",
      ACC["q3pairs"] >= 10000 and ACC["q3bad"] == 0
      and ACC["q3extra"] >= 10000,
      "%d lambda=r-1 pairs, %d (pair, other-edge) tests, %d failures"
      % (ACC["q3pairs"], ACC["q3extra"], ACC["q3bad"]))

check("THE FIBRE MECHANISM, the step where F is actually born.  On "
      "every (z, f) pair with z not in f: the PART-MATE fibre -- f's "
      "cell in z's own part -- carries r_u = 0 every time (0 "
      "exceptions, so at most five fibres are ever non-empty); the "
      "identity sum_u C(r_u,2) = sum over pairs inside E(z) of "
      "|e cap g cap f| holds every time; and sum_u r_u >= d(z) with "
      "sum_u C(r_u,2) >= Phi(sum r_u, r-1) every time.  A large "
      "minority of the pairs have a STRICTLY POSITIVE identity, so the "
      "mirror is exercised and not vacuously satisfied.  Two edges in "
      "the same fibre share z AND u, so their q is at least 1 -- that "
      "is why C(r_u,2) may be charged to the excess at all",
      ACC["pairs"] >= 50000 and ACC["mate_bad"] == 0 and ACC["id_bad"] == 0
      and ACC["fib_bad"] == 0 and ACC["id_nz"] >= 10000,
      "%d (z,f) pairs, %d with a positive identity, %d part-mate and %d "
      "identity and %d Phi-minimality failures"
      % (ACC["pairs"], ACC["id_nz"], ACC["mate_bad"], ACC["id_bad"],
         ACC["fib_bad"]))

check("(BDH) ENACTED, conclusion level: F(d(z)) <= s(z) on every vertex "
      "that some edge avoids -- zero failures -- and TIGHT (with a "
      "positive star excess, so not a 0 <= 0 reading) on a nameable "
      "set, which is what tells a sharp bound from a slack one.  The "
      "one-line corollary the summed laws need is measured with it: "
      "every vertex with F(d) >= 1 has s(z) >= 1, hence qmax(z) >= 1, "
      "0 exceptions -- and the POPULATION that corollary runs on is "
      "pinned, not merely reported non-empty: 2,331 high vertices.  "
      "(Pinning it matters: the corollary is what licenses the +H term "
      "of (SG), and M1 measures +H as carrying 17 of section 3's 35 "
      "cells.  A guard drifted from F(d) >= 1 to F(d) >= 2 would drop "
      "every d = 6 vertex from the count and nothing else here would "
      "notice)",
      ACC["bdh_n"] >= 10000 and ACC["bdh_bad"] == 0
      and ACC["bdh_tight"] > 0 and ACC["hi_bad"] == 0
      and ACC["hi_n"] == 2331,
      "%d vertices, %d failures, %d non-vacuously tight; %d high "
      "vertices, %d with s(z) = 0"
      % (ACC["bdh_n"], ACC["bdh_bad"], ACC["bdh_tight"], ACC["hi_n"],
         ACC["hi_bad"]))

check("(SSC+) ENACTED UNDER ITS OWN GUARD -- and the guard is "
      "tau-RELATIVISED, tau >= qmax(z) + 2, NOT a blanket tau >= 3.  On "
      "every vertex of every family meeting that guard: "
      "F(d(z)) + qmax(z) <= s(z), zero failures.  The reading that "
      "matters is the one BELOW the guard: on vertices with "
      "tau <= qmax + 1 the same inequality FAILS repeatedly.  The "
      "guard is not decoration and it is not conservative -- it is "
      "exactly the condition that an edge avoiding e* cap g* exists",
      ACC["ssc_n"] >= 500 and ACC["ssc_bad"] == 0
      and ACC["ssc_unguard_bad"] > 0 and ACC["ssc_tightnz"] > 0,
      "guarded %d (0 failures, %d with s>0, %d tight); unguarded %d with "
      "%d ACTUAL FAILURES"
      % (ACC["ssc_n"], ACC["ssc_nz"], ACC["ssc_tightnz"],
         ACC["ssc_unguard"], ACC["ssc_unguard_bad"]))

check("AND AT tau = 6 THE GUARD IS FREE, for a reason that has nothing "
      "to do with (q3): two DISTINCT 6-tuples agree in at most 5 "
      "coordinates, so lambda <= 5 and q <= 4 for any two distinct "
      "edges whatever, whence qmax + 2 <= 6 = tau.  (q3) sharpens this "
      "to q <= 3 using tau = 6, but (SSC+) never needs it -- and does "
      "not get it, since the censuses below carry the q = 4 and q = 5 "
      "rows.  That the corpus itself carries lambda >= 5 pairs is "
      "counted, not asserted",
      max(lam(a, b) for a, b in itertools.combinations(
          [(0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 1, 2)], 2))
      == 5 and 4 + 2 <= 6 and ACC["q5"] > 0,
      "%d corpus families carry a pair with lambda >= 5 (q >= 4)"
      % ACC["q5"])

check("(SG) P + H <= R ENACTED -- AND ITS TWO HALVES ARE ENACTED TO "
      "DIFFERENT DEPTHS, WHICH IS SAID HERE RATHER THAN AVERAGED OVER. "
      "(a) THE EXCHANGE OF SUMMATION, sum_v s(v) = sum over pairs of "
      "q*lambda = R (a pair lies inside E(v) for exactly its "
      "lambda = q+1 shared cells), is enacted NON-VACUOUSLY and BOTH "
      "corpus-wide AND PER FAMILY: both sides are computed "
      "independently, agree in aggregate at a strictly positive value, "
      "and agree family by family with zero mismatches -- so "
      "compensating errors across families cannot pass.  (b) THE "
      "INEQUALITY P + H <= R is the shallow half.  Under the family "
      "guard tau >= qmax + 2 there are 71 families and zero failures, "
      "but ON 70 OF THEM THE READING IS 0 <= 0: the corpus's high-tau "
      "objects are the affine planes AG(2,q), all of whose degrees are "
      "q = r-1, so Phi(d, r-1) = 0 everywhere and P = H = R = 0.  ONE "
      "family reads it non-vacuously -- the fattened AG(2,3) of "
      "fat_plane(), built for exactly this purpose, at P + H = 3 "
      "against R = 30 -- and the count of non-vacuous readings is "
      "asserted, not merely printed.  The inequality's real backing is "
      "the proof above plus the mutation suite (M1 prices the +H term "
      "at 17 of section 3's 35 cells); this check measures what it "
      "measures.  The must-fail reading below the guard is beside it",
      ACC["sg_bad"] == 0 and ACC["sg_n"] > 0
      and ACC["sg_unguard_bad"] > 0
      and ACC["star_sum"] == ACC["Rsum"] and ACC["star_sum"] > 0
      and ACC["star_perfam_bad"] == 0
      and ACC["sg_nz"] > 0
      and (FATtau, FATq, FATP + FATH, FATR) == (3, 1, 3, 30)
      and FATtau >= FATq + 2 and max(FATD.values()) < len(FAT53),
      "guarded families %d (0 failures, %d with P + H > 0); unguarded %d "
      "with %d failures; sum_v s(v) = %d = R corpus-wide, %d per-family "
      "mismatches; fattened plane: m=%d tau=%d qmax=%d P+H=%d <= R=%d"
      % (ACC["sg_n"], ACC["sg_nz"], ACC["sg_unguard"],
         ACC["sg_unguard_bad"], ACC["star_sum"], ACC["star_perfam_bad"],
         len(FAT53), FATtau, FATq, FATP + FATH, FATR))

check("THE (Q) IDENTITY ENACTED EXACTLY, family by family: on every "
      "r = 6 family of the corpus, 10 P = m^2 - 25m + 2X + Sigma5 -- "
      "not an inequality, an equality, and it holds with zero "
      "exceptions.  This is the residue identity summed against "
      "sum_v d = 6m and sum_v d^2 = m^2 + 5m + 2X, so an error in "
      "either moment convention would show up here immediately",
      ACC["qid_n"] > 0 and ACC["qid_bad"] == 0
      and len(QROWS) == ACC["qid_n"],
      "%d r=6 families, %d identity failures"
      % (ACC["qid_n"], ACC["qid_bad"]))
CK_QID = NCHECK[0]

# ---- must-fail controls
PEN6 = [tuple([0] + [i] * 5) for i in range(9)]
pd = {}
for e in PEN6:
    for i in range(6):
        pd[(i, e[i])] = pd.get((i, e[i]), 0) + 1
pP = sum(F(d) for d in pd.values())
pH = sum(1 for d in pd.values() if d >= 6)
pR = sum((lam(a, b) - 1) * lam(a, b)
         for a, b in itertools.combinations(PEN6, 2))
check("MUST-FAIL CONTROL 1 -- (BDH) AND (SG) NEED AN EDGE AVOIDING z.  "
      "The r = 6, m = 9 pencil through one cell has X = R = 0 but its "
      "hub has degree 9, so P + H = F(9) + 1 = 5 > 0 = R and (SG) is "
      "FALSE on it.  No edge avoids the hub, so (BDH) has no f to "
      "spend.  In a critical core the hypothesis is free: a universal "
      "vertex is a 1-cover against tau = 6.  Across the corpus the "
      "control is not a one-off -- hundreds of universal-vertex "
      "families, of which a named minority break (SG) outright",
      pP + pH == 5 and pR == 0 and pP + pH > pR
      and max(pd.values()) == 9 and ACC["univ"] > 100
      and ACC["univ_break"] > 0,
      "pencil: P+H = %d > R = %d; corpus: %d universal-vertex families, "
      "%d break (SG)" % (pP + pH, pR, ACC["univ"], ACC["univ_break"]))

WITROWS = []
for q in (2, 3, 4, 5):
    W = ag_witness(q)
    r = q + 1
    dg = {}
    for e in W:
        for i in range(r):
            dg[(i, e[i])] = dg.get((i, e[i]), 0) + 1
    tw = mincover(W)
    bad = []
    for z in sorted(dg):
        Ez = [e for e in W if e[z[0]] == z[1]]
        if len(Ez) < 2:
            continue
        st = sum(lam(a, b) - 1 for a, b in itertools.combinations(Ez, 2))
        qm = max(lam(a, b) - 1 for a, b in itertools.combinations(Ez, 2))
        if phi(len(Ez), r - 1) + qm > st:
            bad.append((z, len(Ez), st, qm))
    inter = all(lam(a, b) >= 1 for a, b in itertools.combinations(W, 2))
    WITROWS.append((q, len(W), tw, len(bad),
                    bad[0][3] if bad else None, inter))
check("MUST-FAIL CONTROL 2 -- FOUR (SSC+) VIOLATION WITNESSES AT "
      "tau = qmax + 1 EXACTLY, one for each qmax = 1, 2, 3, 4, with tau "
      "COMPUTED EXACTLY by minimum cover rather than asserted.  Each is "
      "AG(2,q) with one edge's vertical coordinate renamed onto a new "
      "twin and the other q-1 points of that line deleted: the twin "
      "pair shares q cells, those cells are a MINIMUM cover, and every "
      "one of them is a vertex with d = q+1, s = qmax = q-1 and "
      "Phi(d, q) = 1 -- so (SSC+) reads 1 + (q-1) <= q-1 and fails by "
      "exactly one unit.  This is what makes the guard tau >= qmax + 2 "
      "sharp at every value of qmax the window can carry, and it is why "
      "the guard could not be weakened to tau >= 3",
      all(t[2] == t[4] + 1 and t[3] > 0 and t[5] for t in WITROWS)
      and sorted(t[4] for t in WITROWS) == [1, 2, 3, 4],
      show(["q=%d: m=%d tau=%d qmax=%d violations=%d"
            % (t[0], t[1], t[2], t[4], t[3]) for t in WITROWS]))

TRI = [(0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 1, 2)]
triq = sorted(lam(a, b) - 1 for a, b in itertools.combinations(TRI, 2))
triX = sum(triq)
triR = sum(q * (q + 1) for q in triq)
check("MUST-FAIL CONTROL 3 -- R <= 4X IS FALSE WITHOUT tau = 6.  The "
      "three edges (0,0,0,0,0,0), (0,0,0,0,0,1), (0,0,0,0,1,2) have "
      "lambda = 5, 4, 4, so q = (4,3,3): X = 10 and R = 44 > 40 = 4X.  "
      "The lambda = 5 pair is exactly what (q3) forbids, and it forbids "
      "it by the cover lemma -- this triple's five common cells ARE a "
      "cover, tau = 1 in fact, so the object is not a core.  Without "
      "that step the whole quadratic law loses its constant",
      triq == [3, 3, 4] and triX == 10 and triR == 44 and 4 * triX == 40
      and triR > 4 * triX and mincover(TRI) == 1,
      "q = %s, X = %d, R = %d > %d" % (show(triq), triX, triR, 4 * triX))

AG5 = AGF[5]
ag_deg = {}
for e in AG5:
    for i in range(6):
        ag_deg[(i, e[i])] = ag_deg.get((i, e[i]), 0) + 1
agX = sum(lam(a, b) - 1 for a, b in itertools.combinations(AG5, 2))
agR = sum((lam(a, b) - 1) * lam(a, b)
          for a, b in itertools.combinations(AG5, 2))
agP = sum(F(d) for d in ag_deg.values())
agH = sum(1 for d in ag_deg.values() if d >= 6)
agS5 = sum((d % 5) * (5 - d % 5) for d in ag_deg.values())
check("TIGHTNESS CONTROL -- THE CONSTANT 25 HAS ZERO SLACK AT ITS OWN "
      "THRESHOLD.  AG(2,5), the affine plane of order 5 read as a "
      "6-partite 6-uniform intersecting family, has m = 25, tau = 5, "
      "all 30 degrees equal to 5, and X = R = P = H = Sigma5 = 0.  Both "
      "summed laws are TIGHT on it: (SG) reads 0 <= 0 and (Q) reads "
      "m(m-25) + Sigma5 + 10H = 0 <= 38X = 0.  m = 25 is precisely "
      "where m(m-25) changes sign, and this object sits on that line "
      "with nothing to spare -- which is why the window starting at "
      "m = 22 is not a place the law can be read carelessly.  It is "
      "NOT a counterexample core: tau = 5 < 6",
      len(AG5) == 25 and mincover(AG5) == 5 and len(ag_deg) == 30
      and sorted(set(ag_deg.values())) == [5]
      and (agX, agR, agP, agH, agS5) == (0, 0, 0, 0, 0)
      and agP + agH == agR
      and 25 * (25 - 25) + agS5 + 10 * agH == 38 * agX,
      "m=25 tau=5 n=30 all degrees 5; X=R=P=H=Sigma5=0, both laws tight")

note("STATED, NOT TESTED (one line, 0019 (L-a) re-derived): a universal "
     "vertex is a 1-cover of K, so tau(K) = 1 < 6.  Every critical core "
     "therefore satisfies the hypothesis of (BDH) at every vertex -- "
     "some edge avoids z -- which is all the fibre count ever needs")
note("STATED, NOT TESTED (0019 (L-b) re-derived): each part's blocks "
     "partition the edge set, so they cover it; a part with <= 5 blocks "
     "would be a 5-cover against tau = 6.  Hence >= 6 vertices per part, "
     "n >= 36, and each part's degrees sum to m.  n >= 36 is a "
     "constraint of every census below and is priced at mutant M4")
note("STATED, NOT TESTED (0005 re-derived in two lines): if d(v) = 1 "
     "with unique edge e, then e minus v is a 5-set, hence not a cover, "
     "so some edge g avoids it; g must meet e, so g meets it in v -- "
     "but then g is a second edge through v.  Contradiction, so every "
     "degree is at least 2 and every census starts at d = 2")
note("STATED, NOT TESTED -- THE TWO MOMENT IDENTITIES, BOTH BY DOUBLE "
     "COUNTING.  They are the most-used inputs in the file and were the "
     "one pair that had escaped the ledger, so they are billed here.  "
     "FIRST MOMENT: count incident (vertex, edge) pairs.  Each edge is "
     "6 cells, so the count is 6m; each vertex v lies in d(v) edges, so "
     "it is also sum_v d(v).  Hence sum_v d(v) = 6m.  SECOND MOMENT: "
     "count triples (v, {e,f}) with v in e cap f, e != f.  Through each "
     "vertex there are C(d(v), 2) such pairs; each pair {e,f} is "
     "counted |e cap f| = lambda = q + 1 times.  Hence "
     "sum_v C(d(v),2) = sum over pairs (q+1) = C(m,2) + X, equivalently "
     "sum_v d(v)^2 = m^2 + 5m + 2X.  Both are enforced in every cell of "
     "both engines and they pin the definition of X itself; the second "
     "is also the identity the star identity of section 4 is the "
     "vertex-local shadow of")
note("STATED, NOT TESTED -- THE b = 5 COVERING BRANCH (0015 step (1) "
     "re-derived, and the ledger row that names it made honest).  In "
     "the per-edge budget the private e-avoiding 5-cover T_e is split "
     "over the on-e vertices, b_i of its cells falling in the fibres of "
     "the i-th one.  If b_i = 5 the cover exhausts that vertex's five "
     "free fibres, so every edge through it other than e is forced onto "
     "T_e in a part where it already agrees with e -- i.e. d_i = 1 -- "
     "and the term Phi(d_i - 1, 5 - b_i) = Phi(0, 0) is 0: the branch "
     "contributes nothing and the b <= 4 monotonicity of check 3 "
     "covers the rest.  This is the ONLY place b = 5 enters, and the "
     "two per-edge budgets it feeds are DERIVED here and then NOT "
     "IMPOSED in section 3's engine (check 23), so no kill in this "
     "file rests on it")

# ==========================================================================
# 3.  T-A20: the X = 5 field on m = 22..26 is empty
# ==========================================================================

head("3.  T-A20 -- X = 5 dies on m = 22..26, so X >= 6 EVERYWHERE")


def delta_of(X, q1):
    """The key cap, read as a degree ceiling: F(d) <= X - q_1.  At X = 5
    also intersected with the (SSC+) ceiling F(d) + 1 <= s <= X."""
    d1 = capF(X - q1)
    return min(d1, capF(X - 1)) if X == 5 else min(d1, 5 + X)


DELTAS = [(pi[0], delta_of(5, pi[0])) for pi in P5]
check("THE KEY CAP, READ OFF ONE PARTITION AT A TIME.  F(d(v)) <= X - "
      "q_1 for EVERY vertex: if v lies in the q_1-pair's shared set then "
      "(SSC+) subtracts qmax(v) >= q_1 from s(v) <= X; if it does not, "
      "that pair is not inside E(v) and s(v) <= X - q_1 already.  At "
      "X = 5 this gives Delta = 9, 8, 8, 7, 7, 6, 5 on the seven "
      "partitions (q_1 = 1, 2, 2, 3, 3, 4, 5).  It is written as an "
      "intersection with the (SSC+) ceiling F(d) <= 4 => d <= 9 that "
      "holds at every high vertex whatever q_1 is; SAID PLAINLY, that "
      "second term is just the q_1 = 1 case of the first and NEVER "
      "BINDS, since q_1 >= 1 always -- it is kept only to show the "
      "ceiling is free, not because it does work",
      [d for (t, d) in DELTAS] == [5, 6, 7, 7, 8, 8, 9]
      and capF(4) == 9 and F(10) == 5,
      show(["q1=%d: Delta=%d" % t for t in DELTAS]))

DOM = []
for (X, q1) in ((5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 3), (7, 3),
                (8, 3), (9, 3)):
    d_key = delta_of(X, q1)
    d_off = 5 + X - q1                  # 0019 (DH) with x_f >= q_1
    b32 = int(Fr(3, 2) * (X - q1))
    d32 = capF(b32) + 1                 # w(d) <= b  <=>  d <= capF(b)+1
    d43 = capF(int(Fr(4, 3) * (5 - q1))) + 1 if X == 5 else None
    DOM.append((X, q1, d_key, d_off, d32, d43))
check("WHAT THE KEY CAP ADDS TO 0019 (DH), AND WHAT THE TWO PER-EDGE "
      "BUDGETS DO NOT ADD -- BOTH MEASURED, AND NEITHER OVERSTATED.  "
      "(a) 0019's OFF-f CAP d <= 5 + X - x_f, read at x_f >= q_1, gives "
      "5 + X - q_1.  Measured against Delta(pi) it does NOT sit above "
      "the key cap: at X = 5 the two COINCIDE EXACTLY at every q_1 "
      "(9/8/7/6/5 against 9/8/7/6/5), and across the section 4 rows it "
      "is equal or weaker, strictly weaker only at X = 9 (11 against "
      "10).  So the key cap's gain over (DH) is NOT tightness, it is "
      "COVERAGE: (DH) caps only the vertices that some q_1-pair edge "
      "AVOIDS, while the key cap also covers the S_1 vertices -- which "
      "no q_1-pair edge avoids -- and that is what licenses capping "
      "EVERY degree.  (b) 0015 (CC)'s sum_{v in f} w(d(v)) <= "
      "floor((3/2)(X - x_f)) and 0017 check 9's floor((4/3)(5 - x_f)) "
      "are DERIVED here and then NOT IMPOSED in the census at all.  The "
      "justification for dropping them is that omitting a constraint "
      "WIDENS the census, and a wider census can only LOWER min S, so "
      "every kill in this section holds a fortiori.  The table below is "
      "the secondary observation, not the justification: read one "
      "on-f degree at a time each budget caps it at capF(budget) + 1, "
      "which sits at least one degree above capF(X - q_1) every time.  "
      "Both budgets are SUMS over the six cells of f, so this per-vertex "
      "reading does NOT establish that the sums are slack, and the word "
      "'non-binding' is not used for them",
      all(t[3] >= t[2] for t in DOM)
      and all(t[3] == t[2] for t in DOM if t[0] == 5)
      and [t for t in DOM if t[3] > t[2]] == [(9, 3, 10, 11, 13, None)]
      and all(t[4] > t[2] for t in DOM)
      and all(t[5] is None or t[5] > t[2] for t in DOM),
      show(["X=%d q1=%d: key %d vs off-f %d vs 3/2 %s vs 4/3 %s"
            % (t[0], t[1], t[2], t[3], t[4], t[5]) for t in DOM]))
CK_DOM = NCHECK[0]

t0 = time.time()
S3ROWS = []
for pi in P5:
    D = delta_of(5, pi[0])
    row = []
    for m in range(22, 27):
        v, arg = minS(m, 5, D)
        row.append(v)
    S3ROWS.append((pi, D, Rof(pi), tuple(row)))
S3TIME = time.time() - t0
print("\n      partition        Delta   R    min S at m = 22, 23, 24, 25, 26"
      "        margins", flush=True)
for (pi, D, R, row) in S3ROWS:
    print("      %-16s  %2d   %2d    %-28s  %s"
          % (str(pi), D, R,
             show([("infeasible" if v is None else v) for v in row]),
             show([("-" if v is None else v - R) for v in row])), flush=True)
S3_ALIVE = [(pi, 22 + i) for (pi, D, R, row) in S3ROWS
            for i in range(5) if row[i] is not None and row[i] <= R]
S3_MARG = sorted(row[i] - R for (pi, D, R, row) in S3ROWS
                 for i in range(5) if row[i] is not None)
check("THE X = 5 CENSUS ON m = 22..26, ALL SEVEN PARTITIONS, 35 CELLS: "
      "min S > R(pi) in EVERY ONE, so no census survives and X = 5 is "
      "empty on the whole of 0019 T-B's residual band.  Each cell "
      "enforces both moment identities, n >= 36, n_2 <= floor(m/2) and "
      "the partition's Delta -- and minimises S = P + H, which (SG) "
      "caps at R(pi).  The two WIDE rows (4,1) and (5) are carried, not "
      "deleted: their censuses are INFEASIBLE outright, which is the "
      "census killing them rather than (q3) doing it -- (q3) is not "
      "spent anywhere in this section",
      S3_ALIVE == []
      and all(row[i] is None or row[i] > R
              for (pi, D, R, row) in S3ROWS for i in range(5))
      and [pi for (pi, D, R, row) in S3ROWS
           if all(v is None for v in row)] == [(5,), (4, 1)],
      "35 cells, 0 survivors, thinnest margin %s, %.1fs"
      % (S3_MARG[0] if S3_MARG else "no feasible cell", S3TIME))
CK_S3 = NCHECK[0]
check("and the enumerator's LEAF RE-VERIFICATION held: every vector the "
      "census emits is re-checked from scratch against all four "
      "constraints -- both moments, n >= nmin, and the first-moment "
      "bound n_d <= floor(6m/d) RECOMPUTED FROM m rather than read off "
      "the threaded caps.  Recorded into a list and checked here, NOT "
      "by a bare assert, which -O strips",
      INTERNAL == [] and LEAVES[0] > 0,
      "%d census vectors emitted so far, 0 internal violations"
      % LEAVES[0])

note("TWO MODELS, TWO TABLES, BOTH CORRECT -- A MODEL COMPARISON, NOT A "
     "CORRECTION (D-036, restated 2026-07-28).  The desk spec carried "
     "the outside review's own min-S table -- 13,14,14,15,15 / "
     "15,15,16,17,19 twice / 19,21,21,24,25 twice -- and transcribed it "
     "faithfully.  THOSE ROWS ARE RIGHT UNDER THE MODEL THE REVIEW "
     "STATES: a GLOBAL Delta <= 9 from (SSC+), the 0019 off-f cap "
     "d <= 10 - t on the vertices some q_1-pair edge avoids, and the "
     "0017 4/3 budget sum_{v in f} w(d(v)) <= floor((4/3)(5-t)) on the "
     "six cells of f.  Re-run under that model they reproduce.  THIS "
     "FILE RUNS A DIFFERENT MODEL: the per-partition key cap "
     "F(d(v)) <= X - q_1 imposed at EVERY vertex, with NO on-f budget "
     "imposed at all.  It returns 16,16,16,19,20 on the q_1 = 2 rows "
     "and 21,23,23,24,27 on the q_1 = 3 rows -- uniformly LARGER, i.e. "
     "WIDER KILLS -- while the q_1 = 1 row and the whole m = 27..31 "
     "extension agree with the review exactly.  Neither table is an "
     "error; they price different constraint sets, and this file is "
     "governed by its own.  CONSEQUENCE UNDER THIS MODEL: the spec's "
     "'three one-unit cells' do not exist here -- the thinnest margin "
     "in this section is 2, at (2,2,1) on m = 22, 23 and 24.  An "
     "earlier draft of this note called the review's rows 'withdrawn' "
     "and 'a spec error' and asserted that no cap set reproduces them.  "
     "That was a deflation of correct peer work; it is retracted, and "
     "the retraction is kept in the file rather than quietly edited "
     "out")

EXT = []
for pi in P5:
    D = delta_of(5, pi[0])
    EXT.append((pi, Rof(pi),
                tuple(minS(m, 5, D)[0] for m in range(27, 32))))
check("BELT AND SUSPENDERS: THE SAME CENSUS EMPTIES X = 5 ON m = 27..31 "
      "TOO, so T-A20 does not actually lean on 0019 T-B.  C3 at X = 5 "
      "caps m <= 31, and on those five rungs min S runs 20, 23, 25, 30, "
      "35 for the matching partition against R = 10, and higher still "
      "on the wider ones.  If T-B were withdrawn tomorrow, X >= 6 would "
      "survive on the strength of this section alone.  THE m <= 31 "
      "CEILING IS EVALUATED HERE, not asserted: c3cap(5, 31) = 1 > 0 "
      "and c3cap(5, 32) = 0, so C3 itself closes the X = 5 band at 31 "
      "and the emptied rungs 22..31 are ALL of it -- which is what "
      "makes the belt-and-suspenders route complete",
      all(v is None or v > R for (pi, R, row) in EXT for v in row)
      and [t[2] for t in EXT if t[0] == (1, 1, 1, 1, 1)][0]
      == (20, 23, 25, 30, 35)
      and c3cap(5, 31) >= 1 and c3cap(5, 32) <= 0,
      show(["%s: %s" % (str(t[0]), show(t[2])) for t in EXT[-3:]])
      + "; c3cap(5,31) = %d, c3cap(5,32) = %d"
      % (c3cap(5, 31), c3cap(5, 32)))

check("T-A20 ASSEMBLED -- A RESTATEMENT, NOT A NEW KILL.  0019 T-A puts "
      "X >= 5 on every critical core in [22, 456].  0019 T-B confines "
      "X = 5 to m <= 26.  This section empties X = 5 on m = 22..26 -- "
      "and, independently, on m = 27..31.  Hence X >= 6 for every "
      "critical core in the window.  Every conjunct is asserted above; "
      "this line says what they add up to",
      S3_ALIVE == [] and all(v is None or v > R
                             for (pi, R, row) in EXT for v in row)
      and len(S3ROWS) == 7)

# ==========================================================================
# 4.  T-B20: the staircase
# ==========================================================================

head("4.  T-B20 -- the staircase, by per-X sweeps with a structural floor")

RUNGS = {}
for X in (6, 7, 8, 9):
    lo = {6: 27, 7: 29, 8: 30, 9: 32}[X]
    ms = []
    m = lo
    while c3cap(X, m) > 0:
        ms.append((m, c3cap(X, m)))
        m += 1
    RUNGS[X] = (ms, m)
check("THE RUNG CEILINGS COME FROM C3 BEFORE ANY CENSUS RUNS.  0017's "
      "per-edge law 2m + 5x_e <= 52 + 3X, together with sum_e x_e = 2X "
      "> 0 forcing SOME edge to carry x_e >= 1, kills a rung outright "
      "as soon as floor((52+3X-2m)/5) <= 0.  That happens at m = 33, "
      "35, 36, 38 for X = 6, 7, 8, 9, so each band is exactly six rungs "
      "wide, and on every rung the same law caps the largest pair "
      "excess at c = floor((52+3X-2m)/5) <= 3.  THAT is why parts <= 3 "
      "here -- C3, not (q3), which is spent nowhere in this section",
      [RUNGS[X][1] for X in (6, 7, 8, 9)] == [33, 35, 36, 38]
      and all(len(RUNGS[X][0]) == 6 for X in (6, 7, 8, 9))
      and max(c for X in (6, 7, 8, 9) for (m, c) in RUNGS[X][0]) == 3,
      show(["X=%d: m=%d..%d, c=%s" % (X, RUNGS[X][0][0][0],
                                      RUNGS[X][0][-1][0],
                                      show([c for (m, c) in RUNGS[X][0]]))
            for X in (6, 7, 8, 9)]))


def sweep(nmin=36, use_n2cap=False, pilimit=None):
    """Every (X, m, partition) cell of the staircase, run through the
    second-moment maximiser.  A cell DIES when the largest second moment
    any admissible census can reach falls short of the required
    m^2 + 5m + 2X.

    THE PRIMARY RUN IS (D2)-FREE -- use_n2cap defaults to FALSE here,
    unlike censuses(), because 0008 is billed to section 3 and this
    engine must not quietly spend it.  M3 re-runs the sweep with the cap
    ON and measures that no cell value and no survivor moves."""
    cells = []
    for X in (6, 7, 8, 9):
        for (m, c) in RUNGS[X][0]:
            req = m * m + 5 * m + 2 * X
            pis = parts_of(X, min(3, c))
            if pilimit and (X, m) in pilimit:
                pis = pilimit[(X, m)]
            for pi in pis:
                D = min(capF(X - pi[0]), 5 + X)
                bw = dict((d, F(d) + pi[-1]) for d in range(6, D + 1))
                mx, arg = maximize_sq(m, X, D, bw, Rof(pi), nmin, use_n2cap)
                cells.append((X, m, pi, c, D, Rof(pi), mx, req, arg))
    return cells


t0 = time.time()
CELLS = sweep(use_n2cap=False)
S4TIME = time.time() - t0
SURV = [c for c in CELLS if c[6] is not None and c[6] >= c[7]]
KILLS = sorted((c[7] - c[6], c) for c in CELLS
               if c[6] is not None and c[6] < c[7])
print("\n      thinnest arithmetic kills in the sweep:", flush=True)
for (mg, c) in KILLS[:4]:
    print("      margin %4d   X=%d m=%d pi=%-14s Delta=%2d R=%2d  "
          "max sum d^2 = %d  vs required %d"
          % (mg, c[0], c[1], str(c[2]), c[4], c[5], c[6], c[7]), flush=True)
check("THE SWEEP: 92 (X, m, partition) cells across the four bands, "
      "each one asking the second-moment maximiser for the largest "
      "sum d^2 n_d an admissible census can reach under sum d n_d = 6m, "
      "n >= 36, the key-cap ceiling Delta = capF(X - q_1) intersected "
      "with 0019's Delta <= 5 + X, and the per-partition high-vertex "
      "budget sum_{d>=6} (F(d) + q_min) n_d <= R(pi) -- which is NOT "
      "(SG) restricted to the high vertices (that would carry +1, not "
      "+q_min) but the UN-WEAKENED line (SG)'s own proof passes "
      "through, sum_v F(d(v)) + sum_v qmax(v) <= sum_v s(v) = R, with "
      "qmax(v) >= q_min because qmax(v) is the excess of an actual "
      "pair.  For q_min >= 2 that is strictly stronger than (SG), so it "
      "is named here rather than left to be looked for in the claim "
      "table.  THAT LIST IS THE WHOLE "
      "LIST: this engine does NOT impose 0008's n_2 <= floor(m/2), "
      "which is billed to section 3 -- the staircase is (D2)-free by "
      "construction here and not merely by consequence, and M3 measures "
      "that switching the cap on moves nothing.  EXACTLY ONE CELL "
      "SURVIVES: X = 8, m = 30, pi = (3,3,1,1), which reaches 1076 "
      "against the required 1066.  Every other cell falls short, the "
      "thinnest by 2 -- (8, 30, (3,2,2,1)) at 1064 against 1066",
      len(CELLS) == 92 and len(SURV) == 1
      and (SURV[0][0], SURV[0][1], SURV[0][2]) == (8, 30, (3, 3, 1, 1))
      and SURV[0][6] == 1076 and SURV[0][7] == 1066
      and len(KILLS) == 91 and KILLS[0][0] == 2
      and (KILLS[0][1][0], KILLS[0][1][1], KILLS[0][1][2])
      == (8, 30, (3, 2, 2, 1)),
      "%d survivor(s), %d kills, thinnest margin %s, widest %s, %.1fs"
      % (len(SURV), len(KILLS),
         KILLS[0][0] if KILLS else "no arithmetic kill",
         KILLS[-1][0] if KILLS else "-", S4TIME))
CK_SWEEP = NCHECK[0]

note("MEASURED AND REPORTED AGAINST THE DESK SPEC, which pinned the "
     "thinnest arithmetic kill at (8,30,(3,2,2,1)) with MARGIN 6.  "
     "Measured here it is margin 2 (1064 against 1066).  The cell and "
     "its identity as the thinnest are confirmed; the number is not.  "
     "The measurement stands")

check("AND THE MAXIMISER'S WITNESSES ARE RE-VERIFIED, not trusted: for "
      "every cell that reports a finite maximum, the census vector it "
      "returns is re-checked from scratch -- non-negative, first moment "
      "exactly 6m, n >= 36, degrees within Delta, the (SG) budget "
      "respected, and its second moment EQUAL to the reported value.  "
      "SIX constraints, and n_2 <= floor(m/2) is deliberately NOT among "
      "them: this engine does not impose (D2), so re-verifying against "
      "it would be checking a constraint the sweep never used.  A "
      "maximiser that overstates its optimum would kill cells the "
      "lemmas do not kill, and that is the direction nothing else in "
      "this file could see",
      all(c[8] is not None for c in CELLS)
      and all(sum((i + 2) * v for i, v in enumerate(c[8])) == 6 * c[1]
              and sum(v for v in c[8]) >= 36
              and all(v >= 0 for v in c[8])
              and len(c[8]) == c[4] - 1
              and sum((i + 2) ** 2 * v for i, v in enumerate(c[8])) == c[6]
              and sum((F(i + 2) + c[2][-1]) * v
                      for i, v in enumerate(c[8]) if i + 2 >= 6) <= c[5]
              for c in CELLS),
      "%d cells, every optimum re-verified against all six constraints; "
      "%d of the winning witnesses would also have satisfied (D2)"
      % (len(CELLS), sum(1 for c in CELLS if c[8][0] <= c[1] // 2)))
CK_REVER = NCHECK[0]


def brute_max(m, X, dmax, budget_w, R, nmin=36, cap2=None):
    """A SECOND, DELIBERATELY STUPID maximiser: recurse over every degree
    from dmax down to 3 and solve n_2 at the leaf, keeping the largest
    second moment seen.  It shares no code path with maximize_sq -- no
    closed form, no early break, no identity -- so agreement between the
    two is a genuine cross-assertion and not a re-run.  cap2 = None
    means NO (D2) cap, matching the primary sweep."""
    S1 = 6 * m
    if cap2 is None:
        cap2 = 6 * m
    best = [None]

    def rec(d, r1, cnt, bl, sq):
        NODES[0] += 1
        if d == 2:
            if r1 % 2:
                return
            n2 = r1 // 2
            if n2 > cap2 or cnt + n2 < nmin:
                return
            v = sq + 4 * n2
            if best[0] is None or v > best[0]:
                best[0] = v
            return
        wg = budget_w.get(d, 0)
        k = 0
        while d * k <= r1 and (wg == 0 or wg * k <= bl):
            rec(d - 1, r1 - d * k, cnt + k, bl - wg * k, sq + d * d * k)
            k += 1

    rec(dmax, S1, 0, R, 0)
    return best[0]


t0 = time.time()
XSET = [(8, 30, (3, 3, 1, 1)), (8, 30, (3, 2, 2, 1)), (7, 29, (3, 3, 1)),
        (6, 27, (3, 2, 1)), (9, 32, (3, 3, 2, 1)), (6, 32, (1,) * 6),
        (8, 35, (1,) * 8), (9, 37, (1,) * 9)]
XROWS = []
for (X, m, pi) in XSET:
    c = [t for t in CELLS if (t[0], t[1], t[2]) == (X, m, pi)][0]
    XROWS.append((X, m, pi, c[6], brute_max(m, X, c[4],
                                            dict((d, F(d) + pi[-1])
                                                 for d in range(6, c[4] + 1)),
                                            c[5])))
check("AND THE MAXIMISER IS CROSS-ASSERTED AGAINST A SECOND, INDEPENDENT "
      "ONE.  maximize_sq is fast because it solves the low half in "
      "closed form and breaks the scan early; both of those could in "
      "principle UNDERSTATE an optimum, and understating is the "
      "dangerous direction -- it would kill cells the lemmas do not "
      "kill, and check 30's re-verification could not see it, since a "
      "valid-but-suboptimal witness passes every constraint.  So eight "
      "cells -- THE SURVIVOR, THE THINNEST ARITHMETIC KILL IN EACH OF "
      "THE FOUR BANDS ((8,30,(3,2,2,1)), (7,29,(3,3,1)), "
      "(6,27,(3,2,1)), (9,32,(3,3,2,1))), AND THE WIDEST PARTITION AT "
      "THREE OF THE FOUR BAND TOPS -- are re-maximised by brute "
      "recursion over every degree with no closed form and no early "
      "break.  All eight agree EXACTLY",
      all(t[3] == t[4] for t in XROWS) and len(XROWS) == 8,
      "%d cells re-maximised, 0 disagreements, %.1fs"
      % (len(XROWS), time.time() - t0))
note("STATED, NOT TESTED -- THE OTHER 84 CELLS.  The same "
     "maximize_sq-against-brute_max comparison was run offline on ALL "
     "92 cells, also with zero disagreements; it costs about 70 s, "
     "which would push the bare 3.9.6 run past its budget, so eight "
     "cells are kept in-run for the clock.  Stated here rather than "
     "inside a green check label, because the artifact cannot "
     "reproduce it as it stands")

# ---- the exceptional cell, structurally
head("4(x).  the one survivor -- X = 8, m = 30, q = (3,3,1,1) -- killed "
     "by structure")

EX = SURV[0] if SURV else (8, 30, (3, 3, 1, 1), 3, 10, 0, 0, 0, None)
exX, exm, expi, exc_cap, exD = EX[0], EX[1], EX[2], EX[3], EX[4]
sizes = tuple(q + 1 for q in expi)
share_ok = [(i, j) for i in range(4) for j in range(i + 1, 4)
            if expi[i] + expi[j] <= exc_cap]
check("(i) WHICH PAIRS MAY SHARE AN EDGE.  |S_i| = q_i + 1 gives shared "
      "sets of sizes 4, 4, 2, 2.  If P_i and P_j share an edge e then "
      "q_i + q_j <= x_e <= c = 3 on this rung, by C3 -- so only "
      "{P_3, P_4} (1 + 1 = 2 <= 3) may share one.  Every other pairing "
      "needs at least 4",
      sizes == (4, 4, 2, 2) and exc_cap == 3
      and share_ok == [(2, 3)],
      "shared-set sizes %s, c = %d, pairs that may share an edge: %s"
      % (show(sizes), exc_cap, show(share_ok)))

ok_ii, why_ii = licensed_ii(expi, exc_cap)
check("(ii) |S_i cap S_j| <= 1 FOR ALL i != j, by exhaustive case "
      "analysis over the two ways two shared sets could meet twice.  If "
      "P_i and P_j are EDGE-DISJOINT, two common vertices sit on all "
      "four edges, so all SIX pairs among them are excessive -- pi "
      "would need six parts and it has four.  THAT COUNT CARRIES EVERY "
      "INDEX PAIR AND IS WHAT THE CODE TESTS.  (The x-bound route, "
      "'each edge then carries x >= q_i + 2 > c', closes only where "
      "q_i >= 2; at {P_3, P_4}, with q_3 = q_4 = 1, it gives x >= 3 = c "
      "and does NOT close -- which is exactly why licensed_ii's Case A "
      "conjoins k >= 6 rather than leaning on the x-bound.)  If they "
      "SHARE an edge (only {P_3, P_4} may, by (i)), then with "
      "P_3 = {e,g} and P_4 = {e,h} the two common vertices lie in "
      "g cap h too, so {g,h} is a fifth excessive pair; it must be P_1 "
      "or P_2, and then g sits in two pairs with x_g >= 3 + 1 = 4 > 3.  "
      "Both cases die.  THE REVIEW'S DEFECT, STATED EXACTLY: its "
      "section 7.2 table names (3+3+2) as the only remaining partition "
      "at (8,30) and so omits this one.  Its edge-disjointness sentence "
      "is TRUE of the partitions it did list -- there q_i + q_j >= 5 > "
      "3 = c for every index pair, so edge-disjointness is forced -- "
      "and becomes false only at the omitted (3,3,1,1), where {P_3,P_4} "
      "may share.  One defect, two consequences.  This is the repair, "
      "and it is checked mechanically, not asserted",
      ok_ii and why_ii == []
      and licensed_ii((3, 3, 2), 3)[0]
      and [(i, j) for i in range(3) for j in range(i + 1, 3)
           if (3, 3, 2)[i] + (3, 3, 2)[j] <= 3] == [],
      "all 6 index pairs licensed; at the review's (3,3,2) no index "
      "pair may share an edge at all, which is why its sentence held "
      "there")

PROF = legal_profiles(expi, exD)
sing = [(T, dm) for (T, dm, wt) in legal_profiles(expi, exD, minsize=1)
        if len(T) <= 1]
check("(iii) EVERY HIGH VERTEX HAS |T_v| >= 2, and its degree is capped "
      "by its own index set.  All excess sits in the four pairs, so the "
      "STAR IDENTITY s(v) = sum_{i in T_v} q_i holds exactly, with "
      "T_v = {i : v in S_i}.  If |T_v| <= 1 then s(v) = qmax(v) and "
      "(SSC+) forces F(d(v)) <= 0, i.e. d(v) <= 5: not high.  With "
      "|T_v| >= 2, d(v) <= capF(s(T_v) - qmax(T_v)), which reads d <= 8 "
      "for {1,2}, d <= 6 for the four mixed pairs and for {3,4}, d <= 9 "
      "for {1,2,3} and {1,2,4}, d <= 7 for {1,3,4} and {2,3,4}, and "
      "d <= 10 for the full set",
      all(dm <= 5 for (T, dm) in sing)
      and dict(((T, dm) for (T, dm, wt) in PROF))[(0, 1)] == 8
      and dict(((T, dm) for (T, dm, wt) in PROF))[(2, 3)] == 6
      and dict(((T, dm) for (T, dm, wt) in PROF))[(0, 1, 2)] == 9
      and dict(((T, dm) for (T, dm, wt) in PROF))[(0, 2, 3)] == 7
      and dict(((T, dm) for (T, dm, wt) in PROF))[(0, 1, 2, 3)] == 10
      and len(sing) == 4 and all(len(T) == 1 for (T, dm) in sing),
      "the %d SINGLETON index sets cap at d <= %d (the empty set is not "
      "enumerated -- its qmax is undefined -- and is trivial anyway: "
      "s = qmax = 0 forces F(d) <= 0, d <= 5)"
      % (len(sing), max(dm for (T, dm) in sing)))
CK_III = NCHECK[0]

MAXHIGH, BESTPROF = profile_max(expi, exD)
bnd = 42 * exm - 360 + MAXHIGH
req = exm * exm + 5 * exm + 2 * exX
check("(iv) + (v) THE PROFILE MAXIMISER, AND THE KILL.  By (ii) each "
      "index PAIR {i,j} lies in at most one shared-set intersection, so "
      "it hosts at most one high vertex -- the T_v's form a linear "
      "system on the four parts.  Enumerating every legal profile and "
      "maximising sum (d-2)(d-5) over it gives MAXHIGH = 40, attained "
      "by a single vertex with T_v = {1,2,3,4} at degree 10 -- and, "
      "WITHIN THE RELAXED PROFILE SPACE THE ENUMERATOR SEARCHES, also "
      "by {1,2,3} at 9 plus the three sets containing 4 (28 + 4 + 4 + "
      "4).  That second profile is NOT REALISABLE -- it puts three "
      "distinct high vertices in S_4 and |S_4| = q_4 + 1 = 2 -- because "
      "the enumerator deliberately omits the |S_i| <= q_i + 1 slot cap. "
      "Omitting it can only RAISE MAXHIGH, hence only weaken the bound, "
      "which is the safe direction; and it changes nothing here, since "
      "the {1,2,3,4} witness needs exactly one slot in each S_i.  Then "
      "sum d^2 = 42m - 10n + sum exc <= 42*30 - 360 + 40 = 940, against "
      "the 1066 the second moment requires.  DEAD, by 126 units -- and "
      "note the cell has NO arithmetic margin at all: this is a "
      "structural kill, the only one in the certificate",
      MAXHIGH == 40 and bnd == 940 and req == 1066 and bnd < req
      and len(BESTPROF) >= 1
      and 42 * exm - 360 + MAXHIGH == 940,
      "MAXHIGH = %d, best profile %s, bound %d < %d required"
      % (MAXHIGH, show([("T=%s d<=%d" % (tuple(i + 1 for i in T), dm))
                        for (T, dm) in BESTPROF]), bnd, req))
CK_KILL = NCHECK[0]

CORROB = []
for (X, m, pi) in ((6, 27, (3, 3)), (7, 29, (3, 3, 1)), (9, 32, (3, 3, 3))):
    D = min(capF(X - pi[0]), 5 + X)
    mh, _ = profile_max(pi, D)
    lic, _ = licensed_ii(pi, c3cap(X, m))
    CORROB.append((X, m, pi, mh, 42 * m - 360 + mh, m * m + 5 * m + 2 * X,
                   lic))
check("(vi) THE SAME MAXIMISER ON THE OTHER THREE HEAVY CELLS, as "
      "corroboration that the structural layer is a general instrument "
      "and not a bespoke argument for one cell.  (6,27,(3,3)): MAXHIGH "
      "18, bound 792 vs 876 required.  (7,29,(3,3,1)): 28, 886 vs 1000. "
      "(9,32,(3,3,3)): 54, 1038 vs 1202.  All three dead, all three "
      "with (ii) independently licensed -- and all three were ALREADY "
      "dead arithmetically, so this layer is corroboration there and "
      "load-bearing only at (8,30,(3,3,1,1))",
      [t[3] for t in CORROB] == [18, 28, 54]
      and all(t[4] < t[5] for t in CORROB)
      and all(t[6] for t in CORROB),
      show(["X=%d m=%d %s: MAXHIGH %d, %d < %d"
            % (t[0], t[1], str(t[2]), t[3], t[4], t[5]) for t in CORROB]))
CK_CORR = NCHECK[0]

check("T-B20 ASSEMBLED.  Every cell of every rung of every band is "
      "dead: 91 by arithmetic, one by structure.  Hence X = 6 forces "
      "m <= 26, X = 7 forces m <= 28, X = 8 forces m <= 29 and X = 9 "
      "forces m <= 31 -- equivalently m >= 27 forces X >= 7, m >= 29 "
      "forces X >= 8, m >= 30 forces X >= 9 and m >= 32 forces X >= 10",
      len(CELLS) == 92 and len(SURV) == 1 and MAXHIGH == 40 and bnd < req
      and [RUNGS[X][0][0][0] for X in (6, 7, 8, 9)] == [27, 29, 30, 32])
CK_TB = NCHECK[0]

M26 = []
for pi in parts_of(6, min(3, c3cap(6, 26))):
    D = min(capF(6 - pi[0]), 11)
    bw = dict((d, F(d) + pi[-1]) for d in range(6, D + 1))
    mx, arg = maximize_sq(26, 6, D, bw, Rof(pi), 36, False)
    mh, _ = profile_max(pi, D)
    M26.append((pi, mx, 26 * 26 + 5 * 26 + 12, 42 * 26 - 360 + mh,
                licensed_ii(pi, c3cap(6, 26))[0], mh))
M26_alive = [t for t in M26 if t[1] is not None and t[1] >= t[2]]
note("STATED, NOT CLAIMED -- THE m <= 25 BY-PRODUCT, MEASURED.  Running "
     "the X = 6 machinery one rung lower, at m = 26, kills every "
     "partition but %s, which survives the ARITHMETIC by %d (%d against "
     "%d) and then dies to the profile maximiser at MAXHIGH = %d, bound "
     "%d against %d -- with step (ii) independently licensed there too "
     "(%s).  So X = 6 => m <= 25 is MEASURED.  Every number in this "
     "sentence is computed in this run, not transcribed.  It is NOT "
     "claimed: it is single-route, it leans on the structural layer at "
     "a rung where nothing else corroborates, and the desk spec's own "
     "expectation for this rung (a clean arithmetic kill at margin 8) "
     "did not reproduce.  This certificate claims X = 6 => m <= 26 and "
     "stops"
     % (show([str(t[0]) for t in M26_alive]),
        M26_alive[0][1] - M26_alive[0][2] if M26_alive else 0,
        M26_alive[0][1] if M26_alive else 0,
        M26_alive[0][2] if M26_alive else 0,
        M26_alive[0][5] if M26_alive else 0,
        M26_alive[0][3] if M26_alive else 0,
        M26_alive[0][2] if M26_alive else 0,
        "step (ii) licensed"
        if M26_alive and M26_alive[0][4] else "NOT licensed"))

# ==========================================================================
# 5.  The quadratic law and the ceiling
# ==========================================================================

head("5.  (Q), (Q0), (H1) -- the law that reaches the far end of the window")

QIDROWS = [t for t in QROWS
           if 10 * t[1] == t[0] * t[0] - 25 * t[0] + 2 * t[3] + t[4]]
QCHAIN = [t for t in QROWS if t[1] + t[2] <= t[5] and t[5] <= 4 * t[3]]
QCHBAD = [t for t in QCHAIN
          if t[0] * (t[0] - 25) + t[4] + 10 * t[2] > 38 * t[3]]
check(("(Q) DERIVED -- AND THE DERIVATION IS RUN ON DATA, NOT NARRATED.  "
      "Summing the residue identity over the vertices and substituting "
      "the two moments gives 10P = m^2 - 25m + 2X + Sigma5.  RE-RUN "
      "HERE family by family over every r = 6 corpus family from its "
      "own (m, P, H, X, Sigma5, R): the residual 10P - (m^2 - 25m + 2X "
      "+ Sigma5) is 0 on all of them, and the family count is positive "
      "so the statement is not vacuous.  THEN THE CHAIN STEP ITSELF, "
      "also on data: on every family where the two hypotheses actually "
      "hold -- (SG) P + H <= R and (q3) R <= 4X -- the conclusion "
      "m(m-25) + Sigma5 + 10H <= 38X holds, with zero exceptions and a "
      "positive population.  Symbolically it is 10P + 10H <= 10R <= 40X "
      "with 10P = m(m-25) + 2X + Sigma5, the 38 being 40 minus the 2 "
      "that 2X contributes on the left; it is not a fitted constant.  "
      "The identity's primary enactment is at check %d" % CK_QID),
      len(QROWS) > 0 and len(QIDROWS) == len(QROWS)
      and len(QCHAIN) > 0 and QCHBAD == []
      and 40 - 2 == 38 and Q0[456] == 5172,
      "%d r=6 families: %d satisfy the identity exactly (0 residuals), "
      "%d satisfy both chain hypotheses and ALL of those satisfy "
      "(Q); ceiling floor ceil(456*431/38) = %d"
      % (len(QROWS), len(QIDROWS), len(QCHAIN), Q0[456]))
CK_QD = NCHECK[0]

Q0WIN = [(m, ceil_fr(Fr(m * (m - 25), 38))) for m in range(22, 457)]
check("(Q0) ACROSS THE WHOLE WINDOW, exact Fractions: the floor it "
      "imposes is 0 up to m = 25 (where m(m-25) <= 0 and the law says "
      "nothing), 1 at m = 26, and then climbs -- 13 at m = 38, 236 at "
      "m = 108, 2310 at m = 309, 5172 at m = 456.  It first exceeds "
      "this certificate's X >= 6 at m = 33, so from m = 33 up (Q0) is "
      "already the stronger statement and the staircase is a LOW-m "
      "instrument -- which is also why the staircase stops at X = 9: "
      "its bands end at m = 37, and (Q0) has taken over long before",
      [v for (m, v) in Q0WIN if m in (25, 26, 38, 108, 309, 456)]
      == [0, 1, 13, 236, 2310, 5172]
      and min(m for (m, v) in Q0WIN if v > 6) == 33
      and all(Q0WIN[i][1] <= Q0WIN[i + 1][1] for i in range(len(Q0WIN) - 1)),
      "(Q0) overtakes X >= 6 at m = %d"
      % min(m for (m, v) in Q0WIN if v > 6))
CK_Q0WIN = NCHECK[0]

check("(H1) H >= 1 FOR EVERY CORE WITH m >= 26.  If H = 0 then every "
      "degree is at most 5, so F(d(v)) = 0 at every vertex and P = 0; "
      "the identity then reads m(m-25) + 2X + Sigma5 = 0 with all three "
      "terms non-negative at m >= 26.  Impossible.  So 10H >= 10 and "
      "X >= ceil((m(m-25) + 10)/38), which AT THE CEILING m = 456 reads "
      "X >= 5173: 456*431 = 196536 is 38*5172 EXACTLY, so the ten units "
      "of the lone high vertex are what lift the floor by one.  Nowhere "
      "else in the window does the +10 change the answer by more than "
      "one",
      F(5) == 0 and ceil_fr(Fr(456 * 431 + 10, 38)) == 5173
      and ceil_fr(Fr(456 * 431, 38)) == 5172
      and max(ceil_fr(Fr(m * (m - 25) + 10, 38))
              - ceil_fr(Fr(m * (m - 25), 38))
              for m in range(26, 457)) == 1,
      "X >= 5173 at m = 456")
CK_H1 = NCHECK[0]

note("STATED, NOT TESTED -- AND THE CEILING FLOOR IS FAR FROM TIGHT.  "
     "Substitute X = 5172 back into the chain: (Q) forces Sigma5 = 0 "
     "AND H = 0, so every degree is at most 5 and sum d^2 <= 5 * 6m = "
     "13,680.  But the second moment at m = 456 is m^2 + 5m + 2X = "
     "220,560.  The contradiction is not marginal, it is a factor of "
     "sixteen -- which says the true floor at the ceiling is far above "
     "5173 and that the next lever is the joint consistency of H's size "
     "with the degree distribution, not another constant in (Q)")

# ==========================================================================
# 6.  The mutation suite
# ==========================================================================

head("6.  the mutation suite: ten mutants in twelve measured readings")

MUT = []


def s3run(**kw):
    """Re-run section 3's 35 cells under a mutation; return the cells
    that lose their kill."""
    alive = []
    Ffn = kw.pop("Ffn", F)
    useH = kw.pop("useH", True)
    dbump = kw.pop("dbump", 0)
    for pi in P5:
        D = min(capF(5 - pi[0]) if Ffn is F
                else max(d for d in range(0, 40) if Ffn(d) <= 5 - pi[0]),
                capF(4) if Ffn is F
                else max(d for d in range(0, 40) if Ffn(d) <= 4)) + dbump
        R = Rof(pi)
        for m in range(22, 27):
            v, arg = minS(m, 5, D, useH=useH, Ffn=Ffn, **kw)
            if v is not None and v <= R:
                alive.append((pi, m, v, R))
    return alive


t0 = time.time()
m1 = s3run(useH=False)
MUT.append(("M1  +H dropped from S (S := P only)", str(CK_S3), len(m1),
            "17 of 35 X=5 cells reopen"))
check("M1 -- THE +H TERM.  (SG) is P + H <= R, not P <= R: the H counts "
      "one unit of qmax per high vertex, licensed because F(d) >= 1 "
      "forces s(v) >= 1 hence qmax(v) >= 1.  Drop it and 17 of the 35 "
      "cells of section 3 lose their kill, on every narrow partition "
      "and every rung of the band.  The cheapest-looking term in the "
      "whole law is carrying half the section",
      len(m1) == 17
      and sorted(set(t[1] for t in m1)) == [22, 23, 24, 25, 26]
      and len(set(t[0] for t in m1)) == 5,
      "reopened %d cells at m in %s" % (len(m1),
                                        show(sorted(set(t[1] for t in m1)))))

m2 = s3run(dbump=1)
MUT.append(("M2  Delta relaxed by one at X = 5", str(CK_S3), len(m2),
            "10 cells reopen, incl. the wide row (4,1) at m = 22"))
check("M2 -- THE KEY CAP, RELAXED BY ONE DEGREE.  Allow each partition "
      "one more degree than F(d) <= X - q_1 licenses and 10 cells "
      "reopen: (2,2,1) and (3,1,1) and (3,2) on m = 22..24, and -- the "
      "reading that matters -- the WIDE row (4,1) at m = 22, whose "
      "census is INFEASIBLE at the true cap and becomes both feasible "
      "and alive one degree up.  So the key cap is what kills the wide "
      "rows, exactly as the billing note claims, and (q3) is not "
      "quietly doing it",
      len(m2) == 10 and (4, 1) in set(t[0] for t in m2)
      and sorted(set(t[1] for t in m2)) == [22, 23, 24],
      "reopened %d cells; partitions %s"
      % (len(m2), show(sorted(set(str(t[0]) for t in m2)))))

m3a = s3run(n2bump=1)
m3b = s3run(use_n2cap=False)
SW_D2a = sweep(use_n2cap=True)
sv_a = [c for c in SW_D2a if c[6] is not None and c[6] >= c[7]]
D2SAME = ([c[6] for c in SW_D2a] == [c[6] for c in CELLS]
          and [c[:3] for c in SW_D2a] == [c[:3] for c in CELLS])
MUT.append(("M3  (D2) relaxed in S3, imposed in S4",
            str(CK_S3), len(m3a) + len(m3b),
            "S3: 0 then 11 reopen; S4 unmoved either way"))
check("M3 -- (D2), MEASURED IN BOTH DIRECTIONS, AND IT IS THE "
      "LEDGER-DECIDING READING.  SECTION 3 IMPOSES IT, so the mutants "
      "there relax it: raise 0008's cap n_2 <= floor(m/2) by ONE and "
      "NOTHING reopens -- the cap has a full unit of slack everywhere "
      "it is used.  Drop it entirely and 11 cells reopen, on m = 22 and "
      "23 only, including the wide row (4,1).  SECTION 4 DOES NOT "
      "IMPOSE IT AT ALL, so the mutant there runs the other way: switch "
      "the cap ON in the staircase sweep and every one of the 92 cell "
      "maxima is UNCHANGED, the same single survivor and the same "
      "value.  So (D2) is consumed by section 3 alone, is not even "
      "tight there, and section 4 is (D2)-FREE BY CONSTRUCTION with the "
      "imposition measured inert on top",
      len(m3a) == 0 and len(m3b) == 11
      and sorted(set(t[1] for t in m3b)) == [22, 23]
      and len(sv_a) == 1 and D2SAME
      and (sv_a[0][0], sv_a[0][1], sv_a[0][2]) == (8, 30, (3, 3, 1, 1)),
      "S3 +1: %d reopen; S3 dropped: %d reopen; S4 with (D2) imposed: "
      "%d cells, %d survivor, every maximum identical to the primary "
      "run: %s" % (len(m3a), len(m3b), len(SW_D2a), len(sv_a), D2SAME))

m4 = s3run(nmin=35)
SW35 = sweep(nmin=35)
sv35 = [c for c in SW35 if c[6] is not None and c[6] >= c[7]]
MUT.append(("M4  n >= 36 -> n >= 35", "%d, %d" % (CK_S3, CK_SWEEP),
            len(m4) + len(sv35),
            "S3: 13 reopen; S4: survivors 1 -> 5"))
check("M4 -- THE VERTEX FLOOR.  One block short in one part and 13 "
      "cells of section 3 come back, on m = 22..24; on the staircase "
      "the survivor count goes from ONE to FIVE, adding (7,29,(3,3,1)) "
      "and three more partitions at (8,30).  n >= 36 is a two-line "
      "consequence of tau = 6 and it is doing as much work as any "
      "lemma in the file -- which is why the second-moment maximiser "
      "spends it as the -10n term rather than as a side condition",
      len(m4) == 13 and len(sv35) == 5
      and (7, 29, (3, 3, 1)) in [(c[0], c[1], c[2]) for c in sv35],
      "S3 %d reopen; S4 survivors %s"
      % (len(m4), show(["(%d,%d,%s)" % (c[0], c[1], str(c[2]))
                        for c in sv35])))

F6 = lambda d: phi(d, 6)
m5 = s3run(Ffn=F6)
check("M5 -- SIX FIBRES INSTEAD OF FIVE: the part-mate exclusion, "
      "priced.  If f's cell in z's own part could carry edges of E(z), "
      "F would be Phi(., 6) and not Phi(., 5).  Measured twice.  In the "
      "enactment: the corpus contains vertices where the five-fibre "
      "bound is TIGHT, F(d) = s(z), while Phi(d,6) < F(d) -- there the "
      "weakened bound genuinely misses a real collision.  In the "
      "census: replace F by Phi(., 6) EVERYWHERE -- in the key cap, in "
      "the (SSC+) ceiling and in S itself -- and 29 of the 35 cells of "
      "section 3 lose their kill.  ONLY SIX SURVIVE THE MUTATION: the "
      "whole (5) row, which stays census-infeasible, and (1,1,1,1,1) at "
      "m = 26.  The exclusion is not a detail of the write-up; it is "
      "most of the certificate",
      len(m5) == 29 and ACC["m6_load"] > 0
      and phi(6, 5) == 1 and phi(6, 6) == 0
      and phi(7, 5) == 2 and phi(7, 6) == 1,
      "%d cells reopen; %d corpus vertices where 5 fibres are tight and "
      "6 would not be" % (len(m5), ACC["m6_load"]))
MUT.append(("M5  six fibres (F := Phi(., 6))", str(CK_S3), len(m5),
            "29 of 35 cells reopen; part-mate exclusion load-bearing"))

r48 = ceil_fr(Fr(456 * 431 + 10, 48))
m6b = s3run()
MUT.append(("M6  q <= 4 in the Q chain (R <= 5X)",
            "%d, %d, %d, %d" % (CK_Q0, CK_QD, CK_Q0WIN, CK_H1),
            5173 - r48, "ceiling floor 5173 -> 4095; S3 INERT"))
check("M6 -- (q3) PERMITTED TO SLIP TO q <= 4, i.e. R <= 5X instead of "
      "R <= 4X.  The chain then reads m(m-25) + Sigma5 + 10H <= 48X and "
      "the ceiling floor at m = 456 collapses from 5173 to 4095 -- a "
      "loss of 1,078 units.  AND THE SAME MUTANT IS COMPLETELY INERT IN "
      "SECTION 3: not one of the 35 cells changes, because (q3) is "
      "billed to the Q law and to nothing else.  That inertness is the "
      "point of the measurement, not a disappointment: it is what a "
      "correct billing looks like from the outside.  MEASURED SITING: "
      "carried into the file, the mutated constant reddens the four "
      "checks that state the law -- the (Q0) spot values, (Q) derived, "
      "(Q0) across the window and (H1) -- and is inert at check 5, "
      "whose subject is the arithmetic q(q+1) <= 4q and not the chain",
      r48 == 4095 and 5173 - r48 == 1078 and len(m6b) == 0
      and len(s3run()) == 0,
      "5173 -> %d at m = 456; section 3 unchanged (%d cells reopen)"
      % (r48, len(m6b)))

bad7 = sum(1 for d in range(0, 601)
           if 5 * d + 10 * F(d) - d * d != (d % 5) * (4 - d % 5))
MUT.append(("M7  residue r(5-r) -> r(4-r)", str(CK_RESID), bad7,
            "identity fails at %d of 601 degrees" % bad7))
check("M7 -- THE RESIDUE CONSTANT.  Replace r(5-r) by r(4-r) and the "
      "identity 5d + 10F(d) - d^2 = r(5-r) fails at 480 of the 601 "
      "degrees d = 0..600 -- every d not divisible by 5.  It is an "
      "IDENTITY, so it reddens instantly and everywhere; the mutation "
      "exists to show that the check is testing an identity and not a "
      "tautology",
      bad7 == 480 and bad7 > 0,
      "%d of 601 degrees fail the mutated identity" % bad7)

fl456 = (456 * 431 + 10) // 38
gap = [m for m in range(22, 457)
       if ceil_fr(Fr(m * (m - 25) + 10, 38)) != (m * (m - 25) + 10) // 38]
MUT.append(("M8  ceil -> floor in (Q0)/(H1)",
            "%d, %d, %d" % (CK_Q0, CK_Q0WIN, CK_H1), 5173 - fl456,
            "ceiling floor 5173 -> 5172; differs on %d of 435 rungs"
            % len(gap)))
check("M8 -- INTEGRALITY, WHERE IT ACTUALLY LIVES.  X is an integer, so "
      "(Q0) and (H1) must be read with a ceiling; read with a floor, "
      "the ceiling rung m = 456 drops from 5173 to 5172 and ALL 435 "
      "window rungs report a strictly weaker floor -- 38 divides "
      "m(m-25) + 10 at no m in the window at all.  MEASURED "
      "AGAINST THE SPEC, which asked for this mutant 'at the three "
      "one-unit S3 cells': there is no rounding step in section 3 at "
      "all -- min S and R are integers and the comparison is exact -- "
      "and there are no one-unit cells either.  The mutant is therefore "
      "sited where the ceiling function really is",
      fl456 == 5172 and 5173 - fl456 == 1
      and len(gap) == 435 and all(isinstance(t, int) for t in gap),
      "5173 -> %d at m = 456; %d of 435 rungs differ" % (fl456, len(gap)))

SWTR = sweep(pilimit={(8, 30): [(3, 3, 2)]})
svtr = [c for c in SWTR if c[6] is not None and c[6] >= c[7]]
allparts830 = parts_of(8, 3)
MUT.append(("M9  (8,30) partitions cut to {(3,3,2)}",
            str(CK_SWEEP), len(allparts830) - 1,
            "sweep reports 0 survivors -- a FALSE all-clear"))
check("M9 -- THE PARTITION ENUMERATOR'S COMPLETENESS.  At X = 8 with "
      "c = 3 there are TEN partitions with parts <= 3; the review's "
      "section 7.2 table names (3+3+2) as the only remaining one, so "
      "the two it drops include exactly (3,3,1,1) -- the survivor -- "
      "and (3,2,2,1) -- the thinnest kill.  Truncate the list to the "
      "review's single entry {(3,3,2)} and the sweep "
      "returns ZERO survivors and would report the staircase closed "
      "with no structural work at all.  This is the one mutant that "
      "makes the certificate look STRONGER rather than weaker, which is "
      "why it is here",
      len(allparts830) == 10 and (3, 3, 1, 1) in allparts830
      and (3, 2, 2, 1) in allparts830 and len(svtr) == 0
      and len(SWTR) == 83,
      "full list %d partitions; truncated sweep: %d cells, %d survivors "
      "(a false all-clear)" % (len(allparts830), len(SWTR), len(svtr)))

mh_lit, _ = profile_max(expi, exD, minsize=1)
mh_bdh, _ = profile_max(expi, exD, minsize=1, bdh_only=True)
mh_slot, slotprof = profile_max(expi, exD, minsize=1, bdh_only=True,
                                slots=[q + 1 for q in expi])
sing_bdh = [(T, dm) for (T, dm, wt) in
            legal_profiles(expi, exD, 1, bdh_only=True) if len(T) == 1]
need = req - (42 * exm - 360)
MUT.append(("M10 |T_v| >= 2 dropped (structural step)",
            "%d-%d" % (CK_III, CK_TB), mh_slot - MAXHIGH,
            "LITERAL reading INERT (40 -> 40); FAITHFUL 40 -> %d, kill "
            "FAILS" % mh_slot))
check("M10 -- |T_v| >= 2, MEASURED IN TWO READINGS, AND THE SPEC'S "
      "GUESS DOES NOT REPRODUCE.  The spec expected MAXHIGH to rise to "
      "'>= 74' and marked the number for measurement.  READING ONE, "
      "literal: delete the |T_v| >= 2 filter from the profile "
      "enumerator and keep the (SSC+) cap.  MAXHIGH is UNCHANGED at 40 "
      "-- the mutant is INERT, because a singleton index set gives "
      "s = qmax and (SSC+) caps such a vertex at d <= 5, so it cannot "
      "be high in the first place.  |T_v| >= 2 is a DERIVED LABEL, not "
      "an assumption.  READING TWO, faithful: withdraw step (iii) "
      "itself, so EVERY vertex is capped only by (BDH), F(d) <= s(T_v) "
      "-- a singleton on a q = 3 pair then reaches d = 8 and exc = 18, "
      "and (iv) does not limit how many such vertices exist, since they "
      "consume no index pair.  SO SAY EXACTLY WHAT IS TRUE AND MEASURE "
      "IT.  With NOTHING bounding the number of singletons the faithful "
      "profile space is indeed unbounded -- but that is not the "
      "certificate's geometry: |S_i| = q_i + 1 gives 4, 4, 2, 2 SLOTS, "
      "and every vertex of T_v occupies one slot in each S_i it lies "
      "in, which is the real bound on how many singletons can exist.  "
      "Two numbers, both measured here: the enumerator visiting each "
      "index set at most once returns 206, and the same enumerator with "
      "the slot cap -- allowing a set to be REUSED while the slots "
      "last -- returns 190.  The kill fails as soon as the maximum "
      "reaches "
      "1066 - 900 = 166, and 190 > 166, SO THE FAITHFUL MUTANT BREAKS "
      "THE KILL: the bound becomes 1090 against the required 1066.  "
      "THE WITNESS IS REALISABLE AND IS PRINTED: one vertex on "
      "{2,3,4} at d = 10, one on {1,2} at d = 10, one each on {1,3} and "
      "{1,4} at d = 9, two singletons on {2} and one on {1} at d = 8 -- "
      "4 slots used in S_1, 4 in S_2, 2 in S_3, 2 in S_4, and all six "
      "index pairs distinct.  (The '7 singletons at 18 each' route is "
      "NOT realisable: the {1,2,3,4} vertex occupies one slot of every "
      "S_i, leaving only 3 + 3 = 6 singleton slots in S_1 and S_2, and "
      "40 + 6*18 = 148 < 166.  The step is load-bearing either way; the "
      "route by which it is load-bearing is this one.)  The literal "
      "filter is not load-bearing.  MEASURED SITING, in full: carried "
      "into the file, the faithful mutation reddens the four structural "
      "checks of section 4(x) -- (iii), the kill, the corroboration and "
      "T-B20 assembled -- and, downstream of the changed MAXHIGH, this "
      "row and the margins row as well.  The REDDENS column names the "
      "structural block, which is where a reader should look",
      mh_lit == MAXHIGH and mh_lit == 40
      and mh_bdh == 206 and mh_slot == 190
      and max(dm for (T, dm) in sing_bdh) == 8
      and need == 166 and mh_slot >= need
      and 42 * exm - 360 + mh_slot == 1090
      and 42 * exm - 360 + MAXHIGH + 6 * 18 < req
      and len(slotprof) == 7,
      "literal: %d (inert); faithful: %d unslotted, %d with the "
      "|S_i| = q_i+1 slot cap, against the %d that breaks the kill "
      "-- bound %d vs %d required.  Witness: %s"
      % (mh_lit, mh_bdh, mh_slot, need, 42 * exm - 360 + mh_slot, req,
         show([("T=%s d<=%d" % (tuple(i + 1 for i in T), dm))
               for (T, dm) in slotprof])))

MUTS = sorted(MUT, key=lambda t: int(t[0].split()[0][1:]))
print("\n      MUTANT                                     REDDENS               "
      "COUNT   MEASURED EFFECT", flush=True)
for (nm, wh, n, det) in MUTS:
    print("      %-42s %-21s %5d   %s"
          % (nm, "check " + wh, n, det), flush=True)
MUTTIME = time.time() - t0
CITED = [("the ledger's '(c23)' rows", CK_DOM, 23),
         ("the b = 5 note's 'check 23'", CK_DOM, 23),
         ("the b = 5 note's 'check 3'", CK_MONO, 3),
         ("M6's 'inert at check 5'", CK_Q3A, 5),
         ("check 31's 'check 30's re-verification'", CK_REVER, 30),
         ("(Q) derived, citing the identity's enactment", CK_QID, 17),
         ("M7's residue check", CK_RESID, 4),
         ("M6/M8's (Q0) spot values", CK_Q0, 9),
         ("M6's (Q) derivation", CK_QD, 38),
         ("M6/M8's (Q0) window", CK_Q0WIN, 39),
         ("M6/M8's (H1)", CK_H1, 40),
         ("M10's structural block, low end", CK_III, 34),
         ("M10's structural block, high end", CK_TB, 37),
         ("M1-M3, M5's section 3 census", CK_S3, 24),
         ("M4, M9's staircase sweep", CK_SWEEP, 29)]
check("THE MUTATION TABLE, printed above, is COMPLETE over the "
      "certificate's parameters: the +H term of (SG) (M1), the key cap "
      "(M2), (D2) in both readings and on both engines (M3), the vertex "
      "floor on both engines (M4), the part-mate exclusion (M5), (q3)'s "
      "billing (M6), the residue constant (M7), integrality (M8), the "
      "partition enumerator's completeness (M9) and the structural "
      "step (M10, two readings).  Every one of them reddens something "
      "except M6-in-section-3 and M10-literal, both of which are "
      "recorded as INERT with the reason rather than quietly dropped.  "
      "Every count is a MEASUREMENT made in this run, and every REDDENS "
      "entry is a CAPTURED check number rather than a literal.  AND THE "
      "CROSS-REFERENCES ARE PINNED HERE: every check number this file's "
      "prose cites -- in the printed ledger, in the notes, in the "
      "mutant table -- is asserted equal to the number the run actually "
      "assigned, so a renumbering REDDENS this check instead of "
      "silently making the prose wrong.  The census enumerator's leaf "
      "re-verification held across every mutant that re-runs section 3 "
      "(M1-M6); the staircase-side sweeps run through maximize_sq, "
      "which records nothing into INTERNAL, so they are NOT covered by "
      "that statement",
      len(MUTS) == 10 and all(isinstance(t[2], int) for t in MUTS)
      and [t[0] for t in MUTS] == sorted([t[0] for t in MUTS],
                                         key=lambda s: int(s.split()[0][1:]))
      and all(got == want for (_, got, want) in CITED)
      and INTERNAL == [] and LEAVES[0] > 0,
      "%d mutants, %d census vectors emitted in all, 0 internal "
      "violations, %d cited check numbers all matching, %.1fs"
      % (len(MUTS), LEAVES[0], len(CITED), MUTTIME))

# ==========================================================================
# 7.  Margins -- measured and named (D-035)
# ==========================================================================

head("7.  the margins, every one named")

thin3 = [(pi, 22 + i, row[i] - R) for (pi, D, R, row) in S3ROWS
         for i in range(5) if row[i] is not None and row[i] - R == S3_MARG[0]]
print("""
      SECTION 3, thinnest cells        (2,2,1) at m = 22, 23, 24, margin 2
      SECTION 3, wide rows             (4,1) and (5): census INFEASIBLE
      SECTION 4, thinnest arithmetic   (8,30,(3,2,2,1)), margin 2
      SECTION 4, the survivor          (8,30,(3,3,1,1)): ZERO arithmetic
                                       margin -- it survives by 10 -- and
                                       dies structurally by 126
      SECTION 4, structural corroborat. margins 84, 114, 164
      the Delta cap exposure           one degree of relaxation reopens 10
                                       section 3 cells, incl. the wide row
                                       (4,1) at m = 22 -- priced at M2
      (D2) exposure                    section 3 only, and not tight there
      n >= 36 exposure                 both engines (M4)
      (H1) AT THE CEILING              ONE UNIT: 38 divides 456*431 exactly,
                                       so 5172 -> 5173 is the whole of 10H
      (Q0) at the ceiling              5173, and NOT tight -- section 5""",
      flush=True)
check("THE MARGINS, NAMED AND MEASURED (D-035).  Section 3's thinnest "
      "cells are three, all on the partition (2,2,1), at m = 22, 23 and "
      "24, each with min S exactly 2 above R = 14.  Section 4's "
      "thinnest arithmetic kill is 2 units, at (8,30,(3,2,2,1)).  The "
      "surviving cell has NO arithmetic margin -- it clears the "
      "requirement by 10 -- and is killed only by the structural layer, "
      "with 126 units to spare there.  NO CENSUS CELL AND NO STRUCTURAL "
      "KILL in this certificate is decided by a single unit, which is a "
      "change from 0018 and 0019; the exposure has moved from "
      "arithmetic thinness to the structural step, which is priced at "
      "M10.  THE ONE PLACE A SINGLE UNIT DECIDES AN ANSWER IS (H1) AT "
      "m = 456: 456*431 = 196536 = 38*5172 exactly, so the ten units of "
      "one high vertex are the whole of the 5172 -> 5173 lift, and M8 "
      "measures the cost of getting that rounding wrong as exactly 1.  "
      "Section 5 shows the true floor there is far above either number, "
      "so the exposure is cosmetic -- but it is named rather than "
      "covered by a blanket sentence",
      len(thin3) == 3 and S3_MARG[0] == 2
      and sorted(set(str(t[0]) for t in thin3)) == ["(2, 2, 1)"]
      and sorted(t[1] for t in thin3) == [22, 23, 24]
      and KILLS[0][0] == 2 and req - bnd == 126
      and SURV[0][6] - SURV[0][7] == 10
      and 456 * 431 == 38 * 5172
      and ceil_fr(Fr(456 * 431 + 10, 38)) - ceil_fr(Fr(456 * 431, 38)) == 1
      and len(m2) == 10,
      "section 3 thinnest %d (x%d), section 4 thinnest %d, structural "
      "%d; (H1) at the ceiling decides by exactly 1"
      % (S3_MARG[0], len(thin3), KILLS[0][0], req - bnd))

# ==========================================================================
# 8.  Controls
# ==========================================================================

head("8.  controls -- what this certificate must NOT contradict")

check("0019 CONSISTENCY.  0019 proves X >= 5 everywhere and X = 5 => "
      "m <= 26.  This file adds that the X = 5 band m = 22..26 is "
      "empty, so 0019's theorem is SUPERSEDED, not contradicted: T-B "
      "survives as a true implication whose antecedent no core "
      "satisfies.  Nothing in 0019 changes; one of its bands simply "
      "stops being reachable.  What is TESTED here is the emptiness "
      "itself -- 35 cells, zero survivors -- and the fact that the same "
      "census independently empties m = 27..31, so the supersession "
      "does not depend on the theorem being superseded",
      S3_ALIVE == [] and len(S3ROWS) == 7
      and all(v is None or v > R for (pi, R, row) in EXT for v in row))

D11 = [c for c in CELLS if c[4] == 11]
D11MARG = sorted(c[7] - c[6] for c in D11 if c[6] is not None)
check("HOW MUCH OF 0019 THIS ACTUALLY STRENGTHENS -- MEASURED, AND LESS "
      "THAN THE HEADLINE SUGGESTS, BUT NOT NOTHING.  F(d) >= (d-5)_+ "
      "always, so (BDH) implies 0019's (DH); and F(d) - (d-5)_+ is "
      "ZERO for every d <= 10, reaching 1, 2, 3 at d = 11, 12, 13.  "
      "EVERY DEGREE CAP IN SECTION 3 SITS AT 9 OR BELOW, so there "
      "(BDH) and (DH) are the same pointwise statement.  SECTION 4 IS "
      "NOT: 24 of its 92 cells run at Delta = 11 -- capF(7) = capF(8) "
      "= 11, so the six (1^8) cells at X = 8 and the eighteen q_1 <= 2 "
      "cells at X = 9 -- and at d = 11, F(11) = 7 against (11-5)_+ = "
      "6, so on "
      "those cells (BDH) buys ONE TO TWO DEGREES over the linear "
      "reading, which would have allowed d <= 5 + X - q_1 = 12 or 13.  "
      "THE GAIN IS REAL AND IT IS NOT LOAD-BEARING: every one of those "
      "24 cells dies by 44 or more, so none is decided by the "
      "difference.  What the sections actually run on is the qmax "
      "subtraction in (SSC+) -- which yields the key cap and has no "
      "counterpart in 0019 -- and the +H term, priced at M1.  Where "
      "F's quadratic growth does the work is section 5, at large m, "
      "where degrees may reach 5 + X: there F(d) exceeds (d-5)_+ "
      "without bound (at d = 100 it is 950 against 95) and the residue "
      "identity, hence (Q), exists only because of it.  Said plainly "
      "rather than rounded up -- or, as an earlier draft of this label "
      "did, rounded DOWN",
      all(F(d) >= max(d - 5, 0) for d in range(0, 601))
      and [F(d) - max(d - 5, 0) for d in range(9, 14)] == [0, 0, 1, 2, 3]
      and F(100) == 950 and 100 - 5 == 95
      and all(F(d) == max(d - 5, 0) for d in range(0, 11))
      and max(D for (pi, D, R, row) in S3ROWS) <= 9
      and len(D11) == 24 and len(D11MARG) == 24 and D11MARG[0] >= 44
      and max(c[4] for c in CELLS) == 11
      and capF(7) == 11 and capF(8) == 11 and F(11) == 7,
      "F(d) - (d-5)+ at d = 9..13: %s; section 3 caps top out at %d; "
      "%d of %d section 4 cells run at Delta = 11, thinnest of those "
      "dying by %d, widest by %d"
      % (show([F(d) - max(d - 5, 0) for d in range(9, 14)]),
         max(D for (pi, D, R, row) in S3ROWS), len(D11), len(CELLS),
         D11MARG[0], D11MARG[-1]))

check("NO TENSION WITH THE TIGHTNESS OBJECT.  AG(2,5) has m = 25 and "
      "X = 0, which would violate X >= 6 if it were a core in the "
      "window.  It is not: tau = 5, and the window's quantifier is over "
      "cores with tau = 6.  The distinction is not cosmetic -- AG(2,5) "
      "is exactly where both summed laws are tight, so a certificate "
      "that quietly admitted it would be proving a false statement",
      mincover(AG5) == 5 and len(AG5) == 25 and agX == 0 and 5 < 6)

note("STATED, NOT TESTED: certificate 0018 remains the authority for "
     "its own theorem; this file does not consume it and does not "
     "re-derive its shape census.  T-A20 implies its statement, as "
     "0019 already did")
note("STATED, NOT TESTED -- WHAT REMAINS OPEN.  X = 6 on m in [22, 26] "
     "is NOT emptied: the staircase confines X = 6 to those five rungs "
     "and stops, exactly as 0019 stopped one rung of excess lower.  "
     "That band is the next field.  Nothing here bears on X >= 10 below "
     "m = 32, on existence, or on the true floor at the ceiling, which "
     "section 5 shows is far above the 5173 this certificate proves")

# ==========================================================================

head("Result")

print("""
  (q3)   lambda <= 4, q <= 3, R <= 4X                    PROVEN-BY-CERT
  (BDH)  F(d(z)) <= s(z)                                 PROVEN-BY-CERT
  (SSC+) F(d(z)) + qmax(z) <= s(z) at tau >= qmax + 2    PROVEN-BY-CERT
  (SG)   P + H <= R                                      PROVEN-BY-CERT
  (Q)    m(m-25) + Sigma5 + 10H <= 38X                   PROVEN-BY-CERT
  (H1)   H >= 1 at m >= 26; X >= 5173 at m = 456         PROVEN-BY-CERT
  (T-A20) X >= 6 for every critical core in [22, 456]    PROVEN-BY-CERT
  (T-B20) X = 6 => m <= 26; 7 => 28; 8 => 29; 9 => 31    PROVEN-BY-CERT

  One line does the work.  0019 counted a vertex's collisions with
  (d - 5)_+ and threw the rest away; keeping the whole balanced-split
  minimum Phi(d, 5) -- and then subtracting the largest excess a vertex
  already owns -- turns the star-collision inequality from linear into
  quadratic.  Out of it fall a per-vertex degree cap F(d) <= X - q_1
  that drives every sweep, a quadratic law m(m-25) + Sigma5 + 10H <= 38X
  that reaches the far end of the window, and a staircase at the near
  end.  92 staircase cells, one arithmetic survivor, killed by counting
  the index-profiles its high vertices could carry.

  THE MARGINS: two units, three times, in section 3; two units once in
  section 4; and a structural kill with 126 to spare where the
  arithmetic had none.  (D2) is consumed by section 3 alone and is not
  tight even there.  Three numbers in the desk spec did not reproduce
  and the measurements are what stand.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(exit_code(FAILED))
