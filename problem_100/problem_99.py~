from itertools import permutations
from time import time

def is_anagram(a, b):
    if len(a) != len(b):
        return False
    b_bag = {letter : 0 for letter in b}
    for letter in b:
        b_bag[letter] += 1
    for letter in a:
        if letter in b and b_bag[letter] > 0:
            b_bag[letter] -= 1
        else:
            return False
    if max(b_bag.values()) != 0:
        return False
    return True

def to_number(numbers):
    return int(''.join(map(str, numbers)))

def translate(word, mapping):
    return [mapping[letter] for letter in word]

start = time()

f = open("p098_words.txt")
strings = f.read().replace('"', '').split(',')
squares = set([n**2 for n in range(1, int(9876543210**0.5))])
anagrams = [(strings[i], strings[j]) 
            for i in range(len(strings)) 
            for j in range(i+1, len(strings)) 
            if is_anagram(strings[i], strings[j])]

largest = 0

for a, b in anagrams:
    letters = list(set(b))
    for numbers in permutations([9,8,7,6,5,4,3,2,1,0], len(letters)):
        mapping = {letters[i] : numbers[i] for i in range(len(letters))}
        if mapping[a[0]] != 0 and mapping[b[0]] != 0:
            a_n = to_number(translate(a, mapping))
            b_n = to_number(translate(b, mapping))
            if a_n in squares and b_n in squares:
                largest = max(largest, max(a_n, b_n))
                
print largest, time()-start
