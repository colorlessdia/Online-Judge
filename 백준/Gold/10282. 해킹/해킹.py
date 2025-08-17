import sys
from heapq import heappush, heappop

def dijkstra(s):
    dist = [INF] * (N + 1)
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

T = int(input())

for _ in range(T):
    N, D, C = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(D):
        A, B, S = map(int, input().split())

        graph[B].append((S, A))
    
    INF = float('inf')
    distance_list = dijkstra(C)

    count = 0
    maximum_distance = -1

    for distance in distance_list:

        if distance == INF:
            continue

        if maximum_distance < distance:
            maximum_distance = distance

        count += 1

    print(count, maximum_distance)