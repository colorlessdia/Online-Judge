import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

INF = float('inf')
dist = [[0 if i == j else INF for j in range(N + 1)] for i in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())

    if C < dist[A][B]:
        dist[A][B] = C

for k in range(1, N + 1):

    for i in range(1, N + 1):

        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N + 1):
    row = dist[i]

    for j in range(1, N + 1):
        col = row[j]

        if col == INF:
            col = 0

        if j == N:
            print(col)
        else:
            print(col, end=' ')