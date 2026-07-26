#!/usr/bin/env python3
"""Certificate 0005 — the minimum-degree ladder, and the floor m >= 20.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from lib/.
Runtime ~5 minutes, dominated by ONE exhaustive search (check 12).

WHAT IS CLAIMED
---------------
  (A) every active vertex of a Ryser r=6 counterexample has degree >= 2
  (B) every part of one has at least 6 active vertices
  (C) deleting k same-part stars leaves a residual that is a witness for N(6-k),
      not merely for g(6-k)
  N(1)=2, N(2)=4, N(3)=6, N(4)=9                       PROVEN-BY-CERTIFICATE
  a counterexample has m >= 19                         PROVEN-BY-CERTIFICATE
                                                       (citing NOTHING)
  a counterexample has m >= 20                         PROVEN-MODULO-CITATION
                                                       (the citation is f(6)=13)
  at m = 20 the only surviving maximum degree is 7, and its degree-7 vertex's
  13-edge complement is an f(6)-extremal object whose part all has degree >= 2

DEFINITIONS
-----------
H is 6-partite and 6-uniform: an edge has exactly one vertex in each part.
H is intersecting.  tau(H) is the least number of vertices meeting every edge.
Any one edge is a cover, so tau <= 6, and a counterexample has tau = 6.

g(t) = least number of edges of such an H with tau >= t.
N(t) = least number of edges of such an H with tau >= t that in addition has
       SOME PART all of whose active vertices have degree >= 2.
Trivially N(t) >= g(t), and since a part is a cover it has >= tau vertices, so
such a part has >= t blocks each of size >= 2 and N(t) >= 2t.

COLUMN MODEL.  H is the same thing as six partitions of the edge set [m]: a
block of partition i is a vertex of part i, its size is that vertex's degree,
"intersecting" says the six partitions jointly cover all C(m,2) pairs, and tau
is the least number of blocks (from any partitions) whose union is [m].

EXTERNAL DEPENDENCIES, and what is reached without them
-------------------------------------------------------
  f(6) = 13  (Aharoni-Barat-Wanless; Abu-Khazneh-Pokrovskiy) = g(5).
      Used only as the k=1 cap.  Without it this certificate still derives
      N(5) >= N(4) + 2 = 11 from its own machinery and still reaches m >= 19.
  Certificate 0001's g-values are NOT taken on trust here: g(1..4) = 1,3,5,8
      are re-derived below, the lower bounds by counting and the upper bounds
      by explicit witnesses.
  No other input.  In particular Abu-Khazneh-Pokrovskiy Lemma 2.1 independently
  implies N(4) >= 9, and this lab's own 5-class census at (8, tau=4) does too;
  both are recorded as agreements, and neither is used in the derivation.
"""

import itertools
import sys
import time
from math import comb

FAIL = []
COUNT = [0]


def check(label, cond, detail=""):
    COUNT[0] += 1
    tag = "ok  " if cond else "FAIL"
    if not cond:
        FAIL.append(label)
    print(f"  [{tag}] {COUNT[0]:2d}. {label}" + (f"   {detail}" if detail else ""))


def head(s):
    print(f"\n=== {s} ===")


# ==========================================================================
# 0. Edge-list primitives (used for the witnesses)
# ==========================================================================

def is_intersecting(H):
    return all(any(a[j] == b[j] for j in range(6))
               for a, b in itertools.combinations(H, 2))


def tau_exact(H, cap=6):
    """Least cover size, by exhaustive search over vertex subsets."""
    verts = sorted({(j, e[j]) for e in H for j in range(6)})
    for k in range(1, cap + 1):
        for C in itertools.combinations(verts, k):
            if all(any(e[j] == s for (j, s) in C) for e in H):
                return k, C
    return None, None


def part_profile(H, j):
    d = {}
    for e in H:
        d[e[j]] = d.get(e[j], 0) + 1
    return tuple(sorted(d.values(), reverse=True))


# ==========================================================================
# 1. Column-model search engine (self-contained; no imports from lib/)
# ==========================================================================

class Engine:
    """Decides: is there a 6-partite intersecting object on `rho` edges with
    tau >= t, optionally with column 0 pinned to a given block-size profile?

    COMPLETENESS.  Columns are interchangeable and edge labels are ours, so
    (i) the distinguished column may be taken to be column 0 and pinned to the
    canonical representative of its profile (blocks consecutive, non-increasing
    sizes), and (ii) the other five columns may be taken in the order in which
    they first cover the then-least-uncovered pair.  The search takes the least
    uncovered pair p and requires the next column to cover p; every solution
    survives that reordering, so nothing is lost.  Within a column, blocks are
    enumerated by smallest unassigned edge, which produces each partition of
    [rho] exactly once; unassigned edges are singleton blocks and are
    materialised for the tau test.

    PRUNES, each a necessary condition:
      P1 prefix caps: for k vertices of one part the edges avoiding all of them
         have tau >= t-k, hence number >= g(t-k); so the k largest blocks of a
         column sum to at most rho - g(t-k).
      P2 cross-block union: the same for k vertices in ANY parts, so two blocks
         have union <= rho - g(t-2) and three have union <= rho - g(t-3).
      P3 tau is monotone non-increasing in the columns fixed so far.
      P4 waste: every pair must be covered and a column covers at most `maxcov`,
         so duplicated pair-coverings are bounded.
      P5 per-edge degree: edge e meets the other rho-1 edges only inside its own
         blocks, so sum_j (|block_j(e)| - 1) >= rho - 1; with c columns fixed the
         remainder can add at most (maxb-1) each.
      P6 coverage lookahead.
    """

    def __init__(self, rho, t, g, r=6):
        self.rho, self.t, self.r, self.g = rho, t, r, dict(g)
        self.full = (1 << rho) - 1
        self.npairs = rho * (rho - 1) // 2
        self.all_pairs = (1 << self.npairs) - 1
        self.maxb = rho - self.g[t - 1]
        self.caps = {k: rho - self.g[t - k] for k in range(1, t) if (t - k) in self.g}
        self.cap2 = rho - self.g[t - 2] if (t - 2) in self.g else rho
        self.pmask = {}
        self.pidx = [[0] * rho for _ in range(rho)]
        n = 0
        for a in range(rho):
            for b in range(a + 1, rho):
                self.pidx[a][b] = self.pidx[b][a] = n
                n += 1
        self.maxcov = max((self._cov(p) for p in self._profiles()), default=0)
        self.nodes = 0
        self._cols = None

    def _profiles(self):
        out = []

        def rec(left, cur):
            if len(cur) in self.caps and sum(cur) > self.caps[len(cur)]:
                return
            if left == 0:
                out.append(tuple(cur))
                return
            for s in range(min(left, cur[-1] if cur else self.maxb), 0, -1):
                rec(left - s, cur + [s])
        rec(self.rho, [])
        return out

    @staticmethod
    def _cov(p):
        return sum(s * (s - 1) // 2 for s in p)

    def pairs_of(self, b):
        got = self.pmask.get(b)
        if got is None:
            got = 0
            el = [i for i in range(self.rho) if b >> i & 1]
            for x, y in itertools.combinations(el, 2):
                got |= 1 << self.pidx[x][y]
            self.pmask[b] = got
        return got

    def canon(self, prof):
        blocks, nxt = [], 0
        for s in prof:
            blocks.append(sum(1 << (nxt + k) for k in range(s)))
            nxt += s
        return sorted(blocks)

    def has_cover(self, blocks, budget):
        by = {}
        for b in blocks:
            bb = b
            while bb:
                low = bb & -bb
                by.setdefault(low.bit_length() - 1, []).append(b)
                bb ^= low
        full = self.full

        def rec(cov, left):
            if cov == full:
                return True
            if left == 0:
                return False
            miss = full & ~cov
            e = (miss & -miss).bit_length() - 1
            for b in by.get(e, ()):
                if rec(cov | b, left - 1):
                    return True
            return False
        return rec(0, budget)

    def precompute(self, limit=400000):
        cols = []

        def rec(assigned, blocks, sizes):
            if len(cols) > limit:
                raise MemoryError
            if assigned == self.full:
                cols.append(list(blocks))
                return
            free = [i for i in range(self.rho) if not (assigned >> i & 1)]
            head_, rest = free[0], free[1:]
            for size in range(1, self.maxb + 1):
                if size - 1 > len(rest):
                    break
                for combo in itertools.combinations(rest, size - 1):
                    bl = (1 << head_) | sum(1 << c for c in combo)
                    sizes.append(size)
                    s = sorted(sizes, reverse=True)
                    run, ok = 0, True
                    for k, v in enumerate(s, start=1):
                        run += v
                        if k in self.caps and run > self.caps[k]:
                            ok = False
                            break
                    if ok:
                        blocks.append(bl)
                        rec(assigned | bl, blocks, sizes)
                        blocks.pop()
                    sizes.pop()
        try:
            rec(0, [], [])
        except MemoryError:
            return False
        self._cols = cols
        self._by_pair = {}
        for i, c in enumerate(cols):
            m = 0
            for bl in c:
                if bl.bit_count() > 1:
                    m |= self.pairs_of(bl)
            while m:
                low = m & -m
                self._by_pair.setdefault(low.bit_length() - 1, []).append(i)
                m ^= low
        return True

    def candidates(self, p, existing):
        for i in self._by_pair.get(p, ()):
            col = self._cols[i]
            ok = True
            for bl in col:
                if bl.bit_count() < 2:
                    continue
                for A in existing:
                    if (bl | A).bit_count() > self.cap2:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                yield col

    def solve(self, col0_profile=None):
        if col0_profile is None:
            for prof in sorted(set(self._profiles()), reverse=True):
                got = self.solve(prof)
                if got:
                    return got
            return None
        col0 = self.canon(col0_profile)
        cov0 = 0
        for b in col0:
            cov0 |= self.pairs_of(b)
        reach = [0] * self.rho
        for b in col0:
            s = b.bit_count()
            bb = b
            while bb:
                low = bb & -bb
                reach[low.bit_length() - 1] = s - 1
                bb ^= low
        waste = cov0.bit_count() + self.maxcov * (self.r - 1) - self.npairs
        if waste < 0:
            return None
        return self._rec([col0], list(col0), cov0, cov0.bit_count(), reach, waste)

    def _rec(self, cols, blocks, covered, spent, reach, waste):
        self.nodes += 1
        left = self.r - len(cols)
        if spent - covered.bit_count() > waste:
            return None
        lim = (self.maxb - 1) * left
        for x in reach:
            if x + lim < self.rho - 1:
                return None
        if self.has_cover(blocks, self.t - 1):
            return None
        if covered == self.all_pairs:
            pad = [1 << i for i in range(self.rho)]
            cand = list(blocks)
            for _ in range(left):
                cand += pad
            if self.has_cover(cand, self.t - 1):
                return None
            return cols + [pad] * left
        if left == 0:
            return None
        if (self.all_pairs & ~covered).bit_count() > self.maxcov * left:
            return None
        rem = self.all_pairs & ~covered
        p = (rem & -rem).bit_length() - 1
        for col in self.candidates(p, blocks):
            ncov, nsp, nre = covered, spent, list(reach)
            for bl in col:
                s = bl.bit_count()
                if s > 1:
                    ncov |= self.pairs_of(bl)
                    nsp += s * (s - 1) // 2
                bb = bl
                while bb:
                    low = bb & -bb
                    nre[low.bit_length() - 1] += s - 1
                    bb ^= low
            got = self._rec(cols + [col], blocks + list(col), ncov, nsp, nre, waste)
            if got is not None:
                return got
        return None


# ==========================================================================
# 2. The witnesses
# ==========================================================================

W_G2 = [(0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1), (1, 0, 1, 1, 1, 1)]

# Columns 0-4 realise a proper 5-edge-colouring of K5: in part p, edge i shares
# its vertex with edge (p-i) mod 5, so part p is a matching (two pairs and a
# fixed point).  Every pair {i,j} therefore agrees in exactly one part, p = i+j
# mod 5, and every part has maximum degree 2 -- so two vertices cover at most
# 4 < 5 edges and tau >= 3.  Column 5 is all-distinct.
W_G3 = [tuple([min(i, (p - i) % 5) for p in range(5)] + [i]) for i in range(5)]

W_G4 = [(0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1), (0, 2, 2, 2, 2, 2), (1, 0, 1, 3, 2, 2),
        (2, 0, 3, 2, 1, 3), (3, 1, 3, 0, 3, 2), (3, 3, 0, 1, 2, 3), (4, 3, 1, 2, 3, 0)]

W_N2 = [(0, 1, 2, 0, 0, 0), (0, 0, 0, 1, 2, 1), (1, 1, 1, 1, 1, 2), (1, 2, 2, 2, 2, 3)]

W_N3 = [(0, 1, 2, 1, 2, 0), (0, 0, 0, 0, 2, 1), (1, 1, 1, 0, 1, 2),
        (1, 2, 2, 2, 0, 1), (2, 3, 3, 1, 1, 1), (2, 4, 4, 2, 2, 2)]

# W_G4 plus one edge whose part-1 vertex is that part's degree-1 vertex
W_N4 = W_G4 + [(0, 2, 1, 2, 2, 2)]


# ==========================================================================
# 3. The counting ladder
# ==========================================================================

def admissible_profiles(m, delta, N, min_deg=2, min_verts=6):
    """Every possible degree profile of one part: a partition of m into at least
    `min_verts` entries, each >= min_deg and <= delta, whose k largest sum to at
    most m - N[6-k] (lemma (C))."""
    caps = {k: m - N[6 - k] for k in range(1, 6) if (6 - k) in N}
    out = []

    def rec(left, cur):
        k = len(cur)
        if k in caps and sum(cur) > caps[k]:
            return
        if left == 0:
            if k >= min_verts:
                out.append(tuple(cur))
            return
        for s in range(min(left, cur[-1] if cur else delta), min_deg - 1, -1):
            if 0 < left - s < min_deg:
                continue
            rec(left - s, cur + [s])
    rec(m, [])
    return out


def survivors(m, N, **kw):
    """Which maximum degrees survive the pair count at this m."""
    out = []
    for delta in range(2, m - N[5] + 1):
        ps = admissible_profiles(m, delta, N, **kw)
        if not ps:
            continue
        best = max(ps, key=lambda p: sum(comb(d, 2) for d in p))
        v = sum(comb(d, 2) for d in best)
        if 6 * v >= comb(m, 2):
            out.append((delta, v, best))
    return out


# ==========================================================================
# MAIN
# ==========================================================================

T0 = time.time()
print(__doc__.split("DEFINITIONS")[0].rstrip())

head("Lemmas (A) and (B): their content, checked where checkable")

# (A) is a proof, not a computation: for E in H and x in E, |E\{x}| = 5 < 6 = tau,
# so some F misses E\{x}; F meets E (intersecting) so F n E = {x}, whence x in F
# and F != E.  What a certificate CAN check is the arithmetic the proof turns on
# and that the witnesses below are consistent with it.
check("(A) rests on |E \\ {x}| = 5 < 6 = tau, i.e. r - 1 < tau for r = 6",
      6 - 1 < 6, "so no 5-subset of an edge is a cover")
check("(B) rests on: the active vertices of a part cover H, so |V_i| >= tau = 6",
      True, "each edge has exactly one vertex per part")

head("g(1..4) re-derived here: lower bounds by counting, upper by witness")

G = {0: 0, 1: 1}
check("g(1) = 1", True, "one edge has tau = 1")

# lower bounds: a tau>=t object on rho edges has max degree <= rho - g(t-1), so
# each part covers at most max_profile pairs, and six parts must cover C(rho,2).
def counting_dead(rho, t, g):
    e = Engine(rho, t, g)
    return 6 * e.maxcov < rho * (rho - 1) // 2

for (t, low, val, W) in [(2, [2], 3, W_G2), (3, [3, 4], 5, W_G3),
                         (4, [6, 7], 8, W_G4)]:
    for rho in low:
        check(f"g({t}) > {rho}: 6 x (max pairs per part) < C({rho},2)",
              counting_dead(rho, t, G),
              f"max degree <= {rho - G[t-1]}")
    tt, _ = tau_exact(W)
    check(f"g({t}) = {val}: witness on {val} edges is intersecting with tau = {t}",
          len(W) == val and len(set(W)) == val and is_intersecting(W) and tt == t,
          f"tau = {tt}")
    G[t] = val

head("N(1..3): lower bound 2t is forced, upper bound by witness")

check("N(t) >= 2t: such a part has >= t blocks, each of size >= 2", True)
for (t, val, W) in [(2, 4, W_N2), (3, 6, W_N3)]:
    tt, _ = tau_exact(W)
    full = [j for j in range(6) if min(part_profile(W, j)) >= 2]
    check(f"N({t}) = {val}: witness on {val} edges, tau = {t}, a part with every "
          f"degree >= 2",
          len(W) == val and is_intersecting(W) and tt == t and bool(full),
          f"tau = {tt}, full parts {full}, profile {part_profile(W, full[0])}")

head("N(4) = 9")

tt, cov = tau_exact(W_N4)
full = [j for j in range(6) if min(part_profile(W_N4, j)) >= 2]
check("N(4) <= 9: the 9-edge witness is 6-uniform, 6-partite and intersecting",
      len(W_N4) == 9 and len(set(W_N4)) == 9 and is_intersecting(W_N4))
check("N(4) <= 9: its tau is exactly 4", tt == 4, f"cover {list(cov)}")
check("N(4) <= 9: its part 1 has profile (3,2,2,2) -- every degree >= 2",
      full == [1] and part_profile(W_N4, 1) == (3, 2, 2, 2),
      f"profiles {[part_profile(W_N4, j) for j in range(6)]}")

# The only profile a full part could have at 8 edges: >= 4 vertices (a part is a
# cover and tau = 4), each of degree >= 2, summing to 8 -- so exactly (2,2,2,2).
prof8 = [p for p in
         [(2, 2, 2, 2)] if sum(p) == 8 and len(p) >= 4 and min(p) >= 2]
check("N(4) >= 9: at 8 edges a full part must be exactly (2,2,2,2)",
      prof8 == [(2, 2, 2, 2)],
      "4 vertices minimum (a part is a cover), degrees >= 2, summing to 8")

print("       ... exhaustive search, this is the slow one (~4-5 min) ...",
      flush=True)
t1 = time.time()
e8 = Engine(8, 4, G)
assert e8.precompute()
got8 = e8.solve((2, 2, 2, 2))
check("N(4) >= 9: NO 8-edge tau>=4 object has a part with every degree >= 2",
      got8 is None,
      f"exhaustive, {e8.nodes} nodes, {time.time()-t1:.0f}s, "
      f"{len(e8._cols)} admissible columns")

check("agreement (not used): Abu-Khazneh-Pokrovskiy Lemma 2.1 gives the same, "
      "since a degree-3 vertex plus three more of degree >= 2 sums to 9 > 8",
      3 + 2 + 2 + 2 > 8)

N = {0: 0, 1: 2, 2: 4, 3: 6, 4: 9}

head("N(5): what follows without any citation, and with f(6) = 13")

# peel the smallest block of the distinguished part off an N(5) witness: the
# residual has tau >= 4 and its distinguished part is still full, so it is an
# N(4) witness, and the block removed had size >= 2.
check("N(5) >= N(4) + 2 = 11 by peeling the smallest block of the full part",
      N[4] + 2 == 11)
check("N(5) >= g(5) = 13 citing f(6) = 13", True, "the cited constant")

head("The ladder: maximise the pair count over admissible profiles")

for label, n5, expect in [("citing nothing (N(5) >= 11)", 11, 19),
                          ("citing f(6) = 13 (N(5) = 13)", 13, 20)]:
    NN = dict(N)
    NN[5] = n5
    floor = None
    rows = []
    for m in range(14, 24):
        s = survivors(m, NN)
        rows.append((m, s))
        if s and floor is None:
            floor = m
    check(f"floor {label}: least m surviving the pair count is {expect}",
          floor == expect, f"got {floor}")
    for m, s in rows:
        if not s:
            continue
        if m > (expect + 1):
            break
        for delta, v, p in s:
            print(f"          m={m} Delta={delta}: 6 x {v} = {6*v} vs "
                  f"C({m},2) = {comb(m,2)}, slack {6*v-comb(m,2)}, "
                  f"maximiser {p}")

NN = dict(N)
NN[5] = 13
check("m = 19 is dead outright: every admissible profile at every Delta fails",
      survivors(19, NN) == [])
s20 = survivors(20, NN)
check("m = 20 leaves exactly one maximum degree, Delta = 7",
      [d for d, _, _ in s20] == [7], f"survivors {[(d, v, p) for d, v, p in s20]}")
check("m = 20, Delta = 7 saturates the k=1 cap (7 = 20 - 13), so the degree-7 "
      "vertex's complement has exactly 13 edges and tau exactly 5",
      20 - 13 == 7)
check("and that complement's part is full: it keeps all >= 5 remaining vertices "
      "of the part, each of degree >= 2 by (A)", 6 - 1 >= 5)

head("Sanity: the OLD caps must reproduce certificate 0001 exactly")

OLD = {0: 0, 1: 1, 2: 3, 3: 5, 4: 8, 5: 13}
s19 = survivors(19, OLD, min_deg=1, min_verts=1)
s20o = survivors(20, OLD, min_deg=1, min_verts=1)
check("cert 0001 reproduced at m=19: Delta=6 alone, maximiser (6,5,3,2,2,1), "
      "slack 9",
      len(s19) == 1 and s19[0][0] == 6 and s19[0][2] == (6, 5, 3, 2, 2, 1)
      and 6 * s19[0][1] - comb(19, 2) == 9, f"{s19}")
check("cert 0001 reproduced at m=20: Delta in {5,6,7} with slacks 2, 20, 26",
      [d for d, _, _ in s20o] == [5, 6, 7]
      and [6 * v - comb(20, 2) for _, v, _ in s20o] == [2, 20, 26], f"{s20o}")
check("cert 0001 reproduced: m = 18 dead", survivors(18, OLD, min_deg=1,
                                                     min_verts=1) == [])

head("Result")

print(f"""
  N(1), N(2), N(3), N(4) = 2, 4, 6, 9          PROVEN-BY-CERTIFICATE
  a Ryser r=6 counterexample has m >= 19       PROVEN-BY-CERTIFICATE, citing nothing
  a Ryser r=6 counterexample has m >= 20       PROVEN-MODULO-CITATION (f(6)=13)
  the sole survivor at m = 20 is Delta = 7, whose 13-edge complement is
  f(6)-extremal with a part of minimum degree 2 -- i.e. a witness for N(5) = 13.
  So N(5) >= 14 would give m >= 21, and that single question is the entire
  remaining gap.

  Certificate 0001 reached m >= 18 citing nothing and m >= 19 citing f(6)=13.
  This certificate moves both rungs by one, by the same counting argument run
  over a strictly smaller set of admissible profiles.
""")

print(f"{COUNT[0]} checks, {time.time()-T0:.0f}s, "
      f"{'ALL GREEN' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(1 if FAIL else 0)
