from Fastexpon import *
#import numpy as np

def fib(n):
	a = np.array([[0, 1], [1, 1]], dtype = object)	
	M = exp(a, n)
	return M[0][1]

for x in xrange(100):
	print fib(x)

