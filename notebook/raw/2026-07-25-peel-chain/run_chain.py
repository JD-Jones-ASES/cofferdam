"""Q1 (2026-07-25): enumerate the peeling chain up to (13,5), then decide m=19.

PRE-REGISTRATION (No-Noise Law -- written before the run)
  HYPOTHESIS. Every 6-partite intersecting hypergraph with tau >= t decomposes as
    star(v) + R for a maximum-degree v, with tau(R) >= t-1. Certificate 0002 pins
    Delta to a narrow window, so enumeration at (19,6) reduces along
        (19,6) -> (13,5) -> (9,4)/(8,4) -> (6,3)/(5,3) -> base.
    Expectation: the class counts stay in the hundreds or low thousands, because
    the cap ladder plus the escape-every-minimum-cover condition are severe.
  BUDGET. 90 minutes wall for the whole chain. Any single level exceeding 45
    minutes is a re-slice signal, not a push-through.
  KILL CRITERIA.
    (a) if enumerate(13,5) exceeds ~200k classes, abandon full enumeration and
        switch to a direct existence search at (19,6) -- the counts would say the
        extremal family is not the small rigid object the argument assumes;
    (b) if the m=19 step finds a CANDIDATE (tau >= 6 on 19 edges), STOP, verify it
        independently through the edge-wise tau, and wake JD -- that is a
        counterexample to Ryser's conjecture, not a bookkeeping result;
    (c) if the chain completes with no m=19 object, that CLOSES m=19 and lifts the
        floor to m >= 20.
  WHAT WOULD MAKE THIS WRONG. The peeling is complete only if Delta really is
    confined to the certified window and if attach_stars enumerates every star up
    to isomorphism. Both are re-checked below against known values: enumerate(5,3)
    must return 12 (matching the independent edge-wise census) and enumerate(4,3)
    must return 0 (matching g(3)=5).
"""
import json, sys, time
sys.path.insert(0, '/Users/jjones/Documents/repos/cofferdam/lib')
from peel import enumerate_tau, attach_stars, delta_window
from ryser import tau, is_intersecting, max_degree, canonical_fast

G = {1: 1, 2: 3, 3: 5, 4: 8, 5: 13}
t0 = time.time()
log = lambda s: print(f'[{time.time()-t0:7.1f}s] {s}', flush=True)
cache, record = {}, {}

# calibration first: the engine must reproduce what we already know independently
cal = {(4, 3): 0, (5, 3): 12}
for (m, t), want in cal.items():
    got = len(enumerate_tau(m, t, G, cache))
    log(f'CALIBRATION enumerate({m},{t}) = {got}, expected {want} -> '
        + ('OK' if got == want else 'MISMATCH -- ABORT'))
    if got != want:
        sys.exit(1)

for (m, t) in [(6, 3), (8, 4), (9, 4), (13, 5)]:
    s = time.time()
    res = enumerate_tau(m, t, G, cache, log=log)
    record[f'{m},{t}'] = len(res)
    log(f'*** enumerate(m={m}, tau>={t}) = {len(res)} classes  [{time.time()-s:.1f}s]')
    for H in res[:3]:
        if not (is_intersecting(H) and tau(H) >= t):
            log('!! BAD OBJECT EMITTED'); sys.exit(1)
    if m == 13 and len(res) > 200000:
        log('KILL CRITERION (a) FIRED -- too many classes for full enumeration')
        sys.exit(2)

R13 = cache[(13, 5)]
log(f'--- m=19, Delta=6: attaching a 6-star to each of {len(R13)} extremal 13-edge objects ---')
hits = []
for i, R in enumerate(R13):
    got = attach_stars(R, 6, 6, 19, G, first_only=True)
    if got:
        hits.append(got[0]); log(f'!!! CANDIDATE at residual #{i}'); break
    if i % 25 == 0:
        log(f'    {i}/{len(R13)} residuals done, none extend')
record['m19_candidates'] = len(hits)
log(f'=== m=19: {len(hits)} candidates from {len(R13)} residuals ===')
if hits:
    H = hits[0]
    log(f'VERIFY: intersecting={is_intersecting(H)} tau={tau(H)} m={len(H)}')
    for e in H: log('   ' + str(e))
json.dump(record, open('/Users/jjones/Documents/repos/cofferdam/notebook/raw/2026-07-25-peel-chain/counts.json', 'w'), indent=1)
log('DONE ' + json.dumps(record))
