from infgeoax import is_prime

a,b,c = [3, 5, 7]
da,db,dc = [10, 12, 14]
total = 5
primes = 3
side_length = 3

while primes > total * 0.1:
    a,b,c = a+da,b+db,c+dc
    da,db,dc=da+8,db+8,dc+8
    total = total + 4
    if is_prime(a):
        primes = primes + 1
    if is_prime(b):
        primes = primes + 1
    if is_prime(c):
        primes = primes + 1
    side_length = side_length + 2

print side_length
    
