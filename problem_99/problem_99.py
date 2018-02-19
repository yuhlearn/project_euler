from math import log

f = open("p099_base_exp.txt")
powers = [tuple(map(int, line[:-1].split(','))) for line in f]
numbers = [b * log(a) for a, b in powers]
maxIndex, maxValue = max(enumerate(numbers), key=lambda v: v[1])

print maxIndex+1, maxValue
