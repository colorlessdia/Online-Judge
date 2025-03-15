import sys
from collections import deque

def BFS(graph, start, size, color):
    queue = deque([start])

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while 0 < len(queue):
        r, c = queue.popleft()

        graph[r][c] = ''
        
        for i in range(4):
            y = r + dy[i]
            x = c + dx[i]

            if (x < 0) or (y < 0) or (size <= x) or (size <= y):
                continue
            
            if graph[y][x] != color:
                continue

            graph[y][x] = ''
            queue.append([y, x])

input = sys.stdin.readline

N = int(input())

A = [[0 for _ in range(N)] for _ in range(N)]
B = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    line = input().rstrip()

    for j in range(N):
        cell = line[j]

        A[i][j] = cell
        B[i][j] = cell if cell == 'B' else 'G'

A_count = 0
B_count = 0

for k in range(N):
    
    for l in range(N):
        
        if A[k][l] != '':
            BFS(A, [k, l], N, A[k][l])
            A_count += 1

        if B[k][l] != '':
            BFS(B, [k, l], N, B[k][l])
            B_count += 1

print(A_count, B_count)