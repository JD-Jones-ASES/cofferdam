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
3. **The excess floor, window-wide** (certs 0019–0020): **every critical
   core has X ≥ 6**, at every m in the window — and a **staircase** above
   it: **m ≥ 27 forces X ≥ 7, m ≥ 29 forces X ≥ 8, m ≥ 30 forces X ≥ 9,
   m ≥ 32 forces X ≥ 10**. The machinery is a family of counting lemmas
   (the defect-hub bound; the balanced form F(d) ≤ s(z); the **strict**
   form F + q_max ≤ s, whose extra unit is what empties X = 5; the global
   P + H ≤ R) driving exhaustive census engines — 3,056 runs in 0019,
   35 + 92 cells in 0020, one structural kill. The earlier floor-local
   chain (0015–0018) still stands on its own underneath.
4. **The growth laws** (certs 0017 + 0020): excess grows **quadratically**
   across the window — **X ≥ ⌈m(m−25)/38⌉** everywhere (cert 0020's law
   m(m−25) + Σ₅ + 10H ≤ 38X), which reads **X ≥ 5173 at the ceiling
   m = 456** — more than double 0017's Jensen bound there, and itself
   provably far from tight.
5. **The frontier**: **X = 6 on m ∈ {22,…,26}** — the minimum-excess band.
   The window has no arithmetic-free rung, and every layer X ≤ 5 is empty
   at every m.

| cert | one line |
| --- | --- |
| [0001–0012](certificates/) | the floor m ≥ 22, citing nothing (see each NOTES.md) |
| [0013](certificates/0013-finite-window) | the window [22, 462]; Ryser r = 6 intersecting ⟺ no critical core in the window |
| [0014](certificates/0014-window-456) | part-confinement → **[22, 456]** |
| [0015](certificates/0015-cc-x-floor) | (CC) + **X ≥ 2** at m = 22 (margin: one unit) |
| [0016](certificates/0016-ccplus-x3) | the triangle lemma + (CC⁺) → **X ≥ 3** at m = 22 (margin: one unit of the (D2) cap) |
| [0017](certificates/0017-growth-laws) | the corner ladder ((CC⁺) holds through X ≤ 4) + the linear and second-moment **growth laws** across the window |
| [0018](certificates/0018-x4-floor) | the eight-shape census empties the X = 3 layer → **X ≥ 4** at m = 22 (margin: one unit of (D2) again; two shapes at zero W-slack, killed by census clash) |
| [0019](certificates/0019-star-collision) | the defect-hub + star-collision lemmas → **X ≥ 5 everywhere; X = 5 ⟹ m ≤ 26** (margins: m = 27/28 kill at zero slack by divisibility) |
| [0020](certificates/0020-strict-star-collision) | the **strict** star-collision family (q ≤ 3 · F ≤ s · F + q_max ≤ s · P + H ≤ R) → **X ≥ 6 everywhere; the staircase; the quadratic law X ≥ ⌈m(m−25)/38⌉, X ≥ 5173 at m = 456** (92-cell staircase sweep (D2)-free; one structural kill, its key constraint measurably load-bearing) |

The theorems in 0018, 0019 and 0020 were all **proposed by outside audits**
(GPT 5.6 Sol Pro, reading this public repo — three reviews in two days) and
re-proven entirely in-house under the peer-intake laws (D-036/D-037/D-038):
statements to blind derivation lanes, received proof text **verbatim** to
hostile refuters and retained in `notebook/raw/`, the desk re-deriving
everything before anything is consumed. The lane's record is honest in both
directions: turn 15 briefly misattributed a circularity to the second
review's valid proof (the defect was in the desk's own transcription — the
third review caught it, the record is corrected everywhere, and the law it
bought is D-038), and the third review's own proof carried one real gap (an
incomplete case list at one staircase cell), found independently by three
refuter lanes and repaired in-house before certification.

A floor says where the object *cannot* be. Nothing here claims a
counterexample exists — at 22, 456, or anywhere.

## If you are here to attack it

Good — that is what this repo is for, and outside audit is the reason it is
public. **[PLAN.md](PLAN.md) § "Where to attack"** carries the ranked list
(what rests on the most, checked the least). Standing invitations:

- **Replay any certificate**: one command each, all sub-minute except the
  floor's heavy ones (see "Checking a claim" below). A red run on your
  machine is a finding; please report it.
- **Attack the newest first**: 0020's staircase has exactly **one cell the
  arithmetic cannot kill** — (X, m, partition) = (8, 30, (3,3,1,1)) — closed
  only by a structural profile argument whose key constraint (every
  high-degree vertex lies in ≥ 2 shared sets) is *measured* load-bearing:
  drop it and the kill genuinely fails (mutant M10, 1090 > 1066). Its
  thinnest arithmetic kill is **2 units** ((8,30,(3,2,2,1))), its X = 6
  floor needs (D2) at m = 22–23 (11 cells reopen without it) and n ≥ 36
  everywhere. 0019's m = 27/28 rungs kill at zero slack by divisibility.
  All margins are documented per house law D-017/D-035 rather than hidden;
  **the (D2) cap (cert 0008), the strict-lemma guard τ ≥ q_max + 2, and
  0020's structural cell are the highest-leverage things an outside reader
  can scrutinise.**
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
