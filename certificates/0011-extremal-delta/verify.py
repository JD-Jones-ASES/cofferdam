#!/usr/bin/env python3
"""Certificate 0011 -- Delta = 4 exactly, for 13 edges at tau >= 5.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from lib/.
Runs under Python 3.9.  Deterministic.  Green under `python3` and `python3 -O`.

WHAT IS CLAIMED
---------------
  **every 6-partite 6-uniform intersecting hypergraph with m = 13 edges and
    tau >= 5 has maximum degree exactly 4**      PROVEN-BY-CERTIFICATE,
                                                 citing NOTHING

The two halves are proved by completely different machinery and are worth
separating, because only one of them is hard.

  Delta >= 4   is pure counting and needs no hypothesis on tau at all: the
               pair count of an intersecting family on 13 edges cannot be met
               with every degree <= 3.  Section 2.
  Delta <= 4   peels the star of a would-be big vertex and refutes what is
               left, one residual isomorphism class at a time.  Sections 3-5.

The peel is what makes the second half finite.  If deg(v) = D >= 5 then the
residual R = H \\ star(v) has 13 - D edges and tau(R) >= 4, so 13 - D >= g(4)
>= 8 forces D = 5 and |R| = 8 -- and then tau(R) >= 5 would need |R| >= g(5)
>= 12, so tau(R) = 4 exactly.  There are exactly FIVE such R up to isomorphism.
Each is paired with each of the six choices of the star vertex's part, and at
all 30 pairs the escape condition that tau(H) >= 5 imposes on the star is
refuted by exhaustive search.  No 5-star escapes.  Hence no vertex of degree 5,
and (since degrees cannot jump) none of any degree above 4.

WHAT THIS IS FOR
----------------
It is item 1 of PLAN.md: the last turn-4 result still uncertified, used nowhere
load-bearing, and therefore the cheapest place in the lab a real error could
still be hiding.  Nothing downstream of it moves if it is wrong -- which is
exactly why it was worth writing down properly rather than carrying as a
remembered fact.

It does pay one small dividend, and section 7 states it carefully because it is
easy to overstate.  A 13-edge tau >= 5 witness's FULL part -- every vertex of
degree >= 2 -- has one of exactly four degree profiles, and Delta <= 4 kills
(5,2,2,2,2).  The lab already had that three-profile list, from the cap
d1 <= 13 - N(4) = 4, i.e. from N(4) = 9.  What is new is the SECOND ROUTE: this
one consumes g(4) >= 8 and g(5) >= 12, both derived here in eleven lines of
counting, and never touches N(4) = 9 -- the step that was the floor's single
point of failure for two turns.  It is also stronger in scope: the N-cap bounds
one distinguished part, Delta <= 4 bounds all six.

THE LEDGER, in full
-------------------
  (L1)  peel-cap        stated and used here; proof in the section 1 comment
  (L2)  pair count      stated and used here; proof in the section 1 comment
  g(2) >= 3, g(3) >= 5,
  g(4) >= 8, g(5) >= 12 DERIVED HERE in section 1 from (L1) + (L2), by
                        induction on t.  Not imported from certificate 0001,
                        which proves the same rungs by different means -- this
                        file answers for its own inputs.
  the (8,4) census      DERIVED HERE, twice, by two routes that share no code
                        path (section 4), and the two agree.
  W, the 13-edge tau=5
  witness               COPIED from certificate 0008 section 3, and re-verified
                        here from scratch (6-partiteness, intersection, tau by
                        brute force over all C(30,4) vertex 4-sets).  It is used
                        only as a CONTROL; no claim rests on it.
  sibling certificates  NOT consumed.  0005's N(4) = 9, 0009's g(5) = 13,
                        0010's hand proof of the hinge are each stronger than
                        anything used here, and none of them is read.  The
                        ladder in section 1 is re-derived from scratch exactly
                        so that this file does not sit downstream of the
                        floor's hinge -- see section 7.
  EXTERNAL INPUTS       -- NONE.  There is nothing to remove, and so nothing to
                        state a fallback floor for.

Note in particular that f(6) = 13 is NOT used.  "13 edges" is a hypothesis of
the theorem, not a consequence of a citation.  A reader who disbelieves
f(6) = 13 loses nothing here; the statement is simply about 13-edge objects.

WHAT IS NOT CLAIMED
-------------------
Nothing here says a 13-edge tau >= 5 object exists.  W says that, and W is
carried as a control precisely so the theorem is not vacuously true.  Nothing
here bounds m for a Ryser counterexample: a counterexample has tau = 6, and
this file's hypothesis is tau >= 5 at exactly 13 edges.  And nothing here says
Delta <= 4 anywhere else -- section 5's argument consumes |R| = 8 and
tau(R) = 4, which are consequences of m = 13 and of nothing more general.
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
    """A check.  `cond` must be COMPUTED.  A literal True here is a note (D-015)."""
    NCHECK[0] += 1
    ok = bool(cond)
    if not ok:
        FAILED.append(label)
    tag = "ok  " if ok else "FAIL"
    print("  [%s] %2d. %s%s" % (tag, NCHECK[0], label,
                                ("   " + detail) if detail else ""),
          flush=True)
    return ok


def note(label, detail=""):
    """Stated, not tested here.  Never counted as a check."""
    NNOTE[0] += 1
    print("  [note] %s%s" % (label, ("   " + detail) if detail else ""),
          flush=True)


def head(s):
    print("\n" + "=" * 74)
    print(s)
    print("=" * 74, flush=True)


def prog(s):
    print("       ... " + s, flush=True)


R6 = 6
FRESH = -1


# =========================================================================
# PRIMITIVES.  An edge is a 6-tuple; edge[i] names the vertex of part i that
# it uses.  A vertex is the pair (part, symbol).  Two edges intersect iff they
# agree in some coordinate.  A cover is a vertex set meeting every edge.
# =========================================================================

def is_intersecting(H):
    for a in range(len(H)):
        ea = H[a]
        for b in range(a + 1, len(H)):
            eb = H[b]
            if not any(ea[i] == eb[i] for i in range(R6)):
                return False
    return True


def degrees_of(H):
    d = {}
    for e in H:
        for i in range(R6):
            k = (i, e[i])
            d[k] = d.get(k, 0) + 1
    return d


def symbols_of(H):
    return [sorted({e[i] for e in H}) for i in range(R6)]


def vertex_masks(H):
    """(part, symbol) -> bitmask of the edges of H through it."""
    vm = {}
    for j, e in enumerate(H):
        b = 1 << j
        for i in range(R6):
            k = (i, e[i])
            vm[k] = vm.get(k, 0) | b
    return vm


def has_cover(H, k):
    """True iff some set of at most k vertices meets every edge of H.

    Exhaustive.  Any cover must meet the lowest-indexed uncovered edge, so it
    contains one of that edge's six vertices; branching on those six is
    complete, and the depth is k.  No heuristics, no pruning beyond that."""
    n = len(H)
    if n == 0:
        return True
    if k <= 0:
        return False
    vm = vertex_masks(H)
    evm = [tuple(vm[(i, e[i])] for i in range(R6)) for e in H]
    full = (1 << n) - 1

    def rec(cov, d):
        if cov == full:
            return True
        if d == 0:
            return False
        j = 0
        while cov >> j & 1:
            j += 1
        for m in evm[j]:
            if rec(cov | m, d - 1):
                return True
        return False

    return rec(0, k)


def tau_of(H):
    for k in range(0, R6 + 1):
        if has_cover(H, k):
            return k
    return R6


def part_profile(H, i):
    d = degrees_of(H)
    return tuple(sorted((v for (p, _), v in d.items() if p == i), reverse=True))


# =========================================================================
# CANONICAL FORM.  Isomorphism = permute the six parts, relabel symbols within
# each part, edges unordered.  `canon_slow` minimises over all 720 part orders;
# `canon_fast` minimises only over the part orders that sort an isomorphism-
# invariant part signature, and carries that signature in the key -- so the
# PAIR is a complete invariant even though its second component need not equal
# `canon_slow`'s answer.  Section 4 checks the two agree on the finals.
# =========================================================================

def _lexmin(rows, bound):
    """Lex-least flattening of `rows` over all row orders, symbols renamed by
    first appearance within each part.  `bound` prunes."""
    m = len(rows)
    best = [bound]
    improved = [False]

    def rec(prefix, remaining, maps, counters):
        if not remaining:
            if best[0] is None or prefix < best[0]:
                best[0] = prefix
                improved[0] = True
            return
        cands = []
        for idx in remaining:
            row = rows[idx]
            cands.append((tuple(maps[j].get(row[j], counters[j])
                                for j in range(R6)), idx))
        cands.sort()
        lo = cands[0][0]
        headp = prefix + lo
        if best[0] is not None and headp > best[0][:len(headp)]:
            return
        for img, idx in cands:
            if img != lo:
                break
            row = rows[idx]
            nmaps = list(maps)
            ncnt = list(counters)
            for j in range(R6):
                if row[j] not in maps[j]:
                    dd = dict(maps[j])
                    dd[row[j]] = ncnt[j]
                    nmaps[j] = dd
                    ncnt[j] += 1
            rec(headp, tuple(x for x in remaining if x != idx),
                tuple(nmaps), tuple(ncnt))

    rec((), tuple(range(m)), tuple({} for _ in range(R6)),
        tuple(0 for _ in range(R6)))
    return best[0] if improved[0] else None


def _part_invariants(H):
    deg = degrees_of(H)
    einv = {}
    for e in H:
        einv[e] = tuple(sorted(deg[(i, e[i])] for i in range(R6)))
    out = []
    for i in range(R6):
        syms = {}
        for e in H:
            syms.setdefault(e[i], []).append(einv[e])
        out.append(tuple(sorted((len(v), tuple(sorted(v)))
                                for v in syms.values())))
    return out


def canon_fast(H):
    inv = _part_invariants(H)
    order = sorted(range(R6), key=lambda i: inv[i])
    sig = tuple(inv[i] for i in order)
    groups, start = [], 0
    for k in range(1, R6 + 1):
        if k == R6 or inv[order[k]] != inv[order[start]]:
            groups.append(order[start:k])
            start = k
    best = None
    for pick in itertools.product(*[itertools.permutations(g) for g in groups]):
        sigma = [i for g in pick for i in g]
        rows = [tuple(e[sigma[j]] for j in range(R6)) for e in H]
        got = _lexmin(rows, best)
        if got is not None:
            best = got
    return (sig, best)


def canon_slow(H):
    """The honest version: minimise over all 6! = 720 part orders, no invariant
    shortcut.  Used only on the finals, where its cost is affordable."""
    best = None
    for sigma in itertools.permutations(range(R6)):
        rows = [tuple(e[sigma[j]] for j in range(R6)) for e in H]
        got = _lexmin(rows, best)
        if got is not None:
            best = got
    return best


# =========================================================================
# 1.  THE COUNTING INDUCTION:  g(2) >= 3, g(3) >= 5, g(4) >= 8, g(5) >= 12
# =========================================================================
#
# g(t) = the least number of edges in a 6-partite 6-uniform intersecting
# hypergraph with tau >= t.  Two lemmas, both proved here in words and used
# below only through the arithmetic they license.
#
# (L1) PEEL CAP.  Let H have m edges and tau(H) >= t, and let v_1..v_k be
#      distinct vertices of ONE part.  Their stars are pairwise disjoint (an
#      edge meets each part once), so deleting all of them removes exactly
#      d(v_1)+...+d(v_k) edges.  The residual R has tau(R) >= t - k, since a
#      cover of R of size t-k-1 together with v_1..v_k would cover H with t-1
#      vertices.  Hence |R| >= g(t-k), i.e.
#                d(v_1) + ... + d(v_k)  <=  m - g(t-k).
#      Only LOWER bounds on g(t-k) are ever substituted, which makes the cap
#      larger, i.e. weaker -- so the induction never overreaches.
#
# (L2) PAIR COUNT.  Two edges intersect iff they agree in some coordinate, and
#      in part q exactly sum_v C(d_v, 2) pairs agree.  Summing over the six
#      parts counts every intersecting pair at least once, so
#                sum_{q} sum_{v in part q} C(d_v, 2)  >=  C(m, 2).
#
# A part's degree sequence is a partition of m (every edge meets the part once)
# obeying the (L1) prefix caps.  So if six times the LARGEST value of
# sum C(d,2) over such partitions is still below C(m,2), no object exists.
#
# The prefix caps are applied only to profiles with at least k entries.  Padding
# a short profile with degree-0 vertices would be sound too and would kill
# strictly more, but every kill below lands without it, so the weaker reading
# is the one used.

def caps_for(m, t, G):
    return {k: m - G[t - k] for k in range(1, t) if (t - k) in G}


def maxpairs(m, caps):
    """(best value of sum C(d,2), attaining profile) over non-increasing
    partitions of m obeying the prefix caps; (-1, None) if there are none."""
    best = [-1, None]

    def rec(prof, total, prev):
        if total == m:
            v = 0
            for d in prof:
                v += (d * (d - 1)) // 2
            if v > best[0]:
                best[0] = v
                best[1] = tuple(prof)
            return
        for d in range(min(prev, m - total), 0, -1):
            k, sm = len(prof) + 1, total + d
            if k in caps and sm > caps[k]:
                continue
            prof.append(d)
            rec(prof, sm, d)
            prof.pop()

    rec([], 0, m)
    return best[0], best[1]


def pair_count_kills(m, t, G):
    caps = caps_for(m, t, G)
    val, prof = maxpairs(m, caps)
    return (val < 0 or 6 * val < comb(m, 2)), caps, val, prof


head("1.  the ladder g(2) >= 3, g(3) >= 5, g(4) >= 8, g(5) >= 12")

note("(L1) peel cap: k distinct vertices of one part have degrees summing to "
     "at most m - g(t-k)", "their stars are disjoint, and a (t-k-1)-cover of "
     "what is left plus those k vertices would be a (t-1)-cover of H")
note("(L2) pair count: sum over the six parts of sum_v C(deg v, 2) is at least "
     "C(m, 2)", "every one of the C(m,2) pairs of edges agrees in some "
     "coordinate, and part q accounts for sum_v C(d_v,2) agreements")

G = {}
single = ((0, 0, 0, 0, 0, 0),)
check("g(1) = 1: one edge is an intersecting family with tau = 1",
      len(single) == 1 and is_intersecting(single) and tau_of(single) == 1)
G[1] = 1

HEADLINE = [(2, 2), (3, 3), (4, 3), (5, 4), (6, 4), (7, 4),
            (8, 5), (9, 5), (10, 5), (11, 5)]
BOUND = {2: 3, 3: 5, 4: 8, 5: 12}

for t in (2, 3, 4, 5):
    for (mm, tt) in HEADLINE:
        if tt != t:
            continue
        dead, caps, val, prof = pair_count_kills(mm, tt, G)
        if val < 0:
            det = "caps %s admit NO degree profile at all" % (caps,)
        else:
            det = ("caps %s, best profile %s gives %d pairs per part, "
                   "6 x %d = %d < C(%d,2) = %d"
                   % (caps, prof, val, val, 6 * val, mm, comb(mm, 2)))
        check("(m = %d, tau >= %d) is impossible" % (mm, tt), dead, det)
    rng = list(range(1, BOUND[t]))
    allkill = all(pair_count_kills(mm, t, G)[0] for mm in rng)
    check("g(%d) >= %d: EVERY m from %d to %d dies, not just the headline one"
          % (t, BOUND[t], rng[0], rng[-1]), allkill,
          "swept m = %d..%d; a loop's range is part of its claim (D-016)"
          % (rng[0], rng[-1]))
    G[t] = BOUND[t]

check("the ladder used from here on is exactly what section 1 proved",
      G == {1: 1, 2: 3, 3: 5, 4: 8, 5: 12}, "G = %s" % (G,))


# =========================================================================
# 2.  LOWER HALF:  Delta >= 4, and tau is not needed for it
# =========================================================================

head("2.  Delta >= 4 -- pure counting, no hypothesis on tau")

mp13 = maxpairs(13, {1: 3})
check("with every degree <= 3, one part contributes at most 12 agreeing pairs",
      mp13[0] == 12 and mp13[1] == (3, 3, 3, 3, 1),
      "exhaustive over all partitions of 13 into parts <= 3; the maximiser is "
      "%s" % (mp13[1],))
check("6 x 12 = 72 falls short of C(13,2) = 78, so some vertex has degree >= 4",
      6 * mp13[0] < comb(13, 2),
      "%d < %d -- the shortfall is %d pairs"
      % (6 * mp13[0], comb(13, 2), comb(13, 2) - 6 * mp13[0]))
note("this half is STRONGER than the theorem needs",
     "it holds for every 6-partite 6-uniform intersecting hypergraph on 13 "
     "edges, whatever its tau. Only Delta <= 4 uses tau >= 5.")


# =========================================================================
# 3.  THE REDUCTION.  What a vertex of degree >= 5 would force.
# =========================================================================

head("3.  the reduction: deg v = D >= 5 forces D = 5, |R| = 8, tau(R) = 4")

# Let H be 6-partite 6-uniform intersecting, m = 13, tau(H) >= 5, and let v be
# a vertex of part p with deg(v) = D >= 5.  Write R = H \ star(v), so |R| = 13-D.
#
# (a) tau(R) >= 4.  A minimum cover of R together with v covers H, so
#     tau(H) <= tau(R) + 1; with tau(H) >= 5 that gives tau(R) >= 4.  Then
#     |R| >= g(4) >= 8, i.e. 13 - D >= 8, i.e. D <= 5.  With D >= 5: D = 5 and
#     |R| = 8 exactly.
#
# (b) tau(R) = 4 EXACTLY.  If tau(R) >= 5 then |R| >= g(5) >= 12 > 8.
#
# (c) EVERY STAR EDGE COVERS R WITH ITS OTHER FIVE COORDINATES.  Let f be an
#     edge through v.  No edge of R uses v, so f meets each edge of R in some
#     part other than p; hence {(q, f[q]) : q != p} covers R.  A coordinate of f
#     whose symbol does not occur in R at all ("fresh") lies on no edge of R and
#     so does no covering work.  The NON-FRESH ones therefore already cover R,
#     and since tau(R) = 4 there are at least 4 of them among 5 -- so f has at
#     most ONE fresh coordinate.  Section 5 does not assume this: it enumerates
#     with no cap and checks that the cap comes out.
#
# (d) THE ESCAPE CONDITION, both directions.
#     (=>) If some 4-element cover C of R meets every edge of star(v), then C
#          covers all of H, so tau(H) <= 4, contradiction.  So every 4-cover of
#          R is AVOIDED by at least one star edge.
#     (<=) Conversely, suppose tau(H) <= 4 and let C be a minimum cover of H.
#          v is not in C, else C - {v} would cover R with <= 3 vertices against
#          tau(R) = 4.  So C covers R, hence |C| = 4 and C is a 4-cover of R,
#          and every star edge meets it.  So "every 4-cover of R is avoided by
#          some star edge" is equivalent to tau(H) >= 5, not merely implied by
#          it.
#     Note also that every 4-cover of R consists of vertices OF R: a cover of
#     size tau(R) has no vertex to spare, and a vertex outside R covers nothing
#     in R.  So brute force over V(R) finds them all.
#     Finally, whether a star edge f avoids C depends on f only through its
#     PATTERN -- the map q -> f[q] for q != p, with fresh symbols identified,
#     since v and the fresh vertices are never in C.  So each pattern has an
#     ESCAPE MASK over the list of 4-covers, and
#          H exists  ==>  five patterns' masks OR to all-ones,
#     hence at most five DISTINCT masks OR to all-ones.  Section 5 refutes the
#     right-hand side, which refutes the left.  Only this direction is used;
#     the converse is exercised on a known-good object in section 6.

check("(a) 13 - D >= g(4) = 8 forces D <= 5, so D >= 5 leaves only D = 5",
      all(13 - D < G[4] for D in range(6, 14)) and 13 - 5 == 8,
      "checked at every D from 6 to 13, and |R| = 13 - 5 = 8")
check("(b) tau(R) >= 5 is impossible at 8 edges, since g(5) >= 12",
      8 < G[5], "8 < %d, so tau(R) = 4 exactly" % G[5])
note("(c) the fresh cap: 5 coordinates, at least tau(R) = 4 of them doing the "
     "covering, leaves at most 1 fresh",
     "max_fresh = 5 - tau(R) = 1 is arithmetic once (a) and (b) are in; the "
     "REAL test is section 5's check that the uncapped enumeration never "
     "produces a covering pattern with 2 fresh coordinates")
note("(d) the escape condition is an EQUIVALENCE, not an implication",
     "tau(H) >= 5 iff every 4-cover of R is avoided by some edge of star(v). "
     "Only the forward direction is used to kill; the backward direction is "
     "what makes section 6's recovery control a real test of the machinery.")
note("running the star part p over all six parts is enough",
     "an isomorphism carrying R to R' carries the pair (R, p) to (R', sigma p), "
     "so the 5 census representatives crossed with 6 parts cover every (R, p) "
     "up to isomorphism.")


# =========================================================================
# 4.  THE (8, tau=4) CENSUS, BY TWO ROUTES
# =========================================================================

head("4.  the (8, tau >= 4) census -- built twice, by routes sharing no code")

# Every residual R is 6-partite 6-uniform intersecting with 8 edges and
# tau(R) = 4.  (L1) with k = 1, 2, 3 caps its degree profile per part:
#     d1 <= 8 - g(3) = 3,  d1+d2 <= 8 - g(2) = 5,  d1+d2+d3 <= 8 - g(1) = 7.
CAPS8 = {k: 8 - G[4 - k] for k in (1, 2, 3)}
check("the (L1) prefix caps for an 8-edge tau >= 4 object are {1:3, 2:5, 3:7}",
      CAPS8 == {1: 3, 2: 5, 3: 7}, "computed from the ladder, not written in")

MP8 = maxpairs(8, CAPS8)
XCAP8 = 6 * MP8[0] - comb(8, 2)
check("under those caps one part contributes at most 5 agreeing pairs, so the "
      "excess X = sum_parts sum_v C(d,2) - C(m,2) is at most 2",
      MP8[0] == 5 and XCAP8 == 2,
      "maximiser %s; 6 x 5 = 30 against C(8,2) = 28" % (MP8[1],))
note("X is non-decreasing along an intersecting edge-wise growth",
     "adding edge f to a family H' of m' edges changes X by "
     "sum_q deg(q, f[q]) - m' = sum_{e in H'} (t_ef) - m', and t_ef >= 1 for "
     "every e because H' + f is intersecting. So X' > 2 at any stage kills the "
     "whole branch soundly.")


def profile_ok(deg, caps):
    for i in range(R6):
        ds = sorted((d for (p, _), d in deg.items() if p == i), reverse=True)
        run = 0
        for k, d in enumerate(ds, 1):
            run += d
            if k in caps and run > caps[k]:
                return False
    return True


def extensions(H, nsym, deg, max_deg):
    """Every edge f, not already in H, with H + (f,) still intersecting and no
    degree pushed above max_deg.

    f must meet every edge of H, so we repeatedly take an unmet edge and branch
    on which part f agrees with it in (the symbol is then forced).  Parts still
    free at the end range over the symbols already present plus ONE fresh
    representative -- all fresh symbols of a part are interchangeable."""
    present = set(H)
    out = set()

    def fill_free(assign):
        free = [i for i in range(R6) if assign[i] is None]
        for combo in itertools.product(*[range(nsym[i] + 1) for i in free]):
            f = list(assign)
            for i, s in zip(free, combo):
                f[i] = s
            ft = tuple(f)
            if ft in present:
                continue
            bad = False
            for i in range(R6):
                if deg.get((i, ft[i]), 0) + 1 > max_deg:
                    bad = True
                    break
            if not bad:
                out.add(ft)

    def rec(assign, unmet):
        if not unmet:
            fill_free(assign)
            return
        e = unmet[0]
        for i in range(R6):
            if assign[i] is not None:
                continue
            if deg.get((i, e[i]), 0) + 1 > max_deg:
                continue
            a2 = list(assign)
            a2[i] = e[i]
            rec(tuple(a2), [g for g in unmet if g[i] != e[i]])

    rec((None,) * R6, list(H))
    return sorted(out)


def census(m_t, t_t, caps, xcap, label):
    """PATH A: isomorph-free edge-wise growth to m_t edges with tau >= t_t.

    Sound because every prune is monotone: degrees only grow (so the caps hold
    at every stage), X only grows, and tau rises by at most one per edge added
    (so a family that cannot reach t_t in the edges remaining is dead)."""
    seed = (tuple([0] * R6),)
    level = {canon_fast(seed): seed}
    sizes = [1]
    for size in range(1, m_t):
        t0 = time.time()
        need = t_t - (m_t - size - 1)
        nxt = {}
        for H in level.values():
            deg = degrees_of(H)
            nsym = [len({e[i] for e in H}) for i in range(R6)]
            for f in extensions(H, nsym, deg, caps[1]):
                H2 = tuple(sorted(H + (f,)))
                d2 = degrees_of(H2)
                if not profile_ok(d2, caps):
                    continue
                if xcap is not None:
                    x = -comb(len(H2), 2)
                    for d in d2.values():
                        x += (d * (d - 1)) // 2
                    if x > xcap:
                        continue
                if need > 0 and has_cover(H2, need - 1):
                    continue
                c = canon_fast(H2)
                if c not in nxt:
                    nxt[c] = H2
        level = nxt
        sizes.append(len(level))
        prog("%s level %d: %d classes [%.1fs]"
             % (label, size + 1, len(level), time.time() - t0))
    return [H for H in level.values() if not has_cover(H, t_t - 1)], sizes


prog("PATH A: edge-wise growth, Delta <= 3, prefix caps, tau lookahead, X <= 2")
tA = time.time()
CENSUS_A, SIZES_A = census(8, 4, CAPS8, XCAP8, "(8,4)")
tA = time.time() - tA
check("PATH A: the (8, tau >= 4) census has exactly 5 isomorphism classes",
      len(CENSUS_A) == 5,
      "level sizes %s, %.0fs" % (SIZES_A, tA))
check("each is 6-uniform, 6-partite, intersecting, 8 distinct edges, tau = 4",
      all(len(H) == 8 and len(set(H)) == 8 and is_intersecting(H)
          and tau_of(H) == 4 for H in CENSUS_A))
check("each has Delta = 3 exactly -- the cap is attained, so it was not a "
      "silently over-tight prune",
      all(max(degrees_of(H).values()) == 3 for H in CENSUS_A))
check("each representative uses contiguous symbols 0..n-1 in every part",
      all(symbols_of(H)[q] == list(range(len(symbols_of(H)[q])))
          for H in CENSUS_A for q in range(R6)),
      "growth introduces only the next free symbol, so this holds by "
      "construction -- checked rather than assumed, because section 5 indexes "
      "vertices by symbol")

# g(4) = 8 exactly falls out: section 1 proved >= 8, and the census exhibits it.
check("g(4) = 8 exactly: section 1 gave >= 8 and the census exhibits 8-edge "
      "objects with tau = 4", len(CENSUS_A) > 0 and G[4] == 8,
      "the upper bound is a by-product here and is used nowhere")

# ---- the corollary that cross-checks certificate 0005 -------------------
profs8 = sorted({part_profile(H, q) for H in CENSUS_A for q in range(R6)})
check("every part of every class has profile (3,2,2,1) or (3,2,1,1,1)",
      profs8 == [(3, 2, 1, 1, 1), (3, 2, 2, 1)],
      "over all 5 x 6 = 30 parts the whole list is %s" % (profs8,))
note("that is the per-part half of the corrected AKP Lemma 2.8",
     "certificate 0005 derives the same dichotomy from its (2,2,2,2) "
     "exhaustion, by a route with no code in common with this census. Agreement "
     "is corroboration, not proof, and 0005 is not consulted here.")

# ---- PATH B: peel a maximum-degree vertex ------------------------------
#
# Delta(R) = 3 exactly.  (L1) k=1 gives <= 3; and if every degree were <= 2 the
# pair count would fail, as the check below computes.  Peeling a vertex of
# degree 3 leaves R5 with 5 edges and tau(R5) >= 3 (same argument as 3(a)), and
# tau(R5) >= 4 would need |R5| >= g(4) >= 8.  So tau(R5) = 3 exactly, and (L1)
# on R5 gives Delta(R5) <= 5 - g(2) = 2.  So every (8,4) object is a (5,3)
# object with a 3-star attached.

MP8_2 = maxpairs(8, {1: 2})
check("Delta(R) = 3 exactly: degrees all <= 2 would give at most 6 x 4 = 24 "
      "agreeing pairs against C(8,2) = 28",
      MP8_2[0] == 4 and 6 * MP8_2[0] < comb(8, 2),
      "maximiser %s; combined with the (L1) cap Delta <= 3" % (MP8_2[1],))

CAPS5 = {k: 5 - G[3 - k] for k in (1, 2)}
check("the (L1) prefix caps for a 5-edge tau >= 3 object are {1:2, 2:4}",
      CAPS5 == {1: 2, 2: 4})
MP5 = maxpairs(5, CAPS5)
XCAP5 = 6 * MP5[0] - comb(5, 2)
prog("PATH B: (5, tau >= 3) census, then attach 3-stars")
CENSUS_5, SIZES_5 = census(5, 3, CAPS5, XCAP5, "(5,3)")
check("the (5, tau >= 3) census has exactly 12 isomorphism classes, each "
      "intersecting with tau = 3 exactly",
      len(CENSUS_5) == 12
      and all(len(H) == 5 and len(set(H)) == 5 and is_intersecting(H)
              and tau_of(H) == 3 for H in CENSUS_5),
      "level sizes %s; tau = 4 would need |R5| >= g(4) = 8" % (SIZES_5,))


def all_covers_of_size(H, k):
    """Every k-subset of V(H) covering H.  Brute force over C(|V|, k)."""
    vm = vertex_masks(H)
    V = sorted(vm)
    full = (1 << len(H)) - 1
    out = []
    for S in itertools.combinations(V, k):
        m = 0
        for v in S:
            m |= vm[v]
        if m == full:
            out.append(frozenset(S))
    return out, V


def covering_patterns(R, nsym, p, covlist):
    """EVERY assignment of the five parts other than p to (a symbol of R, or
    FRESH) whose non-fresh vertices cover R.  No cap on the number of fresh
    coordinates -- the cap is a conclusion, and the caller checks it.

    Returns a list of (combo, n_fresh, escape_mask) with the mask taken over
    `covlist`: bit j is set iff the pattern avoids covlist[j] entirely."""
    others = [q for q in range(R6) if q != p]
    vm = vertex_masks(R)
    hit = {}
    for j, C in enumerate(covlist):
        b = 1 << j
        for v in C:
            hit[v] = hit.get(v, 0) | b
    fullE = (1 << len(R)) - 1
    fullK = (1 << len(covlist)) - 1
    out = []
    ranges = [list(range(nsym[q])) + [FRESH] for q in others]
    for combo in itertools.product(*ranges):
        cov = 0
        h = 0
        nf = 0
        for q, s in zip(others, combo):
            if s == FRESH:
                nf += 1
            else:
                cov |= vm.get((q, s), 0)
                h |= hit.get((q, s), 0)
        if cov != fullE:
            continue
        out.append((combo, nf, fullK & ~h))
    return others, out


def set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for sub in set_partitions(rest):
        for i in range(len(sub)):
            yield sub[:i] + [[first] + sub[i]] + sub[i + 1:]
        yield [[first]] + sub


def full_or_multisets(masks, size, K):
    """EVERY multiset of EXACTLY `size` values drawn from `masks` whose OR is
    all-ones -- not merely the minimal ones.

    Complete by the same element-driven argument the section 5 search uses.
    Given a target multiset M with OR all-ones, at every stage some unused
    member of M contains the lowest uncovered element, so the branch that picks
    it is explored.  Once the running OR is already all-ones the remaining
    slots are filled with ANY mask, because a star's third edge still exists
    and still has to be built even when the first two already escape every
    cover -- stopping at minimal solutions here would silently drop objects.
    Results are deduplicated as sorted tuples of mask VALUES."""
    full = (1 << K) - 1
    by_elem = [[m for m in masks if m >> j & 1] for j in range(K)]
    out = set()

    def rec(cov, chosen):
        if len(chosen) == size:
            if cov == full:
                out.add(tuple(sorted(chosen)))
            return
        if cov == full:
            for m in masks:
                rec(cov, chosen + [m])
            return
        j = 0
        while cov >> j & 1:
            j += 1
        for m in by_elem[j]:
            rec(cov | m, chosen + [m])

    rec(0, [])
    return sorted(out)


prog("PATH B: attaching 3-stars to the 12 (5,3) classes, all 6 parts each")
tB = time.time()
FOUND_B = {}
b_cand = 0
b_tau_bad = 0
maxfresh5 = 0
for R5 in CENSUS_5:
    nsym5 = [len(s) for s in symbols_of(R5)]
    cov3, _V5 = all_covers_of_size(R5, 3)
    K5 = len(cov3)
    for p in range(R6):
        others, pats = covering_patterns(R5, nsym5, p, cov3)
        for (_c, nf, _m) in pats:
            if nf > maxfresh5:
                maxfresh5 = nf
        use = [x for x in pats if x[1] <= 2]
        bymask = {}
        for (combo, nf, msk) in use:
            bymask.setdefault(msk, []).append(combo)
        for trip in full_or_multisets(sorted(bymask), 3, K5):
            # trip is a sorted tuple of 3 mask values; group by value and pick
            # a multiset of patterns from each group.  No index gymnastics: the
            # patterns of a star, grouped by their mask, form exactly this.
            groups = []
            for mv in sorted(set(trip)):
                k = trip.count(mv)
                groups.append(list(itertools.combinations_with_replacement(
                    bymask[mv], k)))
            for pick in itertools.product(*groups):
                sel = [c for g in pick for c in g]
                rows = []
                for c in sel:
                    row = [None] * R6
                    row[p] = nsym5[p]
                    for q, s in zip(others, c):
                        row[q] = s
                    rows.append(row)
                fslots = {q: [i for i in range(3) if rows[i][q] == FRESH]
                          for q in others}
                qs = [q for q in others if fslots[q]]
                stack = [(0, rows)]
                while stack:
                    kk, cur = stack.pop()
                    if kk == len(qs):
                        edges = [tuple(r) for r in cur]
                        if len(set(edges)) != 3:
                            continue
                        H8 = tuple(sorted(tuple(R5) + tuple(edges)))
                        b_cand += 1
                        if has_cover(H8, 3):
                            b_tau_bad += 1
                            continue
                        FOUND_B[canon_fast(H8)] = H8
                        continue
                    q = qs[kk]
                    for part in set_partitions(fslots[q]):
                        cur2 = [list(r) for r in cur]
                        for bb, block in enumerate(part):
                            for i in block:
                                cur2[i][q] = nsym5[q] + bb
                        stack.append((kk + 1, cur2))
tB = time.time() - tB

check("PATH B: attaching 3-stars to the (5,3) census also yields exactly 5 "
      "classes", len(FOUND_B) == 5,
      "%d candidate objects built, %.0fs" % (b_cand, tB))
check("and the two routes produce the IDENTICAL canonical set",
      set(FOUND_B) == {canon_fast(H) for H in CENSUS_A},
      "path A grew edge by edge from one edge; path B peeled to 5 edges and "
      "re-attached a star -- no shared enumeration")
check("SUFFICIENCY of the mask condition, one rung below section 5: every "
      "object path B builds from a full-OR mask triple really does have "
      "tau >= 4", b_tau_bad == 0 and b_cand > 0,
      "%d of %d candidates failed the tau test" % (b_tau_bad, b_cand))
note("and A = B tests the OTHER half of 3(d) -- the half section 5 uses",
     "path B enumerates ONLY full-OR mask triples, so it can be complete just "
     "when every (8, tau >= 4) object's own 3-star ORs to all-ones: the "
     "NECESSITY direction. Path A never mentions a mask. So their agreeing at "
     "5 classes is a test of necessity at the (5,3) rung, and the check above "
     "is sufficiency -- between them, both directions of 3(d), one rung under "
     "the place the kill spends them.")
check("the fresh cap 5 - tau(R5) = 2 is a conclusion, not an imposition",
      maxfresh5 == 2,
      "the uncapped product was enumerated at all 12 x 6 = 72 (R5, p) pairs; "
      "the largest number of fresh coordinates on any covering pattern is %d"
      % maxfresh5)

# ---- the slow canonical form, on the finals ----------------------------
slowA = {canon_slow(H) for H in CENSUS_A}
slowB = {canon_slow(H) for H in FOUND_B.values()}
check("the slow canonical form -- all 720 part orders, no invariant shortcut "
      "-- also separates the 5 classes and confirms A = B",
      len(slowA) == 5 and slowA == slowB,
      "720 part permutations x lex-least row order, run on all 10 finals")


# =========================================================================
# 5.  THE SWEEP.  No 5-star escapes any of the five residuals.
# =========================================================================

head("5.  the sweep: 5 residuals x 6 parts, and no admissible 5-star exists")


def search_index_order(masks, K, limit):
    """Is there a multiset of at most `limit` masks whose OR is all-ones?

    Branch on the LOWEST-INDEX uncovered element.  Complete: a solution covers
    every element, so in particular that one, so it uses one of the masks
    containing it.  No other pruning.  Returns (solvable, nodes)."""
    full = (1 << K) - 1
    allor = 0
    for m in masks:
        allor |= m
    if allor != full:
        return False, 1
    by_elem = [[m for m in masks if m >> j & 1] for j in range(K)]
    nodes = [0]

    def rec(cov, depth, lo):
        nodes[0] += 1
        if cov == full:
            return True
        if depth == limit:
            return False
        j = lo
        while cov >> j & 1:
            j += 1
        for m in by_elem[j]:
            if rec(cov | m, depth + 1, j + 1):
                return True
        return False

    return rec(0, 0, 0), nodes[0]


def search_rarest_order(masks, K, limit):
    """Same question, same completeness argument, different element order: the
    elements are ranked once, statically, by how few masks contain them, and
    the branch is always on the first uncovered element in that ranking."""
    full = (1 << K) - 1
    allor = 0
    for m in masks:
        allor |= m
    if allor != full:
        return False, 1
    by_elem = [[m for m in masks if m >> j & 1] for j in range(K)]
    order = sorted(range(K), key=lambda j: len(by_elem[j]))
    nodes = [0]

    def rec(cov, depth):
        nodes[0] += 1
        if cov == full:
            return True
        if depth == limit:
            return False
        j = -1
        for jj in order:
            if not cov >> jj & 1:
                j = jj
                break
        for m in by_elem[j]:
            if rec(cov | m, depth + 1):
                return True
        return False

    return rec(0, 0), nodes[0]


note("max_fresh = 1 is derived, not decreed",
     "a star edge's five non-p coordinates must cover R with their non-fresh "
     "part, and tau(R) = 4, so at most one may be fresh. Below, the pattern "
     "product is enumerated with NO cap and the cap is read off.")

n_pairs = 0
n_allor_dead = 0
n_solvable_A = 0
n_solvable_B = 0
n_disagree = 0
nodes_A = 0
nodes_B = 0
maxfresh8 = 0
tau_ok = 0
class_ok = []
Krep = []
for ci, R in enumerate(CENSUS_A):
    t0 = time.time()
    nsym = [len(s) for s in symbols_of(R)]
    cov3, V = all_covers_of_size(R, 3)
    cov4, V = all_covers_of_size(R, 4)
    if len(cov3) == 0 and len(cov4) > 0:
        tau_ok += 1
    K = len(cov4)
    Krep.append(K)
    ok_class = True
    for p in range(R6):
        others, pats = covering_patterns(R, nsym, p, cov4)
        for (_c, nf, _m) in pats:
            if nf > maxfresh8:
                maxfresh8 = nf
        masks = sorted({m for (_c, nf, m) in pats if nf <= 1}, reverse=True)
        gotA, nA = search_index_order(masks, K, 5)
        gotB, nB = search_rarest_order(masks, K, 5)
        allor = 0
        for m in masks:
            allor |= m
        if allor != (1 << K) - 1:
            n_allor_dead += 1
        n_pairs += 1
        nodes_A += nA
        nodes_B += nB
        if gotA:
            n_solvable_A += 1
        if gotB:
            n_solvable_B += 1
        if gotA != gotB:
            n_disagree += 1
        if gotA or gotB:
            ok_class = False
    class_ok.append(ok_class)
    prog("class %d: |V(R)| = %d, %d four-covers, 6 parts done [%.0fs]"
         % (ci, len(V), K, time.time() - t0))

check("tau(R) = 4 for all five residuals, checked in BOTH directions by brute "
      "force", tau_ok == 5,
      "no 3-subset of V(R) covers R (C(|V|,3) tested exhaustively) and 4-subsets "
      "do; four-cover counts %s" % (Krep,))
check("the fresh cap 5 - tau(R) = 1 is a conclusion, not an imposition",
      maxfresh8 == 1,
      "the uncapped product over all six parts of all five classes was "
      "enumerated; the largest number of fresh coordinates on any covering "
      "pattern is %d" % maxfresh8)
for ci in range(5):
    check("class %d: no admissible 5-star escapes every 4-cover, at any of the "
          "six parts" % ci, class_ok[ci])
check("all %d (residual, part) pairs were swept -- 5 classes x 6 parts"
      % n_pairs, n_pairs == 30)
check("UNSOLVABLE at every pair under the lowest-index-uncovered order",
      n_solvable_A == 0, "%d search nodes" % nodes_A)
check("UNSOLVABLE at every pair under the static rarest-first order too",
      n_solvable_B == 0,
      "%d search nodes -- a %dx smaller tree reaching the same verdict"
      % (nodes_B, nodes_A // max(nodes_B, 1)))
check("the two orders agree at every pair", n_disagree == 0)
check("at 5 of the 30 pairs the OR of EVERY admissible pattern's mask already "
      "misses a 4-cover, so no star of any size could work",
      n_allor_dead == 5,
      "the search is not even entered there; the other 25 need it")


# =========================================================================
# 6.  CONTROLS
# =========================================================================

head("6.  controls: the theorem is non-vacuous, and the machinery can say yes")

# W: 13 edges, 6-partite, intersecting, tau = 5.  Copied from certificate 0008
# section 3 and re-verified here from scratch.
W = ((0, 1, 4, 2, 3, 1), (0, 2, 3, 4, 1, 2), (0, 4, 1, 3, 2, 4),
     (1, 1, 0, 3, 4, 2), (1, 2, 4, 0, 2, 3), (2, 0, 2, 2, 2, 2),
     (2, 3, 4, 3, 1, 0), (2, 4, 3, 0, 4, 1), (3, 1, 2, 0, 1, 4),
     (4, 0, 4, 4, 4, 4), (4, 1, 3, 1, 2, 0), (4, 2, 2, 3, 0, 1),
     (4, 3, 1, 0, 3, 2))
Wdeg = degrees_of(W)
Wv = sorted(Wdeg)
check("the witness W has 13 distinct edges, is 6-partite 6-uniform and "
      "intersecting",
      len(W) == 13 and len(set(W)) == 13 and all(len(e) == R6 for e in W)
      and is_intersecting(W), "all %d pairs meet" % comb(13, 2))

t0 = time.time()
has4 = False
vmW = vertex_masks(W)
fullW = (1 << 13) - 1
for S in itertools.combinations(Wv, 4):
    m = 0
    for v in S:
        m |= vmW[v]
    if m == fullW:
        has4 = True
        break
cover5 = [(0, s) for s in range(5)]
m5 = 0
for v in cover5:
    m5 |= vmW.get(v, 0)
check("tau(W) = 5 exactly, by brute force over every 4-subset of V(W)",
      (not has4) and m5 == fullW,
      "no cover among C(%d,4) = %d subsets; explicit 5-cover = all of part 0; "
      "%.0fs" % (len(Wv), comb(len(Wv), 4), time.time() - t0))

D4 = sorted(v for v, d in Wdeg.items() if d == 4)
check("Delta(W) = 4, attained at seven vertices -- so the theorem is neither "
      "vacuous nor loose",
      max(Wdeg.values()) == 4 and len(D4) == 7,
      "degree-4 vertices %s" % (D4,))

# ---- RECOVERY: the same machinery, on an instance with a known answer ----
#
# Peel a degree-4 vertex v of W.  The residual R9 has 9 edges and tau(R9) = 4,
# so the escape structure of section 3 applies verbatim at t = 5 with a 4-star
# instead of a 5-star.  W itself realises a solution, so the machinery MUST
# say SOLVABLE -- and its pattern enumeration MUST contain W's own star.

n_rec = 0
rec_member = 0
rec_full = 0
rec_dfs = 0
rec_tau = 0
rec_nodes = 0
tooth_member = 0
tooth_dfs = 0
for v in D4:
    p, s = v
    star = [e for e in W if e[p] == s]
    R9raw = [e for e in W if e[p] != s]
    maps = []
    for q in range(R6):
        mp = {}
        for e in R9raw:
            if e[q] not in mp:
                mp[e[q]] = len(mp)
        maps.append(mp)
    R9 = tuple(tuple(maps[q][e[q]] for q in range(R6)) for e in R9raw)
    nsym9 = [len(maps[q]) for q in range(R6)]
    cov3, _ = all_covers_of_size(R9, 3)
    cov4, _ = all_covers_of_size(R9, 4)
    if len(cov3) == 0 and len(cov4) > 0:
        rec_tau += 1
    K = len(cov4)
    fullK = (1 << K) - 1
    others, pats = covering_patterns(R9, nsym9, p, cov4)
    patmap = {}
    for (combo, nf, msk) in pats:
        if nf <= 1:
            patmap[combo] = msk
    wpats = [tuple(maps[q].get(e[q], FRESH) for q in others) for e in star]
    if all(c in patmap for c in wpats):
        rec_member += 1
    wor = 0
    for c in wpats:
        wor |= patmap.get(c, 0)
    if wor == fullK:
        rec_full += 1
    masks = sorted(set(patmap.values()), reverse=True)
    gotA, nA = search_index_order(masks, K, 4)
    gotB, nB = search_rarest_order(masks, K, 4)
    rec_nodes += nA + nB
    if gotA and gotB:
        rec_dfs += 1
    # TOOTH: the under-enumeration bug family, simulated.  max_fresh = 0 drops
    # exactly the patterns with a fresh coordinate -- the commonest way an
    # enumeration silently misses cases -- and the control must die.
    pat0 = {combo: msk for (combo, nf, msk) in pats if nf <= 0}
    if all(c in pat0 for c in wpats):
        tooth_member += 1
    masks0 = sorted(set(pat0.values()), reverse=True)
    g0A, _ = search_index_order(masks0, K, 4)
    g0B, _ = search_rarest_order(masks0, K, 4)
    if g0A or g0B:
        tooth_dfs += 1
    n_rec += 1

check("all seven degree-4 vertices of W were peeled", n_rec == 7)
check("each peel leaves a 9-edge residual with tau = 4 exactly, both directions "
      "brute-forced", rec_tau == 7)
check("MEMBERSHIP: W's own four star edges appear in the enumerated pattern "
      "list, at every peel", rec_member == 7,
      "an enumeration that misses a real object's own configuration is the "
      "failure mode section 5 is exposed to")
check("FULL-OR: the four real star patterns' escape masks OR to all-ones, at "
      "every peel", rec_full == 7,
      "so the mask encoding agrees with tau(W) = 5 on an object that has it")
check("SOLVABLE: the section 5 search, unchanged, finds a solution at every "
      "peel, in both element orders", rec_dfs == 7,
      "%d search nodes; the same code that returns UNSOLVABLE 30 times in "
      "section 5 returns SOLVABLE 14 times here" % rec_nodes)
check("TOOTH: with the fresh cap wrongly set to 0, the membership clause fails "
      "at all seven peels", tooth_member == 0,
      "the commonest under-enumeration bug is visibly fatal to the control, "
      "which is what makes the control worth running")
check("TOOTH: and the search then reports UNSOLVABLE at all seven peels -- a "
      "false negative of exactly the shape section 5 reports", tooth_dfs == 0,
      "so section 5's emptiness is only as good as its enumeration, and the "
      "enumeration is the thing checked twice above")


# =========================================================================
# 7.  RESULT
# =========================================================================

head("7.  result")


def full_part_profiles(m, t):
    """What a FULL part's degree profile could be: at least t active vertices
    (a part is a cover, and tau >= t), each of degree >= 2, summing to m."""
    out = []

    def rec(left, cur):
        if left == 0:
            if len(cur) >= t:
                out.append(tuple(cur))
            return
        for s in range(min(left, cur[-1] if cur else left), 1, -1):
            rec(left - s, cur + [s])

    rec(m, [])
    return out


fp13 = sorted(full_part_profiles(13, 5))
survive = sorted(p for p in fp13 if max(p) <= 4)
check("a 13-edge tau >= 5 witness's FULL part has one of exactly four degree "
      "profiles", len(fp13) == 4 and fp13 == sorted(
          [(5, 2, 2, 2, 2), (4, 3, 2, 2, 2), (3, 3, 3, 2, 2),
           (3, 2, 2, 2, 2, 2)]),
      "enumerated: %s" % (fp13,))
check("Delta <= 4 excludes exactly one of them, (5,2,2,2,2), leaving three",
      len(survive) == 3 and (5, 2, 2, 2, 2) not in survive,
      "survivors %s" % (survive,))
Wfull = [q for q in range(R6) if min(part_profile(W, q)) >= 2]
check("and the list is not vacuous: W has a full part, and its profile is one "
      "of the three survivors",
      len(Wfull) == 1 and part_profile(W, Wfull[0]) in survive,
      "part %d of W has profile %s"
      % (Wfull[0], part_profile(W, Wfull[0])))
note("this three-profile list is NOT new -- what is new is that it no longer "
     "needs N(4) = 9",
     "the turn-5 notebook derives the same three profiles from the ladder cap "
     "d1 <= 13 - N(4) = 4, so the list stood on the 52M-node exhaustion of "
     "certificate 0005 (since re-proved by hand in 0010). This certificate "
     "reaches the same exclusion from g(4) >= 8 and g(5) >= 12 alone, and "
     "bounds ALL SIX parts rather than the distinguished one. Two routes, one "
     "answer, and the second does not touch the floor's hinge.")
note("nor does anything here consume certificate 0009's g(5) = 13",
     "section 1 derives g(5) >= 12 for itself, which is all the reduction "
     "needs (it only has to beat 8). The stronger rung would change nothing.")

print("""
  g(2) >= 3, g(3) >= 5, g(4) >= 8, g(5) >= 12   PROVEN-BY-CERTIFICATE (sec. 1)
  the (8, tau >= 4) census is 5 classes         PROVEN-BY-CERTIFICATE (sec. 4)
  Delta >= 4 at m = 13, any tau                 PROVEN-BY-CERTIFICATE (sec. 2)
  Delta <= 4 at m = 13, tau >= 5                PROVEN-BY-CERTIFICATE (sec. 5)

  **every 6-partite 6-uniform intersecting hypergraph with 13 edges and
    tau >= 5 has Delta = 4 exactly**            PROVEN-BY-CERTIFICATE,
                                                CITING NOTHING

  EXTERNAL INPUTS -- NONE.  Nothing to remove, so no fallback floor to state.
  f(6) = 13 is not used: "13 edges" is a hypothesis, not a borrowed constant.

  Where the weight sits.  The whole upper half funnels through the claim that
  the (8, tau >= 4) census is complete at 5 classes.  Two routes with no shared
  enumeration agree on it, and the finals survive the slow 720-permutation
  canonical form -- but both routes consume the same ladder from section 1, so
  an error in g(3) >= 5 or g(4) >= 8 would move both together.  Section 1 is
  eleven lines of counting and is the place to attack.

  What this does NOT do.  It does not bound m for a Ryser counterexample; that
  needs tau = 6, and this is a statement about tau >= 5 at exactly 13 edges. It
  is used nowhere load-bearing, by design: it was written because it was the
  last uncertified turn-4 result, not because anything waits on it.
""")

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(1 if FAILED else 0)
