import sys
from heapq import heappush, heappop

def dijkstra(s, g):
    dist = [INF] * (N + 1)
    dist[s] = 0

    priority_queue = [(0, s)]

    while priority_queue:
        w1, u = heappop(priority_queue)

        if dist[u] < w1:
            continue

        for w2, v in g[u]:
            w = w1 + w2
            
            if w < dist[v]:
                dist[v] = w
                heappush(priority_queue, (w, v))
    
    return dist

input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
reversed_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    S, E, T = map(int, input().split())

    graph[S].append((T, E))
    reversed_graph[E].append((T, S))

INF = float('inf')

dist1 = dijkstra(X, graph)
dist2 = dijkstra(X, reversed_graph)

maximum_distance = 0

for i in range(1, N + 1):
    distance = dist1[i] + dist2[i]

    if maximum_distance < distance:
        maximum_distance = distance

print(maximum_distance)