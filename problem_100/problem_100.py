from time import time

start = time()

b = 15
n = 21
limit = 10**12

while n < limit:
    b, n = 3*b + 2*n - 2, 4*b + 3*n - 3

print "Result:", "b =", b, "n =", n
print "Time:", time()-start
