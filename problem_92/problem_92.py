from time import time

def square_digit(i):
    summ = 0
    while i > 0:
        summ += (i % 10)**2
        i = i / 10
    return summ

ones = {1}
enes = {89}
start = time()

for n in range(1, 10**7):
    i = n
    while (i not in ones) and (i not in enes):
        i = square_digit(i)
    if i in ones:
        ones.add(n)
    elif i in enes:
        enes.add(n)
    
print len(enes), time()-start
