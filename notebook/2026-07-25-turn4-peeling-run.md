# 2026-07-25 · turn 4 — the peeling engine, and the run at m = 19 / 20

Append-only. Technical. Failure recorded as failure.

## 0. Seal check

Intact. The only external reading was published literature (AKP arXiv:1409.4938,
ABW abstract), which the BRIEF permits — the seal covers the *chain*, not the field.

## 1. What the three surviving cases actually are

Certs 0001–0003 leave (19,Δ=6), (20,Δ=7), (20,Δ=6). Peel a maximum-degree vertex:
H = star(v) + R with |R| = 13, 13, 14. In each, **τ(R) = 5 exactly** — at least 5
by the peeling lemma, and at most 5 because τ(R) = 6 would put a counterexample at
13 or 14 edges, below cert 0001's floor of 19. So R is f(6)-extremal (or one edge
above), and:

- **every star edge is a rainbow minimum cover of R.** It must meet all of R using
  only its five coordinates outside v's part; a vertex fresh to R meets nothing, so
  j fresh coordinates would force τ(R) ≤ 5−j. With τ(R)=5, j=0.
- **τ(H) ≥ 6 iff every minimum cover of R is disjoint from some star edge.** A
  5-cover of H cannot contain v, so it is a minimum cover of R meeting every star
  edge — and it meets f = C_f ∪ {v} exactly when it meets C_f.

So each case is a set cover over the minimum covers of R, and no solver is involved
anywhere. The whole difficulty moves to *enumerating* the residuals.

## 2. The engine, and two bugs caught before any result was trusted

`lib/peel.py`. The decisive trick is separating a star edge's **pattern** (which
coordinates are fresh) from its **labelling** (how the fresh ones group), because a
minimum cover of R never contains a fresh vertex — so the escape mask depends only
on the pattern. The set cover is therefore decided *before* any labelling, and
labels are then enumerated as set partitions of the fresh slots.

Bugs found and fixed:

- the fresh allowance was set to 5−τ(R), which bounds the fresh coordinates of
  **one** star edge, not the distinct fresh symbols a part carries across the whole
  star (up to Δ). Using the per-edge bound per-part **under-enumerates**.
- stored hypergraphs kept construction labels, so a part's symbols could be
  non-contiguous — and `symbol_counts`, which counts *distinct* symbols, would then
  return a "fresh" index already in use, silently fusing two vertices. Everything
  stored now goes through `canon_hyp`.

Both would have shrunk the census silently, i.e. produced a *false* proof. Neither
was caught by a test; both were caught by re-reading the completeness argument.

## 3. Validation

- `enumerate(5,3) = 12` by peeling, matching the edge-wise census exactly through a
  disjoint code path. `enumerate(4,3) = 0`, matching g(3)=5.
- `enumerate(8,4) = 5` classes, checked against AKP Lemma 2.8 — which it
  **contradicts as printed**; see the erratum note. The lemma is off by one in its
  second degree structure, and our census realises the corrected version exactly.
- **Positive control built into the run:** f(6)=13 forces (13,τ=5) to be non-empty.
  A systematic zero from the search — the one failure mode that fakes a proof —
  would trip it, and the run aborts if it does.
- An independent re-implementation of the decisive test lives in
  `notebook/raw/2026-07-25-chain2/crosscheck.py`, sharing no code with the search
  beyond the primitives, for sampling agreement.

## 4. Cost data (measured, on a clean machine)

`(8,4)`: 107 s → 21 s (parallel) → **4.1 s** (parallel, prunes restored).
`base(6,3,≤3)` = 53,906 classes in 146 s. `base(5,3)` 8.7 s → 1.0 s after
`canonical_fast`. Parallelism over 8 cores gives roughly 5×.

**A machine trap that invalidated an hour of earlier timings:** `pkill -f python3`
matches nothing on this box, because Homebrew's `python3` is a shim and the process
command line is the resolved `.../MacOS/Python`. Nine background runs accumulated
at ~65% CPU each. Recorded in the vault's MACHINE.md.
