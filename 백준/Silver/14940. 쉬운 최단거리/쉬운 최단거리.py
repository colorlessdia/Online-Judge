import sys
from collections import deque

def BFS(graph, start):
    queue = deque(start)
    graph[start[0][0]][start[0][1]] = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x, distance = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < N) and (0 <= X < M)):
                continue

            if graph[Y][X] != -1:
                continue

            graph[Y][X] = distance + 1
            queue.append((Y, X, distance + 1))

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[-1 for _ in range(M)] for _ in range(N)]
start = []

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        col = row[j]

        if col == 0:
            graph[i][j] = 0
            continue

        if col == 2:
            start.append((i, j, 0))

BFS(graph, start)

for row in graph:
    print(*row)