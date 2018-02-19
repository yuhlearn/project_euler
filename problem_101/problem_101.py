import numpy as np
from time import time

def gen(n): 
  return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def solve(n, kk):
  m = len(kk)
  return sum([k*n**(m-i-1) for i, k in enumerate(kk)])

start = time()
sol = 0
max = 10
for m in range(1, max+1):
  A = [[n**(m-c) for c in xrange(1, m+1)] for n in range(m, 0, -1)]
  b = [gen(n) for n in xrange(m, 0, -1) ]
  k = [int(round(k)) for k in np.linalg.solve(A,b)]
  sol += solve(m+1, k)

print "Time:", time()-start 
print sol
