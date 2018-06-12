from time import time

start = time()

primes = [2]

for n in range(3, 20, 2):
  primes.append(n)
  for p in primes[:-1]:
    if n % p == 0:
      primes.pop()
      break

def no_factor_pairs(n):
  no_pairs = 1
  remainder = n
  for p in primes:
    exponent = 1
    if p**2 > n:
      no_pairs *= 2
      break
    if p <= remainder:
      while remainder % p == 0:
        exponent += 2
        remainder /= p
    no_pairs *= exponent
    if remainder == 1:
      break
  return no_pairs
      
n = 1

while (no_factor_pairs(n)+1)/2 <= 1000:
  n += 1
  
print n, time()-start
