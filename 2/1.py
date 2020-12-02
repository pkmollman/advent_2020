passwd_list = []
with open('input.txt','r') as f:
    for line in f.readlines():
        clean_line = line.strip().split(' ')
        min_max = clean_line[0].split('-')
        letter = clean_line[1][0]
        passwd = clean_line[2]
        passwd_count = passwd.count(letter)
        if passwd_count >= int(min_max[0]) and passwd_count <= int(min_max[1]):
            passwd_list.append(passwd)

print(len(passwd_list))