"""Dump the enumerated censuses from the run cache into the certificate directory.

The certificate must be standalone and stdlib-only, so it ships the census as data
and re-verifies it from scratch rather than importing anything from lib/.
"""
import json, os, pickle, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = '/Users/jjones/Documents/repos/cofferdam/certificates/0004-m21'
os.makedirs(OUT, exist_ok=True)
cache = pickle.load(open(os.path.join(HERE, 'cache.pkl'), 'rb'))
for key, name in (('(13,5)', 'census-13-5.json'), ('(14,5)', 'census-14-5.json'),
                  ('(9,4)', 'census-9-4.json'), ('(8,4)', 'census-8-4.json')):
    if key not in cache:
        print(f'  {key}: not in cache'); continue
    data = [[list(e) for e in H] for H in cache[key]]
    p = os.path.join(OUT, name)
    json.dump(data, open(p, 'w'))
    print(f'  {key}: {len(data)} objects -> {name} ({os.path.getsize(p)//1024} KB)')
