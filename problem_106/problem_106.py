import itertools as it
from time import time

def le(l):
  for a,b in l:
    if a >= b:
      return False
  return True

start = time()
n = 12
start_set = range(1, n+1)
subsets = [set(comb) for m in start_set for comb in it.combinations(start_set, m)]
subset_pairs = [(sorted(list(a)),sorted(list(b))) for a,b in it.combinations(subsets, 2) if not a & b]
results = [(a,b) for a,b in subset_pairs if len(a) > 1 and len(a) == len(b) and not le(zip(a,b))]

print len(results), time()-start

