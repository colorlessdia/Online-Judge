import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
T_list = [0] + list(map(int, input().split()))

INF = float('inf')
dist = [[0 if i == j else INF for j in range(N + 1)] for i in range(N + 1)]

for _ in range(R):
    A, B, I = map(int, input().split())

    if I < dist[A][B]:
        dist[A][B] = I

    if I < dist[B][A]:
        dist[B][A] = I

for k in range(1, N + 1):

    for i in range(1, N + 1):

        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

maximum_item = 0

for d in dist:
    item = 0

    for i in range(1, N + 1):
        
        if d[i] <= M:
            item += T_list[i]
    
    if maximum_item < item:
        maximum_item = item

print(maximum_item)