import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    depart, arrive, cost = map(int, input().split())

    graph[depart].append((cost, arrive))

A, B = map(int, input().split())

visited = [False] * (N + 1)
dist = [float('inf')] * (N + 1)
dist[A] = 0

priority_queue = [(0, A)]

while priority_queue:
    cost1, city1 = heappop(priority_queue)

    if visited[city1]:
        continue

    visited[city1] = True

    for cost2, city2 in graph[city1]:
        cost = cost1 + cost2

        if cost < dist[city2]:
            dist[city2] = cost
            heappush(priority_queue, (cost, city2))

print(dist[B])