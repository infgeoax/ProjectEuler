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