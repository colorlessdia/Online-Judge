N, M = map(int, input().split())

chessboard = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):

    for j in range(M):
        i_is_even = 1 if i % 2 == 0 else 0
        j_is_even = 1 if j % 2 == 0 else 0
        cell = '*' if i_is_even == j_is_even else '.'

        chessboard[i][j] = cell

for row in chessboard:
    print(''.join(row))