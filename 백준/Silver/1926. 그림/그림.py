import sys
from collections import deque

def BFS(graph, start, size):
    queue = deque([start])
    graph[start[0]][start[1]] = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    area = 1

    while 0 < len(queue):
        r, c = queue.popleft()

        for i in range(4):
            y = dy[i] + r
            x = dx[i] + c

            if (x < 0) or (y < 0) or (size[1] <= x) or (size[0] <= y):
                continue
            
            if graph[y][x] == 0:
                continue
            
            queue.append([y, x])
            graph[y][x] = 0
            area += 1

    return area

input = sys.stdin.readline

N, M = map(int, input().split())

painting = [list(map(int, input().split())) for _ in range(N)]
painting_area_list = []

for i in range(N):
    
    for j in range(M):
        cell = painting[i][j]

        if cell == 0:
            continue
        
        painting_area_list.append(BFS(painting, [i, j], [N, M]))

painting_area_count = len(painting_area_list)

print(painting_area_count)

if painting_area_count == 0:
    print(0)
else:
    print(max(painting_area_list))