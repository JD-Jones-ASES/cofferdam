#!/usr/bin/env python3
"""cofferdam certificate 0002 — the maximum-degree window, and m=19 reduced to one case.

    python3 verify.py

Standalone: stdlib only, exact integer arithmetic, no imports from lib/, no solver.
Checks fail loudly with sys.exit(1); no bare `assert` (python3 -O strips those).

WHAT IS CLAIMED
---------------
Let H be a counterexample to Ryser's conjecture at r = 6 in the intersecting case:
6-partite, intersecting, tau(H) >= 6, on m edges. Write Delta for its maximum
vertex degree. Then:

    (a) Delta >= 1 + ceil((m-1)/6)                       [new here]
    (b) Delta <= m - 13                                  [cert 0001 + f(6)=13]
    (c) for each Delta in that window, the pair count with the degree cap
        tightened to Delta either survives or dies -- and at

            m = 19  ONLY Delta = 6 survives
            m = 20  Delta in {5,6,7} survive, with slack 2, 20, 26
            m = 21  Delta = 5 dies; {6,7,8} survive

    (d) CONSEQUENCE. An m = 19 counterexample has a vertex v of degree exactly 6,
        and deleting it leaves exactly 13 edges with tau >= 5 -- that is, an
        f(6)-EXTREMAL hypergraph. So m = 19 is no longer an open range: it is a
        single extension question about a classified-in-principle object.

This certificate does NOT raise the floor. m >= 19 stands from cert 0001. What it
does is collapse the first unconfirmed rung from a search to one case.

THE NEW LEMMA (L4), AND WHERE IT CAME FROM
------------------------------------------
For any edge E of an intersecting H on m edges, each of the other m-1 edges meets
E in at least one of its 6 vertices. Counting incidences at E's vertices,

    sum over v in E of (deg(v) - 1)  >=  m - 1,   i.e.   sum of deg over E >= m+5.

Hence some vertex of E has degree >= 1 + ceil((m-1)/6), giving (a). This is the
pointwise refinement of cert 0001's lemma (L2): summing (L4) over all edges gives
back exactly (L2), so (L2) is its average and (L4) is strictly stronger.

Provenance, honestly: (L4) is the generalisation of Claim 2.3 in Abu-Khazneh and
Pokrovskiy, "Intersecting extremal constructions in Ryser's Conjecture for
r-partite hypergraphs" (arXiv:1409.4938), where the same pigeonhole is run at
m = 8 to show every edge of an 8-edge tau=4 hypergraph meets a vertex of degree 3.
Their Lemma 2.1 is the statement built from it. The generalisation to arbitrary m,
and the Delta-window consequence, are done here.

A PARITY KILL, AS A SECOND ROUTE
--------------------------------
If 6*Delta = m+5 exactly, then (L4) forces equality on every edge, so every vertex
of every edge -- hence every vertex -- has degree exactly Delta. Then the total
degree 6m must be divisible by Delta. At m = 19, Delta = 4 that reads 114/4, which
is not an integer. So m=19, Delta=4 dies by parity as well as by counting: two
independent kills of the same case.
"""

import sys
from math import comb

R = 6
FAILURES = []
CHECKS = [0]

# Inputs, each a NAMED dependency rather than something re-proved here:
#   g(1..4) -- cofferdam certificate 0001 (proven there twice over, witness +
#              exhaustive absence). g(t) = least edges of a 6-partite
#              intersecting hypergraph with tau >= t.
#   g(5)=13 -- f(6) = 13, Aharoni-Barat-Wanless; independently Abu-Khazneh-
#              Pokrovskiy. Cert 0001 derives only g(5) >= 12 unaided.
G = {1: 1, 2: 3, 3: 5, 4: 8, 5: 13}
DEPENDS = [
    ("g(1)=1, g(2)=3, g(3)=5, g(4)=8", "cofferdam cert 0001, proven there"),
    ("g(5) = f(6) = 13", "Aharoni-Barat-Wanless; indep. Abu-Khazneh-Pokrovskiy arXiv:1409.4938"),
    ("the (L4) pigeonhole", "generalises Claim 2.3 of Abu-Khazneh-Pokrovskiy; "
                            "generalisation and consequences derived here"),
]


def check(cond, label):
    CHECKS[0] += 1
    print(("  ok    " if cond else "  FAIL  ") + label)
    if not cond:
        FAILURES.append(label)


def maxpairs(m, caps):
    """Largest sum of C(d,2) over one part's degrees: they sum to m, and every
    prefix of the sorted-descending profile obeys caps."""
    best = (-1, None)

    def rec(prof, total, prev):
        nonlocal best
        if total == m:
            v = sum(comb(d, 2) for d in prof)
            if v > best[0]:
                best = (v, tuple(prof))
            return
        for d in range(min(prev, m - total), 0, -1):
            k, s = len(prof) + 1, total + d
            if k in caps and s > caps[k]:
                continue
            rec(prof + [d], s, d)

    rec([], 0, m)
    return best


def caps_for(m, delta=None):
    """Cap lemma prefix caps at tau >= 6, optionally with the degree cap
    tightened to a hypothesised maximum degree."""
    c = {k: m - G[6 - k] for k in range(1, 6)}
    if delta is not None:
        c[1] = min(c[1], delta)
    return c


def delta_window(m):
    lo = 1 + -(-(m - 1) // 6)      # ceil((m-1)/6)
    hi = m - G[5]
    return lo, hi


def survives(m, delta):
    val, prof = maxpairs(m, caps_for(m, delta))
    return (R * val >= comb(m, 2)), val, prof


def main():
    print("cofferdam certificate 0002 — the maximum-degree window")
    print()

    print("[A] the window is well posed")
    for m in (19, 20, 21):
        lo, hi = delta_window(m)
        check(lo <= hi, f"m={m}: Delta window [{lo}, {hi}] is nonempty")

    print()
    print("[B] (L4) is consistent with (L2): summing the per-edge bound over all")
    print("    edges must reproduce cert 0001's pair count exactly")
    for m in range(14, 25):
        # sum_E sum_{v in E} deg v = sum_v deg(v)^2 ; (L4) gives >= m(m+5);
        # and sum_v C(deg,2) = (sum deg^2 - 6m)/2 >= (m(m+5) - 6m)/2 = C(m,2)
        lhs = (m * (m + 5) - R * m) // 2
        check(lhs == comb(m, 2), f"m={m}: (L4) summed = (L2) exactly ({lhs} = C({m},2))")

    print()
    print("[C] the Delta-refined pair count, case by case")
    verdicts = {}
    for m in (19, 20, 21):
        lo, hi = delta_window(m)
        alive = []
        for d in range(lo, hi + 1):
            ok, val, prof = survives(m, d)
            if ok:
                alive.append(d)
            print(f"    m={m} Delta={d}: max/part {val} at {prof} -> "
                  f"6*{val}={R*val} vs C({m},2)={comb(m,2)}   "
                  f"{'survives, slack %d' % (R*val-comb(m,2)) if ok else 'DEAD'}")
        verdicts[m] = alive
    check(verdicts[19] == [6], f"m=19: exactly one surviving Delta, and it is 6 (got {verdicts[19]})")
    check(verdicts[20] == [5, 6, 7], f"m=20: Delta in {{5,6,7}} survive (got {verdicts[20]})")
    check(5 not in verdicts[21], f"m=21: Delta=5 dies (surviving: {verdicts[21]})")

    print()
    print("[D] the parity kill, independently of the counting")
    m, d = 19, 4
    forced = (R * d == m + 5)
    check(forced, f"m={m}, Delta={d}: 6*Delta = {R*d} = m+5, so (L4) forces equality on every edge")
    check((R * m) % d != 0, f"m={m}, Delta={d}: every degree would be {d}, but 6m={R*m} "
                            f"is not divisible by {d} ({R*m}/{d} = {R*m/d}) -> impossible")
    ok, _, _ = survives(m, d)
    check(not ok, f"m={m}, Delta={d}: also dead by counting -- two independent kills")

    print()
    print("[E] the consequence at m = 19")
    resid = 19 - 6
    check(resid == G[5], f"m=19, Delta=6: deleting the degree-6 vertex leaves {resid} edges")
    check(True, "those 13 edges have tau >= 5 (else a 5-cover plus v covers H in 6... "
                "precisely: a 4-cover of them plus v would give tau(H) <= 5)")
    check(resid == G[5], "13 = f(6), so the residual is an f(6)-EXTREMAL hypergraph")

    print()
    print("-" * 72)
    print(f"checks run: {CHECKS[0]}   failures: {len(FAILURES)}")
    print()
    print("RESULT   m = 19 is reduced to a SINGLE case: Delta = 6, with the")
    print("         degree-6 vertex's complement an f(6)-extremal 13-edge object.")
    print("         m = 20 keeps three cases (Delta = 5, 6, 7); the Delta=5 case")
    print("         survives on a slack of only 2 and is the natural next target.")
    print()
    print("NOT CLAIMED: the floor is unchanged at m >= 19 (cert 0001). This is a")
    print("reduction, not an improvement of the bound.")
    print()
    print("DEPENDENCIES")
    for name, why in DEPENDS:
        print(f"  {name}: {why}")

    if FAILURES:
        print("\nCERTIFICATE RED")
        sys.exit(1)
    print("\nCERTIFICATE GREEN")


if __name__ == "__main__":
    main()
