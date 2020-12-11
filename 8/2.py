#!/usr/bin/env python3

adapters = []

with open('input.txt', 'r') as f:
    adapters = [int(line.strip()) for line in f.readlines()]


adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

count_one_gap = 1
count_three_gap = 1

global g_counter
g_counter = 0

main_list = []

def options(i, slices):
    return [ num for num in slices if (num - i) <= 3 ]

def options_r(i, adapters, adapter, sliced):
    global g_counter
    for option in [ num for num in sliced if (num - adapter) <= 3 ]:
        # print(option)
        if option == adapters[-1]:
            g_counter += 1
            main_list.append(option)
            # return g_counter
        option_index = adapters.index(option)
        options_r(option_index,adapters,option,adapters[option_index+1:option_index+4])

option_multiplier = 1

print(options_r(0,adapters,adapters[0],adapters[1:4]))
print(main_list)
print(g_counter)

# for i,adapter in enumerate(adapters):
#     if i == 0:
#         pass
#     elif adapter - adapters[i-1] == 1:
#         count_one_gap += 1
#     elif adapter - adapters[i-1] == 3:
#         count_three_gap += 1
#     print(adapter)
#     print(options(adapter, adapters[i+1:i+4]))
#     if len(options(adapter, adapters[i+1:i+4])) > 0:
#         option_multiplier *= len(options(adapter, adapters[i+1:i+4]))

# print(count_one_gap * count_three_gap)
# print(option_multiplier)