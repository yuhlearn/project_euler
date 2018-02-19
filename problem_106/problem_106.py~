from math import *
from time import time

start = time()

numbers = list("123456789")

fibs = [0,1]

k = 2

while True:
    fib = fibs[0] + fibs[1]

    if k >= 2749 and fib >= 123456789:
        last = sorted(str(fib % 10**9))
        if last == numbers:
            first = sorted(str(fib/10**int(floor(log(fib, 10)+1)-9)))
            if first == numbers:
                break
    fibs[0] = fibs[1]
    fibs[1] = fib
    k += 1

print "Time (sec):", time()-start
print k
