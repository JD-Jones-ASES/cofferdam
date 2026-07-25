# cofferdam

A small, deliberately sealed lab establishing a **floor** on the size of a
counterexample to Ryser's conjecture at r = 6 — the first open case.

Ryser's conjecture says τ ≤ (r−1)ν. In the intersecting case (ν = 1) that reads
τ ≤ r−1, proven for r ≤ 5 (Tuza) and open at r = 6. A counterexample would be a
6-partite 6-uniform intersecting hypergraph with τ ≥ 6. The question here is how
few edges such an object could possibly have.

## Why a cofferdam

A cofferdam is a watertight enclosure pumped dry so you can build on the
riverbed — you hold the water back in order to work on the floor. This repo does
both. Four other stations have already produced a proposed floor by a correlated
chain; this lab was given the *statement* and nothing else, and derives its own.
[BRIEF.md](BRIEF.md) §2 names exactly what is sealed and why the seal is
constitutional rather than a preference.

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
