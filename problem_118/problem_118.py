from itertools import permutations as perms
from itertools import product as prod
from bitarray import bitarray
from time import time

def gen_primes(n):
    A = bitarray(n + 1)
    A[2:] = True
    for i in range(2, int(n**.5) + 1):
        if A[i] == True:
            j = i**2
            while j <= n:
                A[j] = False
                j += i
    return A

def gen_numbers(digits):
    numbers = []

    for m in range(1, len(digits) + 1):
        for c in perms(digits, m):
            s = ''.join(c)
            i = int(s)
            numbers.append(i)

    return numbers

def filter_numbers(numbers):
    primes_b = gen_primes(int(numbers[-1]**.5))
    primes_i = [i for i, x in enumerate(primes_b) if x]
    filtered = []
    i = 0
    n = numbers[i]

    while numbers[i] <= primes_i[-1]:
        if primes_b[numbers[i]]:
            filtered.append(numbers[i])
        i += 1

    primes_i += range(primes_i[-1] + 1, int(numbers[-1]**.5) + 1)

    for n in numbers[i:]:
        is_prime = True
        for p in primes_i:
            if p**2 > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            filtered.append(n)

    return filtered

def arrange(filtered):
    arranged = { i : [] for i in range(1, 10) }

    for n in filtered:
        arranged[len(str(n))].append(str(n))

    return arranged

def recurse(arranged):
    sets = dict()

    for i in range(1, 10):
        temp_set = {(n,) for n in arranged[i]}
        for j in range(1, i/2 + 1):
            k = i - j
            for a, b in prod(sets[j], sets[k]):
                flat = a + b
                if len(set(''.join(flat))) == i:
                    temp_set.add(tuple(sorted(flat)))
        sets[i] = temp_set

    return sets

start = time()
digits = '123456789'
numbers = gen_numbers(digits)
filtered = filter_numbers(numbers)
arranged = arrange(filtered)
recursed = recurse(arranged)

result = len(recursed[9])

print time() - start, result # 44680

