import numpy as np

def exp(M, n):
	p = [[1, 0], [0, 1]]
	dub = M
	while(n>0):
		if n%2 == 1:
			p = np.dot(p, dub)
		dub = np.dot(dub, dub)
		n /= 2
	return p

a = [[0, 1], [1, 1]]

print exp(a, 10)




