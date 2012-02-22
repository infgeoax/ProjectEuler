c = 0
for n in range(1,22):
    for i in range(1,10):
        if len("%d" % i**n) == n:
            print i,n
            c = c + 1
print c
