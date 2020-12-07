#!/usr/bin/env python3

import re

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
        bag_types[main_result.group(1).strip()][result[2].strip()] = int(result[1])

shiny_golds = list(bag_types['shiny gold'].keys())

number_o_bags = 0

def num_bag(bag_type, number):
    numbag = number
    if bag_types[bag_type]:
        for bag in bag_types[bag_type]:
            numbag += num_bag(bag, bag_types[bag_type][bag]) * number
    else:
        return number
    return numbag


for bag in shiny_golds:
    number_o_bags += num_bag(bag, bag_types['shiny gold'][bag])

print(number_o_bags)
