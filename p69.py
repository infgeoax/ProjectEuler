from infgeoax import phi

r = 0
n = 0

for i in range(2, 1000000):
    _r = i/float(phi(i))
    if r < _r:
        n = i
        r = _r
    if i % 50 == 0:
        print i

print n,r