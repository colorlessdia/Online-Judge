import sys
from collections import deque

def BFS(graph, start_points, H, N, M):
    queue = deque()

    while start_points:
        queue.append((*start_points.popleft(), 0))

    dz = [0, 0, 0, 0, 1, -1]
    dy = [1, 0, -1, 0, 0, 0]
    dx = [0, 1, 0, -1, 0, 0]

    while queue:
        z, y, x, count = queue.popleft()

        for i in range(6):
            Z, Y, X = z + dz[i], y + dy[i], x + dx[i]

            if not ((0 <= Z < H) and (0 <= Y < N) and (0 <= X < M)):
                continue
            
            if graph[Z][Y][X] != 0:
                continue

            graph[Z][Y][X] = count + 1
            queue.append((Z, Y, X, count + 1))

input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
unripe_tomato_count = 0
ripe_tomato_list = deque()

for z in range(H):

    for y in range(N):
        row = list(map(int, input().split()))
    
        for x in range(M):
            col = row[x]

            if col == 0:
                graph[z][y][x] = 0
                unripe_tomato_count += 1
                continue
            
            if col == 1:
                graph[z][y][x] = 1
                ripe_tomato_list.append([z, y, x])
                continue

if not unripe_tomato_count:
    print(0)
else:
    BFS(graph, ripe_tomato_list, H, N, M)

    maximum_day = 0

    for i in range(H):
        
        for j in range(N):
            
            for k in range(M):
                state = graph[i][j][k]

                if state == 0:
                    print(-1)
                    sys.exit()

                if maximum_day < state:
                    maximum_day = state

    print(maximum_day)