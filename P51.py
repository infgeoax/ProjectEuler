from infgeoax import eras
from itertools import combinations

def mask(m, str):
    cpy = [chr for chr in str]
    v = -1
    for _m in m:
        if v == -1:
            v = cpy[_m]
        elif v != cpy[_m]:
            return None
        cpy[_m]='*'
    return ''.join(cpy)

d = {}

masks = {}
for i in range(1,8):
    for j in range(1, i):
        for c in combinations(range(i), j):
            if masks.has_key(i):
                masks[i].append(c)
            else:
                masks[i] = [c]
print masks

for p in eras(1000000):
    if (p < 100000):
        continue
    if (p > 1000000):
        break
    pr = "%d" % p
    s = len(pr)
    for c in masks[s]:
        _m = mask(c, pr)
        if not _m:
            continue
        if d.has_key(_m):
            d[_m].append(pr)
        else:
            d[_m] = [pr]

for m,p in d.items():
    if len(p) == 8:
        print m,p
