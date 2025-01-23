M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

P = M + U + D
Q = N + L + R

board = [
    ['#' if q % 2 == 0 else '.' for q in range(Q)]
    if p % 2 == 0 else
    ['.' if q % 2 == 0 else '#' for q in range(Q)]
    for p in range(P)
]

X1, X2 = L, Q - R
Y1 = U

for i in range(M):
    board[Y1 + i][X1:X2] = list(input())

for row in board:
    print(''.join(row))