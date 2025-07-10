import sys
from heapq import heappush, heappop

def BFS(graph, start_points, N, S):
    queue = start_points
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        sec, number, (y, x) = heappop(queue)

        if sec == S + 1:
            break

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < N) and (0 <= X < N)):
                continue
            
            if graph[Y][X] != 0:
                continue
            
            graph[Y][X] = number
            heappush(queue, (sec + 1, number, (Y, X)))

input = sys.stdin.readline

N, K = map(int, input().split())

graph = [[0 for _ in range(N)] for _ in range(N)]
start_points = []

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(N):
        col = row[j]
        graph[i][j] = col

        if 0 < col:
            heappush(start_points, (1, col, (i, j)))

S, Y, X = map(int, input().split())

BFS(graph, start_points, N, S)

print(graph[Y - 1][X - 1])