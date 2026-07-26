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

## D-008 · The surplus in a counting bound is a resource, not slack (2026-07-26)

Every counting lemma in this lab was written as `quantity ≥ threshold`, and the
amount by which a configuration exceeded the threshold was called "slack" and
treated as bad news — the bigger the slack, the weaker the argument. Certificates
0001 and 0002 both report slack that way, and turn 6's (L4)/(L7) squeeze stalled
at 30 against exactly 30 and was filed as a dead heat.

**Codex** inverted it. For the pair count the surplus is not
slack, it is an
**exact quantity with a structural meaning**:

  sum_v C(d(v),2) - C(m,2) = sum_{e<f} (|e n f| - 1) = X,

so X *is* the total repeated agreement in the object, and every structural feature
that forces two edges to agree twice **spends** it. Two overlapping high-degree
stars in different parts cost C(c,2) units. Once X is a budget rather than a
margin, a configuration can be killed by making it buy more than it can afford —
and that is what closed m = 20 after the same inequalities, read as bounds, had
tied.

Therefore: **state every counting lemma with its surplus identified as a
quantity, and ask what spends it.** A bound of the form `A >= B` should be
recorded as `A - B = <what that difference counts>`. Where the difference has no
combinatorial meaning, say so; where it does, it is a second lever the bound was
hiding.

Corollary worth keeping: a dead heat is the *most* promising place to look for a
kill, not the least. Equality forces every inequality in the chain to be tight,
which is a very strong structural statement — it was equality that pinned all
fifteen part-pair overlaps to exactly 2 and made the rest forced.

## D-009 · Weaken a step deliberately if the conclusion survives it (2026-07-26)

Certificate 0006's ceiling on A began as an exact dynamic program over the degree
value-pool with the (L4) per-edge bound folded in — the most machinery in the
repo. Replacing it with the crudest possible bound (maximum concentration, no pool,
no (L4)) makes the test **strictly more permissive**, and it still killed all 105
configurations at m = 20.

So the weaker version shipped. This is not tidiness: the pool DP was the one part
of the argument a reader would have had to trust rather than check, and dropping it
removed a whole layer from the trust chain at zero cost to the result. It also
removed the layer whose relaxation semantics ("sound in the negative direction
only") were the easiest thing in the certificate to get subtly wrong.

**Rule:** once a result is established, retry it with each expensive step replaced
by the cheapest sound bound available. Keep whichever version still concludes, and
prefer the one a reader can check by hand. Strength you do not need is exposure.

## D-010 · Provenance conventions (2026-07-26)

Three labs worked r = 6 in parallel; this one fell behind and inherited the thread,
which is why it re-derives rather than transcribes. The pointers that opened
certificates 0005 and 0006 came from Codex; the proofs, searches, machinery and
controls are this repo's. Nothing sealed was read.

Two conventions follow, and that is all this needs to be:

1. **Credit the station that produced the mathematics** — Codex, Grok, a paper (AKP,
   ABW, MSY), or this lab. Put it in the artifact that travels (a certificate's
   docstring), not only the notebook. Where a step's origin is unknown, ask rather
   than fill it in.
2. **The owner's name does not appear in a mathematical derivation.** He owns and
   relays between stations; he is not a party to the mathematics. His name belongs
   where the subject is ownership — seal rulings, licensing, machine time, and the
   digests addressed to him.

Neither convention is about credit as a good in itself. They exist because a
provenance ledger that is wrong anywhere is untrustworthy everywhere, and because
this lab's results are meant to be attacked by the other two labs — an attacker needs
to know which parts to hit, and mis-stated origins waste their time.

## D-011 · Seal status (2026-07-26)

Certificates 0001–0007 were derived without reading any peer derivation. That
does not change. The seal has since been opened, so a later session in this repo
is not a blind verifier and should not be presented as one.

How this lab takes in peer work is a Brain-level question and lives there, not
here. This repo is about the mathematics.

## D-012 · A peer's wrong inference can carry a right experiment (2026-07-26)

Grok's audit reported that (L8) still killed everything at m = 20 under weakened
caps, and concluded: "combined with 0005's citation-free m ≥ 19, that would give
m ≥ 21 with no literature citation." **The conclusion does not follow.** m ≥ 19
leaves m = 19 *standing*; killing m = 20 alone leaves the floor at 19. The
inference needed a rung nobody had run.

Running it — (L8) at m = 19 on the citation-free ladder — killed all 33
configurations, and the floor became citation-free after all (certificate 0007).
So the audit's conclusion was unearned and its **experiment was the best thing
anyone contributed this turn.**

Therefore: **from an adversarial report, extract the experiment separately from
the inference.** Re-run the experiment; re-derive the inference from scratch.
A peer who runs a sensitivity you did not think to run has given you something
real even when the conclusion drawn from it is invalid — and a peer whose
conclusion happens to be right has given you nothing you can use until you have
re-derived it anyway.

Corollary, and the reason this is a decision rather than an anecdote: the failure
mode D-005 warns about was live here. The claim flattered — it *upgraded our own
label* — and it arrived from a friendly source with a plausible argument
attached. It happened to survive repair. The next one will not.

## D-013 · A displayed identity is an untested identity (2026-07-26)

Certificate 0006 printed, in its docstring and its NOTES, the layer-cake identity
`D = Σ_{t≥3}(δ(t)−δ(t−1))|W_t|`. It is false: δ(0) = 1, so δ dips at k = 0 → 1,
and the true statement carries a leading `n₀ = #{e : k_e = 0}`. The certificate's
**own shipped 5-edge witness has n₀ = 1** and reads 3 where D = 4. The error sat
in the repo through five certificates and two labs' audits because the code never
evaluated it — `l8_kills` computes D exactly from (C4) and never forms |W_t|.

**Every identity a certificate displays must also be asserted on the objects the
certificate already carries.** Prose is not checked by the checker; the moment an
identity is only printed, it has left the trust chain while still looking like
part of it. Found by Codex; the direction matters and Codex did not say it — the
false form *understates* D, and understating D makes a kill harder, so the defect
was conservative. Had it gone the other way it would have manufactured false
kills, silently.

## D-014 · Prove the whole statement, or restate what you proved (2026-07-26)

Certificate 0005 proved that every part of an 8-edge τ=4 object is (3,2,2,1) or
(3,2,1,1,1), and the repo recorded that as "the corrected AKP Lemma 2.8, proven
outright". The printed lemma has a second half — *all six parts A, or five A and
one B* — which our checker did not prove. Worse, that global half is precisely
the one AKP's Lemma 2.9 consumes: its Δ=4 case bounds intersections by 7+6·4 =
**31** against **32** required, a margin of one that a second B part erases.

**We proved the half that was not load-bearing and claimed the lemma.** The half
we skipped cost 52 seconds of our own machinery to settle (b ≤ 2 by counting,
b = 2 forces excess 0, one search at waste budget 0 comes back empty, and its
positive control at budget 1 finds the 5A+1B object). It is now certified.

Rule: when a result is quoted from a source, **restate the source's statement in
full and check it clause by clause against what was actually proven.** A partial
proof recorded as a whole one is not a small inaccuracy — the missing clause is
disproportionately likely to be the one the source needed, because that is the
clause the source went to the trouble of stating.

## D-015 · A checker must be green under `python3 -O`, and annotations are not checks (2026-07-26)

Two hygiene failures with one root: **the printed check count was not a count of
things that ran.**

1. Certificate 0005 held three `assert engine.precompute()` calls. `python3 -O`
   deletes assert statements, so under `-O` the engine was never built and the
   certificate died on a missing attribute in 0.05 s. Certificates 0001, 0002 and
   0004 each *advertise* "no bare assert — `python3 -O` strips those". The rule
   was written down three times and broken in the one certificate that never
   states it. (The failure was loud, exit 1, so nothing was ever falsely green.)
2. Thirteen `check(...)` calls across four certificates passed a literal `True`.
   Some were honest annotations of un-machine-checkable facts (a citation, a
   pointer to a notebook). One — `N(t) ≥ 2t` in 0005 — was an **input to the
   m ≥ 21 arithmetic**, transcribed into 0006's ladder. Being counted among the
   "40 checks" made it look tested.

Therefore: side effects never go inside `assert`; every certificate replays under
both `python3` and `python3 -O`; and a stated fact prints through `note()`, which
has its own tag and its own tally, so the check count can never imply a test that
did not run. `N(t) ≥ 2t` is now computed rather than stated.

## D-016 · A loop's range is part of its claim (2026-07-26)

Certificate 0005's docstring claims "a counterexample has m ≥ 19"; its ladder loop
runs `range(14, 24)`, so as executed it never tested m = 12 or 13. Certificate
0006's check was labelled "m ≤ 19 has no admissible configuration at all" while
testing exactly `(17, 18, 19)`. Neither claim was false — both ranges are empty —
but neither was *checked* over the range its label asserts, and a reader auditing
the chain would have had to notice the gap unaided.

**A test's range is part of what it claims.** State the range in the label, make
the loop cover it, and where a range is bounded below by an argument rather than
by a search, check that argument too (here: six parts of ≥ 6 active vertices of
degree ≥ 2 force m ≥ 12, so 12 is where searching has to start). Certificate 0007
sweeps m = 12..20 itself rather than inheriting a floor, for exactly this reason.

## D-017 · "Conservative" is a claim about direction, not about margin (2026-07-26)

An adversarial pass hunted (L8) for a **false kill** — a configuration reality
permits that the code rejects — and found none. Loop bounds hold with room, the
greedy B_min equals the exact DP minimum, the ceiling on A is genuine, the
δ-budget never exceeds the true requirement. Good. But it also found that the
repo's own defence of (L8) told only the safe half of the story, in two ways.

**One: the margin is exactly 1.** The tightest point in the entire m = 20 kill is
the (7,…,7) dead heat at A = 30 under level structure {4,4,3}: **D = 8 against a
need of 9**, and the need is exact rather than a bound. Three inputs — g(4) = 8,
X, and the δ-budget — each flip the result if moved by a single unit. Six other
quantities turned out not to be binding at all, and were loosened by large amounts
with no survivors appearing. Saying the test is "conservative" while omitting
"margin 1" invites a reader to hear *robust*. Those are different claims.
**Report the margin wherever you report conservatism.**

**Two: the relaxation argument does not cover the whole pipeline.** Everything
inside `l8_kills` is a *relaxation* — it permits configurations reality forbids,
so a total kill under it is conservative by construction, and both peer audits
said so correctly. But the configurations it is handed come from `profiles()`,
which is a **restriction**: it *forbids* via the N-caps and lemmas (A)/(B)/(C).
That is the opposite direction, and it is the only place a false kill could live.
The blanket sentence "every relaxation makes survival easier" gave that half a
free pass — in our writing and in both audits.

The consequence is a sharper ranking than the reassurance was providing: the
weakest step in the chain is not anything in (L8), it is **N(4) = 9**. Measured:
N(4) = 8 turns 0 survivors into 1445 of 3664.

**Rule.** For any argument of the form "our test is safe because it is loose",
state (a) the *margin* at the tightest point, and (b) which parts of the pipeline
run in the loose direction and which run in the tight one. A defence that applies
to only half the pipeline is not a defence, however true it is of its half.

## D-018 · An empty search should exhibit what it rejected (2026-07-26)

N(4) ≥ 9 — the step everything now funnels through — was confirmed by a second,
structurally different exhaustion in the turn-7 completeness pass: 1505 candidate
columns against our 2220, 5,713,053 nodes against our 52,023,309, same verdict.

The part worth keeping is not the agreement. It is that **the second search
exhibits what it rejects**: it built **8648 full pair-covers on 8 edges and found
every one of them at τ = 3**. Ours returns `None` and a node count.

A node count is a claim about effort, not about coverage — an under-enumerating
search produces a small node count and an empty answer, which is exactly what a
correct search on a genuinely empty space also produces. **The two are
indistinguishable from the outside.** A search that hands back the objects it
built and the property that killed each one is distinguishable: you can check the
objects, and you can see the search reached the region where an answer would have
been.

**Rule.** Any "no such object exists" result should ship the near-misses — the
objects that satisfied every constraint but the last, with the value of the
quantity that failed. Where that set is too large, ship a sample plus its size.
The completeness argument stops being a promise and becomes an artifact.

Corollary for the standing request to the other labs: **a third implementation
should match the verdict by a different route, not match the node count.**
Reproducing 52,023,309 nodes would only demonstrate that someone reimplemented
our prunes.

## D-019 · State which step carries what, or the attack goes to the wrong place (2026-07-26)

Ablation across the whole chain (turn 7): remove **(L7)** and 100% of
configurations survive at every m. Remove the **excess budget X** and the same.
Remove **N(4) = 9** and m = 20 revives. Remove the **δ-budget** and *only* m = 20
revives — below it, the kills come from (L7) + X alone, with a margin of 16 at
m = 19. Remove the **concentration ceiling U** and nothing happens at all: it is
inert.

Both peer audits ranked the δ-budget as the thing to attack, and so did we — it
is the newest inequality and the least checked. It is also the one that can cost
the least: **a δ-budget failure drops the floor from m ≥ 21 to m ≥ 20, still
citing nothing.** Meanwhile (L7) and X, which carry everything, appeared on
nobody's list, precisely because they are old, simple, and were never in doubt.

**Rule.** Publish a risk decomposition beside the attack surface: for each step,
what the result degrades to if that step fails. "Newest and least checked" is a
proxy for fragility, and it is a bad one — it correlates with *attention*, not
with *load*. The steps most worth defending are the ones so settled that nobody
lists them.

(Also vindicating D-009: U was kept deliberately weak for safety and turns out to
be doing no work whatever. A step you kept only as insurance and that proves inert
is the best possible outcome — it can be deleted from the trust chain outright.)
