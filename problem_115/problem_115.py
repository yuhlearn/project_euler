from time import time

start_t = time()

m = 50
n = m
res = [0] * (200 + 1)

while res[n] + 1 <= 10**6:
    n += 1
    d = n - m
    res[n] += (d + 1) * (d + 2) / 2
    res[n] += sum([a * b for a, b in zip(res[1 : d], range(d - 1, 0, -1))])

res = [r + 1 for r in res]

print time() - start_t
print n
