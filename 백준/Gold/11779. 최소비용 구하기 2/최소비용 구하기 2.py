import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())

    graph[A].append((C, B))

P, Q = map(int, input().split())

INF = float('inf')
parent = [None] * (N + 1)
dist = [INF] * (N + 1)
dist[P] = 0

priority_queue = [(0, P)]

while priority_queue:
    w1, u = heappop(priority_queue)

    if dist[u] < w1:
        continue

    for w2, v in graph[u]:
        w = w1 + w2

        if w < dist[v]:
            dist[v] = w
            parent[v] = u
            heappush(priority_queue, (w, v))

cost = dist[Q]
count = 0
path_list = []
i = Q

while not (i == None):
    path_list.append(i)
    count += 1
    i = parent[i]

print(cost)
print(count)
print(*path_list[::-1])