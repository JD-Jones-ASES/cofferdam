# cofferdam

A small, deliberately sealed lab establishing a **floor** on the size of a
counterexample to Ryser's conjecture at r = 6 — the first open case.

Ryser's conjecture says τ ≤ (r−1)ν. In the intersecting case (ν = 1) that reads
τ ≤ r−1, proven for r ≤ 5 (Tuza) and open at r = 6. A counterexample would be a
6-partite 6-uniform intersecting hypergraph with τ ≥ 6. The question here is how
few edges such an object could possibly have.

## Where it stands

**A Ryser r=6 intersecting counterexample has at least 21 edges.**
**PROVEN-BY-CERTIFICATE, citing nothing.** There is no external input: no
literature constant, no unreproduced lemma, no solver.

| certificate | result |
| --- | --- |
| [0001](certificates/0001-degree-cap-ladder) | the degree-cap ladder; g(1..4) = 1,3,5,8, each proven twice → m ≥ 18 citing nothing |
| [0002](certificates/0002-delta-window) · [0003](certificates/0003-low-incidence) | the maximum-degree window; the low-incidence bound |
| [0005](certificates/0005-min-degree-ladder) | the **minimum-degree ladder** → m ≥ 19 citing nothing, **m ≥ 20** citing f(6)=13; and the corrected AKP Lemma 2.8, both halves |
| [0006](certificates/0006-excess-concentration) | **(L8) excess-concentration** → m = 20 impossible, so **m ≥ 21** citing f(6)=13 |
| [0007](certificates/0007-citation-free-floor) | **the citation is unnecessary** — (L8) run on the weaker rung N(5) ≥ 11, which is ours, kills every m ≤ 20 → **m ≥ 21 citing nothing** |

0007 is the load-bearing one now. It runs the same machinery on a *strictly
weaker* input — 7159 admissible configurations at m = 20 rather than 105 — and
still kills everything, so the floor cannot be an artefact of the cited constant.
It also sweeps m = 12..20 itself rather than inheriting a lower range.

A floor says where the object *cannot* be, not where it is. Nothing here claims a
counterexample exists at 21 or above.

## If you are here to attack it

Good — that is what it is for. **[PLAN.md](PLAN.md) § "Where to attack this"**
carries a ranked list: what rests on the most, checked the least. Two shortcuts
worth knowing before you start:

- **Hit N(4) = 9 first.** Since 0007 removed the citation, the single load-bearing
  step in the whole repo is one exhaustive search of ours — 52,023,309 nodes,
  ρ=8 pinned to (2,2,2,2). An under-enumerating search fakes a proof, and 0007's
  sensitivity check prices it exactly: set N(4) = 8 and m = 20 comes back to life.
  A third independent implementation is the most valuable thing anyone could
  contribute. Do not attack the literature — it is no longer holding anything up.
- The load-bearing control on 0006 and 0007 is that the identical machinery, run
  at m = 21, leaves 6198 of 43875 configurations alive. Had it killed every m it
  would be "proving" Ryser at r = 6 and would therefore be wrong. If you can break
  that control, you have broken the certificates.
- 0006's ceiling was deliberately weakened to the crudest concentration bound, so an
  earlier value-pool argument is **no longer in the trust chain** — don't spend time
  on it.

The standing law here is that a search which under-enumerates fakes a proof, so
every "no such object exists" ships with its completeness argument and is validated
first on targets with known answers. Those are the joints to lever.

## Why a cofferdam

A cofferdam is a watertight enclosure pumped dry so you can build on the
riverbed — you hold the water back in order to work on the floor. This repo does
both. Three labs worked r = 6 in parallel; this one fell behind, was given the *statement*
and nothing else, and re-derives rather than transcribes. [BRIEF.md](BRIEF.md) §2
names exactly what is sealed and why the seal is constitutional rather than a
preference. The pointers that opened certificates 0005 and 0006 came from Codex; the
proofs, searches, machinery and controls are this repo's.

## The design commitment

**No solver appears anywhere in the trust chain.** τ ≤ 5 is witnessed by five
vertices, which any reader checks by inspection; "no counterexample below m
edges" is exactly the claim that every candidate has such a witness. So the
expensive half of the work is exhaustive generation plus a list of explicit
covers. Nothing rests on a SAT solver's unsupported word, and every checker runs
under a bare `python3` with no installs.

## Layout

```
BRIEF.md        frozen founding brief — the seed, the seal, the laws
AGENTS.md       operating instructions; which engine to use when
PLAN.md         the living plan
lib/ryser.py    edge-wise engine: canonical forms, exact tau, census
lib/columns.py  column-wise engine: the hypergraph as r partitions of the
                edge set — orders of magnitude faster for existence questions
certificates/   one directory per result; each has a standalone verify.py
notebook/       append-only technical entries
reports/        plain-language digests for the owner
```

## Checking a claim

Every certificate is self-contained:

```bash
python3 certificates/0001-degree-cap-ladder/verify.py
```

No arguments, no installs, no imports from `lib/`. It prints its own checks, its
external dependencies, and the floor it would still reach with each dependency
removed.

The **six green certificates** (0001, 0002, 0003, 0005, 0006, 0007) are verified on
**Python 3.9** — the version macOS ships as `/usr/bin/python3` — as well as on 3.14,
and under **`python3 -O`** as well as plain `python3`. A checker that is green
normally and broken under `-O` is not a checker (D-015), and 0005 was exactly that
until 2026-07-26. 0004 is never-green scaffolding and is labelled as such. Note the
runtimes: certificate 0005 takes ~7.5 min on Python 3.10+ and considerably longer on
3.9, where it falls back to a slower popcount. It is slow, not hung.

Each certificate prints **checks** and **notes** separately. A note is a stated fact
— a citation, or a step proved by hand — and is *not* machine-tested; keeping the two
tallies apart is what stops a check count from implying a test that never ran.

```bash
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 certificates/0006-excess-concentration/verify.py
```

---

Owner: JD. Researcher: the Brain (Claude). Licensed MIT for code; results are
unlicensed until first publication, which is the owner's call alone.

An erratum note on a published lemma lives at
[notebook/2026-07-25-akp-lemma-28-erratum.md](notebook/2026-07-25-akp-lemma-28-erratum.md).
It is now scoped to **both** editions — arXiv:1409.4938v1 and the version of record,
*JCMCC* **103** (2017) 81–104 — each read firsthand. The journal PDF is an image-only
scan with no text layer, which is why a text-based check of it comes back empty; that
is not evidence of absence.
