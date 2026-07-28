# Cofferdam, turn 13 — the whole window bends (2026-07-27)

## What happened, in plain language

Until today every certified structural statement lived at the window's
floor, m = 22. Certificate 0017 makes the first claims about the **whole
window**: the bigger a hypothetical counterexample core is, the more
tangled it is forced to be — and the forcing grows fast. By the window's
ceiling (m = 456) a core must carry at least **2,259** extra overlaps.
Concretely: on 431 of the window's 435 sizes, some tangling is now
forced; the only sizes where nothing is forced are **23 through 26** —
we now know exactly where the map's thin spots are.

Three laws do this: a linear law extracted from yesterday's machinery, a
"rounding" sharpening of it (overlaps come in whole units), and a
second-moment law that uses convexity the way a statistician would. Each
was derived at least twice by independent stations, attacked by a
dedicated refuter, recomputed blind, and drafted + hostile-audited before
going green. Yesterday's corner trick also turned out stronger than we
said: it survives one excess level higher (X ≤ 4), and the exact point
where it dies (excess 5) is now exhibited with a witness. One question
this opened is honestly marked OPEN in the certificate.

## The catches this turn

- A wrong lookup table in my own briefing (one index off) would have made
  the ceiling number 2323 instead of 2259 — bigger, i.e. *flattering*.
  Two independent lanes caught it; the certificate now derives the table
  from first principles and keeps the wrong version as a test that must
  fail.
- Two notes in yesterday's certificate 0016 overclaimed a boundary
  ("(CC+) is unavailable at X = 3" — actually it survives to X ≤ 4).
  Dated errata applied, checks untouched, re-verified green.

## The repo goes public

Per your instruction: README rewritten with a prominent header — AI
disclaimer first, beta-testing/work-in-progress second, no strong claims
— then the current state and an explicit invitation to attack, aimed at
outside auditors. The flip to public happens with this commit.

## The one command

```bash
python3 ~/Documents/repos/cofferdam/certificates/0017-growth-laws/verify.py
```

~14 s, 61 checks, ALL GREEN.
