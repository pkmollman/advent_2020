#!/usr/bin/env python3

from multiprocessing import Pool

adapters = []

# with open('input.txt', 'r') as f:
#     adapters = [int(line.strip()) for line in f.readlines()]

with open('testinput1.txt', 'r') as f:
    adapters = [int(line.strip()) for line in f.readlines()]

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

count_one_gap = 1
count_three_gap = 1

global g_counter
# g_counter = 0

main_list = []

def options(i, slices):
    return [ num for num in slices if (num - i) <= 3 ]

def options_r(i, adapters, adapter, sliced):
    global g_counter
    for nummy,option in enumerate([ num for num in sliced if (num - adapter) <= 3 ]):
        if option == adapters[-1]:
            g_counter += 1
        option_index = i + nummy + 1
        options_r(option_index,adapters,option,adapters[option_index+1:option_index+4])

def options_r2(i, adapters, adapter, sliced, g_counter):
    thingy = g_counter
    for nummy,option in enumerate([ num for num in sliced if (num - adapter) <= 3 ]):
        if option == adapters[-1]:
            thingy += 1
        option_index = i + nummy + 1
        thingy += options_r2(option_index,adapters,option,adapters[option_index+1:option_index+4],g_counter)
    return thingy

def options_r3(i, adapters, adapter, sliced, g_counter):
    thingy = g_counter
    tup_list = []
    for nummy,option in enumerate([ num for num in sliced if (num - adapter) <= 3 ]):
        if option == adapters[-1]:
            thingy += 1
        option_index = i + nummy + 1
        tup_list.append((option_index,adapters,option,adapters[option_index+1:option_index+4],g_counter))
    with Pool(len(tup_list)) as p:
        thingy += sum(p.starmap(options_r3,tup_list))
    return thingy

# def thread_i_guess(ind,v):
#     option_index = i + ind + 1
#     thingy += options_r3(option_index,adapters,option,adapters[option_index+1:option_index+4],g_counter)




g_counter = options_r3(0,adapters,adapters[0],adapters[1:4],0)
print(g_counter)