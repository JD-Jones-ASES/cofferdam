"""Q2 parallel runner -- decide m>=21. Same mathematics as run.py's docstring.

Every level is built explicitly so the parallel map covers the expensive loops.
Order-independent: results are deduplicated by canonical form. lib/peel.py stays
single-threaded and deterministic, so the certificate path is unaffected.

Levels, with residual sizes from the peeling lemma and Delta from certs 0002/0003:
  (8,4)  <- (5,3) Delta=3
  (9,4)  <- (6,3) Delta=3 ; (5,3) Delta=4
  (10,4) <- (7,3) Delta=3 ; (6,3) Delta=4
  (13,5) <- (9,4) Delta=4 ; (8,4) Delta=5
  (14,5) <- (10,4) Delta=4; (9,4) Delta=5 ; (8,4) Delta=6
Then: m=19 Delta=6 over (13,5); m=20 Delta=7 over (13,5); m=20 Delta=6 over (14,5).
"""
import json, os, pickle, sys, time
from multiprocessing import Pool
sys.path.insert(0, '/Users/jjones/Documents/repos/cofferdam/lib')
from peel import attach_stars, canon_hyp, delta_alive, generate_base
from ryser import canonical_fast, is_intersecting, tau

G = {1: 1, 2: 3, 3: 5, 4: 8, 5: 13}
HERE = os.path.dirname(os.path.abspath(__file__))
NPROC = 8
t0 = time.time()
def log(s): print(f'[{time.time()-t0:8.1f}s] {s}', flush=True)
CK = os.path.join(HERE, 'cache.pkl')
cache = pickle.load(open(CK, 'rb')) if os.path.exists(CK) else {}
def save(): pickle.dump(cache, open(CK, 'wb'))

def _attach(a):
    R, d, t, m = a
    return [canon_hyp(H) for H in attach_stars(R, d, t, m, G)]

def _probe(a):
    R, d, m = a
    got = attach_stars(R, d, 6, m, G, first_only=True, verify_sample=1)
    return got[0] if got else None

def base(m, t, md):
    k = ('base', m, t, md)
    if k in cache:
        log(f'  cached base({m},{t},<={md}) = {len(cache[k])}'); return cache[k]
    s = time.time()
    r = generate_base(m, t, G, md, log=log)
    cache[k] = r; save()
    log(f'*** base({m},{t},<={md}) = {len(r)} [{time.time()-s:.1f}s]')
    return r

def level(name, jobs):
    """jobs: list of (residuals, delta, t, m)."""
    if name in cache:
        log(f'  cached {name} = {len(cache[name])}'); return cache[name]
    out = {}
    for (Rs, d, t, m) in jobs:
        s = time.time()
        with Pool(NPROC) as pool:
            for k, res in enumerate(pool.imap_unordered(
                    _attach, [(R, d, t, m) for R in Rs], chunksize=2)):
                for H in res:
                    out[canonical_fast(H)] = H
                if k and k % 1000 == 0:
                    log(f'    {name} Delta={d}: {k}/{len(Rs)}, {len(out)} classes so far')
        log(f'  {name} Delta={d}: {len(Rs)} residuals -> {len(out)} cumulative [{time.time()-s:.1f}s]')
    res = list(out.values())
    cache[name] = res; save()
    log(f'*** {name} = {len(res)} classes')
    return res

def decide(Rs, d, m, label):
    log(f'--- {label}: probing {len(Rs)} residuals with {d}-stars ---')
    s = time.time()
    with Pool(NPROC) as pool:
        for k, H in enumerate(pool.imap_unordered(
                _probe, [(R, d, m) for R in Rs], chunksize=2)):
            if H is not None:
                log(f'!!! CANDIDATE {label}')
                log(f'VERIFY: m={len(H)} intersecting={is_intersecting(H)} tau={tau(H)}')
                for e in H: log('    ' + str(e))
                json.dump({'label': label, 'H': [list(e) for e in H]},
                          open(os.path.join(HERE, 'CANDIDATE.json'), 'w'))
                log('KILL (b): WAKE JD'); sys.exit(3)
            if k and k % 5000 == 0:
                log(f'    {k}/{len(Rs)} probed, none extend')
    log(f'=== {label}: NO extension over {len(Rs)} residuals. CASE CLOSED. [{time.time()-s:.1f}s] ===')

if __name__ == '__main__':
    for (m, t, want) in [(4, 3, 0), (5, 3, 12)]:
        got = len(generate_base(m, t, G, None))
        log(f'CALIBRATION base({m},{t}) = {got} want {want} -> ' + ('OK' if got == want else 'ABORT'))
        if got != want: sys.exit(1)
    for spec in ((13, 5), (14, 5), (10, 4), (9, 4), (8, 4)):
        log(f'  surviving Delta at {spec}: {delta_alive(spec[0], spec[1], G)}')

    B53 = base(5, 3, 3); B54 = base(5, 3, 4); B63 = base(6, 3, 3)
    L8 = level('(8,4)', [(B53, 3, 4, 8)])
    L9 = level('(9,4)', [(B54, 4, 4, 9), (B63, 3, 4, 9)])
    L13 = level('(13,5)', [(L8, 5, 5, 13), (L9, 4, 5, 13)])
    if not L13:
        log('!! (13,5) IS EMPTY -- that contradicts f(6)=13, so the enumeration is WRONG. ABORT.')
        sys.exit(4)
    log(f'### POSITIVE CONTROL: (13,5) non-empty ({len(L13)}), consistent with f(6)=13 ###')
    decide(L13, 6, 19, 'm=19 Delta=6')
    json.dump({'(13,5)': len(L13), 'm=19': 'CLOSED'},
              open(os.path.join(HERE, 'result.json'), 'w'), indent=1)
    log('### m = 19 CLOSED ###')

    decide(L13, 7, 20, 'm=20 Delta=7')
    B73 = base(7, 3, 3); B64 = base(6, 3, 4)
    L10 = level('(10,4)', [(B64, 4, 4, 10), (B73, 3, 4, 10)])
    L14 = level('(14,5)', [(L8, 6, 5, 14), (L9, 5, 5, 14), (L10, 4, 5, 14)])
    decide(L14, 6, 20, 'm=20 Delta=6')
    json.dump({'(13,5)': len(L13), '(14,5)': len(L14), 'm=19': 'CLOSED',
               'm=20': 'CLOSED', 'verdict': 'm >= 21'},
              open(os.path.join(HERE, 'result.json'), 'w'), indent=1)
    log('ALL CASES CLOSED -> m >= 21 PROVEN')
