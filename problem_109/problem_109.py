values = [
	1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 
	6, 7, 8, 8, 9, 9, 10, 10, 11, 12, 
	12, 12, 13, 14, 14, 15, 15, 16, 16, 17, 
	18, 18, 18, 19, 20, 20, 21, 22, 24, 24, 
	25, 26, 27, 28, 30, 30, 32, 33, 34, 36, 
	36, 38, 39, 40, 42, 45, 48, 50, 51, 54, 
	57, 60
]

doubles = [
	2, 6, 9, 13, 17, 20, 24, 28, 31, 35, 37, 
	38, 41, 43, 44, 46, 48, 49, 51, 53, 57
]

result = [0]*100

def count_aux(s, v, d):
	for v in range(v, len(values)):
		ss = s + values[v]
		if ss < 100 and d < 3:
			result[ss] += 1
			count_aux(ss, v, d + 1)
	return

def count():
	for d in doubles:
		s = values[d]
		result[s] += 1
		count_aux(s, 0, 1)
	return

count()

print sum(result), result

