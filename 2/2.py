passwd_list = []
with open('input.txt','r') as f:
    for line in f.readlines():
        clean_line = line.strip().split(' ')
        poses = clean_line[0].split('-')
        letter = clean_line[1][0]
        passwd = clean_line[2]
        passwd_count = passwd.count(letter)
        if bool(passwd[int(poses[0])-1] == letter) ^ bool(passwd[int(poses[1])-1] == letter):
            passwd_list.append(passwd)

print(len(passwd_list))