import sys

def calc_L1_distance(p, q):
    x1, y1 = p
    x2, y2 = q

    return abs(x1 - x2) + abs(y1 - y2)

input = sys.stdin.readline

N, T = map(int, input().split())

city_list = []
special_city_list = []

for i in range(N):
    S, X, Y = map(int, input().split())

    city_list.append((X, Y))

    if S:
        special_city_list.append(i)

INF = 10000
graph = [[0 if i == j else INF for j in range(N)] for i in range(N)]

for i in range(N):
    P = city_list[i]

    for j in range(i + 1, N):
        Q = city_list[j]

        distance = calc_L1_distance(P, Q)

        graph[i][j] = distance
        graph[j][i] = distance

tp_distance = [0] * N

for i in range(N):

    if i in special_city_list:
        continue

    minimum_distance = 10000

    for special_city in special_city_list:
        
        if graph[i][special_city] < minimum_distance:
            minimum_distance = graph[i][special_city]
    
    tp_distance[i] = minimum_distance

for i in range(N):

    for j in range(i + 1, N):
        D = min(graph[i][j], (tp_distance[i] + tp_distance[j] + T))

        graph[i][j] = D
        graph[j][i] = D

M = int(input())

for _ in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())

    print(graph[A][B])