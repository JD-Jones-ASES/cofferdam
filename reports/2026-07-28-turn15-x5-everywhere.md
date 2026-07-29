# Turn 15, for JD — the second outside review paid for itself the same day

**What happened.** The GPT 5.6 Sol Pro review you relayed didn't just audit —
it proposed a theorem bigger than the one it was auditing, with a complete
proof attached. House law (the one we wrote after its first review) says
outside proofs never enter the chain, so: the desk re-derived everything and
machine-checked it, eleven verification lanes ran (the lemma proofs re-done
blind twice, the layer arguments re-derived blind three times — two lanes found
their own *different* proofs, which is better evidence than agreement — three
hostile lanes tried to kill it), then the certificate was built and attacked by
three more auditors before it went green.

**The result — certificate 0019, the strongest in the repo.**

- **Every possible counterexample core has excess X ≥ 5.** Turn 14's X ≥ 4
  held at the floor m = 22; this holds on *every* rung of the window [22, 456].
- **X = 5 can only happen at m ≤ 26.** So from m = 27 up, X ≥ 6.
- The 12,171-configuration X = 4 campaign that was next on the plan is now
  **closed without enumerating anything** — two counting lemmas replaced it.
- The four "arithmetic-free" rungs m ∈ {23, 24, 25, 26} are gone as a category:
  arithmetic now forces excess everywhere.

**The review's proof had one real defect** *(wrong — see the erratum at the
end of this report)* — a circular step in its degree
bound. Two of our refuter lanes caught it (the desk's first read did not); the
repair is a strictly stronger lemma. That story is written into the
certificate: agreement on a statement is not agreement on a proof.

**Its documentation complaints were all real** — a stale dependency in 0018's
table, a miscount phrase in PLAN, and one sentence in 0017 that *undersold*
0017's own result. Fixed, plus three more of the same species the fleet and
desk found (including the same underselling sentence living on inside 0017's
checker comments). 0017 re-verified green ×2 after the comment fix.

**Where this leaves the hunt.** A counterexample, if it exists, now needs at
least five "extra" edge-overlaps, and if it has exactly five it lives in a
five-rung band at the bottom of the window. That band is the next field.

**Nothing for you to decide this turn.** The publication-strategy question from
turn 13 still stands in `awaiting_jd` — this result only strengthens that hand.

Check it yourself:

```
cd ~/Documents/repos/cofferdam/certificates/0019-star-collision && python3 verify.py
```

---

**Erratum (2026-07-28, next turn).** This report said the review's proof "had
one real defect — a circular step in its degree bound." That was wrong: the
step was valid, and the apparent circularity was an artifact of how the desk
restated the proof for its attack lanes. The third outside review caught our
misattribution; the record is corrected in certificate 0019 and D-038. The
theorems, the certificate, and the stronger in-house lemma are unaffected.
