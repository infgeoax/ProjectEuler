
# I believe there's a better way to count bouncy numbers, consider bouncy-prefix
def is_bouncy(n):
    if n < 100:
        return False
    digits = [int(c) for c in "%d" % n]
    a, b = digits[0], digits[1]
    digits = digits[2:]
    for d in digits:
        if (a > b and d > b) or (a < b and d < b):
            return True
        if d != b:
            a, b = b, d
    return False

bouncy_count = 0

i = 100

while True:
    if is_bouncy(i):
        bouncy_count += 1
    
    if bouncy_count/float(i) == 0.99:
        print bouncy_count, i
        break
    
    i += 1