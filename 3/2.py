#!/usr/bin/env python3

matrix   = []
location = [0,0]
trees = 0
big_number = 0
slopes = [
    [3,1],
    [1,1],
    [5,1],
    [7,1],
    [1,2],
]

with open('input.txt', 'r') as f:
    for line in f.readlines():
        matrix.append(line.strip())

def tree_or_nah(matrix,x,y):
    r_x = (x % len(matrix[0]))
    print(r_x, y)
    print(matrix[y])
    if matrix[y][r_x] == '#':
        return True
    return False

for slope in slopes:
    while location[1] < len(matrix)-1:
        location[0] += slope[0]
        location[1] += slope[1]
        print(location)
        if tree_or_nah(matrix,location[0],location[1]):
            trees += 1
    if big_number == 0:
        big_number = trees
    else:
        big_number = big_number * trees
    trees = 0
    location = [0,0]

print(big_number)