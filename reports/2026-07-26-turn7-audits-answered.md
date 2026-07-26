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
- **Four implementations agree**, one of them blind — a subagent auditing an
  unrelated question reproduced 33/0 and 7159/0 without being told the result was
  being pursued.

## Where the exposure went

It did not vanish; it moved, and it is now sharper and cheaper to attack.

**Everything now rests on N(4) = 9 — one exhaustive search of ours, 52,023,309
nodes.** Grok called this correctly, ahead of its own headline. But its claim that
N(4) ≥ 9 has "dual support" is **wrong, and wrong in the unsafe direction**: our
corrected Lemma 2.8 derivation *consumes* that same search, so it is a consequence
of N(4) ≥ 9, never a check on it. The published AKP Lemma 2.1 would be a genuine
second leg, but we cite it and mark it "not used".

So: one search, no independent implementation anywhere. **A third implementation of
that one search is now the most valuable thing anyone could contribute to this
repo** — worth more than any further work on the literature, which is no longer
holding anything up.

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

## The seal — and this is the one thing needing your attention

**The seal is spent.** You lifted it by handing me the Grok audit, and the
condition in BRIEF §2 was met, so that was correct. But it does not come back:
you cannot un-read an argument.

Through certificate 0007 this lab's derivations are its own and were made blind.
**Nothing after this turn can claim that.** If a blind check of r = 6 is ever
wanted again, it needs a station that has not read this repo. I have recorded this
as D-011 so nobody has to rediscover it.

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
