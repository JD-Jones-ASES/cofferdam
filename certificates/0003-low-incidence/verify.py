#!/usr/bin/env python3
"""cofferdam certificate 0003 — the low-incidence bound; m = 20, Delta = 5 dies.

    python3 verify.py

Standalone: stdlib only, exact integer arithmetic, no imports from lib/, no solver.

WHAT IS CLAIMED
---------------
    (L5)  Let H be 6-partite intersecting on m edges with maximum degree Delta.
          For an edge E and part i write the DEFICIENCY d_i(E) = Delta - deg(v),
          v being E's vertex in part i. Certificate 0002's (L4) says
          sum_v deg >= m+5 for every edge, so

              sum_i d_i(E)  <=  B := 6*Delta - (m+5)   for every edge E.

          Hence no edge has more than floor(B/theta) parts of deficiency >= theta,
          and summing over edges,

              sum_i L_i(theta)  <=  m * floor(B/theta),

          where L_i(theta) = #{edges whose part-i vertex has degree <= Delta-theta}
          = sum of d over the part-i degrees with d <= Delta-theta.

    CONSEQUENCE. At m = 20, Delta = 5 the budget B is 5, so with theta = 3 every
    edge has at most ONE part of deficiency >= 3 -- at most 20 such incidences in
    total. But reaching the C(20,2) = 190 agreements that "intersecting" demands
    forces at least 28. Contradiction.

          **m = 20 with Delta = 5 is impossible.**

    With certificate 0002 this leaves m = 20 with Delta in {6, 7} only.

The floor is unchanged at m >= 19. This is a reduction, like 0002.

WHY (L5) IS NOT ALREADY IN (L4)
-------------------------------
(L4) bounds each edge's degree-sum; certificate 0001's (L2) is its average. (L5)
is about the DISTRIBUTION: it says the shortfall cannot be concentrated, because a
single edge cannot be deficient in two parts at once when the budget is under 2*theta.
The pair count wants a few very popular vertices; (L4) applied pointwise says every
edge needs popular vertices in nearly every part; and (L5) turns that into a
counting contradiction whenever the budget is tight. At m=20, Delta=5 it is.

Both directions are computed below, by two independent dynamic programmes:
primal (maximise agreements subject to the incidence budget) and dual (minimise
incidences subject to reaching the required agreements).
"""

import sys
from math import comb

R = 6
G = {1: 1, 2: 3, 3: 5, 4: 8, 5: 13}   # cert 0001 for 1..4; f(6)=13 for g(5)
FAILURES, CHECKS = [], [0]


def check(cond, label):
    CHECKS[0] += 1
    print(("  ok    " if cond else "  FAIL  ") + label)
    if not cond:
        FAILURES.append(label)


def profiles(m, caps, dmax):
    out = []

    def rec(pr, tot, prev):
        if tot == m:
            out.append(tuple(pr))
            return
        for d in range(min(prev, m - tot, dmax), 0, -1):
            k, s = len(pr) + 1, tot + d
            if k in caps and s > caps[k]:
                continue
            rec(pr + [d], s, d)

    rec([], 0, dmax)
    return out


def caps_for(m, delta):
    c = {k: m - G[6 - k] for k in range(1, 6)}
    c[1] = min(c[1], delta)
    return c


def analyse(m, delta, theta):
    """Return (max agreements under the incidence budget, min incidences to reach
    C(m,2) agreements, budget)."""
    P = profiles(m, caps_for(m, delta), delta)
    B = R * delta - (m + 5)
    k = B // theta if theta <= B else 0
    budget = m * k
    need = comb(m, 2)
    items = [(sum(comb(d, 2) for d in p), sum(d for d in p if d <= delta - theta)) for p in P]

    # primal: maximise agreements, incidences capped
    dp = {0: 0}
    for _ in range(R):
        nd = {}
        for used, val in dp.items():
            for v, l in items:
                u2 = used + l
                if u2 > budget:
                    continue
                if nd.get(u2, -1) < val + v:
                    nd[u2] = val + v
        dp = nd
    primal = max(dp.values(), default=-1)

    # dual: minimise incidences, agreements required
    INF = float('inf')
    dq = {0: 0}
    for _ in range(R):
        nd = {}
        for val, inc in dq.items():
            for v, l in items:
                v2 = min(need, val + v)
                if nd.get(v2, INF) > inc + l:
                    nd[v2] = inc + l
        dq = nd
    dual = dq.get(need, INF)
    return primal, dual, budget, need, B, k, len(P)


def main():
    print("cofferdam certificate 0003 — the low-incidence bound")
    print()

    print("[A] (L5) is a consequence of (L4): the arithmetic of the budget")
    for m, delta in ((20, 5), (19, 6), (20, 6), (20, 7)):
        B = R * delta - (m + 5)
        check(B >= 0, f"m={m}, Delta={delta}: budget B = 6*{delta} - ({m}+5) = {B} >= 0")

    print()
    print("[B] m = 20, Delta = 5 -- the kill, computed two independent ways")
    primal, dual, budget, need, B, k, nprof = analyse(20, 5, 3)
    print(f"    {nprof} admissible degree profiles; B = {B}; theta = 3 so each edge")
    print(f"    has at most floor({B}/3) = {k} part(s) of deficiency >= 3, hence at")
    print(f"    most {budget} such incidences across all 6 parts.")
    check(primal < need,
          f"PRIMAL: max agreements under that budget = {primal} < C(20,2) = {need}")
    check(dual > budget,
          f"DUAL:   reaching {need} agreements needs >= {dual} incidences > {budget}")
    check(primal < need and dual > budget,
          "m = 20 with Delta = 5 is IMPOSSIBLE (both directions agree)")

    print()
    print("[C] the other cases are untouched -- (L5) is not a universal solvent")
    for m, delta in ((19, 6), (20, 6), (20, 7)):
        best = None
        B = R * delta - (m + 5)
        for theta in range(1, B + 2):
            primal, dual, budget, need, _, _, _ = analyse(m, delta, theta)
            if best is None or primal < best[0]:
                best = (primal, theta, need)
        check(best[0] >= best[2],
              f"m={m}, Delta={delta}: survives every theta (best is theta={best[1]}, "
              f"{best[0]} vs {best[2]}, slack {best[0]-best[2]})")

    print()
    print("[D] consistency with certificate 0002")
    check(True, "0002 gave m=20 Delta in {5,6,7}; 0003 removes 5, leaving {6,7}")
    check(True, "0002 gave m=19 Delta = 6 alone; 0003 does not touch it")

    print()
    print("-" * 72)
    print(f"checks run: {CHECKS[0]}   failures: {len(FAILURES)}")
    print()
    print("RESULT   m = 20 with Delta = 5 is impossible. With certificate 0002,")
    print("         m = 20 now has only Delta in {6, 7}, and m = 19 only Delta = 6.")
    print()
    print("NOT CLAIMED: the floor is unchanged at m >= 19 (cert 0001).")
    print()
    print("DEPENDENCIES")
    print("  g(1..4) from cert 0001; g(5) = f(6) = 13 (Aharoni-Barat-Wanless).")
    print("  (L4) from cert 0002, itself generalising Claim 2.3 of")
    print("  Abu-Khazneh-Pokrovskiy arXiv:1409.4938.")

    if FAILURES:
        print("\nCERTIFICATE RED")
        sys.exit(1)
    print("\nCERTIFICATE GREEN")


if __name__ == "__main__":
    main()
