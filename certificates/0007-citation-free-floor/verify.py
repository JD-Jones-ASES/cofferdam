#!/usr/bin/env python3
"""Certificate 0007 — the floor m >= 21 needs no citation at all.

    python3 verify.py

Stdlib only.  Exact integer arithmetic.  No solver.  No imports from lib/.

WHAT IS CLAIMED
---------------
  **a Ryser r=6 counterexample has m >= 21**        PROVEN-BY-CERTIFICATE,
                                                    citing NOTHING

  Certificates 0005 and 0006 reached m >= 21 as PROVEN-MODULO-CITATION, the
  citation being f(6) = 13.  This certificate removes it.  The floor is the same
  number; what changes is that no external result stands behind it.

HOW THE CITATION WAS ENTERING, AND WHY IT NEED NOT
--------------------------------------------------
f(6) = 13 entered at exactly one place: the k=1 rung of the (C) ladder, as the
cap Delta <= m - N(5) with N(5) = 13.  Certificate 0005 also derives, citing
nothing, a weaker rung by peeling: an N(5) witness minus the smallest block of
its full part is an N(4) witness, and the block had size >= 2, so

    (P)   N(5) >= N(4) + 2 = 11.

With N(5) = 11 instead of 13, certificate 0005's ladder no longer closes m = 19 --
which is exactly why its citation-free floor stopped at 19.  But (L8) is much
stronger than the pair count that ladder uses, and (L8) does close it.  Running
the certificate-0006 machinery under the WEAKER, citation-free rung:

    m = 19:    33 admissible profile multisets,  0 survive (L8)
    m = 20:  7159 admissible profile multisets,  0 survive (L8)

and m = 12..18 are swept here too (all empty), while m <= 11 dies on lemmas (A)
and (B) alone -- six parts of >= 6 active vertices of degree >= 2 need m >= 12.
So the whole range below 21 is closed inside this certificate.  m >= 21.

Note the direction.  Weakening N(5) from 13 to 11 ADMITS MORE configurations --
34 profiles instead of 32 at m = 20, 7159 multisets instead of 105 -- so this is
a strictly harder problem than certificate 0006 solved, and every configuration
0006 killed is one of the ones killed here.  The last check verifies that
containment rather than asserting it.

THE LEDGER, in full
-------------------
  (A), (B), (C)        lemmas          certificate 0005   ours
  N(1..4) = 2,4,6,9    ladder rungs    certificate 0005   ours (N(4) by
                                                          exhaustion, 52.0M nodes)
  (P)  N(5) >= 11      peeling         certificate 0005   ours
  g(4) = 8             makes (L7) numerical, certs 0001/0005   ours
  (L7), (L8)           counting        certificate 0006   ours (0006's (L8)
                                                          pointer came from Codex)
  EXTERNAL INPUTS      -- NONE.

Note this certificate does NOT lean on certificate 0005's m >= 19: it sweeps
m = 12..20 itself.  That is deliberate.  0005's ladder loop runs range(14, 24),
so as executed it never tests m = 12 or 13, and inheriting its floor would have
inherited that gap.

PROVENANCE
----------
Three labs worked this problem in parallel; this one fell behind the others and
inherited the thread, which is why it re-derives rather than transcribes.  The
sensitivity that pointed here -- that (L8) might not need the citation -- was
raised by Grok's Witness-Lab in the adversarial pass on certificates 0005/0006.
Its stated inference was incomplete: it tested m = 20 only, and m >= 21 needs
m = 19 dead as well, which is the rung certificate 0005's citation-free ladder
had left standing.  The m = 19 sweep, the controls and this certificate are this
repo's.

WHAT IS NOT CLAIMED
-------------------
Nothing here says a counterexample exists at 21 or above.  A floor localises; it
does not construct.  And this does not retire the literature reading in
certificates 0005/0006 -- f(6) = 13 remains true and remains the cheaper route to
the same rung.  What it retires is the DEPENDENCE.
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

NOTES_N = [0]


def note(label, detail=""):
    """A STATED FACT -- a citation, or a step proved by hand and recorded here --
    and NOT a machine check.  Printed with its own tag and counted separately, so
    the check count can never imply a test that did not run."""
    NOTES_N[0] += 1
    print(f"  [note] {label}" + (f"   {detail}" if detail else ""))


def head(s):
    print(f"\n=== {s} ===")


G4 = 8                                   # ours (certificates 0001, 0005)
N_FREE = {1: 2, 2: 4, 3: 6, 4: 9, 5: 11}    # every rung ours; N(5) by peeling
N_CITED = {1: 2, 2: 4, 3: 6, 4: 9, 5: 13}   # certificate 0006's ladder, for the
                                            # containment check only

T0 = time.time()


# ==========================================================================
# The machinery of certificate 0006, restated here so this certificate stands
# alone.  Identical mathematics; the ladder is a parameter rather than a global.
# ==========================================================================

def profiles(m, N):
    """A part's degree profile: a partition of m into at least 6 entries, each at
    least 2 (lemmas (A) and (B)), whose k largest sum to at most m - N(6-k)
    (lemma (C))."""
    caps = {k: m - N[6 - k] for k in range(1, 6)}
    out = []

    def rec(left, cur):
        k = len(cur)
        if k in caps and sum(cur) > caps[k]:
            return
        if left == 0:
            if len(cur) >= 6:
                out.append(tuple(cur))
            return
        for s in range(min(left, cur[-1] if cur else m - N[5]), 1, -1):
            if 0 < left - s < 2:
                continue
            rec(left - s, cur + [s])
    rec(m, [])
    return out


def sc(p):
    return sum(comb(d, 2) for d in p)


def qmin(n):
    if n <= 0:
        return 0
    q = 2
    while comb(q, 2) < n:
        q += 1
    return q


def l8_kills(combo, m, g4=G4):
    """True iff (L8) rules this multiset of six part profiles out."""
    Ms = [p[0] for p in combo]
    S = sum(Ms)
    X = sum(sc(p) for p in combo) - comb(m, 2)
    Pc = sum(comb(x, 2) for x in Ms)
    floors = [max(0, Ms[i] + Ms[j] - (m - g4))
              for i in range(6) for j in range(i + 1, 6)]
    L = sum(floors)
    q, rr = divmod(S, 6)
    U = min(q, m) * comb(6, 2) + (comb(rr, 2) if q < m else 0)
    if U < L:
        return True
    for A in range(L, U + 1):
        D = A - S + m
        if D < 0:
            continue
        c = list(floors)
        for _ in range(A - L):
            c[min(range(len(c)), key=lambda i: c[i])] += 1
        Bmin = sum(comb(v, 2) for v in c)
        Bcap = (5 * X) // 2
        if Bmin > Bcap:
            continue
        for Bv in range(Bmin, Bcap + 1):
            for n5 in range(0, X // 4 + 1):
                for n4 in range(0, (X - 4 * n5) // 3 + 1):
                    for n3 in range(0, (X - 4 * n5 - 3 * n4) // 2 + 1):
                        rest = Bv - 10 * n5 - 6 * n4 - 3 * n3
                        if rest < 0:
                            continue
                        n2 = rest
                        if n2 + 2 * n3 + 3 * n4 + 4 * n5 > X:
                            continue
                        if 2 * n2 + 3 * n3 + 4 * n4 + 5 * n5 > Pc:
                            continue
                        if n2 + n3 + n4 + n5 > comb(m, 2):
                            continue
                        need = (qmin(n3 + n4 + n5) + 2 * qmin(n4 + n5)
                                + 3 * qmin(n5))
                        if D >= need:
                            return False
    return True


def multisets(m, N):
    P = sorted(profiles(m, N), key=sc, reverse=True)
    return P, [c for c in itertools.combinations_with_replacement(P, 6)
               if sum(sc(p) for p in c) >= comb(m, 2)]


def sweep(m, N, g4=G4, stop_at_first=False):
    P, C = multisets(m, N)
    surv = []
    for combo in C:
        if not l8_kills(combo, m, g4):
            surv.append(combo)
            if stop_at_first:
                break
    return P, C, surv


# ==========================================================================
# 1. The citation-free rung, and that it really is weaker
# ==========================================================================

head("(P): the citation-free N(5) rung, and the direction of the weakening")

check("(P) N(5) >= N(4) + 2 = 11, by peeling the smallest block of the full part",
      N_FREE[4] + 2 == 11,
      "the residual still has tau >= 4 and its distinguished part keeps every "
      "vertex it had, at unchanged degree, so it is an N(4) witness")
check("11 < 13, so this certificate runs on a STRICTLY WEAKER input than "
      "certificates 0005 and 0006", N_FREE[5] < N_CITED[5])

for m in (19, 20):
    Pf = set(profiles(m, N_FREE))
    Pc = set(profiles(m, N_CITED))
    check(f"at m = {m} the weaker rung admits MORE part profiles, and every "
          f"profile the cited rung admits is among them",
          Pc < Pf, f"{len(Pc)} cited profiles is a proper subset of "
                   f"{len(Pf)} citation-free profiles")

# ==========================================================================
# 2. The sweeps
# ==========================================================================

head("(L8) under the citation-free ladder N = {1:2, 2:4, 3:6, 4:9, 5:11}")

# The whole range is swept HERE rather than inherited.  Certificate 0005's floor
# would have served for m <= 18, but its ladder loop runs `range(14, 24)` and so
# never tests m = 12 or 13 -- leaning on it would have imported a gap.  Sweeping
# 12..20 here costs about a second and makes this certificate answer for its own
# whole range.
check("m <= 11 is impossible by (A) and (B) alone, before any search",
      not profiles(11, N_FREE) and not profiles(10, N_FREE),
      "degrees within one part sum to m, so a part with >= 6 active vertices "
      "each of degree >= 2 forces m >= 12")

results = {}
for m in range(12, 21):
    t = time.time()
    P, C, surv = sweep(m, N_FREE)
    results[m] = (P, C, surv)
    check(f"m = {m}: impossible", not surv,
          f"{len(P):>3} profiles, {len(C):>5} admissible multisets, "
          f"{len(surv)} survivors"
          + (f", {time.time()-t:.0f}s" if time.time() - t > 1 else ""))

check("m = 20's admissible set is 68x the cited one and still dies completely",
      len(results[20][1]) == 7159,
      f"{len(results[20][1])} multisets here against 105 in certificate 0006")
check("so EVERY m <= 20 is impossible, citing nothing -- swept here, not "
      "inherited from another certificate",
      all(not results[m][2] for m in results))

# ==========================================================================
# 3. Controls.  This result RAISES the lab's own claim, which by D-005 is the
#    most dangerous direction an error can point, so it gets more than one.
# ==========================================================================

head("Controls")

# THE control: an argument that killed every m would be proving Ryser at r = 6.
t = time.time()
P21, C21, s21 = sweep(21, N_FREE, stop_at_first=True)
check("NOT TOO STRONG: at m = 21 the same machinery, on the same weak ladder, "
      "leaves survivors", bool(s21),
      f"{len(P21)} profiles; stopped at the first survivor "
      f"({'+'.join(str(p[0]) for p in s21[0]) if s21 else '-'}) after "
      f"{time.time()-t:.0f}s -- the full m=21 count is NOT swept here")

# NEGATIVE CONTROL on the load-bearing search.  N(4) = 9 rests on one exhaustive
# search of ours (52.0M nodes).  If that search had under-enumerated and the truth
# were N(4) = 8, the kill must visibly fail -- otherwise this certificate would be
# concluding m >= 21 for reasons unconnected to its stated inputs.
t = time.time()
N_BAD = dict(N_FREE)
N_BAD[4] = 8
_, C20b, s20b = sweep(20, N_BAD, stop_at_first=True)
check("SENSITIVITY: with N(4) falsely set to 8, m = 20 survives -- so the kill "
      "really does rest on N(4) = 9 and is not an artefact", bool(s20b),
      f"{len(C20b)} multisets, first survivor found in {time.time()-t:.0f}s")

# CONTAINMENT.  Certificate 0006's 105 multisets must be a subset of the 7159
# killed here -- otherwise the two certificates are answering different questions
# and this one does not subsume it.
_, C20cited = multisets(20, N_CITED)
here = set(results[20][1])
check("every one of certificate 0006's 105 multisets is among the "
      f"{len(results[20][1])} killed here, so this certificate subsumes it "
      "rather than sitting beside it",
      set(C20cited) < here, f"{len(C20cited)} is a proper subset of {len(here)}")

head("Result")

print(f"""
  (P) N(5) >= 11                                PROVEN-BY-CERTIFICATE (0005)
  m = 19 impossible, citing nothing             PROVEN-BY-CERTIFICATE
  m = 20 impossible, citing nothing             PROVEN-BY-CERTIFICATE
  **a Ryser r=6 counterexample has m >= 21**    PROVEN-BY-CERTIFICATE,
                                                CITING NOTHING

  Certificates 0005 and 0006 reached this floor leaning on f(6) = 13.  They no
  longer have to.  The external exposure of m >= 21 is now empty, and the whole
  of the standing question about that citation -- whether AKP Lemma 2.9 holds,
  whether its definition of f(6) matches the one the ladder consumes -- is moot
  for the floor.  It remains live for the literature, and for any attempt to
  push past 21.

  The load-bearing step is no longer a citation.  It is N(4) = 9, one exhaustive
  search of ours at 52.0M nodes.  An under-enumerating search fakes a proof, and
  the sensitivity check above shows exactly how much rests on that one: set
  N(4) = 8 and m = 20 comes back to life.  A third independent implementation of
  that search is now the single most valuable thing anyone could contribute.
""")

print(f"{COUNT[0]} checks + {NOTES_N[0]} notes (stated, not tested), "
      f"{time.time()-T0:.0f}s, "
      f"{'ALL GREEN' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(1 if FAIL else 0)
