#!/usr/bin/env python3

input_text = ''

with open('input.txt', 'r') as f:
    input_text = f.read().split('\n')

text_groups = []
text_group = []

# for single line of answers append to a list,
# once a blank line is reached, append list to the main list,
# and reset current working list to empty
for line in input_text:
    if line == '':
        text_groups.append(text_group)
        text_group = []
        continue
    text_group.append(line)

group_answer_total = 0

# for list of answer strings in text_groups
for group in text_groups:
    # track group's unique answers
    letters = []
    for answers in group:
        for letter in answers:
            if letter in letters:
                continue
            letters.append(letter)
    # track all group's answer strings in a single string
    all_answers = ''
    for answers in group:
        all_answers += answers
    # track group's valid answers
    group_total = 0
    # if unique letter count in combined answer string
    # equals number of group members the answer is counted in group_total
    for letter in letters:
        if all_answers.count(letter) == len(group): group_total += 1
    group_answer_total += group_total

print(group_answer_total)
