import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())

graph = dict(zip(range(1, N + 1), [[] for _ in range(N)]))

for _ in range(M):
    A, B, C = map(int, input().split())

    graph[A].append((C, B))
    graph[B].append((C, A))

dist = [float('inf')] * (N + 1)
dist[0] = 0
dist[1] = 0

priority_queue = [(0, 1)]
visited = [False] * (N + 1)

while priority_queue:
    d1, n1 = heappop(priority_queue)

    if visited[n1]:
        continue

    visited[n1] = True

    for d2, n2 in graph[n1]:
        d = d1 + d2

        if d < dist[n2]:
            dist[n2] = d
            heappush(priority_queue, (d, n2))

print(dist[N])