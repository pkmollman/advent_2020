#!/usr/bin/env python3

import re

# REGEX = r'([\w\s]+)bags contain((\s\d+)\s([\w\s]+)bags?[\.,])+'
main_bag_reg = r'([\w\s]+)bags contain'
inner_bag_reg = r'((\s\d+)\s([\w\s]+) bags?)+'
input_text = ''

with open('input.txt', 'r') as f:
    input_text = [line for line in f.readlines()]

bag_types = {}

for line in input_text:
    main_result = re.match(main_bag_reg, line)
    inner_result = re.findall(inner_bag_reg, line)
    bag_types[main_result.group(1).strip()] = {}
    for result in inner_result:
        bag_types[main_result.group(1).strip()][result[2].strip()] = result[1]

contains_shiny_golds = []

for bag in bag_types:
    # print(bag_types[bag])
    if 'shiny gold' in bag_types[bag]:
        contains_shiny_golds.append(bag)


while True:
    inner_num = 0
    for bag_type in bag_types:
        for bag in contains_shiny_golds:
            if bag in bag_types[bag_type]:
                if not bag_type in contains_shiny_golds:
                    contains_shiny_golds.append(bag_type)
                    inner_num += 1
    if inner_num == 0:
        break

print(len(contains_shiny_golds))