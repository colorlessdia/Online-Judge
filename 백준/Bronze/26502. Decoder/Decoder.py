import sys

matched_char = dict(zip(list('yaeiou'), list('aeiouy')))

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().rstrip()

    new_line = ''

    for char in line:
        
        if char.lower() not in ['a', 'e', 'i', 'o', 'u', 'y']:
            new_line += char
            continue
        
        if char.isupper():
            new_line += matched_char[char.lower()].upper()
            continue

        new_line += matched_char[char]

    print(new_line)