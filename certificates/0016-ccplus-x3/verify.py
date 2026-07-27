#!/usr/bin/env python3
"""Certificate 0016 -- the triangle lemma, the sharpened critical-cover
inequality (CC+), and the excess floor X >= 3 at the bottom of the window.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from
lib/.  Runs under Python 3.9 and under python3 -O.  Deterministic.

WHAT IS CLAIMED
---------------
  (T) THE TRIANGLE LEMMA.  In an intersecting family, if e, f, g are
      three DISTINCT edges with |f cap g cap e| >= 2, then X >= 3:
      the three distinct pairs {f,g}, {e,f}, {e,g} each have
      lambda >= 2, and X = sum over ALL pairs of (lambda - 1) with
      every term >= 0.                               PROVEN-BY-CERTIFICATE
      EXTERNAL INPUTS -- NONE.  In-house inputs -- NONE.  (T) is
      self-contained: intersecting-ness and counting, nothing else.

  (CC+) THE SHARPENED CRITICAL-COVER INEQUALITY.  For every edge e of a
      critical core K with X <= 2:                   PROVEN-BY-CERTIFICATE
                                                      (in-house: 0013
          sum_i Phi(d_i - 1, 5 - b_i) <= I_e          private covers;
                                     <= X - x_e       0015 steps (2)-(3);
                                                      external NONE)
      a full factor 3/2 stronger than 0015's (CC), which reads
      2 sum_i Phi(d_i - 1, 5 - b_i) <= 3(X - x_e).

  X >= 3 FOR EVERY CRITICAL CORE AT m = 22           PROVEN-BY-CERTIFICATE
  (every critical core at the window floor is         (in-house: field
  nonlinear, with excess at least three)              0005/0009/0012,
                                                      (D2) 0008, covers
                                                      0013, and 0015 --
                                                      both its steps
                                                      (2)-(3) and its
                                                      certified X >= 2;
                                                      external NONE)

NOTATION.  K is an edge-critical counterexample core to Ryser r = 6
intersecting: finite, 6-partite (V_1..V_6), 6-uniform, intersecting,
tau(K) = 6, tau(K - e) = 5 for every e.  lambda(f,g) = |f cap g| >= 1.
X = sum_v C(deg v, 2) - C(m, 2) = sum over pairs of (lambda - 1).
x_e = sum_{f != e} (lambda(e,f) - 1) >= 0, and sum_e x_e = 2X.
For e's private minimum 5-cover T_e (certificate 0013: T_e cap e = empty,
T_e inside V(K), T_e covers K - e): d_i = deg of e's part-i vertex,
b_i = |T_e cap V_i|, sum_i b_i = 5.  Phi(n, k) = the balanced-split
minimum of sum C(n_j, 2) over k classes totalling n.
w(d) := Phi(d - 1, 5), the cover-free per-vertex weight: w(d) = 0 for
d <= 6, w(7) = 1, w(8) = 2, w(9) = 3.
W := sum_v deg(v) * w(deg v) = sum_e sum_i w(d_i(e)) -- one quantity read
two ways, and a function of the degree multiset alone, which is exactly
what a field configuration is.

THE PROOF, IN ORDER
-------------------
 (1) (T).  Pick distinct u, v in f cap g cap e.  Then u, v lie in each of
     f cap g, e cap f, e cap g, so each of those three pairs has
     lambda >= 2 and contributes >= 1 to X.  The three pairs are distinct
     because e, f, g are.  Section 2 exhausts this over all 5^6
     per-coordinate agreement patterns of a 6-partite triple.

 (2) THE SHARPENED CORNER.  0015's step (4) proves a*b <= (3/2)(s - 1)
     for a + b <= s <= 5, tight at (a,b,s) = (2,3,5).  That corner needs
     a = 2 -- and by (T), a = 2 needs X >= 3.  So at X <= 2 the true
     corner is
         a * b <= s - 1     for a <= 1, a + b <= s, s >= 1,
     proved in TWO CASES, not one chain:
         a = 0:  a*b = 0 <= s - 1, because s >= 1;
         a = 1:  b <= s - a = s - 1, so a*b = b <= s - 1.
     (The one-line chain "a*b <= b <= s - a <= s - 1" is FALSE at a = 0,
     where s - a = s.  It is not written here and must not be.)
     s >= 1 is load-bearing and holds because K - e is a subfamily of an
     intersecting family, so every pair inside it still meets.

 (3) (CC+).  0015 step (2) (pigeonhole) gives sum_i Phi(d_i-1, 5-b_i)
     <= I_e; 0015 step (3) (the accounting identity) gives
     I_e = sum over pairs {f,g} inside K - e of a*b, with
     a = |f cap g cap e|, b = |f cap g cap T_e|, and a + b <= s because
     e cap T_e = empty makes the two sets disjoint subsets of f cap g.
     Apply (2) pairwise and sum: I_e <= sum (s - 1) = X - x_e.

 (4) PER-EDGE BUDGETS.  With the safe relaxation Phi(n, 5-b) >= Phi(n, 5)
     (Phi is nonincreasing in the class count), (CC+) gives
         sum_{v in e} w(deg v) <= X - x_e = 2 - x_e   at X = 2.
     Exhausting degree 6-multisets (entries >= 2 by (A), <= 9 by the
     ladder) the COMPLETE heavy-degree patterns are
         x_e = 0:  {}, {7}, {7,7}, {8}
         x_e = 1:  {}, {7}
         x_e = 2:  {}          (every vertex of such an edge has d <= 6)
     COROLLARY, stated plainly: Delta <= 8 at X = 2, because w(9) = 3 > 2.
     It is NOT load-bearing for the kill -- W <= 24 implies it on its own
     (a degree-9 vertex alone contributes 9*w(9) = 27 > 24).  It is
     reported because it is true and cheap, not because anything needs it.

 (5) THE LAMBDA-TRICHOTOMY OF X = 2.  X = 2 = sum over pairs of
     (lambda - 1) with all terms >= 0, so the excess multiset is (2) or
     (1,1):
        (i)   one lambda-3 pair {f,g}       x-profile {2, 2, 0^20}
        (ii)  two lambda-2 pairs sharing an edge, {f,g},{f,h}
                                            x-profile {2, 1, 1, 0^19}
        (iii) two lambda-2 pairs on four distinct edges
                                            x-profile {1, 1, 1, 1, 0^18}
     Each profile sums to 4 = 2X, as the identity sum_e x_e = 2X demands.

 (6) THE PAIR-SUM.  Exchanging the order of summation (exact, not a
     bound):
         sum_e I_e = sum over EXCESSIVE pairs {f,g} of
                     sum_{e not in {f,g}} a_e * b_e,
     and at X <= 2, a_e <= 1 by (T) -- a_e = 2 would give X >= 3 outright.
     So each contributing e meets f cap g in exactly one vertex, and the
     number of such e is exactly sum_{u in f cap g} (deg u - 2), counted
     once each (deg u - 2 >= 0 since u lies on both f and g).  Each
     contributes a_e*b_e = b_e <= lambda - 1, because the shared vertex
     on e is not in T_e (0013 (3a)) so a_e and b_e count disjoint parts
     of f cap g.  Hence
         W <= sum_e I_e <= sum over excessive pairs of
              (lambda - 1) * sum_{u in f cap g} (deg u - 2).
     An edge may serve two different excessive pairs; nothing is double
     counted, because the exchange of summation is exact and a_e is a
     per-pair quantity.

 (7) W <= 24.  The shared vertices of an excessive pair lie on the
     excess edges themselves, whose budgets from (4) cap their degrees:
        (i)   3 shared vertices, all on f with x_f = 2, so all d <= 6:
              (lambda-1) * sum = 2 * (4+4+4) = 24
        (ii)  4 shared slots, all inside the hub edge f with x_f = 2:
              1*(4+4) + 1*(4+4) = 16
        (iii) 2 shared vertices per pair, both on an edge with x = 1,
              whose whole-edge budget is 1: at most ONE degree-7 among
              them and NO degree-8 -- excluded by the BUDGET (w(8) = 2 > 1),
              not by Delta <= 8.  So (5+4) per pair, 18 in total.
     Therefore W <= max(24, 16, 18) = 24 for a critical core at m = 22
     with X = 2.  Section 5 exhausts all three cases arithmetically.

 (8) THE FIELD.  Over the pinned-ladder configuration field at m = 22
     (0005 (A)(B) + ladder caps 0009/0012, which quantifies over ALL
     counterexamples, cores a fortiori) the X = 2 layer holds 210,713
     configurations.  The (D2) cap of certificate 0008 (2*D2 <= m) kills
     192,744, leaving 17,969, whose minimum W is 27 -- above 24.  Nothing
     survives.  With 0015's certified X >= 2:  X >= 3.

MANDATORY HONESTY NOTES
-----------------------
 (1) PROVENANCE.  The sharpening is IN-HOUSE.  It was found by this
     turn's derivation fleet and re-derived at the desk; no external
     sketch was consumed, and no peer derivation contains it.  The only
     outside object anywhere in this lineage is the turn-9 review that
     seeded plain (CC), already audited and repaired inside 0015.

 (2) THE MARGIN IS IN THE (D2) COORDINATE, AND IT IS ONE UNIT.
     Measured in section 7, in-transcript.  The comfortable-looking
     4 units of W headroom (min W = 28 against the bound 24) is the
     WRONG coordinate to quote.  Relax certificate 0008's cap by a
     single degree-2 vertex -- 2*D2 <= 24 instead of 2*D2 <= 22 -- and
     9 configurations survive W <= 24, the first at D2 = 12, W = 23.
     THE KILL CLOSES BY EXACTLY ONE UNIT OF THE (D2) CAP.  Per D-017 a
     certificate that says "conservative" without saying "margin 1" has
     told the reader only the safe half.

 (3) COVERAGE LIMIT, stated plainly.  In section 3 no randomly generated
     family ever realised X <= 2 AND W > 0 at the same time -- the X <= 2
     regime never produced a vertex of degree 7 or above.  So the two
     halves of the chain are exercised SEPARATELY: (CC+) and the pair-sum
     at X <= 2 with W = 0 on the left, and the pigeonhole / W <= sum I_e
     link at W > 0 with X large.  Their CONJUNCTION is exercised only by
     the field kill itself.  This is unsurprising -- the theorem says
     such objects do not exist at m = 22 -- but the enactment counts must
     not be read as covering more than they do.

 (4) CROSS-REFERENCE, and an erratum against a green certificate.
     Certificate 0015's check 18 ORIGINALLY carried the label "the floor
     lands at exactly X >= 2, not higher".  That LABEL was a claim about
     the FLOOR where only a claim about THAT JUDGE was proven, and this
     certificate disbelieves it.  It is amended by erratum applied in the
     same commit -- 0015's NOTES.md now carries the erratum and its
     check-18 label is reworded.  The CHECK itself is untouched and
     remains true: it asserts alive2 == 9224, a fact about 0015's own
     judge, which at X = 2 reduces to (D2) plus the global form W <= 60
     and genuinely does not decide that layer.  Section 6 here
     re-measures the same field and shows W <= 24 empties it.  PLAN.md
     carried the same superseded wording ("the 9,224 X = 2 survivors
     are the frontier field") and is rewritten in this same commit; the
     turn-11 notebook entry is append-only history and stands as
     written, with the correction recorded in the turn-12 entry.

THE LEDGER, in full
-------------------
  (T)                       EXTERNAL -- NONE.  In-house -- NONE.
                            Intersecting-ness and counting only.
  (CC+)                     EXTERNAL -- NONE.  In-house: 0013 (criticality,
                            private covers, (3a) e cap T_e = empty, T_e in
                            V(K)) and 0015 steps (2)-(3) (the pigeonhole
                            and the accounting identity).  Plus (T).
  X >= 3 at m = 22          additionally: the configuration field
                            (0005 (A)(B) + pinned ladder 0009/0012), the
                            (D2) cap (0008), and certificate 0015's
                            X >= 2 for the rungs below.  EXTERNAL -- NONE.
  the tau = 5 enactment      CONTROL-ONLY: rebuilds 0013's rehearsal core
                            deterministically; an error there reddens this
                            certificate, never greens it.

WHAT THIS DOES NOT CLAIM.  Nothing about m >= 23.  No core is claimed to
exist.  The constant 24 is an X = 2 statement built from the X = 2
trichotomy; section 9 shows it does not transfer to X = 3, where (T) no
longer forbids a = 2 and (CC+) is unavailable.
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


def w(d):
    """The cover-free per-vertex weight Phi(d-1, 5)."""
    return phi(d - 1, 5)


def show(seq):
    """Deterministic printable form of a collection."""
    return ", ".join(str(x) for x in seq)


# ==========================================================================
# 1.  Phi, and the sharpened corner a*b <= s - 1
# ==========================================================================

head("1.  Phi, and the corner that (T) unlocks")

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
check("the four values every budget in this certificate leans on: "
      "Phi(6,5) = 1, Phi(7,5) = 2, Phi(8,5) = 3, Phi(9,5) = 4 -- so a "
      "vertex of degree 7 costs w = 1, degree 8 costs 2, degree 9 costs "
      "3, and degree <= 6 is free.  Phi(8,5) is THREE (the desk's first "
      "sketch of this certificate used 4 and drew the right conclusion "
      "from the wrong number; caught in phase 1)",
      (phi(6, 5), phi(7, 5), phi(8, 5), phi(9, 5)) == (1, 2, 3, 4))
check("Phi is nonincreasing in the class count k for all n <= 10, "
      "1 <= k <= k' <= 6 -- which is exactly what licenses the relaxation "
      "Phi(d-1, 5-b_i) >= Phi(d-1, 5) = w(d) used in every budget below, "
      "whatever the private cover does",
      all(phi(n, k) >= phi(n, kk)
          for n in range(11) for k in range(1, 7) for kk in range(k, 7)))

corner_bad = []
for s in range(1, 21):
    for a in range(0, 2):
        for b in range(0, s + 1 - a):
            if a * b > s - 1:
                corner_bad.append((a, b, s))
check("THE SHARPENED CORNER, exhaustively: a*b <= s - 1 for ALL integers "
      "a, b >= 0 with a <= 1, a + b <= s and 1 <= s <= 20.  Proved in two "
      "cases (a = 0 uses s >= 1; a = 1 uses b <= s - 1), never as the "
      "false one-line chain through s - a",
      corner_bad == [])
check("TEETH, and this is the whole content of the sharpening: at a = 2 "
      "the sharpened corner FAILS -- (a,b,s) = (2,3,5) gives 6 > 4 -- "
      "while 0015's plain corner still holds there (2*6 <= 3*4).  So "
      "(CC+) is FALSE without (T); the hypothesis X <= 2 is doing real "
      "work, not decoration (static arithmetic: this check documents the "
      "boundary, it cannot fail on its own)",
      2 * 3 > 5 - 1 and 2 * (2 * 3) <= 3 * (5 - 1))
check("TEETH: at s = 0 the sharpened corner would read 0 > -1 and FAIL, "
      "so s >= 1 is load-bearing -- and it holds because K - e is a "
      "subfamily of an intersecting family, so every pair inside K - e "
      "still meets.  Intersecting-ness is spent exactly here, on the "
      "a = 0 branch (static arithmetic)",
      0 * 0 > 0 - 1)

# ==========================================================================
# 2.  (T), the triangle lemma -- exhaustive over agreement patterns
# ==========================================================================

head("2.  (T): |f cap g cap e| >= 2 forces X >= 3")

# For a 6-partite triple (e, f, g) the only data that matter to lambda and
# to a are, per coordinate, which of the three coincide.  Five patterns:
#   0 = efg (all equal) | 1 = ef|g | 2 = eg|f | 3 = fg|e | 4 = e|f|g
# lambda(e,f) counts coordinates in {0,1}; lambda(e,g) in {0,2};
# lambda(f,g) in {0,3}; a = |f cap g cap e| counts coordinates in {0}.
PAT = []
for pat in itertools.product(range(5), repeat=6):
    lef = sum(1 for p in pat if p == 0 or p == 1)
    leg = sum(1 for p in pat if p == 0 or p == 2)
    lfg = sum(1 for p in pat if p == 0 or p == 3)
    a = sum(1 for p in pat if p == 0)
    PAT.append((pat, a, lef, leg, lfg))
check("the reduction is complete: all 5^6 = 15,625 per-coordinate "
      "agreement patterns of a 6-partite triple are enumerated (every "
      "pattern is realisable -- three values per part suffice; static "
      "aside), and "
      "exactly 13,629 of them are INTERSECTING, i.e. have all three "
      "pairwise lambdas >= 1",
      len(PAT) == 15625
      and sum(1 for r in PAT if min(r[2], r[3], r[4]) >= 1) == 13629)

INTER = [r for r in PAT if min(r[2], r[3], r[4]) >= 1]
# e == f iff no coordinate separates them, i.e. lambda(e,f) = 6.
NONDEG = [r for r in INTER if r[1] >= 2 and not (r[2] == 6 and r[3] == 6)]
sums_nd = [(r[2] - 1) + (r[3] - 1) + (r[4] - 1) for r in NONDEG]
check("exactly 5,384 intersecting patterns have a = |f cap g cap e| >= 2 "
      "and are not the single fully degenerate pattern e = f = g; on "
      "EVERY one of them the three-pair total "
      "(lambda(f,g)-1) + (lambda(e,f)-1) + (lambda(e,g)-1) is >= 3, and "
      "its minimum over the 5,384 is EXACTLY 3 -- the lemma is tight, "
      "not slack",
      len(NONDEG) == 5384 and min(sums_nd) == 3
      and all(s >= 3 for s in sums_nd))

PAIRWISE = [r for r in INTER
            if r[1] >= 2 and r[2] != 6 and r[3] != 6 and r[4] != 6]
sums_pw = [(r[2] - 1) + (r[3] - 1) + (r[4] - 1) for r in PAIRWISE]
check("PRECISION, and the count that matches (T)'s actual hypothesis: of "
      "those 5,384, exactly 5,216 have e, f and g PAIRWISE distinct "
      "(some coordinate separates each of the three pairs) -- the other "
      "168 have exactly two of the three edges equal, where the 'three "
      "distinct pairs' of (T) collapse to two.  (T) is asserted for the "
      "5,216; the bound holds on all 5,384 anyway, minimum exactly 3 in "
      "both readings",
      len(PAIRWISE) == 5216 and len(NONDEG) - len(PAIRWISE) == 168
      and min(sums_pw) == 3 and all(s >= 3 for s in sums_pw))

A1 = [r for r in INTER
      if r[1] == 1 and r[2] != 6 and r[3] != 6 and r[4] != 6]
check("TEETH: exactly 636 intersecting patterns with pairwise-distinct "
      "edges and a = 1 have three-pair total < 3.  So the hypothesis "
      "a >= 2 is load-bearing and (T) is not vacuously true -- drop it "
      "and the conclusion fails 636 times over",
      sum(1 for r in A1
          if (r[2] - 1) + (r[3] - 1) + (r[4] - 1) < 3) == 636)
note("STATED, NOT TESTED (it is an identity, not a computation): the "
     "excess X of the FULL family is at least the three-pair total "
     "computed above, because X = sum over ALL pairs of (lambda - 1) and "
     "every term of that sum is >= 0 for an intersecting family.  The "
     "patterns above therefore bound X from below, which is the "
     "direction (T) needs")

# ==========================================================================
# 3.  (CC+) and the pair-sum, enacted on random systems
# ==========================================================================

head("3.  (CC+), the pigeonhole and the pair-sum, enacted")


class LCG(object):
    """The house LCG.  Deterministic; identical on every interpreter."""

    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFF

    def next(self):
        self.s = (25214903917 * self.s + 11) & 0xFFFFFFFFFFFF
        return self.s >> 16

    def below(self, k):
        return self.next() % k


RNG = LCG(20260727)


def lam(e, f):
    return sum(1 for i in range(6) if e[i] == f[i])


def degrees(F):
    d = {}
    for f in F:
        for i in range(6):
            key = (i, f[i])
            d[key] = d.get(key, 0) + 1
    return d


def cover5(F, k, size):
    """A set of at most `size` cells, none of them a cell of F[k], hitting
    every other edge of F -- i.e. an explicit private cover T_e with
    T_e cap e = empty covering F - e.  Deterministic branch order."""
    e = F[k]
    others = [f for j, f in enumerate(F) if j != k]
    ecells = set((i, e[i]) for i in range(6))
    chosen = []

    def rec(rem, depth):
        if not rem:
            return list(chosen)
        if depth == 0:
            return None
        f = rem[0]
        for i in range(6):
            c = (i, f[i])
            if c in ecells or c in chosen:
                continue
            chosen.append(c)
            got = rec([g for g in rem if g[c[0]] != c[1]], depth - 1)
            chosen.pop()
            if got is not None:
                return got
        return None

    return rec(others, size)


def pad5(F, e, T):
    """Extend a minimum cover T to EXACTLY five cells outside e,
    lex-first from the family's cell universe.  A superset of a cover
    is a cover, still disjoint from e -- so the enactment is literally
    (CC+) with sum_i b_i = 5, not a weakened form.  (The phase-3 audit
    caught the draft enacting Phi against 5 - b_i while |T| < 5, which
    systematically UNDERSTATES the left side; padding repairs it.)"""
    ecells = set((i, e[i]) for i in range(6))
    out = list(T)
    for c in sorted(set((i, f[i]) for f in F for i in range(6)) - ecells):
        if len(out) >= 5:
            break
        if c not in out:
            out.append(c)
    if len(out) < 5:
        return None
    return sorted(out)


def enact(F, k, T, deg):
    """Returns (I_e by cells, I_e by pairs, the pigeonhole left side, the
    number of parts where the cover concentrates so hard that no cell is
    left outside the part -- b_i = 5 -- while the vertex still has
    degree > 1 (covering alone forbids that; the counter checks it), the
    number of b_i = 5 parts at all, and the largest b_i seen)."""
    e = F[k]
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
        Ip += a * b
    b_i = [sum(1 for (p, u) in T if p == i) for i in range(6)]
    lhs = 0
    degen = 0
    b5 = 0
    for i in range(6):
        cls = 5 - b_i[i]
        n = deg[(i, e[i])] - 1
        if cls > 0:
            lhs += phi(n, cls)
        else:
            b5 += 1
            if n > 0:
                degen += 1
    return I, Ip, lhs, degen, b5, max(b_i)


# ---- (a) random intersecting families with X <= 2 and genuine covers
t0 = time.time()
fams_a = 0
fams_le2 = 0
enacts_a = 0
id_bad = 0
cc_bad = 0
pig_bad_a = 0
tight_a = 0
maxdeg_le2 = 0
degen_cov = 0
b5_seen = 0
max_bi = 0
pad_skip = 0
for trial in range(40000):
    nv = 2 + RNG.below(4)
    target = 3 + RNG.below(7)
    F = []
    for _ in range(400):
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
    if X > 2:
        continue
    fams_le2 += 1
    deg = degrees(F)
    if max(deg.values()) > maxdeg_le2:
        maxdeg_le2 = max(deg.values())
    xs = [sum(lam(F[k], f) - 1 for j, f in enumerate(F) if j != k)
          for k in range(m)]
    for k in range(m):
        T = cover5(F, k, 5)
        if T is None:
            continue
        T = pad5(F, F[k], T)
        if T is None:
            pad_skip += 1
            continue
        I, Ip, lhs, degen, b5, mbi = enact(F, k, T, deg)
        enacts_a += 1
        degen_cov += degen
        b5_seen += b5
        if mbi > max_bi:
            max_bi = mbi
        if I != Ip:
            id_bad += 1
        if I > X - xs[k]:
            cc_bad += 1
        if lhs > I:
            pig_bad_a += 1
        if I == X - xs[k] and I > 0:
            tight_a += 1
check("(CC+) ENACTED.  40,000 LCG trials (house seed 20260727) yield "
      "34,286 random intersecting 6-partite 6-uniform systems reaching "
      "m >= 4; exactly 646 of them have X <= 2; on those, 2,692 (edge, "
      "explicit disjoint cover PADDED TO EXACTLY FIVE CELLS -- a "
      "superset of a cover is a cover, so this is literally (CC+) with "
      "sum b_i = 5) pairs were built, zero padding failures, and every "
      "one satisfies BOTH the accounting identity I_e = sum over pairs "
      "of a*b AND the sharpened bound I_e <= X - x_e -- zero failures "
      "of either, with exactly 175 enactments TIGHT at "
      "I_e = X - x_e > 0, so the bound is exercised at equality and "
      "not only with slack",
      fams_a == 34286 and fams_le2 == 646 and enacts_a == 2692
      and pad_skip == 0 and id_bad == 0 and cc_bad == 0
      and tight_a == 175,
      "%.1fs" % (time.time() - t0))
check("COVERAGE LIMIT, measured rather than asserted: across those 646 "
      "X <= 2 systems the largest vertex degree seen anywhere is 4, so "
      "w = 0 throughout and W = 0 in every single one.  The LEFT half of "
      "the chain (W <= sum_e I_e, the half the theorem actually spends) "
      "is therefore NOT exercised by test (a) at all; it is exercised by "
      "test (b) below, at large X.  The conjunction X <= 2 AND W > 0 is "
      "exercised only by the field kill itself",
      maxdeg_le2 == 4 and pig_bad_a == 0)

# ---- (b) heavy-star systems: the pigeonhole with a POSITIVE left side
t0 = time.time()
hf = 0
pig_n = 0
pig_pos = 0
pig_bad_b = 0
maxlhs = 0
w_n = 0
w_pos = 0
w_bad = 0
w_id_bad = 0
for trial in range(6000):
    nstar = 6 + RNG.below(6)
    extra = RNG.below(3)
    nv = 2 + RNG.below(3)
    F = []
    for _ in range(nstar * 8):
        if sum(1 for f in F if f[0] == 0) >= nstar:
            break
        c = (0,) + tuple(RNG.below(nv) for _ in range(5))
        if c in F:
            continue
        F.append(c)
    for _ in range(extra * 20):
        if len(F) >= nstar + extra:
            break
        c = tuple(RNG.below(nv) for _ in range(6))
        if c in F:
            continue
        if all(lam(c, f) >= 1 for f in F):
            F.append(c)
    m = len(F)
    if m < 6:
        continue
    if not all(lam(p, q) >= 1 for p, q in itertools.combinations(F, 2)):
        continue
    deg = degrees(F)
    sumI = 0
    loc = []
    ok = True
    for k in range(m):
        T = cover5(F, k, 5)
        if T is not None:
            T = pad5(F, F[k], T)
        if T is None:
            ok = False
            break
        I, Ip, lhs, degen, b5, mbi = enact(F, k, T, deg)
        loc.append((I, Ip, lhs))
        degen_cov += degen
        b5_seen += b5
        if mbi > max_bi:
            max_bi = mbi
        sumI += I
    if not ok:
        continue
    hf += 1
    for (I, Ip, lhs) in loc:
        pig_n += 1
        if lhs > 0:
            pig_pos += 1
        if lhs > maxlhs:
            maxlhs = lhs
        if lhs > I:
            pig_bad_b += 1
        if I != Ip:
            id_bad += 1
    Wv = sum(d * w(d) for d in deg.values())
    Wv2 = sum(w(deg[(i, F[k][i])]) for k in range(m) for i in range(6))
    if Wv2 != Wv:
        w_id_bad += 1
    w_n += 1
    if Wv > 0:
        w_pos += 1
    if Wv > sumI:
        w_bad += 1
check("THE PIGEONHOLE WITH A POSITIVE LEFT SIDE (the refuter's design, "
      "supplying what test (a) cannot).  Of 6,000 LCG trials, 5,980 "
      "heavy-star systems qualify (1 rejected as non-intersecting, 19 "
      "for a cell universe too small to pad a cover to five); every "
      "edge carries a disjoint cover padded to exactly five cells; "
      "56,584 per-edge enactments of sum_i Phi(d_i-1, 5-b_i) <= I_e, "
      "of which 54,119 have a STRICTLY POSITIVE left side (largest "
      "seen: 27).  Zero failures",
      hf == 5980 and pig_n == 56584 and pig_pos == 54119 and maxlhs == 27
      and pig_bad_b == 0,
      "%.1fs" % (time.time() - t0))
check("THE W LINK, also with a positive left side: W = sum_v deg(v)*w(deg v) "
      "<= sum_e I_e holds on all 5,980 of those systems, and on 5,457 of "
      "them W is strictly positive -- so the inequality the field kill "
      "actually spends is exercised nonvacuously, just never simultaneously "
      "with X <= 2.  The TWO READINGS of W (per-vertex and per-edge sums) "
      "were computed separately on every system and agree every time -- "
      "the interface identity that lets a core be judged by its degree "
      "multiset alone, which is the hinge of the field kill",
      w_n == 5980 and w_pos == 5457 and w_bad == 0 and w_id_bad == 0)
check("HONEST SCOPE of the b_i = 5 well-definedness guard: across all "
      "59,276 padded-cover enactments of tests (a) and (b) the largest "
      "b_i ever seen is 4 (measured, asserted) -- the b_i = 5 "
      "concentration NEVER AROSE, so the in-run guard is unexercised "
      "and supplies no evidence.  The well-definedness of (CC+) at "
      "b_i = 5 rests on the covering argument alone: all five cover "
      "cells in part i leave the d_i - 1 sibling edges through v_i no "
      "cell to hit, forcing d_i = 1 and a zero Phi term",
      degen_cov == 0 and b5_seen == 0 and max_bi == 4
      and enacts_a + pig_n == 59276)

# ---- (c) the pair-sum, and the mutant that drops (lambda - 1)
t0 = time.time()
ps_n = 0
ps_nz = 0
ps_bad = 0
mut_bad = 0
for trial in range(20000):
    nv = 2 + RNG.below(3)
    target = 5 + RNG.below(6)
    F = []
    for _ in range(400):
        if len(F) >= target:
            break
        c = tuple(RNG.below(nv) for _ in range(6))
        if c in F:
            continue
        if all(lam(c, f) >= 1 for f in F):
            F.append(c)
    m = len(F)
    if m < 5:
        continue
    good = True
    for f, g, h in itertools.combinations(F, 3):
        if sum(1 for i in range(6) if f[i] == g[i] == h[i]) >= 2:
            good = False
            break
    if not good:
        continue
    deg = degrees(F)
    sumI = 0
    short = False
    for k in range(m):
        e = F[k]
        cells = sorted(set((i, f[i]) for f in F for i in range(6))
                       - set((i, e[i]) for i in range(6)))
        if len(cells) < 5:
            short = True
            break
        pool = list(cells)
        T = []
        for _ in range(5):
            T.append(pool.pop(RNG.below(len(pool))))
        I, Ip, lhs, degen, b5, mbi = enact(F, k, sorted(T), deg)
        if I != Ip:
            id_bad += 1
        sumI += I
    if short:
        continue
    rhs = 0
    mut = 0
    for f, g in itertools.combinations(F, 2):
        L = lam(f, g)
        if L >= 2:
            base = sum(deg[(i, f[i])] - 2 for i in range(6) if f[i] == g[i])
            rhs += (L - 1) * base
            mut += base
    ps_n += 1
    if rhs > 0:
        ps_nz += 1
    if sumI > rhs:
        ps_bad += 1
    if sumI > mut:
        mut_bad += 1
check("THE PAIR-SUM as pure combinatorics.  On 1,446 of 20,000 LCG "
      "trials -- those reaching m >= 5 and satisfying the hypothesis "
      "a_e <= 1 by construction (no triple shares two vertices), with "
      "at least five paddable cells -- carrying ARBITRARY disjoint 5-sets "
      "T_e rather than covers -- which is all the pair-sum needs -- "
      "sum_e I_e <= sum over excessive pairs of "
      "(lambda-1) * sum_{u in f cap g} (deg u - 2) holds every time, and "
      "the right side is nonzero in all 1,446, so the test is nonvacuous",
      ps_n == 1446 and ps_nz == 1446 and ps_bad == 0,
      "%.1fs" % (time.time() - t0))
check("MUTANT, and it FAILS as it must: drop the (lambda - 1) factor from "
      "the pair-sum and the resulting inequality is FALSE on exactly 119 "
      "of those same 1,446 systems.  The factor is load-bearing and this "
      "test can go red -- it is not a tautology dressed as a check",
      mut_bad == 119 and mut_bad > 0)
check("the accounting identity I_e = sum over pairs of a*b was checked on "
      "every enactment of all three tests -- (a), (b) and (c) together, "
      "with covers and with arbitrary disjoint 5-sets -- and failed zero "
      "times.  It needs only T_e cap e = empty, not that T_e covers "
      "anything",
      id_bad == 0)
note("STATED, NOT TESTED: in test (c) the sets T_e are arbitrary disjoint "
     "5-sets, not private covers.  That is deliberate and it is the "
     "honest scope of the pair-sum, which is a statement about the "
     "exchange of summation and the corner, not about covering.  A "
     "critical core supplies covers as well (0013), which is strictly "
     "more than the pair-sum consumes")
note("STATED, NOT TESTED here (verified by the phase-2 refuter, whose "
     "record is in NOTES.md): the two bookkeeping claims inside the "
     "pair-sum derivation -- 'exactly deg(u) - 2 accounting edges per "
     "shared vertex u, counted once each' and 'an edge serving two "
     "excessive pairs is not double counted' -- were checked by the "
     "refuter against actual edge counts on 390 pair enactments (zero "
     "discrepancies) and on 18 families exhibiting a two-pair edge "
     "(zero failures).  Test (c) above exercises both en masse through "
     "the inequality itself")

# ==========================================================================
# 4.  Per-edge budgets and the complete heavy-degree patterns
# ==========================================================================

head("4.  budgets: what an edge of a critical core may carry at X = 2")

PATTERNS = {}
MAXDEG = {}
for xe in (0, 1, 2):
    pats = set()
    md = 0
    for ms in itertools.combinations_with_replacement(range(2, 10), 6):
        if sum(w(d) for d in ms) <= 2 - xe:
            pats.add(tuple(sorted((d for d in ms if d >= 7), reverse=True)))
            if max(ms) > md:
                md = max(ms)
    PATTERNS[xe] = sorted(pats)
    MAXDEG[xe] = md
check("EXHAUSTIVE over all degree 6-multisets with entries in 2..9 "
      "(>= 2 is lemma (A) of 0005; <= 9 is the pinned ladder's top cap): "
      "the budget sum_{v in e} w(deg v) <= 2 - x_e admits the heavy "
      "patterns {} / {7} / {7,7} / {8} at x_e = 0, exactly {} / {7} at "
      "x_e = 1, and exactly {} at x_e = 2 -- COMPLETE lists, nothing "
      "else survives",
      PATTERNS[0] == [(), (7,), (7, 7), (8,)]
      and PATTERNS[1] == [(), (7,)]
      and PATTERNS[2] == [()])
check("at x_e = 2 the budget is zero, so EVERY vertex of such an edge has "
      "degree <= 6 -- the fact case (i) and case (ii) of the "
      "trichotomy spend; at x_e = 1 the ceiling is 7 and at x_e = 0 it "
      "is 8",
      MAXDEG[2] == 6 and MAXDEG[1] == 7 and MAXDEG[0] == 8)
check("COROLLARY Delta <= 8 at X = 2: no admissible multiset at any x_e "
      "contains a 9, because w(9) = 3 exceeds every budget 2 - x_e <= 2. "
      "Stated plainly and separately: this corollary is NOT load-bearing "
      "for the kill.  The W <= 24 bound implies it on its own, since a "
      "single degree-9 vertex contributes 9*w(9) = 27 > 24",
      max(MAXDEG.values()) == 8 and 9 * w(9) == 27 and 27 > 24)
note("STATED, NOT TESTED: Lemma 1.2 (0015's bookkeeping, re-derived from "
     "6-uniformity alone) also fixes sum_i d_i(e) = m + 5 + x_e = 27 + x_e "
     "at m = 22.  The pattern lists above do not use it -- they are pure "
     "budget statements -- so the row sum is available as an independent "
     "constraint wherever a later rung wants it")

# ==========================================================================
# 5.  The lambda-trichotomy of X = 2 and the bound W <= 24
# ==========================================================================

head("5.  the three lambda-shapes of X = 2, and W <= 24")

# Case (i): one lambda-3 pair {f,g}.  Its three shared vertices all lie on
# f, and x_f = 2, so each has degree <= 6.  Factor lambda - 1 = 2.
best_i = 0
for t in itertools.combinations_with_replacement(range(2, 13), 3):
    if sum(w(d) for d in t) > 0:          # the whole-edge budget at x_f = 2
        continue
    best_i = max(best_i, 2 * sum(d - 2 for d in t))
# Case (ii): two lambda-2 pairs sharing the hub edge f, x_f = 2, so all
# four shared slots lie inside f and carry degree <= 6.  Factor 1 each.
best_ii = 0
for t in itertools.combinations_with_replacement(range(2, 13), 4):
    if sum(w(d) for d in t) > 0:
        continue
    best_ii = max(best_ii, sum(d - 2 for d in t))
# Case (iii): four distinct edges, each with x = 1.  A pair's two shared
# vertices both lie on one such edge, whose whole-edge budget is 1.
best_pair = 0
for t in itertools.combinations_with_replacement(range(2, 13), 2):
    if sum(w(d) for d in t) > 1:
        continue
    best_pair = max(best_pair, sum(d - 2 for d in t))
check("CASE (i), one lambda-3 pair (x-profile {2,2,0^20}), exhaustively "
      "over shared-vertex degree triples with entries 2..12: the pair-sum "
      "right side maxes at 2*((6-2)+(6-2)+(6-2)) = 24.  The cap on those "
      "three degrees is the x_f = 2 budget of section 4, not a "
      "global Delta",
      best_i == 24)
check("CASE (ii), two lambda-2 pairs sharing an edge (x-profile "
      "{2,1,1,0^19}): all four shared slots lie inside the hub edge f, "
      "whose x_f = 2 budget forces degree <= 6, so the right side maxes "
      "at (4+4) + (4+4) = 16",
      best_ii == 16)
check("CASE (iii), two lambda-2 pairs on four distinct edges (x-profile "
      "{1,1,1,1,0^18}): each pair's two shared vertices sit on one edge "
      "of whole-edge budget 1, so AT MOST ONE of them has degree 7 and "
      "NEITHER has degree 8 -- degree 8 is excluded by the BUDGET "
      "(w(8) = 2 > 1), not by Delta <= 8.  Per pair the maximum is "
      "(7-2) + (6-2) = 9, and 18 in total",
      best_pair == 9 and 2 * best_pair == 18)
check("THEREFORE W <= max(24, 16, 18) = 24 for every critical core at "
      "m = 22 with X = 2.  The trichotomy is complete (2 = 2 or 1+1 as a "
      "sum of positive pair-excesses, and two distinct pairs either share "
      "an edge or do not), so these three cases exhaust the shape space",
      max(best_i, best_ii, 2 * best_pair) == 24)
check("the comparator, in arithmetic: summing (CC+) over the 22 edges "
      "WITHOUT the lambda-shape analysis gives only "
      "W <= sum_e (X - x_e) = mX - 2X = (m-2)X = 40, since sum_e x_e = 2X. "
      "The shape analysis is worth 40 - 24 = 16 units of W.  What those "
      "16 units buy on the real field is MEASURED in section 6, not "
      "asserted here (static arithmetic: this comparator cannot fail on "
      "its own)",
      (22 - 2) * 2 == 40 and 40 - 24 == 16)

# ==========================================================================
# 6.  The field kill at m = 22
# ==========================================================================

head("6.  the field: the X = 2 layer at m = 22 is empty")

LADDER = {1: 2, 2: 4, 3: 6, 4: 9, 5: 13}
M = 22
TARGET = comb(M, 2)


def profiles(m, ladder):
    caps = {k: m - ladder[6 - k] for k in range(1, 6)}
    out = []

    def rec(left, cur):
        k = len(cur)
        if k in caps and sum(cur) > caps[k]:
            return
        if left == 0:
            if len(cur) >= 6:
                out.append(tuple(cur))
            return
        for s in range(min(left, cur[-1] if cur else m - ladder[5]), 1, -1):
            if 0 < left - s < 2:
                continue
            rec(left - s, cur + [s])
    rec(m, [])
    return out


def sc(p):
    return sum(comb(d, 2) for d in p)


P22 = sorted(profiles(M, LADDER), key=sc)
S22 = [sc(p) for p in P22]
PW = [sum(d * w(d) for d in p) for p in P22]
PD2 = [sum(1 for d in p if d == 2) for p in P22]
PMX = [max(p) for p in P22]
P7 = [sum(1 for d in p if d == 7) for p in P22]
P8 = [sum(1 for d in p if d == 8) for p in P22]
P9 = [sum(1 for d in p if d == 9) for p in P22]
check("the pinned-ladder profile list at m = 22 has 67 members (entries "
      ">= 2 by 0005 (A), at least 6 entries by 0005 (B), prefix caps "
      "top-k <= 22 - N(6-k) from the ladder 0009/0012) -- rebuilt here "
      "with 0015's own construction, so the two certificates quantify "
      "over the same field",
      len(P22) == 67)


def scan(xmax):
    found = []
    n = len(P22)

    def rec(start, k, tot, cur):
        if k == 6:
            if TARGET <= tot <= TARGET + xmax:
                found.append(tuple(cur))
            return
        rem = 6 - k
        for i in range(start, n):
            t2 = tot + S22[i]
            if t2 + (rem - 1) * S22[i] > TARGET + xmax:
                break
            if t2 + (rem - 1) * S22[-1] < TARGET:
                continue
            cur.append(i)
            rec(i, k + 1, t2, cur)
            cur.pop()
    rec(0, 0, 0, [])
    return found


t0 = time.time()
ALLCF = scan(3)
CF2 = []
SW = {0: [], 1: [], 2: [], 3: []}
SD2 = {0: [], 1: [], 2: [], 3: []}
SDM = {0: [], 1: [], 2: [], 3: []}
S789 = {0: [], 1: [], 2: [], 3: []}
for c in ALLCF:
    x = 0
    ww = 0
    d2 = 0
    dm = 0
    n7 = 0
    n8 = 0
    n9 = 0
    for i in c:
        x += S22[i]
        ww += PW[i]
        d2 += PD2[i]
        n7 += P7[i]
        n8 += P8[i]
        n9 += P9[i]
        if PMX[i] > dm:
            dm = PMX[i]
    x -= TARGET
    SW[x].append(ww)
    SD2[x].append(d2)
    SDM[x].append(dm)
    if x == 2:
        S789[2].append((n7, n8, n9))
        CF2.append(c)
del ALLCF
SCAN_T = time.time() - t0

check("the X = 2 layer of the field holds exactly 210,713 configurations "
      "(6-multisets of profiles with total degree-pair sum 233 = 231 + 2)",
      len(SW[2]) == 210713, "%.1fs for the whole X <= 3 scan" % SCAN_T)

n2 = len(SW[2])
d2_kill = sum(1 for k in range(n2) if 2 * SD2[2][k] > M)
d2_pass = [k for k in range(n2) if 2 * SD2[2][k] <= M]
check("THE KILL, in the order that spends (D2) first: certificate 0008's "
      "cap 2*D2 <= m kills 192,744 of the 210,713, leaving 17,969; the "
      "MINIMUM W over those 17,969 survivors is 27, strictly above the "
      "bound W <= 24 of section 5, so W <= 24 kills every one of them "
      "and ZERO configurations survive.  No critical core at m = 22 has "
      "X = 2",
      d2_kill == 192744 and len(d2_pass) == 17969
      and min(SW[2][k] for k in d2_pass) == 27
      and sum(1 for k in d2_pass if SW[2][k] <= 24) == 0)

w_pass = [k for k in range(n2) if SW[2][k] <= 24]
check("THE KILL, in the other order: W <= 24 alone leaves 843 of the "
      "210,713, and EVERY one of those 843 carries at least 12 "
      "degree-2 vertices -- the minimum is exactly 12, one above the "
      "(D2) cap of 11.  Both orders end at zero, and this one shows "
      "where the theorem is thin",
      len(w_pass) == 843 and min(SD2[2][k] for k in w_pass) == 12
      and all(SD2[2][k] >= 12 for k in w_pass))

check("NOT TOO WEAK, measured (section 5's comparator on the real "
      "field): keep Delta <= 8 and (D2) but replace W <= 24 by the "
      "un-shaped global bound W <= (m-2)X = 40, and 286 configurations "
      "survive.  The lambda-shape analysis of section 5 is worth exactly "
      "those 286 configurations -- 16 units of W, and the difference "
      "between a kill and no kill",
      sum(1 for k in range(n2)
          if SDM[2][k] <= 8 and 2 * SD2[2][k] <= M and SW[2][k] <= 40) == 286)

check("CONCLUSION: not one of the 210,713 configurations in the X = 2 "
      "layer satisfies BOTH 2*D2 <= 22 and W <= 24, so no critical core "
      "at m = 22 has X = 2.  Certificate 0015 proved X >= 2 for every "
      "critical core at m = 22; therefore X >= 3 FOR EVERY CRITICAL CORE "
      "AT m = 22.  Both ingredients are re-measured in this run -- "
      "0015's X <= 1 field totals in section 8, the X = 2 emptiness here",
      sum(1 for k in range(n2)
          if 2 * SD2[2][k] <= M and SW[2][k] <= 24) == 0
      and n2 == 210713)
note("STATED, NOT TESTED (0015's erratum, applied in the same commit): "
     "0015's check-18 LABEL originally read 'the floor lands at exactly "
     "X >= 2, not higher' -- a claim about the FLOOR where only a claim "
     "about THAT JUDGE was proven.  It is reworded and an erratum is in "
     "0015's NOTES.  Its CHECK is untouched and still true: alive2 == "
     "9224 is a fact about 0015's own judge, which at X = 2 reduces to "
     "(D2) plus the global form W <= 60 and simply does not decide that "
     "layer")

# ==========================================================================
# 7.  The margin (D-017): one unit of the (D2) cap
# ==========================================================================

head("7.  THE MARGIN -- and it is not where it looks")

sweep = []
for R in (22, 23, 24, 26, 28):
    sweep.append(sum(1 for k in w_pass if 2 * SD2[2][k] <= R))
check("THE (D2) SENSITIVITY SWEEP, in-transcript: the number of X = 2 "
      "configurations satisfying BOTH W <= 24 and 2*D2 <= R, for "
      "R = 22 (the true cap), 23, 24, 26, 28, is 0, 0, 9, 66, 218.  ONE "
      "additional degree-2 vertex -- R = 24 instead of 22 -- and nine "
      "configurations survive the whole chain.  THE KILL CLOSES BY "
      "EXACTLY ONE UNIT OF THE (D2) CAP",
      sweep == [0, 0, 9, 66, 218], "sweep = " + show(sweep))

near = sorted([tuple(sorted((P22[i] for i in CF2[k]), reverse=True))
               for k in w_pass if SD2[2][k] == 12])
NAMED = ((8, 5, 3, 2, 2, 2), (7, 6, 3, 2, 2, 2), (6, 6, 3, 3, 2, 2),
         (6, 6, 3, 3, 2, 2), (6, 6, 3, 3, 2, 2), (6, 4, 3, 3, 3, 3))
print("  the nine near-misses at D2 = 12 (each has W <= 24 and dies ONLY "
      "on (D2)):", flush=True)
for cfg in near:
    print("      " + show(cfg), flush=True)
nm = [k for k in w_pass if SD2[2][k] == 12
      and tuple(sorted((P22[i] for i in CF2[k]), reverse=True)) == NAMED]
check("THE NEAR-MISS, exhibited: exactly 9 field configurations have "
      "W <= 24 and D2 = 12, and the named witness is one of them -- "
      "profiles (8,5,3,2,2,2), (7,6,3,2,2,2), (6,6,3,3,2,2) three times, "
      "(6,4,3,3,3,3) -- with X = 2, Delta = 8, D2 = 12 and W = 23 <= 24. "
      "It satisfies EVERY other rule this certificate proves; only "
      "2*D2 <= 22 stops it",
      len(near) == 9 and len(nm) == 1
      and SW[2][nm[0]] == 23 and SDM[2][nm[0]] == 8 and SD2[2][nm[0]] == 12)

cand = [k for k in range(n2) if SDM[2][k] <= 8 and 2 * SD2[2][k] <= M]
minW = min(SW[2][k] for k in cand)
mins = sorted([tuple(sorted((P22[i] for i in CF2[k]), reverse=True))
               for k in cand if SW[2][k] == minW])
MINS_PINNED = sorted([
    ((7, 6, 3, 2, 2, 2), (7, 6, 3, 2, 2, 2), (7, 6, 3, 2, 2, 2),
     (7, 3, 3, 3, 3, 3), (6, 6, 3, 3, 2, 2), (6, 4, 3, 3, 3, 3)),
    ((7, 6, 3, 2, 2, 2), (7, 6, 3, 2, 2, 2), (7, 3, 3, 3, 3, 3),
     (7, 3, 3, 3, 3, 3), (6, 6, 4, 2, 2, 2), (6, 6, 3, 3, 2, 2)),
    ((7, 6, 3, 2, 2, 2), (7, 6, 3, 2, 2, 2), (7, 4, 3, 3, 3, 2),
     (7, 3, 3, 3, 3, 3), (6, 6, 3, 3, 2, 2), (6, 6, 3, 3, 2, 2))])
print("  the three W-minimizers under Delta <= 8 + (D2):", flush=True)
for cfg in mins:
    print("      " + show(cfg), flush=True)
check("THE W CLIFF: over the 4,160 configurations passing Delta <= 8 and "
      "(D2), the minimum W is EXACTLY 28, attained by EXACTLY 3 "
      "configurations, each with degree-7/8/9 census (4, 0, 0) -- four "
      "degree-7 vertices, nothing heavier -- and each sitting exactly ON "
      "the (D2) boundary at D2 = 11.  The three are printed above and "
      "asserted here",
      len(cand) == 4160 and minW == 28 and len(mins) == 3
      and mins == MINS_PINNED
      and all(S789[2][k] == (4, 0, 0) and SD2[2][k] == 11
              for k in cand if SW[2][k] == minW))

min27 = [k for k in d2_pass if SW[2][k] == 27]
check("and the same minimum WITHOUT the degree cap: over the "
      "(D2)-passers alone the minimum W is 27, attained by exactly 3 "
      "configurations, EVERY one with degree-7/8/9 census (0, 0, 1) -- "
      "a single degree-9 vertex, 9*w(9) = 27, asserted rather than "
      "stated.  27 > 24 too, so the kill does not need Delta <= 8 -- "
      "consistent with section 4's plain statement that the corollary "
      "is not load-bearing",
      min(SW[2][k] for k in d2_pass) == 27 and len(min27) == 3
      and all(S789[2][k] == (0, 0, 1) for k in min27))
note("STATED, NOT TESTED, and it is the maintenance instruction: all "
     "three W-minimizers sit ON the (D2) boundary, D2 = 11 = floor(m/2). "
     "If certificate 0008's cap is ever weakened -- to D2 <= 12, say -- "
     "the minimum must be recomputed BEFORE this kill is re-quoted; the "
     "sweep above shows it would then fail with 9 survivors")

# ==========================================================================
# 8.  Rung-down controls (0015 remains the authority for X <= 1)
# ==========================================================================

head("8.  controls one and two rungs down")

check("the X <= 1 layer of the field holds 506,204 configurations, "
      "splitting as X = 0: 267,965 and X = 1: 238,239 -- 0015's own "
      "total, reproduced here by an independent scan of the same field. "
      "0015 remains the authority for X <= 1; this is a consistency "
      "control, not a re-proof",
      len(SW[0]) + len(SW[1]) == 506204
      and len(SW[0]) == 267965 and len(SW[1]) == 238239)

p1 = [k for k in range(len(SW[1])) if SDM[1][k] <= 7 and 2 * SD2[1][k] <= M]
best1 = 0
for t in itertools.combinations_with_replacement(range(2, 13), 2):
    if sum(w(d) for d in t) <= 0:
        best1 = max(best1, sum(d - 2 for d in t))
check("AT X = 1 this certificate's own machinery closes the rung WITHOUT "
      "0015's star-disjointness rule.  X = 1 has exactly one excessive "
      "pair, a lambda-2 pair {f,g}, and x_f = x_g = 1, so BOTH its edges "
      "have budget X - x_e = 0 and every one of their degrees is <= 6; "
      "the two shared vertices lie on f, so the pair-sum gives "
      "W <= 1*((6-2)+(6-2)) = 8 -- exhausted over shared-vertex degree "
      "pairs under the budget, like section 5's cases, not prose.  The "
      "same budget gives Delta <= 7.  Field: exactly 47 configurations "
      "pass Delta <= 7 and (D2), and their minimum W is 28 -- far above "
      "8, so the rung is empty",
      best1 == 8 and len(p1) == 47
      and min(SW[1][k] for k in p1) == 28 and 28 > 8)

p0 = [k for k in range(len(SW[0])) if SDM[0][k] <= 6 and 2 * SD2[0][k] <= M]
check("AT X = 0 there is no excessive pair at all, so every I_e = 0, so "
      "W <= 0 and Delta <= 6.  Field: ZERO configurations even pass "
      "Delta <= 6 together with (D2) -- the rung is empty before the W "
      "bound is applied",
      len(p0) == 0)

# ==========================================================================
# 9.  NOT TOO STRONG: the X = 3 frontier is alive
# ==========================================================================

head("9.  not too strong -- X = 3 survives, and must")

n3 = len(SW[3])
alive3 = sum(1 for k in range(n3)
             if 2 * SD2[3][k] <= M and SDM[3][k] <= 9 and SW[3][k] <= 90)
alive3_nod = sum(1 for k in range(n3)
                 if 2 * SD2[3][k] <= M and SW[3][k] <= 90)
check("the X = 3 layer holds 186,086 configurations, and the rules that "
      "remain available there -- (D2), the ladder's own Delta <= 9, and "
      "PLAIN (CC)'s global form 2W <= 3(m-2)X, i.e. W <= 90 -- leave "
      "15,340 of them ALIVE.  Strictly positive, and asserted as such: "
      "this certificate stops exactly where its evidence stops.  The "
      "Delta <= 9 clause is INERT (the count is identical without it -- "
      "the ladder's own top cap enforces it upstream), asserted so no "
      "filter is priced as load-bearing that is not",
      n3 == 186086 and alive3 == 15340 and alive3 > 0
      and alive3_nod == alive3,
      "%d alive at X = 3" % alive3)

c3 = [k for k in range(n3) if SDM[3][k] <= 8 and 2 * SD2[3][k] <= M]
check("and the W floor moves with the rung: over the X = 3 configurations "
      "passing Delta <= 8 and (D2) the minimum W is 30 (it was 28 at "
      "X = 2).  Re-derived here, matching the independent "
      "reimplementation's measurement",
      len(c3) > 0 and min(SW[3][k] for k in c3) == 30)
note("STATED, NOT TESTED, and it is a warning: at X = 3 the triangle "
     "lemma no longer forbids a = |f cap g cap e| = 2, so (CC+) is "
     "UNAVAILABLE and the constant 24 DOES NOT TRANSFER.  The whole "
     "lambda-case analysis of section 5 must be redone at X = 3 -- the "
     "shape space there includes a lambda-4 pair and a codegree-3 "
     "triangle, neither of which occurs at X = 2.  Anyone reusing 24 one "
     "rung up is reusing an X = 2 theorem outside its hypothesis")

# ==========================================================================
# 10.  tau = 5 enactment on 0013's real rehearsal core
# ==========================================================================

head("10.  the tau = 5 rehearsal core -- a real object the chain must not "
     "contradict")


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
VMASK = [0] * 30
for ei, e in enumerate(EDGES):
    for v in e:
        VMASK[v] |= (1 << ei)
FULL = (1 << 25) - 1


def kcover(E, k):
    for c in itertools.combinations(range(30), k):
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
    for ei in list(active):
        E2 = E & ~(1 << ei)
        if kcover(E2, 4) is None:
            active.remove(ei)
            E = E2
            changed = True
            break
CE = [EDGES[i] for i in active]
mr = len(CE)
degr = {}
for e in CE:
    for v in e:
        degr[v] = degr.get(v, 0) + 1
Xr = sum(comb(d, 2) for d in degr.values()) - comb(mr, 2)
check("the deterministic rebuild reproduces certificate 0013's rehearsal "
      "core from PG(2,5) -- 14 edges, excess X = 0 (inside a projective "
      "plane every two lines meet exactly once) -- the same construction "
      "0015 section 4 runs (identical in structure; two locals renamed, "
      "and the parts/covers blocks this section does not need are "
      "omitted)",
      mr == 14 and Xr == 0, "%.1fs" % (time.time() - t0))

check("its maximum degree is EXACTLY 5, and that is the falsification "
      "opportunity taken: the tau = 5 analog of (CC+) at X = 0 gives "
      "budget X - x_e = 0 on every edge, so EVERY Phi(d_i - 1, 4 - b_i) "
      "must vanish; with the safe relaxation Phi(d_i - 1, 4) = 0 that "
      "forces d_i <= 5 on every vertex.  A single degree-6 vertex in "
      "this real object would have falsified the chain outright.  There "
      "is none -- and it clears by exactly one",
      max(degr.values()) == 5)

tri = 0
for f, g, h in itertools.combinations(CE, 3):
    if len(f & g & h) > tri:
        tri = len(f & g & h)
check("the analog of (T) on the same real object: over ALL C(14,3) = 364 "
      "edge triples the maximum of |f cap g cap e| is 1, exactly as (T) "
      "demands at X = 0 -- a triple with 2 would force X >= 3 and this "
      "object has X = 0",
      comb(mr, 3) == 364 and tri == 1)

Wprime = sum(d * phi(d - 1, 4) for d in degr.values())
check("and the analog weight W' = sum_v deg(v)*Phi(deg(v)-1, 4) is 0 on "
      "the core, as the X = 0 budget forces -- the chain and the object "
      "agree at margin exactly zero, which is where a sign or factor "
      "error would show",
      Wprime == 0)
note("STATED, NOT TESTED: this section is CONTROL-ONLY.  The rehearsal "
     "core is a tau = 5 object and cannot witness anything about tau = 6 "
     "counterexamples; it can only redden this certificate, never green "
     "it.  Note also that it carries three degree-1 vertices, so lemma "
     "(A) does not hold on it -- correctly, since (A) binds tau = 6 "
     "counterexamples and the chain never applies it here")

# ==========================================================================

head("Result")

print("""
  (T)   distinct e,f,g with |f cap g cap e| >= 2  =>  X >= 3
                                                      PROVEN-BY-CERTIFICATE
        (intersecting-ness and counting only; external NONE, in-house NONE)

  (CC+) sum_i Phi(d_i - 1, 5 - b_i) <= I_e <= X - x_e  at X <= 2
                                                      PROVEN-BY-CERTIFICATE
        (in-house: 0013 covers, 0015 steps (2)-(3), and (T))

  X >= 3 FOR EVERY CRITICAL CORE AT m = 22            PROVEN-BY-CERTIFICATE
        (field 0005/0009/0012; (D2) 0008; 0015's X >= 2; external NONE)

  The corner inside (CC) is not tight when the excess is small: a = 2
  needs three excessive pairs, and at X <= 2 there are not three to be
  had.  Removing that slack removes a factor 3/2 from every budget, and
  the budgets then cap the degrees of exactly the vertices the excess
  runs through -- W <= 24 against a field minimum of 27.  The X = 2
  layer is empty.

  THE MARGIN IS ONE UNIT OF (D2), not the four units of W it resembles.
  Relax certificate 0008's cap by a single degree-2 vertex and nine
  configurations live, the first at D2 = 12, W = 23.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(1 if FAILED else 0)
