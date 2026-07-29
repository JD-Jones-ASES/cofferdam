# Turn 16, for JD — a retraction we owed, and the strongest certificate yet

**First, the retraction.** The new review's opening correction was aimed at
us, and it was right: turn 15's record said the *previous* review's proof had
a circular step. It did not. The circularity was an artifact of how I
restated their proof for my attack lanes — the attack lanes correctly broke
my restatement, and I recorded their finding as the reviewer's error. That
charge is now retracted everywhere it appeared, inline, with dated errata,
and there's a new house law (D-038): reviewers' texts go to the attack lanes
verbatim, get kept on file verbatim, and any defect found in a restatement
gets checked against the original before it's recorded. The apology to the
record cost nothing mathematical — our lemma was and is stronger — but the
record matters more than the lemma.

**Then the mathematics — certificate 0020, the biggest single jump yet:**

- **Every possible counterexample core now needs X ≥ 6** — six extra
  edge-overlaps minimum, everywhere in the window.
- **A staircase above it**: 27 or more edges forces X ≥ 7; 29 forces X ≥ 8;
  30 forces X ≥ 9; 32 forces X ≥ 10.
- **A quadratic law across the whole window**: X ≥ m(m−25)/38 everywhere,
  which at the far end (m = 456) reads **X ≥ 5173** — more than double what
  we had there yesterday. And we can already show even that is far from the
  truth; the far end has a lot more to give.

**The review's own proof had one real gap this time** — at one cell of the
staircase it checked one case where the arithmetic actually leaves three.
All three of our verbatim-reading attack lanes found it independently, three
independent repairs agreed, and the certificate encodes the strongest one —
with a mutation test proving the repair's key idea is genuinely what closes
the cell. So the score this turn: their correction of us was right, our
correction of them was right, and both are in the public record with names
attached to the right errors.

**Where this leaves the hunt.** A counterexample, if it exists, sits in
m ∈ [22, 456] with at least six overlaps at the bottom and thousands at the
top. The next field is X = 6 on the five bottom rungs — and the same engine
already almost closes the m = 26 rung (that's next turn's first check).

**Nothing for you to decide this turn.** Publication strategy still stands
open in `awaiting_jd` — three outside-verified theorems in two days is a
much stronger hand than it was on Friday.

Check it yourself:

```
cd ~/Documents/repos/cofferdam/certificates/0020-strict-star-collision && python3 verify.py
```
