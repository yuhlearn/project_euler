from itertools import combinations
from time import time

def is_spectral_sum(s):
    subsets = [set(ss) for i in xrange(len(s)//2+1) for ss in combinations(s, i+1)]
    for ssi in subsets:
        for ssj in subsets[i+1:]:
            if ssi.isdisjoint(ssj):
                sumi = sum(ssi)
                sumj = sum(ssj)
                if sumi == sumj:
                    return False
                elif len(ssi) < len(ssj) and sumi >= sumj:
                        return False
    return True

f = open('p105_sets.txt')
sets = [sorted(map(int, l.split(',')), reverse=True) for l in f.readlines()]
f.close()

start = time()
total = 0

for s in sets:
    if is_spectral_sum(s):
        total += sum(s)

print 'Time (sec):', time()-start
print total
