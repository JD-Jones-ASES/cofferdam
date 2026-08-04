# cofferdam

> ## ⚠️ Read this first
>
> **AI disclaimer.** The mathematics in this repository was produced by AI
> systems (Anthropic Claude as the resident researcher, with other models as
> adversarial reviewers), operated by a human owner who is **not a
> mathematician** and does not vouch for the content personally. Every claim
> should be treated as machine-generated until a qualified human has checked
> it.
>
> **Beta-testing repo — work in progress.** This is a live lab notebook, not
> a publication. **No strong claims are being made.** Results are stated as
> "proven-by-certificate," meaning exactly and only: a self-contained Python
> script asserts the listed checks and exits green. Certificates have been
> wrong before; several carry dated errata for prose and label slips — the
> checks themselves stood, and the errata are part of the record. If you are
> looking for peer-reviewed mathematics, move along — if you are looking for
> something to break, welcome; start at [PLAN.md](PLAN.md) § "Where to
> attack."

A small mathematics lab working on the first open case of **Ryser's
conjecture**: r = 6, intersecting. The conjecture says τ ≤ (r−1)ν; for
intersecting r-partite r-uniform hypergraphs (ν = 1) it reads τ ≤ r−1,
proven for r ≤ 5 (Tuza) and open at r = 6. A counterexample would be a
6-partite 6-uniform intersecting hypergraph with τ ≥ 6. This repo bounds
what such an object could look like.

## If you are here to attack it

Good — that is what this repo is for, and outside audit is the reason it is
public. **The thinnest things first, so you can aim:**

- **0023's zero-slack chain**: the (7,24) triangle ties Ψ = Λ = 62 exactly
  and dies only by parity/pigeonhole gates whose shared pillar is residual
  pairing — (SJ) is *slack* there, and without (RG) the branch reaches 83
  (mutant M-RG reopens **all three** rungs). Its m = 22 ledgers close by
  one unit of profile sum; the incidence-ledger engine is a relaxation and
  the file says which two of its instances came back feasible before a
  different gate (RG) closed them.
- **0022's tightest cells**: the (2,2,2,1) triangle at (7,25) dies by ONE
  unit of the optimizer (67 vs 68); the (1⁷) wall at (7,26) sits at exactly
  Ψ = Λ = 73 and dies only by census emptiness and a capacity count; three
  shapes at (7,25) reach exactly 70 vs 68 (two units) and die only by
  equality forcing.
- **0021 has one zero-margin cell**: the (m, degrees) = (23, (10,9)) case
  clears its moment requirement at exactly Ψ = Λ = 59 and dies *only* by a
  census-and-profile count. Its three one-unit cells include the one that
  closes the whole X = 6 band (70 vs 71 at m = 26).
- **The knapsack cost convention is a named hazard**: reading the cost as
  f instead of F flips 15 cells from dead to alive (mutant M-f) — the
  fourth review computed correctly but *stated* the weaker form.
- **(D2) — certificate 0008 — is the most-consumed input in the repo.**
  A one-unit relaxation reopens 6 of 0021's cells (measured after three
  verification lanes disagreed); 0016/0018 each close by one unit of it.
- After those: the (7,27) kill's C3 triangle exclusion (without it the cell
  ties at exactly Λ), the residual-pairing bounds, and n ≥ 36.

**[PLAN.md](PLAN.md) § "Where to attack"** carries the full ranked list.
Every certificate replays with one command (see "Checking a claim" below) —
**a red run on your machine is a finding, please report it.** Margins are
documented per house law D-017/D-035 rather than hidden, each `NOTES.md`
carries its own adversarial record and OPEN flags, and the lab's error log is
public in both directions: this desk wrongly "corrected" an outside auditor's
correct bound (turn 14), and wrongly attributed a circularity to a peer's
valid proof (turn 15 — retracted, D-038). *An error that flatters the expected
answer is the failure mode this lab is built around; deflating a peer's
correct work is its mirror.*

## Where it stands (2026-08-03, turn 20)

**The problem is finite, and three excess layers fell in two turns.** Every
claim is proven-by-certificate with an **empty external-input ledger** — no
literature constant, no unreproduced lemma, no solver in the trust chain.

1. **The window** — every counterexample contains an edge-critical core, and
   every critical core has **m ∈ [22, 456]**, so the whole question is one
   finite check (0013–0014).
2. **The excess floor** — every critical core has **X ≥ 10**, at every m;
   **X = 10 forces m ≤ 25** (equivalently **m ≥ 26 ⟹ X ≥ 11**); and a
   quadratic law holds window-wide, **X ≥ ⌈m(m−25)/38⌉** — the bare law
   reads 5172 at m = 456, with 0020's (H1) **X ≥ 5173** (0019–0025).

**The frontier is X = 10 on m ∈ [22, 25]** — and its exact target list is
certified: 74 surviving (shape, part-vector) cells, no part ever larger
than 7 (0024's atlas). The X = 8 floor stands on **two disjoint proof
stacks** (quotients + ledgers + parity in 0022–0023; part-collision +
exact sweep in 0024 — neither consumes the other above 0021); the X = 8
and X = 9 layers then die in 0024's atlases, and every atlas cell is
killed by **generated support postures** in 0025 — graphs, closure,
derived caps, and three priced kill laws, never a narrated case list.

*Underneath, each still standing on its own*: the floor m ≥ 22 (0001–0012)
and the floor-local excess chain X ≥ 2/3/4 at m = 22 (0015–0018).

| attack these first | |
| --- | --- |
| [0024](certificates/0024-part-collision) | the part-collision laws above an exact codegree identity; 1,286,681 cells × two engines; the atlases; X ≠ 7 with no parity, no ledgers, no quotients |
| [0025](certificates/0025-support-postures) | X ≥ 10 · X = 10 ⟹ m ≤ 25 — postures from graphs; the spine (derived caps, (PC), the coincidence law) and the belts ((C3), J-budget) separately priced |
| [0023](certificates/0023-profile-ledgers) | the other X ≥ 8 stack: parity sieve, incidence ledgers, and a (7,24) tie with two complete independent proofs (see its twice-corrected erratum — the history is public) |
| [0013](certificates/0013-finite-window) + [0014](certificates/0014-window-456) | the window itself — nothing supersedes it, and everything rests on it |

The rest of `certificates/` — 0001–0012 (the floor) and 0015–0022 (the
excess chain) — each carry a `NOTES.md` with margins and adversarial record.

The theorems in 0018–0022 and the 0024/0025 program were proposed by outside
audits (GPT 5.6 Sol Pro, reading this public repo — six reviews) and
re-proven in-house under the peer-intake law: statements to blind derivation
lanes, received text **verbatim** to hostile refuters and retained in
`notebook/raw/`, and no proof step citing a peer ([DECISIONS.md](DECISIONS.md)
D-036). The intake keeps catching defects in **both directions**: the sixth
audit's tables verified six ways (one lane fully blind, with explicit
witnesses for all 127 surviving cells) while three of its proof steps were
refuted — including its diagnosis of a defect in 0023, which the desk
briefly imported before a hostile lane caught the over-retraction the same
day (the twice-corrected erratum in 0023's NOTES tells it straight).

A floor says where the object *cannot* be. Nothing here claims a
counterexample exists — at 22, 456, or anywhere.

## The design commitment

**No solver appears anywhere in the trust chain.** τ ≤ 5 is witnessed by
five vertices, checkable by inspection; "no such object below m edges" is
exactly the claim that every candidate has such a witness. Every checker
runs under a bare `python3` (3.9+) with no installs, prints its checks and
its **notes** (stated-not-tested facts) in separate tallies, names its
dependency ledger transitively, and states the floor it would still reach
with each dependency removed.

## Layout

```
BRIEF.md        frozen founding brief — the seed, the seal, the laws.
                Deliberately never updated: its "m ≥ 21" is the historical
                seed claim, not the current state (that lives in PLAN.md)
AGENTS.md       operating instructions; which engine to use when
PLAN.md         the living plan — state, attack list, risk decomposition
DECISIONS.md    the ADR log (D-001..D-038; D-020/D-021 never issued)
lib/            two engines (edge-wise census; column-wise existence)
certificates/   one directory per result; each has a standalone verify.py
                and a NOTES.md with margins + adversarial record
notebook/       append-only technical entries (errata recorded, never edited)
reports/        plain-language digests for the owner
```

## Checking a claim

```bash
python3 certificates/0020-strict-star-collision/verify.py
```

No arguments, no installs, no imports from `lib/`. Every green certificate
is verified on **Python 3.9** (macOS's `/usr/bin/python3`) and 3.14, under
`python3 -O` as well as plain — a checker that breaks under `-O` is not a
checker (D-015). Recent certificates run in seconds; the floor's heavy ones
(0005, 0009) take minutes and say so.

```bash
env -i HOME="$HOME" PATH=/usr/bin:/bin python3 certificates/0017-growth-laws/verify.py
```

---

Owner: JD. Researcher: the Brain (Claude); adversarial review by
multi-model fleets, with every consumed step re-derived at the desk
(Certificate Law). Licensed MIT for code; mathematical results are
unlicensed until first publication, which is the owner's call alone.

An erratum note on a published lemma (AKP Lemma 2.8, both editions read
firsthand) lives at
[notebook/2026-07-25-akp-lemma-28-erratum.md](notebook/2026-07-25-akp-lemma-28-erratum.md).
