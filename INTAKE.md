# Peer intake — how this lab learns from the other two without becoming them

**Adopted 2026-07-26 (turn 7), amending BRIEF §2.** BRIEF.md stays frozen; this
file is the amendment and the owner's ruling is what makes it law. See D-020.

BRIEF §2's seal was **binary and one-shot**: four paths unread, lifting once, for
a diff. It did its job — certificates 0001–0007 are this lab's own, derived blind.
But a one-shot seal has a bad endgame: the moment it lifts, the lab either stops
being useful as an independent station or gets archived and rebuilt somewhere
clean. Quarry was archived; cofferdam should not have to be.

This is the mechanism that makes the seal **repeatable**.

## First, the thing that does not work

**Branching does not solve it.** Git isolates *files*; the seal protects
*context*. If a session reads a peer's derivation on `explore/`, it is
contaminated on `main` too — there is no `git checkout` back to not knowing
something. That is the literal content of "you cannot un-read an argument"
(D-011). A worktree, a submodule, a sparse checkout and a separate clone all fail
for the same reason.

## What does work: the airlock is the agent boundary

A subagent's context is **destroyed when it returns**. That is a real isolation
boundary, and it is the only one available. Git supplies what an agent cannot:
a durable, diffable, SHA-pinned ledger and a merge gate.

```
sealed peer artifact
   │
   ▼   READER  — a disposable agent. Reads everything. Emits statements only.
   │             Its context dies with it; nothing else in the lab ever reads
   │             the artifact.
   │
   ├── TIER 1  statements ──────────────► PEER-LEDGER (in the brain, not here)
   │                                       readable by this lab
   │
   └── TIER 2  methods, quarantined ────► brain, owner-only.
                                           Reading it forfeits independence.
   ▼
DERIVER  — this lab, still sealed. Sees Tier 1 only: a claim, never its argument.
   │        Re-derives it, or refutes it, from scratch.
   ▼
merge to main
```

This is not new law. It is BRIEF §2's founding move — *seeded with the statement,
never the derivation* — turned from a one-time setup into a pipeline that can run
again whenever a peer produces something.

## The graded seal

Binary "sealed / spent" was too coarse and cost us accuracy on the very day it
lifted. The seal has levels, and a lab records which one it is at:

| level | means |
| --- | --- |
| **S3 — blind** | no peer material of any kind has been read. Founding state. |
| **S2 — audited** | peer *critiques of our own work* have been read; no peer *derivation* has. **This lab is here.** |
| **S1 — briefed** | Tier-1 statements from peer derivations have been read. Independence of *re-derivation* is intact; independence of *problem selection* is not. |
| **S0 — merged** | peer arguments have been read. This lab is no longer a verifier of those results. |

Descent is one-way. A certificate records the level the lab was at when it was
derived, and **certificates 0001–0007 were all derived at S3.** That fact is
permanent and does not degrade if the lab later drops to S1.

The distinction that matters: **reading a critique of your own work is not
reading someone else's derivation.** Turn 7 conflated them and recorded the seal
as spent when it had only gone S3 → S2.

## Branches

Now branches earn their place — on the *second* half, where the question is what
gets built on, not what gets known.

| branch | rule |
| --- | --- |
| `main` | every result independently derivable. Nothing merges that has not been re-derived here. |
| `explore/<topic>` | contaminated play. Read anything, try anything, keep no promises. Never fast-forwards into `main`. |
| `peer/<lab>-<date>` | a frozen SHA-pinned snapshot of what a peer claimed and when, if one is ever needed for a dispute. Statements only — see the leak rule below. |

**The merge gate.** A result crosses `explore/*` → `main` only when re-derived by
a station that has not read the source. In practice that is a fresh sealed
subagent handed the statement and nothing else — the same instrument as the
READER, pointed the other way. A result that cannot pass the gate is not blocked
from existing; it lives on `explore/` and is labelled **PROVEN-MODULO-PEER**, a
sixth honesty label alongside the five in BRIEF §6.

## The leak rule, which is easy to get wrong

**Codex reads this repository.** So peer material committed here does not stay
here: putting Grok's findings on `main` shows them to Codex, and vice versa. That
correlates the two labs whose independence is the whole point of the arrangement —
the same failure the seal exists to prevent, arriving through the back door.

Therefore: **the peer ledger lives in the brain, not in this repo.** What lives
here is the protocol, and results that have already passed the merge gate — by
which point they are ours, and their provenance is a credit line rather than a
channel. If a peer artifact must be quoted here for a dispute, anonymise the
source.

## Running it

1. Owner rules that intake is open, and on what.
2. Spawn one READER with the sealed paths, the two-tier output contract, and an
   explicit instruction that its Tier 1 must carry no argument. Do not read the
   artifacts yourself, and do not read the agent's raw transcript.
3. Tier 1 → the brain's peer ledger. Tier 2 → the brain, owner-only, marked
   quarantined.
4. Work Tier-1 claims as ordinary open problems: re-derive or refute, certificate
   per usual. A peer claim carries **no evidential weight** until it does — a
   ledger entry is a lead, not a result.
5. Record the lab's seal level if it changed.

## Why bother, when the peers are usually right

Because being right is not the same as being checkable, and because agreement
between models that share corpora and failure modes is weak evidence — that is
BRIEF §2's founding observation and turn 7 confirmed it twice over. Both peer
audits concluded the floor survived; both were substantially correct; and the two
most valuable findings of the turn came from *re-running* what one of them did,
not from believing what either of them said.
