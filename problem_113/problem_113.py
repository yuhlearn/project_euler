def binomial(n, k):
    if k > n - k:
        k = n - k
    num = 1
    den = 1
    for i in range(1, k+1):
        num *= (n + 1 - i)
        den *= i
    return num / den

n = 100

print binomial(n + 10, n) + binomial(n + 9, n) - (10 * n + 2)
