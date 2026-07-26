# cofferdam

A small, deliberately sealed lab establishing a **floor** on the size of a
counterexample to Ryser's conjecture at r = 6 — the first open case.

Ryser's conjecture says τ ≤ (r−1)ν. In the intersecting case (ν = 1) that reads
τ ≤ r−1, proven for r ≤ 5 (Tuza) and open at r = 6. A counterexample would be a
6-partite 6-uniform intersecting hypergraph with τ ≥ 6. The question here is how
few edges such an object could possibly have.

## Where it stands

**A Ryser r=6 intersecting counterexample has at least 21 edges.**
PROVEN-MODULO-CITATION, the citation being f(6) ≥ 13 (Abu-Khazneh–Pokrovskiy
Theorem 1.1; independently Aharoni–Barát–Wanless), which enters at exactly one
place. Without it the floor is 19.

| certificate | result |
| --- | --- |
| [0001](certificates/0001-degree-cap-ladder) | the degree-cap ladder; g(1..4) = 1,3,5,8, each proven twice → m ≥ 18 citing nothing |
| [0002](certificates/0002-delta-window) · [0003](certificates/0003-low-incidence) | the maximum-degree window; the low-incidence bound |
| [0005](certificates/0005-min-degree-ladder) | the **minimum-degree ladder** → m ≥ 19 citing nothing, **m ≥ 20** citing f(6)=13; and the corrected AKP Lemma 2.8, proven sharp |
| [0006](certificates/0006-excess-concentration) | **(L8) excess-concentration** → m = 20 impossible, so **m ≥ 21** |

A floor says where the object *cannot* be, not where it is. Nothing here claims a
counterexample exists at 21 or above.

## If you are here to attack it

Good — that is what it is for. **[PLAN.md](PLAN.md) § "Where to attack this"**
carries a ranked list: what rests on the most, checked the least. Two shortcuts
worth knowing before you start:

- The load-bearing control on certificate 0006 is that the identical machinery, run
  at m = 21, leaves 6198 of 43875 configurations alive. Had it killed every m it
  would be "proving" Ryser at r = 6 and would therefore be wrong. If you can break
  that control, you have broken the certificate.
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

---

Owner: JD. Researcher: the Brain (Claude). Licensed MIT for code; results are
unlicensed until first publication, which is the owner's call alone.

An erratum note on a published lemma lives at
[notebook/2026-07-25-akp-lemma-28-erratum.md](notebook/2026-07-25-akp-lemma-28-erratum.md).
Read its first paragraph before citing it: the claim is scoped to **arXiv:1409.4938v1**,
the only version on arXiv, and the reported 2017 journal text has **not** been checked.
