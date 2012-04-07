from infgeoax import *

def range_numbers(lower, upper, numbers):
	l = []
	for n in numbers:
		if n > upper:
			break
		if n > lower:
			l.append(n)
	return l

lower, upper = 999, 9999

tri = range_numbers(lower, upper, triangle_numbers())
squ = range_numbers(lower, upper, square_numbers())
pen = range_numbers(lower, upper, pentagonal_numbers())
hex = range_numbers(lower, upper, hexagonal_numbers())
hep = range_numbers(lower, upper, heptagonal_numbers())
oct = range_numbers(lower, upper, octagonal_numbers())

numbers = (tri, squ, pen, hex, hep, oct)

def num(idx):
	return numbers[idx[0]][idx[1]]

def empty(c):
	return len(c) == 0


edges = []

for i in range(6):
	for j in range(i + 1, 6):
		s1, s2 = numbers[i], numbers[j]
		for m in range(len(s1)):
			for n in range(len(s2)):
				if s1[m] % 100 == s2[n] / 100:
					edges.append(((i, m), (j, n)))
				if s1[m] / 100 == s2[n] % 100:
					edges.append(((j, n), (i, m)))


q = []

for e in edges:
	q.append([e[0]])

while not empty(q):

	c = q.pop()

	if len(c)>=6:
		x = [num(a) for a in c]
		if x[0] / 100 == x[-1] % 100:
			print sum(x)
			break

	for e in edges:
		if e[0] == c[-1]:
			for _ in c:
				if e[1][0] == _[0]:
					break
			else:
				_c = [_ for _ in c]
				_c.append(e[1])
				for x in q:
					if _c == x:
						break
				else:
					q.append(_c)