board = [[1 for _ in range(8)] for _ in range(8)]

for i in range(8):
    row = input().rstrip()

    for j in range(8):
        col = row[j]

        if col == 'R':

            for k in range(8):

                if board[i][k] == 1:
                    board[i][k] = 0

                if board[k][j] == 1:
                    board[k][j] = 0

count = 0

for line in board:
    count += sum(line)

print(count)