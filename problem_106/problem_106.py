from itertools import combinations
from time import time
  
def le(a,b):
  for n,m in zip(a,b):
    if n >= m:
      return False
  return True

start = time()
n = 12
N = range(1, n+1)
pairs = (combinations((c for c in combinations(N, k)), 2) for k in N[1:n/2])
results = [(a,b) for seq in pairs for a,b in seq if not (set(a) & set(b) or le(a,b))]

print len(results), time()-start
