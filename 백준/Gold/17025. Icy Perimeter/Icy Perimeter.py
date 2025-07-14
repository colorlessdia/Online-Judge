import sys
from collections import deque

def BFS(graph, start, N):
    queue = deque([start])
    graph[start[0]][start[1]] = -1

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    A = 1
    P = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < N) and (0 <= X < N)):
                P += 1
                continue

            if graph[Y][X] == 0:
                P += 1
                continue

            if graph[Y][X] < 0:
                continue

            graph[Y][X] = -1
            queue.append((Y, X))
            A += 1
    
    return A, P

input = sys.stdin.readline

N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    row = list(input().rstrip())

    for j in range(N):
        col = row[j]

        if col == '.':
            graph[i][j] = 0
            continue
        
        graph[i][j] = 1

info_list = []

for i in range(N):

    for j in range(N):

        if graph[i][j] == 1:
            info_list.append(BFS(graph, (i, j), N))

info_list.sort(key=lambda x: (-x[0], x[1]))
print(*info_list[0])