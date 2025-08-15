import sys
from heapq import heappush, heappop

def dijkstra(s):
    dist = [INF] * N
    dist[s] = 0

    priority_queue = [(0, s)]

    while priority_queue:
        w1, u = heappop(priority_queue)

        if dist[u] < w1:
            continue

        for w2, v in graph[u]:
            w = w1 + w2

            if (v < N - 1) and (N_list[v]):
                continue

            if w < dist[v]:
                dist[v] = w
                heappush(priority_queue, (w, v))

    return dist[N - 1]

input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for _ in range(M):
    A, B, T = map(int, input().split())

    graph[A].append((T, B))
    graph[B].append((T, A))

INF = float('inf')
distance = dijkstra(0)

if distance == INF:
    print(-1)
else:
    print(distance)