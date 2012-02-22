
from infgeoax import gcd

D = 12000

# from TAOCP of course.
def consecutive_proper_fractions(n):
    count = 0
    x0, y0 = 0, 1
    x1, y1 = 1, 3
    while x1 + x1 < y1:
        count += 1
        c = (y0+n) / y1
        x2, y2 = c * x1 - x0, c * y1 - y0
        x0, y0 = x1, y1
        x1, y1 = x2, y2
    return count

print consecutive_proper_fractions(D)