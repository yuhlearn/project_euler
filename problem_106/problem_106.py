from gecode import *
from time import time
from itertools import combinations

def max_sol(n):
    m = [1]
    for k in range(1, n):
        m = [m[k/2]] + [m[k/2] + a for a in m]
    return m

start = time()

card = 4
maxSol = max_sol(card)
maxSum = 100000#sum(maxSol)
minSum = 1
maxNum = maxSum
minNum = 1
subsetInds = [set(ss) for i in range(1, card+1) for ss in combinations(range(card), i)]

s = space()

A = s.intvars(card, minNum, maxNum)
subsetCosts = s.intvars(len(subsetInds), minNum, maxSum)

for i in range(card-1):
    s.rel(A[i], IRT_EQ, A[i+1])
    
for i, ssi in enumerate(subsetInds):
    s.linear([(e in ssi) for e in range(card)], A, IRT_EQ, subsetCosts[i])
    for j, ssj in enumerate(subsetInds[i+1:], start=i+1):
        if ssi.isdisjoint(ssj):
            if len(ssi) == len(ssj):
                s.rel(subsetCosts[i], IRT_NQ, subsetCosts[j])
            else:
                s.rel(subsetCosts[i], IRT_LE, subsetCosts[j])

                
s.branch(subsetCosts[-1], INT_VAL_MIN)
s.branch(A, INT_VAR_NONE, INT_VAL_MIN)

print 'Init (sec):', time() - start
cnt = 0
for sol in s.search(threads=5, time_limit=30000):
    cnt += 1
    print sol.val(subsetCosts[-1]), '== sum(', sol.val(A), ')', cnt
    
print 'Time (sec):', time() - start

