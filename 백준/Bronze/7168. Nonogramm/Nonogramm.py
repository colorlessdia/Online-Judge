import sys

def calc_block_count(li):
    count = 0
    temp = []

    for char in li:

        if char == '#':
            count += 1
            continue

        if count == 0:
            continue

        temp.append(str(count))
        count = 0

    if count != 0:
        temp.append(str(count))

    if len(temp) == 0:
        temp.append('0')

    return ' '.join(temp)

input = sys.stdin.readline

N, M = map(int, input().split())

row_list = [[] for _ in range(N)]
col_list = [[] for _ in range(M)]

for i in range(N):
    row = list(input().rstrip())
    row_list[i] = row

    for j in range(M):
        col = row[j]
        col_list[j].append(col)

for row in row_list:
    print(calc_block_count(row))

for col in col_list:
    print(calc_block_count(col))