"""cofferdam/lib/columns.py — the column-wise decision engine.

Stdlib only. Exact. No solver.

THE REFRAMING
-------------
An r-partite intersecting hypergraph on m edges is the same thing as an ordered
r-tuple of PARTITIONS of the edge set [m]:

  * part i of the hypergraph induces a partition P_i of [m] -- two edges lie in
    the same block of P_i exactly when they use the same vertex of part i. A
    block IS a vertex; its size IS that vertex's degree.
  * "intersecting" says every pair of edges shares a block in some P_i, i.e. the
    r partitions jointly COVER all C(m,2) pairs.
  * a cover of the hypergraph is a set of blocks whose union is [m], so
    tau(H) = the least number of blocks, drawn from any of the r partitions,
    that cover [m].

Building by column rather than by edge is dramatically cheaper for the questions
this lab asks ("is tau >= t reachable on m edges?"), for three reasons:

  (1) the search is an exact-cover over PAIRS -- branch on the lexicographically
      least uncovered pair and only consider partitions that join it;
  (2) block sizes are capped by the degree lemma, which prunes the partition list
      hard before the search starts;
  (3) tau is MONOTONE NON-INCREASING in the number of columns fixed so far --
      adding a column only adds blocks, which can only make covering easier. So
      the moment a partial column set admits a (t-1)-cover, the whole branch
      dies. This prune fires early and constantly.

Symmetry: edges may be relabelled ([m] permuted) and columns permuted. We break
the first by fixing column 0 to one representative per block-size profile, and
the second by never caring which column is which (columns are chosen in the
order the uncovered pairs demand).
"""

from __future__ import annotations

import itertools
from typing import Dict, List, Optional, Sequence, Tuple

Partition = Tuple[int, ...]  # tuple of block bitmasks, sorted


# --------------------------------------------------------------------------
# partitions of [m] with bounded block size
# --------------------------------------------------------------------------

def partitions_bounded(m: int, max_block: int,
                       caps: Optional[Dict[int, int]] = None) -> List[Partition]:
    """Every partition of {0..m-1} into blocks of size <= max_block, optionally
    filtered by the PREFIX CAPS from the degree ladder.

    caps maps k -> the largest possible total degree of any k vertices lying in a
    single part. Since a part's vertices are exactly this partition's blocks, a
    partition is admissible only if its k largest blocks sum to at most caps[k],
    for every k. These caps come from the cap lemma (see certificates/0001) and
    are far stronger than the block-size bound alone: at m=8 with tau>=4, for
    instance, the 2-cap forbids any column from holding two blocks of size 3,
    which the max_block bound alone happily allows.
    """
    out: List[Partition] = []

    def admissible(blocks: List[int]) -> bool:
        if not caps:
            return True
        sizes = sorted((bin(b).count('1') for b in blocks), reverse=True)
        run = 0
        for k, s in enumerate(sizes, start=1):
            run += s
            if k in caps and run > caps[k]:
                return False
        return True

    def rec(remaining: List[int], blocks: List[int]):
        # sound as a prune: adding further blocks can only raise the sorted
        # prefix sums, so a violation now is a violation forever
        if not admissible(blocks):
            return
        if not remaining:
            out.append(tuple(blocks))
            return
        head = remaining[0]
        rest = remaining[1:]
        for size in range(1, max_block + 1):
            if size - 1 > len(rest):
                break
            for combo in itertools.combinations(rest, size - 1):
                mask = (1 << head) | sum(1 << c for c in combo)
                chosen = set(combo)
                rec([x for x in rest if x not in chosen], blocks + [mask])

    rec(list(range(m)), [])
    return out


def block_profile(P: Partition) -> Tuple[int, ...]:
    return tuple(sorted((bin(b).count('1') for b in P), reverse=True))


def pairs_of(P: Partition, m: int) -> int:
    """Bitmask over pair-indices covered by partition P."""
    mask = 0
    for b in P:
        elems = [i for i in range(m) if b >> i & 1]
        for a, c in itertools.combinations(elems, 2):
            mask |= 1 << pair_index(a, c, m)
    return mask


def pair_index(a: int, b: int, m: int) -> int:
    if a > b:
        a, b = b, a
    # index of pair (a,b) in lexicographic order
    return a * m - a * (a + 1) // 2 + (b - a - 1)


# --------------------------------------------------------------------------
# tau over a set of blocks
# --------------------------------------------------------------------------

def covers_within(blocks: Sequence[int], full: int, budget: int) -> Optional[Tuple[int, ...]]:
    """Least-size subset of `blocks` (size <= budget) whose union is `full`,
    or None. Exact: branch on the least uncovered element -- any cover must use
    a block containing it.
    """
    by_elem: Dict[int, List[int]] = {}
    for b in blocks:
        i = (b & -b).bit_length() - 1
        while True:
            by_elem.setdefault(i, []).append(b)
            nxt = b >> (i + 1)
            if not nxt:
                break
            i = i + 1 + ((nxt & -nxt).bit_length() - 1)

    def rec(covered: int, chosen: Tuple[int, ...], left: int):
        if covered == full:
            return chosen
        if left == 0:
            return None
        missing = full & ~covered
        e = (missing & -missing).bit_length() - 1
        for b in by_elem.get(e, ()):
            got = rec(covered | b, chosen + (b,), left - 1)
            if got is not None:
                return got
        return None

    return rec(0, (), budget)


# --------------------------------------------------------------------------
# the decision procedure
# --------------------------------------------------------------------------

def union_bound_violated(blocks: Sequence[int], m: int, k_union_cap: Optional[int]) -> bool:
    """The general cap lemma at k = 2.

    For ANY set S of k vertices -- not merely k vertices of a single part -- the
    edges avoiding S must have tau >= t - k, since a cover of them of size
    t-1-k together with S would cover everything in t-1. So S leaves at least
    g(t-k) edges uncovered:

        | union of the stars of S |  <=  m - g(t-k).

    The same-part case is the degree ladder (stars are disjoint, so degrees add);
    this is the cross-part case, and at k = 2 it is a cheap pairwise test that
    prunes very hard. At m = 8, t = 4 it says no two blocks may have union of
    size 6 or more -- so any two blocks of size 3 must intersect.
    """
    if k_union_cap is None:
        return False
    n = len(blocks)
    for i in range(n):
        bi = blocks[i]
        for j in range(i + 1, n):
            if bin(bi | blocks[j]).count('1') > k_union_cap:
                return True
    return False


def exists_with_tau(m: int, r: int, t: int, max_block: int,
                    caps: Optional[Dict[int, int]] = None,
                    g: Optional[Dict[int, int]] = None,
                    want_witness: bool = True, verbose: bool = False):
    """Decide: is there an r-partite intersecting hypergraph on m edges with
    tau >= t, every vertex degree <= max_block, and (optionally) satisfying the
    prefix caps of the degree ladder?

    Returns a witness (list of r partitions) or None. Exhaustive.
    """
    full = (1 << m) - 1
    all_pairs = (1 << (m * (m - 1) // 2)) - 1
    parts = partitions_bounded(m, max_block, caps)
    pcov = [pairs_of(P, m) for P in parts]
    maxcov = max((bin(c).count('1') for c in pcov), default=0)

    # partitions that join a given pair
    joins: Dict[int, List[int]] = {}
    for idx, c in enumerate(pcov):
        for p in range(m * (m - 1) // 2):
            if c >> p & 1:
                joins.setdefault(p, []).append(idx)

    # Symmetry break on the first column. Edge labels are ours to choose, so we
    # may relabel [m] to put the first column's partition into the CONSECUTIVE
    # form for its block-size profile: blocks in non-increasing size order,
    # filled with 0,1,2,... in turn. One representative per profile suffices.
    # (Whenever the largest block has size >= 2 this rep joins the pair (0,1),
    # which is exactly the pair the branching rule demands of the first column.)
    index_of = {P: i for i, P in enumerate(parts)}
    first_reps = []
    for prof in sorted({block_profile(P) for P in parts}, reverse=True):
        blocks, nxt = [], 0
        for size in prof:
            blocks.append(sum(1 << (nxt + k) for k in range(size)))
            nxt += size
        rep = tuple(blocks)
        if rep in index_of:
            first_reps.append(index_of[rep])
        else:  # block order differs from generation order; find it by content
            target = frozenset(rep)
            for i, P in enumerate(parts):
                if frozenset(P) == target:
                    first_reps.append(i)
                    break

    # general cap lemma at k = 2: any two vertices leave >= g(t-2) edges
    # uncovered, so their stars' union is capped. Cross-part, unlike the degree
    # ladder, and cheap to test.
    k_union_cap = (m - g[t - 2]) if (g and (t - 2) in g) else None

    nodes = [0]

    # WASTE BUDGET. r columns can cover at most maxcov*r pair-slots, and
    # C(m,2) pairs must each be covered at least once, so across the whole
    # object at most maxcov*r - C(m,2) pair-coverings may be duplicates. Waste
    # only accumulates, so a branch that has already overspent is dead. At
    # m = 8, t = 4 the budget is 30 - 28 = 2, which bites almost immediately.
    waste_budget = maxcov * r - (m * (m - 1) // 2)

    def rec(chosen: List[int], covered: int, blocks: List[int], spent: int):
        nodes[0] += 1
        if spent - bin(covered).count('1') > waste_budget:
            return None
        # tau prune: tau only falls as columns are added
        if covers_within(blocks, full, t - 1) is not None:
            return None
        if union_bound_violated(blocks, m, k_union_cap):
            return None
        if covered == all_pairs:
            # pad out to r columns with the all-singletons partition (adds only
            # degree-1 blocks, which cannot lower tau below t here since the
            # prune above already passed and singletons cover one edge each)
            need = r - len(chosen)
            if need < 0:
                return None
            pad = tuple(1 << i for i in range(m))
            cand_blocks = blocks + [b for _ in range(need) for b in pad]
            if covers_within(cand_blocks, full, t - 1) is not None:
                return None
            return [parts[i] for i in chosen] + [pad] * need
        if len(chosen) == r:
            return None
        # coverage bound
        missing = bin(all_pairs & ~covered).count('1')
        if missing > maxcov * (r - len(chosen)):
            return None
        # branch on the least uncovered pair
        rem = all_pairs & ~covered
        p = (rem & -rem).bit_length() - 1
        pool = first_reps if not chosen else joins.get(p, [])
        if not chosen:
            pool = [i for i in first_reps if pcov[i] >> p & 1] or first_reps
        for idx in pool:
            got = rec(chosen + [idx], covered | pcov[idx], blocks + list(parts[idx]),
                      spent + bin(pcov[idx]).count('1'))
            if got is not None:
                return got
        return None

    res = rec([], 0, [], 0)
    if verbose:
        print(f"    [m={m} r={r} t={t} D={max_block}] {len(parts)} partitions, "
              f"{nodes[0]} nodes -> {'WITNESS' if res else 'none'}")
    return res


def to_edges(cols: Sequence[Partition], m: int) -> Tuple[Tuple[int, ...], ...]:
    """Convert a column presentation back to the edge-list representation."""
    sym = [[0] * m for _ in cols]
    for c, P in enumerate(cols):
        for s, b in enumerate(P):
            for i in range(m):
                if b >> i & 1:
                    sym[c][i] = s
    return tuple(tuple(sym[c][i] for c in range(len(cols))) for i in range(m))
