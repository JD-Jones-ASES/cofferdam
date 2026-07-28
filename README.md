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

## Where it stands (2026-07-28)

**The problem is finite, and the shape of a counterexample is pinned from
five sides.** Every claim below is proven-by-certificate with an **empty
external-input ledger** — no literature constant, no unreproduced lemma, no
solver anywhere in the trust chain.

1. **The floor**: any counterexample has **m ≥ 22 edges**
   (certs 0001–0012, eleven green certificates culminating in the pinned
   degree ladder).
2. **The window**: every counterexample contains an edge-critical core, and
   every critical core has **m ∈ [22, 456]** — so the whole question is one
   finite check (certs 0013–0014: a Katona-style disjoint-events argument,
   then part-confinement in Λ⁶(R¹¹)).
3. **The excess floor, window-wide** (cert 0019): **every critical core has
   X ≥ 5**, at every m in the window — and **X = 5 is only possible at
   m ≤ 26**, so **m ≥ 27 forces X ≥ 6**. Two counting lemmas carry it (the
   defect-hub bound Δ ≤ 5 + X and the star-collision inequality D ≤ R) plus
   a census engine: 3,056 exhaustive runs, every one empty. The earlier
   floor-local chain still stands on its own (0015–0016: X ≥ 2, X ≥ 3 at
   m = 22; 0018: the eight-shape census gives X ≥ 4 there — now also a
   corollary of 0019, which does not consume it).
4. **The growth laws** (cert 0017): excess grows across the whole window —
   X ≥ 10 from m = 38, X ≥ 100 from m = 108, and **X ≥ 2259 at the ceiling
   m = 456** (a linear law from the cover structure, an integrality lift,
   and a second-moment Jensen law).
5. **The frontier**: **X = 5 on m ∈ {22,…,26}** — the only place a
   minimum-excess core can live, five excess partitions in all. The
   12,171-configuration X = 4 field of turn 14 closed **without enumerating
   a single configuration**, and the window no longer has any
   arithmetic-free rung.

| cert | one line |
| --- | --- |
| [0001–0012](certificates/) | the floor m ≥ 22, citing nothing (see each NOTES.md) |
| [0013](certificates/0013-finite-window) | the window [22, 462]; Ryser r = 6 intersecting ⟺ no critical core in the window |
| [0014](certificates/0014-window-456) | part-confinement → **[22, 456]** |
| [0015](certificates/0015-cc-x-floor) | (CC) + **X ≥ 2** at m = 22 (margin: one unit) |
| [0016](certificates/0016-ccplus-x3) | the triangle lemma + (CC⁺) → **X ≥ 3** at m = 22 (margin: one unit of the (D2) cap) |
| [0017](certificates/0017-growth-laws) | the corner ladder ((CC⁺) holds through X ≤ 4) + the linear and second-moment **growth laws** across the window |
| [0018](certificates/0018-x4-floor) | the eight-shape census empties the X = 3 layer → **X ≥ 4** at m = 22 (margin: one unit of (D2) again; two shapes at zero W-slack, killed by census clash) |
| [0019](certificates/0019-star-collision) | the defect-hub + star-collision lemmas → **X ≥ 5 everywhere; X = 5 ⟹ m ≤ 26; m ≥ 27 ⟹ X ≥ 6** (margins: m = 27/28 kill at zero slack by divisibility; the X = 4 max-2 cell at m = 22 is the named pressure point) |

The theorems in 0018 and 0019 were both **proposed by outside audits**
(GPT 5.6 Sol Pro, reading this public repo — one day apart) and re-proven
entirely in-house under the peer-intake laws (D-036/D-037): statements to
blind derivation lanes, received proof text only to hostile refuters, the
desk re-deriving everything before anything is consumed. 0019's intake also
caught and repaired a circular step in the received proof — agreement on a
statement is not agreement on a proof. The outside-audit lane this repo
went public for is live and has produced two theorems in two days.

A floor says where the object *cannot* be. Nothing here claims a
counterexample exists — at 22, 456, or anywhere.

## If you are here to attack it

Good — that is what this repo is for, and outside audit is the reason it is
public. **[PLAN.md](PLAN.md) § "Where to attack"** carries the ranked list
(what rests on the most, checked the least). Standing invitations:

- **Replay any certificate**: one command each, all sub-minute except the
  floor's heavy ones (see "Checking a claim" below). A red run on your
  machine is a finding; please report it.
- **Attack the newest first**: 0019's two thinnest rungs (m = 27, 28) kill
  at **zero slack** — D is forced to equal R = 14 exactly, and the kills
  are divisibility facts, not size — and its named pressure-point cell
  (X = 4 max-2 at m = 22) **revives under five of its nine mutants**, each
  a one-unit move. Its measured (D2) exposure is exactly three
  configurations, all named. 0018's field side closes by one unit of (D2);
  0016 the same one layer down. All margins are documented per house law
  D-017/D-035 rather than hidden; **the (D2) cap (cert 0008) and 0019's
  degree caps are the highest-leverage things an outside reader can
  scrutinise.**
- **The known soft spots are listed, not buried**: each certificate's
  NOTES.md carries its adversarial record, its margins in every consumed
  coordinate, and its OPEN flags (e.g. whether (CC⁺)'s end-to-end
  conclusion survives at X = 5 is **open**; the c = 1 corner dies there —
  witness in 0017 — while the 4/3 rung holds).
- The lab's own error log is public: guessed constants caught by runs, a
  Φ(8,5) miscomputation caught by the fleet, dated prose/tally errata
  (D-034), and turn 14's pair — the desk wrongly "corrected" an outside
  auditor's correct bound (27 → 26; three refuter lanes restored it) and
  missed an equality subcase both it and the auditor's summary skipped —
  see DECISIONS.md (D-036) and the notebook. An error that flatters the
  expected answer is the failure mode this lab is built around; a
  deflation of a peer's correct number is its mirror.

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
DECISIONS.md    the ADR log (D-001..D-036)
lib/            two engines (edge-wise census; column-wise existence)
certificates/   one directory per result; each has a standalone verify.py
                and a NOTES.md with margins + adversarial record
notebook/       append-only technical entries (errata recorded, never edited)
reports/        plain-language digests for the owner
```

## Checking a claim

```bash
python3 certificates/0016-ccplus-x3/verify.py
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
