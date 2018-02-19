from copy import deepcopy
from time import time


def print_grid(grid):
    letters = "ABCDEFGHI"
    numbers = "123456789"
    print "    1   2   3   4   5   6   7   8   9" 
    print "  -------------------------------------"
    for row in letters:
        print row + " |",
        for column in numbers:
            square_id = row+column
            if len(grid[square_id]) != 1:
                print " ", "|",
            else:
                print list(grid[square_id])[0], "|",
        print
        print "  -------------------------------------"


def load_grids(f):
    raw_list = [g.split()[1:] for g in f.read().split("Grid")][1:]
    letters = "ABCDEFGHI"
    numbers = "123456789"

    unsolved_list = []
    grid_list = []
    neighbors = dict()
        
    for raw in raw_list:
        grid = dict()
        unsolved = set()
        for r, row in enumerate(raw):
            for c, square_content in enumerate(row):
                square_id = str(letters[r] + numbers[c])
                if square_content == "0":
                    unsolved.add(square_id)
                    grid[square_id] = set(numbers)
                else:
                    grid[square_id] = set(square_content)
        unsolved_list.append(unsolved)
        grid_list.append(grid)

    for r, letter in enumerate(letters):
        for c, number in enumerate(numbers):
            square_id = letter + number
            neighbors_tmp = set()
            neighbors_tmp.update(set([letter + n for n in numbers]))
            neighbors_tmp.update(set([l + number for l in letters]))
            neighbors_tmp.update(set([l + n for l in letters[3 * (r / 3) : 3 * (r / 3) + 3] \
                                            for n in numbers[3 * (c / 3) : 3 * (c / 3) + 3]]))
            neighbors_tmp.remove(square_id)
            neighbors[square_id] = list(neighbors_tmp)
    return grid_list, unsolved_list, neighbors


def solve(i, grid_list, unsolved, neighbors):
    grid = grid_list[i]
    done = False
    while not done:
        done = True
        for square_id in list(unsolved):
            for neighbor in neighbors[square_id]:
                if neighbor not in unsolved:
                    grid[square_id].difference_update(grid[neighbor])
            if len(grid[square_id]) == 1:
                unsolved.remove(square_id)
                done = False
            elif len(grid[square_id]) == 0:
                return False

    if bool(unsolved):
        solved = False 
        square_id = unsolved.pop()
        for guess in grid[square_id]:
            new_unsolved = deepcopy(unsolved)
            grid_list[i] = deepcopy(grid)
            grid_list[i][square_id] = set(guess)
            if solve(i, grid_list, new_unsolved, neighbors):
                solved = True
                break
        if not solved:
            return False

    return True 


def verify(grid):
    letters = "ABCDEFGHI"
    numbers = "123456789"
    sections = [[letter + number for letter in letters[i:i+3] for number in numbers[j:j+3]] \
                for i in range(0,7,3) for j in range(0,7,3)]
    sections.extend([[letter + number for number in numbers] for letter in letters])
    sections.extend([[letter + number for letter in letters] for number in numbers])

    for section in sections:
        values = [list(grid[square_id])[0] for square_id in section]
        for number in numbers:
            if values.count(number) != 1:
                return False
    return True


grid_list, unsolved_list, neighbors = load_grids(open("p096_sudoku.txt"))

start = time()

summ = 0

for i in range(len(grid_list)):
    solved = solve(i, grid_list, unsolved_list[i], neighbors)
    if not solved:
        print "Failed: Grid", i
    summ += int(list(grid_list[i]['A1'])[0])*100 + int(list(grid_list[i]['A2'])[0])*10 + int(list(grid_list[i]['A3'])[0])

end = time()

print "Time: " + str(end - start)
print "Solution: " + str(summ)
