import sys

input = sys.stdin.readline

N, M = map(int, input().split())

INF = float('inf')
dist = [[0 if i == j else INF for j in range(N + 1)] for i in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())

    dist[A][B] = 1
    dist[B][A] = 1

for k in range(1, N + 1):

    for i in range(1, N + 1):

        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

result = [0, 0, INF]

for i in range(1, N + 1):

    for j in range(1, N + 1):

        if i == j:
            continue

        time = 0

        for di, dj in zip(dist[i][1:], dist[j][1:]):
            time += min(di, dj) * 2
        
        if time < result[-1]:
            result = i, j, time

print(*result)