#!/usr/bin/env python3

input_text = ''

with open('input.txt', 'r') as f:
    input_text = f.read().split('\n')

print(input_text)

text_groups = []
text_group = []

for line in input_text:
    if line == '':
        text_groups.append(text_group)
        text_group = []
        continue
    text_group.append(line)

group_answer_total = 0

for group in text_groups:
    letters = []
    all_answers = ''
    group_total = 0
    for answers in group:
        all_answers += answers
    for answers in group:
        for letter in answers:
            if letter in letters:
                continue
            letters.append(letter)
    for letter in letters:
        if all_answers.count(letter) == len(group): group_total += 1
    group_answer_total += group_total

print(group_answer_total)
