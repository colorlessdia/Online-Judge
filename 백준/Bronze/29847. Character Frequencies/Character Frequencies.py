import sys

N = int(sys.stdin.readline())

char_count = dict()

for _ in range(N):
    line = sys.stdin.readline().rstrip()

    for char in line:
        
        if char == ' ':
            continue
        
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

sorted_char_count = sorted(char_count.items(), key=lambda x: x[0])

for char, count in sorted_char_count:
    print(char, count)