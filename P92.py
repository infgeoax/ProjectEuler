squares = [x*x for x in range(10)]

def sum_digit_squared(n):
    s = 0
    while n > 0:
        d = n % 10
        n = n / 10
        s += squares[d]
    return s

def ends_with_89(n):
    while n != 1 and n != 89:
        n = sum_digit_squared(n)
    return n != 1

cache = {}

for c in range(1, 10000000):
    if cache.has_key(c) or ends_with_89(c):
        cache[c] = 1

print len(cache)
