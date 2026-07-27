# Turn 11 — the bottom of the window is not smooth

*2026-07-27 · for JD · plain language*

## What happened

One new certificate, attacked by two independent verifiers before going
green.

**Certificate 0015.** Two results. First, the "critical-cover
inequality" the outside review sketched is now a proven, certified
theorem — I re-derived it from scratch and it's lovely: in a minimal
counterexample, the edges crowding through any vertex must all pass
through a tiny private bottleneck, and every collision in that
bottleneck charges the structure a unit of "excess." Second, its first
consequence: **a minimal counterexample with exactly 22 edges — the
bottom rung of our window — must carry excess at least 2.** In plain
terms: it cannot be a clean, every-two-edges-meet-once object; it is
forced into tangled, nonlinear territory the moment it exists. That
gives the next rung (ruling out 22, then 23...) a structural handle
that didn't exist before.

## The honesty story (worth your thirty seconds)

The review's sketch said the result would follow from "the inequality
plus one old cap." We measured before trusting: as sketched, it leaves
exactly 52 surviving cases — it does *not* close. The repair needed two
extra consequences the sketch never mentioned (a degree ceiling, and a
counting trick: four high-degree "stars" can't fit disjointly in 22
edges). The certificate states all of this in its own transcript,
including the margin: the final kill closes by exactly one unit, and
says so. Audited, repaired, delivered stronger than claimed — and the
repair is ours.

## Where the fight goes next

The certificate also maps the next battlefield precisely: at excess
exactly 2, there are 9,224 surviving degree-patterns — a small, rigid
family (excess 2 means exactly two double-meets, or one triple-meet).
Stratifying those is the m = 22 → 23 campaign. The ceiling lanes from
turn 10 (the possible drop toward 252) remain queued untouched.

## Reproduce

```bash
cd ~/Documents/repos/cofferdam/certificates/0015-cc-x-floor && python3 verify.py
```
