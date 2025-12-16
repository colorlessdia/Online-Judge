import sys

input = sys.stdin.readline

T = int(input())

dy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

for t in range(1, T + 1):
    N, R1, C1, R2, C2 = map(int, input().split())

    is_arrived = False

    for i in range(8):
        Y, X = R1 + dy[i], C1 + dx[i]

        if not((1 <= Y <= N) and (1 <= X <= N)):
            continue

        if (Y == R2) and (X == C2):
            is_arrived = True
            break

    result = 'YES' if is_arrived else 'NO'

    print(f'Case {t}: {result}')