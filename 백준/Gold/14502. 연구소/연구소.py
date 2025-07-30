import sys
from collections import deque

def BFS(g):
    queue = deque(virus_points)
    visited = [[False for _ in range(M)] for _ in range(N)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    area = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < N) and (0 <= X < M)):
                continue

            if visited[Y][X]:
                continue

            if g[Y][X] != 0:
                continue
            
            queue.append((Y, X))
            visited[Y][X] = True
            area += 1

    return area

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]
blank_count = -3
blank_points = []
virus_points = []

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        col = row[j]
        graph[i][j] = col
        
        if col == 0:
            blank_count += 1
            blank_points.append((i, j))
        elif col == 2:
            virus_points.append((i, j))

length = len(blank_points)
maximum_area = 0

for i in range(length):

    for j in range(i + 1, length):

        for k in range(j + 1, length):
            copy_graph = [[graph[n][m] for m in range(M)] for n in range(N)]

            for y, x in [blank_points[i], blank_points[j], blank_points[k]]:
                copy_graph[y][x] = 1

            area = blank_count - BFS(copy_graph)

            if maximum_area < area:
                maximum_area = area

print(maximum_area)