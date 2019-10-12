n = 50
m = 3
res = [0] * (n + 1)

for s in range(3, n + 1):
    d = s - m
    res[s] += (d + 1) * (d + 2) / 2
    res[s] += sum([a * b for a, b in zip(res[1 : d], range(d - 1, 0, -1))])

res = [r + 1 for r in res]

print res[-1]

