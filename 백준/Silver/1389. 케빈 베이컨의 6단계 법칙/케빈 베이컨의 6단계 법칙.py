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

count = -1
number = 0

for i in range(1, N + 1):
    dist_sum = sum(dist[i][1:])

    if count < 0:
        count = dist_sum
        number = i
        continue

    if dist_sum < count:
        count = dist_sum
        number = i

print(number)