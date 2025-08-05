import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [False] * M

for i in range(M):
    A, B, C = map(int, input().split())

    graph[i] = (A, B, C)

INF = float('inf')
dist = [INF] * (N + 1)
dist[1] = 0

for _ in range(N - 1):

    for a, b, c in graph:

        if dist[a] == INF:
            continue

        if dist[a] + c < dist[b]:
            dist[b] = dist[a] + c

is_negative = False

for a, b, c in graph:

    if dist[a] == INF:
        continue

    if dist[a] + c < dist[b]:
        is_negative = True
        break

if is_negative:
    print(-1)
else:
    
    for i in range(2, N + 1):
        distance = dist[i]

        if distance == INF:
            print(-1)
        else:
            print(distance)