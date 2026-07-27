# Cofferdam, turn 12 — the bottom of the window sinks another rung (2026-07-27)

## What happened, in plain language

Yesterday's result said: any minimal counterexample at the window floor
(m = 22) must be "tangled" — at least two extra overlaps beyond the bare
minimum (X ≥ 2). Today's session set out to map the 9,224 remaining ways
such a doubly-tangled object could look, as the base camp for the next
climb.

The map came back empty. **There are no doubly-tangled objects at m = 22
at all. Certificate 0016: X ≥ 3.**

The key was noticing that the worst case inside yesterday's inequality —
the configuration that made its constant as bad as 3/2 — is itself a
tangle: three edges sharing two common vertices already forces THREE extra
overlaps (the "triangle lemma": those three edges make three overlapping
pairs, each counted once). So in a lightly-tangled object that worst case
cannot occur, the inequality tightens by exactly that factor 3/2, and the
tightened version crushes every one of the 9,224 candidates. The station
that found this was one of this turn's derivation lanes; the desk
re-derived every step before anything was written down, and three
independent attackers (one working blind from the bare statements) tried
and failed to break it.

## Two catches worth your eye

- **My own error, caught by the fleet**: my first sketch used a wrong value
  for one small constant (Φ(8,5) — I wrote 4, it is 3) and "concluded"
  something true for a wrong reason. The measurement lane caught it within
  the hour. This is exactly the failure mode the lab was built to catch,
  and it is on the record in the certificate itself.
- **The margin is thinner than it looks, and we say where.** The kill
  appears to close with room to spare (4 units in one coordinate). The
  adversarial pass showed the REAL binding constraint is a different,
  older certificate's cap (0008's degree-2 bound), and the kill closes by
  exactly ONE unit of it. The certificate quotes the one-unit margin, not
  the comfortable-looking four.

## Where this leaves the problem

Every critical core has m ∈ [22, 456], and at the floor it now carries
excess at least three. The next field is mapped: 186,086 configurations at
X = 3, of which 15,340 survive today's tools — a different world, where the
triangle trick no longer applies and a genuinely new idea is needed. Also
banked: a set of proven "cover-side" theorems from the second lane, and one
unverified lead suggesting the excess must GROW steeply across the whole
window (X ≥ 289 near the ceiling) — next turn's first verification target.

Sixteen certificates, each green twice (bare Python 3.9 and -O). One label
in yesterday's certificate overclaimed ("the floor lands exactly at 2");
it carries a dated erratum now, applied and re-verified in the same commit
as the certificate that outgrew it.

## The one command

```bash
python3 ~/Documents/repos/cofferdam/certificates/0016-ccplus-x3/verify.py
```

~14 s, 45 checks, exit 0, ALL GREEN.
