import sys

input = sys.stdin.readline

N, M = map(int, input().split())

square = []

is_find = False
x1, y1 = 0, 0
length = 0
half = 0

for i in range(N):
    row = input().rstrip()

    square.append(row)

    if is_find:
        continue

    if '#' not in row:
        continue

    is_find = True
    x1, y1 = row.index('#'), i
    length = M - x1 - row[::-1].index('#')
    half = length // 2

if square[y1][x1 + half] == '.':
    print('UP')
elif square[y1 + length - 1][x1 + half] == '.':
    print('DOWN')
elif square[y1 + half][x1] == '.':
    print('LEFT')
elif square[y1 + half][x1 + half] == '.':
    print('RIGHT')