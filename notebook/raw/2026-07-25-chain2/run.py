"""Q2 (2026-07-25 evening): close m=19 and m=20 -- decide m >= 21.

PRE-REGISTRATION (No-Noise Law; written before the run)
  TARGET. Certs 0001-0003 leave three cases: (19,Delta=6), (20,Delta=7),
    (20,Delta=6), with residuals at (13,tau=5), (13,tau=5), (14,tau=5). In each,
    tau(R)=5 exactly (>=5 by peeling; =6 would put a counterexample below the
    certified floor m>=19), so every star edge restricts to a RAINBOW MINIMUM
    COVER of R and the decision per R is a small set cover.
  ORDER. m=19 first and completely -- it needs only (13,5). Within (13,5) the
    Delta=5 branch descends through (8,4), which is 5 classes and cheap, so a
    verdict on part of the space arrives early; the Delta=4 branch needs (9,4)
    and is the expensive one. m=20 last, since it additionally needs (14,5).
  BUDGET. Overnight. Checkpoint every level; nothing recomputed on resume.
  KILL CRITERIA.
    (a) any level > 3,000,000 classes -> stop and report the census;
    (b) a CANDIDATE (tau>=6) -> STOP, re-verify through the independent edge-wise
        tau, wake JD. That is a counterexample to Ryser, not bookkeeping;
    (c) all three cases closed -> m >= 21 PROVEN (modulo f(6)=13).
  CALIBRATION FIRST. base(4,3) must be 0 and base(5,3) must be 12; abort if not.
  KNOWN RISK. Completeness rests on the peeling and on attach_stars. The latter
    runs with verify_sample, re-checking its set-cover reduction against a direct
    tau computation on sampled outputs.
"""
import json, os, pickle, sys, time
sys.path.insert(0, '/Users/jjones/Documents/repos/cofferdam/lib')
from peel import (attach_stars, canon_hyp, delta_alive, enumerate_tau,
                  generate_base)
from ryser import canonical_fast, is_intersecting, max_degree, tau

G = {1: 1, 2: 3, 3: 5, 4: 8, 5: 13}
HERE = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()
def log(s): print(f'[{time.time()-t0:8.1f}s] {s}', flush=True)

CK = os.path.join(HERE, 'cache.pkl')
cache = pickle.load(open(CK, 'rb')) if os.path.exists(CK) else {}
def save(): pickle.dump(cache, open(CK, 'wb'))

def enum(m, t, md=None):
    key = (m, t, md)
    if key in cache:
        log(f'  cached ({m},{t},<={md}) = {len(cache[key])}')
        return cache[key]
    s = time.time()
    res = enumerate_tau(m, t, G, max_deg=md, cache=cache, log=log)
    cache[key] = res; save()
    log(f'*** ({m},{t},<={md}) = {len(res)} classes [{time.time()-s:.1f}s]')
    if len(res) > 3_000_000:
        log('KILL (a)'); sys.exit(2)
    return res

def decide(Rs, delta, m, label):
    log(f'--- {label}: {len(Rs)} residuals, attaching {delta}-stars ---')
    for i, R in enumerate(Rs):
        if attach_stars(R, delta, 6, m, G, first_only=True, verify_sample=2):
            H = attach_stars(R, delta, 6, m, G, first_only=True)[0]
            log(f'!!! CANDIDATE {label} at residual #{i}')
            log(f'VERIFY: m={len(H)} intersecting={is_intersecting(H)} tau={tau(H)}')
            for e in H: log('    ' + str(e))
            json.dump({'label': label, 'H': [list(e) for e in H]},
                      open(os.path.join(HERE, 'CANDIDATE.json'), 'w'))
            log('KILL (b): WAKE JD'); sys.exit(3)
        if i and i % 200 == 0:
            log(f'    {i}/{len(Rs)} done, none extend')
    log(f'=== {label}: NO extension. CASE CLOSED. ===')

for (m, t, want) in [(4, 3, 0), (5, 3, 12)]:
    got = len(generate_base(m, t, G, None))
    log(f'CALIBRATION base({m},{t}) = {got} want {want} -> ' + ('OK' if got == want else 'ABORT'))
    if got != want: sys.exit(1)

results = {}
# ---- m = 19, in two stages so the cheap half reports early -----------------
log('### STAGE 1: (13,5) via Delta=5, which descends through (8,4) ###')
R8 = enum(8, 4, 5)
part1 = {}
for R in R8:
    for H in attach_stars(R, 5, 5, 13, G):
        part1[canonical_fast(H)] = canon_hyp(H)
log(f'*** (13,5) Delta=5 branch: {len(part1)} classes')
decide(list(part1.values()), 6, 19, 'm=19 Delta=6 [from Delta=5 residuals]')

log('### STAGE 2: (13,5) via Delta=4, which descends through (9,4) ###')
R9 = enum(9, 4, 4)
part2 = {}
for R in R9:
    for H in attach_stars(R, 4, 5, 13, G):
        c = canonical_fast(H)
        if c not in part1:
            part2[c] = canon_hyp(H)
log(f'*** (13,5) Delta=4 branch: {len(part2)} new classes')
R13 = list(part1.values()) + list(part2.values())
cache[(13, 5, None)] = R13; save()
log(f'*** (13,5) TOTAL = {len(R13)} classes')
decide(list(part2.values()), 6, 19, 'm=19 Delta=6 [from Delta=4 residuals]')
results['m=19'] = 'CLOSED'
json.dump({'(13,5)': len(R13), 'm=19': 'closed'}, open(os.path.join(HERE, 'result.json'), 'w'), indent=1)

# ---- m = 20 ----------------------------------------------------------------
decide(R13, 7, 20, 'm=20 Delta=7')
results['m=20 Delta=7'] = 'CLOSED'
R14 = enum(14, 5)
decide(R14, 6, 20, 'm=20 Delta=6')
results['m=20 Delta=6'] = 'CLOSED'
results['census'] = {'(13,5)': len(R13), '(14,5)': len(R14)}
json.dump(results, open(os.path.join(HERE, 'result.json'), 'w'), indent=1)
log('ALL CASES CLOSED -> m >= 21 PROVEN')
log(json.dumps(results))
