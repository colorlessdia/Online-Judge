import sys
from collections import deque

def BFS(graph, sy, sx):
    queue = deque([(sy, sx, 1)])
    graph[sy][sx] = 1

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x, count = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < N) and (0 <= X < M)):
                continue

            if graph[Y][X] != 0:
                continue

            graph[Y][X] = count + 1
            queue.append((Y, X, count + 1))

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    row = input().rstrip()

    for j in range(M):
        col = int(row[j])
        
        if col == 1:
            graph[i][j] = 0

BFS(graph, 0, 0)

print(graph[N - 1][M - 1])