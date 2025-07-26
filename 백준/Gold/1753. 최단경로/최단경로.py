import sys
from heapq import heappush, heappop

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())

    graph[u].append((w, v))

visited = [False] * (V + 1)
dist = [float('inf')] * (V + 1)
dist[K] = 0

priority_queue = [(0, K)]

while priority_queue:
    w1, u = heappop(priority_queue)

    if visited[u]:
        continue

    visited[u] = True

    for w2, v in graph[u]:
        w = w1 + w2

        if w < dist[v]:
            dist[v] = w
            heappush(priority_queue, (w, v))

for i in range(1, V + 1):
    
    if dist[i] == float('inf'):
        print('INF')
        continue

    print(dist[i])