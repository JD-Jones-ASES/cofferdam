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

- **0020's staircase has exactly one cell the arithmetic cannot kill** —
  (X, m, partition) = (8, 30, (3,3,1,1)) — closed only by a structural
  profile argument whose key constraint (every high-degree vertex lies in at
  least two shared sets) is *measured* load-bearing: drop it and the kill
  genuinely fails (mutant M10, 1090 > 1066).
- **The thinnest arithmetic kill is 2 units**, at (8,30,(3,2,2,1)); 0019's
  m = 27 and m = 28 rungs kill at **zero** slack, by divisibility alone.
- **(D2) — certificate 0008 — is the most-consumed input in the repo.**
  0020's X ≥ 6 floor needs it at m = 22–23 (11 cells reopen without it), and
  0016/0018 each close by one unit of it.
- After those: the strict-lemma guard τ ≥ q_max + 2, and n ≥ 36.

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

## Where it stands (2026-07-29)

**The problem is finite, and the excess floor is now window-wide.** Every
claim is proven-by-certificate with an **empty external-input ledger** — no
literature constant, no unreproduced lemma, no solver in the trust chain.

1. **The window** — every counterexample contains an edge-critical core, and
   every critical core has **m ∈ [22, 456]**, so the whole question is one
   finite check (0013–0014).
2. **The excess floor** — every critical core has **X ≥ 6**, at every m, with
   a staircase above it (**m ≥ 27 ⟹ X ≥ 7 · m ≥ 29 ⟹ X ≥ 8 · m ≥ 30 ⟹
   X ≥ 9 · m ≥ 32 ⟹ X ≥ 10**) and a quadratic law window-wide,
   **X ≥ ⌈m(m−25)/38⌉**, which reads **X ≥ 5173 at m = 456** (0019–0020).

**The frontier is X = 6 on m ∈ {22,…,26}**, the minimum-excess band. No rung
of the window is arithmetic-free, and every layer X ≤ 5 is empty at every m.

*Underneath, each still standing on its own*: the floor m ≥ 22 (0001–0012)
and the floor-local excess chain X ≥ 2/3/4 at m = 22 (0015–0018).

| attack these first | |
| --- | --- |
| [0020](certificates/0020-strict-star-collision) | X ≥ 6 everywhere · the staircase · the quadratic law — the newest, and the thinnest |
| [0013](certificates/0013-finite-window) + [0014](certificates/0014-window-456) | the window itself — nothing supersedes it, and everything rests on it |
| [0008](certificates/0008-degree-two-cap) | the (D2) cap — the most-consumed input in the chain |

The rest of `certificates/` — 0001–0012 (the floor) and 0015–0019 (the excess
chain) — each carry a `NOTES.md` with margins and adversarial record.

The theorems in 0018–0020 were proposed by outside audits (GPT 5.6 Sol Pro,
reading this public repo) and re-proven in-house under the peer-intake law:
statements to blind derivation lanes, received text **verbatim** to hostile
refuters and retained in `notebook/raw/`, and no proof step citing a peer
([DECISIONS.md](DECISIONS.md) D-036).

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
