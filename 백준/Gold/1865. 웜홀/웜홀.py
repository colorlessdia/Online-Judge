import sys

input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())

    graph = []

    for i in range(M):
        S, E, T = map(int, input().split())

        graph.append((S, E, T))
        graph.append((E, S, T))
    
    for i in range(M, M + W):
        S, E, T = map(int, input().split())

        graph.append((S, E, -T))
    
    INF = float('inf')
    dist = [0] * (N + 1)

    is_negative = False

    for i in range(N + 1):

        if is_negative:
            break

        for u, v, w in graph:

            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
                if i == N:
                    is_negative = True
                    break
    
    if is_negative:
        print('YES')
    else:
        print('NO')