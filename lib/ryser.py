"""cofferdam/lib/ryser.py — core primitives for r-partite intersecting hypergraphs.

Stdlib only. Exact throughout. No SAT solver, no ILP solver, no floating point.

REPRESENTATION
--------------
An r-partite r-uniform hypergraph is a tuple of EDGES. Each edge is a tuple of r
ints; edge[i] names which vertex of part i the edge uses. A vertex is the pair
(part_index, symbol). Two edges intersect iff they agree in at least one
coordinate. So the whole object is a set of length-r words, pairwise agreeing
somewhere.

A COVER is a set of vertices meeting every edge; tau(H) is the least cover size.

WHY THERE IS NO SOLVER HERE
---------------------------
Every single edge of an intersecting H is itself a cover of size r, so
tau(H) <= r always. The interesting direction, "tau <= r-1", is witnessed by an
explicit cover, which any reader can check by inspection. So the expensive claim
("no small counterexample") decomposes into exhaustive generation plus a list of
explicit covers -- nothing in the trust chain is a solver's word.

Finding a cover of size <= k is a depth-k branch: any cover must hit a fixed
uncovered edge, so it contains one of that edge's r vertices. That is r**k nodes
worst case (6**5 = 7776 here), exact and instant.
"""

from __future__ import annotations

import itertools
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

Edge = Tuple[int, ...]
Hyp = Tuple[Edge, ...]
Vertex = Tuple[int, int]  # (part index, symbol)


# --------------------------------------------------------------------------
# basic predicates
# --------------------------------------------------------------------------

def meets(e: Edge, f: Edge) -> bool:
    """True iff edges e and f share a vertex (agree in some coordinate)."""
    return any(a == b for a, b in zip(e, f))


def is_intersecting(H: Sequence[Edge]) -> bool:
    return all(meets(H[i], H[j]) for i in range(len(H)) for j in range(i + 1, len(H)))


def is_covered_by(e: Edge, C: Iterable[Vertex]) -> bool:
    return any(e[i] == s for (i, s) in C)


def covers(H: Sequence[Edge], C: Iterable[Vertex]) -> bool:
    C = tuple(C)
    return all(is_covered_by(e, C) for e in H)


# --------------------------------------------------------------------------
# exact cover number
# --------------------------------------------------------------------------

def find_cover(H: Sequence[Edge], k: int) -> Optional[Tuple[Vertex, ...]]:
    """Return a cover of size <= k, or None if none exists. Exact.

    Correctness: if H is nonempty, every cover must hit the first uncovered
    edge e, hence contains (i, e[i]) for some i. Branching on those r choices is
    exhaustive; each branch removes every edge through the chosen vertex.
    """
    if not H:
        return ()
    r = len(H[0])

    def rec(uncovered: List[Edge], chosen: List[Vertex], budget: int):
        if not uncovered:
            return tuple(chosen)
        if budget == 0:
            return None
        e = uncovered[0]
        for i in range(r):
            v = (i, e[i])
            rest = [f for f in uncovered if f[i] != e[i]]
            got = rec(rest, chosen + [v], budget - 1)
            if got is not None:
                return got
        return None

    return rec(list(H), [], k)


def tau(H: Sequence[Edge]) -> int:
    """Exact cover number. For intersecting H this is at most r."""
    if not H:
        return 0
    r = len(H[0])
    for k in range(0, r + 1):
        if find_cover(H, k) is not None:
            return k
    raise AssertionError("intersecting hypergraph with tau > r is impossible")


def all_covers(H: Sequence[Edge], k: int) -> List[Tuple[Vertex, ...]]:
    """Every minimal-ish cover of size <= k (deduplicated, not necessarily minimal)."""
    if not H:
        return [()]
    r = len(H[0])
    out = set()

    def rec(uncovered: List[Edge], chosen: Tuple[Vertex, ...], budget: int):
        if not uncovered:
            out.add(tuple(sorted(chosen)))
            return
        if budget == 0:
            return
        e = uncovered[0]
        for i in range(r):
            rest = [f for f in uncovered if f[i] != e[i]]
            rec(rest, chosen + ((i, e[i]),), budget - 1)

    rec(list(H), (), k)
    return sorted(out)


# --------------------------------------------------------------------------
# structure
# --------------------------------------------------------------------------

def degrees(H: Sequence[Edge]) -> Dict[Vertex, int]:
    d: Dict[Vertex, int] = {}
    for e in H:
        for i, s in enumerate(e):
            d[(i, s)] = d.get((i, s), 0) + 1
    return d


def symbol_counts(H: Sequence[Edge], r: int) -> List[int]:
    """Number of distinct symbols used in each part."""
    return [len({e[i] for e in H}) for i in range(r)]


def max_degree(H: Sequence[Edge]) -> int:
    return max(degrees(H).values()) if H else 0


# --------------------------------------------------------------------------
# extensions
# --------------------------------------------------------------------------

def extension_edges(H: Sequence[Edge], r: int, max_deg: Optional[int] = None) -> List[Edge]:
    """Every edge f such that H + (f,) is still intersecting.

    Such an f must meet every edge of H, i.e. f is a cover of H that happens to
    use exactly one vertex per part. We enumerate by repeatedly taking an edge
    of H not yet met and branching on which part f will agree with it in; the
    symbol is then forced. Parts left free at the end range over the symbols
    already present plus one fresh symbol (all fresh symbols in a part are
    interchangeable, so one representative suffices).

    max_deg, if given, discards extensions that would push any vertex degree
    above it.
    """
    nsym = symbol_counts(H, r) if H else [0] * r
    deg = degrees(H)
    fresh = list(nsym)  # next unused symbol in each part
    out = set()

    def fill_free(assign: Tuple[Optional[int], ...]):
        free = [i for i in range(r) if assign[i] is None]
        ranges = [range(fresh[i] + 1) for i in free]
        for combo in itertools.product(*ranges):
            f = list(assign)
            for i, s in zip(free, combo):
                f[i] = s
            ft = tuple(f)
            if max_deg is not None:
                if any(deg.get((i, s), 0) + 1 > max_deg for i, s in enumerate(ft)):
                    continue
            out.add(ft)

    def rec(assign: Tuple[Optional[int], ...], unmet: List[Edge]):
        if not unmet:
            fill_free(assign)
            return
        e = unmet[0]
        for i in range(r):
            if assign[i] is not None:
                continue  # if it equalled e[i], e would have been met already
            if max_deg is not None and deg.get((i, e[i]), 0) + 1 > max_deg:
                continue
            a2 = list(assign)
            a2[i] = e[i]
            rec(tuple(a2), [g for g in unmet if g[i] != e[i]])

    if not H:
        return [tuple([0] * r)]
    rec((None,) * r, list(H))
    return sorted(out)


# --------------------------------------------------------------------------
# canonical form  (isomorphism = permute parts, relabel symbols within a part,
#                  edges are an unordered set)
# --------------------------------------------------------------------------

def _lexmin_under_row_order(rows: Sequence[Edge], r: int,
                            bound: Optional[Tuple[int, ...]]) -> Optional[Tuple[int, ...]]:
    """Lex-least flattening of `rows` over all row orders, with symbols in each
    part renamed by order of first appearance. `bound` prunes: if the result
    cannot beat it, return None.
    """
    m = len(rows)
    best: List[Optional[Tuple[int, ...]]] = [bound]
    improved = [False]

    def rec(prefix: Tuple[int, ...], remaining: Tuple[int, ...],
            maps: Tuple[Dict[int, int], ...], counters: Tuple[int, ...]):
        if not remaining:
            if best[0] is None or prefix < best[0]:
                best[0] = prefix
                improved[0] = True
            return
        # image of each remaining row under the current partial relabelling
        cands = []
        for idx in remaining:
            row = rows[idx]
            img = tuple(maps[j].get(row[j], counters[j]) for j in range(r))
            cands.append((img, idx))
        cands.sort()
        lo = cands[0][0]
        head = prefix + lo
        if best[0] is not None and head > best[0][:len(head)]:
            return  # cannot beat the incumbent
        for img, idx in cands:
            if img != lo:
                break
            row = rows[idx]
            nmaps = list(maps)
            ncnt = list(counters)
            for j in range(r):
                if row[j] not in maps[j]:
                    d = dict(maps[j])
                    d[row[j]] = ncnt[j]
                    nmaps[j] = d
                    ncnt[j] += 1
            rec(head, tuple(x for x in remaining if x != idx), tuple(nmaps), tuple(ncnt))

    rec((), tuple(range(m)), tuple({} for _ in range(r)), tuple(0 for _ in range(r)))
    return best[0] if improved[0] else None


def canonical(H: Sequence[Edge]) -> Tuple[int, ...]:
    """A canonical form: the lex-least flattening over all part orders and all
    edge orders, with symbols renamed by first appearance within each part.

    This is invariant under the full isomorphism group by construction (the
    minimum is taken over the whole group's action), so two hypergraphs are
    isomorphic iff their canonical forms are equal.
    """
    if not H:
        return ()
    r = len(H[0])
    best: Optional[Tuple[int, ...]] = None
    for sigma in itertools.permutations(range(r)):
        rows = [tuple(e[sigma[j]] for j in range(r)) for e in H]
        got = _lexmin_under_row_order(rows, r, best)
        if got is not None:
            best = got
    assert best is not None
    return best


def unflatten(canon: Tuple[int, ...], r: int) -> Hyp:
    return tuple(tuple(canon[i:i + r]) for i in range(0, len(canon), r))


# --------------------------------------------------------------------------
# isomorph-free layer generation
# --------------------------------------------------------------------------

def generate(r: int, m_target: int, tau_target: int,
             max_deg: Optional[int] = None,
             report=None) -> Dict[int, List[Hyp]]:
    """All isomorphism classes of r-partite intersecting hypergraphs on <= m_target
    edges that could still be completed, within m_target edges, to one with
    tau >= tau_target.

    Two prunes, both sound:

      (P1) tau rises by at most 1 per added edge -- if C covers H-e then C plus
           any vertex of e covers H. So a partial H' on m' edges can only reach
           tau_target at m_target edges if tau(H') >= tau_target - (m_target - m').

      (P2) every vertex degree in a subfamily is at most its degree in the
           finished object, so any degree cap valid for the target is valid at
           every intermediate stage.

    Returns {m: [representatives]}.
    """
    levels: Dict[int, List[Hyp]] = {1: [(tuple([0] * r),)]}
    for m in range(1, m_target):
        need = tau_target - (m_target - m)
        seen = {}
        for H in levels[m]:
            for f in extension_edges(H, r, max_deg=max_deg):
                H2 = tuple(sorted(H + (f,)))
                m2 = m + 1
                need2 = tau_target - (m_target - m2)
                if need2 > 0 and tau(H2) < need2:
                    continue
                c = canonical(H2)
                if c not in seen:
                    seen[c] = H2
        levels[m + 1] = list(seen.values())
        if report:
            report(m + 1, len(levels[m + 1]))
        if not levels[m + 1]:
            break
    return levels


def min_edges_for_tau(r: int, tau_target: int, m_cap: int, report=None):
    """Least m <= m_cap admitting an r-partite intersecting hypergraph with
    tau >= tau_target, together with a witness -- or None if there is none at
    or below m_cap.
    """
    for m in range(1, m_cap + 1):
        levels = generate(r, m, tau_target, report=None)
        pool = levels.get(m, [])
        for H in pool:
            if tau(H) >= tau_target:
                if report:
                    report(m, len(pool), True)
                return m, H
        if report:
            report(m, len(pool), False)
    return None
