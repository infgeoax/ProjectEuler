
seq = []
for k in range(1, 34):
    seq.extend([1, 2*k, 1])

seq.pop()
n = 1
d = 1

while len(seq) > 0:
    s = seq.pop()
    n, d = d, s*d + n

n = n + d * 2

print sum([int(c) for c in "%d" % n])
