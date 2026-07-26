"""Independent re-implementation of the decisive test, for cross-checking.

attach_stars decides "does R extend to tau >= 6?" via a set-cover over precomputed
escape masks, with pattern/label separation and several prunes. If it ever returned
an empty answer for a systematic reason -- a bug rather than a fact -- the run would
report m >= 21 falsely, and no positive control is available at t = 6 because
nothing with tau = 6 exists to be found.

So this script decides the same question a second, deliberately naive way:

  * enumerate the rainbow minimum covers of R directly, part by part, by brute
    force over one vertex per part (no masks, no patterns, no prunes);
  * for each choice of the omitted part p, take the covers avoiding p as the
    available star edges;
  * ask whether any 6 of them leave every minimum cover of R escaped, by direct
    subset search;
  * and for any that pass, build H and run the edge-wise tau to confirm.

Slower by design and sharing no code with attach_stars beyond the primitives.
Agreement on a sample is the check.
"""
import itertools, sys, pickle, os, random
sys.path.insert(0, '/Users/jjones/Documents/repos/cofferdam/lib')
from ryser import all_covers, tau, is_intersecting, degrees, symbol_counts

R6 = 6


def naive_extends(R, delta):
    """True iff R + a delta-star can reach tau >= 6. Brute force."""
    mc = all_covers(R, 5)                      # tau(R) = 5, so these are minimum
    if not mc:
        return None
    nsym = symbol_counts(R, R6)
    for p in range(R6):
        # every rainbow choice of one existing vertex per part other than p
        pools = [range(nsym[q]) for q in range(R6) if q != p]
        others = [q for q in range(R6) if q != p]
        stars = []
        for combo in itertools.product(*pools):
            C = {others[i]: combo[i] for i in range(5)}
            # must cover R: every edge of R agrees with C somewhere
            if not all(any(e[q] == s for q, s in C.items()) for e in R):
                continue
            f = tuple(nsym[p] if q == p else C[q] for q in range(R6))
            esc = frozenset(j for j, cov in enumerate(mc)
                            if not any(f[i] == s for (i, s) in cov))
            stars.append((f, esc))
        if len(stars) < delta:
            continue
        need = set(range(len(mc)))
        for pick in itertools.combinations(range(len(stars)), delta):
            got = set()
            for i in pick:
                got |= stars[i][1]
            if got >= need:
                H = tuple(sorted(tuple(R) + tuple(stars[i][0] for i in pick)))
                if is_intersecting(H) and tau(H) >= 6:
                    return H
    return False


if __name__ == '__main__':
    HERE = os.path.dirname(os.path.abspath(__file__))
    cache = pickle.load(open(os.path.join(HERE, 'cache.pkl'), 'rb'))
    key = '(13,5)' if '(13,5)' in cache else None
    if key is None:
        print('(13,5) not in cache yet'); sys.exit(0)
    L13 = cache[key]
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    random.seed(12345)
    sample = random.sample(L13, min(n, len(L13)))
    print(f'cross-checking {len(sample)} of {len(L13)} residuals at (m=19, delta=6)', flush=True)
    from peel import attach_stars
    G = {1: 1, 2: 3, 3: 5, 4: 8, 5: 13}
    bad = 0
    for i, R in enumerate(sample):
        a = bool(attach_stars(R, 6, 6, 19, G, first_only=True))
        b = naive_extends(R, 6)
        b = bool(b) if b is not False else False
        if a != b:
            print(f'  !! DISAGREEMENT on residual {i}: attach_stars={a} naive={b}')
            bad += 1
        elif i % 5 == 0:
            print(f'  {i}: agree ({a})', flush=True)
    print(f'disagreements: {bad} of {len(sample)}')
    print('CROSS-CHECK PASSED' if bad == 0 else 'CROSS-CHECK FAILED')
