#!/usr/bin/env python3
"""Certificate 0018 -- the X = 3 layer at the window floor is empty:
every edge-critical core at m = 22 has X >= 4.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from
lib/.  Runs under Python 3.9 and under python3 -O.  Deterministic.

WHAT IS CLAIMED
---------------
  X >= 4 FOR EVERY CRITICAL CORE AT m = 22            PROVEN-BY-CERTIFICATE
  (equivalently: no critical core at the window        (in-house: field
  floor has X = 3; with 0016's X >= 3, the floor        0005/0009/0012,
  is nonlinear by at least four units)                  (D2) 0008, covers
                                                        0013, 0015 steps
                                                        (2)-(3), 0016
                                                        (T) + X >= 3,
                                                        0017 C1 (CC4+)
                                                        + C2;
                                                        external NONE)

NOTATION.  As in 0016/0017: K edge-critical, 6-partite, 6-uniform,
intersecting, tau = 6, tau(K - e) = 5; lambda(f,g) = |f cap g|;
X = sum over pairs of (lambda - 1); x_e = sum_{f != e} (lambda(e,f) - 1);
T_e = e's private 5-cover (0013: T_e cap e = empty, T_e in V(K));
I_e = sum over pairs {f,g} in K - e of a*b, a = |f cap g cap e|,
b = |f cap g cap T_e|; Phi(n,k) = balanced-split minimum; w(d) =
Phi(d-1,5); W = sum_v deg(v) * w(deg v).

THE PROOF, IN ORDER
-------------------
Assume a critical core K at m = 22 with X = 3 (0016 proved X >= 3; this
certificate empties the X = 3 layer, so X >= 4).

 (0) TOOLS, all previously certified.  (CC4+) at X <= 4 (0017 C1 with
     0015 steps (2)-(3)): sum_i Phi(d_i-1, 5-b_i) <= I_e <= X - x_e,
     and the w-corollary sum_{v in e} w(deg v) <= 3 - x_e.  The
     unconditional pair-sum (C2) (0017).  The link W <= sum_e I_e
     (0015 step (2) + Phi nonincreasing in class count -- X- and m-free).
     The pinned-ladder field (0005 (A)(B), 0009/0012) and the (D2) cap
     (0008).  (0015's row-sum Lemma 1.2 is consumed NOWHERE in this
     certificate; the outside-reader audit caught it in the ledger and
     it is struck.)  LOCALIZATION (section 3): only
     EXCESSIVE pairs contribute to I_e, because a lambda-1 pair's single
     shared cell cannot lie in both e and T_e (0013: T_e cap e = empty);
     per excessive pair the term a*b is at most lambda - 1 at X <= 4
     (0017 C1's corner).

 (1) THE SHAPE CENSUS (section 2).  X = 3 = sum over pairs of
     (lambda-1), all terms >= 0, so the positive pair-excesses partition
     3: (3) a lambda-4 pair; (2,1) a lambda-3 pair + a lambda-2 pair,
     adjacent (sharing an edge) or disjoint; (1,1,1) three lambda-2
     pairs whose pair-graph is one of the FIVE 3-edge simple graphs:
     star K1,3, triangle, path P4, P3+K2, 3K2.  Eight shapes; every
     pair outside the ledger has lambda = 1 exactly -- any further
     lambda >= 2 pair adds excess and forces X >= 4, a contradiction
     available in every kill below ("the spent ledger").

 (2) SHAPE 1, the lambda-4 pair {f,g}: m <= 20 (section 4).  x_f =
     x_g = 3, so by the w-corollary every vertex of f and g has degree
     <= 6.  f,g agree on 4 parts (shared S, |S| = 4) and differ on 2.
     Every other edge e has lambda(e,f) = lambda(e,g) = 1 and is EITHER
     through exactly one shared cell -- at most sum_{u in S}(deg u - 2)
     <= 4*4 = 16 such -- OR meets f and g at private cells, which
     forces e to contain one of only TWO cross-cell pairs (channels);
     two edges in one channel would share two cells, a spent-ledger
     violation, so at most 2.  m - 2 <= 16 + 2 = 18.  Dead at 22.

 (3) SHAPE 2, lambda-3 + adjacent lambda-2 ({f,g}, {f,h}): m <= 21
     (section 5).  x_f = 3 caps all of f's degrees at 6; A = f cap g
     (3 cells); |f cap g cap h| <= 1 by the corner (a >= 2, s = 3 gives
     X >= 4).  Each e outside {f,g,h} is through-A (at most
     sum_A (deg - 2) <= 12) or crosses f-private to g-private cells in
     different parts: 6 channels, at most one edge each (a doubled
     channel is a THIRD excessive pair; the ledger has none to spare).
     m - 3 <= 12 + 6 = 18.  Dead at 22.

 (4) SHAPE 3, lambda-3 + disjoint lambda-2 ({f,g}, {h,k}): W <= 23
     (section 6).  HEAVY CONFINEMENT: a vertex z with deg z >= 7 and
     z outside U cup V (U = f cap g, V = h cap k) is impossible --
     every edge through z has I_e >= w(deg z) >= 1 by (CC4+)'s left
     side, so by localization it meets U cup V; two edges through z
     meeting U cup V at the same cell would share two cells (ledger);
     so deg z <= |U cup V| = 5 < 7.  Heavy vertices therefore lie in
     U cup V, where the certified x_e patterns cap the census: U (on f,
     x = 2) holds at most one 7; V (on h, x = 1) holds at most {7,7} or
     {8}.  Max W = 23 < 27, the field floor of section 7.  Dead.

 (5) THE FIELD (section 7).  The 67-profile pinned-ladder field at
     m = 22: the X = 3 layer holds 186,086 configurations; (D2) leaves
     15,451; the minimum W is 27; W <= 30 leaves exactly FIVE
     configurations -- one at W = 27 with heavy census (n7,n8,n9) =
     (0,0,1), four at W = 30 with census (2,1,0), every one of the five
     sitting ON the (D2) boundary at D2 = 11.

 (6) SHAPES 4-8, the (1,1,1) shapes: pair-sum maxima (section 8).
     W <= sum_e I_e <= sum over the three pairs of
     sum_{u in f cap g} (deg u - 2)  [(C2), lambda - 1 = 1].  Shared
     2-sets live on their pairs' edges, whose budgets cap degrees.
     EXHAUSTIVELY over all identification patterns of the six shared
     slots (set partitions filtered by the spent ledger: same-pair
     slots distinct; a vertex on both edges of a pair belongs to its
     shared set; unlisted edge-pairs share at most one vertex) and all
     degree assignments 2..9 under the per-edge budgets:
         star 24 · triangle 27 · path 27 · P3+K2 28 · 3K2 30.
     Star: 24 < 27, dead outright.  The other four reach the field.

 (7) THE (0,0,1) CONFIGURATION DIES FOR EVERY SHAPE (section 8, same
     enumeration): its only heavy vertex has degree 9, which appears in
     NO x_e >= 1 pattern, so it lies on no excess edge; with n7 = n8 =
     0 every shared vertex has degree <= 6 and the pair-sum caps at
     3*(4+4) = 24 < 27 = W.  Dead.  (This kills triangle, path and
     P3+K2 -- whose maxima 27/27/28 admit only this configuration --
     and the W = 27 route into 3K2.)

 (8) SHAPE 8 (3K2) AT W = 30, the equality analysis (section 9).  The
     four remaining configurations have census (2,1,0): sevens a, b,
     eight c.  Equality W = 30 = pair-sum forces deg u_i + deg v_i = 14
     on each shared 2-set, and the x = 1 patterns allow exactly
     {7,7} and {8,6}.  Two {a,b} pairs would coincide (ledger); so
     either ONE pair is {a,b} and c serves the other two, or c serves
     all three.
       SUBCASE A (S1 = {a,b}, S2 = {c,t2}, S3 = {c,t3}): edge f2
     contains c, its x = 1 pattern is {8}, so no degree-7 vertex is on
     f2 and S1 misses f2 entirely.  (CC4+)'s left side gives I_{f2} >=
     w(8) = 2, but localization caps I_{f2} by the pair-1 term (zero:
     a = 0) plus the pair-3 term (at most 1): 2 <= 1.  Dead.
       SUBCASE B (S_i = {c,t_i} all i): c is on all six pair edges,
     every pair edge's pattern is {8}, so the degree-7 vertex a is on
     NO pair edge and in no shared set.  Each of a's 7 edges has
     I >= w(7) = 1, hence meets M = {c,t1,t2,t3} (localization); two
     a-edges meeting M at the same cell share two cells (ledger); so
     7 = deg a <= |M| = 4.  Dead.

 (9) ASSEMBLY.  All eight shapes dead; the X = 3 layer of the window
     floor is EMPTY.  With certificate 0016 (X >= 3): X >= 4 FOR EVERY
     CRITICAL CORE AT m = 22.

MANDATORY HONESTY NOTES
-----------------------
 (1) PROVENANCE.  The theorem and the eight-case attack plan were
     PROPOSED BY AN OUTSIDE AUDIT (GPT 5.6 Sol Pro, 2026-07-28, reading
     the public repo at baed4d1) whose field numbers matched this lab's
     to the last digit.  Its proofs were NOT ingested: the audit
     arrived as a statement list with one-line mechanisms, and every
     proof in this certificate was derived in-house (desk + nine blind
     fleet lanes + five hostile refuters), then desk-re-derived.  Two
     honest scars from the process, recorded in NOTES.md: the desk
     first "corrected" the audit's path-shape bound 27 to 26 -- wrongly;
     three refuter lanes restored 27 by exhaustive enumeration.  And
     BOTH the audit's summarized equality route AND the desk's first
     write-up missed the all-(8,6) subcase (B above); the desk caught
     it in self-review and three refuter lanes caught it independently.
     An error that flatters the expected answer remains the worst kind.
 (2) THE FIELD SIDE SITS ON THE (D2) BOUNDARY AGAIN.  All five
     surviving configurations have D2 = 11 = floor(m/2) exactly
     (asserted in section 7).  Section 10 sweeps the cap: relax 0008's
     2*D2 <= 22 to 24 and the W <= 30 survivor list grows from 5 to 46.
     The equality analysis of section 9 was derived ONLY for the five;
     if 0008 is ever weakened, sections 7-9 must be redone before this
     certificate is re-quoted (same maintenance law as 0016, D-017).
 (3) WHERE THE KILL IS THIN, by shape: triangle and path close with
     ZERO units of W slack -- their maxima EQUAL the field floor 27,
     and the kill is the census clash of step (7), not the bound; the
     binding coordinate is the heavy census, not W.  3K2 closes at
     forced equality: subcase A by one unit (2 vs 1), subcase B by
     three (7 vs 4).  Shape 1 closes by two rungs of m, shape 2 by
     one, shape 3 by two units of the confinement injection (7 vs 5)
     and four of W.  Star closes by three units of W.
 (4) ENACTMENT SCOPE.  The finite exhaustions here are: the per-part
     agreement-pattern classifications behind the channel counts
     (sections 4-5), the slot-partition x degree-assignment maxima
     (section 8), the equality-split census (section 9), and the full
     field scan (section 7).  The STRUCTURAL steps -- localization,
     the confinement injection, the channel cap, the subcase kills --
     are proofs in this docstring whose finite content those
     exhaustions pin; the random-family enactments of section 3
     exercise the localization identity itself.  Nothing here claims
     an enactment it does not run.
 (5) WHAT THIS DOES NOT CLAIM.  Nothing about m >= 23 (the thin rungs
     m in {23..26} remain the window's arithmetic-free stretch).  No
     core is claimed to exist.  Lemma D9 (X = 3 forces Delta <= 8,
     window-wide) was proven by the fleet and desk-verified but is NOT
     consumed by this chain; it is banked in the turn-14 notebook.
     0017's corner-ladder profile forces X >= 4 from m = 28 (its
     margins row -- NOT its C5 coupling, which is the X <= 4 => m <= 28
     direction), so X = 3 lives only on m <= 27; this certificate
     empties m = 22, the one rung where X = 3 met a live field.

THE LEDGER, in full
-------------------
  the shape census            EXTERNAL -- NONE.  In-house -- the
                              X-identity (0015/0016 notation).
  shapes 1-3                  (CC4+) 0017 C1 + 0015 (2)-(3); covers
                              0013; corner 0017 C1; spent ledger.
                              (0015 Lemma 1.2: not consumed.)
  the field                   0005 (A)(B), 0009/0012 ladder, 0008 (D2).
  shapes 4-8                  additionally (C2) 0017 and the W-link
                              (0015 step (2) + Phi monotonicity).
  X >= 4                      all of the above + 0016's X >= 3.
  EXTERNAL INPUTS -- NONE.  The outside audit is attribution, not a
  dependency: no step cites it.
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
    NCHECK[0] += 1
    ok = bool(cond)
    if not ok:
        FAILED.append(label)
    print("  [%s] %2d. %s%s" % ("ok  " if ok else "FAIL", NCHECK[0], label,
                                ("   " + detail) if detail else ""),
          flush=True)


def note(label, detail=""):
    NNOTE[0] += 1
    print("  [note] %s%s" % (label, ("   " + detail) if detail else ""),
          flush=True)


def head(s):
    print("\n=== %s ===" % s, flush=True)


def phi(n, k):
    """Balanced-split minimum of sum C(n_j, 2) over k classes totalling n."""
    if n <= 0:
        return 0
    q, r = divmod(n, k)
    return r * comb(q + 1, 2) + (k - r) * comb(q, 2)


def w(d):
    """The cover-free per-vertex weight Phi(d-1, 5)."""
    return phi(d - 1, 5)


# ==========================================================================
# 1.  Budgets: the per-edge heavy-degree patterns at X = 3
# ==========================================================================

head("1.  the (CC4+) budgets at X = 3, exhaustively")

check("the w-table this certificate spends: w(d) = 0 for d <= 6, w(7) = 1, "
      "w(8) = 2, w(9) = 3, w(10) = 4 -- derived from Phi, never tabulated "
      "by hand (the 0017 lesson)",
      [w(d) for d in range(2, 11)] == [0, 0, 0, 0, 0, 1, 2, 3, 4])
check("Phi is nonincreasing in the class count for all n <= 10, "
      "1 <= k <= k' <= 6 -- the relaxation Phi(d-1, 5-b) >= Phi(d-1, 5) "
      "= w(d) that every budget and every I_e >= w(deg v) step below uses",
      all(phi(n, k) >= phi(n, kk)
          for n in range(11) for k in range(1, 7) for kk in range(k, 7)))

PATTERNS = {}
for xe in (0, 1, 2, 3):
    pats = set()
    for ms in itertools.combinations_with_replacement(range(2, 10), 6):
        if sum(w(d) for d in ms) <= 3 - xe:
            pats.add(tuple(sorted((d for d in ms if d >= 7), reverse=True)))
    PATTERNS[xe] = sorted(pats)
check("EXHAUSTIVE over degree 6-multisets in 2..9: the X = 3 budget "
      "sum_{v in e} w(deg v) <= 3 - x_e admits heavy patterns "
      "{} at x_e = 3; {}, {7} at x_e = 2; {}, {7}, {7,7}, {8} at x_e = 1; "
      "and adds {7,7,7}, {8,7}, {9} at x_e = 0 -- COMPLETE lists",
      PATTERNS[3] == [()]
      and PATTERNS[2] == [(), (7,)]
      and PATTERNS[1] == [(), (7,), (7, 7), (8,)]
      and PATTERNS[0] == [(), (7,), (7, 7), (7, 7, 7), (8,), (8, 7), (9,)])
check("degree 9 appears in NO pattern with x_e >= 1 -- the fact that bars "
      "the (0,0,1) configuration's degree-9 vertex from every excess edge "
      "in sections 6-9 -- and degree 8 in none with x_e >= 2",
      all(9 not in p for xe in (1, 2, 3) for p in PATTERNS[xe])
      and all(8 not in p for xe in (2, 3) for p in PATTERNS[xe]))
note("STATED, NOT TESTED: (CC4+) itself -- sum_i Phi(d_i-1, 5-b_i) <= "
     "I_e <= X - x_e for every edge of a critical core with X <= 4 -- is "
     "certificate 0017's C1 on 0015's steps (2)-(3); the b_i = 5 branch "
     "is closed by covering (0015 step (1): five cover cells in one part "
     "force d_i = 1).  This certificate consumes it, it does not re-prove "
     "it; the budget lists above are its arithmetic shadow at X = 3")

# ==========================================================================
# 2.  The shape census: eight shapes, complete
# ==========================================================================

head("2.  the eight shapes of X = 3")

parts3 = []


def partsof(n, mx, cur):
    if n == 0:
        parts3.append(tuple(cur))
        return
    for p in range(min(n, mx), 0, -1):
        partsof(n - p, p, cur + [p])


partsof(3, 3, [])
check("the pair-excess multiset partitions 3: exactly (3), (2,1), (1,1,1) "
      "-- a lambda-4 pair, a lambda-3 + a lambda-2 pair, or three "
      "lambda-2 pairs (X = sum over pairs of (lambda - 1), all terms "
      ">= 0)",
      parts3 == [(3,), (2, 1), (1, 1, 1)])

# (2,1): the two pairs share an edge or not -- 2 shapes, by |{f,g} cap {h,k}|
note("STATED, NOT TESTED (it is a triviality, and the phase-3 spec audit "
     "correctly demoted it from a check): a lambda-3 pair and a lambda-2 "
     "pair either share exactly one edge (adjacent) or none (disjoint) -- "
     "sharing both would make them the same pair with two different "
     "lambdas.  2 shapes")

# (1,1,1): classify ALL 3-subsets of edges of K6 by isomorphism type
SHAPES_FOUND = {}
EDGES6 = list(itertools.combinations(range(6), 2))
for trip in itertools.combinations(EDGES6, 3):
    verts = sorted(set(v for e in trip for v in e))
    deg = {}
    for e in trip:
        for v in e:
            deg[v] = deg.get(v, 0) + 1
    key = (len(verts), tuple(sorted(deg.values())))
    SHAPES_FOUND[key] = SHAPES_FOUND.get(key, 0) + 1
check("EXHAUSTIVE over all C(15,3) = 455 sets of three distinct pairs on "
      "six labeled edges: exactly FIVE isomorphism types occur -- "
      "triangle (3 vertices, degrees 2,2,2), star K1,3 (4; 1,1,1,3), "
      "path P4 (4; 1,1,2,2), P3+K2 (5; 1,1,1,1,2), 3K2 (6; all 1) -- "
      "so 1 + 2 + 5 = 8 shapes and the census is complete",
      sorted(SHAPES_FOUND.keys()) == [(3, (2, 2, 2)), (4, (1, 1, 1, 3)),
                                      (4, (1, 1, 2, 2)),
                                      (5, (1, 1, 1, 1, 2)),
                                      (6, (1, 1, 1, 1, 1, 1))]
      and sum(SHAPES_FOUND.values()) == 455)
note("STATED, NOT TESTED: two distinct unordered pairs cannot consist of "
     "the same two edges, and a 'pair' of one edge with itself is no "
     "pair; the pair-graph of three distinct lambda-2 pairs is therefore "
     "a simple 3-edge graph, which the enumeration above exhausts.  "
     "EVERY pair outside a shape's ledger has lambda = 1 exactly: one "
     "more lambda >= 2 pair adds >= 1 to X = 3 -- the spent ledger that "
     "every kill below invokes")

# ==========================================================================
# 3.  Localization of I_e, enacted
# ==========================================================================

head("3.  only excessive pairs feed I_e -- the localization, enacted")


class LCG(object):
    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFF

    def next(self):
        self.s = (25214903917 * self.s + 11) & 0xFFFFFFFFFFFF
        return self.s >> 16

    def below(self, k):
        return self.next() % k


RNG = LCG(20260728)


def lam(e, f):
    return sum(1 for i in range(6) if e[i] == f[i])


t0 = time.time()
fams = 0
enacts = 0
loc_bad = 0
split_bad = 0
cap_n = 0
cap_bad = 0
nz_loc = 0
for trial in range(20000):
    nv = 2 + RNG.below(3)
    target = 4 + RNG.below(6)
    F = []
    for _ in range(300):
        if len(F) >= target:
            break
        c = tuple(RNG.below(nv) for _ in range(6))
        if c in F:
            continue
        if all(lam(c, f) >= 1 for f in F):
            F.append(c)
    m = len(F)
    if m < 4:
        continue
    fams += 1
    X = sum(lam(p, q) - 1 for p, q in itertools.combinations(F, 2))
    cells = sorted(set((i, f[i]) for f in F for i in range(6)))
    for k in range(m):
        e = F[k]
        pool = [c for c in cells if e[c[0]] != c[1]]
        if len(pool) < 5:
            continue
        T = []
        pl = list(pool)
        for _ in range(5):
            T.append(pl.pop(RNG.below(len(pl))))
        T = set(T)
        others = [f for j, f in enumerate(F) if j != k]
        total = 0
        loc = 0
        for f, g in itertools.combinations(others, 2):
            a = sum(1 for i in range(6) if f[i] == g[i] == e[i])
            b = sum(1 for i in range(6) if f[i] == g[i]
                    and (i, f[i]) in T)
            total += a * b
            L = lam(f, g)
            if a + b > L:
                split_bad += 1
            if L >= 2:
                loc += a * b
                if X <= 4:
                    cap_n += 1
                    if a * b > L - 1:
                        cap_bad += 1
            elif a * b != 0:
                loc_bad += 1
        enacts += 1
        if total != loc:
            loc_bad += 1
        if total > 0:
            nz_loc += 1
check("LOCALIZATION, enacted: all 20,000 LCG trials (house seed "
      "20260728) reach m >= 4; 129,005 (edge, arbitrary disjoint 5-set) "
      "enactments: the lambda-1 pairs contribute ZERO to I_e every "
      "single time (their one shared cell cannot lie in both e and "
      "T_e), so I_e = sum over EXCESSIVE pairs only -- and 120,876 "
      "enactments have I_e > 0, so the identity is exercised "
      "nonvacuously",
      fams == 20000 and enacts == 129005 and loc_bad == 0
      and nz_loc == 120876,
      "%.1fs" % (time.time() - t0))
check("the split fact a + b <= lambda held on every pair of every "
      "enactment (unconditional: e and T_e are disjoint, so a and b "
      "count disjoint parts of f cap g); and on the systems with "
      "X <= 4 -- where 0017 C1's corner is certified -- the per-pair "
      "cap a*b <= lambda - 1 held on all 4,442 excessive-pair terms.  "
      "The cap is NOT asserted for X >= 5 systems (0017's X = 5 "
      "witness broke exactly it); this certificate only ever spends it "
      "at X = 3",
      split_bad == 0 and cap_n == 4442 and cap_bad == 0)
note("STATED, NOT TESTED: for a lambda-2 pair the localization term is "
     "0 or 1 -- a + b <= 2 splits as 1 + 1 or worse.  For the shapes "
     "below this makes I_e <= (number of ledger pairs whose shared set "
     "meets e, excluding e's own pairs), the cap that kills 3K2's "
     "subcase A in section 9")

# ==========================================================================
# 4.  Shape 1 -- the lambda-4 pair: m <= 20
# ==========================================================================

head("4.  shape 1, the lambda-4 pair: m <= 20")

# f,g agree on parts 0-3 (shared cells), differ on parts 4-5.
# A third edge's per-part relation: parts 0-3: agrees with the shared
# cell or not (2); parts 4-5: f's cell, g's cell, or neither (3).
CLS = {"shared": set(), "chanA": 0, "chanB": 0}
bad1 = 0
for pat in itertools.product((0, 1), (0, 1), (0, 1), (0, 1),
                             (0, 1, 2), (0, 1, 2)):
    lef = sum(1 for i in range(4) if pat[i] == 1) \
        + sum(1 for i in (4, 5) if pat[i] == 0)
    leg = sum(1 for i in range(4) if pat[i] == 1) \
        + sum(1 for i in (4, 5) if pat[i] == 1)
    if lef != 1 or leg != 1:
        continue
    sh = [i for i in range(4) if pat[i] == 1]
    if len(sh) == 1 and pat[4] == 2 and pat[5] == 2:
        CLS["shared"].add(sh[0])
    elif not sh and pat[4] == 0 and pat[5] == 1:
        CLS["chanA"] += 1
    elif not sh and pat[4] == 1 and pat[5] == 0:
        CLS["chanB"] += 1
    else:
        bad1 += 1
check("EXHAUSTIVE over all 2^4 * 3^2 = 144 per-part relations of a third "
      "edge to a lambda-4 pair: the intersecting relations with "
      "lambda(e,f) = lambda(e,g) = 1 are EXACTLY: through one of the 4 "
      "shared cells (4 relations), or channel A = (f's part-5 cell, g's "
      "part-6 cell), or channel B = (g's part-5, f's part-6) -- 6 in "
      "all, nothing else.  The branch dichotomy of the count is "
      "complete and disjoint",
      CLS["shared"] == {0, 1, 2, 3} and CLS["chanA"] == 1
      and CLS["chanB"] == 1 and bad1 == 0)
check("the count: through-shared edges number sum_{u in S}(deg u - 2) "
      "<= 4*(6-2) = 16, because x_f = 3 gives f the pattern {} of "
      "section 1 -- every shared degree <= 6; each channel holds at "
      "most ONE edge (two would share both channel cells: a second "
      "excessive pair on a spent ledger).  So m - 2 <= 16 + 2 = 18, "
      "m <= 20 < 22.  SHAPE 1 IS DEAD, two rungs below the floor",
      4 * (6 - 2) + 2 == 18 and 18 + 2 == 20 and 20 < 22)
note("STATED, NOT TESTED (structural, pinned by the 144-relation "
     "exhaustion): an edge through a shared cell meets BOTH f and g "
     "there, so it can touch no other cell of either -- and an edge "
     "through two shared cells would have lambda(e,f) >= 2.  Both are "
     "instances of the spent ledger")

# ==========================================================================
# 5.  Shape 2 -- lambda-3 + adjacent lambda-2: m <= 21
# ==========================================================================

head("5.  shape 2, lambda-3 + adjacent lambda-2: m <= 21")

CLS2 = {"shared": set(), "cross": set()}
bad2 = 0
for pat in itertools.product((0, 1), (0, 1), (0, 1),
                             (0, 1, 2), (0, 1, 2), (0, 1, 2)):
    lef = sum(1 for i in range(3) if pat[i] == 1) \
        + sum(1 for i in (3, 4, 5) if pat[i] == 0)
    leg = sum(1 for i in range(3) if pat[i] == 1) \
        + sum(1 for i in (3, 4, 5) if pat[i] == 1)
    if lef != 1 or leg != 1:
        continue
    sh = [i for i in range(3) if pat[i] == 1]
    fpriv = [i for i in (3, 4, 5) if pat[i] == 0]
    gpriv = [i for i in (3, 4, 5) if pat[i] == 1]
    if len(sh) == 1 and not fpriv and not gpriv:
        CLS2["shared"].add(sh[0])
    elif not sh and len(fpriv) == 1 and len(gpriv) == 1 \
            and fpriv[0] != gpriv[0]:
        CLS2["cross"].add((fpriv[0], gpriv[0]))
    else:
        bad2 += 1
check("EXHAUSTIVE over all 2^3 * 3^3 = 216 per-part relations of a third "
      "edge to a lambda-3 pair: lambda(e,f) = lambda(e,g) = 1 happens "
      "EXACTLY through one of the 3 shared cells or through one of the "
      "6 cross channels (f-private cell in one differing part, g-private "
      "in another) -- 9 relations, nothing else",
      CLS2["shared"] == {0, 1, 2} and len(CLS2["cross"]) == 6
      and bad2 == 0)
check("shape 2's count: A = f cap g has all degrees <= 6 (x_f = 3, "
      "pattern {}), so through-A edges other than {f,g,h} number at "
      "most 3*(6-2) = 12; each of the 6 channels holds at most one "
      "edge -- a doubled channel is a THIRD excessive pair and the "
      "(2,1) ledger has none spare.  h meets f twice and is neither.  "
      "m - 3 <= 12 + 6 = 18, m <= 21 < 22.  SHAPE 2 IS DEAD",
      3 * (6 - 2) + 6 == 18 and 18 + 3 == 21 and 21 < 22)
check("the corner spends here: |f cap g cap h| >= 2 with s = "
      "lambda(f,g) = 3 would force X >= 2(2-1) + (3-1) = 4 > 3 (0017 "
      "C1), so h occupies at most one A-slot -- the count above never "
      "relied on where h sits, only that it is excluded",
      2 * (2 - 1) + (3 - 1) == 4)
note("STATED, NOT TESTED (fleet-proven, desk-verified, NOT consumed): "
     "a blind derivation lane proved the stronger m-free lemma that "
     "shape 2 forces Delta <= 6 outright -- heavy vertices' edges "
     "inject into the <= 5 cells of (f cap g) u (f cap h) -- and then "
     "dies by pure counting (max sum C(deg,2) = 226 < 234 at m = 22 "
     "under (A), (B), (D2)).  Banked in the turn-14 notebook; the "
     "channel count above is the consumed kill")

# ==========================================================================
# 6.  Shape 3 -- lambda-3 + disjoint lambda-2: heavy confinement, W <= 23
# ==========================================================================

head("6.  shape 3, lambda-3 + disjoint lambda-2: W <= 23 < 27")

check("HEAVY CONFINEMENT, the arithmetic: a heavy vertex z (deg >= 7) "
      "outside U cup V would need every one of its >= 7 edges to meet "
      "U cup V at pairwise DISTINCT cells (each edge has I_e >= "
      "w(deg z) >= 1 by (CC4+)'s left side; localization sends it "
      "through U cup V; a repeated cell is a spent-ledger pair whose "
      "membership would put z itself in U or V).  |U cup V| = 3 + 2 = "
      "5 < 7.  So every heavy vertex lies in U cup V",
      3 + 2 == 5 and 5 < 7)
best3 = 0
for uheavy in PATTERNS[2]:
    for vheavy in PATTERNS[1]:
        # no size guard needed: PATTERNS[2] lists hold <= 1 heavy entry
        # and PATTERNS[1] <= 2, within |U| = 3 and |V| = 2 (the phase-3
        # sabotage audit found the earlier guard could never fire)
        Wv = sum(d * w(d) for d in uheavy) + sum(d * w(d) for d in vheavy)
        if Wv > best3:
            best3 = Wv
check("the census caps, exhausted over the certified patterns: U's "
      "heavies fit x = 2's lists ({} or {7}: at most one 7, nothing "
      "bigger), V's fit x = 1's ({}, {7}, {7,7}, {8}).  Max W = "
      "7 + 16 = 23 (a 7 in U, an 8 in V) -- and 23 < 27, the field "
      "floor of section 7.  SHAPE 3 IS DEAD",
      best3 == 23 and 23 < 27)
note("STATED, NOT TESTED: U lies on f (x_f = 2) so its heavy content is "
     "capped by f's pattern; V lies on h (x_h = 1) likewise.  A "
     "second, independent desk kill by channel counting (m <= 22 with "
     "forced equality, then a1's six-edge pencil defeats the 5-cell "
     "cover T_f) survived hostile refutation and is recorded in the "
     "turn-14 notebook -- two kills, one consumed")

# ==========================================================================
# 7.  The field at m = 22, X = 3
# ==========================================================================

head("7.  the field: the X = 3 layer and its five W <= 30 survivors")

LADDER = {1: 2, 2: 4, 3: 6, 4: 9, 5: 13}
M = 22
TARGET = comb(M, 2)
CAPS = {k: M - LADDER[6 - k] for k in range(1, 6)}


def profiles():
    out = []

    def rec(left, mx, cur):
        if left == 0:
            if len(cur) >= 6:
                out.append(tuple(cur))
            return
        k = len(cur)
        for p in range(min(left, mx), 1, -1):
            if left - p == 1:
                continue
            if k < 5 and sum(cur) + p > CAPS[k + 1]:
                continue
            rec(left - p, p, cur + [p])
    rec(M, M - LADDER[5], [])
    return out


P22 = sorted(profiles(), key=lambda p: sum(comb(d, 2) for d in p))
SC = [sum(comb(d, 2) for d in p) for p in P22]
PW = [sum(d * w(d) for d in p) for p in P22]
PD2 = [sum(1 for d in p if d == 2) for p in P22]
P789 = [(sum(1 for d in p if d == 7), sum(1 for d in p if d == 8),
         sum(1 for d in p if d == 9)) for p in P22]
check("the pinned-ladder profile list at m = 22 has 67 members (entries "
      ">= 2 by 0005 (A), >= 6 entries by 0005 (B), prefix caps from the "
      "ladder 0009/0012) -- built here by an independent generator, "
      "same field as 0015/0016",
      len(P22) == 67)

t0 = time.time()
layers = {0: 0, 1: 0, 2: 0, 3: 0}
X3 = []
stack = []


def dfs(start, k, tot):
    if k == 6:
        x = tot - TARGET
        if 0 <= x <= 3:
            layers[x] += 1
            if x == 3:
                X3.append(tuple(stack))
        return
    rem = 6 - k
    for i in range(start, len(P22)):
        t2 = tot + SC[i]
        if t2 + (rem - 1) * SC[i] > TARGET + 3:
            break
        if t2 + (rem - 1) * SC[-1] < TARGET:
            continue
        stack.append(i)
        dfs(i, k + 1, t2)
        stack.pop()


dfs(0, 0, 0)
check("the layer counts: X = 0: 267,965 · X = 1: 238,239 · X = 2: "
      "210,713 · X = 3: 186,086 (total 903,003) -- the first three "
      "reproduce 0015/0016's certified numbers, the fourth is this "
      "certificate's layer",
      [layers[x] for x in range(4)] == [267965, 238239, 210713, 186086],
      "%.1fs" % (time.time() - t0))

D2P = [c for c in X3 if 2 * sum(PD2[i] for i in c) <= M]
WOF = {}
for c in D2P:
    WOF[c] = sum(PW[i] for i in c)
check("the (D2) cap of 0008 leaves 15,451 of the 186,086; their minimum "
      "W is 27 -- so ANY shape whose pair-sum bound is below 27 is dead "
      "outright, the fact sections 6 and 8 spend",
      len(D2P) == 15451 and min(WOF.values()) == 27)

SURV = sorted((c for c in D2P if WOF[c] <= 30), key=lambda c: WOF[c])
cens = []
for c in SURV:
    n7 = sum(P789[i][0] for i in c)
    n8 = sum(P789[i][1] for i in c)
    n9 = sum(P789[i][2] for i in c)
    d2 = sum(PD2[i] for i in c)
    cens.append((WOF[c], (n7, n8, n9), d2))
    print("      W=%d census=%s D2=%d: %s"
          % (WOF[c], (n7, n8, n9), d2,
             ", ".join(str(P22[i]) for i in c)), flush=True)
check("W <= 24: NONE.  W <= 30: exactly FIVE configurations, printed "
      "above -- ONE at W = 27 with heavy census (0,0,1) (a single "
      "degree-9 vertex), FOUR at W = 30 with census (2,1,0) (two "
      "sevens, one eight) -- and EVERY one sits ON the (D2) boundary "
      "at D2 = 11.  W <= 28 admits only the first",
      sum(1 for c in D2P if WOF[c] <= 24) == 0
      and len(SURV) == 5
      and cens[0] == (27, (0, 0, 1), 11)
      and all(cn == (30, (2, 1, 0), 11) for cn in cens[1:])
      and sum(1 for c in D2P if WOF[c] <= 28) == 1)
check("consistency with the banked turn-13 census: the shape-blind "
      "W <= 48 relaxation leaves 1,580 configurations -- the number "
      "the turn-13 notebook recorded and the outside audit reproduced",
      sum(1 for c in D2P if WOF[c] <= 48) == 1580)

# ==========================================================================
# 8.  Shapes 4-8: the pair-sum maxima, exhaustively
# ==========================================================================

head("8.  the five (1,1,1) shapes: maxima 24 / 27 / 27 / 28 / 30")

# Shapes as pair lists over abstract edge names.
SHAPES5 = {
    "star": [("f", "g"), ("f", "h"), ("f", "k")],
    "triangle": [("f", "g"), ("g", "h"), ("f", "h")],
    "path": [("f", "g"), ("g", "h"), ("h", "k")],
    "p3k2": [("f", "g"), ("g", "h"), ("k", "l")],
    "3k2": [("f1", "g1"), ("f2", "g2"), ("f3", "g3")],
}
BOUND = {"star": 24, "triangle": 27, "path": 27, "p3k2": 28, "3k2": 30}


def setparts(items):
    """All set partitions of a list (Bell recursion, deterministic)."""
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in setparts(rest):
        for i in range(len(part)):
            yield part[:i] + [[first] + part[i]] + part[i + 1:]
        yield [[first]] + part


def shape_max(pairs, allow78=True, ledger=True):
    """Exhaustive max of the pair-sum RHS over identification patterns
    (set partitions of the six shared slots) and degree assignments
    2..9 under the per-edge budgets.  ledger=True applies the two
    spent-ledger legality filters (closure; unlisted edge-pairs share
    <= 1 vertex); ledger=False maximizes over the unconditional
    superset -- the robustness run the phase-3 audit asked for.  The
    same-pair-slots-distinct rule is definitional (a shared 2-set has
    two distinct vertices) and always applies.  Returns
    (max, every-maximizer-has-a-7-or-8-flag)."""
    edges = sorted(set(e for pr in pairs for e in pr))
    xe = {e: sum(1 for pr in pairs if e in pr) for e in edges}
    slots = [(i, s) for i in range(3) for s in (0, 1)]
    best = -1
    max_needs_heavy = True
    for part in setparts(slots):
        ok = True
        hosts = []
        for block in part:
            pidx = [sl[0] for sl in block]
            if len(pidx) != len(set(pidx)):
                ok = False      # two slots of one pair identified
                break
            hedges = set(e for i in pidx for e in pairs[i])
            # closure: on both edges of an unrepresented pair
            if ledger:
                for j in range(3):
                    if j not in pidx and set(pairs[j]) <= hedges:
                        ok = False
                        break
            if not ok:
                break
            hosts.append((set(pidx), hedges))
        if not ok:
            continue
        # unlisted edge-pairs share at most one vertex
        if ledger:
            listed = set(frozenset(pr) for pr in pairs)
            for a, b in itertools.combinations(edges, 2):
                if frozenset((a, b)) in listed:
                    continue
                if sum(1 for _, he in hosts if a in he and b in he) > 1:
                    ok = False
                    break
            if not ok:
                continue
        degsets = [range(2, 10)] * len(hosts)
        for degs in itertools.product(*degsets):
            if not allow78 and any(d in (7, 8) for d in degs):
                continue
            # (the explicit degree-9 bar for x_e >= 1 hosts is subsumed
            # by the budget filter below -- w(9) = 3 > 3 - x_e -- and
            # was removed after the phase-3 sabotage audit proved it
            # dead code; the budget is the operative mechanism)
            good = True
            for e in edges:
                if sum(w(d) for d, (_, he) in zip(degs, hosts)
                       if e in he) > 3 - xe[e]:
                    good = False
                    break
            if not good:
                continue
            val = sum((degs[bi] - 2)
                      for bi, (pidx, _) in enumerate(hosts)
                      for _ in pidx)
            if val > best:
                best = val
                max_needs_heavy = any(d >= 7 for d in degs)
            elif val == best and not any(d >= 7 for d in degs):
                max_needs_heavy = False
    return best, max_needs_heavy


t0 = time.time()
maxima = {}
needs7 = {}
for name, pairs in SHAPES5.items():
    maxima[name], needs7[name] = shape_max(pairs)
check("EXHAUSTIVE over all identification patterns of the six shared "
      "slots (set partitions, filtered by the spent ledger: same-pair "
      "slots distinct; a vertex on both edges of a pair belongs to its "
      "shared set; unlisted edge-pairs share <= 1 vertex) and ALL "
      "degree assignments 2..9 under the section-1 budgets: the "
      "pair-sum maxima are star 24, triangle 27, PATH 27, P3+K2 28, "
      "3K2 30.  With W <= sum_e I_e and (C2), these bound W per shape",
      maxima == BOUND, "%.1fs" % (time.time() - t0))
check("STAR IS DEAD OUTRIGHT: 24 < 27, the field floor.  And the desk's "
      "history is pinned as a tooth: the path maximum is 27, NOT 26 -- "
      "the desk's first pass missed the triple identification (one "
      "degree-7 vertex serving all three shared sets, legal since "
      "every unlisted edge-pair still meets only at it) and three "
      "hostile refuter lanes restored 27 by this same exhaustion.  The "
      "outside audit had quoted 27 correctly all along",
      maxima["star"] == 24 and 24 < 27 and maxima["path"] == 27)
check("EVERY maximizer of triangle, path and P3+K2 needs a degree >= 7 "
      "vertex in a shared set (asserted by the enumeration).  "
      "CORROBORATIVE, NOT LOAD-BEARING: the phase-3 sabotage audit "
      "showed this flag is falsifiable only toward False, and the "
      "(0,0,1) kill below is carried by the light run, which has "
      "independent teeth (its 7/8 filter reddens the cert when dropped)",
      needs7["triangle"] and needs7["path"] and needs7["p3k2"]
      and not needs7["star"])

t0 = time.time()
light = {}
for name, pairs in SHAPES5.items():
    light[name], _ = shape_max(pairs, allow78=False)
check("THE (0,0,1) CONFIGURATION DIES FOR EVERY SHAPE: with no degree-7 "
      "or -8 vertex anywhere and degree 9 excluded from every shared "
      "slot by the budgets themselves (w(9) = 3 > 3 - x_e on every "
      "pair edge), every shared vertex has degree <= 6 and the same "
      "exhaustion caps the pair-sum at 24 for ALL FIVE shapes -- but "
      "the configuration's W is 27 > 24.  Triangle, path and P3+K2 "
      "(maxima 27/27/28, which admit ONLY this configuration among the "
      "five survivors) are DEAD; 3K2's W = 27 route is DEAD",
      all(v == 24 for v in light.values()),
      "%.1fs" % (time.time() - t0))

t0 = time.time()
loose = {}
for name, pairs in SHAPES5.items():
    loose[name], _ = shape_max(pairs, ledger=True)
    loose[name + "/noledger"], _ = shape_max(pairs, ledger=False)
check("ROBUSTNESS, the phase-3 audit's ask enacted: re-run the whole "
      "exhaustion with BOTH spent-ledger legality filters DISABLED -- "
      "the unconditionally sound superset -- and every maximum is "
      "UNCHANGED (24/27/27/28/30).  The per-edge budgets alone pin the "
      "maxima; the ledger filters narrow the search space but the "
      "bounds do not depend on their correctness.  The fatal direction "
      "(a filter wrongly excluding a real core and shrinking a maximum) "
      "is closed unconditionally",
      all(loose[n] == loose[n + "/noledger"] == BOUND[n]
          for n in SHAPES5),
      "%.1fs" % (time.time() - t0))

# ==========================================================================
# 9.  3K2 at W = 30: the equality analysis
# ==========================================================================

head("9.  3K2 on the four W = 30 configurations: forced equality, dead "
     "twice")

splits = set()
maxpair = 0
for d1, d2 in itertools.combinations_with_replacement(range(2, 10), 2):
    heavy = tuple(sorted((d for d in (d1, d2) if d >= 7), reverse=True))
    if heavy in PATTERNS[1]:
        if d1 + d2 > maxpair:
            maxpair = d1 + d2
        if d1 + d2 == 14:
            splits.add(tuple(sorted((d1, d2), reverse=True)))
check("the per-pair premise, ENACTED (the spec audit found it implied "
      "but untested): over ALL pattern-legal degree pairs on an x = 1 "
      "edge the maximum of deg u + deg v is EXACTLY 14, so each pair "
      "contributes at most 10 to the pair-sum and equality W = 30 "
      "forces every shared 2-set to sum to 14; the sum-14 splits the "
      "patterns admit are EXACTLY {7,7} and {8,6} -- (9,5) and "
      "everything else is pattern-barred",
      maxpair == 14 and splits == {(7, 7), (8, 6)})
ASGS = list(itertools.combinations_with_replacement(sorted(splits), 3))
LEGAL = [a for a in ASGS if a.count((7, 7)) <= 1]
check("census (2,1,0) bookkeeping: of the 4 ways to assign the two "
      "splits to three pairs, exactly 2 survive 'at most ONE pair is "
      "{7,7}' (two {7,7} pairs would put the same two sevens in two "
      "shared sets -- their four edges would pairwise share both, a "
      "spent-ledger violation) -- and they are exactly SUBCASE A (one "
      "{7,7}, so c, the single eight, is in the other two shared sets) "
      "and SUBCASE B (no {7,7}, c in all three).  The dichotomy is "
      "exhaustive",
      len(ASGS) == 4 and len(LEGAL) == 2
      and sorted(a.count((7, 7)) for a in LEGAL) == [0, 1])
check("SUBCASE A DIES BY ONE UNIT: f2 contains c (degree 8), its x = 1 "
      "pattern is {8} -- no degree-7 vertex on f2 -- so the {7,7} "
      "shared set misses f2 entirely and localization (section 3) caps "
      "I_{f2} <= 0 + 1 = 1 (its own pair excluded, the {a,b} term has "
      "a = 0, the other c-pair term is <= 1).  But (CC4+)'s left side "
      "demands I_{f2} >= w(8) = 2.  2 <= 1 is false",
      w(8) == 2 and 2 > 1)
check("SUBCASE B DIES BY THREE: c on all six pair edges makes every "
      "pair edge's pattern {8}, so the degree-7 vertex a sits on no "
      "pair edge and in no shared set; each of its 7 edges has I >= "
      "w(7) = 1, hence meets M = {c, t1, t2, t3} (localization), at "
      "pairwise distinct cells (a repeat is a spent-ledger pair).  "
      "7 = deg a <= |M| = 4 is false",
      w(7) == 1 and 7 > 4)
note("STATED, NOT TESTED (structural steps of section 9, proven in the "
     "docstring and by two independent fleet lanes): c cannot sit on a "
     "{7,7}-pair's edges (its w = 2 would exceed their remaining "
     "budget); t_i != t_j for i != j (equal sixes would give two pair "
     "edges a second shared vertex); and in subcase B the two extra "
     "c-edges beyond the six pair edges are the only other c-incidences "
     "(deg c = 8).  Each is a one-line spent-ledger or budget argument")

# ==========================================================================
# 10.  Assembly, controls, and the margins
# ==========================================================================

head("10.  assembly, controls, margins")

check("ASSEMBLY, as a conjunction of this run's own results (the spec "
      "audit demoted the prose form): shapes 1 and 2 die by edge counts "
      "(m <= 20, 21 < 22, on the exhausted 144/216 relation spaces); "
      "shape 3 by confinement (W <= 23 < 27); star by its bound "
      "(24 < 27); triangle, path, P3+K2 and 3K2's W = 27 route by the "
      "(0,0,1) census kill (light maxima 24 < 27); 3K2's four W = 30 "
      "configurations by the equality dichotomy over {7,7}/{8,6}.  "
      "Eight of eight shapes dead: NO CRITICAL CORE AT m = 22 HAS "
      "X = 3.  With certificate 0016's X >= 3: X >= 4 FOR EVERY "
      "CRITICAL CORE AT m = 22",
      CLS["shared"] == {0, 1, 2, 3} and CLS["chanA"] == 1
      and CLS["chanB"] == 1
      and CLS2["shared"] == {0, 1, 2} and len(CLS2["cross"]) == 6
      and best3 == 23 and maxima == BOUND
      and all(v == 24 for v in light.values())
      and min(WOF.values()) == 27 and len(SURV) == 5
      and maxpair == 14 and splits == {(7, 7), (8, 6)}
      and len(LEGAL) == 2)

alive4 = 0
t0 = time.time()
lay4 = 0
stack4 = []


def dfs4(start, k, tot):
    global lay4, alive4
    if k == 6:
        if tot - TARGET == 4:
            lay4 += 1
            d2 = sum(PD2[i] for i in stack4)
            ww = sum(PW[i] for i in stack4)
            if 2 * d2 <= M and ww <= 80:
                alive4 += 1
        return
    rem = 6 - k
    for i in range(start, len(P22)):
        t2 = tot + SC[i]
        if t2 + (rem - 1) * SC[i] > TARGET + 4:
            break
        if t2 + (rem - 1) * SC[-1] < TARGET:
            continue
        stack4.append(i)
        dfs4(i, k + 1, t2)
        stack4.pop()


dfs4(0, 0, 0)
check("NOT TOO STRONG: the X = 4 layer holds 163,682 configurations and "
      "the tools available there -- (D2) plus the shape-blind global "
      "cap W <= (m-2)X = 80 -- leave 12,171 ALIVE.  This certificate "
      "stops exactly where its evidence stops: the X = 4 frontier is "
      "real and open",
      lay4 == 163682 and alive4 == 12171 and alive4 > 0,
      "%.1fs" % (time.time() - t0))

relax = sorted(c for c in X3
               if 2 * sum(PD2[i] for i in c) <= 24
               and sum(PW[i] for i in c) <= 30)
check("THE MARGIN IS IN THE (D2) COORDINATE ONCE MORE (D-035): relax "
      "0008's cap by one degree-2 vertex (2*D2 <= 24) and the W <= 30 "
      "survivor list grows from 5 to 46.  The equality analysis of "
      "section 9 covered the five; if (D2) is ever weakened, sections "
      "7-9 must be redone before this certificate is re-quoted",
      len(relax) == 46 and len(SURV) == 5)
check("the W-coordinate margins, stated so the thin ones are visible: "
      "star closes by 3 units (24 vs 27); shape 3 by 4 (23 vs 27); "
      "triangle and path close by ZERO units of W -- their maxima "
      "EQUAL the floor 27, and the kill is the (0,0,1) census clash, "
      "whose binding fact is 'every maximizer needs a heavy shared "
      "vertex' (checked in section 8), not the bound itself.  3K2's "
      "subcase A closes by one unit (2 vs 1), subcase B by three "
      "(7 vs 4); shapes 1 and 2 close by two rungs and one rung of m",
      maxima["triangle"] == 27 and maxima["path"] == 27
      and 27 - 27 == 0 and best3 == 23)
note("RUNG-DOWN CONSISTENCY: the X <= 2 layer counts above match "
     "certificate 0016's (267,965 / 238,239 / 210,713) -- re-measured "
     "here by an independent generator, a control not a re-proof.  "
     "0016 remains the authority for X <= 2")
note("STATED, NOT TESTED: Lemma D9 -- X = 3 forces Delta <= 8 at any "
     "m > 9, by the same localization pigeonhole (a degree-9 vertex "
     "forces x_e = 0 and I_e = 3 on all nine of its edges; each needs "
     "a shared set meeting it; the ledger's shared cells number at "
     "most 4 < 9... and an edge avoiding v can meet the nine at only "
     "6 cells) -- fleet-proven twice, desk-verified, NOT consumed "
     "above.  Banked in the turn-14 notebook with the fleet's full "
     "degree-descent alternative proof of this whole theorem")

# ==========================================================================

head("Result")

print("""
  X >= 4 FOR EVERY CRITICAL CORE AT m = 22            PROVEN-BY-CERTIFICATE
        (field 0005/0009/0012; (D2) 0008; covers 0013; 0015 (2)-(3);
         0016 (T) + X >= 3; 0017 C1 (CC4+) + C2; external NONE)

  The excess of three had eight possible shapes.  Two die by counting
  edges through the shared cells (the lambda-4 pair two rungs below the
  floor), one by confining its heavy vertices to five cells, one by its
  own bound, three by a census the field cannot supply, and the last --
  three disjoint lambda-2 pairs at exact equality -- twice over, by one
  unit and by three.  The 1,549-configuration lambda-4 frontier of
  turn 13 is gone; the frontier is X = 4, where 12,171 configurations
  wait.

  THE MARGIN IS ONE UNIT OF (D2) on the field side (all five survivors
  at D2 = 11), and ZERO units of W on triangle and path, where the
  census clash -- not the bound -- does the killing.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(1 if FAILED else 0)
