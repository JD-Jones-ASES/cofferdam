#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
0025 -- SUPPORT POSTURES: THE ATLAS KILLS, GENERATED NOT NARRATED.
        X >= 10 EVERYWHERE; X = 10 => m <= 25.

THEOREMS
--------
  (T-A25) X >= 10 FOR EVERY CRITICAL CORE IN THE WINDOW [22, 456].
      Chain: 0021 (X >= 7, the 7/8/9 windows) -> 0024 (X != 7; the
      X = 8 and X = 9 atlases are the ONLY surviving cells) -> this
      file (every atlas cell is structurally impossible).  The
      minimum-excess frontier moves two layers in one turn.

  (T-B25) X = 10  =>  m <= 25.  Equivalently m >= 26 => X >= 11.
      0024's T-B24 (X = 10 => m <= 28 + the high-rung atlas) plus this
      file's kills of every X = 10 cell at m = 26, 27, 28.  The live
      minimum-excess frontier becomes X = 10 ON m IN [22, 25] -- the
      66 cells of 0024's low-rung atlas are the entire next campaign.

THE METHOD -- POSTURES FROM GRAPHS, NOT FROM PROSE.  Three outside
audits in a row lost a posture to narration (the third: one partition
listed where three survive; the fifth: an unlisted adjacent-apex; the
sixth: "edge-disjoint" asserted for shapes whose support triangles are
realizable -- refuted at this desk and by two hostile lanes, one with
an explicit 3-edge witness).  So this certificate ENUMERATES: a
posture of the shape pi = (q_1..q_t) is a simple graph H whose t
labeled edges are the support pairs and whose vertices are core-edges
(canonical-growth enumeration, deduplicated, counts asserted).  Each
posture is then closed and killed by the first law that reaches it:

  (K0) CLOSURE.  Pairs a, b sharing a core-edge force
       q(f_a, f_b) >= q_a + q_b - 5 on their far ends; a forced
       excessive pair that is not in H kills the posture (it would
       need a part pi does not have).
  (K1) (C3).  A core-edge ridden by pairs of total label x_e obeys
       x_e <= floor((52 + 3X - 2m) / 5)  (0017, billed).  Every
       q = 4 + q = 3 adjacency dies here at once (x_e >= 7).
  (K2) THE BUDGET.  J >= sum over sets, greedily, of q_i x (fresh
       cells under the pairwise caps); (SJ) P <= R - J; the (LD)/(KC)
       knapsack ceiling under the (PC) degree cap must clear the
       moment requirement m^2 - 43m + 2X + 15n - 3 floor(m/2).
  (K3) CAPACITY.  High cells live only in multi-membership regions:
       membership patterns M (>= 2 sets, pairwise caps > 0, the
       triangle-coincidence law: two sets of an H-triangle intersect
       INSIDE the third, so |M ^ triangle| = 2 is impossible); each
       pattern's F-cap is sum q - max q (and (KC)); its degree cap is
       min of that and (PC); an exact small ILP over pattern counts
       under slot and pair-cap constraints bounds Psi.

PAIRWISE CAPS, DERIVED PER POSTURE.  |S_a ^ S_b| <= min(q)+1 always;
adjacent pairs: = the triple intersection, <= label(far pair) + 1 if
that pair is in H, else <= 1; disjoint pairs: >= 2 would force all
four crosses excessive, so <= 1 unless H carries all four.

EXTERNAL INPUTS (the cited-constant ledger)
-------------------------------------------
  0024 (the atlases; (PC)/(GPC); Lambda)  -- the cells killed here are
       exactly 0024's certified survivor lists; (PC) caps degrees
       inside K2/K3; the moment requirement is 0024 section 3's.
  0021 ((SJ)/(LD)/(KC); T-B21 windows)    -- the budget engine.
  0017 ((C3) the per-edge excess cap)     -- K1.  Without it: every
       C3-killed posture falls through to K2/K3, and M-C3 prices the
       outcome (the kills still close -- (C3) is a belt here, but the
       belt is billed).
  0008/0005 ((D2), degree floor)          -- inherited via 0024's
       atlases and Lambda.
  0013/0014 (the window [22, 456])        -- "everywhere" is finite.
  No peer text is cited (D-036).  The sixth audit PROPOSED kills of
  this shape; its union-bound route was REFUTED for (4,3,2)/(4,3,3)/
  (4,3,2,1) (desk + two lanes, independently); the generated posture
  space plus K1-K3 is the lab's own repair, and the refuted route
  appears below only as the M-UNION mutation's corpse.

MANDATORY HONESTY NOTES
-----------------------
 (1) NOTHING HERE IS A NONEXISTENCE PROOF ALONE.  This file kills the
     SURVIVOR CELLS of 0024's relaxation.  The two files together --
     and only together -- give X >= 10 and the staircase.
 (2) THE POSTURE SPACE IS THE COMPLETENESS CLAIM.  Every simple graph
     with t labeled edges, no isolated vertices, vertices <= 2t is
     enumerated (counts asserted per shape; M-POST deletes one posture
     class and the count assertions notice).  What is NOT enumerated:
     support structures on MORE core-edges than 2t -- impossible,
     since t pairs involve <= 2t distinct core-edges.
 (3) J IS BOUNDED, NOT COMPUTED.  K2's greedy J is a lower bound under
     the derived caps; a hostile lane's exhaustive realizability audit
     (k <= 6 support edges) found min J = 36/23/27/23/20/23 for
     (4,4)/(3,3,2)/(3,3,3)/(4,3,2)/(4,3,3)/(4,3,2,1) -- each >= this
     file's greedy bound where used, and the greedy bound is used only
     in the sound direction.
 (4) PROVENANCE.  Desk turn 20.  The posture-generation cure and both
     new kills were desk-derived after the sixth audit's posture gaps
     surfaced; every constant was re-derived in-house (>= 2
     implementations, D-036) before assertion.

NOTATION.  As in 0015-0024.  H = the support graph; a POSTURE is H
with labels; T = a triple intersection; slots_a = |S_a| = q_a + 1;
caps = the pairwise intersection bounds; req = the 0024 section-3
moment floor at the cell's exact n.
"""

import sys
import time
from itertools import combinations
from math import comb

START = time.time()
FAILED = []
NCHECK = [0]
NNOTE = [0]


def check(name, ok, detail=""):
    NCHECK[0] += 1
    tag = "ok  " if ok else "FAIL"
    if not ok:
        FAILED.append("%d. %s" % (NCHECK[0], name.split(".")[0]))
    print("  [%s] %d. %s%s" % (tag, NCHECK[0], name,
                               ("  [%s]" % detail) if detail else ""))
    return ok


def note(text):
    NNOTE[0] += 1
    print("  [note] %s" % text)


def head(text):
    print()
    print("=" * 74)
    print("  " + text)
    print("=" * 74)



# ======================================================================
head("0.  PRIMITIVES (0024/0021/0017, restated and billed)")
# ======================================================================

def Phi(a, b):
    q, r = divmod(a, b)
    return r * comb(q + 1, 2) + (b - r) * comb(q, 2)


def F(d):
    return Phi(d, 5)


def psi(d):
    f = max(d - 5, 0)
    return f * (f + 2)


def req(X, m, nvec):
    """0024 section 3's moment floor at the cell's exact n."""
    return m * m - 43 * m + 2 * X + 15 * sum(nvec) - 3 * (m // 2)


def dcap_pc(X, m, nvec):
    """(PC), billed from 0024: the LOOSEST per-vertex degree cap over
    the parts of nvec (loosest = sound for upper bounds)."""
    best = 5
    for i in range(6):
        gt = nvec[:i] + nvec[i + 1:]
        d = 5
        while d + 1 <= m:
            if sum(Phi(d + 1, nj) for nj in gt) > X:
                break
            d += 1
        best = max(best, d)
    return best


def dcap_F(cf):
    d = 5
    while F(d + 1) <= cf:
        d += 1
    return d


def knap_max(budget, cf, dmax):
    """Max sum psi over high multisets with sum F <= budget, F <= cf,
    d <= dmax -- the 0021 (LD)/(KC) knapsack under the (PC) cap."""
    if budget < 0:
        return -1
    items = [(F(d), psi(d)) for d in range(6, dmax + 1) if F(d) <= cf]
    best = [0] * (budget + 1)
    for b in range(1, budget + 1):
        for (c, v) in items:
            if c <= b and best[b - c] + v > best[b]:
                best[b] = best[b - c] + v
    return best[budget]


check("PRIMITIVE TABLES.  F(6..11) = 1,2,3,4,5,7; psi(6..11) = "
      "3,8,15,24,35,48; req(8,23,6^6) = 63 and req(9,26,6^5 7) = 92 "
      "(the +15-per-vertex n-term is live); (C3)'s cap floor((52 + "
      "3X - 2m)/5) reads 6/6/5 at (8,22)/(9,23)/(10,27)",
      [F(d) for d in range(6, 12)] == [1, 2, 3, 4, 5, 7]
      and [psi(d) for d in range(6, 12)] == [3, 8, 15, 24, 35, 48]
      and req(8, 23, (6,) * 6) == 63
      and req(9, 26, (6, 6, 6, 6, 6, 7)) == 92
      and [(52 + 3 * X - 2 * m) // 5
           for (X, m) in ((8, 22), (9, 23), (10, 27))] == [6, 6, 5])


# ======================================================================
head("1.  THE POSTURE SPACE -- enumerated, closed, deduped, counted")
# ======================================================================

def postures(pi):
    """Every drawing of the t labeled support pairs as edges of a
    simple graph: canonical growth (endpoints reuse existing vertices
    or extend minimally).  Vertices are core-edges; two distinct pairs
    cannot join the same two core-edges (one q per edge pair)."""
    t = len(pi)
    out = []

    def rec(i, edges, nverts):
        if i == t:
            out.append(list(edges))
            return
        q = pi[i]
        for u in range(nverts):
            for v in range(u + 1, nverts):
                if any(set((u, v)) == set(e) for (e, _) in edges):
                    continue
                rec(i + 1, edges + [((u, v), q)], nverts)
        for u in range(nverts):
            rec(i + 1, edges + [((u, nverts), q)], nverts + 1)
        rec(i + 1, edges + [((nverts, nverts + 1), q)], nverts + 2)

    rec(0, [], 0)
    return out


def closure_ok(edges):
    """(K0) Pairs {e,f}, {e,g} force q(f,g) >= q_a + q_b - 5 (their
    shared sets live inside e's six cells); a forced excessive pair
    absent from H is a part pi does not have."""
    lab = {}
    for ((u, v), q) in edges:
        lab[frozenset((u, v))] = q
    for (ea, qa), (eb, qb) in combinations(edges, 2):
        shared = set(ea) & set(eb)
        if len(shared) == 1:
            fa = (set(ea) - shared).pop()
            fb = (set(eb) - shared).pop()
            if qa + qb - 5 >= 1:
                if lab.get(frozenset((fa, fb)), 0) < qa + qb - 5:
                    return False
    return True


def pair_caps(edges):
    """max |S_a ^ S_b| per pair of support pairs (see header)."""
    t = len(edges)
    lab = {}
    for ((u, v), q) in edges:
        lab[frozenset((u, v))] = q
    cap = [[0] * t for _ in range(t)]
    for a in range(t):
        for b in range(a + 1, t):
            (ea, qa), (eb, qb) = edges[a], edges[b]
            mn = min(qa, qb) + 1
            shared = set(ea) & set(eb)
            if len(shared) == 1:
                fa = (set(ea) - shared).pop()
                fb = (set(eb) - shared).pop()
                third = lab.get(frozenset((fa, fb)))
                c = min(mn, (third + 1) if third is not None else 1)
            else:
                crosses = [frozenset((x, y)) for x in ea for y in eb]
                c = mn if all(fs in lab for fs in crosses) else 1
            cap[a][b] = cap[b][a] = c
    return cap


def triangles(edges):
    tri = []
    for a, b, c in combinations(range(len(edges)), 3):
        vs = set(edges[a][0]) | set(edges[b][0]) | set(edges[c][0])
        if len(vs) == 3:
            tri.append((a, b, c))
    return tri


_PD = {}


def pdata(pi):
    """Closure-surviving posture CLASSES: drawings deduped by derived
    signature (cap matrix + triangle set + max core-edge load) --
    isomorphic drawings produce identical downstream computations."""
    if pi not in _PD:
        seen = {}
        for p in postures(pi):
            if not closure_ok(p):
                continue
            cap = pair_caps(p)
            tri = triangles(p)
            load = {}
            for ((u, v), q) in p:
                load[u] = load.get(u, 0) + q
                load[v] = load.get(v, 0) + q
            sig = (tuple(tuple(cap[a]) for a in range(len(p))),
                   tuple(sorted(tri)), max(load.values()))
            if sig not in seen:
                seen[sig] = {"p": p, "cap": cap, "tri": tri,
                             "maxload": max(load.values())}
        _PD[pi] = list(seen.values())
    return _PD[pi]


SHAPES = [(4, 4), (3, 3, 2), (4, 4, 1), (4, 3, 2), (3, 3, 3),
          (3, 3, 2, 1), (3, 3, 1, 1, 1), (3, 2, 2, 2), (2, 2, 2, 2, 1),
          (4, 4, 2), (4, 4, 1, 1), (4, 3, 3), (4, 3, 2, 1),
          (3, 3, 3, 1), (3, 3, 2, 2), (3, 3, 2, 1, 1), (2, 2, 2, 2, 2),
          (2, 2, 2, 2, 1, 1)]
COUNTS = [1, 3, 2, 3, 2, 12, 48, 17, 69,
          1, 7, 2, 7, 7, 14, 58, 50, 459]

check("THE POSTURE CLASSES, COUNTED -- the completeness anchor "
      "(delete any class and this line goes red): " +
      ", ".join("%s:%d" % (s, c) for (s, c) in zip(SHAPES, COUNTS)),
      [len(pdata(s)) for s in SHAPES] == COUNTS)

tri432 = [pd for pd in pdata((4, 3, 2)) if pd["tri"]]
check("THE SIXTH AUDIT'S GAP, PINNED FOREVER.  The (4,3,2) support "
      "TRIANGLE exists as a posture class (the audit asserted "
      "edge-disjointness and never analysed it); its pairwise caps "
      "are (3,3,3), NOT <= 1 as the edge-disjoint reading assumed; "
      "its shared core-edge carries load 4 + 3 = 7.  Same for the "
      "(4,3,3) triangle (caps (3,4,4)/(4,3,3) rows, load 7).  Both "
      "are killed below by laws, not by assumption",
      len(tri432) == 1
      and sorted(tri432[0]["cap"][0][1:]) == [3, 3]
      and tri432[0]["maxload"] == 7
      and len([pd for pd in pdata((4, 3, 3)) if pd["tri"]]) == 1
      and [pd for pd in pdata((4, 3, 3)) if pd["tri"]][0]["maxload"]
      == 7)


# ======================================================================
head("2.  THE KILLS")
# ======================================================================

def J_lb(edges, cap):
    """Greedy fresh-cell lower bound on J = sum_v qmax(v): sets in
    label order (descending q); each set's cells not capped away by
    earlier sets carry qmax >= its q."""
    t = len(edges)
    order = sorted(range(t), key=lambda a: -edges[a][1])
    J = 0
    for rank, a in enumerate(order):
        qa = edges[a][1]
        fresh = (qa + 1) - sum(cap[a][b] for b in order[:rank])
        if fresh > 0:
            J += qa * fresh
    return J


def budget_kill(X, m, pi, nvec, pd, dmax=None, capfn=None):
    R = sum(q * (q + 1) for q in pi)
    cap = capfn(pd["p"]) if capfn is not None else pd["cap"]
    P = R - J_lb(pd["p"], cap)
    if P < 0:
        return True
    if dmax is None:
        dmax = dcap_pc(X, m, nvec)
    return knap_max(P, X - pi[0], dmax) < req(X, m, nvec)


def capacity_kill(X, m, pi, nvec, pd, dmax=None, coincidence=True,
                  capfn=None):
    """Exact small ILP over membership patterns (see header K3)."""
    edges, cap, tri = pd["p"], pd["cap"], pd["tri"]
    if capfn is not None:
        cap = capfn(edges)
    t = len(edges)
    if dmax is None:
        dmax = dcap_pc(X, m, nvec)
    cf_kc = X - pi[0]
    pats = []
    for size in range(2, t + 1):
        for M in combinations(range(t), size):
            if any(cap[a][b] == 0 for a, b in combinations(M, 2)):
                continue
            if coincidence and any(len(set(M) & set(T)) == 2
                                   for T in tri):
                continue
            qs = [edges[a][1] for a in M]
            fcap = min(sum(qs) - max(qs), cf_kc)
            if fcap < 1:
                continue
            d = min(dcap_F(fcap), dmax)
            if d < 6:
                continue
            capM = min(cap[a][b] for a, b in combinations(M, 2))
            pats.append((M, capM, psi(d)))
    slots = [edges[a][1] + 1 for a in range(t)]
    need = req(X, m, nvec)
    paircap = {}
    for a, b in combinations(range(t), 2):
        paircap[(a, b)] = cap[a][b]
    best = [0]

    def dfs(i, used_slots, used_pairs, val):
        if val > best[0]:
            best[0] = val
        if best[0] >= need or i == len(pats):
            return
        if val + sum(c * p for (_, c, p) in pats[i:]) <= best[0]:
            return
        (M, capM, ps) = pats[i]
        cmax = capM
        for a in M:
            cmax = min(cmax, slots[a] - used_slots[a])
        for a, b in combinations(M, 2):
            cmax = min(cmax, paircap[(a, b)] - used_pairs[(a, b)])
        for c in range(cmax, -1, -1):
            us = list(used_slots)
            for a in M:
                us[a] += c
            up = dict(used_pairs)
            for a, b in combinations(M, 2):
                up[(a, b)] += c
            dfs(i + 1, us, up, val + c * ps)
            if best[0] >= need:
                return

    dfs(0, [0] * t, {k: 0 for k in paircap}, 0)
    return best[0] < need


def cell_dead(X, m, pi, nvec, use_c3=True, use_bud=True, use_cap=True,
              dmax=None, coincidence=True, capfn=None, use_J=True):
    """True iff every posture class dies; returns (verdict, kills)."""
    c3 = (52 + 3 * X - 2 * m) // 5
    kills = {"C3": 0, "BUD": 0, "CAP": 0}
    for pd in pdata(pi):
        if use_c3 and pd["maxload"] > c3:
            kills["C3"] += 1
            continue
        if use_bud:
            if use_J:
                ok = budget_kill(X, m, pi, nvec, pd, dmax=dmax,
                                 capfn=capfn)
            else:
                R = sum(q * (q + 1) for q in pi)
                dm = dmax if dmax is not None else dcap_pc(X, m, nvec)
                ok = knap_max(R, X - pi[0], dm) < req(X, m, nvec)
            if ok:
                kills["BUD"] += 1
                continue
        if use_cap and capacity_kill(X, m, pi, nvec, pd, dmax=dmax,
                                     coincidence=coincidence,
                                     capfn=capfn):
            kills["CAP"] += 1
            continue
        return False, kills
    return True, kills


# ======================================================================
head("3.  THE ATLAS KILLS -- every 0024 survivor cell dies")
# ======================================================================

V66 = (6, 6, 6, 6, 6, 6)
V57 = (6, 6, 6, 6, 6, 7)
V477 = (6, 6, 6, 6, 7, 7)

# 0024's certified atlases, restated verbatim (billed).
ATLAS8 = [
    (22, (4, 4), V66),
    (23, (3, 3, 2), V66), (23, (4, 4), V66),
    (24, (3, 3, 2), V66), (24, (4, 4), V66), (24, (4, 4), V57),
    (25, (4, 4), V66), (26, (4, 4), V66),
]
ATLAS9 = [
    (22, (4, 4, 1), V66),
    (23, (3, 3, 3), V66), (23, (4, 3, 2), V66),
    (23, (4, 4, 1), V66), (23, (4, 4, 1), V57),
    (24, (2, 2, 2, 2, 1), V66), (24, (3, 2, 2, 2), V66),
    (24, (3, 3, 1, 1, 1), V66), (24, (3, 3, 2, 1), V66),
    (24, (3, 3, 3), V66), (24, (3, 3, 3), V57),
    (24, (4, 3, 2), V66), (24, (4, 4, 1), V66), (24, (4, 4, 1), V57),
    (25, (3, 3, 2, 1), V66), (25, (3, 3, 3), V66),
    (25, (3, 3, 3), V57), (25, (4, 4, 1), V66), (25, (4, 4, 1), V57),
    (26, (3, 3, 3), V66), (26, (3, 3, 3), V57),
    (26, (4, 4, 1), V66), (26, (4, 4, 1), V57),
]
ATLAS10 = [
    (26, (2, 2, 2, 2, 1, 1), V66), (26, (2, 2, 2, 2, 2), V66),
    (26, (3, 3, 2, 1, 1), V66),
    (26, (3, 3, 2, 2), V66), (26, (3, 3, 2, 2), V57),
    (26, (3, 3, 3, 1), V66), (26, (3, 3, 3, 1), V57),
    (26, (4, 3, 2, 1), V66),
    (26, (4, 3, 3), V66), (26, (4, 3, 3), V57),
    (26, (4, 4, 1, 1), V66), (26, (4, 4, 1, 1), V57),
    (26, (4, 4, 2), V66), (26, (4, 4, 2), V57), (26, (4, 4, 2), V477),
    (27, (3, 3, 2, 2), V66), (27, (3, 3, 3, 1), V66),
    (27, (4, 3, 3), V66), (27, (4, 4, 1, 1), V66),
    (27, (4, 4, 2), V66), (27, (4, 4, 2), V57),
    (28, (4, 4, 2), V66),
]


def killall(rows, X, **kw):
    live = []
    tally = {"C3": 0, "BUD": 0, "CAP": 0}
    for (m, pi, nvec) in rows:
        dead, kills = cell_dead(X, m, pi, nvec, **kw)
        for k in tally:
            tally[k] += kills[k]
        if not dead:
            live.append((m, pi, nvec))
    return live, tally


t0 = time.time()
live8, t8 = killall(ATLAS8, 8)
check("THE X = 8 ATLAS IS DEAD -- all 8 cells, every posture class "
      "(kill tally C3/BUD/CAP = %d/%d/%d).  With 0024's T-A24 "
      "(X >= 8) and T-B21 (X = 8 => m <= 28): X != 8 ANYWHERE"
      % (t8["C3"], t8["BUD"], t8["CAP"]),
      live8 == [], "%.0f s" % (time.time() - t0))

t0 = time.time()
live9, t9 = killall(ATLAS9, 9)
check("THE X = 9 ATLAS IS DEAD -- all 23 cells (kill tally C3/BUD/"
      "CAP = %d/%d/%d).  With T-B21 (X = 9 => m <= 29) and 0024's "
      "zero rows at 27-29: X != 9 ANYWHERE -- the (4,3,2) triangle "
      "the audit missed dies at (9,23) and (9,24) inside this tally"
      % (t9["C3"], t9["BUD"], t9["CAP"]),
      live9 == [], "%.0f s" % (time.time() - t0))

t0 = time.time()
live10, t10 = killall(ATLAS10, 10)
check("THE X = 10 HIGH-RUNG ATLAS IS DEAD -- all 22 cells at "
      "m = 26/27/28 (kill tally C3/BUD/CAP = %d/%d/%d)"
      % (t10["C3"], t10["BUD"], t10["CAP"]),
      live10 == [], "%.0f s" % (time.time() - t0))


# ======================================================================
head("4.  ASSEMBLY")
# ======================================================================

check("(T-A25)  X >= 10 FOR EVERY CRITICAL CORE.  0021: X >= 7 and "
      "the windows; 0024: X != 7 (T-A24) and the X = 8 / X = 9 "
      "atlases are the ONLY cells the exact sweep leaves; section 3: "
      "every such cell is posture-impossible.  Hence X != 7, 8, 9 "
      "everywhere on [22, 456]: X >= 10",
      live8 == [] and live9 == [])

check("(T-B25)  X = 10 => m <= 25.  0024's T-B24 (X = 10 => m <= 28, "
      "with the 22-cell high-rung atlas certified); section 3 kills "
      "all 22.  The live minimum-excess frontier is X = 10 on "
      "m in [22, 25] -- 0024's 74-cell low-rung atlas is the whole "
      "next campaign",
      live10 == [])


# ======================================================================
head("5.  MUTATIONS -- five, priced")
# ======================================================================

MUT = []


def mut(name, flipped, expect, detail):
    MUT.append(name)
    tag = "ok  " if flipped == expect else "FAIL"
    if flipped != expect:
        FAILED.append("MUT " + name.split()[0])
    print("  [%s] %s -- %s" % (tag, name, detail))


t0 = time.time()
c8, _ = killall(ATLAS8, 8, use_c3=False)
c9, _ = killall(ATLAS9, 9, use_c3=False)
c10, _ = killall(ATLAS10, 10, use_c3=False)
mut("M-C3  (0017) withdrawn from the kill chain",
    (c8, c9, c10) == ([], [], []),
    True,
    "every atlas cell STILL dies -- (C3) is a measured BELT here "
    "(1112 posture kills rerouted to budget/capacity), billed but "
    "not load-bearing.  %.0f s" % (time.time() - t0))

t0 = time.time()
j8, _ = killall(ATLAS8, 8, use_J=False)
j9, _ = killall(ATLAS9, 9, use_J=False)
j10, _ = killall(ATLAS10, 10, use_J=False)
mut("M-J  the greedy J credit zeroed (budget = all of R)",
    (j8, j9, j10) == ([], [], []),
    True,
    "every atlas cell STILL dies -- the capacity ILP alone carries "
    "the atlases; the J-budget kill is a second measured BELT.  The "
    "file's load-bearing spine is CAPACITY + (PC), priced next.  "
    "%.0f s" % (time.time() - t0))

TRI_SHAPES9 = [(23, (3, 3, 3), V66), (23, (4, 3, 2), V66),
               (24, (3, 3, 3), V66), (24, (4, 3, 2), V66),
               (23, (3, 3, 2), V66), (24, (3, 3, 2), V66)]
t0 = time.time()
coin_live6 = []
for (m, pi, nv) in TRI_SHAPES9:
    X_ = 8 if pi == (3, 3, 2) else 9
    dead, _ = cell_dead(X_, m, pi, nv, coincidence=False)
    if not dead:
        coin_live6.append((X_, m, pi))
coin_flips = []
for (X_, m, pi, nv) in [(9, 24, (3, 3, 3), V57),
                        (10, 26, (3, 3, 2, 1, 1), V66),
                        (10, 26, (3, 3, 3, 1), V66)]:
    dead, _ = cell_dead(X_, m, pi, nv, coincidence=False)
    if not dead:
        coin_flips.append((X_, m, pi, nv))
mut("M-COIN  the triangle-coincidence law disabled -- LOAD-BEARING, "
    "not a belt",
    coin_live6 == [] and len(coin_flips) == 3,
    True,
    "a full-atlas measurement (5,424 s, off-cert) found the law "
    "carries THREE cells: (9,24,(3,3,3),6^5 7), "
    "(10,26,(3,3,2,1,1),6^6) and (10,26,(3,3,3,1),6^6) all REOPEN "
    "without it (re-verified here), while the six 6^6 triangle rows "
    "at X = 8/9 still die behind C3/budget.  An earlier draft of "
    "this mutation scoped only those six rows and called the law a "
    "third belt -- WRONG, caught by the full measurement the same "
    "day; the coincidence law (S_a ^ S_b = e ^ f ^ g inside the "
    "third set) is part of the SPINE.  %.0f s" % (time.time() - t0))

def worst_caps(edges):
    t = len(edges)
    cap = [[0] * t for _ in range(t)]
    for a in range(t):
        for b in range(a + 1, t):
            c = min(edges[a][1], edges[b][1]) + 1
            cap[a][b] = cap[b][a] = c
    return cap


d1, _ = cell_dead(10, 26, (3, 3, 2, 1, 1), V66, capfn=worst_caps)
mut("M-CAPS  pairwise caps loosened to min(q)+1 (posture-blind)",
    not d1,
    True,
    "(10,26,(3,3,2,1,1),6^6) REOPENS under posture-blind caps -- "
    "the derived caps are load-bearing: without the posture space "
    "the capacity ILP reaches 84 >= 79 and the budget dies with it. "
    "THE POSTURE MACHINERY IS THE PROOF, not decoration")

d2, _ = cell_dead(9, 23, (3, 3, 3), V66, dmax=dcap_F(9 - 3))
mut("M-PCCAP  the (PC) degree cap replaced by (KC)-only",
    not d2,
    True,
    "(9,23,(3,3,3),6^6) REOPENS without 0024's pointwise law: the "
    "triangle's T carries d <= 10 under (KC) alone (4 x psi(10) = "
    "140 >= 65) and only (PC)'s d <= 7 closes it (4 x psi(7) = 32 "
    "< 65).  (PC) is THE load-bearing degree law of this file")


check("MUTATION LEDGER: %d mutants priced" % len(MUT), len(MUT) == 5)


# ======================================================================
head("RESULT")
# ======================================================================

ok = not FAILED
print()
print("  checks : %d" % NCHECK[0])
print("  notes  : %d (stated, not tested)" % NNOTE[0])
print("  failed : %d%s" % (len(FAILED),
                           "" if ok else "  " + " | ".join(FAILED)))
print("  time   : %.1f s" % (time.time() - START))
print()
if ok:
    print("  GREEN.  EVERY ATLAS CELL IS POSTURE-IMPOSSIBLE:")
    print("      X >= 10 for every critical core in [22, 456], and")
    print("      X = 10  =>  m <= 25.")
    print("  The live minimum-excess frontier is X = 10 on m in [22, 25].")
else:
    print("  NOT GREEN.")
sys.exit(0 if ok else 1)
