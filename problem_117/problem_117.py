from time import time

def F(n):
    res = [0] * (n + 1)

    for s in range(2, n + 1):
        for m in range(2, min(s + 1, 5)):
            d = s - m
            res[s] += 1 + d + sum(res[2 : d + 1])

    return [r + 1 for r in res][-1]

start = time()
r = F(50)
print r, time() - start
