import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()

    if line == '0':
        break

    binary = []
    count = 1

    for i in range(len(line) - 1):
        A = line[i]
        B = line[i + 1]

        if A == B:
            count += 1
            continue

        binary.append(f'{count}{A}')
        count = 1

    binary.append(f'{count}{line[-1]}')
    
    print(''.join(binary))