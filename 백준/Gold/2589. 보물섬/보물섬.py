import sys
from collections import deque

input = sys.stdin.readline

def BFS(r, c):
    queue = deque([(r, c)])
    dist = [[0 for _ in range(C)] for _ in range(R)]
    dist[r][c] = 1

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    maximum_distance = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < R) and (0 <= X < C)):
                continue

            if graph[Y][X] == 0:
                continue

            if 0 < dist[Y][X]:
                continue

            distance = dist[y][x] + 1
        
            queue.append((Y, X))
            dist[Y][X] = distance

            if maximum_distance < distance:
                maximum_distance = distance
    
    return maximum_distance - 1

R, C = map(int, input().split())

graph = [[0 for _ in range(C)] for _ in range(R)]
start_points = []

for r in range(R):
    row = list(input().rstrip())

    for c in range(C):
        col = row[c]

        if col == 'L':
            graph[r][c] = 1
            start_points.append((r, c))

time = 0

for y, x in start_points:
    t = BFS(y, x)

    if time < t:
        time = t

print(time)