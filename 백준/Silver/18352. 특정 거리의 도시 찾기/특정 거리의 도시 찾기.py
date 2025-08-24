import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = dict(zip(range(1, N + 1), [deque() for _ in range(N)]))

for _ in range(M):
    A, B = map(int, input().split())

    graph[A].append((1, B))

priority_queue = [(0, X)]

visited = [False] * (N + 1)
dist = [float('inf')] * (N + 1)
dist[0] = 0
dist[X] = 0

while priority_queue:
    d1, x1 = heappop(priority_queue)

    if visited[x1]:
        continue

    visited[x1] = True

    for d2, x2 in graph[x1]:
        d = d1 + d2

        if d < dist[x2]:
            dist[x2] = d
            heappush(priority_queue, (d, x2))

count = 0

for i in range(1, N + 1):

    if dist[i] == K:
        count += 1
        print(i)

if not count:
    print(-1)