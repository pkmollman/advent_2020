#!/usr/bin/env python3

def seat_id(seat):

    row_max = 128
    row_min = 0
    row_nums = list(range(row_min,row_max))

    for char in seat[:7]:
        if char == 'F':
            row_nums = row_nums[:int((len(row_nums)-1)/2)+1]
        if char == 'B':
            row_nums = row_nums[int((len(row_nums)-1)/2)+1:]
    print(row_nums)

    column_max = 8
    column_min = 0
    column_nums = list(range(column_min,column_max))

    for char in seat[-3:]:
        if char == 'L':
            column_nums = column_nums[:int((len(column_nums)-1)/2)+1]
        if char == 'R':
            column_nums = column_nums[int((len(column_nums)-1)/2)+1:]
        print(column_nums)
    return row_nums[0] * 8 + column_nums[0]


print(seat_id('BBFFBBFRLL'))

seat_ids = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        seat_ids.append(seat_id(line.strip()))
        print(line)

seat_ids.sort()
print(seat_ids)
print(seat_ids[-1])