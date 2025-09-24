import sys
from collections import deque

def BFS(sy, sx):
    queue = deque([(sy, sx)])
    graph[sy][sx] = 0

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < R) and (0 <= X < C)):
                continue

            if graph[Y][X] == 0:
                continue

            graph[Y][X] = 0
            queue.append((Y, X))

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [[0 for _ in range(C)] for _ in range(R)]
grass_list = []

for i in range(R):
    row = input().rstrip()

    for j in range(C):
        col = row[j]

        if col == '#':
            graph[i][j] = 1
            grass_list.append((i, j))

count = 0

for gy, gx in grass_list:

    if graph[gy][gx] == 0:
        continue

    BFS(gy, gx)
    count += 1

print(count)