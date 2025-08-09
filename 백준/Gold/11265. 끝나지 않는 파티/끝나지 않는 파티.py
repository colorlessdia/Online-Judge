import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dist = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):

    for i in range(N):

        for j in range(N):

            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1

    if dist[A][B] <= C:
        print('Enjoy other party')
    else:
        print('Stay here')