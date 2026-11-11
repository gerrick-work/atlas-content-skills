"""Fetch 3D icons from Microsoft Fluent Emoji 3D (MIT licence) into a local cache.

Usage:
    python3 fetch_icon.py search nose            list matching icon names
    python3 fetch_icon.py get "Nose" "Test tube"  download PNGs (transparent, 256px) to CACHE
Skin-tone icons resolve to the Default tone.
"""
import os, sys, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.environ.get('ICON_CACHE', '/home/claude/assets/icons3d')
RAW = 'https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/'
PATHS = [l.strip() for l in open(os.path.join(HERE, 'fluent3d_index.txt')) if l.strip()]

def name_of(p): return p.split('/')[1]

def search(q):
    q = q.lower()
    return sorted({name_of(p) for p in PATHS if q in name_of(p).lower()})

def get(name):
    hits = [p for p in PATHS if name_of(p).lower() == name.lower()]
    if not hits: raise SystemExit(f'no icon named {name!r}; try: search')
    p = sorted(hits, key=lambda x: ('/Default/' not in x, len(x)))[0]
    os.makedirs(CACHE, exist_ok=True)
    out = os.path.join(CACHE, name.lower().replace(' ', '_') + '.png')
    if not os.path.exists(out):
        urllib.request.urlretrieve(RAW + urllib.parse.quote(p), out)
    return out

if __name__ == '__main__':
    cmd, *args = sys.argv[1:]
    if cmd == 'search':
        for a in args: print('\n'.join(search(a)))
    else:
        for a in args: print(get(a))
