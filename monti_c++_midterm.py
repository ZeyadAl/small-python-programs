from random import randint
import math

n=4
results=[]

comp=[]
while len(comp) != math.factorial(n):
	l=[]
	while len(l) != n:
		r = randint(0, n-1)
		if r not in l:
			l.append(r)
	if l not in comp:
		comp.append(l)


for i in range(100):
	init=[i for i in range(n)]

	for i in range(n):
		
		r1 = randint(0,n-1)
		r2 = randint(0,n-1)
		
		temp 	 = init[r1]
		init[r1] = init[r2]
		init[r2] = temp
	results.append(comp.index(init))

f=[]
for i in range(math.factorial(n)):
	f.append(results.count(i))
print(f)
