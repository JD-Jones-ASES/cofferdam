"""cofferdam/lib/peel.py — enumeration by peeling a maximum-degree vertex.

Stdlib only. Exact. No solver.

THE RECURSION
-------------
Let H be 6-partite intersecting with tau(H) >= t and m edges, and let v be a
vertex of maximum degree Delta. Split

        H  =  star(v)  u  R,        R = H - star(v),   |R| = m - Delta.

Then tau(R) >= t-1: a (t-2)-cover of R together with v would cover H with t-1
vertices. So every such H is obtained from some smaller object R by attaching the
star of one new vertex -- and Delta is confined to a window (certificate 0002):

        1 + ceil((m-1)/6)  <=  Delta  <=  m - g(t-1),

with the Delta-refined pair count killing most of the window outright. Peeling
therefore reduces enumeration at (m, t) to enumeration at (m-Delta, t-1), and the
chain for the Ryser question bottoms out at objects small enough to enumerate
directly:

    (19,6) -> (13,5) -> (9,4) or (8,4) -> (6,3) or (5,3) -> base

ATTACHING A STAR
----------------
Every edge f of star(v) carries the fresh vertex v in some fixed part p, and v is
new, so it does no work towards meeting R. Hence f must meet every edge of R
using its OTHER five coordinates: the restriction of f to the parts other than p
is a cover of R. That is a small branch (pick an unmet edge of R, choose which of
the five parts agrees with it, symbol forced).

THE TAU CONDITION, AS A SET COVER
---------------------------------
Suppose C is a (t-1)-set covering H. Then v not in C, since otherwise C-{v} would
cover R with t-2 vertices, contradicting tau(R) >= t-1. So C covers R using t-1
vertices, which is only possible when tau(R) = t-1 exactly, and then C is a
MINIMUM cover of R. Therefore:

    tau(R) >= t         =>  any star works (for tau);
    tau(R) == t-1       =>  tau(H) >= t  iff  for every minimum cover C of R,
                            at least one edge of star(v) avoids C.

So the star must "escape" every minimum cover of R -- a set-cover condition over
a precomputed list, which is cheap to test and prunes the star search hard.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple

from ryser import (Edge, all_covers, canonical_fast, degrees, is_intersecting,
                   max_degree, symbol_counts, tau)

R6 = 6


def caps_for(m: int, t: int, G: Dict[int, int]) -> Dict[int, int]:
    """Cap-lemma prefix caps for a finished object with m edges and tau >= t."""
    return {k: m - G[t - k] for k in range(1, t) if (t - k) in G}


def delta_window(m: int, t: int, G: Dict[int, int]) -> Tuple[int, int]:
    return 1 + -(-(m - 1) // 6), m - G[t - 1]


def profile_ok(deg: Dict[Tuple[int, int], int], caps: Dict[int, int]) -> bool:
    """Prefix caps, per part. Sound as a prune on a PARTIAL object too: degrees
    only grow as edges are added, so a violation now is a violation forever."""
    for i in range(R6):
        ds = sorted((d for (p, _), d in deg.items() if p == i), reverse=True)
        run = 0
        for k, d in enumerate(ds, start=1):
            run += d
            if k in caps and run > caps[k]:
                return False
    return True


def star_candidates(R: Sequence[Edge], p: int, extra: int,
                    deg: Dict[Tuple[int, int], int], cap1: int) -> List[Tuple[int, ...]]:
    """Every assignment of the five parts other than p that covers R, extended by
    free choices (existing symbols, or one of `extra` fresh ones) in the parts the
    covering left unconstrained. Part p is left as None -- the caller fills in v.

    cap1 bounds any single vertex degree in the finished object, so a symbol
    already at that degree in R cannot be used at all.
    """
    nsym = symbol_counts(R, R6)
    out = set()
    others = [q for q in range(R6) if q != p]

    def fill(assign: Tuple[Optional[int], ...]):
        free = [q for q in others if assign[q] is None]

        def rec_free(k: int, cur: List[Optional[int]]):
            if k == len(free):
                out.add(tuple(cur))
                return
            q = free[k]
            for s in range(nsym[q] + extra):
                if deg.get((q, s), 0) + 1 > cap1:
                    continue
                cur[q] = s
                rec_free(k + 1, cur)
                cur[q] = None
        rec_free(0, list(assign))

    def rec(assign: Tuple[Optional[int], ...], unmet: List[Edge]):
        if not unmet:
            fill(assign)
            return
        e = unmet[0]
        for q in others:
            if assign[q] is not None:
                continue
            if deg.get((q, e[q]), 0) + 1 > cap1:
                continue
            a2 = list(assign)
            a2[q] = e[q]
            rec(tuple(a2), [g for g in unmet if g[q] != e[q]])

    rec((None,) * R6, list(R))
    return sorted(out)


def attach_stars(R: Sequence[Edge], delta: int, t: int, m: int,
                 G: Dict[int, int], first_only: bool = False) -> List[Tuple[Edge, ...]]:
    """All H = R + star(v) with |star(v)| = delta, tau(H) >= t, obeying the caps
    for a finished object of m edges. Returns canonical-deduped hypergraphs.
    With first_only, stops at the first H found.
    """
    caps = caps_for(m, t, G)
    # v is a MAXIMUM-degree vertex, so no degree in H exceeds delta -- a much
    # tighter bound than the cap lemma alone gives
    cap1 = min(caps.get(1, m), delta)
    tR = tau(R)
    mincovers = [] if tR >= t else all_covers(R, t - 1)
    if tR < t - 1:
        return []
    K = len(mincovers)
    full = (1 << K) - 1

    found: Dict[object, Tuple[Edge, ...]] = {}
    nsym = symbol_counts(R, R6)
    degR = degrees(R)

    for p in range(R6):
        v = nsym[p]                      # the fresh vertex, in part p
        if degR.get((p, v), 0) + delta > cap1:
            continue
        cands = star_candidates(R, p, delta, degR, cap1)
        # escape-masks: which minimum covers of R this edge avoids
        masks = []
        for c in cands:
            f = tuple(v if q == p else c[q] for q in range(R6))
            msk = 0
            for j, C in enumerate(mincovers):
                if not any(f[i] == s for (i, s) in C):
                    msk |= 1 << j
            masks.append((f, msk))
        n = len(masks)

        def rec(start: int, chosen: List[Edge], deg: Dict, covered: int):
            if len(chosen) == delta:
                if covered != full:
                    return False
                H = tuple(sorted(tuple(R) + tuple(chosen)))
                if max_degree(H) != delta:
                    return False          # v must BE a maximum-degree vertex
                if not is_intersecting(H) or tau(H) < t:
                    return False
                found.setdefault(canonical_fast(H), H)
                return first_only
            need = delta - len(chosen)
            if n - start < need:
                return False
            for idx in range(start, n):
                f, msk = masks[idx]
                d2 = dict(deg)
                bad = False
                for i, s in enumerate(f):
                    d2[(i, s)] = d2.get((i, s), 0) + 1
                    if d2[(i, s)] > cap1:
                        bad = True
                        break
                if bad or not profile_ok(d2, caps):
                    continue
                if rec(idx + 1, chosen + [f], d2, covered | msk):
                    return True
            return False

        if rec(0, [], dict(degR), 0) and first_only:
            break

    return list(found.values())


def enumerate_tau(m: int, t: int, G: Dict[int, int],
                  cache: Optional[Dict] = None, log=None) -> List[Tuple[Edge, ...]]:
    """All 6-partite intersecting hypergraphs on m edges with tau >= t, up to
    isomorphism, by peeling. Base cases are handled by the edge-wise generator."""
    if cache is None:
        cache = {}
    key = (m, t)
    if key in cache:
        return cache[key]

    if t <= 1 or m <= 1:
        from ryser import generate
        lv = generate(R6, m, max(t, 1))
        res = [H for H in lv.get(m, []) if tau(H) >= t]
        cache[key] = res
        return res

    lo, hi = delta_window(m, t, G)
    out: Dict[object, Tuple[Edge, ...]] = {}
    for delta in range(lo, hi + 1):
        sub = enumerate_tau(m - delta, t - 1, G, cache, log)
        sub = [Rr for Rr in sub if max_degree(Rr) <= delta]
        got = 0
        for Rr in sub:
            for H in attach_stars(Rr, delta, t, m, G):
                if canonical_fast(H) not in out:
                    out[canonical_fast(H)] = H
                    got += 1
        if log:
            log(f"    (m={m},t>={t}) Delta={delta}: {len(sub)} residuals -> {got} new classes")
    res = list(out.values())
    cache[key] = res
    if log:
        log(f"  enumerate(m={m}, tau>={t}) = {len(res)} classes")
    return res
