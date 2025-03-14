import sys
from collections import deque

def BFS(graph, start, size):
    queue = deque([start])

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while 0 < len(queue):
        r, c = queue.popleft()

        graph[r][c] = 0

        for i in range(4):
            x = c + dx[i]
            y = r + dy[i]

            if (x < 0) or (y < 0) or (size[0] <= x) or (size[1] <= y):
                continue

            if graph[y][x] == 0:
                continue
            
            graph[y][x] = 0
            queue.append([y, x])

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())

        graph[Y][X] = 1

    count = 0

    for i in range(N):
        
        for j in range(M):
            cell = graph[i][j]

            if cell == 0:
                continue
            
            BFS(graph, [i, j], [M, N])
            count += 1
    
    print(count)