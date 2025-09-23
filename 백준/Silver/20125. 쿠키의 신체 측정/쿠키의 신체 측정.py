import sys

input = sys.stdin.readline

N = int(input())

long_leg_x = -1
x, y = -1, -1
size_list = [0] * 5

for i in range(N):
    row = input().rstrip()

    count = 0

    for j in range(N):
        col = row[j]

        if col == '*':
            count += 1

    if count == 0:
        continue

    if x == y == -1:
        x = row.index('*')
        y = i
        continue

    if count == 1:

        if size_list[3] == size_list[4] == 0:
            size_list[2] += 1
            continue

        if long_leg_x == -1:
            long_leg_x = row.index('*')

        if x < long_leg_x:
            size_list[4] += 1
        else:
            size_list[3] += 1

    elif count == 2:
        size_list[3] += 1
        size_list[4] += 1
    else:
        size_list[0] = row[:x].count('*')
        size_list[1] = row[x + 1:].count('*')

print(y + 2, x + 1)
print(*size_list)