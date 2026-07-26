# cofferdam — decisions

## D-001 · The lab is seeded with the statement, never the derivation (2026-07-25)

The claim m ≥ 21 arrived through a correlated chain: GPT 5.6 Sol Pro proposed,
Codex-Brain verified with the proposal in context, Grok's Witness-Lab re-verified
having seen the chain. This lab is the only station that fell out of the loop
before the pivot, so it is the only one that can derive independently. Reading
their work would convert the sole available independent verifier into a
transcriber.

Therefore: seeded with the statement and the problem setup only; the sealed paths
in BRIEF §2 are off-limits to this repo and to any subagent it runs; the seal
lifts only after our own derivation is committed, and only for the diff.

**Consequence accepted:** this lab will re-derive things the others already have,
and will sometimes reach a weaker result. That duplication is the product, not
waste.

## D-002 · No solver in the trust chain (2026-07-25)

τ ≤ 5 is witnessed by five vertices and checked by inspection. "No counterexample
below m edges" is exactly the claim that every candidate has such a witness. So
the work decomposes into exhaustive generation plus a list of explicit covers, and
a solver's unsupported `s UNSATISFIABLE` never enters the argument.

This also settles the toolchain: checkers are stdlib-only and run under a bare
`python3`. PEP 668 blocks `pip install` into the system Python on this machine,
which is convenient — it keeps the constraint honest rather than aspirational.
nauty is installed and may cross-validate canonical forms, but no certificate may
depend on it.

## D-003 · Two engines, kept separate (2026-07-25)

Edge-wise generation (`lib/ryser.py`) gives isomorphism-class censuses and is the
right shape for classification, but canonicalising over all 6! part orders makes
it slow at r=6. Column-wise decision (`lib/columns.py`) — the hypergraph as r
partitions of the edge set — answers existence questions orders of magnitude
faster because the search becomes an exact cover over pairs with a monotone τ
prune.

Both are kept. The edge-wise engine is the census instrument and the independent
check on the column engine's witnesses; the column engine is the workhorse. Every
witness the column engine returns is re-verified through the edge-wise τ before it
is believed.

## D-004 · Cited constants are named dependencies, never absorbed (2026-07-25)

A floor that leans on f(6)=13 is a different object from one that leans on
nothing, and the difference must be visible without reading the source. Every
certificate prints its external inputs and states the floor it would still reach
with each removed. Cert 0001 reaches 18 alone and 19 with f(6)=13, and says so on
its own output.

This is the discipline that keeps a verification honest: a chain that quietly
absorbs its citations cannot be audited for the thing this lab exists to check.

## D-005 · Guessed lemma values are forbidden inputs (2026-07-25)

At founding, this lab guessed g(3)=6 and g(4)=9 from a valid upper-bound
embedding, and both were wrong — the truth is 5 and 8, found by search. Those
guesses would have produced a floor of **20**: much stronger, entirely false, and
suspiciously close to the number under verification.

An error that flatters the expected answer is the most dangerous kind available to
a verifier. Ladder inputs are computed, never inferred from the shape of the
answer, and any value that cannot be computed is carried as an explicit open
parameter with the result stated for each of its possible values.

## D-006 · A cited lemma is only as good as what we let it sit next to (2026-07-26)

Certificate 0002 folded Abu-Khazneh–Pokrovskiy Lemma 2.1 into the ladder, worked
the two-star equality case, found the residual's tail forced to (3,2,1,1,1), saw
that the existing caps already forced exactly that, and recorded the lemma as
*subsumed — moves the floor by nothing*. The lemma was cited correctly. The
conclusion was wrong, because it was set beside an unstated assumption of our
own: that a counterexample may contain degree-1 vertices. It may not, by a
two-line argument nobody had written down. With that, the equality case is not
constrained but empty, and the same lemma moves the floor by a full rung.

**The failure mode is not "we mis-cited".** It is that a negative result — *this
lever does nothing* — was accepted without auditing the assumptions surrounding
the lever. Positive results get checked because they are load-bearing; negative
ones close doors quietly and are checked far less. Therefore: **a recorded dead
end must name the assumptions under which it is dead**, so that a later turn can
see what would have to change to reopen it. Cert 0002's NOTES said only that the
ladder "already encodes this structure"; it did not say *under the profiles the
ladder then admitted*, which is precisely the clause that stopped being true.

## D-007 · The N-ladder: strengthen the class, not the constant (2026-07-26)

The degree-cap ladder asks "how few edges can carry τ ≥ t?" (that is g(t)) and
squeezes the answer. Turn 5 got its improvement instead by **changing the class
being minimised over**: N(t) counts the least edges with τ ≥ t *and a part all of
whose vertices have degree ≥ 2*. Since a deleted star leaves exactly such an
object — the surviving vertices of that part keep every edge they had — every cap
in the ladder can be restated over the smaller class for free. N(4) = 9 against
g(4) = 8 is the whole gain, and it is worth two rungs.

Recorded as a method, not a result: when a bound is tight and its constants are
already computed exactly, look for a **property the extremal object inherits from
the context it appears in** and re-minimise over the restricted class. The
constants stop being the thing to improve.
