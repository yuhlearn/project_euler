from time import time as current_time

def divisors(n):
    prime_list = [2]
    divisor_dict = dict()
    for n in range(2, n):
        prime = True
        divisors = set()
        divisors.add(1)
        for p in prime_list:
            if p > n**.5:
                break
            elif n % p == 0:
                for d in divisor_dict[n/p]:
                    divisors.add(d)
                    divisors.add(d*p)
                divisors.add(n/p)
                divisors.add(p)
                prime = False
                break
        if prime:
            prime_list.append(n)
        divisor_dict[n] = divisors
    return divisor_dict

def circles(divisor_dict):
    circle_dict = {1:1}
    for n in divisor_dict.keys():
        summ = sum(divisor_dict[n])
        circle_dict[n] = summ
    return circle_dict
      
def visit(visited_dict, circle_dict, n, count, lim):
    if n >= lim:
        return 1
    if n not in visited_dict:
        visited_dict[n] = -count
        count = visit(visited_dict, circle_dict, circle_dict[n], count+1, lim)
        if visited_dict[n] > 0:
            count = 1
        visited_dict[n] = count
        return count
    else:
        if visited_dict[n] > 0:
            return 1
        visited_dict[n] = count + visited_dict[n]
        return visited_dict[n] 

start_time = current_time()

lim = 10**6+1
circle_dict = circles(divisors(lim))
visited_dict = dict() 
global_max = 0
global_min = lim

for n in xrange(lim-1, 1, -1):
    visit(visited_dict, circle_dict, n, 0, lim)
    
for n in xrange(lim-1, 1, -1):
    if global_max <= visited_dict[n]:
        global_max = visited_dict[n]
        global_min = n

print current_time() - start_time, global_max, global_min
