import sys
from string import ascii_uppercase as uppercase

input = sys.stdin.readline

temp = []
char_list = [' '] + list(uppercase) + ['\'', ',', '-', '.', '?']
matched_char = dict(zip(range(31 + 1), char_list))

while True:
    line = input().rstrip()

    if line == '#':
        break

    if line == '*':
        count = len(temp) % 5

        if count != 0:

            for _ in range(5 - count):
                temp.append('0')

        steganography = []
        
        for i in range(0, len(temp), 5):
            binary = int(''.join(temp[i:i + 5]), 2)
            steganography.append(matched_char[binary])

        print(''.join(steganography))
        temp.clear()
        continue

    length = 0

    for char in line:

        if char == ' ':
            length += 1
            continue

        if length == 0:
            continue

        if length % 2 == 0:
            temp.append('1')
        else:
            temp.append('0')
        
        length = 0