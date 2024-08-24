import sys

t = int(sys.stdin.readline())

matched_number = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
}

phone_number_count = dict()

for _ in range(t):
    line = sys.stdin.readline().rstrip()

    phone_number = ''

    for char in line:
        
        if len(phone_number) == 3:
            phone_number += '-'
        
        if char == '-':
            continue
        
        if char.isnumeric():
            phone_number += char
        elif char.isalpha():
            phone_number += matched_number[char]

    if phone_number in phone_number_count:
        phone_number_count[phone_number] += 1
    else:
        phone_number_count[phone_number] = 1

sorted_phone_number = sorted(phone_number_count.items(), key=lambda x: (x[0]))

duplicates = []

for k, v in sorted_phone_number:
    
    if v < 2:
        continue
    
    duplicates.append((k, v))

if len(duplicates) == 0:
    print('No duplicates.')
else:
    
    for k, v in duplicates:
        print(k, v)