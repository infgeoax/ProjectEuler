from __future__ import generators
from math import sqrt
from array import array

def is_prime(n):
    if n < 0:
        n = -n
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(sqrt(n)+1)
    for x in range(3, limit, 2):
        if n % x == 0:
            return False
    return True

def gcd(a, b):
    if b > a:
        a, b = b, a
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b

def eras(n):
  siv=range(n+1)
  siv[1]=0
  sqn=int(round(n**0.5))
  for i in range(2,sqn+1):
    if siv[i]!=0:
        siv[2*i:n/i*i+1:i]=[0]*(n/i-1)
  return filter(None,siv)

def primes_million(limit):
    limit = min(1000000, limit)
    f = open('primes1.txt')
    primes = []
    for l in f:
        if limit > 0:
            primes.append(int(l.strip()))
            limit -= 1
        else:
            break
    return primes

def phi(a):
    """
    A rather naive method.
    """
    p = 1
    for x in range(2, a):
        if gcd(a, x)==1:
            p = p + 1
    return p

def factorial(n):
    f = 1
    
    for x in range(1, n+1):
        f *= x
    
    return f

class polygonal_numbers:
    def __init__(self, initial_d, increment_d):
        self.initial_d = initial_d
        self.increment_d = increment_d
        self.p = 1
    
    def __iter__(self):
        return self

    def next(self):
        val = self.p
        self.p += self.initial_d
        self.initial_d += self.increment_d
        return val

class triangle_numbers(polygonal_numbers):
    def __init__(self):
        polygonal_numbers.__init__(self, 2, 1)

class square_numbers(polygonal_numbers):
    def __init__(self):
        polygonal_numbers.__init__(self, 3, 2)

class pentagonal_numbers(polygonal_numbers):
    def __init__(self):
        polygonal_numbers.__init__(self, 4, 3)

class hexagonal_numbers(polygonal_numbers):
    def __init__(self):
        polygonal_numbers.__init__(self, 5, 4)

class heptagonal_numbers(polygonal_numbers):
    def __init__(self):
        polygonal_numbers.__init__(self, 6, 5)

class octagonal_numbers(polygonal_numbers):
    def __init__(self):
        polygonal_numbers.__init__(self, 7, 6)
