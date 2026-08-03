# Turn 18 — 2026-08-03 — cert 0022: X = 7 ⟹ m ≤ 24

## Intake (D-036)

Fifth outside audit (GPT 5.6 Sol Pro, 2026-08-01) arrived with: (a) zero
errors found in the certified chain through 0021; (b) one real defect in
0021's triangle prose ("every high cell lies in T" — false for (2,2,2,1));
(c) a complete proposed proof of X = 7 ⟹ m ≤ 24 (kill (7,25) and (7,26));
(d) commentary on the OpenAI ten-proofs collection (it was given the
walkthroughs volume, not the proofs volume). Received text verbatim to
`raw/2026-08-03-received-turn18-gpt-pro-ryser-4.md` on arrival.

## Fleet (10 lanes, all Opus 5) + desk

Three verbatim refuters (m=26 / m=25 / frame), three blind lanes (m=26 /
m=25 / computational sieve), four research lanes on the two OpenAI PDFs.
Desk re-derived the entire §2–§5 chain by hand before the fleet returned.

**The intake ledger, both directions:**

- Desk confirmed the 0021 defect (code-level: `tri_max` searches T only)
  and measured corrected maxima 62/67/74/83 at m = 24..27 — unchanged, by
  convexity. Erratum filed in 0021 (docstring reworded, no check touched,
  re-verified green ×2).
- **Desk caught the audit's repair being itself incomplete**: |S₄ ∩ U| ≤ 1
  fails in the adjacent-apex pattern (q = 1 pair rides a triangle edge;
  both S₄ cells in U ∖ T; no fifth pair). All three refuters found the
  same hole independently. One refuter sharpened: the apex edge carries
  x_e = 5 > 4 = c₃, so the pattern is **C3-dead at 25/26 but live at
  m = 24** (c₃ = 5) — load-bearing for the next campaign. 0022 §3 carries
  the honest four-branch case law with witnesses for both apex variants.
- Refuters: zero errors in the audit's §2–§5 otherwise; two implicit steps
  named and written into check text (J ≥ 9 outside-union step in §4.4;
  q ≥ 2 reason for the seventh-pair claim in §4.6). The audit's knapsacks
  are F-cost-only (its table hides F(11) = 7): under linear f the decisive
  (1⁷) wall jumps 73 → 83 — M-f armed again.
- Blind m=25 lane **proved the full rung independently** (15/15 partitions,
  no peer text). Blind sieve reproduced every raw table and rediscovered
  the d ≤ 10 ceiling's role unprompted.

## Cert 0022 — shared-set quotients

64 checks, green ×2 (bare 3.9.6, `-O`). Raw sieve over all 15 partitions
(4 raw survivors at 26 — the audit's "three" imported 0021's J-debited
preview; re-enumerated honestly — 6 at 25) → quotient classification →
J-debits → exact censuses. New machinery: census solver (emptiness =
the audit's arithmetic walls), triangular-multiplicity capacity test
(kills (1⁷)-(10,10,6) m-independently), corrected triangle optimizer with
completeness counters, monotone-derived degree ceiling (closes the audit's
engineering note). Ten mutants priced; M-RG reopens the (7,25) triangle
kill outright (67 → 74) — residual pairing is load-bearing at every rung
of the triangle branch.

**Result: X = 7 ⟹ m ≤ 24. Staircase: X ≥ 7 on [22,24] · X ≥ 8 on
[25,28] · X ≥ 9 at 29 · X ≥ 10 from 30. Frontier: three edge counts.**

## The next wall, exact

(7,24), (2,2,2,1) triangle: Ψ = Λ = 62 at (10,9,6), census (12,5,0,16),
apex pattern live at c₃ = 5. Zero margin — counting alone will not breach
it. The audit proposes the quotient/profile engine there; the desk agrees
it is the right opening.

## Research (the two OpenAI PDFs — four lanes, all verified firsthand per ADR-023)

The audit's three characterizations of the walkthroughs volume all check
against the text, with corrections that matter:

- **Ch 11 / proofs Ch 10 (admissible quotients) — the high-value import.**
  "Essentially verbatim in substance" per the verification lane. The
  extremal lane read the ACTUAL proof (which the audit never saw) and
  delivered the formal translation: an admissible identification is
  part-preserving (free in our 6-partite setting) and edge-injective on
  distinguished subgraphs; the hazard lives exactly where quotients merge
  excessive pairs or collapse q-values. Proposed engine upgrade **(EC)**:
  per shape, build the free template (2t formal transversal edges, all
  cells distinct), enumerate ALL admissible quotients, and check every one
  lands in the certificate's case list — one uniform completeness
  mechanism with one mutant, replacing 0022's per-shape bespoke prose.
  The adjacent-apex escape is precisely an admissible quotient the audit's
  repair missed; under (EC) it is generated, not remembered.
- **Ch 10 / proofs Ch 9 (Ramsey) — correct but incomplete as glossed.**
  The decisive move is a PAIR: strengthen the invariant AND relax it by
  one label per stage so the induction closes. Also mined: the
  forced-equality mechanism ("determinism, not existence, kills the
  two-block case") — a label forced as a function of the far endpoint,
  the sharpest cousin of our equality-forcing kills; and the
  bounded-exceptional-set + generic-mechanism pattern (one cheap generic
  argument for the bulk, a hard finite bound on exceptions). The exact
  self-similar bookkeeping does NOT transfer (cores have no sub-object
  recursion) — written down so nobody spends a turn on it.
- **Ch 12 (entropy/Hamming) — rejected, as the audit said, with a
  salvage.** The potential-exhaustion schema IS our kill template; two
  hazards named for census work: independence corrections in multiplied
  counts, and order-of-quantifiers.
- **Chapters 1–8 sweep — four hits.** (1) Ch 1's discipline: bound the
  certificate CLASS, not just the instance — the (7,24) tie is exactly
  that statement for our counting schema (Ψ/Λ counting has hit its own
  limit; the wall needs structure, not sharper counting). (2) Ch 2:
  positivity by explicit Gram factorization = our exact-integer law,
  outside confirmation. (3) Ch 5: the Möbius/inclusion-exclusion
  injectivity conversion — finite, combinatorial, a candidate tool for
  straddling-part configurations. (4) Ch 5's local-to-global packing
  template with completeness check.

## New banked levers (derived this turn, consumed nowhere)

1. **The 6-partite tiling test** (blind m=26 lane, desk-verified in three
   lines): at n = 36 each part holds exactly six cells and each part
   partitions the edge set, so the 36-degree multiset must tile into six
   6-blocks each summing to m. Strictly stronger than the census.
   **Measured against the (7,24) template: it TILES** — the wall stands,
   the lever is banked, honest negative recorded
   (scratchpad tiling_724.py; groups exist for (10,9,6)+(12,5,0,16)).
2. **(EC) admissible-quotient completeness** (above) — the candidate
   engine for the (7,24) campaign.
3. The blind m=26 lane also proved its rung independently (census → tiling
   route), so BOTH rungs of T-A22 now carry a fully blind derivation
   alongside the desk's and the audit's.
