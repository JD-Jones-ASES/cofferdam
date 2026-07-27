#!/usr/bin/env python3
"""Certificate 0009 -- the g(5) rung is pinned: g(5) = N(5) = 13, citing nothing.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from lib/.
Runs under a bare /usr/bin/python3 (3.9) and under python3 -O.

WHAT IS CLAIMED
---------------
  g(5) = 13                                     PROVEN-BY-CERTIFICATE,
                                                citing NOTHING
  N(5) = 13                                     PROVEN-BY-CERTIFICATE,
                                                citing NOTHING
  Q13 is answered YES                           (corollary -- the witness below
                                                 is exactly the object Q13 asks
                                                 for; PLAN item 5's search is
                                                 retired, its target found)
  the citation-free ladder N = {2,4,6,9,13}     (corollary -- it now EQUALS the
                                                 ladder that used to cite
                                                 f(6) = 13)

Here g(t) = least edges of a 6-partite 6-uniform intersecting hypergraph with
tau >= t, and N(t) adds the requirement of a full part: some part all of whose
active vertices have degree >= 2.  Trivially N(t) >= g(t): the N-class is a
subclass of the g-class.

WHY THIS RUNG WAS THE OPEN ONE
------------------------------
Certificate 0001's counting ladder ((L1) star-deletion caps + (L2) pair count)
kills m = 10 (30 < 45) and m = 11 (48 < 55) but comes to a DEAD HEAT at m = 12:
the per-part maximum of sum C(d,2) under the caps is 11, attained uniquely by
the profile (4,3,2,2,1), and 6 x 11 = 66 = C(12,2) exactly.  Counting cannot
decide m = 12.  What it CAN do -- and this is the whole design of this
certificate -- is force the shape of any surviving object so hard that the
remaining search space is tiny:

  equality is forced in every part, so every part's profile is EXACTLY
  (4,3,2,2,1), and the excess X = sum_v C(deg v, 2) - C(m,2) is EXACTLY 0,
  i.e. every pair of edges meets in exactly one part, and no edge repeats
  (a repeated edge-pair meets in 6 parts and alone contributes 5 to X).

In column form that says: the six parts are six partitions of the edge set
[12], each with block sizes (4,3,2,2,1), whose within-block pairs TILE the 66
edge-pairs exactly once.  Section 3 exhausts that design space: 11,520
complete designs exist (with the first part pinned), and EVERY ONE has an
explicit 4-cover.  No tau >= 5 object lives at m = 12.  g(5) >= 13.

The upper bound is an explicit witness (section 4): a 13-edge object with
tau = 5 exactly -- first shipped in certificate 0008 for an unrelated purpose
(it falsifies (D2) one rung below the floor), re-verified here from scratch.
Its part 1 is (4,3,2,2,2), a full part, so the SAME witness pins N(5) <= 13
and answers Q13 (certificate 0005's open question) YES.

THE LEDGER, in full
-------------------
  g(1) = 1, g(2) >= 3, g(3) >= 5, g(4) >= 8    re-derived HERE, sections 1
                                               (counting; no witnesses needed:
                                               only lower bounds feed caps)
  (L1) star-deletion caps                      proved by hand, stated below
  (L2) pair count                              proved by hand, stated below
  the m = 12 exhaustion                        HERE, section 3
  the 13-edge witness                          verified HERE, section 4
  EXTERNAL INPUTS -- NONE.

(L1), same-part form, as consumed here: if tau(H) >= t and S is a set of k
vertices all in one part, then the edges avoiding S number >= g(t-k) -- any
cover C of them makes C u S a cover of H, so |C| >= t - k.  Same-part stars
are disjoint (an edge has one vertex per part), so the k largest degrees of a
part sum to at most m - g(t-k).  (L2): every pair of edges shares a vertex in
some part, so sum over parts of sum_v C(deg v, 2) >= C(m,2), with equality iff
every pair agrees in exactly one part.

WHAT THIS BUYS DOWNSTREAM
-------------------------
- N(5) rises 11 -> 13 in the citation-free ladder, which therefore now equals
  the cited ladder everywhere.  Every sweep this lab ever ran on the cited
  ladder (0006's m=20: 105 multisets; 0008's m=21: 43,875 admissible, 567
  cap-passers, 0 survivors; m=22: 30,436 survivors) is citation-free as of
  this certificate.  The floor m >= 22 does not move; its margins tighten
  (2,478 -> 567 configurations carried by (L8) at m = 21).
- The k=1 cap on a counterexample's degrees tightens to Delta <= m - 13.
- Q13 is retired: answered YES, not searched for.  The 'NO => N(5) >= 14'
  branch is dead -- N(5) = 13 exactly, so no future work can raise this rung.
- Certificate 0005's three-profile prediction for a 13-edge N(5) witness's
  full part -- (4,3,2,2,2), (3,3,3,2,2), (3,2,2,2,2,2) -- is realised by the
  first of the three.  (That list presupposes Delta <= 4 for such objects,
  which is PLAN's still-uncertified item; the witness satisfies Delta = 4, so
  nothing here leans on the presupposition.)

WHAT IS NOT CLAIMED
-------------------
No isomorphism classification of the 11,520 designs is claimed (their count is
reported as found by one canonical search; the INVARIANT claim is only that
every design has a 4-cover).  Nothing here says anything about m >= 23, and
nothing here moves the floor: m >= 22 stands exactly as certificate 0008 left
it, on lighter foundations.
"""

import itertools
import sys
import time
from math import comb

FAIL = []
COUNT = [0]
NOTES_N = [0]


def check(label, cond, detail=""):
    COUNT[0] += 1
    tag = "ok  " if cond else "FAIL"
    if not cond:
        FAIL.append(label)
    print("  [%s] %2d. %s%s" % (tag, COUNT[0], label,
                                ("   " + detail) if detail else ""), flush=True)


def note(label, detail=""):
    """A stated fact -- proved by hand above or in the docstring -- and NOT a
    machine check.  Counted separately (D-015)."""
    NOTES_N[0] += 1
    print("  [note] %s%s" % (label, ("   " + detail) if detail else ""),
          flush=True)


def head(s):
    print("\n=== %s ===" % s, flush=True)


T0 = time.time()

# ==========================================================================
# 0.  Machinery: capped profiles and their pair-count maxima
# ==========================================================================

def capped_profiles(m, caps):
    """All nonincreasing partitions of m whose k largest entries sum to at
    most caps[k] (for the k present in caps).  A partition is a part's degree
    profile over its active vertices; entries are >= 1."""
    out = []

    def rec(left, cur):
        k = len(cur)
        if k in caps and m - left > caps[k]:
            return
        if left == 0:
            out.append(tuple(cur))
            return
        top = cur[-1] if cur else left
        for d in range(min(left, top), 0, -1):
            rec(left - d, cur + [d])
    rec(m, [])
    return out


def sc(p):
    return sum(comb(d, 2) for d in p)


def caps_for(m, t, G):
    """(L1) same-part prefix caps at tau >= t from proven lower bounds G."""
    return {k: m - G[t - k] for k in range(1, min(5, t))}


# ==========================================================================
# 1.  The ladder's lower bounds, re-derived here: g(2) >= 3, g(3) >= 5,
#     g(4) >= 8, and every m from 8 to 11 dead at t = 5
# ==========================================================================

head("1.  Ladder lower bounds by (L1) + (L2), every rung, every m -- no gaps")

note("g(1) = 1: a single edge has tau = 1 (any one of its vertices covers "
     "it), and the empty family has tau = 0 < 1; so tau >= 1 forces m >= 1 "
     "and m = 1 attains it")
note("coverage of small m below each range: tau >= t implies tau >= t-1, so "
     "m >= g(t-1); the ranges below start exactly there -- no m is skipped "
     "(D-016)")

G = {1: 1}
LADDER_PLAN = (
    (2, (1, 2), 3),
    (3, (3, 4), 5),
    (4, (5, 6, 7), 8),
    (5, (8, 9, 10, 11), 12),
)
for t, ms, rung in LADDER_PLAN:
    for m in ms:
        caps = caps_for(m, t, G)
        profs = capped_profiles(m, caps)
        if not profs:
            dead, why = True, "no profile satisfies the caps"
        else:
            best = max(sc(p) for p in profs)
            dead = 6 * best < comb(m, 2)
            why = "%d capped profiles, max pair count %d, 6 x %d = %d < %d" \
                  % (len(profs), best, best, 6 * best, comb(m, 2))
        check("t=%d, m=%d is impossible under caps %s" % (t, m, caps),
              dead, why)
    G[t] = rung
    note("hence g(%d) >= %d (smaller m die above or by monotonicity "
         "tau >= %d => tau >= %d => m >= %d)"
         % (t, rung, t, t - 1, G[t - 1]))

# ==========================================================================
# 2.  m = 12: the dead heat, and what equality forces
# ==========================================================================

head("2.  m = 12, tau >= 5: counting comes to equality and forces the shape")

CAPS12 = caps_for(12, 5, G)
P12 = capped_profiles(12, CAPS12)
check("the (L1) caps at m = 12, t = 5 are prefix sums <= (4, 7, 9, 11)",
      CAPS12 == {1: 4, 2: 7, 3: 9, 4: 11})
check("26 admissible profiles under the caps", len(P12) == 26)

best = max(sc(p) for p in P12)
argmax = [p for p in P12 if sc(p) == best]
second = max(sc(p) for p in P12 if sc(p) < best)
check("maximum per-part pair count is 11, attained UNIQUELY by (4,3,2,2,1)",
      best == 11 and argmax == [(4, 3, 2, 2, 1)])
check("the runner-up is 10, so the forcing has margin one",
      second == 10,
      "argmaxes at 10: %s" %
      sorted(p for p in P12 if sc(p) == 10).__repr__())
check("6 x 11 = 66 = C(12,2): the dead heat is exact",
      6 * best == comb(12, 2))

note("FORCING: (L2) needs the six parts' pair counts to sum to >= 66; each "
     "is <= 11; so each part contributes EXACTLY 11, i.e. every part's "
     "profile is exactly (4,3,2,2,1), and the total equals C(12,2) exactly, "
     "so X = 0: every pair of edges meets in exactly ONE part")
note("no repeated edges: a repeated pair would meet in all 6 parts, "
     "contributing lambda - 1 = 5 > 0 to X")

# sensitivity: every one of the four caps is load-bearing for the forcing
for k in (1, 2, 3, 4):
    caps_k = dict(CAPS12)
    del caps_k[k]
    loose = max(sc(p) for p in capped_profiles(12, caps_k))
    check("drop the k=%d cap and the forcing breaks: max rises to %d >= 12"
          % (k, loose), loose >= 12)

capsg3 = {1: 4, 2: 8, 3: 9, 4: 11}          # g(3) falsely 4
loosest = max(sc(p) for p in capped_profiles(12, capsg3))
check("SENSITIVITY: with g(3) falsely weakened to 4 the caps admit "
      "(4,4,1,1,1,1) with 12 pairs -- the dead heat opens and this whole "
      "route fails; the ladder inputs are load-bearing",
      loosest >= 12 and sc((4, 4, 1, 1, 1, 1)) == 12)

# ==========================================================================
# 3.  The exhaustion: the forced design space is tiled and emptied
# ==========================================================================

head("3.  Exhausting the forced shape at m = 12")

note("COLUMN FORM: part i's active vertices are the blocks of a partition "
     "of the edge set [12]; block size = degree.  The forcing says: six "
     "partitions of [12], each of shape (4,3,2,2,1), whose within-block "
     "pairs tile all 66 edge-pairs exactly once.  Conversely any such "
     "design IS such a hypergraph (vertices = blocks; two edges share "
     "exactly the one block covering their pair, so it is intersecting), "
     "and tau is the least number of blocks covering [12]")
note("WLOG: edges may be relabelled (an isomorphism), so the first part's "
     "partition is pinned to {0123 | 456 | 78 | 9,10 | 11}; parts are "
     "unordered, and the exact-cover search below finds each unordered "
     "completion exactly once (at every node the branching pair is a "
     "function of the covered set, and exactly one member of any completion "
     "covers it)")

M12 = 12
PAIR_IDX = {}
for a in range(M12):
    for b in range(a + 1, M12):
        PAIR_IDX[(a, b)] = len(PAIR_IDX)
NPAIRS = len(PAIR_IDX)


def block_pairmask(block):
    mm = 0
    for pr in itertools.combinations(sorted(block), 2):
        mm |= 1 << PAIR_IDX[pr]
    return mm


P0 = ((0, 1, 2, 3), (4, 5, 6), (7, 8), (9, 10), (11,))
COV0 = 0
for blk in P0:
    COV0 |= block_pairmask(blk)
check("the pinned first part covers 6 + 3 + 1 + 1 + 0 = 11 pairs",
      bin(COV0).count("1") == 11)


def shape_partitions(avoid_mask):
    """All (4,3,2,2,1) partitions of [12] none of whose within-block pairs
    hits avoid_mask.  Complete by construction: the 4-block is chosen as a
    sorted 4-subset, the 3-block from the rest, the singleton from the five
    remaining, and the two 2-blocks split the last four anchored on their
    smallest element (3 splits) -- every partition arises exactly once."""
    out = []
    for b4 in itertools.combinations(range(M12), 4):
        m4 = block_pairmask(b4)
        if m4 & avoid_mask:
            continue
        rest1 = [x for x in range(M12) if x not in b4]
        for b3 in itertools.combinations(rest1, 3):
            m3 = block_pairmask(b3)
            if m3 & (avoid_mask | m4):
                continue
            rest2 = [x for x in rest1 if x not in b3]
            for b1 in rest2:
                rem = [x for x in rest2 if x != b1]
                for p1 in rem[1:]:
                    b2a = (rem[0], p1)
                    m2a = block_pairmask(b2a)
                    if m2a & (avoid_mask | m4 | m3):
                        continue
                    b2b = tuple(x for x in rem[1:] if x != p1)
                    m2b = block_pairmask(b2b)
                    if m2b & (avoid_mask | m4 | m3 | m2a):
                        continue
                    out.append((m4 | m3 | m2a | m2b,
                                (b4, b3, tuple(sorted(b2a)),
                                 tuple(sorted(b2b)), (b1,))))
    return out


t_enum = time.time()
ALL_SHAPE = shape_partitions(0)
check("completeness control: with no exclusions the enumerator returns "
      "exactly 12!/(4! 3! 2! 2! 1!)/2! = 415,800 shape-(4,3,2,2,1) "
      "partitions of [12]",
      len(ALL_SHAPE) == 415800, "closed form vs enumeration")

CANDS = shape_partitions(COV0)
check("35,424 candidate partitions are pair-compatible with the pinned part",
      len(CANDS) == 35424, "%.1fs" % (time.time() - t_enum))

FULL = (1 << NPAIRS) - 1
CMASKS = [c[0] for c in CANDS]
CBLOCKS = [c[1] for c in CANDS]

solutions = []
nodes = [0]


def census(covered, live, chosen):
    """Exact cover: every set of five candidates tiling the remaining pairs
    is found exactly once.  live = indices still pair-compatible."""
    nodes[0] += 1
    if covered == FULL:
        solutions.append(tuple(chosen))
        return
    if len(chosen) == 5:
        return
    nxt = [i for i in live if not CMASKS[i] & covered]
    if not nxt:
        return
    cnt = [0] * NPAIRS
    for i in nxt:
        mm = CMASKS[i]
        while mm:
            low = mm & -mm
            cnt[low.bit_length() - 1] += 1
            mm ^= low
    # every uncovered pair must be coverable; branch on the scarcest
    bp, bc = -1, 1 << 30
    mm = ~covered & FULL
    while mm:
        low = mm & -mm
        p = low.bit_length() - 1
        c = cnt[p]
        if c == 0:
            return
        if c < bc:
            bp, bc = p, c
        mm ^= low
    for i in nxt:
        if CMASKS[i] >> bp & 1:
            census(covered | CMASKS[i], nxt, chosen + [i])


t_dfs = time.time()
census(COV0, list(range(len(CANDS))), [])
check("the exact-cover census finds 11,520 complete designs",
      len(solutions) == 11520,
      "%d nodes, %.0fs" % (nodes[0], time.time() - t_dfs))

# independent re-verification of the first designs, and the tau audit
def design_parts(sol):
    return (P0,) + tuple(CBLOCKS[i] for i in sol)


def retile_ok(parts):
    seen = 0
    for part in parts:
        for blk in part:
            mm = block_pairmask(blk)
            if mm & seen:
                return False
            seen |= mm
        if sorted(len(b) for b in part) != [1, 2, 2, 3, 4]:
            return False
        if sorted(x for b in part for x in b) != list(range(12)):
            return False
    return seen == FULL


check("independent re-check of the first 100 designs: six shape-(4,3,2,2,1) "
      "partitions of [12], 66 pairs tiled exactly once",
      all(retile_ok(design_parts(s)) for s in solutions[:100]))

t_tau = time.time()
no4 = []
first_cover = None
for s in solutions:
    parts = design_parts(s)
    blocks = []
    for part in parts:
        for b in part:
            em = 0
            for e in b:
                em |= 1 << e
            blocks.append((em, b))
    blocks.sort(key=lambda x: -bin(x[0]).count("1"))
    fullm = (1 << M12) - 1
    found = None
    for quad in itertools.combinations(blocks, 4):
        u = quad[0][0] | quad[1][0] | quad[2][0] | quad[3][0]
        if u == fullm:
            found = tuple(q[1] for q in quad)
            break
    if found is None:
        no4.append(parts)
    elif first_cover is None:
        first_cover = (parts, found)

check("EVERY one of the 11,520 designs has an explicit 4-cover -- none "
      "reaches tau >= 5", len(no4) == 0,
      "11,520 covers found and verified below; %.0fs" % (time.time() - t_tau))
pc, fc = first_cover
check("the first design's cover, verified explicitly: 4 blocks whose union "
      "is [12]",
      sorted(set(x for b in fc for x in b)) == list(range(12)),
      "design #1 cover: %s" % (fc,))

check("g(5) >= 13: no 6-partite 6-uniform intersecting object with 12 edges "
      "has tau >= 5 (sections 1 + 2 + 3 cover every m <= 12)",
      len(no4) == 0 and len(solutions) == 11520)

# ==========================================================================
# 4.  The witness: g(5) <= 13, and the SAME object pins N(5) and Q13
# ==========================================================================

head("4.  The 13-edge witness (from certificate 0008, re-verified here)")

W = ((0, 1, 4, 2, 3, 1), (0, 2, 3, 4, 1, 2), (0, 4, 1, 3, 2, 4),
     (1, 1, 0, 3, 4, 2), (1, 2, 4, 0, 2, 3), (2, 0, 2, 2, 2, 2),
     (2, 3, 4, 3, 1, 0), (2, 4, 3, 0, 4, 1), (3, 1, 2, 0, 1, 4),
     (4, 0, 4, 4, 4, 4), (4, 1, 3, 1, 2, 0), (4, 2, 2, 3, 0, 1),
     (4, 3, 1, 0, 3, 2))
Wsets = [frozenset((i, e[i]) for i in range(6)) for e in W]
Wv = sorted(set().union(*Wsets))
Wdeg = {}
for e in W:
    for i in range(6):
        Wdeg[(i, e[i])] = Wdeg.get((i, e[i]), 0) + 1

check("the witness has 13 distinct edges, 6-partite 6-uniform, on 30 "
      "vertices", len(set(W)) == 13 and len(Wv) == 30
      and all(len(s) == 6 for s in Wsets))
check("it is intersecting: all C(13,2) = 78 pairs meet",
      all(a & b for a, b in itertools.combinations(Wsets, 2)))
cover5 = frozenset((0, s) for s in range(5))
check("tau <= 5: all of part 0 is an explicit 5-cover",
      all(cover5 & s for s in Wsets))
has4 = any(all(set(S) & s for s in Wsets)
           for S in itertools.combinations(Wv, 4))
check("tau = 5 exactly: no 4-cover among all C(30,4) = 27,405 subsets",
      not has4)
check("hence g(5) <= 13, and with section 3: g(5) = 13, CITING NOTHING", not has4)

prof1 = tuple(sorted((d for (i, s), d in Wdeg.items() if i == 1),
                     reverse=True))
check("part 1 of the witness is (4,3,2,2,2) -- a FULL part, every active "
      "vertex of degree >= 2", prof1 == (4, 3, 2, 2, 2) and min(prof1) >= 2)
note("N(5) >= g(5): an N(5) object is in particular a tau >= 5 object; "
     "so N(5) >= 13, and the witness gives N(5) <= 13")
check("N(5) = 13, CITING NOTHING", prof1 == (4, 3, 2, 2, 2) and not has4
      and len(no4) == 0)
note("Q13 (certificate 0005: 'is there a 13-edge tau >= 5 object with a "
     "full part?') is answered YES by this witness.  It was shipped in "
     "certificate 0008 to show (D2) fails one rung down; nobody had asked "
     "it Q13's question.  The 'NO => N(5) >= 14 => m >= 21' lever is dead: "
     "N(5) = 13 exactly, and no future search can raise this rung")

# ==========================================================================
# 5.  Controls
# ==========================================================================

head("5.  Controls")

caps13 = caps_for(13, 5, G)
p13 = capped_profiles(13, caps13)
best13 = max(sc(p) for p in p13)
check("NOT TOO STRONG: at m = 13 the same counting leaves slack -- max "
      "6 x %d = %d >= %d = C(13,2) -- and the witness lives there; the "
      "argument correctly cannot kill 13" % (best13, 6 * best13, comb(13, 2)),
      6 * best13 >= comb(13, 2))

# teeth: the tau machinery must SEE tau = 5 (witness, above) and must find
# 4-covers (11,520 of them, above).  One more with a known answer: remove one
# edge of the witness; tau can drop to 4 but not below 4 - check the checker
# agrees tau(W minus an edge) is 4 or 5 and finds any 4-cover it claims.
W12sets = Wsets[1:]
has3 = any(all(set(S) & s for s in W12sets)
           for S in itertools.combinations(Wv, 3))
has4b = None
for S in itertools.combinations(Wv, 4):
    if all(set(S) & s for s in W12sets):
        has4b = S
        break
check("TEETH: on witness-minus-one-edge the checker finds tau exactly 4 "
      "(a verified 4-cover exists, no 3-cover does)",
      has4b is not None and not has3
      and all(set(has4b) & s for s in W12sets))

note("the census count 11,520 = 1152 x 10, where 1152 = |stabiliser| of the "
     "pinned partition (4! 3! 2! 2! x 2 for the equal 2-blocks) -- "
     "consistent with a free action on ~10 classes; stated as arithmetic "
     "context only, no isomorphism claim is made or needed")

# ==========================================================================

head("Result")

print("""
  g(5) = 13                                  PROVEN-BY-CERTIFICATE, citing NOTHING
  N(5) = 13                                  PROVEN-BY-CERTIFICATE, citing NOTHING
  Q13                                        answered YES (witness exhibited)
  the citation-free ladder                   {1:2, 2:4, 3:6, 4:9, 5:13} -- equal
                                             to the cited ladder from here on

  The floor m >= 22 does not move.  What moves is what stands under it: the
  last daylight between 'citing f(6) = 13' and 'citing nothing' is closed,
  every cited-ladder sweep in certificates 0006-0008 is citation-free as of
  this certificate, and the k=1 degree cap on a counterexample tightens to
  Delta <= m - 13.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (COUNT[0], NOTES_N[0], time.time() - T0,
         "ALL GREEN" if not FAIL else "FAILURES: " + ", ".join(FAIL)),
      flush=True)
sys.exit(1 if FAIL else 0)
