from time import time

def F(m, n):
    res = [0] * (n + 1)

    for s in range(m, n + 1):
        d = s - m
        res[s] = 1 + d + sum(res[m : d + 1])

    return res[-1]

start = time()
r = F(2, 50) + F(3, 50) + F(4, 50)
print r, time() - start
