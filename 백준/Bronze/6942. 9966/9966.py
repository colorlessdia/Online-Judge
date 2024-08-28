m = int(input())
n = int(input())

count = 0

for i in range(m, n + 1):
    s = str(i)

    number = ''

    for c in s[::-1]:
        
        if c in '23457':
            break
        
        if c in '018':
            number += c
            continue
        
        if c == '6':
            number += '9'
            continue
        
        if c == '9':
            number += '6'
            continue
    
    if number == s:
        count += 1

print(count)