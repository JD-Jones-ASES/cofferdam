#!/usr/bin/env python3
"""Certificate 0021 -- the q_max debit: X >= 7 for every critical core in the
window, and the staircase sharpens to X = 7 => m <= 26, X = 8 => m <= 28,
X = 9 => m <= 29.

    python3 verify.py

Stdlib only.  Exact integer arithmetic on every load-bearing bound.  No
solver.  No imports from lib/.  Reads nothing from disk.  Runs under
Python 3.9 and under python3 -O.  Deterministic (hand-rolled LCG, seed
20260728; no dict-order dependence).

WHAT IS CLAIMED
---------------
  (SJ) THE UN-WEAKENED SUMMED LAW.  P + J <= R, where P := sum_v F(d(v)),
      J := sum_v qmax(v) over ALL vertices, R := sum over pairs of
      q(q+1).
          PROVEN-BY-CERTIFICATE.  Derived in-cert by summing 0020's
          (SSC+) and using the exchange identity sum_v s(v) = R.
          PROVENANCE: this is verbatim the line 0020's own (SG) proof
          passes through before weakening J to H -- see 0020's
          NOTES.md, "### (SG) P + H <= R", the sentence beginning
          "Sum (SSC+) over every vertex".  0020 threw J away and kept
          only J >= H.  Keeping J is the whole of this certificate.

  (LD) THE LARGEST-PAIR DEBIT.  P <= R - q_1(q_1 + 1), where q_1 is the
      largest pair excess and |S_1| = q_1 + 1 its shared set.
          PROVEN-BY-CERTIFICATE.  Derived in-cert from (SJ): every one
          of the q_1 + 1 cells of S_1 has qmax >= q_1.

  (DM) THE DEGREE-MOMENT INEQUALITY, POINTWISE AND SUMMED.  For EVERY
      d >= 2,
          d^2 <= 8d - 15 + 3[d = 2] + f(d)(f(d) + 2),  f(d) := (d-5)_+,
      an IDENTITY at every d >= 5 and at d = 2, 3, with slack exactly 1
      at d = 4 and NOWHERE ELSE.  IT IS FALSE AT d <= 1, so 0005's
      min degree >= 2 is load-bearing and is billed.  Summed against
      both moments it is an EXACT identity,
          Psi = m^2 - 43m + 2X + 15n - 3 n_2 + n_4,
      Psi := sum_v psi(d(v)), psi(d) := f(d)(f(d)+2); hence
          Psi >= Lambda_X(m) := m^2 - 43m + 2X + 540 - 3 floor(m/2)
      by n >= 36, 0008's (D2) n_2 <= floor(m/2), and n_4 >= 0 (pure
      loss).
          PROVEN-BY-CERTIFICATE.  Derived in-cert; enacted.

  (RG) RESIDUAL PAIRING.  An intersecting family of r edges has a cover
      of size <= ceil(r/2).  For a cell set U with |U| = k <= 5, the
      subfamily K_U of edges avoiding all of U has tau(K_U) >= 6 - k,
      hence |K_U| >= 2(6-k) - 1.  (k >= 6 is the edge case where K_U
      may be empty; it is never used.)
          PROVEN-BY-CERTIFICATE.  Derived in-cert; enacted.

  (S5) THE PER-EDGE DEGREE SUM.  sum_{z in e} d(z) = m + 5 + x_e.
          PROVEN-BY-CERTIFICATE.  Derived in-cert; enacted per edge.

  (T-A21) X >= 7 FOR EVERY CRITICAL CORE IN THE WINDOW [22, 456].
          PROVEN-BY-CERTIFICATE.  0020 T-A20 (X >= 6) and T-B20
          (X = 6 => m <= 26), plus section 3's elimination of X = 6 on
          m = 22..26.  Belt: section 4 also empties X = 6 on
          m = 27..32, the whole of the rest of its C3 band, so the
          conclusion survives the withdrawal of T-B20.

  (T-B21) THE SHARPENED STAIRCASE.  X = 7 => m <= 26;  X = 8 => m <= 28;
      X = 9 => m <= 29.  Equivalently m >= 27 => X >= 8, m >= 29 =>
      X >= 9, m >= 30 => X >= 10.
          PROVEN-BY-CERTIFICATE.  Section 4 kills (7,27), (7,28),
          (8,29), (9,30), (9,31) and -- as a belt that removes the
          transitive dependence on T-B20 -- every remaining rung of
          every band up to the C3 ceiling m <= 34 / 35 / 37.

NOTATION.  As in 0015-0020.  K edge-critical, 6-partite (V_1..V_6),
6-uniform, intersecting, tau(K) = 6, tau(K - e) = 5.  A VERTEX is a cell
(part, value); d(v) its degree; n_d the number of vertices of degree d;
n = sum_d n_d.  lambda(e,g) = |e cap g| >= 1; q = lambda - 1;
X = sum over pairs of q;  x_e = sum_{g != e} q(e,g), sum_e x_e = 2X.
Phi(n,k) = balanced-split minimum of sum C(n_j,2).  F(d) := Phi(d,5) is
the COLLISION COST; f(d) := (d-5)_+ its linear reading;
psi(d) := f(d)(f(d)+2) is the MOMENT VALUE.  E(z) = the edges through z;
s(z) := sum over pairs inside E(z) of q; qmax(z) := the largest such q.
P := sum_v F(d(v));  J := sum_v qmax(v);  R := sum over pairs q(q+1).
The EXCESS PARTITION pi = (q_1 >= q_2 >= ... >= q_k) lists the excesses
of the excessive pairs; S_i is the i-th shared set, |S_i| = q_i + 1.

THE PROOF, IN ORDER
-------------------
 (1) THE TWO DEBITS (section 2).  Summing (SSC+) F(d(v)) + qmax(v) <=
     s(v) over every vertex, against sum_v s(v) = R, gives (SJ)
     P + J <= R.  The q_1 + 1 cells of S_1 each carry qmax >= q_1, so
     J >= q_1(q_1+1) and (LD) P <= R - q_1(q_1+1) follows.  Both are
     enacted on a built corpus, with universal-vertex must-fail
     controls and tau = qmax + 1 guard-violation witnesses.
 (2) THE MOMENT INEQUALITY (section 1).  psi is what d^2 costs once
     8d - 15 is paid: d^2 = 8d - 15 + psi(d) exactly for d >= 5, with
     the low degrees needing 3[d=2] and giving back 1 at d = 4.  Summed
     against sum_v d = 6m and sum_v d^2 = m^2 + 5m + 2X this is an
     EXACT identity for Psi, and dropping its three slack terms gives
     the floor Lambda_X(m) that every sweep below compares against.
 (3) THE ENGINE (section 0).  Every kill in this file is one integer
     knapsack:  MAXIMISE Psi = sum psi(d_i) over multisets of degrees
     d_i >= 6 subject to  sum F(d_i) <= B  and  F(d_i) <= C.
     THE COST IS F AND THE VALUE IS psi -- they are different functions
     and F(11) = 7 > f(11) = 6 is where the difference bites.  B is
     R(pi) minus a debit, C = X - q_1 is the key cap re-derived
     in-cert.  The knapsack is EXHAUSTIVE, never greedy: psi/F falls at
     d = 11, so greedy-at-cap understates once C >= 7 -- and
     understating is the false-kill direction.  M-f and M-greedy price
     both conventions.
 (4) X = 6 DIES (section 3).  Nine excess partitions -- the seven with
     parts <= 3 and, carried rather than deleted, (4,2) and (4,1,1),
     so that (q3) is spent nowhere in this file.  Four die to the
     knapsack alone, two to the key cap, and the three hard rows --
     (3,3), (2,2,2), (1^6) -- to union bounds on J, an excess-graph
     trichotomy, and finally a census-and-profile count on five
     surviving degree pairs.
 (5) THE STAIRCASE (section 4).  Five rungs, c = floor((52+3X-2m)/5) =
     3 on each, so parts <= 3 by C3.  The knapsack leaves TEN
     survivors across the five rungs; every one dies to a J-debit whose
     union bound is DERIVED, not asserted.  The belt re-runs the same
     engine on every remaining rung of every band up to the C3 ceiling.

MANDATORY HONESTY NOTES
-----------------------
 (1) PROVENANCE.  EVERY CLAIM ROW AND THE WHOLE BLUEPRINT WERE PROPOSED
     BY AN OUTSIDE AUDIT (GPT 5.6 Sol Pro, fourth audit, 2026-07-28/29,
     reading the public repo), which also found ZERO errors in the
     lab's existing chain.  Per D-036 the received text entered no
     chain: it is retained verbatim in notebook/raw/, the desk
     re-derived every step, blind lanes received statements only, and
     hostile refuter lanes were given the file verbatim and told to
     break it.  No step below cites the audit.  The audit's own
     stated-step defects, all repaired in-cert and none fatal, are
     listed in NOTES.md.
 (2) THREE SPEC NUMBERS THAT DID NOT REPRODUCE, AND THE MEASUREMENTS
     STAND.  (a) The desk spec pinned the exhaustive-vs-greedy knapsack
     gap at "up to 9"; MEASURED 10, at (C, B) = (7, 30) and (8, 30) and
     two more.  (b) The spec pinned the (7, 26) preview's J-layer at
     TWO surviving shapes, with (2,2,2,1) "alive only through its
     triangle at one unit"; MEASURED, under this file's conservative
     Jlb THREE shapes survive and (2,2,2,1) is alive at 94 against
     Lambda = 73 -- twenty-one units clear, not one.  The two-shape
     reading needs the sharper adjacency-aware bound this file derives
     and declines to impose.  (c) The spec described the (SJ) equality
     witness as an "r = 3, m = 4 family"; an EXHAUSTIVE anchored search
     over 3-, 4- and 5-partite guarded families finds equality only
     VACUOUSLY (P = J = R = 0), because a 3-partite intersecting family
     has tau <= 2 by Ryser r = 3 and the (SSC+) guard tau >= qmax + 2
     then forces qmax = 0.  Section 2 states this as the measurement it
     is and supplies a NON-VACUOUS guarded family instead.
     AND ONE SPEC NUMBER THAT DID REPRODUCE EXACTLY, AGAINST AN EARLIER
     DESK READING OF IT: the spec's "15" M-f flips is the RAW-SIEVE
     flip count and this run measures exactly 15 there.  Ten of those
     fifteen survive the union bounds, which is the number the mutation
     table reports; both are printed and asserted by the M-f check of
     section 5, and neither is a transcription error.
 (3) WHERE THE FLEET DISAGREED, THIS FILE'S MEASUREMENT SETTLES IT.
     Three intake lanes returned three different answers for the M-D2
     reopen set (nothing / m = 22 and 23 / the m = 25 zero-margin
     cell).  Section 5 measures it over ALL section 3 and section 4
     cells and prints the answer; the disagreement is recorded rather
     than tidied away.
 (4) WHAT ENACTMENT DOES AND DOES NOT PRICE.  Section 2 enacts (SJ),
     (LD), (RG), (S5) and both moments on a built corpus, which prices
     the LEMMAS.  It cannot price the census layers: nothing this lab
     can build has m >= 22.  Those are priced by the mutation suite of
     section 5, which is why every cap and every counting step carries
     a mutant.
 (5) WHAT THIS DOES NOT CLAIM.  No core is claimed to exist.  X = 7 on
     m in [22, 26] is NOT emptied -- that is the new frontier, and
     section 7 previews it as a measurement: THREE shapes are alive at
     m = 26 under this file's own conservative bound, two under the
     sharper one it declines to impose, and the single unit that gets
     quoted for the frontier belongs to one sub-branch of one of them.
     Nothing here bears on X >= 10 below m = 30.  The guarded-engine
     bonus rungs are named as leads, stated-not-claimed.

THE LEDGER, in full
-------------------
  CONSUMES.  0020 (SSC+) F(d(z)) + qmax(z) <= s(z) and (BDH)
  F(d(z)) <= s(z) as CLAIM ROWS -- (SSC+) is what is summed to get
  (SJ); 0020 T-A20 (X >= 6 window-wide) and T-B20 (X = 6 => m <= 26 and
  the four rung ceilings) as CLAIM ROWS, with T-B20's ceilings
  corroborated in-cert by section 4's belt; 0017 C3
  (2m + 5x_e <= 52 + 3X, X-unrestricted) -- LOAD-BEARING, it supplies
  the per-rung cap c and every edge-disjointness licence; 0008 (D2)
  (each edge holds at most one degree-2 vertex, hence n_2 <=
  floor(m/2)) -- LOAD-BEARING TWICE, in Lambda and in the support-edge
  profile lists; 0005 (min degree >= 2) -- LOAD-BEARING in (DM), which
  is FALSE at d <= 1.
  RE-DERIVED IN-CERT, and claim rows nowhere.  The key cap
  F(d(v)) <= X - q_1 (two-case proof) - the exchange identity
  sum_v s(v) = R - both moment identities - n >= 36 and the per-part
  degree sum m - the 42m - 10n identity - (SJ), (LD), (DM), (RG), (S5).
  NOT CONSUMED.  (q3) / lambda <= 4 IS NOT SPENT ANYWHERE: the
  partition enumeration needs only q <= 4, which is free from
  6-partiteness (distinct 6-tuples share at most 5 cells), and the two
  parts-4 rows (4,2) and (4,1,1) are CARRIED AND KILLED rather than
  deleted.  Also not consumed: 0018, 0019 internals, 0017 C2, 0015
  (CC), any solver, any (RG) alternative.
  EXTERNAL INPUTS: NONE.
"""

import itertools
import sys
import time
from math import comb

START = time.time()
FAILED = []
NCHECK = [0]
NNOTE = [0]
INTERNAL = []
LEAVES = [0]


def record(label, cond, sink):
    """The ONE place a verdict becomes a failure.  Split out of check()
    so that section 0's canary can drive this exact code path on a
    deliberately false condition, against a private sink, without
    reddening the run."""
    ok = bool(cond)
    if not ok:
        sink.append(label)
    return ok


def exit_code(sink):
    """The ONE place a failure becomes an exit status."""
    return 1 if sink else 0


def check(label, cond, detail=""):
    NCHECK[0] += 1
    ok = record(label, cond, FAILED)
    print("  [%s] %2d. %s%s" % ("ok  " if ok else "FAIL", NCHECK[0], label,
                                ("   " + detail) if detail else ""),
          flush=True)


def note(label, detail=""):
    NNOTE[0] += 1
    print("  [note] %s%s" % (label, ("   " + detail) if detail else ""),
          flush=True)


def head(s):
    print("\n=== %s ===" % s, flush=True)


def show(seq):
    return ", ".join(str(x) for x in seq)


class LCG(object):
    """The house LCG.  Deterministic; identical on every interpreter."""

    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFF

    def next(self):
        self.s = (25214903917 * self.s + 11) & 0xFFFFFFFFFFFF
        return self.s >> 16

    def below(self, k):
        return self.next() % k


# ==========================================================================
# S0.  Phi, the two cost readings, the knapsack, the censuses
# ==========================================================================

def phi(n, k):
    """Balanced-split minimum of sum C(n_j, 2) over k classes totalling n."""
    if n <= 0:
        return 0
    q, r = divmod(n, k)
    return r * comb(q + 1, 2) + (k - r) * comb(q, 2)


def F(d):
    """THE COST.  Phi(d, 5) -- the five-fibre collision floor."""
    return phi(d, 5)


def flin(d):
    """THE LINEAR READING of the same quantity, (d-5)_+.  F(d) = flin(d)
    for every d <= 10 and F(d) > flin(d) from d = 11 on."""
    return d - 5 if d > 5 else 0


def psi(d):
    """THE VALUE.  f(d)(f(d)+2) = d^2 - 8d + 15 for d >= 5."""
    return flin(d) * (flin(d) + 2)


def exc(d):
    """(d-2)(d-5), the second-moment excess of one vertex."""
    return (d - 2) * (d - 5)


def capcost(b, cost):
    """max{d : cost(d) <= b}."""
    return max(d for d in range(0, 400) if cost(d) <= b)


def knap(B, C, cost=F, dcap=None):
    """THE ENGINE.  Exhaustive integer knapsack: the largest
    Psi = sum psi(d_i) over multisets of degrees d_i >= 6 with
    sum cost(d_i) <= B and cost(d_i) <= C (and, if given, d_i <= dcap).

    NEVER GREEDY.  psi/F is 3, 4, 5, 6, 7 at d = 6..10 and 48/7 < 7 at
    d = 11, so the ratio FALLS at the top of the range the cap admits
    once C >= 7 -- greedy-at-cap then understates, and understating a
    maximum is the false-kill direction.  Unbounded-knapsack dynamic
    programme over the budget; best[b] is monotone in b because b - 1
    is always an option, so leaving budget unspent is allowed."""
    if B < 0:
        return 0
    dmax = capcost(C, cost)
    if dcap is not None:
        dmax = min(dmax, dcap)
    best = [0] * (B + 1)
    for b in range(1, B + 1):
        best[b] = best[b - 1]
        for d in range(6, dmax + 1):
            c = cost(d)
            if c <= b and best[b - c] + psi(d) > best[b]:
                best[b] = best[b - c] + psi(d)
    return best[B]


def knap_brute(B, C, cost=F, dcap=None):
    """A SECOND, DELIBERATELY STUPID maximiser: plain recursion over the
    multiset, no table, no monotonicity, no reuse of subproblems.  It
    shares no code path with knap(), so agreement is a cross-assertion
    and not a re-run."""
    dmax = capcost(C, cost)
    if dcap is not None:
        dmax = min(dmax, dcap)
    best = [0]

    def rec(d, left, acc):
        if acc > best[0]:
            best[0] = acc
        if d < 6:
            return
        k = 0
        while cost(d) * k <= left:
            rec(d - 1, left - cost(d) * k, acc + psi(d) * k)
            k += 1

    if B >= 0:
        rec(dmax, B, 0)
    return best[0]


def knap_greedy(B, C, cost=F, dcap=None):
    """GREEDY-AT-CAP, the convention this file does NOT use: take the
    largest affordable admissible degree, repeat."""
    dmax = capcost(C, cost)
    if dcap is not None:
        dmax = min(dmax, dcap)
    tot, b = 0, B
    while True:
        pick = None
        for d in range(dmax, 5, -1):
            if cost(d) <= b:
                pick = d
                break
        if pick is None:
            return tot
        tot += psi(pick)
        b -= cost(pick)


def parts_of(X, mx):
    """Every partition of X into parts <= mx, largest part first."""
    out = []

    def rec(left, m_, cur):
        if left == 0:
            out.append(tuple(cur))
            return
        for p in range(min(left, m_), 0, -1):
            rec(left - p, p, cur + [p])

    rec(X, min(mx, X) if X else 0, [])
    return out


def parts_exact(total, k, lo, hi, maxtwos=None):
    """Every multiset of exactly k integers in [lo, hi] summing to total,
    with at most maxtwos of them equal to 2 (None = no restriction)."""
    out = []
    cur = []

    def rec(left, parts, mn):
        if parts == 0:
            if left == 0:
                out.append(tuple(cur))
            return
        for p in range(mn, min(hi, left - lo * (parts - 1)) + 1):
            cur.append(p)
            rec(left - p, parts - 1, p)
            cur.pop()

    rec(total, k, lo)
    if maxtwos is None:
        return out
    return [t for t in out if sum(1 for x in t if x == 2) <= maxtwos]


def Rof(pi):
    """R(pi) = sum q(q+1) over the parts of pi."""
    return sum(q * (q + 1) for q in pi)


def c3cap(X, m):
    """0017 C3: 2m + 5 x_e <= 52 + 3X, hence x_e <= floor((52+3X-2m)/5)."""
    return (52 + 3 * X - 2 * m) // 5


def Lambda(X, m, P):
    """The floor Psi must clear.  Lambda = m^2 - 43m + 2X + 15*nmin
    - 3*n2cap, i.e. the exact identity with its three slack terms
    dropped: n >= nmin, n_2 <= n2cap, n_4 >= 0."""
    return (m * m - 43 * m + 2 * X + 15 * P["nmin"]
            - 3 * (m // 2 + P["n2bump"]))


def Jlb(pi, c, P):
    """THE UNION BOUND ON J, DERIVED AND NOT ASSERTED.  Restrict to the
    indices with q_i >= 2.  For two such indices the pairs P_i, P_j are
    EDGE-DISJOINT whenever q_i + q_j > c, because an edge in both would
    carry x_e >= q_i + q_j and C3 caps x_e at c.  Given
    edge-disjointness, |S_i cap S_j| <= 1: two common cells would lie in
    all FOUR edges, making all SIX pairs among them excessive, so the
    excess partition would need at least six parts -- which is why the
    bound is withdrawn outright at k >= 6.  Then, taking the indices in
    the order they are listed (largest q first),
        |S_i \\ (S_1 u ... u S_{i-1})| >= (q_i + 1) - (i - 1),
    and every cell of that difference carries qmax >= q_i.  Summing is
    the bound.  Returns 0 -- no bound at all, the conservative reading
    -- whenever any licence fails.

    THE WHOLE BOUND RESTS ON 0017's C3, through the edge-disjointness
    licence q_i + q_j > c.  P["c3disj"] withdraws that licence and is
    what mutant M-C3disj spends, so the price of C3 is measured and not
    only asserted."""
    k = len(pi)
    idx = [i for i in range(k) if pi[i] >= 2]
    if not P["c3disj"]:
        return 0
    if k >= 6:
        return 0
    for a, i in enumerate(idx):
        for j in idx[a + 1:]:
            if pi[i] + pi[j] <= c:
                return 0
    return sum(pi[i] * max(0, pi[i] + 1 - rank)
               for rank, i in enumerate(idx))


def Jsharp(pi, c):
    """THE SHARPER UNION BOUND -- DERIVED HERE AND THEN NOT IMPOSED.
    Jlb withdraws the moment two shared sets may share an EDGE.  In
    that case they can still not meet arbitrarily: if P_i = {e,g} and
    P_j = {e,h} meet in z >= 2 cells then those cells lie in g and h
    too, so q(g,h) >= z - 1 and the partition must contain a THIRD part
    of size >= z - 1 -- the CLOSING EDGE.  So the largest feasible
    |S_i cap S_j| is bounded by what the partition can pay for, and the
    union bound survives in weakened form.  This function measures that
    reading; the certificate's engine uses the conservative Jlb, and
    section 3 reports where the sharper one would have bitten."""
    k = len(pi)
    idx = [i for i in range(k) if pi[i] >= 2]

    def maxz(i, j):
        best = 1
        for z in range(2, min(pi[i], pi[j]) + 2):
            # edge-disjoint: all six pairs among four edges become
            # excessive, so the partition needs six parts
            if k >= 6:
                best = max(best, z)
            # adjacent: needs x_e = q_i + q_j <= c and a third part
            # of size >= z - 1 to be the closing edge
            if pi[i] + pi[j] <= c:
                rest = list(pi)
                rest.pop(max(i, j))
                rest.pop(min(i, j))
                if any(p >= z - 1 for p in rest):
                    best = max(best, z)
        return best

    tot = 0
    for rank, i in enumerate(idx):
        overlap = sum(maxz(i, j) for j in idx[:rank])
        tot += pi[i] * max(0, pi[i] + 1 - overlap)
    return tot


def budget(pi, c, P):
    """B = R(pi) - the debit.  (LD) contributes q_1(q_1+1); the union
    bound contributes Jlb; the larger of the two governs, since both are
    lower bounds on the same J."""
    d1 = pi[0] * (pi[0] + 1) if P["debit"] else 0
    return Rof(pi) - max(d1, Jlb(pi, c, P))


def budget_ld(pi, P):
    """B under (LD) alone -- the RAW sieve, before any union bound."""
    return Rof(pi) - (pi[0] * (pi[0] + 1) if P["debit"] else 0)


def censuses(m, X, highs, P):
    """EVERY integer vector (n_2, n_3, n_4, n_5) of low-degree counts
    consistent with a FIXED multiset `highs` of degrees >= 6, i.e. with

        sum_d d n_d + sum(highs)      = 6m                (first moment)
        sum_d d^2 n_d + sum(h^2)      = m^2 + 5m + 2X     (second moment)
        n = sum_d n_d + len(highs)   >= nmin              (n >= 36)
        n_2                          <= n2cap             ((D2))

    TERMINATION IS PROVEN, not hoped: every low degree is >= 2 (0005),
    so the number of low vertices is at most (6m - sum highs)/2 and the
    two inner loops are bounded by it.  n_3 is SOLVED from the first
    moment and n_2 from the vertex count, so nothing can be missed.
    EVERY emitted vector is re-verified from scratch against all four
    constraints before it leaves the loop; a violation is recorded into
    INTERNAL (checked later) rather than raised by a bare assert, which
    -O strips."""
    A = 6 * m - sum(highs)
    Bm = m * m + 5 * m + 2 * X - sum(h * h for h in highs)
    n2cap = m // 2 + P["n2bump"]
    out = []
    if A < 0:
        return out
    for nlow in range(0, A // 2 + 1):
        n = nlow + len(highs)
        if n < P["nmin"]:
            continue
        for n5 in range(0, nlow + 1):
            for n4 in range(0, nlow + 1 - n5):
                n3 = (A - 2 * nlow) - 2 * n4 - 3 * n5
                if n3 < 0:
                    continue
                n2 = nlow - n3 - n4 - n5
                if n2 < 0 or n2 > n2cap:
                    continue
                v = (n2, n3, n4, n5)
                if (2 * n2 + 3 * n3 + 4 * n4 + 5 * n5 != A
                        or 4 * n2 + 9 * n3 + 16 * n4 + 25 * n5 != Bm):
                    continue
                # RE-VERIFIED FROM SCRATCH, with every quantity
                # recomputed from m, X and the vector rather than read
                # off the loop variables.
                vd = dict((d, v[d - 2]) for d in (2, 3, 4, 5))
                if (sum(d * vd[d] for d in vd) + sum(highs) != 6 * m
                        or sum(d * d * vd[d] for d in vd)
                        + sum(h * h for h in highs) != m * m + 5 * m + 2 * X
                        or sum(vd.values()) + len(highs) < P["nmin"]
                        or vd[2] > m // 2 + P["n2bump"]
                        or any(vd[d] < 0 for d in vd)):
                    INTERNAL.append(("leaf", m, X, tuple(highs), v))
                    continue
                LEAVES[0] += 1
                out.append((n, v))
    return out


DEFAULT = dict(nmin=36, n2bump=0, cost=F, debit=True, triexcl=True,
               twosup=False, greedy=False, rg2=7, rg3=5, c3disj=True)


def alive_at(top, L):
    """THE CASE-COMBINATION CONVENTION, IN ONE PLACE.  A cell survives
    iff its maximum REACHES the floor: a TIE IS ALIVE, not dead.  Both
    sweeps call this, so the convention cannot drift between them, and
    the convention check of section 4 drives it on a real tie."""
    return top >= L


def par(**kw):
    """A parameter set: the certificate's own reading, overridden."""
    P = dict(DEFAULT)
    P.update(kw)
    return P


def KN(B, C, P, dcap=None):
    eng = knap_greedy if P["greedy"] else knap
    return eng(B, C, P["cost"], dcap)


def mincover(fam):
    """Exact tau, by iterative deepening on the six cells of the first
    uncovered edge.  Depth <= r+1 and each node has r children, so the
    search terminates and returns the MINIMUM."""
    r = len(fam[0])

    def rec(rem, k):
        if not rem:
            return True
        if k == 0:
            return False
        e = rem[0]
        for i in range(r):
            if rec([g for g in rem if g[i] != e[i]], k - 1):
                return True
        return False

    for k in range(0, r + 2):
        if rec(list(fam), k):
            return k
    return r + 2


def lam(e, g):
    return sum(1 for i in range(len(e)) if e[i] == g[i])


def pair_cover(fam):
    """(RG) step one, CONSTRUCTED: pair the edges up, take one cell each
    pair shares, and add the odd edge's first cell.  Size <= ceil(r/2)
    where r = |fam|."""
    cov = []
    i = 0
    while i + 1 < len(fam):
        e, g = fam[i], fam[i + 1]
        j = next(t for t in range(len(e)) if e[t] == g[t])
        cov.append((j, e[j]))
        i += 2
    if i < len(fam):
        cov.append((0, fam[i][0]))
    return cov


head("0.  the dependency ledger, printed in-run")

print("""    CONSUMES   0020 (SSC+)          F(d(z)) + qmax(z) <= s(z) -- the
                                    line this file SUMS, claim row
               0020 (BDH)           F(d(z)) <= s(z), claim row
               0020 T-A20           X >= 6 on the whole window
               0020 T-B20           X = 6 => m <= 26 (+ ceilings; the
                                    ceilings are re-derived by the belt)
               0017 C3              2m + 5x_e <= 52 + 3X -- LOAD-BEARING:
                                    the per-rung cap c and every
                                    edge-disjointness licence
               0008 (D2)            <= 1 degree-2 cell per edge, hence
                                    n_2 <= floor(m/2) -- LOAD-BEARING
                                    TWICE (Lambda; the profile lists)
               0005                 min degree >= 2 -- LOAD-BEARING:
                                    (DM) is FALSE at d <= 1
    DERIVES    (SJ) P + J <= R      (LD) P <= R - q_1(q_1+1)
               (DM) pointwise + summed, and the floor Lambda_X(m)
               (RG) residual pairing        (S5) per-edge degree sum
               THE KEY CAP  F(d(v)) <= X - q_1  at EVERY vertex
               the exchange identity sum_v s(v) = R
               both moments, n >= 36, the per-part degree sum m,
               and the 42m - 10n identity
    NOT USED   (q3) / lambda <= 4 IS SPENT NOWHERE.  q <= 4 is free from
               6-partiteness, and the parts-4 rows (4,2), (4,1,1) are
               carried and killed by the engine itself
               also unused: 0018, 0019 internals, 0017 C2, 0015 (CC),
               any solver
    EXTERNAL   NONE""", flush=True)

head("0(h).  the harness canary -- the failure path itself, exercised")

_probe = []
_ok_false = record("CANARY: a deliberately false condition", False, _probe)
_ok_true = record("CANARY: a true condition", True, _probe)
check("THE HARNESS REDDENS.  Before a single mathematical claim is "
      "made, the machinery that turns a verdict into a failure is "
      "driven on a deliberately FALSE condition -- against a private "
      "sink, so the run itself stays green.  record() returned False, "
      "appended exactly that one label, and exit_code() reads 1 on the "
      "sink; a true condition returns True, appends nothing, and reads "
      "0.  check() and the final sys.exit() call these same two "
      "functions, so 'ALL GREEN' below is a measurement and not a "
      "printing convention",
      _ok_false is False and _ok_true is True
      and _probe == ["CANARY: a deliberately false condition"]
      and exit_code(_probe) == 1 and exit_code([]) == 0
      and FAILED == [],
      "private sink: " + show(_probe))

# ==========================================================================
# 1.  The tables, (DM), and the knapsack convention
# ==========================================================================

head("1.  F against f, (DM) pointwise and summed, and the engine")

ok_min = True
for n in range(0, 13):
    for k in range(1, 7):
        best = None
        for compo in itertools.product(range(n + 1), repeat=k):
            if sum(compo) == n:
                v = sum(comb(c, 2) for c in compo)
                if best is None or v < best:
                    best = v
        if best != phi(n, k):
            ok_min = False
FTAB = [F(d) for d in range(0, 14)]
fTAB = [flin(d) for d in range(0, 14)]
PTAB = [psi(d) for d in range(0, 14)]
check("Phi(n,k) IS THE EXHAUSTIVE MINIMUM of sum C(n_j,2) over every "
      "composition of n into k classes (n <= 12, k <= 6).  THE THREE "
      "TABLES THIS FILE RUNS ON, side by side at d = 0..13: the COST "
      "F = Phi(.,5) reads 0,0,0,0,0,0,1,2,3,4,5,7,9,11; its LINEAR "
      "READING f = (d-5)_+ reads 0,0,0,0,0,0,1,2,3,4,5,6,7,8; the "
      "VALUE psi = f(f+2) reads 0,...,0,3,8,15,24,35,48,63,80.  F and "
      "f AGREE ON EVERY d <= 10 AND SEPARATE AT d = 11, where F = 7 "
      "and f = 6.  That one unit is the f/F trap: the cost is F, the "
      "value is psi, and psi is built from f",
      ok_min
      and FTAB == [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 7, 9, 11]
      and fTAB == [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
      and PTAB == [0, 0, 0, 0, 0, 0, 3, 8, 15, 24, 35, 48, 63, 80]
      and all(F(d) == flin(d) for d in range(0, 11))
      and F(11) == 7 and flin(11) == 6,
      "F(11) = %d > f(11) = %d" % (F(11), flin(11)))
CK_TAB = NCHECK[0]


def dm_rhs(d):
    return 8 * d - 15 + (3 if d == 2 else 0) + psi(d)


DM_SLACK = [(d, dm_rhs(d) - d * d) for d in range(2, 61)]
check("(DM) POINTWISE, FOR EVERY d >= 2 AND NOT JUST THE HIGH ONES: "
      "d^2 <= 8d - 15 + 3[d=2] + f(d)(f(d)+2).  Checked at d = 2..60.  "
      "It is an IDENTITY at d = 2, at d = 3 and at every d >= 5 -- for "
      "d >= 5 because psi(d) = (d-5)(d-3) = d^2 - 8d + 15 exactly -- "
      "and it has slack at exactly ONE degree, d = 4, where it gives "
      "back one unit.  That single unit is the n_4 term of the summed "
      "identity and it is a PURE LOSS when dropped.  The 3[d=2] term "
      "is what makes d = 2 an identity rather than a failure by three, "
      "and it is where 0008's (D2) enters the floor",
      all(sl >= 0 for (d, sl) in DM_SLACK)
      and [d for (d, sl) in DM_SLACK if sl != 0] == [4]
      and dict(DM_SLACK)[4] == 1
      and all(dm_rhs(d) == d * d for d in range(5, 61))
      and dm_rhs(2) == 4 and dm_rhs(3) == 9,
      "slack is 0 everywhere on 2..60 except d = 4, where it is 1")
CK_DM = NCHECK[0]

MUSTFAIL = [(d, d * d, dm_rhs(d)) for d in (0, 1)]
check("(DM) MUST-FAIL CONTROLS AT d <= 1, so that 0005's min degree "
      ">= 2 is BILLED AND NOT ASSUMED SILENTLY.  At d = 1 the right "
      "side is 8 - 15 = -7 against d^2 = 1; at d = 0 it is -15 against "
      "0.  Both FAIL, by 8 and by 15.  A census that admitted a "
      "degree-1 vertex would break the summed identity and every floor "
      "below it, which is why 0005 is a load-bearing input of this "
      "certificate and is named as one in the ledger",
      all(sq > rhs for (d, sq, rhs) in MUSTFAIL)
      and dm_rhs(1) == -7 and dm_rhs(0) == -15,
      show(["d=%d: %d > %d" % t for t in MUSTFAIL]))
CK_MF = NCHECK[0]

rng = LCG(20260728)
IDROWS = []
idbad = 0
for _ in range(400):
    vec = {}
    for d in range(2, 12):
        vec[d] = rng.below(9)
    S1 = sum(d * vec[d] for d in vec)
    if S1 % 6:
        continue
    m = S1 // 6
    S2 = sum(d * d * vec[d] for d in vec)
    if (S2 - m * m - 5 * m) % 2 or m < 2:
        continue
    X = (S2 - m * m - 5 * m) // 2
    n = sum(vec.values())
    Ps = sum(psi(d) * vec[d] for d in vec)
    rhs = m * m - 43 * m + 2 * X + 15 * n - 3 * vec[2] + vec[4]
    if Ps != rhs:
        idbad += 1
    IDROWS.append((m, X, n, Ps))
check("THE SUMMED IDENTITY, EXACT, ON RANDOM CENSUSES.  Summing (DM) "
      "against sum_v d = 6m and sum_v d^2 = m^2 + 5m + 2X, and "
      "accounting the slack exactly (one unit per degree-4 vertex, "
      "nothing anywhere else), gives Psi = m^2 - 43m + 2X + 15n - 3n_2 "
      "+ n_4 as an IDENTITY, not an inequality.  Enacted on %d random "
      "integer censuses drawn from the house LCG (seed 20260728) with "
      "degrees 2..11 -- each one has its m and X SOLVED from the two "
      "moments, so the identity is tested against the same quantities "
      "the sweeps use.  ZERO failures" % len(IDROWS),
      idbad == 0 and len(IDROWS) > 30,
      "%d censuses, 0 mismatches, m in [%d, %d]"
      % (len(IDROWS), min(t[0] for t in IDROWS), max(t[0] for t in IDROWS)))
CK_ID = NCHECK[0]

P0 = par()
LAMROWS = [(X, m, Lambda(X, m, P0)) for (X, m) in
           [(6, m) for m in range(22, 27)]
           + [(7, 27), (7, 28), (8, 29), (9, 30), (9, 31)]]
check("THE FLOOR Lambda_X(m), AND ITS THREE SLACK TERMS NAMED.  "
      "Dropping 15(n - 36) >= 0, then 3(floor(m/2) - n_2) >= 0 by "
      "0008's (D2), then n_4 >= 0 -- the last a PURE LOSS, nothing "
      "recovers it -- turns the identity into Psi >= Lambda_X(m) = "
      "m^2 - 43m + 2X + 540 - 3 floor(m/2).  It reads 57, 59, 60, 66, "
      "71 at X = 6 on m = 22..26 and 83, 92, 108, 123, 141 on the five "
      "staircase rungs.  Every kill in sections 3 and 4 is a knapsack "
      "maximum measured against one of these eleven numbers",
      [t[2] for t in LAMROWS] == [57, 59, 60, 66, 71,
                                  83, 92, 108, 123, 141]
      and Lambda(6, 22, P0) == 22 * 22 - 43 * 22 + 12 + 540 - 33,
      show(["(%d,%d): %d" % t for t in LAMROWS]))
CK_LAM = NCHECK[0]

CAPS = [(C, capcost(C, F)) for C in range(1, 9)]
check("THE KEY CAP, READ AS A DEGREE CEILING.  F(d(v)) <= X - q_1 at "
      "EVERY vertex.  TWO CASES, and this is the whole proof: if v "
      "lies in S_1, the shared set of the largest pair, then that pair "
      "is inside E(v), so qmax(v) >= q_1 and (SSC+) subtracts it from "
      "s(v) <= X; if v does not lie in S_1 then that pair is NOT "
      "inside E(v), so s(v) <= X - q_1 already and (SSC+) only helps.  "
      "Read as a ceiling, capF(C) is 6, 7, 8, 9, 10, 10, 11, 11 at "
      "C = 1..8: the cap sticks at d = 10 for every C <= 6 and admits "
      "d = 11 exactly at C = 7 and C = 8.  THAT is where the f/F trap "
      "lives, because d = 11 is the one degree whose cost F = 7 "
      "exceeds its linear reading f = 6",
      [c for (C, c) in CAPS] == [6, 7, 8, 9, 10, 10, 11, 11]
      and capcost(6, F) == 10 and capcost(7, F) == 11,
      show(["C=%d: d<=%d" % t for t in CAPS]))
CK_CAP = NCHECK[0]

XPAIRS = [(B, C) for C in range(1, 9) for B in range(0, 31)]
XBAD = [(B, C) for (B, C) in XPAIRS if knap(B, C) != knap_brute(B, C)]
check("THE ENGINE IS CROSS-ASSERTED AGAINST A SECOND, INDEPENDENT ONE.  "
      "knap() is a dynamic programme over the budget; knap_brute() is "
      "plain recursion over the multiset with no table, no "
      "monotonicity step and no reuse of subproblems.  Understating a "
      "maximum is the dangerous direction -- it would kill cells the "
      "lemmas do not kill -- so both are run on all %d (B, C) pairs "
      "with B <= 30 and C <= 8.  ALL AGREE EXACTLY" % len(XPAIRS),
      XBAD == [] and knap(10, 5) == 70 and knap_brute(10, 5) == 70,
      "%d pairs, 0 disagreements" % len(XPAIRS))
CK_XENG = NCHECK[0]

GAPS = [(C, B, knap(B, C), knap_greedy(B, C))
        for C in range(1, 9) for B in range(0, 41)]
GDIFF = [(C, B, e, g, e - g) for (C, B, e, g) in GAPS if e != g]
GMAX = max(t[4] for t in GDIFF) if GDIFF else 0
check("GREEDY-AT-CAP UNDERSTATES, AND THE FILE MEASURES BY HOW MUCH.  "
      "Taking the largest affordable admissible degree and repeating "
      "agrees with the exhaustive maximum at EVERY C <= 6 -- the ratio "
      "psi/F is strictly increasing up to d = 10, so greedy is optimal "
      "there -- and DISAGREES only at C = 7 and C = 8, exactly the two "
      "caps that admit d = 11, where psi/F drops from 7 to 48/7.  "
      "MEASURED ON B <= 40: %d disagreeing cells, all of them with "
      "greedy STRICTLY BELOW the truth, largest shortfall %d.  THE "
      "DESK SPEC PINNED THAT SHORTFALL AT 9; MEASURED %d, and the "
      "measurement is what stands"
      % (len(GDIFF), GMAX, GMAX),
      GDIFF != [] and all(t[0] >= 7 for t in GDIFF)
      and all(t[4] > 0 for t in GDIFF)
      and [t for t in GAPS if t[0] <= 6 and t[2] != t[3]] == []
      and GMAX == 10,
      "worst cells: %s"
      % show(["C=%d B=%d: %d vs greedy %d" % (t[0], t[1], t[2], t[3])
              for t in GDIFF if t[4] == GMAX]))
CK_GREEDY = NCHECK[0]

CEIL = {}
for X in (6, 7, 8, 9):
    m = 22
    while c3cap(X, m) > 0:
        m += 1
    CEIL[X] = m - 1
RUNG3 = [(X, m, c3cap(X, m)) for (X, m) in
         ((7, 27), (7, 28), (8, 29), (9, 30), (9, 31))]
check("C3 SUPPLIES THE RUNG CEILINGS AND THE PART BOUND BEFORE ANY "
      "SWEEP RUNS.  sum_e x_e = 2X > 0 forces some edge to carry "
      "x_e >= 1, so a rung dies outright once floor((52+3X-2m)/5) <= "
      "0: the bands stop at m = 32, 34, 35, 37 for X = 6, 7, 8, 9.  On "
      "each of the FIVE rungs this certificate must kill, c = 3 "
      "exactly -- so the excess partition has parts <= 3 THERE BY C3, "
      "not by (q3), which is spent nowhere in this file",
      [CEIL[X] for X in (6, 7, 8, 9)] == [32, 34, 35, 37]
      and [t[2] for t in RUNG3] == [3, 3, 3, 3, 3]
      and c3cap(6, 22) == 5 and c3cap(6, 26) == 3,
      "ceilings %s; c on the five rungs %s; c(6, 22..26) = %s"
      % (show([CEIL[X] for X in (6, 7, 8, 9)]),
         show([t[2] for t in RUNG3]),
         show([c3cap(6, m) for m in range(22, 27)])))
CK_C3 = NCHECK[0]

# ==========================================================================
# 2.  The lemmas, enacted on a built corpus
# ==========================================================================

head("2.  (SJ), (LD), (RG) and (S5) -- enacted on a built corpus")

MUL4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]


def field(q):
    if q == 4:
        return (lambda a, b: a ^ b), (lambda a, b: MUL4[a][b]), (lambda a: a)
    return ((lambda a, b: (a + b) % q), (lambda a, b: (a * b) % q),
            (lambda a: (-a) % q))


def ag(q):
    """AG(2,q) as a (q+1)-partite (q+1)-uniform intersecting family of
    q^2 edges.  Every lambda is 1, so X = R = 0 and tau = q."""
    add, mul, neg = field(q)
    return [tuple([add(b, mul(neg(s), a)) for s in range(q)] + [a])
            for a in range(q) for b in range(q)]


def ag_witness(q):
    """AG(2,q) with one vertical line RENAMED on a new edge and the rest
    of that line deleted: tau = q = qmax + 1 exactly, so the (SSC+)
    guard FAILS by one and the shared cells violate it by one unit."""
    A = ag(q)
    x = A[0]
    i0 = q
    keep = [e for e in A if e == x or e[i0] != x[i0]]
    return keep + [tuple(list(x[:i0]) + [q])]


def fat_plane(q, tri):
    """AG(2,q) with one EXTRA part appended, constant on all but the
    points of `tri`.  The fat cell has degree q^2 - |tri|, which is high,
    while tau stays at q because the excluded points are not collinear.
    This is the corpus's NON-VACUOUSLY guarded family: it satisfies
    tau >= qmax + 2 with P > 0 and R > 0 at the same time."""
    A = ag(q)
    out = []
    k = 0
    for i, e in enumerate(A):
        if i in tri:
            k += 1
            out.append(tuple(list(e) + [k]))
        else:
            out.append(tuple(list(e) + [0]))
    return out


def pencil(r, k):
    """k edges through one cell -- a universal vertex by construction."""
    return [tuple([0] + [i + 1 if j == 0 else i for j in range(r - 1)])
            for i in range(k)]


def sunflower2(r, k):
    return [tuple([0, 0] + [i] * (r - 2)) for i in range(k)]


def nearpencil(r, k):
    return ([tuple([0, i] + [0] * (r - 2)) for i in range(k)]
            + [tuple([1, k] + [0] * (r - 2))])


def twins(r, k, extra, rg):
    """k edges agreeing on parts 1..r-1: every pair has lambda = r-1, so
    this is the large-q generator."""
    fam = [tuple([i] + [0] * (r - 1)) for i in range(k)]
    tries = 0
    while len(fam) < k + extra and tries < 300:
        tries += 1
        c = tuple([rg.below(3)] + [rg.below(2) for _ in range(r - 1)])
        if c in fam:
            continue
        if all(lam(c, g) >= 1 for g in fam):
            fam.append(c)
    return fam


def rand_family(r, rg, nv, target):
    fam = []
    for _ in range(400):
        if len(fam) >= target:
            break
        c = tuple(rg.below(nv) for _ in range(r))
        if c in fam:
            continue
        if all(lam(c, g) >= 1 for g in fam):
            fam.append(c)
    return fam


def greedy_family(r, nv, skip, cap):
    fam = []
    i = 0
    for c in itertools.product(range(nv), repeat=r):
        i += 1
        if i % skip:
            continue
        if all(lam(c, g) >= 1 for g in fam):
            fam.append(c)
        if len(fam) >= cap:
            break
    return fam


ACC = dict((k, 0) for k in (
    "fams", "short", "bad", "guard", "unguard", "univ", "sj_bad",
    "sj_nz", "sj_nonvac", "sj_eq_nz", "sj_eq_vac", "unguard_bad",
    "univ_bad", "rg_maxtk",
    "ld_n", "ld_bad", "ld_nz", "jhigh_short", "jhigh_n", "keycap_n",
    "keycap_bad", "s5_n", "s5_bad", "s5_nz", "star_perfam_bad",
    "mom_n", "mom_bad", "dm_n", "dm_bad", "rg_n", "rg_bad", "rg_cov",
    "rg_cov_bad", "rg_tight"))
BYR = {}
TAUH = {}


def noncollinear(q, tri):
    """Are these three points of AG(2,q) off a common line?  Read
    straight off the plane's own edges: two AG edges share exactly one
    cell, so a line is a cell, and the triple is collinear iff some
    coordinate agrees across all three."""
    A = ag(q)
    e, f, g = A[tri[0]], A[tri[1]], A[tri[2]]
    return not any(e[i] == f[i] == g[i] for i in range(len(e)))


def build_corpus():
    rg = LCG(20260728)
    fams = []
    for q in (2, 3, 4, 5):
        fams.append(ag(q))
    for q in (3, 4, 5):
        fams.append(ag_witness(q))
    # FAT PLANES, many of them: these are the only guarded families
    # this lab can build with P > 0 and R > 0 at the same time, so the
    # non-vacuous half of (SJ) and (LD) rests on them and the corpus
    # carries as many as the clock allows.
    for (q, want) in ((3, 12), (4, 8), (5, 2)):
        good = [t for t in itertools.combinations(range(q * q), 3)
                if noncollinear(q, t)]
        for tri in good[:want]:
            fams.append(fat_plane(q, tri))
    for r in range(3, 7):
        for k in (3, 4, 5, 6):
            fams.append(pencil(r, k))
            fams.append(sunflower2(r, k))
            fams.append(nearpencil(r, k))
            fams.append(twins(r, k, 2, rg))
        for nv in (2, 3, 4):
            for _ in range(6):
                fams.append(rand_family(r, rg, nv, 7))
        for skip in (1, 2, 3):
            fams.append(greedy_family(r, 3, skip, 8))
    return fams


def audit(fam):
    """Every claim of section 2, on one family."""
    if len(fam) < 3:
        ACC["short"] += 1
        return
    r = len(fam[0])
    m = len(fam)
    if (any(len(e) != r for e in fam) or len(set(fam)) != m
            or any(lam(p, g) < 1
                   for p, g in itertools.combinations(fam, 2))):
        ACC["bad"] += 1
        return
    ACC["fams"] += 1
    BYR[r] = BYR.get(r, 0) + 1
    deg = {}
    for e in fam:
        for i in range(r):
            deg[(i, e[i])] = deg.get((i, e[i]), 0) + 1
    pairs = list(itertools.combinations(fam, 2))
    X = sum(lam(p, g) - 1 for p, g in pairs)
    R = sum((lam(p, g) - 1) * lam(p, g) for p, g in pairs)
    q1 = max(lam(p, g) - 1 for p, g in pairs)
    tau = mincover(fam)
    TAUH[tau] = TAUH.get(tau, 0) + 1
    univ = any(d == m for d in deg.values())
    # ---- both moments (r-uniform, r-partite)
    ACC["mom_n"] += 1
    if (sum(deg.values()) != r * m
            or sum(comb(d, 2) for d in deg.values()) != comb(m, 2) + X):
        ACC["mom_bad"] += 1
    # ---- (S5), per edge
    for e in fam:
        xe = sum(lam(e, g) - 1 for g in fam if g != e)
        ACC["s5_n"] += 1
        if sum(deg[(i, e[i])] for i in range(r)) != m + (r - 1) + xe:
            ACC["s5_bad"] += 1
        if xe > 0:
            ACC["s5_nz"] += 1
    # ---- the star quantities and the exchange identity
    P = sum(phi(d, r - 1) for d in deg.values())
    J = 0
    Jhigh = 0
    starsum = 0
    for z in sorted(deg):
        Ez = [e for e in fam if e[z[0]] == z[1]]
        dz = len(Ez)
        s = sum(lam(p, g) - 1 for p, g in itertools.combinations(Ez, 2))
        starsum += s
        if dz < 2:
            continue
        qm = max(lam(p, g) - 1 for p, g in itertools.combinations(Ez, 2))
        J += qm
        if phi(dz, r - 1) >= 1:
            Jhigh += qm
        if (not univ) and tau >= q1 + 2:
            ACC["keycap_n"] += 1
            if phi(dz, r - 1) > X - q1:
                ACC["keycap_bad"] += 1
    if starsum != R:
        ACC["star_perfam_bad"] += 1
    # ---- (SJ) and (LD)
    if univ:
        ACC["univ"] += 1
        if P + J > R:
            ACC["univ_bad"] += 1
    elif tau >= q1 + 2:
        ACC["guard"] += 1
        if P + J > R:
            ACC["sj_bad"] += 1
        if P + J > 0:
            ACC["sj_nz"] += 1
        if P + J > 0 and R > 0:
            ACC["sj_nonvac"] += 1
        if P + J == R:
            if R > 0:
                ACC["sj_eq_nz"] += 1
            else:
                ACC["sj_eq_vac"] += 1
        ACC["ld_n"] += 1
        if P > R - q1 * (q1 + 1):
            ACC["ld_bad"] += 1
        if R - q1 * (q1 + 1) > 0 and P > 0:
            ACC["ld_nz"] += 1
        if R > 0:
            ACC["jhigh_n"] += 1
            if Jhigh < q1 * (q1 + 1):
                ACC["jhigh_short"] += 1
    else:
        ACC["unguard"] += 1
        if P + J > R:
            ACC["unguard_bad"] += 1
    # ---- (DM) summed, on the 6-partite 6-uniform families with min deg 2
    if r == 6 and min(deg.values()) >= 2:
        ACC["dm_n"] += 1
        n = len(deg)
        n2 = sum(1 for d in deg.values() if d == 2)
        n4 = sum(1 for d in deg.values() if d == 4)
        Ps = sum(psi(d) for d in deg.values())
        if Ps != m * m - 43 * m + 2 * X + 15 * n - 3 * n2 + n4:
            ACC["dm_bad"] += 1
    # ---- (RG)
    cov = pair_cover(fam)
    ACC["rg_cov"] += 1
    if (len(cov) > -(-m // 2)
            or any(not any(e[i] == v for (i, v) in cov) for e in fam)):
        ACC["rg_cov_bad"] += 1
    cells = sorted(deg)
    rg2 = LCG(20260728 + m)
    Us = [(c,) for c in cells[:6]]
    for _ in range(10):
        k = 2 + rg2.below(min(4, max(1, len(cells) - 1)))
        U = tuple(sorted(set(cells[rg2.below(len(cells))]
                             for _ in range(k))))
        if U:
            Us.append(U)
    for U in Us:
        k = len(U)
        KU = [e for e in fam if all(e[i] != v for (i, v) in U)]
        ACC["rg_n"] += 1
        tu = mincover(KU) if KU else 0
        if tu < tau - k:
            ACC["rg_bad"] += 1
        if tau - k >= 1 and len(KU) < 2 * (tau - k) - 1:
            ACC["rg_bad"] += 1
        if tau - k >= 1 and len(KU) == 2 * (tau - k) - 1:
            ACC["rg_tight"] += 1
        if tau - k >= 1 and tau - k > ACC["rg_maxtk"]:
            ACC["rg_maxtk"] = tau - k


t0 = time.time()
for _fam in build_corpus():
    audit(_fam)
CORPTIME = time.time() - t0

check("THE CORPUS.  %d intersecting r-partite families built and "
      "audited: affine planes AG(2,q) for q = 2..5, their "
      "tau = qmax + 1 guard-violation variants, TWENTY-TWO FAT PLANES "
      "(a plane with an extra part carrying one high cell, the three "
      "excluded points chosen NON-COLLINEAR -- verified in-run off the "
      "plane's own edges -- so that tau survives; this is the only "
      "construction this lab has that satisfies the (SSC+) guard "
      "NON-VACUOUSLY, i.e. with P > 0 and R > 0 together), pencils, "
      "sunflowers, near-pencils, twin families, and LCG-random and "
      "lexicographic-greedy maximal families at r = 3..6.  Every "
      "family is re-verified to be intersecting and duplicate-free "
      "before it is audited; %d were rejected as malformed and %d as "
      "too short.  tau histogram and per-r counts are printed, not "
      "asserted from memory" % (ACC["fams"], ACC["bad"], ACC["short"]),
      ACC["fams"] > 150 and ACC["bad"] == 0
      and sorted(BYR) == [3, 4, 5, 6, 7] and max(TAUH) >= 4,
      "by r: %s; tau histogram: %s; %.1fs"
      % (show(["r=%d:%d" % (k, BYR[k]) for k in sorted(BYR)]),
         show(["tau=%d:%d" % (k, TAUH[k]) for k in sorted(TAUH)]),
         CORPTIME))
CK_CORP = NCHECK[0]

check("BOTH MOMENT IDENTITIES, ON EVERY FAMILY.  sum_v d(v) = rm "
      "counts incidences twice over; sum_v C(d(v),2) = C(m,2) + X "
      "counts, for each pair of edges, the cells they share -- which "
      "is lambda = q + 1, so the total is C(m,2) + X.  Both are "
      "DOUBLE COUNTS and both are enacted here rather than quoted, on "
      "all %d families, with zero failures.  The second one is what "
      "turns (DM) from a pointwise statement into a statement about m "
      "and X" % ACC["mom_n"],
      ACC["mom_bad"] == 0 and ACC["mom_n"] == ACC["fams"],
      "%d families, 0 failures" % ACC["mom_n"])
CK_MOM = NCHECK[0]

check("THE EXCHANGE IDENTITY sum_v s(v) = R, PER FAMILY.  A pair "
      "{e,g} lies inside E(v) for exactly the lambda = q + 1 cells it "
      "shares, so summing the star excess over all vertices counts "
      "each pair q + 1 times, giving sum over pairs of q(q+1) = R.  "
      "Checked family by family, not merely corpus-wide, so "
      "compensating errors across families cannot pass.  ZERO "
      "failures.  This is the right-hand side of (SJ)",
      ACC["star_perfam_bad"] == 0 and ACC["fams"] > 0,
      "%d families, 0 mismatches" % ACC["fams"])
CK_STAR = NCHECK[0]

check("(SJ) P + J <= R, ENACTED ON THE GUARDED FAMILIES.  Sum (SSC+) "
      "F(d(v)) + qmax(v) <= s(v) over every vertex and use the "
      "exchange identity on the right: that IS (SJ).  0020 proved the "
      "same line and then weakened sum_v qmax(v) to H = #{v : d(v) >= "
      "6}, which is the crudest possible reading of it since "
      "qmax >= 1 at a high vertex.  Enacted on %d guarded families "
      "(no universal vertex, tau >= qmax + 2), zero violations, and "
      "NON-VACUOUSLY on %d of them -- the fat planes, where P + J is "
      "strictly positive AND R is strictly positive AT ONCE.  That "
      "conjunction is ONE counter and not two measured apart: %d "
      "families have P + J > 0 and %d have R > 0, and the non-vacuous "
      "count is the families that have both.  The %d UNGUARDED "
      "families are audited too and are NOT required to satisfy it; "
      "%d of them do not -- ASSERTED, not merely printed, because that "
      "is what makes the guard a hypothesis rather than decoration"
      % (ACC["guard"], ACC["sj_nonvac"], ACC["sj_nz"], ACC["jhigh_n"],
         ACC["unguard"], ACC["unguard_bad"]),
      ACC["sj_bad"] == 0 and ACC["guard"] > 20 and ACC["sj_nonvac"] > 0
      and ACC["unguard"] > 0 and ACC["unguard_bad"] > 0,
      "guarded %d (0 violations, %d non-vacuous); unguarded %d, of "
      "which %d violate"
      % (ACC["guard"], ACC["sj_nonvac"], ACC["unguard"],
         ACC["unguard_bad"]))
CK_SJ = NCHECK[0]

check("(SJ) MUST-FAIL CONTROL: THE UNIVERSAL VERTEX.  The whole "
      "mechanism starts by choosing an edge f that AVOIDS z; a vertex "
      "on every edge admits no such f, and (SSC+) -- hence (SJ) -- is "
      "simply not available.  The corpus contains %d families with a "
      "universal vertex, and %d of them BREAK P + J <= R.  They are "
      "excluded by hypothesis and not by luck: in a critical core no "
      "vertex is universal, because a universal vertex is a 1-cover "
      "and tau = 6"
      % (ACC["univ"], ACC["univ_bad"]),
      ACC["univ"] > 0 and ACC["univ_bad"] > 0,
      "%d universal-vertex families, %d violate (SJ)"
      % (ACC["univ"], ACC["univ_bad"]))
CK_UNIV = NCHECK[0]

check("(LD) P <= R - q_1(q_1+1), ENACTED.  The shared set S_1 of a "
      "largest pair has |S_1| = q_1 + 1 cells, and each of them has "
      "that pair inside its own star, so qmax >= q_1 there; J is a sum "
      "over ALL vertices and therefore already contains those "
      "q_1(q_1+1) units.  Enacted on %d guarded families, zero "
      "violations, and non-vacuously (both sides positive) on %d.  "
      "This is the debit every knapsack row of sections 3 and 4 spends"
      % (ACC["ld_n"], ACC["ld_nz"]),
      ACC["ld_bad"] == 0 and ACC["ld_n"] > 20 and ACC["ld_nz"] > 0,
      "%d families, 0 violations, %d non-vacuous"
      % (ACC["ld_n"], ACC["ld_nz"]))
CK_LD = NCHECK[0]

check("WHY J MUST RUN OVER ALL VERTICES -- THE RESTRICTED-J "
      "INSUFFICIENCY, MEASURED.  If J were summed only over the HIGH "
      "vertices (the ones that contribute to P at all), (LD) would "
      "NOT follow: the cells of S_1 need not be high.  Measured on the "
      "corpus: of %d guarded families with R > 0, %d have "
      "J restricted to high vertices STRICTLY BELOW q_1(q_1+1), so "
      "the restricted reading cannot support the debit.  The fat "
      "planes are the clean example -- one high cell, qmax 1, against "
      "a debit of 2"
      % (ACC["jhigh_n"], ACC["jhigh_short"]),
      ACC["jhigh_n"] > 0 and ACC["jhigh_short"] > 0,
      "%d of %d guarded R > 0 families fall short under the "
      "restricted reading" % (ACC["jhigh_short"], ACC["jhigh_n"]))
CK_JHIGH = NCHECK[0]

check("THE (SJ) EQUALITY QUESTION, ANSWERED BY EXHAUSTION AND NOT BY "
      "TRANSCRIPTION.  The desk spec named an 'r = 3, m = 4 equality "
      "witness'.  It reproduces -- AG(2,2) is guarded and has "
      "P + J = R -- but the equality is VACUOUS: P = J = R = 0.  IT "
      "CANNOT BE OTHERWISE AT r = 3.  Ryser's conjecture is a theorem "
      "at r = 3, so a 3-partite intersecting family has tau <= 2; the "
      "(SSC+) guard tau >= qmax + 2 then forces qmax = 0, hence R = 0. "
      "Measured on the corpus: %d guarded families reach equality "
      "vacuously and %d reach it with R > 0.  The non-vacuous "
      "enactment of (SJ) therefore rests on the fat planes, where the "
      "inequality is strict and both sides are positive -- which is "
      "stated plainly rather than dressed up as tightness"
      % (ACC["sj_eq_vac"], ACC["sj_eq_nz"]),
      ACC["sj_eq_vac"] > 0 and ACC["sj_eq_nz"] == 0
      and ACC["sj_bad"] == 0,
      "vacuous equalities %d, non-vacuous equalities %d"
      % (ACC["sj_eq_vac"], ACC["sj_eq_nz"]))
CK_EQ = NCHECK[0]

check("THE KEY CAP, ENACTED: F(d(v)) <= X - q_1 AT EVERY VERTEX of "
      "every guarded family.  %d vertices tested, zero violations.  "
      "The two-case proof is in check %d; this is the enactment of "
      "it.  Read as a degree ceiling it is the C of every knapsack "
      "below" % (ACC["keycap_n"], CK_CAP),
      ACC["keycap_bad"] == 0 and ACC["keycap_n"] > 100,
      "%d vertices, 0 violations" % ACC["keycap_n"])
CK_KEY = NCHECK[0]

check("(S5) sum_{z in e} d(z) = m + 5 + x_e, PER EDGE.  The proof is "
      "one double count: summing d(z) over the six cells of e counts "
      "each other edge g once per shared cell, i.e. lambda(e,g) = "
      "1 + q(e,g) times, plus 6 for e itself -- so the total is "
      "6 + (m-1) + x_e.  Enacted in its general r-uniform form "
      "sum = m + (r-1) + x_e on %d edges, %d of them with x_e > 0, "
      "zero failures.  Sections 3 and 4 spend it on the support edges, "
      "where x_e = 3 pins the ordinary-cell degree sum exactly"
      % (ACC["s5_n"], ACC["s5_nz"]),
      ACC["s5_bad"] == 0 and ACC["s5_nz"] > 20,
      "%d edges, %d with x_e > 0, 0 failures"
      % (ACC["s5_n"], ACC["s5_nz"]))
CK_S5 = NCHECK[0]

check("(RG) STEP ONE, CONSTRUCTED: an intersecting family of r edges "
      "has a cover of size <= ceil(r/2).  Pair the edges up; each pair "
      "shares a cell; take one such cell per pair, plus any cell of "
      "the odd edge.  That set is EXHIBITED and then verified to cover "
      "-- on all %d families, with its size checked against "
      "ceil(m/2).  Zero failures.  A construction, not an existence "
      "claim" % ACC["rg_cov"],
      ACC["rg_cov_bad"] == 0 and ACC["rg_cov"] > 150,
      "%d families, 0 failures" % ACC["rg_cov"])
CK_RGC = NCHECK[0]

check("(RG) STEP TWO: tau(K_U) >= tau - k and |K_U| >= 2(tau-k) - 1.  "
      "If C covers K_U then C u U covers all of K, since every edge "
      "either meets U or lies in K_U -- so |C| + k >= tau.  Combining "
      "with step one, ceil(|K_U|/2) >= tau(K_U) >= tau - k gives the "
      "edge count.  Enacted on %d (family, U) pairs with |U| = 1..5, "
      "zero failures, and TIGHT on %d of them -- so the bound is not "
      "slack by construction.  THE EDGE CASE IS STATED: at k >= tau "
      "the bound reads |K_U| >= negative and K_U may be empty, which "
      "is why sections 3 and 4 only ever use it at k = 2 and k = 3, "
      "where tau - k is 4 and 3.  AND WHAT THE ENACTMENT CANNOT REACH "
      "IS SAID TOO: the largest tau any family this lab can build is "
      "%d, so the (tau, k) = (6, 2) and (6, 3) instances sections 3 "
      "and 4 actually spend are carried by the PROOF above; the "
      "enactment prices the GENERAL statement, at tau - k up to %d"
      % (ACC["rg_n"], ACC["rg_tight"], max(TAUH), ACC["rg_maxtk"]),
      ACC["rg_bad"] == 0 and ACC["rg_n"] > 100 and ACC["rg_tight"] > 0
      and max(TAUH) == 5 and ACC["rg_maxtk"] == 4,
      "%d (family, U) pairs, 0 failures, %d tight; max tau built %d, "
      "max tau - k enacted %d"
      % (ACC["rg_n"], ACC["rg_tight"], max(TAUH), ACC["rg_maxtk"]))
CK_RG = NCHECK[0]

check("THE SUMMED (DM) IDENTITY ON REAL FAMILIES, not only on random "
      "censuses.  On the %d 6-partite 6-uniform corpus families whose "
      "minimum degree is >= 2 -- the hypothesis 0005 supplies for a "
      "core -- Psi = m^2 - 43m + 2X + 15n - 3n_2 + n_4 holds exactly, "
      "with m, X, n, n_2, n_4 all read off the family.  Zero "
      "mismatches.  Together with check %d this prices the identity "
      "both ways: algebraically on wide random censuses and "
      "structurally on objects that actually exist"
      % (ACC["dm_n"], CK_ID),
      ACC["dm_bad"] == 0 and ACC["dm_n"] > 0,
      "%d families, 0 mismatches" % ACC["dm_n"])
CK_DMFAM = NCHECK[0]

note("STATED, NOT TESTED -- WHAT THE CORPUS CANNOT PRICE.  Nothing "
     "this lab can build has m >= 22, so no family here can exercise "
     "the census layers of sections 3 and 4.  Those are priced by the "
     "mutation suite of section 5 instead, which is why every cap, "
     "every union bound and every counting step below carries a "
     "mutant.  The corpus prices the LEMMAS and says so")

# ==========================================================================
# 3.  T-A21: the X = 6 field on m = 22..26 is empty
# ==========================================================================

head("3.  T-A21 -- X = 6 dies on m = 22..26, so X >= 7 EVERYWHERE")

P6 = parts_of(6, 4)
check("THE NINE EXCESS PARTITIONS AT X = 6, AND WHY (q3) IS NOT SPENT.  "
      "Distinct 6-tuples of a 6-partite family share at most 5 cells, "
      "so lambda <= 5 and q <= 4 -- FREE FROM 6-PARTITENESS, with no "
      "appeal to (q3)'s lambda <= 4.  Partitions of 6 with parts <= 4 "
      "number NINE: the seven with parts <= 3 plus (4,2) and (4,1,1).  "
      "This file CARRIES the two parts-4 rows and kills them with the "
      "same engine rather than deleting them by citation, which is "
      "exactly what keeps (q3) billed to nothing in this certificate",
      len(P6) == 9 and (4, 2) in P6 and (4, 1, 1) in P6
      and len([p for p in P6 if p[0] <= 3]) == 7
      and (5, 1) not in P6 and (6,) not in P6,
      show([str(p) for p in P6]))
CK_NINE = NCHECK[0]


def s2_branches(m, pi, P):
    """Every branch of the X = 6 kill for one (m, pi) cell, as
    (label, bound).  The cell dies iff every bound is < Lambda."""
    c = c3cap(6, m)
    q1 = pi[0]
    R = Rof(pi)
    C = 6 - q1
    out = []
    if pi == (3, 3):
        # the two 4-cell shared sets meet in <= 1 cell, so their union
        # is >= 7 cells, every one carrying qmax >= 3.  That IS Jlb's
        # derivation, and Jlb returns 21 here on every rung of the
        # band -- so the bound is taken from the derived function and
        # not restated as a literal.
        J = Jlb(pi, c, P)
        out.append(("union J >= %d" % J, KN(Rof(pi) - J, C, P)))
    elif pi == (2, 2, 2):
        # THE TRICHOTOMY licenses |S_i cap S_j| <= 1 in the
        # non-triangle case AT ANY c, because two common cells force
        # the closing edge and hence a triangle.  Union >= 6, and every
        # cell of it carries qmax >= 2.  THIS FLOOR IS LIVE: Jlb
        # withdraws at c >= 4 (q_i + q_j = 4 <= c), so on m = 22..25 the
        # 12 is the only bound there is, and it does not come from C3.
        J = max(Jlb(pi, c, P), 12)
        out.append(("non-triangle, J >= %d" % J,
                    KN(Rof(pi) - J, C, P)))
        if P["triexcl"] and c < 4:
            out.append(("triangle: C3 kills (x_e = 4 > c = %d)" % c, 0))
        else:
            out.append(("triangle, <= 2 high cells", 2 * psi(capcost(4, F))))
            lim = m - (9 + P["rg3"])
            best = 0
            # THREE HIGH CELLS, so every f_i >= 1: a T-cell at f = 0 has
            # d = 5 and is NOT high, and that configuration is already
            # bounded by the <= 2 branch above.  The range starts at 1
            # so the branch computes what its label says; letting it
            # start at 0 would compute the OTHER branch's field under
            # this branch's name.
            for a in range(1, 5):
                for b in range(1, 5):
                    for d in range(1, 5):
                        if (a + b + d <= lim
                                and F(a + 5) + F(b + 5) + F(d + 5)
                                <= Rof(pi) - 6):
                            best = max(best, psi(a + 5) + psi(b + 5)
                                       + psi(d + 5))
            out.append(("triangle, |T| = 3 all high, sum f <= %d" % lim,
                        best))
    elif pi == (1,) * 6:
        out.append(("no f = 5 vertex", KN(budget(pi, c, P), C, P, dcap=9)))
        out.append(("f = 5, no K4", psi(10) + KN(budget(pi, c, P) - F(10),
                                                 C, P, dcap=7)))
    else:
        out.append(("knapsack", KN(budget(pi, c, P), C, P)))
    return out


def k4_survivors(m, P):
    """The K4 branch of (1^6): all six shared sets are {u, v}, so u and
    v are the ONLY high cells and both are capped at d = 10.  A fifth
    edge through {u,v} would make C(5,2) = 10 excessive pairs, so
    exactly four edges carry the pair and the star-union is 6 + p with
    p = f(u) + f(v); (RG) at k = 2 leaves >= %d edges avoiding both, so
    p <= m - 13.  Returns the (d_u, d_v) pairs that clear Lambda."""
    L = Lambda(6, m, P)
    pmax = m - (6 + P["rg2"])
    out = []
    for j in range(0, 6):
        p = 5 + j
        if p > pmax:
            continue
        val = psi(10) + psi(5 + j)
        if F(10) + F(5 + j) > budget((1,) * 6, c3cap(6, m), P):
            continue
        if val >= L:
            out.append((10, 5 + j, val, L))
    return out


def support_profiles(m, du, dv, P, hi=5):
    """(S5) on a support edge: x_e = 3 (it meets the other three support
    edges in {u,v} and nothing else), so the four ORDINARY cells have
    degrees summing to m + 8 - d_u - d_v.  Each is >= 2 (0005) and
    <= 5 (only u and v are high), and (D2) allows at most one of them
    to be a degree-2 cell.  `hi` is the ordinary-cell ceiling, exposed
    so the run can MEASURE whether that ceiling is load-bearing rather
    than advertise it."""
    tot = m + 5 + 3 - du - dv
    return parts_exact(tot, 4, 2, hi, maxtwos=(1 + P["n2bump"]))


def special_parts(m, d):
    """THE FIVE LOW CELLS OF A SPECIAL PART -- the part holding a high
    cell of degree d.  At n = 36 every part holds exactly six cells
    (each part is a cover, so |part| >= tau = 6), so THE PER-PART DEGREE
    SUM puts the other five at m - d.  Each is >= 2 by 0005 and <= 5
    because only u and v are high.  ONE function, called by the stage-2
    kill and asserted by the two-special-parts check, so the executed
    path is the tested path."""
    return parts_exact(m - d, 5, 2, 5)


def demand_of(choice, P):
    """The cell demand of a choice of four support-edge profiles.  No
    ordinary cell serves two support edges: two support edges share
    exactly {u,v} at q = 1, and a third common cell would give q >= 2.
    Under M-2sup that distinctness is withdrawn and each cell may serve
    two edges, so the demand halves (rounded up)."""
    need = {}
    for prof in choice:
        for x in prof:
            need[x] = need.get(x, 0) + 1
    if P["twosup"]:
        need = dict((k, -(-v // 2)) for (k, v) in need.items())
    return need


def k4_census_kill(m, du, dv, P):
    """Does every census + profile assignment fail?  Stage one uses the
    support edges alone; stage two additionally places the two SPECIAL
    PARTS -- the parts holding u and v, which are distinct because a
    support edge has one cell per part.  At n = 36 every part holds
    exactly 6 cells (each part is a cover, so |part| >= tau = 6), so a
    special part is its high cell plus five low cells summing to
    m - d.  Stage two is only run where n = 36 is FORCED, which is
    checked, not assumed."""
    cs = censuses(m, 6, [du, dv], P)
    nvals = sorted(set(n for (n, v) in cs))
    profs = support_profiles(m, du, dv, P)
    sp = (special_parts(m, du), special_parts(m, dv))
    survivors1 = []
    for (n, v) in cs:
        cnt = {2: v[0], 3: v[1], 4: v[2], 5: v[3]}
        for choice in itertools.combinations_with_replacement(profs, 4):
            need = demand_of(choice, P)
            if all(need[k] <= cnt.get(k, 0) for k in need):
                survivors1.append((n, v, choice))
                break
    if not survivors1:
        return True, "stage 1 (support-edge demand)", cs, nvals, profs, \
            [], sp
    if nvals != [36]:
        return False, "stage 1 fails and n = 36 is not forced", cs, \
            nvals, profs, survivors1, sp
    spa, spb = sp
    survivors2 = []
    for (n, v, _c) in survivors1:
        cnt = {2: v[0], 3: v[1], 4: v[2], 5: v[3]}
        for pa in spa:
            for pb in spb:
                left = dict(cnt)
                bad = False
                for x in pa + pb:
                    left[x] = left.get(x, 0) - 1
                    if left[x] < 0:
                        bad = True
                if bad:
                    continue
                for choice in itertools.combinations_with_replacement(
                        profs, 4):
                    need = demand_of(choice, P)
                    if all(need[k] <= left.get(k, 0) for k in need):
                        survivors2.append((n, v, pa, pb, choice))
                        break
                if survivors2:
                    break
            if survivors2:
                break
        if survivors2:
            break
    if not survivors2:
        return True, "stage 2 (two special parts)", cs, nvals, profs, \
            survivors1, sp
    return False, "alive", cs, nvals, profs, survivors2, sp


def s2_sweep(P):
    """Every (m, pi) cell of the X = 6 field, with its branches and, for
    (1^6), its K4 census sub-kills."""
    rows = []
    for m in range(22, 27):
        L = Lambda(6, m, P)
        for pi in P6:
            br = s2_branches(m, pi, P)
            top = max(b for (_l, b) in br)
            alive = alive_at(top, L)
            k4 = []
            if pi == (1,) * 6:
                for (du, dv, val, _L) in k4_survivors(m, P):
                    dead, why, cs, nvals, profs, sv, sp = \
                        k4_census_kill(m, du, dv, P)
                    k4.append((du, dv, val, dead, why, cs, nvals, profs,
                               sp))
                    if not dead:
                        alive = True
            rows.append((m, pi, br, top, L, alive, k4))
    return rows


t0 = time.time()
S2 = s2_sweep(P0)
S2TIME = time.time() - t0
S2ALIVE = [(r[0], r[1]) for r in S2 if r[5]]

print("\n      X = 6:  partition  R   B at m = 22..26    max Psi at "
      "m = 22..26      vs Lambda", flush=True)
for pi in P6:
    rowvals = [max(b for (_l, b) in r[2]) for r in S2 if r[1] == pi]
    print("      %-18s %2d  %-18s %-26s  %s"
          % (str(pi), Rof(pi),
             show([budget(pi, c3cap(6, m), P0) for m in range(22, 27)]),
             show(rowvals),
             show([Lambda(6, m, P0) for m in range(22, 27)])), flush=True)
print("      NOTE.  B IS PER RUNG, because c = c3cap(6, m) is 5, 4, 4, 4, 3\n"
      "      and the union bounds switch on with it -- reading one column\n"
      "      for the whole row would not reproduce (3,2,1)'s 38 or\n"
      "      (2,2,1,1)'s 56.  AND THE (1^6) ROW'S PRINTED MAXIMUM IS ITS\n"
      "      KNAPSACK BRANCHES ONLY: its K4 branch reaches %s --\n"
      "      ABOVE Lambda on four of the five rungs -- and is killed by\n"
      "      the census-and-profile count below, not by the floor.  It\n"
      "      is this certificate's thinnest row, not a comfortable one"
      % show(["m=%d: %s" % (r[0], "/".join(str(t[2]) for t in r[6]) or "none")
              for r in S2 if r[1] == (1,) * 6]), flush=True)

check("THE FOUR PURE-KNAPSACK ROWS AT X = 6.  With the cost F, the "
      "value psi, the (LD) budget B = R - q_1(q_1+1) and the key cap "
      "C = X - q_1, the exhaustive maxima are 38 for (3,2,1), 30 for "
      "(3,1,1,1), 56 for (2,2,1,1) and 48 for (2,1,1,1,1) -- against "
      "the smallest floor in the band, Lambda_6(22) = 57.  All four "
      "die on every rung.  NAME THE THIN ONE: (2,2,1,1) clears 56 "
      "against 57, A MARGIN OF ONE UNIT, and it is the first of this "
      "certificate's three one-unit margins",
      [max(b for (_l, b) in r[2]) for r in S2
       if r[0] == 22 and r[1] in ((3, 2, 1), (3, 1, 1, 1), (2, 2, 1, 1),
                                  (2, 1, 1, 1, 1))] == [38, 30, 56, 48]
      and Lambda(6, 22, P0) == 57
      and not any(r[5] for r in S2
                  if r[1] in ((3, 2, 1), (3, 1, 1, 1), (2, 2, 1, 1),
                              (2, 1, 1, 1, 1))),
      "thinnest of the four: (2,2,1,1) at 56 vs 57")
CK_KNAP4 = NCHECK[0]

LD42 = [KN(budget_ld(pi, P0), 6 - pi[0], P0) for pi in ((4, 2), (4, 1, 1))]
check("THE TWO PARTS-4 ROWS, CARRIED AND KILLED.  (4,2) has R = 26, a "
      "(LD) debit of 20 and a key cap C = 2, which admits only d <= 7: "
      "three degree-7 cells at psi 8 give max Psi = 24.  (4,1,1) has "
      "R = 24, the same debit and cap, and two cells give 16.  Both "
      "are far under 57 on the (LD) debit alone, and the union bound "
      "then takes them further down still -- to 8 and 16 -- which the "
      "table above prints.  THE POINT OF CARRYING THEM is billing: "
      "with these rows present the partition enumeration needs only "
      "q <= 4, which 6-partiteness gives for free, so (q3)'s "
      "lambda <= 4 is not spent here or anywhere else in this file",
      LD42 == [24, 16]
      and not any(r[5] for r in S2 if r[1] in ((4, 2), (4, 1, 1)))
      and capcost(2, F) == 7,
      "(LD) alone: (4,2) 24, (4,1,1) 16; with the union bound %s; "
      "both vs 57"
      % show([max(b for (_l, b) in r[2]) for r in S2
              if r[0] == 22 and r[1] in ((4, 2), (4, 1, 1))]))
CK_P4 = NCHECK[0]

check("(3,3) DIES BY ITS UNION.  The two shared sets have four cells "
      "each.  They cannot share an EDGE: an edge in both pairs would "
      "carry x_e >= 3 + 3 = 6, and C3 caps x_e at c = 5, 4, 4, 4, 3 on "
      "m = 22..26.  Being edge-disjoint, they cannot share TWO CELLS "
      "either: two common cells would lie in all four edges, making "
      "all SIX pairs among those edges excessive, and this partition "
      "has two parts.  So |S_1 cap S_2| <= 1, the union is >= 7 cells, "
      "each with qmax >= 3, and J >= 21.  Then (SJ) leaves "
      "P <= 24 - 21 = 3, the cap C = 3 admits d <= 8, and max Psi = "
      "15 -- dead by 42 at the thinnest rung",
      all(Jlb((3, 3), c3cap(6, mm), P0) == 21 for mm in range(22, 27))
      and [max(b for (_l, b) in r[2]) for r in S2 if r[1] == (3, 3)]
      == [15] * 5
      and not any(r[5] for r in S2 if r[1] == (3, 3)),
      "J >= 21, B = 3, max Psi = 15 vs 57..71")
CK_33 = NCHECK[0]

SHARPROWS = [(m, pi, max(b for (_l, b) in r[2]),
              KN(Rof(pi) - max(Jsharp(pi, c3cap(6, m)),
                               pi[0] * (pi[0] + 1)), 6 - pi[0], P0))
             for m in range(22, 27) for pi in P6
             for r in [x for x in S2 if x[0] == m and x[1] == pi]]
SHARPGAIN = [t for t in SHARPROWS if t[3] < t[2]]
note("DERIVED AND THEN NOT IMPOSED -- THE SHARPER UNION BOUND.  Jlb "
     "withdraws entirely as soon as C3 stops forcing edge-disjointness "
     "(q_i + q_j <= c).  It need not: two shared sets meeting in z >= 2 "
     "cells force a CLOSING EDGE whose excess is >= z - 1, so the "
     "partition itself limits how far they can overlap.  That reading "
     "is computed here for all 45 cells and IS NOT IMPOSED anywhere -- "
     "omitting a constraint widens the field, and a wider field can "
     "only make a kill harder, so every kill below holds a fortiori.  "
     "It would tighten %d of the 45 cells -- (2,2,1,1) on all of "
     "m = 22..25, from 56 down to 48, and (3,2,1) at m = 22, from 38 "
     "down to 30.  THAT MATTERS "
     "FOR HONESTY ABOUT MARGINS: this file's first named one-unit "
     "margin exists under the bound this file actually runs, and "
     "evaporates under a bound it declines to run.  Both are stated"
     % len(SHARPGAIN))

check("(2,2,2): THE EXCESS-GRAPH TRICHOTOMY.  Read the three excessive "
      "pairs as edges of a graph on the edges of K.  (a) NOT A "
      "TRIANGLE.  Then |S_i cap S_j| <= 1 for every i, j.  If P_i and "
      "P_j are edge-disjoint, two common cells put all six pairs among "
      "their four edges in excess and the partition has three parts.  "
      "If they SHARE an edge e -- P_i = {e,g}, P_j = {e,h} -- then two "
      "common cells lie in e, g and h, so |g cap h| >= 2 and {g,h} is "
      "a third excessive pair: THE CLOSING EDGE, and the three pairs "
      "are a triangle after all.  So union >= 6, J >= 12, "
      "P <= 18 - 12 = 6, and with C = 4 the maximum is 32.  (b) A "
      "TRIANGLE on {e,f,g}: each triangle edge then carries "
      "x_e = 2 + 2 = 4, so C3 KILLS THE WHOLE BRANCH at m = 26, where "
      "c = 3.  That is the one-line kill and it is carried first",
      [max(b for (_l, b) in r[2]) for r in S2
       if r[1] == (2, 2, 2)][0] == 48
      and [b for (l, b) in [x for x in S2
                            if x[1] == (2, 2, 2) and x[0] == 22][0][2]][0]
      == 32
      and c3cap(6, 26) == 3
      and [l for (l, b) in [x for x in S2
                            if x[1] == (2, 2, 2) and x[0] == 26][0][2]][1]
      .startswith("triangle: C3 kills"),
      "non-triangle max 32; at m = 26 the triangle branch is C3-dead "
      "(x_e = 4 > c = 3)")
CK_222A = NCHECK[0]

TRI3 = []
for m in range(22, 26):
    r = [x for x in S2 if x[0] == m and x[1] == (2, 2, 2)][0]
    TRI3.append((m, r[2][1][1], r[2][2][1], r[4]))
check("(2,2,2) TRIANGLE, m = 22..25, WHERE C3 DOES NOT REACH.  In a "
      "triangle a cell in two shared sets lies in all three edges, so "
      "it lies in the TRIPLE INTERSECTION T; and by (SSC+) a cell in "
      "at most one shared set has s = qmax, hence F(d) <= 0 and "
      "d <= 5.  So every high cell lies in T.  SPLIT BY THE NUMBER OF "
      "HIGH CELLS, NOT BY |T|.  At most two high cells: each has "
      "s = 6, qmax = 2, so F(d) <= 4, d <= 9, psi <= 24 -- at most 48.  "
      "THREE high cells: no outside edge may hold two T-cells (it "
      "would meet e, f and g twice each, adding three excessive pairs "
      "and pushing X to 9), so their stars overlap only in {e,f,g} and "
      "the star-union is 9 + sum f_i; (RG) at k = 3 leaves >= 5 edges "
      "avoiding all of T, so sum f_i <= m - 14.  EVERY f_i >= 1 IN "
      "THIS BRANCH, because a T-cell at f = 0 has d = 5 and is not "
      "high -- that configuration is the <= 2 branch, already bounded "
      "at 48, and letting f_i = 0 in here would compute the other "
      "branch's field under this branch's name.  The per-rung maxima "
      "are 42, 51, 56, 63 against 57, 59, 60, 66; the ROW maximum at "
      "m = 22 is the other branch's 48.  All four dead",
      [t[2] for t in TRI3] == [42, 51, 56, 63]
      and [t[3] for t in TRI3] == [57, 59, 60, 66]
      and all(t[2] < t[3] for t in TRI3)
      and [t[1] for t in TRI3] == [48] * 4,
      show(["m=%d: %d < %d" % (t[0], t[2], t[3]) for t in TRI3]))
CK_222B = NCHECK[0]

MOM26 = 42 * 26 - 10 * 36 + 3 * exc(9)
REQ26 = 26 * 26 + 5 * 26 + 12
check("AND A REDUNDANT TOOTH AT m = 26, by the second moment rather "
      "than by C3.  Identically, sum_v d^2 = 42m - 10n - 2n_3 - 2n_4 "
      "+ sum_{d>=6} (d-2)(d-5) n_d whenever sum_v d = 6m.  In the "
      "triangle branch at m = 26 there are at most three high cells, "
      "each at d <= 9, so sum d^2 <= 42*26 - 360 + 3*28 = 816 against "
      "the 818 the second moment requires -- dropping -2n_3 - 2n_4, "
      "which is the conservative direction.  The C3 kill is PRIMARY "
      "and this is corroboration; two independent routes close the "
      "same branch",
      MOM26 == 816 and REQ26 == 818 and MOM26 < REQ26
      and exc(9) == 28,
      "816 < 818, margin 2")
CK_MOM26 = NCHECK[0]

ONESIX = [x for x in S2 if x[1] == (1,) * 6]
check("(1^6), FIRST BRANCH: NO CELL AT f = 5.  q_1 = 1, so the (LD) "
      "debit is 2 and B = 12 - 2 = 10, while the key cap C = 5 admits "
      "d <= 10.  If no cell reaches d = 10 the cap drops to d <= 9 and "
      "the exhaustive maximum is 56 -- two degree-9 cells at cost 4 "
      "each and a degree-7 cell with the last 2.  56 against 57 is "
      "THE SECOND ONE-UNIT MARGIN of this certificate, and it holds on "
      "every rung of the band",
      [b for (l, b) in ONESIX[0][2]][0] == 56
      and budget((1,) * 6, 5, P0) == 10 and capcost(5, F) == 10
      and Lambda(6, 22, P0) - 56 == 1,
      "56 vs 57 at m = 22; 56 vs %s across the band"
      % show([Lambda(6, m, P0) for m in range(22, 27)]))
CK_16A = NCHECK[0]

check("(1^6), SECOND BRANCH: A CELL u AT f(u) = 5, BUT NO K4.  (SSC+) "
      "gives F(10) + qmax(u) <= s(u), i.e. 5 + 1 <= s(u) <= X = 6, so "
      "s(u) = 6 and u lies in ALL SIX shared sets.  Any other high "
      "cell w then shares each of its own shared sets with u, and "
      "|S_i| = 2 forces S_i = {u,w} for every i in T_w -- so the edges "
      "through both u and w carry ALL the pairs of T_w.  With k such "
      "edges that is C(k,2) pairs, and s(w) = C(k,2), qmax(w) = 1, so "
      "(SSC+) caps F(d(w)) at C(k,2) - 1: k = 2 gives d <= 5 (not "
      "high), k = 3 gives d <= 7, and k >= 5 is impossible since "
      "C(5,2) = 10 > 6.  Without a k = 4 cell every other high cell "
      "sits at d <= 7, and the maximum is 35 + 8 + 8 + 3 = 54",
      [b for (l, b) in ONESIX[0][2]][1] == 54
      and comb(3, 2) - 1 == 2 and capcost(2, F) == 7
      and comb(5, 2) > 6 and comb(4, 2) == 6,
      "35 + 8 + 8 + 3 = 54 vs 57")
CK_16B = NCHECK[0]

K4ROWS = []
for m in range(22, 27):
    K4ROWS.append((m, [(t[0], t[1], t[2]) for t in
                       [x for x in S2 if x[0] == m and x[1] == (1,) * 6][0][6]],
                   Lambda(6, m, P0), m - 13))
print("\n      (1^6), the K4 branch:   m    p <= m-13   Lambda   "
      "arithmetic survivors (d_u, d_v, Psi)", flush=True)
for (m, sv, L, pm) in K4ROWS:
    print("                             %2d      %2d        %3d     %s"
          % (m, pm, L, show(sv) if sv else "none"), flush=True)
check("(1^6), THIRD BRANCH: THE K4.  If some high w has k = 4 then "
      "C(4,2) = 6 exhausts X, so S_i = {u,w} for ALL SIX pairs and "
      "u, w are the ONLY high cells.  A FIFTH edge through {u,w} would "
      "make C(5,2) = 10 excessive pairs and X >= 10 > 6, so exactly "
      "four edges carry the pair; the star-union is then "
      "4 + (d(u)-4) + (d(w)-4) = 6 + p with p = f(u) + f(w).  (RG) at "
      "k = 2 leaves >= 7 edges avoiding both, so 6 + p <= m - 7 and "
      "p <= m - 13.  With both cells capped at d = 10 the arithmetic "
      "survivors are (10,9) at m = 22; (10,9) and (10,10) at m = 23; "
      "(10,10) at m = 24 and 25; and NONE at m = 26, where 70 falls "
      "one unit short of 71 -- THE THIRD ONE-UNIT MARGIN",
      [[(t[0], t[1]) for t in row[1]] for row in K4ROWS]
      == [[(10, 9)], [(10, 9), (10, 10)], [(10, 10)], [(10, 10)], []]
      and Lambda(6, 26, P0) == 71 and psi(10) * 2 == 70,
      "m = 26: 70 vs 71, one unit")
CK_16C = NCHECK[0]

CENSROWS = []
for m in range(22, 27):
    for t in [x for x in S2 if x[0] == m and x[1] == (1,) * 6][0][6]:
        CENSROWS.append((m, t[0], t[1], t[3], t[4], t[6],
                         [v for (n, v) in t[5]], t[7], t[8]))
print("\n      the five survivors, killed by census and profile:", flush=True)
for (m, du, dv, dead, why, nvals, cs, profs, sp) in CENSROWS:
    print("      m=%d (%d,%d)  n in %s  censuses %s" % (m, du, dv,
                                                        show(nvals),
                                                        show(cs)),
          flush=True)
    print("               support profiles %s -> %s by %s"
          % (show([str(p) for p in profs]),
             "DEAD" if dead else "ALIVE", why), flush=True)
NOD2 = [(t[0], t[1], t[2],
         sorted(set(n for (n, v) in censuses(t[0], 6, [t[1], t[2]],
                                             par(n2bump=99)))))
        for t in CENSROWS]
NOD2_MOVE = [t for t in NOD2 if t[3] != [36]]
NOD2_37 = [t for t in NOD2 if 37 in t[3]]
NOD2_38 = [t for t in NOD2 if 38 in t[3]]
check("EVERY K4 SURVIVOR HAS n = 36 FORCED.  n >= 36 because each part "
      "is a cover and tau = 6.  Running the census enumerator with n "
      "FREE, over both moments and 0008's n_2 <= floor(m/2), returns "
      "solutions at n = 36 AND AT NO OTHER n, on all five survivors -- "
      "checked computationally per case, not argued.  THAT IS "
      "(D2) DOING LOAD-BEARING WORK, AND THE PRICE IS COUNTED PER "
      "SURVIVOR RATHER THAN NARRATED: without the n_2 cap the same "
      "enumerator returns solutions above n = 36 on %d of the five -- "
      "n = 37 on %d of them and n = 38 on %d -- and only m = 25 stays "
      "at 36.  With n = 36 every part holds EXACTLY six cells, which "
      "is what licenses the two-special-parts count below"
      % (len(NOD2_MOVE), len(NOD2_37), len(NOD2_38)),
      all(t[5] == [36] for t in CENSROWS)
      and len(CENSROWS) == 5
      and len(NOD2_MOVE) == 4 and len(NOD2_37) == 4 and len(NOD2_38) == 2
      and [t[0] for t in NOD2 if t[3] == [36]] == [25],
      "n-values per survivor: %s; without (D2): %s"
      % (show([str(t[5]) for t in CENSROWS]),
         show(["m=%d (%d,%d): %s" % (t[0], t[1], t[2], t[3])
               for t in NOD2])))
CK_N36 = NCHECK[0]

PROFHI = [support_profiles(t[0], t[1], t[2], P0, hi=6) for t in CENSROWS]
check("THE SUPPORT-EDGE PROFILE LISTS, FROM (S5) AND (D2) TOGETHER.  A "
      "support edge meets the other three support edges in {u,v} and "
      "nothing else, so x_e = 3 and (S5) pins its six degrees at "
      "m + 8; subtracting d(u) + d(v) leaves the four ORDINARY cells "
      "summing to m + 8 - d_u - d_v.  Each is >= 2 by 0005 and <= 5 "
      "because only u and v are high, and (D2) allows AT MOST ONE "
      "degree-2 cell per edge.  That leaves {2,3,3,3} alone at "
      "m = 22 and at m = 23 with (10,10); {3,3,3,3} and {2,3,3,4} at "
      "m = 23 with (10,9) and at m = 24; and {2,3,3,5}, {2,3,4,4}, "
      "{3,3,3,4} at m = 25.  Enumerated, not narrated.  AND THE <= 5 "
      "CEILING IS REPORTED THE WAY THE k = 2 ARM OF (RG) IS -- "
      "MEASURED INERT, WITH THE REASON: recomputing every list at a "
      "ceiling of 6 returns THE SAME LISTS on all five survivors, "
      "because the profiles that would use a degree-6 cell are already "
      "removed by the at-most-one-2 clause of (D2).  The ceiling is "
      "sound and it is not what does the work here",
      PROFHI == [t[7] for t in CENSROWS]
      and [len(t[7]) for t in CENSROWS] == [1, 2, 1, 2, 3]
      and [x for x in CENSROWS if x[0] == 22][0][7] == [(2, 3, 3, 3)]
      and sorted([x for x in CENSROWS
                  if x[0] == 23 and x[2] == 9][0][7]) == [(2, 3, 3, 4),
                                                          (3, 3, 3, 3)],
      show(["m=%d (%d,%d): %s" % (t[0], t[1], t[2],
                                  show([str(p) for p in t[7]]))
            for t in CENSROWS]))
CK_PROF = NCHECK[0]

check("AND EVERY ONE OF THE FIVE SURVIVORS DIES.  No ordinary cell "
      "serves two support edges -- two support edges share exactly "
      "{u,v} at q = 1, and a third common cell would give q >= 2 -- so "
      "the four edges need FOUR DISJOINT copies of their profiles.  "
      "m = 22 needs twelve degree-3 cells against n_3 = 11.  m = 23 "
      "with (10,9) has n_4 = 0 in its only census, which removes the "
      "{2,3,3,4} profile and forces {3,3,3,3}: sixteen degree-3 cells "
      "against n_3 = 9.  m = 24 needs 16 - 2t degree-3 and t degree-4 "
      "cells; only t = 4 gets under the degree-3 supply and it wants "
      "four degree-4 cells where the only census with n_3 >= 8 has "
      "n_4 = 1.  m = 25 needs at least four degree-3 cells against "
      "n_3 <= 3.  m = 23 with (10,10) is the one that needs the SECOND "
      "STAGE: three of its four censuses fail on n_3 < 12 outright, "
      "and (8,13,2,11) dies once the two special parts are placed",
      all(t[3] for t in CENSROWS)
      and [t[4] for t in CENSROWS].count("stage 1 (support-edge demand)")
      == 4
      and [t[4] for t in CENSROWS].count("stage 2 (two special parts)")
      == 1,
      show(["m=%d (%d,%d): %s" % (t[0], t[1], t[2], t[4])
            for t in CENSROWS]))
CK_CENS = NCHECK[0]

SPA = [t for t in CENSROWS if t[0] == 23 and t[2] == 10][0][8][0]
SPPAIRS = []
for a in range(len(SPA)):
    for b in range(a, len(SPA)):
        u2 = sum(1 for x in SPA[a] + SPA[b] if x == 2)
        u3 = sum(1 for x in SPA[a] + SPA[b] if x == 3)
        SPPAIRS.append((SPA[a], SPA[b], 13 - u3, 8 - u2))
check("THE TWO-SPECIAL-PARTS COUNT AT m = 23, (10,10), CENSUS "
      "(8,13,2,11) -- ENUMERATED.  u and v lie in DIFFERENT parts, "
      "since a support edge holds one cell per part.  Each special "
      "part is its degree-10 cell plus five low cells summing to 13, "
      "which allows exactly three profiles: (5,2,2,2,2), (4,3,2,2,2), "
      "(3,3,3,2,2).  The support demand is twelve degree-3 and four "
      "degree-2 cells, ALL of them in the other four parts.  All six "
      "unordered pairs of special profiles are enumerated: every one "
      "leaves either fewer than twelve degree-3 cells or fewer than "
      "four degree-2 cells.  The two extremes say it plainly -- both "
      "parts at (3,3,3,2,2) leaves 7 degree-3 cells, and any "
      "combination keeping 12 of them consumes at least seven of the "
      "eight degree-2 cells.  THE LIST TESTED HERE IS THE ONE THE "
      "STAGE-2 KILL ACTUALLY RAN: it is read back out of the sweep, "
      "not recomputed from literals, so a one-unit error in the "
      "per-part degree sum m - d cannot hide inside the kill",
      SPA == [(2, 2, 2, 2, 5), (2, 2, 2, 3, 4), (2, 2, 3, 3, 3)]
      and all(sum(t) == 23 - 10 and len(t) == 5 for t in SPA)
      and len(SPA) == 3 and len(SPPAIRS) == 6
      and all(t[2] < 12 or t[3] < 4 for t in SPPAIRS)
      and (3, 3, 3, 2, 2) in [tuple(sorted(p, reverse=True)) for p in SPA],
      show(["%s+%s: n3 left %d, n2 left %d"
            % (str(t[0]), str(t[1]), t[2], t[3]) for t in SPPAIRS]))
CK_SP = NCHECK[0]

check("T-A21 ASSEMBLED.  0020 T-A20 puts X >= 6 on every critical core "
      "in [22, 456]; 0020 T-B20 confines X = 6 to m <= 26; this "
      "section empties all 45 (m, partition) cells on m = 22..26.  "
      "Hence X >= 7 FOR EVERY CRITICAL CORE IN THE WINDOW.  Every "
      "conjunct is asserted above; this line says what they add up to, "
      "and section 4's belt then removes the dependence on T-B20 by "
      "emptying X = 6 on m = 27..32 as well",
      S2ALIVE == [] and len(S2) == 45,
      "45 cells, 0 survivors, %.1fs" % S2TIME)
CK_TA = NCHECK[0]

# ==========================================================================
# 4.  T-B21: the staircase, sharpened
# ==========================================================================

head("4.  T-B21 -- X = 7 => m <= 26, X = 8 => m <= 28, X = 9 => m <= 29")


def tri_max(X, m, pi, P):
    """The (2,2,2,*) TRIANGLE branch, when C3 does not exclude it: three
    q = 2 pairs on three edges e, f, g, all three shared sets meeting
    in T = e cap f cap g.  ERRATUM 2026-08-03 (see NOTES): the claim
    "every high cell lies in T" that stood here is FALSE for (2,2,2,1)
    -- a cell of S_4 cap (U \\ T) has s = 2 + 1 = 3, qmax = 2, so
    F <= 1 and d = 6 is possible outside T.  At the rungs THIS file
    runs the branch (c = 4) such cells cannot arise: an S_4 landing in
    U needs the q = 1 pair riding a triangle edge, which then carries
    x_e = 5 > 4 (C3), or forces a fifth excessive pair.  So this
    optimizer's numbers are correct AS RUN HERE; 0022 section 3 proves
    the honest case law, carries the outside-cell branches, and
    measures the corrected maxima equal (62/67/74/83 at m = 24..27).
    |S_4 cap T| <= 1, because two cells of S_4 inside T force a fifth
    excessive pair whether or not the q = 1 pair rides a triangle
    edge.  J >= 2|S_1 u S_2 u S_3| plus one per S_4 cell outside that
    union; the star-union bound of (RG) at k = 3 caps sum f_i at
    m - 9 - rg3.  Exhaustive over |T| and |S_4 cap T|."""
    R = Rof(pi)
    best = 0
    k4 = len(pi) > 3
    for t in range(0, 4):
        U = 9 - 2 * t
        for a in ((0, 1) if k4 else (0,)):
            if a > t:
                continue
            outside = (2 - a) if t == 3 else 0
            J = 2 * U + outside
            Bud = R - J
            if Bud < 0:
                continue
            caps = [(5 if (i == 0 and a == 1) else 4) for i in range(t)]
            lim = m - (9 + P["rg3"])
            for combo in itertools.product(*[range(0, cc + 1)
                                             for cc in caps]):
                if sum(combo) > lim:
                    continue
                if sum(F(x + 5) for x in combo) > Bud:
                    continue
                best = max(best, sum(psi(x + 5) for x in combo))
    return best


def s3_branches(X, m, pi, P):
    """The bounds on Psi for one staircase cell.  Branch 0 is ALWAYS
    the raw (LD) knapsack, so the sieve can be read before any union
    bound; branch 1, when it exists, is the J-debited one, which is a
    bound on the SAME configuration and therefore replaces it.  Any
    further branch is a genuine CASE SPLIT and the cell dies only if
    every case does."""
    c = c3cap(X, m)
    C = X - pi[0]
    raw = KN(budget_ld(pi, P), C, P)
    out = [("raw (LD) knapsack", raw)]
    J = Jlb(pi, c, P)
    if J > pi[0] * (pi[0] + 1):
        out.append(("J >= %d" % J, KN(Rof(pi) - J, C, P)))
    if pi in ((2, 2, 2), (2, 2, 2, 1)):
        if not (P["triexcl"] and c < 4):
            out.append(("triangle live at c = %d" % c, tri_max(X, m, pi, P)))
    return out


def s3_bound(br):
    """The certificate's bound for a cell: within the first case the
    tightest debit governs (branches 0 and 1 bound the same object), and
    across cases the LARGEST governs."""
    first = br[1][1] if len(br) > 1 and br[1][0].startswith("J >=") \
        else br[0][1]
    rest = [b for (l, b) in br if l.startswith("triangle live")]
    return max([first] + rest)


def s3_sweep(P, rungs):
    rows = []
    for (X, m) in rungs:
        c = c3cap(X, m)
        L = Lambda(X, m, P)
        for pi in parts_of(X, min(4, c)):
            br = s3_branches(X, m, pi, P)
            top = s3_bound(br)
            rows.append((X, m, pi, c, L, br, top, alive_at(top, L)))
    return rows


RUNGS5 = [(7, 27), (7, 28), (8, 29), (9, 30), (9, 31)]
t0 = time.time()
S3 = s3_sweep(P0, RUNGS5)
S3TIME = time.time() - t0
S3ALIVE = [r for r in S3 if r[7]]

RAW = [(r[0], r[1], r[2], r[5][0][1]) for r in S3]
RAWALIVE = [t for t in RAW if t[3] >= Lambda(t[0], t[1], P0)]
print("\n      staircase, raw (LD) knapsack survivors, before any union "
      "bound:", flush=True)
for t in RAWALIVE:
    print("      X=%d m=%d %-16s max Psi %3d  vs Lambda %3d"
          % (t[0], t[1], str(t[2]), t[3], Lambda(t[0], t[1], P0)), flush=True)
PFLIN = par(cost=flin)
F8 = KN(budget_ld((1,) * 8, PFLIN), 7, PFLIN)
check("THE RAW SIEVE ON THE FIVE RUNGS.  %d (X, m, partition) cells, "
      "each run through the exhaustive knapsack at cost F with the "
      "(LD) budget and the key cap ALONE, before any union bound.  TEN "
      "SURVIVE the arithmetic: (2,2,2,1) at m = 27 and at m = 28; "
      "(3,3,2), (3,3,1,1), (2,2,2,2) and (2,2,2,1,1) at (8,29); "
      "(3,3,3), (3,3,2,1) and (2,2,2,2,1) at (9,30); and (3,3,3) alone "
      "at (9,31).  Note (1^8) at (8,29): its cap C = 7 admits d = 11, "
      "and the COST-F knapsack gives 96 against 108 -- had the cost "
      "been read as f the cap would have widened to d = 12 and the "
      "same budget would have bought TWO degree-12 cells, reaching "
      "%d against 108 and living, which is M-f's business.  That "
      "number is MEASURED here, not transcribed" % (len(RAW), F8),
      len(RAWALIVE) == 10
      and (7, 27, (2, 2, 2, 1)) in [(t[0], t[1], t[2]) for t in RAWALIVE]
      and (8, 29, (1,) * 8) not in [(t[0], t[1], t[2]) for t in RAWALIVE]
      and [t[3] for t in RAW
           if (t[0], t[1], t[2]) == (8, 29, (1,) * 8)] == [96]
      and F8 == 126 and capcost(7, flin) == 12,
      "%d cells, %d raw survivors; (1^8)@29 = 96 < 108, and %d under "
      "cost f" % (len(RAW), len(RAWALIVE), F8))
CK_RAW = NCHECK[0]

R7 = [r for r in S3 if r[0] == 7 and r[2] == (2, 2, 2, 1)]
check("(7,27) AND (7,28), THE PARTITION (2,2,2,1): THE C3 TRIANGLE "
      "EXCLUSION IS WHERE THE KILL LIVES.  Two q = 2 pairs sharing an "
      "edge would put x_e >= 4 on it, and c = 3 on both rungs -- so "
      "the three q = 2 pairs are PAIRWISE EDGE-DISJOINT, which also "
      "rules out the triangle outright.  Edge-disjointness then gives "
      "|S_i cap S_j| <= 1 by the six-pairs count against four parts, "
      "three 3-cell sets meeting pairwise in at most a point have "
      "union >= 6, every such cell carries qmax >= 2, so J >= 12.  "
      "(SJ) leaves P <= 20 - 12 = 8, the cap C = 5 admits d <= 10, and "
      "the maximum is 50 -- against 83 and 92.  THE EXCLUSION IS NOT "
      "COSMETIC: mutant M-tri withdraws it and the branch climbs to a "
      "TIE with Lambda at 83",
      [r[6] for r in R7] == [50, 50]
      and [r[7] for r in R7] == [False, False]
      and Jlb((2, 2, 2, 1), 3, P0) == 12 and c3cap(7, 27) == 3,
      "J >= 12, B = 8, max Psi = 50 vs 83 and 92")
CK_7 = NCHECK[0]

R8 = [(r[2], r[5][0][1], r[6]) for r in S3 if r[0] == 8]
R8A = [t for t in R8 if t[2] >= Lambda(8, 29, P0)]
check("(8,29): FOUR RAW SURVIVORS, FOUR UNION BOUNDS, ALL DERIVED.  "
      "(3,3,2): the two 4-cell sets give union >= 7 and J >= 21; the "
      "3-cell set of the q = 2 pair meets each of them in at most a "
      "point (q_i + q_j = 5 > 3 = c licenses edge-disjointness), so at "
      "least one of its cells is new and carries qmax >= 2 -- J >= 23. "
      "BOTH READINGS KILL, and this file uses the DERIVED 23: "
      "B = 30 - 23 = 7 gives 43, where 21 would give 59; both are far "
      "under 108.  (3,3,1,1): J >= 21, B = 7, 43.  (2,2,2,2): four "
      "3-cell sets pairwise meeting in <= 1 point need union >= 6 -- "
      "twelve incidences on five cells would force nine coincident "
      "pairs where only six index pairs exist -- so J >= 12, B = 12, "
      "78.  (2,2,2,1,1): the same union, J >= 12, B = 10, 70",
      len(R8A) == 0 and len([r for r in S3 if r[0] == 8 and r[7]]) == 0
      and Jlb((3, 3, 2), 3, P0) == 23 and Jlb((3, 3, 1, 1), 3, P0) == 21
      and Jlb((2, 2, 2, 2), 3, P0) == 12
      and KN(30 - 21, 5, P0) == 59 and KN(30 - 23, 5, P0) == 43,
      "J-debited maxima: %s"
      % show(["%s: %d" % (str(t[0]), t[2]) for t in R8
              if t[0] in ((3, 3, 2), (3, 3, 1, 1), (2, 2, 2, 2),
                          (2, 2, 2, 1, 1))]))
CK_8 = NCHECK[0]

UNIONCHK = []
for u in range(1, 13):
    feas = False
    for mult in itertools.combinations_with_replacement(range(1, 5), u):
        if sum(mult) == 12 and sum(comb(x, 2) for x in mult) <= 6:
            feas = True
    UNIONCHK.append((u, feas))
check("AND THE FOUR-SET UNION BOUND IS ENUMERATED, NOT ASSERTED.  Four "
      "3-cell shared sets, pairwise meeting in at most one cell, place "
      "twelve incidences on the cells of their union; a cell lying in "
      "j of them accounts for C(j,2) index pairs, and there are only "
      "C(4,2) = 6 index pairs in all.  Every multiplicity vector "
      "summing to 12 is enumerated: NO union of five or fewer cells "
      "admits one, and six does -- all multiplicities 2, using all six "
      "index pairs exactly once.  So union >= 6",
      [u for (u, ok) in UNIONCHK if ok][0] == 6
      and all(not ok for (u, ok) in UNIONCHK if u <= 5),
      "smallest admissible union: %d cells"
      % [u for (u, ok) in UNIONCHK if ok][0])
CK_UNION = NCHECK[0]

R9 = [(r[1], r[2], r[5][0][1], r[6], r[4]) for r in S3 if r[0] == 9]
ONEUNIT9 = [t for t in R9 if t[4] - t[2] == 1]
check("(9,30) AND (9,31): THE TWO ONE-UNIT ARITHMETIC CELLS DO NOT "
      "REST ON ONE UNIT.  At m = 31 the raw knapsack kills (3,3,2,1) "
      "at 140 against 141 and (2,2,2,2,1) at 140 against 141 -- one "
      "unit each -- so BOTH ARE KILLED AGAIN BY THEIR GEOMETRY, with "
      "the m = 30 arguments verbatim.  (3,3,3): three 4-cell sets "
      "pairwise meeting in <= 1 point give union >= 9 and J >= 27, so "
      "B = 9 and max Psi = 59.  (3,3,2,1): J >= 23 by the same "
      "reasoning as (8,29)'s (3,3,2), so B = 9 and 59.  (2,2,2,2,1): "
      "four 3-cell sets, union >= 6, J >= 12, B = 14, and the cap "
      "C = 7 admits d = 11 -- the cost-F knapsack gives 96.  Against "
      "123 and 141 every one is dead by 27 or more",
      len([r for r in S3 if r[0] == 9 and r[7]]) == 0
      and len(ONEUNIT9) == 2
      and Jlb((3, 3, 3), 3, P0) == 27 and Jlb((3, 3, 2, 1), 3, P0) == 23
      and KN(36 - 27, 6, P0) == 59 and KN(26 - 12, 7, P0) == 96,
      "one-unit raw cells: %s; after the debit: %s"
      % (show(["(9,%d,%s)" % (t[0], str(t[1])) for t in ONEUNIT9]),
         show(["%d" % t[3] for t in ONEUNIT9])))
CK_9 = NCHECK[0]

BELT = []
for X in (6, 7, 8, 9):
    lo = {6: 27, 7: 27, 8: 29, 9: 30}[X]
    rung = [(X, m) for m in range(lo, CEIL[X] + 1)]
    BELT.extend(s3_sweep(P0, rung))
BELTALIVE = [r for r in BELT if r[7]]
check("THE BELT: EVERY RUNG OF EVERY BAND, UP TO THE C3 CEILING.  0020 "
      "T-B20 already caps X = 6 at m <= 26, X = 7 at 28, X = 8 at 29 "
      "and X = 9 at 31, and this certificate consumes those as claim "
      "rows.  The belt re-derives them: the SAME engine is run on all "
      "%d (X, m, partition) cells from each band's first live rung to "
      "its C3 ceiling -- X = 6 on m = 27..32, X = 7 on 27..34, X = 8 "
      "on 29..35, X = 9 on 30..37 -- and EVERY ONE IS DEAD.  So "
      "T-A21 and T-B21 do not actually lean on T-B20; if it were "
      "withdrawn tomorrow both would survive on this section alone.  "
      "X = 6 on m = 27..32 dies to the raw knapsack with no union "
      "bound at all" % len(BELT),
      BELTALIVE == []
      and len([r for r in BELT if r[0] == 6]) > 0
      and max(r[1] for r in BELT if r[0] == 9) == 37
      and all(max(b for (_l, b) in r[5]) < r[4]
              for r in BELT if r[0] == 6),
      "%d cells across the four bands, 0 survivors" % len(BELT))
CK_BELT = NCHECK[0]

check("T-B21 ASSEMBLED.  Every cell of every rung of every band is "
      "dead: the five rungs this certificate must kill -- (7,27), "
      "(7,28), (8,29), (9,30), (9,31) -- and, by the belt, every rung "
      "above them.  Hence X = 7 forces m <= 26, X = 8 forces m <= 28 "
      "and X = 9 forces m <= 29; equivalently m >= 27 forces X >= 8, "
      "m >= 29 forces X >= 9 and m >= 30 forces X >= 10.  Each of the "
      "three ceilings drops by TWO, ONE and TWO rungs respectively "
      "against 0020's staircase",
      S3ALIVE == [] and len(S3) == 50 and BELTALIVE == [],
      "%d cells on the five rungs, 0 survivors, %.1fs"
      % (len(S3), S3TIME))
CK_TB = NCHECK[0]

PTIE = par(triexcl=False)
TIEBR = s3_branches(7, 27, (2, 2, 2, 1), PTIE)
TIEROW = [r for r in s3_sweep(PTIE, [(7, 27)]) if r[2] == (2, 2, 2, 1)][0]
LTIE = Lambda(7, 27, P0)
check("THE TWO CASE-COMBINATION CONVENTIONS, DRIVEN ON A REAL TIE AND "
      "NOT ONLY INSIDE A MUTANT.  On the certificate's own parameters "
      "no cell ties its floor and no section 3 cell has a live second "
      "case, so both conventions would otherwise be exercised nowhere "
      "at the primary level.  (a) A TIE IS ALIVE.  Both sweeps decide "
      "survival through ONE function, alive_at(top, L) = top >= L; it "
      "returns True at %d = %d and False at %d, and the (7,27) cell "
      "(2,2,2,1) with the C3 triangle exclusion withdrawn comes back "
      "ALIVE at exactly Lambda.  Reading the comparison strictly would "
      "count a tie as dead, which is a FALSE KILL.  (b) ACROSS CASES "
      "THE LARGEST GOVERNS.  That same cell then carries three "
      "readings -- the raw (LD) knapsack at %d, the J-debited bound at "
      "%d which REPLACES it because both bound the same "
      "configuration, and the triangle CASE at %d.  s3_bound returns "
      "%d, the maximum over the genuine case split; taking the minimum "
      "instead would report %d and manufacture a kill the geometry "
      "does not support"
      % (LTIE, LTIE, LTIE - 1, TIEBR[0][1], TIEBR[1][1], TIEBR[2][1],
         s3_bound(TIEBR), TIEBR[1][1]),
      alive_at(LTIE, LTIE) is True and alive_at(LTIE - 1, LTIE) is False
      and [b for (_l, b) in TIEBR] == [94, 50, 83]
      and s3_bound(TIEBR) == 83 and LTIE == 83
      and TIEROW[6] == 83 and TIEROW[7] is True
      and min(b for (_l, b) in TIEBR) == 50,
      "alive_at ties ALIVE; branches %s -> s3_bound %d = Lambda %d"
      % (show([b for (_l, b) in TIEBR]), s3_bound(TIEBR), LTIE))
CK_CONV = NCHECK[0]

# ==========================================================================
# 5.  The mutation suite
# ==========================================================================

head("5.  the mutation suite: nine mutants in ten measured readings")

MUT = []


def cellset(P):
    """The (m, pi) cells of section 3 and the (X, m, pi) cells of the
    five staircase rungs that DIE under P.  A mutant reopens a cell
    when the primary run kills it and the mutant does not."""
    dead = set()
    for r in s2_sweep(P):
        if not r[5]:
            dead.add(("S3", r[0], r[1]))
    for r in s3_sweep(P, RUNGS5):
        if not r[7]:
            dead.add(("S4", r[0], r[1], r[2]))
    return dead


t0 = time.time()
BASE = cellset(P0)
check("THE BASELINE CELL SET.  Every one of section 3's 45 cells and "
      "section 4's 50 cells is dead under the certificate's own "
      "parameters: %d cells in all.  Each mutant below re-runs BOTH "
      "engines end to end and reports the cells that LOSE their kill.  "
      "A mutant that reopens nothing is reported as INERT with the "
      "reason, not quietly dropped" % len(BASE),
      len(BASE) == 95,
      "%d dead cells (45 + 50)" % len(BASE))
CK_BASE = NCHECK[0]

mf = BASE - cellset(PFLIN)
RAWFLIP = [(X, mm, pi)
           for (X, mm) in RUNGS5
           for pi in parts_of(X, min(3, c3cap(X, mm)))
           if KN(budget_ld(pi, P0), X - pi[0], P0) < Lambda(X, mm, P0)
           <= KN(budget_ld(pi, PFLIN), X - pi[0], PFLIN)]
MUT.append(("M-f    cost read as f, not F", str(CK_TAB), len(mf),
            "%d raw-sieve flips, %d survive the union bounds"
            % (len(RAWFLIP), len(mf))))
check("M-f -- THE COST/VALUE CONFUSION, PRICED AT BOTH LAYERS, WHICH "
      "IS WHERE AN EARLIER DESK READING WENT WRONG.  The engine's cost "
      "is F = Phi(.,5) and its value is psi = f(f+2); f is the LINEAR "
      "reading of the same collision count and is smaller from d = 11 "
      "on.  Swap the cost to f and the caps widen (capf(6) = 11, where "
      "capF(6) = 10) and every degree-11 cell gets a unit of budget "
      "back.  AT THE RAW (LD) SIEVE LAYER %d cells flip alive -- AND "
      "THE DESK SPEC'S '15' IS EXACTLY THIS NUMBER AND REPRODUCES "
      "EXACTLY; it was never a mis-transcription, and calling it one "
      "would have been a deflation of a correct count.  AFTER the "
      "union bounds re-kill six of those fifteen, and one further cell "
      "-- (9,30,(2,2,2,2,1)), whose raw 140 already clears "
      "Lambda = 123 -- flips at the J layer instead, %d cells of the "
      "two sweeps lose their kill.  The two sets are not nested and "
      "both are printed.  The flip the spec named reproduces exactly: "
      "(1^7) at (7,27) climbs from 78 to 96 against Lambda 83"
      % (len(RAWFLIP), len(mf)),
      len(RAWFLIP) == 15 and len(mf) == 10
      and ("S4", 7, 27, (1,) * 7) in mf
      and (7, 27, (1,) * 7) in RAWFLIP
      and (9, 30, (2, 2, 2, 2, 1)) not in RAWFLIP
      and ("S4", 9, 30, (2, 2, 2, 2, 1)) in mf
      and sorted(str(t) for t in mf) == [
          "('S4', 7, 27, (1, 1, 1, 1, 1, 1, 1))",
          "('S4', 7, 28, (1, 1, 1, 1, 1, 1, 1))",
          "('S4', 8, 29, (1, 1, 1, 1, 1, 1, 1, 1))",
          "('S4', 9, 30, (1, 1, 1, 1, 1, 1, 1, 1, 1))",
          "('S4', 9, 30, (2, 1, 1, 1, 1, 1, 1, 1))",
          "('S4', 9, 30, (2, 2, 1, 1, 1, 1, 1))",
          "('S4', 9, 30, (2, 2, 2, 1, 1, 1))",
          "('S4', 9, 30, (2, 2, 2, 2, 1))",
          "('S4', 9, 31, (1, 1, 1, 1, 1, 1, 1, 1, 1))",
          "('S4', 9, 31, (2, 2, 2, 1, 1, 1))"]
      and KN(budget((1,) * 7, 3, PFLIN), 6, PFLIN) == 96
      and KN(budget((1,) * 7, 3, P0), 6, P0) == 78
      and capcost(6, flin) == 11 and capcost(6, F) == 10,
      "raw-sieve flips %d: %s; after the union bounds %d reopen: %s"
      % (len(RAWFLIP),
         show(["(%d,%d,%s)" % (t[0], t[1], str(t[2])) for t in RAWFLIP]),
         len(mf), show(sorted(str(t) for t in mf))))
CK_MF2 = NCHECK[0]

PD2 = par(n2bump=1)
md2 = BASE - cellset(PD2)
MUT.append(("M-D2   n_2 cap +1 (Lambda -3)", "%d, %d" % (CK_LAM, CK_N36),
            len(md2), "%d cells reopen" % len(md2)))
check("M-D2 -- 0008 RELAXED BY ONE, AND THIS RUN SETTLES A "
      "DISAGREEMENT.  Raising the cap to n_2 <= floor(m/2) + 1 lowers "
      "Lambda by 3 everywhere AND widens every census.  THREE INTAKE "
      "LANES RETURNED THREE DIFFERENT REOPEN SETS -- nothing at all / "
      "m = 22 and 23 / only the m = 25 zero-margin cell -- so the "
      "answer here is a measurement and the disagreement is recorded "
      "rather than tidied away.  MEASURED, AND THIS IS THE VERDICT: %d "
      "cells reopen -- (1^6) and (2,2,1,1) at m = 22 AND at m = 23, "
      "(2,2,2) at m = 25, and ONE STAIRCASE CELL, "
      "(9, 30, (2,2,2,1,1,1)), which clears the lowered floor at 121 "
      "against 120.  So the second lane was right about m = 22 and 23 "
      "and missed three cells; the third lane was right that m = 25 "
      "moves but named the wrong cell -- the zero-margin cell is "
      "(23, (10,9)) and it does NOT reopen, because its kill is a "
      "counting kill and nothing about Lambda touches it; the first "
      "lane was simply wrong.  (D2) is load-bearing in two distinct "
      "places -- the n_2 term of Lambda and the at-most-one-degree-2 "
      "clause of the support-edge profiles -- and this mutant moves "
      "both at once, which is the honest way to price it"
      % len(md2),
      len(md2) == 6
      and ("S3", 22, (1,) * 6) in md2 and ("S3", 22, (2, 2, 1, 1)) in md2
      and ("S3", 23, (1,) * 6) in md2 and ("S3", 23, (2, 2, 1, 1)) in md2
      and ("S3", 25, (2, 2, 2)) in md2
      and ("S4", 9, 30, (2, 2, 2, 1, 1, 1)) in md2,
      "reopened: %s" % show(sorted(str(t) for t in md2)))
CK_MD2 = NCHECK[0]

mn35 = BASE - cellset(par(nmin=35))
MUT.append(("M-n35  n >= 36 -> n >= 35 (Lambda -15)", str(CK_LAM),
            len(mn35), "%d cells reopen" % len(mn35)))
check("M-n35 -- THE VERTEX FLOOR.  n >= 36 is a two-line consequence "
      "of tau = 6: every part is a cover, so no part has fewer than "
      "six cells.  One block short in one part costs Lambda fifteen "
      "units and %d cells reopen -- including the two the desk spec "
      "named, (2,1,1,1,1) and (2,2,1,1) at X = 6.  This is the "
      "single most expensive constant in the file, which is why it is "
      "spent as the 15n term of an identity rather than as a side "
      "condition" % len(mn35),
      len(mn35) > 10
      and ("S3", 22, (2, 1, 1, 1, 1)) in mn35
      and ("S3", 22, (2, 2, 1, 1)) in mn35,
      "%d cells reopen, at m in %s"
      % (len(mn35),
         show(sorted(set(t[1] for t in mn35 if t[0] == "S3")))))
CK_MN35 = NCHECK[0]

mrg2 = BASE - cellset(par(rg2=6))
mrg2w = BASE - cellset(par(rg2=0))
mrg3 = BASE - cellset(par(rg3=4))
CENS22 = censuses(22, 6, [10, 10], par(rg2=6))
PROF22 = support_profiles(22, 10, 10, par(rg2=6))
MUT.append(("M-RG   |K_U| >= 7 -> 6 at k = 2", str(CK_RG), len(mrg2),
            "INERT (%d reopen) -- (D2) already closes it" % len(mrg2)))
MUT.append(("M-RG'  |K_U| >= 5 -> 4 at k = 3", str(CK_RG), len(mrg3),
            "%d cells reopen" % len(mrg3)))
check("M-RG, BOTH ARMS, AND ONE OF THEM IS NOT LOAD-BEARING -- WHICH "
      "IS A MEASUREMENT AND NOT A DISAPPOINTMENT.  (a) At k = 2 the "
      "bound gives >= 7 edges avoiding {u,v}, hence p <= m - 13.  "
      "Weaken it to 6, and (10,10) DOES become an arithmetic survivor "
      "at m = 22 with FIVE censuses instead of the primary run's one "
      "-- the desk spec's expectation, reproduced exactly.  BUT THE "
      "CELL STILL DIES, AND NOT BY CENSUS: at (22,10,10) a support "
      "edge's four ordinary cells must sum to 10, and EVERY partition "
      "of 10 into four parts >= 2 contains at least two 2s, which "
      "(D2) forbids on one edge -- the profile list is EMPTY, so no "
      "support edge exists at all.  Withdrawing the k = 2 bound "
      "ENTIRELY still reopens %d cells.  (b) At k = 3 the bound gives "
      ">= 5 edges avoiding T, hence sum f_i <= m - 14 in the (2,2,2) "
      "triangle branch.  Weaken it to 4 and the branch reaches 63 at "
      "m = 24 and 72 at m = 25 against 60 and 66: (2,2,2) LIVES on "
      "both rungs, %d cells reopen.  So this file's use of (RG) is "
      "load-bearing at k = 3 and slack at k = 2, and the ledger should "
      "be read that way" % (len(mrg2w), len(mrg3)),
      len(mrg2) == 0 and len(mrg2w) == 0 and len(mrg3) == 2
      and ("S3", 24, (2, 2, 2)) in mrg3 and ("S3", 25, (2, 2, 2)) in mrg3
      and len(CENS22) == 5 and PROF22 == []
      and parts_exact(10, 4, 2, 5) != []
      and all(sum(1 for x in t if x == 2) >= 2
              for t in parts_exact(10, 4, 2, 5)),
      "k=2: %d reopen even when withdrawn entirely (five censuses at "
      "(10,10)@22, but %d legal support profiles); k=3: %s reopen"
      % (len(mrg2w), len(PROF22), show(sorted(str(t) for t in mrg3))))
CK_MRG = NCHECK[0]

mdeb = BASE - cellset(par(debit=False))
MUT.append(("M-debit  (LD) dropped, P <= R kept", str(CK_LD), len(mdeb),
            "%d cells reopen" % len(mdeb)))
check("M-debit -- THE LARGEST-PAIR DEBIT ITSELF.  Drop q_1(q_1+1) and "
      "keep only P <= R, which is what (SG) alone would give with "
      "H = 0.  The four pure-knapsack rows at X = 6 revive at once -- "
      "(3,2,1) climbs from 38 to 98 -- and %d cells reopen across "
      "both sweeps.  The rows that die by a union bound are untouched, "
      "because Jlb already exceeds q_1(q_1+1) there; that split is "
      "exactly the billing this file claims" % len(mdeb),
      len(mdeb) > 0
      and ("S3", 22, (3, 2, 1)) in mdeb
      and KN(Rof((3, 2, 1)), 3, P0) == 98
      and ("S3", 22, (3, 3)) not in mdeb,
      "%d cells reopen; (3,2,1) 38 -> 98; the union-bound rows are "
      "unmoved" % len(mdeb))
CK_MDEB = NCHECK[0]

TRI27 = tri_max(7, 27, (2, 2, 2, 1), P0)
TRI26 = tri_max(7, 26, (2, 2, 2, 1), P0)
mtri = BASE - cellset(par(triexcl=False))
MUT.append(("M-tri  C3 triangle exclusion skipped",
            "%d, %d" % (CK_222A, CK_7), len(mtri),
            "(7,27) ties at 83 = Lambda; %d cells reopen" % len(mtri)))
check("M-tri -- THE C3 TRIANGLE EXCLUSION, AND IT IS THE THINNEST "
      "STRUCTURAL STEP IN THE FILE.  Withdraw the observation that a "
      "triangle of q = 2 pairs puts x_e = 4 on each of its edges and "
      "that c = 3 forbids it, and the (7,27) cell (2,2,2,1) climbs "
      "from 50 to EXACTLY 83 = Lambda_7(27) -- A TIE, so the kill is "
      "LOST, not merely narrowed.  The tying configuration is fully "
      "determined: |T| = 3 with one T-cell also in S_4, giving J >= 7, "
      "B = 13, caps f <= 5, 4, 4 and sum f_i <= 13 from (RG) at "
      "k = 3, hence psi(10) + psi(9) + psi(9) = 35 + 24 + 24 = 83.  "
      "MEASURED, and the same branch at m = 26 gives 74 against 73 -- "
      "one unit, which is the frontier this file leaves open.  %d "
      "cells reopen in all.  AND THE SCOPE IS STATED: M-tri withdraws "
      "the exclusion only where an EXPLICIT triangle branch is carried "
      "-- (2,2,2) and (2,2,2,1) -- while the same C3 step also "
      "licenses Jlb's edge-disjointness on every other multi-2 row, so "
      "%d is a LOWER BOUND on this step's exposure and not its price.  "
      "M-C3disj below withdraws that licence and measures the rest"
      % (len(mtri), len(mtri)),
      TRI27 == 83 and TRI27 == Lambda(7, 27, P0)
      and TRI26 == 74 and Lambda(7, 26, P0) == 73
      and ("S4", 7, 27, (2, 2, 2, 1)) in mtri
      and psi(10) + 2 * psi(9) == 83,
      "(7,27) triangle branch = %d = Lambda; (7,26) = %d vs %d"
      % (TRI27, TRI26, Lambda(7, 26, P0)))
CK_MTRI = NCHECK[0]

mgre = cellset(par(greedy=True)) - BASE
GDIFFCELLS = []
for (X, m) in RUNGS5:
    for pi in parts_of(X, min(3, c3cap(X, m))):
        a = KN(budget(pi, c3cap(X, m), P0), X - pi[0], P0)
        b = KN(budget(pi, c3cap(X, m), par(greedy=True)), X - pi[0],
               par(greedy=True))
        if a != b:
            GDIFFCELLS.append((X, m, pi, a, b))
GSHORT = max(t[3] - t[4] for t in GDIFFCELLS) if GDIFFCELLS else 0
MUT.append(("M-greedy  greedy-at-cap engine", str(CK_GREEDY),
            len(GDIFFCELLS),
            "%d cells understated by up to %d; %d false kills VISIBLE"
            % (len(GDIFFCELLS), GSHORT, len(mgre))))
check("M-greedy -- THE ENGINE CONVENTION, AND IT MUTATES THE WRONG "
      "WAY ON PURPOSE.  Every other mutant here weakens the "
      "certificate; this one would STRENGTHEN it falsely.  "
      "Greedy-at-cap understates the maximum wherever the cap admits "
      "d = 11, and understating a maximum manufactures kills the "
      "lemmas do not support.  MEASURED on the five rungs: %d cells "
      "get a strictly smaller maximum, by up to %d units, every one of "
      "them at q_1 = 1 or 2 where C >= 7.  AND THE HONEST READING OF "
      "WHAT THAT COSTS HERE: %d cells change verdict, because every "
      "cell on these rungs is already dead by a wide margin and no "
      "understatement spans its Lambda.  So no kill in THIS file rests "
      "on the convention -- and the convention is still pinned, "
      "because the shortfall is real and the very next rung out is "
      "where it would start deciding answers"
      % (len(GDIFFCELLS), GSHORT, len(mgre)),
      len(GDIFFCELLS) > 0 and all(t[3] > t[4] for t in GDIFFCELLS)
      and all(t[0] - t[2][0] >= 7 for t in GDIFFCELLS)
      and len(mgre) == 0,
      "understated cells: %s"
      % show(["(%d,%d,%s) %d -> %d" % (t[0], t[1], str(t[2]), t[3], t[4])
              for t in GDIFFCELLS]))
CK_MGRE = NCHECK[0]

m2s = BASE - cellset(par(twosup=True))
D22 = k4_census_kill(22, 10, 9, par(twosup=True))
MUT.append(("M-2sup  ordinary cells may serve two support edges",
            str(CK_CENS), len(m2s),
            "%d cells reopen" % len(m2s)))
check("M-2sup -- THE DISTINCTNESS OF THE SUPPORT-EDGE ORDINARY CELLS.  "
      "Two support edges share exactly {u,v}, at q = 1; a third common "
      "cell would make lambda >= 3 and q >= 2, which (1^6) forbids.  "
      "Withdraw that and each ordinary cell may serve two edges, so "
      "the demand halves: m = 22 needs six degree-3 cells instead of "
      "twelve, against n_3 = 11, and the kill is LOST.  MEASURED: %d "
      "cells reopen -- the (1^6) row at m = 22, 23 and 24.  NOT at "
      "m = 25, although a K4 survivor exists there too: halving the "
      "demand still leaves every legal profile at tot = 13 wanting "
      "more degree-3 cells than n_3 <= 3 supplies, so that cell dies "
      "under the mutant as well.  This is the counting step that the "
      "census lists actually run into, and it is worth a mutant of "
      "its own" % len(m2s),
      len(m2s) == 3 and D22[0] is False
      and sorted(str(t) for t in m2s) == [
          "('S3', 22, (1, 1, 1, 1, 1, 1))",
          "('S3', 23, (1, 1, 1, 1, 1, 1))",
          "('S3', 24, (1, 1, 1, 1, 1, 1))"]
      and k4_census_kill(25, 10, 10, par(twosup=True))[0] is True,
      "%d cells reopen (m = 22, 23, 24); m = 22 (10,9) survives under "
      "the mutant, m = 25 (10,10) still dies" % len(m2s))
CK_M2S = NCHECK[0]

mc3 = BASE - cellset(par(c3disj=False))
MUT.append(("M-C3disj  C3 edge-disjointness licence",
            "%d, %d" % (CK_33, CK_8), len(mc3),
            "%d cells reopen" % len(mc3)))
check("M-C3disj -- 0017's C3 WHERE IT ACTUALLY BITES, AND THE REASON "
      "M-tri's TWO IS A FLOOR AND NOT A PRICE.  Every positive value "
      "Jlb returns is licensed by C3: two shared sets are edge-"
      "disjoint because an edge in both would carry x_e >= q_i + q_j "
      "and C3 caps x_e at c.  Withdraw that licence -- Jlb returns 0, "
      "the conservative reading -- and %d cells lose their kill: all "
      "five (3,3) cells of section 3, whose J >= 21 is exactly this "
      "licence, and every staircase cell that dies by a union bound.  "
      "WHAT SURVIVES THE WITHDRAWAL IS AS INFORMATIVE: the (2,2,2) "
      "row is untouched, because its J >= 12 comes from the "
      "excess-graph TRICHOTOMY, which is valid at any c and needs no "
      "C3 at all.  C3'S THIRD USE IS NOT MUTATED AND IS SAID SO: the "
      "per-rung part bound and the band ceilings define the FIELD "
      "rather than bound a cell, and withdrawing them would enlarge "
      "the partition lists instead of loosening a maximum -- a "
      "different experiment, not run here" % len(mc3),
      len(mc3) == 15
      and all(("S3", mm, (3, 3)) in mc3 for mm in range(22, 27))
      and ("S4", 8, 29, (3, 3, 2)) in mc3
      and ("S3", 22, (2, 2, 2)) not in mc3
      and Jlb((3, 3), 3, par(c3disj=False)) == 0
      and Jlb((3, 3), 3, P0) == 21,
      "%d cells reopen: %s"
      % (len(mc3), show(sorted(str(t) for t in mc3))))
CK_MC3 = NCHECK[0]

MUTTIME = time.time() - t0
print("\n      MUTANT                                     REDDENS            "
      "   COUNT   MEASURED EFFECT", flush=True)
for (nm, wh, n, det) in MUT:
    print("      %-42s %-18s %5d   %s" % (nm, "check " + wh, n, det),
          flush=True)

CITED = [("M-f's table row", CK_TAB, 2),
         ("M-D2's Lambda row", CK_LAM, 6),
         ("M-D2's n = 36 forcing", CK_N36, 34),
         ("M-n35's Lambda row", CK_LAM, 6),
         ("M-RG's (RG) step two", CK_RG, 22),
         ("M-debit's (LD)", CK_LD, 16),
         ("M-tri's trichotomy", CK_222A, 28),
         ("M-tri's (7,27) row", CK_7, 40),
         ("M-greedy's gap measurement", CK_GREEDY, 9),
         ("M-2sup's census kills", CK_CENS, 36),
         ("the key cap's two-case proof", CK_CAP, 7),
         ("the identity's random censuses", CK_ID, 5),
         ("the key-cap enactment's back-reference", CK_CAP, 7),
         ("the (DM)-on-families back-reference", CK_ID, 5),
         ("the margins row's citation of the census kill",
          CK_CENS, 36)]
check("THE MUTATION TABLE IS COMPLETE OVER THE CERTIFICATE'S "
      "PARAMETERS: the cost/value convention (M-f), 0008 in both of "
      "its uses (M-D2), the vertex floor (M-n35), both arms of (RG) "
      "(M-RG, M-RG'), the (LD) debit (M-debit), 0017's C3 in BOTH of "
      "the uses that bound a cell -- the triangle exclusion (M-tri) "
      "and the edge-disjointness licence behind every union bound "
      "(M-C3disj) -- the engine convention in the false-kill "
      "direction (M-greedy) and the support-cell distinctness "
      "(M-2sup).  EVERY COUNT IS A MEASUREMENT MADE IN THIS RUN and "
      "every REDDENS entry is a CAPTURED check number, so a "
      "renumbering reddens this check instead of silently making the "
      "prose wrong.  EIGHT OF THE TEN READINGS REOPEN CELLS.  "
      "M-greedy's count is not a reopen count at all -- it counts "
      "cells whose maximum the greedy engine UNDERSTATES, the "
      "false-kill direction -- and the k = 2 arm of (RG) is flatly "
      "INERT, RECORDED WITH THE REASON rather than quietly dropped: "
      "(D2) empties the support-edge profile list before the weakened "
      "bound can be used.  The census enumerator's leaf "
      "re-verification held across every mutant: %d vectors emitted, "
      "0 internal violations" % LEAVES[0],
      len(MUT) == 10 and all(isinstance(t[2], int) for t in MUT)
      and len([t for t in MUT if t[2] > 0]) == 9
      and len([t for t in MUT if "INERT" in t[3]]) == 1
      and len(mrg2) == 0 and len(mgre) == 0
      and all(got == want for (_n, got, want) in CITED)
      and INTERNAL == [] and LEAVES[0] > 0,
      "%d mutant readings, %d cited check numbers all matching, "
      "%d census vectors, %.1fs"
      % (len(MUT), len(CITED), LEAVES[0], MUTTIME))
CK_MUTTAB = NCHECK[0]

# ==========================================================================
# 6.  Margins
# ==========================================================================

head("6.  the margins, every one named (D-035)")

M1 = Lambda(6, 22, P0) - [max(b for (_l, b) in r[2]) for r in S2
                          if r[0] == 22 and r[1] == (2, 2, 1, 1)][0]
M2 = Lambda(6, 22, P0) - [b for (l, b) in ONESIX[0][2]][0]
M3 = Lambda(6, 26, P0) - 2 * psi(10)
ZERO = [(m, du, dv) for (m, du, dv, dead, why, nv, cs, pr, sp) in CENSROWS
        if psi(du) + psi(dv) == Lambda(6, m, P0)]
S2MARG = sorted((r[4] - r[3], r[0], r[1]) for r in S2)
S3MARG = sorted((r[4] - r[6], r[0], r[1], r[2]) for r in S3)
K4OVER = sorted((psi(du) + psi(dv) - Lambda(6, mm, P0), mm, du, dv)
                for (mm, du, dv, dd, wy, nv, cs, pr, sp) in CENSROWS)
print("""
      X = 6, (2,2,1,1), m = 22..25  56 vs 57, 59, 60, 66 -- ONE UNIT at
                                    m = 22.  (At m = 26 the union bound
                                    is licensed and takes it to 32)
      X = 6, (1^6) with no f = 5    56 vs 57 -- ONE UNIT AT m = 22.  The
                                    BRANCH VALUE 56 holds on every rung;
                                    the MARGIN does not -- it is
                                    1, 3, 4, 10, 15 across the band
      X = 6, (1^6) K4 at m = 26     70 vs 71 -- ONE UNIT, closes the band
      X = 6, (1^6) K4 at m = 23,
              degrees (10,9)        59 vs 59 -- ZERO.  This cell clears
                                    the moment floor EXACTLY and is
                                    killed by census and profile alone
      X = 9, m = 31, (3,3,2,1)      140 vs 141 -- one unit in the raw
              and (2,2,2,2,1)       sieve; both re-killed by geometry at
                                    59 and 96, so neither rests on it
      the f/F cost/value            ONE UNIT at d = 11, where F = 7 and
      convention                    f = 6.  M-f flips %d cells at the raw
                                    sieve, %d of them still open after the
                                    union bounds -- incl. (1^8)@29, which
                                    reads 96 under F and %d under f
      thinnest margin AMONG THE     section 3: %d, at %s
      KNAPSACK BRANCHES             section 4: %d, at %s
      and the (1^6) K4 branch is    it stands ABOVE Lambda on four of the
      NOT in that number            five survivors, by up to %d, and is
                                    killed by counting cells, not by the
                                    floor -- the zero-margin row above is
                                    where that exposure is stated
      the C3 triangle exclusion     M-tri turns the (7,27) kill into a
                                    TIE at 83; at (7,26) it is 74 vs 73.
                                    M-C3disj withdraws the neighbouring
                                    edge-disjointness licence: %d cells
      (D2)                          load-bearing twice; M-D2 reopens 6
                                    cells at m = 22, 23, 25 and one
                                    staircase cell at (9,30)
      n >= 36                       15 units of Lambda; M-n35 prices it
      (RG) at k = 3                 load-bearing (2 cells); at k = 2 it
                                    is measured INERT""" % (
    len(RAWFLIP), len(mf), F8,
    S2MARG[0][0], "(m=%d, %s)" % (S2MARG[0][1], str(S2MARG[0][2])),
    S3MARG[0][0], "(X=%d, m=%d, %s)" % (S3MARG[0][1], S3MARG[0][2],
                                        str(S3MARG[0][3])),
    K4OVER[-1][0], len(mc3)), flush=True)
check("THE MARGINS, NAMED AND MEASURED (D-035).  THREE ONE-UNIT CELLS: "
      "(2,2,1,1) and the no-f = 5 branch of (1^6), both at 56 against "
      "57, and the K4 branch of (1^6) at m = 26, 70 against 71 -- and "
      "that last one is what CLOSES the X = 6 band, so the band's top "
      "rung is decided by a single unit.  ONE ZERO-MARGIN CELL: at "
      "m = 23 the degree pair (10,9) reaches Psi = 59 against "
      "Lambda = 59 exactly -- it clears the moment requirement with "
      "nothing to spare and is killed ONLY by the census-and-profile "
      "count of check %d.  Two further one-unit cells at (9,31) are "
      "re-killed by geometry so that no staircase cell rests on a "
      "single unit.  AMONG THE KNAPSACK BRANCHES the thinnest "
      "surviving margins are %d in section 3 and %d in section 4, both "
      "MEASURED here rather than transcribed -- AND THE K4 BRANCH OF "
      "(1^6) IS DELIBERATELY NOT IN THAT NUMBER, because it is not a "
      "knapsack branch: it stands ABOVE Lambda on four of the five "
      "survivors, by up to %d units, and is killed by counting cells.  "
      "Saying 'after every bound' of a number that excludes the "
      "certificate's most exposed row would be the flattering "
      "direction, so the quantity is named for what it measures.  "
      "This certificate is thinner than 0020, whose thinnest census "
      "margin was 2, and the exposure is stated rather than covered "
      "by a blanket sentence"
      % (CK_CENS, S2MARG[0][0], S3MARG[0][0], K4OVER[-1][0]),
      M1 == 1 and M2 == 1 and M3 == 1
      and ZERO == [(23, 10, 9)]
      and psi(10) + psi(9) == Lambda(6, 23, P0)
      and len(ONEUNIT9) == 2
      and S2MARG[0][0] == 1 and S3MARG[0][0] == 2
      and K4OVER[-1][0] == 11 and K4OVER[-1][1] == 23
      and len([t for t in K4OVER if t[0] > 0]) == 4
      and [Lambda(6, mm, P0) - 56 for mm in range(22, 27)]
      == [1, 3, 4, 10, 15],
      "three one-unit margins (%d, %d, %d), one zero-margin cell %s; "
      "thinnest cells after every bound: %s and %s"
      % (M1, M2, M3, show(ZERO),
         "(m=%d, %s) by %d" % (S2MARG[0][1], str(S2MARG[0][2]),
                               S2MARG[0][0]),
         "(X=%d, m=%d, %s) by %d" % (S3MARG[0][1], S3MARG[0][2],
                                     str(S3MARG[0][3]), S3MARG[0][0])))
CK_MARG = NCHECK[0]

# ==========================================================================
# 7.  Controls
# ==========================================================================

head("7.  controls -- what this certificate must NOT contradict")

check("0020 CONSISTENCY.  0020 proves X >= 6 everywhere and X = 6 => "
      "m <= 26.  This file empties the X = 6 band m = 22..26, so "
      "0020's T-A20 is SUPERSEDED, not contradicted: T-B20 survives as "
      "a true implication whose antecedent no core satisfies.  0020's "
      "own m <= 25 BY-PRODUCT -- measured there, explicitly NOT "
      "claimed, single-route -- is absorbed here by a proof that goes "
      "one rung further and kills m = 26 as well.  What is TESTED is "
      "the emptiness itself, all 45 cells, plus the belt's independent "
      "kill of m = 27..32",
      S2ALIVE == [] and len(S2) == 45
      and all(max(b for (_l, b) in r[5]) < r[4]
              for r in BELT if r[0] == 6),
      "45 cells at X = 6 dead; m = 27..32 dead by knapsack alone")
CK_C20 = NCHECK[0]

PREV = []
for r in s3_sweep(P0, [(7, 26)]):
    sh = KN(Rof(r[2]) - max(Jsharp(r[2], r[3]),
                            r[2][0] * (r[2][0] + 1)), 7 - r[2][0], P0)
    PREV.append((r[2], r[5][0][1], r[6], r[4], sh))
PREV_RAW = [t[0] for t in PREV if t[1] >= t[3]]
PREV_J = [t[0] for t in PREV if t[2] >= t[3]]
PREV_SH = [t[0] for t in PREV if max(t[4], t[2] if t[0] == (2, 2, 2, 1)
                                     else 0) >= t[3]]
check("THE (7,26) FRONTIER, PREVIEWED AS A MEASUREMENT -- AND ONE SPEC "
      "NUMBER THAT DID NOT REPRODUCE.  c = 4 there, so parts <= 4 and "
      "the raw (LD) sieve leaves FOUR shapes alive against "
      "Lambda_7(26) = 73: %s -- exactly as the desk spec pinned them.  "
      "THE J-LAYER IS WHERE THE READINGS PART, AND THE VALUES ARE "
      "PRINTED FROM THE TABLE RATHER THAN NARRATED.  Under THIS FILE'S "
      "conservative Jlb, which withdraws the moment C3 stops forcing "
      "edge-disjointness, (3,3,1) dies at 27 and THREE shapes survive: "
      "%s.  THE SPEC READ THIS RUNG AS TWO SHAPES, with (2,2,2,1) "
      "'alive only through its triangle at one unit'; MEASURED, "
      "(2,2,2,1) is alive at %d -- because 2 + 2 = 4 <= c = 4 "
      "withdraws Jlb's licence entirely, so nothing is debited and the "
      "raw value stands -- which is TWENTY-ONE units clear of 73, not "
      "one.  Under the SHARPER adjacency-aware reading (derived above, "
      "NOT imposed) (2,2,1,1,1) drops to 70 and dies, and TWO shapes "
      "survive: that is the spec's answer, reached by a bound this "
      "file declines to run.  The ONE UNIT is real but belongs to "
      "(2,2,2,1)'s TRIANGLE SUB-BRANCH alone, which reaches 74 against "
      "73, and that is the shape of the frontier.  NOT CLAIMED: this "
      "rung is stated open and the adjacent-but-not-triangle "
      "configurations at c = 4 are not separated here"
      % (show(["%s at %d" % (str(t[0]), t[1]) for t in PREV
               if t[1] >= t[3]]),
         show(["%s at %d" % (str(t[0]), t[2]) for t in PREV
               if t[2] >= t[3]]),
         [t[2] for t in PREV if t[0] == (2, 2, 2, 1)][0]),
      sorted(PREV_RAW) == sorted([(3, 3, 1), (2, 2, 2, 1),
                                  (2, 2, 1, 1, 1), (1,) * 7])
      and sorted(PREV_J) == sorted([(2, 2, 2, 1), (2, 2, 1, 1, 1),
                                    (1,) * 7])
      and sorted(PREV_SH) == sorted([(2, 2, 2, 1), (1,) * 7])
      and [t[2] for t in PREV if t[0] == (2, 2, 2, 1)] == [94]
      and [t[2] for t in PREV if t[0] == (2, 2, 1, 1, 1)] == [78]
      and [t[2] for t in PREV if t[0] == (1,) * 7] == [78]
      and [t[1] for t in PREV if t[0] == (3, 3, 1)] == [80]
      and [t[2] for t in PREV if t[0] == (3, 3, 1)] == [27]
      and Jlb((2, 2, 2, 1), 4, P0) == 0
      and tri_max(7, 26, (2, 2, 2, 1), P0) == 74
      and Lambda(7, 26, P0) == 73 and c3cap(7, 26) == 4
      and [t[4] for t in PREV if t[0] == (2, 2, 1, 1, 1)] == [70],
      "raw: %s; this file's J-layer: %s; sharper reading: %s"
      % (show([str(p) for p in PREV_RAW]),
         show([str(p) for p in PREV_J]),
         show([str(p) for p in PREV_SH])))
CK_PREV = NCHECK[0]

AG5 = ag(5)
agX = sum(lam(p, g) - 1 for p, g in itertools.combinations(AG5, 2))
check("NO TENSION WITH THE TIGHTNESS OBJECT.  AG(2,5) has m = 25 and "
      "X = 0, which would violate X >= 7 if it were a core in the "
      "window.  It is not: tau = 5, and the window's quantifier is "
      "over cores with tau = 6.  The distinction is not cosmetic -- "
      "AG(2,5) is exactly where the summed laws are tight, so a "
      "certificate that quietly admitted it would be proving a false "
      "statement",
      mincover(AG5) == 5 and len(AG5) == 25 and agX == 0 and 5 < 6)

check("AND THE CENSUS ENUMERATOR'S LEAF RE-VERIFICATION HELD "
      "THROUGHOUT.  Every vector the enumerator emits -- in section 3, "
      "in the controls, and inside every mutant that re-runs either "
      "sweep -- is re-checked from scratch against all four "
      "constraints (both moments, n >= nmin, n_2 <= the cap) before it "
      "leaves the loop, and any violation is recorded into a list "
      "rather than raised by a bare assert, which -O strips.  %d "
      "vectors emitted, %d violations" % (LEAVES[0], len(INTERNAL)),
      INTERNAL == [] and LEAVES[0] > 0,
      "%d census vectors, 0 internal violations" % LEAVES[0])

CAPTURED = [("CK_TAB", CK_TAB, 2), ("CK_DM", CK_DM, 3),
            ("CK_MF", CK_MF, 4), ("CK_ID", CK_ID, 5),
            ("CK_LAM", CK_LAM, 6), ("CK_CAP", CK_CAP, 7),
            ("CK_XENG", CK_XENG, 8), ("CK_GREEDY", CK_GREEDY, 9),
            ("CK_C3", CK_C3, 10), ("CK_CORP", CK_CORP, 11),
            ("CK_MOM", CK_MOM, 12), ("CK_STAR", CK_STAR, 13),
            ("CK_SJ", CK_SJ, 14), ("CK_UNIV", CK_UNIV, 15),
            ("CK_LD", CK_LD, 16), ("CK_JHIGH", CK_JHIGH, 17),
            ("CK_EQ", CK_EQ, 18), ("CK_KEY", CK_KEY, 19),
            ("CK_S5", CK_S5, 20), ("CK_RGC", CK_RGC, 21),
            ("CK_RG", CK_RG, 22), ("CK_DMFAM", CK_DMFAM, 23),
            ("CK_NINE", CK_NINE, 24), ("CK_KNAP4", CK_KNAP4, 25),
            ("CK_P4", CK_P4, 26), ("CK_33", CK_33, 27),
            ("CK_222A", CK_222A, 28), ("CK_222B", CK_222B, 29),
            ("CK_MOM26", CK_MOM26, 30), ("CK_16A", CK_16A, 31),
            ("CK_16B", CK_16B, 32), ("CK_16C", CK_16C, 33),
            ("CK_N36", CK_N36, 34), ("CK_PROF", CK_PROF, 35),
            ("CK_CENS", CK_CENS, 36), ("CK_SP", CK_SP, 37),
            ("CK_TA", CK_TA, 38), ("CK_RAW", CK_RAW, 39),
            ("CK_7", CK_7, 40), ("CK_8", CK_8, 41),
            ("CK_UNION", CK_UNION, 42), ("CK_9", CK_9, 43),
            ("CK_BELT", CK_BELT, 44), ("CK_TB", CK_TB, 45),
            ("CK_CONV", CK_CONV, 46), ("CK_BASE", CK_BASE, 47),
            ("CK_MF2", CK_MF2, 48), ("CK_MD2", CK_MD2, 49),
            ("CK_MN35", CK_MN35, 50), ("CK_MRG", CK_MRG, 51),
            ("CK_MDEB", CK_MDEB, 52), ("CK_MTRI", CK_MTRI, 53),
            ("CK_MGRE", CK_MGRE, 54), ("CK_M2S", CK_M2S, 55),
            ("CK_MC3", CK_MC3, 56), ("CK_MUTTAB", CK_MUTTAB, 57),
            ("CK_MARG", CK_MARG, 58), ("CK_C20", CK_C20, 59),
            ("CK_PREV", CK_PREV, 60)]
check("EVERY CAPTURED CHECK NUMBER IS PINNED, NOT ONLY THE %d THE "
      "PROSE CITES.  Each `CK_* = NCHECK[0]` line binds a name to the "
      "number this run assigned to the check just printed, and every "
      "one of those %d bindings is asserted here against a literal.  "
      "That closes the gap the anti-drift device otherwise leaves: "
      "without this, a capture that no check reads is a variable that "
      "cannot fail, and a table saying 'every REDDENS entry is a "
      "captured check number' would advertise more coverage than "
      "exists.  The numbers are also checked to be distinct and "
      "strictly increasing in source order, and the four checks that "
      "carry no capture are named: %s -- the harness canary, the "
      "AG(2,5) control, the leaf re-verification and this check "
      "itself, none of which is cited by number anywhere"
      % (len(CITED), len(CAPTURED),
         show(sorted(set(range(1, NCHECK[0] + 2))
                     - set(t[1] for t in CAPTURED)))),
      all(got == want for (_n, got, want) in CAPTURED)
      and len(set(t[1] for t in CAPTURED)) == len(CAPTURED)
      and [t[1] for t in CAPTURED] == sorted(t[1] for t in CAPTURED)
      and sorted(set(range(1, NCHECK[0] + 2))
                 - set(t[1] for t in CAPTURED)) == [1, 61, 62, 63]
      and len(CAPTURED) == 59,
      "%d captures, all matching; uncaptured checks: %s"
      % (len(CAPTURED),
         show(sorted(set(range(1, NCHECK[0] + 2))
                     - set(t[1] for t in CAPTURED)))))

note("STATED, NOT CLAIMED -- THE BANKED LEADS.  One unaudited lane "
     "reported that a GUARDED engine (imposing the (SSC+) ceiling "
     "F(d) + qmax <= X at every high vertex simultaneously with the "
     "key cap) yields bonus rungs: X = 9 => m <= 28, X = 10 and 11 => "
     "m <= 29, X = 12 => m <= 31.  Single-lane, unaudited, and NOT "
     "re-derived here.  They are named so they are not lost and are "
     "claimed nowhere")
note("STATED, NOT TESTED -- WHAT REMAINS OPEN.  X = 7 on m in [22, 26] "
     "is NOT emptied: this certificate confines X = 7 to those five "
     "rungs and stops, exactly as 0020 stopped one rung of excess "
     "lower.  The preview above measures THREE shapes alive at m = 26 "
     "under this file's own Jlb -- (2,2,2,1) at 94, (2,2,1,1,1) at 78 "
     "and (1^7) at 78 against 73 -- and two under the sharper bound it "
     "declines to impose; the single unit belongs to (2,2,2,1)'s "
     "triangle sub-branch, 74 against 73.  Nothing here bears on X >= 10 "
     "below m = 30, on existence, or on the far end of the window, "
     "which is 0020's (Q0) business and is untouched")
note("STATED, NOT TESTED: certificates 0018, 0019 and 0020 remain the "
     "authorities for their own theorems.  This file consumes four of "
     "0020's rows and re-derives everything else it uses; it does not "
     "re-run their censuses and does not supersede their statements, "
     "only their bands")

# ==========================================================================

head("Result")

print("""
  (SJ)   P + J <= R, J over ALL vertices               PROVEN-BY-CERT
  (LD)   P <= R - q_1(q_1+1)                           PROVEN-BY-CERT
  (DM)   d^2 <= 8d - 15 + 3[d=2] + psi(d), d >= 2      PROVEN-BY-CERT
         summed: Psi = m^2-43m+2X+15n-3n_2+n_4         PROVEN-BY-CERT
  (RG)   tau(K_U) >= 6-k, |K_U| >= 2(6-k)-1            PROVEN-BY-CERT
  (S5)   sum_{z in e} d(z) = m + 5 + x_e               PROVEN-BY-CERT
  (T-A21) X >= 7 for every critical core in [22, 456]  PROVEN-BY-CERT
  (T-B21) X = 7 => m <= 26; 8 => 28; 9 => 29           PROVEN-BY-CERT

  One line does the work, and 0020 had already written it.  Summing
  (SSC+) gives P + J <= R with J the sum of qmax over EVERY vertex;
  0020 kept only J >= H and threw the rest away.  Keeping J gives the
  largest-pair debit for free, and the debit plus a moment inequality
  that is an identity at every degree above four turn each cell of the
  field into a single integer knapsack -- cost F, value psi, and those
  are different functions.  Nine partitions empty X = 6 across five
  rungs; five surviving degree pairs die to a census and a profile
  count; the staircase drops two rungs, one rung and two rungs.

  THE MARGINS: three cells decided by one unit, one by none at all --
  (10,9) at m = 23 clears the moment floor at exactly 59 = 59 and is
  killed only by counting cells.  The structural exposure is the C3
  triangle exclusion, which M-tri turns into a tie.  Three numbers in
  the desk spec did not reproduce and the measurements are what stand.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(exit_code(FAILED))
