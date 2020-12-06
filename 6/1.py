#!/usr/bin/env python3

input_text = ''

with open('input.txt', 'r') as f:
    input_text = f.read().split('\n')

# track each group of answers as a single string
text_groups = []

# track current group for below iteration 
text_group = ''

# for single line of answers append to a single string,
# once a blank line is reached, append to the main list,
# and reset current working string to empty
for line in input_text:
    if line == '':
        text_groups.append(text_group)
        text_group = ''
        continue
    text_group += line

# total sum of unique answers per group
group_answer_total = 0

# for char in group answer string, if char not in letters list, append it
# len(letters) is group total unique answers
for group in text_groups:
    letters = []
    for letter in group:
        if letter in letters:
            continue
        letters.append(letter)
    group_answer_total += len(letters)

print(group_answer_total)
