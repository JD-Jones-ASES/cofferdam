#!/usr/bin/env python3
"""Certificate 0017 -- the excess-growth laws: the corner ladder, the
linear law, and the second-moment law.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from
lib/.  Runs under Python 3.9 and under python3 -O.  Deterministic.
NO m = 22 FIELD SCAN ANYWHERE: every claim here is window-wide.

WHAT IS CLAIMED
---------------
  (C1) THE CORNER LADDER.                            PROVEN-BY-CERTIFICATE
      For a pair {f,g} inside K - e with s = |f cap g|,     (in-house:
      a = |f cap g cap e|, b = |f cap g cap T_e|, the        0013 covers,
      excess accounting gives X >= 2(a-1) + (s-1) for        0015 steps
      a >= 2 -- three DISTINCT pairs {e,f}, {e,g}, {f,g},    (2)-(3),
      no double count (0016's (T), generalized off a = 2).   0016 (T);
      Exhaustively over a + b <= s:                          external
          a*b <=       s-1   whenever X <= 4                 NONE)
          a*b <= (4/3)(s-1)  whenever X <= 5
          a*b <= (3/2)(s-1)  always, for s <= 5   (0015)
      Hence (CC4+):  sum_i Phi(d_i - 1, 5 - b_i) <= I_e <= X - x_e
      for every edge of a critical core with X <= 4.

  (C2) THE UNCONDITIONAL PAIR-SUM.  For ANY X:       PROVEN-BY-CERTIFICATE
          sum_e I_e <= sum over excessive pairs of
                       (lambda - 1) * sum_{u in f cap g} (deg u - 2)
      with NO hypothesis on a_e.  Supersedes the a_e <= 1
      hypothesis of certificate 0016 section 6.

  (C3) THE LINEAR LAW, PER EDGE.                     PROVEN-BY-CERTIFICATE
          2m + 5*x_e <= 52 + 3X
      for EVERY edge of EVERY critical core, at every m.

  (C4) THE LINEAR LAW, GLOBAL, WITH THE             PROVEN-BY-CERTIFICATE
      INTEGRALITY LIFT.
          X >= 2m(m - 26)/(3m - 10),  and, since x_e is a
          non-negative INTEGER,  2X <= m*floor((52 + 3X - 2m)/5).

  (C5) THE COUPLING.  X <= 2 => m <= 26 (from C4     PROVEN-BY-CERTIFICATE
      alone).  X <= 4 => m <= 28 (from C4 AND C1's c = 1
      corner -- C4 alone admits (m, X) = (29, 4)).

  (C6) (G) THE SECOND-MOMENT LAW.                    PROVEN-BY-CERTIFICATE
          2 * (6m * psihat(mu))  <=  3(m - 2) X,
      psi(d) := Phi(d-1, 5), psihat its piecewise-linear
      interpolation, mu = (m^2 + 5m + 2X)/(6m) the mean over
      the 6m incidence slots.  Quadratic where C3/C4 are linear:
      X >= 2259 at m = 456, against C4's 290.

  (C7) THE COMBINED WINDOW PROFILE.                  PROVEN-BY-CERTIFICATE
      max(0016 at m = 22, the C4 lift, (G)) forces X >= 1 on 431 of
      the 435 integers m in [22, 456] -- all but 23, 24, 25, 26.

NOTATION.  K is an edge-critical counterexample core to Ryser r = 6
intersecting: finite, 6-partite (V_1..V_6), 6-uniform, intersecting,
tau(K) = t, t = 6 for Ryser r = 6.  lambda(f,g) = |f cap g| >= 1.
X = sum_v C(deg v, 2) - C(m, 2) = sum over pairs of (lambda - 1).
x_e = sum_{f != e} (lambda(e,f) - 1) >= 0, and sum_e x_e = 2X.
For e's private minimum (t-1)-cover T_e (certificate 0013:
T_e cap e = empty, T_e inside V(K), T_e covers K - e): d_i = deg of
e's part-i vertex, b_i = |T_e cap V_i|, sum_i b_i = t - 1 = sigma.
Phi(n, k) = the balanced-split minimum of sum C(n_j, 2) over k classes
totalling n.  psi(d) := Phi(d - 1, 5), the cover-free per-vertex
weight, DERIVED FROM Phi throughout and never tabulated by hand.
Theta := 5*sigma + 1 = 5t - 4, the threshold constant: 26 at t = 6,
21 at t = 5.  I_e = sum over pairs {f,g} inside K - e of a*b.

THE PROOF, IN ORDER
-------------------
 (1) THE RELAXATION.  C(j,2) >= j - 1 for every integer j >= 0, so any
     split of n into k >= 1 classes has sum_j C(n_j,2) >= n - k, i.e.
     Phi(n,k) >= n - k, and Phi >= 0 makes it unconditional when n < k.
     Section 1 exhausts this and shows the floor is ATTAINED, so n - k
     is the exact linear floor of Phi, not a slack bound.

 (2) THE PER-EDGE LINEAR LAW (C3).  With sum_i b_i = 5,
         sum_i [ (d_i - 1) - (5 - b_i) ] = sum_i d_i - 31,
     and sum_i d_i = m + 5 + x_e (6-uniform counting, 0015 Lemma 1.2),
     so sum_i Phi(d_i - 1, 5 - b_i) >= m + x_e - 26.  Chain with plain
     (CC) of 0015, sum_i Phi <= I_e <= (3/2)(X - x_e):
         m + x_e - 26 <= (3/2)(X - x_e)   <=>   2m + 5x_e <= 52 + 3X.
     THE b_i = 5 BRANCH IS CLOSED BY COVERING ALONE (0015 step (1)):
     five cover cells in part i leave the d_i - 1 siblings through v_i
     no cell to hit, forcing d_i = 1, and the term reads 0 >= 0.  It is
     NOT closed by lemma (A) of 0005 -- the law never invokes (A).
     Section 4 exhibits the 9,015 states where the step would FAIL if
     that branch were left open, worst gap 9.

 (3) THE SUMMED LAW AND THE LIFT (C4).  Summing over the m edges with
     sum_e x_e = 2X gives m(m - 26) <= X*((3/2)(m-2) - 2), i.e.
     X >= 2m(m-26)/(3m-10).  But x_e is a non-negative INTEGER, so
     x_e <= floor((52 + 3X - 2m)/5) =: B and 2X <= m*B, which is
     strictly stronger at every calibration point.

 (4) THE CORNER LADDER (C1).  A triple e, f, g with a = |e cap f cap g|
     >= 2 forces lambda(e,f) >= a, lambda(e,g) >= a, lambda(f,g) = s,
     over three DISTINCT pairs, so X >= 2(a-1) + (s-1).  Pricing every
     (a,b,s) with a + b <= s by that forced excess, the corner constant
     is 1 at X <= 4, 4/3 at X = 5, and 3/2 always (s <= 5).

 (5) (G), THE SECOND-MOMENT LAW (C6).  The 6m incidence slots (e,i)
     carry d_i(e); a vertex v occupies exactly deg(v) slots each
     carrying deg(v), so the slot-total is sum_v deg(v)^2, which the
     pair identity sum_v C(deg,2) = C(m,2) + X turns into
     m^2 + 5m + 2X.  psi is convex (increments floor((d-1)/5)), so
     Jensen against the piecewise-linear psihat at the rational mean
     bounds W = sum_v deg(v) psi(deg v) from below; plain (CC) summed
     bounds it from above by (3/2)(m-2)X.

MANDATORY HONESTY NOTES
-----------------------
 (1) THE CORNER GENUINELY DIES AT X = 5, AND WHAT DIES IS THE MIDDLE
     STEP.  Section 2 exhibits the repaired witness (T_e inside V(K))
     with X = 5, (a,b,s) = (2,2,4), I_e = 4 > X - x_e = 3 while plain
     (CC) survives (8 <= 9).  But its LEFT side sum_i Phi is ZERO, so
     the END-TO-END conclusion sum_i Phi <= X - x_e reads 0 <= 3 and
     HOLDS on it.  WHETHER (CC+)'s END-TO-END CONCLUSION SURVIVES AT
     X = 5 IS OPEN.  A 120,000-trial hunt by the phase-2 refuter found
     no counterexample AND zero enactments with a positive left side --
     no evidence either way.  This certificate claims the c = 1 corner
     at X <= 4, the 4/3 PER-PAIR corner AT X = 5 (check 9), and flags
     the constant-one end-to-end conclusion at X = 5 as open.
     (ERRATUM 2026-07-28: this sentence originally deflated C1's own
     4/3 rung; caught by the second outside audit.  Comment only.)

 (2) C2 IS A COMPLEMENT TO PLAIN (CC), NOT A STRENGTHENING.  Its
     per-pair coefficient sum_{u in f cap g}(deg u - 2) <= 5(Delta - 2)
     can EXCEED plain (CC)'s (3/2)(m - 2): at m = 22 with the pinned
     ladder's Delta <= 9 it is 35 against 30.  Measured in both
     directions in section 3.  Never quote it as dominating.

 (3) THE MARGIN (D-035) IS THE RELAXATION COORDINATE M2, NOT THE
     HEADLINE.  On the tau = 5 rehearsal core the Phi-vs-linear
     relaxation loses 7 units per edge, uniformly, and the per-edge law
     then clears by 14 = 2*7.  The control clears on relaxation slack:
     it tests that the law's DIRECTION is not reversed and nothing
     more.  Real objects pin the constant only within [28, 52]; 52
     rests on the DERIVATION, not on enactment.  Section 11.

 (4) ENACTMENT CANNOT PRICE (G) AT ALL.  Everything this lab can build
     has m <= 25, and (G) is vacuous below m = 32.  (G) ships as a
     chain of certified links with two rounding mutants and one index
     mutant as its teeth -- and its criticality tooth does not exist:
     section 10 shows the 25-edge truncated PG(2,5) violates the linear
     law by 8 units per edge while satisfying (G)_5 at margin exactly
     zero.  The criticality mutant is INVISIBLE to (G).

 (5) NEVER QUOTE m^2/90.  The asymptotic overstates at finite m:
     2310.4 against the true 2259 at m = 456.  It is a note, not a
     bound.

 (6) ADDENDUM, NOT ERRATUM, against certificate 0016 section 6.  0016
     derived the pair-sum under a_e <= 1, which at X <= 2 is true by
     (T).  That derivation is CORRECT; it is merely not minimal.  C2
     removes the hypothesis.  No 0016 check or condition changes.

THE LEDGER, in full
-------------------
  C1 corner ladder        EXTERNAL -- NONE.  In-house: 0013 (private
                          covers, T_e cap e = empty, T_e inside V(K)),
                          0015 steps (2)-(3), 0016's (T) generalized.
  C2 pair-sum             EXTERNAL -- NONE.  In-house: 0013 (3a) only.
  C3 per-edge law         EXTERNAL -- NONE.  In-house: 0013, 0015
                          steps (1)-(5) incl. plain (CC) and Lemma 1.2.
  C4 lift                 additionally: nothing.  Pure integrality.
  C5 coupling             C4 + C1's c = 1 corner.  The second rung is a
                          corollary of C1, NOT of C4 -- said in place.
  C6 (G)                  EXTERNAL -- NONE.  In-house: 0015's plain
                          (CC) global form; the two moment identities;
                          convexity of psi; Jensen.
  C7 profile              additionally: certificate 0016's X >= 3 at
                          m = 22, and hence TRANSITIVELY 0016's own
                          ledger (field 0005/0009/0012, (D2) 0008,
                          0015's X >= 2).  That single m = 22 entry is
                          the ONLY place this certificate touches a
                          field scan, and it touches it by citation.
  the tau = 5 sections    CONTROL-ONLY: they can redden this
                          certificate, never green it.

WHAT THIS DOES NOT CLAIM.  No core is claimed to exist -- every law
here is conditional on a critical core at that m.  At X = 5, nothing
beyond what C1-C3 state: the c = 1 corner fails (witness), the 4/3
per-pair corner HOLDS (check 9), C2/C3 carry no X restriction; open is
the constant-one end-to-end conclusion.  (ERRATUM 2026-07-28: comment
only; the original line deflated C1's 4/3 rung.)  The laws are VACUOUS
on m in [23, 26], which is exactly the band no certificate holds.
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


def phi(n, k):
    """Balanced-split minimum of sum C(n_j, 2) over k classes totalling n."""
    if n <= 0:
        return 0
    q, r = divmod(n, k)
    return r * comb(q + 1, 2) + (k - r) * comb(q, 2)


def psi(d):
    """The cover-free per-vertex weight Phi(d-1, 5).  DERIVED, never a
    hand table -- the phase-2 refuter caught a one-index shift in the
    desk's prompt, which inflates (G) at m = 456 from 2259 to 2323."""
    return phi(d - 1, 5)


def psi5(d):
    """The tau = 5 analog Phi(d-1, 4)."""
    return phi(d - 1, 4)


def show(seq):
    """Deterministic printable form of a collection."""
    return ", ".join(str(x) for x in seq)


def forced_excess(a, s):
    """The excess a triple with |e cap f cap g| = a and lambda(f,g) = s
    forces, by the generalized (T): three DISTINCT pairs, lambda(e,f)
    and lambda(e,g) both >= a, lambda(f,g) = s."""
    return 2 * max(a - 1, 0) + (s - 1)


def lam(e, f):
    return sum(1 for i in range(6) if e[i] == f[i])


class LCG(object):
    """The house LCG.  Deterministic; identical on every interpreter."""

    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFF

    def next(self):
        self.s = (25214903917 * self.s + 11) & 0xFFFFFFFFFFFF
        return self.s >> 16

    def below(self, k):
        return self.next() % k


# ==========================================================================
# 1.  Phi, psi, and the exact linear floor
# ==========================================================================

head("1.  Phi, psi, and the linear floor Phi(n,k) >= n-k")

ok_min = True
for n in range(0, 11):
    for k in range(1, 7):
        best = None
        for compo in itertools.product(range(n + 1), repeat=k):
            if sum(compo) == n:
                v = sum(comb(c, 2) for c in compo)
                if best is None or v < best:
                    best = v
        if best != phi(n, k):
            ok_min = False
check("Phi(n, k) equals the exhaustive minimum of sum C(n_j, 2) over ALL "
      "compositions of n into k classes, for every n <= 10 and every "
      "k <= 6 -- the closed form is the true minimum, not an ansatz",
      ok_min)

check("Phi is nonincreasing in the class count k for all n <= 200, "
      "1 <= k <= k' <= 12.  This is what licenses the relaxation "
      "Phi(d-1, 5-b_i) >= Phi(d-1, 5) = psi(d) used by (G), whatever "
      "the private cover does with its five cells",
      all(phi(n, k) >= phi(n, kk)
          for n in range(0, 201) for k in range(1, 13)
          for kk in range(k, 13)))

lin_bad = []
lin_eq = 0
lin_neg = 0
for n in range(0, 201):
    for k in range(1, 9):
        if phi(n, k) < n - k:
            lin_bad.append((n, k))
        if phi(n, k) == n - k:
            lin_eq += 1
        if n - k < 0:
            lin_neg += 1
check("THE RELAXATION, exhaustively: Phi(n,k) >= n - k for every n <= 200 "
      "and 1 <= k <= 8, including the 36 pairs with n - k < 0 where Phi = 0 "
      "beats a negative right side.  Its one-line proof is C(j,2) >= j-1 "
      "for every integer j >= 0, applied class by class.  The floor is "
      "ATTAINED 44 times in that range (first at (n,k) = (1,1)), so n - k "
      "is the EXACT linear floor of Phi -- sharpening it to n - k + 1 is "
      "false, and every unit the linear law loses to (G) is lost above "
      "this step, not at it",
      lin_bad == [] and lin_eq == 44 and lin_neg == 36)

PSI15 = [psi(d) for d in range(0, 15)]
check("psi PINNED BY INDEX, and DERIVED from Phi rather than tabulated: "
      "psi(0..14) = 0,0,0,0,0,0,0,1,2,3,4,5,7,9,11.  psi(6) = Phi(5,5) = 0 "
      "-- five singletons collide nowhere -- and psi(7) = Phi(6,5) = 1.  "
      "The one-index shift caught by the phase-2 refuter would read this "
      "row starting at d = 0; section 7 asserts what that mutant costs",
      PSI15 == [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 7, 9, 11]
      and psi(6) == phi(5, 5) and psi(6) == 0 and psi(7) == 1,
      "psi(0..14) = " + show(PSI15))

incr_ok = all(psi(d + 1) - psi(d) == (d - 1) // 5 for d in range(1, 401))
conv_ok = all(psi(d + 2) - psi(d + 1) >= psi(d + 1) - psi(d)
              for d in range(0, 400))
check("psi IS CONVEX, verified to d = 400: its increment is exactly "
      "psi(d+1) - psi(d) = floor((d-1)/5), which is nondecreasing.  "
      "Convexity is the whole licence for Jensen in (G), and it is "
      "checked as an increment comparison, not asserted",
      incr_ok and conv_ok)

gap = [d for d in range(0, 401) if psi(d) < d - 6]
first_strict = min(d for d in range(7, 401) if psi(d) > d - 6)
check("psi(d) >= d - 6 for every d <= 400 -- the linear law's relaxation "
      "read at b_i = 0 -- with the FIRST STRICT gap at d = 12 (psi = 7 "
      "against 6).  That is the exact degree at which the linear law of "
      "C3/C4 begins losing to (G), and it is why (G) overtakes it in the "
      "window rather than everywhere",
      gap == [] and first_strict == 12)

# ==========================================================================
# 2.  (C1) the corner ladder, and the X = 5 witness
# ==========================================================================

head("2.  (C1) the corner ladder -- c = 1 at X <= 4, 4/3 at X = 5, "
     "3/2 always")

PAT = []
for pat in itertools.product(range(5), repeat=6):
    lef = sum(1 for p in pat if p == 0 or p == 1)
    leg = sum(1 for p in pat if p == 0 or p == 2)
    lfg = sum(1 for p in pat if p == 0 or p == 3)
    a = sum(1 for p in pat if p == 0)
    PAT.append((a, lef, leg, lfg))
INTER = [r for r in PAT if min(r[1], r[2], r[3]) >= 1]
DIST = [r for r in INTER if r[1] != 6 and r[2] != 6 and r[3] != 6]
acc_bad = 0
acc_tight = 0
for (a, lef, leg, lfg) in DIST:
    if a >= 2:
        tot = (lef - 1) + (leg - 1) + (lfg - 1)
        if tot < forced_excess(a, lfg):
            acc_bad += 1
        if tot == forced_excess(a, lfg):
            acc_tight += 1
check("THE EXCESS ACCOUNTING, exhaustively over all 5^6 = 15,625 "
      "per-coordinate agreement patterns of a 6-partite triple (0016's "
      "(T), generalized off a = 2): on every intersecting pattern with "
      "e, f, g PAIRWISE DISTINCT and a = |e cap f cap g| >= 2, the "
      "three-pair total (lam(e,f)-1)+(lam(e,g)-1)+(lam(f,g)-1) is at "
      "least 2(a-1) + (s-1) with s = lam(f,g).  Zero failures, and the "
      "bound is attained, so the pricing is exact and not slack.  The "
      "three pairs are DISTINCT because e, f, g are, so nothing is "
      "double counted in X = sum over ALL pairs of (lambda-1)",
      len(PAT) == 15625 and acc_bad == 0 and acc_tight > 0,
      "tight on %d patterns" % acc_tight)

SMAX = 19
LADDER = []
for (cnum, cden, thr, name) in ((1, 1, 4, "c = 1"), (4, 3, 5, "c = 4/3"),
                                (3, 2, 10 ** 9, "c = 3/2")):
    viol = []
    for s in range(1, SMAX + 1):
        for a in range(0, s + 1):
            for b in range(0, s - a + 1):
                if cden * a * b > cnum * (s - 1):
                    viol.append((forced_excess(a, s), a, b, s))
    viol = sorted(viol)
    inside = [v for v in viol if v[0] <= thr]
    LADDER.append((name, viol, inside))

c1_viol = LADDER[0][1]
check("c = 1 IS VALID AT X <= 4, exhaustively over EVERY (a, b, s) with "
      "a + b <= s and 1 <= s <= 19: no state whose forced excess is at "
      "most 4 violates a*b <= s - 1.  The FIRST violator, by forced "
      "excess, is (a,b,s) = (2,2,4) and it forces EXACTLY 5.  It is the "
      "unique cheapest violator",
      LADDER[0][2] == [] and c1_viol[0] == (5, 2, 2, 4)
      and len([v for v in c1_viol if v[0] == 5]) == 1)

c43_viol = LADDER[1][1]
check("c = 4/3 IS VALID AT X <= 5: no state with forced excess <= 5 "
      "violates 3ab <= 4(s-1); the first violator is (2,3,5), forcing "
      "EXACTLY 6, and it too is unique at its cost.  So the corner "
      "constant is a three-rung LADDER 1 -> 4/3 -> 3/2, not a single "
      "number",
      LADDER[1][2] == [] and c43_viol[0] == (6, 2, 3, 5)
      and len([v for v in c43_viol if v[0] == 6]) == 1)

v32_5 = sorted((a, b, s) for s in range(1, 6) for a in range(0, s + 1)
               for b in range(0, s - a + 1) if 2 * a * b > 3 * (s - 1))
v32_6 = sorted((a, b, s) for s in range(6, 7) for a in range(0, s + 1)
               for b in range(0, s - a + 1) if 2 * a * b > 3 * (s - 1))
check("c = 3/2 (0015's corner) holds unconditionally for s <= 5 -- no "
      "violator at all -- and FAILS at s = 6, on exactly (2,4,6), "
      "(3,3,6), (4,2,6).  So 6-uniformity (s <= 5) is load-bearing for "
      "0015's constant.  It is NOT needed for c = 1, whose a <= 1 branch "
      "was just exhausted out to s = 19: at a = 0, a*b = 0 <= s-1 needs "
      "only s >= 1; at a = 1, b <= s-1 directly",
      v32_5 == [] and v32_6 == [(2, 4, 6), (3, 3, 6), (4, 2, 6)])

check("TEETH: at s = 0 the corner would read 0 > -1 and FAIL, so s >= 1 "
      "is load-bearing -- and it holds because K - e is a subfamily of "
      "an intersecting family, so every pair inside it still meets.  "
      "Intersecting-ness is spent exactly here (static arithmetic: this "
      "check documents the boundary and cannot fail on its own)",
      0 * 0 > 0 - 1)

t0 = time.time()
ASM = LCG(31415926)
asm_bad = 0
asm_n = 0
for _ in range(3000):
    nv = 2 + ASM.below(3)
    F = []
    for _ in range(120):
        if len(F) >= 3 + ASM.below(6):
            break
        c = tuple(ASM.below(nv) for _ in range(6))
        if c in F:
            continue
        if all(lam(c, f) >= 1 for f in F):
            F.append(c)
    m = len(F)
    if m < 3:
        continue
    X = sum(lam(p, q) - 1 for p, q in itertools.combinations(F, 2))
    for k in range(m):
        others = [f for j, f in enumerate(F) if j != k]
        xe = sum(lam(F[k], f) - 1 for f in others)
        rest = sum(lam(f, g) - 1
                   for f, g in itertools.combinations(others, 2))
        asm_n += 1
        if rest != X - xe:
            asm_bad += 1
check("THE ASSEMBLY OF (CC4+), which is the step the corner is FOR: "
      "sum over pairs {f,g} inside K - e of (s - 1) = X - x_e exactly, "
      "because X sums (lambda - 1) over ALL pairs and the pairs meeting "
      "e contribute exactly x_e.  Verified as an identity on 13,335 "
      "(family, edge) instances.  Apply the corner a*b <= s - 1 "
      "pairwise and sum: I_e = sum a*b <= sum (s-1) = X - x_e.  That "
      "is (CC4+), and it is one line once the corner is in hand",
      asm_bad == 0 and asm_n == 13335,
      "%.1fs" % (time.time() - t0))

# ---- the repaired X = 5 witness
W_E = (0, 0, 0, 0, 0, 0)
W_F = (0, 0, 1, 1, 1, 1)
W_G = (0, 0, 1, 1, 2, 2)
W_K = [W_E, W_F, W_G]
W_T = sorted([(2, 1), (3, 1), (4, 1), (4, 2), (5, 1)])
VK = sorted(set((i, f[i]) for f in W_K for i in range(6)))
w_ecells = sorted(set((i, W_E[i]) for i in range(6)))
w_X = sum(lam(p, q) - 1 for p, q in itertools.combinations(W_K, 2))
w_xe = (lam(W_E, W_F) - 1) + (lam(W_E, W_G) - 1)
w_a = sum(1 for i in range(6) if W_F[i] == W_G[i] == W_E[i])
w_b = sum(1 for (i, u) in W_T if W_F[i] == W_G[i] == u)
w_s = lam(W_F, W_G)
w_covers = all(any(f[i] == u for (i, u) in W_T) for f in (W_F, W_G))
check("THE X = 5 WITNESS, repaired and verified in-transcript.  "
      "e = (0,0,0,0,0,0), f = (0,0,1,1,1,1), g = (0,0,1,1,2,2), "
      "T_e = {(2,1),(3,1),(4,1),(4,2),(5,1)}.  ALL FOUR HYPOTHESES "
      "hold: |T_e| = 5, T_e cap e = empty, T_e INSIDE V(K) (the "
      "phase-2 refuter found the originally quoted T_e used three "
      "cells no edge of K carries), and T_e covers K - e.  X = 5, "
      "x_e = 2, (a,b,s) = (2,2,4)",
      len(W_T) == 5
      and [c for c in W_T if c in w_ecells] == []
      and [c for c in W_T if c not in VK] == []
      and w_covers and w_X == 5 and w_xe == 2
      and (w_a, w_b, w_s) == (2, 2, 4))

w_Ie = w_a * w_b
check("AND THE CORNER DIES ON IT: a*b = 4 > s - 1 = 3, so I_e = 4 "
      "exceeds X - x_e = 3 and the MIDDLE step of (CC+) FAILS -- while "
      "PLAIN (CC) survives on the same object, 2ab = 8 <= 3(s-1) = 9.  "
      "The witness separates (CC4+) from (CC) and nothing else.  The "
      "corner genuinely dies at X = 5, not at X = 4",
      w_Ie == 4 and w_Ie > w_X - w_xe
      and 2 * w_Ie <= 3 * (w_s - 1))

w_deg = {}
for f in W_K:
    for i in range(6):
        w_deg[(i, f[i])] = w_deg.get((i, f[i]), 0) + 1
w_d = [w_deg[(i, W_E[i])] for i in range(6)]
w_bi = [sum(1 for (p, u) in W_T if p == i) for i in range(6)]
w_left = sum(phi(w_d[i] - 1, 5 - w_bi[i]) for i in range(6)
             if w_bi[i] < 5)
check("THE OPEN FLAG, asserted rather than glossed: on that same "
      "witness the degrees along e are (3,3,1,1,1,1) and b = "
      "(0,0,1,1,2,1), so the LEFT side sum_i Phi(d_i-1, 5-b_i) is "
      "ZERO and the END-TO-END conclusion sum_i Phi <= X - x_e reads "
      "0 <= 3 and HOLDS.  The witness bounds the PROOF METHOD at "
      "X <= 4; it does NOT exhibit an object where (CC+)'s conclusion "
      "is false.  WHETHER (CC+) SURVIVES END TO END AT X = 5 IS OPEN",
      sorted(w_d) == [1, 1, 1, 1, 3, 3] and sum(w_bi) == 5
      and w_left == 0 and w_left <= w_X - w_xe)
note("STATED, NOT TESTED, and it is the honest scope of the open flag: "
     "the phase-2 refuter ran a 120,000-trial randomized hunt for an "
     "X = 5 family whose END-TO-END conclusion fails.  It found none -- "
     "and it also found ZERO enactments with a positive left side, so "
     "the hunt has no teeth in either direction.  There is NO EVIDENCE "
     "either way, and this certificate claims none")
note("STATED, NOT TESTED: the witness is an ABSTRACT corner object, not "
     "a critical core.  With m = 3 its tau(K - e) is 1 -- the single "
     "cell (2,1) covers both f and g -- so T_e is a 5-cover but not a "
     "MINIMUM one, and {e,f,g} is not and cannot be a critical core.  "
     "The corner is a statement about (a,b,s) arithmetic; criticality "
     "enters only where the law consumes 0013's private covers")

# ==========================================================================
# 3.  (C2) the unconditional pair-sum
# ==========================================================================

head("3.  (C2) the pair-sum, with the a_e <= 1 hypothesis removed")

two_bad = []
for s in range(1, SMAX + 1):
    for a in range(0, s + 1):
        for b in range(0, s - a + 1):
            if not (a * b <= a * (s - a) <= a * (s - 1)):
                two_bad.append((a, b, s))
check("THE TWO-STEP BOUND, exhaustively over every (a,b,s) with "
      "a + b <= s and s <= 19: a_e*b_e <= a_e(s - a_e) <= a_e(s - 1).  "
      "The first step is b_e <= s - a_e (0013 (3a) makes f cap g cap e "
      "and f cap g cap T_e DISJOINT subsets of f cap g); the second is "
      "s - a_e <= s - 1 when a_e >= 1, and both sides vanish at "
      "a_e = 0.  NO hypothesis on a_e, and s <= 5 is not used -- the "
      "6-uniform cap is spent nowhere in C2",
      two_bad == [])
note("STATED, NOT TESTED (it is an exchange of two finite sums, not a "
     "computation): sum_{e not in {f,g}} a_e = sum_{u in f cap g} "
     "(deg u - 2), counting each accounting edge once per shared vertex "
     "it contains.  It is an IDENTITY IN THE MULTIPLICITIES a_e, not a "
     "count of edges -- an a_e = 2 edge contributes 2 -- and every term "
     "is >= 0 because u lies on both f and g so deg u >= 2.  Section 3 "
     "enacts it on families that CONTAIN codegree-3 triangles, where "
     "a_e = 2 is realised rather than excluded by construction")


RNG = LCG(20260727)


def degrees(F):
    d = {}
    for f in F:
        for i in range(6):
            d[(i, f[i])] = d.get((i, f[i]), 0) + 1
    return d


# ---- (a) the corner and (CC4+) on random X <= 4 families
t0 = time.time()
fams_a = 0
le4 = 0
enacts_a = 0
id_bad = 0
cc_bad = 0
corner_bad = 0
tight_a = 0
a2_pairs = 0
a2_fams = 0
for trial in range(30000):
    nv = 2 + RNG.below(3)
    target = 4 + RNG.below(6)
    F = []
    for _ in range(300):
        if len(F) >= target:
            break
        c = tuple(RNG.below(nv) for _ in range(6))
        if c in F:
            continue
        if all(lam(c, f) >= 1 for f in F):
            F.append(c)
    m = len(F)
    if m < 4:
        continue
    fams_a += 1
    X = sum(lam(p, q) - 1 for p, q in itertools.combinations(F, 2))
    if X > 4:
        continue
    le4 += 1
    deg = degrees(F)
    xs = [sum(lam(F[k], f) - 1 for j, f in enumerate(F) if j != k)
          for k in range(m)]
    cells = sorted(set((i, f[i]) for f in F for i in range(6)))
    hasa2 = False
    for k in range(m):
        e = F[k]
        ec = sorted(set((i, e[i]) for i in range(6)))
        pool = [c for c in cells if c not in ec]
        if len(pool) < 5:
            continue
        pl = list(pool)
        T = []
        for _ in range(5):
            T.append(pl.pop(RNG.below(len(pl))))
        T = sorted(T)
        others = [f for j, f in enumerate(F) if j != k]
        I = 0
        for i in range(6):
            for (pu, uu) in T:
                if pu == i:
                    continue
                nn = sum(1 for f in others if f[i] == e[i] and f[pu] == uu)
                I += comb(nn, 2)
        Ip = 0
        for f, g in itertools.combinations(others, 2):
            a = sum(1 for i in range(6) if f[i] == g[i] == e[i])
            b = sum(1 for (i, u) in T if f[i] == g[i] == u)
            s = lam(f, g)
            if a >= 2:
                a2_pairs += 1
                hasa2 = True
            if a * b > s - 1:
                corner_bad += 1
            Ip += a * b
        enacts_a += 1
        if I != Ip:
            id_bad += 1
        if I > X - xs[k]:
            cc_bad += 1
        if I == X - xs[k] and I > 0:
            tight_a += 1
    if hasa2:
        a2_fams += 1
check("(CC4+) ENACTED.  30,000 LCG trials (house seed 20260727) build "
      "30,000 random intersecting 6-partite 6-uniform systems with "
      "m >= 4; exactly 1,086 have X <= 4.  On those, 4,494 (edge, "
      "ARBITRARY disjoint 5-set) enactments -- arbitrary, because the "
      "corner needs only T_e cap e = empty and not covering -- satisfy "
      "the accounting identity I_e = sum over pairs of a*b, the corner "
      "a*b <= s-1 pairwise, and the bound I_e <= X - x_e.  Zero "
      "failures of any of the three, with 460 enactments TIGHT at "
      "I_e = X - x_e > 0.  The a >= 2 branch -- the branch the whole "
      "ladder is about -- fires on 45 pairs across 15 systems, so it "
      "is exercised and not vacuous",
      fams_a == 30000 and le4 == 1086 and enacts_a == 4494
      and id_bad == 0 and cc_bad == 0 and corner_bad == 0
      and tight_a == 460 and a2_pairs == 45 and a2_fams == 15,
      "%.1fs" % (time.time() - t0))

# ---- (b) the pair-sum on families CONTAINING codegree-3 triangles
t0 = time.time()
ps_n = 0
ps_bad = 0
ps_id_bad = 0
ps_a2 = 0
mut_bad = 0
cmp_n = 0
cmp_small = 0
cmp_large = 0
for trial in range(6000):
    nv = 2 + RNG.below(3)
    F = []
    for _ in range(60):
        if len(F) >= 3:
            break
        c = (0, 0) + tuple(RNG.below(nv) for _ in range(4))
        if c in F:
            continue
        F.append(c)
    if len(F) < 3:
        continue
    extra = RNG.below(4)
    for _ in range(extra * 15):
        if len(F) >= 3 + extra:
            break
        c = tuple(RNG.below(nv) for _ in range(6))
        if c in F:
            continue
        if all(lam(c, f) >= 1 for f in F):
            F.append(c)
    m = len(F)
    if m < 3:
        continue
    if not all(lam(p, q) >= 1 for p, q in itertools.combinations(F, 2)):
        continue
    deg = degrees(F)
    X = sum(lam(p, q) - 1 for p, q in itertools.combinations(F, 2))
    cells = sorted(set((i, f[i]) for f in F for i in range(6)))
    sumI = 0
    short = False
    for k in range(m):
        e = F[k]
        ec = sorted(set((i, e[i]) for i in range(6)))
        pool = [c for c in cells if c not in ec]
        if len(pool) < 5:
            short = True
            break
        pl = list(pool)
        T = []
        for _ in range(5):
            T.append(pl.pop(RNG.below(len(pl))))
        others = [f for j, f in enumerate(F) if j != k]
        for f, g in itertools.combinations(others, 2):
            a = sum(1 for i in range(6) if f[i] == g[i] == e[i])
            b = sum(1 for (i, u) in T if f[i] == g[i] == u)
            sumI += a * b
    if short:
        continue
    okid = True
    rhs = 0
    mut = 0
    sawa2 = False
    for f, g in itertools.combinations(F, 2):
        L = lam(f, g)
        shared = [i for i in range(6) if f[i] == g[i]]
        lhs_id = 0
        for e2 in F:
            if e2 == f or e2 == g:
                continue
            ae = sum(1 for i in shared if e2[i] == f[i])
            lhs_id += ae
            if ae >= 2:
                sawa2 = True
        rhs_id = sum(deg[(i, f[i])] - 2 for i in shared)
        if lhs_id != rhs_id:
            okid = False
        if L >= 2:
            rhs += (L - 1) * rhs_id
            mut += rhs_id
    ps_n += 1
    if sawa2:
        ps_a2 += 1
    if not okid:
        ps_id_bad += 1
    if sumI > rhs:
        ps_bad += 1
    if sumI > mut:
        mut_bad += 1
    cc = 3 * (m - 2) * X
    if 2 * rhs != cc:
        cmp_n += 1
    if 2 * rhs < cc:
        cmp_small += 1
    elif 2 * rhs > cc:
        cmp_large += 1
check("THE PAIR-SUM ENACTED WHERE 0016 COULD NOT GO: 4,819 systems "
      "BUILT to contain a codegree-3 triangle (three edges through the "
      "same two vertices), so a_e >= 2 is realised in ALL 4,819 -- 0016 "
      "section 6's test excluded exactly this by construction.  Zero "
      "failures of the identity sum_e a_e = sum_u (deg u - 2), zero "
      "failures of sum_e I_e <= sum over excessive pairs of "
      "(lambda-1)*sum_u (deg u - 2).  The hypothesis-free form holds",
      ps_n == 4819 and ps_a2 == 4819 and ps_id_bad == 0 and ps_bad == 0,
      "%.1fs" % (time.time() - t0))
check("MUTANT, and it FAILS as it must: drop the (lambda - 1) factor "
      "from the pair-sum and the resulting inequality is FALSE on 1,306 "
      "of those same 4,819 systems.  The factor is load-bearing and this "
      "check can go red -- it is not a tautology dressed as a check",
      mut_bad == 1306 and mut_bad > 0)
check("HONESTY, MEASURED IN BOTH DIRECTIONS (D-035): C2 is a COMPLEMENT "
      "to plain (CC), NOT a strengthening.  Over the 4,763 of those "
      "systems where the two right sides differ, C2's is strictly "
      "SMALLER on 1,755 and strictly LARGER on 3,008.  The reason is "
      "structural: C2's per-pair coefficient is sum_u (deg u - 2) <= "
      "5(Delta - 2), against plain (CC)'s (3/2)(m - 2).  At m = 22 with "
      "the pinned ladder's Delta <= 9 that is 35 against 30 -- C2 is the "
      "WEAKER of the two on exactly the heavy-shared-vertex pairs the "
      "X = 3 frontier is fighting over.  It ties at Delta = 8 and wins "
      "at Delta = 7",
      cmp_n == 4763 and cmp_small == 1755 and cmp_large == 3008
      and 5 * (9 - 2) == 35 and 3 * (22 - 2) == 2 * 30
      and 5 * (8 - 2) == 30 and 5 * (7 - 2) == 25)
note("LEDGER note for the comparison above: Delta <= 9 at m = 22 is the "
     "pinned ladder's cap (0009/0012), entering this certificate only "
     "through C7's transitive row; the 35-vs-30 line is illustrative "
     "arithmetic at those parameters, and the load-bearing evidence for "
     "'complement, not strengthening' is the measured two-way split")

# ---- (c) adversarially chosen covers
t0 = time.time()
adv_n = 0
adv_bad = 0
adv_min = None
for trial in range(4000):
    nv = 2 + RNG.below(2)
    F = []
    for _ in range(60):
        if len(F) >= 3:
            break
        c = (0, 0) + tuple(RNG.below(nv) for _ in range(4))
        if c in F:
            continue
        F.append(c)
    if len(F) < 3:
        continue
    extra = RNG.below(3)
    for _ in range(extra * 12):
        if len(F) >= 3 + extra:
            break
        c = tuple(RNG.below(nv) for _ in range(6))
        if c in F:
            continue
        if all(lam(c, f) >= 1 for f in F):
            F.append(c)
    m = len(F)
    if not all(lam(p, q) >= 1 for p, q in itertools.combinations(F, 2)):
        continue
    deg = degrees(F)
    cells = sorted(set((i, f[i]) for f in F for i in range(6)))
    tot = 0
    short = False
    for k in range(m):
        e = F[k]
        ec = sorted(set((i, e[i]) for i in range(6)))
        pool = [c for c in cells if c not in ec]
        if len(pool) < 5 or comb(len(pool), 5) > 200:
            short = True
            break
        others = [f for j, f in enumerate(F) if j != k]
        best = 0
        for T in itertools.combinations(pool, 5):
            I = 0
            for f, g in itertools.combinations(others, 2):
                a = sum(1 for i in range(6) if f[i] == g[i] == e[i])
                b = sum(1 for (i, u) in T if f[i] == g[i] == u)
                I += a * b
            if I > best:
                best = I
        tot += best
    if short:
        continue
    rhs = 0
    for f, g in itertools.combinations(F, 2):
        L = lam(f, g)
        if L >= 2:
            rhs += (L - 1) * sum(deg[(i, f[i])] - 2
                                 for i in range(6) if f[i] == g[i])
    adv_n += 1
    if tot > rhs:
        adv_bad += 1
    if adv_min is None or rhs - tot < adv_min:
        adv_min = rhs - tot
check("AND WITH ADVERSARIALLY CHOSEN COVERS: on 2,570 further systems, "
      "T_e is picked EXHAUSTIVELY over every disjoint 5-set so as to "
      "MAXIMISE I_e edge by edge -- the worst case the bound must "
      "survive -- and the pair-sum still never fails.  FUNNEL, said in "
      "full: of 4,000 trials, 1,355 lack a 5-cell pool (hypothesis "
      "failure) and 75 exceed the C(pool,5) <= 200 enumeration cap "
      "(a runtime guard, near-inert at 2.8%; 'exhaustively' is true of "
      "every retained system).  MEASURED AND "
      "SAID: the minimum slack in this run is 6, so THIS generator "
      "never attains the bound, and this certificate claims no "
      "attainability from its own evidence",
      adv_n == 2570 and adv_bad == 0 and adv_min == 6,
      "%.1fs, min slack %d" % (time.time() - t0, adv_min))
note("STATED, NOT TESTED, and it is the scope limit of the check above: "
     "the phase-2 refuter DID reach equality, in 54 of 350 families "
     "under its own adversarial-cover design.  So the pair-sum is "
     "attainable and not gratuitously loose -- but that is the "
     "refuter's measurement, not this checker's, and it is recorded as "
     "such rather than re-quoted as if this run had produced it")
note("ADDENDUM, NOT ERRATUM, against certificate 0016 section 6: 0016 "
     "derived the pair-sum under 'a_e <= 1 by (T)', which at X <= 2 is "
     "TRUE.  That derivation is correct -- merely not minimal.  C2 "
     "removes the hypothesis outright.  No 0016 check condition, and no "
     "0016 conclusion, changes; the addendum belongs in 0016's NOTES, "
     "and no erratum is owed")

# ==========================================================================
# 4.  (C3) the per-edge linear law
# ==========================================================================

head("4.  (C3) the per-edge linear law 2m + 5x_e <= 52 + 3X")

t0 = time.time()
ok31 = True
R2 = LCG(11223344)
for _ in range(200000):
    b = [0] * 6
    for _ in range(5):
        b[R2.below(6)] += 1
    d = [1 + R2.below(12) for _ in range(6)]
    if sum((d[i] - 1) - (5 - b[i]) for i in range(6)) != sum(d) - 31:
        ok31 = False
check("THE -31 IDENTITY: sum_i [(d_i - 1) - (5 - b_i)] = sum_i d_i - 31 "
      "whenever sum_i b_i = 5, on 200,000 random (d, b) pairs from an "
      "independent LCG stream.  It is -6 - 30 + sum_i b_i and nothing "
      "else.  The sabotage constant -30 is never right; -36, the value "
      "obtained by DROPPING the b_i's, moves Theta from 26 to 31 and is "
      "priced in section 11",
      ok31, "%.1fs" % (time.time() - t0))

BPROF = sorted(b for b in itertools.product(range(6), repeat=6)
               if sum(b) == 5)
DMS = sorted(itertools.combinations_with_replacement(range(1, 11), 6))
TAB = {}
for d in range(1, 11):
    for b in range(0, 6):
        TAB[(d, b)] = phi(d - 1, 5 - b) if b < 5 else None
t0 = time.time()
n_excl = 0
n_test = 0
n_viol = 0
n_excl_fail = 0
worst_gap = 0
for b in BPROF:
    for d in DMS:
        bad = False
        for i in range(6):
            if b[i] == 5 and d[i] >= 2:
                bad = True
                break
        lhs = 0
        for i in range(6):
            t = TAB[(d[i], b[i])]
            if t is not None:
                lhs += t
        need = sum(d) - 31
        if bad:
            n_excl += 1
            if lhs < need:
                n_excl_fail += 1
                if need - lhs > worst_gap:
                    worst_gap = need - lhs
        else:
            n_test += 1
            if lhs < need:
                n_viol += 1
check("THE STEP, EXHAUSTED: over all 252 b-profiles (sum b_i = 5) times "
      "all 5,005 ascending degree 6-multisets with entries in 1..10 -- "
      "1,261,260 states -- the inequality sum_i Phi(d_i-1, 5-b_i) >= "
      "sum_i d_i - 31 holds on ALL 1,234,233 states with no b_i = 5 "
      "concentration.  Zero violations",
      len(BPROF) == 252 and len(DMS) == 5005
      and n_test == 1234233 and n_viol == 0,
      "%.1fs" % (time.time() - t0))
check("AND THE TEETH THAT MAKE THE b_i = 5 BRANCH LOAD-BEARING: on the "
      "27,027 EXCLUDED states -- b_i = 5 in some part together with "
      "d_i >= 2 -- the step is FALSE 9,015 times, worst gap exactly 9 "
      "(at b = (0,0,0,0,0,5), d = (6,6,6,6,6,10): left side 0 against a "
      "required 9).  A derivation that does not close this branch is "
      "not conservative, it is WRONG -- and the omission flatters the "
      "conclusion, which is this lab's named worst failure mode",
      n_excl == 27027 and n_excl_fail == 9015 and worst_gap == 9)
check("THE BRANCH IS CLOSED BY COVERING ALONE, NOT BY LEMMA (A).  If "
      "b_i = 5 then every one of the d_i - 1 edges through v_i other "
      "than e must meet T_e minus V_i, which is EMPTY -- and it cannot "
      "meet T_e inside V_i either, because such an edge's unique part-i "
      "vertex is v_i and v_i is not in T_e (0013 (3a)).  So d_i = 1 and "
      "the term reads 0 >= (1-1) - (5-5) = 0.  This is 0015 step (1).  "
      "Lemma (A) of 0005 (d_i >= 2, hence b_i <= 4) would ALSO close it, "
      "and the law deliberately does not spend it: C3 holds for any "
      "intersecting family with private covers, critical or not "
      "(static arithmetic plus a registry lookup: this check documents "
      "the argument; the load-bearing evidence is the 9,015 exhibited "
      "failures of the check before it)",
      TAB[(1, 5)] is None and (1 - 1) - (5 - 5) == 0)

grid_bad = 0
grid_n = 0
for m in range(1, 121):
    for xe in range(0, 16):
        for X in range(0, 41):
            grid_n += 1
            if ((2 * (m + xe - 26) <= 3 * (X - xe))
                    != (2 * m + 5 * xe <= 52 + 3 * X)):
                grid_bad += 1
check("THE ASSEMBLY, as an integer equivalence rather than prose: "
      "2(m + x_e - 26) <= 3(X - x_e)  <=>  2m + 5x_e <= 52 + 3X, "
      "verified over the whole grid m in [1,120], x_e in [0,15], "
      "X in [0,40].  The left form is the chain 'relaxation <= sum_i "
      "Phi <= I_e <= (3/2)(X - x_e)' cleared of its denominator; the "
      "right form is the law as quoted",
      grid_bad == 0 and grid_n == 120 * 16 * 41)

check("THE tau-GENERIC FORM.  The threshold is Theta = 5*sigma + 1 with "
      "sigma = |T_e| = t - 1, i.e. Theta = 5t - 4: 21 at sigma = 4 "
      "(t = 5), 26 at sigma = 5 (t = 6), 31 at sigma = 6 (t = 7).  The "
      "per-edge constant is 2*Theta = 10t - 8, so 52 at t = 6 and 42 "
      "at t = 5.  The 10 in "
      "(3m - 10) does NOT move with t -- it is 5 (the x_e coefficient) "
      "times the 2 of sum_e x_e = 2X, a corner-constant artefact "
      "(static arithmetic: cannot fail on its own)",
      [5 * s + 1 for s in (4, 5, 6)] == [21, 26, 31]
      and [2 * (5 * s + 1) for s in (4, 5, 6)] == [42, 52, 62]
      and 5 * 6 - 4 == 26 and 10 * 6 - 8 == 52 and 10 * 5 - 8 == 42)

# ==========================================================================
# 5.  (C4) the summed law and the integrality lift
# ==========================================================================

head("5.  (C4) the summed law, and the integrality lift")


def lin_unlift(m):
    """ceil(2m(m-26)/(3m-10)), floored at 0."""
    num = 2 * m * (m - 26)
    den = 3 * m - 10
    return max(-((-num) // den), 0)


def lin_ok(m, X):
    """The LIFTED per-edge test: x_e <= floor((52+3X-2m)/5) for every
    edge, and sum_e x_e = 2X, so 2X <= m * that floor."""
    return 2 * X <= m * ((52 + 3 * X - 2 * m) // 5)


def lin_min(m):
    """Smallest X >= 0 the lift admits.  MUST scan from 0: the lifted
    predicate is not upward-closed in X."""
    X = 0
    while not lin_ok(m, X):
        X += 1
    return X


UNL = [(m, lin_unlift(m)) for m in
       (22, 26, 27, 28, 29, 30, 31, 50, 100, 200, 300, 456, 462)]
check("THE SUMMED LAW, un-lifted: X >= 2m(m-26)/(3m-10), as exact "
      "integer ceilings.  m = 22 and 26 give 0 (the law is VACUOUS at "
      "the window floor and says nothing there), then 1, 2, 3, 3, 4 at "
      "m = 27..31, 18 at 50, 52 at 100, 118 at 200, 185 at 300, 289 at "
      "456 and 293 at 462",
      UNL == [(22, 0), (26, 0), (27, 1), (28, 2), (29, 3), (30, 3),
              (31, 4), (50, 18), (100, 52), (200, 118), (300, 185),
              (456, 289), (462, 293)])

LIFT = [(m, lin_min(m)) for m in
        (27, 28, 29, 30, 31, 50, 100, 200, 300, 456, 462)]
check("THE INTEGRALITY LIFT, pinned: x_e is a non-negative INTEGER, so "
      "x_e <= floor((52 + 3X - 2m)/5) and 2X <= m*floor(...).  Floors "
      "m = 27:3, 28:3, 29:4, 30:5, 31:5, 50:18, 100:53, 200:120, "
      "300:186, 456:290, 462:294 -- strictly above the un-lifted law at "
      "every one of 27, 28, 29, 30, 31, 100, 200, 300, 456, 462, and "
      "worth exactly one unit at the window ceiling",
      LIFT == [(27, 3), (28, 3), (29, 4), (30, 5), (31, 5), (50, 18),
               (100, 53), (200, 120), (300, 186), (456, 290),
               (462, 294)])

s289 = (52 + 3 * 289 - 2 * 456)
s290 = (52 + 3 * 290 - 2 * 456)
check("BOTH SIDES PRINTED AT THE CEILING, m = 456.  At X = 289 the "
      "numerator is 7, floor(7/5) = 1, so sum_e x_e <= 456 while "
      "2X = 578 -- CONTRADICTION, and the un-lifted law's own floor "
      "DIES.  At X = 290 the numerator is 10, floor = 2, so "
      "sum_e x_e <= 912 >= 580 -- CONSISTENT.  And no X below 290 "
      "passes, checked exhaustively from X = 0",
      s289 == 7 and s289 // 5 == 1 and 456 * 1 == 456 and 456 < 578
      and s290 == 10 and s290 // 5 == 2 and 456 * 2 == 912
      and 912 >= 580
      and [X for X in range(0, 290) if lin_ok(456, X)] == [],
      "456*1 = 456 < 578 FAILS ; 456*2 = 912 >= 580 HOLDS")

check("AND AT m = 462, the other end of the certified window: 293 fails "
      "(462 < 586) and 294 holds (924 >= 588); no X below 294 passes",
      not lin_ok(462, 293) and lin_ok(462, 294)
      and [X for X in range(0, 294) if lin_ok(462, X)] == [])

check("THE LIFTED PREDICATE IS NOT UPWARD-CLOSED IN X, and this is why "
      "the floor must be found by scanning from X = 0 and never by "
      "bisection: at m = 26 the value X = 1 is FORBIDDEN while X = 0 "
      "and X = 2 are both admitted, and at m = 94 the value X = 48 is "
      "forbidden while 47 and 49 are admitted.  The law excludes "
      "isolated values, it does not merely place a floor",
      lin_ok(26, 0) and not lin_ok(26, 1) and lin_ok(26, 2)
      and lin_ok(94, 47) and not lin_ok(94, 48) and lin_ok(94, 49))

check("AND IT IS NOT MONOTONE IN m: the floor at m = 93 is 48 and at "
      "m = 94 it is 47.  A bigger core can be admitted at a SMALLER "
      "excess.  Anyone reading the floor table as a monotone curve will "
      "mis-state the law; asserted here so the table cannot be read "
      "that way",
      lin_min(93) == 48 and lin_min(94) == 47 and lin_min(93) > lin_min(94))


def someedge(m):
    return max(-((-(2 * m - 47)) // 3), 0)


agree = sorted(m for m in range(27, 463) if someedge(m) == lin_min(m))
below = sorted(m for m in range(27, 463) if someedge(m) < lin_min(m))
persist = min(m0 for m0 in range(27, 463)
              if all(someedge(z) < lin_min(z) for z in range(m0, 463)))
check("THE SOME-EDGE FORM, an easy corollary and never the headline.  "
      "m >= 27 forces X >= 1 by the law itself; X >= 1 forces some pair "
      "with lambda >= 2, hence BOTH its edges carry x_e >= 1; the "
      "per-edge law on either of them reads 2m + 5 <= 52 + 3X, i.e. "
      "3X >= 2m - 47.  It TIES the full lift on all of m = 27..92 and "
      "again at 94 (67 values), first falls strictly below at m = 93, "
      "and is strictly weaker from m = 95 onward.  Quote it for its "
      "one-line proof, never for its strength",
      len(agree) == 67 and below[0] == 93 and persist == 95
      and someedge(27) == 3 and someedge(456) == 289
      and lin_min(456) == 290)

# ==========================================================================
# 6.  (C5) the coupling of excess to size
# ==========================================================================

head("6.  (C5) X <= 2 => m <= 26 ;  X <= 4 => m <= 28")


def c1_ok(m, X):
    """The c = 1 per-edge law m + 2x_e <= X + 26, lifted.  Legal only
    under the hypothesis X <= 4 -- a conditional use, and legitimate."""
    return 2 * X <= m * ((X + 26 - m) // 2)


big2 = sorted(m for m in range(1, 3000)
              if any(lin_ok(m, X) for X in range(0, 3)))
check("X <= 2 IMPLIES m <= 26, from the C4 lift ALONE: exhausting every "
      "m up to 2,999, no m >= 27 admits any X in {0,1,2}.  It is SHARP "
      "-- m = 26 with X = 0 passes (floor(0/5) = 0 and 2X = 0 <= 0), so "
      "26 is genuinely not excluded",
      max(big2) == 26 and lin_ok(26, 0))

big4_lin = sorted(m for m in range(1, 3000)
                  if any(lin_ok(m, X) for X in range(0, 5)))
big4_both = sorted(m for m in range(1, 3000)
                   if any(lin_ok(m, X) and c1_ok(m, X)
                          for X in range(0, 5)))
check("X <= 4 IMPLIES m <= 28 -- AND C1 IS LOAD-BEARING HERE, stated "
      "plainly.  C4 ALONE gives only m <= 29, because (m, X) = (29, 4) "
      "PASSES it: numerator 52 + 12 - 58 = 6, floor(6/5) = 1, "
      "m*B = 29 >= 2X = 8.  Adding C1's c = 1 corner -- whose per-edge "
      "law is m + 2x_e <= X + 26, lifted to 2X <= m*floor((X+26-m)/2) "
      "-- kills it: floor(1/2) = 0, so 0 >= 8 is false.  m = 28 is "
      "sharp (floor(2/2) = 1, 28 >= 8 passes).  THE LEDGER OF THIS RUNG "
      "IS C4 + C1, NOT C4",
      max(big4_lin) == 29 and max(big4_both) == 28
      and lin_ok(29, 4) and not c1_ok(29, 4) and c1_ok(28, 4)
      and (52 + 12 - 58) // 5 == 1 and 29 * 1 == 29 and 29 >= 8
      and (4 + 26 - 29) // 2 == 0,
      "C4 alone: 29*1 = 29 >= 8 PASSES ; with c=1: 29*0 = 0 < 8 DIES")
note("THE TAIL BEYOND THE SCAN, and it is the proof of universality in "
     "m: both couplings above scan m < 3,000, and the tail is a sign "
     "argument -- for m >= 33 and X <= 4 the numerator 52 + 3X - 2m is "
     "negative, so m*floor(.) < 0 <= 2X and the lifted predicate fails; "
     "for m in [30, 32] the scan itself covers it.  The scan is "
     "verification; the sign argument is the proof (audit repair)")
note("STATED AS THE COROLLARY IT IS: certificate 0016 proved X >= 3 for "
     "every critical core at m = 22, and C5 caps X <= 2 at m <= 26.  So "
     "ANY hypothetical critical core with X <= 2 lives in m in "
     "{23, 24, 25, 26} -- four values, and nothing else in the whole "
     "window [22, 456].  0016's X = 2 near-miss becomes a BOUNDED "
     "object.  This certificate runs no field scan at any of those four "
     "m; it only says where such a core could be")

# ==========================================================================
# 7.  (C6) (G), the second-moment law
# ==========================================================================

head("7.  (C6) (G), the second-moment law")


def G_left(m, X):
    """6m * psihat(mu) as an EXACT INTEGER, with mu the rational mean
    (m^2 + 5m + 2X)/(6m) and psihat the piecewise-linear interpolation
    of psi.  No floats anywhere in the decision."""
    tot = m * m + 5 * m + 2 * X
    d, rem = divmod(tot, 6 * m)
    return 6 * m * psi(d) + rem * (psi(d + 1) - psi(d))


def G_ok(m, X):
    return 2 * G_left(m, X) <= 3 * (m - 2) * X


def G_min(m):
    X = 0
    while not G_ok(m, X):
        X += 1
    return X


t0 = time.time()
mom_bad = 0
R3 = LCG(55667788)
for _ in range(4000):
    nv = 2 + R3.below(3)
    F = []
    for _ in range(80):
        if len(F) >= 3 + R3.below(6):
            break
        c = tuple(R3.below(nv) for _ in range(6))
        if c in F:
            continue
        if all(lam(c, f) >= 1 for f in F):
            F.append(c)
    m = len(F)
    if m < 3:
        continue
    deg = degrees(F)
    X = sum(lam(p, q) - 1 for p, q in itertools.combinations(F, 2))
    dv = sorted(deg.values())
    if sum(comb(d, 2) for d in dv) != comb(m, 2) + X:
        mom_bad += 1
    if sum(d * d for d in dv) != m * m + 5 * m + 2 * X:
        mom_bad += 1
    slots = [deg[(i, F[k][i])] for k in range(m) for i in range(6)]
    if len(slots) != 6 * m or sum(slots) != sum(d * d for d in dv):
        mom_bad += 1
    if sum(psi(s) for s in slots) != sum(d * psi(d) for d in dv):
        mom_bad += 1
check("THE TWO MOMENT IDENTITIES AND THE SLOT READING, on 4,000 random "
      "intersecting systems: sum_v C(deg,2) = C(m,2) + X (this is where "
      "INTERSECTING-NESS is spent -- every lambda >= 1); hence "
      "sum_v deg^2 = m^2 + 5m + 2X; the 6m incidence slots (e,i) carry "
      "d_i(e) and their total is exactly sum_v deg^2, because in a "
      "6-partite 6-uniform family v is the unique part-i vertex of each "
      "of its deg(v) edges; and the two readings of "
      "W = sum over slots of psi = sum_v deg(v)*psi(deg v) agree every "
      "time.  Zero failures of any of the four",
      mom_bad == 0, "%.1fs" % (time.time() - t0))

t0 = time.time()
jen_bad = 0
jen_tight = 0
R4 = LCG(99001122)
for _ in range(20000):
    N = 2 + R4.below(12)
    xs = [R4.below(30) for _ in range(N)]
    d, rem = divmod(sum(xs), N)
    hat = N * psi(d) + rem * (psi(d + 1) - psi(d))
    if N * sum(psi(x) for x in xs) < hat:
        jen_bad += 1
    if N * sum(psi(x) for x in xs) == hat:
        jen_tight += 1
check("JENSEN, IN THE ALL-INTEGER FORM (G) USES, on 20,000 random "
      "integer samples: with d, rem = divmod(sum x_i, N), "
      "N * sum_i psi(x_i) >= N*psi(d) + rem*(psi(d+1) - psi(d)) = "
      "N * psihat(mean).  Zero violations, with equality reached "
      "whenever every sample lies in {d, d+1}, where psihat is linear.  "
      "Integrality of the samples is used ONLY to replace psi by psihat "
      "on the left; the inequality itself is Jensen for a convex "
      "function on the reals, so a rational mean is harmless",
      jen_bad == 0 and jen_tight > 0,
      "%.1fs, %d tight" % (time.time() - t0, jen_tight))

GTAB = [(m, G_min(m)) for m in (50, 67, 93, 94, 100, 200, 300, 456, 462)]
check("(G) PINNED: floors m = 50:14, 67:31, 93:69, 94:71, 100:83, "
      "200:396, 300:942, 456:2259, 462:2321.  At m = 456 that is 2259 "
      "against C4's 290 -- the top of the window is a WALL, not a flat "
      "sea, and it is quadratic where C3/C4 are linear",
      GTAB == [(50, 14), (67, 31), (93, 69), (94, 71), (100, 83),
               (200, 396), (300, 942), (456, 2259), (462, 2321)])

check("BOTH SIDES PRINTED AT m = 456: at X = 2258 the left side "
      "6m*psihat(mu) is 1,538,340 against (3/2)(m-2)X = 1,537,698 -- "
      "the law FAILS.  At X = 2259 it is 1,538,370 against 1,538,379 "
      "-- it HOLDS, by nine units.  Cleared of denominators throughout, "
      "so every comparison is between exact integers",
      G_left(456, 2258) == 1538340
      and 3 * 454 * 2258 == 2 * 1537698
      and not G_ok(456, 2258)
      and G_left(456, 2259) == 1538370
      and 3 * 454 * 2259 == 2 * 1538379
      and G_ok(456, 2259))

gap_bad = []
for (m, fl) in GTAB:
    if [X for X in range(0, fl) if G_ok(m, X)]:
        gap_bad.append(m)
check("THE CONCAVITY CAUTION, ASSERTED NOT ASSUMED.  g(X) = "
      "3(m-2)X - 2*6m*psihat(mu(X)) is CONCAVE in X (linear minus "
      "convex, since mu is affine in X and psihat is convex), so "
      "{X : (G) holds} is an INTERVAL and (G) is NOT automatically a "
      "lower bound.  Exhaustively, at every pinned m, NO X below the "
      "stated floor satisfies (G) -- there is no gap under the floor, "
      "and the floor really is a floor",
      gap_bad == [])


def G_hi(m):
    lo = G_min(m)
    hi = lo + 1
    while G_ok(m, hi):
        hi *= 2
    a, b = lo, hi
    while a + 1 < b:
        mid = (a + b) // 2
        if G_ok(m, mid):
            a = mid
        else:
            b = mid
    return a


HI456 = G_hi(456)
check("AND THE UPPER BRANCH OF THAT INTERVAL IS INERT, said out loud so "
      "nobody rediscovers it as an upper bound on X: at m = 456 the "
      "interval's top is X_hi = 4,455,141, more than TEN TIMES the "
      "trivial cap 4*C(456,2) = 414,960 that lambda <= 5 already gives.  "
      "(G) technically supplies an upper bound on X and it is worthless",
      HI456 == 4455141 and G_ok(456, HI456)
      and not G_ok(456, HI456 + 1) and HI456 > 4 * comb(456, 2)
      and 4 * comb(456, 2) == 414960,
      "X_hi = %d vs trivial cap %d" % (HI456, 4 * comb(456, 2)))

t0 = time.time()
GM = {}
LM = {}
for m in range(22, 463):
    GM[m] = G_min(m)
    LM[m] = lin_min(m)
cross = [(m, GM[m], LM[m]) for m in (65, 66, 67)]
vac = sorted(m for m in range(22, 40) if GM[m] == 0)
kept = sorted(m for m in range(67, 463) if GM[m] <= LM[m])
check("THE CROSSOVER, pinned: (G) TIES the lifted linear law at m = 65 "
      "(28 = 28) and m = 66 (29 = 29) and takes the lead at m = 67 "
      "(31 against 29) and NEVER GIVES IT BACK -- asserted STRICTLY "
      "(GM > LM, not merely >=), by "
      "comparing the two floors at every m from 67 to 462, not merely "
      "at the crossover.  Below that the LINEAR law is the strong one: "
      "(G) is VACUOUS for every m <= 31 and first bites at m = 32.  Two "
      "branches of one law, with the crossover measured, so neither may "
      "be quoted outside its range",
      cross == [(65, 28, 28), (66, 29, 29), (67, 31, 29)]
      and vac == sorted(range(22, 32)) and GM[32] == 1 and kept == [],
      "%.1fs for both floor curves over [22, 462]" % (time.time() - t0))


def G_min_variant(m, leftfn):
    X = 0
    while not (2 * leftfn(m, X) <= 3 * (m - 2) * X):
        X += 1
    return X


def left_shift(m, X):
    tot = m * m + 5 * m + 2 * X
    d, rem = divmod(tot, 6 * m)
    return 6 * m * psi(d + 1) + rem * (psi(d + 2) - psi(d + 1))


def left_ceil(m, X):
    tot = m * m + 5 * m + 2 * X
    d, rem = divmod(tot, 6 * m)
    return 6 * m * psi(d + (1 if rem else 0))


def left_floor(m, X):
    tot = m * m + 5 * m + 2 * X
    d, rem = divmod(tot, 6 * m)
    return 6 * m * psi(d)


check("MUTANT 1 -- THE psi-INDEX SHIFT, and it is the one that would "
      "have shipped.  Reading the psi row as starting at d = 0 instead "
      "of d = 1 (i.e. psi'(d) = Phi(d,5), so psi'(6) = 1 rather than "
      "the true psi(6) = Phi(5,5) = 0) inflates (G)'s floor at m = 456 "
      "from 2259 to 2323 -- SIXTY-FOUR UNITS OF PURE OVERCLAIM, in the "
      "direction that flatters the expected answer.  psi is DERIVED "
      "from Phi in this checker so the mutant cannot be written by "
      "accident, and if it were, FOUR checks would redden at once -- "
      "the psi index pin, the (G) floor table, the both-sides print at "
      "m = 456, and this one",
      G_min_variant(456, left_shift) == 2323
      and 2323 > 2259 and 2323 - 2259 == 64
      and psi(6) == 0 and phi(6, 5) == 1)

CEIL_X = [6] * 9 + [7]
cd, crem = divmod(sum(CEIL_X), len(CEIL_X))
check("MUTANT 2 -- psi(ceil(mu)) IS UNSOUND, with a ten-sample witness: "
      "nine 6s and one 7 have sum_i psi(x_i) = 1, while the rounded "
      "form claims 10*psi(ceil(6.1)) = 10*psi(7) = 10.  Ten times the "
      "truth, in the unsafe direction.  Coded that way (G) would read "
      "2291 at m = 456 -- a fake +32",
      sum(psi(x) for x in CEIL_X) == 1
      and len(CEIL_X) * psi(cd + (1 if crem else 0)) == 10
      and G_min_variant(456, left_ceil) == 2291)

check("MUTANT 3 -- psi(floor(mu)) IS SOUND BUT WEAKER, and it prices "
      "the interpolation: it gives 2230 at m = 456 against the true "
      "2259.  THE PIECEWISE-LINEAR INTERPOLATION IS WORTH 29 UNITS.  So "
      "the rem*(psi(d+1) - psi(d)) term in G_left is load-bearing, not "
      "decoration, and dropping it loses real strength without going "
      "red -- which is exactly why it is asserted here",
      G_min_variant(456, left_floor) == 2230
      and 2259 - 2230 == 29)
note("STATED, NOT TESTED, and it is a prohibition: the ASYMPTOTIC "
     "X ~ m^2/90 OVERSTATES the true floor at finite m -- 2310.4 "
     "against 2259 at m = 456, i.e. the real floor is 97.8% of the "
     "asymptote and approaches it FROM BELOW, crossing only near "
     "m = 1000.  m^2/90 is a note about the shape of the law.  It is "
     "NOT a bound and must never be quoted as one at any m in the "
     "window")
note("STATED, NOT TESTED (D-035, and it is the honest scope of (G)): "
     "ENACTMENT CANNOT PRICE (G) AT ALL.  Every real object this lab "
     "can build has m <= 25, and (G) is vacuous below m = 32.  The "
     "phase-2 refuter's 4,000 families and 30,062 per-edge enactments "
     "found zero violations of Jensen, of the relaxation and of (G) -- "
     "but only 1,265 had W > 0 and all had m <= 11.  Such runs detect a "
     "sign or direction error and NOTHING ELSE.  (G) ships as a chain "
     "of certified links whose teeth are the three mutants above, and "
     "that must be said rather than dressed up")

# ==========================================================================
# 8.  (C7) the combined window profile
# ==========================================================================

head("8.  (C7) the forced-X profile over the whole window [22, 456]")

t0 = time.time()
PROF = {}
for m in range(22, 457):
    v = max(LM[m], GM[m])
    if m == 22:
        v = max(v, 3)
    PROF[m] = v
zeros = sorted(m for m in sorted(PROF) if PROF[m] == 0)
counts = []
for thr in (1, 10, 100, 1000):
    ms = sorted(m for m in sorted(PROF) if PROF[m] >= thr)
    counts.append((thr, len(ms), ms[0]))
check("THE COMBINED PROFILE, recomputed in this run rather than quoted: "
      "max(0016's X >= 3 at m = 22, the C4 lift, (G)) forces X >= 1 on "
      "431 of the 435 integers m in [22, 456].  The four exceptions are "
      "EXACTLY m = 23, 24, 25, 26 -- the weakest rungs in the window, "
      "where the arithmetic forces NOTHING and the field campaign must "
      "do the work by hand.  Named, not buried",
      zeros == [23, 24, 25, 26] and counts[0] == (1, 431, 22),
      "%.1fs" % (time.time() - t0))
check("AND THE PROFILE'S UPPER REACHES: X >= 10 is forced from m = 38 "
      "up (419 of the 435 values), X >= 100 from m = 108 (349 values), "
      "X >= 1000 from m = 309 (148 values), and the maximum over the "
      "window is 2,259 at m = 456.  Each threshold's first m and count "
      "are recomputed here",
      counts[1] == (10, 419, 38) and counts[2] == (100, 349, 108)
      and counts[3] == (1000, 148, 309)
      and max(PROF[m] for m in sorted(PROF)) == 2259
      and PROF[456] == 2259)
note("STATED, NOT TESTED: the single m = 22 entry of that profile is "
     "certificate 0016's, cited and not re-derived -- it is the ONLY "
     "place this certificate touches a field scan, and it touches it by "
     "citation.  Everything else in the row is arithmetic that "
     "quantifies over every m at once.  THERE IS NO m = 22 FIELD SCAN "
     "IN THIS CERTIFICATE")

# ==========================================================================
# 9.  the tau = 5 rehearsal core -- DIRECTION CONTROL
# ==========================================================================

head("9.  the tau = 5 rehearsal core -- DIRECTION CONTROL, not a pin")


def norm(v):
    for x in v:
        if x % 5:
            inv = pow(x, 3, 5)
            return tuple((inv * y) % 5 for y in v)
    return None


PTS = sorted(set(n for n in (norm(v) for v in
                             itertools.product(range(5), repeat=3))
                 if n is not None))


def on(l, p):
    return (l[0] * p[0] + l[1] * p[1] + l[2] * p[2]) % 5 == 0


P_DEL = (0, 0, 1)
VERTS = sorted(q for q in PTS if q != P_DEL)
VIDX = {}
for i, q in enumerate(VERTS):
    VIDX[q] = i
EDGES = [frozenset(VIDX[q] for q in PTS if q != P_DEL and on(l, q))
         for l in PTS if not on(l, P_DEL)]
PART = {}
for pi, l in enumerate(sorted(q for q in PTS if on(q, P_DEL))):
    for q in PTS:
        if q != P_DEL and on(l, q):
            PART[VIDX[q]] = pi
VMASK = [0] * 30
for ei, e in enumerate(EDGES):
    for v in e:
        VMASK[v] |= (1 << ei)
FULL = (1 << 25) - 1


def kcover(E, k, allow=None):
    pool = range(30) if allow is None else allow
    for c in itertools.combinations(pool, k):
        mm = 0
        for v in c:
            mm |= VMASK[v]
        if mm & E == E:
            return c
    return None


t0 = time.time()
active = list(range(25))
E = FULL
changed = True
while changed:
    changed = False
    for ei in sorted(active):
        E2 = E & ~(1 << ei)
        if kcover(E2, 4) is None:
            active.remove(ei)
            E = E2
            changed = True
            break
active = sorted(active)
CE = [EDGES[i] for i in active]
mr = len(CE)
degr = {}
for e in CE:
    for v in e:
        degr[v] = degr.get(v, 0) + 1
Xr = sum(comb(d, 2) for d in sorted(degr.values())) - comb(mr, 2)
crit = all(kcover(E & ~(1 << ei), 4) is not None for ei in active)
avoid = all(kcover(E & ~(1 << ei), 4,
                   [v for v in range(30) if v not in EDGES[ei]]) is not None
            for ei in active)
partite = all(sorted(PART[v] for v in e) == [0, 1, 2, 3, 4, 5] for e in CE)
check("the deterministic rebuild reproduces certificate 0013's "
      "rehearsal core from PG(2,5) -- 14 edges, excess X = 0, maximum "
      "degree 5, 6-partite (every edge a transversal of the six lines "
      "through the deleted point), tau = 5 (no 4 vertices cover it), "
      "EDGE-CRITICAL (every K - e has a 4-cover) and every edge carries "
      "an e-AVOIDING 4-cover, which is 0013 (3a) at t = 5.  It is the "
      "same construction 0016 section 10 runs",
      mr == 14 and Xr == 0 and max(sorted(degr.values())) == 5
      and kcover(E, 4) is None and crit and avoid and partite,
      "%.1fs" % (time.time() - t0))

rows = sorted(set(sum(degr[v] for v in e) for e in CE))
tphi = sorted(set(sum(phi(degr[v] - 1, 4) for v in e) for e in CE))
slacks = sorted(set(sum(phi(degr[v] - 1, 4) for v in e)
                    - (sum(degr[v] for v in e) - 26) for e in CE))
check("THE SLACK DECOMPOSITION, per edge and uniform.  At t = 5 the "
      "identity constant is -(5t+1) = -26, so the relaxation offers "
      "sum_i d_i - 26 = 19 - 26 = -7 while the TRUE sum_i Phi is 0 on "
      "every edge: THE RELAXATION LOSES EXACTLY 7 UNITS PER EDGE, "
      "uniformly across all 14.  The row sum 19 is Lemma 1.2's "
      "m + 5 + x_e = 14 + 5 + 0.  The per-edge law then reads "
      "2*14 + 0 = 28 <= 42 + 0, clearing by 14 = 2*7 -- ALL of the law's "
      "clearance on this object is relaxation slack.  The true sum is "
      "COMPUTED here, not assumed (the audit caught a hard-coded 0)",
      rows == [19] and tphi == [0] and slacks == [7] and 2 * mr == 28
      and 42 - 28 == 14 and 14 == 2 * 7)
note("STATED, NOT TESTED, and it is the D-035 label: this section is a "
     "DIRECTION CONTROL.  It clears the law on relaxation slack alone, "
     "so it tests that the law's direction is not reversed and NOTHING "
     "MORE.  It does not test the binding step, and it does not pin the "
     "constant -- section 11 prices exactly what it can and cannot say")

sd2 = sum(d * d for d in sorted(degr.values()))
check("(G)_5 ON THE SAME REAL OBJECT, AT MARGIN EXACTLY ZERO -- the one "
      "genuine tooth in the controls.  With psi_5(d) = Phi(d-1, 4), "
      "psi_5(6) = Phi(5,4) = 1 > 0, so at X = 0 the chain "
      "2*sum_v deg*psi_5(deg) <= 3(m-2)X = 0 forces psi_5(deg v) = 0 "
      "for EVERY vertex, i.e. Delta <= 5.  The real object has Delta = "
      "EXACTLY 5.  One degree higher and (G)_5 would have killed a "
      "genuine edge-critical core.  The moment identity also holds: "
      "sum_v deg^2 = 266 = m(m-1) + 6m + 2X",
      psi5(6) == 1 and psi5(5) == 0
      and max(sorted(degr.values())) == 5
      and sum(d * psi5(d) for d in sorted(degr.values())) == 0
      and sd2 == 266 and sd2 == mr * (mr - 1) + 6 * mr + 2 * Xr)


def lin5_ok(m, X):
    return 2 * X <= m * ((42 + 3 * X - 2 * m) // 5)


def lin5_min(m):
    X = 0
    while not lin5_ok(m, X):
        X += 1
    return X


first5 = min(m for m in range(2, 60) if lin5_min(m) > 0)
check("THE t = 5 LIFTED LAW FIRST GOES POSITIVE AT m = 22, EXACTLY -- "
      "the same integer as the t = 6 window floor.  At m = 21 it forces "
      "nothing (Theta(6,5) = 21) and at m = 22 it forces X >= 3.  The "
      "ECHO IS NOTED AND NOTHING IS CLAIMED FROM IT: the two windows "
      "have different constants and the coincidence is arithmetic, not "
      "structural.  It is recorded because a reader will notice it and "
      "should be told in advance that it means nothing",
      first5 == 22 and lin5_min(21) == 0 and lin5_min(22) == 3
      and lin5_min(14) == 0)

# ==========================================================================
# 10.  criticality teeth -- the un-pruned 25-edge truncated PG(2,5)
# ==========================================================================

head("10.  criticality teeth: the 25-edge truncated PG(2,5)")

deg25 = {}
for e in EDGES:
    for v in e:
        deg25[v] = deg25.get(v, 0) + 1
X25 = sum(comb(d, 2) for d in sorted(deg25.values())) - comb(25, 2)
check("THE OBJECT: the UN-PRUNED truncated PG(2,5) is 6-partite, "
      "6-uniform, intersecting, has m = 25 edges, X = 0, Delta = 5 and "
      "tau = 5 -- and it VIOLATES the t = 5 per-edge law by 8 units on "
      "every edge (2*25 + 0 = 50 against 42 + 0).  A real, "
      "constructible object the law would kill",
      len(EDGES) == 25 and X25 == 0
      and max(sorted(deg25.values())) == 5
      and all(sorted(PART[v] for v in e) == [0, 1, 2, 3, 4, 5]
              for e in EDGES)
      and kcover(FULL, 4) is None and kcover(FULL, 5) is not None
      and 2 * 25 + 0 == 50 and 50 - 42 == 8)

t0 = time.time()
tested = 0
withcov = 0
for ei in range(25):
    E2 = FULL & ~(1 << ei)
    outs = sorted(v for v in range(30) if v not in EDGES[ei])
    nn = len(outs)
    MM = [VMASK[v] for v in outs]
    hit = False
    for i1 in range(nn):
        m1 = MM[i1]
        for i2 in range(i1 + 1, nn):
            m2 = m1 | MM[i2]
            for i3 in range(i2 + 1, nn):
                m3 = m2 | MM[i3]
                for i4 in range(i3 + 1, nn):
                    m4 = m3 | MM[i4]
                    for i5 in range(i4 + 1, nn):
                        tested += 1
                        if (m4 | MM[i5]) & E2 == E2:
                            hit = True
    if hit:
        withcov += 1
check("AND WHY IT DOES NOT: EXHAUSTIVELY over all C(24,5) = 42,504 "
      "five-subsets disjoint from each of its 25 edges -- 1,062,600 "
      "subsets tested -- NOT ONE EDGE admits an e-avoiding 5-cover of "
      "the rest.  Every 5-cover of F - e meets e.  That is 0013 (3a) "
      "read backwards: the e-avoiding private cover is a CONSEQUENCE of "
      "criticality, and this object cannot supply it.  THE HYPOTHESIS "
      "IS LOAD-BEARING, and the mutant that drops it is exhibited, not "
      "imagined",
      tested == 25 * comb(24, 5) and tested == 1062600 and withcov == 0,
      "%.1fs" % (time.time() - t0))

sd25 = sum(d * d for d in sorted(deg25.values()))
check("AND THE FINDING THAT FORCES (G) TO CARRY ITS OWN MUTANTS: THE "
      "CRITICALITY MUTANT IS INVISIBLE TO (G).  On this same object "
      "sum_v deg^2 = 750 = m(m-1) + 6m + 2X, so the slot mean is "
      "EXACTLY 5 (750/150), psi_5(5) = 0, and (G)_5 reads 0 <= 0 -- "
      "SATISFIED AT MARGIN EXACTLY ZERO.  The linear law's single best "
      "tooth is worth nothing to (G), which is why section 7 builds "
      "three mutants of its own instead of reusing this one",
      sd25 == 750 and sd25 == 25 * 24 + 6 * 25 + 2 * X25
      and 6 * 25 == 150 and sd25 % 150 == 0 and sd25 // 150 == 5
      and psi5(5) == 0)

# ==========================================================================
# 11.  the margins (D-035), in every coordinate, with one named
# ==========================================================================

head("11.  THE MARGINS (D-035) -- four coordinates, one binding")

M1a = (3 * 456 - 10) * 289 - 2 * 456 * (456 - 26)
M1b = (3 * 456 - 10) * 290 - 2 * 456 * (456 - 26)
check("M1, THE HEADLINE COORDINATE -- AND IT IS NOT THE BINDING ONE.  "
      "The summed chain's per-m slack (3m - 10)X - 2m(m - 26) is 302 at "
      "(m, X) = (456, 289) and 1,660 at (456, 290).  It looks like the "
      "number to quote and it is not: it measures how far the ALREADY "
      "RELAXED law sits from its own floor, which says nothing about "
      "how far the law sits from the truth.  M2 below says that, and "
      "says it is enormous",
      M1a == 302 and M1b == 1660)

check("M2, THE BINDING COORDINATE, NAMED: the Phi-vs-linear RELAXATION "
      "slack.  On the tau = 5 rehearsal core it is 7 per edge, "
      "uniformly, and it is the whole of the law's clearance there.  At "
      "the window ceiling it is enormous: at m = 456 with X near the "
      "floor the slot mean is 78, where psi(78) = 555 against the "
      "linear estimate 78 - 6 = 72 -- the linear law throws away 483 "
      "units per vertex, which is precisely the gap (G) recovers.  THE "
      "HEADLINE COORDINATE (the summed law's per-m slack) IS NOT THE "
      "BINDING ONE",
      psi(78) == 555 and 78 - 6 == 72 and 555 - 72 == 483
      and (456 * 456 + 5 * 456 + 2 * 2259) // (6 * 456) == 78)

check("AND WHAT ENACTMENT CAN AND CANNOT PRICE, said plainly: the "
      "tightest real object this lab can build sits at (m, X, x_e) = "
      "(14, 0, 0) and needs only 2m + 5x_e = 28.  So replacing the "
      "t = 5 constant 42 by 27 GOES RED on it, while ANY constant >= 28 "
      "survives every object available.  ENACTMENT PINS THE t = 6 "
      "CONSTANT 52 ONLY WITHIN [28, 52].  THE CONSTANT RESTS ON THE "
      "DERIVATION OF SECTION 4, NOT ON ENACTMENT",
      2 * mr + 0 == 28 and 28 > 27 and 28 <= 42 and 28 <= 52)


def lift_theta(m, theta):
    X = 0
    while not (2 * X <= m * ((2 * theta + 3 * X - 2 * m) // 5)):
        X += 1
        if X > 5000:
            return None
    return X


check("M4, THE CONSUMED-CAP COORDINATE: the threshold is Theta = "
      "5*sigma + 1 in the cover size sigma = |T_e|, so ONE UNIT OF "
      "sigma MOVES Theta BY FIVE.  sigma = 5 is FORCED by criticality "
      "(tau(K - e) = 5), not assumed -- but the sensitivity is stated: "
      "with Theta = 31, the value obtained by DROPPING the b_i's "
      "entirely (sum_i d_i - 36 in place of - 31), the whole rung "
      "column m = 27..31 collapses from 3, 3, 4, 5, 5 to 0, 0, 0, 0, 0.  "
      "The b_i bookkeeping is worth the entire low end of the law",
      [lift_theta(m, 26) for m in range(27, 32)] == [3, 3, 4, 5, 5]
      and [lift_theta(m, 31) for m in range(27, 32)] == [0, 0, 0, 0, 0])

def ladder_ok(m, X):
    """The THREE-RUNG ladder, each rung used only where C1 licenses it:
    c = 1 at X <= 4, c = 4/3 at X = 5, c = 3/2 above.  The per-edge law
    is m + (1+c) x_e <= c X + 26, lifted by integrality of x_e."""
    if X <= 4:
        return 2 * X <= m * ((X + 26 - m) // 2)
    if X == 5:
        return 2 * X <= m * ((4 * X + 78 - 3 * m) // 7)
    return lin_ok(m, X)


M3 = []
M3B = []
for m in range(27, 32):
    X = 0
    while not ladder_ok(m, X):
        X += 1
    M3.append(X)
    Y = 0
    while not (lin_ok(m, Y) and (Y > 4 or c1_ok(m, Y))):
        Y += 1
    M3B.append(Y)
check("M3, THE CORNER COORDINATE: the ladder of C1 -- c = 1 at X <= 4, "
      "c = 4/3 at X = 5, c = 3/2 above, each rung used only where C1 "
      "licenses it -- moves the low rungs from C4's 3, 3, 4, 5, 5 to "
      "3, 4, 5, 5, 6 at m = 27..31.  Worth one to two units per rung "
      "exactly where the law is weakest.  AND THE c = 4/3 RUNG IS "
      "LOAD-BEARING FOR THE LAST ENTRY: with only c = 1 the m = 31 "
      "rung reads 5, not 6.  Both columns asserted, so the ladder "
      "cannot be quoted as two-rung",
      M3 == [3, 4, 5, 5, 6] and M3B == [3, 4, 5, 5, 5]
      and M3[4] != M3B[4],
      "ladder " + show(M3) + " ; c=1 only " + show(M3B))

check("AND THE INTEGRALITY COORDINATE, priced at the ceiling: dropping "
      "the floor on x_e costs EXACTLY ONE UNIT at m = 456 (290 -> 289) "
      "and one at m = 462 (294 -> 293).  One unit is the whole of what "
      "integrality buys at the top of the window -- and 1 to 2 units "
      "per rung at the bottom, where it matters more (m = 27: 1 -> 3)",
      lin_min(456) - lin_unlift(456) == 1
      and lin_min(462) - lin_unlift(462) == 1
      and lin_unlift(27) == 1 and lin_min(27) == 3)

# ==========================================================================

head("Result")

print("""
  (C1) the corner ladder  c = 1 (X<=4) -> 4/3 (X=5) -> 3/2 (always)
       hence (CC4+): sum_i Phi(d_i-1, 5-b_i) <= I_e <= X - x_e at X <= 4
                                                      PROVEN-BY-CERTIFICATE
  (C2) sum_e I_e <= sum over excessive pairs of
       (lambda-1) * sum_{u in f cap g} (deg u - 2), for ANY X
                                                      PROVEN-BY-CERTIFICATE
  (C3) 2m + 5 x_e <= 52 + 3X  on every edge of every critical core
                                                      PROVEN-BY-CERTIFICATE
  (C4) 2X <= m * floor((52 + 3X - 2m)/5)              PROVEN-BY-CERTIFICATE
  (C5) X <= 2 => m <= 26   (C4)                       PROVEN-BY-CERTIFICATE
       X <= 4 => m <= 28   (C4 + C1, and C1 is load-bearing)
  (C6) (G)  2 * 6m * psihat(mu) <= 3(m-2) X           PROVEN-BY-CERTIFICATE
       X >= 2259 at m = 456, against C4's 290
  (C7) X >= 1 on 431 of the 435 m in [22, 456]        PROVEN-BY-CERTIFICATE
       all but m = 23, 24, 25, 26

  The excess is coupled to the size across the whole window, and the
  coupling is NONLINEAR.  The linear law owns the bottom (it first
  bites at m = 27 and is vacuous below); the second-moment law owns
  the top (it first bites at m = 32 and takes the lead at m = 67).

  OPEN, and flagged: whether (CC+)'s END-TO-END conclusion survives at
  X = 5.  The corner dies there; the witness that kills it has a zero
  left side, so it kills the middle step only, and no evidence exists
  either way.

  THE MARGIN IS THE RELAXATION COORDINATE M2 -- 7 units per edge on
  the one real object, and 483 per vertex at the ceiling.  Real
  objects pin the constant 52 only within [28, 52]; it rests on the
  derivation.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(1 if FAILED else 0)
