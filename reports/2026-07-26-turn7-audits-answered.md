# cofferdam — turn 7 digest, 2026-07-26

Plain language. For JD.

## The headline

**Both audits are answered. Nothing in them broke the floor — and the floor got
stronger.** m ≥ 21 is now **PROVEN-BY-CERTIFICATE, citing nothing.** The single
literature dependency the whole repo was built around is gone.

That is not a bigger number. It is the same number, standing on nothing external.

## What the two labs found, adjudicated

Both concluded m ≥ 21 survives. **That agreement is exactly the correlated social
proof the seal was built to distrust**, so every claim was re-derived here from
the code, the run, or the paper — not from their reports. Eleven verification
agents, all carrying the seal, plus my own runs.

**Codex filed twelve items. All twelve check out.** Five needed real repairs:

| what | verdict |
| --- | --- |
| a false displayed identity in cert 0006 (the δ layer-cake dropped a term) | **real** — and sharper than Codex put it: the certificate's *own shipped 5-edge witness* falsifies it, reading 3 where D = 4 |
| cert 0005 dies under `python3 -O` | **real** — side-effecting `assert`s get stripped; three other certificates *advertise* a no-assert rule that 0005 broke |
| we claimed AKP Lemma 2.8 but proved only half of it | **real, and the half we skipped was the load-bearing one** |
| thirteen "checks" across four certificates were literal `True` | **real** — one of them was an *input* to the m ≥ 21 arithmetic |
| the erratum was scoped to arXiv only | **real** — the journal version repeats the error, verified by rendering the scanned PDF |

**Grok found no defect, and its numbers are flawless.** I reproduced every one:
32 profiles, 105 multisets, the 91/14 kill split, the dead-heat arithmetic, and
its 7008/151 split under the weakened cap. All exact.

It made **one wrong inference and one wrong hedge**:

- It concluded that killing m = 20 without the citation "would give m ≥ 21 with no
  literature citation". **That does not follow** — our citation-free floor was
  m ≥ 19, which leaves m = 19 *standing*. Killing m = 20 alone leaves the floor at
  19.
- It hedged that our "only two level structures, needing 13 and 9" might be a
  sampling artefact. It is not; the Diophantine system has exactly two solutions.
  On that point the audit was *behind* the artifact it was auditing.

## The thing worth having, which is not in either report

Grok's inference was wrong. **Its experiment was the best thing anyone
contributed.** Nobody had run (L8) at m = 19 on the weak ladder. I ran it: all 33
configurations die. With m = 20 also dying (7159 configurations, all dead), the
citation drops out entirely.

So **certificate 0007** now proves m ≥ 21 citing nothing, sweeping m = 12..20
itself. The controls matter more than usual here, because this result *upgrades our
own label* — the most dangerous direction an error can point (D-005):

- **Not too strong**: m = 21 still leaves survivors under the same weak ladder. Had
  it killed 21 too, it would be "proving" Ryser at r = 6 and would be wrong.
- **Right direction**: the weaker rung admits **more** configurations (7159 against
  105) and still kills all of them. A result obtained by *loosening* an input
  cannot be an artefact of that input.
- **Sensitivity**: falsify N(4) = 9 to 8 and m = 20 comes back to life. So the kill
  genuinely rests on what we say it rests on.
- **Three implementations agree**, one of them blind — a subagent auditing an
  unrelated question reproduced 33/0 and 7159/0 without being told the result was
  being pursued.

## The false-kill hunt — no hole, but the reassurance was half a story

Both audits argued that every relaxation in (L8) makes survival *easier*, so a
total kill is conservative and a false kill would need an over-strong step. A
dedicated adversarial pass tested that to destruction and **found no false kill** —
loop bounds hold with room, the greedy minimum equals the exact one, the δ-budget
never overstates. The result stands.

Two things it found anyway, both worth having:

- **The margin is exactly one.** The tightest point in the whole m = 20 kill is
  the (7,…,7) dead heat: D = 8 against a need of 9, with the need exact rather
  than a bound. Three inputs flip the result if moved a single unit. "Conservative"
  and "robust" are different claims, and we had been reporting only the first.
- **The relaxation argument covers half the pipeline.** Everything inside (L8) is
  a relaxation and is safe. But the configurations it is handed come from
  `profiles()`, which *restricts* — and that is the only place a false kill could
  live. Both audits, and our own notes, gave that half a free pass.

Which sharpens the ranking rather than softening it: the weakest step is not in
(L8) at all. It is N(4) = 9. (Recorded as D-017.)

## What neither audit examined — and it was the repo's own #1 target

A completeness pass asked what *both* auditors had left alone. The answer was
uncomfortable: **neither touched N(4) = 9**, which our own PLAN and README both
named as the single load-bearing step with no independent check. Grok *identified*
it as the hinge, which is not the same as testing it — and its claim that N(4) ≥ 9
has "dual support" is wrong in the unsafe direction, since our corrected Lemma 2.8
*consumes* that same search and is therefore downstream of it.

So the pass did the missing work. **N(4) ≥ 9 is now confirmed by a second,
structurally different exhaustion** — 1505 candidate columns against our 2220,
5.7M nodes against our 52.0M, same verdict. And it is a *better* control than
ours, because it **exhibits what it rejects: 8648 full pair-covers built, every
one at τ = 3.** Ours returns "None" and a node count, and a node count is a claim
about effort, not coverage — an under-enumerating search and a correct search on
an empty space look identical from outside. One that hands you 8648 near-misses
does not. (D-018.)

It also caught **a vacuous check sitting exactly at the funnel point**: the test
licensing the pin of that whole exhaustion to profile (2,2,2,2) was a filter over
a hardcoded one-element list, so it could not fail. True claim, untested. It now
enumerates. And two overclaims of my own in cert 0007, including — with some
irony — a stated-not-tested check under a line asserting the certificate had none.

## Where the exposure went, and what carries what

Ablation relocated the risk, and it is not where anyone was looking:

| step | what fails without it |
| --- | --- |
| **(L7)** and the **excess budget X** | everything — 100% survive at every m |
| **N(4) = 9** | m = 20 revives |
| the δ-budget | **only m = 20**; the floor would drop to m ≥ 20, still citing nothing |
| the concentration ceiling U | nothing — **inert** |

Both audits ranked the δ-budget as the thing to attack. So did we. It is the
newest inequality and the least checked — and also the one that can cost the
least. **(L7) and X carry everything and appeared on nobody's list**, precisely
because they are old, simple and were never in doubt. "Newest and least checked"
turns out to be a proxy for *attention*, not for *load*. (D-019.)

## What else changed in the repo

- **The corrected AKP Lemma 2.8 is now proven in full**, both halves. The global
  clause — at most one part is type B — is the one AKP's own Lemma 2.9 leans on,
  with a margin of *one* (7 + 6·4 = 31 against 32 required). It cost 52 seconds.
- **Certificate 0005 is green under `-O`** and ~5 minutes faster, because it no
  longer repeats its own 52M-node search.
- **Checks and notes are now tallied separately** everywhere. A "note" is a stated
  fact, not a machine test. Honest counts replaced inflated ones.
- Certificate 0006 now **computes** the 6198-of-43875 control it used to only
  assert, and its range checks cover the ranges their labels claim.
- The erratum covers both editions. The journal text is a re-typeset, so the error
  passed a copy-editing pass into the version of record.

## What I did not do

I have **not** replied to Codex's issue. A draft response is ready — publishing
and outward correspondence are yours (AGENTS.md §Session shape). Say the word and
I will post it, or you can send it yourself.

## Two commands

```bash
cd ~/Documents/repos/cofferdam && python3 certificates/0007-citation-free-floor/verify.py
```

```bash
cd ~/Documents/repos/cofferdam && python3 -O certificates/0006-excess-concentration/verify.py
```
