# cofferdam — founding brief

**Frozen 2026-07-25.** Owner: JD. Researcher: the Brain (Claude), piloting this
repo directly (the scoped exception first granted for quarry, hub ADR-025).

A cofferdam is a watertight enclosure pumped dry so you can build on the
riverbed. You hold the water back in order to work on the floor. That is exactly
this repo's job, in both senses: it establishes a *floor* on the size of a Ryser
counterexample at r = 6, and it does so behind a deliberate seal that holds back
everything four other models have already said about that floor.

---

## 1. The mathematics

**Ryser's conjecture.** For an r-partite r-uniform hypergraph, τ ≤ (r−1)·ν. The
intersecting case (ν = 1) reduces to **τ ≤ r−1**, and is settled for r ≤ 5
(Tuza). **r = 6 is the first open case.** A counterexample H would be 6-partite,
6-uniform, intersecting, with τ(H) ≥ 6.

Throughout, **m** is the number of edges. Since any single edge of an
intersecting family is itself a cover of size r, τ ≤ 6 always; so a
counterexample has τ exactly 6.

**The claim under verification:**

> A minimal counterexample to Ryser's conjecture at r = 6 has **m ≥ 21** edges.

That is the entire seed. This repo was given the statement and the setup. It was
given no derivation, no certificate, and no lemma.

---

## 2. Why this repo exists, and why it is sealed

Four control planes worked r = 6 in a loose relay: quarry (this lab's
predecessor), Codex-Brain's station, Grok-Brain's Witness-Lab, and — at the
pivot — GPT 5.6 Sol Pro, which proposed m ≥ 21 by a route that did not need the
"Open Lemma" two stations had spent double-digit hours pursuing. Codex verified
that proposal with the proposal in context. Grok re-verified having seen the
chain.

**Four language models concurring is social proof, not verification.** They share
corpora and they share failure modes on long combinatorial case analyses. The
chain is correlated end to end.

This lab is the one station that fell out of the loop before the pivot, which
makes it the only one capable of a blind derivation. Bringing it current would
convert the single available independent verifier into a transcriber. So:

### The seal

The following are **sealed** and must not be read, grepped, summarised, or
delegated to a subagent, by this repo or by anyone working in it:

- `~/Downloads/GPT-Sol-Pro-Floor-Raise.md` — the proposal
- `~/Documents/repos/counterexample-research-station/` — Codex-Brain's station
- `~/Documents/Grok-Brain/`, `~/Documents/Grok-Repos/` — the Witness-Lab, W0025–W0050
- `~/Downloads/ryser-r6-status-and-path.md` §Forward-path leads beyond the statement

**The seal lifts only after this repo's own derivation is committed**, and it
lifts for one purpose: the diff. Compare final verdicts and isomorphism-class
counts. Never merge their argument into ours.

Quarry's own record through turn 16 is **not** sealed — it is this lab's own
history, and it predates the pivot. What quarry actually held at close: the
m = 20 residual class ledger was *Grok's*, intaken and pilot-verified with "deep
lemma-level clean-room NOT yet done" flagged; Codex proof-killed nine R=7
classes; 179 classes at R ≥ 8 were left undecided. So m ≥ 21 was never quarry's,
and nothing in quarry's record answers it.

---

## 3. The standing audit question

Inherited from the status note, and the highest-priority item in this repo:

> Two stations spent double-digit hours convinced the Open Lemma was the road to
> m ≥ 21. A new route arrives and doesn't need it. There are exactly two
> explanations: the new route is genuinely better, or the new route quietly
> assumes what the Open Lemma was going to prove.

A long-sought lemma becoming unnecessary is either a real result or a gap wearing
a disguise. This repo does not record m ≥ 21 as settled until that question is
answered on its own terms.

---

## 4. The terminal artifact

The deliverable is **not** a number and **not** a chain of model attestations. It
is an object that requires trusting no model:

- isomorph-free generation, replayable, with isomorphism-class counts recorded at
  each edge count so each layer is independently re-checkable;
- τ decided **exactly**, in exact arithmetic, with no SAT solver and no ILP in
  the trust chain;
- every "this candidate is not a counterexample" discharged by an **explicit
  5-cover** a reader can check by inspection.

That last point is the design's hinge. τ ≤ 5 is witnessed by five vertices; the
claim "no counterexample below 21 edges" is exactly the claim that every
candidate has such a witness. So the expensive half of the work reduces to
exhaustive generation plus a list of covers — and a solver's unsupported
"UNSATISFIABLE" never enters the argument.

---

## 5. Scope discipline

- The floor is **not the point**. Its purpose is localisation: it says where a
  counterexample cannot hide, so the frontier is where the geometry has been
  squeezed hardest. The floor says where the object **can't** be, not where it
  **is**. It could sit at 30 or 40 with nothing visible from below.
- Extract **structure, not the scalar**. The reason m must exceed a given bound
  encodes degree bounds, link conditions, forbidden sub-configurations. Those are
  reusable. The integer is not.
- Ryser is proven for **linear** intersecting hypergraphs, r ≤ 9 (Francetić,
  Herke, McKay, Wanless), so any r = 6 counterexample has two edges meeting in
  ≥ 2 vertices.
- f(r), the fewest edges in an intersecting r-partite hypergraph with τ = r−1:
  f(3)=3, f(4)=6, f(5)=9, **f(6)=13** (Aharoni–Barát–Wanless; also
  Abu-Khazneh–Pokrovskiy). Note this is the τ = r−1 regime — a *different*
  regime from τ ≥ r, and the two must never be conflated when reading a bound.
- The classical extremal object at r = 6 is truncated PG(2,5): 25 edges, 30
  vertices, τ = 5. **Do not seed searches from it** — it is rigid, and τ tends to
  break before it rises. Seed from the sparse family instead; f(6)=13 shows τ=5
  is reachable far below 25, so density is not what obstructs a high cover
  number.

---

## 6. Laws

Inherited from quarry, deliberately and with one addition.

**Certificate Law.** Every claimed result ships as (a) the statement, (b) the
explicit artifact, (c) a standalone checker — exact arithmetic, one command, no
harness imports, **stdlib only** so it runs under a bare `python3` — and (d) an
honesty label: PROVEN-BY-CERTIFICATE / PROVEN-MODULO-CITATION /
COMPUTATIONAL-EVIDENCE / NEGATIVE-SEARCH / CONJECTURE. Nothing is presented above
its label. Subagent output is fleet-claimed until re-derived here.

**No-Noise Law.** Searches run only inside frames where every solution is a
meaningful object. Blind enumeration requires a written hypothesis, budget, and
kill criterion *before* the run. Every search ends in a verdict: an object, or an
inconsistency certificate filed as a lemma — never discarded.

**Seal Law** (new, and constitutional). See §2. A derivation that has touched the
sealed material is not this lab's derivation, and the lab's entire value is that
its derivation is its own. Violating the seal is not a mistake to be corrected
later; it is unrecoverable, because you cannot un-read an argument.

**Cited-input discipline.** Any external constant the floor leans on (f(6)=13 and
its kin) must be recorded as a named dependency with its own line in the
certificate, so that a reader can see exactly how much of the result rests on
literature and how much is ours. Prefer a self-derived weaker bound to a cited
stronger one when the weaker one suffices.

---

## 7. What must not happen

- Seeding this repo with the existing certificate chain.
- Bringing this lab current by feeding it W0025–W0050.
- Recording m ≥ 21 as settled before §3 is answered.
- Presenting a floor derived from cited constants as self-contained.
