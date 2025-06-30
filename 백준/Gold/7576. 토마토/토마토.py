import sys
from collections import deque

def BFS(graph, start_point, limit):
    queue = deque()

    while start_point:
        b, a = start_point.popleft()

        queue.append((b, a, 0))

    ly, lx = limit

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        b, a, c = queue.popleft()

        for i in range(4):
            y, x = b + dy[i], a + dx[i]

            if not ((0 <= y < ly) and (0 <= x < lx)):
                continue
            
            if graph[y][x] != 0:
                continue
            
            graph[y][x] = c + 1
            queue.append((y, x, c + 1))

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]
start_point = deque()
unripe_tomato = 0

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        col = row[j]
        graph[i][j] = col

        if col == 1:
            start_point.append([i, j])
        
        if col == 0:
            unripe_tomato += 1

if not unripe_tomato:
    print(0)
else:
    BFS(graph, start_point, (N, M))

    day = 0
    is_valid = True

    for row in graph:
        
        if not is_valid:
            break
        
        for col in row:
            
            if col == 0:
                is_valid = False
                break
            
            if day < col:
                day = col
    
    if is_valid:
        print(day)
    else:
        print(-1)