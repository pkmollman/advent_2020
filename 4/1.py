#!/usr/bin/env python3

import re

passports_text = ''

with open('input.txt', 'r') as f:
    for line in f.readlines():
        passports_text += line

unsep_passports = passports_text.split('\n')
passports = []
passport_group = []

def byr(value):
    if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
        return True
    return False
def iyr(value):
    if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
        return True
    return False
def eyr(value):
    if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
        return True
    return False
def hgt(value):
    if 'cm' in value[-2:] and int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
        return True
    if 'in' in value[-2:] and int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
        return True
    return False
def hcl(value):
    return re.match('^#[0-9a-f]{6}$',value)
def ecl(value):
    return value in ['amb','blu','brn','gry','grn','hzl','oth']
def pid(value):
    # this is trash, shoot me
    return re.match('^[0-9]{9}$',value)

required_values = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
}

for line in unsep_passports:
    if line == '':
        passports.append(passport_group)
        passport_group = []
    elif line == unsep_passports[-1]:
        passport_group.append(line)
        passports.append(passport_group)
    else:
        passport_group.append(line)

clean_passports = []

for passport in passports:
    clean_passport = {}
    for line in passport:
        for key_value in line.split(' '):
            k,v = key_value.split(':')
            clean_passport[k] = v
    clean_passports.append(clean_passport)

valid_passports = 0

for passport in clean_passports:
    valid_passport = True
    for required_value in required_values:
        if required_value in passport and required_values[required_value](passport[required_value]):
            pass
        else:
            valid_passport = False
    if valid_passport:
        valid_passports += 1

print(valid_passports)