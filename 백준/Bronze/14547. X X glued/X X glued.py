import sys

input = sys.stdin.readline

while True:
    line = input().rstrip().split()

    if line[0] == '#':
        break

    glued_list = []

    for i in range(3):
        A = line[1][i]
        B = line[1][i + 1]

        if A == B:

            if not glued_list:
                glued_list.append(A)
                continue

            if A != glued_list[-1]:
                glued_list.append(A)
    
    if not glued_list:
        continue

    message = []

    for i in range(len(glued_list)):
        X = glued_list[i]

        if i == 0:
            message.append(f'{X} {X} glued')
            continue

        message.append(f' and {X} {X} glued')
    
    print(''.join(message))