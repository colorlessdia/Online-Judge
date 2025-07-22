import sys
from heapq import heappush, heappop

def dijkstra(s):
    dist = [float('inf')] * (N + 1)
    dist[s] = 0

    priority_queue = [(0, s)]

    while priority_queue:
        w1, u = heappop(priority_queue)

        if dist[u] < w1:
            continue

        for w2, v in graph[u]:
            w = w1 + w2

            if w < dist[v]:
                dist[v] = w
                heappush(priority_queue, (w, v))
    
    return dist

input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())

    graph[A].append((C, B))
    graph[B].append((C, A))

V1, V2 = map(int, input().split())

path1 = [(1, V1), (V1, V2), (V2, N)]
path2 = [(1, V2), (V2, V1), (V1, N)]

count1 = 0
count2 = 0

for i in range(3):
    s1, e1 = path1[i]
    s2, e2 = path2[i]

    count1 += dijkstra(s1)[e1]
    count2 += dijkstra(s2)[e2]

count = min(count1, count2)

if count == float('inf'):
    print(-1)
else:
    print(count)