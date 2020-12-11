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

adapters_r = adapters[::-1]

count_one_gap = 1
count_three_gap = 1

global g_counter
g_counter = 0

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

def options_rb(i, adapters, adapter, sliced):
    global g_counter
    for nummy,option in enumerate([ num for num in sliced if (adapter - num) <= 3 ]):
        if option == adapters[-1]:
            g_counter += 1
        option_index = i + nummy + 1
        options_rb(option_index,adapters,option,adapters[option_index+1:option_index+4])



adapt_len = len(adapters)
adapt_mid = int(adapt_len//2)

mid_starts = [adapt_mid-1,adapt_mid,adapt_mid+1]
back_starts = [adapters_r.index(adapters[num-3]) for num in mid_starts]
print(back_starts)
print(mid_starts)
# for start in mid_starts:
#     options_r(start, adapters, adapters[start],adapters[start+1:start+4])

for start in back_starts:
    options_rb(start, adapters_r, adapters_r[start],adapters_r[start+1:start+4])

print(g_counter)
# def thread_i_guess(ind,v):
#     option_index = i + ind + 1
#     thingy += options_r3(option_index,adapters,option,adapters[option_index+1:option_index+4],g_counter)
