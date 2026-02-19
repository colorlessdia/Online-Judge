import sys
from collections import deque

def BFS(sy, sx):
    queue = deque([(sy, sx)])

    dist = [[-1 for _ in range(M)] for _ in range(N)]
    dist[sy][sx] = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x = queue.popleft()

        if (y == y2) and (x == x2):
            return dist[y][x]
        
        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < N) and (0 <= X < M)):
                continue
            
            if dist[Y][X] == -1:

                if graph[Y][X] == '0':
                    dist[Y][X] = dist[y][x]
                    queue.appendleft((Y, X))
                else:
                    dist[Y][X] = dist[y][x] + 1
                    queue.append((Y, X))

input = sys.stdin.readline

N, M = map(int, input().split())
y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())

graph = [list(input().rstrip()) for _ in range(N)]

print(BFS(y1, x1))