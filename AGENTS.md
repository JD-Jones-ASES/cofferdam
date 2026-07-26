# cofferdam — operating instructions

The lean rebuild of the Ryser r = 6 floor. Read [BRIEF.md](BRIEF.md) first — it is
frozen, and it is the founding statement of what this repo is for. Its §2 (the
seal) has since been opened; see below.

## The seal

Certificates 0001–0007 were derived without reading any peer derivation. The seal
has since been opened, so this repo is no longer a blind verifier — don't present
it as one. How the lab takes in peer work is a Brain-level question and lives
there. Here, the mathematics.

## Routing

| You are here to… | Read, in order |
| --- | --- |
| Continue the derivation | [PLAN.md](PLAN.md) → latest `notebook/` entry |
| Check a claimed result | its `certificates/` dir → run `verify.py` |
| Understand the founding | [BRIEF.md](BRIEF.md) → [DECISIONS.md](DECISIONS.md) |
| Brief JD | `reports/` (latest first) — plain language, ends with the one command |
| Use the machinery | `lib/ryser.py` (edge-wise) · `lib/columns.py` (column-wise) |

## The laws

Certificate Law · No-Noise Law · **Seal Law** · Cited-input discipline — all four
stated in [BRIEF.md](BRIEF.md) §6. Two operational consequences worth repeating:

- **Checkers are stdlib-only.** `python3 verify.py` from a clean shell, no
  installs, no venv, no imports from `lib/`. A certificate that needs the repo's
  own library to check itself is not a certificate.
- **Cited constants are named dependencies.** Every certificate prints its
  external inputs and states the floor it would still reach with each one
  removed. A result must never look more self-contained than it is.

## Two engines, and when to use which

`lib/ryser.py` — **edge-wise**. Builds a hypergraph one edge at a time and dedups
by canonical form. General, gives isomorphism-class counts per edge count, and is
the right tool for classification. It is also slow: r = 6 costs ~3 minutes by
m = 5, because canonicalisation runs over all 6! part orders.

`lib/columns.py` — **column-wise**. Represents the hypergraph as r partitions of
the edge set: a block is a vertex, its size is that vertex's degree, intersecting
means the partitions jointly cover all pairs of edges, and τ is the least number
of blocks covering the edge set. Answers existence questions ("is τ ≥ t reachable
on m edges?") in milliseconds where the edge-wise engine takes minutes, because

1. the search is an exact-cover over *pairs* — branch on the least uncovered pair
   and only consider partitions that join it;
2. the degree cap bounds block size, pruning the partition list before the search
   starts;
3. **τ is monotone non-increasing in the columns fixed so far** — adding a column
   only adds blocks, which can only make covering easier — so a partial column
   set that already admits a (t−1)-cover kills its whole branch.

Use the column-wise engine for the ladder rungs; use the edge-wise engine when
the deliverable is a census rather than a yes/no.

## Session shape

1. Re-read the seal. Confirm nothing in the session's plan requires breaking it.
2. Work the agreed scope in PLAN.md. Notebook entries are append-only, dated,
   technical. A dead end is a result and gets written down as one.
3. Close: digest in `reports/`, PLAN.md revised, commit.
4. Publishing anything, anywhere, is JD's line — always.

## Toolchain

**Certificates must run on the OLDEST `python3` a reader plausibly has, not the
newest on this box.** macOS ships **3.9.6** at `/usr/bin/python3`, and a bare
`python3` in a clean environment finds that one — so `int.bit_count()` (3.10+),
`match`, and friends are out. Bind a fast path behind `hasattr` and fall back.
Test with `env -i HOME="$HOME" PATH=/usr/bin:/bin python3 certificates/<id>/verify.py`;
the six green certificates are verified under 3.9 AND under `python3 -O` (0004 is never-green scaffolding). "Runs under a bare python3" is a
claim about someone else's machine, so it has to be tested against one.

python.org / Homebrew `python3`, stdlib only for anything that ships. `nauty` is
installed on this box (`/opt/homebrew/bin`: `dreadnaut`, `labelg`, `shortg`, …)
and may be used for **cross-validating** canonical forms, never as a dependency
of a certificate. `pip install` into the system Python is blocked by PEP 668 on
this machine — treat that as a feature, since it keeps checkers honest.
