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
                   max_degree, symbol_counts, tau, unflatten)


def canon_hyp(H: Sequence[Edge]) -> Tuple[Edge, ...]:
    """The canonical representative itself, not just its key.

    Everything stored must be relabelled this way. Constructions leave gaps in a
    part's symbols, and symbol_counts() counts DISTINCT symbols -- so on a gapped
    object the "next fresh" index it implies can already be in use, silently
    fusing the new vertex with an old one."""
    return tuple(sorted(unflatten(canonical_fast(H)[1], R6)))

R6 = 6


def caps_for(m: int, t: int, G: Dict[int, int]) -> Dict[int, int]:
    """Cap-lemma prefix caps for a finished object with m edges and tau >= t."""
    return {k: m - G[t - k] for k in range(1, t) if (t - k) in G}


def delta_window(m: int, t: int, G: Dict[int, int]) -> Tuple[int, int]:
    return 1 + -(-(m - 1) // 6), m - G[t - 1]


def maxpairs(m: int, caps: Dict[int, int]):
    from math import comb
    best = (-1, None)

    def rec(prof, total, prev):
        nonlocal best
        if total == m:
            v = sum(comb(d, 2) for d in prof)
            if v > best[0]:
                best = (v, tuple(prof))
            return
        for d in range(min(prev, m - total), 0, -1):
            k, sm = len(prof) + 1, total + d
            if k in caps and sm > caps[k]:
                continue
            rec(prof + [d], sm, d)

    rec([], 0, m)
    return best


def delta_alive(m: int, t: int, G: Dict[int, int], max_deg=None) -> List[int]:
    """The maximum degrees not already excluded by certificates 0002/0003: the
    pigeonhole window intersected with the Delta-refined pair count. Skipping the
    dead ones is sound and saves whole subtrees."""
    from math import comb
    lo, hi = delta_window(m, t, G)
    if max_deg is not None:
        hi = min(hi, max_deg)
    out = []
    for d in range(lo, hi + 1):
        caps = caps_for(m, t, G)
        caps[1] = min(caps.get(1, m), d)
        val, _ = maxpairs(m, caps)
        if val >= 0 and R6 * val >= comb(m, 2):
            out.append(d)
    return out


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


def set_partitions(items: List[int]):
    """Every set partition of `items`, blocks ordered by least element."""
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for sub in set_partitions(rest):
        for i in range(len(sub)):
            yield sub[:i] + [[first] + sub[i]] + sub[i + 1:]
        yield [[first]] + sub


FRESH = -1


def star_patterns(R: Sequence[Edge], p: int, tR: int,
                  deg: Dict[Tuple[int, int], int], cap1: int):
    """Every PATTERN a star edge can take: for each part other than p, either an
    existing symbol of R or the marker FRESH, such that the existing ones cover R.

    Separating pattern from labelling is what makes this tractable. A fresh vertex
    lies on no edge of R, so it can neither help cover R nor belong to a minimum
    cover of R -- which means (i) the non-fresh coordinates alone must cover R, so
    a pattern carries at most 5 - tau(R) fresh marks, and (ii) whether a star edge
    escapes a given minimum cover of R depends only on its pattern, never on which
    fresh labels it ends up with. So the set-cover test can be run at pattern
    level, before any labelling is chosen.
    """
    nsym = symbol_counts(R, R6)
    others = [q for q in range(R6) if q != p]
    out = set()
    max_fresh = max(0, 5 - tR)

    def fill(assign):
        free = [q for q in others if assign[q] is None]
        if len(free) > max_fresh + len([q for q in free]) - len(free):
            pass
        def rec_free(k, cur, nfresh):
            if k == len(free):
                out.add(tuple(cur))
                return
            q = free[k]
            for s in range(nsym[q]):
                if deg.get((q, s), 0) + 1 > cap1:
                    continue
                cur[q] = s
                rec_free(k + 1, cur, nfresh)
            if nfresh < max_fresh:
                cur[q] = FRESH
                rec_free(k + 1, cur, nfresh + 1)
            cur[q] = None
        rec_free(0, list(assign), sum(1 for q in others if assign[q] == FRESH))

    def rec(assign, unmet):
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
                 G: Dict[int, int], first_only: bool = False,
                 verify_sample: int = 0) -> List[Tuple[Edge, ...]]:
    """All H = R + star(v) with |star(v)| = delta and tau(H) >= t, deduped.

    Two facts do the work.

    (1) A star edge must meet every edge of R using only its five coordinates
        outside v's part, since v is new and meets nothing. A fresh symbol there
        meets nothing either, so if j of the five are fresh the other 5-j must
        cover R, forcing tau(R) <= 5-j. At the top of the Ryser chain tau(R) = 5,
        so j = 0 and every star edge restricts to a RAINBOW MINIMUM COVER of R.

    (2) A (t-1)-cover of H cannot contain v (removing v would leave a (t-2)-cover
        of R, against tau(R) >= t-1), so it is a minimum cover C of R meeting
        every star edge -- and it meets f = C_f + {v} iff it meets C_f. Hence

            tau(H) >= t  iff  every minimum cover of R is disjoint from some C_f,

        a set cover over precomputed masks. Since minimum covers of R contain no
        fresh vertex, the mask is a property of the PATTERN, so the set cover is
        decided before fresh labels are assigned.
    """
    caps = caps_for(m, t, G)
    cap1 = min(caps.get(1, m), delta)
    tR = tau(R)
    if tR < t - 1:
        return []
    mincovers = [] if tR >= t else all_covers(R, t - 1)
    K = len(mincovers)
    full = (1 << K) - 1

    found: Dict[object, Tuple[Edge, ...]] = {}
    nsym = symbol_counts(R, R6)
    degR = degrees(R)
    checked = [0]

    for p in range(R6):
        if delta > cap1:
            continue
        pats = star_patterns(R, p, tR, degR, cap1)
        masks = []
        for c in pats:
            msk = 0
            for j, C in enumerate(mincovers):
                if not any(c[i] == s for (i, s) in C if i != p):
                    msk |= 1 << j
            masks.append(msk)
        n = len(pats)
        if n == 0:
            continue
        nfresh = [sum(1 for q in range(R6) if c[q] == FRESH) for c in pats]
        suffix = [0] * (n + 1)
        pops = [bin(x).count('1') for x in masks]
        suffmax = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | masks[i]
            suffmax[i] = max(suffmax[i + 1], pops[i])
        # the non-fresh coordinates a pattern occupies, for incremental degree caps
        fixed = [[(q, c[q]) for q in range(R6) if q != p and c[q] != FRESH] for c in pats]

        def expand(slots: List[int]):
            v = nsym[p]
            base = [[pats[j][q] for q in range(R6)] for j in slots]
            for row in base:
                row[p] = v
            parts_fresh = {q: [i for i, j in enumerate(slots) if pats[j][q] == FRESH]
                           for q in range(R6) if q != p}
            qs = [q for q, lst in parts_fresh.items() if lst]

            def rec_q(k, rows):
                if k == len(qs):
                    edges = [tuple(r) for r in rows]
                    if len(set(edges)) != len(edges):
                        return None
                    H = tuple(sorted(tuple(R) + tuple(edges)))
                    d = degrees(H)
                    if max(d.values()) != delta or not profile_ok(d, caps):
                        return None
                    if verify_sample and checked[0] < verify_sample:
                        checked[0] += 1
                        if tau(H) < t or not is_intersecting(H):
                            raise AssertionError("set-cover reduction FAILED")
                    found.setdefault(canonical_fast(H), canon_hyp(H))
                    return True
                q = qs[k]
                for part in set_partitions(parts_fresh[q]):
                    r2 = [list(r) for r in rows]
                    for b, block in enumerate(part):
                        for i in block:
                            r2[i][q] = nsym[q] + b
                    got = rec_q(k + 1, r2)
                    if got and first_only:
                        return True
                return None
            return rec_q(0, base)

        def rec(start: int, slots: List[int], covered: int, deg: Dict):
            need = delta - len(slots)
            if need == 0:
                if covered != full:
                    return False
                return bool(expand(slots)) and first_only
            missing = full & ~covered
            # set-cover prunes: what remains must be coverable, and coverable in
            # the number of picks left
            if missing & ~suffix[start]:
                return False
            if need * suffmax[start] < bin(missing).count('1'):
                return False
            for idx in range(start, n):
                if need * suffmax[idx] < bin(missing).count('1'):
                    break
                d2 = dict(deg)
                bad = False
                for (q, sym) in fixed[idx]:
                    d2[(q, sym)] = d2.get((q, sym), 0) + 1
                    if d2[(q, sym)] > cap1:
                        bad = True
                        break
                if bad or not profile_ok(d2, caps):
                    continue
                nxt = idx if nfresh[idx] else idx + 1
                if rec(nxt, slots + [idx], covered | masks[idx], d2):
                    return True
            return False

        d0 = dict(degR)
        d0[(p, nsym[p])] = delta
        if rec(0, [], 0, d0) and first_only:
            break

    return list(found.values())


def generate_base(m: int, t: int, G: Dict[int, int],
                  max_deg: Optional[int] = None, log=None) -> List[Tuple[Edge, ...]]:
    """Edge-wise isomorph-free generation with every prune we have, for the small
    (m, t) at the bottom of the peeling chain.

    All three prunes are sound on a PARTIAL object, because tau rises by at most
    one per added edge and degrees only grow:
      - tau(H') >= t - (m - |H'|)
      - every degree <= max_deg (the caller knows the final Delta)
      - the cap-lemma prefix caps for the finished object
    """
    from ryser import extension_edges
    caps = caps_for(m, t, G)
    cap1 = caps.get(1, m)
    if max_deg is not None:
        cap1 = min(cap1, max_deg)
    level = {canonical_fast((tuple([0] * R6),)): (tuple([0] * R6),)}
    for size in range(1, m):
        need = t - (m - size - 1)
        nxt: Dict[object, Tuple[Edge, ...]] = {}
        for H in level.values():
            for f in extension_edges(H, R6, max_deg=cap1):
                H2 = tuple(sorted(H + (f,)))
                d = degrees(H2)
                if max(d.values()) > cap1 or not profile_ok(d, caps):
                    continue
                if need > 0 and tau(H2) < need:
                    continue
                c = canonical_fast(H2)
                if c not in nxt:
                    nxt[c] = canon_hyp(H2)
        level = nxt
        if log:
            log(f"      base(m={m},t>={t},maxdeg<={max_deg}) level {size+1}: {len(level)}")
        if not level:
            break
    return [H for H in level.values() if len(H) == m and tau(H) >= t]


BASE_M = 7


def enumerate_tau(m: int, t: int, G: Dict[int, int],
                  max_deg: Optional[int] = None,
                  cache: Optional[Dict] = None, log=None) -> List[Tuple[Edge, ...]]:
    """All 6-partite intersecting hypergraphs on m edges with tau >= t and every
    degree <= max_deg, up to isomorphism.

    Small cases go to the edge-wise generator; larger ones peel a maximum-degree
    vertex, passing Delta DOWN as the residual's degree cap -- which is what keeps
    the low-tau levels from exploding.
    """
    if cache is None:
        cache = {}
    key = (m, t, max_deg)
    if key in cache:
        return cache[key]

    if m <= BASE_M or t <= 2:
        res = generate_base(m, t, G, max_deg, log=log)
        cache[key] = res
        if log:
            log(f"  base enumerate(m={m}, tau>={t}, maxdeg<={max_deg}) = {len(res)}")
        return res

    alive = delta_alive(m, t, G, max_deg)
    out: Dict[object, Tuple[Edge, ...]] = {}
    if log:
        log(f"  (m={m},t>={t},maxdeg<={max_deg}) surviving Delta: {alive}")
    for delta in alive:
        sub = enumerate_tau(m - delta, t - 1, G, max_deg=delta, cache=cache, log=log)
        got = 0
        for Rr in sub:
            for H in attach_stars(Rr, delta, t, m, G):
                c = canonical_fast(H)
                if c not in out:
                    out[c] = canon_hyp(H)
                    got += 1
        if log:
            log(f"    (m={m},t>={t},maxdeg<={max_deg}) Delta={delta}: "
                f"{len(sub)} residuals -> {got} new")
    res = list(out.values())
    cache[key] = res
    if log:
        log(f"  enumerate(m={m}, tau>={t}, maxdeg<={max_deg}) = {len(res)} classes")
    return res
