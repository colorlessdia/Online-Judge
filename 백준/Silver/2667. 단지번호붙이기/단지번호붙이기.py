import sys
from collections import deque

def BFS(graph, r, c):
    queue = deque([(r, c)])
    graph[r][c] = '0'

    size = len(graph)
    apt = 1

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while 0 < len(queue):
        r, c = queue.popleft()

        for i in range(4):
            row = r + dx[i]
            col = c + dy[i]

            if (row < 0) or (size <= row) or (col < 0) or (size <= col):
                continue

            if graph[row][col] == '0':
                continue
            
            apt += 1
            graph[row][col] = '0'
            queue.append((row, col))

    return apt

input = sys.stdin.readline

N = int(input())

graph = [list(input().rstrip()) for _ in range(N)]
apt_complex_list = []

for r in range(N):

    for c in range(N):
        cell = graph[r][c]

        if cell == '0':
            continue
        
        apt_complex_list.append(BFS(graph, r, c))

apt_complex_list.sort()

print(len(apt_complex_list))

for apt_complex in apt_complex_list:
    print(apt_complex)