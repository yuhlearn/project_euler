from itertools import combinations


def is_cubes(cubes, comb1, comb2):
    cubes_copy = set(cubes)
    for n1 in comb1:
        for n2 in comb2:
            cubes_copy.discard(n1+n2)
            cubes_copy.discard(n2+n1)
    return not cubes_copy


cubes = {'01', '04', '09', '16', '25', '36', '49', '64', '81'}
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
combs = list()
solutions = set()

for comb in combinations(numbers, 6):
    if '6' in comb and '9' not in comb:
        combs.append(comb+('9',))
    elif '9' in comb and '6' not in comb:
        combs.append(comb+('6',))
    else:
        combs.append(comb)

for comb1 in combs:
    if comb1[0] != '0':
        break
    for comb2 in combs:
        if is_cubes(cubes, comb1, comb2) and (comb2, comb1) not in solutions:
            solutions.add((comb1, comb2))

print len(solutions)
