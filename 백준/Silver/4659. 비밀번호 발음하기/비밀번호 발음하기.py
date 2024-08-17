import sys

while True:
    password = sys.stdin.readline().rstrip()

    if password == 'end':
        break
    
    vowel_count = 0
    is_valid = True

    temp = ''

    for char in password:
        temp += char

        if char in 'aeiou':
            vowel_count += 1

        if len(temp) < 2:
            continue
        
        if (
            temp[-1] == temp[-2] and
            ''.join(temp[-2:]) not in ['ee', 'oo']
        ):
            is_valid = False
            break
        
        if len(temp) < 3:
            continue
        
        result = 0
        
        for char_2 in temp[-3:]:
            
            if char_2 in 'aeiou':
                result += 1
        
        if result == 0 or result == 3:
            is_valid = False
            break
    
    if 0 < vowel_count and is_valid:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')