import sys
from collections import deque

def BFS(graph, start, size):
    queue = deque([start])

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    count = 0

    while 0 < len(queue):
        r, c = queue.popleft()
        
        for i in range(4):
            row = r + dy[i]
            col = c + dx[i]

            if (row < 0) or (col < 0) or (size[0] <= row) or (size[1] <= col):
                continue

            cell = graph[row][col]

            if cell == 'X':
                continue
            
            if cell == 'P':
                count += 1
            
            graph[row][col] = 'X'
            queue.append([row, col])

    return count

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
start = []
size = [N, M]

for i in range(N):
    line = list(input().rstrip())
    graph[i] = line
    
    for j in range(M):
        cell = line[j]

        if 'I' in cell:
            start = [i, j]
            graph[i][j] = 'O'

friend = BFS(graph, start, size)

if friend == 0:
    print('TT')
else:
    print(friend)