import sys

input = sys.stdin.readline

n = int(input())
board = [['.' for _ in range(n)] for _ in range(n)]
count_row = dict(zip(range(n), [1] * n))
count_col = dict(zip(range(n), [1] * n))

for i in range(n):
    line = input().rstrip()

    for j in range(n):
        cell = line[j]

        if cell == 'W':
            board[i][j] = 'W'
            
            if i in count_row:
                del count_row[i]

            if j in count_col:
                del count_col[j]

for r, c in zip(count_row.keys(), count_col.keys()):
    board[r][c] = 'W'

for line in board:
    formatted_line = ''.join(line)

    print(formatted_line)