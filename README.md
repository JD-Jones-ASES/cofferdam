# cofferdam

A small lab — its first seven certificates derived under a since-opened seal
(D-011) — establishing a **floor** on the size of a
counterexample to Ryser's conjecture at r = 6 — the first open case.

Ryser's conjecture says τ ≤ (r−1)ν. In the intersecting case (ν = 1) that reads
τ ≤ r−1, proven for r ≤ 5 (Tuza) and open at r = 6. A counterexample would be a
6-partite 6-uniform intersecting hypergraph with τ ≥ 6. The question here is how
few edges such an object could possibly have.

## Where it stands

**A Ryser r=6 intersecting counterexample has at least 22 edges.**
**PROVEN-BY-CERTIFICATE, citing nothing.** There is no external input: no
literature constant, no unreproduced lemma, no solver.

| certificate | result |
| --- | --- |
| [0001](certificates/0001-degree-cap-ladder) | the degree-cap ladder; g(1..4) = 1,3,5,8, each with witness + counting kill (one lower-bound argument, two code forms — D-028) → m ≥ 18 citing nothing |
| [0002](certificates/0002-delta-window) · [0003](certificates/0003-low-incidence) | the maximum-degree window; the low-incidence bound |
| [0005](certificates/0005-min-degree-ladder) | the **minimum-degree ladder** → m ≥ 19 citing nothing, **m ≥ 20** citing f(6)=13; and the corrected AKP Lemma 2.8, both halves |
| [0006](certificates/0006-excess-concentration) | **(L8) excess-concentration** → m = 20 impossible, so **m ≥ 21** citing f(6)=13 |
| [0007](certificates/0007-citation-free-floor) | **the citation is unnecessary** — (L8) run on the weaker rung N(5) ≥ 11, which is ours, kills every m ≤ 20 → **m ≥ 21 citing nothing** |
| [0008](certificates/0008-degree-two-cap) | **the degree-two cap** — each line holds ≤ 1 degree-2 vertex, so 2·D₂ ≤ m; kills m = 21 → **m ≥ 22 citing nothing** |
| [0009](certificates/0009-g5-pinned) | **the ladder is pinned** — g(5) = N(5) = 13 citing nothing (the m = 12 dead heat forces the shape; 11,520 designs, all τ = 4); Q13 answered YES; the citation-free ladder now *equals* the cited one |
| [0010](certificates/0010-n4-by-hand) | **N(4) = 9 by hand** — the floor's hinge is a readable theorem; the two exhaustive searches drop to corroboration |
| [0011](certificates/0011-extremal-delta) | **Δ = 4 exactly** for 13-edge τ ≥ 5 objects — the last uncertified structural result, and (L10)'s input |
| [0012](certificates/0012-delta-budget-retired) | **the δ-budget retires** — (L10), the saturation floor, + convexity kill all 567 m = 21 configurations at margin ≥ 6; the minimal chain consumes no δ-budget, level system, qmin or U |

On the pinned ladder the load-bearing set is 0008 + 0009 + 0010 + 0011 + 0012
(plus 0005's lemmas): one ladder, entirely in-house, its hinge a theorem, and
m = 21 killed on floors and convexity alone. 0006 and 0007 remain green as the
weak-ladder record — 0007 ran the machinery on a *strictly weaker* input (7,159
admissible configurations at m = 20 rather than 105) and still killed
everything, so the floor was never an artefact of a cited constant — but they
are retired from the minimal chain, not refuted.

**What 0008 does and does not claim.** The floor is new; the lemma is not. The
degree-two cap is clause (iii) of Lemma 2.1 of Francetić–Herke–McKay–Wanless
(2017), re-derived in full here so the floor cites nothing — but re-deriving a
published lemma is a different act from finding one. The lab's lemmas (A) and (B)
are that paper's 2.1(ii) and 2.1(i) and are in the same position. The lever buys
**one rung and stops**: m = 22 survives.

A floor says where the object *cannot* be, not where it is. Nothing here claims a
counterexample exists at 22 or above.

## If you are here to attack it

Good — that is what it is for. **[PLAN.md](PLAN.md) § "Where to attack"**
carries a ranked list: what rests on the most, checked the least. Three shortcuts
worth knowing before you start:

- **Hit N(4) = 9 first — it is now a theorem, so attack the proof.** Through
  turn 8 this rung was one exhaustive search (then two); certificate 0010 made
  it a hand proof whose finite case checks run in seconds, with the searches as
  corroboration. The sensitivity is unchanged: set N(4) = 8 and m = 20 comes
  back to life — **and so does m = 19**, so that failure drops the floor to 19.
  Breaking the theorem's case analysis is now the single most valuable thing
  anyone could contribute. Do not attack the literature — it is no longer
  holding anything up.
- **Then the excess budget X, and g(4) = 8.** PLAN.md's corrected risk table
  (D-023) says X is the *sole* step whose removal leaves 100% of configurations
  surviving; the previously published claim that (L7) does the same was false.
  And g(4) = 8 carries a margin of exactly one — weaken it to 7 and 649 of 7,159
  survive at m = 20 — while appearing on no attack list until now.
- **The δ-budget holds up nothing anymore.** Certificate 0012 retired it from
  the minimal chain: m ≤ 19 admits no configuration on the pinned ladder,
  m = 20 dies on the (D2) cap, and m = 21 dies on (L7)+(L10) floors + (L9)
  convexity at margin ≥ 6. Attack (L10)'s input instead — certificate 0011's
  Δ ≤ 4, which rests on the twice-built (8,4) census; weakening it to Δ ≤ 5
  revives 65 of the 567.
- The load-bearing control is that the identical machinery, run at m = 21, still
  leaves survivors — had it killed every m it would be "proving" Ryser at r = 6 and
  would therefore be wrong. **Certificate 0006 computes it in full: 6198 of 43875.**
  Certificate 0007's control is on the weaker ladder and stops at the first
  survivor, which is what that control needs and all it claims. If you can break
  either, you have broken the certificate it belongs to.
- 0006's ceiling was deliberately weakened to the crudest concentration bound, so an
  earlier value-pool argument is **no longer in the trust chain** — don't spend time
  on it.

The standing law here is that a search which under-enumerates fakes a proof, so
every "no such object exists" ships with its completeness argument and is validated
first on targets with known answers. Those are the joints to lever.

## Why a cofferdam

A cofferdam is a watertight enclosure pumped dry so you can build on the
riverbed — you hold the water back in order to work on the floor. This repo did
both: it was given the *statement* and nothing else, and re-derives rather than
transcribes. [BRIEF.md](BRIEF.md) §2 names what was sealed and why; the seal has
since been opened and spent (D-011). Provenance conventions and the full origin
story live in D-010 — the short of it: pointers came from peers twice, and every
proof, search and control is this repo's.

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
DECISIONS.md    the ADR log (D-001..D-030)
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

The **eleven green certificates** (0001–0003, 0005–0012, with 0004 never-green
scaffolding, labelled as such) are verified on **Python 3.9** — the version
macOS ships as `/usr/bin/python3` — as well as on 3.14, and under **`python3
-O`** as well as plain `python3`. A checker that is green normally and broken
under `-O` is not a checker (D-015), and 0005 was exactly that until
2026-07-26. Runtimes to expect: 0008 ~2 min; 0005 ~6.5–7 min on 3.10+
(slower on 3.9, where it falls back from `int.bit_count`); **0009 ~12 min**
(its exact-cover census is the heavy step); 0010 ~30 s; 0011 ~3 min;
0012 ~80 s. They are slow, not hung.

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
