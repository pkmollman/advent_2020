#!/usr/bin/env python3

input_text = ''

with open('input.txt', 'r') as f:
    input_text = f.read().split('\n')

print(input_text)

text_groups = []
text_group = ''

for line in input_text:
    if line == '':
        text_groups.append(text_group)
        text_group = ''
        continue
    text_group += line

group_answer_total = 0

for group in text_groups:
    letters = []
    for letter in group:
        if letter in letters:
            continue
        letters.append(letter)
    group_answer_total += len(letters)

print(group_answer_total)
