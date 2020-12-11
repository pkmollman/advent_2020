#!/usr/bin/env python3

adapters = []

with open('input.txt', 'r') as f:
    adapters = [int(line.strip()) for line in f.readlines()]

adapters.sort()

count_one_gap = 1
count_three_gap = 1

for i,adapter in enumerate(adapters):
    if i == 0:
        pass
    elif adapter - adapters[i-1] == 1:
        count_one_gap += 1
    elif adapter - adapters[i-1] == 3:
        count_three_gap += 1

print(count_one_gap * count_three_gap)