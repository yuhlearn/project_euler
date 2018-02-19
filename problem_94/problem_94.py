from time import time

start = time()
x, h = 2, 1
result = 0

while True:
    x_next = 2 * x + 3 * h
    h_next =     x + 2 * h 
    x, h = x_next, h_next

    if 2 * x - 1 > 10**9:
        break

    p_1, a_1 = 2 * x - 1, h * (x - 2)
    p_2, a_2 = 2 * x + 1, h * (x + 2) 

    if p_1 % 3 == 0 and a_1 % 3 == 0:
        result += p_1 - 1

    if p_2 % 3 == 0 and a_2 % 3 == 0:
        result += p_2 + 1

print "Solution:", result
print "Time:", time() - start
