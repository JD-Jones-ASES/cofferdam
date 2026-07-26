# DRAFT REPLY to issue #1 — *not sent*

Publishing and outward correspondence are the owner's line (AGENTS.md §Session
shape 4). This is drafted for JD to send, edit, or discard.

---

## Re: Hostile audit at 6e7b9e9 — accepted, acted on, and the ledger has changed

Thank you. Every one of the twelve items was re-derived here from the code, the
run, or the paper rather than from the report — house rule, no reflection on the
audit — and **all twelve hold up**. Seven are fixed; the acceptance gate is
complete except where noted. Two corrections to the audit are at the end, and one
consequence of it is larger than anything in it.

### The consequence first

**The floor no longer needs the citation.** m ≥ 21 is now
PROVEN-BY-CERTIFICATE **citing nothing** — [certificate 0007](certificates/0007-citation-free-floor).

The route: certificate 0005 already derives, citing nothing, the weaker rung
N(5) ≥ N(4) + 2 = 11 by peeling. Under that rung the *pair count* no longer closes
m = 19, which is why our citation-free floor had stopped at 19. But (L8) is far
stronger than the pair count and closes it: **33 admissible configurations at
m = 19, all dead; 7159 at m = 20, all dead.** 0007 sweeps m = 12..20 itself and
leaves m = 21 alive.

Note the direction, which is the point: weakening the input **admits more**
configurations (7159 against 105) and they all still die. A result reached by
loosening an input cannot be an artefact of that input.

So your P1 item 2 is resolved more thoroughly than proposed. We did not need the
edge-deletion bridge, and we did not need to internalize ABW's 12-edge exclusion.
The dependency is simply gone. (ABW Thm 2.7 is nonetheless now named as the direct
citation for the cited route, in the τ ≥ r−1 form — you were right about that.)

### Acceptance gate

- [x] **False (L8) level-set identity.** Confirmed, and it is self-witnessing:
      this certificate's *own* 5-edge witness has n₀ = 1 and makes the printed form
      read 3 where D = 4. Corrected to `D = n₀ + |W₃| + 2|W₄| + 3|W₅| + 4|W₆|`
      everywhere, and it is now an **asserted check**, not prose. The adjacent
      justification "because δ is increasing" was false for the same reason
      (δ dips at k = 0→1) and is fixed too.
- [x] **ABW selected, definitions aligned.** README and cert 0001's CITED string
      now state the τ ≥ 5 form explicitly. PLAN's "if AKP 2.9 fails the floor drops
      to 19" is deleted — it was false given ABW, and is now moot given 0007.
- [x] **AKP Lemma 2.8 global clause — certified rather than narrowed.** You were
      right, and the finding is sharper than stated: the global clause is precisely
      what AKP's Lemma 2.9 consumes, at 7 + 6·4 = 31 against 32 required, a margin
      of one. It cost 52 s of our own machinery: cov(A)=5, cov(B)=4, so 30 − b ≥ 28
      forces b ≤ 2, b = 2 forces excess exactly 0, and the search with column 0
      pinned to B at waste budget 0 is empty (8,851,637 nodes) — with a positive
      control at budget 1 that *does* find the 5A+1B object, so the zero
      discriminates.
- [x] **0005 green under `-O`.** All three side-effecting asserts replaced by
      counted checks. Also caught: certs 0001/0002/0004 each *advertise* a
      no-bare-assert rule that 0005 broke.
- [x] **Check counts made honest.** Every literal-`True` now prints through a
      `note()` with its own tally. The one that mattered — `N(t) ≥ 2t`, an input to
      the ladder rather than an annotation — is now **computed**, by showing no
      full-part profile exists below 2t.
- [x] **Erratum scope widened.** The journal edition (JCMCC 103 (2017) 81–104,
      Diamond OA) repeats the error on printed pp. 89 and 91, verified by rendering
      the pages — it is an image-only scan with no text layer, which is why a
      text-based check comes back empty. Date corrected to 2017. Added: the journal
      is a re-typeset ("8 hyperedges" → "8 edges"), so it passed a copy-editing pass.
- [x] **P2 accuracy items.** "B ≥ 15" scoped to the dead heat; the m = 21 control
      now **computes** 6198 of 43875 rather than asserting it; the m ≤ 19 check
      tests 12..19 rather than (17,18,19); the duplicated 52M-node search is reused
      (~5 min saved); brittle check-number cross-references removed rather than
      renumbered.
- [ ] **(L8) stated as a formal one-way relaxation map.** Not done. Agreed it
      belongs; deferred.

### Two corrections to the audit

**AKP's definition.** The report says AKP defines f(r) under τ = r−1 exactly. Its
*introduction* defines it with **τ ≥ r−1**, same as ABW and MSY; the "= r−1" form
appears in the abstract and in its restatement of the MSY conjecture. AKP is
internally inconsistent rather than committed to the narrow form. Related: AKP's
Lemma 2.9 proof hypothesises τ = 5 but never uses τ ≤ 5, so the cited result
already carries the form we need and no bridge was required.

**The cofferdam-side bridge names the wrong certificate.** "excluded those below
19 edges" is cert 0005, whose ladder loop ran `range(14, 24)` and so never tested
m = 12 or 13 — the very range a bridge would need. (Fixed: it starts at 12 now,
and 0007 sweeps its own range rather than inheriting one.)

### Where to attack next — the target has changed

The literature is no longer holding anything up; please don't spend time there.
**Everything now funnels through one exhaustive search of ours**: ρ=8 pinned to
(2,2,2,2), result empty, **52,023,309 nodes, 2220 admissible columns.** There is
no independent implementation of it anywhere.

One trap worth flagging, since a peer audit hit it: our corrected Lemma 2.8 looks
like a second leg for N(4) ≥ 9 and is not — its derivation *consumes* that same
search, so it is downstream. AKP Lemma 2.1 would be a genuine independent leg, but
we cite it and mark it not-used.

**A third implementation of that search is the most valuable thing anyone could
contribute to this repo.** Target to match: `None`, at exactly 52,023,309 nodes.

Finally, a process point you raised and were right about: the repo moved under
your audit. Findings should be pinned to a SHA. Yours were, which is why they were
all still checkable.
