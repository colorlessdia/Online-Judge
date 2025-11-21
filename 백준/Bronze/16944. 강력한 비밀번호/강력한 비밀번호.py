N = int(input())
S = input()

check_list = [False] * 4
special_char_set = set('!@#$%^&*()-+')

for char in S:

    if char.isnumeric():
        check_list[0] = True
        
    elif char.islower():
        check_list[1] = True
        
    elif char.isupper():
        check_list[2] = True
        
    elif char in special_char_set:
        check_list[3] = True

count = check_list.count(False)

if N + count < 6:
    count += (6 - (N + count))

print(count)