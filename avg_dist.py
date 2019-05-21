"""
We want to know what's the average of the distances if we took two random points on a segment of length 1. 
"""
import random
from statistics import mean

m=[]
h = int(input('insert: '))

for i in range(h):
	x1=random.random()
	x2=random.random()

	y1=random.random()
	y2=random.random()

	m.append(((x1-x2)**2 + (y1-y2)**2)**(1/2))

print(mean(m))
