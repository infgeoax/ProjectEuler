
from infgeoax import factorial

factorials = [factorial(x) for x in range(10)]

cache = {}

blackholes = {169: 2, 363601: 2, 1454: 2, 871: 1, 45361: 1, 872: 1, 45362: 1, 1: 0, 2: 0, 145: 0, 40585: 0}

chains = {}

def f(n):
    if cache.has_key(n):
        return cache[n]
    else:
        s = sum([factorials[int(c)] for c in "%d" % n])
        cache[n] = s
        return s

for j in range(1000000):
    chain = 1
    i = j
    while True:
        if blackholes.has_key(i):
            chain += blackholes[i]
            chains[j] = chain
            break
        i = f(i)
        if chains.has_key(i):
            chain += chains[i]
            chains[j] = chain
            break
        else:
            chain += 1
    if chain==60:
        print j, chain
