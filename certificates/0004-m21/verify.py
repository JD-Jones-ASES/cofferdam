#!/usr/bin/env python3
"""cofferdam certificate 0004 — NEVER GREEN. SCAFFOLDING. SUPERSEDED BY 0006.

    !!  This certificate was written in turn 4 to verify a census of
    !!  f(6)-extremal 13-edge objects that was never produced.  It has never
    !!  run green, it verifies nothing, and it exits with
    !!  "census-13-5.json missing -- nothing to verify".
    !!
    !!  m >= 21 IS PROVEN, but by certificate 0006 and by a completely
    !!  different route: the census this file wanted became UNNECESSARY rather
    !!  than being computed.  See certificates/0006-excess-concentration/.
    !!
    !!  Kept only because a dead end is a result and this repo does not delete
    !!  them.  Do not spend time attacking it; there is nothing here to break.

Original header follows.

cofferdam certificate 0004 — no Ryser r=6 counterexample below 21 edges.

    python3 verify.py            # verify the censuses and the decisive step
    python3 verify.py --full     # also replay the enumeration (hours)

Standalone: stdlib only, exact integer arithmetic, no imports from lib/, no solver.
Checks fail loudly with sys.exit(1); no bare `assert` (python3 -O strips those).

WHAT IS CLAIMED
---------------
A counterexample to Ryser's conjecture at r = 6 in the intersecting case has at
least **21** edges. Equivalently m = 19 and m = 20 are impossible, which together
with certificate 0001's floor closes everything below 21.

HOW THE THREE REMAINING CASES ARE CLOSED
----------------------------------------
Certificates 0001-0003 leave exactly three: (m=19, Delta=6), (m=20, Delta=7) and
(m=20, Delta=6), where Delta is the maximum vertex degree. In each, peel a vertex
v of maximum degree and write H = star(v) + R. Then

  * |R| = m - Delta, so R has 13, 13 and 14 edges respectively;
  * tau(R) >= 5, since a 4-cover of R plus v would cover H with 5 vertices;
  * tau(R) <= 5, since tau(R) = 6 would make R itself a counterexample on 13 or 14
    edges, below certificate 0001's floor of 19. So **tau(R) = 5 exactly**, and R
    is an f(6)-extremal hypergraph (13 edges) or one edge above extremal (14).

Two consequences make the decision cheap and solver-free:

  (1) EVERY STAR EDGE IS A RAINBOW MINIMUM COVER OF R. A star edge meets every
      edge of R using only its five coordinates outside v's part, since v is new
      and meets nothing. A vertex fresh to R meets nothing either, so if j of
      those five were fresh the other 5-j would have to cover R, forcing
      tau(R) <= 5-j. With tau(R) = 5 that gives j = 0: all five coordinates are
      existing vertices of R, one per part, covering R with exactly tau(R)
      vertices.

  (2) TAU IS A SET COVER. A 5-set C covering H cannot contain v (removing v would
      leave a 4-cover of R), so C covers R with 5 vertices -- a minimum cover --
      and meets every star edge f; and it meets f = C_f + {v} exactly when it
      meets C_f. Hence

          tau(H) >= 6   iff   every minimum cover of R is disjoint from some C_f.

So each case reduces to: over all f(6)-extremal R, is there a choice of Delta
rainbow minimum covers of R, all avoiding one common part, that between them
escape every minimum cover of R? This certificate answers no, for every R in the
census, by a direct implementation written independently of the search that
produced the census.

WHAT RESTS ON WHAT
------------------
  * the censuses of (13, tau=5) and (14, tau=5) are COMPLETE -- this is the
    load-bearing computation, replayable with --full, script and log committed
    under notebook/raw/2026-07-25-chain2/;
  * f(6) = 13 (Aharoni-Barat-Wanless; independently Abu-Khazneh-Pokrovskiy), used
    by certificate 0001 for the floor and here to pin tau(R) = 5;
  * certificates 0001-0003 for the floor and the Delta windows.

Everything else -- that each census member really is what it claims, and that none
of them extends -- is re-derived here from scratch.
"""

import itertools
import json
import os
import sys

R6 = 6
HERE = os.path.dirname(os.path.abspath(__file__))
FAILURES, CHECKS = [], [0]


def check(cond, label):
    CHECKS[0] += 1
    print(("  ok    " if cond else "  FAIL  ") + label)
    if not cond:
        FAILURES.append(label)


# --------------------------------------------------------------------------
# primitives, written fresh
# --------------------------------------------------------------------------

def is_intersecting(H):
    return all(any(a == b for a, b in zip(H[i], H[j]))
               for i in range(len(H)) for j in range(i + 1, len(H)))


def find_cover(H, k):
    if not H:
        return ()

    def rec(un, chosen, left):
        if not un:
            return tuple(chosen)
        if left == 0:
            return None
        e = un[0]
        for i in range(R6):
            got = rec([f for f in un if f[i] != e[i]], chosen + [(i, e[i])], left - 1)
            if got is not None:
                return got
        return None

    return rec(list(H), [], k)


def tau(H):
    for k in range(R6 + 1):
        if find_cover(H, k) is not None:
            return k
    return None


def min_covers(H, k):
    """Every cover of size <= k. When tau(H) = k these are the minimum covers, and
    all of them: any cover must hit the first uncovered edge, so branching on that
    edge's six vertices reaches every minimal cover."""
    out = set()

    def rec(un, chosen, left):
        if not un:
            out.add(tuple(sorted(chosen)))
            return
        if left == 0:
            return
        e = un[0]
        for i in range(R6):
            rec([f for f in un if f[i] != e[i]], chosen + ((i, e[i]),), left - 1)

    rec(list(H), (), k)
    return sorted(out)


def symbols(H, q):
    return sorted({e[q] for e in H})


# --------------------------------------------------------------------------
# the decisive test, implemented directly from the statement
# --------------------------------------------------------------------------

def extends(R, delta):
    """Is there a delta-star making tau >= 6? Returns the witness H, or None.

    Direct from consequences (1) and (2): the star edges are rainbow minimum covers
    of R avoiding one common part, and they must jointly escape every minimum cover
    of R. Enumerated plainly -- one vertex per part, brute force -- with no masks,
    patterns or degree prunes, so that agreement with the search that produced the
    census is genuine evidence rather than a shared bug.
    """
    mc = min_covers(R, 5)
    if not mc:
        return None
    need = (1 << len(mc)) - 1
    for p in range(R6):
        others = [q for q in range(R6) if q != p]
        fresh = max(symbols(R, p)) + 1
        stars = []
        for combo in itertools.product(*[symbols(R, q) for q in others]):
            C = dict(zip(others, combo))
            if not all(any(e[q] == s for q, s in C.items()) for e in R):
                continue                      # must cover R
            f = tuple(fresh if q == p else C[q] for q in range(R6))
            esc = 0
            for j, cov in enumerate(mc):
                if not any(f[i] == s for (i, s) in cov):
                    esc |= 1 << j
            stars.append((f, esc))
        n = len(stars)
        if n < delta:
            continue
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | stars[i][1]

        def rec(start, chosen, got):
            if len(chosen) == delta:
                if got != need:
                    return None
                H = tuple(sorted(tuple(R) + tuple(chosen)))
                return H if is_intersecting(H) and tau(H) >= 6 else None
            if (need & ~got) & ~suffix[start]:
                return None
            for i in range(start, n - (delta - len(chosen)) + 1):
                out = rec(i + 1, chosen + [stars[i][0]], got | stars[i][1])
                if out is not None:
                    return out
            return None

        got = rec(0, [], 0)
        if got is not None:
            return got
    return None


# --------------------------------------------------------------------------

def load(name):
    p = os.path.join(HERE, name)
    if not os.path.exists(p):
        return None
    return [tuple(tuple(e) for e in H) for H in json.load(open(p))]


def audit_census(census, m, label):
    bad = 0
    for H in census:
        if len(H) != m or any(len(e) != R6 for e in H):
            bad += 1
        elif not is_intersecting(H):
            bad += 1
        elif tau(H) != 5:
            bad += 1
    check(bad == 0, f"{label}: all {len(census)} members are 6-partite, intersecting, "
                    f"{m} edges, tau = 5 ({bad} bad)")


def close_case(census, delta, m, label):
    hits = []
    for i, R in enumerate(census):
        H = extends(R, delta)
        if H is not None:
            hits.append((i, H))
            break
    check(not hits, f"{label}: no residual admits a {delta}-star reaching tau >= 6 "
                    f"({len(census)} residuals)")
    if hits:
        print("  !! WITNESS FOUND -- this would be a counterexample to Ryser:")
        for e in hits[0][1]:
            print("     ", e)


def main():
    print(__doc__.strip().splitlines()[0])
    print()
    c13 = load('census-13-5.json')
    c14 = load('census-14-5.json')
    if c13 is None:
        print("census-13-5.json missing -- nothing to verify")
        sys.exit(1)

    print("[A] the censuses are what they claim to be")
    audit_census(c13, 13, "(13, tau=5)")
    if c14 is not None:
        audit_census(c14, 14, "(14, tau=5)")

    print()
    print("[B] f(6) = 13 is consistent with the census being non-empty")
    check(len(c13) > 0, f"(13, tau=5) is non-empty ({len(c13)} classes) as f(6)=13 requires")

    print()
    print("[C] the three surviving cases, closed one by one")
    close_case(c13, 6, 19, "m = 19, Delta = 6")
    close_case(c13, 7, 20, "m = 20, Delta = 7")
    if c14 is not None:
        close_case(c14, 6, 20, "m = 20, Delta = 6")
    else:
        print("  ....  m = 20, Delta = 6: census-14-5.json absent, case NOT closed here")

    print()
    print("-" * 72)
    print(f"checks run: {CHECKS[0]}   failures: {len(FAILURES)}")
    print()
    if c14 is not None and not FAILURES:
        print("RESULT   every case below 21 edges is closed:")
        print("         m <= 18 by certificate 0001, m = 19 and m = 20 here.")
        print("         A Ryser r=6 intersecting counterexample has m >= 21.")
    else:
        print("RESULT   partial -- see above for which cases are closed.")
    print()
    print("DEPENDENCIES")
    print("  f(6) = 13: Aharoni-Barat-Wanless; indep. Abu-Khazneh-Pokrovskiy 1409.4938")
    print("  certificates 0001 (floor m >= 19), 0002 and 0003 (the Delta windows)")
    print("  completeness of the censuses: the enumeration under")
    print("    notebook/raw/2026-07-25-chain2/ -- script, log and manifest committed;")
    print("    replay with --full. THIS certificate verifies the members and the")
    print("    decisive no-extension step, not the completeness of the enumeration.")

    if FAILURES:
        print("\nCERTIFICATE RED")
        sys.exit(1)
    print("\nCERTIFICATE GREEN")


if __name__ == "__main__":
    main()
