#!/usr/bin/env python3
"""cofferdam certificate 0001 — the degree-cap ladder and the Ryser r=6 floor.

    python3 verify.py

Standalone: stdlib only, exact integer arithmetic, no imports from lib/, no
solver, no floating point. Every check fails loudly with sys.exit(1); nothing
here relies on `assert`, which `python3 -O` silently strips.

WHAT IS CLAIMED
---------------
Write g(t) for the least number of edges in a 6-partite 6-uniform INTERSECTING
hypergraph with tau >= t. A counterexample to Ryser's conjecture at r = 6 in the
intersecting case is exactly an object counted by g(6), so the least size of such
a counterexample IS g(6).

    g(1) = 1,  g(2) = 3,  g(3) = 5,  g(4) = 8      -- each proved here, both ways
    g(5) >= 12                                      -- derived here
    g(6) >= 18                                      -- derived here, CITING NOTHING
    g(6) >= 19                                      -- derived here, citing f(6) = 13

So a counterexample to intersecting Ryser at r = 6 has at least 18 edges with no
external input at all, and at least 19 edges given the single published constant
f(6) = 13. Label: PROVEN-BY-CERTIFICATE for the floor of 18; the floor of 19 is
PROVEN-MODULO-CITATION, and the citation is named in CITED below.

THE TWO LEMMAS
--------------
(L1) CAP LEMMA. Let H have tau >= t and let S be any set of k < t vertices. Then
     the edges of H avoiding S form a 6-partite intersecting family with
     tau >= t - k -- because a cover of them of size t-1-k, together with S,
     would cover H with t-1 vertices. Hence

         #(edges avoiding S)  >=  g(t - k).

     When the k vertices lie in a single part their stars are disjoint, so the
     degrees add and this reads: the k largest degrees in any one part sum to at
     most m - g(t-k). That is the ladder's prefix cap.

(L2) PAIR COUNT. H is intersecting, so every one of the C(m,2) pairs of edges
     agrees in at least one part. In part i a pair agreeing there shares a
     vertex v, and is counted once in C(deg v, 2). Hence

         sum over parts i of sum over v in part i of C(deg v, 2)  >=  C(m, 2).

Combining: fix t and m, cap each part's sorted degree profile by (L1), maximise
the left side of (L2) over admissible profiles, and if the maximum falls short of
C(m,2) then no such H exists -- so g(t) > m. Walking m upward gives g(t), and
walking t upward from g(1) = 1 gives the ladder.

The exact small values g(2), g(3), g(4) are checked in both directions: an
explicit witness at the claimed value, and absence below it.  [Corrected
2026-07-27, turn 9: this docstring used to say the absence side was
"exhaustive search rather than counting, because counting alone is not tight
there".  Both halves of that were wrong -- the counting ladder is tight
through g(5), and the absence searches below never branch: their root
waste-budget prune (6*maxcov < C(m,2)) IS the counting kill, one node per m
(D-028).  The searches are the counting argument in code form; the
genuinely independent absence route lives in the turn-9 notebook.]
"""

import sys
from itertools import combinations, permutations

R = 6           # 6-partite
FAILURES = []
CHECKS = [0]


def check(cond, label):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append(label)
        print(f"  FAIL  {label}")
    else:
        print(f"  ok    {label}")

NOTES_N = [0]


def note(label, detail=""):
    """A STATED FACT -- a citation, or a step proved by hand and recorded here --
    and NOT a machine check.  Printed with its own tag and counted separately, so
    the check count can never imply a test that did not run."""
    NOTES_N[0] += 1
    print(f"  [note] {label}" + (f"   {detail}" if detail else ""))


def comb2(n):
    return n * (n - 1) // 2


# --------------------------------------------------------------------------
# hypergraphs as edge lists (an edge is an r-tuple; edge[i] is its vertex in part i)
# --------------------------------------------------------------------------

def is_intersecting(H):
    return all(any(a == b for a, b in zip(H[i], H[j]))
               for i in range(len(H)) for j in range(i + 1, len(H)))


def find_cover(H, k):
    """A cover of size <= k, or None. Exact: any cover must hit the first
    uncovered edge, so it holds one of that edge's r vertices."""
    if not H:
        return ()
    r = len(H[0])

    def rec(uncov, chosen, left):
        if not uncov:
            return tuple(chosen)
        if left == 0:
            return None
        e = uncov[0]
        for i in range(r):
            got = rec([f for f in uncov if f[i] != e[i]], chosen + [(i, e[i])], left - 1)
            if got is not None:
                return got
        return None

    return rec(list(H), [], k)


def tau(H):
    r = len(H[0])
    for k in range(r + 1):
        if find_cover(H, k) is not None:
            return k
    return None


# --------------------------------------------------------------------------
# the column-wise exhaustive decision procedure
# --------------------------------------------------------------------------

def partitions_bounded(m, max_block, caps):
    out = []

    def admissible(blocks):
        sizes = sorted((bin(b).count('1') for b in blocks), reverse=True)
        run = 0
        for k, s in enumerate(sizes, start=1):
            run += s
            if k in caps and run > caps[k]:
                return False
        return True

    def rec(remaining, blocks):
        if not admissible(blocks):
            return
        if not remaining:
            out.append(tuple(blocks))
            return
        head, rest = remaining[0], remaining[1:]
        for size in range(1, max_block + 1):
            if size - 1 > len(rest):
                break
            for cmb in combinations(rest, size - 1):
                mask = (1 << head) | sum(1 << c for c in cmb)
                drop = set(cmb)
                rec([x for x in rest if x not in drop], blocks + [mask])

    rec(list(range(m)), [])
    return out


def blocks_cover(blocks, full, budget):
    by_elem = {}
    for b in blocks:
        for i in range(full.bit_length()):
            if b >> i & 1:
                by_elem.setdefault(i, []).append(b)

    def rec(cov, left):
        if cov == full:
            return True
        if left == 0:
            return False
        miss = full & ~cov
        e = (miss & -miss).bit_length() - 1
        return any(rec(cov | b, left - 1) for b in by_elem.get(e, ()))

    return rec(0, budget)


def exists_with_tau(m, t, g):
    """Exhaustive: is there a 6-partite intersecting hypergraph on m edges with
    tau >= t? Returns a witness as a list of R partitions of [m], or None.

    A hypergraph IS an R-tuple of partitions of the edge set: a block is a
    vertex, its size is that vertex's degree, intersecting means the partitions
    jointly cover all pairs, and tau is the least number of blocks covering [m].
    Prunes, all sound and all consequences of (L1)/(L2) above:
      - block sizes and profile prefixes capped by (L1);
      - tau falls monotonically as columns are added, so a partial column set
        already admitting a (t-1)-cover is dead;
      - any two blocks' union is capped by (L1) at k=2, cross-part;
      - waste budget: R columns supply at most maxcov*R pair-slots and C(m,2)
        pairs need covering, so only the difference may be duplicated.
    """
    caps = {k: m - g[t - k] for k in range(1, t) if (t - k) in g}
    if not caps:
        return None
    D = caps[1]
    full = (1 << m) - 1
    npairs = comb2(m)
    all_pairs = (1 << npairs) - 1

    def pidx(a, b):
        return a * m - a * (a + 1) // 2 + (b - a - 1)

    parts = partitions_bounded(m, D, caps)
    if not parts:
        return None
    pcov = []
    for P in parts:
        msk = 0
        for b in P:
            el = [i for i in range(m) if b >> i & 1]
            for a, c in combinations(el, 2):
                msk |= 1 << pidx(a, c)
        pcov.append(msk)
    maxcov = max(bin(c).count('1') for c in pcov)
    waste_budget = maxcov * R - npairs
    ucap = m - g[t - 2] if (t - 2) in g else None

    joins = {}
    for i, c in enumerate(pcov):
        for p in range(npairs):
            if c >> p & 1:
                joins.setdefault(p, []).append(i)

    # symmetry break: relabel [m] so the first column is the consecutive
    # representative of its block-size profile; one per profile suffices
    by_content = {frozenset(P): i for i, P in enumerate(parts)}
    first = []
    for prof in sorted({tuple(sorted((bin(b).count('1') for b in P), reverse=True))
                        for P in parts}, reverse=True):
        blocks, nxt = [], 0
        for s in prof:
            blocks.append(sum(1 << (nxt + k) for k in range(s)))
            nxt += s
        i = by_content.get(frozenset(blocks))
        if i is not None:
            first.append(i)

    def rec(chosen, covered, blocks, spent):
        if spent - bin(covered).count('1') > waste_budget:
            return None
        if blocks_cover(blocks, full, t - 1):
            return None
        if ucap is not None:
            for i in range(len(blocks)):
                for j in range(i + 1, len(blocks)):
                    if bin(blocks[i] | blocks[j]).count('1') > ucap:
                        return None
        if covered == all_pairs:
            need = R - len(chosen)
            pad = [1 << i for i in range(m)]
            if blocks_cover(blocks + pad * need, full, t - 1):
                return None
            return [parts[i] for i in chosen] + [tuple(pad)] * need
        if len(chosen) == R:
            return None
        if bin(all_pairs & ~covered).count('1') > maxcov * (R - len(chosen)):
            return None
        rem = all_pairs & ~covered
        p = (rem & -rem).bit_length() - 1
        pool = [i for i in first if pcov[i] >> p & 1] if not chosen else joins.get(p, [])
        for i in pool:
            got = rec(chosen + [i], covered | pcov[i], blocks + list(parts[i]),
                      spent + bin(pcov[i]).count('1'))
            if got is not None:
                return got
        return None

    return rec([], 0, [], 0)


def to_edges(cols, m):
    sym = [[0] * m for _ in cols]
    for c, P in enumerate(cols):
        for s, b in enumerate(P):
            for i in range(m):
                if b >> i & 1:
                    sym[c][i] = s
    return tuple(tuple(sym[c][i] for c in range(len(cols))) for i in range(m))


# --------------------------------------------------------------------------
# (L2) maximise the pair count over admissible degree profiles
# --------------------------------------------------------------------------

def maxpairs(m, caps):
    """Largest possible sum of C(d,2) over one part's vertex degrees, given the
    degrees sum to m and every prefix of the sorted-descending profile obeys
    caps. Returns (value, profile)."""
    best = (-1, None)

    def rec(prof, total, prev):
        nonlocal best
        if total == m:
            v = sum(comb2(d) for d in prof)
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


def ladder_floor(g, t, m_cap=40):
    """Least m not excluded by (L1)+(L2), i.e. a lower bound for g(t)."""
    for m in range(1, m_cap + 1):
        caps = {k: m - g[t - k] for k in range(1, t) if (t - k) in g}
        if any(c < 0 for c in caps.values()):
            continue
        val, _ = maxpairs(m, caps)
        if val >= 0 and R * val >= comb2(m):
            return m, caps, val
    return None, None, None


# --------------------------------------------------------------------------
# the certificate
# --------------------------------------------------------------------------

# an explicit tau=3 family on 5 edges. Columns 0..4 realise a proper 5-edge-
# colouring of K5 (pair {i,j} gets colour i+j mod 5), so each of those columns is
# a matching on the 5 edges; column 5 is all-distinct. Every pair of edges agrees
# in exactly one column, and no vertex has degree above 2, so two vertices cover
# at most 4 of the 5 edges.
W5 = ((0, 0, 2, 1, 1, 1), (0, 1, 1, 2, 0, 4), (1, 1, 0, 1, 2, 2),
      (1, 2, 1, 0, 1, 3), (2, 0, 0, 0, 0, 0))

# an explicit tau=4 family on 8 edges, found by the exhaustive search below
W8 = ((0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1), (0, 2, 2, 1, 2, 2), (1, 0, 3, 2, 2, 1),
      (1, 2, 0, 3, 1, 3), (2, 2, 2, 0, 3, 1), (2, 3, 3, 1, 0, 3), (3, 3, 2, 2, 1, 0))

# an explicit tau=2 family on 3 edges
W3 = ((0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1), (1, 0, 1, 1, 1, 1))

CITED = [
    ("f(6) = 13", "the fewest edges in a 6-partite intersecting hypergraph with "
                  "tau >= 5 -- note the INEQUALITY: what the ladder consumes is a "
                  "lower bound over tau >= 5, not over tau = 5 exactly, and the "
                  "two differ by precisely the objects a Ryser counterexample "
                  "would be. Aharoni-Barat-Wanless Thm 2.7 proves it in that form "
                  "(arXiv:1409.4833, Graphs Combin. 32 (2016) 1-15); independently "
                  "Abu-Khazneh-Pokrovskiy Lemma 2.9 (arXiv:1409.4938v1), whose own "
                  "definition is also tau >= r-1 though its proof text says = 5. "
                  "Used ONLY to lift the floor from 18 to 19."),
]


def main():
    print(__doc__.split("WHAT IS CLAIMED")[0].strip().splitlines()[0])
    print()
    g = {1: 1}

    print("[A] witnesses -- upper bounds on g(t), each verified from scratch")
    for W, want, name in ((W3, 2, "g(2) <= 3"), (W5, 3, "g(3) <= 5"), (W8, 4, "g(4) <= 8")):
        check(len(W[0]) == R, f"{name}: witness is 6-partite")
        check(is_intersecting(W), f"{name}: witness is intersecting")
        check(tau(W) == want, f"{name}: witness has tau = {want} (got {tau(W)})")

    print()
    print("[B] exhaustive absence -- lower bounds, walking the ladder upward")
    check(exists_with_tau(2, 2, g) is None, "no 6-partite intersecting m=2 with tau>=2")
    g[2] = 3
    for m in (3, 4):
        check(exists_with_tau(m, 3, g) is None, f"no 6-partite intersecting m={m} with tau>=3")
    g[3] = 5
    for m in (6, 7):
        check(exists_with_tau(m, 4, g) is None, f"no 6-partite intersecting m={m} with tau>=4")
    g[4] = 8

    # the search must also FIND the witnesses it is supposed to find -- a search
    # that returns None everywhere would pass [B] vacuously
    print()
    print("[C] the search is not vacuous -- it re-finds the witnesses")
    for m, t in ((3, 2), (5, 3), (8, 4)):
        w = exists_with_tau(m, t, g)
        ok = w is not None
        if ok:
            H = to_edges(w, m)
            ok = is_intersecting(H) and tau(H) >= t
        check(ok, f"search finds a genuine tau>={t} witness at m={m}")

    print()
    print("[D] the ladder -- (L1) caps plus the (L2) pair count")
    m5, caps5, v5 = ladder_floor(g, 5)
    check(m5 == 12, f"g(5) >= 12  [caps {caps5}, per-part max {v5}, "
                    f"6*{v5}={R*v5} vs C(12,2)={comb2(12)}]")
    g_self = dict(g); g_self[5] = m5
    m6, caps6, v6 = ladder_floor(g_self, 6)
    check(m6 == 18, f"g(6) >= 18  SELF-CONTAINED  [caps {caps6}, per-part max {v6}, "
                    f"6*{v6}={R*v6} vs C(18,2)={comb2(18)}]")

    g_cited = dict(g); g_cited[5] = 13
    m6c, caps6c, v6c = ladder_floor(g_cited, 6)
    check(m6c == 19, f"g(6) >= 19  CITING f(6)=13  [caps {caps6c}, per-part max {v6c}, "
                     f"6*{v6c}={R*v6c} vs C(19,2)={comb2(19)}]")

    print()
    print("[E] published-record consistency -- PLUS one load-bearing rung "
          "(corrected 2026-07-27: the m=5 absence check below is NOT a smoke "
          "test; g(4) = 8 needs m = 5, 6, 7 all dead and section [B] covers "
          "only 6 and 7)")
    check(m5 <= 13, "the derived g(5) >= 12 does not overshoot the published f(6) = 13")
    check(exists_with_tau(5, 4, g) is None,
          "no tau>=4 family at m = 5 -- LOAD-BEARING for g(4) = 8")

    print()
    print("-" * 72)
    print(f"checks run: {CHECKS[0]}   notes (stated, not tested): {NOTES_N[0]}"
          f"   failures: {len(FAILURES)}")
    print()
    print("PROVEN VALUES        g(1)=1  g(2)=3  g(3)=5  g(4)=8   (witness + exhaustion)")
    print("DERIVED              g(5) >= 12")
    print("FLOOR, self-contained    a Ryser r=6 intersecting counterexample has m >= 18")
    print("FLOOR, citing f(6)=13    ...............................  m >= 19")
    print()
    print("EXTERNAL DEPENDENCIES")
    for name, why in CITED:
        print(f"  {name}: {why}")
    print("  Remove it and the floor falls to 18; nothing else in this certificate")
    print("  depends on any external result.")
    print()
    print("NOT CLAIMED: anything about m = 19 or m = 20. This certificate does not")
    print("reach 21 and does not attempt to. See NOTES.md for exactly where it stops")
    print("and why the next rung is hard.")

    if FAILURES:
        print()
        print("CERTIFICATE RED")
        sys.exit(1)
    print()
    print("CERTIFICATE GREEN")


if __name__ == "__main__":
    main()
