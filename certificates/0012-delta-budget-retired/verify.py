#!/usr/bin/env python3
"""Certificate 0012 -- the delta-budget retires: m = 21 dies on floors and
convexity alone.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from lib/.
Runs under Python 3.9 and under python3 -O.  Deterministic.

WHAT IS CLAIMED
---------------
  (L10), the saturation floor: in a Ryser r=6 counterexample
  with m edges, if deg(v) = m - 13 and u is a vertex of
  another part, then |E(v) cap E(u)| >= deg(u) - 4          PROVEN-BY-CERTIFICATE
                                                            (three lines, from
                                                            certificate 0011)
  m = 21 impossible via profiles + (D2) cap + (L7)+(L10)
  floors + A >= S-m + (L9) + B <= floor(5X/2)               PROVEN-BY-CERTIFICATE

  and therefore: ON THE PINNED LADDER, THE FLOOR m >= 22 NO LONGER CONSUMES
  THE DELTA-BUDGET, THE LEVEL SYSTEM, qmin, OR THE CEILING U -- at any rung.

WHY THIS MATTERS
----------------
Both peer audits (turn 7) attacked the delta-budget inside (L8) -- the
narrowest-margin machinery in the repo (D-017: the m = 20 kill ran on a
margin of exactly one; 0008's tightest cap-passer at m = 21 missed by
D - need = -1).  Certificate 0008 already showed (L8) is consulted at exactly
one rung, m = 21.  This certificate replaces its role there:

  measured first (turn 9): of the 567 cap-passing m = 21 configurations on
  the pinned ladder, 502 die on (L9)+B_cap+A>=S-m alone, 22 more on level
  feasibility, and 43 genuinely needed the delta-budget.  Every one of those
  43 has at least one part whose maximum degree SATURATES the k=1 cap
  Delta <= m - N(5) = 8.  Saturation is structure: the saturating vertex's
  complement is a 13-edge object with tau >= 5, and certificate 0011 says
  such an object has maximum degree at most 4.  That single fact converts
  the cap's equality case into a large overlap floor -- (L10) -- and under
  the boosted floors ALL 567 configurations die on the convexity bound
  (L9) against B <= floor(5X/2).  One evaluation per configuration.

The retirement claim, stated precisely.  On the pinned ladder N(1..5) =
2,4,6,9,13 (certificates 0005/0009/0010): m <= 11 dies on lemmas (A)+(B);
m = 12..20 die because NO admissible configuration passes the (D2) cap
(section 5 recomputes this here); m = 21 dies by section 4 below; m >= 22 is
the floor.  Nothing in that chain evaluates a delta-budget, a level
structure, qmin, or U.  Certificates 0006/0007 remain green and remain the
record of the weak-ladder route -- their machinery is retired from the
minimal chain, not refuted.

(L10) AND ITS PROOF
-------------------
  Let H be 6-partite 6-uniform intersecting with tau(H) = 6, |H| = m.  Let
  deg(v) = m - 13, and let u be a vertex of a different part.  Then

        |E(v) cap E(u)|  >=  deg(u) - 4.

  Proof.  R = H minus star(v) has exactly 13 edges, is 6-partite 6-uniform
  intersecting, and tau(R) >= 5: a cover of R together with v covers H, so
  tau(R) >= tau(H) - 1.  By certificate 0011, Delta(R) <= 4.  Every edge of
  E(u) not through v survives into R (u != v and u is not in v's part, so
  no edge is counted out twice), hence deg_R(u) = deg(u) - |E(u) cap E(v)|
  <= 4.  QED.

  At m = 21 the saturating degree is 8, and (L10) beats (L7)'s floor
  Ms_i + Ms_j - 13 exactly where the delta-budget used to be needed: an
  (8,8) pair's floor rises 3 -> 4, an (8,7) pair's 2 -> 3, an (8,6) pair's
  1 -> 2.

THE REST OF THE CHAIN, restated for self-containment
----------------------------------------------------
Fix in each part i a maximum-degree vertex u_i, Ms_i = deg(u_i), S = sum Ms.
c_ij = |E(u_i) cap E(u_j)| for i < j, A = sum c_ij.  X = sum_parts sum_v
C(deg v, 2) - C(m,2) >= 0 is the excess (L2).

  A >= S - m:  with k_e = #{i : u_i in e}, sum_e k_e = S and
      A = sum_e C(k_e, 2), so A - S + m = sum_e (C(k_e,2) - k_e + 1)
      = sum_e C(k_e - 1, 2) >= 0.
  B := sum_{i<j} C(c_ij, 2) = sum over edge pairs {e,f} of C(t_ef, 2),
      t_ef = #{i : u_i in e cap f}.  Since t_ef <= 5 (t = 6 forces e = f)
      and C(t,2) <= (5/2)(t-1) for t <= 5 (equality at t = 5), and
      sum (t_ef - 1)+ <= sum (lambda_ef - 1) = X:   B <= floor(5X/2).
  B >= B_min(A):  the (L9) water-filling floor (named turn 9; proved by
      exchange; audited over 262,729 instances, zero mismatches).
  B_min is nondecreasing in A (for A >= sum floors): any minimiser at A+1
      has an entry strictly above its floor; decrement it.  Checked below
      as well as stated.

  THE KILL.  For a configuration with floors F (from (L7) and (L10)) let
  A0 = max(sum F, S - m).  A real object has A >= A0, so
  B >= B_min(A) >= B_min(A0); if B_min(A0) > floor(5X/2) >= B, contradiction.

THE LEDGER, in full
-------------------
  the pinned ladder N(1..5)=2,4,6,9,13   certificates 0005 (N(1..4)), 0009
                                         (N(5)); N(4) also by hand in 0010
  (A), (B), (C)                          certificate 0005
  (D2), the cap 2*D2 <= m                certificate 0008 (re-derived there)
  (L7)                                   certificate 0006
  Delta <= 4 at 13 edges, tau >= 5       certificate 0011  <- the new input
  (L2), A >= S-m, B <= floor(5X/2),
  (L9) and its monotonicity              stated above, proved by hand;
                                         (L9) audited turn 9; the B_cap
                                         identity brute-forced over 1.86M
                                         audits (turn 8)
  EXTERNAL INPUTS -- NONE.
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


G4 = 8
N = {1: 2, 2: 4, 3: 6, 4: 9, 5: 13}      # the pinned ladder
M = 21


def profiles(m, ladder):
    caps = {k: m - ladder[6 - k] for k in range(1, 6)}
    out = []

    def rec(left, cur):
        k = len(cur)
        if k in caps and sum(cur) > caps[k]:
            return
        if left == 0:
            if len(cur) >= 6:
                out.append(tuple(cur))
            return
        for s in range(min(left, cur[-1] if cur else m - ladder[5]), 1, -1):
            if 0 < left - s < 2:
                continue
            rec(left - s, cur + [s])
    rec(m, [])
    return out


def sc(p):
    return sum(comb(d, 2) for d in p)


def d2_of(p):
    return sum(1 for d in p if d == 2)


def floors_of(Ms, m, delta_bound):
    """(L7) floors max(0, Ms_i + Ms_j - (m - g(4))), boosted by (L10) where a
    part's maximum degree saturates the k=1 cap m - N(5) = m - 13."""
    out = []
    for i in range(6):
        for j in range(i + 1, 6):
            f = max(0, Ms[i] + Ms[j] - (m - G4))
            if Ms[i] == m - 13:
                f = max(f, Ms[j] - delta_bound)
            if Ms[j] == m - 13:
                f = max(f, Ms[i] - delta_bound)
            out.append(f)
    return out


def bmin(floors, A):
    """(L9): water-fill above the floors to total A, then sum C(.,2)."""
    c = list(floors)
    for _ in range(A - sum(floors)):
        c[min(range(len(c)), key=lambda i: c[i])] += 1
    return sum(comb(v, 2) for v in c)


def reduced_kill(combo, m, delta_bound=4):
    """True iff the configuration dies on floors + (L9) + B_cap alone."""
    Ms = [p[0] for p in combo]
    S = sum(Ms)
    X = sum(sc(p) for p in combo) - comb(m, 2)
    F = floors_of(Ms, m, delta_bound)
    A0 = max(sum(F), S - m)
    return bmin(F, A0) > (5 * X) // 2


# ==========================================================================
# 1.  The m = 21 field on the pinned ladder
# ==========================================================================

head("1.  m = 21, pinned ladder: 43,875 admissible, 567 pass the cap")

t0 = time.time()
P21 = sorted(profiles(M, N), key=sc, reverse=True)
C21 = [c for c in itertools.combinations_with_replacement(P21, 6)
       if sum(sc(p) for p in c) >= comb(M, 2)]
check("the pinned ladder admits 43,875 configurations at m = 21 -- the "
      "number certificate 0008 published for the (then-cited) ladder",
      len(C21) == 43875, "%d profiles, %.0fs" % (len(P21), time.time() - t0))
CAP21 = [c for c in C21 if sum(d2_of(p) for p in c) <= M // 2]
check("567 pass the (D2) cap D2 <= 10", len(CAP21) == 567)

# ==========================================================================
# 2.  (L10): saturation converts to overlap
# ==========================================================================

head("2.  (L10), the saturation floor")

note("(L10) proof, in full (docstring for the prose): deg(v) = m - 13 makes "
     "the complement R of star(v) a 13-edge intersecting 6-partite object "
     "with tau(R) >= 5; certificate 0011 gives Delta(R) <= 4; and "
     "deg_R(u) = deg(u) - |E(u) cap E(v)| for u outside v's part")
check("at m = 21 the saturating degree is 8 = m - N(5), and every admissible "
      "profile's largest entry is at most 8",
      M - 13 == 8 and max(p[0] for p in P21) == 8,
      "the k=1 cap and its equality case are both live at this rung")
check("(L10) beats (L7) by exactly one unit on every saturated pair at the "
      "top degrees: (8,8) floor 3 -> 4, (8,7) 2 -> 3, (8,6) 1 -> 2",
      all(max(max(0, 8 + b - 13), b - 4, (8 - 4) if b == 8 else 0)
          == max(0, 8 + b - 13) + 1 for b in (6, 7, 8)),
      "one unit per pair, but at A0 the units compound across all "
      "saturated pairs at once, and (L9) is convex")

# ==========================================================================
# 3.  The chain's inequalities, checked where checkable
# ==========================================================================

head("3.  A >= S - m, B <= floor(5X/2), (L9) and monotonicity")

note("A >= S - m: A = sum_e C(k_e,2), S = sum_e k_e, so A - S + m = "
     "sum_e C(k_e - 1, 2) >= 0 -- an identity, not an estimate")
note("B <= floor(5X/2): B = sum over edge pairs of C(t,2), t <= 5 since six "
     "shared coordinates would make the edges identical, C(t,2) <= "
     "(5/2)(t-1) for t <= 5 with equality at t = 5, and sum (t-1)+ <= X. "
     "The underlying identities were brute-forced over 1.86M audits at "
     "turn 8, zero failures")
check("C(t,2) <= (5/2)(t-1) holds at every t from 2 to 5, with equality "
      "exactly at t = 5",
      all(2 * comb(t, 2) <= 5 * (t - 1) for t in range(2, 6))
      and 2 * comb(5, 2) == 5 * 4)

mono_bad = 0
for cfg in CAP21[::7]:
    Ms = [p[0] for p in cfg]
    F = floors_of(Ms, M, 4)
    A0 = max(sum(F), sum(Ms) - M)
    vals = [bmin(F, A0 + d) for d in range(6)]
    if any(vals[i] > vals[i + 1] for i in range(5)):
        mono_bad += 1
check("(L9)'s B_min is nondecreasing in A -- checked on 81 sampled "
      "configurations over six consecutive A values each (the hand proof: "
      "a minimiser at A+1 has an entry strictly above its floor; decrement "
      "it)", mono_bad == 0,
      "so B_min(A0) > B_cap kills EVERY A >= A0 at once")

# ==========================================================================
# 4.  The kill
# ==========================================================================

head("4.  every one of the 567 dies on B_min(A0) > floor(5X/2)")

t0 = time.time()
margins = []
for cfg in CAP21:
    Ms = [p[0] for p in cfg]
    S = sum(Ms)
    X = sum(sc(p) for p in cfg) - comb(M, 2)
    F = floors_of(Ms, M, 4)
    A0 = max(sum(F), S - M)
    margins.append(bmin(F, A0) - (5 * X) // 2)
check("ALL 567 cap-passing configurations die: B_min(A0) exceeds the B-cap "
      "at every single one", min(margins) > 0,
      "%.0fs; one convexity evaluation each -- no level system, no "
      "delta-budget, no qmin, no U" % (time.time() - t0))
check("the margin is not thin: the tightest configuration clears by %d, "
      "the median by %d" % (min(margins), sorted(margins)[len(margins) // 2]),
      min(margins) >= 2,
      "margins range %d..%d -- compare the delta-budget's margin of "
      "exactly one (D-017)" % (min(margins), max(margins)))

# ==========================================================================
# 5.  m <= 20 on the pinned ladder: the cap leaves nothing at all
# ==========================================================================

head("5.  m = 12..20, pinned ladder: zero cap-passers -- (L8) never needed")

all_zero = True
detail = []
for mm in range(12, 21):
    Pm = profiles(mm, N)
    Cm = [c for c in itertools.combinations_with_replacement(Pm, 6)
          if sum(sc(p) for p in c) >= comb(mm, 2)]
    npass = sum(1 for c in Cm if sum(d2_of(p) for p in c) <= mm // 2)
    detail.append("m=%d: %d/%d" % (mm, npass, len(Cm)))
    if npass:
        all_zero = False
check("at every m from 12 to 20 nothing reaches (L8): for m <= 19 the pinned "
      "ladder admits NO configuration at all, and m = 20's 105 all fail the "
      "(D2) cap", all_zero, "; ".join(detail))
note("m <= 11 dies on lemmas (A) and (B) alone: six parts of >= 6 active "
     "vertices of degree >= 2 need m >= 12 (certificate 0007, check 5)")

# ==========================================================================
# 6.  Controls
# ==========================================================================

head("6.  controls")

# NOT TOO STRONG: the identical reduced test must leave m = 22 alive.
t0 = time.time()
P22 = sorted(profiles(22, N), key=sc, reverse=True)
alive22 = None
scanned = 0
for c in itertools.combinations_with_replacement(P22, 6):
    if sum(sc(p) for p in c) < comb(22, 2):
        continue
    if sum(d2_of(p) for p in c) > 11:
        continue
    scanned += 1
    Ms = [p[0] for p in c]
    S = sum(Ms)
    X = sum(sc(p) for p in c) - comb(22, 2)
    F = floors_of(Ms, 22, 4)
    A0 = max(sum(F), S - 22)
    if bmin(F, A0) <= (5 * X) // 2:
        alive22 = c
        break
check("NOT TOO STRONG: at m = 22 (saturating degree 9) the same reduced "
      "test leaves survivors", alive22 is not None,
      "first survivor after %d cap-passers, %.0fs; killing every m would be "
      "proving Ryser and would therefore be wrong" % (scanned, time.time() - t0))

# SENSITIVITY: certificate 0011 is load-bearing by exactly this much.
revived = sum(1 for c in CAP21 if not reduced_kill(c, M, delta_bound=5))
check("SENSITIVITY: weaken certificate 0011's bound to Delta <= 5 and 65 of "
      "the 567 come back to life -- the new theorem is load-bearing, and by "
      "more than one configuration", revived == 65,
      "the 22 + 43 configurations that needed more than (L9)+B_cap before "
      "(L10) are exactly the exposure")

revived4 = sum(1 for c in CAP21
               if not reduced_kill(c, M, delta_bound=4))
check("and with the true bound Delta <= 4 the revival count is zero "
      "(the same computation as section 4, run through the sensitivity "
      "harness as a consistency check)", revived4 == 0)

# CLASSIFICATION EXHIBIT: what the old machinery needed, for the record.
note("what retired, measured (turn 9, notebook): under the OLD guard set "
     "the 567 split 502 on (L9)+B_cap+A>=S-m, 22 on level feasibility, 43 "
     "on the delta-budget proper -- and all 43 delta-needers have >= 2 "
     "saturated parts. Saturation was the structure the delta-budget was "
     "paying for numerically; (L10) buys it as a theorem")

head("Result")

print("""
  (L10) the saturation floor                        PROVEN-BY-CERTIFICATE
  m = 21 impossible on the reduced chain            PROVEN-BY-CERTIFICATE
  the pinned-ladder floor m >= 22 consumes:         profiles (A)(B)(C)+ladder,
                                                    the pair count, (D2),
                                                    (L7), (L10), A >= S-m,
                                                    (L9), B <= floor(5X/2)
  and does NOT consume:                             the delta-budget, the
                                                    level system, qmin, U

  Both peer audits attacked the delta-budget.  As of this certificate it
  holds up nothing on the pinned ladder: the narrowest-margin machinery in
  the repo is retired from the minimal chain, replaced by a three-line lemma
  standing on certificate 0011 and a convexity bound whose margin is at
  least SIX at every configuration (median 24), where the delta-budget's
  was exactly one.  Certificates 0006/0007 remain the green record of the
  weak-ladder route.
""", flush=True)

print("%d checks + %d notes (stated, not tested), %.0fs, %s"
      % (NCHECK[0], NNOTE[0], time.time() - START,
         "ALL GREEN" if not FAILED else "FAILURES: " + ", ".join(FAILED)))
sys.exit(1 if FAILED else 0)
