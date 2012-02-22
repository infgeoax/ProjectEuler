from infgeoax import eras, is_prime

s = [3, 7, 109, 673]

primes = set(eras(1000000))

for p in primes:
    for x in s:
        a = int("%d%d" % (x, p))
        b = int("%d%d" % (p, x))
        if not a in primes or not b in primes:
            break
        print x, p
    else:
        print p