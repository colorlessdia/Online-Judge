import sys
from collections import deque

def BFS():
    queue = deque([(0, 0)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    counts = dict()

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < N) and (0 <= X < M)):
                continue

            if visited[Y][X]:
                continue

            if graph[Y][X] == 0:
                queue.append((Y, X))
                visited[Y][X] = True
                continue

            if (Y, X) not in counts:
                counts[(Y, X)] = 0
            
            counts[(Y, X)] += 1
    
    return counts

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]
cheese = 0

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        col = row[j]
        
        if col == 1:
            graph[i][j] = 1
            cheese += 1

time = 0

while 0 < cheese:
    counts = BFS()

    for (y, x), count in counts.items():

        if 2 <= count:
            graph[y][x] = 0
            cheese -= 1
    
    time += 1

print(time)