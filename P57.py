
def next(enumerator, denominator):
    return denominator, 2 * denominator + enumerator

count = 0
enum,deno = 1, 2
for i in range(1000):
    if len(str(enum+deno)) > len(str(deno)):
        count = count + 1
    enum, deno = next(enum, deno)
print count