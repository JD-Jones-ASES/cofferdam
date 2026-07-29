# cofferdam — decisions

## Standing law — read these before working here

The twelve entries below are operative rules. Everything else here is the
**incident record** — the reasoning behind a decision, kept because the reasoning
is the value and a rule stripped of its evidence is the first thing a later turn
talks itself out of. The numbering skips **D-020 and D-021**: never issued.

- **D-002** — no solver in the trust chain; checkers are stdlib-only under a bare `python3`.
- **D-004** — a cited constant is a named dependency, printed with the floor reached without it.
- **D-005** — ladder values are computed, never guessed; an error that flatters the expected answer is the worst kind.
- **D-010** — credit the station that produced the mathematics; the owner's name never enters a derivation.
- **D-015** — green under `python3 -O`; a stated fact prints through `note()`, never as a check.
- **D-016** — a loop's range is part of its claim: state it, then cover it.
- **D-017** — claim conservatism only with the margin at the tightest point, and say which half runs loose.
- **D-032** — one ledger, transitive; a consumption feeding no claim is CONTROL-ONLY, with its fail-safe direction.
- **D-034** — certificate errata: reworded label, dated NOTES erratum, CONDITION untouched, same commit.
- **D-035** — k consumed caps means k margin coordinates: sweep each, name the binding one.
- **D-036** — peer intake: statements in, proofs never, text verbatim to refuters and retained; a deflation is an error too.
- **D-038** — see D-036: refuters read the original, never a desk transcription; received texts are kept in `notebook/raw/`.

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
the two-star equality case, found the residual's tail forced to (3,2,2,1), saw
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

This entry originally routed the question of how the lab takes in peer work to the
Brain as an out-of-scope matter. That stopped being true at turn 14: **intake is
house law and it lives here — see D-036.**

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
in the repo through five certificates because the code never evaluated it, and it
was Codex's audit that found it — `l8_kills` computes D exactly from (C4) and never forms |W_t|.

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

Certificate 0005's docstring claimed "a counterexample has m ≥ 19" while its ladder
loop ran `range(14, 24)`, so as executed it never tested m = 12 or 13. (Now
`range(12, 24)`.) Certificate
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
with no survivors appearing. *(Corrected in 0006's NOTES, 2026-07-26: five, not
six — the count wrongly included L, which a later pass found binding.)* Saying the test is "conservative" while omitting
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

> **Corrected by [D-023](#d-023--a-risk-decomposition-is-a-claim-and-ours-was-wrong-2026-07-26-turn-8).**
> The turn-7 ablation table this entry published was **false in its (L7) row** —
> removing (L7) leaves 2.9%–22.6% surviving, not 100%. The rule below survives;
> the table did not, and D-023 carries its corrected numbers.

Both peer audits ranked the δ-budget as the thing to attack, and so did we —
newest inequality, least checked. It is also the one that costs least: **a
δ-budget failure drops the floor from m ≥ 21 to m ≥ 20, still citing nothing.**
The steps carrying the load were on nobody's list. One row survived the
correction: the **concentration ceiling U is inert**, vindicating D-009 — a step
kept only as insurance and proved inert can be deleted outright.

**Rule.** Publish a risk decomposition beside the attack surface: for each step,
what the result degrades to if that step fails. "Newest and least checked" is a
bad proxy for fragility — it correlates with *attention*, not with *load*. The
steps most worth defending are the ones so settled that nobody lists them.

## D-022 · The residual of a cross-part peel keeps nothing (2026-07-26, turn 8)

The lever that looked free: if the two-star residual R had a part of minimum
degree 2, (L7) would take **N(4) = 9** in place of g(4) = 8 and tighten by one
unit everywhere — where D-017 prices the margin at exactly one.

**The min-degree-2 route is dead exactly where it would have mattered.** The only
ρ = |R| at which the +1 changes a floor is ρ = 8, and there **τ(R) = 4 exactly**
(≥ 4 by the peel, ≤ 4 because g(5) ≥ 12) — so every part is a cover with ≥ 4
active vertices, and the only partition of 8 into ≥ 4 entries each ≥ 2 is
(2,2,2,2). "R has a part of minimum degree 2" *is* the statement N(4) ≤ 8: the
hypothesis the lever needs is the negation of the constant it would invoke.
Machine-checked, 15 of 15 two-star residuals of W8 and 15 of 15 of W9 have no such
part. (Scope: this kills the min-degree-2 route, not every route — the first
version overstated it — and it needs **no appeal to AKP Lemma 2.8**, whose
derivation consumes the same N(4) search.)

**Rule.** A same-part peel and a cross-part peel are not the same operation.
Lemma (C) gets N(6−k) because deleting k vertices of **one** part never touches
that part's survivors — an edge has exactly one vertex per part — while a
cross-part peel destroys that guarantee, so nothing stops a degree-2 vertex
dropping to 1. Before carrying a per-part hypothesis across a deletion, ask which
part paid for it.

## D-023 · A risk decomposition is a claim, and ours was wrong (2026-07-26, turn 8)

D-019 published a table so that attack would go to the right place. **Its (L7)
row was false.** It said removing (L7) leaves 100% of configurations surviving at
every m. Measured, with certificate 0007's own `l8_kills` and one line changed:
**3 of 105 survive at m = 20 cited (2.9%), 1,616 of 7,159 at m = 20 free (22.6%),
1 of 33 at m = 19 free**, four implementations agreeing. With (L7) gone, D ≥ 0
still forces A ≥ S − m, convexity still forces B_min large, and X still refuses
to pay; most no-(L7) survivors first survive at D = 0, the minimum-surviving-D
histogram at m = 20 free being **{0:1612, 4:4}**.

> **Erratum, ours, same day.** This paragraph first read "Every no-(L7) survivor
> sits at exactly D = 0." **False** — four of the 1,616 free-m=20 survivors first
> survive at D = 4, and the union of surviving D values runs 0..27 there. Caught
> by the verification pass on this very ADR. An entry written to correct an
> unchecked claim is exactly where a fresh unchecked claim costs most.

**The step actually doing that work has no name anywhere in this repo.** 100%
survival reproduces only when **B_min(A)** — the convexity lower bound on
B = Σ C(c_ij,2) subject to Σ c_ij = A — is zeroed *as well as* the (L7) floors,
and it is in no risk table, ledger line or certificate label. The lab spent two
turns ranking the δ-budget (worth at most one rung) above a step it never wrote
down. The same pass found **g(4) = 8** carrying a margin of one (weaken it to 7
and 649 of 7,159 survive at m = 20 free), on no attack list anywhere, and the
N(4) = 8 row numerically right but **understated** — m = 19 revives too, so that
failure drops the floor to 19, not 20.

**Rule.** D-019 stands; this is D-019 applied to itself. A published risk
decomposition is a load-bearing claim and gets the same treatment as any other —
an executable ablation, re-derived, with the numbers printed. An unchecked table
that misstates a step's load by a factor of 35 does not merely fail to direct
attack; it directs it away.

## D-024 · Some controls are impossible, and saying so is the control (2026-07-26, turn 8)

PLAN.md owed "a positive control: the bound must hold on objects that exist" for
the degree-2 cap. **On the 6-partite class that cannot be discharged, by anyone** —
an intersecting 6-partite object with τ = 6 *is* a Ryser counterexample. Measured:
**0 of 67,463** census objects have τ = r.

> **Erratum, ours, same day.** This ADR first said the control was impossible
> **full stop**, and certificate 0008 repeated it. That is scoped wrong. The
> lemma the floor actually rests on — (III-C) — **never uses r-partiteness**, so
> its hypothesis class is non-empty at r = 6 and constructible in a second;
> certificate 0008 ships that witness (PG(2,5) minus the ten secants of a 5-arc,
> not 6-partite, so the floor is untouched) with its full spec.
>
> "We could not find a violating object", "no object of that kind exists", and
> "no object satisfying *this particular strengthening* of the hypotheses exists"
> are three different sentences. The ADR asserted the second and had only earned
> the third.

What replaced it: **test the proof, not the conclusion.** The lemma is a
construction, so it runs on objects regardless of τ — exhaustively, in certificate
0008: **248,460 constructed sets, zero failures**, with a mutant drawing x from
outside ℓ_u ∩ ℓ_v failing 3,780 of 3,780 to prove the test has teeth.

**Rule.** When a lemma's hypothesis class is conjecturally empty, no compute
produces a positive control on its conclusion, and a checklist item demanding one
sits there forever looking like diligence. Test the *construction* instead: a
proof by explicit witness runs wherever its construction is defined, a strictly
larger class than where its conclusion holds. Record the impossibility in the
exact scope earned.

## D-025 · `extension_edges` returns edges already present (2026-07-26, turn 8)

`lib/ryser.py`'s `extension_edges(H, r)` promises "every edge f such that
H + (f,) is still intersecting" — and an edge **already in H** trivially meets
every edge of H, so it is returned. `generate()` then does
`H2 = tuple(sorted(H + (f,)))` with no check that f is new, and `canonical_fast`
treats a duplicated row as a distinct object, so the duplicate survives dedup.
Reproduces in one line: `generate(3,3,1)` returns `((0,0,0),(0,0,0))` and
`((0,0,0),(0,0,0),(0,0,0))`.

Blast radius, measured by the auditing agent: 4,304 of 71,767 emitted objects
across its runs are not simple, and it reaches the peeling engine —
**`enumerate(6,3)` is 53,871, not the 53,906 this lab has published.** The
**extremal** counts are unaffected: a repeat at (5,3) would mean 4 distinct edges
with τ ≥ 3, contradicting g(3) = 5, and likewise at (8,4). So `enumerate(5,3)=12`,
`enumerate(8,4)=5`, N(4) = 9 and the whole ladder stand.

**Rule.** "Every f such that H + f has property P" is not the same set as "every
f **not already in H** such that H + f has property P", and for a hereditary P
the difference is silent — it inflates counts without ever producing an invalid
object. A census engine needs a simplicity assertion on its output, not just on
its logic.

## D-026 · Inventory your own witnesses (2026-07-27, turn 9)

Q13 — is there a 13-edge τ ≥ 5 object with a full part? — was posed at turn
5, priced at turn 8 (232 search slices, 44 min on 3 cores unfinished), and
listed as PLAN item 5. The answer had been sitting in certificate 0008 since
the day before the pricing: its 13-edge (D2)-falsifier W has part 1 =
(4,3,2,2,2), a full part. W was built to answer one question and nobody
asked it any other.

**Why:** an object's certificate records the properties its *purpose*
needed. Every other property is invisible until someone looks — and a search
for an object you already own is the most expensive form of not looking.

**How to apply:** when a new named object enters the repo (witness,
falsifier, control), run it once against the standing open questions —
today: does it have a full part, what is its Δ, what are its part profiles,
what is its D₂. One screenful of properties per object, recorded in the
certificate that ships it. And when pricing any search, first ask what
existing object is closest to the target.

## D-027 · (L9): the unnamed load-bearer now has a name, a proof and an audit (2026-07-27, turn 9)

D-023 found that the step carrying 77.4% of the m = 20 kills appeared in no
table, ledger or label. It is now **(L9), the water-filling floor for B**:
over integer vectors c ≥ floors with Σc = A, the greedy that always
increments a current-minimum entry attains min Σ C(c_i, 2) exactly;
minimizers are exactly the levelled-above-floors vectors; the value is
tie-break independent. Proved by exchange argument; audited against
exhaustive brute force and an independent DP over 262,729 instances
including **every (floors, A) pair certificates 0007/0008 actually
consult** — zero mismatches.

**Why:** the audit is not decoration. The greedy evaluates the objective at
a *feasible* vector, so its value can never sit below the true minimum —
which means its only possible failure mode is B_min **too high**, i.e.
false kills, the D-005 direction. A bound whose error modes are all
dangerous must be exact, and exactness is checkable.

**How to apply:** when a risk decomposition names a new load-bearer, the
follow-through is mechanical: state it, prove it, audit it at its actual
points of use, and put its name in the certificate docs so the next ablation
has something to ablate.

## D-028 · "Proven twice" must mean two arguments, not one argument in two code forms (2026-07-27, turn 9)

Certificate 0001's lower bounds for g(2), g(3), g(4) were believed proven
twice: counting, and "exhaustive absence" searches. Instrumented replay
shows the searches **never branch** — at every sub-threshold m the root
waste-budget prune (6·maxcov < C(m,2)) kills immediately, and that prune IS
the (L1)+(L2) counting argument. One proof, two costumes. Two 0001 doc
claims fell with it: "counting alone is not tight there" (it is tight
through g(5) — the dead heat at m = 12 is where it first fails to *decide*)
and "runtime dominated by the m = 7 absence check" (that check is one node;
the runtime is the m = 8 witness re-find).

**Why:** independence claims are load-bearing in a verification lab — the
whole point of a second proof is that it can catch the first one. A search
whose prunes encode the counting argument cannot catch an error in the
counting argument.

**How to apply:** before recording two verifications as independent, ask
what the second one would DO differently if the first were wrong. If the
answer is nothing, it is the same verification. Instrument node/branch
counts when in doubt — a search that "confirms" in one node is a
restatement. (The genuine second leg for the g-ladder — a definitions-only
brute force with no (L1)/(L2) — was run this turn; see the notebook.)

## D-029 · A dead heat is a forcing, not a failure (2026-07-27, turn 9)

The counting ladder's equality case at (m, t) = (12, 5) — capped per-part
maximum 11, 6 × 11 = 66 = C(12,2) exactly — sat unread in certificate
0001's own output for eight turns, filed mentally as "counting cannot decide
m = 12". Read as a forcing, it pins every part to (4,3,2,2,1), sets X = 0,
forbids repeated edges, and collapses the rung to an 11,520-design
exhaustion that runs in minutes and closed g(5) = N(5) = 13.

**Why:** an inequality that closes with slack kills a rung; an inequality
that closes with equality *describes the survivors*. The second is worth
more: it hands over structure for free, at exactly the rungs where the kill
was going to be hardest.

**How to apply:** at any rung where a counting bound comes within a unit or
two of its target, do not shelve it as indecisive — extract the equality
conditions and enumerate the forced class. PLAN's attack list now carries
the systematic version (the equality-regime scan).

## D-030 · A saturated cap is a structure statement, and fresh theorems pay same-day (2026-07-27, turn 9)

The k=1 cap Δ ≤ m − N(5) reads as a ceiling. Its equality case is a
construction: deg(v) = m − 13 hands you a 13-edge τ ≥ 5 complement, i.e. a
member of the exact class certificate 0011 had just bounded, and the bound
transfers back as the overlap floor (L10). The 43 configurations the
δ-budget alone could kill at m = 21 were precisely the ≥-2-saturated ones —
the δ-budget was paying numerically for structure that saturation gives as
a theorem.

**Why:** extremal inputs are consumed as numbers, but wherever a
configuration SITS at a cap, the cap's equality case is a hypothesis it
satisfies — usually a much stronger statement than the number. And a
theorem proved "for completeness" (0011 was PLAN's lowest-stakes item)
can become load-bearing the day it exists, because floors compose.

**How to apply:** when a kill needs its narrowest-margin step, first list
which caps the surviving configurations saturate, and ask what object each
saturation constructs. Check whether an existing certificate already bounds
that object's class. (L10) took three lines once the question was asked.

## D-031 · Attribution is recorded, not consumed — and novelty statements name the exact function (2026-07-27, turn 10)

Certificate 0013 re-derives classical machinery (Bollobás 1965 / Katona
1974 / Jaeger–Payan 1971) from first principles and ships citing
nothing; the attribution lives in NOTES.md and the notebook, stated as
precisely as the lit sweep could pin it. Separately: the turn-10 sweep
found three distinct published 13s and three distinct 9s adjacent to
our ladder (q(5), f(6), 8r/3−3; q(4), f(5), our N(4)) — functions with
different domains that collide numerically.

**Why:** a certificate that silently consumes a citation is fragile,
and one that hides a re-derivation's ancestry overclaims novelty. Both
failure modes are cheap to avoid if attribution is a *recorded*
artifact rather than a dependency. And a numerically colliding function
zoo is exactly how a future session mis-cites its own results.

**How to apply:** re-derived classical machinery ships with an
ATTRIBUTION section (recorded, not consumed) in the certificate's
docstring and exact citations in NOTES; every novelty statement names
the function and its domain, never the bare value. The disambiguation
table lives in the turn-10 notebook §5.

## D-032 · Ledgers are stated transitively, and CONTROL-ONLY is a ledger category (2026-07-27, turn 10)

Certificate 0013's first draft shipped three mutually inconsistent
floor-dependency lists (a hand-picked subset, a dash range, and a §7
note); the adversarial pass caught it. The fix: the authority for a
composed input is the consumed certificate's OWN ledger, followed
transitively (the floor = 0005/0006/0008–0012 per 0012). Separately,
0013 consumes 0009's g(5) = 13 in exactly one consistency check on a
rehearsal object — disclosed under a new ledger category, CONTROL-ONLY,
with the fail-safe direction stated (an error there can only redden the
certificate, never wrongly green it).

**Why:** "the ledger, in full" that is neither full nor unique is worse
than no ledger — it teaches readers to distrust the honest ones. And a
control that consumes a sibling certificate is a real edge in the trust
graph even when no claim stands on it; undisclosed, it looks like a
hidden input the day someone diffs the imports.

**How to apply:** one ledger, transitive, with the consumed cert's own
ledger as authority; every consumption that is not an input to a claim
gets the CONTROL-ONLY label plus its fail-safe direction.

## D-033 · Calibrate a claimed refinement at the smallest parameter before deriving (2026-07-27, turn 10)

Before the 456 audit fleet launched, the abstract transversal set-pair
maximum was computed at r = 2 by hand and machine: it is 2 = C(3,2) −
(r−1), not C(3,2) − r. That single data point proved no uniform "−r"
refinement can be a pure set-pair theorem, was handed to the fleet in
its briefing, and forced the derivation to locate exactly which
hypothesis buys the six units (the concentration lemma (*), which is
UNSATISFIABLE at r = 2 — the boundary case explains itself).

**Why:** a claimed refinement arrives shaped like a formula, and the
cheapest place a formula breaks is the smallest parameter. Twenty
minutes at r = 2 bought the audit its sharpest constraint and turned
"desk-read plausible" into "mechanism located, boundary understood."
This is D-005's compute-never-infer, sharpened to the audit of claimed
bounds: measure the CLAIM's pattern at tiny scale first. (ERRATUM
2026-07-29: this line cited "D-020", an ADR that was never issued —
the numbering skips D-020 and D-021. Caught by an internal doc sweep.)

**How to apply:** when auditing any claimed bound parametrized by r (or
m, or t), first compute the ground truth at the smallest nontrivial
parameter by exhaustion; hand the result to whoever attempts the
derivation as a constraint their proof must explain.

## D-034 · Errata against green certificates: same-commit, dated, condition-untouched (2026-07-27, turn 12)

Certificate 0016 disproved a sentence living inside green certificate
0015 — the check-18 LABEL "the floor lands at exactly X ≥ 2, not
higher", a claim about the floor where only a claim about that judge
was proven (the judge's count, alive2 == 9224, remains true). The
policy enacted: reword the label to what was actually proven, add a
dated erratum section to the certificate's NOTES naming what changed
and why, leave the check's CONDITION byte-identical, re-verify green
under both interpreters, and land the erratum in the same commit as
the certificate that forced it, which cross-references it. Append-only
artifacts (notebook entries) are never edited; their corrections live
in the later entry.

**Why:** a green transcript is the lab's word. Silently rewording it
is history-editing; leaving a refuted sentence in it is worse. The
narrow path is an erratum that is loud, dated, and provably changes no
mathematics — the condition diff is empty, the rerun is green.

**How to apply:** when new work falsifies prose inside a green
certificate, fix label + NOTES erratum + same-commit cross-ref +
rerun ×2. If new work would falsify a CONDITION, that is not an
erratum — the certificate was wrong, and it is retracted, not amended.

## D-035 · A margin is stated in the coordinate of every consumed cap, and the binding one is named (2026-07-27, turn 12)

0016's kill looked comfortable in its own coordinate — field minimum
W = 27..28 against a bound of 24 — and is knife-edge in a consumed
certificate's coordinate: W ≤ 24 alone leaves 843 configurations whose
minimum D2 is 12, exactly one above 0008's cap. One more degree-2
vertex and the theorem does not close. The refuter found it; the
certificate now quotes the (D2) sweep as THE margin and the W cliff as
secondary. Same turn, same lesson in miniature: the drafted enactment
fed size-<5 covers to 5-class Φ terms — systematically UNDERSTATING
its left side — a weakened test wearing the label of the real one;
repaired by padding to the hypothesis and re-pinning.

**Why:** D-017 demands margins be computed; this sharpens WHERE. A
kill that consumes k caps has k margin coordinates, and the flattering
one is usually not the binding one. An error (or a slack statement)
that flatters the expected answer is the worst kind a verifier makes.

**How to apply:** for every certificate consumed by a kill, run the
sensitivity sweep in THAT certificate's coordinate; name the binding
coordinate in the margin statement; and when an enactment's hypothesis
has a fixed size or count, construct the test AT the hypothesis (pad,
don't approximate) so the label and the code test the same claim.

## D-036 · Peer intake: statements in, proofs never, verbatim text to refuters (2026-07-28, turns 14–16)

The lab's intake law for outside review, settled over three turns; D-037 and
D-038 point back here.

**Turn 14 — statements only, and the deflation mirror.** The first outside audit
(GPT 5.6 Sol Pro) proposed turn 14's theorem, its field numbers matching ours
digit-for-digit. Statements and claimed constants come IN; proofs are never
ingested. The desk re-derives, blind lanes re-derive from a definitions pack
alone, refuters attack the desk versions, the certificate consumes only in-house
derivations, and the peer is credited in NOTES provenance (D-031) but cited by
zero proof steps — corroboration counted in implementations, not authority. Two
scars: the desk "corrected" the audit's path-shape bound 27 to 26 and was itself
wrong (refuters restored 27 by enumeration); and both the audit and the desk
asserted a forced census split ("one (7,7), two (8,6)") where the argument proved
only "at most one (7,7)".
**Deflating a peer's correct number inside a "correction" is the mirror image of
the flattering overclaim** — skepticism must be symmetric, and equality analyses
must ENUMERATE their dichotomies, not narrate them.

**Turn 15 — routing, when full text arrives.** The second audit came as statements
PLUS a complete proof. The desk desk-checks the received text first, before any
lane flies; blind lanes get statements and one-line mechanisms only, never the
text; the text goes only to hostile refuters. Both halves paid — two INDEPENDENT
alternative proofs from the blind lanes, a circular degree-cap step flagged by the
refuters. (ERRATUM 2026-07-28, caught by the third outside audit: the refuters
were in fact reading the DESK'S TRANSCRIPTION, not the received text, and the
circularity lived only in the transcription — the received step was valid.
The routing principle stands; the motivating example was misattributed. The
repair is D-038.)

**Turn 16 — verbatim to refuters, retained on arrival.** The retraction, in the
words it was published in: Turn 15 routed the received proof to its refuter lanes
through a desk-written transcription. The transcription restated the weight
function w = Φ(d−1, 5) — an integer at every degree — as a finite table plus the
inequality w(d) ≥ d − 6 above d = 11. Under that weakened spec, the received
proof's integer-flooring step genuinely fails; two refuters correctly flagged it;
and the desk recorded their finding as the peer's defect. The third outside audit
caught it: the received step was valid, and the lab's public record briefly
charged a correct proof with a nonexistent circularity. (The step was also INERT —
w(d) ≥ d − 6 closes d ≥ 12 against 16/3 with no integrality — so the record was
wrong twice over: false of the received text, and consequence-free even of the
transcription.) **A transcription is itself a mathematical
claim, and this one was never verified.** Hence: refuters receive the text
VERBATIM; a defect found in restated material is re-verified against the original
before it is recorded as the peer's; errata to the lab's own provenance narrative
rank with certificate errata (D-034); and **every received peer text is retained
in `notebook/raw/` on arrival**.

**Why:** the lane multiplies eyes without importing trust, and stays sound only if
the boundary — statements in, proofs never, derivations in-house — is mechanical.
Route text to sympathetic readers and you get transcription; route it to refuters
and you get defects. The blind lanes' packs are transcriptions BY DESIGN, so their
findings bind only the pack while refuters' may bind the peer. And D-017's
flattering-error law needs its mirror: an error that DEFLATES a peer's correct
claim survives review just as easily, because it wears the costume of rigor.

**How to apply:** every peer constant is reproduced in-house (>= 2 independent
implementations) before it may appear in a certificate, and every claimed theorem
is re-derived blind + refuted before its statement is consumed. NOTES must say
"full proof text received" when it was — claiming statements-only intake when text
was read is a provenance falsehood — and any defect found in the text is stated
concretely with its repair. When checking a peer bound, enumerate; never
hand-derive a smaller number and prefer it for being yours.

## D-037 — Full-text peer intake: the received proof goes only to refuters (2026-07-28, turn 15)

Merged into **D-036** (turn-15 clause), which carries this entry's routing
protocol and its ERRATUM verbatim. Kept as a pointer: cited by name in PLAN.md
and README.md.

## D-038 — A transcription is a claim: refuters read the verbatim text (2026-07-28, turn 16)

Merged into **D-036** (turn-16 clause), which carries the verbatim-routing law,
the `notebook/raw/` retention clause and the turn-15 retraction verbatim. Kept as
a pointer: cited by name in PLAN.md, README.md and certificates 0019/0020.
